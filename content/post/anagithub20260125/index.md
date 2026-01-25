---
title: "GitHub 趋势报告 2026-01-25"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-01-25T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-01-25 20:27:31

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
        'daily': {"categories": ["clash-verge-rev/clash-verge-rev", "n8n-io/n8n", "tw93/Mole", "Shubhamsaboo/awesome-llm-apps", "public-apis/public-apis", "firecrawl/firecrawl", "github/spec-kit", "x1xhlol/system-prompts-and-models-of-ai-tools", "yt-dlp/yt-dlp", "daytonaio/daytona", "sindresorhus/awesome", "openai/codex", "DigitalPlatDev/FreeDomain", "anthropics/claude-code", "codecrafters-io/build-your-own-x", "browser-use/browser-use", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "remotion-dev/remotion"], "data": [154, 158, 162, 167, 168, 170, 174, 175, 176, 216, 235, 238, 245, 282, 306, 312, 654, 908, 939, 1098]},
        'weekly': {"categories": ["n8n-io/n8n", "firecrawl/firecrawl", "sindresorhus/awesome", "tw93/Mole", "github/spec-kit", "yt-dlp/yt-dlp", "twitter/the-algorithm", "microsoft/Data-Science-For-Beginners", "public-apis/public-apis", "DigitalPlatDev/FreeDomain", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "anthropics/skills", "anomalyco/opencode", "MHSanaei/3x-ui", "remotion-dev/remotion", "obra/superpowers", "slatedocs/slate"], "data": [1405, 1550, 1557, 1592, 1647, 1653, 1660, 1759, 1793, 1816, 1939, 2400, 2485, 2692, 8283, 10765, 29105, 30479, 35862, 36169]},
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
| 1 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1098 | 30479 |
| 2 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +939 | 87281 |
| 3 | [anthropics/skills](https://github.com/anthropics/skills) | +908 | 52783 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +654 | 35862 |
| 5 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +312 | 77024 |
| 6 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +306 | 460564 |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +282 | 60553 |
| 8 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +245 | 143376 |
| 9 | [openai/codex](https://github.com/openai/codex) | +238 | 57389 |
| 10 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +235 | 431977 |
| 11 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +216 | 50385 |
| 12 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +176 | 144069 |
| 13 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +175 | 111029 |
| 14 | [github/spec-kit](https://github.com/github/spec-kit) | +174 | 65013 |
| 15 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +170 | 77293 |
| 16 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +168 | 393406 |
| 17 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +167 | 89346 |
| 18 | [tw93/Mole](https://github.com/tw93/Mole) | +162 | 31666 |
| 19 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +158 | 171189 |
| 20 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +154 | 94057 |
| 21 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +151 | 269992 |
| 22 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +147 | 279873 |
| 23 | [usememos/memos](https://github.com/usememos/memos) | +130 | 55630 |
| 24 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +129 | 31795 |
| 25 | [upstash/context7](https://github.com/upstash/context7) | +125 | 43460 |
| 26 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +123 | 58100 |
| 27 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | +123 | 54784 |
| 28 | [ollama/ollama](https://github.com/ollama/ollama) | +117 | 160571 |
| 29 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +116 | 92484 |
| 30 | [DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) | +113 | 37094 |
| 31 | [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) | +112 | 143560 |
| 32 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +112 | 141141 |
| 33 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +108 | 333334 |
| 34 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +105 | 101412 |
| 35 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +104 | 203663 |
| 36 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +101 | 44468 |
| 37 | [Lissy93/web-check](https://github.com/Lissy93/web-check) | +100 | 30974 |
| 38 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +95 | 163740 |
| 39 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +90 | 68548 |
| 40 | [torvalds/linux](https://github.com/torvalds/linux) | +89 | 215188 |
| 41 | [tw93/Pake](https://github.com/tw93/Pake) | +85 | 45324 |
| 42 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +83 | 256600 |
| 43 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +83 | 163429 |
| 44 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +83 | 121841 |
| 45 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +81 | 56566 |
| 46 | [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | +76 | 72143 |
| 47 | [immich-app/immich](https://github.com/immich-app/immich) | +74 | 89888 |
| 48 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | +73 | 110216 |
| 49 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +72 | 31842 |
| 50 | [langgenius/dify](https://github.com/langgenius/dify) | +70 | 127162 |
