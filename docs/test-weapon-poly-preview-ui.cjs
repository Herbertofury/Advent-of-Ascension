'use strict';
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const elements=new Map(),queue=new Map(),fetches=[];let clock=0,id=0,drawn=0;
const context2d={drawImage(){},getImageData(){return {data:new Uint8ClampedArray([100,120,80,255])};},fillRect(){},beginPath(){},moveTo(){},lineTo(){},closePath(){},fill(){drawn++;},stroke(){}};
function element(name){if(!elements.has(name))elements.set(name,{id:name,hidden:name==='viewer',disabled:true,checked:false,value:'0',dataset:{},clientWidth:800,clientHeight:480,width:800,height:480,textContent:'',events:{},addEventListener(type,fn){this.events[type]=fn;},getContext(type){return type==='webgl'?null:context2d;},setPointerCapture(){}});return elements.get(name);}
const ready=['recoil','reset','zoom-in','zoom-out','timeline','motion'].map(element);
const document={hidden:false,events:{},getElementById:element,querySelectorAll(){return ready;},createElement(){return {width:1,height:1,getContext(){return context2d;}};},addEventListener(type,fn){this.events[type]=fn;}};
const sandbox={document,console,performance:{now:()=>clock},devicePixelRatio:1,matchMedia:()=>({matches:false}),ResizeObserver:class{observe(){}},requestAnimationFrame(fn){queue.set(++id,fn);return id;},cancelAnimationFrame(n){queue.delete(n);},Image:class{constructor(){this.width=1;this.height=1;}set src(value){fetches.push(value);queueMicrotask(()=>this.onload());}},fetch:async url=>{fetches.push(url);return {ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(__dirname,url)))};}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'weapon-poly-preview.js'),'utf8'),sandbox);
const emit=(name,type,event={})=>element(name).events[type](event);
function frame(t){clock=t;const entry=queue.entries().next().value;if(entry){queue.delete(entry[0]);entry[1](t);}}
(async()=>{
 await new Promise(resolve=>setImmediate(resolve));
 assert.match(element('status').textContent,/6,111 triangles.*software/);assert.equal(element('viewer').hidden,false);assert.equal(element('fallback').hidden,true);assert.ok(drawn>0);assert.equal(queue.size,0);assert.ok(ready.every(x=>!x.disabled));
 assert.deepEqual(fetches,['carrot-cannon-study.software.geo.json','carrot-cannon-study.animation.json','carrot-cannon-study-basecolor.png']);
 emit('recoil','click');assert.equal(queue.size,1);frame(80);assert.equal(element('clip-time').textContent,'0.080 s');assert.equal(queue.size,1);
 clock=100;emit('recoil','click');emit('recoil','click');assert.equal(queue.size,1);frame(900);assert.equal(element('clip-time').textContent,'0.800 s');assert.equal(queue.size,0);assert.match(element('status').textContent,/ready pose restored/);
 element('timeline').value='.03';emit('timeline','input');frame(1000);assert.equal(element('clip-time').textContent,'0.030 s');
 emit('reset','click');frame(1100);assert.equal(element('clip-time').textContent,'0.000 s');assert.equal(queue.size,0);
 element('motion').checked=false;emit('motion','change');frame(1200);emit('recoil','click');assert.match(element('status').textContent,/Motion preview is off/);assert.equal(queue.size,0);
 emit('viewer','pointerdown',{clientX:1,clientY:2,pointerId:1});emit('viewer','pointermove',{clientX:4,clientY:8,pointerId:1});frame(1300);emit('viewer','pointercancel');emit('viewer','pointermove',{clientX:8,clientY:12,pointerId:1});assert.equal(queue.size,0);
 emit('viewer','keydown',{key:'ArrowLeft',preventDefault(){}});frame(1400);assert.equal(queue.size,0);
 element('motion').checked=true;clock=1500;emit('recoil','click');document.hidden=true;document.events.visibilitychange();assert.equal(queue.size,0);assert.match(element('status').textContent,/paused while hidden/);document.hidden=false;document.events.visibilitychange();frame(1600);assert.equal(queue.size,0);
 assert.equal(fetches.length,3);
 console.log(JSON.stringify({status:'PASS',scenarios:12,softwareFacesDrawn:drawn,dynamicAssetLoads:fetches.length,scope:'Simulated DOM/Canvas2D control-flow fixture; real browser, pixels and WebGL remain separate checks'}));
})().catch(error=>{console.error(error);process.exitCode=1;});
