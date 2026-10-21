package net.tslat.aoa3.content.world.gen.compat.dungeons;

import net.minecraft.client.renderer.DimensionSpecialEffects;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.client.event.RegisterDimensionSpecialEffectsEvent;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Both original providers have no skylight and exact black fog. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class DungeonDimensionEffects extends DimensionSpecialEffects {
    private DungeonDimensionEffects(){super(128,false,SkyType.NONE,false,false);}
    @SubscribeEvent public static void register(RegisterDimensionSpecialEffectsEvent event){for(String realm:DungeonRealmFamily.REALMS)event.register(new ResourceLocation("aoa3",realm),new DungeonDimensionEffects());}
    @Override public Vec3 getBrightnessDependentFogColor(Vec3 input,float sunlight){return Vec3.ZERO;}
    @Override public boolean isFoggyAt(int x,int z){return true;}
}
