package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.*;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.phys.BlockHitResult;
import net.tslat.aoa3.common.registration.custom.AoASkills;
import net.tslat.aoa3.content.entity.cavern.*;
import net.tslat.aoa3.event.TributeEvents;
import net.tslat.aoa3.player.resource.TributeResource;
import net.tslat.aoa3.util.PlayerUtil;

/** Every original skill/tribute gate and both directions of each shrine.
 * Existing classic skill save keys remain authoritative when present; their
 * current version-family skill counterpart supplies new-player progression.
 */
public final class CavernShrineBlock extends Block {
    public final CavernDeityBoss.Kind kind;
    public CavernShrineBlock(CavernDeityBoss.Kind kind,BlockBehaviour.Properties properties){super(properties);this.kind=kind;}
    private static int level(ServerPlayer player,String skill,String classic){
        var old=player.getPersistentData().getCompound(Player.PERSISTED_NBT_TAG);
        if(classic!=null&&old.contains(classic,3))return old.getInt(classic);
        if(skill.equals("hunter"))return 1;
        var definition=AoASkills.getSkill(new ResourceLocation("aoa3",skill));if(definition==null)throw new IllegalStateException("Missing canonical shrine skill "+skill);
        return PlayerUtil.getSkill(player,definition).getLevel(false);
    }
    @Override public InteractionResult use(BlockState state,Level world,BlockPos pos,Player player,InteractionHand hand,BlockHitResult hit){
        if(world.isClientSide||player.isCrouching()||!(player instanceof ServerPlayer server))return InteractionResult.sidedSuccess(world.isClientSide);
        if(!world.dimension().location().toString().equals("aoa3:ancient_cavern"))return InteractionResult.CONSUME;
        String skill=switch(kind){case CONIFERON->"imbuing";case HORON->"runation";case PENUMBRA->"hunter";case GOLDORTH->"foraging";};
        String old=switch(kind){case CONIFERON->"ILevel";case PENUMBRA->"HLevel";default->null;};
        if(level(server,"augury",null)<=70||level(server,skill,old)<=70){server.sendSystemMessage(Component.translatable("message.feedback.ancientCavernRequirement."+kind.deity+".levels"));return InteractionResult.CONSUME;}
        TributeResource tribute=TributeEvents.tribute(server);if(tribute==null)throw new IllegalStateException("Complete original tribute resource is required");
        var deity=switch(kind){case CONIFERON->TributeResource.Deities.Selyan;case HORON->TributeResource.Deities.Luxon;case PENUMBRA->TributeResource.Deities.Erebon;case GOLDORTH->TributeResource.Deities.Pluton;};
        if(tribute.getTribute(deity)!=200){server.sendSystemMessage(Component.translatable("message.feedback.ancientCavernRequirement."+kind.deity+".tribute"));return InteractionResult.CONSUME;}
        boolean inside=switch(kind){case CONIFERON->pos.getX()<-20&&pos.getZ()<-20;case HORON->pos.getX()>60&&pos.getZ()<-20;case PENUMBRA->pos.getX()<-20&&pos.getZ()>60;case GOLDORTH->pos.getX()>60&&pos.getZ()>60;};
        if(inside)server.teleportTo(0,17,0);
        else{
            int x=switch(kind){case CONIFERON->-60;case PENUMBRA->-70;default->80;};int z=switch(kind){case CONIFERON->-65;case HORON->-70;default->80;};
            server.teleportTo(x,18,z);CavernEncounterState.get(server.serverLevel()).trySpawn(server.serverLevel(),kind);
        }
        return InteractionResult.CONSUME;
    }
}
