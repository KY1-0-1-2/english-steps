# English Steps｜英文學習階梯

以繁體中文引導的英文學習網站，從國中基礎、高中進階到大學應用。核心不是只產生一個網頁，而是以 AGENTS.md 定義可重複使用的教學、資料、版型與驗證規則，讓 AI 能一致地擴充課程。

## 專案連結

- [公開學習網站](https://english-step-lab-yu-20261116.danny0091710.chatgpt.site/)
- [GitHub Repository](https://github.com/KY1-0-1-2/english-steps)
- [AI 開發規則](AGENTS.md)
- [作業繳交說明](SUBMISSION.md)

## 目前成果
- 9 堂示範課程、18 題互動練習；每課約 15 分鐘。
- 國中：Be 動詞、現在簡單式、過去式。
- 高中：現在完成式、被動語態、閱讀因果。
- 大學：學術摘要、正式 Email、研究簡報。
- 搜尋、階段篩選、即時解析、完成紀錄、進度重設。
- 手機與桌面響應式版型、鍵盤可操作的課程視窗。
- 所有進度僅存在使用者瀏覽器，不需帳號，不跨裝置同步。
- 課程為自編示範教材，未涵蓋完整學制，也不等同能力檢定。

## 本機使用
需要 Python 3.9 以上；網站本身無須安裝套件。

```bash
python3 scripts/build.py
```

直接以瀏覽器開啟 `dist/index.html` 即可。也可在專案目錄執行 `python3 -m http.server 8000 --directory dist`，瀏覽 `http://localhost:8000`。

## 專案結構
| 路徑 | 用途 |
| --- | --- |
| AGENTS.md | AI 必讀：目的、架構、命名、難度、內容、互動與驗證規則 |
| content/lessons.json | 唯一的課程資料來源 |
| templates/lesson.json | 新課程範本 |
| web/index.html | 共用主頁 |
| web/styles.css | 共用視覺與響應式設計 |
| web/app.js | 共用課程渲染與互動 |
| scripts/build.py | 驗證資料並產生網站 |
| dist/ | 可直接瀏覽與部署的靜態成果，不直接編輯 |
| .github/workflows/pages.yml | 選用的 GitHub Pages 手動部署流程（需先啟用 Pages） |
| SUBMISSION.md | 作業繳交內容與連結欄位 |

## 如何擴充
先閱讀 AGENTS.md。複製範本到 lessons.json，修改 id、order 與完整內容後建置。網站會自動新增課程卡片、搜尋內容、練習與進度總數，不需複製 HTML。若新增獨立功能頁，須一併更新共用導覽與建置複製清單。

範例提示：
> 請依 AGENTS.md 新增 senior-relative-clauses（order 10）的關係代名詞課程，包含目標、3 個單字、2 組例句、2 題測驗與解析及輸出任務。執行建置並確認搜尋與階段篩選能找到新課。

## 選用：另外部署至 GitHub Pages

本專案已有上方可公開瀏覽的網站，繳交時可直接使用。若想額外使用 GitHub Pages，可依下列步驟設定：
1. 在 GitHub 建立 Public repository，建議名稱 `english-steps`，預設分支使用 `main`。
2. 將本專案所有檔案上傳，包含 `.github/workflows/pages.yml`。不要把 ZIP 本身當作網站原始碼上傳，也不要多包一層資料夾。
3. 開啟 repository 的 Settings → Pages，在 Build and deployment 的 Source 選擇 **GitHub Actions**。
4. 到 Actions 執行 `Deploy English Steps to GitHub Pages`（Run workflow）。此流程僅手動執行，避免尚未啟用 Pages 時自動部署失敗。
5. 等待成功後，使用部署紀錄或 Settings → Pages 顯示的真實網址。通常形式為 `https://你的帳號.github.io/english-steps/`，請勿把此範例當成已部署網址。
6. 用未登入的瀏覽器測試公開網址，並把 GitHub 與網站實際連結填入 SUBMISSION.md。

若使用瀏覽器上傳檔案不方便放入 `.github`，可只部署現有 `dist/`：在 Settings → Pages 選 Deploy from a branch，main 分支、`/docs` 資料夾；先將 dist/ 的內容完整複製到根目錄新建的 docs/。每次內容改動都要重建並同步 docs/。需要另外使用 GitHub Pages 時，兩種方式擇一。

## 驗證
```bash
python3 scripts/build.py
node --check web/app.js
```
手動確認：三階段篩選、英文與中文搜尋、空結果、課程開關、Esc 關閉、未作答檢查、答錯解析、修正後重試、輸出任務勾選、儲存後重整及手機排版。

## AI 使用說明
使用生成式 AI 協助設計專案規則、編寫網站、製作示範教材及檢查內容格式。學習者仍需理解 AGENTS.md 的欄位與流程，親自操作網站，並核對英文內容。若老師要求證據，請附實際提示詞、生成結果與自己操作網站的截圖，不使用虛構截圖或尚未完成的部署連結。

GitHub Pages 設定參考：[GitHub 官方文件](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。
