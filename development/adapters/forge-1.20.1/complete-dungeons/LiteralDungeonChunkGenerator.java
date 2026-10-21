package net.tslat.aoa3.content.world.gen.compat.dungeons;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.*;
import net.minecraft.core.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.level.*;
import net.minecraft.world.level.biome.*;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.chunk.*;
import net.minecraft.world.level.levelgen.*;
import net.minecraft.world.level.levelgen.blending.Blender;
import net.minecraftforge.registries.ForgeRegistries;

/** Native void-world lifecycle for both complete fixed dungeons. Only new
 * chunks use this generator. No loaded chunk, save or other realm is rewritten.
 * Every exact original field/metadata binding must be supplied by its reviewed
 * codec palette: absence or an extra binding is an error, never AIR fallback.
 */
public final class LiteralDungeonChunkGenerator extends ChunkGenerator {
    public static final Codec<LiteralDungeonChunkGenerator> CODEC=RecordCodecBuilder.create(instance->instance.group(
        BiomeSource.CODEC.fieldOf("biome_source").forGetter(value->value.biomeSource),
        Codec.STRING.fieldOf("realm").forGetter(value->value.realm),
        Codec.unboundedMap(Codec.STRING,BlockState.CODEC).fieldOf("exact_original_palette").forGetter(value->value.palette),
        Codec.STRING.listOf().fieldOf("unbreakable_original_fields").forGetter(value->value.unbreakableFields)
    ).apply(instance,LiteralDungeonChunkGenerator::new));
    private static final BlockState AIR=Blocks.AIR.defaultBlockState();
    private static final Map<String,LiteralDungeonIndex> INDEXES=new ConcurrentHashMap<>();
    private final String realm;
    private final Map<String,BlockState> palette;
    private final LiteralDungeonIndex index;
    private final Map<Long,List<Cell>> chunks;
    private final List<String> unbreakableFields;
    private final Map<BlockPos,Block> protectedCells;
    private record Cell(int x,int y,int z,BlockState state){}
    public LiteralDungeonChunkGenerator(BiomeSource biomes,String realm,Map<String,BlockState> palette,List<String> unbreakableFields){
        super(biomes);this.realm=realm;this.index=INDEXES.computeIfAbsent(realm,LiteralDungeonChunkGenerator::load);
        Set<String> required=new HashSet<>();for(var binding:index.bindings())required.add(binding.key());
        if(!palette.keySet().equals(required)||palette.values().stream().anyMatch(Objects::isNull))throw new IllegalArgumentException("Complete reviewed original field/metadata palette required for "+realm);
        Set<String> originalFields=new HashSet<>();for(var binding:index.bindings())originalFields.add(binding.originalField());
        if(new HashSet<>(unbreakableFields).size()!=unbreakableFields.size()||!originalFields.containsAll(unbreakableFields))throw new IllegalArgumentException("Unowned original dungeon protection field");
        this.unbreakableFields=List.copyOf(unbreakableFields);
        this.palette=Map.copyOf(palette);Map<Long,List<Cell>> projected=new HashMap<>();Map<BlockPos,Block> protectedMap=new HashMap<>();
        for(var entry:index.chunks().entrySet()){
            List<Cell> cells=new ArrayList<>();for(var write:entry.getValue().finalWrites()){
                BlockState state=palette.get(write.binding().key());cells.add(new Cell(write.x(),write.y(),write.z(),state));
                if(unbreakableFields.contains(write.binding().originalField()))protectedMap.put(new BlockPos(write.x(),write.y(),write.z()),state.getBlock());
            }
            projected.put(entry.getKey(),List.copyOf(cells));
        }
        chunks=Map.copyOf(projected);protectedCells=Map.copyOf(protectedMap);
    }
    public boolean protects(BlockPos pos,BlockState state){return protectedCells.get(pos)==state.getBlock();}
    private static LiteralDungeonIndex load(String realm){
        String resource="/data/aoa3/legacy_programs/complete_two_dungeons.json";
        try(InputStream stream=Objects.requireNonNull(LiteralDungeonChunkGenerator.class.getResourceAsStream(resource),"Missing complete dungeon family");Reader reader=new InputStreamReader(stream,StandardCharsets.UTF_8)){
            return new LiteralDungeonIndex(realm,reader);
        }catch(IOException error){throw new UncheckedIOException(error);}
    }
    private List<Cell> cells(int x,int z){return chunks.getOrDefault(LiteralDungeonIndex.chunkKey(x,z),List.of());}
    @Override protected Codec<? extends ChunkGenerator> codec(){return CODEC;}
    @Override public CompletableFuture<ChunkAccess> fillFromNoise(Executor executor,Blender blender,RandomState random,StructureManager structures,ChunkAccess chunk){
        return CompletableFuture.supplyAsync(()->{
            BlockPos.MutableBlockPos position=new BlockPos.MutableBlockPos();
            for(Cell cell:cells(chunk.getPos().x,chunk.getPos().z)){
                if(cell.y<chunk.getMinBuildHeight()||cell.y>=chunk.getMaxBuildHeight())throw new IllegalStateException("Native world cannot contain the complete authored dungeon");
                chunk.setBlockState(position.set(cell.x,cell.y,cell.z),cell.state,false);
                if(cell.state.getBlock() instanceof net.tslat.aoa3.content.entity.snapshot1710.SnapshotTempleSpawners spawner){
                    var tile=(net.tslat.aoa3.content.entity.snapshot1710.SnapshotTempleSpawners.Tile)spawner.newBlockEntity(position.immutable(),cell.state);
                    tile.initializeNewNaturalEncounter(false);chunk.setBlockEntityNbt(tile.saveWithFullMetadata());
                }
            }
            Heightmap.primeHeightmaps(chunk,EnumSet.of(Heightmap.Types.WORLD_SURFACE_WG,Heightmap.Types.OCEAN_FLOOR_WG));return chunk;
        },executor);
    }
    @Override public void buildSurface(WorldGenRegion region,StructureManager structures,RandomState random,ChunkAccess chunk){}
    @Override public void applyCarvers(WorldGenRegion region,long seed,RandomState random,BiomeManager biomes,StructureManager structures,ChunkAccess chunk,GenerationStep.Carving step){}
    @Override public void applyBiomeDecoration(WorldGenLevel level,ChunkAccess chunk,StructureManager structures){
        super.applyBiomeDecoration(level,chunk,structures);
        for(Cell cell:cells(chunk.getPos().x,chunk.getPos().z)){
            BlockPos pos=new BlockPos(cell.x,cell.y,cell.z);
            BlockState current=level.getBlockState(pos);
            BlockState connected=Block.updateFromNeighbourShapes(current,level,pos);
            if(!current.equals(connected))level.setBlock(pos,connected,2);
            // Native chunk loading owns block-entity creation. Fluid scheduling
            // stays with newly generated cells, never a saved-world rewrite.
            var fluid=level.getFluidState(pos);if(!fluid.isEmpty())level.scheduleTick(pos,fluid.getType(),fluid.getType().getTickDelay(level));
        }
    }
    @Override public void spawnOriginalMobs(WorldGenRegion region){
        if(!realm.equals("immortallis"))return;
        // At original population chunk (0,0), the final seed is exactly the
        // world seed, irrespective of previous provider RNG history. These are
        // its only two random calls, in original constructor/spawn order.
        java.util.Random random=new java.util.Random(region.getSeed());
        String[] keys={"dungeon_keeper","token_collector"};int[] x={15,-3};
        for(int i=0;i<2;i++){
            float yaw=random.nextFloat()*360F;
            if(region.getCenter().x!=Math.floorDiv(x[i],16)||region.getCenter().z!=0)continue;
            var type=ForgeRegistries.ENTITY_TYPES.getValue(new ResourceLocation("aoa3",keys[i]));
            if(type==null)throw new IllegalStateException("Missing complete dungeon actor "+keys[i]);
            Entity actor=type.create(region.getLevel());if(actor==null)throw new IllegalStateException("Dungeon actor factory returned null");
            actor.moveTo(x[i],19,5,yaw,0);
            if(actor instanceof net.minecraft.world.entity.Mob mob)mob.setPersistenceRequired();
            if(!region.addFreshEntity(actor))throw new IllegalStateException("Native generation rejected a complete dungeon actor");
        }
    }
    @Override public int getMinY(){return 0;}
    @Override public int getGenDepth(){return 256;}
    @Override public int getSeaLevel(){return 0;}
    @Override public int getSpawnHeight(LevelHeightAccessor access){return realm.equals("immortallis")?20:18;}
    @Override public int getBaseHeight(int x,int z,Heightmap.Types type,LevelHeightAccessor access,RandomState random){
        int result=access.getMinBuildHeight();for(Cell cell:cells(Math.floorDiv(x,16),Math.floorDiv(z,16)))if(cell.x==x&&cell.z==z&&type.isOpaque().test(cell.state))result=Math.max(result,cell.y+1);return result;
    }
    @Override public NoiseColumn getBaseColumn(int x,int z,LevelHeightAccessor access,RandomState random){
        BlockState[] column=new BlockState[access.getHeight()];Arrays.fill(column,AIR);
        for(Cell cell:cells(Math.floorDiv(x,16),Math.floorDiv(z,16)))if(cell.x==x&&cell.z==z&&cell.y>=access.getMinBuildHeight()&&cell.y<access.getMaxBuildHeight())column[cell.y-access.getMinBuildHeight()]=cell.state;
        return new NoiseColumn(access.getMinBuildHeight(),column);
    }
    @Override public void addDebugScreenInfo(List<String> lines,RandomState random,BlockPos pos){lines.add("AoA complete authored dungeon: "+realm);}
}
