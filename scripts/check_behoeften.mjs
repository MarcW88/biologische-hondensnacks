import fs from "node:fs";
import path from "node:path";
const root = path.resolve(import.meta.dirname, "..");
const routes = ["", "hypoallergene-hondensnacks", "mono-eiwit-hondensnacks", "graanvrije-hondensnacks", "hondensnacks-gevoelige-maag", "vetarme-hondensnacks"];
const failures = [];
let drafts = 0;
for (const slug of routes) {
  const route = "/voor-gevoelige-honden/" + (slug ? slug + "/" : "");
  const filepath = path.join(root, "voor-gevoelige-honden", slug, "index.html");
  if (!fs.existsSync(filepath)) {failures.push(route + " missing HTML"); continue;}
  const html = fs.readFileSync(filepath, "utf8");
  const checks = {
    "NL lang": /<html\s+lang="nl"/i,
    "noindex draft": /<meta\s+name="robots"\s+content="noindex,follow"/i,
    "single H1": /<h1(?:\s|>)/ig,
    "navigation": /site-navigation/,
    "stylesheet": /assets\/styles.css/,
  };
  if (!checks["NL lang"].test(html)) failures.push(route + " lang");
  if (!checks["noindex draft"].test(html)) failures.push(route + " robots");
  if ((html.match(checks["single H1"]) || []).length !== 1) failures.push(route + " H1");
  if (!checks.navigation.test(html)) failures.push(route + " navigation");
  if (!checks.stylesheet.test(html)) failures.push(route + " stylesheet");
  if (/Inhoud nog te schrijven|Dit paginatype staat klaar|Structuur wordt bepaald na intentie/i.test(html)) drafts++;
  const report = path.join(root, ".content", "behoeften", slug || "index");
  if (fs.existsSync(report + ".md") && /Inhoud nog te schrijven|Dit paginatype staat klaar|Structuur wordt bepaald na intentie/i.test(html))
    failures.push(route + " reviewed page still has placeholder");
}
if (failures.length) {console.error(failures.join("\n")); process.exit(1);}
console.log("PASS: " + routes.length + " Behoeften routes structurally checked; " + drafts + " still drafts. Editorial/veterinary review is manual.");
