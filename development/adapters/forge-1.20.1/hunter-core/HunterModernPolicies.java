package net.tslat.aoa3.event;

import java.util.*;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;
import net.minecraftforge.registries.ForgeRegistries;
import net.tslat.aoa3.common.registration.AoAConfigs;

/** Later released configurable, exact-class registrations. Resolve factories
 * once per server/configuration, never scan entities or read files on a tick. */
public final class HunterModernPolicies {
    public record Policy(int requiredLevel,float reward,ResourceLocation id){}
    private static volatile Map<Class<?>,Policy> policies;
    private static volatile List<String> unresolved=List.of();
    private static volatile List<? extends String> configuration;
    private HunterModernPolicies(){}
    public static synchronized void invalidate(){policies=null;configuration=null;unresolved=List.of();}
    public static List<String> unresolved(){return unresolved;}
    public static Map<Class<?>,Policy> all(Level level){ensure(level);return policies;}
    public static Policy get(LivingEntity entity){ensure(entity.level());return policies.get(entity.getClass());}
    private static void ensure(Level level){
        List<? extends String> current=AoAConfigs.SERVER.hunterEntities.get();
        if(policies!=null&&Objects.equals(configuration,current))return;
        synchronized(HunterModernPolicies.class){
            if(policies!=null&&Objects.equals(configuration,current))return;
            Map<Class<?>,Policy> selected=new LinkedHashMap<>();List<String> rejected=new ArrayList<>();
            for(String entry:current){
                try{
                    String[] parts=entry.split(" ");
                    if(parts.length<3)throw new IllegalArgumentException("Expected registry_id lvl:N xp:N");
                    ResourceLocation id=new ResourceLocation(parts[0]);
                    int required=Math.max(1,Math.min(100,Integer.parseInt(parts[1].replace("lvl:",""))));
                    float reward=Float.parseFloat(parts[2].replace("xp:",""));
                    if(!Float.isFinite(reward))throw new IllegalArgumentException("Non-finite Hunter XP");
                    reward=Math.max(0,reward);
                    if(!ForgeRegistries.ENTITY_TYPES.containsKey(id)){rejected.add(entry+" [unregistered entity]");continue;}
                    Entity entity=ForgeRegistries.ENTITY_TYPES.getValue(id).create(level);
                    if(!(entity instanceof LivingEntity)){rejected.add(entry+" [non-living factory]");continue;}
                    // Identical Java classes deliberately share one first-wins
                    // registration, matching the later author's actual parser.
                    selected.putIfAbsent(entity.getClass(),new Policy(required,reward,id));
                    entity.discard();
                }catch(IllegalArgumentException failure){rejected.add(entry+" ["+failure.getMessage()+"]");}
            }
            unresolved=List.copyOf(rejected);configuration=List.copyOf(current);policies=Collections.unmodifiableMap(selected);
        }
    }
}
