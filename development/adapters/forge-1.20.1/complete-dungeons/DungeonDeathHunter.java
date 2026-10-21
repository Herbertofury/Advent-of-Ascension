package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.core.BlockPos;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.*;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.attributes.*;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.state.BlockState;

/** Original Death Day creature, including its complete push/pull program. */
public final class DungeonDeathHunter extends Monster {
    public DungeonDeathHunter(EntityType<? extends DungeonDeathHunter> type,Level level){super(type,level);}
    public static AttributeSupplier.Builder attributes(){return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH,200).add(Attributes.ATTACK_DAMAGE,6).add(Attributes.FOLLOW_RANGE,52).add(Attributes.KNOCKBACK_RESISTANCE,.1).add(Attributes.MOVEMENT_SPEED,.8);}
    @Override protected void registerGoals(){
        goalSelector.addGoal(0,new FloatGoal(this));goalSelector.addGoal(2,new MeleeAttackGoal(this,1,false));goalSelector.addGoal(7,new WaterAvoidingRandomStrollGoal(this,1));goalSelector.addGoal(8,new LookAtPlayerGoal(this,Player.class,8));goalSelector.addGoal(8,new RandomLookAroundGoal(this));
        targetSelector.addGoal(1,new HurtByTargetGoal(this));targetSelector.addGoal(2,new NearestAttackableTargetGoal<Player>(this,Player.class,true){@Override protected double getFollowDistance(){return 16;}});
    }
    @Override protected SoundEvent getAmbientSound(){return DungeonMissingDependencies.sound("death_hunter_living");}
    @Override protected SoundEvent getHurtSound(DamageSource damage){return DungeonMissingDependencies.sound("death_hunter_hit");}
    @Override protected SoundEvent getDeathSound(){return DungeonMissingDependencies.sound("death_hunter_death");}
    @Override protected void playStepSound(BlockPos pos,BlockState state){playSound(DungeonMissingDependencies.sound("death_hunter_step"),2,1);}
    @Override public boolean checkSpawnRules(LevelAccessor world,MobSpawnType reason){return world.getDifficulty()!=Difficulty.PEACEFUL&&world instanceof ServerLevelAccessor server&&DungeonDeathDay.isDeadly(server.getLevel());}
    @Override public boolean checkSpawnObstruction(LevelReader world){return world.isUnobstructed(this)&&!world.containsAnyLiquid(getBoundingBox());}
    @Override public void aiStep(){
        super.aiStep();if(level().isClientSide)return;
        var players=level().getEntitiesOfClass(Player.class,getBoundingBox().inflate(15),p->!p.isCreative()&&!p.isSpectator());
        if(random.nextInt(200)==15)for(Player player:players){player.push(Math.signum(player.getX()-getX())*3.049,0,Math.signum(player.getZ()-getZ())*3.049);player.hurtMarked=true;playSound(getAmbientSound(),4,1/(random.nextFloat()*.4F+.8F));}
        for(Player player:players){player.push(Math.signum(getX()-player.getX())*.049,(double).07F,Math.signum(getZ()-player.getZ())*.049);player.fallDistance=-.5F;player.hurtMarked=true;}
    }
}
