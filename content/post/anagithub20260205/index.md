---
title: "GitHub 趋势报告 2026-02-05"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-05T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-05 20:36:59

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
        'daily': {"categories": ["x1xhlol/system-prompts-and-models-of-ai-tools", "public-apis/public-apis", "n8n-io/n8n", "remotion-dev/remotion", "asgeirtj/system_prompts_leaks", "bmad-code-org/BMAD-METHOD", "firecrawl/firecrawl", "github/spec-kit", "sindresorhus/awesome", "microsoft/qlib", "codecrafters-io/build-your-own-x", "OpenBMB/ChatDev", "anthropics/claude-code", "daytonaio/daytona", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "openclaw/openclaw"], "data": [169, 169, 172, 182, 190, 216, 225, 260, 292, 294, 318, 365, 380, 403, 538, 843, 882, 893, 898, 4573]},
        'weekly': {"categories": ["karpathy/nanochat", "Shubhamsaboo/awesome-llm-apps", "bmad-code-org/BMAD-METHOD", "x1xhlol/system-prompts-and-models-of-ai-tools", "remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "firecrawl/firecrawl", "github/spec-kit", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "TauricResearch/TradingAgents", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "openclaw/openclaw"], "data": [1306, 1416, 1497, 1497, 1531, 1587, 1624, 1638, 1801, 2037, 2204, 2239, 5473, 5908, 6030, 6182, 29334, 30265, 30709, 65024]},
        'monthly': {"categories": ["anthropics/claude-code", "TauricResearch/TradingAgents", "anthropics/skills", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "blakeblackshear/frigate", "block/goose", "asgeirtj/system_prompts_leaks", "OpenBMB/ChatDev", "ComposioHQ/awesome-claude-skills", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [12291, 29334, 29493, 29643, 29779, 29960, 29975, 30265, 30307, 30709, 31891, 33468, 34356, 35134, 36171, 36645, 40510, 45243, 46964, 167276]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4573 | 167276 |
| 2 | [anthropics/skills](https://github.com/anthropics/skills) | +898 | 63907 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +893 | 98347 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +882 | 45243 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +843 | 40510 |
| 6 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +538 | 30709 |
| 7 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +403 | 53181 |
| 8 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +380 | 64403 |
| 9 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +365 | 30307 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +318 | 463917 |
| 11 | [microsoft/qlib](https://github.com/microsoft/qlib) | +294 | 36794 |
| 12 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +292 | 435296 |
| 13 | [github/spec-kit](https://github.com/github/spec-kit) | +260 | 67825 |
| 14 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +225 | 79864 |
| 15 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +216 | 34356 |
| 16 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +190 | 30265 |
| 17 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +182 | 35134 |
| 18 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +172 | 173189 |
| 19 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +169 | 395392 |
| 20 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +169 | 113411 |
| 21 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +166 | 96071 |
| 22 | [openai/codex](https://github.com/openai/codex) | +164 | 59091 |
| 23 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +157 | 271788 |
| 24 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +157 | 205211 |
| 25 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +151 | 281581 |
| 26 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | +147 | 58376 |
| 27 | [tw93/Mole](https://github.com/tw93/Mole) | +147 | 33468 |
| 28 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +144 | 92261 |
| 29 | [ollama/ollama](https://github.com/ollama/ollama) | +143 | 161843 |
| 30 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +143 | 145935 |
| 31 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | +123 | 91355 |
| 32 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +119 | 123033 |
| 33 | [upstash/context7](https://github.com/upstash/context7) | +119 | 44836 |
| 34 | [astral-sh/uv](https://github.com/astral-sh/uv) | +117 | 78656 |
| 35 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +116 | 165025 |
| 36 | [langgenius/dify](https://github.com/langgenius/dify) | +116 | 128809 |
| 37 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +115 | 93689 |
| 38 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +112 | 69587 |
| 39 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +103 | 334508 |
| 40 | [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | +103 | 74645 |
| 41 | [docling-project/docling](https://github.com/docling-project/docling) | +101 | 52210 |
| 42 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +100 | 145929 |
| 43 | [torvalds/linux](https://github.com/torvalds/linux) | +98 | 216382 |
| 44 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +95 | 35298 |
| 45 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | +94 | 126034 |
| 46 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +89 | 102546 |
| 47 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +89 | 70258 |
| 48 | [immich-app/immich](https://github.com/immich-app/immich) | +87 | 91754 |
| 49 | [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | +87 | 32349 |
| 50 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | +86 | 382164 |
