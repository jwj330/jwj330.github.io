---
title: "GitHub 趋势报告 2026-02-20"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-20T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-20 20:35:42

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
        'daily': {"categories": ["daytonaio/daytona", "Developer-Y/cs-video-courses", "Shubhamsaboo/awesome-llm-apps", "bmad-code-org/BMAD-METHOD", "codecrafters-io/build-your-own-x", "github/spec-kit", "f/prompts.chat", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "sindresorhus/awesome", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "thedotmack/claude-mem"], "data": [196, 196, 197, 199, 200, 205, 214, 224, 235, 240, 247, 260, 263, 275, 383, 470, 552, 892, 2568, 29551]},
        'weekly': {"categories": ["github/spec-kit", "code-yeongyu/oh-my-opencode", "anthropics/claude-code", "google/langextract", "Shubhamsaboo/awesome-llm-apps", "ComposioHQ/awesome-claude-skills", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "nextlevelbuilder/ui-ux-pro-max-skill", "firecrawl/firecrawl", "daytonaio/daytona", "anthropics/skills", "ashishps1/awesome-system-design-resources", "affaan-m/everything-claude-code", "Developer-Y/cs-video-courses", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "thedotmack/claude-mem", "patchy631/ai-engineering-hub"], "data": [1298, 1361, 1375, 1412, 1533, 1646, 1713, 1771, 1963, 2011, 2935, 3053, 3096, 3203, 3487, 3649, 5106, 22472, 29551, 30287]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "anthropics/claude-code", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "thedotmack/claude-mem", "TauricResearch/TradingAgents", "patchy631/ai-engineering-hub", "MHSanaei/3x-ui", "block/goose", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "slatedocs/slate", "ComposioHQ/awesome-claude-skills", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8361, 8973, 9545, 23963, 24501, 25538, 29551, 30251, 30287, 30586, 30781, 32265, 32581, 33001, 33369, 36162, 36202, 37360, 48722, 214034]}
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
| 1 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +29551 | 29551 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2568 | 214034 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +892 | 56126 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +552 | 107624 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +470 | 72376 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +383 | 48722 |
| 7 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +275 | 84241 |
| 8 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +263 | 32581 |
| 9 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +260 | 438900 |
| 10 | [tw93/Mole](https://github.com/tw93/Mole) | +247 | 35695 |
| 11 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +240 | 36202 |
| 12 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +235 | 33001 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +224 | 68010 |
| 14 | [f/prompts.chat](https://github.com/f/prompts.chat) | +214 | 145816 |
| 15 | [github/spec-kit](https://github.com/github/spec-kit) | +205 | 70811 |
| 16 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +200 | 467440 |
| 17 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +199 | 36655 |
| 18 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +197 | 96284 |
| 19 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +196 | 74199 |
| 20 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +196 | 58804 |
| 21 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +184 | 283834 |
| 22 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +183 | 274296 |
| 23 | [PostHog/posthog](https://github.com/PostHog/posthog) | +178 | 31502 |
| 24 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +167 | 175524 |
| 25 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +158 | 30287 |
| 26 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +157 | 95073 |
| 27 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +145 | 148286 |
| 28 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +140 | 37360 |
| 29 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +140 | 32265 |
| 30 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +137 | 97822 |
| 31 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +136 | 33247 |
| 32 | [docling-project/docling](https://github.com/docling-project/docling) | +130 | 53679 |
| 33 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +119 | 399289 |
| 34 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +119 | 115323 |
| 35 | [block/goose](https://github.com/block/goose) | +119 | 30781 |
| 36 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +112 | 207064 |
| 37 | [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | +109 | 72934 |
| 38 | [upstash/context7](https://github.com/upstash/context7) | +104 | 46328 |
| 39 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +101 | 335988 |
| 40 | [openai/codex](https://github.com/openai/codex) | +101 | 61217 |
| 41 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +100 | 147779 |
| 42 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +98 | 124444 |
| 43 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | +97 | 81194 |
| 44 | [torvalds/linux](https://github.com/torvalds/linux) | +91 | 218060 |
| 45 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +86 | 165608 |
| 46 | [google/langextract](https://github.com/google/langextract) | +85 | 33369 |
| 47 | [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | +83 | 349484 |
| 48 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +83 | 72969 |
| 49 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +82 | 95468 |
| 50 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +81 | 166513 |
