package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.core.BlockPos;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.*;
import net.minecraft.sounds.*;
import net.minecraft.tags.DamageTypeTags;
import net.minecraft.world.BossEvent;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.effect.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.attributes.*;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.entity.monster.RangedAttackMob;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.entity.projectile.*;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.Vec3;
import net.tslat.aoa3.common.registration.block.AoABlocks;
import net.tslat.aoa3.common.registration.custom.AoAResources;
import net.tslat.aoa3.content.block.functional.misc.TrophyBlock;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotOverlayPacket;
import net.tslat.aoa3.util.PlayerUtil;

/** All four complete cavern combat roles, sharing native lifecycle ownership.
 * Original per-boss callbacks remain explicit. Native goals, authority checks,
 * synchronized velocity and save-aware encounters replace removed engine APIs.
 */
public final class CavernDeityBoss extends Monster implements RangedAttackMob {
    public enum Kind {
        CONIFERON(4F,5.5F,4000,25,52,.3,.8,"selyan",1.5F,-56,18,-52),
        GOLDORTH(2.2F,2.9F,3000,17,52,1,.10000000149011612,"pluton",1.2F,97,18,88),
        HORON(1.8F,2.3F,3000,24,52,.3,.8,"luxon",1.2F,95,18,-51),
        PENUMBRA(1.5F,3F,3000,15,16,0,.5,"erebon",1.5F,-51,18,92);
        public final float width,height,scale;public final double health,damage,range,resistance,speed;public final String deity;public final int x,y,z;
        Kind(float width,float height,double health,double damage,double range,double resistance,double speed,String deity,float scale,int x,int y,int z){this.width=width;this.height=height;this.health=health;this.damage=damage;this.range=range;this.resistance=resistance;this.speed=speed;this.deity=deity;this.scale=scale;this.x=x;this.y=y;this.z=z;}
        public String key(){return name().toLowerCase(java.util.Locale.ROOT);}
        public AttributeSupplier.Builder attributes(){return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH,health).add(Attributes.ATTACK_DAMAGE,damage).add(Attributes.FOLLOW_RANGE,range).add(Attributes.KNOCKBACK_RESISTANCE,resistance).add(Attributes.MOVEMENT_SPEED,speed);}
    }
    private final Kind kind;
    private final ServerBossEvent boss=new ServerBossEvent(getDisplayName(),BossEvent.BossBarColor.GREEN,BossEvent.BossBarOverlay.PROGRESS);
    public CavernDeityBoss(EntityType<? extends CavernDeityBoss> type,Level level,Kind kind){super(type,level);this.kind=kind;setPersistenceRequired();}
    public Kind kind(){return kind;}
    @Override protected void registerGoals(){
        goalSelector.addGoal(1,new FloatGoal(this));
        goalSelector.addGoal(2,new RestrictSunGoal(this){@Override public boolean canUse(){return kind==Kind.PENUMBRA&&super.canUse();}});
        goalSelector.addGoal(4,new MeleeAttackGoal(this,1,true){@Override public boolean canUse(){return kind!=Kind.PENUMBRA&&super.canUse();}@Override public boolean canContinueToUse(){return kind!=Kind.PENUMBRA&&super.canContinueToUse();}});
        goalSelector.addGoal(5,new RandomStrollGoal(this,.45));
        goalSelector.addGoal(6,new LookAtPlayerGoal(this,Player.class,8));goalSelector.addGoal(6,new RandomLookAroundGoal(this));
        goalSelector.addGoal(7,new RangedAttackGoal(this,1,20,64){@Override public boolean canUse(){return kind==Kind.PENUMBRA&&super.canUse();}@Override public boolean canContinueToUse(){return kind==Kind.PENUMBRA&&super.canContinueToUse();}});
        targetSelector.addGoal(1,new HurtByTargetGoal(this));
        targetSelector.addGoal(2,new NearestAttackableTargetGoal<Player>(this,Player.class,1,true,false,null){
            @Override protected double getFollowDistance(){return kind==Kind.GOLDORTH?32:16;}
            @Override protected net.minecraft.world.phys.AABB getTargetSearchArea(double range){return getBoundingBox().inflate(range,range,range);}
        });
    }
    @Override public boolean canChangeDimensions(){return false;}
    @Override public boolean removeWhenFarAway(double distance){return false;}
    @Override public boolean checkSpawnObstruction(LevelReader world){return !world.containsAnyLiquid(getBoundingBox())&&world.isUnobstructed(this)&&world.noCollision(this);}
    @Override protected SoundEvent getAmbientSound(){return CavernDeityFamily.sound(kind.key()+"_living");}
    @Override protected SoundEvent getHurtSound(DamageSource source){return CavernDeityFamily.sound(kind.key()+"_hit");}
    @Override protected SoundEvent getDeathSound(){return CavernDeityFamily.sound(kind.key()+"_death");}
    @Override protected void playStepSound(BlockPos pos,BlockState state){playSound(kind==Kind.HORON?CavernDeityFamily.sound("cavern_heavy_step"):SoundEvents.PIG_STEP,kind==Kind.HORON?.85F:.55F,1);}
    @Override public void aiStep(){
        super.aiStep();if(level().isClientSide||!isAlive())return;
        if(kind==Kind.CONIFERON){
            Player player=level().getNearestPlayer(this,30);if(player==null||player.distanceTo(this)>30)return;
            if(random.nextInt(150)==37){
                playSound(CavernDeityFamily.sound("coniferon_spawn"),1.85F,1);player.addEffect(new MobEffectInstance(MobEffects.POISON,60,0));
                if(player instanceof ServerPlayer server)SnapshotOverlayPacket.send(server,70,9);
            }
            player.push(Math.signum(getX()-player.getX())*.029,0,Math.signum(getZ()-player.getZ())*.029);player.hurtMarked=true;
            if(random.nextInt(250)==137)player.teleportTo(getX(),getY(),getZ());
        }else if(kind==Kind.GOLDORTH){
            Player player=level().getNearestPlayer(this,20);if(player!=null&&player.distanceTo(this)<=20&&random.nextInt(250)==137)player.teleportTo(getX(),getY(),getZ());
        }else if(kind==Kind.HORON){
            // Original createExplosion(...,false) damages actors but does not
            // destroy blocks. Native NONE preserves that distinction.
            if(random.nextInt(60)==13)level().explode(this,getX(),getY(),getZ(),2,false,Level.ExplosionInteraction.NONE);
            if(random.nextInt(400)==35){Player player=level().getNearestPlayer(this,64);if(player!=null){teleportTo(player.getX(),player.getY(),player.getZ());player.addEffect(new MobEffectInstance(MobEffects.WEAKNESS,120,3));}}
        }
    }
    @Override public boolean doHurtTarget(Entity target){
        boolean hit=super.doHurtTarget(target);if(!hit||level().isClientSide)return hit;
        if(kind==Kind.CONIFERON){
            // Repair the old cast of attackTarget: the actual hit recipient is
            // the knockback-resistance owner, including multiplayer targets.
            if(target instanceof Player player&&player.getAttributeValue(Attributes.KNOCKBACK_RESISTANCE)!=1){Vec3 motion=getDeltaMovement();target.push(motion.x*10.5,motion.y*.5,motion.z*22);target.hurtMarked=true;}
            // Original EntityLiving excludes players (EntityLivingBase).
            if(target instanceof Mob mob)mob.addEffect(new MobEffectInstance(MobEffects.MOVEMENT_SLOWDOWN,140,2));
        }else if(kind==Kind.HORON&&target instanceof ServerPlayer player){
            PlayerUtil.getResource(player,AoAResources.ENERGY.get()).consume(60,true);
            PlayerUtil.getResource(player,AoAResources.CREATION.get()).consume(600,true);
            PlayerUtil.getResource(player,AoAResources.SOUL_POWER.get()).consume(2000,true);
        }
        return true;
    }
    @Override public boolean hurt(DamageSource source,float amount){
        if(!level().isClientSide&&kind==Kind.HORON&&(source.is(DamageTypeTags.IS_PROJECTILE)||source.getDirectEntity() instanceof AbstractArrow||source.getDirectEntity() instanceof ThrowableProjectile)&&random.nextInt(3)==2)return false;
        return super.hurt(source,amount);
    }
    @Override public void performRangedAttack(LivingEntity target,float power){
        if(kind!=Kind.PENUMBRA||level().isClientSide)return;
        CavernPenumbraShot shot=new CavernPenumbraShot(level(),this);double dx=target.getX()-getX(),dz=target.getZ()-getZ(),dy=target.getY()+target.getEyeHeight()-1.1F-shot.getY();
        shot.shoot(dx,dy+(float)Math.sqrt(dx*dx+dz*dz)*.2F,dz,1.6F,12);
        playSound(CavernDeityFamily.sound("penumbra_fire"),1,1/(random.nextFloat()*.4F+.8F));level().addFreshEntity(shot);
    }
    @Override protected void dropCustomDeathLoot(DamageSource source,int looting,boolean player){
        super.dropCustomDeathLoot(source,looting,player);
        if(random.nextInt(10)==4)spawnAtLocation(SnapshotEntityFamily.item(kind.deity+"_scythe"));
        if(random.nextInt(10)==4)spawnAtLocation(SnapshotEntityFamily.item(kind.deity+"_stickler"));
        if(random.nextInt(5)==3)spawnAtLocation(SnapshotEntityFamily.item(kind.deity+"_banner"));
        if(random.nextInt(5)==3){ItemStack trophy=new ItemStack(AoABlocks.TROPHY.get());trophy.setTag(TrophyBlock.getOriginalTrophyTag(getType(),AoABlocks.TROPHY.get()));spawnAtLocation(trophy);}
    }
    @Override public void tick(){super.tick();if(!level().isClientSide){boss.setProgress(getHealth()/getMaxHealth());if(tickCount%20==0&&level() instanceof ServerLevel world)CavernEncounterState.note(world,this);}}
    @Override public void die(DamageSource source){super.die(source);if(level() instanceof ServerLevel world)CavernEncounterState.died(world,this);}
    @Override public void remove(RemovalReason reason){if((reason==RemovalReason.KILLED||reason==RemovalReason.DISCARDED)&&level() instanceof ServerLevel world&&kind!=null)CavernEncounterState.died(world,this);super.remove(reason);}
    @Override public void startSeenByPlayer(ServerPlayer player){super.startSeenByPlayer(player);boss.addPlayer(player);}
    @Override public void stopSeenByPlayer(ServerPlayer player){super.stopSeenByPlayer(player);boss.removePlayer(player);}
    @Override public void setCustomName(Component name){super.setCustomName(name);if(boss!=null)boss.setName(getDisplayName());}
    @Override public void readAdditionalSaveData(CompoundTag tag){super.readAdditionalSaveData(tag);boss.setName(getDisplayName());}
    @Override public void travel(Vec3 input){
        if(kind!=Kind.GOLDORTH){super.travel(input);return;}
        // Complete Goldorth's authored constant-friction travel, rather than
        // replacing its 1.6 movement callback with the .1 attribute default.
        if(isInWater()||isInLava()){
            boolean water=isInWater();double oldY=getY();moveRelative(water?.52F:.02F,input);move(MoverType.SELF,getDeltaMovement());setDeltaMovement(getDeltaMovement().scale(water?.8F:.5).add(0,-.02,0));
            Vec3 motion=getDeltaMovement();if(horizontalCollision&&isFree(motion.x,motion.y+.6F-getY()+oldY,motion.z))setDeltaMovement(motion.x,.3F,motion.z);
        }else{
            float friction=.91F,factor=.16277136F/(friction*friction*friction);moveRelative(onGround()?1.6F*factor:.02F,input);Vec3 motion=getDeltaMovement();
            if(onClimbable()){motion=new Vec3(Math.max(-.15F,Math.min(.15F,motion.x)),Math.max(-.15,motion.y),Math.max(-.15F,Math.min(.15F,motion.z)));fallDistance=0;}
            setDeltaMovement(motion);move(MoverType.SELF,motion);motion=getDeltaMovement();if(horizontalCollision&&onClimbable())motion=new Vec3(motion.x,.2,motion.z);
            double y=motion.y-.08;if(level().isClientSide&&!level().hasChunkAt(blockPosition()))y=getY()>0?-.1:0;
            setDeltaMovement(motion.x*friction,y*.98F,motion.z*friction);
        }
        calculateEntityAnimation(false);
    }
}
