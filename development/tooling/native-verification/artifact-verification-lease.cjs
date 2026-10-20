'use strict';
// One admission only. Every distinct complete artifact is read and hashed;
// identical references reuse that verified read while file identity is stable.
const fs=require('node:fs');
function fingerprint(file){
 const s=fs.statSync(file,{bigint:true});
 return [s.dev,s.ino,s.size,s.mtimeNs,s.ctimeNs,s.mode].map(String).join(':');
}
function createVerificationLease(verify,{maxStableReadAttempts=3}={}){
 if(typeof verify!=='function'||!Number.isSafeInteger(maxStableReadAttempts)||maxStableReadAttempts<1)throw TypeError('A complete artifact verifier and bounded stable-read attempts are required');
 const verified=new Map();
 const stats={references:0,completeHashVerifications:0,stableDuplicateReferences:0,metadataRetries:0,logicalBytesHashed:0,duplicateLogicalBytesAvoided:0};
 function check(ref){
  stats.references++;
  const key=JSON.stringify(Object.keys(ref).sort().map(name=>[name,ref[name]]));
  let before=fingerprint(ref.path);
  if(verified.get(key)===before){stats.stableDuplicateReferences++;stats.duplicateLogicalBytesAvoided+=ref.bytes;return;}
  for(let attempt=0;attempt<maxStableReadAttempts;attempt++){
   stats.completeHashVerifications++;stats.logicalBytesHashed+=ref.bytes;
   verify(ref);
   const after=fingerprint(ref.path);
   if(before===after){verified.set(key,after);return;}
   stats.metadataRetries++;before=after;
  }
  const error=Error('Artifact kept changing during complete verification: '+ref.path);error.code='ERR_ARTIFACT_CHANGING_DURING_VERIFICATION';throw error;
 }
 return {check,snapshot:()=>({...stats,distinctVerifiedReferenceIdentities:verified.size,scope:'One admission; full hashes for every distinct artifact, no durable or timestamp-only cache'})};
}
module.exports={createVerificationLease};
