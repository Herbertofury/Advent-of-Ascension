'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const A=require('./weapon-concept-gallery.js');const data=JSON.parse(fs.readFileSync(path.join(__dirname,'weapon-concept-catalog.json')));A.validate(data);
const evidence=JSON.parse(fs.readFileSync(path.join(__dirname,'weapon-dimension-associations.json')));let checks=0;function ok(v){assert.ok(v);checks++;}
for(const w of data.weapons){assert.deepEqual(w.dimension_associations,evidence.weapons[w.id]);checks++;for(const a of w.dimension_associations){ok(w.lanes.includes(a.version));ok(!!evidence.sources[a.source]);}}
const fixtures=[{id:'one',name:'One',brief:'test',families:['gun'],lanes:['1.12.2','1.20.1'],concept:'yes',dimension_associations:[{version:'1.12.2',dimension:'abyss'},{version:'1.20.1',dimension:'haven'},{version:'1.20.1',dimension:'abyss'}]},{id:'two',name:'Two',brief:'test',families:['staff'],lanes:['1.20.1'],concept:null,dimension_associations:[]}];
const f=(q='',family='all',lane='',status='',dim='')=>A.filter(fixtures,q,family,lane,status,dim).map(w=>w.id);
assert.deepEqual(f('','all','','','abyss'),['one']);checks++;
assert.deepEqual(f('','all','1.12.2','','haven'),[]);checks++;
assert.deepEqual(f('','all','1.20.1','','haven'),['one']);checks++;
assert.deepEqual(f('','all','1.20.1','','unmapped'),['two']);checks++;
assert.deepEqual(f('','gun','','','unmapped'),[]);checks++;
assert.deepEqual(f('two','staff','1.20.1','missing','unmapped'),['two']);checks++;
assert.deepEqual(f('','all','','','not_a_dimension'),[]);checks++;
assert.deepEqual(A.dimensions(fixtures[0]),['abyss','haven']);checks++;
for(const mutation of [a=>a.dimension='../bad',a=>a.version='9.9',a=>a.source='../private.json']){const bad=structuredClone(data),w=bad.weapons.find(w=>w.dimension_associations.length);mutation(w.dimension_associations[0]);assert.throws(()=>A.validate(bad));checks++;}
const dims=[...new Set(data.weapons.flatMap(w=>A.dimensions(w)))];for(const d of dims){ok(A.filter(data.weapons,'','all','','',d).every(w=>A.dimensions(w).includes(d)));}
for(const lane of ['', '1.12.2','1.20.1','1.21.1']){const all=A.filter(data.weapons,'','all',lane),unmapped=A.filter(data.weapons,'','all',lane,'','unmapped');ok(unmapped.every(w=>!A.dimensions(w,lane).length));ok(unmapped.length<=all.length);}
const html=fs.readFileSync(path.join(__dirname,'weapon-concepts.html'),'utf8'),js=fs.readFileSync(path.join(__dirname,'weapon-concept-gallery.js'),'utf8');ok(html.includes('id="dimension"'));ok(html.includes('id="dimension-note"'));ok(js.includes("[4,'dimension']"));ok(js.includes("params.get('dimension')"));console.log(JSON.stringify({status:'PASS',checks,mapped:evidence.mapped_id_count,unmapped:data.weapons.length-evidence.mapped_id_count,dimensions:dims.length,native_acceptance:false}));
