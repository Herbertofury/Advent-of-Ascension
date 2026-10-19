'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const M=require('./weapon-poly-preview.js');
const geo=JSON.parse(fs.readFileSync(path.join(__dirname,'carrot-cannon-study.geo.json')));
const anim=JSON.parse(fs.readFileSync(path.join(__dirname,'carrot-cannon-study.animation.json')));
const model=M.compile(geo,anim);
assert.equal(model.triangles,49616);assert.equal(model.meshes.length,3);
let checks=2;
function near(a,b,eps=1e-6){assert.equal(a.length,b.length);for(let i=0;i<a.length;i++){assert.ok(Math.abs(a[i]-b[i])<eps,`${a[i]} vs ${b[i]}`);checks++;}}
near(M.point(M.translation([1,2,3]),[2,3,4]),[3,5,7]);
near(M.point(M.rotationX(90),[0,1,0]),[0,0,1]);
for(const t of [0,.8,2])for(const value of M.pose(model,t).values())near(value,M.identity());
for(let i=0;i<=192;i++){
 const poses=M.pose(model,i*.8/192),pivot=model.bones.get('carrot_trigger_pivot').pivot;
 near(M.point(poses.get('carrot_trigger_pivot'),pivot),M.point(poses.get('carrot_weapon_root'),pivot));
 near(poses.get('carrot_glass_illuminated'),poses.get('carrot_weapon_root'));
 for(const matrix of poses.values())assert.ok(matrix.every(Number.isFinite));
}
near(M.sample([[0,[0,0,0]],[1,[2,4,6]]],.5),[1,2,3]);
function badGeometry(change){const g=structuredClone(geo);change(g['minecraft:geometry'][0].bones);assert.throws(()=>M.compile(g,anim));checks++;}
badGeometry(b=>b.push(b[0]));badGeometry(b=>b[1].parent='missing');badGeometry(b=>b[0].parent=b[1].name);
badGeometry(b=>b.find(x=>x.poly_mesh).poly_mesh.polys[0][0][0]=-1);
badGeometry(b=>b.find(x=>x.poly_mesh).poly_mesh.positions[0][0]=1e100);
badGeometry(b=>b.find(x=>x.poly_mesh).poly_mesh.normals[0]=[0,0,0]);
badGeometry(b=>b.find(x=>x.poly_mesh).poly_mesh.uvs[0]=[2,0]);
badGeometry(b=>b.find(x=>x.poly_mesh).poly_mesh.normalized_uvs=false);
const broken=structuredClone(anim);broken.animations.carrot_cannon_shoot.bones.carrot_weapon_root.rotation['0.000000000']=[0,1,0];assert.throws(()=>M.compile(geo,broken));checks++;
assert.throws(()=>M.pose(model,NaN));checks++;
const software=M.compile(JSON.parse(fs.readFileSync(path.join(__dirname,'carrot-cannon-study.software.geo.json'))),anim);
assert.equal(software.triangles,6111);assert.equal(software.meshes.length,3);checks+=2;
for(const t of [0,.03,.15,.8])for(const [name,matrix]of M.pose(software,t))near(matrix,M.pose(model,t).get(name));
console.log(JSON.stringify({status:'PASS',checks,triangles:model.triangles,meshGroups:model.meshes.length,softwareTriangles:software.triangles,scope:'Data validation, sampled transform math and negative fixtures; browser/GPU/gameplay are separate checks'}));
