package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.sounds.*;
import net.minecraft.world.*;
import net.minecraft.world.effect.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.attributes.*;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.Vec3;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;

/** Complete unique original Penumbra summon. This is the original creature's
 * own geometry/combat/rewards; it never substitutes another modern mob. */
public final class CavernHellspot extends Monster {
    public CavernHellspot(EntityType<? extends CavernHellspot> type,Level level){super(type,level);}
    public static AttributeSupplier.Builder attributes(){return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH,50).add(Attributes.ATTACK_DAMAGE,4).add(Attributes.FOLLOW_RANGE,52).add(Attributes.KNOCKBACK_RESISTANCE,.1).add(Attributes.MOVEMENT_SPEED,.8);}
    @Override protected void registerGoals(){
        goalSelector.addGoal(0,new FloatGoal(this));goalSelector.addGoal(2,new MeleeAttackGoal(this,1,false));goalSelector.addGoal(7,new WaterAvoidingRandomStrollGoal(this,1));goalSelector.addGoal(8,new LookAtPlayerGoal(this,Player.class,8));goalSelector.addGoal(8,new RandomLookAroundGoal(this));
        targetSelector.addGoal(1,new HurtByTargetGoal(this));
        targetSelector.addGoal(2,new NearestAttackableTargetGoal<Player>(this,Player.class,true){@Override protected double getFollowDistance(){return 16;}});
    }
    @Override protected SoundEvent getAmbientSound(){return CavernMissingDependencies.sound("hellspot_living");}
    @Override protected SoundEvent getHurtSound(DamageSource damage){return CavernMissingDependencies.sound("hellspot_hit");}
    @Override protected SoundEvent getDeathSound(){return CavernMissingDependencies.sound("hellspot_death");}
    @Override protected void playStepSound(BlockPos pos,BlockState state){playSound(SoundEvents.PIG_STEP,.55F,1);}
    @Override public boolean checkSpawnRules(LevelAccessor world,MobSpawnType reason){return world.getDifficulty()!=Difficulty.PEACEFUL;}
    @Override public boolean checkSpawnObstruction(LevelReader world){return world.isUnobstructed(this)&&!world.containsAnyLiquid(getBoundingBox());}
    @Override public boolean doHurtTarget(Entity target){boolean hit=super.doHurtTarget(target);if(hit&&!level().isClientSide&&target instanceof LivingEntity living)living.addEffect(new MobEffectInstance(MobEffects.BLINDNESS,150,2));return hit;}
    @Override public void aiStep(){
        super.aiStep();if(level().isClientSide)return;Player player=level().getNearestPlayer(this,15);if(!(player instanceof ServerPlayer server))return;
        Vec3 look=player.getViewVector(1).normalize(),toward=new Vec3(getX()-player.getX(),getBoundingBox().minY+getBbHeight()/2.0-player.getY()+player.getEyeHeight()/2.0,getZ()-player.getZ());double distance=toward.length();
        if(look.dot(toward.normalize())>1-.025/distance&&player.hasLineOfSight(this))server.teleportTo(getX(),getY(),getZ());
    }
    @Override protected void dropCustomDeathLoot(DamageSource source,int looting,boolean player){
        super.dropCustomDeathLoot(source,looting,player);spawnAtLocation(SnapshotEntityFamily.item("copper_coin"),5+random.nextInt(10));
        if(random.nextInt(2)==0)spawnAtLocation(CavernMissingDependencies.NETHER_GEMS.get(),3);
        if(random.nextInt(80)==34)spawnAtLocation(SnapshotEntityFamily.item("laser_blaster"));
        spawnAtLocation(SnapshotEntityFamily.item("copper_coin"),7);
    }
}
