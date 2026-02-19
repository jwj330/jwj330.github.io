---
title: "GitHub 趋势报告 2026-02-19"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-19T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-19 20:36:40

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
        'daily': {"categories": ["bmad-code-org/BMAD-METHOD", "public-apis/public-apis", "n8n-io/n8n", "anthropics/claude-code", "awesome-selfhosted/awesome-selfhosted", "vinta/awesome-python", "github/spec-kit", "ComposioHQ/awesome-claude-skills", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "firecrawl/firecrawl", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "Developer-Y/cs-video-courses", "obra/superpowers", "daytonaio/daytona", "openclaw/openclaw"], "data": [193, 199, 204, 207, 211, 217, 218, 247, 271, 273, 298, 315, 343, 469, 477, 507, 726, 905, 953, 3136]},
        'weekly': {"categories": ["awesome-selfhosted/awesome-selfhosted", "github/spec-kit", "anthropics/claude-code", "code-yeongyu/oh-my-opencode", "ComposioHQ/awesome-claude-skills", "sindresorhus/awesome", "Shubhamsaboo/awesome-llm-apps", "codecrafters-io/build-your-own-x", "nextlevelbuilder/ui-ux-pro-max-skill", "firecrawl/firecrawl", "google/langextract", "daytonaio/daytona", "anthropics/skills", "ashishps1/awesome-system-design-resources", "Developer-Y/cs-video-courses", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw", "patchy631/ai-engineering-hub"], "data": [1144, 1268, 1358, 1372, 1655, 1657, 1787, 1788, 1939, 2020, 2041, 3043, 3145, 3222, 3289, 3348, 3738, 4773, 22831, 30129]},
        'monthly': {"categories": ["codecrafters-io/build-your-own-x", "anthropics/claude-code", "daytonaio/daytona", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "patchy631/ai-engineering-hub", "TauricResearch/TradingAgents", "MHSanaei/3x-ui", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "slatedocs/slate", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8477, 9160, 9996, 24391, 25231, 26766, 30129, 30197, 30550, 30662, 31028, 32125, 32318, 32766, 33284, 35962, 36160, 37220, 48339, 211466]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3136 | 211466 |
| 2 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +953 | 58608 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +905 | 55234 |
| 4 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +726 | 74003 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +507 | 107072 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +477 | 71906 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +469 | 48339 |
| 8 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +343 | 83966 |
| 9 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +315 | 438640 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +298 | 467240 |
| 11 | [google/langextract](https://github.com/google/langextract) | +273 | 33284 |
| 12 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +271 | 32766 |
| 13 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +247 | 35962 |
| 14 | [github/spec-kit](https://github.com/github/spec-kit) | +218 | 70606 |
| 15 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +217 | 283650 |
| 16 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +211 | 274113 |
| 17 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +207 | 67786 |
| 18 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +204 | 175357 |
| 19 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +199 | 399170 |
| 20 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +193 | 36456 |
| 21 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +189 | 96087 |
| 22 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +176 | 206952 |
| 23 | [docling-project/docling](https://github.com/docling-project/docling) | +170 | 53549 |
| 24 | [tw93/Mole](https://github.com/tw93/Mole) | +165 | 35448 |
| 25 | [f/prompts.chat](https://github.com/f/prompts.chat) | +164 | 145602 |
| 26 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +162 | 115204 |
| 27 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +160 | 32318 |
| 28 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +158 | 335887 |
| 29 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +154 | 165522 |
| 30 | [torvalds/linux](https://github.com/torvalds/linux) | +152 | 217969 |
| 31 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +152 | 32125 |
| 32 | [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | +142 | 40277 |
| 33 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +141 | 30129 |
| 34 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | +136 | 117124 |
| 35 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +135 | 37220 |
| 36 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +133 | 70731 |
| 37 | [upstash/context7](https://github.com/upstash/context7) | +132 | 46224 |
| 38 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +130 | 103639 |
| 39 | [openai/codex](https://github.com/openai/codex) | +129 | 61116 |
| 40 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | +124 | 258729 |
| 41 | [immich-app/immich](https://github.com/immich-app/immich) | +120 | 92937 |
| 42 | [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) | +116 | 349401 |
| 43 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +110 | 95386 |
| 44 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +110 | 94916 |
| 45 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | +106 | 126998 |
| 46 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +105 | 148141 |
| 47 | [supabase/supabase](https://github.com/supabase/supabase) | +104 | 97897 |
| 48 | [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | +104 | 72678 |
| 49 | [microsoft/vscode](https://github.com/microsoft/vscode) | +98 | 181904 |
| 50 | [ollama/ollama](https://github.com/ollama/ollama) | +98 | 162955 |
