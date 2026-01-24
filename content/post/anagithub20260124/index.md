---
title: "GitHub 趋势报告 2026-01-24"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-24T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-24 20:24:52

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
        'daily': {"categories": ["public-apis/public-apis", "github/spec-kit", "yt-dlp/yt-dlp", "upstash/context7", "awesome-selfhosted/awesome-selfhosted", "firecrawl/firecrawl", "Asabeneh/30-Days-Of-Python", "openai/codex", "sindresorhus/awesome", "microsoft/Data-Science-For-Beginners", "x1xhlol/system-prompts-and-models-of-ai-tools", "DigitalPlatDev/FreeDomain", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "browser-use/browser-use", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "remotion-dev/remotion"], "data": [149, 152, 153, 156, 166, 177, 180, 184, 196, 228, 230, 252, 324, 375, 383, 388, 755, 986, 997, 29381]},
        'weekly': {"categories": ["n8n-io/n8n", "sindresorhus/awesome", "firecrawl/firecrawl", "github/spec-kit", "twitter/the-algorithm", "tw93/Mole", "microsoft/Data-Science-For-Beginners", "yt-dlp/yt-dlp", "public-apis/public-apis", "DigitalPlatDev/FreeDomain", "x1xhlol/system-prompts-and-models-of-ai-tools", "codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "anomalyco/opencode", "MHSanaei/3x-ui", "remotion-dev/remotion", "obra/superpowers", "slatedocs/slate"], "data": [1421, 1567, 1607, 1645, 1647, 1658, 1727, 1729, 1785, 1845, 1984, 2635, 2664, 2718, 8099, 11442, 29051, 29381, 35208, 36167]},
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
| 1 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +29381 | 29381 |
| 2 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +997 | 86342 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +986 | 51875 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +755 | 35208 |
| 5 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +388 | 50169 |
| 6 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +383 | 76712 |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +375 | 60271 |
| 8 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +324 | 460258 |
| 9 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +252 | 143131 |
| 10 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +230 | 110854 |
| 11 | [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | +228 | 33532 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +196 | 431742 |
| 13 | [openai/codex](https://github.com/openai/codex) | +184 | 57151 |
| 14 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +180 | 56485 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +177 | 77123 |
| 16 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +166 | 269841 |
| 17 | [upstash/context7](https://github.com/upstash/context7) | +156 | 43335 |
| 18 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +153 | 143893 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +152 | 64839 |
| 20 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +149 | 393238 |
| 21 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +145 | 171031 |
| 22 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +140 | 89179 |
| 23 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +139 | 279726 |
| 24 | [tw93/Mole](https://github.com/tw93/Mole) | +134 | 31504 |
| 25 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +123 | 203559 |
| 26 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +121 | 31666 |
| 27 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +119 | 93903 |
| 28 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +115 | 333226 |
| 29 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +111 | 121758 |
| 30 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +110 | 68458 |
| 31 | [ollama/ollama](https://github.com/ollama/ollama) | +108 | 160454 |
| 32 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +106 | 115265 |
| 33 | [usememos/memos](https://github.com/usememos/memos) | +105 | 55500 |
| 34 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +104 | 163645 |
| 35 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +103 | 143448 |
| 36 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +101 | 31770 |
| 37 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +100 | 57977 |
| 38 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +98 | 54661 |
| 39 | [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | +98 | 41047 |
| 40 | [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | +98 | 36981 |
| 41 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +97 | 92368 |
| 42 | [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | +92 | 72067 |
| 43 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +89 | 141029 |
| 44 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +89 | 101307 |
| 45 | [Lissy93/web-check](https://github.com/Lissy93/web-check) | +87 | 30874 |
| 46 | [langgenius/dify](https://github.com/langgenius/dify) | +84 | 127092 |
| 47 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +83 | 163346 |
| 48 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +83 | 42021 |
| 49 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | +81 | 95328 |
| 50 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +78 | 85699 |
