package net.tslat.aoa3.content.entity.cavern;

import enderloom.compat.model1710.Legacy1710EntityModel;
import net.minecraft.client.renderer.entity.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.tslat.aoa3.client.model.entity.boss.AutomatonModel;
import net.tslat.aoa3.client.model.entity.boss.DeathHunterModel;

@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class DungeonMissingClient {
    @SubscribeEvent public static void register(EntityRenderersEvent.RegisterRenderers event){event.registerEntityRenderer(DungeonMissingDependencies.AUTOMATON.get(),Renderer::new);event.registerEntityRenderer(DungeonMissingDependencies.DEATH_HUNTER.get(),DeathHunterRenderer::new);}
    public static final class Renderer extends MobRenderer<DungeonAutomaton,Legacy1710EntityModel<DungeonAutomaton>>{
        public Renderer(EntityRendererProvider.Context context){super(context,new AutomatonModel<DungeonAutomaton>(),.5F);}
        @Override public ResourceLocation getTextureLocation(DungeonAutomaton entity){return CavernDeityFamily.id("textures/entity/cavern/automaton_"+entity.colour()+".png");}
    }
    public static final class DeathHunterRenderer extends MobRenderer<DungeonDeathHunter,Legacy1710EntityModel<DungeonDeathHunter>>{
        public DeathHunterRenderer(EntityRendererProvider.Context context){super(context,new DeathHunterModel<DungeonDeathHunter>(),.5F);}
        @Override protected void scale(DungeonDeathHunter entity,com.mojang.blaze3d.vertex.PoseStack stack,float partial){stack.scale(2,2,2);}
        @Override public ResourceLocation getTextureLocation(DungeonDeathHunter entity){return CavernDeityFamily.id("textures/entity/cavern/death_hunter.png");}
    }
}
