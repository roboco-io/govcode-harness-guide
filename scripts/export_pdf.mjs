// Requires Playwright and its Chromium browser in the document production environment.
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const site=path.resolve(fileURLToPath(new URL('../site/',import.meta.url)));
const server=createServer(async(req,res)=>{
  const name=path.resolve(site,'.'+decodeURIComponent(new URL(req.url,'http://127.0.0.1').pathname));
  if(!name.startsWith(site+path.sep)){res.writeHead(403);res.end();return;}
  try{const b=await readFile(name);res.setHeader('Content-Type',name.endsWith('.css')?'text/css':name.endsWith('.js')?'text/javascript':'text/html; charset=utf-8');res.end(b);}catch{res.writeHead(404);res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
let browser;
try{
  browser=await chromium.launch({channel:process.env.PLAYWRIGHT_CHANNEL || undefined});const page=await browser.newPage();
  await page.goto(`http://127.0.0.1:${server.address().port}/brochure.html`);
  await page.emulateMedia({media:'print'});
  const overflow=await page.locator('.sheet').evaluateAll(xs=>xs.some(x=>x.scrollHeight>x.clientHeight+1));
  if(overflow)throw Error('Print content overflows a sheet');
  const bytes=await page.pdf({format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false});
  await writeFile(path.join(site,'downloads/govcode-harness-brochure.pdf'),bytes);
  await writeFile(path.join(site,'downloads/SHA256SUMS'),createHash('sha256').update(bytes).digest('hex')+'  govcode-harness-brochure.pdf\n');
  console.log('PDF and SHA256SUMS updated. Verify 2 pages and visually review before publishing.');
}finally{if(browser)await browser.close();await new Promise(r=>server.close(r));}
