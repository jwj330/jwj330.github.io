#!/usr/bin/env python3
"""
分析每日 Star 快照（github_top_5000_*.json），生成日/周/月增长趋势报告。

增长的计算方式：
    用今天的 Star 快照与 1 天前 / 7 天前 / 30 天前的快照做差分，
    即 growth = stars(今天) - stars(基线)。这取代了旧的 OSS Insight 趋势 API
    与 GH Archive star 事件方案——后者因 GitHub 公开事件流在 ~2026 年被削弱
    而失效。
"""

import datetime
import json
import os
import re
import sys

# 快照前缀须与 FetchTopRepos.py 的 TOP_N 保持一致
SNAPSHOT_PREFIX = "github_top_5000_"


def parse_date_from_filename(filename):
    """从文件名解析 8 位日期 YYYYMMDD。"""
    m = re.search(r"(\d{8})", filename)
    return m.group(1) if m else ""


def format_offertime(date_str):
    """将 YYYYMMDD 转换为 YYYY-MM-DD。"""
    if len(date_str) == 8 and date_str.isdigit():
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_str


def snapshot_path(date_str):
    return os.path.join("scriptData", f"{SNAPSHOT_PREFIX}{date_str}.json")


def load_snapshot(filepath):
    """加载快照文件，返回以 id 为 key 的字典。"""
    if not filepath or not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        result = {}
        for repo in data:
            rid = repo.get("id")
            if rid is not None:
                result[str(rid)] = repo
        return result
    except Exception as e:
        print(f"加载文件失败 {filepath}: {e}")
        return {}


def find_latest_snapshot():
    """查找最新的 github_top_5000_*.json 快照。"""
    data_dir = "scriptData"
    if not os.path.exists(data_dir):
        return ""
    files = [f for f in os.listdir(data_dir)
             if f.startswith(SNAPSHOT_PREFIX) and f.endswith(".json")]
    if not files:
        return ""
    files.sort(reverse=True)
    return os.path.join(data_dir, files[0])


def date_offset(base_date, days):
    """返回 base_date 往前偏移 days 天的 YYYYMMDD 字符串。"""
    return (base_date - datetime.timedelta(days=days)).strftime("%Y%m%d")


def compute_growth(today_data, baseline_data, min_created):
    """
    计算增长。

    - 仓库同时出现在今天与基线快照中：growth = 今天 stars - 基线 stars。
    - 仓库只在今天出现：
        * 若其创建时间在窗口内（created >= min_created），视为全新仓库，
          以其当前 stars 作为 growth；
        * 否则无法得知其历史 stars，跳过（避免把总 stars 误当成增长）。
    """
    growth_list = []
    for rid, repo in today_data.items():
        stars_now = int(repo.get("stars") or 0)
        if rid in baseline_data:
            stars_prev = int(baseline_data[rid].get("stars") or 0)
            growth = stars_now - stars_prev
        else:
            created = (repo.get("created_at") or "")[:10].replace("-", "")
            if created and created >= min_created:
                growth = stars_now
            else:
                continue

        if growth <= 0:
            continue

        growth_list.append({
            "id": repo.get("id"),
            "full_name": repo["full_name"],
            "stars": stars_now,
            "growth": growth,
            "description": repo.get("description", ""),
            "html_url": repo.get("html_url") or f"https://github.com/{repo['full_name']}",
        })

    growth_list.sort(key=lambda x: x["growth"], reverse=True)
    return growth_list


def generate_echarts_html(daily_data, weekly_data, monthly_data, date_str):
    """生成带有 ECharts 的 Hugo Markdown 报告。"""
    dir_name = f"content/post/anagithub{date_str}"
    os.makedirs(dir_name, exist_ok=True)
    md_filepath = os.path.join(dir_name, "index.md")

    formatted_date = format_offertime(date_str)
    # 快照日期以 UTC 为准；展示时间用北京时间（UTC+8）
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    beijing_now = now_utc + datetime.timedelta(hours=8)
    current_time = beijing_now.strftime('%Y-%m-%d %H:%M:%S')

    top_n = 20

    def process_data(data):
        if not data:
            return [], [], []
        top = data[:top_n]
        names = [item['full_name'] for item in top]
        values = [item['growth'] for item in top]
        return names[::-1], values[::-1], top

    d_names, d_values, _ = process_data(daily_data)
    w_names, w_values, _ = process_data(weekly_data)
    m_names, m_values, _ = process_data(monthly_data)

    daily_json = json.dumps({'categories': d_names, 'data': d_values}, ensure_ascii=False)
    weekly_json = json.dumps({'categories': w_names, 'data': w_values}, ensure_ascii=False)
    monthly_json = json.dumps({'categories': m_names, 'data': m_values}, ensure_ascii=False)

    def get_clean_name(full_name):
        return full_name.split('/')[-1] if '/' in full_name else full_name

    article_title = f"{formatted_date} GitHub增长趋势报告"

    desc_items = [f"{i + 1}.{get_clean_name(item['full_name'])}+{item['growth']}"
                  for i, item in enumerate(daily_data[:5])]
    article_desc = " ".join(desc_items) or "增长数据积累中"

    if date_str == now_utc.strftime("%Y%m%d"):
        post_date = beijing_now.strftime('%Y-%m-%dT%H:%M:%S+08:00')
    else:
        post_date = f"{formatted_date}T12:00:00+08:00"

    content = f"""---
title: "{article_title}"
description: "{article_desc}"
date: {post_date}
categories:
  - GitHub Trends
---

**生成时间**: {current_time}

本报告展示了 GitHub 上 Star 数增长最快的仓库（基于每日 Top-5000 Star 快照差分计算）。

<!-- ECharts 容器 -->
<div id="main" style="width: 100%;height:600px;"></div>
<div style="text-align: center; margin-top: 20px;">
    <button onclick="updateChart('daily')" style="padding: 5px 10px;">日榜 (Daily)</button>
    <button onclick="updateChart('weekly')" style="padding: 5px 10px;">周榜 (Weekly)</button>
    <button onclick="updateChart('monthly')" style="padding: 5px 10px;">月榜 (Monthly)</button>
</div>

<!-- 引入 ECharts -->
<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>

<script type="text/javascript">
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option;

    // 数据源
    var dataMap = {{
        'daily': {daily_json},
        'weekly': {weekly_json},
        'monthly': {monthly_json}
    }};

    function getOption(type) {{
        var currentData = dataMap[type];
        var titleText = '';
        if (type === 'daily') titleText = '日增长排行 (Top {top_n})';
        else if (type === 'weekly') titleText = '周增长排行 (Top {top_n})';
        else if (type === 'monthly') titleText = '月增长排行 (Top {top_n})';

        if (!currentData || currentData.categories.length === 0) {{
             return {{
                title: {{ text: titleText + ' (暂无数据)' }},
                xAxis: {{ show: false }},
                yAxis: {{ show: false }}
             }};
        }}

        return {{
            title: {{
                text: titleText,
                left: 'center'
            }},
            tooltip: {{
                trigger: 'axis',
                axisPointer: {{ type: 'shadow' }}
            }},
            grid: {{
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            }},
            xAxis: {{
                type: 'value',
                boundaryGap: [0, 0.01]
            }},
            yAxis: {{
                type: 'category',
                data: currentData.categories
            }},
            series: [{{
                name: 'Stars Growth',
                type: 'bar',
                data: currentData.data,
                itemStyle: {{
                    color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                        {{offset: 0, color: '#83bff6'}},
                        {{offset: 0.5, color: '#188df0'}},
                        {{offset: 1, color: '#188df0'}}
                    ])
                }},
                label: {{
                    show: true,
                    position: 'right'
                }}
            }}]
        }};
    }}

    // 初始化显示日榜
    option = getOption('daily');
    myChart.setOption(option);

    function updateChart(type) {{
        myChart.setOption(getOption(type));
    }}

    window.addEventListener('resize', function() {{
        myChart.resize();
    }});
</script>

"""
    # 生成 Markdown 表格
    if daily_data:
        content += "\n\n### 🚀 今日 Top 30 详情\n\n"
        content += "| 排名 | 仓库 | 增长 | 总 Stars |\n"
        content += "|---|---|---|---|\n"
        for i, repo in enumerate(daily_data[:30], 1):
            content += f"| {i} | [{repo['full_name']}]({repo['html_url']}) | +{repo['growth']} | {repo['stars']} |\n"
    else:
        content += "\n\n### 🚀 今日 Top 30 详情\n\n"
        content += "_日增长数据积累中，明日开始自动展示。_\n"

    if weekly_data:
        content += "\n\n### 📅 本周 Top 120 详情\n\n"
        content += "| 排名 | 仓库 | 增长 | 总 Stars |\n"
        content += "|---|---|---|---|\n"
        for i, repo in enumerate(weekly_data[:120], 1):
            content += f"| {i} | [{repo['full_name']}]({repo['html_url']}) | +{repo['growth']} | {repo['stars']} |\n"
    else:
        content += "\n\n### 📅 本周 Top 120 详情\n\n"
        content += "_周增长数据积累中，7 天后自动展示。_\n"

    if monthly_data:
        content += "\n\n### 🌙 本月 Top 300 详情\n\n"
        content += "| 排名 | 仓库 | 增长 | 总 Stars |\n"
        content += "|---|---|---|---|\n"
        for i, repo in enumerate(monthly_data[:300], 1):
            content += f"| {i} | [{repo['full_name']}]({repo['html_url']}) | +{repo['growth']} | {repo['stars']} |\n"
    else:
        content += "\n\n### 🌙 本月 Top 300 详情\n\n"
        content += "_月增长数据积累中，30 天后自动展示。_\n"

    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Report generated: {md_filepath}")


def main():
    # 1. 确定基准日期（今天或参数指定）
    if len(sys.argv) > 1 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        today_str = sys.argv[1]
        latest_file = snapshot_path(today_str)
        print(f"Manual date override: {today_str}")
    else:
        latest_file = find_latest_snapshot()

    if not latest_file or not os.path.exists(latest_file):
        print(f"Error: 未找到 {SNAPSHOT_PREFIX}*.json 快照，请先运行 FetchTopRepos.py。")
        return

    today_str = parse_date_from_filename(os.path.basename(latest_file))

    real_today = datetime.datetime.utcnow().strftime("%Y%m%d")
    if today_str != real_today:
        print(f"Warning: 最新快照日期为 {today_str}，而非今天 {real_today}。")

    base_date = datetime.datetime.strptime(today_str, "%Y%m%d")
    print(f"当前基准日期: {today_str}")

    # 2. 加载今日快照
    today_data = load_snapshot(latest_file)

    # 3. 计算日/周/月增长（基线为 1/7/30 天前的快照）
    print("Computing Daily Growth...")
    daily_growth = compute_growth(
        today_data,
        load_snapshot(snapshot_path(date_offset(base_date, 1))),
        date_offset(base_date, 1),
    )

    print("Computing Weekly Growth...")
    weekly_growth = compute_growth(
        today_data,
        load_snapshot(snapshot_path(date_offset(base_date, 7))),
        date_offset(base_date, 7),
    )

    print("Computing Monthly Growth...")
    monthly_growth = compute_growth(
        today_data,
        load_snapshot(snapshot_path(date_offset(base_date, 30))),
        date_offset(base_date, 30),
    )

    print(f"daily={len(daily_growth)} weekly={len(weekly_growth)} monthly={len(monthly_growth)}")

    # 4. 生成报告
    generate_echarts_html(daily_growth, weekly_growth, monthly_growth, today_str)


if __name__ == "__main__":
    main()
