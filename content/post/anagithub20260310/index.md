---
title: "2026-03-10 GitHub增长趋势报告"
description: "1.agency-agents+1059 2.MiroFish+779 3.paperclip+391 4.context-hub+345 5.RuView+313"
date: 2026-03-10T20:37:14+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-10 20:37:14

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
        'daily': {"categories": ["pingdotgg/t3code", "NousResearch/hermes-agent", "koala73/worldmonitor", "karpathy/nanochat", "alibaba/page-agent", "alirezarezvani/claude-skills", "666ghj/BettaFish", "hesamsheikh/awesome-openclaw-usecases", "pbakaus/impeccable", "D4Vinci/Scrapling", "googleworkspace/cli", "VoltAgent/awesome-openclaw-skills", "nikopueringer/CorridorKey", "bytedance/deer-flow", "jundot/omlx", "ruvnet/RuView", "andrewyng/context-hub", "paperclipai/paperclip", "666ghj/MiroFish", "msitarzewski/agency-agents"], "data": [142, 142, 146, 151, 153, 155, 156, 163, 174, 183, 196, 233, 237, 250, 285, 313, 345, 391, 779, 1059]},
        'weekly': {"categories": ["anomalyco/opencode", "nearai/ironclaw", "shanraisshan/claude-code-best-practice", "KeygraphHQ/shannon", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "D4Vinci/Scrapling", "obra/superpowers", "pingdotgg/t3code", "VoltAgent/awesome-openclaw-skills", "666ghj/MiroFish", "koala73/worldmonitor", "ruvnet/RuView", "openai/symphony", "moeru-ai/airi", "affaan-m/everything-claude-code", "paperclipai/paperclip", "googleworkspace/cli", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [1152, 1246, 1407, 1469, 1476, 1559, 1672, 1693, 1700, 1835, 1867, 2328, 2399, 2411, 2433, 3109, 3771, 4017, 4260, 11089]},
        'monthly': {"categories": ["paperclipai/paperclip", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "googleworkspace/cli", "qwibitai/nanoclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "HKUDS/nanobot", "msitarzewski/agency-agents", "D4Vinci/Scrapling", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "hesamsheikh/awesome-openclaw-usecases", "sipeed/picoclaw", "obra/superpowers", "affaan-m/everything-claude-code", "zeroclaw-labs/zeroclaw", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3773, 3875, 3886, 4018, 4232, 4581, 4594, 4604, 4650, 5120, 5707, 5957, 6015, 7017, 7328, 7373, 7706, 7980, 9077, 32670]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1059 | 24436 |
| 2 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +779 | 13872 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +391 | 16008 |
| 4 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +345 | 3127 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +313 | 34171 |
| 6 | [jundot/omlx](https://github.com/jundot/omlx) | +285 | 2649 |
| 7 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +250 | 28414 |
| 8 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +237 | 4720 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +233 | 34429 |
| 10 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +196 | 18072 |
| 11 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +183 | 28050 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +174 | 3600 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +163 | 22883 |
| 14 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +156 | 35735 |
| 15 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +155 | 3924 |
| 16 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +153 | 3433 |
| 17 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +151 | 43973 |
| 18 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +146 | 35301 |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +142 | 3578 |
| 20 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +142 | 5700 |
| 21 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +133 | 11851 |
| 22 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +131 | 22888 |
| 23 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +127 | 15657 |
| 24 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +123 | 31917 |
| 25 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +122 | 14265 |
| 26 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +121 | 9022 |
| 27 | [openai/symphony](https://github.com/openai/symphony) | +118 | 10758 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +107 | 34148 |
| 29 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +104 | 25743 |
| 30 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +101 | 4659 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +11089 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4260 | 24436 |
| 3 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4017 | 18072 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3771 | 16008 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3109 | 51199 |
| 6 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2433 | 32134 |
| 7 | [openai/symphony](https://github.com/openai/symphony) | +2411 | 10758 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2399 | 34171 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2328 | 35301 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1867 | 13872 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1835 | 34429 |
| 12 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1700 | 5700 |
| 13 | [obra/superpowers](https://github.com/obra/superpowers) | +1693 | 60312 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1672 | 28050 |
| 15 | [anthropics/skills](https://github.com/anthropics/skills) | +1559 | 74774 |
| 16 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1476 | 22883 |
| 17 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1469 | 33062 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1407 | 13119 |
| 19 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1246 | 9022 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1152 | 109881 |
| 21 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1104 | 5005 |
| 22 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1066 | 24838 |
| 23 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1035 | 13545 |
| 24 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +970 | 22888 |
| 25 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +948 | 10452 |
| 26 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +942 | 8074 |
| 27 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +929 | 14265 |
| 28 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +913 | 31917 |
| 29 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +912 | 28414 |
| 30 | [openai/skills](https://github.com/openai/skills) | +883 | 13710 |
| 31 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +880 | 4870 |
| 32 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +854 | 27562 |
| 33 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +844 | 21373 |
| 34 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +835 | 4720 |
| 35 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +801 | 5849 |
| 36 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +794 | 25743 |
| 37 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +788 | 32612 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +774 | 26297 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +733 | 11587 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +730 | 3600 |
| 41 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +723 | 15657 |
| 42 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +692 | 34148 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +683 | 18226 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +663 | 22055 |
| 45 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +651 | 37330 |
| 46 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +650 | 20660 |
| 47 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +650 | 6279 |
| 48 | [superset-sh/superset](https://github.com/superset-sh/superset) | +642 | 6481 |
| 49 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +625 | 2671 |
| 50 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +612 | 3433 |
| 51 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +606 | 14280 |
| 52 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +591 | 15223 |
| 53 | [srizzon/git-city](https://github.com/srizzon/git-city) | +579 | 3451 |
| 54 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +577 | 7385 |
| 55 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +561 | 33878 |
| 56 | [maderix/ANE](https://github.com/maderix/ANE) | +558 | 6087 |
| 57 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +546 | 4039 |
| 58 | [m1k1o/neko](https://github.com/m1k1o/neko) | +515 | 19576 |
| 59 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +510 | 3127 |
| 60 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +502 | 20400 |
| 61 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +501 | 15328 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +483 | 12569 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +479 | 29221 |
| 64 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +473 | 4659 |
| 65 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +468 | 11011 |
| 66 | [tobi/qmd](https://github.com/tobi/qmd) | +457 | 13985 |
| 67 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +450 | 8245 |
| 68 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +450 | 10884 |
| 69 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +449 | 6105 |
| 70 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +449 | 9358 |
| 71 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +438 | 23566 |
| 72 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +435 | 2687 |
| 73 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +430 | 35735 |
| 74 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +415 | 20541 |
| 75 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +406 | 9054 |
| 76 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +404 | 26593 |
| 77 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +395 | 10647 |
| 78 | [viperrcrypto/Siftly](https://github.com/viperrcrypto/Siftly) | +391 | 1366 |
| 79 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +387 | 3579 |
| 80 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +386 | 9536 |
| 81 | [duoan/TorchCode](https://github.com/duoan/TorchCode) | +382 | 1514 |
| 82 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +372 | 2137 |
| 83 | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | +362 | 2765 |
| 84 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +360 | 1519 |
| 85 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +358 | 4343 |
| 86 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +356 | 3844 |
| 87 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +351 | 5251 |
| 88 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +349 | 43973 |
| 89 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +346 | 5341 |
| 90 | [cyxzdev/Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | +345 | 1328 |
| 91 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +342 | 30678 |
| 92 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +341 | 30412 |
| 93 | [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) | +331 | 1993 |
| 94 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +325 | 3412 |
| 95 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +323 | 27348 |
| 96 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +320 | 3924 |
| 97 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +306 | 11193 |
| 98 | [jundot/omlx](https://github.com/jundot/omlx) | +297 | 2649 |
| 99 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +275 | 3455 |
| 100 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +272 | 17916 |
| 101 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +270 | 11115 |
| 102 | [win4r/memory-lancedb-pro](https://github.com/win4r/memory-lancedb-pro) | +268 | 2002 |
| 103 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +254 | 4620 |
| 104 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +252 | 15051 |
| 105 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +250 | 21108 |
| 106 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +249 | 1384 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +248 | 24474 |
| 108 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +247 | 14972 |
| 109 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +228 | 36799 |
| 110 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +219 | 5609 |
| 111 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +219 | 1112 |
| 112 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +213 | 9675 |
| 113 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +213 | 7543 |
| 114 | [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe) | +213 | 2111 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +208 | 30912 |
| 116 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +207 | 978 |
| 117 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +202 | 1218 |
| 118 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +188 | 12622 |
| 119 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +182 | 22632 |
| 120 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +177 | 3695 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32670 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +9077 | 35301 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +7980 | 34171 |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7706 | 25743 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7373 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +7328 | 60312 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +7017 | 23566 |
| 8 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +6015 | 22883 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +5957 | 74774 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5707 | 34429 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5120 | 109881 |
| 12 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4650 | 28050 |
| 13 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4604 | 24436 |
| 14 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4594 | 31917 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4581 | 122870 |
| 16 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4232 | 21373 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4018 | 18072 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3886 | 27562 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3875 | 22888 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3773 | 16008 |
| 21 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +3770 | 33062 |
| 22 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3747 | 32134 |
| 23 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3718 | 13545 |
| 24 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3614 | 14265 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3473 | 22055 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3350 | 12895 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3064 | 11587 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2975 | 69674 |
| 29 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2929 | 60117 |
| 30 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2859 | 10452 |
| 31 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2667 | 9356 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2664 | 85286 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2658 | 13119 |
| 34 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2636 | 8824 |
| 35 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2537 | 37330 |
| 36 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2503 | 9054 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2484 | 34148 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2460 | 26297 |
| 39 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2434 | 33878 |
| 40 | [openai/symphony](https://github.com/openai/symphony) | +2412 | 10758 |
| 41 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2403 | 9022 |
| 42 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2343 | 96919 |
| 43 | [google/langextract](https://github.com/google/langextract) | +2291 | 33636 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2177 | 18226 |
| 45 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2161 | 24838 |
| 46 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2111 | 30678 |
| 47 | [huggingface/skills](https://github.com/huggingface/skills) | +2107 | 8707 |
| 48 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2065 | 13872 |
| 49 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2057 | 28415 |
| 50 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2008 | 8074 |
| 51 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1947 | 8901 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1912 | 147486 |
| 53 | [github/spec-kit](https://github.com/github/spec-kit) | +1890 | 71722 |
| 54 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1878 | 6978 |
| 55 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1843 | 20400 |
| 56 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1811 | 9737 |
| 57 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1808 | 9358 |
| 58 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1799 | 11115 |
| 59 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1789 | 20660 |
| 60 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1771 | 15051 |
| 61 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1761 | 21108 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1738 | 6184 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1722 | 26593 |
| 64 | [openai/skills](https://github.com/openai/skills) | +1708 | 13710 |
| 65 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1708 | 6260 |
| 66 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1703 | 5700 |
| 67 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1670 | 7385 |
| 68 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1670 | 6130 |
| 69 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1668 | 74887 |
| 70 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1636 | 149018 |
| 71 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1635 | 10884 |
| 72 | [tobi/qmd](https://github.com/tobi/qmd) | +1604 | 13985 |
| 73 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1570 | 6105 |
| 74 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1569 | 6406 |
| 75 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1564 | 5586 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1550 | 29221 |
| 77 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1544 | 5170 |
| 78 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1526 | 33712 |
| 79 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1504 | 6279 |
| 80 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1501 | 14280 |
| 81 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1501 | 11011 |
| 82 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1450 | 5639 |
| 83 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1438 | 5849 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1431 | 15223 |
| 85 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1431 | 13735 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1429 | 98536 |
| 87 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1421 | 28365 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1406 | 12569 |
| 89 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1386 | 37564 |
| 90 | [tw93/Mole](https://github.com/tw93/Mole) | +1359 | 36870 |
| 91 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1346 | 6481 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1341 | 6087 |
| 93 | [openai/codex](https://github.com/openai/codex) | +1331 | 61744 |
| 94 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1313 | 4722 |
| 95 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1310 | 20541 |
| 96 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1225 | 5609 |
| 97 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1191 | 4870 |
| 98 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1191 | 22516 |
| 99 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1171 | 87598 |
| 100 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1164 | 12806 |
| 101 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1132 | 3993 |
| 102 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1115 | 5005 |
| 103 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1084 | 8245 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1084 | 27348 |
| 105 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +951 | 4722 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +943 | 24474 |
| 107 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +934 | 3695 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +867 | 61818 |
| 109 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +842 | 22643 |
| 110 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +841 | 12622 |
| 111 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +840 | 3579 |
| 112 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +836 | 43973 |
| 113 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +796 | 22632 |
| 114 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +795 | 3154 |
| 115 | [docling-project/docling](https://github.com/docling-project/docling) | +778 | 54041 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +769 | 36799 |
| 117 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +767 | 9384 |
| 118 | [aden-hive/hive](https://github.com/aden-hive/hive) | +754 | 9064 |
| 119 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +741 | 9675 |
| 120 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +741 | 3600 |
| 121 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +736 | 71086 |
| 122 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +735 | 47122 |
| 123 | [wshobson/agents](https://github.com/wshobson/agents) | +703 | 30912 |
| 124 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +689 | 7543 |
| 125 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +671 | 14176 |
| 126 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +665 | 3844 |
| 127 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +655 | 7352 |
| 128 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +654 | 13898 |
| 129 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +646 | 2214 |
| 130 | [google-research/timesfm](https://github.com/google-research/timesfm) | +645 | 10001 |
| 131 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +638 | 4659 |
| 132 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +625 | 2671 |
| 133 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +622 | 35735 |
| 134 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +616 | 15725 |
| 135 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +611 | 30590 |
| 136 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +603 | 47936 |
| 137 | [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) | +591 | 2611 |
| 138 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +585 | 15328 |
| 139 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +585 | 18468 |
| 140 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +582 | 9313 |
| 141 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +582 | 17642 |
| 142 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +554 | 4382 |
| 143 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +551 | 8885 |
| 144 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +547 | 1909 |
| 145 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +543 | 1796 |
| 146 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +542 | 2176 |
| 147 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +539 | 3421 |
| 148 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +528 | 1359 |
| 149 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +508 | 1715 |
| 150 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +504 | 2013 |
| 151 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +499 | 1909 |
| 152 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +498 | 44545 |
| 153 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +497 | 4953 |
| 154 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +497 | 2915 |
| 155 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +493 | 39841 |
| 156 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +479 | 15948 |
| 157 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +479 | 3127 |
| 158 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +470 | 14972 |
| 159 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +468 | 1439 |
| 160 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +466 | 3924 |
| 161 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +461 | 3455 |
| 162 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +456 | 1451 |
| 163 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +448 | 1687 |
| 164 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +445 | 11242 |
| 165 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +443 | 6111 |
| 166 | [eooce/python-ws](https://github.com/eooce/python-ws) | +442 | 1647 |
| 167 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +442 | 17916 |
| 168 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +438 | 11802 |
| 169 | [microsoft/qlib](https://github.com/microsoft/qlib) | +437 | 37792 |
| 170 | [openclaw/skills](https://github.com/openclaw/skills) | +435 | 2505 |
| 171 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +425 | 14761 |
| 172 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +421 | 26063 |
| 173 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +418 | 44232 |
| 174 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +408 | 3956 |
| 175 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +402 | 1607 |
| 176 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +400 | 6486 |
| 177 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +399 | 10410 |
| 178 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +388 | 3378 |
| 179 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +385 | 5207 |
| 180 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +379 | 1462 |
| 181 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +376 | 10603 |
| 182 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +376 | 5633 |
| 183 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +369 | 2315 |
| 184 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +369 | 11286 |
| 185 | [apify/agent-skills](https://github.com/apify/agent-skills) | +361 | 1484 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +360 | 24178 |
| 187 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +357 | 9278 |
| 188 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +350 | 1384 |
| 189 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +344 | 708 |
| 190 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +340 | 1425 |
| 191 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +317 | 1323 |
| 192 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +317 | 10009 |
| 193 | [jundot/omlx](https://github.com/jundot/omlx) | +315 | 2649 |
| 194 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +315 | 2581 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +312 | 3264 |
| 196 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +309 | 36103 |
| 197 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +306 | 2521 |
| 198 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +302 | 1131 |
| 199 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +294 | 1079 |
| 200 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +291 | 4288 |
| 201 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +287 | 1940 |
| 202 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +271 | 1218 |
| 203 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +267 | 1115 |
| 204 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +266 | 3605 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +262 | 21142 |
| 206 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +258 | 36697 |
| 207 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +253 | 848 |
| 208 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +249 | 21398 |
| 209 | [robinebers/openusage](https://github.com/robinebers/openusage) | +241 | 1381 |
| 210 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +241 | 5429 |
| 211 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +234 | 8754 |
| 212 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +228 | 813 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +227 | 12876 |
| 214 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 146 |
| 215 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +219 | 8799 |
| 216 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +217 | 29780 |
| 217 | [usebruno/bruno](https://github.com/usebruno/bruno) | +217 | 41086 |
| 218 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +214 | 747 |
| 219 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +207 | 679 |
| 220 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +206 | 40265 |
| 221 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +201 | 597 |
| 222 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +201 | 6671 |
| 223 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +197 | 776 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +197 | 28670 |
| 225 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +186 | 743 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +183 | 22634 |
| 227 | [VonChange/utao](https://github.com/VonChange/utao) | +175 | 3902 |
| 228 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +172 | 676 |
| 229 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +169 | 4956 |
| 230 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +162 | 531 |
| 231 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +162 | 1890 |
| 232 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +161 | 1393 |
| 233 | [qist/tvbox](https://github.com/qist/tvbox) | +161 | 8408 |
| 234 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +160 | 5034 |
| 235 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +159 | 1370 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +159 | 33000 |
| 237 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +150 | 3392 |
| 238 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +149 | 531 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +149 | 25873 |
| 240 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 521 |
| 241 | [decolua/9router](https://github.com/decolua/9router) | +142 | 799 |
| 242 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +141 | 39596 |
| 243 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +138 | 705 |
| 244 | [lklynet/aurral](https://github.com/lklynet/aurral) | +136 | 850 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +135 | 11938 |
| 246 | [is-a-dev/register](https://github.com/is-a-dev/register) | +132 | 9932 |
| 247 | [expo/skills](https://github.com/expo/skills) | +129 | 1401 |
| 248 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +129 | 750 |
| 249 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +127 | 25156 |
| 250 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +127 | 498 |
| 251 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +126 | 37313 |
| 252 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +125 | 6937 |
| 253 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +125 | 1388 |
| 254 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +125 | 3102 |
| 255 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 256 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +120 | 553 |
| 257 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +120 | 9922 |
| 258 | [fmhy/edit](https://github.com/fmhy/edit) | +119 | 8426 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +119 | 12506 |
| 260 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +118 | 851 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +115 | 3151 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +113 | 1175 |
| 263 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +112 | 3268 |
| 264 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +111 | 400 |
| 265 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +107 | 772 |
| 266 | [4ier/neo](https://github.com/4ier/neo) | +104 | 535 |
| 267 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +103 | 35473 |
| 268 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +97 | 1034 |
| 269 | [skylot/jadx](https://github.com/skylot/jadx) | +97 | 47365 |
| 270 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +95 | 3065 |
| 271 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 339 |
| 272 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11025 |
| 273 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +94 | 1669 |
| 274 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +94 | 2155 |
| 275 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +93 | 588 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +93 | 26800 |
| 277 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +88 | 330 |
| 278 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +88 | 898 |
| 279 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +87 | 319 |
| 280 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +86 | 982 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +85 | 2929 |
| 282 | [apache/kafka](https://github.com/apache/kafka) | +85 | 32043 |
| 283 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +83 | 784 |
| 284 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +82 | 310 |
| 285 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +80 | 848 |
| 286 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +80 | 8657 |
| 287 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +78 | 682 |
| 288 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 243 |
| 289 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 290 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +76 | 4559 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +76 | 915 |
| 292 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +76 | 3502 |
| 293 | [openjdk/jdk](https://github.com/openjdk/jdk) | +76 | 22780 |
| 294 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +75 | 300 |
| 295 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +75 | 262 |
| 296 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +74 | 524 |
| 297 | [dataease/dataease](https://github.com/dataease/dataease) | +74 | 23554 |
| 298 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1320 |
| 299 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +72 | 12323 |
| 300 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +71 | 303 |
