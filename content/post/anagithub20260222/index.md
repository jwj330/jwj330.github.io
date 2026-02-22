---
title: "GitHub 趋势报告 2026-02-22"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-22T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-22 20:29:39

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
        'daily': {"categories": ["Developer-Y/cs-video-courses", "github/spec-kit", "ComposioHQ/awesome-claude-skills", "firecrawl/firecrawl", "karanpratapsingh/system-design", "codecrafters-io/build-your-own-x", "OpenBB-finance/OpenBB", "daytonaio/daytona", "code-yeongyu/oh-my-opencode", "tw93/Mole", "thedotmack/claude-mem", "f/prompts.chat", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "anthropics/claude-code", "sindresorhus/awesome", "obra/superpowers", "x1xhlol/system-prompts-and-models-of-ai-tools", "openclaw/openclaw"], "data": [225, 226, 232, 241, 248, 282, 285, 293, 303, 303, 386, 413, 414, 479, 500, 551, 586, 961, 1851, 2295]},
        'weekly': {"categories": ["bmad-code-org/BMAD-METHOD", "github/spec-kit", "tw93/Mole", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "firecrawl/firecrawl", "nextlevelbuilder/ui-ux-pro-max-skill", "ashishps1/awesome-system-design-resources", "sindresorhus/awesome", "x1xhlol/system-prompts-and-models-of-ai-tools", "affaan-m/everything-claude-code", "anthropics/skills", "daytonaio/daytona", "anomalyco/opencode", "Developer-Y/cs-video-courses", "obra/superpowers", "openclaw/openclaw", "thedotmack/claude-mem"], "data": [1354, 1375, 1451, 1526, 1650, 1843, 1877, 1970, 1995, 2076, 2159, 2737, 2982, 3106, 3111, 3505, 3883, 5793, 21698, 30171]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "thedotmack/claude-mem", "TauricResearch/TradingAgents", "patchy631/ai-engineering-hub", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8091, 8263, 8978, 9738, 22434, 23206, 23393, 30171, 30353, 30451, 30925, 31086, 32560, 33118, 33488, 33495, 36687, 37598, 49458, 218307]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2295 | 218307 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1851 | 117357 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +961 | 57846 |
| 4 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +586 | 439809 |
| 5 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +551 | 68874 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +500 | 73323 |
| 7 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +479 | 108551 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +414 | 49458 |
| 9 | [f/prompts.chat](https://github.com/f/prompts.chat) | +413 | 146634 |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +386 | 30171 |
| 11 | [tw93/Mole](https://github.com/tw93/Mole) | +303 | 36267 |
| 12 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +303 | 33118 |
| 13 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +293 | 59519 |
| 14 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +285 | 60916 |
| 15 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +282 | 468025 |
| 16 | [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | +248 | 40806 |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +241 | 84717 |
| 18 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +232 | 36687 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +226 | 71219 |
| 20 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +225 | 74604 |
| 21 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +212 | 33488 |
| 22 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +190 | 399577 |
| 23 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +171 | 32560 |
| 24 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +165 | 37049 |
| 25 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +164 | 54751 |
| 26 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +164 | 46886 |
| 27 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +161 | 274587 |
| 28 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +154 | 175820 |
| 29 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +152 | 148072 |
| 30 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +150 | 148611 |
| 31 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +141 | 96565 |
| 32 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +139 | 33580 |
| 33 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +135 | 284093 |
| 34 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +135 | 207319 |
| 35 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | +131 | 60689 |
| 36 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +119 | 336210 |
| 37 | [openai/codex](https://github.com/openai/codex) | +118 | 61435 |
| 38 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +117 | 95304 |
| 39 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +117 | 51960 |
| 40 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +113 | 37598 |
| 41 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +108 | 98037 |
| 42 | [torvalds/linux](https://github.com/torvalds/linux) | +107 | 218256 |
| 43 | [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | +103 | 51622 |
| 44 | [upstash/context7](https://github.com/upstash/context7) | +103 | 46521 |
| 45 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | +98 | 106802 |
| 46 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +98 | 47886 |
| 47 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +98 | 44340 |
| 48 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | +95 | 85729 |
| 49 | [syncthing/syncthing](https://github.com/syncthing/syncthing) | +93 | 80210 |
| 50 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +89 | 143545 |
