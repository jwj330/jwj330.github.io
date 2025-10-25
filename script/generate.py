import os
import datetime

def main():
    # 获取当前时间并格式化
    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 构建目标目录路径
    post_dir = os.path.join("content", "post", f"post_{current_time}")
    
    # 创建目录（如果不存在）
    os.makedirs(post_dir, exist_ok=True)
    
    # 创建并写入index.md文件
    index_path = os.path.join(post_dir, "index.md")
    with open(index_path, "w") as f:
        f.write("hello")

if __name__ == "__main__":
    main()
