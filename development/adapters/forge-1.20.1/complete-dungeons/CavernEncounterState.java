package net.tslat.aoa3.content.entity.cavern;

import java.util.*;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.Difficulty;
import net.minecraft.world.level.saveddata.SavedData;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** One saved encounter owner per world, never static entity references shared
 * by unrelated servers. Unloaded UUIDs stay claimed; absence from the loaded
 * entity lookup is never permission to duplicate a saved boss. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.FORGE)
public final class CavernEncounterState extends SavedData {
    private CompoundTag data=new CompoundTag();
    private CavernEncounterState(){}
    private static CavernEncounterState load(CompoundTag tag){var state=new CavernEncounterState();state.data=tag.copy();return state;}
    private static boolean cavern(ServerLevel level){return level.dimension().location().toString().equals("aoa3:ancient_cavern");}
    public static CavernEncounterState get(ServerLevel level){return level.getDataStorage().computeIfAbsent(CavernEncounterState::load,CavernEncounterState::new,"aoa3_cavern_encounters");}
    private CompoundTag slot(CavernDeityBoss.Kind kind){CompoundTag value=data.getCompound(kind.key());if(!data.contains(kind.key(),10))data.put(kind.key(),value);return value;}
    public boolean trySpawn(ServerLevel level,CavernDeityBoss.Kind kind){
        if(!cavern(level)||level.getDifficulty()==Difficulty.PEACEFUL)return false;
        CompoundTag slot=slot(kind);if(slot.hasUUID("Active")||slot.getLong("ReadyAt")>level.getGameTime())return false;
        CavernDeityBoss boss=CavernDeityFamily.BOSSES.get(kind).get().create(level);if(boss==null)throw new IllegalStateException("Missing complete cavern boss factory");
        // The original shrine may target a distant room. Load that exact room
        // before inserting its entity; never place in an unloaded destination.
        level.getChunk(Math.floorDiv(kind.x,16),Math.floorDiv(kind.z,16));boss.moveTo(kind.x,kind.y,kind.z,level.random.nextFloat()*360F,0);
        slot.putUUID("Active",boss.getUUID());slot.putInt("ChunkX",boss.chunkPosition().x);slot.putInt("ChunkZ",boss.chunkPosition().z);slot.putBoolean("Managed",true);slot.remove("ReadyAt");setDirty();
        if(!level.addFreshEntity(boss)){slot.remove("Active");slot.putLong("ReadyAt",level.getGameTime()+20);setDirty();return false;}return true;
    }
    public static void note(ServerLevel level,CavernDeityBoss boss){
        if(!cavern(level))return;var owner=get(level);var slot=owner.slot(boss.kind());
        if(!slot.hasUUID("Active")||!slot.getUUID("Active").equals(boss.getUUID()))return;
        if(slot.getInt("ChunkX")!=boss.chunkPosition().x||slot.getInt("ChunkZ")!=boss.chunkPosition().z){slot.putInt("ChunkX",boss.chunkPosition().x);slot.putInt("ChunkZ",boss.chunkPosition().z);owner.setDirty();}
    }
    public static void died(ServerLevel level,CavernDeityBoss boss){
        if(!cavern(level))return;var owner=get(level);var slot=owner.slot(boss.kind());
        if(slot.hasUUID("Active")&&slot.getUUID("Active").equals(boss.getUUID())){slot.remove("Active");slot.putLong("ReadyAt",level.getGameTime()+700);owner.setDirty();}
    }
    @SubscribeEvent public static void tick(TickEvent.LevelTickEvent event){
        if(event.phase!=TickEvent.Phase.END||!(event.level instanceof ServerLevel level)||!cavern(level))return;
        var state=get(level);for(var kind:CavernDeityBoss.Kind.values()){
            var slot=state.slot(kind);
            if(slot.getBoolean("Managed")&&!slot.hasUUID("Active")&&slot.contains("ReadyAt")&&slot.getLong("ReadyAt")<=level.getGameTime())state.trySpawn(level,kind);
        }
    }
    @Override public CompoundTag save(CompoundTag tag){tag.merge(data.copy());return tag;}
}
