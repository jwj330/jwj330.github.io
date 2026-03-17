---
title: "2026-03-17 GitHub增长趋势报告"
description: "1.MiroFish+501 2.agency-agents+422 3.context-hub+299 4.autoresearch+291 5.Crucix+262"
date: 2026-03-17T20:41:41+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-17 20:41:41

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
        'daily': {"categories": ["htdt/godogen", "ZhuLinsen/daily_stock_analysis", "Crosstalk-Solutions/project-nomad", "koala73/worldmonitor", "nextlevelbuilder/ui-ux-pro-max-skill", "shadps4-emu/shadPS4", "alibaba/page-agent", "rtk-ai/rtk", "abhigyanpatwari/GitNexus", "lightpanda-io/browser", "langchain-ai/deepagents", "shareAI-lab/learn-claude-code", "thedotmack/claude-mem", "volcengine/OpenViking", "paperclipai/paperclip", "calesthio/Crucix", "karpathy/autoresearch", "andrewyng/context-hub", "msitarzewski/agency-agents", "666ghj/MiroFish"], "data": [93, 93, 104, 109, 114, 122, 131, 146, 146, 158, 197, 200, 203, 221, 253, 262, 291, 299, 422, 501]},
        'weekly': {"categories": ["p-e-w/heretic", "NousResearch/hermes-agent", "andrewyng/context-hub", "promptfoo/promptfoo", "shanraisshan/claude-code-best-practice", "AstrBotDevs/AstrBot", "shareAI-lab/learn-claude-code", "microsoft/BitNet", "pbakaus/impeccable", "anthropics/skills", "alibaba/page-agent", "lightpanda-io/browser", "volcengine/OpenViking", "paperclipai/paperclip", "affaan-m/everything-claude-code", "obra/superpowers", "666ghj/MiroFish", "karpathy/autoresearch", "openclaw/openclaw", "msitarzewski/agency-agents"], "data": [957, 968, 987, 1050, 1050, 1086, 1143, 1149, 1161, 1348, 1469, 1657, 1918, 2346, 2394, 2863, 3855, 3914, 5077, 5628]},
        'monthly': {"categories": ["qwibitai/nanoclaw", "AlexsJones/llmfit", "moeru-ai/airi", "anomalyco/opencode", "googleworkspace/cli", "x1xhlol/system-prompts-and-models-of-ai-tools", "D4Vinci/Scrapling", "zeroclaw-labs/zeroclaw", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "666ghj/MiroFish", "paperclipai/paperclip", "anthropics/skills", "koala73/worldmonitor", "ruvnet/RuView", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4048, 4119, 4193, 4582, 4619, 4639, 5129, 5392, 5617, 5661, 5786, 6085, 6086, 7849, 8364, 8500, 8537, 8876, 10158, 30430]}
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
| 1 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +501 | 32452 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +422 | 51429 |
| 3 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +299 | 9095 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +291 | 40206 |
| 5 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +262 | 2926 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +253 | 27914 |
| 7 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +221 | 15099 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +203 | 30678 |
| 9 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +200 | 30388 |
| 10 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +197 | 13913 |
| 11 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +158 | 20947 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +146 | 16586 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +146 | 9606 |
| 14 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +131 | 10390 |
| 15 | [shadps4-emu/shadPS4](https://github.com/shadps4-emu/shadPS4) | +122 | 29453 |
| 16 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +114 | 34148 |
| 17 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +109 | 39995 |
| 18 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +104 | 2163 |
| 19 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +93 | 21886 |
| 20 | [htdt/godogen](https://github.com/htdt/godogen) | +93 | 844 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +87 | 9910 |
| 22 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +84 | 5464 |
| 23 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +83 | 4447 |
| 24 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +79 | 38895 |
| 25 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +79 | 3728 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +78 | 31754 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +77 | 29376 |
| 28 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +76 | 15662 |
| 29 | [jackwener/opencli](https://github.com/jackwener/opencli) | +73 | 1338 |
| 30 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +72 | 31576 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5628 | 51429 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5077 | 224760 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3914 | 40206 |
| 4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3855 | 32452 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +2863 | 60312 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2394 | 51199 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2346 | 27915 |
| 8 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1918 | 15099 |
| 9 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1657 | 20947 |
| 10 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1469 | 10390 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1348 | 74774 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1161 | 9910 |
| 13 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1149 | 35235 |
| 14 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1143 | 30388 |
| 15 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1086 | 25572 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1050 | 18093 |
| 17 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1050 | 17156 |
| 18 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +987 | 9095 |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +968 | 8426 |
| 20 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +957 | 15662 |
| 21 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +925 | 38895 |
| 22 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +886 | 39995 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +865 | 16585 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +793 | 37766 |
| 25 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +757 | 31754 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +756 | 21886 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +735 | 34148 |
| 28 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +681 | 3173 |
| 29 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +675 | 43973 |
| 30 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +659 | 13913 |
| 31 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +648 | 7981 |
| 32 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +639 | 31453 |
| 33 | [jundot/omlx](https://github.com/jundot/omlx) | +635 | 5561 |
| 34 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +626 | 17492 |
| 35 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +615 | 25044 |
| 36 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +614 | 12485 |
| 37 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +614 | 21168 |
| 38 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +612 | 30678 |
| 39 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +607 | 29376 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +600 | 9606 |
| 41 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +571 | 25711 |
| 42 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +566 | 27981 |
| 43 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +535 | 30662 |
| 44 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +534 | 3182 |
| 45 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +527 | 4861 |
| 46 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +522 | 34276 |
| 47 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +518 | 23597 |
| 48 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +504 | 37330 |
| 49 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +503 | 23827 |
| 50 | [openai/symphony](https://github.com/openai/symphony) | +503 | 13187 |
| 51 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +483 | 34243 |
| 52 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +480 | 23053 |
| 53 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +479 | 3353 |
| 54 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +478 | 2531 |
| 55 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +478 | 25249 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +473 | 17407 |
| 57 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +467 | 12450 |
| 58 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +461 | 27665 |
| 59 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +456 | 31576 |
| 60 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +452 | 6921 |
| 61 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +449 | 2082 |
| 62 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +442 | 33878 |
| 63 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +432 | 2926 |
| 64 | [ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots) | +431 | 2864 |
| 65 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +428 | 5340 |
| 66 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +412 | 6379 |
| 67 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +402 | 3476 |
| 68 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +386 | 45886 |
| 69 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +367 | 5021 |
| 70 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +364 | 25224 |
| 71 | [tobi/qmd](https://github.com/tobi/qmd) | +356 | 15851 |
| 72 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +350 | 2163 |
| 73 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +344 | 12507 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +342 | 28160 |
| 75 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +338 | 4582 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +338 | 12715 |
| 77 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +335 | 9701 |
| 78 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +333 | 5537 |
| 79 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +333 | 35735 |
| 80 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +322 | 6160 |
| 81 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +319 | 2302 |
| 82 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +313 | 1632 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +312 | 14278 |
| 84 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +306 | 21374 |
| 85 | [tw93/Mole](https://github.com/tw93/Mole) | +303 | 36870 |
| 86 | [kepano/defuddle](https://github.com/kepano/defuddle) | +298 | 5308 |
| 87 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +295 | 2262 |
| 88 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +294 | 1262 |
| 89 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +293 | 28800 |
| 90 | [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | +291 | 24906 |
| 91 | [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | +279 | 1684 |
| 92 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +275 | 14785 |
| 93 | [blader/humanizer](https://github.com/blader/humanizer) | +273 | 9764 |
| 94 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +272 | 1592 |
| 95 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +264 | 29765 |
| 96 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +264 | 4772 |
| 97 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +262 | 14531 |
| 98 | [jackwener/opencli](https://github.com/jackwener/opencli) | +261 | 1338 |
| 99 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +259 | 14272 |
| 100 | [jackwener/xiaohongshu-cli](https://github.com/jackwener/xiaohongshu-cli) | +246 | 1264 |
| 101 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +228 | 2121 |
| 102 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +219 | 1127 |
| 103 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +216 | 2424 |
| 104 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +208 | 15300 |
| 105 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +207 | 16093 |
| 106 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +203 | 1101 |
| 107 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +187 | 6921 |
| 108 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +184 | 47936 |
| 109 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +183 | 22081 |
| 110 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +178 | 1925 |
| 111 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +173 | 2488 |
| 112 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +171 | 2296 |
| 113 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +171 | 44232 |
| 114 | [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli) | +167 | 1295 |
| 115 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +166 | 9829 |
| 116 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +164 | 7350 |
| 117 | [openai/skills](https://github.com/openai/skills) | +160 | 14471 |
| 118 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +159 | 47122 |
| 119 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +154 | 13416 |
| 120 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +149 | 36799 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30430 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +10158 | 51429 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +8876 | 60312 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +8537 | 40206 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8500 | 51199 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8364 | 37766 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7849 | 39995 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +6086 | 74774 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6085 | 27915 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +5786 | 32452 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5661 | 25711 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5617 | 38895 |
| 13 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +5392 | 27665 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5129 | 30662 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4639 | 122870 |
| 16 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4619 | 21168 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4582 | 109881 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4193 | 34243 |
| 19 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4119 | 17492 |
| 20 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4048 | 23827 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3990 | 14785 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3947 | 31754 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3912 | 16585 |
| 24 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3570 | 34276 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3560 | 25249 |
| 26 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3546 | 18093 |
| 27 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3322 | 12450 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3190 | 30388 |
| 29 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3138 | 13357 |
| 30 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +3063 | 25224 |
| 31 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3016 | 25044 |
| 32 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3015 | 69674 |
| 33 | [openai/symphony](https://github.com/openai/symphony) | +2907 | 13187 |
| 34 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2839 | 15099 |
| 35 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2808 | 60117 |
| 36 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2775 | 9951 |
| 37 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2657 | 85286 |
| 38 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2627 | 31453 |
| 39 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2624 | 9609 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2606 | 29376 |
| 41 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2592 | 34148 |
| 42 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2550 | 33891 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2515 | 21886 |
| 44 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2375 | 37330 |
| 45 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2335 | 9701 |
| 46 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2277 | 33878 |
| 47 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2243 | 25572 |
| 48 | [huggingface/skills](https://github.com/huggingface/skills) | +2199 | 9221 |
| 49 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2175 | 15662 |
| 50 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2140 | 147486 |
| 51 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2089 | 10307 |
| 52 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2070 | 10390 |
| 53 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2058 | 9665 |
| 54 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2050 | 30678 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2029 | 23053 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1966 | 21492 |
| 57 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1943 | 7572 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1910 | 9910 |
| 59 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1909 | 10108 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1894 | 6559 |
| 61 | [github/spec-kit](https://github.com/github/spec-kit) | +1872 | 71722 |
| 62 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1854 | 96919 |
| 63 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1838 | 9606 |
| 64 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1803 | 8426 |
| 65 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1787 | 8157 |
| 66 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1763 | 28160 |
| 67 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1739 | 6467 |
| 68 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1717 | 20947 |
| 69 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1708 | 7274 |
| 70 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1707 | 74887 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1702 | 31577 |
| 72 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1700 | 7879 |
| 73 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1693 | 22081 |
| 74 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1676 | 6664 |
| 75 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1668 | 6871 |
| 76 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1659 | 17407 |
| 77 | [tobi/qmd](https://github.com/tobi/qmd) | +1615 | 15851 |
| 78 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1587 | 6263 |
| 79 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1584 | 7981 |
| 80 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1575 | 12715 |
| 81 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1560 | 6921 |
| 82 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1554 | 149018 |
| 83 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1547 | 15300 |
| 84 | [openai/skills](https://github.com/openai/skills) | +1524 | 14471 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1513 | 98536 |
| 86 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1510 | 12507 |
| 87 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1483 | 9095 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1417 | 14278 |
| 89 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1417 | 13944 |
| 90 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1411 | 7272 |
| 91 | [tw93/Mole](https://github.com/tw93/Mole) | +1404 | 36870 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1366 | 6219 |
| 93 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1339 | 5596 |
| 94 | [openai/codex](https://github.com/openai/codex) | +1280 | 61744 |
| 95 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1276 | 17156 |
| 96 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1261 | 43973 |
| 97 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1261 | 37564 |
| 98 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1239 | 35236 |
| 99 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1216 | 12486 |
| 100 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1161 | 5021 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1153 | 28800 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1150 | 16093 |
| 103 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1124 | 5017 |
| 104 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1115 | 22782 |
| 105 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1097 | 87598 |
| 106 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1028 | 6921 |
| 107 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +997 | 12997 |
| 108 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +931 | 6160 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +926 | 5561 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +892 | 35735 |
| 111 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +880 | 13913 |
| 112 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +846 | 13416 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +793 | 61818 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +780 | 45886 |
| 115 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +767 | 36799 |
| 116 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +757 | 47122 |
| 117 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +751 | 9747 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +748 | 5537 |
| 119 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +712 | 4276 |
| 120 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +700 | 3071 |
| 121 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +683 | 33712 |
| 122 | [wshobson/agents](https://github.com/wshobson/agents) | +678 | 31516 |
| 123 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +670 | 23085 |
| 124 | [docling-project/docling](https://github.com/docling-project/docling) | +668 | 54041 |
| 125 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +664 | 23205 |
| 126 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +658 | 5376 |
| 127 | [google-research/timesfm](https://github.com/google-research/timesfm) | +653 | 10065 |
| 128 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +650 | 27981 |
| 129 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +645 | 15652 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +630 | 47936 |
| 131 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +607 | 2076 |
| 132 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +602 | 3182 |
| 133 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +594 | 16313 |
| 134 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +584 | 2063 |
| 135 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +578 | 30590 |
| 136 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +569 | 2488 |
| 137 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +566 | 7945 |
| 138 | [aden-hive/hive](https://github.com/aden-hive/hive) | +532 | 9536 |
| 139 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +531 | 5128 |
| 140 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +530 | 9829 |
| 141 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +530 | 44545 |
| 142 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +526 | 4582 |
| 143 | [google/langextract](https://github.com/google/langextract) | +521 | 33636 |
| 144 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +519 | 44232 |
| 145 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +517 | 2126 |
| 146 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +509 | 1948 |
| 147 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +502 | 3292 |
| 148 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +499 | 9649 |
| 149 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +493 | 14448 |
| 150 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +486 | 15189 |
| 151 | [eooce/python-ws](https://github.com/eooce/python-ws) | +483 | 1819 |
| 152 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +477 | 18254 |
| 153 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +474 | 39841 |
| 154 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +468 | 1957 |
| 155 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +457 | 26682 |
| 156 | [openclaw/skills](https://github.com/openclaw/skills) | +454 | 3006 |
| 157 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +452 | 14272 |
| 158 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +451 | 2082 |
| 159 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +438 | 1925 |
| 160 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +431 | 3783 |
| 161 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +419 | 1614 |
| 162 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +413 | 5214 |
| 163 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +401 | 10493 |
| 164 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +400 | 2926 |
| 165 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +400 | 9684 |
| 166 | [searxng/searxng](https://github.com/searxng/searxng) | +398 | 26664 |
| 167 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +397 | 2121 |
| 168 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +396 | 1563 |
| 169 | [apify/agent-skills](https://github.com/apify/agent-skills) | +396 | 1654 |
| 170 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +387 | 18765 |
| 171 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +379 | 7350 |
| 172 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +373 | 4306 |
| 173 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +370 | 0 |
| 174 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +368 | 3542 |
| 175 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +367 | 2296 |
| 176 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +367 | 24638 |
| 177 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +361 | 3083 |
| 178 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +360 | 5507 |
| 179 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +360 | 6028 |
| 180 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +355 | 2336 |
| 181 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +352 | 10947 |
| 182 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +349 | 24482 |
| 183 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +342 | 1632 |
| 184 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +336 | 5464 |
| 185 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +330 | 2302 |
| 186 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +325 | 1344 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +320 | 10298 |
| 188 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +318 | 1481 |
| 189 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +310 | 13407 |
| 190 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +302 | 1592 |
| 191 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +302 | 3977 |
| 192 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +299 | 1296 |
| 193 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +296 | 1262 |
| 194 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +292 | 2490 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +288 | 3591 |
| 196 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +274 | 2424 |
| 197 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +268 | 1256 |
| 198 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +265 | 29780 |
| 199 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +265 | 1556 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +259 | 36103 |
| 201 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +251 | 21647 |
| 202 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +244 | 954 |
| 203 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +244 | 747 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +244 | 21340 |
| 205 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +225 | 145 |
| 206 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +217 | 2596 |
| 207 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +215 | 1027 |
| 208 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +212 | 1336 |
| 209 | [robinebers/openusage](https://github.com/robinebers/openusage) | +209 | 1528 |
| 210 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +206 | 7057 |
| 211 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +205 | 908 |
| 212 | [usebruno/bruno](https://github.com/usebruno/bruno) | +203 | 41086 |
| 213 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +198 | 8882 |
| 214 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +197 | 28923 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +193 | 40265 |
| 216 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +192 | 811 |
| 217 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +188 | 943 |
| 218 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +186 | 8835 |
| 219 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +183 | 646 |
| 220 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +182 | 5167 |
| 221 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +178 | 902 |
| 222 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +176 | 25349 |
| 223 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +176 | 695 |
| 224 | [decolua/9router](https://github.com/decolua/9router) | +169 | 1021 |
| 225 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +162 | 663 |
| 226 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +155 | 575 |
| 227 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +154 | 2426 |
| 228 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +153 | 698 |
| 229 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +153 | 22770 |
| 230 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +152 | 885 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +151 | 1411 |
| 232 | [jgraph/drawio](https://github.com/jgraph/drawio) | +151 | 4188 |
| 233 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +151 | 33000 |
| 234 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +149 | 893 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +144 | 2032 |
| 236 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +143 | 5166 |
| 237 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +140 | 835 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +140 | 25963 |
| 239 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +140 | 1095 |
| 240 | [es617/claude-replay](https://github.com/es617/claude-replay) | +139 | 535 |
| 241 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +139 | 1467 |
| 242 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +134 | 1963 |
| 243 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +131 | 1636 |
| 244 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +129 | 478 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +129 | 12116 |
| 246 | [is-a-dev/register](https://github.com/is-a-dev/register) | +127 | 9994 |
| 247 | [qist/tvbox](https://github.com/qist/tvbox) | +127 | 8530 |
| 248 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +124 | 28980 |
| 249 | [4ier/neo](https://github.com/4ier/neo) | +121 | 607 |
| 250 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +118 | 854 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +117 | 1287 |
| 252 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +117 | 35473 |
| 253 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +115 | 10067 |
| 254 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +115 | 48784 |
| 255 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +114 | 3468 |
| 256 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +113 | 3251 |
| 257 | [fmhy/edit](https://github.com/fmhy/edit) | +111 | 8532 |
| 258 | [microg/GmsCore](https://github.com/microg/GmsCore) | +111 | 12592 |
| 259 | [expo/skills](https://github.com/expo/skills) | +110 | 1484 |
| 260 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +109 | 7019 |
| 261 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +107 | 424 |
| 262 | [lklynet/aurral](https://github.com/lklynet/aurral) | +105 | 870 |
| 263 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +103 | 436 |
| 264 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +103 | 3180 |
| 265 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 266 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +103 | 37313 |
| 267 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +102 | 11157 |
| 268 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +101 | 416 |
| 269 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +100 | 780 |
| 270 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 881 |
| 271 | [skylot/jadx](https://github.com/skylot/jadx) | +99 | 47365 |
| 272 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +98 | 1007 |
| 273 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +97 | 606 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +94 | 8783 |
| 275 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +93 | 476 |
| 276 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +89 | 363 |
| 277 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +89 | 927 |
| 278 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +87 | 543 |
| 279 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +84 | 563 |
| 280 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +84 | 328 |
| 281 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +83 | 479 |
| 282 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +82 | 836 |
| 283 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +82 | 26906 |
| 284 | [apache/kafka](https://github.com/apache/kafka) | +80 | 32043 |
| 285 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +79 | 3025 |
| 286 | [openjdk/jdk](https://github.com/openjdk/jdk) | +78 | 22731 |
| 287 | [idinging/freemail](https://github.com/idinging/freemail) | +76 | 1037 |
| 288 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +76 | 352 |
| 289 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +75 | 424 |
| 290 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +75 | 977 |
| 291 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +75 | 8222 |
| 292 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1332 |
| 293 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +72 | 425 |
| 294 | [f/agentlytics](https://github.com/f/agentlytics) | +72 | 340 |
| 295 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +72 | 21372 |
| 296 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +70 | 1326 |
| 297 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +70 | 6088 |
| 298 | [freeok/so-novel](https://github.com/freeok/so-novel) | +66 | 6362 |
| 299 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +66 | 7619 |
| 300 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +63 | 908 |
