# 和平島文化觀光網站・第一階段初版

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
