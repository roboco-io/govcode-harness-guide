// Run with Playwright and Chrome available in the document production environment.
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const root=fileURLToPath(new URL('../site/',import.meta.url));
const server=createServer(async(req,res)=>{
 const file=path.resolve(root,'.'+new URL(req.url,'http://localhost').pathname);
 if(!file.startsWith(root.endsWith(path.sep)?root:root+path.sep)){res.writeHead(403);return res.end();}
 try {res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':'text/html; charset=utf-8');res.end(await readFile(file));}catch{res.writeHead(404);res.end();}
});
await new Promise(r=>server.listen(0,'127.0.0.1',r));
const base=`http://127.0.0.1:${server.address().port}`;
const browser=await chromium.launch({channel:process.env.PLAYWRIGHT_CHANNEL||'chrome'});
let passed=0;
try {
 const context=await browser.newContext({colorScheme:'dark'});
 const page=await context.newPage();
 await page.goto(base+'/index.html');
 assert.equal(await page.locator('html').getAttribute('data-theme'),'dark','system dark preference must apply');passed++;
 await page.getByRole('button',{name:'라이트 모드로 전환',exact:true}).click();
 assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 await page.reload();
 assert.equal(await page.locator('html').getAttribute('data-theme'),'light','manual selection must survive reload');
 await page.goto(base+'/start.html');
 assert.equal(await page.locator('html').getAttribute('data-theme'),'light','selection must carry across pages');passed++;
 await page.getByRole('button',{name:'기기 설정 사용',exact:true}).click();
 assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.emulateMedia({colorScheme:'light'});
 await page.waitForFunction(()=>document.documentElement.dataset.theme==='light');
 assert.equal(await page.locator('html').getAttribute('data-theme'),'light','system changes must apply after reset');passed++;
 for(const theme of ['light','dark']){
  await page.emulateMedia({colorScheme:theme});
  for(const width of [1440,390,320]){
   await page.setViewportSize({width,height:900});
   for(const file of ['index.html','start.html','onboarding.html','brochure.html','community.html','license.html','updates.html','pr.html','faq.html','references.html']){
    await page.goto(base+'/'+file);
    assert.equal(await page.locator('html').getAttribute('data-theme'),theme);
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${file} ${width} ${theme} overflow`);
    const link=page.getByRole('link',{name:'프로젝트 GitHub',exact:true}).first();
    assert.equal(await link.getAttribute('href'),'https://github.com/roboco-io/govcode-harness');
    assert.equal(await link.locator('svg').count(),1);
   }
  }
 }
 passed++;
 await page.emulateMedia({colorScheme:'dark'});
 await page.goto(base+'/brochure.html');
 await page.emulateMedia({media:'print'});
 assert.equal(await page.locator('body').evaluate(x=>getComputedStyle(x).backgroundColor),'rgb(255, 255, 255)','print must stay white');
 assert.equal(await page.locator('.sheet').first().evaluate(x=>getComputedStyle(x).color),'rgb(20, 41, 67)','print text must stay dark');passed++;
 await context.close();
 const blocked=await browser.newContext({colorScheme:'dark'});
 await blocked.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked');}});});
 const fallback=await blocked.newPage();await fallback.goto(base+'/index.html');
 assert.equal(await fallback.locator('html').getAttribute('data-theme'),'dark');
 await fallback.getByRole('button',{name:'라이트 모드로 전환',exact:true}).click();
 assert.equal(await fallback.locator('html').getAttribute('data-theme'),'light','storage failure must not block switching');passed++;
 console.log(`PASS: ${passed} theme/header scenarios; 10 pages × 3 widths × 2 themes`);
}finally{await browser.close();await new Promise(r=>server.close(r));}
