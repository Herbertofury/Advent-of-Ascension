'use strict';
const ArmoryCatalog=(()=>{
 const families=new Set(['gun','shotgun','sniper','cannon','blaster']);
 function validate(data){
  if(data.schema_version!==1||!Array.isArray(data.weapons)||data.weapons.length>1000||!Number.isInteger(data.inventory_count)||data.inventory_count<data.weapons.length||!Number.isInteger(data.native_accepted)||data.native_accepted<0||data.native_accepted>data.inventory_count)throw Error('Invalid collection metadata');
  const ids=new Set();for(const w of data.weapons){
   if(!/^aoa3:[a-z0-9_]+$/.test(w.id)||ids.has(w.id)||!families.has(w.family)||typeof w.name!=='string'||!w.name||typeof w.brief!=='string'||typeof w.native_accepted!=='boolean')throw Error('Invalid weapon entry');ids.add(w.id);
   if(!/^concept-thumb-[a-z0-9_]+\.webp$/.test(w.thumbnail))throw Error('Invalid thumbnail path');
   for(const k of ['sprite','concept'])if(!/^[a-z0-9][a-z0-9._-]*\.png$/.test(w[k]))throw Error('Invalid image path');
   if(!/^https:\/\/github\.com\/Herbertofury\/Advent-of-Ascension\/wiki\/[A-Za-z0-9-]+$/.test(w.profile))throw Error('Invalid profile link');
   if(w.interactive&&!/^[a-z0-9-]+\.html(?:\?revision=[a-f0-9]+)?$/.test(w.interactive))throw Error('Invalid preview link');
  }if(data.weapons.filter(w=>w.native_accepted).length>data.native_accepted)throw Error('Acceptance count mismatch');return data;
 }
 function filter(weapons,query,family){const needle=query.trim().toLocaleLowerCase();return weapons.filter(w=>(family==='all'||w.family===family)&&(!needle||[w.name,w.id,w.brief,w.family].join(' ').toLocaleLowerCase().includes(needle)));}
 return {validate,filter};
})();
if(typeof module!=='undefined')module.exports=ArmoryCatalog;
if(typeof document!=='undefined')(async()=>{
 const el=id=>document.getElementById(id),grid=el('collection'),dialog=el('detail'),search=el('search'),family=el('family');let data,returnFocus;
 const node=(tag,text,className)=>{const n=document.createElement(tag);if(text)n.textContent=text;if(className)n.className=className;return n;};
 function openDetail(w,button){returnFocus=button;el('detail-name').textContent=w.name;el('detail-brief').textContent=w.brief;el('detail-original').src=w.sprite;el('detail-original').alt='Released '+w.name+' sprite';el('detail-concept').src=w.concept;el('detail-concept').alt=w.name+' upgrade concept, not in-game';el('detail-profile').href=w.profile;dialog.showModal();el('close-detail').focus();}
 el('close-detail').addEventListener('click',()=>dialog.close());dialog.addEventListener('close',()=>returnFocus?.focus());
 function render(){const rows=ArmoryCatalog.filter(data.weapons,search.value,family.value);grid.replaceChildren();el('empty').hidden=rows.length>0;el('status').textContent=`${rows.length} of ${data.weapons.length} published concepts · ${data.native_accepted} native upgrades accepted`;
  for(const w of rows){const card=node('article',null,'card'),button=node('button',null,'art');button.type='button';button.setAttribute('aria-label','Inspect '+w.name+' concept');const art=node('img');art.src=w.thumbnail;art.alt=w.name+' proposed upgrade';art.loading='lazy';art.decoding='async';art.width=600;art.height=400;button.append(art,node('span','CONCEPT · NOT IN-GAME'));button.addEventListener('click',()=>openDetail(w,button));art.addEventListener('error',()=>{art.hidden=true;button.append(node('p','Image unavailable. Open the source profile.'));});const body=node('div',null,'card-body'),identity=node('div',null,'identity'),sprite=node('img',null,'sprite');sprite.src=w.sprite;sprite.alt='Released '+w.name+' sprite';sprite.loading='lazy';sprite.width=68;sprite.height=68;const label=node('div');label.append(node('div',w.family,'family'),node('h2',w.name),node('div','Released sprite shown at left','source-label'));identity.append(sprite,label);const links=node('div',null,'links'),profile=node('a','Source & full profile');profile.href=w.profile;links.append(profile);if(w.interactive){const link=node('a','Interactive authoring study');link.href=w.interactive;links.append(link);}body.append(identity,node('p',w.brief,'brief'),links);card.append(button,body);grid.append(card);}
 }
 search.addEventListener('input',()=>{if(data)render();});family.addEventListener('change',()=>{if(data)render();});el('clear').addEventListener('click',()=>{search.value='';family.value='all';if(data)render();search.focus();});
 try{const response=await fetch('weapon-concept-catalog.json?v=43');if(!response.ok)throw Error('Collection unavailable');data=ArmoryCatalog.validate(await response.json());el('concept-count').textContent=data.weapons.length;el('inventory-count').textContent=data.inventory_count;el('accepted-count').textContent=data.native_accepted;render();}catch(error){el('status').textContent='The collection could not load. Use the weapon wiki link above.';search.disabled=true;family.disabled=true;el('clear').disabled=true;}
})();
