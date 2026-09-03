// Renders infographic.standalone.html to a full-height PNG (2x) and a single-page PDF.
// Build that file first: inline-assets.py then inline-fonts.py (see README).
// Requires playwright: NODE_PATH=$(npm root -g) node tools/export-poster.js
const { chromium } = require('playwright');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'export');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1200 }, deviceScaleFactor: 2 });
  // render the self-contained build: it carries the embedded typeface
  await page.goto('file://' + path.join(ROOT, 'infographic.standalone.html'));
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(1500);

  const height = await page.evaluate(() => document.querySelector('.poster').offsetHeight);
  await page.setViewportSize({ width: 1200, height: Math.min(height, 30000) });
  await page.waitForTimeout(500);

  await (await page.$('.poster')).screenshot({ path: path.join(OUT, 'eyeon-case-study-infographic@2x.png') });
  await page.pdf({
    path: path.join(OUT, 'eyeon-case-study-infographic.pdf'),
    width: '1200px', height: height + 'px', printBackground: true, pageRanges: '1',
  });

  await browser.close();
  console.log('poster height:', height);
})();
