---
title: "2026-03-11 GitHub增长趋势报告"
description: "1.agency-agents+1038 2.MiroFish+550 3.paperclip+385 4.hermes-agent+237 5.page-agent+231"
date: 2026-03-11T20:36:36+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-11 20:36:36

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
        'daily': {"categories": ["AlexsJones/llmfit", "elder-plinius/CL4R1T4S", "D4Vinci/Scrapling", "HKUDS/nanobot", "Gen-Verse/OpenClaw-RL", "karpathy/nanochat", "nikopueringer/CorridorKey", "hesamsheikh/awesome-openclaw-usecases", "promptfoo/promptfoo", "ruvnet/RuView", "jundot/omlx", "googleworkspace/cli", "bytedance/deer-flow", "andrewyng/context-hub", "VoltAgent/awesome-openclaw-skills", "alibaba/page-agent", "NousResearch/hermes-agent", "paperclipai/paperclip", "666ghj/MiroFish", "msitarzewski/agency-agents"], "data": [91, 98, 103, 105, 107, 111, 115, 130, 132, 158, 160, 167, 185, 198, 230, 231, 237, 385, 550, 1038]},
        'weekly': {"categories": ["shareAI-lab/learn-claude-code", "shanraisshan/claude-code-best-practice", "nearai/ironclaw", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "D4Vinci/Scrapling", "obra/superpowers", "koala73/worldmonitor", "phuryn/pm-skills", "pingdotgg/t3code", "VoltAgent/awesome-openclaw-skills", "ruvnet/RuView", "moeru-ai/airi", "666ghj/MiroFish", "openai/symphony", "affaan-m/everything-claude-code", "paperclipai/paperclip", "googleworkspace/cli", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [1036, 1122, 1296, 1360, 1530, 1549, 1575, 1597, 1660, 1731, 1835, 1933, 2257, 2358, 2491, 2947, 4123, 4172, 4789, 10676]},
        'monthly': {"categories": ["sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "paperclipai/paperclip", "googleworkspace/cli", "qwibitai/nanoclaw", "HKUDS/nanobot", "x1xhlol/system-prompts-and-models-of-ai-tools", "D4Vinci/Scrapling", "anomalyco/opencode", "msitarzewski/agency-agents", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "hesamsheikh/awesome-openclaw-usecases", "sipeed/picoclaw", "obra/superpowers", "affaan-m/everything-claude-code", "zeroclaw-labs/zeroclaw", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3883, 3897, 4124, 4172, 4247, 4393, 4585, 4735, 4960, 5573, 5728, 5990, 5998, 6935, 7404, 7432, 7771, 8118, 8968, 32975]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1038 | 29543 |
| 2 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +550 | 16596 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +385 | 18472 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +237 | 5075 |
| 5 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +231 | 4620 |
| 6 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +230 | 35535 |
| 7 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +198 | 4466 |
| 8 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +185 | 29267 |
| 9 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +167 | 18950 |
| 10 | [jundot/omlx](https://github.com/jundot/omlx) | +160 | 3317 |
| 11 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +158 | 34953 |
| 12 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +132 | 12481 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +130 | 23505 |
| 14 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +115 | 5275 |
| 15 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +111 | 43973 |
| 16 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +107 | 1684 |
| 17 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +105 | 32427 |
| 18 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +103 | 28523 |
| 19 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +98 | 13667 |
| 20 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +91 | 14746 |
| 21 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +86 | 34148 |
| 22 | [openai/symphony](https://github.com/openai/symphony) | +85 | 11212 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +85 | 4003 |
| 24 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +85 | 15977 |
| 25 | [tobi/qmd](https://github.com/tobi/qmd) | +84 | 14346 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +83 | 28093 |
| 27 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +83 | 32618 |
| 28 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +82 | 37330 |
| 29 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +81 | 9413 |
| 30 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +79 | 10749 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +10676 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4789 | 29543 |
| 3 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4172 | 18950 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4123 | 18472 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2947 | 51199 |
| 6 | [openai/symphony](https://github.com/openai/symphony) | +2491 | 11212 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2358 | 16596 |
| 8 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2257 | 32618 |
| 9 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1933 | 34953 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1835 | 35535 |
| 11 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1731 | 5916 |
| 12 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1660 | 6524 |
| 13 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1597 | 35869 |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | +1575 | 60312 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1549 | 28523 |
| 16 | [anthropics/skills](https://github.com/anthropics/skills) | +1530 | 74774 |
| 17 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1360 | 23505 |
| 18 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1296 | 9413 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1122 | 13293 |
| 20 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1036 | 25198 |
| 21 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1035 | 33183 |
| 22 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +969 | 13770 |
| 23 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +952 | 29267 |
| 24 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +924 | 5275 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +894 | 23278 |
| 26 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +892 | 32427 |
| 27 | [openai/skills](https://github.com/openai/skills) | +889 | 13899 |
| 28 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +875 | 5192 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +852 | 6224 |
| 30 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +839 | 14746 |
| 31 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +819 | 4620 |
| 32 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +811 | 28093 |
| 33 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +808 | 8413 |
| 34 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +803 | 4003 |
| 35 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +795 | 15977 |
| 36 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +773 | 21751 |
| 37 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +727 | 26139 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +715 | 26756 |
| 39 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +711 | 10749 |
| 40 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +694 | 5009 |
| 41 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +691 | 4466 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +666 | 18690 |
| 43 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +660 | 34148 |
| 44 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +636 | 2730 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +619 | 22406 |
| 46 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +602 | 5075 |
| 47 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +589 | 37330 |
| 48 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +588 | 11810 |
| 49 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +579 | 32736 |
| 50 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +578 | 15559 |
| 51 | [m1k1o/neko](https://github.com/m1k1o/neko) | +559 | 19750 |
| 52 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +552 | 33878 |
| 53 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +542 | 20960 |
| 54 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +517 | 6745 |
| 55 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +513 | 4289 |
| 56 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +512 | 15423 |
| 57 | [superset-sh/superset](https://github.com/superset-sh/superset) | +491 | 6615 |
| 58 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +482 | 35735 |
| 59 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +477 | 11355 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +476 | 29545 |
| 61 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +473 | 5005 |
| 62 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +463 | 20571 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +459 | 12816 |
| 64 | [srizzon/git-city](https://github.com/srizzon/git-city) | +446 | 3526 |
| 65 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +443 | 23946 |
| 66 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +443 | 8456 |
| 67 | [jundot/omlx](https://github.com/jundot/omlx) | +440 | 3317 |
| 68 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +439 | 9476 |
| 69 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +435 | 14439 |
| 70 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +430 | 43973 |
| 71 | [tobi/qmd](https://github.com/tobi/qmd) | +422 | 14346 |
| 72 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +420 | 6261 |
| 73 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +418 | 2734 |
| 74 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +415 | 20987 |
| 75 | [viperrcrypto/Siftly](https://github.com/viperrcrypto/Siftly) | +412 | 1435 |
| 76 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +407 | 7503 |
| 77 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +401 | 11214 |
| 78 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +398 | 26867 |
| 79 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +390 | 2329 |
| 80 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +386 | 10854 |
| 81 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +377 | 1637 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +374 | 4526 |
| 83 | [cyxzdev/Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | +360 | 1407 |
| 84 | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | +360 | 2872 |
| 85 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +360 | 9718 |
| 86 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +357 | 3922 |
| 87 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +353 | 4241 |
| 88 | [duoan/TorchCode](https://github.com/duoan/TorchCode) | +350 | 1558 |
| 89 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +349 | 5434 |
| 90 | [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) | +314 | 2081 |
| 91 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +306 | 3659 |
| 92 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 27503 |
| 93 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +296 | 9159 |
| 94 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +291 | 30678 |
| 95 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +283 | 3477 |
| 96 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +281 | 12481 |
| 97 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +279 | 11327 |
| 98 | [win4r/memory-lancedb-pro](https://github.com/win4r/memory-lancedb-pro) | +272 | 2093 |
| 99 | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) | +258 | 1629 |
| 100 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +257 | 11232 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +257 | 15247 |
| 102 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +255 | 13022 |
| 103 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +233 | 24658 |
| 104 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +226 | 5800 |
| 105 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +224 | 36799 |
| 106 | [PKU-YuanGroup/Helios](https://github.com/PKU-YuanGroup/Helios) | +221 | 1067 |
| 107 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +219 | 14988 |
| 108 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +218 | 4688 |
| 109 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +214 | 1170 |
| 110 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +212 | 21230 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +206 | 9809 |
| 112 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +204 | 1014 |
| 113 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +204 | 1405 |
| 114 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +200 | 1283 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +196 | 30987 |
| 116 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +194 | 12748 |
| 117 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +189 | 17973 |
| 118 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +179 | 7584 |
| 119 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +177 | 1229 |
| 120 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +171 | 1752 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32975 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8968 | 35869 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8118 | 34953 |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7771 | 26139 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7432 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +7404 | 60312 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6935 | 23946 |
| 8 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5998 | 23505 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +5990 | 74774 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5728 | 35535 |
| 11 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5573 | 29544 |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4960 | 109881 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4735 | 28523 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4585 | 122870 |
| 15 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4393 | 32427 |
| 16 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4247 | 21751 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4172 | 18950 |
| 18 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4124 | 18472 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3897 | 28093 |
| 20 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3883 | 23278 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3817 | 32618 |
| 22 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3765 | 13770 |
| 23 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3688 | 14746 |
| 24 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3362 | 13022 |
| 25 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +3290 | 33183 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3250 | 22406 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3085 | 11810 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2967 | 69674 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2935 | 10749 |
| 30 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2887 | 60117 |
| 31 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2679 | 9400 |
| 32 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2653 | 13293 |
| 33 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2624 | 85286 |
| 34 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2613 | 8851 |
| 35 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2554 | 16596 |
| 36 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2521 | 9159 |
| 37 | [openai/symphony](https://github.com/openai/symphony) | +2491 | 11212 |
| 38 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2487 | 37330 |
| 39 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2456 | 34148 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2454 | 26756 |
| 41 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2424 | 9413 |
| 42 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2385 | 33878 |
| 43 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2238 | 96919 |
| 44 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2221 | 29267 |
| 45 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2215 | 25198 |
| 46 | [huggingface/skills](https://github.com/huggingface/skills) | +2123 | 8791 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2069 | 8413 |
| 48 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2059 | 18690 |
| 49 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2010 | 30678 |
| 50 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1965 | 9043 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1912 | 147486 |
| 52 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1897 | 7033 |
| 53 | [github/spec-kit](https://github.com/github/spec-kit) | +1865 | 71722 |
| 54 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1861 | 20571 |
| 55 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1818 | 9476 |
| 56 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1808 | 11233 |
| 57 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1792 | 20960 |
| 58 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1732 | 6524 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1731 | 5916 |
| 60 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1722 | 21230 |
| 61 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1720 | 6228 |
| 62 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1714 | 6347 |
| 63 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1694 | 7503 |
| 64 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1688 | 6188 |
| 65 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1687 | 15247 |
| 66 | [openai/skills](https://github.com/openai/skills) | +1680 | 13899 |
| 67 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1675 | 74887 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1673 | 26867 |
| 69 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1648 | 11214 |
| 70 | [tobi/qmd](https://github.com/tobi/qmd) | +1640 | 14346 |
| 71 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1622 | 149018 |
| 72 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1574 | 5631 |
| 73 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1573 | 6451 |
| 74 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1565 | 6745 |
| 75 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1549 | 33712 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1548 | 29545 |
| 77 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1546 | 5182 |
| 78 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1521 | 14439 |
| 79 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1516 | 11355 |
| 80 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1510 | 6224 |
| 81 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1466 | 5704 |
| 82 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1451 | 6261 |
| 83 | [google/langextract](https://github.com/google/langextract) | +1451 | 33636 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1443 | 15559 |
| 85 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1433 | 28513 |
| 86 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1430 | 13766 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1416 | 98536 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1398 | 12816 |
| 89 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1371 | 37564 |
| 90 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1361 | 6615 |
| 91 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1350 | 20987 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1346 | 6110 |
| 93 | [openai/codex](https://github.com/openai/codex) | +1332 | 61744 |
| 94 | [tw93/Mole](https://github.com/tw93/Mole) | +1328 | 36870 |
| 95 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1252 | 5800 |
| 96 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1219 | 5009 |
| 97 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1179 | 22535 |
| 98 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1156 | 5192 |
| 99 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1151 | 4091 |
| 100 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1151 | 87598 |
| 101 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1120 | 4809 |
| 102 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1108 | 12842 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1085 | 27503 |
| 104 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1080 | 8456 |
| 105 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1072 | 5075 |
| 106 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1051 | 5275 |
| 107 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +970 | 4289 |
| 108 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +952 | 3775 |
| 109 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +945 | 24658 |
| 110 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +912 | 43973 |
| 111 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +862 | 61818 |
| 112 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +847 | 12748 |
| 113 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +828 | 4003 |
| 114 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +808 | 22763 |
| 115 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +807 | 3238 |
| 116 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +779 | 22704 |
| 117 | [docling-project/docling](https://github.com/docling-project/docling) | +775 | 54041 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +769 | 9462 |
| 119 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +766 | 36799 |
| 120 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +738 | 47122 |
| 121 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +736 | 9809 |
| 122 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +732 | 71086 |
| 123 | [aden-hive/hive](https://github.com/aden-hive/hive) | +724 | 9222 |
| 124 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +709 | 5005 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +698 | 30987 |
| 126 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +677 | 4468 |
| 127 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +675 | 3922 |
| 128 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +670 | 35735 |
| 129 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +660 | 7584 |
| 130 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +652 | 14229 |
| 131 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +651 | 14044 |
| 132 | [google-research/timesfm](https://github.com/google-research/timesfm) | +648 | 10010 |
| 133 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +645 | 2228 |
| 134 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +643 | 7359 |
| 135 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +638 | 2730 |
| 136 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +603 | 15423 |
| 137 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +602 | 15804 |
| 138 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +587 | 47936 |
| 139 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +585 | 30590 |
| 140 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +582 | 17658 |
| 141 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +564 | 9364 |
| 142 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +554 | 1938 |
| 143 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +547 | 1853 |
| 144 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +529 | 4241 |
| 145 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +529 | 1360 |
| 146 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +514 | 1740 |
| 147 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +514 | 4418 |
| 148 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +513 | 3418 |
| 149 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +507 | 2021 |
| 150 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +505 | 8935 |
| 151 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +501 | 1915 |
| 152 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +500 | 3020 |
| 153 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +487 | 44545 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +486 | 18500 |
| 155 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +482 | 39841 |
| 156 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +480 | 16002 |
| 157 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +474 | 14988 |
| 158 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +469 | 4990 |
| 159 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +465 | 1862 |
| 160 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +465 | 3477 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +462 | 3317 |
| 162 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +461 | 1468 |
| 163 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +457 | 1454 |
| 164 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +447 | 6129 |
| 165 | [eooce/python-ws](https://github.com/eooce/python-ws) | +445 | 1669 |
| 166 | [openclaw/skills](https://github.com/openclaw/skills) | +444 | 2610 |
| 167 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +443 | 11252 |
| 168 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +440 | 17973 |
| 169 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +440 | 14878 |
| 170 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +432 | 44232 |
| 171 | [microsoft/qlib](https://github.com/microsoft/qlib) | +422 | 37792 |
| 172 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +416 | 11829 |
| 173 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +415 | 26168 |
| 174 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +411 | 6642 |
| 175 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +407 | 4018 |
| 176 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +402 | 1651 |
| 177 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +398 | 10424 |
| 178 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +381 | 3411 |
| 179 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +379 | 1487 |
| 180 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +379 | 2368 |
| 181 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +377 | 5701 |
| 182 | [apify/agent-skills](https://github.com/apify/agent-skills) | +375 | 1550 |
| 183 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +371 | 5268 |
| 184 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +366 | 11327 |
| 185 | [searxng/searxng](https://github.com/searxng/searxng) | +364 | 26308 |
| 186 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +362 | 10678 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +362 | 24218 |
| 188 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +356 | 1405 |
| 189 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +356 | 9355 |
| 190 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +351 | 726 |
| 191 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +346 | 1453 |
| 192 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +323 | 2645 |
| 193 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +320 | 10035 |
| 194 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +315 | 10490 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +314 | 3307 |
| 196 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +307 | 2529 |
| 197 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +296 | 36103 |
| 198 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +292 | 1229 |
| 199 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +287 | 1943 |
| 200 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +286 | 1175 |
| 201 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +281 | 4318 |
| 202 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +276 | 1283 |
| 203 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +276 | 1162 |
| 204 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +272 | 1109 |
| 205 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +261 | 3660 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +260 | 21172 |
| 207 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +257 | 21435 |
| 208 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +253 | 850 |
| 209 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +239 | 5433 |
| 210 | [robinebers/openusage](https://github.com/robinebers/openusage) | +237 | 1394 |
| 211 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +228 | 819 |
| 212 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 145 |
| 213 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +222 | 8777 |
| 214 | [usebruno/bruno](https://github.com/usebruno/bruno) | +220 | 41086 |
| 215 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +219 | 29780 |
| 216 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +219 | 12895 |
| 217 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +212 | 8809 |
| 218 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +211 | 822 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +208 | 40265 |
| 220 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +207 | 677 |
| 221 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +201 | 599 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +195 | 28694 |
| 223 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +193 | 6687 |
| 224 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +186 | 756 |
| 225 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +181 | 765 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +174 | 22652 |
| 227 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +173 | 680 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +171 | 3907 |
| 229 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +170 | 4987 |
| 230 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +163 | 535 |
| 231 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +161 | 25275 |
| 232 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +161 | 1409 |
| 233 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +159 | 1902 |
| 234 | [qist/tvbox](https://github.com/qist/tvbox) | +158 | 8421 |
| 235 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +156 | 33000 |
| 236 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +153 | 5052 |
| 237 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +152 | 1375 |
| 238 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +150 | 544 |
| 239 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 524 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +145 | 25892 |
| 241 | [decolua/9router](https://github.com/decolua/9router) | +141 | 828 |
| 242 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +140 | 39596 |
| 243 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +135 | 3402 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +134 | 11964 |
| 245 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +134 | 2343 |
| 246 | [lklynet/aurral](https://github.com/lklynet/aurral) | +133 | 855 |
| 247 | [is-a-dev/register](https://github.com/is-a-dev/register) | +131 | 9942 |
| 248 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +131 | 524 |
| 249 | [jgraph/drawio](https://github.com/jgraph/drawio) | +127 | 4028 |
| 250 | [expo/skills](https://github.com/expo/skills) | +126 | 1413 |
| 251 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +125 | 6951 |
| 252 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +124 | 36697 |
| 253 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +123 | 762 |
| 254 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +122 | 37313 |
| 255 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +121 | 1449 |
| 256 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +117 | 718 |
| 257 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +117 | 9943 |
| 258 | [microg/GmsCore](https://github.com/microg/GmsCore) | +117 | 12513 |
| 259 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +116 | 48784 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +115 | 1190 |
| 261 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +114 | 856 |
| 262 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +114 | 3116 |
| 263 | [fmhy/edit](https://github.com/fmhy/edit) | +114 | 8433 |
| 264 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +113 | 417 |
| 265 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +113 | 3165 |
| 266 | [4ier/neo](https://github.com/4ier/neo) | +108 | 552 |
| 267 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +107 | 35473 |
| 268 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +105 | 778 |
| 269 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +98 | 1721 |
| 270 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +97 | 1038 |
| 271 | [skylot/jadx](https://github.com/skylot/jadx) | +97 | 47365 |
| 272 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +96 | 657 |
| 273 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +95 | 3067 |
| 274 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +94 | 551 |
| 275 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +93 | 339 |
| 276 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +92 | 367 |
| 277 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +91 | 839 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +91 | 11048 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +91 | 26819 |
| 280 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +89 | 336 |
| 281 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +88 | 915 |
| 282 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +85 | 999 |
| 283 | [apache/kafka](https://github.com/apache/kafka) | +84 | 32043 |
| 284 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +83 | 2948 |
| 285 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +82 | 311 |
| 286 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +82 | 8683 |
| 287 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +80 | 332 |
| 288 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +78 | 684 |
| 289 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +78 | 532 |
| 290 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 242 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +77 | 928 |
| 292 | [openjdk/jdk](https://github.com/openjdk/jdk) | +77 | 22786 |
| 293 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +75 | 266 |
| 294 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +73 | 4566 |
| 295 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1322 |
| 296 | [dataease/dataease](https://github.com/dataease/dataease) | +73 | 23570 |
| 297 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +73 | 3507 |
| 298 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +71 | 12333 |
| 299 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +70 | 21332 |
| 300 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +70 | 45263 |
