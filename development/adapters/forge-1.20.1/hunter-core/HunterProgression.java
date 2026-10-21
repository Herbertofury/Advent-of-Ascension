package net.tslat.aoa3.player.skill;

/** Exact observed Tslat-era Hunter arithmetic, independent of game adapters.
 * The original binary subtracts the previous threshold before levelUp. CFR's
 * reconstructed for-loop moves that expression after levelUp; do not use it.
 * Every float boundary is verified against the unchanged original runtime.
 */
public final class HunterProgression {
    public record State(int level,float xp){}
    private static final float[] THRESHOLDS=thresholds();
    private HunterProgression(){}
    private static float[] thresholds(){
        float[] values=new float[101];
        for(int level=1;level<=100;level++)values[level]=(float)(Math.pow(1.1,level-1)*50.0);
        return values;
    }
    public static float threshold(int level){
        if(level<1||level>100)throw new IllegalArgumentException("Hunter level outside original domain");
        return THRESHOLDS[level];
    }
    public static State award(int level,float xp,float amount){
        if(!Float.isFinite(xp)||!Float.isFinite(amount)||xp<0||amount<0)throw new IllegalArgumentException("Invalid Hunter experience");
        float required=threshold(level);
        if(level==100&&(int)Math.floor(xp/required*100f)==100)return new State(level,xp);
        float remaining=amount;
        while(remaining>=required-xp){
            remaining-=required-xp;
            if(level>=100)return new State(level,xp);
            level++;xp=0;required=threshold(level);
        }
        return new State(level,xp+remaining);
    }
    public static boolean canHunt(int level,int requirement,boolean creative){
        threshold(level);
        if(requirement<0||requirement>100)throw new IllegalArgumentException("Hunter requirement outside observed original domain");
        return creative||level>=requirement;
    }
    /** Earlier Snapshot Evercron policy: its integer residual truncation is
     * intentional source behavior, not the later container's float algorithm. */
    public static State awardSnapshot(int level,float xp,int amount){
        threshold(level);
        if(!Float.isFinite(xp)||xp<0||amount<0)throw new IllegalArgumentException("Invalid Snapshot Hunter experience");
        boolean run=true;
        while(run){
            float required=threshold(level),left=required-xp;boolean advance;
            if(amount>left){amount=(int)(amount-left);advance=true;}
            else{xp+=amount;amount=0;advance=xp>=required;run=false;}
            if(advance){level=Math.min(100,level+1);xp=0;}
        }
        return new State(level,xp);
    }
}
