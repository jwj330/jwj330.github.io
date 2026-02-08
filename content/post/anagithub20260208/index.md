---
title: "GitHub 趋势报告 2026-02-08"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-08T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-08 20:30:43

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
        'daily': {"categories": ["vinta/awesome-python", "yt-dlp/yt-dlp", "awesome-selfhosted/awesome-selfhosted", "DigitalPlatDev/FreeDomain", "daytonaio/daytona", "firecrawl/firecrawl", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "cloudcommunity/Free-Certifications", "Shubhamsaboo/awesome-llm-apps", "sindresorhus/awesome", "anthropics/skills", "public-apis/public-apis", "anomalyco/opencode", "affaan-m/everything-claude-code", "ComposioHQ/awesome-claude-skills", "obra/superpowers", "openclaw/openclaw", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill"], "data": [148, 171, 175, 180, 199, 236, 240, 246, 258, 276, 276, 521, 569, 586, 627, 752, 761, 2500, 29517, 29598]},
        'weekly': {"categories": ["karpathy/nanochat", "asgeirtj/system_prompts_leaks", "DigitalPlatDev/FreeDomain", "firecrawl/firecrawl", "github/spec-kit", "public-apis/public-apis", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "daytonaio/daytona", "anthropics/claude-code", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "TauricResearch/TradingAgents", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "OpenBMB/ChatDev", "ComposioHQ/awesome-claude-skills", "openclaw/openclaw"], "data": [1356, 1373, 1401, 1592, 1594, 1816, 1827, 1869, 2055, 2341, 5363, 5604, 5699, 5912, 29508, 29517, 29598, 30563, 32607, 35588]},
        'monthly': {"categories": ["anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "blakeblackshear/frigate", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw"], "data": [11286, 29296, 29508, 29517, 29598, 29820, 29950, 30023, 30078, 30563, 30681, 32607, 33811, 35635, 36167, 36699, 42349, 43218, 47614, 176143]}
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
| 1 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +29598 | 29598 |
| 2 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +29517 | 29517 |
| 3 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2500 | 176143 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +761 | 47614 |
| 5 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +752 | 32607 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +627 | 42349 |
| 7 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +586 | 100304 |
| 8 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +569 | 396522 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +521 | 65783 |
| 10 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +276 | 436077 |
| 11 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +276 | 92843 |
| 12 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +258 | 50790 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +246 | 65332 |
| 14 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +240 | 464596 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +236 | 80526 |
| 16 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +199 | 54397 |
| 17 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +180 | 146516 |
| 18 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +175 | 272281 |
| 19 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +171 | 146331 |
| 20 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +148 | 281998 |
| 21 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +148 | 30681 |
| 22 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +142 | 35635 |
| 23 | [github/spec-kit](https://github.com/github/spec-kit) | +138 | 68367 |
| 24 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +133 | 34788 |
| 25 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +131 | 205617 |
| 26 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +128 | 113772 |
| 27 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +126 | 173607 |
| 28 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | +126 | 31783 |
| 29 | [openai/codex](https://github.com/openai/codex) | +123 | 59557 |
| 30 | [tw93/Mole](https://github.com/tw93/Mole) | +117 | 33811 |
| 31 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +116 | 96455 |
| 32 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +103 | 42600 |
| 33 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +101 | 334751 |
| 34 | [microsoft/qlib](https://github.com/microsoft/qlib) | +98 | 37094 |
| 35 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +96 | 35368 |
| 36 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +94 | 165321 |
| 37 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +92 | 30563 |
| 38 | [ollama/ollama](https://github.com/ollama/ollama) | +90 | 162143 |
| 39 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +87 | 257904 |
| 40 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +87 | 46888 |
| 41 | [torvalds/linux](https://github.com/torvalds/linux) | +84 | 216640 |
| 42 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +82 | 43254 |
| 43 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +81 | 142534 |
| 44 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +80 | 123313 |
| 45 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +80 | 93956 |
| 46 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +79 | 45779 |
| 47 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | +78 | 382291 |
| 48 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +77 | 164585 |
| 49 | [docling-project/docling](https://github.com/docling-project/docling) | +73 | 52448 |
| 50 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +73 | 45651 |
