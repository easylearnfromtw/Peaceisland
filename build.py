from pathlib import Path
from html import escape
from urllib.parse import quote
import json
base=Path(__file__).resolve().parent
NAV=[('index.html','首頁'),('about.html','認識和平島'),('places.html','探索景點'),('history.html','島嶼歷史'),('food.html','在地美食'),('temples.html','廟宇文化'),('explore.html','互動探索')]
orgs=['和平島長青協會','和平島文化發展協會','台灣通史協會']

def btn(text,url,light=False):return f'<a class="btn{" light" if light else ""}" href="{escape(url,quote=True)}">{escape(text)} <span class="arrow" aria-hidden="true">↗</span></a>'
def mapurl(s):return 'https://www.google.com/maps/search/?api=1&query='+quote(s)

def source(*items):
    return '<div class="source-links"><div class="eyebrow" style="margin-bottom:10px">資料參考 / SOURCES</div>'+''.join(f'<a href="{escape(u,quote=True)}" target="_blank" rel="noopener noreferrer">{escape(t)} ↗</a><br>' for t,u in items)+'</div>'

def frame(page,title,description,content):
    nav=''.join(f'<a href="{u}" class="{"active" if page==u else ""}{" nav-explore" if u=="explore.html" else ""}" {"aria-current=\"page\"" if page==u else ""}>{t}</a>' for u,t in NAV)
    co='<span class="co-tag">聯合製作 / CO-PRODUCED BY</span>'+''.join(f'<span class="org">{n}</span>' for n in orgs)
    footnav=''.join(f'<a href="{u}">{t}</a>' for u,t in NAV)
    out=f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}｜和平島 HEPING ISLAND</title><meta name="description" content="{escape(description,quote=True)}"><meta name="theme-color" content="#17456a"><meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:site_name" content="和平島 HEPING ISLAND"><meta property="og:title" content="{escape(title,quote=True)}｜和平島"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:image" content="assets/coast.svg">
<link rel="icon" type="image/svg+xml" href="assets/mark.svg"><link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head>
<body><a class="skip" href="#main">跳至主要內容</a><div class="topline" aria-hidden="true"></div>
<header class="header"><div class="wrap head-inner"><a href="index.html" class="brand" aria-label="和平島網站首頁"><img src="assets/mark.svg" alt=""><span><span class="brand-name">和平島</span><small>HEPING ISLAND</small></span></a><button class="menu-btn" aria-expanded="false" aria-controls="site-nav" type="button">選單 ☰</button><nav class="nav" id="site-nav" aria-label="主要導覽">{nav}</nav></div></header>
<main id="main">{content}</main><div class="co-produce"><div class="wrap co-row">{co}</div></div>
<footer class="footer"><div class="wrap footmain"><div><div class="f-label">HEPING ISLAND / 和平島</div><h3>讓島嶼的故事，繼續被看見。</h3><p>探索和平島的景點、歷史、美食、廟宇與生活文化。<br>本網站由三個協會共同規劃製作。</p></div><div><div class="f-label">聯合製作</div>{''.join(f'<p style="margin:0 0 4px">{n}</p>' for n in orgs)}</div><div><div class="f-label">網站導覽</div>{footnav}</div></div><div class="wrap footbottom"><span>© 2026 和平島文化觀光網站 · 聯合製作計畫第一版</span><span>內容及各景點開放資訊可能異動，請以相關單位最新公告為準。</span></div></footer></body></html>'''
    (base/page).write_text(out,encoding='utf-8')

cards=[
('01','認識和平島','從地理、海洋與生活開始，閱讀這座島嶼的輪廓。','about.html',''),
('02','探索景點','走訪海蝕地景、漁港街屋和具有故事的角落。','places.html','sun'),
('03','島嶼歷史','從社寮島到和平島，回望島嶼的時間紋理。','history.html',''),
('04','在地美食','將地方風土與世代記憶，化為舌尖上的滋味。','food.html',''),
('05','廟宇文化','走進信仰中心，認識民間祭典與海上生活。','temples.html','alt'),
('06','互動探索','選一個主題，用輕量導覽開始你的和平島旅程。','explore.html','')]
home='''<section class="hero"><div class="hero-copy"><div class="eyebrow">HEPING ISLAND · KEELUNG · TAIWAN</div><h1 class="hero-claim">和平島，<br><span class="accent">不只有海。</span></h1><p>海岸與港灣是這座島的風景；廟宇、老街與人們的日常，則寫成了它的故事。從這裡出發，用自己的步調重新認識和平島。</p><div class="hero-actions">'''+btn('開始探索','explore.html')+btn('認識這座島','about.html',True)+'''</div></div><div class="hero-side"><img src="assets/coast.svg" alt="以和平島海岸、山丘和彩色街屋為靈感繪製的島嶼插畫"><span class="side-caption">THE ISLAND, BEYOND THE SHORE</span></div></section>'''
home+='''<div class="co-produce"><div class="wrap co-row"><span class="co-tag">三協會聯合製作</span>'''+''.join(f'<span class="org">{n}</span>' for n in orgs)+'''</div></div>
<div class="wrap intro-strip"><strong>一座島，<br>有無數種被認識的方式。</strong><p>來看海，也來聽故事。從西班牙人留下的歷史線索、港灣發展的歲月，到今日仍與生活相連的信仰和料理；我們希望把和平島介紹得更完整，也更貼近生活。</p></div>
<section class="section"><div class="wrap"><div class="secthead"><div class="headline"><div class="eyebrow">SIX WAYS TO EXPLORE</div><h2>用六種方式，<br>走進和平島。</h2></div><p>不用從頭讀到尾，選你感興趣的主題開始。這個網站是讓人們認識和平島的第一站。</p></div><div class="grid">'''
for n,t,d,url,cls in cards:home+=f'<a class="feature {cls} reveal" href="{url}"><span class="num">EXPLORE / {n}</span><h3>{t}</h3><p>{d}</p><span class="go" aria-hidden="true">↗</span></a>'
home+='''</div></div></section><section class="section quote-section"><div class="wrap"><div class="eyebrow yellow">MORE THAN A DESTINATION</div><h2>和平島的故事，<br>不只留在歷史書裡，<br>也藏在今天的巷弄與人情。</h2><p>一個認識家鄉、分享文化，也歡迎旅人走進來的地方。</p></div></section><section class="section"><div class="wrap"><div class="secthead"><div><div class="eyebrow">START HERE</div><h2>今天，你想怎麼認識和平島？</h2></div></div><div class="quicktiles"><a class="quicktile" href="places.html"><small>01 / LANDSCAPE</small><b>去看看，<br>山海的模樣。</b><span aria-hidden="true">↗</span></a><a class="quicktile" href="food.html"><small>02 / LOCAL TASTE</small><b>吃一口，<br>島上的味道。</b><span aria-hidden="true">↗</span></a><a class="quicktile" href="history.html"><small>03 / MEMORY</small><b>讀一段，<br>歲月的故事。</b><span aria-hidden="true">↗</span></a></div></div></section>'''
frame('index.html','一座島，無數種故事','和平島長青協會、和平島文化發展協會、台灣通史協會聯合製作。認識和平島的景點、歷史、在地美食與廟宇文化。',home)

head=lambda en,title,lead,theme='':f'<header class="pagehead {theme}"><div class="wrap"><div class="eyebrow">{en}</div><h1>{title}</h1><p>{lead}</p></div></header>'
about=head('ABOUT THE ISLAND','認識和平島','位於基隆港口東側的和平島，舊稱社寮島。海洋塑造了這裡的地貌，也讓不同時代的人們在此交會。')
about+='''<section class="section"><div class="wrap story-block"><div class="story-text"><div class="eyebrow">A PLACE SHAPED BY THE SEA</div><h2>島嶼的樣貌，<br>來自海，也來自人。</h2><p class="content-copy">和平島不只是地質公園的奇岩海岸。從巴賽族的生活足跡、17 世紀的海上交流，到後來的漁港、移民、宗教與商業生活，這裡的故事一直隨著港灣變遷而延伸。</p><p>來到和平島，可以同時看見自然景觀，也能在巷弄中發現真實的地方日常。</p>'''+btn('前往探索景點','places.html')+'''</div><div class="story-graphic" role="img" aria-label="以環形太陽、海與島嶼構成的抽象視覺"><div class="ring"></div><span>島嶼日常</span></div></div></section><section class="section sm" style="background:#e4ebe4"><div class="wrap"><div class="eyebrow">VISIT INFORMATION</div><h2>如何前往和平島？</h2><div class="content-grid"><div><h3>大眾交通</h3><p>可先抵達基隆車站，再依目的地轉乘當地公車。前往和平島地質公園可參考官方提供的 101、102 等公車資訊；請以當日路線與班次公告為準。</p>'''+btn('查看地質公園官方資訊','https://www.hpigeopark.org/')+'''</div><div><h3>自行規劃</h3><p>和平島不同地點之間仍有距離及坡道。建議先選擇目標景點，再使用地圖確認交通方式與道路狀況。</p>'''+btn('打開地圖',mapurl('基隆和平島'),True)+'''</div></div>'''+source(('和平島地質公園歷史文化','https://www.hpigeopark.org/history'),('交通部觀光署和平島地質公園','https://www.tad.gov.tw/m1.aspx?id=635&sNo=0001016'))+'''</div></section>'''
frame('about.html','認識和平島','和平島的位置、自然地貌、歷史背景與前往方式。',about)

def content_card(k,i,name,tag,desc,query):
    return f'<article class="place-card reveal"><div class="place-art tone-{i%4+1}"><span class="art-title" aria-hidden="true">{escape(name[:8])}</span></div><div class="place-body"><span class="label-chip">{escape(tag)}</span><h3>{escape(name)}</h3><p>{escape(desc)}</p><div class="actions"><a href="{mapurl(query)}" target="_blank" rel="noopener noreferrer">地圖導航 ↗</a></div></div></article>'
places=head('SIGHTS & PLACES','探索景點','從海岸到港灣，從地質景觀到歷史建築。每個地點，都有自己值得停下來的理由。')
places+='<section class="section"><div class="wrap"><div class="secthead"><div><div class="eyebrow">PLACES TO SEE</div><h2>從這幾站出發</h2></div><p>本頁聚焦和平島及周邊港灣文化地景；需要留意私人場域、遺址及受管制區域的進入限制。</p></div><div class="content-grid">'
for i,(n,t,d,q) in enumerate([
('和平島地質公園','海岸自然','海蝕平台、豆腐岩、蕈狀岩等海岸地景，是理解和平島自然環境的重要入口。','和平島地質公園'),
('正濱漁港色彩屋','港灣風景','彩色街屋與港中船影相映，也是認識基隆近代漁港風景的起點。','正濱漁港色彩屋'),
('阿根納造船廠遺構','工業遺產','位在正濱漁港周邊的歷史工業場域，可從周邊觀察建築外觀；請勿擅自進入。','阿根納造船廠遺構'),
('和平島考古遺址周邊','歷史線索','和平島保存跨越多個時代的重要考古文化層；考古現場是否開放，應依主管機關公告。','和平島考古遺址')]):places+=content_card('sight',i,n,t,d,q)
places+='''</div><div class="notice" style="margin-top:25px">參觀提醒：部分文化資產、考古區及地質景觀可能具有進入限制。請遵循現場公告，不擅自攀爬、進入或取走文物。</div>'''+source(('和平島地質公園官方網站','https://www.hpigeopark.org/'),('交通部觀光署和平島地質公園','https://www.tad.gov.tw/m1.aspx?id=635&sNo=0001016'))+'</div></section>'
frame('places.html','探索景點','和平島地質公園、正濱漁港與歷史地景介紹及地圖導航。',places)

history=head('HISTORY & MEMORY','時間留下的和平島','舊稱社寮島的和平島，在不同時代扮演過不同角色。我們用簡明而有來源的方式，閱讀島嶼的歷史。','deep')
history+='''<section class="section"><div class="wrap"><div class="eyebrow">ISLAND TIMELINE</div><h2>跨越年代的島嶼故事</h2><p style="max-width:780px">以下為第一版的歷史脈絡摘要；未來正式深化時，會進一步以文獻、考古報告與居民口述補充。各年代並非表示文化僅在該年開始或結束。</p><ol class="timeline">'''
for y,t,d in [
('史前至近代','原住民族與海岸生活','和平島周邊保存多層次考古文化資訊；巴賽族及北臺灣原住民族的海洋活動，是理解本地歷史不可忽略的一環。'),
('1626','大航海時代的交會','西班牙人於 17 世紀在雞籠地區活動，和平島成為理解北臺灣海洋交流、殖民競逐與宗教活動的重要地點。'),
('1895—1945','日本時代與漁港發展','社寮島的漁業及港灣設施逐步發展，不同地方的人因工作與貿易而來，也豐富了生活文化。'),
('1945 至今','和平島的轉變','戰後改稱和平島；伴隨漁業、產業與人口變化，地方居民持續在生活、文化保存與觀光之間尋找新的可能。')]:history+=f'<li class="reveal"><div class="date">{y}</div><div><h3>{t}</h3><p>{d}</p></div></li>'
history+='''</ol><div class="notice" style="margin-top:26px">歷史編輯原則：可確認的史實、學術推論與地方口述故事將分別標示，不以傳說取代史料。</div>'''+source(('和平島地質公園：歷史文化','https://www.hpigeopark.org/history'),('國家文化記憶庫','https://tcmb.culture.tw/'))+'''</div></section>'''
frame('history.html','島嶼歷史','閱讀和平島從社寮島、17世紀海洋交流到近現代漁港與地方生活的歷史。',history)

food=head('LOCAL FOOD & FLAVOURS','在地美食','有些滋味不是網路熱門排名，而是住在這座島上的人，吃了一代又一代的日常。','sunny')
food+='<section class="section"><div class="wrap"><div class="secthead"><div><div class="eyebrow">TASTE THE ISLAND</div><h2>吃一口和平島</h2></div><p>第一版先介紹有地方特色的料理與店家，不提供尚未確認的菜單價格和即時營業狀態。</p></div><div class="content-grid">'
for i,(n,t,d,q) in enumerate([
('藍媽媽青苔水餃','海藻入菜','將海藻運用在水餃、湯品等料理，呈現和平島靠海而生的地方飲食特色。','藍媽媽青苔水餃 基隆'),
('和平島郭家肉包','街坊小吃','現做肉包與傳統麵食，是許多旅人認識島上小吃的其中一站。','和平島郭家肉包'),
('和平島觀光漁市','港口與海味','從港口看見魚貨、料理與地方經濟的連結。店家營業及市場現況請出發前查詢。','和平島觀光漁市'),
('石花凍與海藻飲食','島嶼飲食文化','和平島與周邊海岸的海藻採集、加工與料理，是值得慢慢認識的地方食物文化。','和平島 石花凍')]):food+=content_card('food',i,n,t,d,q)
food+='''</div><div class="notice" style="margin-top:25px">網站不販售餐點，也未提供訂位服務。推薦是文化介紹，不代表商家已加入合作；正式推出前會確認是否需要店家同意與最新資料。</div>'''+source(('藍媽媽青苔水餃介紹','https://keelungplay.com/motherblue/'),('正濱與和平島店家資料參考','https://suntravel.tw/northerntaiwan/%E5%9F%BA%E9%9A%86%E6%AD%A3%E6%BF%B1%E5%92%8C%E5%B9%B3%E5%B3%B6%E4%BA%AE%E9%BB%9E%E5%BA%97%E5%AE%B6%E8%B3%87%E8%A8%8A/'))+'</div></section>'
frame('food.html','在地美食','探索和平島青苔水餃、肉包、漁市與海藻飲食文化。',food)

temples=head('FAITH & COMMUNITY','廟宇與信仰','一座廟，往往也是一個社區的時間軸。沿著香火、建築與節慶，閱讀島民共同生活的記憶。')
temples+='<section class="section"><div class="wrap"><div class="secthead"><div><div class="eyebrow">FAITH OF THE ISLAND</div><h2>海島上的信仰日常</h2></div><p>以文化尊重為原則，介紹宮廟歷史、建築與歲時祭典；不代替宮廟發布宗教服務或正式活動資訊。</p></div><div class="content-grid">'
for i,(n,t,d,q) in enumerate([
('社寮天后宮（和平島大天后宮）','媽祖信仰','和平島重要的媽祖信仰中心，廟宇沿革與港口生活、居民祭祀密切相關。','社寮天后宮 基隆'),
('和平島天顯宮','伍顯靈官大帝','位於山坡上的道教廟宇，以羅漢石雕、廟宇藝術與港灣視野為特色。','和平島天顯宮'),
('社靈廟','地方信仰','與天后宮、天顯宮同為地方宗教文化的重要組成，進一步的沿革與祭典資料待訪談與審訂。','和平島 社靈廟'),
('地方祭典與遶境','社區文化','透過歲時活動看見社區如何凝聚。確切時程與交通管制以宮廟、主辦單位公告為準。','和平島 廟宇 祭典')]):temples+=content_card('faith',i,n,t,d,q)
temples+='''</div><div class="notice" style="margin-top:25px">不同來源對廟宇建立年代或祭典細節可能有所出入。正式內容應優先核對宮廟文獻與訪談紀錄，並標記資料來源。</div>'''+source(('基隆市政府：和平島大天后宮','https://www.klcg.gov.tw/tw/financial/973-99587.html'),('基隆天顯宮官方網站','https://www.tian-xian-gong.org.tw/'),('國家文化記憶庫：天顯宮','https://tcmb.culture.tw/zh-tw/detail?id=302498&indexCode=Culture_Place'))+'</div></section>'
frame('temples.html','廟宇與信仰','探索和平島社寮天后宮、天顯宮與地方信仰文化。',temples)

explore=head('EXPLORE YOUR WAY','互動探索','挑一個感興趣的主題，從精選地點開始。第一版提供輕量示意探索與外部導航，不追蹤位置、不蒐集個人資料。')
explore+='''<section class="section"><div class="wrap"><div class="eyebrow">PICK A PLACE</div><h2>今天從哪裡開始？</h2><p>按下不同分類，再點擊地圖上的數字，看看這個地方的故事。</p><div class="toolbar" role="group" aria-label="探索分類"><button class="filter" data-filter="all" aria-pressed="true" type="button">全部</button><button class="filter" data-filter="nature" aria-pressed="false" type="button">自然</button><button class="filter" data-filter="sight" aria-pressed="false" type="button">港灣</button><button class="filter" data-filter="faith" aria-pressed="false" type="button">信仰</button><button class="filter" data-filter="food" aria-pressed="false" type="button">美食</button></div><div class="explore-layout"><div class="island-sketch" id="sketch" aria-label="和平島主題互動概念示意圖"><span class="sketch-title">HEPING ISLAND / EXPLORE</span></div><div class="pin-panel" id="pin-panel" aria-live="polite"><h3>選擇地點</h3><p>按地圖上的數字查看介紹與導航。</p></div></div><div class="plan-wrap"><div class="eyebrow">SUGGESTED ROUTES</div><h3>簡單選擇，開始你的島嶼旅程。</h3><div class="planner"><label for="plan-type">我喜歡</label><select id="plan-type"><option value="culture">歷史與文化</option><option value="seaside">海岸與風景</option><option value="food">美食與生活</option></select><label for="plan-time">安排</label><select id="plan-time"><option value="short">輕鬆走幾站</option><option value="long">想多看一點</option></select></div><div class="plan-result" id="plan-result" aria-live="polite"></div></div></div></section>'''
frame('explore.html','互動探索','透過和平島主題互動示意圖與簡易路線靈感探索景點、美食與廟宇。',explore)

(base/'README.md').write_text('''# 和平島文化觀光網站・第一階段初版

聯合製作名稱（依委託人提供）：
- 和平島長青協會
- 和平島文化發展協會
- 台灣通史協會

## 網站內容
- `index.html` 首頁
- `about.html` 認識和平島
- `places.html` 探索景點
- `history.html` 島嶼歷史
- `food.html` 在地美食
- `temples.html` 廟宇與信仰
- `explore.html` 輕量互動探索

## 預覽
雙擊 `index.html` 即可預覽。亦可在本資料夾執行 `python -m http.server 8000`，瀏覽 `http://localhost:8000/`。

## GitHub Pages 部署
將本資料夾內的 `index.html`、其他六個 HTML 及 `assets` 目錄上傳至指定 Repository 根目錄；到 `Settings > Pages` 選擇 `Deploy from a branch` 的 `main / (root)`，網站就能公開。既有 repo 若有自動部署工作流程，應先核對分支設定。

## 已完成
- 繁體中文多頁式網站，黃／藍／綠色品牌，手機版導覽
- 三協會聯合製作名稱展示（首頁、各頁頁尾）
- 地方介紹、景點、美食、廟宇、歷史內容初稿
- 主題篩選、概念地圖、路線靈感、Google Maps 外部導航
- 基本 SEO、ARIA 標籤、鍵盤操作、reduced-motion 支援
- 使用本站原創 SVG 視覺，不依賴未授權的攝影作品

## 尚未實作（刻意排除第一階段）
- CMS、會員、集章、報名、商家自主管理、精確地理底圖、線上預約、AI 聊天、翻譯系統

## 正式上線前必須確認
1. 三協會的正式全銜、共同製作授權、可否公開使用名稱及 Logo；本版依委託人的文字標示，不代表已查證法人登記或各協會背書。
2. 提供協會正式介紹、聯絡資訊與 Logo 後再上稿。請勿填入未核對的地址、電話及統編。
3. 景點是否可入內、店家營業資訊、宮廟祭典日期與名稱；部分資料只作概覽，不應當成即時旅遊資訊。
4. 所有歷史文字由具備背景的編輯核對並補入原始史料，避免混用傳說與史實。
5. 增加正式攝影內容前取得版權授權與肖像同意；本站原創 SVG 可以保留作為品牌插畫。
6. 為正式網域補上 HTTPS、隱私政策（如未來使用分析或表單）、正確 canonical URL、sitemap / og 圖片。

## 參考資料
- https://www.hpigeopark.org/history
- https://www.tad.gov.tw/m1.aspx?id=635&sNo=0001016
- https://www.klcg.gov.tw/tw/financial/973-99587.html
- https://www.tian-xian-gong.org.tw/
- https://tcmb.culture.tw/zh-tw/detail?id=302498&indexCode=Culture_Place
- https://keelungplay.com/motherblue/
- https://suntravel.tw/northerntaiwan/

原型版本：2026-10-10 / phase-one-v1
''',encoding='utf-8')
(base/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')
print('Generated pages:',[p.name for p in base.glob('*.html')]);print('Total bytes',sum(p.stat().st_size for p in base.rglob('*') if p.is_file()))
