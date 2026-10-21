package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.GameRules;
import net.minecraftforge.event.entity.living.*;
import net.minecraftforge.eventbus.api.*;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.items.ItemHandlerHelper;
import net.minecraftforge.registries.ForgeRegistries;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;
import net.tslat.aoa3.event.TributeEvents;
import net.tslat.aoa3.player.resource.TributeResource;
import net.tslat.aoa3.player.resource.TributeResource.Deities;

/** Full original dungeon kill-to-resource/reward chain on canonical mature
 * mobs. No second mob class or loot-table replacement is introduced. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.FORGE)
public final class ImmortallisRewards {
    private static String key(LivingEntity entity){var id=ForgeRegistries.ENTITY_TYPES.getKey(entity.getType());return id!=null&&id.getNamespace().equals("aoa3")?id.getPath():"";}
    private static ServerPlayer player(Entity attacker){
        if(attacker instanceof ServerPlayer player)return player;
        if(attacker instanceof TamableAnimal animal&&animal.getOwner() instanceof ServerPlayer owner)return owner;return null;
    }
    private static void give(ServerPlayer player,String item,int count){ItemHandlerHelper.giveItemToPlayer(player,new ItemStack(SnapshotEntityFamily.item(item),count));}
    private static boolean carrying(ServerPlayer player,String item){var value=SnapshotEntityFamily.item(item);return player.getInventory().items.stream().anyMatch(stack->stack.is(value));}
    private static void message(ServerPlayer player,String key){player.sendSystemMessage(Component.translatable("message.feedback.immortallisProgression."+key));}
    @SubscribeEvent(priority=EventPriority.LOWEST)
    public static void death(LivingDeathEvent event){
        if(event.isCanceled()||event.getEntity().level().isClientSide)return;
        ServerPlayer player=player(event.getSource().getEntity());if(player==null)return;
        String key=key(event.getEntity());
        if(!java.util.Set.of("goldum","goldus","skeledon","skelekyte","ghastus","urv","visage","flash").contains(key))return;
        TributeResource tribute=TributeEvents.tribute(player);if(tribute==null)throw new IllegalStateException("Complete original tribute resource is required");
        switch(key){
            case "goldum" -> {if(tribute.getTribute(Deities.Pluton)<100&&!carrying(player,"impure_gold"))give(player,"impure_gold",1);}
            case "goldus" -> {if(!carrying(player,"pure_gold"))give(player,"pure_gold",1);}
            case "skeledon","skelekyte" -> {if(tribute.getTribute(Deities.Erebon)<100)tribute.adjustTribute(Deities.Erebon,4);if(tribute.getTribute(Deities.Erebon)>=100)message(player,"skeletalSpiritsEnd");}
            case "ghastus","urv","visage" -> {tribute.adjustTribute(Deities.Erebon,4);if(tribute.getTribute(Deities.Erebon)==200)message(player,"evilSpiritsEnd");}
            case "flash" -> {
                message(player,"rewards");var random=event.getEntity().getRandom();
                if(ImmortallisProgression.isDungeon(event.getEntity().level()))give(player,"dungeon_tokens",7+random.nextInt(5));
                if(random.nextInt(3)==2){String[] armour={"archaic_leggings","archaic_boots","archaic_helmet","archaic_chestplate"};give(player,armour[random.nextInt(4)],1);}
            }
        }
        player.getInventory().setChanged();player.containerMenu.broadcastChanges();
    }
    @SubscribeEvent(priority=EventPriority.LOWEST)
    public static void drops(LivingDropsEvent event){
        if(event.isCanceled()||event.getEntity().level().isClientSide||!event.getEntity().level().getGameRules().getBoolean(GameRules.RULE_DOMOBLOOT))return;
        int stage=switch(key(event.getEntity())){case "klobber"->1;case "proshield"->2;case "mirage"->3;case "flash"->4;default->0;};if(stage==0)return;
        if(event.getDrops().stream().anyMatch(drop->ImmortallisProgression.matches(drop.getItem(),stage)))return;
        var actor=event.getEntity();ItemEntity reward=new ItemEntity(actor.level(),actor.getX(),actor.getY(),actor.getZ(),ImmortallisProgression.token(stage));reward.setDefaultPickUpDelay();event.getDrops().add(reward);
    }
    private ImmortallisRewards(){}
}
