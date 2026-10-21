package net.tslat.aoa3.content.entity.cavern;

import java.util.*;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.levelgen.Heightmap;
import net.minecraftforge.common.ForgeSpawnEggItem;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.*;

/** Missing unique dependencies join the same native cohort and registry. */
public final class CavernMissingDependencies {
    private static final DeferredRegister<EntityType<?>> ENTITIES=DeferredRegister.create(ForgeRegistries.ENTITY_TYPES,"aoa3");
    private static final DeferredRegister<Item> ITEMS=DeferredRegister.create(ForgeRegistries.ITEMS,"aoa3");
    private static final DeferredRegister<SoundEvent> SOUNDS=DeferredRegister.create(ForgeRegistries.SOUND_EVENTS,"aoa3");
    public static final RegistryObject<EntityType<CavernHellspot>> HELLSPOT=ENTITIES.register("hellspot",()->EntityType.Builder.<CavernHellspot>of(CavernHellspot::new,MobCategory.MONSTER).sized(.97F,1.2F).fireImmune().clientTrackingRange(10).updateInterval(3).build("aoa3:hellspot"));
    public static final RegistryObject<Item> NETHER_GEMS=ITEMS.register("nether_gems",()->new Item(new Item.Properties()));
    public static final RegistryObject<Item> HELLSPOT_EGG=ITEMS.register("hellspot_spawn_egg",()->new ForgeSpawnEggItem(HELLSPOT,0x531b12,0xe9b155,new Item.Properties()));
    static{for(String key:List.of("hellspot_living","hellspot_hit","hellspot_death"))SOUNDS.register(key,()->SoundEvent.createVariableRangeEvent(CavernDeityFamily.id(key)));}
    public static SoundEvent sound(String key){return Objects.requireNonNull(ForgeRegistries.SOUND_EVENTS.getValue(CavernDeityFamily.id(key)));}
    public static void init(IEventBus bus){
        ENTITIES.register(bus);ITEMS.register(bus);SOUNDS.register(bus);
        bus.addListener((EntityAttributeCreationEvent event)->event.put(HELLSPOT.get(),CavernHellspot.attributes().build()));
        bus.addListener((BuildCreativeModeTabContentsEvent event)->{if(event.getTabKey().equals(CreativeModeTabs.SPAWN_EGGS))event.accept(HELLSPOT_EGG.get());if(event.getTabKey().equals(CreativeModeTabs.INGREDIENTS))event.accept(NETHER_GEMS.get());});
        bus.addListener((net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent event)->event.enqueueWork(()->SpawnPlacements.register(HELLSPOT.get(),SpawnPlacements.Type.NO_RESTRICTIONS,Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,(type,world,reason,pos,random)->world.getDifficulty()!=net.minecraft.world.Difficulty.PEACEFUL)));
    }
    private CavernMissingDependencies(){}
}
