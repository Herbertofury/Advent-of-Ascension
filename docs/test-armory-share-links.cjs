'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),M=require('./weapon-concept-gallery.js');let checks=0;
const empty={query:'',family:'all',lane:'',availability:'',dimension:'',weapon:null};function eq(a,b){assert.deepEqual(a,b);checks++;}
eq(M.readState(''),empty);eq(M.stateQuery(null),'');
eq(M.readState('?q=Ghoul+Gasser&family=blaster&lane=1.20.1&availability=available&dimension=mysterium&weapon=aoa3%3Aghoul_gasser'),{query:'Ghoul Gasser',family:'blaster',lane:'1.20.1',availability:'available',dimension:'mysterium',weapon:'aoa3:ghoul_gasser'});
eq(M.readState('?q=%3Cscript%3E&family=javascript%3Aevil&lane=bad&availability=bad&dimension=..%2Fbad&weapon=https%3A%2F%2Fevil.invalid'),{...empty,query:'<script>'});
for(const query of ['Soul Storm','a+b & c?','Café','幽霊','100%',''])for(const family of ['all','cannon','sniper'])for(const lane of ['','1.20.1'])for(const dimension of ['','mysterium','unmapped']){const s={...empty,query,family,lane,dimension};eq(M.readState(M.stateQuery(s)),s);}
const data=JSON.parse(fs.readFileSync(__dirname+'/weapon-concept-catalog.json'));
for(const w of data.weapons)eq(M.readState(M.stateQuery({weapon:w.id})),{...empty,weapon:w.id});
eq(M.readState('?q='+('x'.repeat(500))).query.length,300);
eq(M.readState('?dimension='+('a'.repeat(65))).dimension,'');
eq(M.readState('?weapon=aoa3:'+('a'.repeat(101))).weapon,null);
eq(M.stateQuery({query:'test',family:'bad',weapon:'javascript:alert(1)',lane:'9.9',dimension:'<bad>'}),'q=test');
eq(M.readState('?unrelated=value&q=one&q=two').query,'one');
eq(M.stateQuery(M.readState('?q=test&unrelated=value')),'q=test');
eq(M.readState('?availability=missing').availability,'missing');
const source=fs.readFileSync(__dirname+'/weapon-concept-gallery.js','utf8');assert(source.includes('const initial=ArmoryCatalog.readState(location.search)'));assert(source.includes('const query=ArmoryCatalog.stateQuery('));checks+=2;
console.log(JSON.stringify({status:'PASS',checks,scope:'Actual shared filter/weapon URL helpers including dimension and release; live DOM behavior requires separate checks'}));
