"""Reduced geometry for a browser software preview, not a native LOD acceptance."""
import bpy,json,hashlib,argparse,sys
from pathlib import Path
R=Path(__file__).resolve().parent;W=R.parent;parser=argparse.ArgumentParser();parser.add_argument('--geometry',type=Path,default=W/'carrot-cannon-transport-v2/carrot_cannon_compact.geo.json');parser.add_argument('--out',type=Path,default=R/'carrot-cannon-study.software.geo.json');args=parser.parse_args(sys.argv[sys.argv.index('--')+1:]if '--'in sys.argv else[]);source=args.geometry;d=json.loads(source.read_text());g=d['minecraft:geometry'][0];bpy.ops.wm.read_factory_settings(use_empty=True);out=[];rows=[];normal_repairs=[];omitted_degenerate=[]
for bone in g['bones']:
 b={k:v for k,v in bone.items()if k!='poly_mesh'};m=bone.get('poly_mesh')
 if m:
  mesh=bpy.data.meshes.new(bone['name']);faces=[[v[0]for v in p]for p in m['polys']];mesh.from_pydata(m['positions'],[],faces);mesh.update();uv=mesh.uv_layers.new(name='AtlasUV');normals=[]
  for poly,corners in zip(mesh.polygons,m['polys']):
   poly.use_smooth=True
   for li,corner in zip(poly.loop_indices,corners):uv.data[li].uv=m['uvs'][corner[2]];normals.append(m['normals'][corner[1]])
  mesh.normals_split_custom_set(normals);o=bpy.data.objects.new(bone['name'],mesh);bpy.context.collection.objects.link(o)
  if len(faces)>500:
   mod=o.modifiers.new('Software preview reduction','DECIMATE');mod.ratio=.12;mod.use_collapse_triangulate=True
  e=o.evaluated_get(bpy.context.evaluated_depsgraph_get());me=e.to_mesh();me.calc_loop_triangles();positions=[list(v.co)for v in me.vertices];ns=[];us=[];polys=[]
  for tri in me.loop_triangles:
   if tri.area<=1e-10:omitted_degenerate.append({'bone':bone['name'],'triangle':tri.index});continue
   p=[]
   for li in tri.loops:
    normal=me.corner_normals[li].vector.copy()
    if normal.length<.5:normal=tri.normal.copy();normal_repairs.append({'bone':bone['name'],'loop':li,'method':'nondegenerate triangle normal'})
    assert normal.length>.5
    normal.normalize();p.append([me.loops[li].vertex_index,len(ns),len(us)]);ns.append(list(normal));us.append(list(me.uv_layers.active.data[li].uv))
   polys.append(p)
  b['poly_mesh']={'normalized_uvs':True,'positions':positions,'normals':ns,'uvs':us,'polys':polys};rows.append({'bone':bone['name'],'source_triangles':len(faces),'preview_triangles':len(polys)});e.to_mesh_clear()
 out.append(b)
g['bones']=out;g['description']['identifier']='geometry.ascension_armory.carrot_software_preview';target=args.out;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(d,separators=(',',':'))+'\n');receipt={'status':'Reduced browser software-preview geometry only','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'bones':rows,'triangles':sum(x['preview_triangles']for x in rows),'repaired_corner_normals':normal_repairs,'omitted_degenerate_triangles':omitted_degenerate,'native_lod_accepted':False,'limits':['Lower-detail appearance and painter-sorted software rendering are approximate','Not a native TaCZ LOD or performance benchmark']};(R/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(receipt)
