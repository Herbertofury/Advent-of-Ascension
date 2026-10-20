package net.tslat.aoa3.content.world.genold.feature.features.trees;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.StructureManager;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.world.level.levelgen.structure.Structure;

/** Exact registered structure identities, cached only in the native region. */
public final class SnapshotVegetationBounds {
    private final StructureManager structures;
    private final Set<Structure> protectedStructures;
    private final Map<Long,List<BoundingBox>> chunks = new ConcurrentHashMap<>();

    public SnapshotVegetationBounds(WorldGenRegion region) {
        structures = region.getLevel().structureManager().forWorldGenRegion(region);
        var registry = region.registryAccess().registryOrThrow(Registries.STRUCTURE);
        Set<Structure> selected = new HashSet<>();
        for (String key : List.of("clunkhead_arena", "snapshot_fragment_temple_abyss", "snapshot_fragment_temple_barathos", "snapshot_fragment_temple_greckon", "snapshot_fragment_temple_haven", "snapshot_fragment_temple_lborean")) {
            Structure structure = registry.get(new ResourceLocation("aoa3",key));
            if (structure != null) selected.add(structure);
        }
        protectedStructures = Set.copyOf(selected);
    }

    public boolean contains(BlockPos position) {
        if (protectedStructures.isEmpty()) return false;
        for (BoundingBox box : bounds(position.getX() >> 4,position.getZ() >> 4)) if (box.isInside(position)) return true;
        return false;
    }

    public boolean intersects(BoundingBox volume) {
        if (protectedStructures.isEmpty()) return false;
        for (int z=volume.minZ() >> 4;z<=volume.maxZ() >> 4;z++)
            for (int x=volume.minX() >> 4;x<=volume.maxX() >> 4;x++)
                for (BoundingBox box : bounds(x,z)) if (box.intersects(volume)) return true;
        return false;
    }

    private List<BoundingBox> bounds(int x,int z) {
        return chunks.computeIfAbsent(ChunkPos.asLong(x,z), key -> {
            List<BoundingBox> found = new ArrayList<>();
            for (var start : structures.startsForStructure(new ChunkPos(x,z), protectedStructures::contains)) {
                if (!start.isValid()) continue;
                BoundingBox box = start.getBoundingBox();
                found.add(new BoundingBox(box.minX(),box.minY(),box.minZ(),box.maxX(),box.maxY(),box.maxZ()));
            }
            return List.copyOf(found);
        });
    }
}
