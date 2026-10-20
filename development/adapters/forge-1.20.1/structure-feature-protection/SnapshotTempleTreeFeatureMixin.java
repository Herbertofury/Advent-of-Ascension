package net.tslat.aoa3.mixin.common.patch;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.WorldGenRegion;
import net.minecraft.world.level.LevelSimulatedReader;
import net.minecraft.world.level.LevelWriter;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.levelgen.feature.TreeFeature;
import net.tslat.aoa3.content.world.genold.feature.features.trees.SnapshotVegetationRegion;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(TreeFeature.class)
public abstract class SnapshotTempleTreeFeatureMixin {
    @Inject(method="validTreePos",at=@At("HEAD"),cancellable=true)
    private static void aoa3$respectStructureSpace(LevelSimulatedReader reader,BlockPos position,CallbackInfoReturnable<Boolean> result) {
        if (reader instanceof WorldGenRegion && ((SnapshotVegetationRegion)reader).aoa3$isTreeProtected(position)) result.setReturnValue(false);
    }

    @Inject(method="setBlockKnownShape",at=@At("HEAD"),cancellable=true)
    private static void aoa3$preserveStructureBlocks(LevelWriter reader,BlockPos position,BlockState state,CallbackInfo result) {
        if (reader instanceof WorldGenRegion && ((SnapshotVegetationRegion)reader).aoa3$isTreeProtected(position)) result.cancel();
    }
}
