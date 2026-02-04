---
title: "GitHub 趋势报告 2026-02-04"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-04T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-04 20:37:58

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
        'daily': {"categories": ["clash-verge-rev/clash-verge-rev", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "remotion-dev/remotion", "trimstray/the-book-of-secret-knowledge", "DigitalPlatDev/FreeDomain", "firecrawl/firecrawl", "x1xhlol/system-prompts-and-models-of-ai-tools", "github/spec-kit", "karpathy/nanochat", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "obra/superpowers", "openclaw/openclaw", "TauricResearch/TradingAgents"], "data": [178, 195, 204, 206, 208, 229, 236, 241, 251, 263, 269, 278, 336, 450, 766, 857, 950, 957, 5568, 29271]},
        'weekly': {"categories": ["karpathy/nanochat", "Shubhamsaboo/awesome-llm-apps", "x1xhlol/system-prompts-and-models-of-ai-tools", "bmad-code-org/BMAD-METHOD", "github/spec-kit", "firecrawl/firecrawl", "remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "TauricResearch/TradingAgents", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "openclaw/openclaw"], "data": [1264, 1517, 1622, 1633, 1646, 1646, 1686, 1727, 1786, 1986, 2175, 2226, 5443, 6115, 6117, 6273, 29271, 30075, 30171, 75659]},
        'monthly': {"categories": ["anthropics/claude-code", "TauricResearch/TradingAgents", "anthropics/skills", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "blakeblackshear/frigate", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [12472, 29271, 29334, 29584, 29717, 29903, 29941, 29942, 30075, 30171, 31861, 33321, 34140, 34952, 36171, 36624, 39667, 44361, 47979, 162703]}
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
| 1 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +29271 | 29271 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5568 | 162703 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +957 | 44361 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +950 | 63009 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +857 | 97454 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +766 | 39667 |
| 7 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +450 | 30171 |
| 8 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +336 | 64023 |
| 9 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +278 | 463599 |
| 10 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +269 | 435004 |
| 11 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +263 | 42247 |
| 12 | [github/spec-kit](https://github.com/github/spec-kit) | +251 | 67565 |
| 13 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +241 | 113242 |
| 14 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +236 | 79639 |
| 15 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +229 | 145829 |
| 16 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +208 | 205054 |
| 17 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +206 | 34952 |
| 18 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +204 | 30075 |
| 19 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +195 | 29942 |
| 20 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +178 | 95905 |
| 21 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +178 | 92117 |
| 22 | [openai/codex](https://github.com/openai/codex) | +178 | 58927 |
| 23 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +177 | 34140 |
| 24 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +174 | 164909 |
| 25 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +172 | 271631 |
| 26 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +171 | 173017 |
| 27 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +166 | 281430 |
| 28 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +165 | 145792 |
| 29 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +163 | 395223 |
| 30 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +158 | 52778 |
| 31 | [ollama/ollama](https://github.com/ollama/ollama) | +142 | 161700 |
| 32 | [tw93/Mole](https://github.com/tw93/Mole) | +131 | 33321 |
| 33 | [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) | +131 | 32492 |
| 34 | [langgenius/dify](https://github.com/langgenius/dify) | +122 | 128693 |
| 35 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +122 | 93574 |
| 36 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +120 | 122914 |
| 37 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +119 | 102457 |
| 38 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | +117 | 125940 |
| 39 | [upstash/context7](https://github.com/upstash/context7) | +112 | 44717 |
| 40 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +109 | 334405 |
| 41 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +109 | 29584 |
| 42 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +105 | 70169 |
| 43 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +102 | 38737 |
| 44 | [docling-project/docling](https://github.com/docling-project/docling) | +101 | 52109 |
| 45 | [immich-app/immich](https://github.com/immich-app/immich) | +100 | 91667 |
| 46 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +98 | 42921 |
| 47 | [f/prompts.chat](https://github.com/f/prompts.chat) | +96 | 144542 |
| 48 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | +92 | 84549 |
| 49 | [astral-sh/uv](https://github.com/astral-sh/uv) | +90 | 78539 |
| 50 | [torvalds/linux](https://github.com/torvalds/linux) | +89 | 216284 |
