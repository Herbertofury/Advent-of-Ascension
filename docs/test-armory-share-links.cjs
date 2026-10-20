'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),M=require('./weapon-concept-gallery.js');let checks=0;
function eq(a,b){assert.deepEqual(a,b);checks++;}
eq(M.readState(''),{query:'',family:'all',weapon:null});
eq(M.readState('?q=Ghoul+Cannon&family=cannon&weapon=aoa3%3Aghoul_cannon'),{query:'Ghoul Cannon',family:'cannon',weapon:'aoa3:ghoul_cannon'});
eq(M.readState('?q=%3Cscript%3E&family=javascript%3Aevil&weapon=https%3A%2F%2Fevil.invalid'),{query:'<script>',family:'all',weapon:null});
for(const query of ['Soul Storm','a+b & c?','Café','幽霊','100%',''])for(const family of ['all','cannon','sniper']){const s={query,family,weapon:null};eq(M.readState(M.stateQuery(s)),s);}
const data=JSON.parse(fs.readFileSync(__dirname+'/weapon-concept-catalog.json'));
for(const w of data.weapons)eq(M.readState(M.stateQuery({weapon:w.id})),{query:'',family:'all',weapon:w.id});
eq(M.readState('?q='+('x'.repeat(500))).query.length,300);
eq(M.stateQuery({query:'test',family:'bad',weapon:'javascript:alert(1)'}),'q=test');
eq(M.readState('?unrelated=value&q=one&q=two').query,'one');
eq(M.stateQuery(M.readState('?q=test&unrelated=value')),'q=test');
console.log(JSON.stringify({status:'PASS',checks,scope:'Filter and exact weapon-link encoding/validation; live dialog and loading behavior require separate checks'}));
