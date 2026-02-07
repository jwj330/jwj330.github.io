---
title: "GitHub 趋势报告 2026-02-07"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-07T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-07 20:30:41

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
        'daily': {"categories": ["Shubhamsaboo/awesome-llm-apps", "aquasecurity/trivy", "openai/codex", "awesome-selfhosted/awesome-selfhosted", "remotion-dev/remotion", "github/spec-kit", "DigitalPlatDev/FreeDomain", "DataExpert-io/data-engineer-handbook", "firecrawl/firecrawl", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "public-apis/public-apis", "affaan-m/everything-claude-code", "daytonaio/daytona", "anomalyco/opencode", "anthropics/skills", "ComposioHQ/awesome-claude-skills", "obra/superpowers", "openclaw/openclaw"], "data": [147, 148, 153, 161, 164, 177, 182, 203, 215, 226, 244, 247, 341, 491, 528, 557, 575, 580, 751, 2639]},
        'weekly': {"categories": ["bmad-code-org/BMAD-METHOD", "karpathy/nanochat", "remotion-dev/remotion", "public-apis/public-apis", "DigitalPlatDev/FreeDomain", "firecrawl/firecrawl", "github/spec-kit", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "daytonaio/daytona", "anthropics/claude-code", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "TauricResearch/TradingAgents", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "openclaw/openclaw"], "data": [1352, 1414, 1416, 1421, 1433, 1567, 1664, 1871, 1893, 2114, 2342, 5537, 5679, 5817, 5828, 29451, 30471, 30533, 31855, 42453]},
        'monthly': {"categories": ["anthropics/claude-code", "flameshot-org/flameshot", "TauricResearch/TradingAgents", "anthropics/skills", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "blakeblackshear/frigate", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw"], "data": [11797, 29240, 29451, 29508, 29762, 29886, 30000, 30052, 30471, 30533, 31855, 33694, 34655, 35493, 36167, 36691, 41722, 44670, 46853, 173643]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2639 | 173643 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +751 | 46853 |
| 3 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +580 | 31855 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +575 | 65262 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +557 | 99718 |
| 6 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +528 | 54198 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +491 | 41722 |
| 8 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +341 | 395953 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +247 | 65086 |
| 10 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +244 | 435801 |
| 11 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +226 | 464356 |
| 12 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +215 | 80290 |
| 13 | [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) | +203 | 40015 |
| 14 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +182 | 146336 |
| 15 | [github/spec-kit](https://github.com/github/spec-kit) | +177 | 68229 |
| 16 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +164 | 35493 |
| 17 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +161 | 272106 |
| 18 | [openai/codex](https://github.com/openai/codex) | +153 | 59434 |
| 19 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | +148 | 31657 |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +147 | 92567 |
| 21 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +140 | 281850 |
| 22 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +134 | 205486 |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +134 | 173481 |
| 24 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +124 | 34655 |
| 25 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +122 | 96339 |
| 26 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +118 | 146160 |
| 27 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +117 | 30533 |
| 28 | [kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans) | +106 | 47501 |
| 29 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +103 | 113644 |
| 30 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +101 | 334650 |
| 31 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +101 | 43172 |
| 32 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +97 | 165227 |
| 33 | [Dokploy/dokploy](https://github.com/Dokploy/dokploy) | +95 | 30033 |
| 34 | [tw93/Mole](https://github.com/tw93/Mole) | +94 | 33694 |
| 35 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +93 | 29707 |
| 36 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +92 | 42497 |
| 37 | [ollama/ollama](https://github.com/ollama/ollama) | +90 | 162053 |
| 38 | [exo-explore/exo](https://github.com/exo-explore/exo) | +88 | 41195 |
| 39 | [upstash/context7](https://github.com/upstash/context7) | +87 | 45039 |
| 40 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +86 | 142453 |
| 41 | [immich-app/immich](https://github.com/immich-app/immich) | +83 | 91924 |
| 42 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | +82 | 91563 |
| 43 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +81 | 164508 |
| 44 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +80 | 69741 |
| 45 | [torvalds/linux](https://github.com/torvalds/linux) | +79 | 216556 |
| 46 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +79 | 123233 |
| 47 | [docling-project/docling](https://github.com/docling-project/docling) | +77 | 52375 |
| 48 | [langgenius/dify](https://github.com/langgenius/dify) | +76 | 128998 |
| 49 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +74 | 29762 |
| 50 | [f/prompts.chat](https://github.com/f/prompts.chat) | +71 | 144759 |
