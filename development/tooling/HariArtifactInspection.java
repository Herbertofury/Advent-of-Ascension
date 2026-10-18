package dev.enderloom.probe;

import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;

/** Byte inspection against the selected renderer's real contract. No mod/game classes are executed. */
public final class HariArtifactInspection {
    private static Method refs, inspect;
    private static Map<?, ?> contracts;
    private static int classes, archives;
    private static final Set<String> unsupported = new TreeSet<>();

    private static void emit(String kind, String value) {
        System.out.println(kind + "=" + Base64.getEncoder().encodeToString(value.getBytes(StandardCharsets.UTF_8)));
    }

    private static void scan(InputStream input, String label, int depth) throws Exception {
        if (depth > 16) throw new IOException("Nested archive inspection limit: " + label);
        archives++;
        Set<String> members = new HashSet<>();
        try (ZipInputStream zip = new ZipInputStream(input)) {
            ZipEntry entry;
            while ((entry = zip.getNextEntry()) != null) {
                if (!members.add(entry.getName())) throw new IOException("Duplicate archive member: " + label + "!" + entry.getName());
                if (entry.isDirectory()) continue;
                String source = label + "!" + entry.getName();
                byte[] bytes = zip.readAllBytes(); // Complete member read also checks the ZIP CRC.
                if (entry.getName().endsWith(".class")) {
                    if (bytes.length < 10 || new DataInputStream(new ByteArrayInputStream(bytes)).readInt() != 0xcafebabe)
                        throw new IOException("Invalid class file: " + source);
                    classes++;
                    List<?> calls = (List<?>)refs.invoke(null, new ByteArrayInputStream(bytes));
                    for (Object call : calls) {
                        Class<?> type = call.getClass();
                        List<String> fields = new ArrayList<>();
                        for (String name : List.of("owner", "name", "descriptor")) {
                            Method getter = type.getDeclaredMethod(name); getter.setAccessible(true);
                            fields.add((String)getter.invoke(call));
                        }
                        emit("REF", String.join("\t", fields) + "\t" + source);
                    }
                    inspect.invoke(null, new ByteArrayInputStream(bytes), entry.getName(), contracts, unsupported, source);
                } else if (entry.getName().endsWith(".jar")) {
                    scan(new ByteArrayInputStream(bytes), source, depth + 1);
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Class<?> gate = Class.forName("net.vulkanmod.compat.UniversalRendererGate");
        Method load = gate.getDeclaredMethod("loadContracts"); load.setAccessible(true);
        contracts = (Map<?, ?>)load.invoke(null);
        if (contracts.isEmpty()) throw new IOException("Selected renderer has no native translation contract");
        refs = gate.getDeclaredMethod("openGlMethodRefs", InputStream.class); refs.setAccessible(true);
        inspect = gate.getDeclaredMethod("collectClassUnsupported", InputStream.class, String.class, Map.class, Set.class, String.class);
        inspect.setAccessible(true);
        for (String arg : args) scan(Files.newInputStream(Path.of(arg)), Path.of(arg).getFileName().toString(), 0);
        for (String value : unsupported) emit("UNSUPPORTED", value);
        System.out.println("CLASSES=" + classes);
        System.out.println("ARCHIVES=" + archives);
        System.out.println("CONTRACT_OWNERS=" + contracts.size());
    }
}
