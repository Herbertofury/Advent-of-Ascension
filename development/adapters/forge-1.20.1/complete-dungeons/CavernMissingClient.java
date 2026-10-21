package net.tslat.aoa3.content.entity.cavern;

import enderloom.compat.model1710.Legacy1710EntityModel;
import net.minecraft.client.renderer.entity.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.tslat.aoa3.client.model.entity.boss.HellspotModel;

@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class CavernMissingClient {
    @SubscribeEvent public static void register(EntityRenderersEvent.RegisterRenderers event){event.registerEntityRenderer(CavernMissingDependencies.HELLSPOT.get(),HellspotRenderer::new);}
    public static final class HellspotRenderer extends MobRenderer<CavernHellspot,Legacy1710EntityModel<CavernHellspot>>{
        public HellspotRenderer(EntityRendererProvider.Context context){super(context,new HellspotModel<CavernHellspot>(),.5F);}
        @Override public ResourceLocation getTextureLocation(CavernHellspot entity){return CavernDeityFamily.id("textures/entity/cavern/hellspot.png");}
    }
}
