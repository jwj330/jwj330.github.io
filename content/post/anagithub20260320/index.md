---
title: "2026-03-20 GitHub增长趋势报告"
description: "1.skills+315 2.opendataloader-pdf+298 3.autoresearch+268 4.get-shit-done+234 5.MiroFish+221"
date: 2026-03-20T20:36:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-20 20:36:05

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
        'daily': {"categories": ["langchain-ai/open-swe", "nidhinjs/prompt-master", "volcengine/OpenViking", "farion1231/cc-switch", "FujiwaraChoki/MoneyPrinterV2", "anthropics/claude-plugins-official", "nextlevelbuilder/ui-ux-pro-max-skill", "tw93/Mole", "KittenML/KittenTTS", "paperclipai/paperclip", "louis-e/arnis", "jarrodwatts/claude-hud", "shareAI-lab/learn-claude-code", "THU-MAIC/OpenMAIC", "msitarzewski/agency-agents", "666ghj/MiroFish", "gsd-build/get-shit-done", "karpathy/autoresearch", "opendataloader-project/opendataloader-pdf", "mattpocock/skills"], "data": [103, 104, 106, 107, 109, 110, 123, 137, 138, 139, 152, 179, 193, 207, 216, 221, 234, 268, 298, 315]},
        'weekly': {"categories": ["pbakaus/impeccable", "langchain-ai/deepagents", "nextlevelbuilder/ui-ux-pro-max-skill", "alibaba/page-agent", "aiming-lab/AutoResearchClaw", "abhigyanpatwari/GitNexus", "anthropics/skills", "shanraisshan/claude-code-best-practice", "gsd-build/get-shit-done", "THU-MAIC/OpenMAIC", "lightpanda-io/browser", "shareAI-lab/learn-claude-code", "paperclipai/paperclip", "volcengine/OpenViking", "affaan-m/everything-claude-code", "karpathy/autoresearch", "666ghj/MiroFish", "obra/superpowers", "openclaw/openclaw", "msitarzewski/agency-agents"], "data": [867, 944, 969, 990, 1042, 1044, 1063, 1080, 1330, 1569, 1614, 1638, 1692, 1813, 2685, 2776, 3177, 3471, 3505, 3736]},
        'monthly': {"categories": ["RightNow-AI/openfang", "abhigyanpatwari/GitNexus", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "x1xhlol/system-prompts-and-models-of-ai-tools", "googleworkspace/cli", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "666ghj/MiroFish", "paperclipai/paperclip", "koala73/worldmonitor", "ruvnet/RuView", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4048, 4170, 4299, 4449, 4476, 4621, 4718, 5233, 5463, 5555, 6090, 6392, 6504, 7641, 8403, 9195, 9258, 9631, 10970, 28732]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +315 | 7891 |
| 2 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +298 | 6893 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +268 | 45508 |
| 4 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +234 | 37091 |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +221 | 36991 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +216 | 56614 |
| 7 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +207 | 10156 |
| 8 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +193 | 34641 |
| 9 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +179 | 9432 |
| 10 | [louis-e/arnis](https://github.com/louis-e/arnis) | +152 | 11508 |
| 11 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +139 | 30546 |
| 12 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +138 | 12568 |
| 13 | [tw93/Mole](https://github.com/tw93/Mole) | +137 | 36870 |
| 14 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +123 | 34148 |
| 15 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +110 | 13554 |
| 16 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +109 | 16564 |
| 17 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +107 | 31058 |
| 18 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +106 | 16915 |
| 19 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +104 | 1640 |
| 20 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +103 | 7569 |
| 21 | [jackwener/opencli](https://github.com/jackwener/opencli) | +101 | 3037 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +91 | 4463 |
| 23 | [mobile-dev-inc/Maestro](https://github.com/mobile-dev-inc/Maestro) | +91 | 12770 |
| 24 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +90 | 18661 |
| 25 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +87 | 15937 |
| 26 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +84 | 5458 |
| 27 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +83 | 12263 |
| 28 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +82 | 6383 |
| 29 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +81 | 23738 |
| 30 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +80 | 32705 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3736 | 56614 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3505 | 224760 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +3471 | 60312 |
| 4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3177 | 36991 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2776 | 45508 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2685 | 51199 |
| 7 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1813 | 16915 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1692 | 30546 |
| 9 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1638 | 34641 |
| 10 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1614 | 22570 |
| 11 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1569 | 10156 |
| 12 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1330 | 37091 |
| 13 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1080 | 19376 |
| 14 | [anthropics/skills](https://github.com/anthropics/skills) | +1063 | 74774 |
| 15 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1044 | 18315 |
| 16 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1042 | 7098 |
| 17 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +990 | 12263 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +969 | 34148 |
| 19 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +944 | 15937 |
| 20 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +867 | 11271 |
| 21 | [mattpocock/skills](https://github.com/mattpocock/skills) | +840 | 7892 |
| 22 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +827 | 5670 |
| 23 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +825 | 23739 |
| 24 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +810 | 16228 |
| 25 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +773 | 41664 |
| 26 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +762 | 10932 |
| 27 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +739 | 9432 |
| 28 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +690 | 3444 |
| 29 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +682 | 30678 |
| 30 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +670 | 6893 |
| 31 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +665 | 60117 |
| 32 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +662 | 11414 |
| 33 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +657 | 17807 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +643 | 31058 |
| 35 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +626 | 40082 |
| 36 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +608 | 13554 |
| 37 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +600 | 3548 |
| 38 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +574 | 26312 |
| 39 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +557 | 26187 |
| 40 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +555 | 36012 |
| 41 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +545 | 9431 |
| 42 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +539 | 23783 |
| 43 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +535 | 5814 |
| 44 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +529 | 38564 |
| 45 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +529 | 2731 |
| 46 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +523 | 3006 |
| 47 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +508 | 18661 |
| 48 | [jackwener/opencli](https://github.com/jackwener/opencli) | +499 | 3037 |
| 49 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +486 | 37330 |
| 50 | [tw93/Mole](https://github.com/tw93/Mole) | +485 | 36870 |
| 51 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +482 | 32705 |
| 52 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +479 | 4463 |
| 53 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +478 | 2317 |
| 54 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +468 | 24565 |
| 55 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +442 | 18148 |
| 56 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +441 | 33878 |
| 57 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +435 | 31485 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +432 | 7352 |
| 59 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +420 | 35134 |
| 60 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +420 | 43973 |
| 61 | [jundot/omlx](https://github.com/jundot/omlx) | +415 | 6123 |
| 62 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +406 | 26433 |
| 63 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +404 | 8639 |
| 64 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +403 | 23824 |
| 65 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +395 | 12819 |
| 66 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +382 | 32045 |
| 67 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +377 | 26166 |
| 68 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +370 | 28518 |
| 69 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +369 | 7460 |
| 70 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +368 | 34897 |
| 71 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +359 | 5458 |
| 72 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +349 | 21788 |
| 73 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +347 | 4960 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +343 | 29017 |
| 75 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +341 | 5461 |
| 76 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +338 | 2178 |
| 77 | [louis-e/arnis](https://github.com/louis-e/arnis) | +336 | 11508 |
| 78 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +336 | 3454 |
| 79 | [novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket) | +335 | 2014 |
| 80 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +330 | 3002 |
| 81 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +320 | 6383 |
| 82 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +319 | 3838 |
| 83 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +316 | 28160 |
| 84 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +315 | 7569 |
| 85 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +314 | 2547 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +309 | 15005 |
| 87 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +308 | 1338 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +299 | 22157 |
| 89 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +299 | 4172 |
| 90 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +298 | 2830 |
| 91 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +296 | 30504 |
| 92 | [openai/symphony](https://github.com/openai/symphony) | +290 | 13638 |
| 93 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +281 | 1647 |
| 94 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +280 | 29405 |
| 95 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +271 | 4615 |
| 96 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +265 | 13330 |
| 97 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +261 | 1674 |
| 98 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +261 | 14408 |
| 99 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +258 | 2084 |
| 100 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +258 | 22111 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +247 | 6072 |
| 102 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +247 | 1834 |
| 103 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +239 | 10127 |
| 104 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +238 | 35735 |
| 105 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +237 | 2208 |
| 106 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +236 | 1515 |
| 107 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +234 | 30590 |
| 108 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +217 | 2083 |
| 109 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +217 | 8873 |
| 110 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +210 | 16564 |
| 111 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +210 | 3190 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +204 | 6496 |
| 113 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +199 | 22425 |
| 114 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +199 | 10064 |
| 115 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +196 | 1311 |
| 116 | [htdt/godogen](https://github.com/htdt/godogen) | +188 | 1434 |
| 117 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +185 | 26233 |
| 118 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +184 | 16436 |
| 119 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +170 | 47936 |
| 120 | [Janis174756/Binance-Futures-Trading-Bot](https://github.com/Janis174756/Binance-Futures-Trading-Bot) | +169 | 545 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +28732 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +10970 | 56614 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +9631 | 60312 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +9258 | 45508 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9195 | 51199 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8403 | 38564 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7641 | 41664 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6504 | 30546 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6392 | 36991 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +6090 | 74774 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5555 | 26433 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5463 | 40082 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5233 | 31485 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4718 | 21788 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4621 | 122870 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4476 | 109881 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4449 | 37091 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4299 | 34897 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4170 | 18315 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4048 | 15085 |
| 21 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4014 | 18148 |
| 22 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +3988 | 24566 |
| 23 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3840 | 34641 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3711 | 19376 |
| 25 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +3499 | 28160 |
| 26 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3400 | 12819 |
| 27 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3308 | 35134 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3072 | 69674 |
| 29 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3005 | 26166 |
| 30 | [openai/symphony](https://github.com/openai/symphony) | +2971 | 13638 |
| 31 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2893 | 26312 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2858 | 34148 |
| 33 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2838 | 16915 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2781 | 31058 |
| 35 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2715 | 32045 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2709 | 23739 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2668 | 9860 |
| 38 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2575 | 85286 |
| 39 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2437 | 10162 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2403 | 10127 |
| 41 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2400 | 37330 |
| 42 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +2365 | 25617 |
| 43 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2351 | 12263 |
| 44 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2350 | 60117 |
| 45 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2341 | 34107 |
| 46 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2307 | 33878 |
| 47 | [huggingface/skills](https://github.com/huggingface/skills) | +2234 | 9505 |
| 48 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2179 | 10597 |
| 49 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2129 | 11271 |
| 50 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2106 | 26187 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2082 | 147486 |
| 52 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2041 | 22111 |
| 53 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2034 | 23824 |
| 54 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2028 | 10551 |
| 55 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2017 | 30678 |
| 56 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2012 | 13778 |
| 57 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1981 | 7837 |
| 58 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1958 | 22570 |
| 59 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1951 | 9431 |
| 60 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1951 | 11414 |
| 61 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1928 | 6813 |
| 62 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1925 | 8873 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1882 | 29017 |
| 64 | [github/spec-kit](https://github.com/github/spec-kit) | +1844 | 71722 |
| 65 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1796 | 18662 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1790 | 32705 |
| 67 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1779 | 10932 |
| 68 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1739 | 96919 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1708 | 16228 |
| 70 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1691 | 6996 |
| 71 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1678 | 22425 |
| 72 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1677 | 8639 |
| 73 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1619 | 7460 |
| 74 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1615 | 6451 |
| 75 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1569 | 10156 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1554 | 13330 |
| 77 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1549 | 15655 |
| 78 | [tw93/Mole](https://github.com/tw93/Mole) | +1548 | 36870 |
| 79 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1546 | 98536 |
| 80 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1534 | 8011 |
| 81 | [tobi/qmd](https://github.com/tobi/qmd) | +1524 | 16289 |
| 82 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1508 | 149018 |
| 83 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1501 | 6608 |
| 84 | [openai/skills](https://github.com/openai/skills) | +1488 | 14746 |
| 85 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1459 | 12966 |
| 86 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1423 | 7521 |
| 87 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1423 | 14064 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1415 | 15005 |
| 89 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1371 | 17807 |
| 90 | [maderix/ANE](https://github.com/maderix/ANE) | +1367 | 6258 |
| 91 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1362 | 5743 |
| 92 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1336 | 36012 |
| 93 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1334 | 13554 |
| 94 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1269 | 43973 |
| 95 | [openai/codex](https://github.com/openai/codex) | +1267 | 61744 |
| 96 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1240 | 5461 |
| 97 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1221 | 5693 |
| 98 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1217 | 15937 |
| 99 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1179 | 37564 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1161 | 7352 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1138 | 16436 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1136 | 29405 |
| 103 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1087 | 7892 |
| 104 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1083 | 87598 |
| 105 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1044 | 7098 |
| 106 | [jundot/omlx](https://github.com/jundot/omlx) | +1034 | 6123 |
| 107 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +967 | 13077 |
| 108 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +963 | 6893 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +958 | 6496 |
| 110 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +952 | 7069 |
| 111 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +928 | 35735 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +928 | 26233 |
| 113 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +918 | 9432 |
| 114 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +912 | 7451 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +815 | 6072 |
| 116 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +814 | 5670 |
| 117 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +806 | 52700 |
| 118 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +806 | 13752 |
| 119 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +791 | 45886 |
| 120 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +791 | 61818 |
| 121 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +765 | 36799 |
| 122 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +755 | 47122 |
| 123 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +739 | 9918 |
| 124 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +722 | 28518 |
| 125 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +712 | 3202 |
| 126 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +701 | 6383 |
| 127 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +691 | 16564 |
| 128 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +685 | 4366 |
| 129 | [wshobson/agents](https://github.com/wshobson/agents) | +675 | 31833 |
| 130 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +668 | 30590 |
| 131 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +663 | 5458 |
| 132 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +646 | 15700 |
| 133 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +643 | 47936 |
| 134 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +638 | 23482 |
| 135 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +636 | 3454 |
| 136 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +635 | 6121 |
| 137 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +629 | 22836 |
| 138 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +618 | 2158 |
| 139 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +611 | 3548 |
| 140 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +596 | 23276 |
| 141 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +593 | 2110 |
| 142 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +591 | 16649 |
| 143 | [docling-project/docling](https://github.com/docling-project/docling) | +587 | 54041 |
| 144 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +567 | 2549 |
| 145 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +555 | 10064 |
| 146 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +542 | 44232 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +538 | 44545 |
| 148 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +537 | 33712 |
| 149 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +517 | 3409 |
| 150 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +517 | 1978 |
| 151 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +511 | 3002 |
| 152 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +508 | 3379 |
| 153 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +500 | 2830 |
| 154 | [eooce/python-ws](https://github.com/eooce/python-ws) | +490 | 1878 |
| 155 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +490 | 8059 |
| 156 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +489 | 18366 |
| 157 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +484 | 1955 |
| 158 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +484 | 39841 |
| 159 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +482 | 2317 |
| 160 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +480 | 26998 |
| 161 | [aden-hive/hive](https://github.com/aden-hive/hive) | +476 | 9680 |
| 162 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +452 | 14549 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +448 | 3170 |
| 164 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +448 | 1993 |
| 165 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +447 | 14408 |
| 166 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +442 | 9775 |
| 167 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +435 | 6108 |
| 168 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +434 | 3918 |
| 169 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +433 | 12568 |
| 170 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +412 | 1662 |
| 171 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +408 | 9893 |
| 172 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +401 | 1584 |
| 173 | [apify/agent-skills](https://github.com/apify/agent-skills) | +400 | 1692 |
| 174 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +398 | 10505 |
| 175 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +395 | 2208 |
| 176 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +387 | 7541 |
| 177 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +375 | 2372 |
| 178 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +373 | 3298 |
| 179 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +371 | 1834 |
| 180 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +367 | 19044 |
| 181 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +365 | 24822 |
| 182 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +351 | 3570 |
| 183 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +351 | 6238 |
| 184 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +338 | 1624 |
| 185 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +334 | 1457 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +332 | 24617 |
| 187 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +331 | 0 |
| 188 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +323 | 7569 |
| 189 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +323 | 2856 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +321 | 10441 |
| 191 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +314 | 4122 |
| 192 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +308 | 1338 |
| 193 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +303 | 13483 |
| 194 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +299 | 1434 |
| 195 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +299 | 1329 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +281 | 3741 |
| 197 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +279 | 29780 |
| 198 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +263 | 1515 |
| 199 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +257 | 21729 |
| 200 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +251 | 2382 |
| 201 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +248 | 36103 |
| 202 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +237 | 21411 |
| 203 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +235 | 1444 |
| 204 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +235 | 963 |
| 205 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +234 | 1077 |
| 206 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 145 |
| 207 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +218 | 935 |
| 208 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +203 | 7194 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +196 | 41086 |
| 210 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +193 | 1408 |
| 211 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +192 | 5270 |
| 212 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +191 | 663 |
| 213 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +191 | 8943 |
| 214 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +186 | 28997 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +183 | 40265 |
| 216 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +179 | 8864 |
| 217 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +178 | 780 |
| 218 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +177 | 25371 |
| 219 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +174 | 1592 |
| 220 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +166 | 2635 |
| 221 | [robinebers/openusage](https://github.com/robinebers/openusage) | +165 | 1562 |
| 222 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +165 | 704 |
| 223 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +164 | 948 |
| 224 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +162 | 755 |
| 225 | [decolua/9router](https://github.com/decolua/9router) | +159 | 1117 |
| 226 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +157 | 2457 |
| 227 | [jgraph/drawio](https://github.com/jgraph/drawio) | +154 | 4262 |
| 228 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +153 | 917 |
| 229 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +148 | 1432 |
| 230 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +145 | 2050 |
| 231 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +145 | 1172 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +145 | 2108 |
| 233 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +142 | 1146 |
| 234 | [es617/claude-replay](https://github.com/es617/claude-replay) | +140 | 553 |
| 235 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +140 | 5212 |
| 236 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +140 | 22823 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +140 | 33000 |
| 238 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +138 | 676 |
| 239 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +132 | 1690 |
| 240 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +132 | 905 |
| 241 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +130 | 35473 |
| 242 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +125 | 502 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +124 | 26010 |
| 244 | [4ier/neo](https://github.com/4ier/neo) | +123 | 621 |
| 245 | [is-a-dev/register](https://github.com/is-a-dev/register) | +122 | 10001 |
| 246 | [qist/tvbox](https://github.com/qist/tvbox) | +119 | 8556 |
| 247 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +117 | 629 |
| 248 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +114 | 417 |
| 249 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +114 | 12195 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +114 | 48784 |
| 251 | [fmhy/edit](https://github.com/fmhy/edit) | +113 | 8614 |
| 252 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +112 | 588 |
| 253 | [microg/GmsCore](https://github.com/microg/GmsCore) | +109 | 12631 |
| 254 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +107 | 3539 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +106 | 1329 |
| 256 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +106 | 10118 |
| 257 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +105 | 3292 |
| 258 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +105 | 8839 |
| 259 | [skylot/jadx](https://github.com/skylot/jadx) | +105 | 47365 |
| 260 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +104 | 429 |
| 261 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +103 | 1069 |
| 262 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 263 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +103 | 11207 |
| 264 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +100 | 510 |
| 265 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +100 | 3207 |
| 266 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +100 | 471 |
| 267 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +99 | 1037 |
| 268 | [lklynet/aurral](https://github.com/lklynet/aurral) | +98 | 878 |
| 269 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +95 | 956 |
| 270 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +95 | 870 |
| 271 | [expo/skills](https://github.com/expo/skills) | +95 | 1513 |
| 272 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +95 | 630 |
| 273 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +95 | 37313 |
| 274 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +94 | 524 |
| 275 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +94 | 810 |
| 276 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +94 | 893 |
| 277 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +89 | 7053 |
| 278 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +86 | 605 |
| 279 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +86 | 498 |
| 280 | [silships/figma-cli](https://github.com/silships/figma-cli) | +86 | 449 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 3069 |
| 282 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +84 | 428 |
| 283 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +84 | 387 |
| 284 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +84 | 396 |
| 285 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +81 | 26958 |
| 286 | [idinging/freemail](https://github.com/idinging/freemail) | +80 | 1078 |
| 287 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +80 | 864 |
| 288 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +73 | 264 |
| 289 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +73 | 8249 |
| 290 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +73 | 21387 |
| 291 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +71 | 446 |
| 292 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +70 | 6106 |
| 293 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +68 | 1006 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +67 | 1358 |
| 295 | [Widdit/now-playing-service](https://github.com/Widdit/now-playing-service) | +66 | 524 |
| 296 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 297 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +65 | 915 |
| 298 | [apache/kafka](https://github.com/apache/kafka) | +65 | 32043 |
| 299 | [freeok/so-novel](https://github.com/freeok/so-novel) | +65 | 6387 |
| 300 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +64 | 12399 |
