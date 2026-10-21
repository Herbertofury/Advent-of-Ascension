package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.entity.living.LivingDestroyBlockEvent;
import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.event.level.*;

/** The original immovable dungeon shell is scoped to authored cells in these
 * worlds. Canonical blocks keep their normal behavior everywhere else. Native
 * Forge hooks, creative editing and already modified cells remain available.
 */
public final class DungeonRealmProtection {
    private static boolean protects(LevelAccessor level,BlockPos pos,BlockState state){
        return level instanceof ServerLevel server&&server.getChunkSource().getGenerator() instanceof LiteralDungeonChunkGenerator generator&&generator.protects(pos,state);
    }
    public static void init(){
        MinecraftForge.EVENT_BUS.addListener((BlockEvent.BreakEvent event)->{if(!event.getPlayer().isCreative()&&protects(event.getLevel(),event.getPos(),event.getState()))event.setCanceled(true);});
        MinecraftForge.EVENT_BUS.addListener((PlayerEvent.BreakSpeed event)->{if(!event.getEntity().isCreative()&&event.getPosition().isPresent()&&protects(event.getEntity().level(),event.getPosition().get(),event.getState()))event.setNewSpeed(0);});
        MinecraftForge.EVENT_BUS.addListener((ExplosionEvent.Detonate event)->event.getAffectedBlocks().removeIf(pos->protects(event.getLevel(),pos,event.getLevel().getBlockState(pos))));
        MinecraftForge.EVENT_BUS.addListener((LivingDestroyBlockEvent event)->{if(protects(event.getEntity().level(),event.getPos(),event.getState()))event.setCanceled(true);});
        MinecraftForge.EVENT_BUS.addListener((PistonEvent.Pre event)->{
            var helper=event.getStructureHelper();if(!helper.resolve())return;
            for(BlockPos pos:helper.getToPush())if(protects(event.getLevel(),pos,event.getLevel().getBlockState(pos))){event.setCanceled(true);return;}
            for(BlockPos pos:helper.getToDestroy())if(protects(event.getLevel(),pos,event.getLevel().getBlockState(pos))){event.setCanceled(true);return;}
        });
    }
    private DungeonRealmProtection(){}
}
