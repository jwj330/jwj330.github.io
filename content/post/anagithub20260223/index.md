---
title: "GitHub 趋势报告 2026-02-23"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-23T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-23 20:47:07

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
        'daily': {"categories": ["thedotmack/claude-mem", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "nextlevelbuilder/ui-ux-pro-max-skill", "firecrawl/firecrawl", "codecrafters-io/build-your-own-x", "f/prompts.chat", "sindresorhus/awesome", "code-yeongyu/oh-my-opencode", "daytonaio/daytona", "tw93/Mole", "OpenBB-finance/OpenBB", "anthropics/claude-code", "anomalyco/opencode", "anthropics/skills", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "qarmin/czkawka"], "data": [249, 263, 273, 290, 290, 302, 320, 325, 330, 425, 432, 444, 453, 561, 623, 684, 1326, 2662, 2762, 29456]},
        'weekly': {"categories": ["github/spec-kit", "f/prompts.chat", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "nextlevelbuilder/ui-ux-pro-max-skill", "codecrafters-io/build-your-own-x", "firecrawl/firecrawl", "anthropics/claude-code", "sindresorhus/awesome", "affaan-m/everything-claude-code", "anthropics/skills", "daytonaio/daytona", "anomalyco/opencode", "Developer-Y/cs-video-courses", "x1xhlol/system-prompts-and-models-of-ai-tools", "obra/superpowers", "openclaw/openclaw", "qarmin/czkawka", "thedotmack/claude-mem"], "data": [1429, 1618, 1674, 1702, 1737, 1753, 1892, 1989, 2173, 2276, 3200, 3338, 3364, 3593, 4031, 5336, 6370, 19935, 29456, 30420]},
        'monthly': {"categories": ["sindresorhus/awesome", "anthropics/claude-code", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "qarmin/czkawka", "thedotmack/claude-mem", "TauricResearch/TradingAgents", "patchy631/ai-engineering-hub", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "google/langextract", "nextlevelbuilder/ui-ux-pro-max-skill", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8392, 9056, 9265, 9775, 22071, 22770, 23964, 29456, 30420, 30450, 30538, 31007, 31142, 32722, 33448, 33572, 33778, 36960, 50142, 220969]}
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
| 1 | [qarmin/czkawka](https://github.com/qarmin/czkawka) | +29456 | 29456 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2762 | 120119 |
| 3 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2662 | 220969 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +1326 | 59172 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +684 | 50142 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +623 | 73946 |
| 7 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +561 | 109112 |
| 8 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +453 | 69327 |
| 9 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +444 | 61360 |
| 10 | [tw93/Mole](https://github.com/tw93/Mole) | +432 | 36699 |
| 11 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +425 | 59944 |
| 12 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +330 | 33448 |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +325 | 440134 |
| 14 | [f/prompts.chat](https://github.com/f/prompts.chat) | +320 | 146954 |
| 15 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +302 | 468327 |
| 16 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +290 | 85007 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +290 | 33778 |
| 18 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +273 | 36960 |
| 19 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +263 | 399840 |
| 20 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +249 | 30420 |
| 21 | [github/spec-kit](https://github.com/github/spec-kit) | +215 | 71434 |
| 22 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +205 | 37254 |
| 23 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +200 | 148811 |
| 24 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +174 | 274761 |
| 25 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +168 | 175988 |
| 26 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +165 | 96730 |
| 27 | [torvalds/linux](https://github.com/torvalds/linux) | +163 | 218419 |
| 28 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +162 | 32722 |
| 29 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +160 | 148232 |
| 30 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +160 | 98197 |
| 31 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +159 | 336369 |
| 32 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +157 | 207476 |
| 33 | [immich-app/immich](https://github.com/immich-app/immich) | +156 | 93326 |
| 34 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | +151 | 60840 |
| 35 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +150 | 74754 |
| 36 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +148 | 284241 |
| 37 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | +147 | 58809 |
| 38 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +134 | 259047 |
| 39 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +122 | 95426 |
| 40 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | +121 | 106923 |
| 41 | [openai/codex](https://github.com/openai/codex) | +118 | 61553 |
| 42 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +115 | 47001 |
| 43 | [upstash/context7](https://github.com/upstash/context7) | +108 | 46629 |
| 44 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +103 | 166760 |
| 45 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +100 | 124698 |
| 46 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +100 | 51660 |
| 47 | [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | +98 | 40904 |
| 48 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +98 | 37696 |
| 49 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +97 | 44437 |
| 50 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +97 | 30450 |
