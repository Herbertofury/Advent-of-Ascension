const fs=require('node:fs');const path=require('node:path');const crypto=require('node:crypto');const assert=require('node:assert/strict');
const read=n=>JSON.parse(fs.readFileSync(path.join(__dirname,n),'utf8'));const receipt=read('archergun-preserved-designs.json');const catalog=read('weapon-concept-catalog.json');let checks=0;
assert.equal(receipt.designs.length,4);checks++;
for(const row of receipt.designs){const w=catalog.weapons.find(w=>w.id===row.id);assert.ok(w);checks++;assert.equal(w.concept,row.selected_artwork);checks++;const bytes=fs.readFileSync(path.join(__dirname,row.selected_artwork));assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),row.sha256);checks++;}
assert.equal(receipt.current_redesign_target,'aoa3:viral_archergun');checks++;console.log(JSON.stringify({status:'PASS',checks,scope:'Four owner-preserved selected artwork filenames and exact bytes; not art fidelity or native acceptance'}));
