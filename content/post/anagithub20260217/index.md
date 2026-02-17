---
title: "GitHub 趋势报告 2026-02-17"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-17T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-17 20:41:08

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
        'daily': {"categories": ["Shubhamsaboo/awesome-llm-apps", "NationalSecurityAgency/ghidra", "github/spec-kit", "awesome-selfhosted/awesome-selfhosted", "anthropics/claude-code", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "sindresorhus/awesome", "bmad-code-org/BMAD-METHOD", "nextlevelbuilder/ui-ux-pro-max-skill", "codecrafters-io/build-your-own-x", "firecrawl/firecrawl", "daytonaio/daytona", "ashishps1/awesome-system-design-resources", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "Developer-Y/cs-video-courses", "openclaw/openclaw"], "data": [172, 173, 179, 179, 193, 202, 227, 239, 241, 257, 274, 327, 363, 399, 416, 421, 513, 673, 876, 3784]},
        'weekly': {"categories": ["public-apis/public-apis", "github/spec-kit", "anthropics/claude-code", "sindresorhus/awesome", "kuchin/awesome-cto", "codecrafters-io/build-your-own-x", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "nextlevelbuilder/ui-ux-pro-max-skill", "daytonaio/daytona", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "ashishps1/awesome-system-design-resources", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "patchy631/ai-engineering-hub", "google/langextract"], "data": [1153, 1356, 1480, 1572, 1601, 1675, 1752, 1909, 1997, 2028, 2121, 2180, 2945, 3738, 3806, 4241, 4315, 22399, 29842, 32842]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "anomalyco/opencode", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [8630, 8958, 9486, 26524, 29516, 29842, 30118, 30472, 30570, 31004, 31853, 31976, 32282, 32842, 35485, 36162, 36944, 47363, 53475, 204818]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3784 | 204818 |
| 2 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +876 | 71599 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +673 | 53475 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +513 | 106032 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +421 | 47363 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +416 | 71024 |
| 7 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +399 | 32762 |
| 8 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +363 | 56943 |
| 9 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +327 | 83345 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +274 | 466709 |
| 11 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +257 | 32282 |
| 12 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +241 | 36118 |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +239 | 438097 |
| 14 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +227 | 35485 |
| 15 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +202 | 31976 |
| 16 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +193 | 67347 |
| 17 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +179 | 273721 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +179 | 70184 |
| 19 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +173 | 64715 |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +172 | 95679 |
| 21 | [openai/codex](https://github.com/openai/codex) | +169 | 60831 |
| 22 | [google/langextract](https://github.com/google/langextract) | +159 | 32842 |
| 23 | [tw93/Mole](https://github.com/tw93/Mole) | +146 | 35108 |
| 24 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +146 | 31853 |
| 25 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +143 | 174945 |
| 26 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +141 | 114924 |
| 27 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +139 | 283267 |
| 28 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +136 | 36944 |
| 29 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +133 | 398811 |
| 30 | [torvalds/linux](https://github.com/torvalds/linux) | +126 | 217688 |
| 31 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +125 | 206624 |
| 32 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +118 | 147902 |
| 33 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +96 | 124178 |
| 34 | [upstash/context7](https://github.com/upstash/context7) | +94 | 45978 |
| 35 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +90 | 165286 |
| 36 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +89 | 147478 |
| 37 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +89 | 29842 |
| 38 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +88 | 335613 |
| 39 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +87 | 30164 |
| 40 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +86 | 94726 |
| 41 | [immich-app/immich](https://github.com/immich-app/immich) | +86 | 92724 |
| 42 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | +83 | 60285 |
| 43 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | +82 | 106830 |
| 44 | [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | +82 | 72498 |
| 45 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +81 | 43551 |
| 46 | [docling-project/docling](https://github.com/docling-project/docling) | +80 | 53281 |
| 47 | [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | +79 | 349209 |
| 48 | [dkhamsing/open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) | +77 | 48845 |
| 49 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +76 | 166273 |
| 50 | [ollama/ollama](https://github.com/ollama/ollama) | +75 | 162779 |
