package net.tslat.aoa3.content.entity.cavern;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.network.protocol.Packet;
import net.minecraft.network.protocol.game.ClientGamePacketListener;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.projectile.ThrowableProjectile;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.*;
import net.minecraftforge.network.NetworkHooks;
import net.minecraftforge.registries.ForgeRegistries;

/** Original four-damage shot, all eight summon outcomes and full black trail.
 * The old constructor ignores its dmg argument; eighteen is not the damage.
 * Save/sync and server-only mutation repair the removed throwable ABI.
 */
public final class CavernPenumbraShot extends ThrowableProjectile {
    private float damage=4;private int age,color=1;
    public CavernPenumbraShot(EntityType<? extends CavernPenumbraShot> type,Level level){super(type,level);}
    public CavernPenumbraShot(Level level,LivingEntity owner){super(CavernDeityFamily.SHOT.get(),owner,level);}
    @Override protected void defineSynchedData(){}
    @Override protected float getGravity(){return .075F;}
    @Override protected void onHit(HitResult hit){
        super.onHit(hit);if(level().isClientSide)return;
        if(hit instanceof EntityHitResult collision&&collision.getEntity() instanceof LivingEntity living){
            living.hurt(damageSources().thrown(this,getOwner()),damage);
            String[] choices={"occulent","alarmo","shifter","devourer","basilisk","apparition","stalker","hellspot"};String key=choices[random.nextInt(8)];
            EntityType<?> type=ForgeRegistries.ENTITY_TYPES.getValue(new ResourceLocation("aoa3",key));
            if(type==null)throw new IllegalStateException("Missing original Penumbra summon "+key);
            Entity mob=type.create(level());if(mob==null)throw new IllegalStateException("Original Penumbra summon factory returned null");mob.setPos(getX(),getY(),getZ());level().addFreshEntity(mob);
        }
        discard();
    }
    @Override public void tick(){super.tick();if(age==40){if(!level().isClientSide)discard();}else age++;}
    @Override public void baseTick(){super.baseTick();if(level().isClientSide&&!isRemoved())CavernDeityClient.trail(this);}
    @Override public void addAdditionalSaveData(CompoundTag tag){super.addAdditionalSaveData(tag);tag.putFloat("CavernDamage",damage);tag.putInt("CavernAge",age);tag.putInt("CavernColor",color);}
    @Override public void readAdditionalSaveData(CompoundTag tag){super.readAdditionalSaveData(tag);damage=tag.contains("CavernDamage")?tag.getFloat("CavernDamage"):4;age=tag.getInt("CavernAge");color=tag.contains("CavernColor")?tag.getInt("CavernColor"):1;}
    @Override public Packet<ClientGamePacketListener> getAddEntityPacket(){return NetworkHooks.getEntitySpawningPacket(this);}
}
