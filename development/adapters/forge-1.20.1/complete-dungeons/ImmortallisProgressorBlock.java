package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.*;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.BlockHitResult;

/** Distinct saved stage blocks share the complete nine-stage implementation. */
public final class ImmortallisProgressorBlock extends Block {
    public static final IntegerProperty STAGE=IntegerProperty.create("stage",1,9);
    public final int stage;
    public ImmortallisProgressorBlock(BlockBehaviour.Properties properties){this(1,properties);}
    public ImmortallisProgressorBlock(int stage,BlockBehaviour.Properties properties){super(properties);if(stage<1||stage>9)throw new IllegalArgumentException("Unknown original progressor");this.stage=stage;registerDefaultState(stateDefinition.any().setValue(STAGE,stage));}
    @Override protected void createBlockStateDefinition(StateDefinition.Builder<Block,BlockState> builder){builder.add(STAGE);}
    @Override public ItemStack getCloneItemStack(BlockGetter world,BlockPos pos,BlockState state){ItemStack stack=new ItemStack(this);stack.getOrCreateTagElement("BlockStateTag").putString("stage",state.getValue(STAGE).toString());return stack;}
    @Override public InteractionResult use(BlockState state,Level world,BlockPos pos,Player player,InteractionHand hand,BlockHitResult hit){
        if(!world.isClientSide&&player instanceof ServerPlayer server)ImmortallisProgression.activate(server,state.getValue(STAGE));
        return InteractionResult.sidedSuccess(world.isClientSide);
    }
}
