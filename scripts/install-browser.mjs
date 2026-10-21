import { spawnSync } from 'node:child_process';
const install = spawnSync('npx', ['playwright', 'install', 'chromium'], { stdio: 'inherit' });
if (install.status === 0) process.exit(0);
// Pinned compatible fallback when the primary archive or mirror is unavailable.
const fallback = spawnSync('npm', ['exec', '--yes', '--package=playwright@1.51.1', '--', 'playwright', 'install', 'chromium'], { stdio: 'inherit' });
process.exit(fallback.status ?? 1);
