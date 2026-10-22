'use strict';
const fsPub=require('node:fs');const pathPub=require('node:path');const assertPub=require('node:assert/strict');
const rootPub=__dirname;const catalogPub=JSON.parse(fsPub.readFileSync(pathPub.join(rootPub,'weapon-concept-catalog.json'),'utf8'));
const requiredPub=new Set(['weapon-concepts.html','weapon-concept-gallery.js','weapon-concept-catalog.json','weapon-concept-publication.json']);
for(const w of catalogPub.weapons){if(w.thumbnail)requiredPub.add(w.thumbnail);if(w.original&&w.original.sheet)requiredPub.add(w.original.sheet);}
let inExcludePub=false;const excludesPub=[];
for(const line of fsPub.readFileSync(pathPub.join(rootPub,'_config.yml'),'utf8').split(/\r?\n/)){
 if(/^exclude:\s*$/.test(line)){inExcludePub=true;continue;}
 if(inExcludePub&&/^-\s+/.test(line)){excludesPub.push(line.replace(/^-\s+/,'').trim().replace(/^['"]|['"]$/g,''));continue;}
 if(inExcludePub&&/^\S/.test(line)&&!line.startsWith('#'))inExcludePub=false;
}
function excludedPub(file,pattern){if(file===pattern||file.startsWith(pattern.replace(/\/$/,'')+'/'))return true;const re='^'+pattern.split('*').map(p=>p.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('.*')+'$';return new RegExp(re).test(file);}
function validatePub(excludes){for(const file of requiredPub){assertPub(fsPub.existsSync(pathPub.join(rootPub,file)),`Missing dependency: ${file}`);for(const ex of excludes)assertPub(!excludedPub(file,ex),`Jekyll excludes required dependency ${file}: ${ex}`);}}
validatePub(excludesPub);let regressionsPub=0;
for(const broken of ['weapon-concepts.html','weapon-concept-gallery.js','weapon-concept-catalog.json','weapon-concept-publication.json',Array.from(requiredPub).find(x=>x.startsWith('concept-thumb-')),'previews','*.webp']){assertPub.throws(()=>validatePub([...excludesPub,broken]));regressionsPub++;}
console.log(JSON.stringify({status:'PASS',public_dependencies:requiredPub.size,negative_exclusion_regressions:regressionsPub,scope:'Jekyll publication inclusion, not native acceptance'}));
