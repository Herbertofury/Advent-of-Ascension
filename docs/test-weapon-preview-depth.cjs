'use strict';
const assert=require('node:assert/strict'),M=require('./weapon-poly-preview.js');
const w=20,h=20,q=[1,1,18,1,1,18],red=[255,0,0],blue=[0,0,255];let checks=0;
function draw(order){const pixels=new Uint8ClampedArray(w*h*4),depth=new Float64Array(w*h).fill(Infinity);for(const [z,c]of order)M.rasterSolid(pixels,depth,w,h,q,z,c);return {pixels,depth};}
const a=[[-.8,.8,-.8],red],b=[[.213,-.187,.213],blue];const first=draw([a,b]),second=draw([b,a]);assert.deepEqual(first,second);checks++;
function color(image,x,y){return [...image.pixels.slice((y*w+x)*4,(y*w+x)*4+3)];}
assert.deepEqual(color(first,2,2),red);checks++;assert.deepEqual(color(first,14,2),blue);checks++;
for(const z of [-2,2]){assert.equal(draw([[[z,z,z],red]]).pixels.some(x=>x!==0),false);checks++;}
const empty=draw([]);M.rasterSolid(empty.pixels,empty.depth,w,h,[1,1,1,1,1,1],[0,0,0],red);assert.equal(empty.pixels.some(x=>x!==0),false);checks++;
const reversed=new Uint8ClampedArray(w*h*4),depth=new Float64Array(w*h).fill(Infinity);M.rasterSolid(reversed,depth,w,h,[1,1,1,18,18,1],[0,0,0],red);assert.deepEqual(reversed,draw([[[0,0,0],red]]).pixels);checks++;
// Equal-depth surfaces intentionally keep the first writer; this does not solve coplanar geometry.
assert.deepEqual(color(draw([[[0,0,0],red],[[0,0,0],blue]]),2,2),red);checks++;
console.log(JSON.stringify({status:'PASS',checks,scope:'Software depth interpolation, crossing-surface draw-order independence, winding, clipping and degenerate triangle fixtures; no native acceptance'}));
