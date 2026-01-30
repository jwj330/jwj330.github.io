---
title: "GitHub 趋势报告 2026-01-30"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-30T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-30 20:33:29

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
        'daily': {"categories": ["clash-verge-rev/clash-verge-rev", "x1xhlol/system-prompts-and-models-of-ai-tools", "hashicorp/vault", "remotion-dev/remotion", "github/spec-kit", "firecrawl/firecrawl", "DigitalPlatDev/FreeDomain", "PaddlePaddle/PaddleOCR", "anthropics/claude-code", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "Shubhamsaboo/awesome-llm-apps", "lobehub/lobehub", "sindresorhus/awesome", "obra/superpowers", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "openclaw/openclaw", "flameshot-org/flameshot"], "data": [198, 204, 206, 218, 231, 244, 257, 280, 321, 325, 326, 345, 368, 489, 763, 826, 900, 1018, 15227, 29093]},
        'weekly': {"categories": ["clash-verge-rev/clash-verge-rev", "immich-app/immich", "bmad-code-org/BMAD-METHOD", "x1xhlol/system-prompts-and-models-of-ai-tools", "firecrawl/firecrawl", "DigitalPlatDev/FreeDomain", "github/spec-kit", "daytonaio/daytona", "sindresorhus/awesome", "Shubhamsaboo/awesome-llm-apps", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "flameshot-org/flameshot", "block/goose", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [1296, 1364, 1492, 1494, 1538, 1720, 1731, 1924, 2035, 2151, 2272, 2589, 6080, 7838, 8010, 29093, 29575, 33821, 35306, 117479]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "flameshot-org/flameshot", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "blakeblackshear/frigate", "chen08209/FlClash", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "affaan-m/everything-claude-code", "slatedocs/slate", "ManimCommunity/manim", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [8929, 10254, 12380, 28045, 29093, 29274, 29379, 29575, 29856, 30428, 31449, 32522, 33037, 33821, 35306, 36170, 36544, 40533, 48295, 117479]}
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
| 1 | [flameshot-org/flameshot](https://github.com/flameshot-org/flameshot) | +29093 | 29093 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +15227 | 117479 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1018 | 93183 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +900 | 58899 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +826 | 35306 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +763 | 40533 |
| 7 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +489 | 433581 |
| 8 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | +368 | 71505 |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +345 | 91190 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +326 | 462206 |
| 11 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +325 | 51705 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +321 | 62485 |
| 13 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +280 | 69317 |
| 14 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +257 | 144599 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +244 | 78484 |
| 16 | [github/spec-kit](https://github.com/github/spec-kit) | +231 | 66418 |
| 17 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +218 | 33821 |
| 18 | [hashicorp/vault](https://github.com/hashicorp/vault) | +206 | 34789 |
| 19 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +204 | 112118 |
| 20 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +198 | 95080 |
| 21 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +178 | 33037 |
| 22 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +175 | 144990 |
| 23 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +166 | 280656 |
| 24 | [langgenius/dify](https://github.com/langgenius/dify) | +164 | 128182 |
| 25 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +162 | 172177 |
| 26 | [immich-app/immich](https://github.com/immich-app/immich) | +159 | 91105 |
| 27 | [tw93/Mole](https://github.com/tw93/Mole) | +153 | 32522 |
| 28 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +149 | 270804 |
| 29 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +144 | 394355 |
| 30 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +144 | 204314 |
| 31 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +133 | 36848 |
| 32 | [torvalds/linux](https://github.com/torvalds/linux) | +128 | 215796 |
| 33 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +123 | 257152 |
| 34 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +123 | 164297 |
| 35 | [upstash/context7](https://github.com/upstash/context7) | +123 | 44209 |
| 36 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +117 | 53342 |
| 37 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +115 | 333878 |
| 38 | [makeplane/plane](https://github.com/makeplane/plane) | +114 | 45143 |
| 39 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +112 | 93074 |
| 40 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +110 | 101978 |
| 41 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +110 | 45101 |
| 42 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +106 | 122424 |
| 43 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +106 | 69073 |
| 44 | [ollama/ollama](https://github.com/ollama/ollama) | +103 | 161158 |
| 45 | [f/prompts.chat](https://github.com/f/prompts.chat) | +103 | 144088 |
| 46 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +99 | 141717 |
| 47 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | +99 | 95814 |
| 48 | [docling-project/docling](https://github.com/docling-project/docling) | +99 | 51571 |
| 49 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) | +99 | 38959 |
| 50 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +98 | 59077 |
