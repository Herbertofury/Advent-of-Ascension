"""Per-part software preview reduction, preserving source material UV regions."""
import bpy,json,hashlib,argparse,sys
from pathlib import Path
from mathutils import Matrix
R=Path(__file__).resolve().parent;W=R.parent;p=argparse.ArgumentParser();p.add_argument('--source',type=Path,default=W/'carrot-cannon-shared-atlas-v17/carrot-shared-atlas.blend');p.add_argument('--out',type=Path,default=R/'carrot-cannon-study.software-v2.geo.json');a=p.parse_args(sys.argv[sys.argv.index('--')+1:]if '--'in sys.argv else[]);bpy.ops.wm.open_mainfile(filepath=str(a.source));s=bpy.context.scene;s.frame_set(0);bpy.context.view_layer.update();M=Matrix(((0,-1,0),(0,0,1),(-1,0,0)));groups={};parts=[];repairs=[];omitted=[];violations=[];uv_repairs=[];retained_parts=[]
rects={'orange':(8,8,504,504),'leaf':(520,8,1016,504),'wood':(8,520,504,1016),'iron':(520,520,632,632),'silver':(648,520,760,632),'amber':(776,520,888,632),'bore':(904,520,1016,632)}
roles={'Orange grown ceramic':'orange','Golden growth ridges':'orange','Leaf upper wax':'leaf','Rosid root interpretation':'wood','Dark hammered iron':'iron','Worn silver edges':'silver','Amber petal glass':'amber','Dark inner bore':'bore'}
def pool(g,key,value):
 t=tuple(float(v)for v in value);cache=g['_'+key]
 if t not in cache:cache[t]=len(g[key]);g[key].append(list(t))
 return cache[t]
for o in bpy.data.objects:
 if not o.name.startswith('SharedAtlas_')or o.hide_render:continue
 before=o.data;before.calc_loop_triangles();count=len(before.loop_triangles);mod=None
 if count>48 and o.name!='SharedAtlas_Separate trigger':mod=o.modifiers.new('Per-part software reduction','DECIMATE');mod.ratio=.25;mod.use_collapse_triangulate=True
 dg=bpy.context.evaluated_depsgraph_get();e=o.evaluated_get(dg);me=e.to_mesh();me.calc_loop_triangles()
 candidate_error=0
 for poly in me.polygons:
  material=me.materials[poly.material_index].name;role=next(role for prefix,role in roles.items()if material.startswith(prefix));x0,y0,x1,y1=rects[role]
  for li in poly.loop_indices:
   u,v=me.uv_layers['SharedAtlasUV'].data[li].uv;candidate_error=max(candidate_error,max(x0/1024-u,u-x1/1024,y0/1024-v,v-y1/1024,0)*1024)
 if candidate_error>.25 and mod is not None:
  e.to_mesh_clear();o.modifiers.remove(mod);dg=bpy.context.evaluated_depsgraph_get();e=o.evaluated_get(dg);me=e.to_mesh();me.calc_loop_triangles();retained_parts.append({'part':o.name,'candidate_texel_overshoot':candidate_error,'action':'Preserve original geometry and UVs for this part'})
 nm=M@o.matrix_world.to_3x3().inverted().transposed();written=0
 for tri in me.loop_triangles:
  if tri.area<=1e-10:omitted.append({'part':o.name,'triangle':tri.index});continue
  material=me.materials[tri.material_index].name;role=next((role for prefix,role in roles.items()if material.startswith(prefix)),None);assert role,(o.name,material)
  bone='carrot_trigger_pivot'if o.name=='SharedAtlas_Separate trigger'else('carrot_glass_illuminated'if role=='amber'else'carrot_weapon_root');g=groups.setdefault(bone,{'normalized_uvs':True,'positions':[],'normals':[],'uvs':[],'polys':[],'_positions':{},'_normals':{},'_uvs':{}});poly=[];x0,y0,x1,y1=rects[role]
  for li in tri.loops:
   normal=me.corner_normals[li].vector.copy()
   if normal.length<.5:normal=tri.normal.copy();repairs.append({'part':o.name,'loop':li})
   assert normal.length>.5;normal=(nm@normal).normalized();pos=M@(o.matrix_world@me.vertices[me.loops[li].vertex_index].co)*4;uv=me.uv_layers['SharedAtlasUV'].data[li].uv.copy()
   old_uv=list(uv);uv.x=min(max(uv.x,x0/1024),x1/1024);uv.y=min(max(uv.y,y0/1024),y1/1024);error=max(abs(old_uv[i]-uv[i])for i in [0,1])*1024
   if error>0:uv_repairs.append({'part':o.name,'max_texel_correction':error})
   if error>.25:violations.append([o.name,role,old_uv,error])
   poly.append([pool(g,'positions',pos),pool(g,'normals',normal),pool(g,'uvs',uv)])
  g['polys'].append(poly);written+=1
 parts.append({'part':o.name,'source_triangles':count,'preview_triangles':written});e.to_mesh_clear()
assert not violations,violations[:8]
bones=[{'name':'root','pivot':[0,0,0]}]
for name in ['carrot_weapon_root','carrot_trigger_pivot','carrot_glass_illuminated']:bones.append({'name':name,'parent':'root'if name=='carrot_weapon_root'else'carrot_weapon_root','pivot':[0,2.448,3.4]if name=='carrot_trigger_pivot'else[0,0,0],'poly_mesh':{k:v for k,v in groups[name].items()if not k.startswith('_')}})
data={'format_version':'1.12.0','minecraft:geometry':[{'description':{'identifier':'geometry.ascension_armory.carrot_software_preview_v2','texture_width':1024,'texture_height':1024},'bones':bones}]};a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(data,separators=(',',':'))+'\n');receipt={'status':'Per-part reduced browser preview only','source_sha256':hashlib.sha256(a.source.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(a.out.read_bytes()).hexdigest(),'triangles':sum(x['preview_triangles']for x in parts),'parts':parts,'repaired_corner_normals':repairs,'omitted_degenerate_triangles':omitted,'material_region_violations':violations,'uv_boundary_repairs':uv_repairs,'retained_parts':retained_parts,'maximum_texel_correction':max((x['max_texel_correction']for x in uv_repairs),default=0),'native_lod_accepted':False,'limits':['Painter-sorted software view and centroid texture samples are approximate','Not a native LOD or performance benchmark']};(R/'receipt-v2.json').write_text(json.dumps(receipt,indent=2)+'\n');print({k:receipt[k]for k in ['triangles','material_region_violations','native_lod_accepted']})
