import requests
import json
import time
import os
from datetime import datetime

def get_github_top_repos(count=1000, token=None):
    """使用GraphQL API获取GitHub stars排名前N的仓库，并按指定格式保存"""
    
    if not token:
        print("警告: GitHub Token未提供，公开API调用限制更严格")
        headers = {"Accept": "application/vnd.github.v3+json"}
    else:
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    all_repos = []
    end_cursor = None
    has_next_page = True
    offertime = datetime.now().strftime("%Y-%m-%d")
    
    # GraphQL查询语句 - 更新字段以获取正确的id
    query_template = """
    query {{
      search(
        query: "stars:>1000 sort:stars-desc"
        type: REPOSITORY
        first: 100
        after: {cursor}
      ) {{
        repositoryCount
        pageInfo {{
          hasNextPage
          endCursor
        }}
        edges {{
          node {{
            ... on Repository {{
              databaseId
              nameWithOwner
              stargazerCount
              forkCount
              createdAt
              pushedAt
            }}
          }}
        }}
      }}
    }}
    """
    
    batch_count = 0
    
    while has_next_page and len(all_repos) < count:
        batch_count += 1
        print(f"正在获取第 {batch_count} 批数据...")
        
        # 构建查询参数
        cursor = f'"{end_cursor}"' if end_cursor else "null"
        query = query_template.format(cursor=cursor)
        
        payload = {
            "query": query
        }
        
        try:
            response = requests.post(
                "https://api.github.com/graphql",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            
            # 检查GraphQL错误
            if "errors" in data:
                print(f"GraphQL错误: {data['errors']}")
                break
                
            if "data" not in data or "search" not in data["data"]:
                print("没有获取到仓库数据")
                break
            
            search_data = data["data"]["search"]
            edges = search_data.get("edges", [])
            
            for edge in edges:
                if "node" in edge:
                    repo = edge["node"]
                    # 提取和格式化数据
                    formatted_repo = {
                        "id": repo.get("databaseId", 0),  # 使用databaseId获取数字ID
                        "full_name": repo.get("nameWithOwner", ""),
                        "stars": repo.get("stargazerCount", 0),
                        "forks": repo.get("forkCount", 0),
                        "created_at": repo.get("createdAt", "")[:10] if repo.get("createdAt") else "",  # 只取日期部分
                        "pushed_at": repo.get("pushedAt", "")[:10] if repo.get("pushedAt") else "",   # 只取日期部分
                        "offertime": offertime
                    }
                    
                    all_repos.append(formatted_repo)
            
            # 更新分页信息
            page_info = search_data.get("pageInfo", {})
            has_next_page = page_info.get("hasNextPage", False)
            end_cursor = page_info.get("endCursor")
            
            # 如果已获取足够数据，提前结束
            if len(all_repos) >= count:
                break
                
            # 遵守速率限制
            remaining = int(response.headers.get('X-RateLimit-Remaining', 1))
            if remaining < 10:
                print(f"剩余请求次数较少: {remaining}，等待1秒...")
                time.sleep(1)
            else:
                time.sleep(0.5)
                print("遵守速率限制，等0.5秒")
                
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
            break
        except Exception as e:
            print(f"处理数据时出错: {e}")
            break
    
    # 限制数量
    all_repos = all_repos[:count]
    
    # 创建数据目录
    data_dir = "scriptData"
    os.makedirs(data_dir, exist_ok=True)
    
    # 保存数据
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = os.path.join(data_dir, f"github_top_{len(all_repos)}_{timestamp}.json")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_repos, f, indent=2, ensure_ascii=False)
    
    print(f"\n成功获取 {len(all_repos)} 个仓库")
    print(f"数据已保存到: {filename}")
    
    # 显示前10名
    print(f"\nTop 10 仓库:")
    for i, repo in enumerate(all_repos[:10], 1):
        name = repo.get("full_name", "N/A")
        stars = repo.get("stars", 0)
        forks = repo.get("forks", 0)
        created = repo.get("created_at", "N/A")
        pushed = repo.get("pushed_at", "N/A")
        repo_id = repo.get("id", "N/A")
        
        # 如果name太长，截断
        if len(name) > 40:
            name = name[:37] + "..."
        
        print(f"{i:2}. {name:<40} stars: {stars:,}, forks: {forks:,}")
        print(f"    ID: {repo_id}, 创建于: {created}, 最后推送: {pushed}")
        print(f"    采集时间: {repo.get('offertime', 'N/A')}")
    
    return all_repos

# 使用REST API的备份函数，以防GraphQL失败
def get_github_top_repos_rest(count=1000, token=None):
    """备用：使用REST API获取GitHub stars排名前N的仓库"""
    
    # 设置请求头
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    all_repos = []
    page = 1
    offertime = datetime.now().strftime("%Y-%m-%d")
    
    while len(all_repos) < count:
        print(f"正在获取第 {page} 页...")
        
        # 搜索stars最多的仓库
        url = "https://api.github.com/search/repositories"
        params = {
            "q": "stars:>1000",
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            if "items" not in data:
                print("没有获取到仓库数据")
                break
                
            repos = data["items"]
            for repo in repos:
                formatted_repo = {
                    "id": repo.get("id"),
                    "full_name": repo.get("full_name"),
                    "stars": repo.get("stargazers_count", 0),  # 注意这里是stargazers_count
                    "forks": repo.get("forks_count", 0),
                    "created_at": repo.get("created_at", "")[:10] if repo.get("created_at") else "",
                    "pushed_at": repo.get("pushed_at", "")[:10] if repo.get("pushed_at") else "",
                    "offertime": offertime
                }
                all_repos.append(formatted_repo)
            
            # 检查是否还有更多
            if len(repos) < 100:
                break
                
            page += 1
            
            # 遵守速率限制
            remaining = int(response.headers.get('X-RateLimit-Remaining', 1))
            if remaining < 10:
                print(f"剩余请求次数较少: {remaining}，等待1秒...")
                time.sleep(1)
            else:
                time.sleep(0.5)
                print("遵守速率限制，等0.5秒")
                
        except Exception as e:
            print(f"获取数据时出错: {e}")
            break
    
    # 限制数量
    all_repos = all_repos[:count]
    
    # 创建数据目录
    data_dir = "scriptData"
    os.makedirs(data_dir, exist_ok=True)
    
    # 保存数据
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(data_dir, f"github_top_rest_{len(all_repos)}_{timestamp}.json")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_repos, f, indent=2, ensure_ascii=False)
    
    print(f"\n成功获取 {len(all_repos)} 个仓库")
    print(f"数据已保存到: {filename}")
    
    return all_repos

if __name__ == "__main__":
    # 使用方法1: 使用GraphQL API
    # token = os.getenv("GitHubToken")
    token = os.getenv('GitHubToken')
    try:
        repos = get_github_top_repos(count=1000, token=token)
    except Exception as e:
        print(f"GraphQL API失败: {e}")
        print("尝试使用REST API...")
        repos = get_github_top_repos_rest(count=1000, token=token)
