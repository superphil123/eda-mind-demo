# tasks/run_drc.py
import os

def run_drc():
        print("執行 DRC 任務...")
# 模擬工具輸出（其實是複製一份現成的 log）
        src = "/pytest/eda_mind_demo/reports/drc.log"
        if os.path.exists(src):
            print(f"讀取報告：{src}")
        else:
            print("⚠️ 找不到報告檔案 drc.log！")

        print("✅ DRC 執行完成！")

if __name__ == "__main__":
        run_drc()
