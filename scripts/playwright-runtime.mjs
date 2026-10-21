// Site runtime adapter. Does not modify the shared visual-review script.
import { chromium } from 'playwright';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
const launch = chromium.launch.bind(chromium);
chromium.launch = async (options = {}) => {
  if (options.executablePath || fs.existsSync(chromium.executablePath())) return launch(options);
  const cache = path.join(os.homedir(), '.cache', 'ms-playwright');
  const candidates = fs.existsSync(cache) ? fs.readdirSync(cache).filter(x => /^chromium(?:_headless_shell)?-\d+$/.test(x)).sort().reverse().flatMap(x => ['chrome-linux/headless_shell', 'chrome-headless-shell-linux64/chrome-headless-shell', 'chrome-linux/chrome', 'chrome-linux64/chrome'].map(y => path.join(cache, x, y))) : [];
  const executablePath = process.env.SITE_CHROMIUM_EXECUTABLE || candidates.find(x => fs.existsSync(x));
  if (!executablePath) throw new Error('No Chromium executable. Run npm run visual:install.');
  console.log('Site browser adapter uses:', executablePath);
  return launch({ ...options, executablePath });
};
