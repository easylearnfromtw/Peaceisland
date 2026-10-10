'use strict';
const menuButton=document.querySelector('.menu-btn');const nav=document.querySelector('.nav');
if(menuButton&&nav){menuButton.addEventListener('click',()=>{let open=nav.classList.toggle('open');menuButton.setAttribute('aria-expanded',String(open));menuButton.textContent=open?'關閉 ✕':'選單 ☰'});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menuButton.setAttribute('aria-expanded','false');menuButton.textContent='選單 ☰'}));}
if('IntersectionObserver' in window){const ob=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');ob.unobserve(e.target)}}),{rootMargin:'0px 0px -40px 0px',threshold:.04});document.querySelectorAll('.reveal').forEach(x=>ob.observe(x))}else document.querySelectorAll('.reveal').forEach(x=>x.classList.add('in'));
const maps=(q)=>'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(q);
const points=[
 {id:'park',n:'和平島地質公園',k:'nature',c:'自然景點',d:'沿著海岸看海蝕地形、風化岩與海岸景觀。園區票價、入場與水域開放資訊請以官方公告為準。',q:'和平島地質公園',x:69,y:25},
 {id:'port',n:'正濱漁港色彩屋',k:'sight',c:'港灣景觀',d:'漁船、街屋和繽紛色塊映照在港灣水面，是認識基隆港口生活的好起點。',q:'正濱漁港色彩屋 基隆',x:26,y:71},
 {id:'temple1',n:'社寮天后宮',k:'faith',c:'宮廟信仰',d:'島上重要的媽祖信仰中心，廟宇與海洋、漁業和地方生活有深刻關係。',q:'社寮天后宮 基隆',x:41,y:59},
 {id:'temple2',n:'和平島天顯宮',k:'faith',c:'宮廟信仰',d:'位於山坡上的道教宮廟，主祀伍顯靈官大帝，以羅漢石雕及港灣視野聞名。',q:'和平島天顯宮',x:58,y:44},
 {id:'food1',n:'藍媽媽青苔水餃',k:'food',c:'地方滋味',d:'以海藻入菜的地方特色料理，將海島環境轉化為餐桌上的記憶。',q:'藍媽媽青苔水餃 基隆',x:47,y:74},
 {id:'food2',n:'和平島郭家肉包',k:'food',c:'在地小吃',d:'以現做肉包與傳統麵食聞名的在地小吃；實際營業資訊請先查詢店家。',q:'和平島郭家肉包',x:29,y:46},
];
const sketch=document.querySelector('#sketch');const panel=document.querySelector('#pin-panel');const filterButtons=document.querySelectorAll('.filter[data-filter]');let filter='all';let current=points[0].id;
function drawPins(){if(!sketch||!panel)return;sketch.querySelectorAll('.sketch-pin').forEach(x=>x.remove());let visible=points.filter(p=>filter==='all'||p.k===filter);if(!visible.some(p=>p.id===current))current=visible[0]?.id||points[0].id;visible.forEach((p,i)=>{let b=document.createElement('button');b.className='sketch-pin'+(p.id===current?' active':'');b.style.left=p.x+'%';b.style.top=p.y+'%';b.textContent=String(i+1);b.setAttribute('aria-label','查看'+p.n);b.title=p.n;b.addEventListener('click',()=>{current=p.id;drawPins()});sketch.appendChild(b)});const p=points.find(p=>p.id===current)||points[0];panel.replaceChildren();const top=document.createElement('div');top.className='num';top.textContent=p.c+' / '+p.id.toUpperCase();const h=document.createElement('h3');h.textContent=p.n;const para=document.createElement('p');para.textContent=p.d;const link=document.createElement('a');link.className='btn';link.href=maps(p.q);link.target='_blank';link.rel='noopener noreferrer';link.textContent='開啟地圖導航 ↗';panel.append(top,h,para,link)}
filterButtons.forEach(b=>b.addEventListener('click',()=>{filter=b.dataset.filter;filterButtons.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));drawPins()}));drawPins();
const typeEl=document.querySelector('#plan-type'),timeEl=document.querySelector('#plan-time'),result=document.querySelector('#plan-result');
const suggestions={
 'seaside-short':'正濱漁港色彩屋 → 和平島地質公園',
 'seaside-long':'正濱漁港色彩屋 → 阿根納造船廠遺構周邊 → 和平島地質公園',
 'culture-short':'社寮天后宮 → 和平島天顯宮',
 'culture-long':'正濱漁港 → 社寮天后宮 → 和平島天顯宮 → 和平島地質公園',
 'food-short':'郭家肉包 → 藍媽媽青苔水餃',
 'food-long':'正濱漁港 → 郭家肉包 → 社寮天后宮 → 藍媽媽青苔水餃'
};
function renderPlan(){if(!result||!typeEl||!timeEl)return;let key=typeEl.value+'-'+timeEl.value;result.replaceChildren();const strong=document.createElement('strong');strong.textContent='推薦探索順序：';const p=document.createElement('p');p.textContent=suggestions[key]||suggestions['culture-short'];const note=document.createElement('small');note.textContent='此為路線靈感，未計算實際步行時間；出發前請確認營業及開放資訊。';result.append(strong,p,note)}
[typeEl,timeEl].forEach(x=>x?.addEventListener('change',renderPlan));renderPlan();
