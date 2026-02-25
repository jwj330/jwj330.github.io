# GitHub 趋势分析自动报告系统

[![Hugo](https://img.shields.io/badge/Hugo-0.121.2-blue.svg)](https://gohugo.io/)
[![Theme](https://img.shields.io/badge/Theme-Stack-green.svg)](https://github.com/CaiJimmy/hugo-theme-stack)

本项目是一个基于 [Hugo](https://gohugo.io/) 构建的 **GitHub 趋势分析自动报告系统**，旨在自动生成的 GitHub 数据分析报告并进行在线展示。

## 项目概览

该博客自动化生成并展示 **GitHub Top500 增长榜**，帮助开发者发现全球最热门和增长最快的开源项目。

- **网站标题**: jwj330
- **主要内容**: GitHub 趋势分析、技术笔记
- **默认语言**: 简体中文 (zh-cn)
- **站点格言**: "朝闻道 夕可眠矣"

##  技术架构

- **静态网站生成器**: [Hugo](https://gohugo.io/)
- **主题**: [Hugo Theme Stack](https://github.com/CaiJimmy/hugo-theme-stack) - 一个设计简洁、功能强大的卡片式主题。
- **内容格式**: Markdown
- **自动化**: 包含自动化抓取和生成日报/周报的脚本。

## 📂 目录结构

```text
.
├── config/_default       # 项目配置文件 (参数、菜单、语言等)
├── content               # 博客文章内容 (Markdown 文件)
│   ├── post              # 主要博文，包含大量的 GitHub 增长榜分析
│   └── page              # 静态页面 (关于、档案等)
├── script                # 数据抓取与处理脚本
├── scriptData            # 脚本运行产生的中间数据
├── static                # 静态资源 (图片、图标等)
└── public                # 编译生成的静态网页 (部署用)
```

##  本地运行

在本地运行或预览该博客，您需要安装 [Hugo](https://gohugo.io/installation/)。

1. **克隆仓库**:
   ```bash
   git clone https://github.com/jwj330/jwj330.github.io.git
   cd jwj330.github.io
1: 
2. **启动预览服务器**:
   ```bash
   hugo server
   ```
3. **访问预览**: 默认在浏览器打开 `http://localhost:1313`。


