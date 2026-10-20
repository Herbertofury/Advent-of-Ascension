package net.tslat.aoa3.content.world.genold.feature.features.trees;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.levelgen.structure.BoundingBox;

/** Native generation-region lifetime; no proxy or replacement world identity. */
public interface SnapshotVegetationRegion {
    boolean aoa3$isTreeProtected(BlockPos position);
    boolean aoa3$intersectsProtectedFeature(BoundingBox volume);
}
