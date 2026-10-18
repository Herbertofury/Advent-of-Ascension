"""Independent exact whole-JAR and native saved-merchant capture acceptance."""
import hashlib,json,sys,zipfile
from pathlib import Path

def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def artifact(p):
 p=Path(p)
 with p.open("rb") as f:h=hashlib.file_digest(f,"sha256").hexdigest()
 return dict(path=str(p.absolute()),sha256=h,bytes=p.stat().st_size)
def check(r):
 a=artifact(r["path"]);assert all(a[k]==r[k] for k in ["sha256","bytes"]);return r
server_file,plan_file,output=sys.argv[1:]
s,p=read(server_file),read(plan_file)
assert not Path(output).exists()
assert s["passed"] and s["nativeServerAdmissionVerified"] and s["compileVerified"] and s["allPrimaryChoicesAndAuthoritiesUnchanged"]
assert all(check(s["sourceRecipePlan"])[k]==artifact(plan_file)[k] for k in ["sha256","bytes"])
assert p["skillMasterSavedOfferUpgrade"]["foundingContractsRetained"]==9 and p["skillMasterSavedOfferUpgrade"]["armorOfferFamily"]==8
parent=read(check(s["parent"])["path"])
before,current=check(parent["build"]["artifacts"][0]),check(s["build"]["artifacts"][0])
changes=[]
with zipfile.ZipFile(before["path"]) as a,zipfile.ZipFile(current["path"]) as b:
 assert a.namelist()==b.namelist() and len(b.namelist())==len(set(b.namelist()))==24274
 for name in a.namelist():
  left,right=a.read(name),b.read(name)
  if left==right:continue
  if name=="META-INF/MANIFEST.MF":
   clean=lambda x:[v for v in x.decode("utf-8").splitlines() if not v.startswith("Implementation-Timestamp: ")]
   assert clean(left)==clean(right)
  else:assert name=="net/tslat/aoa3/content/entity/npc/trader/SkillMasterEntity.class"
  changes.append(name)
 assert "net/tslat/aoa3/content/entity/npc/trader/SkillMasterEntity.class" in changes
capture=Path(s["capture"]["path"]).with_name("enderloom-forge1201-skill-master-save-upgrade.json")
raw=capture.read_text(encoding="utf-8");v=json.loads(raw)
assert v["passed"] and v["implemented"] and not v["synthetic"] and v["generatedDisposableFixtures"] and not v["completeAoAPort"]
assert v["adapter"]=="canonical-saved-skill-master-offers-1"
assert read(check(s["capture"])["path"])["skillMasterSavedOfferUpgradeInspection"]==v
with Path(s["build"]["stdout_path"]).open(encoding="utf-8") as stream:
 assert sum(line.rstrip("\r\n")=="ENDERLOOM_FORGE1201_SKILL_MASTER_SAVE_UPGRADE "+raw for line in stream)==1
expected={"original-nine":(9,17),"partial-thirteen":(13,17),"custom-extra":(10,18),"custom-armor-price":(10,17),"custom-founding-price":(9,9),"empty-custom-offers":(0,0),"future-schema":(9,9),"unknown-schema":(9,9),"already-upgraded":(17,17)}
assert len(v["cases"])==len(expected) and set(r["case"] for r in v["cases"])==set(expected)
for r in v["cases"]:
 assert (r["before"],r["after"])==expected[r["case"]]
 assert all(r[k] is True for k in ["allExistingOfferTagsUnchanged","forgeExtensionUnchanged","noDuplicateRewards","completeReloadUnchanged","schemaPreserved"])
result=dict(schema=1,passed=True,synthetic=False,server=artifact(server_file),plan=artifact(plan_file),nativeCapture=artifact(capture),canonicalMod=current,previousMod=before,completeJarEntries=24274,changedMembers=changes,completeNativeSaveCases=v["cases"],currentPlayableChanged=False,completeAoAPort=False,scope="Controlled native saved-merchant cases and exact complete-JAR retention. Real player trade screen, natural progression, existing-user-world migration, multiplayer, full union and performance remain open.")
result["verifier"]=artifact(__file__)
Path(output).write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(dict(passed=True,completeCases=len(expected),completeJarEntries=24274,output=output)))
