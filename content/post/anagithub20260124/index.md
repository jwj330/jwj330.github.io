---
title: "GitHub 趋势报告 2026-01-24"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-24T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-24 19:03:51

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
        'daily': {"categories": ["public-apis/public-apis", "github/spec-kit", "yt-dlp/yt-dlp", "upstash/context7", "awesome-selfhosted/awesome-selfhosted", "firecrawl/firecrawl", "Asabeneh/30-Days-Of-Python", "openai/codex", "sindresorhus/awesome", "x1xhlol/system-prompts-and-models-of-ai-tools", "microsoft/Data-Science-For-Beginners", "DigitalPlatDev/FreeDomain", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "browser-use/browser-use", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "remotion-dev/remotion"], "data": [141, 142, 148, 149, 157, 162, 175, 180, 185, 223, 226, 244, 314, 350, 357, 380, 727, 951, 965, 29345]},
        'weekly': {"categories": ["n8n-io/n8n", "sindresorhus/awesome", "firecrawl/firecrawl", "github/spec-kit", "twitter/the-algorithm", "tw93/Mole", "yt-dlp/yt-dlp", "microsoft/Data-Science-For-Beginners", "public-apis/public-apis", "DigitalPlatDev/FreeDomain", "x1xhlol/system-prompts-and-models-of-ai-tools", "codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "anomalyco/opencode", "MHSanaei/3x-ui", "remotion-dev/remotion", "obra/superpowers", "slatedocs/slate"], "data": [1410, 1556, 1592, 1635, 1642, 1650, 1724, 1725, 1777, 1837, 1977, 2625, 2656, 2693, 8064, 11410, 29050, 29345, 35180, 36167]},
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
| 1 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +29345 | 29345 |
| 2 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +965 | 86310 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +951 | 51840 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +727 | 35180 |
| 5 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +380 | 50161 |
| 6 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +357 | 76686 |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +350 | 60246 |
| 8 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +314 | 460248 |
| 9 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +244 | 143123 |
| 10 | [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | +226 | 33530 |
| 11 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +223 | 110847 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +185 | 431731 |
| 13 | [openai/codex](https://github.com/openai/codex) | +180 | 57147 |
| 14 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +175 | 56480 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +162 | 77108 |
| 16 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +157 | 269832 |
| 17 | [upstash/context7](https://github.com/upstash/context7) | +149 | 43328 |
| 18 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +148 | 143888 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +142 | 64829 |
| 20 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +141 | 393230 |
| 21 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +134 | 279721 |
| 22 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +134 | 171020 |
| 23 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +133 | 89172 |
| 24 | [tw93/Mole](https://github.com/tw93/Mole) | +126 | 31496 |
| 25 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +118 | 93902 |
| 26 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +118 | 31663 |
| 27 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +115 | 203551 |
| 28 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +107 | 333218 |
| 29 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +104 | 115263 |
| 30 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +102 | 143447 |
| 31 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +102 | 68450 |
| 32 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +100 | 121747 |
| 33 | [usememos/memos](https://github.com/usememos/memos) | +100 | 55495 |
| 34 | [ollama/ollama](https://github.com/ollama/ollama) | +99 | 160445 |
| 35 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +99 | 31768 |
| 36 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +97 | 57974 |
| 37 | [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | +97 | 36980 |
| 38 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +96 | 92367 |
| 39 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +95 | 163636 |
| 40 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +93 | 54656 |
| 41 | [fastapi/full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) | +93 | 41042 |
| 42 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +89 | 141029 |
| 43 | [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | +87 | 72062 |
| 44 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +86 | 101304 |
| 45 | [langgenius/dify](https://github.com/langgenius/dify) | +81 | 127089 |
| 46 | [Lissy93/web-check](https://github.com/Lissy93/web-check) | +81 | 30868 |
| 47 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +80 | 163343 |
| 48 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +79 | 42017 |
| 49 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | +75 | 95322 |
| 50 | [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | +75 | 33384 |
