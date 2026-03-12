---
title: "2026-03-12 GitHub增长趋势报告"
description: "1.agency-agents+831 2.paperclip+488 3.BitNet+385 4.MiroFish+368 5.AstrBot+354"
date: 2026-03-12T20:38:22+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-12 20:38:22

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
        'daily': {"categories": ["hesamsheikh/awesome-openclaw-usecases", "HKUDS/nanobot", "farion1231/cc-switch", "googleworkspace/cli", "bytedance/deer-flow", "koala73/worldmonitor", "nikopueringer/CorridorKey", "openai/symphony", "fishaudio/fish-speech", "ruvnet/RuView", "thesysdev/crayon", "VoltAgent/awesome-openclaw-skills", "NousResearch/hermes-agent", "alibaba/page-agent", "andrewyng/context-hub", "AstrBotDevs/AstrBot", "666ghj/MiroFish", "microsoft/BitNet", "paperclipai/paperclip", "msitarzewski/agency-agents"], "data": [109, 114, 117, 121, 123, 128, 130, 137, 139, 143, 158, 182, 228, 261, 275, 354, 368, 385, 488, 831]},
        'weekly': {"categories": ["nikopueringer/CorridorKey", "alibaba/page-agent", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "D4Vinci/Scrapling", "nearai/ironclaw", "anthropics/skills", "obra/superpowers", "phuryn/pm-skills", "moeru-ai/airi", "ruvnet/RuView", "pingdotgg/t3code", "VoltAgent/awesome-openclaw-skills", "openai/symphony", "666ghj/MiroFish", "googleworkspace/cli", "affaan-m/everything-claude-code", "paperclipai/paperclip", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [1044, 1066, 1259, 1326, 1330, 1341, 1532, 1597, 1684, 1687, 1752, 1759, 1766, 2004, 2665, 2711, 2959, 4138, 5174, 10312]},
        'monthly': {"categories": ["sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "qwibitai/nanoclaw", "HKUDS/nanobot", "googleworkspace/cli", "paperclipai/paperclip", "x1xhlol/system-prompts-and-models-of-ai-tools", "D4Vinci/Scrapling", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "msitarzewski/agency-agents", "sipeed/picoclaw", "affaan-m/everything-claude-code", "obra/superpowers", "zeroclaw-labs/zeroclaw", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3930, 3940, 4226, 4235, 4287, 4573, 4602, 4799, 4869, 5742, 6001, 6035, 6339, 6449, 7469, 7513, 7867, 8251, 8807, 32959]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +831 | 33647 |
| 2 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +488 | 20508 |
| 3 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +385 | 32028 |
| 4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +368 | 18613 |
| 5 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +354 | 22729 |
| 6 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +275 | 5406 |
| 7 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +261 | 5790 |
| 8 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +228 | 6048 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +182 | 36301 |
| 10 | [thesysdev/crayon](https://github.com/thesysdev/crayon) | +158 | 1342 |
| 11 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +143 | 35675 |
| 12 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +139 | 26291 |
| 13 | [openai/symphony](https://github.com/openai/symphony) | +137 | 11903 |
| 14 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +130 | 6096 |
| 15 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +128 | 36560 |
| 16 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +123 | 29790 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +121 | 19500 |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +117 | 27276 |
| 19 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +114 | 32844 |
| 20 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +109 | 24009 |
| 21 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +109 | 13276 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +105 | 28656 |
| 23 | [jundot/omlx](https://github.com/jundot/omlx) | +102 | 3833 |
| 24 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +101 | 32992 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +97 | 23662 |
| 26 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +96 | 26479 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +94 | 19112 |
| 28 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +93 | 4993 |
| 29 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +92 | 2024 |
| 30 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +90 | 24275 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +10312 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5174 | 33648 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4138 | 20508 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2959 | 51199 |
| 5 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +2711 | 19500 |
| 6 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2665 | 18614 |
| 7 | [openai/symphony](https://github.com/openai/symphony) | +2004 | 11903 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1766 | 36301 |
| 9 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1759 | 6055 |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1752 | 35675 |
| 11 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1687 | 32992 |
| 12 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1684 | 6740 |
| 13 | [obra/superpowers](https://github.com/obra/superpowers) | +1597 | 60312 |
| 14 | [anthropics/skills](https://github.com/anthropics/skills) | +1532 | 74774 |
| 15 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1341 | 9694 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1330 | 28881 |
| 17 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1326 | 36560 |
| 18 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1259 | 24009 |
| 19 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1066 | 5791 |
| 20 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1044 | 6096 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +997 | 25505 |
| 22 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +990 | 29790 |
| 23 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +957 | 5406 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +925 | 14017 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +903 | 13783 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +887 | 4994 |
| 27 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +881 | 32844 |
| 28 | [openai/skills](https://github.com/openai/skills) | +873 | 14025 |
| 29 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +828 | 15360 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +822 | 28656 |
| 31 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +812 | 16069 |
| 32 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +798 | 6048 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +771 | 6496 |
| 34 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +760 | 5420 |
| 35 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +749 | 23662 |
| 36 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +728 | 26479 |
| 37 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +721 | 22729 |
| 38 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +697 | 22016 |
| 39 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +695 | 27276 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +684 | 8695 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +680 | 19112 |
| 42 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +626 | 34148 |
| 43 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +605 | 10981 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +592 | 22792 |
| 45 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +586 | 15868 |
| 46 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +583 | 5141 |
| 47 | [m1k1o/neko](https://github.com/m1k1o/neko) | +580 | 19842 |
| 48 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +576 | 12132 |
| 49 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +555 | 37330 |
| 50 | [jundot/omlx](https://github.com/jundot/omlx) | +531 | 3833 |
| 51 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +531 | 33878 |
| 52 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +524 | 35735 |
| 53 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +516 | 15516 |
| 54 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +504 | 21318 |
| 55 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +492 | 5275 |
| 56 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +482 | 29910 |
| 57 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +482 | 33305 |
| 58 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +481 | 4441 |
| 59 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +480 | 24275 |
| 60 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +475 | 11613 |
| 61 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +473 | 43973 |
| 62 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +470 | 2777 |
| 63 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +462 | 7158 |
| 64 | [superset-sh/superset](https://github.com/superset-sh/superset) | +452 | 6724 |
| 65 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +447 | 8656 |
| 66 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +444 | 9620 |
| 67 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +423 | 32835 |
| 68 | [viperrcrypto/Siftly](https://github.com/viperrcrypto/Siftly) | +418 | 1451 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +415 | 27115 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +409 | 13035 |
| 71 | [tobi/qmd](https://github.com/tobi/qmd) | +409 | 14656 |
| 72 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +407 | 11538 |
| 73 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +405 | 4865 |
| 74 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +402 | 11016 |
| 75 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +401 | 32028 |
| 76 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +401 | 20728 |
| 77 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +399 | 2023 |
| 78 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +394 | 2488 |
| 79 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +384 | 4531 |
| 80 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +379 | 6418 |
| 81 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +378 | 13278 |
| 82 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +372 | 2776 |
| 83 | [cyxzdev/Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | +366 | 1449 |
| 84 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +360 | 3998 |
| 85 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +347 | 1736 |
| 86 | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | +342 | 2952 |
| 87 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +336 | 9913 |
| 88 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +331 | 14616 |
| 89 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +323 | 3948 |
| 90 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +322 | 5617 |
| 91 | [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) | +309 | 2165 |
| 92 | [duoan/TorchCode](https://github.com/duoan/TorchCode) | +307 | 1607 |
| 93 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +302 | 7619 |
| 94 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +289 | 30678 |
| 95 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +288 | 3491 |
| 96 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +286 | 27672 |
| 97 | [win4r/memory-lancedb-pro](https://github.com/win4r/memory-lancedb-pro) | +285 | 2231 |
| 98 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +269 | 15410 |
| 99 | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) | +266 | 1859 |
| 100 | [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) | +266 | 1979 |
| 101 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +260 | 11627 |
| 102 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +253 | 2024 |
| 103 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +233 | 6505 |
| 104 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +222 | 24855 |
| 105 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +218 | 1200 |
| 106 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +214 | 26291 |
| 107 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +214 | 10152 |
| 108 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +213 | 36799 |
| 109 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +199 | 12877 |
| 110 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +197 | 1330 |
| 111 | [PKU-YuanGroup/Helios](https://github.com/PKU-YuanGroup/Helios) | +194 | 1096 |
| 112 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +191 | 47122 |
| 113 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +190 | 1048 |
| 114 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +190 | 4737 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +189 | 31079 |
| 116 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +186 | 1843 |
| 117 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +179 | 21330 |
| 118 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +177 | 7680 |
| 119 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +174 | 1329 |
| 120 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +163 | 14204 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32959 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8807 | 36560 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8251 | 35675 |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7867 | 26479 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +7513 | 60312 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7469 | 51199 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6449 | 24275 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +6339 | 33648 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6035 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +6001 | 24009 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5742 | 36301 |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4869 | 109881 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4799 | 28881 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4602 | 122870 |
| 15 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4573 | 20508 |
| 16 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4287 | 19500 |
| 17 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4235 | 32844 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4226 | 22016 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3940 | 28656 |
| 20 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3930 | 23662 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3911 | 32992 |
| 22 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3819 | 14017 |
| 23 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3778 | 15360 |
| 24 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3369 | 13091 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3182 | 22792 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3148 | 12132 |
| 27 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +3114 | 33305 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2980 | 69674 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2976 | 10981 |
| 30 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2872 | 18615 |
| 31 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2869 | 60117 |
| 32 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2687 | 9439 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2682 | 13783 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2653 | 85286 |
| 35 | [openai/symphony](https://github.com/openai/symphony) | +2623 | 11903 |
| 36 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2596 | 8887 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2554 | 9239 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2505 | 27276 |
| 39 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2469 | 9694 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2456 | 34148 |
| 41 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2453 | 37330 |
| 42 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2322 | 29791 |
| 43 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2318 | 33878 |
| 44 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2242 | 25505 |
| 45 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2183 | 96919 |
| 46 | [huggingface/skills](https://github.com/huggingface/skills) | +2140 | 8865 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2127 | 8695 |
| 48 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2074 | 19112 |
| 49 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1983 | 9157 |
| 50 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1948 | 30678 |
| 51 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1912 | 7109 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1911 | 147486 |
| 53 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1878 | 20728 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1848 | 71722 |
| 55 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1839 | 9620 |
| 56 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1828 | 21318 |
| 57 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1821 | 11627 |
| 58 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1780 | 6740 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1759 | 6055 |
| 60 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1730 | 6427 |
| 61 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1713 | 7619 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1712 | 6271 |
| 63 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1701 | 21330 |
| 64 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1696 | 27115 |
| 65 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1694 | 6228 |
| 66 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1692 | 11538 |
| 67 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1691 | 22729 |
| 68 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1677 | 74887 |
| 69 | [openai/skills](https://github.com/openai/skills) | +1650 | 14025 |
| 70 | [tobi/qmd](https://github.com/tobi/qmd) | +1643 | 14656 |
| 71 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1631 | 7158 |
| 72 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1613 | 149018 |
| 73 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1585 | 6507 |
| 74 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1584 | 5679 |
| 75 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1576 | 29910 |
| 76 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1558 | 33712 |
| 77 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1551 | 6496 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1526 | 11613 |
| 79 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1513 | 14616 |
| 80 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1474 | 5742 |
| 81 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1472 | 15868 |
| 82 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1469 | 15410 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1421 | 98536 |
| 84 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1414 | 13794 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1412 | 13035 |
| 86 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1408 | 6418 |
| 87 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1381 | 6724 |
| 88 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1350 | 37564 |
| 89 | [maderix/ANE](https://github.com/maderix/ANE) | +1348 | 6136 |
| 90 | [openai/codex](https://github.com/openai/codex) | +1345 | 61744 |
| 91 | [tw93/Mole](https://github.com/tw93/Mole) | +1331 | 36870 |
| 92 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1283 | 6048 |
| 93 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1272 | 6505 |
| 94 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1244 | 5141 |
| 95 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1190 | 5420 |
| 96 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1172 | 6096 |
| 97 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1172 | 4210 |
| 98 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1165 | 22559 |
| 99 | [google/langextract](https://github.com/google/langextract) | +1122 | 33636 |
| 100 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1120 | 87598 |
| 101 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1094 | 8656 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1093 | 27672 |
| 103 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1081 | 12869 |
| 104 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1080 | 5791 |
| 105 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1012 | 4441 |
| 106 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +964 | 3821 |
| 107 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +961 | 5406 |
| 108 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +949 | 24855 |
| 109 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +925 | 4908 |
| 110 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +922 | 43973 |
| 111 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +909 | 4995 |
| 112 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +851 | 61818 |
| 113 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +849 | 12877 |
| 114 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +816 | 3316 |
| 115 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +791 | 22865 |
| 116 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +771 | 22793 |
| 117 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +769 | 36799 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +768 | 9545 |
| 119 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +762 | 47122 |
| 120 | [docling-project/docling](https://github.com/docling-project/docling) | +762 | 54041 |
| 121 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +760 | 5275 |
| 122 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +743 | 10152 |
| 123 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +708 | 35735 |
| 124 | [wshobson/agents](https://github.com/wshobson/agents) | +691 | 31079 |
| 125 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +682 | 3998 |
| 126 | [aden-hive/hive](https://github.com/aden-hive/hive) | +654 | 9315 |
| 127 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +653 | 14204 |
| 128 | [google-research/timesfm](https://github.com/google-research/timesfm) | +650 | 10018 |
| 129 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +648 | 2240 |
| 130 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +643 | 2777 |
| 131 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +637 | 14259 |
| 132 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +634 | 7368 |
| 133 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +625 | 7680 |
| 134 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +614 | 15516 |
| 135 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +588 | 15900 |
| 136 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +580 | 17678 |
| 137 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +578 | 47936 |
| 138 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +567 | 30590 |
| 139 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +566 | 4531 |
| 140 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +562 | 1960 |
| 141 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +555 | 9422 |
| 142 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +554 | 1891 |
| 143 | [jundot/omlx](https://github.com/jundot/omlx) | +553 | 3833 |
| 144 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +516 | 32028 |
| 145 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +515 | 1753 |
| 146 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +508 | 2036 |
| 147 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +503 | 2078 |
| 148 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +503 | 1921 |
| 149 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +498 | 3107 |
| 150 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +497 | 4457 |
| 151 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +486 | 44545 |
| 152 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +482 | 8983 |
| 153 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +482 | 16047 |
| 154 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +480 | 15007 |
| 155 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +479 | 44232 |
| 156 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +474 | 39841 |
| 157 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +466 | 3491 |
| 158 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +459 | 1461 |
| 159 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +455 | 5028 |
| 160 | [eooce/python-ws](https://github.com/eooce/python-ws) | +451 | 1694 |
| 161 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +449 | 6141 |
| 162 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +447 | 18027 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +444 | 2700 |
| 164 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +442 | 11254 |
| 165 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +435 | 18554 |
| 166 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +423 | 1500 |
| 167 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +419 | 26243 |
| 168 | [microsoft/qlib](https://github.com/microsoft/qlib) | +413 | 37792 |
| 169 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +412 | 1156 |
| 170 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +406 | 4067 |
| 171 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +403 | 1707 |
| 172 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +399 | 6755 |
| 173 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +399 | 10435 |
| 174 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +397 | 11853 |
| 175 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +384 | 2415 |
| 176 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +380 | 1498 |
| 177 | [apify/agent-skills](https://github.com/apify/agent-skills) | +380 | 1582 |
| 178 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +379 | 3511 |
| 179 | [searxng/searxng](https://github.com/searxng/searxng) | +373 | 26378 |
| 180 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +373 | 5754 |
| 181 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +365 | 5306 |
| 182 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +364 | 9417 |
| 183 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +363 | 11362 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +360 | 24257 |
| 185 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +358 | 1432 |
| 186 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +357 | 10736 |
| 187 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +348 | 1471 |
| 188 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +341 | 737 |
| 189 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +324 | 2708 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +324 | 10084 |
| 191 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +323 | 10595 |
| 192 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +323 | 1360 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +312 | 3364 |
| 194 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +306 | 2539 |
| 195 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +303 | 1329 |
| 196 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +290 | 1330 |
| 197 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +288 | 1955 |
| 198 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +287 | 36103 |
| 199 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +286 | 1199 |
| 200 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +277 | 1214 |
| 201 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +276 | 3730 |
| 202 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +273 | 1160 |
| 203 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +272 | 4366 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +255 | 21196 |
| 205 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +254 | 21476 |
| 206 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +254 | 851 |
| 207 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +232 | 29780 |
| 208 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +230 | 5436 |
| 209 | [robinebers/openusage](https://github.com/robinebers/openusage) | +229 | 1405 |
| 210 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 144 |
| 211 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +223 | 833 |
| 212 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +217 | 847 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +214 | 12909 |
| 214 | [usebruno/bruno](https://github.com/usebruno/bruno) | +211 | 41086 |
| 215 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +211 | 8821 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +210 | 40265 |
| 217 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +207 | 677 |
| 218 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +205 | 8793 |
| 219 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +202 | 1364 |
| 220 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +201 | 601 |
| 221 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +199 | 6734 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +197 | 28748 |
| 223 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +183 | 793 |
| 224 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +173 | 681 |
| 225 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +173 | 22675 |
| 226 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +170 | 5023 |
| 227 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +170 | 25298 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +169 | 3915 |
| 229 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +163 | 541 |
| 230 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +160 | 790 |
| 231 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +159 | 1421 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +154 | 1912 |
| 233 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +153 | 5087 |
| 234 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +153 | 33000 |
| 235 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +151 | 549 |
| 236 | [qist/tvbox](https://github.com/qist/tvbox) | +151 | 8445 |
| 237 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +149 | 1382 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +146 | 25901 |
| 239 | [decolua/9router](https://github.com/decolua/9router) | +145 | 861 |
| 240 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +144 | 2360 |
| 241 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +144 | 528 |
| 242 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +138 | 39596 |
| 243 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +137 | 628 |
| 244 | [jgraph/drawio](https://github.com/jgraph/drawio) | +135 | 4081 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +135 | 556 |
| 246 | [lklynet/aurral](https://github.com/lklynet/aurral) | +134 | 860 |
| 247 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +131 | 11982 |
| 248 | [is-a-dev/register](https://github.com/is-a-dev/register) | +130 | 9953 |
| 249 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +130 | 3412 |
| 250 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +127 | 1485 |
| 251 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +125 | 6960 |
| 252 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +122 | 790 |
| 253 | [expo/skills](https://github.com/expo/skills) | +122 | 1433 |
| 254 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 255 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +119 | 37313 |
| 256 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +118 | 766 |
| 257 | [microg/GmsCore](https://github.com/microg/GmsCore) | +118 | 12521 |
| 258 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +116 | 424 |
| 259 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +116 | 734 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +116 | 1203 |
| 261 | [fmhy/edit](https://github.com/fmhy/edit) | +115 | 8455 |
| 262 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +114 | 9958 |
| 263 | [4ier/neo](https://github.com/4ier/neo) | +111 | 563 |
| 264 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +111 | 3188 |
| 265 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +111 | 1807 |
| 266 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +109 | 3128 |
| 267 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +109 | 35473 |
| 268 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +108 | 861 |
| 269 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +103 | 781 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +101 | 885 |
| 271 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +100 | 414 |
| 272 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +97 | 1038 |
| 273 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +97 | 3072 |
| 274 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 11075 |
| 275 | [skylot/jadx](https://github.com/skylot/jadx) | +94 | 47365 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +90 | 26823 |
| 277 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +89 | 350 |
| 278 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +89 | 927 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +85 | 8700 |
| 280 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +84 | 349 |
| 281 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +83 | 441 |
| 282 | [apache/kafka](https://github.com/apache/kafka) | +83 | 32043 |
| 283 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +82 | 2963 |
| 284 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +81 | 1007 |
| 285 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +81 | 314 |
| 286 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +81 | 541 |
| 287 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +78 | 683 |
| 288 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 239 |
| 289 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +77 | 936 |
| 290 | [openjdk/jdk](https://github.com/openjdk/jdk) | +77 | 22768 |
| 291 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +76 | 372 |
| 292 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +75 | 277 |
| 293 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1326 |
| 294 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +71 | 21335 |
| 295 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 296 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +71 | 3513 |
| 297 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +70 | 4573 |
| 298 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +70 | 7573 |
| 299 | [dataease/dataease](https://github.com/dataease/dataease) | +69 | 23579 |
| 300 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +69 | 12343 |
