# GitHub Actions：Build and Test Code 實作報告

- 課程作業：GitHub Actions 建置及測試
- 選用語言：Python 3.12
- 作業日期：自行填寫
- 姓名／學號：自行填寫
- GitHub 儲存庫 URL：**[實際完成後貼入，尚未建立]**
- GitHub Actions Run URL：**[實際執行後貼入，尚未驗證]**

## 一、實作目的

學習持續整合（Continuous Integration, CI），讓每次推送程式碼到 GitHub 時，由 GitHub Actions 自動執行 Python 套件建置、安裝及單元測試。Workflow 成功後，產生可下載的 Wheel／Source Distribution 與測試報告。

## 二、使用工具

Git、GitHub、GitHub Actions、Python 3.12、pytest、Python build、setuptools、Ubuntu Runner。

## 三、實作流程與指令

1. 建立 `src/ci_math/calculator.py`，包含 `add`、`subtract`、`multiply`、`divide` 四則運算。
2. 建立 `tests/test_calculator.py`，測試一般輸入、負數、0、分數及除以 0 的例外處理，總共 8 個測試案例。
3. 建立 `pyproject.toml`，設定可建置的 Python 套件及 `src` 來源位置。
4. 建立 `.github/workflows/python-build-test.yml`，設定 main push / pull request / workflow_dispatch 觸發。
5. Workflow 依序執行 checkout、setup-python、pip install、python -m build、安裝 wheel、pytest、upload-artifact。
6. 在 PowerShell 執行 `git init -b main`、`git add .`、`git commit ...`、`git remote add origin ...`、`git push -u origin main`。
7. 開啟 GitHub → Actions → Python Build and Test → 最新 run → `Build and test on Python 3.12`，確認每個步驟的執行日誌。
8. 從 Artifacts 下載 `python-build-and-test-artifacts`，驗證建置成品。

## 四、關鍵設定說明

- `on.push`：推送到 main 時自動執行。
- `on.pull_request`：對 main 發出 PR 時執行。
- `on.workflow_dispatch`：允許手動執行。
- `runs-on: ubuntu-latest`：使用 GitHub 提供的 Ubuntu Runner。
- `actions/checkout@v6`：取得專案原始碼。
- `actions/setup-python@v6`：準備 Python 3.12。
- `python -m build`：建置 Wheel 與 Source Distribution。
- `python -m pytest -v tests`：自動執行單元測試。
- `actions/upload-artifact@v4`：保留建置及測試成果。

## 五、操作截圖（在自己的 GitHub 完成後補上）

- [待貼截圖 1] GitHub Repository 首頁，顯示上傳的檔案及 `.github/workflows`。
- [待貼截圖 2] Workflow YAML 程式碼（含 `on`、`runs-on`、`steps`）。
- [待貼截圖 3] Actions 工作流程執行畫面（綠色成功圖示）。
- [待貼截圖 4] Build source distribution and wheel 執行日誌。
- [待貼截圖 5] Run unit tests 執行日誌（8 passed）。
- [待貼截圖 6] Artifacts 下載項目，或已下載的 wheel、tar.gz 與 test-results.xml。

## 六、執行結果

- 本機建置：**成功產生 Wheel 與 Source Distribution（本機確認）**
- 本機測試：**8 passed（本機確認；亦驗證以已建置 Wheel 安裝後執行）**
- GitHub Actions 建置與測試：**[查看實際 Run 後填寫，不能預先標示成功]**
- 截圖：**[自行補上]**

## 七、心得

本次實作使我理解 GitHub Actions 可以將 Python 專案的建置與測試流程自動化。當程式碼推送到 GitHub 的 main 分支時，CI 工作流程可在獨立的 Ubuntu 環境安裝工具、產生 Python 套件、執行預先編寫的測試案例，並保留建置產出與測試結果。與手動測試相比，CI 有助於及早發現程式修改帶來的錯誤，也能讓執行過程被其他人檢查和重現。

## 八、參考資料

GitHub Docs: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
