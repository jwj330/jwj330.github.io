"""
GitHub Stars增长榜分析脚本
每天分析前1000个仓库的stars增长情况
生成前500名增长榜的Markdown文件
"""

import json
import os
import sys
import datetime
from collections import defaultdict
from typing import List, Dict, Any


def parse_date_from_filename(filename: str) -> str:
    """从文件名解析日期"""
    # 从类似 github_top_1000_20251221.json 提取日期
    date_str = filename.replace("github_top_1000_", "").replace(".json", "")
    return date_str


def format_offertime(date_str: str) -> str:
    """将YYYYMMDD格式转换为YYYY-MM-DD格式"""
    if len(date_str) == 8 and date_str.isdigit():
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_str


def load_json_file(filepath: str) -> Dict[str, Dict[str, Any]]:
    """加载JSON文件并转换为以id为key的字典"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 将列表转换为以id为key的字典
        repo_dict = {}
        for repo in data:
            repo_dict[str(repo['id'])] = repo
        return repo_dict
    except FileNotFoundError:
        print(f"文件不存在: {filepath}")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return {}
    except Exception as e:
        print(f"加载文件时出错 {filepath}: {e}")
        return {}


def calculate_growth(today_data: Dict[str, Dict], yesterday_data: Dict[str, Dict]) -> List[Dict]:
    """
    计算stars增长
    返回按增长量降序排列的仓库列表
    """
    growth_data = []
    
    for repo_id, today_repo in today_data.items():
        growth_info = {
            'id': today_repo['id'],
            'full_name': today_repo['full_name'],
            'stars': today_repo['stars'],
            'created_at': today_repo.get('created_at', ''),
            'pushed_at': today_repo.get('pushed_at', ''),
            'offertime': today_repo.get('offertime', ''),
        }
        
        # 查找昨天的数据
        if repo_id in yesterday_data:
            yesterday_stars = yesterday_data[repo_id]['stars']
            growth = today_repo['stars'] - yesterday_stars
        else:
            # 如果昨天不在榜，增长量就是今天的stars数
            growth = today_repo['stars']
            # 如果没有昨天的创建时间等信息，使用今天的数据
            growth_info['created_at'] = growth_info.get('created_at', '')
            growth_info['pushed_at'] = growth_info.get('pushed_at', '')
        
        growth_info['growth'] = growth
        growth_data.append(growth_info)
    
    # 按增长量降序排序
    growth_data.sort(key=lambda x: x['growth'], reverse=True)
    
    return growth_data


def get_yesterday_date(today_date: str) -> str:
    """获取昨天的日期字符串（YYYYMMDD格式）"""
    try:
        # 从字符串解析日期
        today = datetime.datetime.strptime(today_date, "%Y%m%d")
        yesterday = today - datetime.timedelta(days=1)
        return yesterday.strftime("%Y%m%d")
    except ValueError:
        # 如果日期格式错误，尝试计算前一天
        print(f"日期格式错误: {today_date}")
        return ""


def find_latest_data_file(data_dir: str = "") -> str:
    """查找最新的数据文件"""
    # 在上一级的 scriptData 目录中查找
    script_data_dir = os.path.join(data_dir, "scriptData")
    
    if not os.path.exists(script_data_dir):
        print(f"警告: scriptData目录不存在: {script_data_dir}")
        # 尝试在当前目录的上一级查找
        script_data_dir = os.path.join("", "scriptData")
        if not os.path.exists(script_data_dir):
            print(f"错误: scriptData目录不存在: {script_data_dir}")
            return ""
    
    print(f"正在搜索数据目录: {script_data_dir}")
    
    try:
        json_files = [f for f in os.listdir(script_data_dir) 
                     if f.startswith('github_top_1000_') and f.endswith('.json')]
        
        if not json_files:
            print(f"在 {script_data_dir} 中未找到 github_top_1000_*.json 文件")
            return ""
        
        # 按日期排序，返回最新的文件
        json_files.sort(reverse=True)
        latest_file = json_files[0]
        file_path = os.path.join(script_data_dir, latest_file)
        
        print(f"找到最新文件: {file_path}")
        return file_path
    except Exception as e:
        print(f"查找文件时出错: {e}")
        return ""


def get_data_file_path(date_str: str) -> str:
    """根据日期获取数据文件路径"""
    # 在上一级的 scriptData 目录中查找
    script_data_dir = os.path.join("", "scriptData")
    
    if not os.path.exists(script_data_dir):
        # 如果上一级没有，尝试在当前目录的上一级
        script_data_dir = os.path.join("", "scriptData")
        if not os.path.exists(script_data_dir):
            # 最后尝试直接使用相对路径
            script_data_dir = "scriptData"
    
    filename = f"github_top_1000_{date_str}.json"
    file_path = os.path.join(script_data_dir, filename)
    
    return file_path


def generate_markdown_file(data: List[Dict], date_str: str):
    """生成Markdown文件，按照要求创建目录和文件"""
    
    # 生成目录名
    dir_name = f"content/post/anagithub{date_str}"
    
    # 创建目录
    os.makedirs(dir_name, exist_ok=True)
    
    # 创建Markdown文件路径
    md_filepath = os.path.join(dir_name, "index.md")
    
    # 格式化日期
    formatted_date = format_offertime(date_str)
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(md_filepath, 'w', encoding='utf-8') as f:
        # 写入Front Matter
        f.write("---\n")
        f.write(f'title: "GitHub Top500增长榜{date_str}"\n')
        f.write(f'description: "GitHub增长榜 Top500"\n')
        f.write(f'date: {formatted_date} 14:22:51+0000\n')
        f.write("categories:\n")
        f.write("  - GitHub Top500\n")
        f.write("---\n\n")
        
        # 写入标题
        f.write(f"# GitHub Top500增长榜{date_str}\n\n")
        f.write(f"**生成时间**: {current_datetime}\n\n")
        f.write("以下是GitHub增长最快的500个仓库，按24小时内star增长数排序。\n\n")
        
        # 写入表格
        f.write("| 排名 | 仓库 | Stars | 增长 | 创建时间 | 最后更新 |\n")
        f.write("|------|------|-------|------|----------|----------|\n")
        
        # 写入前500名数据
        for repo in data:
            # 截断过长的仓库名
            repo_name = repo['full_name']
            if len(repo_name) > 40:
                repo_name = repo_name[:37] + "..."
            
            f.write(f"| {repo['rank']} | [{repo['full_name']}](https://github.com/{repo['full_name']}) | "
                   f"{repo['stars']:,} | +{repo['growth']:,} | "
                   f"{repo['created_at'][:10] if repo['created_at'] else 'N/A'} | "
                   f"{repo['pushed_at'][:10] if repo['pushed_at'] else 'N/A'} |\n")
    
    print(f"Markdown文件已生成: {md_filepath}")
    return md_filepath


def save_growth_json(data: List[Dict], date_str: str):
    """保存增长榜JSON文件到指定目录"""
    # 确保输出目录存在
    output_dir = "scriptDataGrowth"
    os.makedirs(output_dir, exist_ok=True)
    
    # 构建输出文件路径
    output_filename = f"github_stars_growth_top_500_{date_str}.json"
    output_path = os.path.join(output_dir, output_filename)
    
    # 保存结果到JSON文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"增长榜JSON结果已保存到: {output_path}")
    return output_path


def main():
    """主函数：计算增长榜前500"""
    
    # 方法1：自动查找最新的数据文件
    latest_file = find_latest_data_file()
    if latest_file:
        filename_only = os.path.basename(latest_file)
        today_date_str = parse_date_from_filename(filename_only)
        today_file = latest_file
    else:
        # 方法2：使用今天的日期
        today = datetime.datetime.now()
        today_date_str = today.strftime("%Y%m%d")
        today_file = get_data_file_path(today_date_str)
    
    # 计算昨天的日期和文件名
    yesterday_date_str = get_yesterday_date(today_date_str)
    if not yesterday_date_str:
        print("无法计算昨天的日期")
        return
    
    yesterday_file = get_data_file_path(yesterday_date_str)
    
    print(f"分析数据:")
    print(f"今天文件: {today_file}")
    print(f"昨天文件: {yesterday_file}")
    
    # 加载数据
    print("正在加载数据...")
    today_data = load_json_file(today_file)
    yesterday_data = load_json_file(yesterday_file)
    
    if not today_data:
        print(f"今天的数据文件不存在或为空: {today_file}")
        return
    
    if not yesterday_data:
        print(f"警告: 昨天的数据文件不存在: {yesterday_file}")
        print("将只使用今天的数据计算增长榜")
    
    # 计算增长
    print("正在计算增长榜...")
    growth_data = calculate_growth(today_data, yesterday_data)
    
    # 获取前500
    top_500 = growth_data[:500]
    
    # 准备输出数据
    output_data = []
    for i, repo in enumerate(top_500, 1):
        repo_info = {
            'rank': i,
            'id': repo['id'],
            'full_name': repo['full_name'],
            'stars': repo['stars'],
            'growth': repo['growth'],
            'created_at': repo['created_at'],
            'pushed_at': repo['pushed_at'],
            'offertime': format_offertime(today_date_str)
        }
        output_data.append(repo_info)
    
    # 保存结果到JSON文件（修改后的保存路径）
    save_growth_json(output_data, today_date_str)
    
    print(f"\n分析完成！")
    print(f"总共分析仓库数: {len(growth_data)}")
    
    # 输出前10名预览
    print(f"增长榜前10名:")
    print("-" * 100)
    
    for i, repo in enumerate(output_data[:10], 1):
        print(f"{i:3d}. {repo['full_name'][:40]:40s} stars: {repo['stars']:7d} "
              f"增长: {repo['growth']:+7d} 创建时间: {repo['created_at']}")
    
    # 输出一些统计信息
    print("\n统计信息:")
    print(f"平均增长: {sum(r['growth'] for r in top_500) / len(top_500):.1f}")
    print(f"最大增长: {max(r['growth'] for r in top_500)}")
    print(f"最小增长: {min(r['growth'] for r in top_500)}")
    
    # 生成Markdown文件
    md_filepath = generate_markdown_file(output_data, today_date_str)
    
    # 输出前10名的Markdown表格格式预览
    print(f"\nMarkdown文件前10行预览:")
    print("-" * 100)
    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines[:20]):  # 预览前20行
            print(line.rstrip())


def analyze_specific_date(target_date: str):
    """分析指定日期的增长榜"""
    print(f"正在分析 {target_date} 的增长榜...")
    
    today_file = get_data_file_path(target_date)
    yesterday_date_str = get_yesterday_date(target_date)
    
    if not yesterday_date_str:
        print("无法计算昨天的日期")
        return
    
    yesterday_file = get_data_file_path(yesterday_date_str)
    
    print(f"今天文件: {today_file}")
    print(f"昨天文件: {yesterday_file}")
    
    # 重新运行主逻辑
    today_data = load_json_file(today_file)
    yesterday_data = load_json_file(yesterday_file)
    
    if not today_data:
        print(f"数据文件不存在: {today_file}")
        return
    
    growth_data = calculate_growth(today_data, yesterday_data)
    top_500 = growth_data[:500]
    
    # 输出结果
    output_data = []
    for i, repo in enumerate(top_500, 1):
        repo_info = {
            'rank': i,
            'id': repo['id'],
            'full_name': repo['full_name'],
            'stars': repo['stars'],
            'growth': repo['growth'],
            'created_at': repo['created_at'],
            'pushed_at': repo['pushed_at'],
            'offertime': format_offertime(target_date)
        }
        output_data.append(repo_info)
    
    # 保存结果到JSON文件（修改后的保存路径）
    save_growth_json(output_data, target_date)
    
    # 生成Markdown文件
    generate_markdown_file(output_data, target_date)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # 如果有命令行参数，分析指定日期的数据
        target_date = sys.argv[1]
        analyze_specific_date(target_date)
    else:
        # 没有参数，分析今天的数据
        main()
