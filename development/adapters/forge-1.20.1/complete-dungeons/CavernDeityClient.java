package net.tslat.aoa3.content.entity.cavern;

import com.mojang.blaze3d.vertex.PoseStack;
import enderloom.compat.model1710.Legacy1710EntityModel;
import net.minecraft.client.Minecraft;
import net.minecraft.client.multiplayer.ClientLevel;
import net.minecraft.client.particle.*;
import net.minecraft.client.renderer.entity.*;
import net.minecraft.client.renderer.texture.TextureAtlasSprite;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.*;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.tslat.aoa3.client.model.entity.boss.*;

/** All 191 authored cubes, every animation and renderer scale use native
 * model buffers/PoseStack. No immediate OpenGL calls or proxy creature model. */
@Mod.EventBusSubscriber(modid="aoa3",bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class CavernDeityClient {
    private static SpriteSet black;
    @SubscribeEvent public static void renderers(EntityRenderersEvent.RegisterRenderers event){
        for(var kind:CavernDeityBoss.Kind.values())event.registerEntityRenderer(CavernDeityFamily.BOSSES.get(kind).get(),context->new BossRenderer(context,kind));
        event.registerEntityRenderer(CavernDeityFamily.SHOT.get(),ShotRenderer::new);
    }
    private static Legacy1710EntityModel<CavernDeityBoss> model(CavernDeityBoss.Kind kind){return switch(kind){case CONIFERON->new ConiferonModel<>();case GOLDORTH->new GoldorthModel<>();case HORON->new HoronModel<>();case PENUMBRA->new PenumbraModel<>();};}
    public static final class BossRenderer extends MobRenderer<CavernDeityBoss,Legacy1710EntityModel<CavernDeityBoss>> {
        private final CavernDeityBoss.Kind kind;
        public BossRenderer(EntityRendererProvider.Context context,CavernDeityBoss.Kind kind){super(context,model(kind),.5F);this.kind=kind;}
        @Override protected void scale(CavernDeityBoss entity,PoseStack stack,float partial){stack.scale(kind.scale,kind.scale,kind.scale);}
        @Override public ResourceLocation getTextureLocation(CavernDeityBoss entity){return CavernDeityFamily.id("textures/entity/cavern/"+kind.key()+".png");}
    }
    public static final class ShotRenderer extends EntityRenderer<CavernPenumbraShot>{
        public ShotRenderer(EntityRendererProvider.Context context){super(context);}
        @Override public ResourceLocation getTextureLocation(CavernPenumbraShot entity){return net.minecraft.client.renderer.texture.TextureAtlas.LOCATION_PARTICLES;}
    }
    @SubscribeEvent public static void particles(RegisterParticleProvidersEvent event){event.registerSpriteSet(CavernDeityFamily.BLACK_TRAIL.get(),sprites->{black=sprites;return (type,level,x,y,z,dx,dy,dz)->new BlackTrail(level,x,y,z,sprites.get(0,1),dx,dy,dz);});}
    public static void trail(CavernPenumbraShot shot){
        if(black==null)throw new IllegalStateException("Complete original cavern trail atlas was not registered");
        TextureAtlasSprite sprite=black.get(0,1);for(int i=0;i<8;i++)Minecraft.getInstance().particleEngine.add(new BlackTrail((ClientLevel)shot.level(),shot.getX(),shot.getY(),shot.getZ(),sprite,0,0,0));
    }
    public static final class BlackTrail extends TextureSheetParticle {
        private final TextureAtlasSprite atlas;private int originalIndex;
        public BlackTrail(ClientLevel level,double x,double y,double z,TextureAtlasSprite atlas,double dx,double dy,double dz){
            super(level,x,y,z,dx,dy,dz);this.atlas=atlas;setSprite(atlas);
            xd=dx+(float)(Math.random()*2-1)*.05F;yd=dy+(float)(Math.random()*2-1)*.05F;zd=dz+(float)(Math.random()*2-1)*.05F;
            float unusedBrightness=random.nextFloat()*.6F+.4F,unusedPortalScale=random.nextFloat()*.2F+.5F;rCol=gCol=bCol=0;
            quadSize=.1F*(random.nextFloat()*random.nextFloat()*6F+1F);lifetime=(int)(3/((double)random.nextFloat()*.8+.2));
        }
        @Override public void tick(){xo=x;yo=y;zo=z;if(age++>=lifetime)remove();originalIndex=7-age*5/lifetime;yd+=.004;xd*=.9F;yd*=.9F;zd*=.9F;if(onGround){xd*=.7F;zd*=.7F;}}
        @Override protected float getU0(){return atlas.getU(originalIndex%16);}
        @Override protected float getU1(){return atlas.getU(originalIndex%16+.999F);}
        @Override protected float getV0(){return atlas.getV(originalIndex/16);}
        @Override protected float getV1(){return atlas.getV(originalIndex/16+.999F);}
        @Override public ParticleRenderType getRenderType(){return ParticleRenderType.PARTICLE_SHEET_OPAQUE;}
    }
}
