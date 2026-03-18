---
title: "2026-03-18 GitHub增长趋势报告"
description: "1.AutoResearchClaw+534 2.OpenMAIC+530 3.get-shit-done+460 4.agency-agents+435 5.learn-claude-code+325"
date: 2026-03-18T20:39:46+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-18 20:39:46

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
        'daily': {"categories": ["lightpanda-io/browser", "alibaba/page-agent", "mattpocock/skills", "paperclipai/paperclip", "jarrodwatts/claude-hud", "sgoudelis/ground-station", "opendataloader-project/opendataloader-pdf", "calesthio/Crucix", "abhigyanpatwari/GitNexus", "langchain-ai/deepagents", "nextlevelbuilder/ui-ux-pro-max-skill", "andrewyng/context-hub", "mukul975/Anthropic-Cybersecurity-Skills", "karpathy/autoresearch", "666ghj/MiroFish", "shareAI-lab/learn-claude-code", "msitarzewski/agency-agents", "gsd-build/get-shit-done", "THU-MAIC/OpenMAIC", "aiming-lab/AutoResearchClaw"], "data": [123, 144, 155, 159, 169, 181, 189, 189, 191, 194, 200, 209, 244, 246, 298, 325, 435, 460, 530, 534]},
        'weekly': {"categories": ["p-e-w/heretic", "abhigyanpatwari/GitNexus", "AstrBotDevs/AstrBot", "shanraisshan/claude-code-best-practice", "gsd-build/get-shit-done", "THU-MAIC/OpenMAIC", "microsoft/BitNet", "pbakaus/impeccable", "anthropics/skills", "alibaba/page-agent", "shareAI-lab/learn-claude-code", "lightpanda-io/browser", "volcengine/OpenViking", "paperclipai/paperclip", "affaan-m/everything-claude-code", "obra/superpowers", "karpathy/autoresearch", "666ghj/MiroFish", "openclaw/openclaw", "msitarzewski/agency-agents"], "data": [997, 1018, 1063, 1090, 1128, 1132, 1189, 1192, 1238, 1369, 1388, 1766, 1999, 2144, 2465, 3220, 3251, 3608, 4260, 5040]},
        'monthly': {"categories": ["abhigyanpatwari/GitNexus", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "zeroclaw-labs/zeroclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "googleworkspace/cli", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "666ghj/MiroFish", "anthropics/skills", "paperclipai/paperclip", "koala73/worldmonitor", "ruvnet/RuView", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4096, 4227, 4259, 4541, 4594, 4636, 4656, 5176, 5542, 5591, 6028, 6117, 6229, 7866, 8397, 8702, 8765, 9249, 10541, 29806]}
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
| 1 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +534 | 6120 |
| 2 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +530 | 7243 |
| 3 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +460 | 34686 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +435 | 53848 |
| 5 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +325 | 32078 |
| 6 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +298 | 34120 |
| 7 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +246 | 41909 |
| 8 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +244 | 3393 |
| 9 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +209 | 10114 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +200 | 34148 |
| 11 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +194 | 15035 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +191 | 17415 |
| 13 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +189 | 4222 |
| 14 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +189 | 3945 |
| 15 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +181 | 2281 |
| 16 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +169 | 6744 |
| 17 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +159 | 28896 |
| 18 | [mattpocock/skills](https://github.com/mattpocock/skills) | +155 | 3730 |
| 19 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +144 | 11199 |
| 20 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +123 | 21684 |
| 21 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +121 | 15716 |
| 22 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +119 | 22695 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +118 | 10452 |
| 24 | [yazinsai/OpenGranola](https://github.com/yazinsai/OpenGranola) | +103 | 956 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +98 | 29916 |
| 26 | [tw93/Mole](https://github.com/tw93/Mole) | +91 | 36870 |
| 27 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +90 | 8585 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +90 | 10263 |
| 29 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +87 | 40626 |
| 30 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +86 | 1047 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5040 | 53848 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4260 | 224760 |
| 3 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3608 | 34120 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3251 | 41909 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +3220 | 60312 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2465 | 51199 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2144 | 28896 |
| 8 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1999 | 15716 |
| 9 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1766 | 21684 |
| 10 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1388 | 32078 |
| 11 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1369 | 11199 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +1238 | 74774 |
| 13 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1192 | 10452 |
| 14 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1189 | 35576 |
| 15 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1132 | 7243 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1128 | 34686 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1090 | 18496 |
| 18 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1063 | 25820 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1018 | 17415 |
| 20 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +997 | 15921 |
| 21 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +988 | 10114 |
| 22 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +975 | 17414 |
| 23 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +900 | 40626 |
| 24 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +858 | 6120 |
| 25 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +847 | 34148 |
| 26 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +805 | 15035 |
| 27 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +805 | 8779 |
| 28 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +803 | 22695 |
| 29 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +776 | 39342 |
| 30 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +701 | 3325 |
| 31 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +694 | 38060 |
| 32 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +647 | 30678 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +641 | 29916 |
| 34 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +622 | 12642 |
| 35 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +607 | 43973 |
| 36 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +606 | 10263 |
| 37 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +601 | 4222 |
| 38 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +600 | 25476 |
| 39 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +580 | 17766 |
| 40 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +578 | 8281 |
| 41 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +559 | 3393 |
| 42 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +530 | 23691 |
| 43 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +529 | 28136 |
| 44 | [jundot/omlx](https://github.com/jundot/omlx) | +515 | 5779 |
| 45 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +507 | 31687 |
| 46 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +506 | 34657 |
| 47 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +505 | 3263 |
| 48 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +501 | 17839 |
| 49 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +500 | 37330 |
| 50 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +496 | 5699 |
| 51 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +493 | 25950 |
| 52 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +492 | 21428 |
| 53 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +491 | 31010 |
| 54 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +489 | 2733 |
| 55 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +485 | 24102 |
| 56 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +476 | 4904 |
| 57 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +475 | 25634 |
| 58 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +473 | 32001 |
| 59 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +472 | 23371 |
| 60 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +459 | 2191 |
| 61 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +446 | 6779 |
| 62 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +444 | 34458 |
| 63 | [openai/symphony](https://github.com/openai/symphony) | +440 | 13359 |
| 64 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +430 | 7203 |
| 65 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +428 | 12595 |
| 66 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +424 | 33878 |
| 67 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +424 | 27865 |
| 68 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +410 | 3516 |
| 69 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +394 | 5211 |
| 70 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +376 | 3599 |
| 71 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +375 | 2312 |
| 72 | [tw93/Mole](https://github.com/tw93/Mole) | +372 | 36870 |
| 73 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +355 | 4915 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +343 | 28438 |
| 75 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +335 | 1742 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +333 | 14574 |
| 77 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +322 | 25370 |
| 78 | [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | +320 | 2055 |
| 79 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +318 | 12689 |
| 80 | [tobi/qmd](https://github.com/tobi/qmd) | +315 | 16002 |
| 81 | [kepano/defuddle](https://github.com/kepano/defuddle) | +310 | 5429 |
| 82 | [jackwener/opencli](https://github.com/jackwener/opencli) | +309 | 1779 |
| 83 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +305 | 9871 |
| 84 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +304 | 1306 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +303 | 21677 |
| 86 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +302 | 35735 |
| 87 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +300 | 1843 |
| 88 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +299 | 5746 |
| 89 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +299 | 12966 |
| 90 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +299 | 45886 |
| 91 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +297 | 6744 |
| 92 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +296 | 2343 |
| 93 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +292 | 30062 |
| 94 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +291 | 28990 |
| 95 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +270 | 6283 |
| 96 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +269 | 2420 |
| 97 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +261 | 14324 |
| 98 | [blader/humanizer](https://github.com/blader/humanizer) | +257 | 9985 |
| 99 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +245 | 1301 |
| 100 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +242 | 1324 |
| 101 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +234 | 2489 |
| 102 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +231 | 1350 |
| 103 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +201 | 16227 |
| 104 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +197 | 25895 |
| 105 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +196 | 9927 |
| 106 | [mattpocock/skills](https://github.com/mattpocock/skills) | +194 | 3730 |
| 107 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +190 | 15432 |
| 108 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +189 | 8585 |
| 109 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +187 | 22203 |
| 110 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +181 | 47936 |
| 111 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +177 | 2954 |
| 112 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +168 | 44232 |
| 113 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +160 | 30590 |
| 114 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +160 | 6992 |
| 115 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +160 | 2510 |
| 116 | [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli) | +158 | 1385 |
| 117 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +158 | 1955 |
| 118 | [jackwener/xiaohongshu-cli](https://github.com/jackwener/xiaohongshu-cli) | +152 | 1301 |
| 119 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +152 | 44545 |
| 120 | [htdt/godogen](https://github.com/htdt/godogen) | +150 | 1036 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +29806 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +10541 | 53848 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +9249 | 60312 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +8765 | 41909 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8702 | 51199 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8397 | 38060 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7866 | 40626 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6229 | 28896 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6117 | 74774 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6028 | 34121 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5591 | 25950 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5542 | 39342 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5176 | 31010 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4656 | 21428 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4636 | 122870 |
| 16 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +4594 | 27865 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4541 | 109881 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4259 | 34686 |
| 19 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4227 | 34458 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4096 | 17415 |
| 21 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4096 | 17766 |
| 22 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4017 | 24102 |
| 23 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4014 | 14884 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3609 | 18496 |
| 25 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3506 | 34657 |
| 26 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3487 | 32078 |
| 27 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3356 | 12595 |
| 28 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3283 | 25634 |
| 29 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3039 | 69674 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2987 | 25476 |
| 31 | [openai/symphony](https://github.com/openai/symphony) | +2925 | 13359 |
| 32 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2900 | 13403 |
| 33 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2791 | 15716 |
| 34 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +2767 | 25370 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2713 | 34148 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2661 | 29916 |
| 37 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2660 | 10034 |
| 38 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2659 | 31687 |
| 39 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2638 | 9721 |
| 40 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2631 | 85286 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2618 | 22695 |
| 42 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2552 | 60117 |
| 43 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2473 | 33978 |
| 44 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2403 | 37330 |
| 45 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2367 | 9871 |
| 46 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2285 | 33878 |
| 47 | [huggingface/skills](https://github.com/huggingface/skills) | +2209 | 9304 |
| 48 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2185 | 11199 |
| 49 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2180 | 25820 |
| 50 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2143 | 147486 |
| 51 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2097 | 10018 |
| 52 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2072 | 30678 |
| 53 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2056 | 10410 |
| 54 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2029 | 23371 |
| 55 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2016 | 10452 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1981 | 21615 |
| 57 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1975 | 15921 |
| 58 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1966 | 7690 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1901 | 6631 |
| 60 | [github/spec-kit](https://github.com/github/spec-kit) | +1880 | 71722 |
| 61 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1875 | 8585 |
| 62 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1874 | 10263 |
| 63 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1858 | 8779 |
| 64 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1832 | 96919 |
| 65 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1825 | 21684 |
| 66 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1796 | 28438 |
| 67 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1747 | 6537 |
| 68 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1736 | 32001 |
| 69 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1716 | 17839 |
| 70 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1685 | 22203 |
| 71 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1674 | 6916 |
| 72 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1667 | 10115 |
| 73 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1651 | 7937 |
| 74 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1646 | 10203 |
| 75 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1619 | 8281 |
| 76 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1591 | 6338 |
| 77 | [tobi/qmd](https://github.com/tobi/qmd) | +1582 | 16002 |
| 78 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1581 | 7203 |
| 79 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1579 | 6708 |
| 80 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1550 | 12966 |
| 81 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1547 | 15432 |
| 82 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1532 | 149018 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1529 | 98536 |
| 84 | [openai/skills](https://github.com/openai/skills) | +1513 | 14572 |
| 85 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1512 | 7308 |
| 86 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1502 | 12689 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +1456 | 36870 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1436 | 14574 |
| 89 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1419 | 13996 |
| 90 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1413 | 7380 |
| 91 | [maderix/ANE](https://github.com/maderix/ANE) | +1369 | 6228 |
| 92 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1341 | 5646 |
| 93 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1323 | 17414 |
| 94 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1277 | 43973 |
| 95 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1274 | 35576 |
| 96 | [openai/codex](https://github.com/openai/codex) | +1255 | 61744 |
| 97 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1239 | 37564 |
| 98 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1229 | 12642 |
| 99 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1200 | 5211 |
| 100 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1161 | 5337 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1154 | 16228 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1149 | 28990 |
| 103 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1136 | 7243 |
| 104 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1097 | 87598 |
| 105 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1063 | 15035 |
| 106 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1007 | 6992 |
| 107 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +993 | 13028 |
| 108 | [jundot/omlx](https://github.com/jundot/omlx) | +960 | 5779 |
| 109 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +955 | 22810 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +952 | 25895 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +949 | 6283 |
| 112 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +914 | 35735 |
| 113 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +846 | 6120 |
| 114 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +830 | 13529 |
| 115 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +793 | 61818 |
| 116 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +790 | 45886 |
| 117 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +778 | 5746 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +765 | 36799 |
| 119 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +755 | 47122 |
| 120 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +744 | 9813 |
| 121 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +706 | 3126 |
| 122 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +693 | 4310 |
| 123 | [wshobson/agents](https://github.com/wshobson/agents) | +675 | 31613 |
| 124 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +674 | 28136 |
| 125 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +659 | 23302 |
| 126 | [google-research/timesfm](https://github.com/google-research/timesfm) | +650 | 10076 |
| 127 | [docling-project/docling](https://github.com/docling-project/docling) | +647 | 54041 |
| 128 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +645 | 15669 |
| 129 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +633 | 47936 |
| 130 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +628 | 5719 |
| 131 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +620 | 23173 |
| 132 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +610 | 2109 |
| 133 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +604 | 3263 |
| 134 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +597 | 30590 |
| 135 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +592 | 16431 |
| 136 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +589 | 2080 |
| 137 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +586 | 33712 |
| 138 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +578 | 5488 |
| 139 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +575 | 52700 |
| 140 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +567 | 4222 |
| 141 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +566 | 3393 |
| 142 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +566 | 15623 |
| 143 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +563 | 2510 |
| 144 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +555 | 4915 |
| 145 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +554 | 9927 |
| 146 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +551 | 7974 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +538 | 44545 |
| 148 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +530 | 44232 |
| 149 | [aden-hive/hive](https://github.com/aden-hive/hive) | +516 | 9579 |
| 150 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +512 | 1961 |
| 151 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +509 | 3328 |
| 152 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +491 | 9695 |
| 153 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +488 | 6744 |
| 154 | [eooce/python-ws](https://github.com/eooce/python-ws) | +487 | 1846 |
| 155 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +485 | 18297 |
| 156 | [google/langextract](https://github.com/google/langextract) | +484 | 33636 |
| 157 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +482 | 3945 |
| 158 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +477 | 39841 |
| 159 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +476 | 1955 |
| 160 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +475 | 14486 |
| 161 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +473 | 26818 |
| 162 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +464 | 2191 |
| 163 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +448 | 14324 |
| 164 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +447 | 2420 |
| 165 | [openclaw/skills](https://github.com/openclaw/skills) | +447 | 3056 |
| 166 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +442 | 1955 |
| 167 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +431 | 3820 |
| 168 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +424 | 1628 |
| 169 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +403 | 9764 |
| 170 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +401 | 5248 |
| 171 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +399 | 1571 |
| 172 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +399 | 10498 |
| 173 | [apify/agent-skills](https://github.com/apify/agent-skills) | +393 | 1665 |
| 174 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +386 | 7430 |
| 175 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +372 | 4354 |
| 176 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +371 | 18800 |
| 177 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +371 | 24702 |
| 178 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +370 | 3174 |
| 179 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +370 | 2326 |
| 180 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +362 | 5552 |
| 181 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +361 | 1742 |
| 182 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +361 | 6101 |
| 183 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +358 | 2282 |
| 184 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +357 | 3556 |
| 185 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +357 | 0 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +350 | 24525 |
| 187 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +336 | 1843 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +328 | 1393 |
| 189 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +324 | 1515 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +319 | 10349 |
| 191 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +310 | 13439 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +308 | 4033 |
| 193 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +304 | 1306 |
| 194 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +298 | 1307 |
| 195 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +295 | 2489 |
| 196 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +288 | 2351 |
| 197 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +285 | 3633 |
| 198 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +276 | 1332 |
| 199 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +270 | 29780 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +264 | 36103 |
| 201 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +254 | 21678 |
| 202 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +243 | 955 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +242 | 21363 |
| 204 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +225 | 757 |
| 205 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +225 | 145 |
| 206 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +212 | 1570 |
| 207 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +211 | 967 |
| 208 | [robinebers/openusage](https://github.com/robinebers/openusage) | +209 | 1543 |
| 209 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +204 | 869 |
| 210 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +202 | 7097 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +199 | 41086 |
| 212 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +196 | 1359 |
| 213 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +196 | 8898 |
| 214 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +192 | 2606 |
| 215 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +190 | 28939 |
| 216 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +189 | 652 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +186 | 40265 |
| 218 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +184 | 5191 |
| 219 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +183 | 8847 |
| 220 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +177 | 699 |
| 221 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +176 | 916 |
| 222 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +175 | 25352 |
| 223 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +167 | 1029 |
| 224 | [decolua/9router](https://github.com/decolua/9router) | +165 | 1055 |
| 225 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +157 | 718 |
| 226 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +156 | 577 |
| 227 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +155 | 2448 |
| 228 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +154 | 1048 |
| 229 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +153 | 891 |
| 230 | [jgraph/drawio](https://github.com/jgraph/drawio) | +151 | 4220 |
| 231 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +150 | 22789 |
| 232 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +149 | 1416 |
| 233 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +149 | 647 |
| 234 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +146 | 33000 |
| 235 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +143 | 661 |
| 236 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +143 | 1120 |
| 237 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +142 | 5187 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +142 | 2059 |
| 239 | [es617/claude-replay](https://github.com/es617/claude-replay) | +140 | 541 |
| 240 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +140 | 1665 |
| 241 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +139 | 895 |
| 242 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +138 | 2002 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +137 | 25984 |
| 244 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +130 | 493 |
| 245 | [is-a-dev/register](https://github.com/is-a-dev/register) | +126 | 9996 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +125 | 12138 |
| 247 | [qist/tvbox](https://github.com/qist/tvbox) | +125 | 8542 |
| 248 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +124 | 29000 |
| 249 | [4ier/neo](https://github.com/4ier/neo) | +121 | 610 |
| 250 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +121 | 35473 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +118 | 48784 |
| 252 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +112 | 3262 |
| 253 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +111 | 449 |
| 254 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +111 | 3502 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +110 | 1303 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +110 | 12609 |
| 257 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +109 | 387 |
| 258 | [fmhy/edit](https://github.com/fmhy/edit) | +109 | 8562 |
| 259 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +108 | 857 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +108 | 10085 |
| 261 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +105 | 447 |
| 262 | [lklynet/aurral](https://github.com/lklynet/aurral) | +105 | 871 |
| 263 | [expo/skills](https://github.com/expo/skills) | +104 | 1496 |
| 264 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +104 | 11178 |
| 265 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +103 | 422 |
| 266 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 267 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +101 | 1028 |
| 268 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +100 | 530 |
| 269 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +100 | 37313 |
| 270 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +99 | 3195 |
| 271 | [skylot/jadx](https://github.com/skylot/jadx) | +99 | 47365 |
| 272 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +98 | 881 |
| 273 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +98 | 8805 |
| 274 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +97 | 7029 |
| 275 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +97 | 613 |
| 276 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +96 | 790 |
| 277 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +94 | 940 |
| 278 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +91 | 374 |
| 279 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 3045 |
| 280 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +85 | 337 |
| 281 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +82 | 580 |
| 282 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +82 | 486 |
| 283 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +81 | 849 |
| 284 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +81 | 26917 |
| 285 | [apache/kafka](https://github.com/apache/kafka) | +78 | 32043 |
| 286 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +77 | 363 |
| 287 | [openjdk/jdk](https://github.com/openjdk/jdk) | +77 | 22699 |
| 288 | [idinging/freemail](https://github.com/idinging/freemail) | +76 | 1050 |
| 289 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +75 | 429 |
| 290 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +74 | 8230 |
| 291 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +72 | 428 |
| 292 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +72 | 1335 |
| 293 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +71 | 988 |
| 294 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +71 | 548 |
| 295 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +71 | 21374 |
| 296 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +70 | 6089 |
| 297 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +69 | 260 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +68 | 1330 |
| 299 | [freeok/so-novel](https://github.com/freeok/so-novel) | +65 | 6370 |
| 300 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +65 | 45263 |
