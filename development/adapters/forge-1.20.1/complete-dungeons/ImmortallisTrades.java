package net.tslat.aoa3.content.world.gen.compat.dungeons;

import java.util.*;
import it.unimi.dsi.fastutil.ints.*;
import net.minecraft.world.entity.npc.VillagerTrades;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.trading.*;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;

/** Complete native merchant listings: newer intended canonical offers plus
 * unique older rewards. Every listing is available; no random two-offer cut.
 * Existing nonempty saved offers, prices, uses and player choices stay intact.
 */
public final class ImmortallisTrades {
    public record Offer(String currency,int count,String result,int quantity,boolean entry){
        private MerchantOffer make(){ItemStack cost=new ItemStack(SnapshotEntityFamily.item(currency),count),output=entry?ImmortallisProgression.token(0):new ItemStack(SnapshotEntityFamily.item(result),quantity);return new MerchantOffer(cost,ItemStack.EMPTY,output,Integer.MAX_VALUE,0,0){@Override public boolean isOutOfStock(){return false;}@Override public void increaseUses(){super.increaseUses();if(getUses()>1024)resetUses();}};}
    }
    private static final List<Offer> KEEPER=List.of(
        new Offer("silver_coin",5,"progress_token",1,true),new Offer("gold_coin",2,"vulcane",1,false),
        new Offer("dungeon_tokens",1,"archaic_tiles",16,false),new Offer("dungeon_tokens",1,"archaic_squares",12,false),new Offer("dungeon_tokens",1,"archaic_rectangles",12,false),
        new Offer("dungeon_tokens",1,"archaic_stream_horizontal",12,false),new Offer("dungeon_tokens",1,"archaic_tile_stream",12,false),new Offer("dungeon_tokens",1,"archaic_dirt",16,false),
        new Offer("dungeon_tokens",1,"archaic_ladder",8,false),new Offer("dungeon_tokens",1,"archaic_glass",8,false),new Offer("dungeon_tokens",1,"archaic_light",4,false));
    private static final List<Offer> COLLECTOR=List.of(
        new Offer("dungeon_tokens",1,"immortal_banner",1,false),new Offer("dungeon_tokens",1,"vulcane",1,false),
        new Offer("dungeon_tokens",13,"fire_vulcane_augment",1,false),new Offer("dungeon_tokens",9,"impairment_vulcane_augment",1,false),new Offer("dungeon_tokens",10,"poison_vulcane_augment",1,false),
        new Offer("dungeon_tokens",5,"power_vulcane_augment",1,false),new Offer("dungeon_tokens",15,"wither_vulcane_augment",1,false),new Offer("dungeon_tokens",25,"equality_vulcane_augment",1,false),new Offer("dungeon_tokens",20,"battle_vulcane_augment",1,false),
        new Offer("dungeon_tokens",28,"vulcammer_maul",1,false),new Offer("dungeon_tokens",26,"meteor_staff",1,false),
        new Offer("dungeon_tokens",30,"everfight_staff",1,false),new Offer("dungeon_tokens",30,"evermight_staff",1,false),new Offer("dungeon_tokens",40,"odious",1,false),new Offer("dungeon_tokens",50,"deadlock",1,false));
    private static List<Offer> offers(boolean collector){return collector?COLLECTOR:KEEPER;}
    public static Int2ObjectMap<VillagerTrades.ItemListing[]> map(boolean collector){
        var rows=offers(collector);var map=new Int2ObjectOpenHashMap<VillagerTrades.ItemListing[]>();map.put(1,rows.stream().<VillagerTrades.ItemListing>map(row->(entity,random)->row.make()).toArray(VillagerTrades.ItemListing[]::new));return map;
    }
    public static void restoreEmpty(MerchantOffers actual,boolean collector){if(actual.isEmpty())for(Offer row:offers(collector))actual.add(row.make());}
    public static int completeCount(boolean collector){return offers(collector).size();}
    private ImmortallisTrades(){}
}
