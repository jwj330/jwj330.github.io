---
title: "GitHub 趋势报告 2026-01-29"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-29T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-29 20:34:06

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
        'daily': {"categories": ["hashicorp/vault", "yt-dlp/yt-dlp", "DigitalPlatDev/FreeDomain", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "immich-app/immich", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "github/spec-kit", "x1xhlol/system-prompts-and-models-of-ai-tools", "lobehub/lobehub", "remotion-dev/remotion", "bmad-code-org/BMAD-METHOD", "anthropics/claude-code", "daytonaio/daytona", "obra/superpowers", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "moltbot/moltbot"], "data": [233, 233, 240, 245, 247, 248, 263, 267, 268, 294, 297, 337, 352, 367, 388, 852, 930, 984, 1105, 15208]},
        'weekly': {"categories": ["yt-dlp/yt-dlp", "n8n-io/n8n", "bmad-code-org/BMAD-METHOD", "firecrawl/firecrawl", "x1xhlol/system-prompts-and-models-of-ai-tools", "DigitalPlatDev/FreeDomain", "github/spec-kit", "sindresorhus/awesome", "daytonaio/daytona", "Shubhamsaboo/awesome-llm-apps", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "OpenBMB/ChatDev", "block/goose", "remotion-dev/remotion", "affaan-m/everything-claude-code", "moltbot/moltbot"], "data": [1337, 1349, 1504, 1518, 1565, 1704, 1764, 1786, 1930, 2049, 2472, 2743, 6461, 8423, 8625, 29039, 29536, 33603, 34480, 102252]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "OpenBMB/ChatDev", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "blakeblackshear/frigate", "chen08209/FlClash", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "affaan-m/everything-claude-code", "slatedocs/slate", "ManimCommunity/manim", "obra/superpowers", "anomalyco/opencode", "moltbot/moltbot"], "data": [8799, 10034, 12309, 27910, 29039, 29253, 29334, 29536, 29838, 30348, 31386, 32369, 32859, 33603, 34480, 36170, 36522, 39770, 47826, 102252]}
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
| 1 | [moltbot/moltbot](https://github.com/moltbot/moltbot) | +15208 | 102252 |
| 2 | [anthropics/skills](https://github.com/anthropics/skills) | +1105 | 57999 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +984 | 92165 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +930 | 34480 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +852 | 39770 |
| 6 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +388 | 51380 |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +367 | 62164 |
| 8 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +352 | 32859 |
| 9 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +337 | 33603 |
| 10 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | +297 | 71137 |
| 11 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +294 | 111914 |
| 12 | [github/spec-kit](https://github.com/github/spec-kit) | +268 | 66187 |
| 13 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +267 | 461880 |
| 14 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +263 | 433092 |
| 15 | [immich-app/immich](https://github.com/immich-app/immich) | +248 | 90946 |
| 16 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +247 | 78240 |
| 17 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +245 | 90845 |
| 18 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +240 | 144342 |
| 19 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +233 | 144815 |
| 20 | [hashicorp/vault](https://github.com/hashicorp/vault) | +233 | 34583 |
| 21 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +206 | 94882 |
| 22 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +190 | 172015 |
| 23 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +185 | 394211 |
| 24 | [langgenius/dify](https://github.com/langgenius/dify) | +164 | 128018 |
| 25 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +151 | 280490 |
| 26 | [torvalds/linux](https://github.com/torvalds/linux) | +148 | 215668 |
| 27 | [upstash/context7](https://github.com/upstash/context7) | +145 | 44086 |
| 28 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +143 | 270655 |
| 29 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +136 | 53225 |
| 30 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +131 | 30348 |
| 31 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | +124 | 38860 |
| 32 | [usememos/memos](https://github.com/usememos/memos) | +121 | 56163 |
| 33 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +119 | 122318 |
| 34 | [ollama/ollama](https://github.com/ollama/ollama) | +118 | 161055 |
| 35 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +118 | 101868 |
| 36 | [openai/codex](https://github.com/openai/codex) | +116 | 58093 |
| 37 | [tw93/Mole](https://github.com/tw93/Mole) | +116 | 32369 |
| 38 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +113 | 257029 |
| 39 | [exo-explore/exo](https://github.com/exo-explore/exo) | +111 | 40774 |
| 40 | [docling-project/docling](https://github.com/docling-project/docling) | +107 | 51472 |
| 41 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +106 | 92962 |
| 42 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +105 | 333763 |
| 43 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +104 | 55655 |
| 44 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +103 | 58979 |
| 45 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +98 | 141618 |
| 46 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +96 | 69037 |
| 47 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +91 | 204170 |
| 48 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +91 | 164174 |
| 49 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +89 | 68967 |
| 50 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +88 | 115635 |
