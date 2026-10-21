package net.tslat.aoa3.player.skill;

import com.google.gson.JsonObject;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.Tag;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.player.Player;
import net.tslat.aoa3.common.registration.custom.AoASkills;
import net.tslat.aoa3.event.custom.AoAEvents;
import net.tslat.aoa3.player.ServerPlayerDataManager;
import net.tslat.aoa3.util.PlayerUtil;

/** One canonical Hunter save, network and UI owner. Original float XP and the
 * older Snapshot integer-award policy remain distinct inputs to this owner.
 * Canonical saves take precedence over both retained historical save formats.
 */
public final class HunterSkill extends AoASkill.Instance {
    public static final String MODERN_POLICY="aoa3";
    public static final String HISTORICAL_POLICY="tslat113";
    private String progressionPolicy=MODERN_POLICY;
    private String importedFormat="new-player";
    private boolean legacyDataNeedsReview;
    public HunterSkill(ServerPlayerDataManager player,JsonObject data) {
        super(AoASkills.HUNTER.get(),player,data);
        CompoundTag old=player.player().getPersistentData().getCompound(Player.PERSISTED_NBT_TAG);
        if(old.contains("Hunter")){
            CompoundTag historical=old.getCompound("Hunter");
            if(old.contains("Hunter",Tag.TAG_COMPOUND)&&numberOrAbsent(historical,"Lvl")&&numberOrAbsent(historical,"Xp"))
                importHistorical(Math.max(1,historical.getInt("Lvl")),Math.max(0,historical.getFloat("Xp")),"tslat-container");
            else invalidLegacy("tslat-container");
        }else if(old.contains("HLevel")||old.contains("HExp")){
            if(numberOrAbsent(old,"HLevel")&&numberOrAbsent(old,"HExp"))
                importHistorical(old.contains("HLevel")?Math.max(1,old.getInt("HLevel")):1,Math.max(0,old.getFloat("HExp")),"snapshot-container");
            else invalidLegacy("snapshot-container");
        }
    }
    public HunterSkill(CompoundTag data){super(AoASkills.HUNTER.get(),data);}
    private static boolean numberOrAbsent(CompoundTag tag,String key){return !tag.contains(key)||tag.contains(key,Tag.TAG_ANY_NUMERIC);}
    private void invalidLegacy(String format){importedFormat="invalid-"+format;legacyDataNeedsReview=true;}
    private void importHistorical(int oldLevel,float oldXp,String format){
        if(oldLevel<1||oldLevel>100||!Float.isFinite(oldXp)||oldXp<0){invalidLegacy(format);return;}
        level=oldLevel;xp=oldXp;progressionPolicy=HISTORICAL_POLICY;importedFormat=format;needsSync=true;
    }
    public String importedFormat(){return importedFormat;}
    public String progressionPolicy(){return progressionPolicy;}
    public boolean historicalProgression(){return HISTORICAL_POLICY.equals(progressionPolicy);}
    @Override public float xpRequiredForLevel(int currentLevel){return historicalProgression()?HunterProgression.threshold(Math.max(1,Math.min(100,currentLevel))):super.xpRequiredForLevel(currentLevel);}
    @Override public int maximumLevel(){return historicalProgression()?100:1000;}
    @Override public void setLevel(int newLevel){super.setLevel(Math.max(1,Math.min(maximumLevel(),newLevel)));mirrorLegacyReaders();}
    @Override protected boolean applyOwnExperience(float amount,boolean unnatural){
        if(!historicalProgression())return false;
        if(amount<0){subtractHunterXp(amount,unnatural);return true;}
        var state=HunterProgression.award(level,xp,amount);
        completeExperience(amount,unnatural,new ExperienceStep(state.level(),state.xp()));
        return true;
    }
    @Override public void adjustXp(float amount,boolean unnatural,boolean ignoreBuffs){
        if(!historicalProgression()){super.adjustXp(amount,unnatural,ignoreBuffs);return;}
        float afterModifiers=!unnatural&&!ignoreBuffs?applyXpBuffs(amount):amount;
        var event=AoAEvents.playerChangeXpEvent(playerDataManager,this,amount,afterModifiers,!unnatural);
        // An explicit zero award still normalizes an original threshold save;
        // a canceled Forge XP event must remain a strict no-op.
        if(event.isCanceled())return;
        applyOwnExperience(event.getNewXpGain(),unnatural);mirrorLegacyReaders();
    }
    private void subtractHunterXp(float amount,boolean unnatural){
        float remaining=Math.abs(amount),updated=xp;int updatedLevel=level;
        while(remaining>updated&&updatedLevel>1){remaining-=updated;updated=HunterProgression.threshold(--updatedLevel);}
        updated=Math.max(0,updated-remaining);
        completeExperience(amount,unnatural,new ExperienceStep(updatedLevel,updated));
    }
    @Override public void loadFromNbt(CompoundTag data){
        // Canonical state wins, even when it is 1/0. Retain all ability/cycle data.
        // The preceding historical prototype had no discriminator. Preserve its
        // real arithmetic instead of silently reinterpreting those saved XP bits.
        progressionPolicy=data.contains("progression_policy",Tag.TAG_STRING)?data.getString("progression_policy"):HISTORICAL_POLICY;
        if(!MODERN_POLICY.equals(progressionPolicy)&&!HISTORICAL_POLICY.equals(progressionPolicy))
            throw new IllegalArgumentException("Unknown Hunter progression policy; refusing silent save conversion");
        super.loadFromNbt(data);
        if(data.contains("legacy_data_needs_review",Tag.TAG_BYTE))legacyDataNeedsReview=data.getBoolean("legacy_data_needs_review");
        importedFormat=legacyDataNeedsReview?"canonical-unreadable-legacy-retained":"canonical";
        if(level<1||level>maximumLevel()||!Float.isFinite(xp)||xp<0)
            throw new IllegalArgumentException("Invalid canonical Hunter save; refusing silent data replacement");
    }
    @Override public CompoundTag saveToNbt(){
        CompoundTag saved=super.saveToNbt();saved.putString("progression_policy",progressionPolicy);saved.putBoolean("legacy_data_needs_review",legacyDataNeedsReview);return saved;
    }
    @Override public CompoundTag getSyncData(boolean setup){CompoundTag data=super.getSyncData(setup);data.putString("progression_policy",progressionPolicy);return data;}
    @Override public void receiveSyncData(CompoundTag data){
        if(data.contains("progression_policy",Tag.TAG_STRING)){
            String policy=data.getString("progression_policy");
            if(!MODERN_POLICY.equals(policy)&&!HISTORICAL_POLICY.equals(policy))throw new IllegalArgumentException("Unknown Hunter sync policy");
            progressionPolicy=policy;
        }
        super.receiveSyncData(data);
    }
    private void mirrorLegacyReaders(){
        if(playerDataManager==null||legacyDataNeedsReview||!historicalProgression())return;
        CompoundTag old=getPlayer().getPersistentData().getCompound(Player.PERSISTED_NBT_TAG);
        old.putInt("HLevel",level);old.putFloat("HExp",xp);
        // Preserve unknown original fields rather than replacing the compound.
        CompoundTag historical=old.getCompound("Hunter");historical.putInt("Lvl",level);historical.putFloat("Xp",xp);old.put("Hunter",historical);
        getPlayer().getPersistentData().put(Player.PERSISTED_NBT_TAG,old);
    }
    public static void awardSnapshot(ServerPlayer player,int amount,int requiredLevel){
        var skill=PlayerUtil.getSkill(player,AoASkills.HUNTER.get());
        if(!(skill instanceof HunterSkill hunter))return; // Respect the existing disableSkills choice.
        if(hunter.level<requiredLevel)return;
        if(!hunter.historicalProgression()){PlayerUtil.giveXpToPlayer(player,AoASkills.HUNTER.get(),amount,false);return;}
        var state=HunterProgression.awardSnapshot(hunter.level,hunter.xp,amount);
        hunter.completeExperience(amount,false,new ExperienceStep(state.level(),state.xp()));
        hunter.mirrorLegacyReaders();
    }
}
