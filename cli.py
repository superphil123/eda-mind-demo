import argparse
import os
import json
from tasks.run_drc import run_drc
from tasks.drc_parser import parse_drc_log, write_summary_csv
from tasks.lvs_parser import parse_lvs_log, write_lvs_summary_csv

def main():
   parser = argparse.ArgumentParser(prog="eda", description="EDA 工具 CLI 控制中心")
   subparsers = parser.add_subparsers(dest="command", required=True, help="可用指令")

   run_parser = subparsers.add_parser("run", help="執行特定任務")
   run_parser.add_argument("task", choices=["drc", "lvs"], help="指定任務名稱")

   parse_parser = subparsers.add_parser("parse", help="分析報告檔")
   parse_parser.add_argument("task", choices=["drc", "lvs"], help="指定分析任務")
   parse_parser.add_argument("--file", required=True, help="輸入報告檔")
   parse_parser.add_argument("--output", default="output/drc_summary.csv", help="輸出報表檔")
   parse_parser.add_argument("--format", choices=["csv", "json"], default="csv", help="輸出格式")

   flow_parser = subparsers.add_parser("flow", help="執行完整流程")
   flow_parser.add_argument("task", choices=["drc", "lvs"], help="任務類型")
   flow_parser.add_argument("--file", default="reports/drc.log", help="輸入檔案")
   flow_parser.add_argument("--output", default="output/drc_summary.csv", help="輸出報表")
   flow_parser.add_argument("--format", choices=["csv", "json"], default="csv", help="輸出格式")

   args = parser.parse_args()
   # ---------- run ----------
   if args.command == "run":
       if args.task == "drc":
           run_drc()
       elif arg.task == "lvs":
           print("執行 LVS 任務（模擬）...")
           
   # ---------- parse ----------
   elif args.command == "parse":
       result = parse_drc_log(args.file)
       if result:
         for k, v in result.items():
            print(f"- {k}: {v} 筆")
         if args.format == "csv":
             write_summary_csv(result, args.output)
         else:
             with open(args.output, "w") as f:
                 json.dump(result, f, indent=2, ensure_ascii=False)
   elif args.task == "lvs":
      result = parse_lvs_log(args.file)
      if result:
            for k, v in result.items():
                print(f"- {k}: {v} 筆")
            if args.format == "csv":
                write_summary_csv(result, args.output)
            else:
                with open(args.output, "w") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
    # ---------- flow ----------
   elif args.command == "flow": 
       if args.task == "drc":
           run_drc()
           result = parse_drc_log(args.file)
           if result:
               for k, v in result.items():
                   print(f"- {k}: {v} 筆")
               if args.format == "csv":
                   write_summary_csv(result, args.output)
               else:
                   with open(args.output, "w") as f:
                        json.dump(result, f, indent=2, ensure_ascii=False)
       elif args.task == "lvs":
            print("執行 LVS 任務（模擬）...")
            result = parse_lvs_log(args.file)
            if result:
                for k, v in result.items():
                    print(f"- {k}: {v} 筆")
                if args.format == "csv":
                    write_lvs_summary_csv(result, args.output)
                else:
                    with open(args.output, "w") as f:
                        json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
