
import json
import os
import sys
import datetime
from typing import List, Dict, Any

def parse_date_from_filename(filename: str) -> str:
    """从文件名解析日期 (支持 gharchive 和 github_top_1000)"""
    import re
    match = re.search(r'(\d{8})', filename)
    return match.group(1) if match else ""

def format_offertime(date_str: str) -> str:
    """将YYYYMMDD格式转换为YYYY-MM-DD格式"""
    if len(date_str) == 8 and date_str.isdigit():
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_str

def load_json_file(filepath: str) -> Dict[str, Dict[str, Any]]:
    """加载JSON文件并转换为以id为key的字典"""
    if not filepath or not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        repo_dict = {}
        for repo in data:
            # 兼容不同来源的 ID 字段名
            repo_id = str(repo.get('id') or repo.get('repo_id'))
            repo_dict[repo_id] = repo
        return repo_dict
    except Exception as e:
        print(f"加载文件时出错 {filepath}: {e}")
        return {}

def calculate_growth(today_data: Dict[str, Dict], past_data: Dict[str, Dict], gh_growth_data: Dict[str, Dict] = None) -> List[Dict]:
    """计算stars增长，优先使用传入的 gh_growth_data (GH Archive)"""
    growth_data = []
    
    # 如果有 GH Archive 增长数据，直接转换格式
    if gh_growth_data:
        for repo_id, repo in gh_growth_data.items():
            growth_info = {
                'id': repo.get('id') or repo.get('repo_id'),
                'full_name': repo['full_name'],
                'stars': repo.get('stars') or repo.get('total_stars') or 0,
                'growth': int(repo.get('growth', 0)),
                'description': repo.get('description', ''),
                'html_url': repo.get('html_url') or f"https://github.com/{repo['full_name']}"
            }
            growth_data.append(growth_info)
        
        # 排序并返回
        growth_data.sort(key=lambda x: x['growth'], reverse=True)
        return growth_data

    # 兜底逻辑：使用原有的差值计算
    if not past_data:
        return []

    for repo_id, today_repo in today_data.items():
        growth = 0
        if repo_id in past_data:
            growth = today_repo['stars'] - past_data[repo_id]['stars']
        else:
            growth = today_repo['stars']

        if growth > 0:
            growth_info = {
                'id': today_repo['id'],
                'full_name': today_repo['full_name'],
                'stars': today_repo['stars'],
                'growth': growth,
                'description': today_repo.get('description', ''),
                'html_url': f"https://github.com/{today_repo['full_name']}"
            }
            growth_data.append(growth_info)
    
    growth_data.sort(key=lambda x: x['growth'], reverse=True)
    return growth_data

def get_date_str(base_date: datetime.datetime, days_delta: int) -> str:
    """获取偏移日期的字符串 YYYYMMDD"""
    target_date = base_date - datetime.timedelta(days=days_delta)
    return target_date.strftime("%Y%m%d")

def find_latest_data_file(data_dir: str = "") -> str:
    """查找最新的 GH Archive 数据文件（过去 24 小时）"""
    script_data_dir = os.path.join(data_dir, "scriptData")
    if not os.path.exists(script_data_dir):
        script_data_dir = "scriptData" 
    
    if not os.path.exists(script_data_dir):
        return ""
        
    try:
        # 优先使用 gharchive 数据作为基准
        json_files = [f for f in os.listdir(script_data_dir) 
                     if f.startswith('gharchive_growth_past_24_hours_') and f.endswith('.json')]
        if not json_files:
            # 兜底旧文件
            json_files = [f for f in os.listdir(script_data_dir) 
                         if f.startswith('github_top_1000_') and f.endswith('.json')]
        
        if not json_files:
            return ""
        json_files.sort(reverse=True)
        return os.path.join(script_data_dir, json_files[0])
    except Exception:
        return ""

def get_data_file_path(date_str: str) -> str:
    """根据日期获取 API 数据文件路径 (用于计算 stars, 如果存在)"""
    script_data_dir = "scriptData"
    if not os.path.exists(script_data_dir):
        if os.path.exists(os.path.join("..", "scriptData")):
             script_data_dir = os.path.join("..", "scriptData")

    filename = f"gharchive_growth_past_24_hours_{date_str}.json"
    path = os.path.join(script_data_dir, filename)
    if os.path.exists(path):
        return path
    
    # 兜底旧格式
    filename = f"github_top_1000_{date_str}.json"
    return os.path.join(script_data_dir, filename)

def generate_echarts_html(daily_data, weekly_data, monthly_data, date_str):
    """生成带有ECharts的Hugo Markdown文件"""
    dir_name = f"content/post/anagithub{date_str}"
    os.makedirs(dir_name, exist_ok=True)
    md_filepath = os.path.join(dir_name, "index.md")
    
    formatted_date = format_offertime(date_str)
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 取前20名用于图表展示，避免图表过密
    top_n = 20
    
    # helper to process data for js
    def process_data(data):
        if not data: return [], [], []
        top = data[:top_n]
        names = [item['full_name'] for item in top]
        values = [item['growth'] for item in top]
        # 反转以在柱状图中从上到下显示
        return names[::-1], values[::-1], top

    d_names, d_values, _ = process_data(daily_data)
    w_names, w_values, _ = process_data(weekly_data)
    m_names, m_values, _ = process_data(monthly_data)

    # 序列化数据给JS使用
    daily_json = json.dumps({'categories': d_names, 'data': d_values}, ensure_ascii=False)
    weekly_json = json.dumps({'categories': w_names, 'data': w_values}, ensure_ascii=False)
    monthly_json = json.dumps({'categories': m_names, 'data': m_values}, ensure_ascii=False)

    # 计算标题和描述
    def get_clean_name(full_name):
        return full_name.split('/')[-1] if '/' in full_name else full_name

    article_title = f"{formatted_date} GitHub增长趋势报告"
    
    desc_items = [f"{i+1}.{get_clean_name(item['full_name'])}+{item['growth']}" for i, item in enumerate(daily_data[:5])]
    article_desc = " ".join(desc_items)

    # 计算日期：如果是今天，使用当前时间以确保 Hugo 立即可见
    today_now = datetime.datetime.now()
    if date_str == today_now.strftime("%Y%m%d"):
        post_date = today_now.strftime('%Y-%m-%dT%H:%M:%S+08:00')
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

本报告展示了 GitHub 上 Star 数增长最快的仓库。

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

    if weekly_data:
        content += "\n\n### 📅 本周 Top 120 详情\n\n"
        content += "| 排名 | 仓库 | 增长 | 总 Stars |\n"
        content += "|---|---|---|---|\n"
        for i, repo in enumerate(weekly_data[:120], 1):
            content += f"| {i} | [{repo['full_name']}]({repo['html_url']}) | +{repo['growth']} | {repo['stars']} |\n"

    if monthly_data:
        content += "\n\n### 🌙 本月 Top 300 详情\n\n"
        content += "| 排名 | 仓库 | 增长 | 总 Stars |\n"
        content += "|---|---|---|---|\n"
        for i, repo in enumerate(monthly_data[:300], 1):
            content += f"| {i} | [{repo['full_name']}]({repo['html_url']}) | +{repo['growth']} | {repo['stars']} |\n"

    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Report generated: {md_filepath}")


def main():
    # 1. 确定基准日期 (今天 或 参数指定)
    import sys
    today_str = ""
    latest_file = ""
    
    if len(sys.argv) > 1 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        today_str = sys.argv[1]
        latest_file = os.path.join("scriptData", f"gharchive_growth_past_24_hours_{today_str}.json")
        if not os.path.exists(latest_file):
             # 兜底旧格式
             latest_file = os.path.join("scriptData", f"github_top_1000_{today_str}.json")
        print(f"Manual date override: {today_str}")
    else:
        latest_file = find_latest_data_file()

    if not latest_file or not os.path.exists(latest_file):
        print("Error: No data files found in scriptData/. Please run FetchGHArchiveData.py first.")
        return

    filename_only = os.path.basename(latest_file)
    today_str = parse_date_from_filename(filename_only)
    
    # 检查是否是今天生成的
    real_today = datetime.datetime.now().strftime("%Y%m%d")
    if today_str != real_today:
        print(f"Warning: Latest data file found is from {today_str}, not today ({real_today}).")
    today = datetime.datetime.strptime(today_str, "%Y%m%d")
    
    print(f"当前基准日期: {today_str}")

    # 2. 计算目标日期
    yesterday_str = get_date_str(today, 1)
    last_week_str = get_date_str(today, 7)
    last_month_str = get_date_str(today, 30)

    # 3. 加载今日数据
    today_data = load_json_file(latest_file)
    
    # 4. 加载历史数据与 GH Archive 增长数据
    yesterday_data = load_json_file(get_data_file_path(yesterday_str))
    week_data = load_json_file(get_data_file_path(last_week_str))
    month_data = load_json_file(get_data_file_path(last_month_str))

    # 尝试加载 GH Archive 数据
    gh_daily_file = os.path.join("scriptData", f"gharchive_growth_past_24_hours_{today_str}.json")
    gh_weekly_file = os.path.join("scriptData", f"gharchive_growth_past_week_{today_str}.json")
    gh_monthly_file = os.path.join("scriptData", f"gharchive_growth_past_month_{today_str}.json")

    gh_daily_data = load_json_file(gh_daily_file) if os.path.exists(gh_daily_file) else None
    gh_weekly_data = load_json_file(gh_weekly_file) if os.path.exists(gh_weekly_file) else None
    gh_monthly_data = load_json_file(gh_monthly_file) if os.path.exists(gh_monthly_file) else None

    # 5. 计算增长
    print("Computing Daily Growth...")
    daily_growth = calculate_growth(today_data, yesterday_data, gh_daily_data)
    
    print("Computing Weekly Growth...")
    weekly_growth = calculate_growth(today_data, week_data, gh_weekly_data)
    
    print("Computing Monthly Growth...")
    monthly_growth = calculate_growth(today_data, month_data, gh_monthly_data)

    # 6. 生成报告
    generate_echarts_html(daily_growth, weekly_growth, monthly_growth, today_str)

if __name__ == "__main__":
    main()
