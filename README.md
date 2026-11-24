# GitHub Actions — Python Build and Test

本專案為「Build and test code」實作範例。GitHub Actions 會自動建置 Python 套件、安裝 wheel、執行 8 項 pytest 測試，並上傳建置及測試檔案。

## 專案結構

```text
.github/workflows/python-build-test.yml  # GitHub Actions 自動化設定
pyproject.toml                           # Python 套件建置設定
src/ci_math/calculator.py               # 四則運算原始碼
src/ci_math/__init__.py                 # 套件公開介面
tests/test_calculator.py                # 8 項測試
REPORT.md                               # 作業報告及截圖清單
```

## Windows PowerShell 本機測試

請先在專案根目錄執行：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install build pytest
python -m build
Get-ChildItem .\dist\*.whl | ForEach-Object { python -m pip install $_.FullName }
python -m pytest -v tests
```

## GitHub 上傳及執行

1. 到 https://github.com/new 建立空白儲存庫 `python-build-test`（不勾選初始化 README）。
2. 開啟 Windows PowerShell，切換至已解壓的專案根目錄。
3. 依序執行（請把 `你的帳號` 改成實際 GitHub 使用者名稱）：

```powershell
git init -b main
git add .
git commit -m "Add Python build and test workflow"
git remote add origin https://github.com/你的帳號/python-build-test.git
git push -u origin main
```

4. 在 GitHub 儲存庫開啟 **Actions** → **Python Build and Test** → 最新一次執行紀錄。
5. 點入 **Build and test on Python 3.12**，依序確認 Checkout、Set up Python、Install tools、Build、Install wheel、Run unit tests、Upload artifacts。
6. 通過時可看到 `8 passed`；執行紀錄下方 **Artifacts** 有 `python-build-and-test-artifacts` 可下載。

也可在 Actions 選該工作流程，使用 **Run workflow** 手動觸發。

## 參考教材

https://docs.github.com/en/actions/tutorials/build-and-test-code/python
