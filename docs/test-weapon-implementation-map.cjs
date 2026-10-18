'use strict';
const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const docs=path.resolve(process.argv[2]||'aoa-expansion');const html=fs.readFileSync(path.join(docs,'weapon-implementation-map.html'),'utf8');assert(html.includes('[hidden]{display:none!important}'),'Author CSS must preserve hidden controls');const code=html.match(/<script>([\s\S]*?)<\/script>/)[1];
class Element{constructor(tag){this.tag=tag;this.children=[];this.events={};this.value='';this.hidden=false;this.textContent='';}append(...nodes){this.children.push(...nodes);}replaceChildren(...nodes){this.children=nodes;}addEventListener(event,fn){this.events[event]=fn;}}
const ids=new Map();for(const id of ['cards','search','family','status','more','reset'])ids.set(id,new Element(id));
const box={console,URL,URLSearchParams,document:{getElementById:id=>ids.get(id),createElement:tag=>new Element(tag)},location:{href:'https://example.test/weapon-implementation-map.html',search:''},history:{replaceState(a,b,u){box.location.href=String(u);}},fetch:async file=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(docs,file),'utf8'))})};
(async()=>{vm.createContext(box);vm.runInContext(code,box);await new Promise(r=>setImmediate(r));assert.equal(ids.get('cards').children.length,30);assert.match(ids.get('status').textContent,/228 matching/);ids.get('search').value='discharge_shotgun';ids.get('search').events.input();assert.equal(ids.get('cards').children.length,1);const card=ids.get('cards').children[0];assert(card.children.some(e=>e.tag==='a'&&e.href.endsWith('/Discharge-Shotgun-Weapon-Profile')));const detail=card.children.at(-1);assert.equal(detail.children.length,1);detail.open=true;detail.events.toggle();assert.equal(detail.children.length,4);detail.events.toggle();assert.equal(detail.children.length,4,'Expanded class chain duplicated');ids.get('reset').events.click();assert.equal(ids.get('cards').children.length,30);ids.get('more').events.click();assert.equal(ids.get('cards').children.length,60);ids.get('family').value='blaster';ids.get('family').events.change();assert.match(ids.get('status').textContent,/56 matching/);ids.get('more').events.click();assert.equal(ids.get('cards').children.length,56);assert.equal(ids.get('more').hidden,true);assert(!code.includes('.innerHTML'),'Source data should use text nodes');console.log('PASS initial pagination, exact profile link, lazy one-time class expansion, reset, family filtering, more control and text-only rendering paths. Simulated DOM, not live browser.');})();

(async()=>{
 const delayedIds=new Map();for(const id of ['cards','search','family','status','more','reset'])delayedIds.set(id,new Element(id));
 let release;const gate=new Promise(r=>release=r);let calls=0;
 const delayed={...box,document:{getElementById:id=>delayedIds.get(id),createElement:tag=>new Element(tag)},location:{href:'https://example.test/weapon-implementation-map.html?q=baronator',search:'?q=baronator'},history:{replaceState(){}},fetch:async file=>{calls++;await gate;return {ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(docs,file),'utf8'))}}};
 vm.createContext(delayed);vm.runInContext(code,delayed);assert.equal(delayedIds.get('search').value,'baronator');
 delayedIds.get('search').value='vortex';delayedIds.get('search').events.input();release();await new Promise(r=>setImmediate(r));
 assert.equal(delayedIds.get('search').value,'vortex');assert.equal(delayedIds.get('cards').children.length,1);assert(delayedIds.get('cards').children[0].children.some(x=>x.tag==='a'&&x.href.endsWith('/Vortex-Blaster-Weapon-Profile')));assert.equal(calls,3);
 console.log('PASS slow-load user search survives data arrival; three initial data fetches only.');
})();

(async()=>{
 const localIds=new Map();for(const id of ['cards','search','family','status','more','reset'])localIds.set(id,new Element(id));
 const context={...box,document:{getElementById:id=>localIds.get(id),createElement:tag=>new Element(tag)},location:{href:'https://example.test/',search:'?q=discharge_shotgun'}};
 vm.createContext(context);vm.runInContext(code,context);await new Promise(r=>setImmediate(r));
 function textTree(e){return [e.textContent,...e.children.map(textTree)].join('\n');}
 let text=textTree(localIds.get('cards'));assert.match(text,/Base damage argument: 0/);assert.match(text,/Recoil modifier field: 13/);assert.match(text,/Pellet count field: 4/);
 localIds.get('search').value='light_spark';localIds.get('search').events.input();text=textTree(localIds.get('cards'));assert.match(text,/Base Spirit field: 0/);assert.match(text,/200/);assert.match(text,/impact/);
 localIds.get('search').value='lunar_assault_rifle';localIds.get('search').events.input();text=textTree(localIds.get('cards'));assert.match(text,/random value/);
 localIds.get('search').value='gravity_blaster';localIds.get('search').events.input();text=textTree(localIds.get('cards'));assert.match(text,/Base Spirit field: 120/);assert(!text.includes('Base Spirit field: 12\n'));
 console.log('PASS typed baseline display, zero damage warning, 13 recoil, four pellets, Spark impact exception, Lunar variation and integer formatting.');
})();

(async()=>{
 const localIds=new Map();for(const id of ['cards','search','family','status','more','reset'])localIds.set(id,new Element(id));
 const context={...box,document:{getElementById:id=>localIds.get(id),createElement:tag=>new Element(tag)},location:{href:'https://example.test/',search:''},fetch:async file=>{if(file.includes('baselines-compact'))throw new Error('optional request offline');return {ok:true,json:async()=>JSON.parse(fs.readFileSync(path.join(docs,file),'utf8'))};}};
 vm.createContext(context);vm.runInContext(code,context);await new Promise(r=>setImmediate(r));assert.equal(localIds.get('cards').children.length,30);assert.match(localIds.get('status').textContent,/228 matching/);assert.match(localIds.get('status').textContent,/Optional baseline values unavailable/);
 console.log('PASS optional baseline network failure keeps structural map working with an explicit warning.');
})();
