package net.tslat.aoa3.content.world.gen.structure.processor;

import com.mojang.serialization.Codec;
import net.minecraft.core.BlockPos;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.Tag;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructurePlaceSettings;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureProcessor;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureProcessorType;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplate;
import net.tslat.aoa3.common.registration.worldgen.AoAStructureProcessors;

import java.util.Set;

/** Target-native entity placement data; original template bytes remain intact.
 * Forge supplies the already mirrored, rotated and translated attachment cell.
 * Existing saved entities/chunks never pass through this processor. */
public final class TemplateEntityDataProcessor extends StructureProcessor {
    public static final TemplateEntityDataProcessor INSTANCE = new TemplateEntityDataProcessor();
    public static final Codec<TemplateEntityDataProcessor> CODEC = Codec.unit(INSTANCE);
    private static final Set<ResourceLocation> TEMPLATES = Set.of(
        new ResourceLocation("aoa3:precasia/feature/opteryx_nest_1"),
        new ResourceLocation("aoa3:precasia/feature/opteryx_nest_2"),
        new ResourceLocation("aoa3:precasia/feature/opteryx_nest_3"),
        new ResourceLocation("aoa3:precasia/feature/opteryx_nest_4"),
        new ResourceLocation("aoa3:precasia/feature/opteryx_nest_5"),
        new ResourceLocation("aoa3:lunalus/zal_ship/front"),
        new ResourceLocation("aoa3:lunalus/zal_ship/middle"),
        new ResourceLocation("aoa3:nowhere/boss/arena/structure/city"));

    private TemplateEntityDataProcessor() {}
    public static boolean appliesTo(ResourceLocation template) { return TEMPLATES.contains(template); }

    @Override
    public StructureTemplate.StructureEntityInfo processEntity(LevelReader level, BlockPos origin,
            StructureTemplate.StructureEntityInfo original, StructureTemplate.StructureEntityInfo processed,
            StructurePlaceSettings settings, StructureTemplate template) {
        if (processed == null || processed.nbt == null) return processed;
        CompoundTag data = processed.nbt;
        String identity = data.getString("id");
        boolean hanging = identity.equals("minecraft:painting") || identity.equals("minecraft:item_frame")
            || identity.equals("minecraft:glow_item_frame");
        boolean emptyBrain = identity.equals("aoa3:opteryx") && (!data.contains("Brain")
            || (data.contains("Brain", Tag.TAG_COMPOUND) && data.getCompound("Brain").isEmpty()));
        if (!hanging && !emptyBrain) return processed;
        CompoundTag updated = data.copy();
        if (hanging) {
            updated.putInt("TileX", processed.blockPos.getX());
            updated.putInt("TileY", processed.blockPos.getY());
            updated.putInt("TileZ", processed.blockPos.getZ());
        }
        if (emptyBrain) {
            CompoundTag brain = new CompoundTag();
            brain.put("memories", new CompoundTag());
            updated.put("Brain", brain);
        }
        return updated.equals(data) ? processed
            : new StructureTemplate.StructureEntityInfo(processed.pos, processed.blockPos, updated);
    }

    @Override
    protected StructureProcessorType<?> getType() { return AoAStructureProcessors.TEMPLATE_ENTITY_DATA.get(); }
}
