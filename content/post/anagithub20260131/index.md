---
title: "GitHub 趋势报告 2026-01-31"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-31T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-31 20:28:52

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
        'daily': {"categories": ["vinta/awesome-python", "n8n-io/n8n", "public-apis/public-apis", "x1xhlol/system-prompts-and-models-of-ai-tools", "PaddlePaddle/PaddleOCR", "firecrawl/firecrawl", "lobehub/lobehub", "Shubhamsaboo/awesome-llm-apps", "remotion-dev/remotion", "anthropics/claude-code", "bmad-code-org/BMAD-METHOD", "codecrafters-io/build-your-own-x", "DigitalPlatDev/FreeDomain", "sindresorhus/awesome", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [164, 166, 177, 208, 228, 239, 241, 248, 256, 259, 266, 279, 304, 327, 379, 492, 684, 718, 879, 13711]},
        'weekly': {"categories": ["clash-verge-rev/clash-verge-rev", "immich-app/immich", "x1xhlol/system-prompts-and-models-of-ai-tools", "firecrawl/firecrawl", "bmad-code-org/BMAD-METHOD", "github/spec-kit", "DigitalPlatDev/FreeDomain", "daytonaio/daytona", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "Shubhamsaboo/awesome-llm-apps", "anthropics/claude-code", "remotion-dev/remotion", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "flameshot-org/flameshot", "block/goose", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [1332, 1428, 1472, 1600, 1637, 1726, 1772, 1915, 2166, 2227, 2259, 2473, 4696, 5817, 7559, 7708, 29133, 29614, 36185, 131190]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "flameshot-org/flameshot", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "blakeblackshear/frigate", "chen08209/FlClash", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "affaan-m/everything-claude-code", "ManimCommunity/manim", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [9054, 10528, 12443, 28233, 29133, 29310, 29431, 29614, 29868, 30494, 31522, 32624, 33303, 34077, 36170, 36185, 36558, 41025, 48710, 131190]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +13711 | 131190 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +879 | 36185 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +718 | 93901 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +684 | 59583 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +492 | 41025 |
| 6 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +379 | 52084 |
| 7 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +327 | 433908 |
| 8 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +304 | 144903 |
| 9 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +279 | 462485 |
| 10 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +266 | 33303 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +259 | 62744 |
| 12 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +256 | 34077 |
| 13 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +248 | 91438 |
| 14 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | +241 | 71746 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +239 | 78723 |
| 16 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +228 | 69545 |
| 17 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +208 | 112326 |
| 18 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +177 | 394532 |
| 19 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +166 | 172343 |
| 20 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +164 | 280820 |
| 21 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +155 | 95235 |
| 22 | [casey/just](https://github.com/casey/just) | +155 | 30314 |
| 23 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +150 | 145140 |
| 24 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +148 | 270952 |
| 25 | [github/spec-kit](https://github.com/github/spec-kit) | +147 | 66565 |
| 26 | [immich-app/immich](https://github.com/immich-app/immich) | +137 | 91242 |
| 27 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | +132 | 336561 |
| 28 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | +126 | 74334 |
| 29 | [hashicorp/vault](https://github.com/hashicorp/vault) | +119 | 34908 |
| 30 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +115 | 204429 |
| 31 | [ollama/ollama](https://github.com/ollama/ollama) | +109 | 161267 |
| 32 | [torvalds/linux](https://github.com/torvalds/linux) | +102 | 215898 |
| 33 | [tw93/Mole](https://github.com/tw93/Mole) | +102 | 32624 |
| 34 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +101 | 333979 |
| 35 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +101 | 164398 |
| 36 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +99 | 257251 |
| 37 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | +99 | 128702 |
| 38 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +96 | 141813 |
| 39 | [usememos/memos](https://github.com/usememos/memos) | +92 | 56343 |
| 40 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +88 | 59165 |
| 41 | [docling-project/docling](https://github.com/docling-project/docling) | +88 | 51659 |
| 42 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +86 | 102064 |
| 43 | [upstash/context7](https://github.com/upstash/context7) | +85 | 44294 |
| 44 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +83 | 93157 |
| 45 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +83 | 55821 |
| 46 | [termux/termux-app](https://github.com/termux/termux-app) | +80 | 49494 |
| 47 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | +80 | 39039 |
| 48 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +80 | 36928 |
| 49 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | +76 | 95890 |
| 50 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +75 | 122499 |
