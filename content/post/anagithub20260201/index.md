---
title: "GitHub 趋势报告 2026-02-01"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-01T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-01 20:29:48

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
        'daily': {"categories": ["Shubhamsaboo/awesome-llm-apps", "EbookFoundation/free-programming-books", "github/spec-kit", "firecrawl/firecrawl", "DigitalPlatDev/FreeDomain", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "casey/just", "PaddlePaddle/PaddleOCR", "anthropics/claude-code", "x1xhlol/system-prompts-and-models-of-ai-tools", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "affaan-m/everything-claude-code", "openclaw/openclaw", "asgeirtj/system_prompts_leaks"], "data": [180, 192, 208, 211, 212, 220, 222, 234, 240, 247, 257, 258, 284, 300, 596, 677, 704, 801, 9365, 29308]},
        'weekly': {"categories": ["immich-app/immich", "x1xhlol/system-prompts-and-models-of-ai-tools", "firecrawl/firecrawl", "bmad-code-org/BMAD-METHOD", "DigitalPlatDev/FreeDomain", "github/spec-kit", "daytonaio/daytona", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "Shubhamsaboo/awesome-llm-apps", "anthropics/claude-code", "remotion-dev/remotion", "obra/superpowers", "anomalyco/opencode", "anthropics/skills", "flameshot-org/flameshot", "asgeirtj/system_prompts_leaks", "block/goose", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [1462, 1554, 1641, 1728, 1739, 1760, 1957, 2205, 2231, 2272, 2438, 3820, 5840, 7324, 7396, 29152, 29308, 29646, 36986, 140555]},
        'monthly': {"categories": ["daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "flameshot-org/flameshot", "asgeirtj/system_prompts_leaks", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "block/goose", "blakeblackshear/frigate", "chen08209/FlClash", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [10494, 12456, 28410, 29152, 29308, 29343, 29487, 29646, 29890, 30557, 31593, 32748, 33523, 34299, 36170, 36580, 36986, 41702, 48982, 140555]}
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
| 1 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +29308 | 29308 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9365 | 140555 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +801 | 36986 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +704 | 94605 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +677 | 41702 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +596 | 60179 |
| 7 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +300 | 434208 |
| 8 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +284 | 462769 |
| 9 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +258 | 52342 |
| 10 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +257 | 112583 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +247 | 62991 |
| 12 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +240 | 69785 |
| 13 | [casey/just](https://github.com/casey/just) | +234 | 30548 |
| 14 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +222 | 34299 |
| 15 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +220 | 33523 |
| 16 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +212 | 145115 |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +211 | 78934 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +208 | 66773 |
| 19 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | +192 | 381703 |
| 20 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +180 | 91618 |
| 21 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +174 | 394706 |
| 22 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +171 | 271123 |
| 23 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +171 | 145311 |
| 24 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | +166 | 128868 |
| 25 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +161 | 41244 |
| 26 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +142 | 95377 |
| 27 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +138 | 280958 |
| 28 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +125 | 204554 |
| 29 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +124 | 172467 |
| 30 | [tw93/Mole](https://github.com/tw93/Mole) | +124 | 32748 |
| 31 | [cline/cline](https://github.com/cline/cline) | +117 | 57469 |
| 32 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +114 | 334093 |
| 33 | [torvalds/linux](https://github.com/torvalds/linux) | +114 | 216012 |
| 34 | [termux/termux-app](https://github.com/termux/termux-app) | +114 | 49608 |
| 35 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +112 | 164510 |
| 36 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +110 | 53518 |
| 37 | [immich-app/immich](https://github.com/immich-app/immich) | +108 | 91350 |
| 38 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +100 | 141913 |
| 39 | [docling-project/docling](https://github.com/docling-project/docling) | +94 | 51753 |
| 40 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +92 | 257343 |
| 41 | [upstash/context7](https://github.com/upstash/context7) | +90 | 44384 |
| 42 | [ollama/ollama](https://github.com/ollama/ollama) | +88 | 161355 |
| 43 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +87 | 93244 |
| 44 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +85 | 38435 |
| 45 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +83 | 122582 |
| 46 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +83 | 42595 |
| 47 | [openai/codex](https://github.com/openai/codex) | +80 | 58341 |
| 48 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +78 | 163987 |
| 49 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +78 | 102142 |
| 50 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +78 | 94171 |
