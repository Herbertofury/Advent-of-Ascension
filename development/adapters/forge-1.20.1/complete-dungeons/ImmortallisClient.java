package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.client.renderer.item.ItemProperties;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.tslat.aoa3.content.entity.snapshot1710.SnapshotEntityFamily;

/** The existing token stays canonical; distinct old stage art is model data. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class ImmortallisClient {
    @SubscribeEvent public static void setup(FMLClientSetupEvent event){event.enqueueWork(()->ItemProperties.register(SnapshotEntityFamily.item("progress_token"),new ResourceLocation("aoa3","immortallis_stage"),(stack,level,entity,seed)->{
        if(!stack.hasTag()||!stack.getTag().contains(ImmortallisProgression.STAGE_TAG))return 0;
        int stage=stack.getTag().getInt(ImmortallisProgression.STAGE_TAG);return stage>=1&&stage<=4?stage:0;
    }));}
}
