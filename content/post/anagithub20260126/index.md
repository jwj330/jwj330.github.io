---
title: "GitHub 趋势报告 2026-01-26"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-26T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-26 20:30:32

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
        'daily': {"categories": ["firecrawl/firecrawl", "sindresorhus/awesome", "tw93/Mole", "DigitalPlatDev/FreeDomain", "DataTalksClub/data-engineering-zoomcamp", "bmad-code-org/BMAD-METHOD", "github/spec-kit", "Shubhamsaboo/awesome-llm-apps", "openai/codex", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "pathwaycom/pathway", "pathwaycom/llm-app", "obra/superpowers", "remotion-dev/remotion", "anthropics/skills", "anomalyco/opencode", "block/goose", "affaan-m/everything-claude-code", "clawdbot/clawdbot"], "data": [224, 234, 235, 247, 248, 250, 286, 291, 313, 330, 390, 451, 459, 993, 1325, 1356, 1422, 29092, 30727, 43206]},
        'weekly': {"categories": ["tw93/Mole", "sindresorhus/awesome", "public-apis/public-apis", "twitter/the-algorithm", "github/spec-kit", "microsoft/Data-Science-For-Beginners", "DigitalPlatDev/FreeDomain", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "block/goose", "MHSanaei/3x-ui", "affaan-m/everything-claude-code", "remotion-dev/remotion", "slatedocs/slate", "clawdbot/clawdbot"], "data": [1557, 1574, 1612, 1663, 1699, 1768, 1775, 1798, 2169, 2453, 2710, 7197, 8605, 10219, 29092, 29170, 30727, 31804, 36168, 43206]},
        'monthly': {"categories": [], "data": []}
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
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +43206 | 43206 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +30727 | 30727 |
| 3 | [block/goose](https://github.com/block/goose) | +29092 | 29092 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1422 | 88703 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +1356 | 54139 |
| 6 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1325 | 31804 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +993 | 36855 |
| 8 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +459 | 55243 |
| 9 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +451 | 58551 |
| 10 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +390 | 60943 |
| 11 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +330 | 460894 |
| 12 | [openai/codex](https://github.com/openai/codex) | +313 | 57702 |
| 13 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +291 | 89637 |
| 14 | [github/spec-kit](https://github.com/github/spec-kit) | +286 | 65299 |
| 15 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +250 | 32045 |
| 16 | [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | +248 | 37342 |
| 17 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +247 | 143623 |
| 18 | [tw93/Mole](https://github.com/tw93/Mole) | +235 | 31901 |
| 19 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +234 | 432211 |
| 20 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +224 | 77517 |
| 21 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +215 | 94272 |
| 22 | [immich-app/immich](https://github.com/immich-app/immich) | +203 | 90091 |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +201 | 171390 |
| 24 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +201 | 44669 |
| 25 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | +183 | 110399 |
| 26 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +179 | 393585 |
| 27 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +178 | 144247 |
| 28 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +175 | 111204 |
| 29 | [upstash/context7](https://github.com/upstash/context7) | +174 | 43634 |
| 30 | [langgenius/dify](https://github.com/langgenius/dify) | +173 | 127335 |
| 31 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +161 | 270153 |
| 32 | [usememos/memos](https://github.com/usememos/memos) | +150 | 55780 |
| 33 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +139 | 163879 |
| 34 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +133 | 280006 |
| 35 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +132 | 203795 |
| 36 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +130 | 143690 |
| 37 | [Lissy93/web-check](https://github.com/Lissy93/web-check) | +130 | 31104 |
| 38 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +127 | 101539 |
| 39 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +124 | 333458 |
| 40 | [amruthpillai/reactive-resume](https://github.com/amruthpillai/reactive-resume) | +119 | 34723 |
| 41 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +118 | 77142 |
| 42 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +115 | 141256 |
| 43 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +115 | 92599 |
| 44 | [ollama/ollama](https://github.com/ollama/ollama) | +108 | 160679 |
| 45 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | +104 | 77244 |
| 46 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +103 | 121944 |
| 47 | [astral-sh/uv](https://github.com/astral-sh/uv) | +103 | 77833 |
| 48 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +103 | 68651 |
| 49 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +98 | 256698 |
| 50 | [torvalds/linux](https://github.com/torvalds/linux) | +98 | 215286 |
