package net.tslat.aoa3.content.world.genold.feature.features.trees;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.StructureManager;
import net.minecraft.world.level.WorldGenLevel;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.world.level.levelgen.structure.Structure;

/** Per-tree, native-start protection; never a global prohibition on tree growth. */
public final class RunicArenaTreeProtection {
    private static final ResourceLocation ARENA = new ResourceLocation("aoa3", "clunkhead_arena");
    private static final ThreadLocal<Context> ACTIVE = new ThreadLocal<>();

    public static Frame enter(WorldGenLevel reader, boolean worldGeneration) {
        Context previous = ACTIVE.get();
        Context next = null;
        if (worldGeneration && reader instanceof WorldGenRegion region) {
            Structure arena = region.registryAccess().registryOrThrow(Registries.STRUCTURE).get(ARENA);
            if (arena != null) next = new Context(region, region.getLevel().structureManager().forWorldGenRegion(region), arena);
        }
        if (next == null) ACTIVE.remove(); else ACTIVE.set(next);
        return new Frame(previous);
    }

    public static boolean protects(WorldGenLevel reader, BlockPos position) {
        Context context = ACTIVE.get();
        return context != null && context.reader == reader && context.contains(position);
    }

    private static final class Context {
        private final WorldGenRegion reader;
        private final StructureManager structures;
        private final Structure arena;
        // A tree's small footprint only; discarded in finally after that tree.
        private final Map<Long, List<BoundingBox>> bounds = new HashMap<>();
        private Context(WorldGenRegion reader, StructureManager structures, Structure arena) {
            this.reader = reader; this.structures = structures; this.arena = arena;
        }
        private boolean contains(BlockPos position) {
            int x = position.getX() >> 4, z = position.getZ() >> 4;
            List<BoundingBox> boxes = bounds.computeIfAbsent(ChunkPos.asLong(x,z), key -> {
                List<BoundingBox> found = new ArrayList<>();
                for (var start : structures.startsForStructure(new ChunkPos(x,z), structure -> structure == arena)) {
                    if (!start.isValid()) continue;
                    BoundingBox box = start.getBoundingBox();
                    found.add(new BoundingBox(box.minX(),box.minY(),box.minZ(),box.maxX(),box.maxY(),box.maxZ()));
                }
                return List.copyOf(found);
            });
            for (BoundingBox box : boxes) if (box.isInside(position)) return true;
            return false;
        }
    }

    public static final class Frame implements AutoCloseable {
        private final Context previous;
        private boolean closed;
        private Frame(Context previous) { this.previous = previous; }
        @Override public void close() {
            if (closed) throw new IllegalStateException("Tree generation scope already closed");
            closed = true;
            if (previous == null) ACTIVE.remove(); else ACTIVE.set(previous);
        }
    }
    private RunicArenaTreeProtection() {}
}
