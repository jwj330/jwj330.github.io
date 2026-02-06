---
title: "GitHub 趋势报告 2026-02-06"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-06T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-06 20:37:23

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
        'daily': {"categories": ["Shubhamsaboo/awesome-llm-apps", "aquasecurity/trivy", "bmad-code-org/BMAD-METHOD", "openai/codex", "remotion-dev/remotion", "firecrawl/firecrawl", "codecrafters-io/build-your-own-x", "public-apis/public-apis", "DigitalPlatDev/FreeDomain", "github/spec-kit", "sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "flameshot-org/flameshot"], "data": [159, 172, 175, 190, 195, 211, 213, 220, 225, 227, 261, 436, 489, 566, 721, 780, 814, 859, 3728, 29236]},
        'weekly': {"categories": ["karpathy/nanochat", "x1xhlol/system-prompts-and-models-of-ai-tools", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "DigitalPlatDev/FreeDomain", "firecrawl/firecrawl", "github/spec-kit", "codecrafters-io/build-your-own-x", "daytonaio/daytona", "sindresorhus/awesome", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "TauricResearch/TradingAgents", "asgeirtj/system_prompts_leaks", "OpenBMB/ChatDev", "ComposioHQ/awesome-claude-skills", "openclaw/openclaw"], "data": [1362, 1423, 1494, 1508, 1555, 1591, 1634, 1924, 1965, 1976, 2354, 5569, 5788, 5925, 5978, 29393, 30416, 30423, 31275, 53525]},
        'monthly': {"categories": ["flameshot-org/flameshot", "TauricResearch/TradingAgents", "anthropics/skills", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "blakeblackshear/frigate", "block/goose", "asgeirtj/system_prompts_leaks", "OpenBMB/ChatDev", "ComposioHQ/awesome-claude-skills", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw"], "data": [29236, 29393, 29610, 29688, 29833, 29974, 30011, 30416, 30423, 31275, 31916, 33600, 34531, 35329, 36167, 36666, 41231, 45937, 46102, 171004]}
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
| 1 | [flameshot-org/flameshot](https://github.com/flameshot-org/flameshot) | +29236 | 29236 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3728 | 171004 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +859 | 46102 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +814 | 99161 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +780 | 64687 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +721 | 41231 |
| 7 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +566 | 31275 |
| 8 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +489 | 53670 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +436 | 64839 |
| 10 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +261 | 435557 |
| 11 | [github/spec-kit](https://github.com/github/spec-kit) | +227 | 68052 |
| 12 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +225 | 146154 |
| 13 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +220 | 395612 |
| 14 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +213 | 464130 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +211 | 80075 |
| 16 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +195 | 35329 |
| 17 | [openai/codex](https://github.com/openai/codex) | +190 | 59281 |
| 18 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +175 | 34531 |
| 19 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | +172 | 31509 |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +159 | 92420 |
| 21 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +158 | 173347 |
| 22 | [kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans) | +158 | 47395 |
| 23 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +157 | 271945 |
| 24 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +151 | 30416 |
| 25 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +146 | 96217 |
| 26 | [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) | +145 | 32494 |
| 27 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +141 | 205352 |
| 28 | [microsoft/qlib](https://github.com/microsoft/qlib) | +135 | 36929 |
| 29 | [tw93/Mole](https://github.com/tw93/Mole) | +132 | 33600 |
| 30 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +130 | 113541 |
| 31 | [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | +130 | 39812 |
| 32 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +129 | 281710 |
| 33 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | +126 | 91481 |
| 34 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +121 | 123154 |
| 35 | [ollama/ollama](https://github.com/ollama/ollama) | +120 | 161963 |
| 36 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +119 | 93808 |
| 37 | [upstash/context7](https://github.com/upstash/context7) | +116 | 44952 |
| 38 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +116 | 30423 |
| 39 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +115 | 53960 |
| 40 | [langgenius/dify](https://github.com/langgenius/dify) | +113 | 128922 |
| 41 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +107 | 146042 |
| 42 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +105 | 165130 |
| 43 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +102 | 142367 |
| 44 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +101 | 35399 |
| 45 | [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | +99 | 40106 |
| 46 | [torvalds/linux](https://github.com/torvalds/linux) | +95 | 216477 |
| 47 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +94 | 164427 |
| 48 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +90 | 43071 |
| 49 | [docling-project/docling](https://github.com/docling-project/docling) | +88 | 52298 |
| 50 | [immich-app/immich](https://github.com/immich-app/immich) | +87 | 91841 |
