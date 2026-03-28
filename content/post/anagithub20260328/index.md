---
title: "2026-03-28 GitHub增长趋势报告"
description: "1.last30days-skill+226 2.paperclip+186 3.claude-howto+177 4.onyx+113 5.learn-claude-code+112"
date: 2026-03-28T20:34:17+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-28 20:34:17

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
        'daily': {"categories": ["MiniMax-AI/skills", "koala73/worldmonitor", "twentyhq/twenty", "ruvnet/ruflo", "davidmonterocrespo24/velxio", "microsoft/VibeVoice", "666ghj/MiroFish", "virattt/dexter", "NousResearch/hermes-agent", "gsd-build/get-shit-done", "datalab-to/chandra", "Crosstalk-Solutions/project-nomad", "microsoft/RustTraining", "msitarzewski/agency-agents", "Yeachan-Heo/oh-my-claudecode", "shareAI-lab/learn-claude-code", "onyx-dot-app/onyx", "luongnv89/claude-howto", "paperclipai/paperclip", "mvanhorn/last30days-skill"], "data": [55, 55, 64, 72, 72, 75, 77, 79, 80, 86, 89, 92, 97, 106, 107, 112, 113, 177, 186, 226]},
        'weekly': {"categories": ["jackwener/opencli", "anthropics/skills", "Lum1104/Understand-Anything", "nextlevelbuilder/ui-ux-pro-max-skill", "shareAI-lab/learn-claude-code", "Donchitos/Claude-Code-Game-Studios", "mvanhorn/last30days-skill", "gsd-build/get-shit-done", "pascalorg/editor", "666ghj/MiroFish", "MiniMax-AI/skills", "microsoft/RustTraining", "msitarzewski/agency-agents", "TauricResearch/TradingAgents", "FujiwaraChoki/MoneyPrinterV2", "karpathy/autoresearch", "Crosstalk-Solutions/project-nomad", "obra/superpowers", "bytedance/deer-flow", "affaan-m/everything-claude-code"], "data": [752, 840, 844, 854, 897, 916, 964, 977, 1026, 1042, 1048, 1144, 1189, 1355, 1667, 1918, 2127, 2550, 2653, 3260]},
        'monthly': {"categories": ["D4Vinci/Scrapling", "shanraisshan/claude-code-best-practice", "hesamsheikh/awesome-openclaw-usecases", "anomalyco/opencode", "gsd-build/get-shit-done", "moeru-ai/airi", "shareAI-lab/learn-claude-code", "VoltAgent/awesome-openclaw-skills", "bytedance/deer-flow", "googleworkspace/cli", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3201, 3472, 3701, 3899, 4096, 4122, 4303, 4412, 4782, 4895, 5079, 6067, 7327, 7593, 8342, 9903, 11412, 11649, 12428, 23104]}
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



### 🚀 今日 Top 30 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +226 | 13964 |
| 2 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +186 | 36692 |
| 3 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +177 | 4095 |
| 4 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +113 | 19675 |
| 5 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +112 | 41720 |
| 6 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +107 | 14545 |
| 7 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +106 | 64845 |
| 8 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +97 | 11074 |
| 9 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +92 | 19027 |
| 10 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +89 | 7508 |
| 11 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +86 | 43944 |
| 12 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +80 | 15212 |
| 13 | [virattt/dexter](https://github.com/virattt/dexter) | +79 | 20116 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +77 | 44838 |
| 15 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +75 | 25323 |
| 16 | [davidmonterocrespo24/velxio](https://github.com/davidmonterocrespo24/velxio) | +72 | 575 |
| 17 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +72 | 27858 |
| 18 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +64 | 40043 |
| 19 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +55 | 44935 |
| 20 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +55 | 7230 |
| 21 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +55 | 14632 |
| 22 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +53 | 1210 |
| 23 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +53 | 44126 |
| 24 | [jackwener/opencli](https://github.com/jackwener/opencli) | +53 | 8380 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +53 | 34830 |
| 26 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +51 | 30678 |
| 27 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +48 | 26957 |
| 28 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +45 | 7010 |
| 29 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +45 | 1366 |
| 30 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +45 | 25492 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3260 | 51199 |
| 2 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2653 | 51164 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2550 | 60312 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2127 | 19027 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1918 | 59425 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1667 | 26957 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1355 | 30590 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1189 | 64845 |
| 9 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1144 | 11074 |
| 10 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1048 | 7230 |
| 11 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1042 | 44838 |
| 12 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1026 | 7905 |
| 13 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +977 | 43944 |
| 14 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +964 | 13964 |
| 15 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +916 | 7010 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +897 | 41720 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +854 | 34148 |
| 18 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +844 | 6830 |
| 19 | [anthropics/skills](https://github.com/anthropics/skills) | +840 | 74774 |
| 20 | [jackwener/opencli](https://github.com/jackwener/opencli) | +752 | 8380 |
| 21 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +734 | 44126 |
| 22 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +717 | 14632 |
| 23 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +713 | 36692 |
| 24 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +701 | 4806 |
| 25 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +692 | 15212 |
| 26 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +676 | 27858 |
| 27 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +658 | 13828 |
| 28 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +576 | 33616 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +491 | 23269 |
| 30 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +490 | 44935 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +487 | 34830 |
| 32 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +472 | 10116 |
| 33 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +430 | 25546 |
| 34 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +419 | 30678 |
| 35 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +419 | 17450 |
| 36 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +414 | 12938 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +413 | 14351 |
| 38 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +411 | 14545 |
| 39 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +403 | 21937 |
| 40 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +391 | 20101 |
| 41 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +387 | 19675 |
| 42 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +385 | 17840 |
| 43 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +381 | 14727 |
| 44 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +376 | 21529 |
| 45 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +370 | 42707 |
| 46 | [louis-e/arnis](https://github.com/louis-e/arnis) | +361 | 13789 |
| 47 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +360 | 39841 |
| 48 | [hectorvent/floci](https://github.com/hectorvent/floci) | +351 | 1991 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +342 | 35107 |
| 50 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +339 | 28697 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +336 | 33878 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +333 | 26546 |
| 53 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +329 | 31650 |
| 54 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +315 | 14430 |
| 55 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +313 | 21245 |
| 56 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +308 | 9298 |
| 57 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +307 | 12059 |
| 58 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +303 | 17919 |
| 59 | [mattpocock/skills](https://github.com/mattpocock/skills) | +302 | 10696 |
| 60 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +283 | 17157 |
| 61 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +282 | 3894 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +280 | 20879 |
| 63 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +277 | 37330 |
| 64 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +275 | 4095 |
| 65 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +271 | 20371 |
| 66 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +269 | 27969 |
| 67 | [tw93/Mole](https://github.com/tw93/Mole) | +260 | 36870 |
| 68 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +257 | 28110 |
| 69 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +257 | 33563 |
| 70 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +251 | 2070 |
| 71 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +246 | 25274 |
| 72 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +243 | 3747 |
| 73 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +242 | 36743 |
| 74 | [eze-is/web-access](https://github.com/eze-is/web-access) | +242 | 2016 |
| 75 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +235 | 7508 |
| 76 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +232 | 7986 |
| 77 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +225 | 25492 |
| 78 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +221 | 30880 |
| 79 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +215 | 3074 |
| 80 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +213 | 7208 |
| 81 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +212 | 6190 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +211 | 8992 |
| 83 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +207 | 2264 |
| 84 | [virattt/dexter](https://github.com/virattt/dexter) | +204 | 20116 |
| 85 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +204 | 27813 |
| 86 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +198 | 36799 |
| 87 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +196 | 15131 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +195 | 23559 |
| 89 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +193 | 1221 |
| 90 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +191 | 32063 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +188 | 7636 |
| 92 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +183 | 16783 |
| 93 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +181 | 1139 |
| 94 | [cacggghp/vk-turn-proxy](https://github.com/cacggghp/vk-turn-proxy) | +177 | 2319 |
| 95 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +176 | 17631 |
| 96 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +169 | 6512 |
| 97 | [jundot/omlx](https://github.com/jundot/omlx) | +167 | 7303 |
| 98 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +165 | 2934 |
| 99 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +164 | 8457 |
| 100 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +163 | 8307 |
| 101 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +162 | 40043 |
| 102 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +159 | 1071 |
| 103 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +158 | 19675 |
| 104 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +155 | 3053 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +154 | 27468 |
| 106 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +147 | 1251 |
| 107 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +145 | 25807 |
| 108 | [usestrix/strix](https://github.com/usestrix/strix) | +139 | 22527 |
| 109 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +136 | 1257 |
| 110 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +131 | 3169 |
| 111 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +129 | 8750 |
| 112 | [htdt/godogen](https://github.com/htdt/godogen) | +128 | 2250 |
| 113 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +126 | 36800 |
| 114 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +123 | 17524 |
| 115 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +122 | 25323 |
| 116 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +120 | 3927 |
| 117 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +117 | 2892 |
| 118 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +116 | 17299 |
| 119 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +115 | 11759 |
| 120 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +114 | 902 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +23104 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12428 | 64845 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11649 | 59425 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11412 | 51199 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +9903 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8342 | 44126 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7593 | 44838 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7327 | 36692 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6067 | 44935 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5079 | 74774 |
| 11 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4895 | 22883 |
| 12 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4782 | 51164 |
| 13 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4412 | 42707 |
| 14 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4303 | 41720 |
| 15 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4122 | 36057 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4096 | 43944 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3899 | 109881 |
| 18 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3701 | 27813 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3472 | 23269 |
| 20 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3201 | 33563 |
| 21 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3162 | 13546 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3106 | 34148 |
| 23 | [openai/symphony](https://github.com/openai/symphony) | +3063 | 14176 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3044 | 15808 |
| 25 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2987 | 19675 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2967 | 19027 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2919 | 20371 |
| 28 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2823 | 14430 |
| 29 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2695 | 19634 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2624 | 34830 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2620 | 14351 |
| 32 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2561 | 17450 |
| 33 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2543 | 85286 |
| 34 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2533 | 69674 |
| 35 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2494 | 25546 |
| 36 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2442 | 15212 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2412 | 26546 |
| 38 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2383 | 26957 |
| 39 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2331 | 28110 |
| 40 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2286 | 36743 |
| 41 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2256 | 27858 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2220 | 28697 |
| 43 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2181 | 14727 |
| 44 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2103 | 25807 |
| 45 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2089 | 12938 |
| 46 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2083 | 30590 |
| 47 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2057 | 8311 |
| 48 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2045 | 7628 |
| 49 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2041 | 10561 |
| 50 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2026 | 37330 |
| 51 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2023 | 12187 |
| 52 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1988 | 60117 |
| 53 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1987 | 29047 |
| 54 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1980 | 27969 |
| 55 | [github/spec-kit](https://github.com/github/spec-kit) | +1963 | 71722 |
| 56 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1942 | 34774 |
| 57 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1878 | 33878 |
| 58 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1870 | 9449 |
| 59 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1860 | 11760 |
| 60 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1803 | 30678 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1801 | 20879 |
| 62 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1788 | 8307 |
| 63 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1786 | 14632 |
| 64 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1784 | 25492 |
| 65 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1752 | 9129 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1709 | 35107 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1704 | 11035 |
| 68 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1661 | 122870 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1608 | 31650 |
| 70 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1569 | 17631 |
| 71 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1507 | 17919 |
| 72 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1495 | 18677 |
| 73 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1466 | 36800 |
| 74 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1452 | 10696 |
| 75 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1451 | 16539 |
| 76 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1440 | 33616 |
| 77 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1423 | 10116 |
| 78 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1396 | 9298 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1393 | 17157 |
| 80 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1382 | 98536 |
| 81 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1382 | 96919 |
| 82 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1357 | 15131 |
| 83 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1352 | 8380 |
| 84 | [tw93/Mole](https://github.com/tw93/Mole) | +1333 | 36870 |
| 85 | [openai/skills](https://github.com/openai/skills) | +1330 | 15607 |
| 86 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1297 | 43973 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1291 | 8992 |
| 88 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1239 | 13964 |
| 89 | [jundot/omlx](https://github.com/jundot/omlx) | +1223 | 7303 |
| 90 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1221 | 26505 |
| 91 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1190 | 87598 |
| 92 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1183 | 6830 |
| 93 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1178 | 17840 |
| 94 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1158 | 7986 |
| 95 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1154 | 78902 |
| 96 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1144 | 11074 |
| 97 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1121 | 7208 |
| 98 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1118 | 14545 |
| 99 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1071 | 7230 |
| 100 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1068 | 7905 |
| 101 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1042 | 13828 |
| 102 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1025 | 7010 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +986 | 7636 |
| 104 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +924 | 52700 |
| 105 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +892 | 35735 |
| 106 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +891 | 17299 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +882 | 23165 |
| 108 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +853 | 7426 |
| 109 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +833 | 4358 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +825 | 27468 |
| 111 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +813 | 21529 |
| 112 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +782 | 37564 |
| 113 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +774 | 45886 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +760 | 6512 |
| 115 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +753 | 28883 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +744 | 36799 |
| 117 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +743 | 3414 |
| 118 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +738 | 6865 |
| 119 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +737 | 39841 |
| 120 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +704 | 21937 |
| 121 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +701 | 4806 |
| 122 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +653 | 3795 |
| 123 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +652 | 3599 |
| 124 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +649 | 3894 |
| 125 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +635 | 3675 |
| 126 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +629 | 15804 |
| 127 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +620 | 47936 |
| 128 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +611 | 4318 |
| 129 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +610 | 2221 |
| 130 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +594 | 14408 |
| 131 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +590 | 2271 |
| 132 | [wshobson/agents](https://github.com/wshobson/agents) | +589 | 32456 |
| 133 | [huggingface/skills](https://github.com/huggingface/skills) | +566 | 9951 |
| 134 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +559 | 7023 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +553 | 8750 |
| 136 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +546 | 3747 |
| 137 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +535 | 2634 |
| 138 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +531 | 47122 |
| 139 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +530 | 17524 |
| 140 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +523 | 4578 |
| 141 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +521 | 23734 |
| 142 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +518 | 2892 |
| 143 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +516 | 24018 |
| 144 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +513 | 1906 |
| 145 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +510 | 44232 |
| 146 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +509 | 3327 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +497 | 44545 |
| 148 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +491 | 27772 |
| 149 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +484 | 10622 |
| 150 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +482 | 2639 |
| 151 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +469 | 2314 |
| 152 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +459 | 2098 |
| 153 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +449 | 10581 |
| 154 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +446 | 14725 |
| 155 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +432 | 7259 |
| 156 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +423 | 3530 |
| 157 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +412 | 3435 |
| 158 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +412 | 22965 |
| 159 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +392 | 30880 |
| 160 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +392 | 1891 |
| 161 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +390 | 2659 |
| 162 | [openclaw/skills](https://github.com/openclaw/skills) | +389 | 3536 |
| 163 | [apify/agent-skills](https://github.com/apify/agent-skills) | +388 | 1767 |
| 164 | [htdt/godogen](https://github.com/htdt/godogen) | +383 | 2250 |
| 165 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +364 | 13333 |
| 166 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +359 | 6376 |
| 167 | [aden-hive/hive](https://github.com/aden-hive/hive) | +354 | 9901 |
| 168 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +354 | 8457 |
| 169 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +354 | 2116 |
| 170 | [hectorvent/floci](https://github.com/hectorvent/floci) | +353 | 1991 |
| 171 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +348 | 1700 |
| 172 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +346 | 10234 |
| 173 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +341 | 33712 |
| 174 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +338 | 6928 |
| 175 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +336 | 1886 |
| 176 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +332 | 1735 |
| 177 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +330 | 3633 |
| 178 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +328 | 3792 |
| 179 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +324 | 3670 |
| 180 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +320 | 2271 |
| 181 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +315 | 1392 |
| 182 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +307 | 1673 |
| 183 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +307 | 4691 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +294 | 24923 |
| 185 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +293 | 1436 |
| 186 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +286 | 4096 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +283 | 10819 |
| 188 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +267 | 1792 |
| 189 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +264 | 29780 |
| 190 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +252 | 13665 |
| 191 | [eze-is/web-access](https://github.com/eze-is/web-access) | +244 | 2016 |
| 192 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +241 | 14828 |
| 193 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +237 | 1251 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +227 | 4063 |
| 195 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +213 | 21988 |
| 196 | [usebruno/bruno](https://github.com/usebruno/bruno) | +204 | 41086 |
| 197 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +200 | 1096 |
| 198 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +199 | 5670 |
| 199 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +198 | 36103 |
| 200 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +196 | 868 |
| 201 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +193 | 1789 |
| 202 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +191 | 0 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +190 | 21639 |
| 204 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +190 | 7436 |
| 205 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +189 | 803 |
| 206 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +186 | 1569 |
| 207 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +178 | 1031 |
| 208 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +176 | 8952 |
| 209 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +168 | 1024 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +163 | 1352 |
| 211 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +163 | 957 |
| 212 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +159 | 2481 |
| 213 | [linlay/zenmind](https://github.com/linlay/zenmind) | +158 | 233 |
| 214 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +158 | 25397 |
| 215 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +151 | 1590 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +150 | 29142 |
| 217 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +148 | 2462 |
| 218 | [es617/claude-replay](https://github.com/es617/claude-replay) | +146 | 579 |
| 219 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +145 | 2250 |
| 220 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +144 | 40265 |
| 221 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +136 | 2602 |
| 222 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +135 | 1690 |
| 223 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +134 | 5347 |
| 224 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +133 | 527 |
| 225 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +133 | 673 |
| 226 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +130 | 35473 |
| 227 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +129 | 986 |
| 228 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +129 | 1273 |
| 229 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +128 | 1943 |
| 230 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +125 | 2504 |
| 231 | [4ier/neo](https://github.com/4ier/neo) | +121 | 640 |
| 232 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +119 | 13799 |
| 233 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +118 | 897 |
| 234 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +117 | 473 |
| 235 | [robinebers/openusage](https://github.com/robinebers/openusage) | +117 | 1633 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +116 | 2229 |
| 237 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10036 |
| 238 | [mauriceboe/NOMAD](https://github.com/mauriceboe/NOMAD) | +115 | 1360 |
| 239 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +110 | 719 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +110 | 26261 |
| 241 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +109 | 12332 |
| 242 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +109 | 1789 |
| 243 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 452 |
| 244 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +107 | 1331 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +105 | 33000 |
| 246 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +104 | 1468 |
| 247 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +104 | 10344 |
| 248 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 249 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 603 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +101 | 48784 |
| 251 | [skylot/jadx](https://github.com/skylot/jadx) | +101 | 47365 |
| 252 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 439 |
| 253 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 577 |
| 254 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +100 | 22960 |
| 255 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +96 | 1383 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +95 | 12728 |
| 257 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +91 | 500 |
| 258 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +91 | 11350 |
| 259 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +90 | 724 |
| 260 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +89 | 537 |
| 261 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +89 | 1469 |
| 262 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +89 | 8981 |
| 263 | [dashersw/gea](https://github.com/dashersw/gea) | +88 | 721 |
| 264 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 265 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +87 | 404 |
| 266 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +85 | 851 |
| 267 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +85 | 932 |
| 268 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +83 | 1038 |
| 269 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +83 | 648 |
| 270 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +81 | 3292 |
| 271 | [idinging/freemail](https://github.com/idinging/freemail) | +80 | 1172 |
| 272 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +79 | 449 |
| 273 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +78 | 655 |
| 274 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +78 | 672 |
| 275 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +77 | 419 |
| 276 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +77 | 422 |
| 277 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +76 | 805 |
| 278 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +73 | 385 |
| 279 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +73 | 3404 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +73 | 27061 |
| 281 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +72 | 935 |
| 282 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +71 | 3640 |
| 283 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +68 | 527 |
| 284 | [Kylsky/chatgpt-team-helper](https://github.com/Kylsky/chatgpt-team-helper) | +68 | 1030 |
| 285 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +68 | 37313 |
| 286 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +67 | 585 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +66 | 8332 |
| 288 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +66 | 12463 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1541 |
| 290 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +64 | 3171 |
| 291 | [apache/kafka](https://github.com/apache/kafka) | +64 | 32043 |
| 292 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +62 | 336 |
| 293 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +61 | 45263 |
| 294 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +60 | 7117 |
| 295 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +60 | 1594 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +60 | 31476 |
| 297 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +60 | 7706 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +59 | 1413 |
| 299 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +56 | 350 |
| 300 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +56 | 11602 |
