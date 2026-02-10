---
title: "GitHub 趋势报告 2026-02-10"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-10T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-10 20:48:01

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
        'daily': {"categories": ["tw93/Mole", "jingyaogong/minimind", "codecrafters-io/build-your-own-x", "drawdb-io/drawdb", "sindresorhus/awesome", "github/spec-kit", "daytonaio/daytona", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "ComposioHQ/awesome-claude-skills", "Shubhamsaboo/awesome-llm-apps", "public-apis/public-apis", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "openclaw/openclaw", "nginx/nginx"], "data": [201, 222, 224, 230, 242, 248, 256, 296, 329, 342, 420, 450, 472, 589, 652, 708, 725, 759, 3168, 29319]},
        'weekly': {"categories": ["awesome-selfhosted/awesome-selfhosted", "remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "github/spec-kit", "Shubhamsaboo/awesome-llm-apps", "codecrafters-io/build-your-own-x", "firecrawl/firecrawl", "sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "obra/superpowers", "openclaw/openclaw", "TauricResearch/TradingAgents", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill"], "data": [1163, 1268, 1272, 1514, 1619, 1713, 1762, 1790, 2180, 2295, 2598, 3855, 4656, 5194, 5227, 5756, 25284, 29708, 30224, 30285]},
        'monthly': {"categories": ["daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "code-yeongyu/oh-my-opencode", "block/goose", "nextlevelbuilder/ui-ux-pro-max-skill", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "anomalyco/opencode", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [9778, 10687, 29679, 29708, 29908, 30092, 30224, 30226, 30285, 30748, 30902, 33576, 34333, 36014, 36167, 36722, 40342, 43557, 49160, 182419]}
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
| 1 | [nginx/nginx](https://github.com/nginx/nginx) | +29319 | 29319 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3168 | 182419 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +759 | 67286 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +725 | 101791 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +708 | 49160 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +652 | 43557 |
| 7 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +589 | 397658 |
| 8 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +472 | 93558 |
| 9 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +450 | 33576 |
| 10 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +420 | 81165 |
| 11 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +342 | 30224 |
| 12 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +329 | 30285 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +296 | 65867 |
| 14 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +256 | 54915 |
| 15 | [github/spec-kit](https://github.com/github/spec-kit) | +248 | 68828 |
| 16 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +242 | 436525 |
| 17 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +230 | 36228 |
| 18 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +224 | 465034 |
| 19 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +222 | 39251 |
| 20 | [tw93/Mole](https://github.com/tw93/Mole) | +201 | 34333 |
| 21 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +199 | 36014 |
| 22 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +195 | 272622 |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +192 | 173964 |
| 24 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +174 | 96764 |
| 25 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +172 | 35118 |
| 26 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +170 | 39536 |
| 27 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +167 | 146872 |
| 28 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +153 | 114076 |
| 29 | [openai/codex](https://github.com/openai/codex) | +148 | 59848 |
| 30 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +145 | 146617 |
| 31 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +139 | 282276 |
| 32 | [langgenius/dify](https://github.com/langgenius/dify) | +135 | 129321 |
| 33 | [torvalds/linux](https://github.com/torvalds/linux) | +132 | 216887 |
| 34 | [upstash/context7](https://github.com/upstash/context7) | +122 | 45334 |
| 35 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +120 | 46030 |
| 36 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +120 | 29708 |
| 37 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +119 | 30902 |
| 38 | [f/prompts.chat](https://github.com/f/prompts.chat) | +116 | 144998 |
| 39 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +115 | 42823 |
| 40 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +110 | 94165 |
| 41 | [docling-project/docling](https://github.com/docling-project/docling) | +110 | 52652 |
| 42 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +109 | 50390 |
| 43 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +108 | 123518 |
| 44 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +107 | 165540 |
| 45 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +106 | 334972 |
| 46 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +106 | 43467 |
| 47 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | +102 | 85065 |
| 48 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +101 | 205850 |
| 49 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +100 | 46965 |
| 50 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +97 | 69998 |
