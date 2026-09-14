import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const root = path.resolve(import.meta.dirname, '..');
const guidesRoot = path.join(root, 'gidsen');

function snapshotDirectory(dir) {
  const files = new Map();
  if (!fs.existsSync(dir)) return files;

  const walk = current => {
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      const absolute = path.join(current, entry.name);
      if (entry.isDirectory()) {
        walk(absolute);
      } else {
        const relative = path.relative(root, absolute);
        files.set(relative, fs.readFileSync(absolute));
      }
    }
  };

  walk(dir);
  return files;
}

function restoreSnapshot(files) {
  for (const [relative, content] of files) {
    const absolute = path.join(root, relative);
    fs.mkdirSync(path.dirname(absolute), { recursive: true });
    fs.writeFileSync(absolute, content);
  }
}

const guideSnapshot = snapshotDirectory(guidesRoot);

await import(pathToFileURL(path.join(import.meta.dirname, 'build.mjs')).href);

restoreSnapshot(guideSnapshot);

for (const [relative, original] of guideSnapshot) {
  const absolute = path.join(root, relative);
  const current = fs.readFileSync(absolute);
  if (!current.equals(original)) {
    throw new Error(`Authored guide changed during build: ${relative}`);
  }
}

await import(pathToFileURL(path.join(import.meta.dirname, 'sync-navigation.mjs')).href);

console.log(`PASS: preserved ${guideSnapshot.size} authored files under gidsen/ before shared navigation sync.`);
