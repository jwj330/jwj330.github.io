---
title: "GitHub 趋势报告 2026-02-13"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-13T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-13 20:41:15

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
        'daily': {"categories": ["public-apis/public-apis", "kuchin/awesome-cto", "github/spec-kit", "massgravel/Microsoft-Activation-Scripts", "sindresorhus/awesome", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "codecrafters-io/build-your-own-x", "ComposioHQ/awesome-claude-skills", "ashishps1/awesome-system-design-resources", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "daytonaio/daytona", "Shubhamsaboo/awesome-llm-apps", "affaan-m/everything-claude-code", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "google/langextract", "openclaw/openclaw"], "data": [167, 168, 175, 192, 204, 207, 211, 217, 249, 262, 274, 284, 304, 451, 528, 559, 562, 641, 714, 2927]},
        'weekly': {"categories": ["awesome-selfhosted/awesome-selfhosted", "DigitalPlatDev/FreeDomain", "github/spec-kit", "kuchin/awesome-cto", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "firecrawl/firecrawl", "daytonaio/daytona", "Shubhamsaboo/awesome-llm-apps", "public-apis/public-apis", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "google/langextract"], "data": [1152, 1214, 1461, 1518, 1539, 1630, 1796, 2155, 2199, 2331, 2636, 3281, 4288, 4636, 4814, 4918, 20558, 31038, 31220, 31957]},
        'monthly': {"categories": ["sindresorhus/awesome", "codecrafters-io/build-your-own-x", "daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "asgeirtj/system_prompts_leaks", "google/langextract", "ComposioHQ/awesome-claude-skills", "anomalyco/opencode", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "obra/superpowers", "openclaw/openclaw"], "data": [7695, 9160, 9436, 10151, 28794, 29940, 30286, 30394, 30942, 31038, 31220, 31379, 31957, 34556, 34932, 36165, 36446, 45519, 51020, 191562]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2927 | 191562 |
| 2 | [google/langextract](https://github.com/google/langextract) | +714 | 31957 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +641 | 103975 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +562 | 69323 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +559 | 51020 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +528 | 45519 |
| 7 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +451 | 94751 |
| 8 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +304 | 55869 |
| 9 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +284 | 82230 |
| 10 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +274 | 31220 |
| 11 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +262 | 30151 |
| 12 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +249 | 34556 |
| 13 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +217 | 465669 |
| 14 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +211 | 31038 |
| 15 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +207 | 66635 |
| 16 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +204 | 437187 |
| 17 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +192 | 165938 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +175 | 69513 |
| 19 | [kuchin/awesome-cto](https://github.com/kuchin/awesome-cto) | +168 | 34031 |
| 20 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +167 | 398248 |
| 21 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +152 | 52154 |
| 22 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +151 | 147368 |
| 23 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | +143 | 129757 |
| 24 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +132 | 282697 |
| 25 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +132 | 174409 |
| 26 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +130 | 43206 |
| 27 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +128 | 273097 |
| 28 | [openai/codex](https://github.com/openai/codex) | +125 | 60259 |
| 29 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +121 | 31379 |
| 30 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +114 | 146973 |
| 31 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +112 | 35513 |
| 32 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +111 | 51205 |
| 33 | [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | +110 | 30186 |
| 34 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +108 | 36446 |
| 35 | [torvalds/linux](https://github.com/torvalds/linux) | +107 | 217288 |
| 36 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +106 | 123823 |
| 37 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +102 | 97164 |
| 38 | [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT) | +92 | 53118 |
| 39 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +91 | 114426 |
| 40 | [upstash/context7](https://github.com/upstash/context7) | +88 | 45669 |
| 41 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +87 | 206166 |
| 42 | [docling-project/docling](https://github.com/docling-project/docling) | +84 | 52944 |
| 43 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +76 | 60218 |
| 44 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +75 | 94428 |
| 45 | [immich-app/immich](https://github.com/immich-app/immich) | +73 | 92413 |
| 46 | [ChrisTitusTech/winutil](https://github.com/ChrisTitusTech/winutil) | +73 | 47191 |
| 47 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +68 | 57875 |
| 48 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +67 | 70244 |
| 49 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +66 | 335253 |
| 50 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +66 | 164958 |
