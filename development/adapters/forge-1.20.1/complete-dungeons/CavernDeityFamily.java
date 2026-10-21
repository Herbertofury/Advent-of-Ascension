package net.tslat.aoa3.content.entity.cavern;

import java.util.*;
import net.minecraft.core.particles.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraftforge.common.ForgeSpawnEggItem;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.*;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;

/** Complete shared entity/projectile/sound/particle registration cohort. */
public final class CavernDeityFamily {
    private static final DeferredRegister<EntityType<?>> ENTITIES=DeferredRegister.create(ForgeRegistries.ENTITY_TYPES,"aoa3");
    private static final DeferredRegister<Item> ITEMS=DeferredRegister.create(ForgeRegistries.ITEMS,"aoa3");
    private static final DeferredRegister<SoundEvent> SOUNDS=DeferredRegister.create(ForgeRegistries.SOUND_EVENTS,"aoa3");
    private static final DeferredRegister<ParticleType<?>> PARTICLES=DeferredRegister.create(ForgeRegistries.PARTICLE_TYPES,"aoa3");
    public static final RegistryObject<SimpleParticleType> BLACK_TRAIL=PARTICLES.register("cavern_black_trail",()->new SimpleParticleType(true));
    public static final Map<CavernDeityBoss.Kind,RegistryObject<EntityType<CavernDeityBoss>>> BOSSES=new EnumMap<>(CavernDeityBoss.Kind.class);
    private static final List<RegistryObject<Item>> EGGS=new ArrayList<>();
    static {
        for(var kind:CavernDeityBoss.Kind.values()){
            var type=ENTITIES.register(kind.key(),()->EntityType.Builder.<CavernDeityBoss>of((entity,level)->new CavernDeityBoss(entity,level,kind),MobCategory.MONSTER).sized(kind.width,kind.height).clientTrackingRange(16).updateInterval(1).build("aoa3:"+kind.key()));BOSSES.put(kind,type);
            EGGS.add(ITEMS.register(kind.key()+"_spawn_egg",()->new ForgeSpawnEggItem(type,0x303030,0x999999,new Item.Properties())));
            for(String event:List.of("living","hit","death")){String key=kind.key()+"_"+event;SOUNDS.register(key,()->SoundEvent.createVariableRangeEvent(id(key)));}
        }
        for(String key:List.of("coniferon_spawn","penumbra_fire","cavern_heavy_step"))SOUNDS.register(key,()->SoundEvent.createVariableRangeEvent(id(key)));
    }
    public static final RegistryObject<EntityType<CavernPenumbraShot>> SHOT=ENTITIES.register("penumbra_shot",()->EntityType.Builder.<CavernPenumbraShot>of(CavernPenumbraShot::new,MobCategory.MISC).sized(.25F,.25F).clientTrackingRange(15).updateInterval(3).build("aoa3:penumbra_shot"));
    public static ResourceLocation id(String key){return new ResourceLocation("aoa3",key);}
    public static SoundEvent sound(String key){return Objects.requireNonNull(ForgeRegistries.SOUND_EVENTS.getValue(id(key)),"Missing complete cavern sound "+key);}
    public static void init(IEventBus bus){
        ENTITIES.register(bus);ITEMS.register(bus);SOUNDS.register(bus);PARTICLES.register(bus);
        bus.addListener((EntityAttributeCreationEvent event)->BOSSES.forEach((kind,type)->event.put(type.get(),kind.attributes().build())));
        bus.addListener((BuildCreativeModeTabContentsEvent event)->{if(event.getTabKey().equals(CreativeModeTabs.SPAWN_EGGS))EGGS.forEach(egg->event.accept(egg.get()));});
        bus.addListener((net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent event)->event.enqueueWork(()->{
            for(var kind:CavernDeityBoss.Kind.values())for(String suffix:List.of("_scythe","_stickler","_banner"))SnapshotEntityFamily.item(kind.deity+suffix);
            for(String key:List.of("occulent","alarmo","shifter","devourer","basilisk","apparition","stalker","hellspot"))if(!ForgeRegistries.ENTITY_TYPES.containsKey(id(key)))throw new IllegalStateException("Missing complete Penumbra summon "+key);
        }));
    }
    private CavernDeityFamily(){}
}
