#!/usr/bin/env python3
"""
抓取 GitHub 按 Star 数排名的 Top 仓库，保存每日快照。

为什么改用本脚本：
    旧流程使用 OSS Insight 的趋势 API（以及 GH Archive 的 star 事件），
    但两者都依赖 GitHub 的公开事件流。该事件流自 ~2026 年起被大幅削弱，
    现在返回空数据或严重失真的数据。GitHub 的 Search API 直接从 GitHub
    同步准确的 Star/Fork 总数，因此改为每天抓取 Top-N Star 快照，
    再由 AnalyzeData2.py 对相邻快照做差分计算增长。

为什么需要“星数区间分片”：
    GitHub Search API 硬性限制单次查询最多返回前 1000 条结果
    （第 11 页会返回 HTTP 422 "Only the first 1000 search results are available"）。
    因此要拿到 Top-5000，必须把查询按星数区间（stars:lo..hi）切成若干片，
    每片最多 1000 条，逐片向下取，直到凑满目标数量。
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

SEARCH_URL = "https://api.github.com/search/repositories"
TOP_N = 5000            # 目标：每天记录 Top 5000（需分片才能突破单查询 1000 条上限）
PER_PAGE = 100          # 每页条数（Search API 上限）
MAX_PAGE = 10           # 每片最多 10 页 = 1000 条（Search API 硬上限）
DATA_DIR = "scriptData"
SNAPSHOT_PREFIX = f"github_top_{TOP_N}_"
MAX_RANGES = 30         # 安全上限，防止区间下探异常时死循环


def _headers(token):
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def _search(token, query, page, max_net_retries=6, max_rate_waits=20):
    """
    执行一次搜索请求。

    对两类可恢复错误做重试，避免一次瞬时故障就让整轮抓取失败：
      - 网络错误（超时 / 连接中断）：指数退避重试；
      - 速率限制（HTTP 403 "rate limit"）：等待到配额重置后重试。
    """
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": PER_PAGE,
        "page": page,
    }
    net_attempts = 0
    rate_waits = 0
    while True:
        try:
            resp = requests.get(SEARCH_URL, headers=_headers(token), params=params, timeout=30)
        except requests.RequestException as e:
            net_attempts += 1
            if net_attempts > max_net_retries:
                raise
            wait = min(5 * (2 ** (net_attempts - 1)), 60)
            print(f"  network error ({type(e).__name__}), retry "
                  f"{net_attempts}/{max_net_retries} in {wait}s ...")
            time.sleep(wait)
            continue

        # 命中速率限制：按 reset 时间等待，而不是直接失败
        if resp.status_code == 403 and "rate limit" in resp.text.lower():
            rate_waits += 1
            if rate_waits > max_rate_waits:
                resp.raise_for_status()
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - int(time.time()) + 2, 10)
            print(f"  rate limited, sleeping {wait}s ...")
            time.sleep(wait)
            continue

        resp.raise_for_status()
        return resp.json()


def _normalize(it):
    return {
        "id": it["id"],
        "full_name": it["full_name"],
        "stars": it.get("stargazers_count", 0),
        "forks": it.get("forks_count", 0),
        "description": it.get("description") or "",
        "html_url": it["html_url"],
        "created_at": it.get("created_at", ""),
    }


def fetch_top_repos(token, target_count=TOP_N):
    """
    按 Star 降序抓取 top `target_count` 个仓库。

    策略：从“无上界”开始，每次取某星数区间内排名最高的 ≤1000 条，
    然后把区间上界下移到本批最小星数 - 1，继续向下取，直到凑满目标数量。
    """
    sleep = 2.5 if token else 6.5  # 认证 30 次/分，未认证 10 次/分
    results = []
    seen = set()
    upper = None  # 星数上界（含）；None 表示无上界

    for rng in range(1, MAX_RANGES + 1):
        if len(results) >= target_count:
            break
        query = "stars:>0" if upper is None else f"stars:1..{upper}"
        print(f"[range {rng}] query='{query}' (collected so far: {len(results)})")

        batch_min = None
        got_any = False
        for page in range(1, MAX_PAGE + 1):
            if len(results) >= target_count:
                break
            data = _search(token, query, page)
            items = data.get("items", [])
            if not items:
                break
            got_any = True
            for it in items:
                rid = str(it["id"])
                if rid in seen:
                    continue
                seen.add(rid)
                results.append(_normalize(it))
                s = it.get("stargazers_count", 0)
                batch_min = s if batch_min is None else min(batch_min, s)
            print(f"  page {page}: +{len(items)} (total {len(results)})")
            if len(items) < PER_PAGE:
                break  # 该区间已取尽
            if page < MAX_PAGE and len(results) < target_count:
                time.sleep(sleep)

        if not got_any or batch_min is None or batch_min <= 1:
            break  # 已无更多结果
        upper = batch_min - 1  # 下移到本批最小星数之下，避免与已取区间重叠

    results.sort(key=lambda r: r["stars"], reverse=True)
    return results[:target_count]


def main():
    # 允许通过命令行参数覆盖日期（用于补跑某天的快照）
    if len(sys.argv) > 1 and len(sys.argv[1]) == 8 and sys.argv[1].isdigit():
        date_str = sys.argv[1]
        print(f"Manual date override: {date_str}")
    else:
        date_str = datetime.now(timezone.utc).strftime("%Y%m%d")

    token = os.getenv("GITHUBTOKEN")
    if token:
        print("Using GitHub token from environment variable: GITHUBTOKEN")
    else:
        print("Warning: GITHUBTOKEN not set. Falling back to unauthenticated search (10 req/min).")

    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"Fetching top {TOP_N} repos by stars (paged by star ranges)...")
    repos = fetch_top_repos(token)
    print(f"Fetched {len(repos)} repos.")

    if not repos:
        print("No repos fetched. Aborting.")
        sys.exit(1)

    filepath = os.path.join(DATA_DIR, f"{SNAPSHOT_PREFIX}{date_str}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)
    size_mb = os.path.getsize(filepath) / 1024 / 1024
    print(f"Saved snapshot to {os.path.abspath(filepath)} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
