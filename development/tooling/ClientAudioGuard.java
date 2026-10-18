package dev.enderloom.probe;

import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Silence only the owned, disposable QA client's master mix, before Minecraft
 * initializes OpenAL. Audio assets and sound callbacks remain fully exercised. */
public final class ClientAudioGuard {
    private static boolean prepared,verified;
    public static void prepare() {
        try {
            Path run=Paths.get("").toAbsolutePath().normalize();
            Path source=run.getParent(),build=source==null?null:source.getParent(),owner=build==null?null:build.getParent();
            if(!"run".equals(run.getFileName().toString())||source==null||!"source".equals(source.getFileName().toString())
                ||build==null||!build.getFileName().toString().matches("[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}")
                ||owner==null||!"conversion-builds".equals(owner.getFileName().toString()))
                throw new IllegalStateException("Audio guard requires an owned disposable conversion-build run");
            for(Path part=run;part!=null;part=part.getParent())if(Files.isSymbolicLink(part))throw new IllegalStateException("Redirected QA audio settings");
            Path options=run.resolve("options.txt");
            if(Files.exists(options,LinkOption.NOFOLLOW_LINKS)&&!Files.isRegularFile(options,LinkOption.NOFOLLOW_LINKS))throw new IllegalStateException("Nonregular QA options");
            List<String> lines=Files.exists(options)?Files.readAllLines(options,StandardCharsets.UTF_8):new ArrayList<String>();
            List<String> muted=new ArrayList<String>();for(String line:lines)if(!line.startsWith("soundCategory_master:"))muted.add(line);
            muted.add("soundCategory_master:0.0");Files.write(options,muted,StandardCharsets.UTF_8);
            int count=0;for(String line:Files.readAllLines(options,StandardCharsets.UTF_8))if(line.startsWith("soundCategory_master:")){if(!line.equals("soundCategory_master:0.0"))throw new IllegalStateException("QA master volume was not muted");count++;}
            if(count!=1)throw new IllegalStateException("Ambiguous QA master volume");prepared=true;
            System.out.println("ENDERLOOM_CLIENT_AUDIO_PRELAUNCH muted=true master=0.0 disposableOnly=true");
        }catch(Exception failure){throw new IllegalStateException("Refusing to start an unmuted QA game",failure);}
    }
    public static void verify(Object minecraft)throws Exception {
        if(verified)return;if(!prepared)throw new IllegalStateException("Missing prelaunch mute guard");
        ClassLoader loader=minecraft.getClass().getClassLoader();Class<?> source=Class.forName("net.minecraft.sounds.SoundSource",false,loader);
        Object options=minecraft.getClass().getField("options").get(minecraft);
        Object master=source.getField("MASTER").get(null);
        float volume=((Number)options.getClass().getMethod("getSoundSourceVolume",source).invoke(options,master)).floatValue();
        if(Float.floatToIntBits(volume)!=Float.floatToIntBits(0f))throw new IllegalStateException("Actual Minecraft QA master volume is not muted: "+volume);
        String record="{\"schema\":1,\"passed\":true,\"prelaunchMuted\":true,\"actualNativeMasterVolume\":0.0,\"disposableSettingsOnly\":true,\"soundCallbacksDisabled\":false}";
        Files.write(Paths.get("enderloom-client-audio-guard.json"),record.getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);
        System.out.println("ENDERLOOM_CLIENT_AUDIO_VERIFIED "+record);verified=true;
    }
    private ClientAudioGuard(){}
}
