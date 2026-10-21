package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.ChatFormatting;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.saveddata.SavedData;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Original 480..12400 Death Day, one 1/25 roll per day. Server/world-owned
 * saved state repairs the old global static/restart leak and repeated rolls
 * when daylight time is frozen at exactly 480. No unrelated event is replaced. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.FORGE)
public final class DungeonDeathDay extends SavedData {
    private long lastRollDay=Long.MIN_VALUE,eventDay=Long.MIN_VALUE;private boolean deadly;
    public static DungeonDeathDay load(CompoundTag tag){var data=new DungeonDeathDay();data.lastRollDay=tag.contains("LastRollDay")?tag.getLong("LastRollDay"):Long.MIN_VALUE;data.eventDay=tag.contains("EventDay")?tag.getLong("EventDay"):Long.MIN_VALUE;data.deadly=tag.getBoolean("Deadly");return data;}
    @Override public CompoundTag save(CompoundTag tag){tag.putLong("LastRollDay",lastRollDay);tag.putLong("EventDay",eventDay);tag.putBoolean("Deadly",deadly);return tag;}
    public static DungeonDeathDay get(ServerLevel level){return level.getServer().overworld().getDataStorage().computeIfAbsent(DungeonDeathDay::load,DungeonDeathDay::new,"aoa3_death_day");}
    public static boolean isDeadly(ServerLevel level){var overworld=level.getServer().overworld();long time=overworld.getDayTime(),day=Math.floorDiv(time,24000),within=Math.floorMod(time,24000);var data=get(overworld);return data.deadly&&data.eventDay==day&&within>=480&&within<12400;}
    @SubscribeEvent public static void tick(TickEvent.LevelTickEvent event){
        if(event.phase!=TickEvent.Phase.END||!(event.level instanceof ServerLevel level)||level.dimension()!=Level.OVERWORLD)return;
        var data=get(level);long time=level.getDayTime(),day=Math.floorDiv(time,24000),within=Math.floorMod(time,24000);
        if(data.deadly&&(data.eventDay!=day||within<480||within>=12400)){
            if(data.eventDay==day&&within==12400)for(var player:level.players())player.sendSystemMessage(Component.translatable("message.event.deathDayEnd").withStyle(ChatFormatting.RED));
            data.deadly=false;data.setDirty();
        }
        if(within==480&&data.lastRollDay!=day){data.lastRollDay=day;data.eventDay=day;data.deadly=level.random.nextInt(25)==12;data.setDirty();if(data.deadly)for(var player:level.players()){player.sendSystemMessage(Component.translatable("message.event.deathDayStart").withStyle(ChatFormatting.RED));level.playSound(null,player.blockPosition(),DungeonMissingDependencies.sound("death_day"),SoundSource.AMBIENT,3.85F,1);}}
    }
}
