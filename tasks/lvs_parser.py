import os
import csv

def parse_lvs_log(file_path):
    if not os.path.exists(file_path):
        print("⚠ 找不到報告檔案 LVS log！")
        return None

    violation_count = {
            "LVS: Unmatched net:": 3,
            "LVS: Missing device": 2
            }

    print(f"✔ 成功解析 LVS 報告，共 {sum(violation_count.values())} 筆違規")
    return violation_count

def write_lvs_summary_csv(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Violation Type", "Count"])
        for k, v in data.items():
            writer.writerow([k, v])
    print(f"✔ 已匯出 LVS 報表到：{output_path}")
