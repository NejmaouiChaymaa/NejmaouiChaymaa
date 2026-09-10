// Exports the packaging template to PDF (filled state) and to a blank PDF.
const { chromium } = require('playwright');
const path = require('path');
const ROOT = __dirname, OUT = path.join(ROOT, 'export');
(async () => {
  const browser = await chromium.launch();
  for (const [name, blank] of [['packaging-case-study.pdf', false], ['packaging-case-study-vierge.pdf', true]]) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 1200 } });
    await page.goto('file://' + path.join(ROOT, 'packaging-case-study.standalone.html'));
    await page.waitForTimeout(1500);
    if (blank) await page.click('#t-blank');
    await page.click('#t-tips');                       // guides off for the printed version
    await page.waitForTimeout(400);
    const h = await page.evaluate(() => document.body.scrollHeight);
    await page.pdf({ path: path.join(OUT, name), width: '1280px', height: h + 'px', printBackground: true, pageRanges: '1' });
    await page.close();
    console.log(name, h);
  }
  await browser.close();
})();
