import fs from "node:fs";
import path from "node:path";
const root=path.resolve(import.meta.dirname,"..");
const records=path.join(root,".content","behoeften");
const required=["01-audit.md","02-brief.md","03-claims.json","04-draft.md","05-review.md","06-corrections.md"];
let errors=[],checked=0;
for(const filename of fs.readdirSync(records).filter(x=>x.endsWith(".json"))){
 const slug=filename.slice(0,-5),run=path.join(records,"runs",slug);
 // Only enforce the full editorial gate on pages registered for a complete run.
 if(!fs.existsSync(run))continue;
 checked++;
 for(const file of required){const p=path.join(run,file);if(!fs.existsSync(p)||fs.statSync(p).size<80)errors.push(slug+" missing/incomplete "+file);}
 const claimsFile=path.join(run,"03-claims.json");
 if(fs.existsSync(claimsFile)){
  try{
   const data=JSON.parse(fs.readFileSync(claimsFile,"utf8"));
   if(!Array.isArray(data.claims)||!data.claims.length)errors.push(slug+" claims missing");
   else for(const [i,c] of data.claims.entries()){
    if(!["CONFIRMED","PARTIAL","UNVERIFIED","CONTRADICTED","OUTDATED"].includes(c.status))errors.push(slug+" claim "+i+" invalid status");
    if(c.status==="CONFIRMED" && !/^https:\/\//.test(c.source||""))errors.push(slug+" claim "+i+" lacks source");
   }
  }catch(e){errors.push(slug+" invalid claims JSON "+e.message);}
 }
 const reviewFile=path.join(run,"05-review.md");
 if(fs.existsSync(reviewFile)){
  const review=fs.readFileSync(reviewFile,"utf8");
  if(!/PASS — READY_FOR_HUMAN_VALIDATION|FAIL — KEEP_NOINDEX/.test(review))errors.push(slug+" missing exact review verdict");
  if(/FAIL — KEEP_NOINDEX/.test(review) && /name="robots" content="index,follow"/.test(fs.readFileSync(path.join(root,"voor-gevoelige-honden",slug,"index.html"),"utf8")))errors.push(slug+" failed review indexed");
 }
}
if(errors.length){console.error(errors.join("\n"));process.exit(1);}
console.log("PASS: "+checked+" registered Behoeften run(s) have complete evidence-record structure; this is NOT an editorial or veterinary approval.");
