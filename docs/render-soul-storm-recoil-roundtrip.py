"""Offline Blender transport preview. Not a TML/game render."""
import bpy,json,sys,argparse
from pathlib import Path
from mathutils import Matrix
R=Path(__file__).resolve().parent;p=argparse.ArgumentParser();p.add_argument('--scene',required=True);a=p.parse_args(sys.argv[sys.argv.index('--')+1:]);bpy.ops.wm.open_mainfile(filepath=str(Path(a.scene).resolve()))
for o in bpy.data.objects:
 if o.type in {'MESH','CURVE','FONT','SURFACE'}:o.hide_render=True
M=Matrix(((0,-1,0),(0,0,1),(-1,0,0))).inverted();image=bpy.data.images.load(str(R/'soul_storm_transport.png'));g=json.loads((R/'soul_storm_transport.geo.json').read_text())['minecraft:geometry'][0]
for b in g['bones']:
 if 'poly_mesh'not in b:continue
 p=b['poly_mesh'];mesh=bpy.data.meshes.new(b['name']);verts=[M@__import__('mathutils').Vector(v)/4 for v in p['positions']];faces=[[x[0]for x in f]for f in p['polys']];mesh.from_pydata(verts,[],faces);mesh.update();o=bpy.data.objects.new(b['name'],mesh);bpy.context.collection.objects.link(o)
 uv=mesh.uv_layers.new(name='Transport UV')
 for face,poly in zip(mesh.polygons,p['polys']):
  for li,idx in zip(face.loop_indices,poly):uv.data[li].uv=p['uvs'][idx[2]]
 mat=bpy.data.materials.new(b['name']);mat.use_nodes=True;n=mat.node_tree.nodes;n.clear();out=n.new('ShaderNodeOutputMaterial');bsdf=n.new('ShaderNodeBsdfPrincipled');tex=n.new('ShaderNodeTexImage');tex.image=image;tex.interpolation='Linear';links=mat.node_tree.links;links.new(tex.outputs['Color'],bsdf.inputs['Base Color']);links.new(tex.outputs['Alpha'],bsdf.inputs['Alpha']);bsdf.inputs['Roughness'].default_value=.5
 if b['name'].endswith('_illuminated'):links.new(tex.outputs['Color'],bsdf.inputs['Emission Color']);bsdf.inputs['Emission Strength'].default_value=1
 links.new(bsdf.outputs['BSDF'],out.inputs['Surface']);mesh.materials.append(mat)

clips=json.loads((R.parent/'soul-storm-recoil-transport-v1/soul_storm_recoil.animation.json').read_text())['animations']
for i,(name,clip)in enumerate(clips.items()):
 for bone,channels in clip['bones'].items():
  ob=bpy.data.objects[bone];ob.location=(0,0,0);ob.keyframe_insert('location',frame=0)
  for t,xyz in channels['position'].items():
   ob.location=M@__import__('mathutils').Vector(xyz)/4;ob.keyframe_insert('location',frame=1+i*6+float(t)*60)
  for fc in ob.animation_data.action.fcurves:
   for key in fc.keyframe_points:key.interpolation='LINEAR'
scene=bpy.context.scene;scene.render.resolution_x=720;scene.render.resolution_y=460;scene.render.resolution_percentage=100;scene.cycles.samples=12;scene.cycles.use_denoising=False;out=R/'roundtrip-motion-frames';out.mkdir(exist_ok=True)
for frame in range(0,25,2):
 scene.frame_set(frame);scene.render.filepath=str(out/f'{frame:03d}.png');bpy.ops.render.render(write_still=True)
