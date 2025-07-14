import argparse
from tasks.run_drc import run_drc
from tasks.drc_parser import parse_drc_log, write_summary_csv

def main():
    parser = argparse.ArgumentParser(description="EDA 任務流程控制器")
    parser.add_argument("--mode", choices=["run", "parse", "all"], default="all", help="選擇要執行的模式")
    parser.add_argument("--input", default="reports/drc.log", help="DRC 報告檔案路徑")
    parser.add_argument("--output", default="output/drc_summary.csv", help="輸出報表路徑")
    args = parser.parse_args()

    if args.mode in ["run", "all"]:
        run_drc()

    if args.mode in ["parse", "all"]:
        result = parse_drc_log(args.input)
        if result:
           for k, v in result.items():
               print(f"- {k}: {v} 筆")
           write_summary_csv(result, args.output)

if __name__== "__main__":
    main()
