---
title: "GitHub 趋势报告 2026-02-15"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-15T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-15 20:30:16

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
        'daily': {"categories": ["github/spec-kit", "awesome-selfhosted/awesome-selfhosted", "DigitalPlatDev/FreeDomain", "yt-dlp/yt-dlp", "code-yeongyu/oh-my-opencode", "anthropics/claude-code", "sindresorhus/awesome", "ComposioHQ/awesome-claude-skills", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "Shubhamsaboo/awesome-llm-apps", "google/langextract", "nextlevelbuilder/ui-ux-pro-max-skill", "firecrawl/firecrawl", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "affaan-m/everything-claude-code", "ashishps1/awesome-system-design-resources", "openclaw/openclaw"], "data": [148, 157, 164, 167, 168, 178, 221, 232, 234, 245, 254, 255, 268, 274, 413, 510, 533, 540, 1302, 2500]},
        'weekly': {"categories": ["kuchin/awesome-cto", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "ashishps1/awesome-system-design-resources", "nextlevelbuilder/ui-ux-pro-max-skill", "public-apis/public-apis", "daytonaio/daytona", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "Shubhamsaboo/awesome-llm-apps", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw", "nginx/nginx", "patchy631/ai-engineering-hub", "google/langextract"], "data": [1568, 1573, 1586, 1665, 1754, 1895, 2006, 2011, 2075, 2221, 2405, 2430, 4127, 4434, 4439, 4742, 20466, 29349, 29658, 32493]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "nextlevelbuilder/ui-ux-pro-max-skill", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "anomalyco/opencode", "google/langextract", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [8937, 9374, 9750, 27235, 29658, 30033, 30380, 30480, 30984, 31493, 31572, 31592, 31730, 32493, 35037, 36163, 36692, 46476, 52053, 196609]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2500 | 196609 |
| 2 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1302 | 31504 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +540 | 46476 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +533 | 52053 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +510 | 105046 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +413 | 70217 |
| 7 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +274 | 82747 |
| 8 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +268 | 31493 |
| 9 | [google/langextract](https://github.com/google/langextract) | +255 | 32493 |
| 10 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +254 | 95248 |
| 11 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +245 | 466182 |
| 12 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +234 | 56408 |
| 13 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +232 | 35037 |
| 14 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +221 | 437650 |
| 15 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +178 | 66997 |
| 16 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +168 | 31592 |
| 17 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +167 | 147257 |
| 18 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +164 | 147663 |
| 19 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +157 | 273395 |
| 20 | [github/spec-kit](https://github.com/github/spec-kit) | +148 | 69844 |
| 21 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +145 | 282976 |
| 22 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +134 | 97411 |
| 23 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +133 | 398528 |
| 24 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +133 | 174664 |
| 25 | [tw93/Mole](https://github.com/tw93/Mole) | +125 | 34816 |
| 26 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +117 | 206405 |
| 27 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +116 | 36692 |
| 28 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +108 | 31572 |
| 29 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +105 | 43378 |
| 30 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +104 | 29658 |
| 31 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +98 | 114620 |
| 32 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +94 | 335438 |
| 33 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +91 | 165119 |
| 34 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | +91 | 39560 |
| 35 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +91 | 35695 |
| 36 | [docling-project/docling](https://github.com/docling-project/docling) | +89 | 53120 |
| 37 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +86 | 258376 |
| 38 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +85 | 124004 |
| 39 | [localsend/localsend](https://github.com/localsend/localsend) | +85 | 75020 |
| 40 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +82 | 143084 |
| 41 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +82 | 59565 |
| 42 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +82 | 47362 |
| 43 | [openai/codex](https://github.com/openai/codex) | +81 | 60424 |
| 44 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +80 | 56212 |
| 45 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +76 | 94574 |
| 46 | [immich-app/immich](https://github.com/immich-app/immich) | +76 | 92561 |
| 47 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | +72 | 106648 |
| 48 | [upstash/context7](https://github.com/upstash/context7) | +70 | 45804 |
| 49 | [torvalds/linux](https://github.com/torvalds/linux) | +69 | 217438 |
| 50 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | +68 | 107557 |
