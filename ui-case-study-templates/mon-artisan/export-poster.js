// Renders mon-artisan/infographic.standalone.html to a full-height PNG (2x) and a single-page PDF.
const { chromium } = require('playwright');
const path = require('path');
const ROOT = __dirname;
const OUT = path.join(ROOT, 'export');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1200 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(ROOT, 'infographic.standalone.html'));
  await page.waitForTimeout(2000);
  const height = await page.evaluate(() => document.querySelector('.poster').offsetHeight);
  await page.setViewportSize({ width: 1200, height: Math.min(height, 30000) });
  await page.waitForTimeout(500);
  await (await page.$('.poster')).screenshot({ path: path.join(OUT, 'mon-artisan-case-study-infographic@2x.png') });
  await page.pdf({ path: path.join(OUT, 'mon-artisan-case-study-infographic.pdf'),
    width: '1200px', height: height + 'px', printBackground: true, pageRanges: '1' });
  await browser.close();
  console.log('poster height:', height);
})();
