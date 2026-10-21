package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.*;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.level.block.state.properties.BooleanProperty;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.phys.BlockHitResult;

public final class ImmortallisAccumulatorBlock extends Block {
    public static final BooleanProperty PURE=BooleanProperty.create("pure");
    public final boolean pure;
    public ImmortallisAccumulatorBlock(BlockBehaviour.Properties properties){this(false,properties);}
    public ImmortallisAccumulatorBlock(boolean pure,BlockBehaviour.Properties properties){super(properties);this.pure=pure;registerDefaultState(stateDefinition.any().setValue(PURE,pure));}
    @Override protected void createBlockStateDefinition(StateDefinition.Builder<Block,BlockState> builder){builder.add(PURE);}
    @Override public ItemStack getCloneItemStack(BlockGetter world,BlockPos pos,BlockState state){ItemStack stack=new ItemStack(this);stack.getOrCreateTagElement("BlockStateTag").putString("pure",state.getValue(PURE).toString());return stack;}
    @Override public InteractionResult use(BlockState state,Level world,BlockPos pos,Player player,InteractionHand hand,BlockHitResult hit){
        if(!world.isClientSide&&player instanceof ServerPlayer server)ImmortallisProgression.deposit(server,state.getValue(PURE));
        return InteractionResult.sidedSuccess(world.isClientSide);
    }
}
