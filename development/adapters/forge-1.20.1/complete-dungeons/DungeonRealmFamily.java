package net.tslat.aoa3.content.world.gen.compat.dungeons;

import java.util.*;
import net.minecraft.core.BlockPos;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.level.*;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.item.*;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.level.material.MapColor;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.*;
import net.minecraftforge.server.ServerLifecycleHooks;
import net.tslat.aoa3.common.registration.AoACreativeModeTabs;
import net.tslat.aoa3.common.registration.worldgen.AoADimensions;
import net.tslat.aoa3.content.block.functional.portal.PortalBlock;
import net.tslat.aoa3.content.entity.cavern.CavernDeityBoss;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotTempleFamily;
import net.tslat.aoa3.content.world.teleporter.AoATeleporter;

/** New native worlds share existing canonical decorative blocks, mob classes
 * and the same spawner lifecycle. Distinct stage/mode choices are block states,
 * preserving every role without nine duplicate progressor item registrations.
 */
public final class DungeonRealmFamily {
    private static final DeferredRegister<Block> BLOCKS=DeferredRegister.create(ForgeRegistries.BLOCKS,"aoa3");
    private static final DeferredRegister<Item> ITEMS=DeferredRegister.create(ForgeRegistries.ITEMS,"aoa3");
    public static final List<String> REALMS=List.of("ancient_cavern","immortallis");
    public static final Map<String,RegistryObject<Block>> PORTALS=new LinkedHashMap<>();
    public static final Map<CavernDeityBoss.Kind,RegistryObject<Block>> SHRINES=new EnumMap<>(CavernDeityBoss.Kind.class);
    private static final List<RegistryObject<Item>> CONTENT=new ArrayList<>();
    public static final RegistryObject<Block> PROGRESSOR=block("immortallis_progressor",()->new ImmortallisProgressorBlock(immutable()));
    public static final RegistryObject<Block> ACCUMULATOR=block("gold_accumulator",()->new ImmortallisAccumulatorBlock(immutable()));
    public static final RegistryObject<Block> CYCADE_LOG=block("cycade_log",()->new RotatedPillarBlock(BlockBehaviour.Properties.of().mapColor(MapColor.WOOD).strength(2,.5F).sound(SoundType.WOOD)));
    public static final RegistryObject<Block> CYCADE_LEAVES=block("cycade_leaves",()->new LeavesBlock(BlockBehaviour.Properties.of().mapColor(MapColor.PLANT).strength(.2F,0).sound(SoundType.GRASS).noOcclusion()){
        @Override public boolean isRandomlyTicking(BlockState state){return false;}
    });
    private static final Map<MinecraftServer,Map<String,HashMap<Long,BlockPos>>> CACHES=new WeakHashMap<>();
    static {
        for(String realm:REALMS)PORTALS.put(realm,block(realm+"_portal",()->new PortalBlock(BlockBehaviour.Properties.copy(Blocks.NETHER_PORTAL).noLootTable(),container(realm).key,realm.equals("immortallis")?0x8e4d32:0x708f83)));
        for(var kind:CavernDeityBoss.Kind.values())SHRINES.put(kind,block(kind.deity+"_shrine",()->new CavernShrineBlock(kind,immutable())));
        for(String mob:List.of("automaton","bloodsucker","rock_critter","fenix","flowerface","ghastus","goldum","goldus","reaver","shavo","skeledon","skelekyte","urioh","urv","visage"))SnapshotTempleFamily.registerSpawner(mob);
    }
    private static BlockBehaviour.Properties immutable(){return BlockBehaviour.Properties.of().mapColor(MapColor.STONE).strength(-1,600000000F).noLootTable();}
    private static RegistryObject<Block> block(String key,java.util.function.Supplier<Block> factory){var block=BLOCKS.register(key,factory);CONTENT.add(ITEMS.register(key,()->new BlockItem(block.get(),new Item.Properties())));return block;}
    public static AoADimensions.DimensionContainer container(String realm){return switch(realm){case "ancient_cavern"->AoADimensions.ANCIENT_CAVERN;case "immortallis"->AoADimensions.IMMORTALLIS;default->throw new IllegalArgumentException("Unknown original dungeon "+realm);};}
    public static void init(IEventBus bus){
        BLOCKS.register(bus);ITEMS.register(bus);
        bus.addListener((BuildCreativeModeTabContentsEvent event)->{
            if(event.getTabKey().equals(AoACreativeModeTabs.FUNCTIONAL_BLOCKS.getKey())){
                CONTENT.forEach(item->event.accept(item.get()));
                for(int stage=2;stage<=9;stage++){ItemStack stack=new ItemStack(PROGRESSOR.get());stack.getOrCreateTagElement("BlockStateTag").putString("stage",Integer.toString(stage));event.accept(stack);}
                ItemStack pure=new ItemStack(ACCUMULATOR.get());pure.getOrCreateTagElement("BlockStateTag").putString("pure","true");event.accept(pure);
            }
        });
    }
    public static AoATeleporter teleporter(String realm){
        if(!REALMS.contains(realm))throw new IllegalArgumentException(realm);
        return new AoATeleporter(){
            @Override public HashMap<Long,BlockPos> getCachedPortalMap(){var server=Objects.requireNonNull(ServerLifecycleHooks.getCurrentServer());synchronized(CACHES){return CACHES.computeIfAbsent(server,s->new HashMap<>()).computeIfAbsent(realm,r->new HashMap<>());}}
            @Override public PortalBlock getPortalBlock(){return (PortalBlock)PORTALS.get(realm).get();}
            @Override public Block getBorderBlock(){return Objects.requireNonNull(ForgeRegistries.BLOCKS.getValue(new ResourceLocation("aoa3",realm.equals("immortallis")?"archaic_tiles":"ancient_tile_core")));}
            @Override protected BlockPos findReturnPos(ServerPlayer player,ServerLevel current,ServerLevel destination){return destination.dimension()==container(realm).key?null:super.findReturnPos(player,current,destination);}
            @Override public BlockPos findExistingPortal(Level destination,Entity actor){
                if(destination.dimension()!=container(realm).key)return super.findExistingPortal(destination,actor);
                BlockPos lobby=new BlockPos(0,realm.equals("immortallis")?20:18,0);destination.getChunk(lobby);return lobby;
            }
        };
    }
    private DungeonRealmFamily(){}
}
