import fs from "node:fs";
import path from "node:path";
const root=path.resolve(import.meta.dirname,"..");
const records=path.join(root,".content","behoeften");
const check=process.argv.includes("--check");
let mismatches=0;
for(const file of fs.readdirSync(records).filter(x=>x.endsWith(".json"))){
 const data=JSON.parse(fs.readFileSync(path.join(records,file),"utf8"));
 if(!/^\/voor-gevoelige-honden\/[a-z0-9-]+\/$/.test(data.route))throw Error("Invalid route");
 const target=path.join(root,data.route,"index.html");
 const before=fs.readFileSync(target,"utf8");
 const match=before.match(/<article>[\s\S]*?<\/article>/);
 if(!match)throw Error("Missing article "+target);
 const after=before.replace(match[0],"<article>"+data.article_html+"</article>");
 if(!after.includes('name="robots" content="noindex,follow"'))throw Error("Missing noindex");
 if(before!==after){mismatches++;if(!check)fs.writeFileSync(target,after);}
}
console.log((check?"CHECK":"APPLY")+" Behoeften: "+mismatches+" unsynchronized pages");
if(check&&mismatches)process.exit(1);
