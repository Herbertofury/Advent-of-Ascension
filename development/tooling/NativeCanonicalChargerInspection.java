package dev.enderloom.probe;

import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Real target factories and callbacks in every loaded level; no natural-spawn claim. */
public final class NativeCanonicalChargerInspection {
    private static ClassLoader loader;
    private static Class<?> c(String name) throws Exception { return Class.forName(name, false, loader); }
    private static Object call(Object owner, String type, String name, Class<?>[] types, Object... args) throws Exception {
        return c(type).getMethod(name, types).invoke(owner, args);
    }
    private static Object tag(String snbt) throws Exception {
        return call(null, "net.minecraft.nbt.TagParser", "parseTag", new Class<?>[]{String.class}, snbt);
    }
    private static Object copy(Object tag) throws Exception {
        return call(tag, "net.minecraft.nbt.CompoundTag", "copy", new Class<?>[0]);
    }
    private static String string(Object tag, String key) throws Exception {
        return (String)call(tag, "net.minecraft.nbt.CompoundTag", "getString", new Class<?>[]{String.class}, key);
    }
    private static void put(Object tag, String key, String value) throws Exception {
        call(tag, "net.minecraft.nbt.CompoundTag", "putString", new Class<?>[]{String.class, String.class}, key, value);
    }
    private static Map<String,Object> map(Object... args) {
        Map<String,Object> result = new LinkedHashMap<String,Object>();
        for (int i=0; i<args.length; i+=2) result.put((String)args[i], args[i+1]);
        return result;
    }
    private static void check(boolean value, String reason) {
        if (!value) throw new IllegalStateException(reason);
    }
    private static Object load(Object input, Object level) throws Exception {
        Optional<?> result = (Optional<?>)call(null, "net.minecraft.world.entity.EntityType", "create",
            new Class<?>[]{c("net.minecraft.nbt.CompoundTag"), c("net.minecraft.world.level.Level")}, input, level);
        check(result.isPresent(), "Historical Charger native factory returned empty");
        Object entity = result.get();
        check(entity.getClass().getName().equals("net.tslat.aoa3.content.entity.mob.overworld.ChargerEntity"), "Duplicate or placeholder Charger owner");
        return entity;
    }
    private static String variant(Object entity) throws Exception {
        // Resolve on the actual Forge-transformed owner admitted by load().
        // The raw SDK has not applied SmartBrainLib's Brain access transformer.
        Object value = call(entity, entity.getClass().getName(), "getVariant", new Class<?>[0]);
        return (String)value.getClass().getField("name").get(value);
    }
    private static Object save(Object entity) throws Exception {
        Object saved = tag("{}");
        check(Boolean.TRUE.equals(call(entity, "net.minecraft.world.entity.Entity", "save",
            new Class<?>[]{c("net.minecraft.nbt.CompoundTag")}, saved)), "Canonical Charger did not save");
        return saved;
    }

    public static String capture(Object server) throws Exception {
        loader = server.getClass().getClassLoader();
        Class<?> anchor = c("net.tslat.aoa3.advent.AdventOfAscension");
        InputStream manifest = anchor.getResourceAsStream("/data/aoa3/compat/historical_charger_variant_manifest.json");
        if (manifest == null) return "null";
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        try (InputStream input = manifest) {
            byte[] buffer = new byte[8192]; int count;
            while ((count=input.read(buffer))!=-1) bytes.write(buffer,0,count);
        }
        Object gson = c("com.google.gson.Gson").getConstructor().newInstance();
        Map<?,?> plan = (Map<?,?>)call(gson,"com.google.gson.Gson","fromJson",new Class<?>[]{String.class,Class.class},
            new String(bytes.toByteArray(),StandardCharsets.UTF_8),Map.class);
        List<?> declared = (List<?>)plan.get("completeCases");
        check(declared.size()==6, "Incomplete original Charger family");
        List<Object> controls = new ArrayList<Object>();
        for (String[] fixture : new String[][]{
            {"foreign entity", "entity", "{id:\"other:desert_charger\",Extra:3s}"},
            {"canonical entity", "entity", "{id:\"aoa3:charger\",ChargerType:\"void\"}"},
            {"unknown entity", "entity", "{id:\"aoa3:unknown_charger\"}"},
            {"foreign egg", "stack", "{id:\"other:desert_charger_spawn_egg\",Count:3b}"},
            {"canonical egg", "stack", "{id:\"aoa3:charger_spawn_egg\",Count:3b}"},
            {"malformed outer tag", "stack", "{id:\"aoa3:desert_charger_spawn_egg\",tag:3s}"},
            {"malformed entity tag", "stack", "{id:\"aoa3:desert_charger_spawn_egg\",tag:{EntityTag:3s}}"}
        }) {
            Object input = tag(fixture[2]), before = copy(input);
            Object result = c("net.tslat.aoa3.content.entity.compat.HistoricalChargerVariantData").getMethod(fixture[1],c("net.minecraft.nbt.CompoundTag")).invoke(null,input);
            check(result==input && input.equals(before),"Foreign, current or malformed data was rewritten: "+fixture[0]);
            controls.add(map("label",fixture[0],"generatedControl",true,"sameObjectAndAllBytesRetained",true));
        }
        List<Object> entities = new ArrayList<Object>(), eggs = new ArrayList<Object>(), attacks = new ArrayList<Object>(), worlds = new ArrayList<Object>();
        Method water = c("net.tslat.aoa3.content.entity.mob.overworld.ChargerEntity").getDeclaredMethod("getWaterSlowDown");
        water.setAccessible(true);
        for (Object level : (Iterable<?>)call(server,"net.minecraft.server.MinecraftServer","getAllLevels",new Class<?>[0])) {
            Object dimension = call(level,"net.minecraft.world.level.Level","dimension",new Class<?>[0]);
            String world = call(dimension,"net.minecraft.resources.ResourceKey","location",new Class<?>[0]).toString();
            worlds.add(world);
            Object current = load(tag("{id:\"aoa3:charger\",NoAI:1b}"),level);
            float defaultWater = ((Number)water.invoke(current)).floatValue();
            for (Object declaration : declared) {
                Map<?,?> row = (Map<?,?>)declaration;
                String variant = (String)row.get("variant"), old = (String)row.get("legacyEntity");
                Object input = tag("{id:\""+old+"\",NoAI:1b,PersistenceRequired:1b,Health:7.0f,CustomName:'{\"text\":\"Saved Charger\"}',Tags:[\"retained\"]}");
                Object before = copy(input), entity = load(input,level), saved = save(entity);
                check(input.equals(before), "Native entity bridge mutated source NBT");
                check(variant(entity).equals(variant) && string(saved,"id").equals("aoa3:charger") && string(saved,"ChargerType").equals(variant), "Saved variant identity lost");
                for (String key : new String[]{"NoAI","PersistenceRequired","Health","CustomName","Tags"})
                    check(call(before,"net.minecraft.nbt.CompoundTag","get",new Class<?>[]{String.class},key).equals(call(saved,"net.minecraft.nbt.CompoundTag","get",new Class<?>[]{String.class},key)), "Original entity field changed: "+key);
                Object reloaded = load(saved,level);
                check(variant(reloaded).equals(variant), "Canonical save/reload lost legacy variant");
                Object explicit = copy(input); put(explicit,"ChargerType","snow");
                check(variant(load(explicit,level)).equals("snow"), "Explicit modern variant was overwritten");
                float waterValue = ((Number)water.invoke(entity)).floatValue();
                check(Float.floatToIntBits(waterValue)==Float.floatToIntBits(Boolean.TRUE.equals(row.get("oldFullWaterSpeed"))?1f:defaultWater), "Original aquatic callback or canonical land movement changed");
                entities.add(map("world",world,"legacy",old,"variant",variant,"canonicalClass",entity.getClass().getName(),"completeInput",before.toString(),"completeSaved",saved.toString(),"originalInputUnchanged",true,"canonicalReloadPreserved",true,"explicitVariantPreserved",true,"waterSlowDown",waterValue,"generatedSavedDataFixture",true));

                Object stackInput = tag("{id:\""+row.get("legacyEgg")+"\",Count:17b,tag:{testShort:3s,testBytes:[B;1b,2b],EntityTag:{NoAI:1b,CustomName:'{\"text\":\"Egg Charger\"}'}}}");
                Object stackBefore = copy(stackInput);
                Object stack = call(null,"net.minecraft.world.item.ItemStack","of",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},stackInput);
                Object stackSaved = call(stack,"net.minecraft.world.item.ItemStack","save",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},tag("{}"));
                Object expectedTag = tag("{testShort:3s,testBytes:[B;1b,2b],EntityTag:{id:\"aoa3:charger\",ChargerType:\""+variant+"\",NoAI:1b,CustomName:'{\"text\":\"Egg Charger\"}'}}");
                check(stackInput.equals(stackBefore) && string(stackSaved,"id").equals("aoa3:charger_spawn_egg"), "Legacy egg did not load canonically or source NBT changed");
                check(((Number)call(stack,"net.minecraft.world.item.ItemStack","getCount",new Class<?>[0])).intValue()==17, "Egg quantity changed");
                check(expectedTag.equals(call(stack,"net.minecraft.world.item.ItemStack","getTag",new Class<?>[0])), "Full custom egg NBT changed");
                Object entityTag = call(expectedTag,"net.minecraft.nbt.CompoundTag","getCompound",new Class<?>[]{String.class},"EntityTag");
                check(variant(load(entityTag,level)).equals(variant), "Native migrated egg entity lost variant");
                eggs.add(map("world",world,"legacy",row.get("legacyEgg"),"variant",variant,"completeInput",stackBefore.toString(),"completeSaved",stackSaved.toString(),"quantity",17,"originalInputUnchanged",true,"fullCustomTagPreserved",true,"actualNativeEggEntityLoad",true,"generatedSavedDataFixture",true));

                Object golemType = c("net.minecraft.world.entity.EntityType").getField("IRON_GOLEM").get(null);
                Object target = call(golemType,"net.minecraft.world.entity.EntityType","create",new Class<?>[]{c("net.minecraft.world.level.Level")},level);
                check(target!=null,"Native attack target absent");
                check(Boolean.TRUE.equals(call(entity,"net.minecraft.world.entity.Mob","doHurtTarget",new Class<?>[]{c("net.minecraft.world.entity.Entity")},target)),"Actual native Charger attack did not hit");
                List<Object> observed = new ArrayList<Object>();
                String expectedEffect = variant.equals("desert")?"WEAKNESS":variant.equals("swamp")?"MOVEMENT_SLOWDOWN":variant.equals("void")?"BLINDNESS":null;
                for (String effectName : new String[]{"WEAKNESS","MOVEMENT_SLOWDOWN","BLINDNESS"}) {
                    Object effect = c("net.minecraft.world.effect.MobEffects").getField(effectName).get(null);
                    Object instance = call(target,"net.minecraft.world.entity.LivingEntity","getEffect",new Class<?>[]{c("net.minecraft.world.effect.MobEffect")},effect);
                    check((instance!=null)==effectName.equals(expectedEffect), "Original Charger effect domain changed");
                    if (instance!=null) {
                        int duration=((Number)call(instance,"net.minecraft.world.effect.MobEffectInstance","getDuration",new Class<?>[0])).intValue();
                        int amplifier=((Number)call(instance,"net.minecraft.world.effect.MobEffectInstance","getAmplifier",new Class<?>[0])).intValue();
                        check(duration==(variant.equals("swamp")?40:150) && amplifier==0,"Original effect duration/amplifier changed");
                        observed.add(map("effect",effectName,"duration",duration,"amplifier",amplifier));
                    }
                }
                attacks.add(map("world",world,"variant",variant,"actualSuccessfulNativeAttack",true,"effects",observed,"detachedActorsNeverAddedToWorld",true));
            }
        }
        // Preserve the exact prior level domain, including Precasia backup.
        // Add every reviewed restored realm; a minimum/count-only check could
        // silently lose one old world when another new world appears.
        Set<Object> expectedWorlds=new HashSet<Object>(Arrays.<Object>asList("minecraft:overworld","minecraft:the_nether","minecraft:the_end","aoa3:abyss","aoa3:barathos","aoa3:candyland","aoa3:celeve","aoa3:creeponia","aoa3:crystevia","aoa3:deeplands","aoa3:dustopia","aoa3:gardencia","aoa3:greckon","aoa3:haven","aoa3:iromine","aoa3:lborean","aoa3:lelyetia","aoa3:lunalus","aoa3:mysterium","aoa3:nowhere","aoa3:precasia","aoa3:precasia_backup","aoa3:runandor","aoa3:shyrelands","aoa3:vox_ponds"));
        try{c("net.tslat.aoa3.content.world.gen.compat.snapshot1710.nativeapi.SnapshotRealmFamily");expectedWorlds.addAll(Arrays.<Object>asList("aoa3:ethereus","aoa3:everland","aoa3:playtopia","aoa3:labricon"));}catch(ClassNotFoundException preceding){}
        try{c("net.tslat.aoa3.content.world.gen.compat.dungeons.DungeonRealmFamily");expectedWorlds.addAll(Arrays.<Object>asList("aoa3:ancient_cavern","aoa3:immortallis"));}catch(ClassNotFoundException preceding){}
        int expectedCases=expectedWorlds.size()*declared.size();
        check(worlds.size()==expectedWorlds.size() && new HashSet<Object>(worlds).equals(expectedWorlds) && entities.size()==expectedCases && eggs.size()==expectedCases && attacks.size()==expectedCases, "Incomplete full level/Charger contexts");
        String result=(String)call(gson,"com.google.gson.Gson","toJson",new Class<?>[]{Object.class},map("schema",1,"passed",true,"synthetic",false,"savedDataInputsAreGeneratedFixtures",true,"worlds",worlds,"entities",entities,"eggs",eggs,"attacks",attacks,"controls",controls,"completeActualCases",expectedCases*3,"duplicateEntitiesAdded",0,"duplicateEggsAdded",0,"naturalSpawningVerified",false,"legacyCommandsVerified",false,"completeAoAPort",false));
        Files.write(Paths.get("enderloom-forge1201-canonical-charger-variants.json"),result.getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);
        System.out.println("ENDERLOOM_FORGE1201_CANONICAL_CHARGER_VARIANTS "+result);
        return result;
    }
}
