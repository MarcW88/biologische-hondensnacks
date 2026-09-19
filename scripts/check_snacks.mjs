import fs from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const briefsRoot = path.join(root, ".content", "snacks", "briefs");
const reviewsRoot = path.join(root, ".content", "snacks", "reviews");
const errors = [];

if (!fs.existsSync(briefsRoot)) {
  console.log("Geen gevalideerde snackbriefs gevonden; niets te controleren.");
  process.exit(0);
}

const slugs = fs
  .readdirSync(briefsRoot)
  .filter((file) => file.endsWith(".md"))
  .map((file) => file.slice(0, -3));

for (const slug of slugs) {
  const pagePath = path.join(root, "soorten", slug, "index.html");
  const reviewPath = path.join(reviewsRoot, `${slug}.md`);

  if (!fs.existsSync(pagePath)) {
    errors.push(`${slug}: HTML-pagina ontbreekt`);
    continue;
  }

  const html = fs.readFileSync(pagePath, "utf8");
  const checks = [
    ["Nederlandse taal ontbreekt", /<html lang="nl">/],
    [
      "noindex,follow ontbreekt",
      /<meta\s+name="robots"\s+content="noindex,follow"\s*\/?\s*>/,
    ],
    [
      "canonical ontbreekt",
      /<link\s+rel="canonical"\s+href="https:\/\/biologische-hondensnacks\.nl\/soorten\/[^"]+\/"\s*\/?\s*>/s,
    ],
    [
      "bronverwijzingen ontbreken",
      /<section[^>]+aria-labelledby="sources-title"/,
    ],
    [
      "placeholdertekst staat nog in de pagina",
      /Inhoud nog te schrijven|Dit paginatype staat klaar|Structuur wordt bepaald na intentie/i,
    ],
  ];

  for (const [message, pattern] of checks) {
    const matched = pattern.test(html);
    if (
      (message === "placeholdertekst staat nog in de pagina" && matched) ||
      (message !== "placeholdertekst staat nog in de pagina" && !matched)
    ) {
      errors.push(`${slug}: ${message}`);
    }
  }

  if (!fs.existsSync(reviewPath))
    errors.push(`${slug}: reviewbestand ontbreekt`);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`PASS: ${slugs.length} snackpagina('s) met brief gecontroleerd.`);
