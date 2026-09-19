import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');

const chevron = '<svg class="nav-chevron" viewBox="0 0 24 24" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>';

const navItem = (label, href, dropdown, ariaLabel = label) => `
<div class="nav-item">
  <div class="nav-item-head">
    <a class="nav-link" href="${href}">${label}${chevron}</a>
    <button class="nav-submenu-toggle" type="button" data-submenu-toggle aria-label="Open ${ariaLabel}" aria-expanded="false">${chevron}</button>
  </div>
  <div class="nav-dropdown">${dropdown}</div>
</div>`;

const navigation = `<header class="header"><div class="container header-row">
<a class="brand" href="/"><img src="/assets/logo.svg" alt=""><span>Biologische<br>Hondensnacks</span></a>
<nav class="nav site-nav" data-nav id="site-navigation" aria-label="Hoofdnavigatie">
${navItem('Snacks', '/soorten/', `
  <span class="nav-dropdown-label">Op type</span>
  <a href="/soorten/kauwsnacks/">Kauwsnacks</a>
  <a href="/soorten/trainingssnacks/">Trainingssnacks</a>
  <a href="/soorten/gedroogde-hondensnacks/">Gedroogde hondensnacks</a>
  <a href="/soorten/tandsnacks/">Tandsnacks</a>
  <div class="nav-dropdown-separator"></div>
  <span class="nav-dropdown-label">Samenstelling</span>
  <a href="/ingredienten/natuurlijke-hondensnacks/">Natuurlijke hondensnacks</a>
  <a href="/ingredienten/hondensnacks-zonder-toevoegingen/">Zonder toevoegingen</a>
  <a href="/ingredienten/gezonde-hondensnacks/">Gezonde hondensnacks</a>
`)}
${navItem('Behoeften', '/voor-gevoelige-honden/', `
  <span class="nav-dropdown-label">Gevoelige honden</span>
  <a href="/voor-gevoelige-honden/">Alle opties voor gevoelige honden</a>
  <a href="/voor-gevoelige-honden/hypoallergene-hondensnacks/">Hypoallergene hondensnacks</a>
  <a href="/voor-gevoelige-honden/mono-eiwit-hondensnacks/">Mono-eiwit hondensnacks</a>
  <a href="/voor-gevoelige-honden/graanvrije-hondensnacks/">Graanvrije hondensnacks</a>
  <a href="/voor-gevoelige-honden/hondensnacks-gevoelige-maag/">Voor een gevoelige maag</a>
  <a href="/voor-gevoelige-honden/vetarme-hondensnacks/">Vetarme hondensnacks</a>
  <div class="nav-dropdown-separator"></div>
  <span class="nav-dropdown-label">Levensfase</span>
  <a href="/levensfase/hondensnacks-puppy/">Voor puppy's</a>
  <a href="/levensfase/hondensnacks-senior-hond/">Voor senior honden</a>
`)}
${navItem('Eiwitbron', '/eiwit/', `
  <span class="nav-dropdown-label">Kies de eiwitbron</span>
  <a href="/eiwit/rund/">Rund</a>
  <a href="/eiwit/kip/">Kip</a>
  <a href="/eiwit/eend/">Eend</a>
  <a href="/eiwit/paard/">Paard</a>
  <a href="/eiwit/vis/">Vis</a>
  <a href="/eiwit/konijn/">Konijn</a>
`)}
${navItem('Gidsen', '/gidsen/', `
  <span class="nav-dropdown-label">Biologisch & etiket</span>
  <a href="/gidsen/wat-zijn-biologische-hondensnacks/">Wat zijn biologische hondensnacks?</a>
  <a href="/gidsen/biologische-of-natuurlijke-hondensnacks/">Biologisch of natuurlijk?</a>
  <a href="/gidsen/biologisch-keurmerk-hondensnacks/">Biologisch keurmerk herkennen</a>
  <a href="/gidsen/ingredienten-hondensnacks-lezen/">Ingrediënten leren lezen</a>
  <a href="/gidsen/hondensnacks-zonder-toevoegingen/">Wat betekent zonder toevoegingen?</a>
  <div class="nav-dropdown-separator"></div>
  <span class="nav-dropdown-label">Kiezen & voeren</span>
  <a href="/gidsen/welke-hondensnacks-zijn-gezond/">Welke snacks zijn gezond?</a>
  <a href="/gidsen/hoeveel-snacks-mag-een-hond-per-dag/">Hoeveel snacks per dag?</a>
  <a href="/gidsen/wat-is-mono-eiwit/">Wat is mono-eiwit?</a>
  <a href="/gidsen/welke-kauwsnack-voor-mijn-hond/">Welke kauwsnack past?</a>
  <a href="/gidsen/welke-snacks-voor-een-puppy/">Welke snacks voor een puppy?</a>
`)}
</nav>
<a class="header-cta" href="/#snack-finder">Vind mijn snack</a>
<button class="icon-btn menu" data-menu type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="site-navigation">☰</button>
</div></header>`;

const headerPattern = /<header class="header">[\s\S]*?<\/header>(?:<div class="protein-bar">[\s\S]*?<\/div><\/div>)?/;
const ignored = new Set(['.git', 'node_modules', '.agents', '.content']);
let updated = 0;
let scanned = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (ignored.has(entry.name)) continue;
    const absolute = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(absolute);
      continue;
    }
    if (!entry.name.endsWith('.html')) continue;
    scanned++;
    const original = fs.readFileSync(absolute, 'utf8');
    if (!original.includes('<header class="header">')) continue;

    let next = original.replace(headerPattern, navigation);
    next = next.replace('</header></div><main>', '</header><main>');
    if (!next.includes('/assets/navigation.css')) {
      next = next.replace('</head>', '<link rel="stylesheet" href="/assets/navigation.css"></head>');
    }
    if (!next.includes('/assets/navigation.js')) {
      next = next.replace('</body>', '<script src="/assets/navigation.js"></script></body>');
    }
    if (next.includes('class="protein-bar"')) {
      throw new Error(`Legacy protein bar still present in ${path.relative(root, absolute)}`);
    }
    if (!next.includes('id="site-navigation"') || !next.includes('Vind mijn snack')) {
      throw new Error(`Shared navigation integrity check failed in ${path.relative(root, absolute)}`);
    }

    if (next !== original) {
      fs.writeFileSync(absolute, next);
      updated++;
    }
  }
}

walk(root);

console.log(`PASS: shared navigation valid; updated ${updated}/${scanned} HTML files.`);
