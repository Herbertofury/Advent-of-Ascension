import com.sun.source.tree.ClassTree;
import com.sun.source.tree.CompilationUnitTree;
import com.sun.source.tree.Tree;
import com.sun.source.util.JavacTask;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import javax.tools.*;

/** Parse every selected complete compilation unit with the target JDK itself. */
public final class CompleteSourceOwners {
    public static void main(String[] args) throws Exception {
        List<String> paths=Files.readAllLines(Paths.get(args[0]),StandardCharsets.UTF_8);
        JavaCompiler compiler=ToolProvider.getSystemJavaCompiler();
        if(compiler==null)throw new IllegalStateException("A complete target JDK is required");
        DiagnosticCollector<JavaFileObject> diagnostics=new DiagnosticCollector<>();
        try(StandardJavaFileManager files=compiler.getStandardFileManager(diagnostics,Locale.ROOT,StandardCharsets.UTF_8)) {
            JavacTask task=(JavacTask)compiler.getTask(null,files,diagnostics,Arrays.asList("-proc:none","-encoding","UTF-8"),null,files.getJavaFileObjectsFromStrings(paths));
            List<String> owners=new ArrayList<>();int units=0;
            for(CompilationUnitTree unit:task.parse()) {
                units++;
                String prefix=unit.getPackageName()==null?"":unit.getPackageName().toString()+".";
                String file=Paths.get(unit.getSourceFile().toUri()).toAbsolutePath().toString();
                for(Tree declaration:unit.getTypeDecls())if(declaration instanceof ClassTree) {
                    String name=((ClassTree)declaration).getSimpleName().toString();
                    if(!name.isEmpty())owners.add(prefix+name+"\t"+file);
                }
            }
            for(Diagnostic<?> diagnostic:diagnostics.getDiagnostics())if(diagnostic.getKind()==Diagnostic.Kind.ERROR)
                throw new IllegalStateException("Complete source parsing failed: "+diagnostic);
            if(units!=paths.size())throw new IllegalStateException("Incomplete compilation-unit census");
            Collections.sort(owners);
            Files.write(Paths.get(args[1]),owners,StandardCharsets.UTF_8,StandardOpenOption.CREATE_NEW);
            System.out.println("completeUnits="+units+" topLevelOwners="+owners.size());
        }
    }
}
