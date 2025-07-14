-Mind Demo CLI 工具平台

A lightweight CLI tool for automating EDA tasks like DRC and LVS parsing.  


---

## 📦 功能介紹 Features

| 功能名稱 | 說明 | 指令範例 |
|----------|------|-----------|
| `run`    | 執行指定任務（模擬 DRC / LVS） | `python3 cli.py run drc` |
| `parse`  | 解析報告檔並輸出統計 | `python3 cli.py parse drc --file reports/drc.log` |
| `flow`   | 執行完整流程（run ➝ parse ➝ output） | `python3 cli.py flow drc` |

---

## 📁 專案結構 Project Structure

eda_mind_demo/
├── cli.py # 主控制腳本，整合任務與 CLI
├── tasks/
│ ├── run_drc.py # 模擬 DRC 工具執行
│ ├── drc_parser.py # 分析 DRC 報告
│ └── lvs_parser.py # 分析 LVS 報告（模擬）
├── reports/ # 放入 DRC / LVS log 原始檔案
├── output/ # 匯出報表資料（CSV / JSON）
└── README.md # 本說明文件



---

## 🚀 使用方式 Usage

### 1️⃣ 執行 DRC 或 LVS 任務（模擬執行）
```bash
python3 cli.py run drc
python3 cli.py run lvs

### 2️⃣ 分析報告
```bash
python3 cli.py parse drc --file reports/drc.log --format csv
python3 cli.py parse lvs --file reports/lvs.log --format json

### 3️⃣ 執行完整流程（run ➝ parse ➝ export）
```bash
python3 cli.py flow drc --file reports/drc.log --output output/drc_summary.csv

# eda-mind-demo
# eda-mind-demo
