import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(import.meta.dirname, '..');
let count = 0;
const errors = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['.git', '.agents', '.artifacts', '.content', 'node_modules'].includes(entry.name)) continue;
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) { walk(file); continue; }
    if (!entry.name.endsWith('.html')) continue;
    count++;
    const html = fs.readFileSync(file, 'utf8');
    const isRedirect = /<meta\\s+http-equiv=["']refresh["']/i.test(html);
    const expectedRobots = isRedirect ? 'noindex,follow' : 'index,follow';
    if (!html.includes(`name="robots" content="${expectedRobots}"`)) errors.push(`${file}: expected ${expectedRobots}`);
    if (!html.includes('assets/styles.css')) errors.push(`${file}: CSS ontbreekt`);
  }
}
walk(root);
if (errors.length) { console.error(errors.join('\\n')); process.exit(1); }
console.log(`${count} HTML-pagina's gecontroleerd.`);
