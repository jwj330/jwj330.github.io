---
title: "2026-03-21 GitHub增长趋势报告"
description: "1.autoresearch+531 2.project-nomad+386 3.agency-agents+329 4.TradingAgents+290 5.skills+283"
date: 2026-03-21T20:29:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-21 20:29:54

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
        'daily': {"categories": ["langchain-ai/open-swe", "jackwener/opencli", "volcengine/OpenViking", "EverMind-AI/MSA", "THU-MAIC/OpenMAIC", "lightpanda-io/browser", "paperclipai/paperclip", "lucija8320nhung4/HacxGPT", "louis-e/arnis", "shareAI-lab/learn-claude-code", "gsd-build/get-shit-done", "alibaba/page-agent", "666ghj/MiroFish", "opendataloader-project/opendataloader-pdf", "jarrodwatts/claude-hud", "mattpocock/skills", "TauricResearch/TradingAgents", "msitarzewski/agency-agents", "Crosstalk-Solutions/project-nomad", "karpathy/autoresearch"], "data": [116, 120, 123, 127, 131, 133, 133, 134, 147, 161, 186, 193, 234, 241, 249, 283, 290, 329, 386, 531]},
        'weekly': {"categories": ["alibaba/page-agent", "jarrodwatts/claude-hud", "langchain-ai/deepagents", "nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/skills", "abhigyanpatwari/GitNexus", "aiming-lab/AutoResearchClaw", "mattpocock/skills", "lightpanda-io/browser", "gsd-build/get-shit-done", "paperclipai/paperclip", "shareAI-lab/learn-claude-code", "volcengine/OpenViking", "THU-MAIC/OpenMAIC", "karpathy/autoresearch", "666ghj/MiroFish", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw", "obra/superpowers"], "data": [930, 968, 1007, 1009, 1043, 1045, 1093, 1108, 1370, 1383, 1561, 1607, 1641, 1689, 2765, 2955, 3049, 3198, 3353, 3598]},
        'monthly': {"categories": ["RightNow-AI/openfang", "abhigyanpatwari/GitNexus", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "x1xhlol/system-prompts-and-models-of-ai-tools", "googleworkspace/cli", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "666ghj/MiroFish", "paperclipai/paperclip", "koala73/worldmonitor", "ruvnet/RuView", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4072, 4200, 4325, 4513, 4567, 4605, 4744, 5270, 5466, 5514, 6096, 6598, 6628, 7678, 8443, 9689, 9776, 9855, 11290, 28465]}
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
| 1 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +531 | 47912 |
| 2 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +386 | 6241 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +329 | 58087 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +290 | 30590 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +283 | 8646 |
| 6 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +249 | 10324 |
| 7 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +241 | 7787 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +234 | 38198 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +193 | 12974 |
| 10 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +186 | 37918 |
| 11 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +161 | 35228 |
| 12 | [louis-e/arnis](https://github.com/louis-e/arnis) | +147 | 12127 |
| 13 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +134 | 906 |
| 14 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +133 | 31088 |
| 15 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +133 | 23203 |
| 16 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +131 | 10606 |
| 17 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +127 | 1431 |
| 18 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +123 | 17437 |
| 19 | [jackwener/opencli](https://github.com/jackwener/opencli) | +120 | 3573 |
| 20 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +116 | 7903 |
| 21 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +115 | 916 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +115 | 19918 |
| 23 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +115 | 42123 |
| 24 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +114 | 19344 |
| 25 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +112 | 542 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +112 | 34148 |
| 27 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +111 | 2183 |
| 28 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +109 | 24092 |
| 29 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +108 | 11854 |
| 30 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +108 | 13904 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | +3598 | 60312 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3353 | 224760 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3198 | 58087 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3049 | 51199 |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2955 | 38198 |
| 6 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2765 | 47912 |
| 7 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1689 | 10606 |
| 8 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1641 | 17437 |
| 9 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1607 | 35228 |
| 10 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1561 | 31088 |
| 11 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1383 | 37918 |
| 12 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1370 | 23203 |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1108 | 8646 |
| 14 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1093 | 7337 |
| 15 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1045 | 18562 |
| 16 | [anthropics/skills](https://github.com/anthropics/skills) | +1043 | 74774 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1009 | 34148 |
| 18 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1007 | 16298 |
| 19 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +968 | 10324 |
| 20 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +930 | 12975 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +919 | 19918 |
| 22 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +912 | 5997 |
| 23 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +907 | 7787 |
| 24 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +804 | 6241 |
| 25 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +794 | 24092 |
| 26 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +775 | 42123 |
| 27 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +758 | 11262 |
| 28 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +745 | 11854 |
| 29 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +701 | 16322 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +684 | 30678 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +655 | 31406 |
| 32 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +641 | 11738 |
| 33 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +616 | 40453 |
| 34 | [jackwener/opencli](https://github.com/jackwener/opencli) | +610 | 3573 |
| 35 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +608 | 3580 |
| 36 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +607 | 13904 |
| 37 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +567 | 26613 |
| 38 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +536 | 2823 |
| 39 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +535 | 5831 |
| 40 | [tw93/Mole](https://github.com/tw93/Mole) | +534 | 36870 |
| 41 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +532 | 3094 |
| 42 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +521 | 3466 |
| 43 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +516 | 30590 |
| 44 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +516 | 18873 |
| 45 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +516 | 37330 |
| 46 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +493 | 9729 |
| 47 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +491 | 38791 |
| 48 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +489 | 18005 |
| 49 | [louis-e/arnis](https://github.com/louis-e/arnis) | +456 | 12127 |
| 50 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +454 | 32896 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +436 | 33878 |
| 52 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +422 | 7903 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +421 | 7512 |
| 54 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +418 | 31673 |
| 55 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +418 | 23818 |
| 56 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +409 | 24719 |
| 57 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +409 | 35308 |
| 58 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +398 | 26327 |
| 59 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +394 | 2403 |
| 60 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +385 | 12887 |
| 61 | [voidzero-dev/vite-plus](https://github.com/voidzero-dev/vite-plus) | +380 | 3174 |
| 62 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +378 | 23990 |
| 63 | [jundot/omlx](https://github.com/jundot/omlx) | +377 | 6301 |
| 64 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +373 | 2356 |
| 65 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +367 | 26595 |
| 66 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +365 | 26355 |
| 67 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +358 | 32454 |
| 68 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +355 | 4968 |
| 69 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +352 | 43973 |
| 70 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +349 | 18272 |
| 71 | [novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket) | +346 | 2065 |
| 72 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +345 | 6482 |
| 73 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +345 | 35029 |
| 74 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +343 | 3076 |
| 75 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +338 | 29184 |
| 76 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +327 | 2988 |
| 77 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +326 | 1943 |
| 78 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +323 | 19344 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +319 | 15259 |
| 80 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +318 | 2610 |
| 81 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +316 | 8728 |
| 82 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +314 | 36210 |
| 83 | [Narcooo/inkos](https://github.com/Narcooo/inkos) | +309 | 1977 |
| 84 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +309 | 30664 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +307 | 22310 |
| 86 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +306 | 21903 |
| 87 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +303 | 28593 |
| 88 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +302 | 2363 |
| 89 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +299 | 1708 |
| 90 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +295 | 1349 |
| 91 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +291 | 7371 |
| 92 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +286 | 5584 |
| 93 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +286 | 28272 |
| 94 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +280 | 17512 |
| 95 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +276 | 15407 |
| 96 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +274 | 29730 |
| 97 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +270 | 4420 |
| 98 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +265 | 22254 |
| 99 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +256 | 1964 |
| 100 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +241 | 2177 |
| 101 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +241 | 10225 |
| 102 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +239 | 14442 |
| 103 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +234 | 1431 |
| 104 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +234 | 3476 |
| 105 | [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | +232 | 1660 |
| 106 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +228 | 12804 |
| 107 | [htdt/godogen](https://github.com/htdt/godogen) | +227 | 1621 |
| 108 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +225 | 3261 |
| 109 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +222 | 8948 |
| 110 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +221 | 1586 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +220 | 6174 |
| 112 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +214 | 35735 |
| 113 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +213 | 1395 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +210 | 6679 |
| 115 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +208 | 2265 |
| 116 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +197 | 10118 |
| 117 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +195 | 22502 |
| 118 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +188 | 906 |
| 119 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +188 | 26353 |
| 120 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +185 | 16530 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +28465 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +11290 | 58087 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +9855 | 60312 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +9776 | 47912 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9689 | 51199 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8443 | 38791 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7678 | 42123 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6628 | 31088 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6598 | 38198 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +6096 | 74774 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5514 | 26595 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5466 | 40453 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5270 | 31673 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4744 | 21903 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4605 | 122870 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4567 | 109881 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4513 | 37918 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4325 | 35029 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4200 | 18562 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4072 | 15171 |
| 21 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4002 | 18272 |
| 22 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3971 | 35228 |
| 23 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +3872 | 24719 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3787 | 19919 |
| 25 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3411 | 12887 |
| 26 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +3351 | 28272 |
| 27 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3252 | 35308 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3102 | 69674 |
| 29 | [openai/symphony](https://github.com/openai/symphony) | +2994 | 13707 |
| 30 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2967 | 26355 |
| 31 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2921 | 17437 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2894 | 34148 |
| 33 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2892 | 26613 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2837 | 31406 |
| 35 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2748 | 32454 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2747 | 24092 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2684 | 9929 |
| 38 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2582 | 85286 |
| 39 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2539 | 12975 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2426 | 10225 |
| 41 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2395 | 37330 |
| 42 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2365 | 60117 |
| 43 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2297 | 34172 |
| 44 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2289 | 33878 |
| 45 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2234 | 11854 |
| 46 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +2224 | 25709 |
| 47 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2190 | 10703 |
| 48 | [huggingface/skills](https://github.com/huggingface/skills) | +2187 | 9574 |
| 49 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2092 | 23203 |
| 50 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2088 | 26327 |
| 51 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2067 | 22254 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2023 | 147486 |
| 53 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2022 | 23990 |
| 54 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2017 | 10630 |
| 55 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2005 | 11738 |
| 56 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2001 | 9729 |
| 57 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2001 | 30678 |
| 58 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1994 | 7888 |
| 59 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1949 | 8948 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1945 | 6918 |
| 61 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1897 | 10735 |
| 62 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1893 | 29184 |
| 63 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1844 | 11262 |
| 64 | [github/spec-kit](https://github.com/github/spec-kit) | +1836 | 71722 |
| 65 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1826 | 18873 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1791 | 32896 |
| 67 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1704 | 96919 |
| 68 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1698 | 7027 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1692 | 16322 |
| 70 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1691 | 10606 |
| 71 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1691 | 8728 |
| 72 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1671 | 22502 |
| 73 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1634 | 7371 |
| 74 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1621 | 6491 |
| 75 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1612 | 13898 |
| 76 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1566 | 98536 |
| 77 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1553 | 15746 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1539 | 13413 |
| 79 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1528 | 149018 |
| 80 | [tw93/Mole](https://github.com/tw93/Mole) | +1527 | 36870 |
| 81 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1516 | 8041 |
| 82 | [openai/skills](https://github.com/openai/skills) | +1482 | 14835 |
| 83 | [tobi/qmd](https://github.com/tobi/qmd) | +1480 | 16392 |
| 84 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1442 | 7644 |
| 85 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1430 | 14126 |
| 86 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1414 | 18005 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1413 | 15259 |
| 88 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1413 | 13063 |
| 89 | [maderix/ANE](https://github.com/maderix/ANE) | +1388 | 6380 |
| 90 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1369 | 36210 |
| 91 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1367 | 5767 |
| 92 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1344 | 13904 |
| 93 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1289 | 8646 |
| 94 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1287 | 43973 |
| 95 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1284 | 16298 |
| 96 | [openai/codex](https://github.com/openai/codex) | +1270 | 61744 |
| 97 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1252 | 5551 |
| 98 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1197 | 7787 |
| 99 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1191 | 7512 |
| 100 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1167 | 10324 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1157 | 29730 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1137 | 16530 |
| 103 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1135 | 37564 |
| 104 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1107 | 87598 |
| 105 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1094 | 7338 |
| 106 | [jundot/omlx](https://github.com/jundot/omlx) | +1071 | 6301 |
| 107 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +988 | 6679 |
| 108 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +986 | 30590 |
| 109 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +937 | 13100 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +930 | 35735 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +918 | 26353 |
| 112 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +915 | 7106 |
| 113 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +913 | 5997 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +833 | 6174 |
| 115 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +826 | 52700 |
| 116 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +802 | 13809 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +792 | 45886 |
| 118 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +790 | 7487 |
| 119 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +778 | 61818 |
| 120 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +772 | 36799 |
| 121 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +760 | 17513 |
| 122 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +751 | 47122 |
| 123 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +743 | 9964 |
| 124 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +739 | 28593 |
| 125 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +726 | 6482 |
| 126 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +718 | 3234 |
| 127 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +690 | 5584 |
| 128 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +682 | 4399 |
| 129 | [wshobson/agents](https://github.com/wshobson/agents) | +675 | 31910 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +647 | 15714 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +643 | 47936 |
| 132 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +640 | 3476 |
| 133 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +631 | 23528 |
| 134 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +619 | 3580 |
| 135 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +619 | 2165 |
| 136 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +615 | 6254 |
| 137 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +597 | 2127 |
| 138 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +590 | 16714 |
| 139 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +581 | 23321 |
| 140 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +580 | 22851 |
| 141 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +569 | 2560 |
| 142 | [docling-project/docling](https://github.com/docling-project/docling) | +564 | 54041 |
| 143 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +562 | 3553 |
| 144 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +556 | 10118 |
| 145 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +548 | 44232 |
| 146 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +538 | 2988 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +533 | 44545 |
| 148 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +524 | 3076 |
| 149 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +518 | 1983 |
| 150 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +510 | 3392 |
| 151 | [eooce/python-ws](https://github.com/eooce/python-ws) | +493 | 1889 |
| 152 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +491 | 2356 |
| 153 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +491 | 18388 |
| 154 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +490 | 1984 |
| 155 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +485 | 27073 |
| 156 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +483 | 8089 |
| 157 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +482 | 39841 |
| 158 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +478 | 33712 |
| 159 | [aden-hive/hive](https://github.com/aden-hive/hive) | +472 | 9748 |
| 160 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +452 | 2005 |
| 161 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +450 | 14442 |
| 162 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +449 | 12804 |
| 163 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +449 | 6165 |
| 164 | [openclaw/skills](https://github.com/openclaw/skills) | +440 | 3206 |
| 165 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +437 | 14592 |
| 166 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +433 | 7903 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +429 | 19354 |
| 168 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +416 | 9926 |
| 169 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +408 | 9809 |
| 170 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +405 | 1591 |
| 171 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +404 | 1669 |
| 172 | [apify/agent-skills](https://github.com/apify/agent-skills) | +402 | 1705 |
| 173 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +401 | 2265 |
| 174 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +393 | 1964 |
| 175 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +385 | 7582 |
| 176 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +379 | 2398 |
| 177 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +373 | 3330 |
| 178 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +355 | 10507 |
| 179 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +354 | 6275 |
| 180 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +349 | 3580 |
| 181 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +344 | 2942 |
| 182 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +338 | 1640 |
| 183 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +335 | 1494 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +327 | 24657 |
| 185 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +320 | 0 |
| 186 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +318 | 4142 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +310 | 10465 |
| 188 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +308 | 1349 |
| 189 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +307 | 2363 |
| 190 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +306 | 1469 |
| 191 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +301 | 1339 |
| 192 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +297 | 3261 |
| 193 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +297 | 13500 |
| 194 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +283 | 29780 |
| 195 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +279 | 1586 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +273 | 3786 |
| 197 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +260 | 21753 |
| 198 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +255 | 1545 |
| 199 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +252 | 36103 |
| 200 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +243 | 1104 |
| 201 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +232 | 961 |
| 202 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +232 | 21432 |
| 203 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +225 | 2401 |
| 204 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +225 | 963 |
| 205 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 145 |
| 206 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +202 | 7214 |
| 207 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +199 | 5316 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +197 | 41086 |
| 209 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +194 | 1423 |
| 210 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +193 | 8960 |
| 211 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +188 | 29013 |
| 212 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +186 | 669 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +184 | 40265 |
| 214 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +178 | 8878 |
| 215 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +177 | 25379 |
| 216 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +171 | 1609 |
| 217 | [linlay/zenmind](https://github.com/linlay/zenmind) | +169 | 289 |
| 218 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +167 | 1276 |
| 219 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +166 | 967 |
| 220 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +165 | 764 |
| 221 | [decolua/9router](https://github.com/decolua/9router) | +158 | 1135 |
| 222 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +158 | 2460 |
| 223 | [jgraph/drawio](https://github.com/jgraph/drawio) | +155 | 4276 |
| 224 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +154 | 922 |
| 225 | [robinebers/openusage](https://github.com/robinebers/openusage) | +154 | 1571 |
| 226 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +154 | 791 |
| 227 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +154 | 2637 |
| 228 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +146 | 1435 |
| 229 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +145 | 2061 |
| 230 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +143 | 2117 |
| 231 | [es617/claude-replay](https://github.com/es617/claude-replay) | +141 | 558 |
| 232 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +141 | 5223 |
| 233 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +140 | 1190 |
| 234 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +137 | 708 |
| 235 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +136 | 22832 |
| 236 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +132 | 35473 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +132 | 33000 |
| 238 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +130 | 1701 |
| 239 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +130 | 687 |
| 240 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +125 | 505 |
| 241 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +125 | 909 |
| 242 | [4ier/neo](https://github.com/4ier/neo) | +124 | 625 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +124 | 26038 |
| 244 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +123 | 669 |
| 245 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +121 | 2332 |
| 246 | [is-a-dev/register](https://github.com/is-a-dev/register) | +119 | 10005 |
| 247 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +119 | 13734 |
| 248 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +119 | 485 |
| 249 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +117 | 12223 |
| 250 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +115 | 432 |
| 251 | [fmhy/edit](https://github.com/fmhy/edit) | +115 | 8628 |
| 252 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +114 | 48784 |
| 253 | [qist/tvbox](https://github.com/qist/tvbox) | +112 | 8568 |
| 254 | [microg/GmsCore](https://github.com/microg/GmsCore) | +110 | 12646 |
| 255 | [skylot/jadx](https://github.com/skylot/jadx) | +106 | 47365 |
| 256 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +105 | 3547 |
| 257 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +105 | 8848 |
| 258 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +105 | 10142 |
| 259 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +104 | 431 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +104 | 1089 |
| 261 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +101 | 3302 |
| 263 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +101 | 1343 |
| 264 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +100 | 3216 |
| 265 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +98 | 11215 |
| 266 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +96 | 486 |
| 267 | [lklynet/aurral](https://github.com/lklynet/aurral) | +96 | 880 |
| 268 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +96 | 595 |
| 269 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +95 | 972 |
| 270 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 902 |
| 271 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +94 | 537 |
| 272 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +94 | 638 |
| 273 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +94 | 37313 |
| 274 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +92 | 469 |
| 275 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +91 | 875 |
| 276 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +90 | 517 |
| 277 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +90 | 1039 |
| 278 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +89 | 814 |
| 279 | [silships/figma-cli](https://github.com/silships/figma-cli) | +89 | 457 |
| 280 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +85 | 609 |
| 281 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +85 | 404 |
| 282 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +85 | 498 |
| 283 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +84 | 7061 |
| 284 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +84 | 3080 |
| 285 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +81 | 26977 |
| 286 | [idinging/freemail](https://github.com/idinging/freemail) | +80 | 1090 |
| 287 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +80 | 870 |
| 288 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +74 | 272 |
| 289 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +73 | 21397 |
| 290 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +72 | 451 |
| 291 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +72 | 8254 |
| 292 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +70 | 395 |
| 293 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +70 | 6113 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +69 | 1362 |
| 295 | [apache/kafka](https://github.com/apache/kafka) | +69 | 32043 |
| 296 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +68 | 1015 |
| 297 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +65 | 918 |
| 298 | [Widdit/now-playing-service](https://github.com/Widdit/now-playing-service) | +64 | 531 |
| 299 | [freeok/so-novel](https://github.com/freeok/so-novel) | +63 | 6392 |
| 300 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +63 | 12409 |
