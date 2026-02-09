---
title: "GitHub 趋势报告 2026-02-09"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-09T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-09 20:42:22

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
        'daily': {"categories": ["DavidHDev/react-bits", "remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "sindresorhus/awesome", "github/spec-kit", "codecrafters-io/build-your-own-x", "firecrawl/firecrawl", "anthropics/claude-code", "Shubhamsaboo/awesome-llm-apps", "daytonaio/daytona", "tw93/Mole", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "public-apis/public-apis", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw"], "data": [173, 180, 189, 206, 213, 214, 219, 239, 243, 262, 321, 358, 365, 519, 547, 556, 744, 762, 838, 3108]},
        'weekly': {"categories": [], "data": []},
        'monthly': {"categories": ["daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "anthropics/prompt-eng-interactive-tutorial", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "anomalyco/opencode", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [9812, 10928, 29466, 29588, 29877, 29882, 29956, 30011, 30129, 30654, 30783, 33126, 34132, 35815, 36167, 36709, 41618, 42905, 48452, 179251]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3108 | 179251 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +838 | 48452 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +762 | 101066 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +744 | 66527 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +556 | 42905 |
| 6 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +547 | 397069 |
| 7 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +519 | 33126 |
| 8 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +365 | 29882 |
| 9 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +358 | 29956 |
| 10 | [tw93/Mole](https://github.com/tw93/Mole) | +321 | 34132 |
| 11 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +262 | 54659 |
| 12 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +243 | 93086 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +239 | 65571 |
| 14 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +219 | 80745 |
| 15 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +214 | 464810 |
| 16 | [github/spec-kit](https://github.com/github/spec-kit) | +213 | 68580 |
| 17 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +206 | 436283 |
| 18 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +189 | 146705 |
| 19 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +180 | 35815 |
| 20 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +173 | 35541 |
| 21 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +165 | 173772 |
| 22 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +158 | 34946 |
| 23 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +151 | 113923 |
| 24 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +146 | 272427 |
| 25 | [openai/codex](https://github.com/openai/codex) | +143 | 59700 |
| 26 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +141 | 146472 |
| 27 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +139 | 282137 |
| 28 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +135 | 96590 |
| 29 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +132 | 205749 |
| 30 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +131 | 45910 |
| 31 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +128 | 35998 |
| 32 | [ollama/ollama](https://github.com/ollama/ollama) | +122 | 162265 |
| 33 | [langgenius/dify](https://github.com/langgenius/dify) | +122 | 129186 |
| 34 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +115 | 334866 |
| 35 | [torvalds/linux](https://github.com/torvalds/linux) | +115 | 216755 |
| 36 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | +115 | 84963 |
| 37 | [upstash/context7](https://github.com/upstash/context7) | +113 | 45212 |
| 38 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +112 | 165433 |
| 39 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +112 | 50902 |
| 40 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +108 | 42708 |
| 41 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +107 | 43361 |
| 42 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +106 | 31202 |
| 43 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +102 | 30783 |
| 44 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +100 | 258004 |
| 45 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +99 | 94055 |
| 46 | [immich-app/immich](https://github.com/immich-app/immich) | +98 | 92086 |
| 47 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +97 | 123410 |
| 48 | [docling-project/docling](https://github.com/docling-project/docling) | +94 | 52542 |
| 49 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +93 | 102848 |
| 50 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +92 | 142626 |
