package net.tslat.aoa3.content.entity.cavern;

import java.util.Set;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.GameRules;
import net.minecraftforge.event.entity.living.*;
import net.minecraftforge.eventbus.api.*;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.registries.ForgeRegistries;
import net.tslat.aoa3.event.TributeEvents;
import net.tslat.aoa3.player.resource.TributeResource.Deities;
import net.tslat.aoa3.common.registration.worldgen.AoADimensions;

/** Add absent original access/tribute rewards to existing canonical mobs.
 * Their newer attacks, models, loot tables and existing drops stay intact. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.FORGE)
public final class DungeonAcquisition {
    @SubscribeEvent(priority=EventPriority.LOWEST) public static void death(LivingDeathEvent event){
        var actor=event.getEntity();if(event.isCanceled()||actor.level().isClientSide||actor.level().dimension()!=AoADimensions.ANCIENT_CAVERN.key||!(event.getSource().getEntity() instanceof ServerPlayer player))return;
        var id=ForgeRegistries.ENTITY_TYPES.getKey(actor.getType());if(id==null||!id.getNamespace().equals("aoa3"))return;
        Deities deity=switch(id.getPath()){case "automaton"->Deities.Luxon;case "bloodsucker"->Deities.Erebon;case "rock_critter"->Deities.Pluton;case "flowerface"->Deities.Selyan;default->null;};
        if(deity!=null){var tribute=TributeEvents.tribute(player);if(tribute==null)throw new IllegalStateException("Missing complete dungeon tribute resource");tribute.adjustTribute(deity,8);}
    }
    @SubscribeEvent(priority=EventPriority.LOWEST) public static void drops(LivingDropsEvent event){
        var actor=event.getEntity();if(event.isCanceled()||actor.level().isClientSide||!actor.level().getGameRules().getBoolean(GameRules.RULE_DOMOBLOOT))return;
        var id=ForgeRegistries.ENTITY_TYPES.getKey(actor.getType());if(id==null||!id.getNamespace().equals("aoa3"))return;
        ItemStack result=ItemStack.EMPTY;
        if(Set.of("bloodsucker","rock_critter","flowerface").contains(id.getPath())&&actor.getRandom().nextInt(40)==17)result=new ItemStack(DungeonMissingDependencies.ANCIENT_CAVERN_STONE.get(),2);
        if(id.getPath().equals("death_hunter"))result=new ItemStack(DungeonMissingDependencies.IMMORTALLIS_STONE.get());
        if(!result.isEmpty()){ItemStack selected=result;if(event.getDrops().stream().noneMatch(drop->drop.getItem().is(selected.getItem())))event.getDrops().add(new ItemEntity(actor.level(),actor.getX(),actor.getY(),actor.getZ(),result));}
    }
    private DungeonAcquisition(){}
}
