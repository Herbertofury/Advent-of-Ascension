package dev.enderloom.probe;

import java.io.*;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.zip.*;

/** Every authored cell is compared after the native FULL chunk lifecycle.
 * Progression uses an explicitly generated Forge FakePlayer fixture; it does
 * not certify player survival or connected-client rendering/gameplay. */
public final class NativeCompleteDungeonRealmInspection {
    private static ClassLoader loader;
    private static final String FAMILY="net.tslat.aoa3.content.world.gen.compat.dungeons.";
    private static Class<?> c(String n)throws Exception{return Class.forName(n,false,loader);}
    private static Object call(Object o,String owner,String n,Class<?>[] types,Object...args)throws Exception{return c(owner).getMethod(n,types).invoke(o,args);}
    private static Object field(String owner,String n)throws Exception{return c(owner).getField(n).get(null);}
    private static Object hidden(Object o,String n)throws Exception{Field f=o.getClass().getDeclaredField(n);f.setAccessible(true);return f.get(o);}
    private static void check(boolean yes,String why){if(!yes)throw new IllegalStateException(why);}
    private static Map<String,Object> row(Object...args){return NativeCompleteHistoricalEquipmentInspection.map(args);}
    private static Object pos(int x,int y,int z)throws Exception{return c("net.minecraft.core.BlockPos").getConstructor(int.class,int.class,int.class).newInstance(x,y,z);}
    private static int number(Object o,String n)throws Exception{return ((Number)o.getClass().getMethod(n).invoke(o)).intValue();}
    private static Object registry(String owner)throws Exception{return field("net.minecraft.core.registries.BuiltInRegistries",owner);}
    private static Object registered(String owner,String name)throws Exception{
        Object id=c("net.minecraft.resources.ResourceLocation").getConstructor(String.class).newInstance(name);
        Optional<?> result=(Optional<?>)call(registry(owner),"net.minecraft.core.Registry","getOptional",new Class<?>[]{c("net.minecraft.resources.ResourceLocation")},id);check(result.isPresent(),"Missing exact native dungeon dependency "+name);return result.get();
    }
    private static Object actor(Object world,String name)throws Exception{return call(registered("ENTITY_TYPE","aoa3:"+name),"net.minecraft.world.entity.EntityType","create",new Class<?>[]{c("net.minecraft.world.level.Level")},world);}
    private static List<Object> realmshifterBuybacks(Object world)throws Exception {
        try{c("net.tslat.aoa3.content.entity.mob.historical.restored.RealmstoneBuybacks");}
        catch(ClassNotFoundException notInEarlierCandidate){return Collections.emptyList();}
        String[] stones={"abyss","ancient_cavern","barathos","lborean","celeve","crystevia","deeplands","dustopia","gardencia","haven","iromine","lelyetia","mysterium","precasia","vox_ponds","candyland","creeponia","immortallis","shyrelands"};
        int[] amounts={6,9,8,7,4,6,9,6,2,1,4,3,1,2,4,5,6,6,9};
        Class<?> stack=c("net.minecraft.world.item.ItemStack"),itemLike=c("net.minecraft.world.level.ItemLike"),offerType=c("net.minecraft.world.item.trading.MerchantOffer"),nbt=c("net.minecraft.nbt.CompoundTag");
        Object trader=actor(world,"realmshifter");
        @SuppressWarnings("unchecked") List<Object> offers=(List<Object>)call(trader,"net.minecraft.world.entity.npc.AbstractVillager","getOffers",new Class<?>[0]);
        List<Object> cases=new ArrayList<Object>();
        for(int i=0;i<stones.length;i++) {
            Object stone=registered("ITEM","aoa3:"+stones[i]+"_realmstone"),coin=registered("ITEM","aoa3:"+(i==6||i==10?"copper_coin":"silver_coin"));
            List<Object> matching=new ArrayList<Object>();
            for(Object offer:offers) {
                Object buy=call(offer,"net.minecraft.world.item.trading.MerchantOffer","getBaseCostA",new Class<?>[0]),sell=call(offer,"net.minecraft.world.item.trading.MerchantOffer","getResult",new Class<?>[0]),second=call(offer,"net.minecraft.world.item.trading.MerchantOffer","getCostB",new Class<?>[0]);
                if(call(buy,"net.minecraft.world.item.ItemStack","getItem",new Class<?>[0])==stone&&call(sell,"net.minecraft.world.item.ItemStack","getItem",new Class<?>[0])==coin&&(Boolean)call(second,"net.minecraft.world.item.ItemStack","isEmpty",new Class<?>[0]))matching.add(offer);
            }
            check(matching.size()==1,"Missing or duplicated whole original buyback: "+stones[i]);
            Object offer=matching.get(0),buy=call(offer,"net.minecraft.world.item.trading.MerchantOffer","getBaseCostA",new Class<?>[0]),sell=call(offer,"net.minecraft.world.item.trading.MerchantOffer","getResult",new Class<?>[0]);
            check(number(buy,"getCount")==1&&number(sell,"getCount")==amounts[i],"Original buyback direction/quantity differs: "+stones[i]);
            Object payment=stack.getConstructor(itemLike,int.class).newInstance(stone,1),empty=field("net.minecraft.world.item.ItemStack","EMPTY"),wrong=stack.getConstructor(itemLike,int.class).newInstance(registered("ITEM","minecraft:dirt"),1);
            check(!(Boolean)call(offer,"net.minecraft.world.item.trading.MerchantOffer","take",new Class<?>[]{stack,stack},wrong,empty)&&number(wrong,"getCount")==1,"Wrong buyback payment consumed");
            check((Boolean)call(offer,"net.minecraft.world.item.trading.MerchantOffer","take",new Class<?>[]{stack,stack},payment,empty)&&(Boolean)call(payment,"net.minecraft.world.item.ItemStack","isEmpty",new Class<?>[0]),"Native buyback failed to consume exactly one stone");
            Object portalHolder=call(stone,"net.tslat.aoa3.content.item.misc.Realmstone","getPortalBlock",new Class<?>[0]);
            check(portalHolder.getClass().getMethod("get").invoke(portalHolder)==registered("BLOCK","aoa3:"+stones[i]+"_portal"),"Historical buyback uses the wrong destination stone");
            cases.add(row("stone","aoa3:"+stones[i]+"_realmstone","currency",i==6||i==10?"aoa3:copper_coin":"aoa3:silver_coin","amount",amounts[i],"nativePaymentConsumed",true,"wrongPaymentPreserved",true,"exactNativePortal",true));
        }
        // Exercise real saved-offer migration rather than rebuilding a pristine
        // merchant and declaring its defaults to be save compatibility.
        Object changed=offers.get(offers.size()-1);
        call(changed,"net.minecraft.world.item.trading.MerchantOffer","increaseUses",new Class<?>[0]);
        call(changed,"net.minecraft.world.item.trading.MerchantOffer","addToSpecialPriceDiff",new Class<?>[]{int.class},2);
        Object changedResult=call(changed,"net.minecraft.world.item.trading.MerchantOffer","getResult",new Class<?>[0]);
        int editedAmount=number(changedResult,"getCount")+1;
        call(changedResult,"net.minecraft.world.item.ItemStack","setCount",new Class<?>[]{int.class},editedAmount);
        Object custom=offerType.getConstructor(stack,stack,int.class,int.class,float.class).newInstance(stack.getConstructor(itemLike,int.class).newInstance(registered("ITEM","minecraft:diamond"),2),stack.getConstructor(itemLike,int.class).newInstance(registered("ITEM","minecraft:emerald"),3),17,4,0.03f);
        offers.add(custom);
        Object before=call(offers,"net.minecraft.world.item.trading.MerchantOffers","createTag",new Class<?>[0]);
        Object tag=call(trader,"net.minecraft.world.entity.Entity","saveWithoutId",new Class<?>[]{nbt},nbt.getConstructor().newInstance()),restored=actor(world,"realmshifter");
        call(restored,"net.minecraft.world.entity.Entity","load",new Class<?>[]{nbt},tag);
        Object reloaded=call(restored,"net.minecraft.world.entity.npc.AbstractVillager","getOffers",new Class<?>[0]);
        Object after=call(reloaded,"net.minecraft.world.item.trading.MerchantOffers","createTag",new Class<?>[0]);
        check(before.equals(after),"Saved Realmshifter uses/prices/custom payout or offers were rebuilt");
        check(call(restored,"net.minecraft.world.entity.npc.AbstractVillager","getOffers",new Class<?>[0])==reloaded,"Repeated complete-offer access replaced native list");
        cases.add(row("case","native-save-reload-and-repeated-access","completeOffers",((List<?>)reloaded).size(),"completeNbtUnchanged",true,"modifiedPayout",editedAmount,"preservedOfferNbt",after.toString()));
        return cases;
    }
    private static Map<String,Object> artifact(Path p)throws Exception{
        MessageDigest digest=MessageDigest.getInstance("SHA-256");try(InputStream in=Files.newInputStream(p)){byte[] b=new byte[65536];int n;while((n=in.read(b))!=-1)digest.update(b,0,n);}StringBuilder hash=new StringBuilder();for(byte b:digest.digest())hash.append(String.format("%02x",b&255));return row("path",p.toAbsolutePath().toString(),"sha256",hash.toString(),"bytes",Files.size(p));
    }
    private static List<Object> actors(Object world)throws Exception{
        List<Object> rows=new ArrayList<Object>();for(Object actor:(Iterable<?>)call(world,"net.minecraft.server.level.ServerLevel","getAllEntities",new Class<?>[0])){
            Object type=call(actor,"net.minecraft.world.entity.Entity","getType",new Class<?>[0]);Object id=call(registry("ENTITY_TYPE"),"net.minecraft.core.Registry","getKey",new Class<?>[]{Object.class},type);
            if(String.valueOf(id).startsWith("aoa3:"))rows.add(row("id",id.toString(),"uuid",call(actor,"net.minecraft.world.entity.Entity","getUUID",new Class<?>[0]).toString()));
        }return rows;
    }
    private static Object item(String key,int count)throws Exception{return c("net.minecraft.world.item.ItemStack").getConstructor(c("net.minecraft.world.level.ItemLike"),int.class).newInstance(registered("ITEM","aoa3:"+key),count);}
    private static void inventorySet(Object inventory,int slot,Object stack)throws Exception{call(inventory,"net.minecraft.world.entity.player.Inventory","setItem",new Class<?>[]{int.class,c("net.minecraft.world.item.ItemStack")},slot,stack);}
    private static int count(Object inventory,int slot)throws Exception{return ((Number)call(call(inventory,"net.minecraft.world.entity.player.Inventory","getItem",new Class<?>[]{int.class},slot),"net.minecraft.world.item.ItemStack","getCount",new Class<?>[0])).intValue();}
    private static List<Object> progression(Object world)throws Exception{
        Object identity=c("com.mojang.authlib.GameProfile").getConstructor(UUID.class,String.class).newInstance(UUID.randomUUID(),"[EnderloomDungeon]");
        Object player=call(null,"net.minecraftforge.common.util.FakePlayerFactory","get",new Class<?>[]{c("net.minecraft.server.level.ServerLevel"),c("com.mojang.authlib.GameProfile")},world,identity),inventory=call(player,"net.minecraft.world.entity.player.Player","getInventory",new Class<?>[0]);
        // Forge's FakePlayerNetHandler deliberately makes both teleport
        // overloads no-ops. Exercise the real native teleport implementation
        // using a detached Connection instead; no client/socket is connected
        // and no expected coordinate is injected into the fixture.
        Object server=call(world,"net.minecraft.server.level.ServerLevel","getServer",new Class<?>[0]);
        Object flow=Enum.valueOf((Class)c("net.minecraft.network.protocol.PacketFlow"),"SERVERBOUND"),connection=c("net.minecraft.network.Connection").getConstructor(c("net.minecraft.network.protocol.PacketFlow")).newInstance(flow);
        Object listener=c("net.minecraft.server.network.ServerGamePacketListenerImpl").getConstructor(c("net.minecraft.server.MinecraftServer"),c("net.minecraft.network.Connection"),c("net.minecraft.server.level.ServerPlayer")).newInstance(server,connection,player);
        c("net.minecraft.server.level.ServerPlayer").getField("connection").set(player,listener);
        Object tribute=call(null,"net.tslat.aoa3.event.TributeEvents","tribute",new Class<?>[]{c("net.minecraft.server.level.ServerPlayer")},player);check(tribute!=null,"Native dungeon player resource unavailable");
        Class<?> deity=c("net.tslat.aoa3.player.resource.TributeResource$Deities"),playerType=c("net.minecraft.server.level.ServerPlayer");List<Object> rows=new ArrayList<Object>();
        int[][] expected={{28,20,2},{67,21,2},{81,21,2},{122,21,2},{141,24,2},{168,24,7},{189,20,2},{233,21,3},{0,20,0}};
        for(int stage=1;stage<=9;stage++){
            call(inventory,"net.minecraft.world.entity.player.Inventory","clearContent",new Class<?>[0]);call(tribute,"net.tslat.aoa3.player.resource.TributeResource","resetAllTribute",new Class<?>[0]);
            check(!(Boolean)call(null,FAMILY+"ImmortallisProgression","activate",new Class<?>[]{playerType,int.class},player,stage),"Dungeon stage accepted absent prerequisite "+stage);
            if(stage==1||stage==3||stage==5||stage==7||stage==9){int coin=(stage-1)/2;inventorySet(inventory,0,call(null,FAMILY+"ImmortallisProgression","token",new Class<?>[]{int.class},coin));}
            else{Object selected=Enum.valueOf((Class)deity,stage==2||stage==6?"Pluton":"Erebon");call(tribute,"net.tslat.aoa3.player.resource.TributeResource","setTribute",new Class<?>[]{deity,int.class},selected,stage<=4?100:200);}
            check((Boolean)call(null,FAMILY+"ImmortallisProgression","activate",new Class<?>[]{playerType,int.class},player,stage),"Native dungeon stage did not activate "+stage);
            for(int axis=0;axis<3;axis++){double actual=((Number)call(player,"net.minecraft.world.entity.Entity","get"+new String[]{"X","Y","Z"}[axis],new Class<?>[0])).doubleValue();check(actual==expected[stage-1][axis],"Native dungeon stage destination changed "+stage+" axis="+axis+" actual="+actual+" expected="+expected[stage-1][axis]);}
            rows.add(row("stage",stage,"missingPrerequisiteRejected",true,"actualDestination",Arrays.asList(expected[stage-1][0],expected[stage-1][1],expected[stage-1][2]),"actualInventory",call(inventory,"net.minecraft.world.entity.player.Inventory","save",new Class<?>[]{c("net.minecraft.nbt.ListTag")},c("net.minecraft.nbt.ListTag").getConstructor().newInstance()).toString()));
        }
        call(inventory,"net.minecraft.world.entity.player.Inventory","clearContent",new Class<?>[0]);
        for(int slot=0;slot<36;slot++)inventorySet(inventory,slot,item("dungeon_tokens",64));Object exact=call(null,FAMILY+"ImmortallisProgression","token",new Class<?>[]{int.class},0);call(exact,"net.minecraft.world.item.ItemStack","setCount",new Class<?>[]{int.class},64);inventorySet(inventory,0,exact);
        Object full=call(inventory,"net.minecraft.world.entity.player.Inventory","save",new Class<?>[]{c("net.minecraft.nbt.ListTag")},c("net.minecraft.nbt.ListTag").getConstructor().newInstance());
        check(!(Boolean)call(null,FAMILY+"ImmortallisProgression","activate",new Class<?>[]{playerType,int.class},player,1),"Full inventory entry lost token");Object after=call(inventory,"net.minecraft.world.entity.player.Inventory","save",new Class<?>[]{c("net.minecraft.nbt.ListTag")},c("net.minecraft.nbt.ListTag").getConstructor().newInstance());check(full.equals(after),"Failed entry changed full inventory bytes");rows.add(row("fullInventoryExactRollback",true,"completeBeforeAndAfter",full.toString()));
        for(boolean pure:new boolean[]{false,true}){
            call(inventory,"net.minecraft.world.entity.player.Inventory","clearContent",new Class<?>[0]);call(tribute,"net.tslat.aoa3.player.resource.TributeResource","resetAllTribute",new Class<?>[0]);inventorySet(inventory,0,item(pure?"pure_gold":"impure_gold",2));
            check((Boolean)call(null,FAMILY+"ImmortallisProgression","deposit",new Class<?>[]{playerType,boolean.class},player,pure)&&count(inventory,0)==1,"Native gold deposit did not consume exactly one");Object pluton=Enum.valueOf((Class)deity,"Pluton");check(((Number)call(tribute,"net.tslat.aoa3.player.resource.TributeResource","getTribute",new Class<?>[]{deity},pluton)).intValue()==20,"Native accumulator award changed");
            call(tribute,"net.tslat.aoa3.player.resource.TributeResource","setTribute",new Class<?>[]{deity,int.class},pluton,pure?200:100);check(!(Boolean)call(null,FAMILY+"ImmortallisProgression","deposit",new Class<?>[]{playerType,boolean.class},player,pure)&&count(inventory,0)==1,"Full native accumulator consumed gold");rows.add(row("pure",pure,"actualAward",20,"fullCapConsumesNothing",true));
        }
        call(inventory,"net.minecraft.world.entity.player.Inventory","clearContent",new Class<?>[0]);return rows;
    }
    @SuppressWarnings("unchecked") public static String capture(Object server)throws Exception{
        loader=server.getClass().getClassLoader();try{c(FAMILY+"DungeonRealmFamily");}catch(ClassNotFoundException absent){return "null";}
        boolean managed=false;for(Path part:Paths.get("").toAbsolutePath().normalize())if(part.toString().equals("conversion-builds"))managed=true;check(managed,"Dungeon fixtures require an owned disposable conversion world");
        Class<?> position=c("net.minecraft.core.BlockPos"),stateType=c("net.minecraft.world.level.block.state.BlockState"),levelType=c("net.minecraft.world.level.Level"),playerType=c("net.minecraft.server.level.ServerPlayer");
        List<Object> worlds=new ArrayList<Object>(),failures=new ArrayList<Object>();Map<String,Object> levels=new LinkedHashMap<String,Object>();int total=0,cages=0,protectedCount=0;
        Path trace=Paths.get("enderloom-complete-dungeon-native-cells.zip");
        try(ZipOutputStream zip=new ZipOutputStream(Files.newOutputStream(trace,StandardOpenOption.CREATE_NEW))){
            zip.putNextEntry(new ZipEntry("all-native-final-cells.tsv"));Writer writer=new BufferedWriter(new OutputStreamWriter(zip,StandardCharsets.UTF_8));
            for(String realm:Arrays.asList("ancient_cavern","immortallis")){
                Object container=call(null,FAMILY+"DungeonRealmFamily","container",new Class<?>[]{String.class},realm),key=container.getClass().getField("key").get(container),world=call(server,"net.minecraft.server.MinecraftServer","getLevel",new Class<?>[]{c("net.minecraft.resources.ResourceKey")},key);check(world!=null,"Missing complete dungeon world "+realm);levels.put(realm,world);
                Object source=call(world,"net.minecraft.server.level.ServerLevel","getChunkSource",new Class<?>[0]),generator=call(source,"net.minecraft.server.level.ServerChunkCache","getGenerator",new Class<?>[0]);check(generator.getClass()==c(FAMILY+"LiteralDungeonChunkGenerator"),"Substituted complete dungeon generator");
                Object type=call(world,"net.minecraft.world.level.Level","dimensionType",new Class<?>[0]);check(!(Boolean)call(type,"net.minecraft.world.level.dimension.DimensionType","hasSkyLight",new Class<?>[0]),"Original no-skylight choice lost");
                for(long time:new long[]{0,6000,12000,Long.MAX_VALUE})check(Float.floatToRawIntBits(((Number)call(type,"net.minecraft.world.level.dimension.DimensionType","timeOfDay",new Class<?>[]{long.class},time)).floatValue())==Float.floatToRawIntBits(.4F),"Original exact .4F provider angle lost");
                Object index=hidden(generator,"index");Map<?,?> chunks=(Map<?,?>)index.getClass().getMethod("chunks").invoke(index);Map<String,Object> palette=(Map<String,Object>)hidden(generator,"palette");
                for(Object chunkKey:chunks.keySet()){
                    long value=((Number)chunkKey).longValue();int x=(int)value,z=(int)(value>>>32);Object loaded=call(source,"net.minecraft.server.level.ServerChunkCache","getChunk",new Class<?>[]{int.class,int.class,c("net.minecraft.world.level.chunk.ChunkStatus"),boolean.class},x,z,field("net.minecraft.world.level.chunk.ChunkStatus","FULL"),true);check(loaded!=null,"Incomplete native dungeon chunk");
                }
                int cells=0,tiles=0,protectedCells=0;List<Object> tileRows=new ArrayList<Object>();
                for(Object chunk:chunks.values())for(Object write:(List<?>)chunk.getClass().getMethod("finalWrites").invoke(chunk)){
                    int x=number(write,"x"),y=number(write,"y"),z=number(write,"z");Object at=pos(x,y,z),binding=write.getClass().getMethod("binding").invoke(write);String bindingKey=String.valueOf(binding.getClass().getMethod("key").invoke(binding));
                    Object expected=palette.get(bindingKey),actual=call(world,"net.minecraft.world.level.Level","getBlockState",new Class<?>[]{position},at);
                    Object connected=call(null,"net.minecraft.world.level.block.Block","updateFromNeighbourShapes",new Class<?>[]{stateType,c("net.minecraft.world.level.LevelAccessor"),position},expected,world,at);
                    // Runtime fluid scheduling may change flowing level, but never
                    // its actual lava identity. No other mismatch is discarded.
                    Object eb=call(connected,"net.minecraft.world.level.block.state.BlockBehaviour$BlockStateBase","getBlock",new Class<?>[0]),ab=call(actual,"net.minecraft.world.level.block.state.BlockBehaviour$BlockStateBase","getBlock",new Class<?>[0]);
                    boolean lava=eb==field("net.minecraft.world.level.block.Blocks","LAVA")&&ab==eb;
                    if(!connected.equals(actual)&&!lava)failures.add(row("realm",realm,"position",Arrays.asList(x,y,z),"binding",bindingKey,"expected",connected.toString(),"actual",actual.toString()));
                    boolean protect=(Boolean)call(generator,FAMILY+"LiteralDungeonChunkGenerator","protects",new Class<?>[]{position,stateType},at,actual);if(protect)protectedCells++;
                    writer.write(realm+"\t"+x+"\t"+y+"\t"+z+"\t"+bindingKey+"\t"+connected+"\t"+actual+"\t"+protect+"\n");cells++;
                    if(c("net.tslat.aoa3.content.entity.snapshot1710.SnapshotTempleSpawners").isInstance(ab)){
                        Object tile=call(world,"net.minecraft.world.level.Level","getBlockEntity",new Class<?>[]{position},at);check(tile!=null,"Missing native dungeon cage tile");Object tag=call(tile,"net.minecraft.world.level.block.entity.BlockEntity","saveWithFullMetadata",new Class<?>[0]);String entity=String.valueOf(ab.getClass().getField("entityKey").get(ab));
                        for(String n:new String[]{"Delay","MinSpawnDelay","MaxSpawnDelay","SpawnCount","MaxNearbyEntities","RequiredPlayerRange","SpawnRange"}){int value=((Number)call(tag,"net.minecraft.nbt.CompoundTag","getShort",new Class<?>[]{String.class},n)).intValue();int expectedValue=n.equals("Delay")?20:n.equals("MinSpawnDelay")?200:n.equals("MaxSpawnDelay")?800:n.equals("SpawnCount")?4:n.equals("MaxNearbyEntities")?6:n.equals("RequiredPlayerRange")?16:4;check(value==expectedValue,"Native cage default changed: "+n);}
                        check(tag.toString().contains("aoa3:"+entity)&&tag.toString().contains("custom_spawn_rules"),"Native cage identity/rules lost");tileRows.add(row("position",Arrays.asList(x,y,z),"entity",entity,"completeNbt",tag.toString()));tiles++;
                    }
                }
                check(cells==(realm.equals("immortallis")?26438:25978)&&tiles==(realm.equals("immortallis")?32:8),"Incomplete authored dungeon domain");total+=cells;cages+=tiles;protectedCount+=protectedCells;worlds.add(row("realm",realm,"completeNativeChunks",chunks.size(),"completeCells",cells,"nativeCages",tileRows,"protectedCells",protectedCells,"observedLoadedActorsBeforeFixture",actors(world)));
            }writer.flush();zip.closeEntry();
        }
        List<Object> offers=new ArrayList<Object>();Object dungeon=levels.get("immortallis");
        for(String key:Arrays.asList("dungeon_keeper","token_collector")){
            Object trader=actor(dungeon,key);List<?> list=(List<?>)call(trader,"net.minecraft.world.entity.npc.AbstractVillager","getOffers",new Class<?>[0]);check(list.size()==(key.equals("dungeon_keeper")?11:15),"Incomplete dungeon merchant offers");Object tag=call(trader,"net.minecraft.world.entity.Entity","saveWithoutId",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},c("net.minecraft.nbt.CompoundTag").getConstructor().newInstance());Object restored=actor(dungeon,key);call(restored,"net.minecraft.world.entity.Entity","load",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},tag);List<?> reloaded=(List<?>)call(restored,"net.minecraft.world.entity.npc.AbstractVillager","getOffers",new Class<?>[0]);check(reloaded.size()==list.size(),"Merchant save lost offers");offers.add(row("id",key,"completeOffers",tag.toString(),"saveReloadOffers",reloaded.size()));
        }
        check(failures.isEmpty(),"Native complete dungeon placement differs: "+failures.subList(0,Math.min(failures.size(),20)));
        List<Object> bossTraits=new ArrayList<Object>();String[] bossKeys={"coniferon","goldorth","horon","penumbra"};
        double[][] originalTraits={{4000,25,52,.3,.8},{3000,17,52,1,.10000000149011612},{3000,24,52,.3,.8},{3000,15,16,0,.5}};String[] attributeKeys={"MAX_HEALTH","ATTACK_DAMAGE","FOLLOW_RANGE","KNOCKBACK_RESISTANCE","MOVEMENT_SPEED"};
        for(int i=0;i<bossKeys.length;i++){
            Object boss=actor(levels.get("ancient_cavern"),bossKeys[i]);List<Object> attributes=new ArrayList<Object>();
            for(int a=0;a<attributeKeys.length;a++){
                Object definition=field("net.minecraft.world.entity.ai.attributes.Attributes",attributeKeys[a]);double actual=((Number)call(boss,"net.minecraft.world.entity.LivingEntity","getAttributeValue",new Class<?>[]{c("net.minecraft.world.entity.ai.attributes.Attribute")},definition)).doubleValue();
                check(Double.doubleToRawLongBits(actual)==Double.doubleToRawLongBits(originalTraits[i][a]),"Original exact boss attribute changed: "+bossKeys[i]+" "+attributeKeys[a]+" "+actual);attributes.add(row("attribute",attributeKeys[a],"actual",actual));
            }
            check(((Number)call(boss,"net.minecraft.world.entity.LivingEntity","getHealth",new Class<?>[0])).doubleValue()==originalTraits[i][0],"Boss initial health differs from its full original max");bossTraits.add(row("id",bossKeys[i],"attributes",attributes,"completeNativeNbt",call(boss,"net.minecraft.world.entity.Entity","saveWithoutId",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},c("net.minecraft.nbt.CompoundTag").getConstructor().newInstance()).toString()));
        }
        List<Object> accessTraits=new ArrayList<Object>();
        String[] accessKeys={"automaton","death_hunter","hellspot"};double[][] accessAttributes={{80,10,52,1,1},{200,6,52,.1,.8},{50,4,52,.1,.8}};
        for(int i=0;i<accessKeys.length;i++){
            Object creature=actor(levels.get("ancient_cavern"),accessKeys[i]);List<Object> values=new ArrayList<Object>();
            for(int a=0;a<attributeKeys.length;a++){
                Object definition=field("net.minecraft.world.entity.ai.attributes.Attributes",attributeKeys[a]);double actual=((Number)call(creature,"net.minecraft.world.entity.LivingEntity","getAttributeValue",new Class<?>[]{c("net.minecraft.world.entity.ai.attributes.Attribute")},definition)).doubleValue();
                check(Double.doubleToRawLongBits(actual)==Double.doubleToRawLongBits(accessAttributes[i][a]),"Original dungeon access attribute changed: "+accessKeys[i]+" "+attributeKeys[a]);values.add(row("attribute",attributeKeys[a],"actual",actual));
            }
            List<Object> variants=new ArrayList<Object>();
            if(accessKeys[i].equals("automaton"))for(int colour=1;colour<=5;colour++){
                call(creature,"net.tslat.aoa3.content.entity.cavern.DungeonAutomaton","setColour",new Class<?>[]{int.class},colour);Object tag=call(creature,"net.minecraft.world.entity.Entity","saveWithoutId",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},c("net.minecraft.nbt.CompoundTag").getConstructor().newInstance()),restored=actor(levels.get("ancient_cavern"),"automaton");
                call(restored,"net.minecraft.world.entity.Entity","load",new Class<?>[]{c("net.minecraft.nbt.CompoundTag")},tag);check(((Number)call(restored,"net.tslat.aoa3.content.entity.cavern.DungeonAutomaton","colour",new Class<?>[0])).intValue()==colour,"Original Automaton colour lost at save/reload");variants.add(row("colour",colour,"nativeSaveReload",true));
            }
            accessTraits.add(row("id",accessKeys[i],"attributes",values,"completeColourSaveCases",variants));
        }
        List<Object> realmstones=new ArrayList<Object>();for(String realm:Arrays.asList("ancient_cavern","immortallis")){
            Object stone=registered("ITEM","aoa3:"+realm+"_realmstone");check(c("net.tslat.aoa3.content.item.misc.Realmstone").isInstance(stone),"Dungeon key does not use complete native portal activation");Object registeredBlock=call(stone,"net.tslat.aoa3.content.item.misc.Realmstone","getPortalBlock",new Class<?>[0]);Object block=registeredBlock.getClass().getMethod("get").invoke(registeredBlock);check(block==registered("BLOCK","aoa3:"+realm+"_portal"),"Dungeon realmstone points to wrong native portal");realmstones.add(row("item",realm+"_realmstone","exactNativePortal",realm+"_portal"));
        }
        List<Object> stages=progression(dungeon);
        List<Object> buybackCases=realmshifterBuybacks(dungeon);
        String text=NativeCompleteHistoricalEquipmentInspection.json(row("passed",true,"syntheticWorld",false,"actualNativeServer",true,"generatedFixture",true,"progressionPlayer","Forge FakePlayer with actual native ServerGamePacketListenerImpl and detached packet Connection; no connected client/survival claim","fullSurvivalVerified",false,"completeAoAPort",false,"completeCells",total,"completeCages",cages,"protectedCells",protectedCount,"worlds",worlds,"completeNativeCellTrace",artifact(trace),"merchantOffers",offers,"completeBossTraits",bossTraits,"completeAccessTraits",accessTraits,"realmstoneBindings",realmstones,"completeProgressionCases",stages,"nativePlacementFailures",failures));
        text=text.substring(0,text.length()-1)+",\"completeRealmshifterBuybackCases\":"+NativeCompleteHistoricalEquipmentInspection.json(buybackCases)+"}";
        Files.write(Paths.get("enderloom-complete-dungeon-native.json"),text.getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);System.out.println("ENDERLOOM_COMPLETE_DUNGEON_NATIVE "+text);return text;
    }
}
