package net.tslat.aoa3.content.entity.cavern;

import java.util.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.levelgen.Heightmap;
import net.minecraftforge.common.ForgeSpawnEggItem;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.event.entity.EntityAttributeCreationEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.*;
import net.tslat.aoa3.common.registration.AoACreativeModeTabs;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;
import net.tslat.aoa3.content.item.misc.Realmstone;
import net.tslat.aoa3.content.world.gen.compat.dungeons.DungeonRealmFamily;

/** All missing dungeon prerequisites, including real survival portal keys. */
public final class DungeonMissingDependencies {
    private static final DeferredRegister<EntityType<?>> ENTITIES=DeferredRegister.create(ForgeRegistries.ENTITY_TYPES,"aoa3");
    private static final DeferredRegister<Item> ITEMS=DeferredRegister.create(ForgeRegistries.ITEMS,"aoa3");
    private static final DeferredRegister<SoundEvent> SOUNDS=DeferredRegister.create(ForgeRegistries.SOUND_EVENTS,"aoa3");
    public static final RegistryObject<EntityType<DungeonAutomaton>> AUTOMATON=ENTITIES.register("automaton",()->EntityType.Builder.<DungeonAutomaton>of(DungeonAutomaton::new,MobCategory.MONSTER).sized(1.5F,2).clientTrackingRange(16).updateInterval(1).build("aoa3:automaton"));
    public static final RegistryObject<EntityType<DungeonDeathHunter>> DEATH_HUNTER=ENTITIES.register("death_hunter",()->EntityType.Builder.<DungeonDeathHunter>of(DungeonDeathHunter::new,MobCategory.MONSTER).sized(3.5F,3.5F).clientTrackingRange(16).updateInterval(1).build("aoa3:death_hunter"));
    public static final RegistryObject<Item> AUTOMATON_EGG=ITEMS.register("automaton_spawn_egg",()->new ForgeSpawnEggItem(AUTOMATON,0x303030,0x999999,new Item.Properties()));
    public static final RegistryObject<Item> DEATH_HUNTER_EGG=ITEMS.register("death_hunter_spawn_egg",()->new ForgeSpawnEggItem(DEATH_HUNTER,0x303030,0x999999,new Item.Properties()));
    public static final RegistryObject<Item> ANCIENT_CAVERN_STONE=ITEMS.register("ancient_cavern_realmstone",()->new Realmstone(DungeonRealmFamily.PORTALS.get("ancient_cavern"),"ancient_cavern",new Item.Properties()));
    public static final RegistryObject<Item> IMMORTALLIS_STONE=ITEMS.register("immortallis_realmstone",()->new Realmstone(DungeonRealmFamily.PORTALS.get("immortallis"),"immortallis",new Item.Properties()));
    public static final List<String> CAGE_MOBS=List.of("automaton","bloodsucker","rock_critter","fenix","flowerface","ghastus","goldum","goldus","reaver","shavo","skeledon","skelekyte","urioh","urv","visage");
    static{for(String key:List.of("automaton_living","automaton_hit","automaton_death","automaton_step","death_hunter_living","death_hunter_hit","death_hunter_death","death_hunter_step","death_day"))SOUNDS.register(key,()->SoundEvent.createVariableRangeEvent(CavernDeityFamily.id(key)));}
    public static SoundEvent sound(String key){return Objects.requireNonNull(ForgeRegistries.SOUND_EVENTS.getValue(CavernDeityFamily.id(key)));}
    public static void init(IEventBus bus){
        ENTITIES.register(bus);ITEMS.register(bus);SOUNDS.register(bus);
        bus.addListener((EntityAttributeCreationEvent event)->{event.put(AUTOMATON.get(),DungeonAutomaton.attributes().build());event.put(DEATH_HUNTER.get(),DungeonDeathHunter.attributes().build());});
        bus.addListener((BuildCreativeModeTabContentsEvent event)->{if(event.getTabKey().equals(CreativeModeTabs.SPAWN_EGGS)){event.accept(AUTOMATON_EGG.get());event.accept(DEATH_HUNTER_EGG.get());}if(event.getTabKey().equals(AoACreativeModeTabs.MISC_ITEMS.getKey())){event.accept(ANCIENT_CAVERN_STONE.get());event.accept(IMMORTALLIS_STONE.get());}});
        bus.addListener((net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent event)->event.enqueueWork(()->{
            SpawnPlacements.register(AUTOMATON.get(),SpawnPlacements.Type.NO_RESTRICTIONS,Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,(type,world,reason,pos,random)->world.getDifficulty()!=net.minecraft.world.Difficulty.PEACEFUL);
            SpawnPlacements.register(DEATH_HUNTER.get(),SpawnPlacements.Type.NO_RESTRICTIONS,Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,(type,world,reason,pos,random)->world.getDifficulty()!=net.minecraft.world.Difficulty.PEACEFUL&&DungeonDeathDay.isDeadly(world.getLevel()));
            // Resolve the whole dependency set before any asynchronous world
            // generation can fail on the first missing cage or reward.
            for(String key:CAGE_MOBS)if(!ForgeRegistries.ENTITY_TYPES.containsKey(new ResourceLocation("aoa3",key)))throw new IllegalStateException("Missing complete dungeon cage dependency "+key);
            for(String key:List.of("copper_coin","utopian_banner","germinator","dragilator","krilinator","frosticator","electinator"))SnapshotEntityFamily.item(key);
        }));
    }
    private DungeonMissingDependencies(){}
}
