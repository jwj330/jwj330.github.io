---
title: "2026-03-29 GitHub增长趋势报告"
description: "1.paperclip+356 2.last30days-skill+249 3.Agent-Reach+235 4.claude-howto+194 5.oh-my-claudecode+169"
date: 2026-03-29T20:36:04+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-29 20:36:04

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
        'daily': {"categories": ["opendataloader-project/opendataloader-pdf", "QuipNetwork/quip-protocol", "datalab-to/chandra", "onyx-dot-app/onyx", "TauricResearch/TradingAgents", "HKUDS/OpenSpace", "gsd-build/get-shit-done", "666ghj/MiroFish", "Crosstalk-Solutions/project-nomad", "nidhinjs/prompt-master", "elder-plinius/G0DM0D3", "microsoft/VibeVoice", "NousResearch/hermes-agent", "shanraisshan/claude-code-best-practice", "shareAI-lab/learn-claude-code", "Yeachan-Heo/oh-my-claudecode", "luongnv89/claude-howto", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "paperclipai/paperclip"], "data": [100, 102, 105, 106, 119, 125, 127, 136, 139, 140, 148, 156, 160, 166, 167, 169, 194, 235, 249, 356]},
        'weekly': {"categories": ["ruvnet/RuView", "Donchitos/Claude-Code-Game-Studios", "NousResearch/hermes-agent", "nextlevelbuilder/ui-ux-pro-max-skill", "666ghj/MiroFish", "gsd-build/get-shit-done", "msitarzewski/agency-agents", "shareAI-lab/learn-claude-code", "paperclipai/paperclip", "MiniMax-AI/skills", "pascalorg/editor", "TauricResearch/TradingAgents", "microsoft/RustTraining", "mvanhorn/last30days-skill", "FujiwaraChoki/MoneyPrinterV2", "karpathy/autoresearch", "Crosstalk-Solutions/project-nomad", "bytedance/deer-flow", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [740, 742, 756, 822, 847, 862, 865, 900, 939, 1049, 1076, 1145, 1189, 1191, 1314, 1526, 1676, 2485, 2489, 2801]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "shanraisshan/claude-code-best-practice", "hesamsheikh/awesome-openclaw-usecases", "anomalyco/opencode", "moeru-ai/airi", "gsd-build/get-shit-done", "VoltAgent/awesome-openclaw-skills", "shareAI-lab/learn-claude-code", "googleworkspace/cli", "bytedance/deer-flow", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3237, 3639, 3727, 3990, 4159, 4218, 4450, 4462, 4921, 5004, 5194, 6109, 7686, 7724, 8399, 10346, 11794, 11857, 12529, 23302]}
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
| 1 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +356 | 38735 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +249 | 15171 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +235 | 12873 |
| 4 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +194 | 6123 |
| 5 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +169 | 15909 |
| 6 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +167 | 42587 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +166 | 24248 |
| 8 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +160 | 16438 |
| 9 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +156 | 26891 |
| 10 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +148 | 1949 |
| 11 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +140 | 3623 |
| 12 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +139 | 19648 |
| 13 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +136 | 45457 |
| 14 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +127 | 44572 |
| 15 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +125 | 2400 |
| 16 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +119 | 30590 |
| 17 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +106 | 20048 |
| 18 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +105 | 7876 |
| 19 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +102 | 7720 |
| 20 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +100 | 10574 |
| 21 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +100 | 22008 |
| 22 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +97 | 28279 |
| 23 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +93 | 2338 |
| 24 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +92 | 2347 |
| 25 | [virattt/dexter](https://github.com/virattt/dexter) | +92 | 20440 |
| 26 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +86 | 40043 |
| 27 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +82 | 33975 |
| 28 | [ronitsingh10/FineTune](https://github.com/ronitsingh10/FineTune) | +80 | 5034 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +79 | 35117 |
| 30 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +77 | 19960 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2801 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2489 | 60312 |
| 3 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2485 | 52399 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1676 | 19648 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1526 | 60465 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1314 | 27171 |
| 7 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1191 | 15171 |
| 8 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1189 | 11339 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1145 | 30590 |
| 10 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1076 | 8127 |
| 11 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1049 | 7537 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +939 | 38735 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +900 | 42587 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +865 | 65489 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +862 | 44572 |
| 16 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +847 | 45457 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +822 | 34148 |
| 18 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +756 | 16438 |
| 19 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +742 | 7195 |
| 20 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +740 | 44372 |
| 21 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +732 | 28279 |
| 22 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +711 | 4831 |
| 23 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +634 | 6975 |
| 24 | [jackwener/opencli](https://github.com/jackwener/opencli) | +633 | 8699 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +558 | 24248 |
| 26 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +546 | 14949 |
| 27 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +523 | 15909 |
| 28 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +509 | 33975 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +476 | 35117 |
| 30 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +463 | 22008 |
| 31 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +449 | 6123 |
| 32 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +432 | 13871 |
| 33 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +399 | 20294 |
| 34 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +396 | 10574 |
| 35 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +389 | 45174 |
| 36 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +388 | 30678 |
| 37 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +373 | 39841 |
| 38 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +348 | 22071 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +341 | 13154 |
| 40 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +340 | 18109 |
| 41 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +336 | 15106 |
| 42 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +334 | 7876 |
| 43 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +332 | 12873 |
| 44 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +327 | 14560 |
| 45 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +326 | 17614 |
| 46 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +322 | 25786 |
| 47 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +321 | 31844 |
| 48 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +319 | 2400 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +314 | 35326 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +313 | 33878 |
| 51 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +307 | 12261 |
| 52 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +304 | 42925 |
| 53 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +303 | 19839 |
| 54 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +294 | 28903 |
| 55 | [virattt/dexter](https://github.com/virattt/dexter) | +285 | 20440 |
| 56 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +282 | 26797 |
| 57 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +275 | 2186 |
| 58 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +266 | 26892 |
| 59 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +266 | 37330 |
| 60 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +262 | 1949 |
| 61 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +260 | 9473 |
| 62 | [eze-is/web-access](https://github.com/eze-is/web-access) | +255 | 2082 |
| 63 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +254 | 33711 |
| 64 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +253 | 20048 |
| 65 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +253 | 21057 |
| 66 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +248 | 20565 |
| 67 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +244 | 40043 |
| 68 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +240 | 28151 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +237 | 17369 |
| 70 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +237 | 28438 |
| 71 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +237 | 2437 |
| 72 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +236 | 18042 |
| 73 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +232 | 36886 |
| 74 | [mattpocock/skills](https://github.com/mattpocock/skills) | +231 | 10832 |
| 75 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +216 | 25618 |
| 76 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +214 | 3224 |
| 77 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +214 | 14556 |
| 78 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +212 | 4642 |
| 79 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +210 | 19960 |
| 80 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +205 | 7894 |
| 81 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +205 | 8149 |
| 82 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +204 | 36799 |
| 83 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +203 | 3623 |
| 84 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +202 | 2338 |
| 85 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +201 | 3993 |
| 86 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +198 | 25366 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +190 | 36870 |
| 88 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +189 | 7419 |
| 89 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +189 | 30988 |
| 90 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +185 | 3776 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +183 | 9134 |
| 92 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +180 | 32207 |
| 93 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +179 | 27949 |
| 94 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +178 | 1198 |
| 95 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +177 | 7720 |
| 96 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +177 | 6333 |
| 97 | [usestrix/strix](https://github.com/usestrix/strix) | +171 | 22694 |
| 98 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +160 | 3192 |
| 99 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +160 | 1770 |
| 100 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +160 | 17737 |
| 101 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +159 | 2347 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +154 | 15265 |
| 103 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +152 | 1330 |
| 104 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +149 | 1324 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +145 | 27552 |
| 106 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +142 | 2948 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +142 | 6572 |
| 108 | [jundot/omlx](https://github.com/jundot/omlx) | +135 | 7419 |
| 109 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +127 | 25890 |
| 110 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +121 | 1290 |
| 111 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +119 | 931 |
| 112 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +117 | 8448 |
| 113 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +116 | 3231 |
| 114 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +115 | 16637 |
| 115 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +113 | 1314 |
| 116 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +110 | 2366 |
| 117 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +108 | 17598 |
| 118 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +106 | 8800 |
| 119 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +105 | 2972 |
| 120 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +103 | 27860 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +23302 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12529 | 65489 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11857 | 60465 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11794 | 51199 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10346 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8399 | 44372 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7724 | 45457 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7686 | 38735 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6109 | 45174 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5194 | 74774 |
| 11 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5004 | 52399 |
| 12 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4921 | 23040 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4462 | 42587 |
| 14 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4450 | 42925 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4218 | 44572 |
| 16 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4159 | 36296 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3990 | 109881 |
| 18 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3727 | 27949 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3639 | 24248 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3237 | 34148 |
| 21 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3235 | 33711 |
| 22 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3175 | 13621 |
| 23 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3100 | 19648 |
| 24 | [openai/symphony](https://github.com/openai/symphony) | +3072 | 14222 |
| 25 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3057 | 15871 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3029 | 19839 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2957 | 20565 |
| 28 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2854 | 14556 |
| 29 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2765 | 19960 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2701 | 35117 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2660 | 14560 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2635 | 85286 |
| 33 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2600 | 16438 |
| 34 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2600 | 69674 |
| 35 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2594 | 17614 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2547 | 25786 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2451 | 26797 |
| 38 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2429 | 27171 |
| 39 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2368 | 28438 |
| 40 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2347 | 28279 |
| 41 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2322 | 36886 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2260 | 28903 |
| 43 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2212 | 15106 |
| 44 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2202 | 30590 |
| 45 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2144 | 13154 |
| 46 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2128 | 25890 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2096 | 12873 |
| 48 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2072 | 37330 |
| 49 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2064 | 8360 |
| 50 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2060 | 7702 |
| 51 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2052 | 10592 |
| 52 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2035 | 12240 |
| 53 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2011 | 28151 |
| 54 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2009 | 60117 |
| 55 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2006 | 29158 |
| 56 | [github/spec-kit](https://github.com/github/spec-kit) | +2001 | 71722 |
| 57 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1957 | 34852 |
| 58 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1917 | 33878 |
| 59 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1888 | 9529 |
| 60 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1865 | 30678 |
| 61 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1849 | 14949 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1834 | 21057 |
| 63 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1818 | 25618 |
| 64 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1806 | 8387 |
| 65 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1760 | 9169 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1740 | 35326 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1715 | 11079 |
| 68 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1680 | 122870 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1639 | 31844 |
| 70 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1592 | 17737 |
| 71 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1533 | 18042 |
| 72 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1518 | 10574 |
| 73 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1514 | 33976 |
| 74 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1502 | 18727 |
| 75 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1483 | 16637 |
| 76 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1480 | 15171 |
| 77 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1472 | 10832 |
| 78 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1470 | 36827 |
| 79 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1421 | 9473 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1420 | 17369 |
| 81 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1413 | 98536 |
| 82 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1412 | 8699 |
| 83 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1398 | 96919 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1380 | 15265 |
| 85 | [tw93/Mole](https://github.com/tw93/Mole) | +1358 | 36870 |
| 86 | [openai/skills](https://github.com/openai/skills) | +1346 | 15678 |
| 87 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1314 | 43973 |
| 88 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1308 | 9134 |
| 89 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1277 | 15909 |
| 90 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1265 | 26678 |
| 91 | [jundot/omlx](https://github.com/jundot/omlx) | +1244 | 7419 |
| 92 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1229 | 18109 |
| 93 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1214 | 6975 |
| 94 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1205 | 87598 |
| 95 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1194 | 8149 |
| 96 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1189 | 11339 |
| 97 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1170 | 78902 |
| 98 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1167 | 7419 |
| 99 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1131 | 7537 |
| 100 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1119 | 8127 |
| 101 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1059 | 7195 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1035 | 7894 |
| 103 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +936 | 52700 |
| 104 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +917 | 22008 |
| 105 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +903 | 17381 |
| 106 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +901 | 35735 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +887 | 23234 |
| 108 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +862 | 7453 |
| 109 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +847 | 27552 |
| 110 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +835 | 4382 |
| 111 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +826 | 4642 |
| 112 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +805 | 37564 |
| 113 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +791 | 45886 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +773 | 6572 |
| 115 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +771 | 36799 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +762 | 39841 |
| 117 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +758 | 28906 |
| 118 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +746 | 3435 |
| 119 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +742 | 6895 |
| 120 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +720 | 22071 |
| 121 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +711 | 4831 |
| 122 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +665 | 3830 |
| 123 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +662 | 3993 |
| 124 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +655 | 3607 |
| 125 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +645 | 4459 |
| 126 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +639 | 3720 |
| 127 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +636 | 47936 |
| 128 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +632 | 15823 |
| 129 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +611 | 2231 |
| 130 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +604 | 14457 |
| 131 | [wshobson/agents](https://github.com/wshobson/agents) | +602 | 32517 |
| 132 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +595 | 2278 |
| 133 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +568 | 7070 |
| 134 | [huggingface/skills](https://github.com/huggingface/skills) | +568 | 9961 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +564 | 8800 |
| 136 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +556 | 3776 |
| 137 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +542 | 2664 |
| 138 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +541 | 17598 |
| 139 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +539 | 47122 |
| 140 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +539 | 7720 |
| 141 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +532 | 2972 |
| 142 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +528 | 23777 |
| 143 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +527 | 24059 |
| 144 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +526 | 4592 |
| 145 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +517 | 44232 |
| 146 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +512 | 1908 |
| 147 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +510 | 3341 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +508 | 44545 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +506 | 27860 |
| 150 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +493 | 10693 |
| 151 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +471 | 2322 |
| 152 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +466 | 6123 |
| 153 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +461 | 2102 |
| 154 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +454 | 14760 |
| 155 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +453 | 10622 |
| 156 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +428 | 3540 |
| 157 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +419 | 30988 |
| 158 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +416 | 3462 |
| 159 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +416 | 22977 |
| 160 | [openclaw/skills](https://github.com/openclaw/skills) | +396 | 3562 |
| 161 | [apify/agent-skills](https://github.com/apify/agent-skills) | +394 | 1776 |
| 162 | [htdt/godogen](https://github.com/htdt/godogen) | +388 | 2271 |
| 163 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +377 | 7876 |
| 164 | [aden-hive/hive](https://github.com/aden-hive/hive) | +369 | 9936 |
| 165 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +367 | 13355 |
| 166 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +362 | 2169 |
| 167 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +361 | 6388 |
| 168 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +358 | 1777 |
| 169 | [hectorvent/floci](https://github.com/hectorvent/floci) | +358 | 2091 |
| 170 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +356 | 6998 |
| 171 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +354 | 8448 |
| 172 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +353 | 10285 |
| 173 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +349 | 26893 |
| 174 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +346 | 2366 |
| 175 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +346 | 33712 |
| 176 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +342 | 1927 |
| 177 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +340 | 1764 |
| 178 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +326 | 3684 |
| 179 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +319 | 4735 |
| 180 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +317 | 1712 |
| 181 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +315 | 1393 |
| 182 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +315 | 20048 |
| 183 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +314 | 2400 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +303 | 24965 |
| 185 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +296 | 10897 |
| 186 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +295 | 1450 |
| 187 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +279 | 1844 |
| 188 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +267 | 29780 |
| 189 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +259 | 13692 |
| 190 | [eze-is/web-access](https://github.com/eze-is/web-access) | +258 | 2082 |
| 191 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +254 | 14869 |
| 192 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +252 | 1302 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +240 | 4111 |
| 194 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +229 | 22036 |
| 195 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +217 | 1770 |
| 196 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +214 | 2347 |
| 197 | [usebruno/bruno](https://github.com/usebruno/bruno) | +209 | 41086 |
| 198 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +208 | 5706 |
| 199 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +205 | 1116 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +203 | 36103 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +197 | 7462 |
| 202 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +196 | 874 |
| 203 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +194 | 1794 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +193 | 21679 |
| 205 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +193 | 819 |
| 206 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +191 | 0 |
| 207 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +189 | 1084 |
| 208 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +180 | 8964 |
| 209 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +175 | 1000 |
| 210 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +174 | 1048 |
| 211 | [decolua/9router](https://github.com/decolua/9router) | +165 | 1382 |
| 212 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +165 | 2538 |
| 213 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +163 | 956 |
| 214 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +159 | 2483 |
| 215 | [linlay/zenmind](https://github.com/linlay/zenmind) | +158 | 216 |
| 216 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +158 | 25400 |
| 217 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +158 | 29167 |
| 218 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +153 | 1599 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +150 | 40265 |
| 220 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 579 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +146 | 2269 |
| 222 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +142 | 2629 |
| 223 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +141 | 1699 |
| 224 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +136 | 5363 |
| 225 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +135 | 680 |
| 226 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +133 | 526 |
| 227 | [jgraph/drawio](https://github.com/jgraph/drawio) | +132 | 4443 |
| 228 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +132 | 35473 |
| 229 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +131 | 655 |
| 230 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +131 | 1289 |
| 231 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +129 | 966 |
| 232 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +127 | 2506 |
| 233 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +127 | 957 |
| 234 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +122 | 13806 |
| 235 | [4ier/neo](https://github.com/4ier/neo) | +121 | 643 |
| 236 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +118 | 477 |
| 237 | [is-a-dev/register](https://github.com/is-a-dev/register) | +117 | 10035 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +117 | 1639 |
| 239 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +117 | 2227 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +114 | 26287 |
| 241 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +113 | 729 |
| 242 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +113 | 12359 |
| 243 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +111 | 10361 |
| 244 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +110 | 1797 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +109 | 33000 |
| 246 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 453 |
| 247 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +107 | 1344 |
| 248 | [skylot/jadx](https://github.com/skylot/jadx) | +107 | 47365 |
| 249 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +105 | 1480 |
| 250 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +103 | 22982 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +103 | 48784 |
| 252 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 253 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 603 |
| 254 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 439 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 579 |
| 256 | [dashersw/gea](https://github.com/dashersw/gea) | +96 | 748 |
| 257 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +96 | 1384 |
| 258 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +96 | 1486 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +96 | 12740 |
| 260 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11367 |
| 261 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +92 | 558 |
| 262 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +91 | 722 |
| 263 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +91 | 735 |
| 264 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +91 | 503 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +91 | 8994 |
| 266 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +88 | 419 |
| 267 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 268 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +85 | 855 |
| 269 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +85 | 932 |
| 270 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +84 | 1052 |
| 271 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +83 | 3303 |
| 272 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +83 | 649 |
| 273 | [idinging/freemail](https://github.com/idinging/freemail) | +82 | 1183 |
| 274 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +81 | 430 |
| 275 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +79 | 3660 |
| 276 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +78 | 3417 |
| 277 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +78 | 818 |
| 278 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +78 | 674 |
| 279 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +77 | 421 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +76 | 27077 |
| 281 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +74 | 942 |
| 282 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +73 | 400 |
| 283 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +71 | 569 |
| 284 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +71 | 37313 |
| 285 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +70 | 597 |
| 286 | [apache/kafka](https://github.com/apache/kafka) | +68 | 32043 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +67 | 8339 |
| 288 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +67 | 3201 |
| 289 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +67 | 12470 |
| 290 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +65 | 45263 |
| 291 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1550 |
| 292 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7129 |
| 293 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +62 | 418 |
| 294 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +62 | 339 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +61 | 1420 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +61 | 31476 |
| 297 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +60 | 1596 |
| 298 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +60 | 7710 |
| 299 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +59 | 26614 |
| 300 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +58 | 430 |
