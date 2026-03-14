---
title: "2026-03-14 GitHub增长趋势报告"
description: "1.agency-agents+946 2.autoresearch+567 3.MiroFish+479 4.browser+413 5.OpenViking+318"
date: 2026-03-14T20:31:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-14 20:31:23

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
        'daily': {"categories": ["vectorize-io/hindsight", "gsd-build/get-shit-done", "AlexsJones/llmfit", "systemdesign42/system-design-academy", "ZhuLinsen/daily_stock_analysis", "p-e-w/heretic", "shareAI-lab/learn-claude-code", "NawfalMotii79/PLFM_RADAR", "AstrBotDevs/AstrBot", "pbakaus/impeccable", "promptfoo/promptfoo", "alibaba/page-agent", "paperclipai/paperclip", "shanraisshan/claude-code-best-practice", "microsoft/BitNet", "volcengine/OpenViking", "lightpanda-io/browser", "666ghj/MiroFish", "karpathy/autoresearch", "msitarzewski/agency-agents"], "data": [120, 129, 134, 138, 141, 151, 182, 188, 215, 233, 236, 269, 283, 288, 308, 318, 413, 479, 567, 946]},
        'weekly': {"categories": ["microsoft/BitNet", "AstrBotDevs/AstrBot", "openai/symphony", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "pingdotgg/t3code", "nikopueringer/CorridorKey", "googleworkspace/cli", "pbakaus/impeccable", "anthropics/skills", "alibaba/page-agent", "VoltAgent/awesome-openclaw-skills", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "666ghj/MiroFish", "paperclipai/paperclip", "msitarzewski/agency-agents", "karpathy/autoresearch", "openclaw/openclaw"], "data": [1024, 1036, 1051, 1064, 1114, 1157, 1245, 1294, 1377, 1475, 1555, 1574, 1593, 1876, 2846, 3412, 3678, 6060, 6945, 9012]},
        'monthly': {"categories": ["HKUDS/nanobot", "gsd-build/get-shit-done", "qwibitai/nanoclaw", "googleworkspace/cli", "x1xhlol/system-prompts-and-models-of-ai-tools", "anomalyco/opencode", "D4Vinci/Scrapling", "paperclipai/paperclip", "sipeed/picoclaw", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "karpathy/autoresearch", "affaan-m/everything-claude-code", "obra/superpowers", "zeroclaw-labs/zeroclaw", "msitarzewski/agency-agents", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [4034, 4050, 4127, 4446, 4617, 4729, 4902, 5094, 5662, 5721, 5969, 6034, 7051, 7673, 7843, 7995, 8188, 8410, 8443, 32392]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +946 | 43348 |
| 2 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +567 | 33800 |
| 3 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +479 | 23630 |
| 4 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +413 | 16909 |
| 5 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +318 | 10275 |
| 6 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +308 | 34530 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +288 | 15998 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +283 | 23189 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +269 | 8297 |
| 10 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +236 | 15845 |
| 11 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +233 | 8064 |
| 12 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +215 | 24482 |
| 13 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +188 | 1528 |
| 14 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +182 | 26894 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +151 | 13565 |
| 16 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +141 | 20056 |
| 17 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +138 | 22221 |
| 18 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +134 | 16603 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +129 | 30003 |
| 20 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +120 | 3902 |
| 21 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +117 | 37841 |
| 22 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +115 | 2648 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +114 | 7629 |
| 24 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +112 | 37354 |
| 25 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +110 | 43973 |
| 26 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +109 | 11195 |
| 27 | [moltlaunch/cashclaw](https://github.com/moltlaunch/cashclaw) | +108 | 484 |
| 28 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +108 | 7226 |
| 29 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +107 | 7089 |
| 30 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +104 | 22829 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9012 | 224760 |
| 2 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +6945 | 33800 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +6060 | 43348 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3678 | 23189 |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3412 | 23630 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2846 | 51199 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +1876 | 60312 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1593 | 36579 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1574 | 37354 |
| 10 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1555 | 8297 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1475 | 74774 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1377 | 8064 |
| 13 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +1294 | 20261 |
| 14 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1245 | 7226 |
| 15 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1157 | 6287 |
| 16 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1114 | 37841 |
| 17 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1064 | 24726 |
| 18 | [openai/symphony](https://github.com/openai/symphony) | +1051 | 12553 |
| 19 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1036 | 24482 |
| 20 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1024 | 34530 |
| 21 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +997 | 6022 |
| 22 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +972 | 7089 |
| 23 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +967 | 6972 |
| 24 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +962 | 30510 |
| 25 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +934 | 29583 |
| 26 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +905 | 26894 |
| 27 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +897 | 9999 |
| 28 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +891 | 33548 |
| 29 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +889 | 30003 |
| 30 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +873 | 15845 |
| 31 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +850 | 6311 |
| 32 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +832 | 33463 |
| 33 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +826 | 16603 |
| 34 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +824 | 10275 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +775 | 20056 |
| 36 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +741 | 16165 |
| 37 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +727 | 16910 |
| 38 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +720 | 7629 |
| 39 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +714 | 15998 |
| 40 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +712 | 43973 |
| 41 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +687 | 27027 |
| 42 | [jundot/omlx](https://github.com/jundot/omlx) | +671 | 4555 |
| 43 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +657 | 24297 |
| 44 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +654 | 28129 |
| 45 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +648 | 14378 |
| 46 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +629 | 34148 |
| 47 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +619 | 22829 |
| 48 | [m1k1o/neko](https://github.com/m1k1o/neko) | +599 | 19952 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +575 | 23709 |
| 50 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +561 | 2822 |
| 51 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +538 | 37330 |
| 52 | [openai/skills](https://github.com/openai/skills) | +536 | 14187 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +515 | 16429 |
| 54 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +512 | 9105 |
| 55 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +509 | 35735 |
| 56 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +508 | 33878 |
| 57 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +499 | 12920 |
| 58 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +495 | 13565 |
| 59 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +491 | 30578 |
| 60 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +489 | 11317 |
| 61 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +476 | 5650 |
| 62 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +464 | 24694 |
| 63 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +452 | 5439 |
| 64 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +447 | 5078 |
| 65 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +440 | 21990 |
| 66 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +426 | 12039 |
| 67 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +424 | 5321 |
| 68 | [tobi/qmd](https://github.com/tobi/qmd) | +418 | 15313 |
| 69 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +406 | 2648 |
| 70 | [superset-sh/superset](https://github.com/superset-sh/superset) | +402 | 6980 |
| 71 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +380 | 27493 |
| 72 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +378 | 27164 |
| 73 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +378 | 13415 |
| 74 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +374 | 11944 |
| 75 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +372 | 11195 |
| 76 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +370 | 4108 |
| 77 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +365 | 4699 |
| 78 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +364 | 2660 |
| 79 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +356 | 8911 |
| 80 | [viperrcrypto/Siftly](https://github.com/viperrcrypto/Siftly) | +354 | 1474 |
| 81 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +339 | 7545 |
| 82 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +326 | 2667 |
| 83 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +325 | 5893 |
| 84 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +316 | 11241 |
| 85 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +313 | 6692 |
| 86 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +303 | 21024 |
| 87 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +302 | 28170 |
| 88 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +299 | 30678 |
| 89 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +297 | 4333 |
| 90 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +294 | 4076 |
| 91 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +294 | 10223 |
| 92 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +286 | 14865 |
| 93 | [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) | +283 | 2233 |
| 94 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +283 | 5116 |
| 95 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +282 | 20751 |
| 96 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +278 | 4355 |
| 97 | [google/A2UI](https://github.com/google/A2UI) | +266 | 13180 |
| 98 | [thesysdev/crayon](https://github.com/thesysdev/crayon) | +263 | 1665 |
| 99 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +252 | 15654 |
| 100 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +243 | 3902 |
| 101 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +243 | 7810 |
| 102 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +227 | 15593 |
| 103 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +222 | 2077 |
| 104 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +214 | 1528 |
| 105 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +205 | 2848 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +203 | 25155 |
| 107 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +197 | 1109 |
| 108 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +189 | 1986 |
| 109 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +187 | 1675 |
| 110 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +184 | 36799 |
| 111 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +180 | 47122 |
| 112 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +180 | 14454 |
| 113 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +176 | 13098 |
| 114 | [wshobson/agents](https://github.com/wshobson/agents) | +175 | 31234 |
| 115 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +170 | 2325 |
| 116 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +169 | 15180 |
| 117 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +167 | 47936 |
| 118 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +163 | 44232 |
| 119 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +152 | 21494 |
| 120 | [openclaw/skills](https://github.com/openclaw/skills) | +152 | 2840 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32392 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8443 | 37841 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8410 | 36579 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +8188 | 43349 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7995 | 27027 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +7843 | 60312 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7673 | 51199 |
| 8 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +7051 | 33801 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6034 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5969 | 24726 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5721 | 37354 |
| 12 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +5662 | 24694 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5094 | 23189 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4902 | 29583 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4729 | 109881 |
| 16 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4617 | 122870 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4446 | 20261 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4127 | 22829 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4050 | 30003 |
| 20 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4034 | 33463 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4014 | 33548 |
| 22 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4006 | 16603 |
| 23 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +4000 | 24297 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3895 | 14378 |
| 25 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3788 | 23630 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3372 | 13218 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3268 | 12920 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3146 | 23710 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3035 | 11317 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3025 | 15998 |
| 31 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2969 | 69674 |
| 32 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2897 | 33516 |
| 33 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2840 | 60117 |
| 34 | [openai/symphony](https://github.com/openai/symphony) | +2752 | 12553 |
| 35 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2695 | 9491 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2676 | 85286 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2571 | 9342 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2553 | 28129 |
| 39 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2502 | 8929 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2500 | 34148 |
| 41 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2466 | 26894 |
| 42 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2454 | 30510 |
| 43 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2406 | 9999 |
| 44 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2406 | 37330 |
| 45 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2292 | 33878 |
| 46 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2209 | 20056 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2197 | 9105 |
| 48 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2152 | 13565 |
| 49 | [huggingface/skills](https://github.com/huggingface/skills) | +2151 | 8994 |
| 50 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2071 | 24482 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2035 | 147486 |
| 52 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2034 | 96919 |
| 53 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2013 | 9384 |
| 54 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1935 | 7197 |
| 55 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1910 | 10275 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1899 | 21024 |
| 57 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1882 | 9840 |
| 58 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1871 | 21990 |
| 59 | [github/spec-kit](https://github.com/github/spec-kit) | +1854 | 71722 |
| 60 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1841 | 30678 |
| 61 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1825 | 6972 |
| 62 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1808 | 6287 |
| 63 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1748 | 6523 |
| 64 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1733 | 7810 |
| 65 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1709 | 6309 |
| 66 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1703 | 7545 |
| 67 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1691 | 74887 |
| 68 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1690 | 21494 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1678 | 27493 |
| 70 | [tobi/qmd](https://github.com/tobi/qmd) | +1661 | 15313 |
| 71 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1653 | 11944 |
| 72 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1633 | 6721 |
| 73 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1630 | 8297 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1614 | 30578 |
| 75 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1601 | 5755 |
| 76 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1596 | 149018 |
| 77 | [openai/skills](https://github.com/openai/skills) | +1585 | 14187 |
| 78 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1583 | 7629 |
| 79 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1539 | 12039 |
| 80 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1514 | 7089 |
| 81 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1505 | 14865 |
| 82 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1500 | 8064 |
| 83 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1500 | 5869 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1499 | 16429 |
| 85 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1485 | 33712 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1457 | 98536 |
| 87 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1427 | 6980 |
| 88 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1422 | 13858 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1420 | 13415 |
| 90 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1416 | 6311 |
| 91 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1382 | 7226 |
| 92 | [tw93/Mole](https://github.com/tw93/Mole) | +1366 | 36870 |
| 93 | [maderix/ANE](https://github.com/maderix/ANE) | +1356 | 6170 |
| 94 | [openai/codex](https://github.com/openai/codex) | +1336 | 61744 |
| 95 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1336 | 37564 |
| 96 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1274 | 5321 |
| 97 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1232 | 15654 |
| 98 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1177 | 6692 |
| 99 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1161 | 22646 |
| 100 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1130 | 34530 |
| 101 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1128 | 43973 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1118 | 28170 |
| 103 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1092 | 87598 |
| 104 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1088 | 6022 |
| 105 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1059 | 4699 |
| 106 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1031 | 12914 |
| 107 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +990 | 4355 |
| 108 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +977 | 15845 |
| 109 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +945 | 25155 |
| 110 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +923 | 11195 |
| 111 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +839 | 13098 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +819 | 5650 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +811 | 61818 |
| 114 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +776 | 5043 |
| 115 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +774 | 22914 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +763 | 36799 |
| 117 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +752 | 35735 |
| 118 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +751 | 47122 |
| 119 | [google/langextract](https://github.com/google/langextract) | +751 | 33636 |
| 120 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +749 | 9634 |
| 121 | [docling-project/docling](https://github.com/docling-project/docling) | +726 | 54041 |
| 122 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +716 | 22992 |
| 123 | [jundot/omlx](https://github.com/jundot/omlx) | +700 | 4555 |
| 124 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +696 | 4108 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +687 | 31234 |
| 126 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +653 | 2848 |
| 127 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +651 | 5078 |
| 128 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +651 | 14454 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +650 | 10036 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +631 | 15593 |
| 131 | [aden-hive/hive](https://github.com/aden-hive/hive) | +604 | 9424 |
| 132 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +602 | 7851 |
| 133 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +596 | 47936 |
| 134 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +592 | 14331 |
| 135 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +583 | 16054 |
| 136 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +583 | 17704 |
| 137 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +578 | 1983 |
| 138 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +575 | 2275 |
| 139 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +571 | 1995 |
| 140 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +547 | 30590 |
| 141 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +543 | 9504 |
| 142 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +529 | 2325 |
| 143 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +511 | 2063 |
| 144 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +506 | 1933 |
| 145 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +503 | 3197 |
| 146 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +500 | 44545 |
| 147 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +492 | 7377 |
| 148 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +485 | 15022 |
| 149 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +483 | 44232 |
| 150 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +475 | 16095 |
| 151 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +471 | 3516 |
| 152 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +469 | 1871 |
| 153 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +466 | 4513 |
| 154 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +463 | 1473 |
| 155 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +462 | 9092 |
| 156 | [eooce/python-ws](https://github.com/eooce/python-ws) | +460 | 1749 |
| 157 | [openclaw/skills](https://github.com/openclaw/skills) | +459 | 2840 |
| 158 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +458 | 27164 |
| 159 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +456 | 18116 |
| 160 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +456 | 39841 |
| 161 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +443 | 11268 |
| 162 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +433 | 2648 |
| 163 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +433 | 1313 |
| 164 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +427 | 26392 |
| 165 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +426 | 3902 |
| 166 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +425 | 5096 |
| 167 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +411 | 3637 |
| 168 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +408 | 1541 |
| 169 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +401 | 1722 |
| 170 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +400 | 18630 |
| 171 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +398 | 4129 |
| 172 | [microsoft/qlib](https://github.com/microsoft/qlib) | +396 | 37792 |
| 173 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +396 | 10456 |
| 174 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +395 | 2510 |
| 175 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +393 | 1784 |
| 176 | [searxng/searxng](https://github.com/searxng/searxng) | +390 | 26491 |
| 177 | [apify/agent-skills](https://github.com/apify/agent-skills) | +388 | 1618 |
| 178 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +383 | 1534 |
| 179 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +372 | 9497 |
| 180 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +371 | 5860 |
| 181 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +368 | 11267 |
| 182 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +363 | 1675 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +358 | 24331 |
| 184 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +355 | 10812 |
| 185 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +354 | 5395 |
| 186 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +343 | 2853 |
| 187 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +339 | 1497 |
| 188 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +335 | 10796 |
| 189 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +331 | 732 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +328 | 10169 |
| 191 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +319 | 2077 |
| 192 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +309 | 2562 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +306 | 3453 |
| 194 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +304 | 1399 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +300 | 1273 |
| 196 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +290 | 1966 |
| 197 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +285 | 3859 |
| 198 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +282 | 1224 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +276 | 4474 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +272 | 36103 |
| 201 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +254 | 942 |
| 202 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +253 | 21250 |
| 203 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +250 | 1257 |
| 204 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +247 | 21539 |
| 205 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +246 | 29780 |
| 206 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +243 | 13208 |
| 207 | [robinebers/openusage](https://github.com/robinebers/openusage) | +235 | 1479 |
| 208 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +232 | 911 |
| 209 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +229 | 1047 |
| 210 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +224 | 863 |
| 211 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 144 |
| 212 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +207 | 664 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +206 | 40265 |
| 214 | [usebruno/bruno](https://github.com/usebruno/bruno) | +205 | 41086 |
| 215 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +204 | 8845 |
| 216 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +203 | 5454 |
| 217 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +203 | 6869 |
| 218 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +203 | 28831 |
| 219 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +198 | 606 |
| 220 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +193 | 8814 |
| 221 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +183 | 833 |
| 222 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +181 | 5082 |
| 223 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +176 | 689 |
| 224 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +173 | 25325 |
| 225 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +165 | 569 |
| 226 | [decolua/9router](https://github.com/decolua/9router) | +161 | 921 |
| 227 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +161 | 22705 |
| 228 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +159 | 33000 |
| 229 | [VonChange/utao](https://github.com/VonChange/utao) | +157 | 3918 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +156 | 682 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +152 | 1395 |
| 232 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +152 | 556 |
| 233 | [qist/tvbox](https://github.com/qist/tvbox) | +149 | 8499 |
| 234 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +149 | 1950 |
| 235 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +148 | 2376 |
| 236 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +146 | 1433 |
| 237 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +145 | 661 |
| 238 | [jgraph/drawio](https://github.com/jgraph/drawio) | +145 | 4123 |
| 239 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +144 | 844 |
| 240 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +144 | 5110 |
| 241 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +138 | 25923 |
| 242 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +134 | 1553 |
| 243 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +134 | 534 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +130 | 12039 |
| 245 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +129 | 39596 |
| 246 | [lklynet/aurral](https://github.com/lklynet/aurral) | +128 | 867 |
| 247 | [is-a-dev/register](https://github.com/is-a-dev/register) | +127 | 9970 |
| 248 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +125 | 802 |
| 249 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +124 | 48784 |
| 250 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +122 | 451 |
| 251 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +121 | 3434 |
| 252 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +120 | 996 |
| 253 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +119 | 6980 |
| 254 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +119 | 1858 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +118 | 1233 |
| 256 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +118 | 37313 |
| 257 | [fmhy/edit](https://github.com/fmhy/edit) | +117 | 8473 |
| 258 | [4ier/neo](https://github.com/4ier/neo) | +116 | 582 |
| 259 | [expo/skills](https://github.com/expo/skills) | +115 | 1455 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +115 | 9998 |
| 261 | [microg/GmsCore](https://github.com/microg/GmsCore) | +114 | 12556 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +112 | 3217 |
| 263 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +110 | 35473 |
| 264 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +108 | 788 |
| 265 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +107 | 753 |
| 266 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +106 | 3148 |
| 267 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +105 | 865 |
| 268 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +99 | 805 |
| 269 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +98 | 386 |
| 270 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +98 | 497 |
| 271 | [skylot/jadx](https://github.com/skylot/jadx) | +97 | 47365 |
| 272 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +96 | 3076 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11107 |
| 274 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 960 |
| 275 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +90 | 384 |
| 276 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +88 | 512 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +88 | 26851 |
| 278 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +85 | 454 |
| 279 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +85 | 561 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +84 | 8727 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +84 | 2983 |
| 282 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +82 | 313 |
| 283 | [apache/kafka](https://github.com/apache/kafka) | +82 | 32043 |
| 284 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +81 | 516 |
| 285 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +80 | 318 |
| 286 | [openjdk/jdk](https://github.com/openjdk/jdk) | +78 | 22700 |
| 287 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +77 | 687 |
| 288 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +77 | 1012 |
| 289 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +77 | 950 |
| 290 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +75 | 400 |
| 291 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1328 |
| 292 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +71 | 329 |
| 293 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +69 | 385 |
| 294 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +69 | 21348 |
| 295 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +69 | 45263 |
| 296 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +69 | 7592 |
| 297 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +68 | 1303 |
| 298 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +65 | 395 |
| 299 | [idinging/freemail](https://github.com/idinging/freemail) | +65 | 996 |
| 300 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +65 | 8181 |
