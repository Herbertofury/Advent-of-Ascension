'use strict';
// Share complete reads across one synchronous admission's nested validators.
// No cached hash survives admission. Changed files are read again, including
// a final stability check after the consumer finishes using its authorities.
const fs=require('node:fs');
const {createVerificationLease}=require('./artifact-verification-lease.cjs');
function createScopedArtifactVerifier(verifyComplete){
 if(typeof verifyComplete!=='function')throw TypeError('A complete byte verifier is required');
 let active=null;
 function verify(record){
  if(!active||typeof record?.path!=='string'||!fs.existsSync(record.path)){
   if(active)active.uncachedReferences++;
   return verifyComplete(record);
  }
  // Additional descriptive fields never change the expected physical bytes.
  // Return the original full record, retaining all provenance and metadata.
  const identity={path:record.path,sha256:record.sha256,bytes:record.bytes};
  active.lease.check(identity);active.identities.set(JSON.stringify(identity),identity);
  return record;
 }
 function run(consume){
  if(active)throw Error('Artifact verification admissions cannot overlap');
  if(typeof consume!=='function')throw TypeError('A synchronous admission is required');
  const scope={lease:createVerificationLease(verifyComplete),identities:new Map(),uncachedReferences:0};active=scope;
  try{
   const value=consume();
   if(value&&typeof value.then==='function')throw TypeError('Artifact verification admission must finish synchronously');
   for(const identity of scope.identities.values())scope.lease.check(identity);
   return {value,verification:{...scope.lease.snapshot(),finalStabilityChecks:scope.identities.size,uncachedReferences:scope.uncachedReferences,nestedValidatorsShareCompleteReads:true}};
  }finally{active=null;}
 }
 return {verify,run};
}
module.exports={createScopedArtifactVerifier};
