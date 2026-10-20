package net.tslat.aoa3.mixin.common.patch;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.levelgen.structure.BoundingBox;
import net.minecraft.server.level.WorldGenRegion;
import net.tslat.aoa3.content.world.genold.feature.features.trees.SnapshotVegetationBounds;
import net.tslat.aoa3.content.world.genold.feature.features.trees.SnapshotVegetationRegion;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Unique;

@Mixin(WorldGenRegion.class)
public abstract class SnapshotVegetationRegionMixin implements SnapshotVegetationRegion {
    @Unique private volatile SnapshotVegetationBounds aoa3$treeBounds;

    @Override public boolean aoa3$isTreeProtected(BlockPos position) {
        return aoa3$bounds().contains(position);
    }

    @Override public boolean aoa3$intersectsProtectedFeature(BoundingBox volume) {
        return aoa3$bounds().intersects(volume);
    }

    @Unique private SnapshotVegetationBounds aoa3$bounds() {
        SnapshotVegetationBounds bounds = aoa3$treeBounds;
        if (bounds == null) {
            synchronized (this) {
                bounds = aoa3$treeBounds;
                if (bounds == null) aoa3$treeBounds = bounds = new SnapshotVegetationBounds((WorldGenRegion)(Object)this);
            }
        }
        return bounds;
    }
}
