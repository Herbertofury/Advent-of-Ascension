'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),M=require('./weapon-concept-gallery.js'),root=__dirname;
const catalog=JSON.parse(fs.readFileSync(path.join(root,'weapon-concept-catalog.json'))),config=fs.readFileSync(path.join(root,'_config.yml'),'utf8');
const excluded=new Set(config.split('\n').filter(l=>l.trim().startsWith('- ')).map(l=>JSON.parse(l.trim().slice(2))));let checks=0;
for(const file of excluded){assert.ok(!file.includes('..')&&!file.startsWith('/')&&fs.existsSync(path.join(root,file)));assert.ok(file.endsWith('.zip')||catalog.weapons.some(w=>w.concept===file));checks+=2;}
for(const w of catalog.weapons){const url=new URL(M.conceptSource(w.concept));assert.equal(url.origin,'https://raw.githubusercontent.com');assert.equal(url.pathname,'/Herbertofury/Advent-of-Ascension/main/docs/'+w.concept);assert.ok(excluded.has(w.concept));assert.ok(fs.existsSync(path.join(root,w.concept)));assert.ok(!excluded.has(w.thumbnail));assert.ok(!excluded.has(w.sprite));checks+=6;}
for(const bad of ['../x.png','//evil.test/x.png','https://evil.test/x.png','x.png?token=x','x%2fy.png','x.png#x','x.svg','',null,42]){assert.throws(()=>M.conceptSource(bad));checks++;}
const code=fs.readFileSync(path.join(root,'weapon-concept-gallery.js'),'utf8');assert.ok(code.includes("el('detail-concept').src=ArmoryCatalog.conceptSource(w.concept)"));assert.ok(code.includes('art.src=w.thumbnail'));checks+=2;
console.log(JSON.stringify({status:'PASS',checks,scope:'Full art stays in repository; fixed-origin modal URLs and local thumbnails. Live image loading remains separate.'}));
