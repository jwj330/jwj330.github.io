---
title: "GitHub 趋势报告 2026-02-18"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-18T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-18 20:42:34

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
        'daily': {"categories": ["tw93/Mole", "awesome-selfhosted/awesome-selfhosted", "code-yeongyu/oh-my-opencode", "github/spec-kit", "n8n-io/n8n", "nextlevelbuilder/ui-ux-pro-max-skill", "Shubhamsaboo/awesome-llm-apps", "sindresorhus/awesome", "ComposioHQ/awesome-claude-skills", "anthropics/claude-code", "codecrafters-io/build-your-own-x", "ashishps1/awesome-system-design-resources", "firecrawl/firecrawl", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "daytonaio/daytona", "obra/superpowers", "Developer-Y/cs-video-courses", "openclaw/openclaw"], "data": [175, 181, 182, 204, 208, 213, 219, 228, 230, 232, 233, 271, 278, 405, 507, 533, 712, 854, 1678, 3512]},
        'weekly': {"categories": ["kuchin/awesome-cto", "github/spec-kit", "anthropics/claude-code", "sindresorhus/awesome", "code-yeongyu/oh-my-opencode", "codecrafters-io/build-your-own-x", "ComposioHQ/awesome-claude-skills", "nextlevelbuilder/ui-ux-pro-max-skill", "Shubhamsaboo/awesome-llm-apps", "firecrawl/firecrawl", "daytonaio/daytona", "Developer-Y/cs-video-courses", "google/langextract", "ashishps1/awesome-system-design-resources", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "patchy631/ai-engineering-hub"], "data": [1180, 1334, 1426, 1559, 1569, 1697, 1761, 1891, 1925, 2019, 2502, 2565, 2728, 3186, 3318, 3683, 3998, 4514, 22851, 29988]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "anthropics/claude-code", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8501, 9346, 9354, 24671, 25895, 28081, 29988, 30151, 30511, 30619, 31017, 31973, 32158, 32495, 33011, 35715, 36162, 37085, 47870, 208330]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3512 | 208330 |
| 2 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1678 | 73277 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +854 | 54329 |
| 4 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +712 | 57655 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +533 | 106565 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +507 | 47870 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | +405 | 71429 |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +278 | 83623 |
| 9 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +271 | 33033 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +233 | 466942 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +232 | 67579 |
| 12 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +230 | 35715 |
| 13 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +228 | 438325 |
| 14 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +219 | 95898 |
| 15 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +213 | 32495 |
| 16 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +208 | 175153 |
| 17 | [github/spec-kit](https://github.com/github/spec-kit) | +204 | 70388 |
| 18 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +182 | 32158 |
| 19 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +181 | 273902 |
| 20 | [tw93/Mole](https://github.com/tw93/Mole) | +175 | 35283 |
| 21 | [google/langextract](https://github.com/google/langextract) | +169 | 33011 |
| 22 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +166 | 283433 |
| 23 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +160 | 398971 |
| 24 | [openai/codex](https://github.com/openai/codex) | +156 | 60987 |
| 25 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +152 | 206776 |
| 26 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +146 | 29988 |
| 27 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +145 | 36263 |
| 28 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +141 | 37085 |
| 29 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +134 | 148036 |
| 30 | [torvalds/linux](https://github.com/torvalds/linux) | +129 | 217817 |
| 31 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +120 | 31973 |
| 32 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +118 | 115042 |
| 33 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +116 | 335729 |
| 34 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +115 | 147593 |
| 35 | [upstash/context7](https://github.com/upstash/context7) | +114 | 46092 |
| 36 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +109 | 70598 |
| 37 | [docling-project/docling](https://github.com/docling-project/docling) | +98 | 53379 |
| 38 | [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) | +94 | 31193 |
| 39 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +93 | 103509 |
| 40 | [immich-app/immich](https://github.com/immich-app/immich) | +93 | 92817 |
| 41 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +90 | 44022 |
| 42 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | +89 | 78933 |
| 43 | [geekan/HowToLiveLonger](https://github.com/geekan/HowToLiveLonger) | +89 | 34871 |
| 44 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +83 | 166356 |
| 45 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +82 | 165368 |
| 46 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +81 | 258605 |
| 47 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +81 | 95276 |
| 48 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +81 | 36267 |
| 49 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +80 | 94806 |
| 50 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +79 | 124257 |
