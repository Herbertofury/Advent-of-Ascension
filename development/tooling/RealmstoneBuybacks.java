package net.tslat.aoa3.content.entity.mob.historical.restored;

import java.util.List;
import java.util.Objects;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.trading.MerchantOffer;
import net.minecraft.world.item.trading.MerchantOffers;
import net.minecraftforge.registries.ForgeRegistries;

/** Complete original Realmshifter buybacks alongside all newer trades.
 * Saved offers, custom amounts, uses, prices and unrelated trades stay intact.
 * These are stone-for-currency buybacks, never currency-for-stone sales.
 */
public final class RealmstoneBuybacks {
    public record Buyback(String stone, String currency, int amount) {}
    public static final List<Buyback> ALL=List.of(
        new Buyback("abyss","silver_coin",6),
        new Buyback("ancient_cavern","silver_coin",9),
        new Buyback("barathos","silver_coin",8),
        new Buyback("lborean","silver_coin",7),
        new Buyback("celeve","silver_coin",4),
        new Buyback("crystevia","silver_coin",6),
        new Buyback("deeplands","copper_coin",9),
        new Buyback("dustopia","silver_coin",6),
        new Buyback("gardencia","silver_coin",2),
        new Buyback("haven","silver_coin",1),
        new Buyback("iromine","copper_coin",4),
        new Buyback("lelyetia","silver_coin",3),
        new Buyback("mysterium","silver_coin",1),
        new Buyback("precasia","silver_coin",2),
        new Buyback("vox_ponds","silver_coin",4),
        new Buyback("candyland","silver_coin",5),
        new Buyback("creeponia","silver_coin",6),
        new Buyback("immortallis","silver_coin",6),
        new Buyback("shyrelands","silver_coin",9));

    public static Item item(String key) {
        Item item=ForgeRegistries.ITEMS.getValue(new ResourceLocation("aoa3",key));
        if(item==null||item==Items.AIR)throw new IllegalStateException("Missing complete Realmshifter dependency: "+key);
        return item;
    }

    public static void ensure(MerchantOffers offers) {
        Objects.requireNonNull(offers);
        for(Buyback row:ALL) {
            Item stone=item(row.stone()+"_realmstone"),coin=item(row.currency());
            boolean present=offers.stream().anyMatch(offer->offer.getBaseCostA().is(stone)
                &&offer.getCostB().isEmpty()&&offer.getResult().is(coin));
            if(!present)offers.add(new MerchantOffer(new ItemStack(stone),new ItemStack(coin,row.amount()),Integer.MAX_VALUE,0,0));
        }
    }
    private RealmstoneBuybacks() {}
}
