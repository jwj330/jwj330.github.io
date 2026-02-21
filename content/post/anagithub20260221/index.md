---
title: "GitHub 趋势报告 2026-02-21"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-21T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-21 20:28:17

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
        'daily': {"categories": ["x1xhlol/system-prompts-and-models-of-ai-tools", "PostHog/posthog", "ashishps1/awesome-system-design-resources", "bmad-code-org/BMAD-METHOD", "thedotmack/claude-mem", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "ComposioHQ/awesome-claude-skills", "tw93/Mole", "nextlevelbuilder/ui-ux-pro-max-skill", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "affaan-m/everything-claude-code", "sindresorhus/awesome", "f/prompts.chat", "daytonaio/daytona", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "openclaw/openclaw"], "data": [183, 193, 194, 229, 234, 234, 235, 253, 269, 275, 303, 313, 322, 323, 405, 422, 447, 448, 759, 1978]},
        'weekly': {"categories": ["tw93/Mole", "bmad-code-org/BMAD-METHOD", "github/spec-kit", "code-yeongyu/oh-my-opencode", "Shubhamsaboo/awesome-llm-apps", "anthropics/claude-code", "ComposioHQ/awesome-claude-skills", "sindresorhus/awesome", "codecrafters-io/build-your-own-x", "firecrawl/firecrawl", "nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/skills", "daytonaio/daytona", "affaan-m/everything-claude-code", "ashishps1/awesome-system-design-resources", "anomalyco/opencode", "Developer-Y/cs-video-courses", "obra/superpowers", "openclaw/openclaw", "thedotmack/claude-mem"], "data": [1273, 1280, 1297, 1391, 1430, 1504, 1650, 1794, 1806, 2003, 2051, 3019, 3052, 3108, 3239, 3536, 3661, 5365, 21903, 29785]},
        'monthly': {"categories": ["sindresorhus/awesome", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "daytonaio/daytona", "anthropics/skills", "obra/superpowers", "anomalyco/opencode", "thedotmack/claude-mem", "TauricResearch/TradingAgents", "patchy631/ai-engineering-hub", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "google/langextract", "ComposioHQ/awesome-claude-skills", "remotion-dev/remotion", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [7917, 8335, 8902, 9776, 23449, 23576, 24330, 29785, 30296, 30370, 30854, 31068, 32389, 32815, 33276, 33433, 36455, 37485, 49044, 216012]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +1978 | 216012 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +759 | 56885 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +448 | 108072 |
| 4 | [anthropics/skills](https://github.com/anthropics/skills) | +447 | 72823 |
| 5 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +422 | 59226 |
| 6 | [f/prompts.chat](https://github.com/f/prompts.chat) | +405 | 146221 |
| 7 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +323 | 439223 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +322 | 49044 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +313 | 68323 |
| 10 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +303 | 467743 |
| 11 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +275 | 33276 |
| 12 | [tw93/Mole](https://github.com/tw93/Mole) | +269 | 35964 |
| 13 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +253 | 36455 |
| 14 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +235 | 84476 |
| 15 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +234 | 32815 |
| 16 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +234 | 29785 |
| 17 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +229 | 36884 |
| 18 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +194 | 33441 |
| 19 | [PostHog/posthog](https://github.com/PostHog/posthog) | +193 | 31695 |
| 20 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +183 | 115506 |
| 21 | [github/spec-kit](https://github.com/github/spec-kit) | +182 | 70993 |
| 22 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +180 | 74379 |
| 23 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +175 | 148461 |
| 24 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +142 | 175666 |
| 25 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +141 | 147920 |
| 26 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +140 | 96424 |
| 27 | [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | +136 | 40441 |
| 28 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +130 | 274426 |
| 29 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +125 | 87464 |
| 30 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +125 | 37485 |
| 31 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +124 | 283958 |
| 32 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +124 | 32389 |
| 33 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +120 | 207184 |
| 34 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +120 | 51843 |
| 35 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +114 | 95187 |
| 36 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +107 | 97929 |
| 37 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +103 | 336091 |
| 38 | [openai/codex](https://github.com/openai/codex) | +100 | 61317 |
| 39 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +98 | 399387 |
| 40 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +93 | 60631 |
| 41 | [upstash/context7](https://github.com/upstash/context7) | +90 | 46418 |
| 42 | [torvalds/linux](https://github.com/torvalds/linux) | +89 | 218149 |
| 43 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | +89 | 81283 |
| 44 | [immich-app/immich](https://github.com/immich-app/immich) | +85 | 93083 |
| 45 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | +85 | 32162 |
| 46 | [docling-project/docling](https://github.com/docling-project/docling) | +84 | 53763 |
| 47 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +83 | 30370 |
| 48 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +80 | 103795 |
| 49 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +79 | 165687 |
| 50 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +78 | 95546 |
