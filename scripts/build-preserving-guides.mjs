import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const root = path.resolve(import.meta.dirname, "..");
// Preserve every existing editorial directory, including puppy and protein
// pages. Rebuild only the homepage and shared navigation around authored text.
const authoredRoots = ['gidsen', 'soorten', 'voor-gevoelige-honden', 'eiwit',
  'levensfase', 'kauwsnacks', 'ingredienten', 'merken', 'producten',
  'contact', 'over-ons', 'transparantie-affiliatie', 'mentions-legales']
  .map(directory => path.join(root, directory));

function snapshotDirectory(dir) {
  const files = new Map();
  if (!fs.existsSync(dir)) return files;

  const walk = (current) => {
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

const authoredSnapshots = authoredRoots.map(snapshotDirectory);

await import(pathToFileURL(path.join(import.meta.dirname, "build.mjs")).href);

for (const snapshot of authoredSnapshots) restoreSnapshot(snapshot);

for (const snapshot of authoredSnapshots) {
  for (const [relative, original] of snapshot) {
    const absolute = path.join(root, relative);
    const current = fs.readFileSync(absolute);
    if (!current.equals(original)) {
      throw new Error(`Authored page changed during build: ${relative}`);
    }
  }
}

await import(
  pathToFileURL(path.join(import.meta.dirname, "sync-navigation.mjs")).href
);

const preservedCount = authoredSnapshots.reduce(
  (total, snapshot) => total + snapshot.size,
  0,
);
console.log(
  `PASS: preserved ${preservedCount} authored files before shared navigation sync.`,
);
