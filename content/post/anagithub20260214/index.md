---
title: "GitHub 趋势报告 2026-02-14"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-14T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-14 20:29:51

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
        'daily': {"categories": ["vinta/awesome-python", "awesome-selfhosted/awesome-selfhosted", "public-apis/public-apis", "github/spec-kit", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "sindresorhus/awesome", "firecrawl/firecrawl", "Shubhamsaboo/awesome-llm-apps", "ComposioHQ/awesome-claude-skills", "codecrafters-io/build-your-own-x", "google/langextract", "daytonaio/daytona", "affaan-m/everything-claude-code", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw", "patchy631/ai-engineering-hub"], "data": [134, 141, 147, 183, 184, 187, 204, 242, 243, 243, 249, 268, 281, 305, 417, 481, 500, 561, 2547, 29554]},
        'weekly': {"categories": ["DigitalPlatDev/FreeDomain", "github/spec-kit", "kuchin/awesome-cto", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "firecrawl/firecrawl", "Shubhamsaboo/awesome-llm-apps", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw", "patchy631/ai-engineering-hub", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "google/langextract"], "data": [1163, 1467, 1556, 1581, 1628, 1733, 1976, 2183, 2427, 2442, 2950, 4214, 4542, 4667, 4818, 20466, 29554, 31225, 31424, 32238]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "asgeirtj/system_prompts_leaks", "google/langextract", "anomalyco/opencode", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [8972, 9403, 9951, 28047, 29554, 29991, 30327, 30436, 30964, 31225, 31424, 31464, 32238, 33296, 34805, 36164, 36576, 45936, 51520, 194109]}
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
| 1 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +29554 | 29554 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2547 | 194109 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +561 | 104536 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +500 | 51520 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +481 | 69804 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +417 | 45936 |
| 7 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +305 | 56174 |
| 8 | [google/langextract](https://github.com/google/langextract) | +281 | 32238 |
| 9 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +268 | 465937 |
| 10 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +249 | 34805 |
| 11 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +243 | 94994 |
| 12 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +243 | 82473 |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +242 | 437429 |
| 14 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +204 | 31424 |
| 15 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +187 | 31225 |
| 16 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +184 | 66819 |
| 17 | [github/spec-kit](https://github.com/github/spec-kit) | +183 | 69696 |
| 18 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +147 | 398395 |
| 19 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +141 | 273238 |
| 20 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +134 | 282831 |
| 21 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +131 | 147499 |
| 22 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +130 | 36576 |
| 23 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +122 | 206288 |
| 24 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +122 | 174531 |
| 25 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +117 | 147090 |
| 26 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +113 | 97277 |
| 27 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +96 | 123919 |
| 28 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +96 | 114522 |
| 29 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +94 | 166032 |
| 30 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | +94 | 39469 |
| 31 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +91 | 335344 |
| 32 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +91 | 35604 |
| 33 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +89 | 47280 |
| 34 | [docling-project/docling](https://github.com/docling-project/docling) | +87 | 53031 |
| 35 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +85 | 143002 |
| 36 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +85 | 31464 |
| 37 | [openai/codex](https://github.com/openai/codex) | +84 | 60343 |
| 38 | [cline/cline](https://github.com/cline/cline) | +82 | 57951 |
| 39 | [torvalds/linux](https://github.com/torvalds/linux) | +81 | 217369 |
| 40 | [ollama/ollama](https://github.com/ollama/ollama) | +79 | 162610 |
| 41 | [tw93/Mole](https://github.com/tw93/Mole) | +76 | 34691 |
| 42 | [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | +74 | 53192 |
| 43 | [immich-app/immich](https://github.com/immich-app/immich) | +72 | 92485 |
| 44 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +70 | 165028 |
| 45 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +70 | 94498 |
| 46 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | +70 | 78670 |
| 47 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +70 | 51275 |
| 48 | [mifi/lossless-cut](https://github.com/mifi/lossless-cut) | +70 | 38215 |
| 49 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | +69 | 107489 |
| 50 | [langgenius/dify](https://github.com/langgenius/dify) | +68 | 129605 |
