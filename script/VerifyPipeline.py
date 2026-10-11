import os
import subprocess
import json
import sys
from datetime import datetime

SNAPSHOT_PREFIX = "github_top_5000_"


def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False, result.stdout
    return True, result.stdout


def verify():
    print("=== GitHub Top-5000 Snapshot Pipeline Verification ===\n")

    # 1. 检查必要文件
    files_to_check = [
        "script/FetchTopRepos.py",
        "script/AnalyzeData2.py",
        ".github/workflows/generate.yml"
    ]
    all_files_exist = True
    for f in files_to_check:
        if os.path.exists(f):
            print(f"[OK] Found {f}")
        else:
            print(f"[FAIL] Missing {f}")
            all_files_exist = False

    if not all_files_exist:
        return

    # 2. 运行采集脚本
    print("\n--- Step 1: Running Data Collection ---")
    success, output = run_command("python3 script/FetchTopRepos.py")
    print(output)
    if not success:
        print("Data collection failed!")
        return

    # 3. 检查快照文件是否生成
    print("\n--- Step 2: Checking Snapshot File ---")
    if not os.path.exists("scriptData"):
        print("No scriptData directory found.")
        return
    files = [f for f in os.listdir("scriptData") if f.startswith(SNAPSHOT_PREFIX) and f.endswith(".json")]
    files.sort(reverse=True)
    if not files:
        print("No snapshot file generated!")
        return
    latest = files[0]
    path = os.path.join("scriptData", latest)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"[OK] {latest} exists, contains {len(data)} repos.")

    # 4. 运行分析脚本
    print("\n--- Step 3: Running Analysis ---")
    success, output = run_command("python3 script/AnalyzeData2.py")
    print(output)
    if not success:
        print("Analysis failed!")
        return

    # 5. 检查报告生成
    print("\n--- Step 4: Checking Final Report ---")
    date_str = latest.replace(SNAPSHOT_PREFIX, "").replace(".json", "")
    report_path = f"content/post/anagithub{date_str}/index.md"
    if os.path.exists(report_path):
        print(f"[OK] Report generated: {report_path}")
        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()
            if "dataMap" in content:
                print("[OK] Report contains the ECharts data block.")
            else:
                print("[WARNING] Report generated but missing dataMap block.")
    else:
        print(f"[FAIL] Report missing: {report_path}")

    print("\n=== Verification Complete ===")


if __name__ == "__main__":
    verify()
