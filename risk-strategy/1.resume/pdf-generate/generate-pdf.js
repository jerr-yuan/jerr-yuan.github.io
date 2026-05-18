/**
 * 简历 HTML 转 PDF（一页 A4）
 * 使用 Puppeteer，依赖 @media print 样式。
 * 运行：npm install && npm run pdf
 * 或：npx puppeteer node generate-pdf.js
 */
const fs = require('fs');
const path = require('path');

const RESUME_DIR = path.join(__dirname, '..');
const HTML_STANDARD = path.join(RESUME_DIR, 'resume-pdf.html');
const HTML_TIGHT = path.join(RESUME_DIR, 'resume-pdf-tight.html');
const OUT_DIR = RESUME_DIR;
const OUT_STANDARD = path.join(OUT_DIR, 'resume-袁鹏-一页.pdf');
const OUT_TIGHT = path.join(OUT_DIR, 'resume-袁鹏-一页-紧凑.pdf');

async function generate(useTight = false) {
  const puppeteer = require('puppeteer');
  const htmlPath = useTight ? HTML_TIGHT : HTML_STANDARD;
  const outPath = useTight ? OUT_TIGHT : OUT_STANDARD;

  const html = fs.readFileSync(htmlPath, 'utf8');
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  await page.setContent(html, {
    waitUntil: 'networkidle0',
    encoding: 'utf8'
  });

  const margin = useTight
    ? { top: '6mm', right: '8mm', bottom: '6mm', left: '8mm' }
    : { top: '8mm', right: '10mm', bottom: '8mm', left: '10mm' };
  await page.pdf({
    path: outPath,
    format: 'A4',
    printBackground: true,
    margin
  });

  await browser.close();
  console.log('PDF 已生成:', outPath);
  return outPath;
}

const useTight = process.argv.includes('tight');
generate(useTight).catch(err => {
  console.error(err);
  process.exit(1);
});
