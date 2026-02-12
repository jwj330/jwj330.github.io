---
title: "GitHub 趋势报告 2026-02-12"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-12T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-12 20:38:15

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
        'daily': {"categories": ["awesome-selfhosted/awesome-selfhosted", "public-apis/public-apis", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "nextlevelbuilder/ui-ux-pro-max-skill", "microsoft/PowerToys", "anthropics/claude-code", "github/spec-kit", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "ComposioHQ/awesome-claude-skills", "code-yeongyu/oh-my-opencode", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "affaan-m/everything-claude-code", "kuchin/awesome-cto", "google/langextract", "openclaw/openclaw"], "data": [188, 195, 207, 217, 223, 264, 275, 284, 327, 342, 353, 357, 412, 646, 650, 767, 804, 866, 960, 3156]},
        'weekly': {"categories": ["remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "kuchin/awesome-cto", "github/spec-kit", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "daytonaio/daytona", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "google/langextract"], "data": [1204, 1288, 1361, 1513, 1535, 1687, 2025, 2039, 2082, 2384, 2689, 3598, 4481, 4854, 4987, 5218, 21359, 30827, 30946, 31243]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "nextlevelbuilder/ui-ux-pro-max-skill", "OpenBMB/ChatDev", "code-yeongyu/oh-my-opencode", "google/langextract", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "slatedocs/slate", "remotion-dev/remotion", "anomalyco/opencode", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [9236, 9606, 10329, 29334, 29903, 30235, 30378, 30827, 30917, 30946, 31243, 31258, 34307, 34549, 36168, 36338, 36459, 44991, 50461, 188635]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3156 | 188635 |
| 2 | [google/langextract](https://github.com/google/langextract) | +960 | 31243 |
| 3 | [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) | +866 | 33863 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +804 | 44991 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +767 | 103334 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +650 | 68761 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +646 | 50461 |
| 8 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +412 | 55565 |
| 9 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +357 | 30946 |
| 10 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +353 | 34307 |
| 11 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +342 | 81946 |
| 12 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +327 | 94300 |
| 13 | [github/spec-kit](https://github.com/github/spec-kit) | +284 | 69338 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +275 | 66428 |
| 15 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | +264 | 129614 |
| 16 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +223 | 30827 |
| 17 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +217 | 436983 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +207 | 465452 |
| 19 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +195 | 398081 |
| 20 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +188 | 272969 |
| 21 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +184 | 147217 |
| 22 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +166 | 43076 |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +164 | 174277 |
| 24 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +151 | 282565 |
| 25 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +146 | 36338 |
| 26 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +144 | 97062 |
| 27 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +143 | 31258 |
| 28 | [openai/codex](https://github.com/openai/codex) | +139 | 60134 |
| 29 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +134 | 35401 |
| 30 | [upstash/context7](https://github.com/upstash/context7) | +127 | 45581 |
| 31 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +125 | 86963 |
| 32 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +125 | 57807 |
| 33 | [torvalds/linux](https://github.com/torvalds/linux) | +123 | 217181 |
| 34 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +120 | 114335 |
| 35 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +119 | 146859 |
| 36 | [docling-project/docling](https://github.com/docling-project/docling) | +116 | 52860 |
| 37 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +115 | 123717 |
| 38 | [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | +115 | 53026 |
| 39 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +114 | 206079 |
| 40 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +112 | 335187 |
| 41 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +105 | 165746 |
| 42 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | +105 | 60005 |
| 43 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +103 | 52002 |
| 44 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +100 | 46232 |
| 45 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +99 | 29903 |
| 46 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +93 | 47251 |
| 47 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +90 | 116630 |
| 48 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +88 | 35881 |
| 49 | [tw93/Mole](https://github.com/tw93/Mole) | +88 | 34549 |
| 50 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +87 | 94353 |
