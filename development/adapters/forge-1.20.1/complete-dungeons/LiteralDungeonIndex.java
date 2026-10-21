package net.tslat.aoa3.content.world.gen.compat.dungeons;

import com.google.gson.*;
import java.io.Reader;
import java.util.*;

/** Immutable chunk ownership for the complete authored dungeon programs.
 * The source retains every ordered write, including overwritten writes, old
 * metadata and update-call modes. Chunk indexing changes lookup cost only.
 * Palette identity, native callbacks and actor behavior require separate proof.
 */
public final class LiteralDungeonIndex {
    public record Binding(String originalField,int metadata) {
        public String key(){return originalField+"#"+metadata;}
    }
    public record Write(int x,int y,int z,Binding binding,int flags,String originalCall,int program,int ordinal) {
        public long chunk(){return chunkKey(Math.floorDiv(x,16),Math.floorDiv(z,16));}
        public int cell(){return ((x&15)<<12)|((z&15)<<8)|y;}
    }
    public record Chunk(List<Write> ordered,List<Write> finalWrites) {
        public Chunk {ordered=List.copyOf(ordered);finalWrites=List.copyOf(finalWrites);}
    }
    private static final Chunk EMPTY=new Chunk(List.of(),List.of());
    private final Map<Long,Chunk> chunks;
    private final Set<Binding> bindings;
    private final List<String> programs;
    private final int completeWrites;

    public static long chunkKey(int x,int z){return (x&0xffffffffL)|((z&0xffffffffL)<<32);}
    public static List<String> programNames(String realm){
        List<String> names=new ArrayList<>();
        switch(realm){
            case "ancient_cavern" -> {
                for(int i=1;i<=6;i++)names.add("net.nevermine.structures.ancientcavern.CavernP"+i);
                for(String name:List.of("ConiferonRoom","HoronRoom","PenumbraRoom","GoldorthRoom"))names.add("net.nevermine.structures.ancientcavern."+name);
            }
            case "immortallis" -> {for(int i=1;i<=9;i++)names.add("net.nevermine.structures.immortallis.ImmortalDungeonP"+i);}
            default -> throw new IllegalArgumentException("Unknown original dungeon realm "+realm);
        }
        return List.copyOf(names);
    }
    private static int[] origin(String name){
        if(name.contains(".immortallis."))return new int[]{-15,17,-40};
        return switch(name.substring(name.lastIndexOf('.')+1)){
            case "ConiferonRoom" -> new int[]{-75,15,-75};
            case "HoronRoom" -> new int[]{75,15,-75};
            case "PenumbraRoom" -> new int[]{-75,15,75};
            case "GoldorthRoom" -> new int[]{75,15,75};
            default -> new int[]{-20,15,-20};
        };
    }
    /** The exact shared family is checked before indexing, never sampled. */
    public LiteralDungeonIndex(String realm,Reader source){
        JsonObject family=JsonParser.parseReader(source).getAsJsonObject();
        if(!family.get("format").getAsString().equals("complete-original-literal-shared-family-1"))throw new IllegalArgumentException("Unknown complete literal family format");
        JsonObject members=family.getAsJsonObject("programs");
        Set<String> expected=new HashSet<>(programNames("ancient_cavern"));expected.addAll(programNames("immortallis"));
        if(!members.keySet().equals(expected))throw new IllegalArgumentException("All nineteen original program owners are required");
        programs=programNames(realm);
        JsonArray bases=family.getAsJsonArray("bases"),modes=family.getAsJsonArray("updateCallModes");
        if(bases.size()!=19||modes.size()!=2||!modes.get(0).getAsString().equals("original-default-call")||!modes.get(1).getAsString().equals("2"))throw new IllegalArgumentException("Changed exact complete layout family contract");
        Map<Long,List<Write>> ordered=new LinkedHashMap<>();Set<Binding> allBindings=new LinkedHashSet<>();int total=0;
        for(int owner=0;owner<programs.size();owner++){
            String name=programs.get(owner);int[] offset=origin(name);JsonObject program=members.getAsJsonObject(name);
            JsonArray fields=program.getAsJsonArray("bindings");int base=integer(program.get("base"));
            if(base<0||base>=bases.size()||fields.isEmpty())throw new IllegalArgumentException("Invalid original layout ownership");
            Set<String> unique=new HashSet<>();for(JsonElement field:fields)if(!unique.add(field.getAsString()))throw new IllegalArgumentException("Duplicate original binding");
            JsonArray rows=bases.get(base).getAsJsonArray();
            for(int ordinal=0;ordinal<rows.size();ordinal++){
                JsonArray row=rows.get(ordinal).getAsJsonArray();if(row.size()!=6)throw new IllegalArgumentException("Incomplete ordered layout operation");
                int x=Math.addExact(integer(row.get(0)),offset[0]),y=Math.addExact(integer(row.get(1)),offset[1]),z=Math.addExact(integer(row.get(2)),offset[2]);
                int field=integer(row.get(3)),metadata=integer(row.get(4)),mode=integer(row.get(5));
                if(y<0||y>=256||field<0||field>=fields.size()||metadata<0||metadata>15||mode<0||mode>=modes.size())throw new IllegalArgumentException("Unrepresentable authored layout operation");
                String original=fields.get(field).getAsString();
                if(!original.matches("net/(?:nevermine/izer/Blockizer|minecraft/init/Blocks)\\.[A-Za-z0-9_]+"))throw new IllegalArgumentException("Unaccounted original block owner");
                Binding binding=new Binding(original,metadata);allBindings.add(binding);
                Write write=new Write(x,y,z,binding,mode==0?3:2,modes.get(mode).getAsString(),owner,ordinal);
                ordered.computeIfAbsent(write.chunk(),ignored->new ArrayList<>()).add(write);total++;
            }
        }
        Map<Long,Chunk> indexed=new LinkedHashMap<>();
        for(var entry:ordered.entrySet()){
            // Later programs may overwrite a previous owner's cells. Keep the
            // full ordered program and materialize only its final cell values.
            Map<Integer,Write> finalCells=new LinkedHashMap<>();
            for(Write write:entry.getValue())finalCells.put(write.cell(),write);
            indexed.put(entry.getKey(),new Chunk(entry.getValue(),new ArrayList<>(finalCells.values())));
        }
        chunks=Collections.unmodifiableMap(indexed);bindings=Collections.unmodifiableSet(allBindings);completeWrites=total;
    }
    private static int integer(JsonElement value){
        if(!value.isJsonPrimitive()||!value.getAsJsonPrimitive().isNumber())throw new IllegalArgumentException("Expected an exact integer");
        return value.getAsBigDecimal().intValueExact();
    }
    public Chunk chunk(int x,int z){return chunks.getOrDefault(chunkKey(x,z),EMPTY);}
    public Map<Long,Chunk> chunks(){return chunks;}
    public Set<Binding> bindings(){return bindings;}
    public List<String> programs(){return programs;}
    public int completeWrites(){return completeWrites;}
}
