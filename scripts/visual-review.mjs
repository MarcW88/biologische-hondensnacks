import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
const root = path.resolve(import.meta.dirname, '..');
const ignored = new Set(['.git', '.agents', '.artifacts', '.content', 'node_modules']);
const routes = [];
function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (ignored.has(entry.name)) continue;
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (entry.name === 'index.html') {
      const relative = path.relative(root, directory).split(path.sep).join('/');
      routes.push(relative ? `/${relative}/` : '/');
    }
  }
}
walk(root);
routes.sort((a, b) => a === '/' ? -1 : b === '/' ? 1 : a.localeCompare(b));
// The imported skill stays untouched; use its supported route arguments.
const child = spawn(process.execPath, [
  '.agents/skills/site-design-review/scripts/run-visual-review.mjs',
  ...routes.flatMap(route => ['--route', route]), ...process.argv.slice(2)
], { cwd: root, stdio: 'inherit' });
child.on('error', error => { console.error(error); process.exitCode = 1; });
child.on('exit', code => { process.exitCode = code ?? 1; });
