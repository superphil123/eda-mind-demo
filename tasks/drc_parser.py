from collections import defaultdict
import argparse
import os

def parse_drc_log(log_path):
    print(f"開始分析:{log_path}")
    violation_count = defaultdict(int)

    try:
        with open(log_path, "r") as f:
            for line in f:
                line = line.strip()
                if "DRC:" in line:
                    v_type = line.split("DRC:")[1].split(" at")[0].strip()
                    violation_count[v_type] += 1
    except FileNotFoundError:
        print("找不到檔案")
        return {}

    print("統計結果")
    for k, v in violation_count.items():
        print(f"- {k}: {v} 筆")
        
    return violation_count
def write_summary_csv(result_dict, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write("ViolationType,Count\n")
        for k, v in result_dict.items():
            f.write(f"{k},{v}\n")

    print(f"報表已寫入: {output_path}")

if __name__ == "__main__":
    par = argparse.ArgumentParser(description="DRC Log Parser")
    par.add_argument("--file", required=True, help="指定 DRC 報告檔案路徑")
    args = par.parse_args()


    parse_drc_log(args.file)


