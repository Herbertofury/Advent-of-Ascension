package dev.enderloom.probe;

import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.function.Supplier;

/** Actual native portal dispatch/cache/transport in controlled complete frames.
 * Does not certify player UI, natural acquisition or multiplayer. */
public final class NativeRestoredPortalInspection {
    private static ClassLoader loader;
    private static final String PORTAL="net.tslat.aoa3.content.block.functional.portal.PortalBlock",TELE="net.tslat.aoa3.content.world.teleporter.AoATeleporter";
    private static Class<?> c(String name)throws Exception{return Class.forName(name,false,loader);}
    private static Object call(Object target,String owner,String method,Class<?>[] types,Object...args)throws Exception{return c(owner).getMethod(method,types).invoke(target,args);}
    private static Object field(String owner,String name)throws Exception{return c(owner).getField(name).get(null);}
    private static Object privateField(Object target,String owner,String name)throws Exception{Field f=c(owner).getDeclaredField(name);f.setAccessible(true);return f.get(target);}
    private static void check(boolean passed,String reason){if(!passed)throw new IllegalStateException(reason);}
    private static Map<String,Object> row(Object...args){return NativeCompleteHistoricalEquipmentInspection.map(args);}
    private static String key(String name,Object object)throws Exception{return String.valueOf(call(field("net.minecraft.core.registries.BuiltInRegistries",name),"net.minecraft.core.Registry","getKey",new Class<?>[]{Object.class},object));}
    private static Object id(String key)throws Exception{return c("net.minecraft.resources.ResourceLocation").getConstructor(String.class).newInstance(key);}
    private static Object registered(String name,String key)throws Exception{Optional<?> result=(Optional<?>)call(field("net.minecraft.core.registries.BuiltInRegistries",name),"net.minecraft.core.Registry","getOptional",new Class<?>[]{c("net.minecraft.resources.ResourceLocation")},id(key));check(result.isPresent(),"Missing native portal dependency "+key);return result.get();}
    private static Object pos(int x,int y,int z)throws Exception{return c("net.minecraft.core.BlockPos").getConstructor(int.class,int.class,int.class).newInstance(x,y,z);}
    private static Object state(Object block)throws Exception{return call(block,"net.minecraft.world.level.block.Block","defaultBlockState",new Class<?>[0]);}
    private static Object block(Object world,Object pos)throws Exception{return call(world,"net.minecraft.world.level.Level","getBlockState",new Class<?>[]{c("net.minecraft.core.BlockPos")},pos);}
    private static void place(Object world,Object pos,Object state)throws Exception{call(world,"net.minecraft.world.level.Level","setBlock",new Class<?>[]{c("net.minecraft.core.BlockPos"),c("net.minecraft.world.level.block.state.BlockState"),int.class},pos,state,2);}
    private static void move(Object e,int x,int y,int z)throws Exception{call(e,"net.minecraft.world.entity.Entity","moveTo",new Class<?>[]{double.class,double.class,double.class,float.class,float.class},x+.5,y+.5,z+.5,0f,0f);}
    private static void discard(Object e)throws Exception{if(e!=null)call(e,"net.minecraft.world.entity.Entity","discard",new Class<?>[0]);}
    private static void cooldown(Object e,int value)throws Exception{Field f=c("net.minecraft.world.entity.Entity").getDeclaredField("portalCooldown");f.setAccessible(true);f.setInt(e,value);}
    private static Object uuid(Object e)throws Exception{return call(e,"net.minecraft.world.entity.Entity","getUUID",new Class<?>[0]);}
    /** ConfigValue.set on Forge's autosaving file provider writes every temporary
     * choice and schedules asynchronous reloads. Exercise the same public value
     * API against a complete detached provider, then restore the actual provider.
     * Never change watcher registration, mod handlers, or the player's file. */
    private static final class ConfigScope implements AutoCloseable {
        final Object spec,original,detached,value,previous;
        final Path file;
        final byte[] originalBytes;
        final Object originalTree;
        final List<?> path;
        ConfigScope(Object value)throws Exception {
            this.value=value;spec=field("net.tslat.aoa3.common.registration.AoAConfigs","SERVER_CONFIG_SPEC");
            Object tracker=field("net.minecraftforge.fml.config.ConfigTracker","INSTANCE"),selected=null;
            Map<?,?> configs=(Map<?,?>)call(tracker,"net.minecraftforge.fml.config.ConfigTracker","fileMap",new Class<?>[0]);
            for(Object config:configs.values())if(call(config,"net.minecraftforge.fml.config.ModConfig","getSpec",new Class<?>[0])==spec){check(selected==null,"Ambiguous actual server configuration");selected=config;}
            check(selected!=null,"Actual registered AoA server configuration absent");
            original=call(selected,"net.minecraftforge.fml.config.ModConfig","getConfigData",new Class<?>[0]);
            check(original!=null&&privateField(spec,"net.minecraftforge.common.ForgeConfigSpec","childConfig")==original,"Actual loaded provider identity differs");
            file=(Path)call(selected,"net.minecraftforge.fml.config.ModConfig","getFullPath",new Class<?>[0]);originalBytes=Files.readAllBytes(file);originalTree=tree(original);
            previous=call(value,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","get",new Class<?>[0]);
            path=new ArrayList<Object>((List<?>)call(value,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","getPath",new Class<?>[0]));
            detached=copy(original);
            check(tree(detached).equals(originalTree)&&detached!=original,"Complete typed/commented configuration copy differs");
            check((Boolean)call(spec,"net.minecraftforge.common.ForgeConfigSpec","isCorrect",new Class<?>[]{c("com.electronwill.nightconfig.core.CommentedConfig")},detached),"Detached complete config needs corrections");
            call(spec,"net.minecraftforge.common.ForgeConfigSpec","setConfig",new Class<?>[]{c("com.electronwill.nightconfig.core.CommentedConfig")},detached);
            check(privateField(spec,"net.minecraftforge.common.ForgeConfigSpec","childConfig")==detached,"Public scoped provider selection failed");
        }
        private static Object copy(Object input)throws Exception {
            if(c("com.electronwill.nightconfig.core.UnmodifiableConfig").isInstance(input)){
                Object result=call(null,"com.electronwill.nightconfig.core.CommentedConfig","inMemory",new Class<?>[0]);
                Map<?,?> entries=(Map<?,?>)call(input,"com.electronwill.nightconfig.core.UnmodifiableConfig","valueMap",new Class<?>[0]);
                for(Map.Entry<?,?> entry:entries.entrySet())call(result,"com.electronwill.nightconfig.core.Config","set",new Class<?>[]{List.class,Object.class},Collections.singletonList(entry.getKey()),copy(entry.getValue()));
                if(c("com.electronwill.nightconfig.core.UnmodifiableCommentedConfig").isInstance(input)){
                    Map<?,?> comments=(Map<?,?>)call(input,"com.electronwill.nightconfig.core.UnmodifiableCommentedConfig","commentMap",new Class<?>[0]);
                    for(Map.Entry<?,?> entry:comments.entrySet())call(result,"com.electronwill.nightconfig.core.CommentedConfig","setComment",new Class<?>[]{List.class,String.class},Collections.singletonList(entry.getKey()),entry.getValue());
                }
                return result;
            }
            if(input instanceof List){List<Object> result=new ArrayList<>();for(Object v:(List<?>)input)result.add(copy(v));return result;}
            check(input==null||input instanceof String||input instanceof Boolean||input instanceof Byte||input instanceof Short||input instanceof Integer||input instanceof Long||input instanceof Float||input instanceof Double||input instanceof Enum||input instanceof java.time.temporal.TemporalAccessor,"Unknown mutable config value: "+(input==null?"null":input.getClass().getName()));
            return input;
        }
        private static Object tree(Object input)throws Exception {
            if(c("com.electronwill.nightconfig.core.UnmodifiableConfig").isInstance(input)){
                Map<String,Object> values=new TreeMap<>();Map<?,?> entries=(Map<?,?>)call(input,"com.electronwill.nightconfig.core.UnmodifiableConfig","valueMap",new Class<?>[0]);
                for(Map.Entry<?,?> entry:entries.entrySet())values.put((String)entry.getKey(),tree(entry.getValue()));
                Map<String,Object> comments=new TreeMap<>();if(c("com.electronwill.nightconfig.core.UnmodifiableCommentedConfig").isInstance(input))for(Map.Entry<?,?> entry:((Map<?,?>)call(input,"com.electronwill.nightconfig.core.UnmodifiableCommentedConfig","commentMap",new Class<?>[0])).entrySet())comments.put((String)entry.getKey(),entry.getValue());
                return row("values",values,"comments",comments);
            }
            if(input instanceof List){List<Object> result=new ArrayList<>();for(Object v:(List<?>)input)result.add(tree(v));return result;}
            return Arrays.asList(input==null?"null":input.getClass().getName(),input);
        }
        public void close()throws Exception {
            boolean providerUnchanged=privateField(spec,"net.minecraftforge.common.ForgeConfigSpec","childConfig")==detached;
            try{
                // Revert only the permitted choice in the detached data before
                // comparing every value, nested list, numeric type and comment.
                call(detached,"com.electronwill.nightconfig.core.Config","set",new Class<?>[]{List.class,Object.class},path,previous);
                check(tree(detached).equals(originalTree),"Portal test changed an unrelated configuration choice/comment");
                check(tree(original).equals(originalTree),"Original provider changed during scoped portal checks");
                check(Arrays.equals(Files.readAllBytes(file),originalBytes),"Portal fixture persisted a temporary choice");
                check(providerUnchanged,"An asynchronous reload replaced the scoped provider");
            }finally{call(spec,"net.minecraftforge.common.ForgeConfigSpec","setConfig",new Class<?>[]{c("com.electronwill.nightconfig.core.CommentedConfig")},original);}
            check(privateField(spec,"net.minecraftforge.common.ForgeConfigSpec","childConfig")==original&&Objects.equals(call(value,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","get",new Class<?>[0]),previous),"Actual provider/cached choice not restored");
        }
    }
    private static final class Frame implements AutoCloseable {
        final Object world,center;final Map<Object,Object> blocks=new LinkedHashMap<>(),tiles=new LinkedHashMap<>();
        Frame(Object world,Object portal,Object border,int x,int y,int z)throws Exception{
            this.world=world;center=pos(x,y,z);
            for(int cy=-1;cy<=3;cy++)for(int cz=-1;cz<=2;cz++){
                Object at=pos(x,y+cy,z+cz);blocks.put(at,block(world,at));Object tile=call(world,"net.minecraft.world.level.Level","getBlockEntity",new Class<?>[]{c("net.minecraft.core.BlockPos")},at);
                if(tile!=null)tiles.put(at,call(tile,"net.minecraft.world.level.block.entity.BlockEntity","saveWithFullMetadata",new Class<?>[0]));
            }
            for(Object at:blocks.keySet())place(world,at,state(border));
            for(int cy=0;cy<3;cy++)for(int cz=0;cz<2;cz++)place(world,pos(x,y+cy,z+cz),state(portal));
        }
        public void close()throws Exception{
            for(Map.Entry<Object,Object> e:blocks.entrySet())place(world,e.getKey(),e.getValue());
            for(Map.Entry<Object,Object> e:tiles.entrySet()){Object tile=call(world,"net.minecraft.world.level.Level","getBlockEntity",new Class<?>[]{c("net.minecraft.core.BlockPos")},e.getKey());check(tile!=null,"Portal fixture lost an original tile");call(tile,"net.minecraft.world.level.block.entity.BlockEntity","load",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},e.getValue());}
            for(Map.Entry<Object,Object> e:blocks.entrySet())check(block(world,e.getKey()).equals(e.getValue()),"Portal frame restoration lost a block");
        }
    }
    private static Object observed(NativeItemEntityObservation observer,Object expectedUuid,String portal,String direction,Object actor,Object allow)throws Exception{
        for(Object e:observer.mergeVisible(Collections.<Integer,Object>emptyMap()).values())if(uuid(e).equals(expectedUuid)&&observer.accepted(e))return e;
        String diagnostic=NativeCompleteHistoricalEquipmentInspection.json(row("passed",false,"synthetic",false,"portal",portal,"direction",direction,"expectedUuid",String.valueOf(expectedUuid),"actualObservedJoins",observer.actualObservedJoins(),"completeObservedEntities",observer.completeAdmissionDiagnostic(),"actorRemoved",call(actor,"net.minecraft.world.entity.Entity","isRemoved",new Class<?>[0]),"actorCanChangeDimensions",call(actor,"net.minecraft.world.entity.Entity","canChangeDimensions",new Class<?>[0]),"actorOnPortalCooldown",call(actor,"net.minecraft.world.entity.Entity","isOnPortalCooldown",new Class<?>[0]),"actualAllowNonPlayerTravel",call(allow,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","get",new Class<?>[0]),"completeAoAPort",false));
        Files.write(Paths.get("enderloom-forge1201-portal-admission-failure.json"),diagnostic.getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);
        throw new IllegalStateException("Native portal did not admit the matching transported entity: "+portal+" / "+direction+" "+diagnostic);
    }
    private static void sentinel(Object entity,String expected)throws Exception{Object data=call(entity,"net.minecraft.world.entity.Entity","getPersistentData",new Class<?>[0]);check(call(data,"net.minecraft.nbt.CompoundTag","getString",new Class<?>[]{String.class},"EnderloomPortalFixture").equals(expected),"Native portal lost Forge extension data");}
    @SuppressWarnings("unchecked")
    public static String capture(Object server)throws Exception{
        loader=server.getClass().getClassLoader();
        Set<String> required=new TreeSet<String>();for(String name:Arrays.asList("abyss","barathos","candyland","celeve","creeponia","crystevia","deeplands","dustopia","gardencia","greckon","haven","iromine","lborean","lelyetia","lunalus","mysterium","nether","nowhere","precasia","runandor","shyrelands","vox_ponds"))required.add("aoa3:"+name+"_portal");
        try{c("net.tslat.aoa3.content.world.gen.compat.snapshot1710.nativeapi.SnapshotRealmFamily");for(String name:Arrays.asList("ethereus","everland","labricon","playtopia"))required.add("aoa3:"+name+"_portal");}catch(ClassNotFoundException preceding){}
        try{c("net.tslat.aoa3.content.world.gen.compat.dungeons.DungeonRealmFamily");required.add("aoa3:ancient_cavern_portal");required.add("aoa3:immortallis_portal");}catch(ClassNotFoundException preceding){}
        int expected=required.size();Supplier<Set<Object>> supplier=(Supplier<Set<Object>>)privateField(null,PORTAL,"USEABLE_PORTALS");Set<Object> supported=supplier.get();Set<String> actual=new TreeSet<String>();for(Object portal:supported)actual.add(key("BLOCK",portal));check(actual.equals(required),"Complete canonical portal identities differ: expected="+required+" actual="+actual);
        Object source=call(server,"net.minecraft.server.MinecraftServer","overworld",new Class<?>[0]),serverConfig=field("net.tslat.aoa3.common.registration.AoAConfigs","SERVER");
        Object allow=serverConfig.getClass().getField("allowNonPlayerPortalTravel").get(serverConfig),previous=call(allow,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","get",new Class<?>[0]);
        List<Object> rows=new ArrayList<>();int transported=0;int x=197,z=-35;long chunkKey=((long)(x>>4)&0xffffffffL)|(((long)(z>>4)&0xffffffffL)<<32);
        try(ConfigScope configuration=new ConfigScope(allow)){
            for(Object portal:supported){
                String portalKey=key("BLOCK",portal);Object worldKey=privateField(portal,PORTAL,"world");check(worldKey!=null,"Canonical dimension portal lost its world key");
                Object target=call(server,"net.minecraft.server.MinecraftServer","getLevel",new Class<?>[]{c("net.minecraft.resources.ResourceKey")},worldKey);check(target!=null,"Restored portal destination unavailable "+portalKey);
                String dimension=String.valueOf(call(worldKey,"net.minecraft.resources.ResourceKey","location",new Class<?>[0]));
                Object teleporter=dimension.equals("minecraft:the_nether")?c("net.tslat.aoa3.content.world.teleporter.specific.NetherTeleporter").getConstructor().newInstance():call(null,PORTAL,"getTeleporterForWorld",new Class<?>[]{c("net.minecraft.server.level.ServerLevel")},target);
                check(c(TELE).isInstance(teleporter)&&call(teleporter,TELE,"getPortalBlock",new Class<?>[0])==portal,"Native destination selected a substitute portal/teleporter");
                Object border=call(teleporter,TELE,"getBorderBlock",new Class<?>[0]);Map<Long,Object> cache=(Map<Long,Object>)call(teleporter,TELE,"getCachedPortalMap",new Class<?>[0]),priorCache=new LinkedHashMap<>(cache);
                int sy=Math.min(((Number)call(source,"net.minecraft.world.level.Level","getMaxBuildHeight",new Class<?>[0])).intValue(),((Number)call(call(source,"net.minecraft.world.level.Level","dimensionType",new Class<?>[0]),"net.minecraft.world.level.dimension.DimensionType","logicalHeight",new Class<?>[0])).intValue())-8;
                int ty=Math.min(((Number)call(target,"net.minecraft.world.level.Level","getMaxBuildHeight",new Class<?>[0])).intValue(),((Number)call(call(target,"net.minecraft.world.level.Level","dimensionType",new Class<?>[0]),"net.minecraft.world.level.dimension.DimensionType","logicalHeight",new Class<?>[0])).intValue())-8;
                Object pig=call(registered("ENTITY_TYPE","minecraft:pig"),"net.minecraft.world.entity.EntityType","create",new Class<?>[]{c("net.minecraft.world.level.Level")},source);check(pig!=null,"Native portal fixture actor unavailable");String marker="portal-"+portalKey;Object data=call(pig,"net.minecraft.world.entity.Entity","getPersistentData",new Class<?>[0]);call(data,"net.minecraft.nbt.CompoundTag","putString",new Class<?>[]{String.class,String.class},"EnderloomPortalFixture",marker);
                Object identity=uuid(pig);move(pig,x,sy,z);call(pig,"net.minecraft.world.entity.Entity","setNoGravity",new Class<?>[]{boolean.class},true);
                try(Frame from=new Frame(source,portal,border,x,sy,z);Frame to=new Frame(target,portal,border,x,ty,z);NativeItemEntityObservation originEvents=new NativeItemEntityObservation(source,c("net.minecraft.world.entity.Entity"));NativeItemEntityObservation destinationEvents=new NativeItemEntityObservation(target,c("net.minecraft.world.entity.Entity"))){
                    check((Boolean)call(source,"net.minecraft.server.level.ServerLevel","addFreshEntity",new Class<?>[]{c("net.minecraft.world.entity.Entity")},pig),"Actual portal fixture entity admission failed");
                    cache.clear();move(pig,x,ty,z);Object found=call(teleporter,TELE,"findExistingPortal",new Class<?>[]{c("net.minecraft.world.level.Level"),c("net.minecraft.world.entity.Entity")},target,pig);
                    boolean specialized=portal.getClass().getName().endsWith("NowherePortalBlock");
                    if(specialized){
                        // Nowhere's complete native override deliberately returns its
                        // fixed activity lobby. It does not use the generic frame cache.
                        check(found!=null&&found.equals(pos(25,1501,15))&&cache.isEmpty(),"Specialized Nowhere lobby routing changed: "+found+" cache="+cache);
                        move(pig,x,sy,z);call(portal,PORTAL,"entityInside",new Class<?>[]{c("net.minecraft.world.level.block.state.BlockState"),c("net.minecraft.world.level.Level"),c("net.minecraft.core.BlockPos"),c("net.minecraft.world.entity.Entity")},state(portal),source,from.center,pig);
                        check(!(Boolean)call(pig,"net.minecraft.world.entity.Entity","isRemoved",new Class<?>[0]),"Specialized player-only Nowhere interaction was bypassed");
                        rows.add(row("portal",portalKey,"destination",dimension,"nativeTeleporter",teleporter.getClass().getName(),"nativeFixedLobbyRoutingVerified",true,"genericPortalCacheNotUsed",true,"specializedPlayerOnlyEntryPreserved",true,"playerTravelVerified",false));
                    }else{
                        boolean dungeon=dimension.equals("aoa3:ancient_cavern")||dimension.equals("aoa3:immortallis");
                        if(dungeon)check(pos(0,dimension.equals("aoa3:immortallis")?20:18,0).equals(found)&&cache.isEmpty(),"Complete dungeon fixed lobby routing changed: "+portalKey+" found="+found+" cache="+cache);
                        else{check(found!=null&&cache.size()==1&&cache.containsKey(chunkKey)&&cache.get(chunkKey).equals(to.center),"Native portal discovery cached the wrong requested chunk/position: "+portalKey+" found="+found+" expected="+to.center+" key="+chunkKey+" cache="+cache);check(!c("net.minecraft.core.BlockPos$MutableBlockPos").isInstance(cache.get(chunkKey)),"Native portal cached a mutable traversal cursor: "+portalKey);}
                        Class<?>[] types={c("net.minecraft.world.level.block.state.BlockState"),c("net.minecraft.world.level.Level"),c("net.minecraft.core.BlockPos"),c("net.minecraft.world.entity.Entity")};
                        move(pig,x,sy,z);call(allow,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","set",new Class<?>[]{Object.class},Boolean.FALSE);call(portal,PORTAL,"entityInside",types,state(portal),source,from.center,pig);check(!(Boolean)call(pig,"net.minecraft.world.entity.Entity","isRemoved",new Class<?>[0]),"Disabled non-player travel choice was ignored");
                        call(allow,"net.minecraftforge.common.ForgeConfigSpec$ConfigValue","set",new Class<?>[]{Object.class},Boolean.TRUE);cooldown(pig,5);call(portal,PORTAL,"entityInside",types,state(portal),source,from.center,pig);check(!(Boolean)call(pig,"net.minecraft.world.entity.Entity","isRemoved",new Class<?>[0]),"Native portal cooldown was ignored");cooldown(pig,0);
                        cache.put(chunkKey,to.center);call(portal,PORTAL,"entityInside",types,state(portal),source,from.center,pig);Object arrived=observed(destinationEvents,identity,portalKey,"outbound",pig,allow);sentinel(arrived,marker);
                        check(call(arrived,"net.minecraft.world.entity.Entity","level",new Class<?>[0])==target,"Native portal entered the wrong destination");
                        cache.put(chunkKey,from.center);cooldown(arrived,0);move(arrived,x,ty,z);call(portal,PORTAL,"entityInside",types,state(portal),target,to.center,arrived);Object returned=observed(originEvents,identity,portalKey,"return",arrived,allow);sentinel(returned,marker);
                        check(call(returned,"net.minecraft.world.entity.Entity","level",new Class<?>[0])==source,"Native portal did not return to Overworld");discard(returned);transported++;
                        rows.add(row("portal",portalKey,"destination",dimension,"nativeTeleporter",teleporter.getClass().getName(),"nativeCacheKeyVerified",!dungeon,"immutableCachedPosition",!dungeon,"nativeFixedLobbyRoutingVerified",dungeon,"disabledNonPlayerChoicePreserved",true,"cooldownChoicePreserved",true,"actualNativeEntityRoundTrip",true,"uuidAndForgeNbtRetained",true,"naturalAcquisitionVerified",false,"playerTravelVerified",false));
                    }
                }finally{
                    discard(pig);
                    for(Object level:Arrays.asList(source,target)){Object remaining=call(level,"net.minecraft.server.level.ServerLevel","getEntity",new Class<?>[]{UUID.class},identity);discard(remaining);}
                    cache.clear();cache.putAll(priorCache);
                }
            }
        }
        check(rows.size()==expected&&transported==expected-1,"Complete native canonical portal cohort missing");
        String json=NativeCompleteHistoricalEquipmentInspection.json(row("adapter","complete-native-restored-portals-1","passed",true,"synthetic",false,"controlledPrebuiltFrames",true,"canonicalPortals",rows,"actualNativeEntityRoundTrips",transported,"nativePortalConfigurationRestored",true,"completeTypedCommentedConfigUnchanged",true,"configFileBytesUnchanged",true,"realProviderIdentityRestored",true,"publicScopedConfigProvider",true,"playerTravelVerified",false,"naturalAcquisitionVerified",false,"multiplayerVerified",false,"completeAoAPort",false));
        Files.write(Paths.get("enderloom-forge1201-restored-portals.json"),json.getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);System.out.println("ENDERLOOM_FORGE1201_RESTORED_PORTALS "+json);return json;
    }
    private NativeRestoredPortalInspection(){}
}
