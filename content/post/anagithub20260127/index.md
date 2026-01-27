---
title: "GitHub 趋势报告 2026-01-27"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-27T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-27 20:27:03

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
        'daily': {"categories": ["public-apis/public-apis", "clash-verge-rev/clash-verge-rev", "langgenius/dify", "DigitalPlatDev/FreeDomain", "n8n-io/n8n", "firecrawl/firecrawl", "bmad-code-org/BMAD-METHOD", "block/goose", "sindresorhus/awesome", "github/spec-kit", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "Shubhamsaboo/awesome-llm-apps", "anthropics/claude-code", "remotion-dev/remotion", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "affaan-m/everything-claude-code", "moltbot/moltbot"], "data": [214, 217, 235, 235, 235, 245, 257, 262, 282, 289, 292, 353, 425, 455, 984, 1050, 1292, 1455, 1503, 25481]},
        'weekly': {"categories": ["tw93/Mole", "yt-dlp/yt-dlp", "sindresorhus/awesome", "x1xhlol/system-prompts-and-models-of-ai-tools", "Shubhamsaboo/awesome-llm-apps", "github/spec-kit", "microsoft/Data-Science-For-Beginners", "DigitalPlatDev/FreeDomain", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "MHSanaei/3x-ui", "block/goose", "affaan-m/everything-claude-code", "remotion-dev/remotion", "slatedocs/slate", "moltbot/moltbot"], "data": [1524, 1528, 1645, 1654, 1689, 1726, 1738, 1769, 2150, 2484, 2772, 7062, 8919, 9689, 29220, 29354, 32230, 32788, 36168, 68687]},
        'monthly': {"categories": [], "data": []}
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
| 1 | [moltbot/moltbot](https://github.com/moltbot/moltbot) | +25481 | 68687 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1503 | 32230 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +1455 | 55594 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1292 | 89995 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +1050 | 37905 |
| 6 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +984 | 32788 |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +455 | 61398 |
| 8 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +425 | 90062 |
| 9 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +353 | 461247 |
| 10 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +292 | 50762 |
| 11 | [github/spec-kit](https://github.com/github/spec-kit) | +289 | 65588 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +282 | 432493 |
| 13 | [block/goose](https://github.com/block/goose) | +262 | 29354 |
| 14 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +257 | 32302 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +245 | 77762 |
| 16 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +235 | 171625 |
| 17 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +235 | 143858 |
| 18 | [langgenius/dify](https://github.com/langgenius/dify) | +235 | 127570 |
| 19 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +217 | 94489 |
| 20 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +214 | 393799 |
| 21 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +200 | 111404 |
| 22 | [tw93/Mole](https://github.com/tw93/Mole) | +196 | 32097 |
| 23 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +193 | 270346 |
| 24 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +193 | 58744 |
| 25 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +187 | 55430 |
| 26 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +168 | 144415 |
| 27 | [usememos/memos](https://github.com/usememos/memos) | +158 | 55938 |
| 28 | [upstash/context7](https://github.com/upstash/context7) | +158 | 43792 |
| 29 | [hashicorp/vault](https://github.com/hashicorp/vault) | +158 | 34045 |
| 30 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +155 | 280161 |
| 31 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | +151 | 110550 |
| 32 | [openai/codex](https://github.com/openai/codex) | +141 | 57843 |
| 33 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +137 | 203932 |
| 34 | [ollama/ollama](https://github.com/ollama/ollama) | +133 | 160812 |
| 35 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | +131 | 38589 |
| 36 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +130 | 92729 |
| 37 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +129 | 122073 |
| 38 | [immich-app/immich](https://github.com/immich-app/immich) | +122 | 90213 |
| 39 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +121 | 52931 |
| 40 | [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) | +117 | 53742 |
| 41 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +114 | 143804 |
| 42 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +114 | 101653 |
| 43 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +113 | 141369 |
| 44 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +111 | 44780 |
| 45 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +106 | 68757 |
| 46 | [Lissy93/web-check](https://github.com/Lissy93/web-check) | +101 | 31205 |
| 47 | [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | +99 | 37441 |
| 48 | [torvalds/linux](https://github.com/torvalds/linux) | +98 | 215384 |
| 49 | [docling-project/docling](https://github.com/docling-project/docling) | +97 | 51268 |
| 50 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +96 | 333554 |
