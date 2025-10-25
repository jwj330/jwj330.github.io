import os
from datetime import datetime

def main():
    # 获取当前时间
    current_time = datetime.now()

    # 格式化日期字符串（用于date字段）
    formatted_date = current_time.strftime('%Y-%m-%d %H:%M:%S+0000')

    # 格式化日期字符串（用于title字段）
    title_date = current_time.strftime('%Y%m%d')
    
    # 构建目标目录路径
    post_dir = os.path.join("content", "post", f"post_{current_time}")
    
    # 创建目录（如果不存在）
    os.makedirs(post_dir, exist_ok=True)
    
    # 创建并写入index.md文件
    index_path = os.path.join(post_dir, "index.md")
    with open(index_path, "w") as f:
        f.write(f"""---
title: report{title_date}ai
description: 今日趋势
slug: report
date: {formatted_date}
categories:
    - 每日Github趋势
tags:
    - hugo
    - Java
weight: 1       # You can add weight to some posts to override the default sorting (date descending)
---
# 今日趋势
""")

if __name__ == "__main__":
    main()
