---
title: "GitHub 趋势报告 2026-01-28"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-28T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-28 20:34:54

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
    var dataMap = {
        'daily': {"categories": ["public-apis/public-apis", "daytonaio/daytona", "lobehub/lobehub", "firecrawl/firecrawl", "DigitalPlatDev/FreeDomain", "langgenius/dify", "hashicorp/vault", "github/spec-kit", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "remotion-dev/remotion", "immich-app/immich", "Shubhamsaboo/awesome-llm-apps", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "affaan-m/everything-claude-code", "moltbot/moltbot", "OpenBMB/ChatDev"], "data": [227, 230, 230, 231, 244, 284, 305, 331, 336, 366, 399, 478, 485, 538, 1013, 1186, 1300, 1320, 18357, 29030]},
        'weekly': {"categories": ["browser-use/browser-use", "microsoft/Data-Science-For-Beginners", "firecrawl/firecrawl", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "DigitalPlatDev/FreeDomain", "sindresorhus/awesome", "github/spec-kit", "Shubhamsaboo/awesome-llm-apps", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "MHSanaei/3x-ui", "block/goose", "remotion-dev/remotion", "affaan-m/everything-claude-code", "slatedocs/slate", "moltbot/moltbot"], "data": [1417, 1500, 1523, 1557, 1733, 1739, 1749, 1772, 2085, 2534, 2760, 6755, 9019, 9095, 29276, 29455, 33266, 33550, 36169, 87044]},
        'monthly': {"categories": ["daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "OpenBMB/ChatDev", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "Dokploy/dokploy", "blakeblackshear/frigate", "chen08209/FlClash", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "affaan-m/everything-claude-code", "slatedocs/slate", "ManimCommunity/manim", "obra/superpowers", "anomalyco/opencode", "moltbot/moltbot"], "data": [9893, 12214, 27764, 29030, 29232, 29276, 29455, 29586, 29814, 30217, 31309, 32253, 32507, 33266, 33550, 36169, 36505, 38918, 47430, 87044]}
    };

    function getOption(type) {
        var currentData = dataMap[type];
        var titleText = '';
        if (type === 'daily') titleText = '日增长排行 (Top 20)';
        else if (type === 'weekly') titleText = '周增长排行 (Top 20)';
        else if (type === 'monthly') titleText = '月增长排行 (Top 20)';

        if (!currentData || currentData.categories.length === 0) {
             return {
                title: { text: titleText + ' (暂无数据)' },
                xAxis: { show: false },
                yAxis: { show: false }
             };
        }

        return {
            title: {
                text: titleText,
                left: 'center'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'value',
                boundaryGap: [0, 0.01]
            },
            yAxis: {
                type: 'category',
                data: currentData.categories
            },
            series: [{
                name: 'Stars Growth',
                type: 'bar',
                data: currentData.data,
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                        {offset: 0, color: '#83bff6'},
                        {offset: 0.5, color: '#188df0'},
                        {offset: 1, color: '#188df0'}
                    ])
                },
                label: {
                    show: true,
                    position: 'right'
                }
            }]
        };
    }

    // 初始化显示日榜
    option = getOption('daily');
    myChart.setOption(option);

    function updateChart(type) {
        myChart.setOption(getOption(type));
    }
    
    window.addEventListener('resize', function() {
        myChart.resize();
    });
</script>



### 🚀 今日 Top 50 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +29030 | 29030 |
| 2 | [moltbot/moltbot](https://github.com/moltbot/moltbot) | +18357 | 87044 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1320 | 33550 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +1300 | 56894 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1186 | 91181 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +1013 | 38918 |
| 7 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +538 | 90600 |
| 8 | [immich-app/immich](https://github.com/immich-app/immich) | +485 | 90698 |
| 9 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +478 | 33266 |
| 10 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +399 | 61797 |
| 11 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +366 | 461613 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +336 | 432829 |
| 13 | [github/spec-kit](https://github.com/github/spec-kit) | +331 | 65919 |
| 14 | [hashicorp/vault](https://github.com/hashicorp/vault) | +305 | 34350 |
| 15 | [langgenius/dify](https://github.com/langgenius/dify) | +284 | 127854 |
| 16 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +244 | 144102 |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +231 | 77993 |
| 18 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | +230 | 70840 |
| 19 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +230 | 50992 |
| 20 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +227 | 394026 |
| 21 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +216 | 111620 |
| 22 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +205 | 32507 |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +200 | 171825 |
| 24 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +187 | 94676 |
| 25 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +178 | 280339 |
| 26 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +167 | 144582 |
| 27 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +166 | 270512 |
| 28 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +158 | 53089 |
| 29 | [tw93/Mole](https://github.com/tw93/Mole) | +156 | 32253 |
| 30 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +151 | 141520 |
| 31 | [upstash/context7](https://github.com/upstash/context7) | +149 | 43941 |
| 32 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +147 | 204079 |
| 33 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | +147 | 38736 |
| 34 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | +140 | 381293 |
| 35 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +139 | 256916 |
| 36 | [torvalds/linux](https://github.com/torvalds/linux) | +136 | 215520 |
| 37 | [openai/codex](https://github.com/openai/codex) | +134 | 57977 |
| 38 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +132 | 58876 |
| 39 | [exo-explore/exo](https://github.com/exo-explore/exo) | +129 | 40663 |
| 40 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +127 | 92856 |
| 41 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +126 | 122199 |
| 42 | [ollama/ollama](https://github.com/ollama/ollama) | +125 | 160937 |
| 43 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +124 | 44904 |
| 44 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +121 | 68878 |
| 45 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +121 | 55551 |
| 46 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +113 | 164083 |
| 47 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | +109 | 110659 |
| 48 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +107 | 143911 |
| 49 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +107 | 59568 |
| 50 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +104 | 333658 |
