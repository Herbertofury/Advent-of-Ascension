package net.tslat.aoa3.event;

import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.projectile.Projectile;
import net.minecraft.world.entity.TamableAnimal;
import net.tslat.aoa3.player.skill.HunterSkill;
import net.minecraftforge.event.entity.living.LivingDropsEvent;
import net.minecraftforge.event.entity.living.LivingAttackEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.eventbus.api.EventPriority;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.registries.ForgeRegistries;
import net.tslat.aoa3.common.registration.AoAConfigs;
import net.tslat.aoa3.common.registration.custom.AoASkills;
import net.tslat.aoa3.player.skill.HunterProgression;
import net.tslat.aoa3.util.PlayerUtil;

/** The full source-bound active Hunter reward/gate table is generated from
 * complete original native/instruction captures. No per-frame scans or IO.
 * Existing newer creature AI, models, IDs and non-player damage remain owned
 * by their current implementations. The explicit disableSkills choice wins.
 */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.FORGE)
public final class HunterCombat {
    private HunterCombat(){}
    public static ServerPlayer player(Entity owner){
        if(owner instanceof ServerPlayer p)return p;
        if(owner instanceof TamableAnimal pet&&pet.getOwner() instanceof ServerPlayer p)return p;
        if(owner instanceof Projectile projectile){
            Entity parent=projectile.getOwner();
            if(parent instanceof ServerPlayer p)return p;
            if(parent instanceof TamableAnimal pet&&pet.getOwner() instanceof ServerPlayer p)return p;
        }
        return null;
    }
    public static ServerPlayer player(DamageSource source){
        ServerPlayer player=player(source.getEntity());return player!=null?player:player(source.getDirectEntity());
    }
    public static boolean historical(ServerPlayer player){return PlayerUtil.getSkill(player,AoASkills.HUNTER.get()) instanceof HunterSkill hunter&&hunter.historicalProgression();}
    public static int requiredLevel(ServerPlayer player,LivingEntity victim){
        if(historical(player)){
            var policy=HunterEntityPolicies.get(ForgeRegistries.ENTITY_TYPES.getKey(victim.getType()));
            return policy==null?-1:policy.requiredLevel();
        }
        var policy=HunterModernPolicies.get(victim);return policy==null?-1:policy.requiredLevel();
    }
    public static boolean canDamage(ServerPlayer player,LivingEntity victim){
        if(AoAConfigs.SERVER.disableSkills.get())return true;
        int required=requiredLevel(player,victim);if(required<0)return true;
        var skill=PlayerUtil.getSkill(player,AoASkills.HUNTER.get());
        if(skill==AoASkills.DEFAULT)return true;
        return player.isCreative()||skill.getLevel(false)>=required;
    }
    @SubscribeEvent(priority=EventPriority.HIGH)
    public static void attack(LivingAttackEvent event){
        ServerPlayer player=player(event.getSource());
        if(player==null||canDamage(player,event.getEntity()))return;
        event.setCanceled(true);
        player.displayClientMessage(Component.translatable("message.feedback.hunterRequirement",requiredLevel(player,event.getEntity())),true);
    }
    @SubscribeEvent(priority=EventPriority.LOWEST)
    public static void death(LivingDeathEvent event){
        if(event.isCanceled()||AoAConfigs.SERVER.disableSkills.get())return;
        ServerPlayer player=player(event.getSource());if(player==null)return;
        float reward;
        if(historical(player)){
            var policy=HunterEntityPolicies.get(ForgeRegistries.ENTITY_TYPES.getKey(event.getEntity().getType()));reward=policy==null?0:policy.reward();
        }else{var policy=HunterModernPolicies.get(event.getEntity());reward=policy==null?0:policy.reward();}
        if(reward>0)PlayerUtil.giveXpToPlayer(player,AoASkills.HUNTER.get(),reward,false);
    }
    @SubscribeEvent(priority=EventPriority.LOWEST)
    public static void drops(LivingDropsEvent event){
        if(event.isCanceled()||AoAConfigs.SERVER.disableSkills.get()||HunterModernPolicies.get(event.getEntity())==null)return;
        // Retain the later release's separate loot qualification. Owned pets
        // credit XP but do not turn an unqualified death into player loot.
        Entity attacker=event.getSource().getEntity();
        if(attacker instanceof ServerPlayer player&&historical(player))return;
        if(!(attacker instanceof ServerPlayer player)||!event.isRecentlyHit()||!canDamage(player,event.getEntity())){
            event.getDrops().clear();event.setCanceled(true);
        }
    }
}
