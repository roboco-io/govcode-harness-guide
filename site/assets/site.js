document.querySelectorAll('[data-copy]').forEach(button=>{button.addEventListener('click',async()=>{const code=button.parentElement.querySelector('code');try{await navigator.clipboard.writeText(code.textContent);button.textContent='복사 완료';document.getElementById('status').textContent='명령을 복사했습니다.';}catch{document.getElementById('status').textContent='복사 권한이 없습니다. 명령을 직접 선택해 복사하세요.';}setTimeout(()=>{button.textContent='복사';},1800);});});
const checks=[...document.querySelectorAll('.checklist input')];
const progress=document.querySelector('[data-progress]');
function update(){if(progress)progress.textContent=`${checks.filter(x=>x.checked).length} / ${checks.length}개 준비 완료`;}
checks.forEach(x=>x.addEventListener('change',update));update();
document.querySelector('[data-print]')?.addEventListener('click',()=>window.print());
