const { chromium } = require('playwright-core');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
for(const f of process.argv.slice(2)){const [n,w,h]=f.split(':');const p=await b.newPage({viewport:{width:+w,height:+h}});
await p.goto('file://'+__dirname+'/'+n+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:__dirname+'/'+n+'.png'});await p.close();}await b.close();})();
