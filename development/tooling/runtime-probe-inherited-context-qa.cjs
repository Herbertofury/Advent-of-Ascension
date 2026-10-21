'use strict';
// Actual retained 1.20.1/1.16.5 choices and generated damaged-reference controls.
const fs=require('node:fs'),assert=require('node:assert/strict');
const {artifact}=require('./lib/complete-java-source-qa.cjs');
const {normalize,inheritedContextArgs}=require('./lib/runtime-probe-receipt.cjs');
const [modernFile,originalFile,output]=process.argv.slice(2);
const modern=normalize(modernFile),original=normalize(originalFile);
const modernArgs=inheritedContextArgs(modern,{base:'forge-official-1.20.1',client:false});
for(const flag of ['--worldgen-pack=','--source-block-manifest=','--original-biome-oracle=','--original-material-oracle=','--legacy-terrain-oracle=','--original-entity-oracle=','--original-hunter-oracle=','--source-arena-plan=','--native-api-parent='])assert.equal(modernArgs.filter(a=>a.startsWith(flag)).length,1,flag);
assert(modernArgs.includes('--live-world-generation'));
const oldArgs=inheritedContextArgs(original,{base:'forge-official-1.16.5',client:false});
assert.equal(oldArgs.filter(a=>a.startsWith('--original-api-parent=')).length,1);
assert.equal(oldArgs.filter(a=>a.startsWith('--metadata-java-home=')).length,1);
for(const field of ['canonicalArenaStation','nativeApiPreflight']){
 const damaged=structuredClone(modern);const ref=field==='canonicalArenaStation'?damaged[field].manifest:damaged[field];ref.sha256='0'.repeat(64);
 assert.throws(()=>inheritedContextArgs(damaged,{base:'forge-official-1.20.1',client:false}));
}
const result={passed:true,actualModernToolkit:artifact(modernFile),actualOriginalToolkit:artifact(originalFile),modernArguments:modernArgs,originalArguments:oldArgs,completeRetainedModernContextChoices:modernArgs.length,generatedChangedReferenceRejections:2,gameLaunched:false,producer:artifact(__filename)};
fs.writeFileSync(output,JSON.stringify(result,null,2),{encoding:'utf8',flag:'wx'});
console.log(JSON.stringify({passed:true,completeRetainedModernContextChoices:modernArgs.length,originalApiParentAndMetadataJdkRetained:true,generatedChangedReferenceRejections:2}));
