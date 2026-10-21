package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.ChatFormatting;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.registries.ForgeRegistries;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;
import net.tslat.aoa3.event.TributeEvents;
import net.tslat.aoa3.player.resource.TributeResource;
import net.tslat.aoa3.player.resource.TributeResource.Deities;

/** All nine original progression transitions, on the actual server/inventory.
 * One canonical progress-token item represents the five distinct legacy coin
 * roles using saved stage metadata. Untagged current tokens keep the entry role.
 * An unsuccessful full-inventory entry returns its exact token in place.
 */
public final class ImmortallisProgression {
    public static final String STAGE_TAG="AoAImmortallisStage";
    public static boolean isDungeon(net.minecraft.world.level.Level world){return world.dimension().location().toString().equals("aoa3:immortallis");}
    public static ItemStack token(int stage){
        if(stage<0||stage>4)throw new IllegalArgumentException("Unknown complete original progression coin");
        ItemStack stack=new ItemStack(SnapshotEntityFamily.item("progress_token"));if(stage!=0)stack.getOrCreateTag().putInt(STAGE_TAG,stage);return stack;
    }
    public static boolean matches(ItemStack stack,int stage){
        if(stack.isEmpty()||stack.getItem()!=SnapshotEntityFamily.item("progress_token"))return false;
        if(stack.hasTag()&&stack.getTag().contains(STAGE_TAG))return stack.getTag().contains(STAGE_TAG,3)&&stack.getTag().getInt(STAGE_TAG)==stage;
        return stage==0;
    }
    private static int slot(Inventory inventory,int stage){for(int i=0;i<inventory.items.size();i++)if(matches(inventory.items.get(i),stage))return i;return -1;}
    private static void notify(ServerPlayer player,String key,ChatFormatting colour){player.sendSystemMessage(Component.translatable("message.feedback.immortallisProgression."+key).withStyle(colour));}
    private static void consume(Inventory inventory,int slot){inventory.items.get(slot).shrink(1);inventory.setChanged();}
    private static void removeCrystal(Inventory inventory){for(int i=0;i<inventory.items.size();i++)if(inventory.items.get(i).is(SnapshotEntityFamily.item("return_crystal"))){consume(inventory,i);return;}}
    private static void move(ServerPlayer player,double x,double y,double z){player.teleportTo(x,y,z);}
    public static void returnToLobby(ServerPlayer player){
        if(!isDungeon(player.level()))throw new IllegalArgumentException("Immortallis return cannot change another world's state");
        move(player,0,20,0);TributeResource tribute=TributeEvents.tribute(player);if(tribute==null)throw new IllegalStateException("Complete tribute resource is required");tribute.resetAllTribute();
        Inventory inventory=player.getInventory();for(int stage=1;stage<=4;stage++){int at=slot(inventory,stage);if(at>=0)consume(inventory,at);}player.containerMenu.broadcastChanges();
    }
    private static void boss(ServerPlayer player,String key,int x,int y,int z){
        ServerLevel world=player.serverLevel();world.getChunk(Math.floorDiv(x,16),Math.floorDiv(z,16));
        var type=ForgeRegistries.ENTITY_TYPES.getValue(new ResourceLocation("aoa3",key));if(type==null)throw new IllegalStateException("Missing original Immortallis boss "+key);
        Entity candidate=type.create(world);if(candidate==null)throw new IllegalStateException("Immortallis boss factory returned null");candidate.moveTo(x,y,z,0,0);
        // The old Mirage/Flash cases mistakenly queried Klobber.class. Match
        // the actual requested boss identity for all four rooms instead.
        if(world.getEntities(candidate,candidate.getBoundingBox().inflate(15,5,15),other->other.getType()==type&&other.isAlive()).isEmpty()){
            if(candidate instanceof net.minecraft.world.entity.Mob mob)mob.setPersistenceRequired();
            if(!world.addFreshEntity(candidate))throw new IllegalStateException("Native world rejected original Immortallis boss "+key);
        }
    }
    public static boolean activate(ServerPlayer player,int stage){
        if(stage<1||stage>9)throw new IllegalArgumentException("Unknown original dungeon progressor");
        if(!isDungeon(player.level())||player.isCrouching())return false;
        Inventory inventory=player.getInventory();TributeResource tribute=TributeEvents.tribute(player);if(tribute==null)throw new IllegalStateException("Complete tribute resource is required");
        int tokenSlot;
        switch(stage){
            case 1 -> {
                tokenSlot=slot(inventory,0);if(tokenSlot<0)return false;
                ItemStack exactBefore=inventory.items.get(tokenSlot).copy();consume(inventory,tokenSlot);
                ItemStack crystal=new ItemStack(SnapshotEntityFamily.item("return_crystal"));
                if(!inventory.add(crystal)){inventory.items.set(tokenSlot,exactBefore);inventory.setChanged();notify(player,"returnCrystal.fail",ChatFormatting.RED);player.containerMenu.broadcastChanges();return false;}
                notify(player,"goldStart.0",ChatFormatting.GOLD);notify(player,"goldStart.1",ChatFormatting.GOLD);move(player,28,20,2);
            }
            case 2 -> {if(tribute.getTribute(Deities.Pluton)<100)return false;notify(player,"klobberStart",ChatFormatting.DARK_AQUA);move(player,67,21,2);boss(player,"klobber",69,21,4);}
            case 3 -> {tokenSlot=slot(inventory,1);if(tokenSlot<0)return false;consume(inventory,tokenSlot);notify(player,"skeletalSpiritsStart",ChatFormatting.RED);move(player,81,21,2);}
            case 4 -> {if(tribute.getTribute(Deities.Erebon)<100)return false;notify(player,"proshieldStart",ChatFormatting.DARK_AQUA);move(player,122,21,2);boss(player,"proshield",123,21,6);}
            case 5 -> {tokenSlot=slot(inventory,2);if(tokenSlot<0)return false;consume(inventory,tokenSlot);notify(player,"pureGoldStart.0",ChatFormatting.GOLD);notify(player,"pureGoldStart.1",ChatFormatting.GOLD);move(player,141,24,2);}
            case 6 -> {if(tribute.getTribute(Deities.Pluton)!=200)return false;notify(player,"mirageStart",ChatFormatting.DARK_AQUA);move(player,168,24,7);boss(player,"mirage",177,24,-2);}
            case 7 -> {tokenSlot=slot(inventory,3);if(tokenSlot<0)return false;consume(inventory,tokenSlot);notify(player,"evilSpiritsStart",ChatFormatting.RED);move(player,189,20,2);}
            case 8 -> {if(tribute.getTribute(Deities.Erebon)!=200)return false;notify(player,"flashStart",ChatFormatting.DARK_AQUA);move(player,233,21,3);boss(player,"flash",235,22,10);}
            case 9 -> {tokenSlot=slot(inventory,4);if(tokenSlot<0)return false;consume(inventory,tokenSlot);move(player,0,20,0);removeCrystal(inventory);}
        }
        inventory.setChanged();player.containerMenu.broadcastChanges();return true;
    }
    /** Keep the resource cap and +20 awards, repairing consumption at a full
     * accumulator so repeated clicks cannot silently destroy valuable gold. */
    public static boolean deposit(ServerPlayer player,boolean pure){
        if(!isDungeon(player.level())||player.isCrouching())return false;
        TributeResource tribute=TributeEvents.tribute(player);if(tribute==null)throw new IllegalStateException("Complete tribute resource is required");
        int cap=pure?200:100,current=tribute.getTribute(Deities.Pluton);if(current>=cap)return false;
        Inventory inventory=player.getInventory();var gold=SnapshotEntityFamily.item(pure?"pure_gold":"impure_gold");int found=-1;
        for(int i=0;i<inventory.items.size();i++)if(inventory.items.get(i).is(gold)){found=i;break;}
        if(found<0)return false;consume(inventory,found);tribute.setTribute(Deities.Pluton,Math.min(cap,current+20));
        if(tribute.getTribute(Deities.Pluton)==cap)player.sendSystemMessage(Component.translatable("message.feedback.immortallisProgression."+(pure?"pureGoldEnd":"goldEnd"),player.getDisplayName()));
        player.containerMenu.broadcastChanges();return true;
    }
    private ImmortallisProgression(){}
}
