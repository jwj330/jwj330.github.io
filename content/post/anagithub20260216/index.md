---
title: "GitHub 趋势报告 2026-02-16"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-16T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-16 20:35:02

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
        'daily': {"categories": ["anthropics/claude-code", "github/spec-kit", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "code-yeongyu/oh-my-opencode", "bmad-code-org/BMAD-METHOD", "google/langextract", "sindresorhus/awesome", "ComposioHQ/awesome-claude-skills", "openai/codex", "codecrafters-io/build-your-own-x", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "obra/superpowers", "ashishps1/awesome-system-design-resources", "openclaw/openclaw"], "data": [157, 161, 163, 172, 182, 182, 190, 208, 221, 238, 253, 259, 271, 391, 466, 473, 532, 749, 859, 4425]},
        'weekly': {"categories": ["sindresorhus/awesome", "anthropics/claude-code", "kuchin/awesome-cto", "public-apis/public-apis", "codecrafters-io/build-your-own-x", "code-yeongyu/oh-my-opencode", "daytonaio/daytona", "nextlevelbuilder/ui-ux-pro-max-skill", "ComposioHQ/awesome-claude-skills", "firecrawl/firecrawl", "Shubhamsaboo/awesome-llm-apps", "ashishps1/awesome-system-design-resources", "affaan-m/everything-claude-code", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw", "nginx/nginx", "patchy631/ai-engineering-hub", "google/langextract"], "data": [1575, 1583, 1588, 1609, 1625, 1892, 1921, 2069, 2132, 2273, 2421, 2573, 4037, 4081, 4350, 4453, 21783, 29351, 29753, 32683]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "anomalyco/opencode", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [8812, 9075, 9601, 26832, 29753, 30076, 30408, 30523, 30619, 30997, 31707, 31774, 32025, 32683, 35258, 36162, 36808, 46942, 52802, 201034]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4425 | 201034 |
| 2 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +859 | 32363 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +749 | 52802 |
| 4 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +532 | 32025 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +473 | 105519 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +466 | 46942 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | +391 | 70608 |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +271 | 83018 |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +259 | 95507 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +253 | 466435 |
| 11 | [openai/codex](https://github.com/openai/codex) | +238 | 60662 |
| 12 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +221 | 35258 |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +208 | 437858 |
| 14 | [google/langextract](https://github.com/google/langextract) | +190 | 32683 |
| 15 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +182 | 35877 |
| 16 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +182 | 31774 |
| 17 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +172 | 56580 |
| 18 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +163 | 114783 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +161 | 70005 |
| 20 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +157 | 67154 |
| 21 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +152 | 283128 |
| 22 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +150 | 398678 |
| 23 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +148 | 64542 |
| 24 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +147 | 273542 |
| 25 | [tw93/Mole](https://github.com/tw93/Mole) | +146 | 34962 |
| 26 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +138 | 174802 |
| 27 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +135 | 31707 |
| 28 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +132 | 147389 |
| 29 | [torvalds/linux](https://github.com/torvalds/linux) | +124 | 217562 |
| 30 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +121 | 147784 |
| 31 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +116 | 36808 |
| 32 | [freqtrade/freqtrade](https://github.com/freqtrade/freqtrade) | +103 | 46864 |
| 33 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +102 | 47464 |
| 34 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | +100 | 106748 |
| 35 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +98 | 166197 |
| 36 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +95 | 29753 |
| 37 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +94 | 206499 |
| 38 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +92 | 43470 |
| 39 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +87 | 335525 |
| 40 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +87 | 58082 |
| 41 | [docling-project/docling](https://github.com/docling-project/docling) | +81 | 53201 |
| 42 | [upstash/context7](https://github.com/upstash/context7) | +80 | 45884 |
| 43 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +78 | 124082 |
| 44 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +77 | 165196 |
| 45 | [immich-app/immich](https://github.com/immich-app/immich) | +77 | 92638 |
| 46 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +76 | 258452 |
| 47 | [sxyazi/yazi](https://github.com/sxyazi/yazi) | +74 | 32709 |
| 48 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | +68 | 132636 |
| 49 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +68 | 36119 |
| 50 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | +67 | 111664 |
