import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const guideRoot = path.join(root, 'gidsen');
const publishGate = process.argv.includes('--publish');
const errors = [];
const warnings = [];

function count(re, text) {
  return [...text.matchAll(re)].length;
}

function resolveInternalHref(href) {
  if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return null;
  if (/^https?:\/\//i.test(href) || href.startsWith('//')) return null;
  const clean = href.split(/[?#]/)[0].replace(/^\//, '');
  if (!clean) return path.join(root, 'index.html');
  let target = path.join(root, clean);
  if (clean.endsWith('/')) target = path.join(target, 'index.html');
  return target;
}

if (!fs.existsSync(guideRoot)) {
  console.error('gidsen/ ontbreekt');
  process.exit(1);
}

const pages = fs.readdirSync(guideRoot, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => path.join(guideRoot, entry.name, 'index.html'))
  .filter((file) => fs.existsSync(file));

if (pages.length === 0) errors.push('Geen gidsen gevonden onder gidsen/*/index.html');

const titles = new Map();
const descriptions = new Map();

for (const file of pages) {
  const rel = path.relative(root, file);
  const slug = path.basename(path.dirname(file));
  const html = fs.readFileSync(file, 'utf8');

  if (!/<html\b[^>]*\blang=["']nl["']/i.test(html)) errors.push(`${rel}: html lang moet nl zijn`);

  const h1Count = count(/<h1\b/gi, html);
  if (h1Count !== 1) errors.push(`${rel}: verwacht exact 1 H1, gevonden ${h1Count}`);

  const title = html.match(/<title>([^<]+)<\/title>/i)?.[1]?.trim();
  if (!title) errors.push(`${rel}: title ontbreekt`);
  else {
    if (titles.has(title)) errors.push(`${rel}: duplicate title met ${titles.get(title)}`);
    titles.set(title, rel);
  }

  const description = html.match(/<meta\s+name=["']description["']\s+content=["']([^"']+)["']/i)?.[1]?.trim();
  if (!description) errors.push(`${rel}: meta description ontbreekt`);
  else {
    if (descriptions.has(description)) warnings.push(`${rel}: duplicate meta description met ${descriptions.get(description)}`);
    descriptions.set(description, rel);
  }

  if (!html.includes('assets/styles.css')) errors.push(`${rel}: stylesheet ontbreekt`);
  if (!html.includes('gidsen/')) errors.push(`${rel}: gidsen-context ontbreekt`);

  const legacy = [
    'bloc-notes-numerique',
    'bloc-notes-numeriques',
    'ocr-manuscrit',
    '/guides/',
    'Vérifié le',
    'guide_content_',
  ];
  for (const marker of legacy) {
    if (html.toLowerCase().includes(marker.toLowerCase())) errors.push(`${rel}: legacy marker gevonden: ${marker}`);
  }

  for (const match of html.matchAll(/href=["']([^"']+)["']/gi)) {
    const target = resolveInternalHref(match[1]);
    if (target && !fs.existsSync(target)) errors.push(`${rel}: gebroken interne link ${match[1]}`);
  }

  for (const match of html.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
    try {
      JSON.parse(match[1]);
    } catch (error) {
      errors.push(`${rel}: ongeldige JSON-LD (${error.message})`);
    }
  }

  const canonical = html.match(/<link\s+rel=["']canonical["']\s+href=["']([^"']+)["']/i)?.[1];
  if (!canonical) warnings.push(`${rel}: canonical ontbreekt`);
  else if (!canonical.includes(`/gidsen/${slug}/`)) warnings.push(`${rel}: canonical lijkt niet bij slug te passen (${canonical})`);

  const placeholderSignals = [
    'Inhoud nog te schrijven.',
    'Dit paginatype staat klaar voor inhoud',
    'Structuur wordt bepaald na intentie- en bronnenonderzoek.',
  ];
  const hasPlaceholder = placeholderSignals.some((signal) => html.includes(signal));
  if (hasPlaceholder) {
    const message = `${rel}: bevat nog placeholdercontent`;
    if (publishGate) errors.push(message);
    else warnings.push(message);
  }
}

for (const warning of warnings) console.warn(`WARN: ${warning}`);
if (errors.length) {
  console.error(errors.map((error) => `ERROR: ${error}`).join('\n'));
  process.exit(1);
}

console.log(`PASS: ${pages.length} gidsen structureel gecontroleerd${publishGate ? ' (publish gate)' : ''}.`);
