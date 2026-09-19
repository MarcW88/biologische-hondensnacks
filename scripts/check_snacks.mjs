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
  const brief = fs.readFileSync(path.join(briefsRoot, `${slug}.md`), "utf8");
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

  // Product intent is declared in the editorial brief by the explicit
  // comparison-workflow handoff. When present, zero-product output is a blocker.
  const productSelectionRequired =
    /Module produit\s*[—-]\s*handoff Comparatif/i.test(brief) ||
    /product_selection_required\s*:\s*true/i.test(brief);

  if (productSelectionRequired) {
    const productCards = html.match(/class="product-card"/g) ?? [];
    const productLinks = html.match(/class="product-card__cta"/g) ?? [];

    if (productCards.length < 2) {
      errors.push(
        `${slug}: productselectie vereist maar minder dan 2 productkaarten gevonden`,
      );
    }

    if (productLinks.length < productCards.length) {
      errors.push(
        `${slug}: niet elke productkaart heeft een controleerbare productlink`,
      );
    }
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(`PASS: ${slugs.length} snackpagina('s) met brief gecontroleerd.`);
