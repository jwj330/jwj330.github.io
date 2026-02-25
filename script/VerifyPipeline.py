import os
import subprocess
import json
import sys
from datetime import datetime

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False, result.stdout
    return True, result.stdout

def verify():
    print("=== GitHub Archive Integration Verification ===\n")
    
    # 1. 检查必要文件
    files_to_check = [
        "script/FetchGHArchiveData.py",
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
    success, output = run_command("python3 script/FetchGHArchiveData.py")
    print(output)
    if not success:
        print("Data collection failed!")
        return

    # 3. 检查数据文件是否生成
    print("\n--- Step 2: Checking Data Files ---")
    # 获取日期（模拟脚本逻辑）
    files = [f for f in os.listdir("scriptData") if f.startswith("github_top_1000_") and f.endswith(".json")]
    files.sort(reverse=True)
    if not files:
        print("No source data found to determine date.")
        return
    date_str = files[0].replace("github_top_1000_", "").replace(".json", "")
    
    expected_patterns = [
        f"gharchive_growth_past_24_hours_{date_str}.json",
        f"gharchive_growth_past_week_{date_str}.json",
        f"gharchive_growth_past_month_{date_str}.json"
    ]
    
    for pattern in expected_patterns:
        path = os.path.join("scriptData", pattern)
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                print(f"[OK] {pattern} exists, contains {len(data)} items.")
        else:
            print(f"[FAIL] {pattern} is missing!")

    # 4. 运行分析脚本
    print("\n--- Step 3: Running Analysis ---")
    success, output = run_command("python3 script/AnalyzeData2.py")
    print(output)
    if not success:
        print("Analysis failed!")
        return

    # 5. 检查报告生成
    print("\n--- Step 4: Checking Final Report ---")
    report_path = f"content/post/anagithub{date_str}/index.md"
    if os.path.exists(report_path):
        print(f"[OK] Report generated: {report_path}")
        # 简单检查报告内容是否包含新数据
        with open(report_path, 'r') as f:
            content = f.read()
            if "dataMap" in content and "openclaw" in content.lower():
                print("[OK] Report confirmed to contain GH Archive data (e.g., 'openclaw').")
            else:
                print("[WARNING] Report generated but 'openclaw' not found. Check if data was correctly merged.")
    else:
        print(f"[FAIL] Report missing: {report_path}")

    print("\n=== Verification Complete ===")

if __name__ == "__main__":
    verify()
