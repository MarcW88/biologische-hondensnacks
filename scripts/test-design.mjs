import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import net from 'node:net';
import { spawn } from 'node:child_process';
import { chromium } from '@playwright/test';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const root = path.resolve(import.meta.dirname, '..');
const routes = [];
function discover(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['.git', '.agents', '.artifacts', '.content', 'node_modules'].includes(entry.name)) continue;
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) discover(file);
    else if (entry.name === 'index.html') routes.push('/' + path.relative(root, dir).split(path.sep).filter(Boolean).join('/') + '/');
  }
}
discover(root);
const port = await new Promise(resolve => {
  const socket = net.createServer();
  socket.listen(0, '127.0.0.1', () => { const port = socket.address().port; socket.close(() => resolve(port)); });
});
const server = spawn('python3', ['-m', 'http.server', String(port), '--bind', '127.0.0.1'], { cwd: root, stdio: 'ignore' });
const base = `http://127.0.0.1:${port}`;
let browser;
const report = { accessibility: [], routes: routes.length, combinations: 0 };
try {
  for (let i = 0; i < 50; i++) {
    try { if ((await fetch(base)).ok) break; } catch {}
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  browser = await chromium.launch({ headless: true });
  const issues = [];
  for (const width of [390, 1440]) {
    const page = await browser.newPage({ viewport: { width, height: 1000 } });
    const pageErrors = [];
    page.on('pageerror', error => pageErrors.push(error.message));
    for (const route of routes) {
      const response = await page.goto(base + route.replace(/\/+/g, '/'), { waitUntil: 'load' });
      assert.equal(response.status(), 200, route);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${route} ${width}: overflow`);
      const navigationTargets = await page.locator('header a, footer a').evaluateAll(nodes => nodes.map(node => new URL(node.href).pathname));
      for (const href of navigationTargets) {
        const target = fs.readFileSync(path.join(root, href.slice(1), 'index.html'), 'utf8');
        assert.doesNotMatch(target, /Inhoud nog te schrijven|Inhoud nog te valideren|Nog geen items/, `Unfinished navigation destination: ${href}`);
      }
      const skip = page.locator('.skip-link');
      if (await skip.count()) assert.equal(new URL(await skip.getAttribute('href'), base).pathname, new URL(page.url()).pathname);
      await page.addScriptTag({ path: require.resolve('axe-core/axe.min.js') });
      const result = await page.evaluate(async () => {
        const r = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } });
        return { violations: r.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.map(n => ({ target: n.target, summary: n.failureSummary })) })), incomplete: r.incomplete.map(v => v.id) };
      });
      report.accessibility.push({ route, width, ...result });
      if (result.violations.length) issues.push({ route, width, violations: result.violations });
    }
    assert.deepEqual(pageErrors, [], 'Uncaught page errors');
    await page.goto(base);
    if (width === 390) {
      await page.locator('[data-menu]').click();
      assert.equal(await page.locator('[data-menu]').getAttribute('aria-expanded'), 'true');
      await page.locator('[data-submenu-toggle]').first().click();
      assert.equal(await page.locator('.nav-item').first().evaluate(e => e.classList.contains('expanded')), true);
      await page.keyboard.press('Escape');
      assert.equal(await page.locator('[data-menu]').getAttribute('aria-expanded'), 'false');
      assert.equal(await page.locator('[data-menu]').evaluate(e => e === document.activeElement), true);
    } else {
      await page.locator('.nav-link').first().hover();
      const link = await page.locator('.nav-link').first().boundingBox();
      await page.mouse.move(link.x + 30, link.y + link.height + 5);
      await page.waitForTimeout(250);
      assert.equal(await page.locator('.nav-dropdown').first().evaluate(e => getComputedStyle(e).visibility), 'visible', 'Dropdown hover bridge');
      await page.locator('.nav-dropdown').first().locator('a').first().hover();
    }
    // Every combination must lead to available content, with focus retained.
    const goals = width === 1440 ? ['Training', 'Beloning', 'Kauwen', 'Puppy'] : ['Training'];
    const needs = width === 1440 ? ['Gevoelige maag', 'Graanvrij', 'Mono-eiwit', 'Geen voorkeur'] : ['Gevoelige maag'];
    const proteins = width === 1440 ? ['Rund', 'Kip', 'Eend', 'Paard', 'Vis', 'Konijn'] : ['Kip'];
    for (const goal of goals) for (const need of needs) for (const protein of proteins) {
      for (const [i, answer] of [goal, need, protein].entries()) {
        await page.locator('[data-step]').nth(i).getByRole('button', { name: answer, exact: true }).click();
        assert.equal(await page.evaluate(() => document.activeElement.tagName), 'H3', `Focus after ${answer}`);
      }
      const links = await page.locator('[data-result-wrap] a').evaluateAll(nodes => nodes.map(e => new URL(e.href).pathname));
      for (const href of links) {
        const html = fs.readFileSync(path.join(root, href.slice(1), 'index.html'), 'utf8');
        assert.doesNotMatch(html, /Inhoud nog te schrijven|Inhoud nog te valideren|Nog geen items/);
      }
      assert.notEqual(links[0], '/soorten/', 'Finder must choose a relevant guide');
      report.combinations++;
      await page.locator('[data-reset]').click();
      assert.equal(await page.locator('[data-step]').first().isVisible(), true);
    }
    await page.close();
  }
  fs.mkdirSync(path.join(root, '.artifacts'), { recursive: true });
  fs.writeFileSync(path.join(root, '.artifacts/design-tests.json'), JSON.stringify(report, null, 2));
  assert.deepEqual(issues, [], 'Accessibility violations');
  console.log(`PASS: ${routes.length * 2} route/viewports, ${report.combinations} Finder combinations, keyboard and hover navigation.`);
} finally {
  await browser?.close();
  server.kill();
}
