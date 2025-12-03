import requests
from datetime import datetime, timedelta
import os
from pathlib import Path
import time

def get_github_token():
    """
    从环境变量获取GitHub Token
    """
    token = os.getenv('GitHubToken')
    if not token:
        print("警告: 未找到GitHubToken环境变量，将以未认证状态访问API（限制60次/小时）")
    return token

def get_top_repos_by_language(language, token=None, per_page=10):
    """
    获取指定语言stars数前10的仓库信息（支持Token认证）
    """
    # GitHub API地址，按语言和stars数降序排列
    url = f"https://api.github.com/search/repositories?q=language:{language}+stars:>1000&sort=stars&order=desc&per_page={per_page}"
    
    # 设置请求头
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Python-Script'
    }
    
    # 如果提供了Token，添加到请求头中
    if token:
        headers['Authorization'] = f'token {token}'
    
    try:
        # 发送API请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        # 打印速率限制信息（用于调试）
        if 'X-RateLimit-Remaining' in response.headers:
            remaining = response.headers['X-RateLimit-Remaining']
            limit = response.headers['X-RateLimit-Limit']
            print(f"速率限制: 剩余 {remaining}/{limit} 次请求")
        
        return {
            'language': language,
            'items': data['items']
        }
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            # 处理速率限制
            if 'X-RateLimit-Reset' in response.headers:
                reset_time = int(response.headers['X-RateLimit-Reset'])
                sleep_duration = reset_time - int(time.time()) + 1
                print(f"API速率限制已超出，等待 {sleep_duration} 秒后重试...")
                time.sleep(sleep_duration)
                # 重试一次
                return get_top_repos_by_language(language, token, per_page)
            else:
                print(f"GitHub API访问被拒绝: {e}")
        else:
            print(f"获取{language}语言GitHub数据时出错: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
        return None

def get_all_languages_top_repos(languages=None):
    """
    获取多种编程语言的top仓库（支持Token认证）
    """
    if languages is None:
        languages = ['python', 'javascript', 'java', 'go', 'rust', 'typescript', 'c++', 'c', 'php', 'ruby']
    
    # 获取GitHub Token
    token = get_github_token()
    
    if token:
        print("使用GitHub Token认证，速率限制提升至5000次/小时")
    else:
        print("未使用Token认证，速率限制为60次/小时，建议设置GitHubToken环境变量")
    
    all_repos = []
    failed_languages = []
    
    for i, language in enumerate(languages):
        print(f"正在获取{language}语言的仓库信息... ({i+1}/{len(languages)})")
        repos = get_top_repos_by_language(language, token)
        
        if repos and repos['items']:
            all_repos.append(repos)
            print(f"成功获取{language}语言 {len(repos['items'])} 个仓库")
        else:
            failed_languages.append(language)
            print(f"获取{language}语言仓库信息失败")
        
        # 添加延迟避免API限制（即使有Token也要礼貌使用）
        if i < len(languages) - 1:  # 最后一个请求后不需要等待
            delay = 1 if token else 2  # 有Token时可以稍快一些
            print(f"等待{delay}秒后继续...")
            time.sleep(delay)
    
    if failed_languages:
        print(f"以下语言获取失败: {', '.join(failed_languages)}")
    
    return all_repos

def generate_markdown_content(all_repos_data):
    """
    生成Markdown格式的内容
    """
    # 获取当前时间并提前6小时，然后格式化
    current_time = datetime.now() - timedelta(hours=6)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S+0000")
    nowday = current_time.strftime("%Y%m%d")
    
    # 生成前置内容
    front_matter = f"""---
title: "GitHub各编程语言Stars Top 10仓库{nowday}"
description: "GitHub各主流编程语言Stars数排名前10的开源仓库汇总"
date: {formatted_time}
categories:
  - GitHub
  - 编程语言
  - 开源项目
tags:
  - GitHub
  - 编程语言
  - 开源
  - 排行榜
---

# GitHub各编程语言Stars Top 10仓库排名

> 统计时间：{current_time.strftime('%Y年%m月%d日 %H:%M')} UTC+0
> 
> 数据来源：GitHub官方API
> 
> 注：时间为发布时间

以下是GitHub上各主流编程语言stars数排名前10的开源仓库信息：

"""
    
    markdown_content = front_matter
    
    # 为每种语言生成章节
    for repo_data in all_repos_data:
        language = repo_data['language']
        repos = repo_data['items']
        
        markdown_content += f"\n## {language.upper()} 语言Top 10仓库\n\n"
        markdown_content += f"| 排名 | 仓库名称 | Stars数 | 描述 | 更新时间 |\n"
        markdown_content += f"|------|----------|---------|------|----------|\n"
        
        # 添加每个仓库的信息
        for i, repo in enumerate(repos, 1):
            full_name = repo['full_name']
            stars = repo['stargazers_count']
            description = repo['description'] or "无描述"
            description = description.replace('|', '\\|').replace('\n', ' ').replace('\r', '')
            updated_at = repo['updated_at'][:10]  # 只取日期部分
            
            markdown_content += f"| {i} | [{full_name}]({repo['html_url']}) | {stars:,} | {description} | {updated_at} |\n"
    
    # 添加详细说明部分
    markdown_content += """
## 仓库详细信息

"""
    
    for repo_data in all_repos_data:
        language = repo_data['language']
        repos = repo_data['items']
        
        markdown_content += f"\n### {language.upper()} 语言详细仓库信息\n\n"
        
        for i, repo in enumerate(repos, 1):
            # 安全地处理许可证信息
            license_info = repo.get('license')
            if license_info and isinstance(license_info, dict):
                license_name = license_info.get('name', '未指定')
            else:
                license_name = '未指定'
            
            markdown_content += f"""
#### {i}. {repo['full_name']}

- **Stars数**: {repo['stargazers_count']:,}
- **Forks数**: {repo['forks_count']:,}
- **Watch数**: {repo['watchers_count']:,}
- **开源协议**: {license_name}
- **创建时间**: {repo['created_at'][:10]}
- **更新时间**: {repo['updated_at'][:10]}
- **主要语言**: {repo['language'] or "未指定"}
- **项目地址**: [{repo['html_url']}]({repo['html_url']})

**项目描述**: {repo['description'] or "暂无描述"}

"""
    
    # 添加统计信息
    total_repos = sum(len(repo_data['items']) for repo_data in all_repos_data)
    total_languages = len(all_repos_data)
    
    markdown_content += f"""
## 统计信息

- **统计时间**: {current_time.strftime('%Y年%m月%d日 %H:%M')}
- **覆盖编程语言数量**: {total_languages}种
- **总仓库数量**: {total_repos}个
- **数据来源**: GitHub官方API

## 说明

1. 数据通过GitHub官方API获取，保证数据的准确性和实时性
2. 排名依据为项目的Stars数量
3. 每个语言取Stars数最多的前10个仓库
4. 时间为文章发布时间，已按需求提前6小时

"""
    
    return markdown_content, nowday

def create_directory(path):
    """
    创建目录，如果目录不存在的话
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        print(f"目录创建成功: {path}")
        return True
    except Exception as e:
        print(f"创建目录时出错: {e}")
        return False

def save_to_markdown_file(content, save_path):
    """
    将内容保存到Markdown文件
    """
    try:
        # 确保目录存在
        directory = os.path.dirname(save_path)
        if not create_directory(directory):
            return False
        
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"文件已保存为: {save_path}")
        return True
    except Exception as e:
        print(f"保存文件时出错: {e}")
        return False

def main():
    """
    主函数
    """
    print("正在获取GitHub各编程语言stars前10的仓库信息...")
    
    # 定义要获取的编程语言列表
    languages = [
        'python', 'javascript', 'java', 'go', 'rust', 
        'typescript', 'c++', 'c', 'php', 'ruby',
        'swift', 'kotlin', 'scala', 'html', 'css'
    ]
    
    # 获取所有语言的仓库信息
    all_repos_data = get_all_languages_top_repos(languages)
    
    if not all_repos_data:
        print("无法获取GitHub仓库信息，请检查网络连接后重试")
        return
    
    print(f"成功获取{len(all_repos_data)}种语言的仓库信息，正在生成Markdown文件...")
    
    # 生成Markdown内容
    markdown_content, nowday = generate_markdown_content(all_repos_data)
    
    # 构建保存路径
    current_time = datetime.now() - timedelta(hours=6)
    save_dir = f"content/post/github{nowday}"
    save_path = os.path.join(save_dir, "index.md")
    
    # 保存到文件
    if save_to_markdown_file(markdown_content, save_path):
        print("Markdown文件生成成功！")
        
        # 统计信息
        total_repos = sum(len(repo_data['items']) for repo_data in all_repos_data)
        languages_list = [repo_data['language'] for repo_data in all_repos_data]
        
        print(f"共处理 {len(languages_list)} 种编程语言，{total_repos} 个仓库信息")
        print(f"涵盖语言: {', '.join(languages_list)}")
        print(f"文件保存路径: {save_path}")
    else:
        print("文件生成失败")

if __name__ == "__main__":
    main()
