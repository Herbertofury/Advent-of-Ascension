package dev.enderloom.reference;

import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.FMLCommonHandler;
import cpw.mods.fml.common.event.FMLInitializationEvent;
import cpw.mods.fml.common.eventhandler.SubscribeEvent;
import cpw.mods.fml.common.gameevent.TickEvent;
import com.google.gson.GsonBuilder;
import com.mojang.authlib.GameProfile;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.util.IChatComponent;
import net.minecraft.world.World;
import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Whole registered original Hunter domain and real original container/gates.
 * Detached players/entities only; no client, audio device or player save. */
@Mod(modid="enderloom_hunter_reference",name="Enderloom complete original Hunter observer",version="1",acceptableRemoteVersions="*")
public final class OriginalWholeHunterFamilyProbe {
    private boolean done;private int ticks;
    @Mod.EventHandler public void initialize(FMLInitializationEvent event){FMLCommonHandler.instance().bus().register(this);}
    private Class<?> c(String name)throws Exception{return Class.forName(name,true,getClass().getClassLoader());}
    private static Map<String,Object> row(Object...values){Map<String,Object> out=new LinkedHashMap<String,Object>();for(int i=0;i<values.length;i+=2)out.put((String)values[i],values[i+1]);return out;}
    private static void check(boolean yes,String why){if(!yes)throw new IllegalStateException(why);}
    public static final class DetachedPlayer extends EntityPlayer {
        public DetachedPlayer(World world){super(world,new GameProfile(UUID.fromString("7a54a566-8a15-4f4f-88be-9caf2c715987"),"OriginalHunterQA"));}
        @Override public void func_145747_a(IChatComponent ignored){}
        @Override public boolean func_70003_b(int level,String command){return false;}
        @Override public net.minecraft.util.ChunkCoordinates func_82114_b(){return new net.minecraft.util.ChunkCoordinates(0,0,0);}
    }
    @SuppressWarnings({"unchecked","rawtypes"})
    @SubscribeEvent public void tick(TickEvent.ServerTickEvent event){
        if(event.phase!=TickEvent.Phase.END||done||++ticks<100)return;done=true;
        Map<String,Object> report=row("passed",false,"originalRuntime",true,"synthetic",false,"generatedDetachedFixtures",true,"completeAoAPort",false,"clientLaunched",false);
        try{
            Object server=c("net.minecraft.server.MinecraftServer").getMethod("func_71276_C").invoke(null);World world=(World)server.getClass().getMethod("func_71218_a",int.class).invoke(server,0);
            Class<?> trait=c("net.nevermine.mob.placement.EntityHunter"),container=c("net.nevermine.container.PlayerContainer"),skill=c("net.nevermine.container.PlayerContainer$Skills");Object hunter=Enum.valueOf((Class)skill,"Hunter");
            Map<?,?> registry=(Map<?,?>)c("net.minecraft.entity.EntityList").getField("field_75626_c").get(null);
            List<Object> entities=new ArrayList<Object>();TreeSet<Integer> requirements=new TreeSet<Integer>();List<Class<?>> owners=new ArrayList<Class<?>>();
            for(Object key:registry.keySet())if(key instanceof Class&&((Class<?>)key).getName().startsWith("net.nevermine.")&&trait.isAssignableFrom((Class<?>)key))owners.add((Class<?>)key);
            Collections.sort(owners,new Comparator<Class<?>>(){public int compare(Class<?>a,Class<?>b){return a.getName().compareTo(b.getName());}});
            for(Class<?> owner:owners){Object entity=owner.getConstructor(World.class).newInstance(world);int required=((Number)trait.getMethod("getLevReq").invoke(entity)).intValue();check(required>=0&&required<=100,"Original native Hunter requirement outside domain: "+owner.getName()+"="+required);requirements.add(required);entities.add(row("class",owner.getName(),"nativeRegistryIdentity",registry.get(owner),"requiredLevel",required,"detachedNeverAdded",true));}
            check(!entities.isEmpty(),"Original native Hunter domain is empty");report.put("completeRegisteredHunterEntities",entities);report.put("completeRequiredLevels",requirements);
            DetachedPlayer player=new DetachedPlayer(world);Object properties=container.getMethod("getProperties",EntityPlayer.class).invoke(null,player);
            if(properties==null){container.getMethod("addProperties",EntityPlayer.class).invoke(null,player);properties=container.getMethod("getProperties",EntityPlayer.class).invoke(null,player);}
            check(properties!=null,"Missing actual original player container");
            Method setLevel=container.getMethod("setLevel",int.class,skill),setXp=container.getMethod("setExperience",float.class,skill),getLevel=container.getMethod("getLevel",skill),getXp=container.getMethod("getExperience",skill),required=container.getMethod("getExpRequired",skill),add=container.getMethod("addExperience",float.class,skill);
            Method hunt=c("net.nevermine.mob.ai.HuntAttempt").getMethod("Hunt",c("net.minecraft.entity.Entity"),int.class,c("net.minecraft.util.DamageSource"));Object damage=c("net.minecraft.util.DamageSource").getMethod("func_76365_a",EntityPlayer.class).invoke(null,player);
            Object capabilities=c("net.minecraft.entity.player.EntityPlayer").getField("field_71075_bZ").get(player);Field creativeFlag=capabilities.getClass().getField("field_75098_d");
            List<Object> gates=new ArrayList<Object>(),experience=new ArrayList<Object>();
            for(int level=1;level<=100;level++){
                setLevel.invoke(properties,level,hunter);setXp.invoke(properties,0f,hunter);
                for(int needed:requirements){creativeFlag.setBoolean(capabilities,false);boolean survival=(Boolean)hunt.invoke(null,player,needed,damage);creativeFlag.setBoolean(capabilities,true);boolean creative=(Boolean)hunt.invoke(null,player,needed,damage);creativeFlag.setBoolean(capabilities,false);check(survival==(level>=needed)&&creative,"Original native survival/creative gate differs");gates.add(row("level",level,"required",needed,"actualSurvivalAllowed",survival,"actualCreativeAllowed",creative));}
                for(int mode=0;mode<4;mode++)for(float amount:new float[]{0f,.25f,1f,49.5f,50f,999f,10000f,1000000f}){
                    setLevel.invoke(properties,level,hunter);setXp.invoke(properties,0f,hunter);float threshold=((Number)required.invoke(properties,hunter)).floatValue();float xp=mode==0?0f:mode==1?threshold/2f:mode==2?threshold-1f:threshold;
                    setXp.invoke(properties,xp,hunter);add.invoke(properties,amount,hunter);experience.add(row("initialLevel",level,"initialXp",xp,"originalThreshold",threshold,"award",amount,"actualLevel",getLevel.invoke(properties,hunter),"actualXp",getXp.invoke(properties,hunter)));
                }
            }
            report.put("completeNativeGateCases",gates);report.put("completeOriginalExperienceCases",experience);
            check(gates.size()==100*requirements.size()&&experience.size()==3200,"Incomplete original native Hunter workload");
            List<Object> armour=new ArrayList<Object>();Class<?> item=c("net.minecraft.item.Item");
            for(String part:new String[]{"Helmet","Chestplate","Leggings","Boots"}){Object value=c("net.nevermine.izer.equipment.Armorizer").getField("Hunter"+part).get(null);Object id=c("cpw.mods.fml.common.registry.GameRegistry").getMethod("findUniqueIdentifierFor",item).invoke(null,value);Object associated=value.getClass().getMethod("getAssociatedSkill").invoke(value);check(associated==hunter,"Original Hunter armour uses a different skill");armour.add(row("originalField","Armorizer.Hunter"+part,"nativeRegistryIdentity",id.toString(),"nativeClass",value.getClass().getName(),"associatedNativeSkill",associated.toString()));}
            report.put("completeHunterArmour",armour);report.put("passed",true);
            report.put("scope","Every registered original Hunter entity and exact native requirement; every required-level/survival/creative combination over levels1..100;3200actual original container XP cases, including fractional boundaries; all four native armour identities. Original XP defects are observed, not treated as a target improvement. No target, client, projectile, combat, armour-effect, save migration or full gameplay parity inferred.");
        }catch(Throwable error){report.put("error",error.toString());error.printStackTrace();}
        try{Files.write(Paths.get(System.getProperty("enderloom.hunter.output")),new GsonBuilder().serializeNulls().disableHtmlEscaping().create().toJson(report).getBytes(StandardCharsets.UTF_8),StandardOpenOption.CREATE_NEW);}catch(Throwable error){error.printStackTrace();}
    }
}
