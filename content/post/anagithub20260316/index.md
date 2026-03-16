---
title: "2026-03-16 GitHub增长趋势报告"
description: "1.MiroFish+817 2.agency-agents+716 3.autoresearch+551 4.paperclip+525 5.OpenViking+482"
date: 2026-03-16T20:41:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-16 20:41:05

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
        'daily': {"categories": ["EdoStra/Marketing-for-Founders", "anthropics/claude-plugins-official", "alibaba/page-agent", "systemdesign42/system-design-academy", "TraderAlice/OpenAlice", "nextlevelbuilder/ui-ux-pro-max-skill", "ZhuLinsen/daily_stock_analysis", "thedotmack/claude-mem", "p-e-w/heretic", "NawfalMotii79/PLFM_RADAR", "langchain-ai/deepagents", "shanraisshan/claude-code-best-practice", "shareAI-lab/learn-claude-code", "abhigyanpatwari/GitNexus", "lightpanda-io/browser", "volcengine/OpenViking", "paperclipai/paperclip", "karpathy/autoresearch", "msitarzewski/agency-agents", "666ghj/MiroFish"], "data": [151, 152, 155, 162, 166, 192, 206, 211, 213, 231, 263, 298, 343, 412, 441, 482, 525, 551, 716, 817]},
        'weekly': {"categories": ["andrewyng/context-hub", "NousResearch/hermes-agent", "shanraisshan/claude-code-best-practice", "shareAI-lab/learn-claude-code", "VoltAgent/awesome-openclaw-skills", "AstrBotDevs/AstrBot", "microsoft/BitNet", "promptfoo/promptfoo", "pbakaus/impeccable", "anthropics/skills", "alibaba/page-agent", "lightpanda-io/browser", "volcengine/OpenViking", "affaan-m/everything-claude-code", "paperclipai/paperclip", "obra/superpowers", "666ghj/MiroFish", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [1019, 1035, 1047, 1054, 1057, 1080, 1109, 1112, 1238, 1382, 1472, 1536, 1756, 2184, 2484, 2648, 4112, 4781, 6238, 6323]},
        'monthly': {"categories": ["qwibitai/nanoclaw", "moeru-ai/airi", "AlexsJones/llmfit", "googleworkspace/cli", "anomalyco/opencode", "x1xhlol/system-prompts-and-models-of-ai-tools", "D4Vinci/Scrapling", "666ghj/MiroFish", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "paperclipai/paperclip", "anthropics/skills", "zeroclaw-labs/zeroclaw", "koala73/worldmonitor", "affaan-m/everything-claude-code", "karpathy/autoresearch", "ruvnet/RuView", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4095, 4157, 4158, 4584, 4638, 4648, 5072, 5335, 5650, 5814, 5864, 6068, 6289, 7848, 8185, 8267, 8385, 8594, 9779, 31214]}
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
| 1 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +817 | 29686 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +716 | 48968 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +551 | 38236 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +525 | 26551 |
| 5 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +482 | 13965 |
| 6 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +441 | 20095 |
| 7 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +412 | 15467 |
| 8 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +343 | 29215 |
| 9 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +298 | 17727 |
| 10 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +263 | 12716 |
| 11 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +231 | 3003 |
| 12 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +213 | 15217 |
| 13 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +211 | 30678 |
| 14 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +206 | 21396 |
| 15 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +192 | 34148 |
| 16 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +166 | 2178 |
| 17 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +162 | 23479 |
| 18 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +155 | 9380 |
| 19 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +152 | 12343 |
| 20 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +151 | 4743 |
| 21 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +149 | 39293 |
| 22 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +141 | 12255 |
| 23 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +140 | 1285 |
| 24 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +137 | 2246 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +135 | 1712 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +133 | 9225 |
| 27 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +132 | 31038 |
| 28 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +129 | 16785 |
| 29 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +126 | 7999 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +126 | 24621 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +6323 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +6238 | 48968 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +4781 | 38236 |
| 4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +4112 | 29687 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +2648 | 60312 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2484 | 26551 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2184 | 51199 |
| 8 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1756 | 13965 |
| 9 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1536 | 20095 |
| 10 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1472 | 9380 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1382 | 74774 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1238 | 9225 |
| 13 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1112 | 16785 |
| 14 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1109 | 34886 |
| 15 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1080 | 25256 |
| 16 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1057 | 38331 |
| 17 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1054 | 29215 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1047 | 17727 |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1035 | 7999 |
| 20 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1019 | 6986 |
| 21 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1018 | 37391 |
| 22 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +908 | 39293 |
| 23 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +904 | 15218 |
| 24 | [jundot/omlx](https://github.com/jundot/omlx) | +858 | 5287 |
| 25 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +845 | 31155 |
| 26 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +842 | 7797 |
| 27 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +782 | 43973 |
| 28 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +780 | 15467 |
| 29 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +763 | 20894 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +760 | 31038 |
| 31 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +742 | 21396 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +728 | 34148 |
| 33 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +707 | 17266 |
| 34 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +675 | 25411 |
| 35 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +651 | 3003 |
| 36 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +634 | 30261 |
| 37 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +618 | 24622 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +618 | 28902 |
| 39 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +605 | 33994 |
| 40 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +602 | 12343 |
| 41 | [openai/symphony](https://github.com/openai/symphony) | +592 | 13018 |
| 42 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +570 | 3085 |
| 43 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +565 | 24925 |
| 44 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +549 | 27818 |
| 45 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +544 | 23505 |
| 46 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +543 | 8643 |
| 47 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +525 | 27441 |
| 48 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +525 | 34042 |
| 49 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +524 | 4770 |
| 50 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +508 | 37330 |
| 51 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +507 | 23479 |
| 52 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +507 | 12255 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +503 | 17060 |
| 54 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +492 | 12716 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +478 | 22728 |
| 56 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +476 | 6711 |
| 57 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +470 | 30678 |
| 58 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +463 | 3199 |
| 59 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +458 | 35735 |
| 60 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +448 | 5388 |
| 61 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +445 | 33878 |
| 62 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +444 | 2246 |
| 63 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +440 | 5993 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +440 | 31122 |
| 65 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +438 | 3211 |
| 66 | [ParthJadhav/app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots) | +430 | 2819 |
| 67 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +415 | 45886 |
| 68 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +408 | 25054 |
| 69 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +391 | 6025 |
| 70 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +385 | 4743 |
| 71 | [tobi/qmd](https://github.com/tobi/qmd) | +377 | 15681 |
| 72 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +370 | 9491 |
| 73 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +364 | 4862 |
| 74 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +361 | 10197 |
| 75 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +356 | 12459 |
| 76 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +345 | 12319 |
| 77 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +344 | 27906 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +327 | 13971 |
| 79 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +324 | 14660 |
| 80 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +313 | 6476 |
| 81 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +303 | 7783 |
| 82 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +301 | 1285 |
| 83 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 28562 |
| 84 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +296 | 1512 |
| 85 | [tw93/Mole](https://github.com/tw93/Mole) | +296 | 36870 |
| 86 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +293 | 1447 |
| 87 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +290 | 4263 |
| 88 | [kepano/defuddle](https://github.com/kepano/defuddle) | +284 | 5182 |
| 89 | [google/A2UI](https://github.com/google/A2UI) | +281 | 13282 |
| 90 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +279 | 1127 |
| 91 | [blader/humanizer](https://github.com/blader/humanizer) | +279 | 9543 |
| 92 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +276 | 4631 |
| 93 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +275 | 7406 |
| 94 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +267 | 2178 |
| 95 | [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | +264 | 1515 |
| 96 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +263 | 14337 |
| 97 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +254 | 1712 |
| 98 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +254 | 14183 |
| 99 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +252 | 1862 |
| 100 | [jackwener/xiaohongshu-cli](https://github.com/jackwener/xiaohongshu-cli) | +238 | 1218 |
| 101 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +234 | 15162 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +227 | 15953 |
| 103 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +226 | 15019 |
| 104 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +213 | 6845 |
| 105 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +210 | 1686 |
| 106 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +193 | 2130 |
| 107 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +190 | 1881 |
| 108 | [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli) | +188 | 1197 |
| 109 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +186 | 2261 |
| 110 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +177 | 44232 |
| 111 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +176 | 2425 |
| 112 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +176 | 47936 |
| 113 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +175 | 21901 |
| 114 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +169 | 892 |
| 115 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +166 | 13277 |
| 116 | [openai/skills](https://github.com/openai/skills) | +166 | 14363 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +161 | 47122 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +161 | 36799 |
| 119 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +156 | 7947 |
| 120 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +155 | 9705 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +31214 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +9779 | 48968 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +8594 | 60312 |
| 4 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8385 | 37392 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +8267 | 38236 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8185 | 51199 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7848 | 39293 |
| 8 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6289 | 27441 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6068 | 74774 |
| 10 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5864 | 26551 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5814 | 25411 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5650 | 38331 |
| 13 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +5335 | 29687 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5072 | 30261 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4648 | 122870 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4638 | 109881 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4584 | 20894 |
| 18 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4158 | 17266 |
| 19 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4157 | 34042 |
| 20 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4095 | 23505 |
| 21 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4015 | 31038 |
| 22 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3969 | 14660 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3789 | 15468 |
| 24 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3749 | 33994 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3698 | 24925 |
| 26 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +3678 | 25054 |
| 27 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3513 | 17727 |
| 28 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3380 | 13320 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3294 | 12255 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3038 | 24622 |
| 31 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3023 | 29215 |
| 32 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3002 | 69674 |
| 33 | [openai/symphony](https://github.com/openai/symphony) | +2882 | 13018 |
| 34 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2773 | 13965 |
| 35 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2769 | 60117 |
| 36 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2758 | 9840 |
| 37 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2683 | 85286 |
| 38 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2637 | 33786 |
| 39 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2614 | 31155 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2601 | 34148 |
| 41 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2588 | 9451 |
| 42 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2567 | 28902 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2457 | 21396 |
| 44 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2376 | 37330 |
| 45 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2308 | 15218 |
| 46 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2302 | 9491 |
| 47 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2274 | 33878 |
| 48 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2263 | 25256 |
| 49 | [huggingface/skills](https://github.com/huggingface/skills) | +2191 | 9149 |
| 50 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2185 | 10197 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2123 | 147486 |
| 52 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2050 | 9532 |
| 53 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2005 | 22728 |
| 54 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1949 | 21360 |
| 55 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1942 | 9380 |
| 56 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1940 | 7250 |
| 57 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1919 | 30678 |
| 58 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1915 | 7406 |
| 59 | [alibaba/zvec](https://github.com/alibaba/zvec) | +1913 | 9011 |
| 60 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1901 | 9984 |
| 61 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1880 | 96919 |
| 62 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1871 | 6476 |
| 63 | [github/spec-kit](https://github.com/github/spec-kit) | +1870 | 71722 |
| 64 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1828 | 9225 |
| 65 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1776 | 7947 |
| 66 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1773 | 6631 |
| 67 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1754 | 7783 |
| 68 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1741 | 7999 |
| 69 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1734 | 8643 |
| 70 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1723 | 6387 |
| 71 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1722 | 27906 |
| 72 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1710 | 21901 |
| 73 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1702 | 74887 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1661 | 31122 |
| 75 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1658 | 6828 |
| 76 | [tobi/qmd](https://github.com/tobi/qmd) | +1647 | 15681 |
| 77 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1628 | 17060 |
| 78 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1593 | 20095 |
| 79 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1568 | 12459 |
| 80 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1561 | 6167 |
| 81 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1555 | 7797 |
| 82 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1554 | 149018 |
| 83 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1543 | 6711 |
| 84 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1539 | 15162 |
| 85 | [openai/skills](https://github.com/openai/skills) | +1537 | 14363 |
| 86 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1512 | 12319 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1486 | 98536 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1426 | 13971 |
| 89 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1422 | 13916 |
| 90 | [tw93/Mole](https://github.com/tw93/Mole) | +1419 | 36870 |
| 91 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1410 | 7176 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1364 | 6200 |
| 93 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1330 | 5534 |
| 94 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1329 | 37564 |
| 95 | [openai/codex](https://github.com/openai/codex) | +1309 | 61744 |
| 96 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1257 | 43973 |
| 97 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1226 | 16785 |
| 98 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1206 | 12343 |
| 99 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1205 | 34886 |
| 100 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1200 | 22751 |
| 101 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1183 | 6986 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1153 | 15953 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1149 | 28562 |
| 104 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1142 | 4862 |
| 105 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1097 | 87598 |
| 106 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1066 | 6845 |
| 107 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1010 | 12967 |
| 108 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +912 | 6025 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +883 | 5287 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +867 | 35735 |
| 111 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +848 | 13277 |
| 112 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +826 | 33712 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +800 | 61818 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +769 | 45886 |
| 115 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +767 | 36799 |
| 116 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +756 | 47122 |
| 117 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +745 | 9705 |
| 118 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +738 | 71086 |
| 119 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +734 | 5388 |
| 120 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +713 | 4243 |
| 121 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +697 | 15019 |
| 122 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +697 | 23018 |
| 123 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +692 | 3015 |
| 124 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +690 | 12716 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +679 | 31418 |
| 126 | [docling-project/docling](https://github.com/docling-project/docling) | +679 | 54041 |
| 127 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +671 | 23114 |
| 128 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +664 | 5185 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +651 | 10052 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +645 | 15632 |
| 131 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +634 | 27818 |
| 132 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +624 | 47936 |
| 133 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +606 | 2060 |
| 134 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +590 | 3085 |
| 135 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +581 | 2032 |
| 136 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +580 | 16209 |
| 137 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +577 | 7911 |
| 138 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +575 | 30590 |
| 139 | [google/langextract](https://github.com/google/langextract) | +572 | 33636 |
| 140 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +571 | 2425 |
| 141 | [aden-hive/hive](https://github.com/aden-hive/hive) | +538 | 9489 |
| 142 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +526 | 9705 |
| 143 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +523 | 44545 |
| 144 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +516 | 9601 |
| 145 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +515 | 2104 |
| 146 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +515 | 5007 |
| 147 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +512 | 44232 |
| 148 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +509 | 1945 |
| 149 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +505 | 14410 |
| 150 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +502 | 3251 |
| 151 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +485 | 15040 |
| 152 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +480 | 4263 |
| 153 | [eooce/python-ws](https://github.com/eooce/python-ws) | +479 | 1799 |
| 154 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +467 | 39841 |
| 155 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +466 | 18193 |
| 156 | [openclaw/skills](https://github.com/openclaw/skills) | +454 | 2941 |
| 157 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +452 | 1905 |
| 158 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +447 | 14183 |
| 159 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +441 | 26560 |
| 160 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +428 | 1881 |
| 161 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +427 | 2320 |
| 162 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +426 | 1313 |
| 163 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +417 | 3721 |
| 164 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +415 | 5173 |
| 165 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +415 | 1591 |
| 166 | [searxng/searxng](https://github.com/searxng/searxng) | +403 | 26608 |
| 167 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +402 | 10485 |
| 168 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +392 | 1555 |
| 169 | [apify/agent-skills](https://github.com/apify/agent-skills) | +392 | 1647 |
| 170 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +392 | 3535 |
| 171 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +391 | 18720 |
| 172 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +389 | 9599 |
| 173 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +384 | 4247 |
| 174 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +378 | 11323 |
| 175 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +370 | 1686 |
| 176 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +368 | 24640 |
| 177 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +365 | 2261 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +365 | 5966 |
| 179 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +363 | 7214 |
| 180 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +361 | 5462 |
| 181 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +359 | 24431 |
| 182 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +353 | 2985 |
| 183 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +327 | 10255 |
| 184 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +325 | 1539 |
| 185 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +323 | 1512 |
| 186 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +321 | 1325 |
| 187 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +319 | 1461 |
| 188 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +307 | 13351 |
| 189 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +301 | 1285 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +301 | 3937 |
| 191 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +295 | 1274 |
| 192 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +294 | 1447 |
| 193 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +292 | 1976 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +290 | 3538 |
| 195 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +285 | 1017 |
| 196 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +277 | 1127 |
| 197 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +266 | 36103 |
| 198 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +258 | 1168 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +258 | 4824 |
| 200 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +258 | 29780 |
| 201 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +256 | 735 |
| 202 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +248 | 21615 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +245 | 21315 |
| 204 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +242 | 950 |
| 205 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +234 | 1315 |
| 206 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +228 | 2588 |
| 207 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +225 | 146 |
| 208 | [robinebers/openusage](https://github.com/robinebers/openusage) | +216 | 1509 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +211 | 41086 |
| 210 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +206 | 6983 |
| 211 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +197 | 8868 |
| 212 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +197 | 28906 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +195 | 40265 |
| 214 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +193 | 8831 |
| 215 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +189 | 831 |
| 216 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +189 | 609 |
| 217 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +187 | 889 |
| 218 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +185 | 664 |
| 219 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +185 | 770 |
| 220 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +184 | 5145 |
| 221 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +182 | 881 |
| 222 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +181 | 635 |
| 223 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +177 | 25340 |
| 224 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +176 | 690 |
| 225 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +170 | 1510 |
| 226 | [decolua/9router](https://github.com/decolua/9router) | +167 | 985 |
| 227 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +160 | 22747 |
| 228 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +156 | 33000 |
| 229 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +153 | 565 |
| 230 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +153 | 2413 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +152 | 1407 |
| 232 | [jgraph/drawio](https://github.com/jgraph/drawio) | +151 | 4174 |
| 233 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +150 | 691 |
| 234 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +147 | 866 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +146 | 2006 |
| 236 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +143 | 5148 |
| 237 | [es617/claude-replay](https://github.com/es617/claude-replay) | +139 | 525 |
| 238 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +139 | 1450 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +137 | 25951 |
| 240 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +137 | 1064 |
| 241 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +133 | 1602 |
| 242 | [qist/tvbox](https://github.com/qist/tvbox) | +132 | 8522 |
| 243 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +129 | 467 |
| 244 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +128 | 28957 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +127 | 12087 |
| 246 | [is-a-dev/register](https://github.com/is-a-dev/register) | +126 | 9986 |
| 247 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +125 | 1906 |
| 248 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +121 | 846 |
| 249 | [4ier/neo](https://github.com/4ier/neo) | +119 | 602 |
| 250 | [lklynet/aurral](https://github.com/lklynet/aurral) | +118 | 871 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +118 | 1273 |
| 252 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +117 | 716 |
| 253 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +116 | 10041 |
| 254 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +115 | 3240 |
| 255 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +114 | 3453 |
| 256 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +114 | 35473 |
| 257 | [fmhy/edit](https://github.com/fmhy/edit) | +113 | 8512 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +113 | 48784 |
| 259 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +112 | 7010 |
| 260 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +112 | 540 |
| 261 | [microg/GmsCore](https://github.com/microg/GmsCore) | +112 | 12571 |
| 262 | [expo/skills](https://github.com/expo/skills) | +111 | 1475 |
| 263 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +107 | 408 |
| 264 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +106 | 773 |
| 265 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +106 | 37313 |
| 266 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +105 | 3168 |
| 267 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +101 | 410 |
| 268 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 420 |
| 269 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +101 | 11136 |
| 270 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 873 |
| 271 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +99 | 990 |
| 272 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +98 | 830 |
| 273 | [skylot/jadx](https://github.com/skylot/jadx) | +98 | 47365 |
| 274 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +95 | 527 |
| 275 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +94 | 589 |
| 276 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +91 | 8760 |
| 277 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +89 | 343 |
| 278 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +87 | 827 |
| 279 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +86 | 911 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +86 | 26886 |
| 281 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +85 | 428 |
| 282 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +84 | 326 |
| 283 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +83 | 467 |
| 284 | [apache/kafka](https://github.com/apache/kafka) | +82 | 32043 |
| 285 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +81 | 546 |
| 286 | [openjdk/jdk](https://github.com/openjdk/jdk) | +81 | 22738 |
| 287 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +79 | 3009 |
| 288 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +76 | 415 |
| 289 | [idinging/freemail](https://github.com/idinging/freemail) | +76 | 1026 |
| 290 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +76 | 971 |
| 291 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +74 | 1331 |
| 292 | [f/agentlytics](https://github.com/f/agentlytics) | +72 | 338 |
| 293 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +71 | 419 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +71 | 1318 |
| 295 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +71 | 21363 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +70 | 8211 |
| 297 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +69 | 7610 |
| 298 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +67 | 6078 |
| 299 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +64 | 12368 |
| 300 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +63 | 908 |
