---
title: "GitHub 趋势报告 2026-02-11"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-11T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-11 20:41:38

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
        'daily': {"categories": ["codecrafters-io/build-your-own-x", "asgeirtj/system_prompts_leaks", "github/spec-kit", "public-apis/public-apis", "daytonaio/daytona", "sindresorhus/awesome", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "drawdb-io/drawdb", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "kuchin/awesome-cto", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "openclaw/openclaw", "google/langextract"], "data": [211, 213, 226, 228, 238, 241, 286, 319, 330, 365, 378, 415, 439, 443, 630, 655, 776, 825, 3060, 30283]},
        'weekly': {"categories": ["awesome-selfhosted/awesome-selfhosted", "DigitalPlatDev/FreeDomain", "remotion-dev/remotion", "github/spec-kit", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "anthropics/claude-code", "daytonaio/daytona", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "google/langextract", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill"], "data": [1150, 1204, 1240, 1489, 1646, 1762, 1856, 1965, 2130, 2375, 2663, 3783, 4520, 5102, 5113, 5454, 22776, 30283, 30589, 30604]},
        'monthly': {"categories": ["anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "google/langextract", "block/goose", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "slatedocs/slate", "remotion-dev/remotion", "ManimCommunity/manim", "anomalyco/opencode", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [10462, 29679, 29804, 29940, 30170, 30283, 30309, 30589, 30604, 30871, 31115, 33954, 34461, 36168, 36192, 36732, 38043, 44187, 49815, 185479]}
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
| 1 | [google/langextract](https://github.com/google/langextract) | +30283 | 30283 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3060 | 185479 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +825 | 68111 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +776 | 102567 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +655 | 49815 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +630 | 44187 |
| 7 | [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) | +443 | 32997 |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +439 | 81604 |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +415 | 93973 |
| 10 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +378 | 33954 |
| 11 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +365 | 30589 |
| 12 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +330 | 36558 |
| 13 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +319 | 30604 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +286 | 66153 |
| 15 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +241 | 436766 |
| 16 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +238 | 55153 |
| 17 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +228 | 397886 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +226 | 69054 |
| 19 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +213 | 31115 |
| 20 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +211 | 465245 |
| 21 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | +191 | 59900 |
| 22 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +178 | 36192 |
| 23 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +174 | 86838 |
| 24 | [torvalds/linux](https://github.com/torvalds/linux) | +171 | 217058 |
| 25 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +161 | 147033 |
| 26 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +159 | 272781 |
| 27 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +154 | 96918 |
| 28 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +149 | 174113 |
| 29 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +149 | 35267 |
| 30 | [openai/codex](https://github.com/openai/codex) | +147 | 59995 |
| 31 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | +141 | 129350 |
| 32 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +139 | 114215 |
| 33 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +138 | 282414 |
| 34 | [tw93/Mole](https://github.com/tw93/Mole) | +128 | 34461 |
| 35 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +123 | 146740 |
| 36 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +123 | 30871 |
| 37 | [upstash/context7](https://github.com/upstash/context7) | +120 | 45454 |
| 38 | [juanfont/headscale](https://github.com/juanfont/headscale) | +117 | 35204 |
| 39 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +115 | 205965 |
| 40 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +115 | 116540 |
| 41 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +111 | 47158 |
| 42 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +106 | 39357 |
| 43 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +103 | 335075 |
| 44 | [langgenius/dify](https://github.com/langgenius/dify) | +102 | 129423 |
| 45 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +102 | 46132 |
| 46 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +101 | 165641 |
| 47 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +101 | 94266 |
| 48 | [immich-app/immich](https://github.com/immich-app/immich) | +100 | 92269 |
| 49 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +98 | 35793 |
| 50 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +96 | 29804 |
