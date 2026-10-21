package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.core.BlockPos;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.syncher.*;
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
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;

/** Unique original five-colour creature, not a substitute for another mob.
 * Colour now survives save/reload and is synchronized to every client. */
public final class DungeonAutomaton extends Monster {
    private static final EntityDataAccessor<Integer> COLOUR=SynchedEntityData.defineId(DungeonAutomaton.class,EntityDataSerializers.INT);
    public DungeonAutomaton(EntityType<? extends DungeonAutomaton> type,Level level){super(type,level);if(!level.isClientSide)setColour(1+random.nextInt(5));}
    public static AttributeSupplier.Builder attributes(){return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH,80).add(Attributes.ATTACK_DAMAGE,10).add(Attributes.FOLLOW_RANGE,52).add(Attributes.KNOCKBACK_RESISTANCE,1).add(Attributes.MOVEMENT_SPEED,1);}
    @Override protected void defineSynchedData(){super.defineSynchedData();entityData.define(COLOUR,1);}
    public int colour(){return entityData.get(COLOUR);}
    public void setColour(int colour){if(colour<1||colour>5)throw new IllegalArgumentException("Original Automaton colour is 1..5");entityData.set(COLOUR,colour);}
    @Override protected void registerGoals(){
        goalSelector.addGoal(0,new FloatGoal(this));goalSelector.addGoal(2,new MeleeAttackGoal(this,1,false));goalSelector.addGoal(7,new WaterAvoidingRandomStrollGoal(this,1));goalSelector.addGoal(8,new LookAtPlayerGoal(this,Player.class,8));goalSelector.addGoal(8,new RandomLookAroundGoal(this));
        targetSelector.addGoal(1,new HurtByTargetGoal(this));targetSelector.addGoal(2,new NearestAttackableTargetGoal<Player>(this,Player.class,true){@Override protected double getFollowDistance(){return 16;}});
    }
    @Override protected SoundEvent getAmbientSound(){return DungeonMissingDependencies.sound("automaton_living");}
    @Override protected SoundEvent getHurtSound(DamageSource damage){return DungeonMissingDependencies.sound("automaton_hit");}
    @Override protected SoundEvent getDeathSound(){return DungeonMissingDependencies.sound("automaton_death");}
    @Override protected void playStepSound(BlockPos pos,BlockState state){playSound(DungeonMissingDependencies.sound("automaton_step"),.55F,1);}
    @Override public boolean checkSpawnRules(LevelAccessor world,MobSpawnType reason){return world.getDifficulty()!=Difficulty.PEACEFUL;}
    @Override public boolean checkSpawnObstruction(LevelReader world){return world.isUnobstructed(this)&&!world.containsAnyLiquid(getBoundingBox());}
    @Override public boolean doHurtTarget(Entity target){boolean hit=super.doHurtTarget(target);if(hit&&target instanceof LivingEntity living&&living.getAttributeValue(Attributes.KNOCKBACK_RESISTANCE)!=1){var motion=getDeltaMovement();target.push(motion.x*7.5,motion.y*.5,motion.z*7);}return hit;}
    @Override public void addAdditionalSaveData(CompoundTag tag){super.addAdditionalSaveData(tag);tag.putInt("AutomatonColour",colour());}
    @Override public void readAdditionalSaveData(CompoundTag tag){super.readAdditionalSaveData(tag);if(tag.contains("AutomatonColour"))setColour(tag.getInt("AutomatonColour"));}
    @Override protected void dropCustomDeathLoot(DamageSource source,int looting,boolean player){
        super.dropCustomDeathLoot(source,looting,player);spawnAtLocation(SnapshotEntityFamily.item("copper_coin"),5+random.nextInt(10));
        if(random.nextInt(40)==17)spawnAtLocation(DungeonMissingDependencies.ANCIENT_CAVERN_STONE.get(),2);
        if(random.nextInt(7)==0)spawnAtLocation(SnapshotEntityFamily.item("utopian_banner"));
        if(random.nextInt(50)==34)spawnAtLocation(SnapshotEntityFamily.item(new String[]{"germinator","dragilator","krilinator","frosticator","electinator"}[colour()-1]));
    }
}
