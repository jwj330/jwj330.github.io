import requests
import json
import os
from datetime import datetime
import time

def fetch_ossinsight_trends(period="past_24_hours", language="All"):
    """
    从 OSS Insight API 获取趋势数据
    period: past_24_hours, past_week, past_month
    language: All, Python, JavaScript, etc.
    """
    url = "https://api.ossinsight.io/v1/trends/repos/"
    params = {
        "period": period,
        "language": language
    }
    
    print(f"Fetching trending repos for {period} (Language: {language})...")
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            break # 成功则退出重试
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed for {period}/{language}: {e}. Retrying in 5s...")
                time.sleep(5)
            else:
                print(f"All {max_retries} attempts failed for {period}/{language}: {e}")
                return []
    
    try:
        repos = []
        if isinstance(data, list):
            repos = data
        elif isinstance(data, dict):
            if "data" in data:
                inner = data["data"]
                if isinstance(inner, list):
                    repos = inner
                elif isinstance(inner, dict) and "rows" in inner:
                    repos = inner["rows"]
            elif "rows" in data:
                rows = data["rows"]
                if rows and isinstance(rows[0], list) and "columns" in data:
                    columns = data["columns"]
                    repos = [dict(zip(columns, row)) for row in rows]
                else:
                    repos = rows
        
        if not repos:
            return []

        formatted_repos = []
        for repo in repos:
            if not isinstance(repo, dict):
                continue
            
            repo_name = repo.get("repo_name") or repo.get("full_name")
            growth = repo.get("stars") or repo.get("growth") or 0
            
            if not repo_name:
                continue

            formatted_repos.append({
                "id": repo.get("repo_id") or repo.get("id"),
                "full_name": repo_name,
                "growth": int(float(growth)) if growth else 0,
                "stars": int(float(repo.get("total_stars") or repo.get("stargazers_count") or 0)),
                "forks": int(float(repo.get("forks") or repo.get("forks_count") or 0)),
                "description": repo.get("description", ""),
                "html_url": f"https://github.com/{repo_name}",
                "offertime": datetime.now().strftime("%Y-%m-%d")
            })
        
        return formatted_repos
    except Exception as e:
        print(f"Error parsing data for {period}/{language}: {e}")
        return []

def get_latest_data_date():
    """从 scriptData 中查找最新的 github_top_1000 文件的日期"""
    import os
    if not os.path.exists("scriptData"):
        return datetime.now().strftime("%Y%m%d")
    files = [f for f in os.listdir("scriptData") if f.startswith("github_top_1000_") and f.endswith(".json")]
    if not files:
        # 如果没有 api 数据，尝试找 gharchive 数据
        files = [f for f in os.listdir("scriptData") if f.startswith("gharchive_growth_") and f.endswith(".json")]
    if not files:
        return datetime.now().strftime("%Y%m%d")
    files.sort(reverse=True)
    import re
    match = re.search(r'(\d{8})', files[0])
    return match.group(1) if match else datetime.now().strftime("%Y%m%d")

def load_local_stars_cache():
    """从本地最新的 github_top_1000 文件加载 Star 数作为缓存"""
    cache = {}
    data_dir = "scriptData"
    if not os.path.exists(data_dir):
        return cache
    
    files = [f for f in os.listdir(data_dir) if (f.startswith("github_top_1000_") or f.startswith("gharchive_growth_past_24_hours_")) and f.endswith(".json")]
    if not files:
        # 兜底查找任何周期的数据
        files = [f for f in os.listdir(data_dir) if f.startswith("gharchive_growth_") and f.endswith(".json")]
    if not files:
        return cache
    
    files.sort(reverse=True)
    latest_file = os.path.join(data_dir, files[0])
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for repo in data:
                rid = str(repo.get('id'))
                stars = repo.get('stars', 0)
                if rid and stars and int(stars) > 0:
                    cache[rid] = int(stars)
    except Exception as e:
        print(f"Warning: Failed to load local stars cache: {e}")
    
    return cache

def fetch_github_stars_bulk(repos, token, cache):
    """
    智能获取 Star 数：优先使用缓存，其次使用 GraphQL，最后兜底使用 REST API
    """
    if not repos:
        return repos
    
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    missing_repos = []
    for repo in repos:
        rid = str(repo.get('id'))
        # 只有当 repo 里的 stars 是 0 时才尝试从 cache 补全
        if repo.get('stars', 0) == 0:
            if rid in cache and cache[rid] > 0:
                repo['stars'] = cache[rid]
                # 注意：补全后依然是 "missing_repos" 吗？不，补全后就不需要 fetch 了
            else:
                missing_repos.append(repo)
    
    if not missing_repos:
        return repos

    print(f"Cache miss for {len(missing_repos)} repos. Fetching from GitHub...")

    # 如果有 Token，使用 GraphQL 批量获取
    if token:
        batch_size = 50
        for i in range(0, len(missing_repos), batch_size):
            batch = missing_repos[i:i+batch_size]
            nodes_query = ""
            for index, repo in enumerate(batch):
                full_name = repo['full_name']
                if '/' not in full_name: continue
                owner, name = full_name.split('/', 1)
                alias = f"repo_{index}"
                nodes_query += f'  {alias}: repository(owner: "{owner}", name: "{name}") {{ stargazerCount }}\n'
            
            query = f"{{\n{nodes_query}\n}}"
            try:
                response = requests.post("https://api.github.com/graphql", headers=headers, json={"query": query}, timeout=30)
                if response.status_code == 200:
                    data = response.json().get("data", {})
                    for index, repo in enumerate(batch):
                        alias = f"repo_{index}"
                        if alias in data and data[alias]:
                            repo['stars'] = data[alias].get("stargazerCount", 0)
                elif response.status_code == 401:
                    print("Unauthorized: GraphQL token invalid.")
                    break
            except Exception as e:
                print(f"GraphQL Error: {e}")
            time.sleep(0.5)
    else:
        # 如果没有 Token，使用 REST API 兜底 (受速率限制)
        print("No GitHubToken found. Using REST API fallback (limited rate)...")
        for repo in missing_repos[:30]: # 本地核对时只补全前 30 个，避免被封 IP
            full_name = repo['full_name']
            try:
                url = f"https://api.github.com/repos/{full_name}"
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    repo['stars'] = resp.json().get("stargazers_count", 0)
                elif resp.status_code == 403:
                    print("Github API Rate limit exceeded.")
                    break
            except Exception:
                pass
            time.sleep(0.8)

    return repos

def main():
    periods = ["past_24_hours", "past_week", "past_month"]
    languages = ["All", "Python", "JavaScript", "Java", "TypeScript", "Go", "Rust", "C++", "C", "PHP", "Ruby", "Haskell", "Swift"]
    data_dir = "scriptData"
    os.makedirs(data_dir, exist_ok=True)
    
    token = os.getenv('GITHUBTOKEN')
    if token:
        print("Using GitHub token from environment variable: GITHUBTOKEN")
    else:
        print("Warning: GITHUBTOKEN environment variable not found.")

    # 获取真实当前日期 (也可以通过参数覆盖)
    import sys
    timestamp = datetime.now().strftime("%Y%m%d")
    if len(sys.argv) > 1 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        timestamp = sys.argv[1]
        print(f"Manual date override: {timestamp}")
    else:
        print(f"Current Date for generation: {timestamp}")
    
    if os.getenv('GITHUB_ACTIONS') == 'true':
        print("Running in GitHub Actions environment.")
        if not token:
            print("WARNING: GITHUBTOKEN is missing in Actions! Data will be incomplete due to rate limits.")
    else:
        print("Running in local environment.")

    cache = load_local_stars_cache()
    
    for period in periods:
        all_period_repos = []
        seen_ids = set()
        
        for lang in languages:
            repos = fetch_ossinsight_trends(period, lang)
            for r in repos:
                rid = str(r.get('id'))
                if rid not in seen_ids:
                    all_period_repos.append(r)
                    seen_ids.add(rid)
            
            if period == "past_24_hours" and len(all_period_repos) >= 100:
                break
            if period == "past_week" and len(all_period_repos) >= 150:
                break
            if period == "past_month" and len(all_period_repos) >= 350:
                break
            time.sleep(0.5)
        
        # 补全 Star 数
        print(f"Updating stars for {len(all_period_repos)} repos ({period})...")
        all_period_repos = fetch_github_stars_bulk(all_period_repos, token, cache)

        all_period_repos.sort(key=lambda x: x['growth'], reverse=True)
        
        if all_period_repos:
            filename = f"gharchive_growth_{period}_{timestamp}.json"
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(all_period_repos, f, indent=2, ensure_ascii=False)
            print(f"Successfully saved {len(all_period_repos)} repos to {os.path.abspath(filepath)}")
        time.sleep(1)

if __name__ == "__main__":
    main()
