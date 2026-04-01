---
title: "2026-04-01 GitHub增长趋势报告"
description: "1.claude-code+1133 2.oh-my-codex+428 3.claude-howto+350 4.openscreen+321 5.codex-plugin-cc+261"
date: 2026-04-01T20:47:34+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-01 20:47:34

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
        'daily': {"categories": ["TauricResearch/TradingAgents", "34306/vphone-aio", "farion1231/cc-switch", "Nahuel990/ministack", "m3y54m/Embedded-Engineering-Roadmap", "Piebald-AI/claude-code-system-prompts", "666ghj/MiroFish", "ssrajadh/sentrysearch", "paperclipai/paperclip", "NousResearch/hermes-agent", "shareAI-lab/learn-claude-code", "TheTom/turboquant_plus", "microsoft/VibeVoice", "shanraisshan/claude-code-best-practice", "Yeachan-Heo/oh-my-claudecode", "openai/codex-plugin-cc", "siddharthvaddem/openscreen", "luongnv89/claude-howto", "Yeachan-Heo/oh-my-codex", "anthropics/claude-code"], "data": [63, 63, 64, 68, 69, 75, 89, 99, 117, 151, 159, 167, 194, 238, 246, 261, 321, 350, 428, 1133]},
        'weekly': {"categories": ["666ghj/MiroFish", "msitarzewski/agency-agents", "microsoft/RustTraining", "nextlevelbuilder/ui-ux-pro-max-skill", "hacksider/Deep-Live-Cam", "openai/codex-plugin-cc", "shanraisshan/claude-code-best-practice", "shareAI-lab/learn-claude-code", "NousResearch/hermes-agent", "JCodesMore/ai-website-cloner-template", "karpathy/autoresearch", "Yeachan-Heo/oh-my-claudecode", "microsoft/VibeVoice", "paperclipai/paperclip", "mvanhorn/last30days-skill", "bytedance/deer-flow", "anthropics/claude-code", "luongnv89/claude-howto", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [625, 679, 703, 772, 866, 873, 911, 920, 955, 974, 976, 980, 1298, 1312, 1326, 1361, 1465, 1631, 2282, 2671]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/claude-code", "moeru-ai/airi", "anomalyco/opencode", "shanraisshan/claude-code-best-practice", "VoltAgent/awesome-openclaw-skills", "gsd-build/get-shit-done", "shareAI-lab/learn-claude-code", "googleworkspace/cli", "anthropics/skills", "bytedance/deer-flow", "koala73/worldmonitor", "ruvnet/RuView", "666ghj/MiroFish", "paperclipai/paperclip", "obra/superpowers", "karpathy/autoresearch", "msitarzewski/agency-agents", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [3421, 3647, 3948, 4052, 4157, 4176, 4233, 4818, 4973, 5257, 5275, 5713, 7026, 7970, 8286, 10900, 12202, 12820, 12957, 22713]}
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
| 1 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1133 | 69674 |
| 2 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +428 | 8232 |
| 3 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +350 | 15360 |
| 4 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +321 | 12937 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +261 | 8154 |
| 6 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +246 | 20636 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +238 | 30364 |
| 8 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +194 | 34301 |
| 9 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +167 | 4772 |
| 10 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +159 | 46356 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +151 | 21453 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +117 | 43678 |
| 13 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +99 | 2316 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +89 | 47563 |
| 15 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +75 | 7924 |
| 16 | [m3y54m/Embedded-Engineering-Roadmap](https://github.com/m3y54m/Embedded-Engineering-Roadmap) | +69 | 10548 |
| 17 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +68 | 1143 |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +64 | 37051 |
| 19 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +63 | 2373 |
| 20 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +63 | 30590 |
| 21 | [9bow/legalize-kr](https://github.com/9bow/legalize-kr) | +60 | 484 |
| 22 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +58 | 30678 |
| 23 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +56 | 4351 |
| 24 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +55 | 35479 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +53 | 29789 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +51 | 20974 |
| 27 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +49 | 37330 |
| 28 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +48 | 17259 |
| 29 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +48 | 46520 |
| 30 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +47 | 33878 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2671 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2282 | 60312 |
| 3 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1631 | 15360 |
| 4 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1465 | 69674 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1361 | 55981 |
| 6 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1326 | 17259 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1312 | 43678 |
| 8 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1298 | 34301 |
| 9 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +980 | 20637 |
| 10 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +976 | 63384 |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +974 | 6917 |
| 12 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +955 | 21453 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +920 | 46356 |
| 14 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +911 | 30364 |
| 15 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +873 | 8154 |
| 16 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +866 | 79656 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +772 | 34148 |
| 18 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +703 | 12127 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +679 | 68138 |
| 20 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +625 | 47563 |
| 21 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +620 | 46520 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +595 | 20974 |
| 23 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +518 | 30590 |
| 24 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +512 | 14371 |
| 25 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +502 | 4772 |
| 26 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +487 | 8232 |
| 27 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +482 | 30678 |
| 28 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +452 | 29170 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +441 | 37051 |
| 30 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +429 | 8513 |
| 31 | [jackwener/opencli](https://github.com/jackwener/opencli) | +409 | 10421 |
| 32 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +409 | 45137 |
| 33 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +388 | 3279 |
| 34 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +381 | 35479 |
| 35 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +376 | 3012 |
| 36 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +376 | 8146 |
| 37 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +368 | 7796 |
| 38 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +353 | 16432 |
| 39 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +348 | 2585 |
| 40 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +343 | 12937 |
| 41 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +342 | 16005 |
| 42 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +340 | 22741 |
| 43 | [millionco/expect](https://github.com/millionco/expect) | +338 | 2978 |
| 44 | [pascalorg/editor](https://github.com/pascalorg/editor) | +337 | 9013 |
| 45 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +304 | 27856 |
| 46 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +300 | 40043 |
| 47 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +299 | 4294 |
| 48 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +290 | 20392 |
| 49 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +287 | 29789 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +285 | 33878 |
| 51 | [virattt/dexter](https://github.com/virattt/dexter) | +284 | 20740 |
| 52 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +273 | 37330 |
| 53 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +272 | 8639 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +265 | 36335 |
| 55 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +259 | 45897 |
| 56 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +253 | 10937 |
| 57 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +247 | 30180 |
| 58 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +242 | 27538 |
| 59 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +240 | 32848 |
| 60 | [alvinunreal/awesome-opensource-ai](https://github.com/alvinunreal/awesome-opensource-ai) | +240 | 2229 |
| 61 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +233 | 26519 |
| 62 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +229 | 43609 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +218 | 18206 |
| 64 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +214 | 15290 |
| 65 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +213 | 20849 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +211 | 22013 |
| 67 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +211 | 2765 |
| 68 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +209 | 18764 |
| 69 | [revfactory/harness](https://github.com/revfactory/harness) | +206 | 1413 |
| 70 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +206 | 20643 |
| 71 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +204 | 39841 |
| 72 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +203 | 21141 |
| 73 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +203 | 36799 |
| 74 | [eze-is/web-access](https://github.com/eze-is/web-access) | +200 | 3377 |
| 75 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +199 | 34162 |
| 76 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +197 | 13627 |
| 77 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +196 | 8616 |
| 78 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +189 | 28612 |
| 79 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +188 | 36827 |
| 80 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +182 | 18091 |
| 81 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +182 | 2460 |
| 82 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +178 | 4002 |
| 83 | [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | +177 | 1530 |
| 84 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +175 | 1511 |
| 85 | [usestrix/strix](https://github.com/usestrix/strix) | +174 | 22964 |
| 86 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +171 | 7495 |
| 87 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +170 | 2317 |
| 88 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +170 | 26135 |
| 89 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +170 | 3512 |
| 90 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +166 | 37505 |
| 91 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +166 | 20407 |
| 92 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +162 | 5154 |
| 93 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +160 | 1148 |
| 94 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +155 | 1756 |
| 95 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 18054 |
| 96 | [chrisryugj/korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp) | +152 | 910 |
| 97 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +152 | 8213 |
| 98 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +152 | 32748 |
| 99 | [facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) | +151 | 1237 |
| 100 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +151 | 22499 |
| 101 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +149 | 12429 |
| 102 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +148 | 9905 |
| 103 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +145 | 9705 |
| 104 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +145 | 18568 |
| 105 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +140 | 7924 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +140 | 15689 |
| 107 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +139 | 8650 |
| 108 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +134 | 1528 |
| 109 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +131 | 6797 |
| 110 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +130 | 1143 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +130 | 28041 |
| 112 | [punitarani/fli](https://github.com/punitarani/fli) | +126 | 957 |
| 113 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +118 | 2373 |
| 114 | [google-research/timesfm](https://github.com/google-research/timesfm) | +115 | 11891 |
| 115 | [jundot/omlx](https://github.com/jundot/omlx) | +113 | 7998 |
| 116 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +113 | 4252 |
| 117 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +113 | 31361 |
| 118 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +108 | 17041 |
| 119 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +103 | 2547 |
| 120 | [jxnxts/mcp-brasil](https://github.com/jxnxts/mcp-brasil) | +102 | 1012 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +22713 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12957 | 51199 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12820 | 68138 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12202 | 63384 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10900 | 60312 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8286 | 43679 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7970 | 47563 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +7026 | 45137 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +5713 | 45898 |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5275 | 55981 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +5257 | 74774 |
| 12 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4973 | 23474 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4818 | 46356 |
| 14 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4233 | 46520 |
| 15 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4176 | 43609 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4157 | 30364 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4052 | 109881 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3948 | 36827 |
| 19 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3647 | 69674 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3421 | 34148 |
| 21 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3272 | 20974 |
| 22 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3165 | 28327 |
| 23 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3099 | 21453 |
| 24 | [openai/symphony](https://github.com/openai/symphony) | +3089 | 14394 |
| 25 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3072 | 20407 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3036 | 34162 |
| 27 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2896 | 14908 |
| 28 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2851 | 21141 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2761 | 37051 |
| 30 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2760 | 85286 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2746 | 15290 |
| 32 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2657 | 18091 |
| 33 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2657 | 14105 |
| 34 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2631 | 20643 |
| 35 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2628 | 26519 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2453 | 27538 |
| 37 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2433 | 27857 |
| 38 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2405 | 16095 |
| 39 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2404 | 30590 |
| 40 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2318 | 29789 |
| 41 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2316 | 16432 |
| 42 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2245 | 37505 |
| 43 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2233 | 30180 |
| 44 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2223 | 13627 |
| 45 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2169 | 29169 |
| 46 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2153 | 9216 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2128 | 14371 |
| 48 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2108 | 37330 |
| 49 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2079 | 7936 |
| 50 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2068 | 12428 |
| 51 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2049 | 30678 |
| 52 | [github/spec-kit](https://github.com/github/spec-kit) | +2047 | 71722 |
| 53 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2029 | 28612 |
| 54 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1979 | 26177 |
| 55 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1967 | 16005 |
| 56 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1946 | 35077 |
| 57 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1938 | 33878 |
| 58 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1889 | 60117 |
| 59 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1877 | 22013 |
| 60 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1819 | 8612 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1817 | 36335 |
| 62 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1815 | 0 |
| 63 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1812 | 26135 |
| 64 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1800 | 17259 |
| 65 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1786 | 20637 |
| 66 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1728 | 9303 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1707 | 11267 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1656 | 32848 |
| 69 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1652 | 15360 |
| 70 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +1646 | 10710 |
| 71 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1644 | 35480 |
| 72 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1603 | 18054 |
| 73 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1582 | 18568 |
| 74 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1578 | 10937 |
| 75 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1559 | 10421 |
| 76 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1535 | 122870 |
| 77 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1522 | 11282 |
| 78 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1521 | 19032 |
| 79 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1498 | 9675 |
| 80 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1478 | 9905 |
| 81 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1475 | 36925 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1457 | 18206 |
| 83 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1440 | 17041 |
| 84 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1438 | 98536 |
| 85 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1414 | 15689 |
| 86 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1402 | 34301 |
| 87 | [openai/codex](https://github.com/openai/codex) | +1385 | 61744 |
| 88 | [tw93/Mole](https://github.com/tw93/Mole) | +1378 | 36870 |
| 89 | [openai/skills](https://github.com/openai/skills) | +1334 | 15950 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1323 | 9705 |
| 91 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1322 | 43973 |
| 92 | [jundot/omlx](https://github.com/jundot/omlx) | +1301 | 7998 |
| 93 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1277 | 7495 |
| 94 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1268 | 12128 |
| 95 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1258 | 96919 |
| 96 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1251 | 18764 |
| 97 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1244 | 9013 |
| 98 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1242 | 8513 |
| 99 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1240 | 8213 |
| 100 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1236 | 8650 |
| 101 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1206 | 78902 |
| 102 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1124 | 7796 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1097 | 8616 |
| 104 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1010 | 79656 |
| 105 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +978 | 22741 |
| 106 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +974 | 6917 |
| 107 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +961 | 87598 |
| 108 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +960 | 52700 |
| 109 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +904 | 35735 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +876 | 5154 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +867 | 28042 |
| 112 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +860 | 17659 |
| 113 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +857 | 8154 |
| 114 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +835 | 39841 |
| 115 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +822 | 7548 |
| 116 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +812 | 37564 |
| 117 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +803 | 4516 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +799 | 6797 |
| 119 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +799 | 45886 |
| 120 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +796 | 23529 |
| 121 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +773 | 36799 |
| 122 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +762 | 22499 |
| 123 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +756 | 28994 |
| 124 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +749 | 3463 |
| 125 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +715 | 4882 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +694 | 4252 |
| 127 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +681 | 3952 |
| 128 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +671 | 4662 |
| 129 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +660 | 3957 |
| 130 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +659 | 3636 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +648 | 47936 |
| 132 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +632 | 15865 |
| 133 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +619 | 7034 |
| 134 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +617 | 8639 |
| 135 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +601 | 14770 |
| 136 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +596 | 3388 |
| 137 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +581 | 8969 |
| 138 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +573 | 3933 |
| 139 | [wshobson/agents](https://github.com/wshobson/agents) | +570 | 32749 |
| 140 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +563 | 47122 |
| 141 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +557 | 2755 |
| 142 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +535 | 28155 |
| 143 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +531 | 17817 |
| 144 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +529 | 4655 |
| 145 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +522 | 44545 |
| 146 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +519 | 1910 |
| 147 | [huggingface/skills](https://github.com/huggingface/skills) | +512 | 10003 |
| 148 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +506 | 24236 |
| 149 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +502 | 44232 |
| 150 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +498 | 4772 |
| 151 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +491 | 23990 |
| 152 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +470 | 2373 |
| 153 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +470 | 10927 |
| 154 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +464 | 2136 |
| 155 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +461 | 14848 |
| 156 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +456 | 7157 |
| 157 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +453 | 31361 |
| 158 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +453 | 3469 |
| 159 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +443 | 3279 |
| 160 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +439 | 7924 |
| 161 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +437 | 10781 |
| 162 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +430 | 4965 |
| 163 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +422 | 3519 |
| 164 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +418 | 8146 |
| 165 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +414 | 3605 |
| 166 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +411 | 23165 |
| 167 | [htdt/godogen](https://github.com/htdt/godogen) | +409 | 2443 |
| 168 | [hectorvent/floci](https://github.com/hectorvent/floci) | +403 | 2471 |
| 169 | [openclaw/skills](https://github.com/openclaw/skills) | +391 | 3684 |
| 170 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +389 | 1975 |
| 171 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +382 | 2547 |
| 172 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +379 | 2394 |
| 173 | [eze-is/web-access](https://github.com/eze-is/web-access) | +370 | 3377 |
| 174 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +367 | 13423 |
| 175 | [aden-hive/hive](https://github.com/aden-hive/hive) | +365 | 9973 |
| 176 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +362 | 20392 |
| 177 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +352 | 2044 |
| 178 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +351 | 6469 |
| 179 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +337 | 33712 |
| 180 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +332 | 10485 |
| 181 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +331 | 1803 |
| 182 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +329 | 4903 |
| 183 | [apify/agent-skills](https://github.com/apify/agent-skills) | +329 | 1804 |
| 184 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +324 | 1855 |
| 185 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +324 | 3712 |
| 186 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +316 | 1418 |
| 187 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +305 | 1549 |
| 188 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +304 | 1979 |
| 189 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +299 | 25110 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +294 | 10751 |
| 191 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +276 | 29780 |
| 192 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +271 | 2765 |
| 193 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +266 | 1408 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +254 | 14952 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +251 | 4298 |
| 196 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +250 | 13744 |
| 197 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +249 | 2056 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +236 | 22190 |
| 199 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +229 | 1429 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +220 | 7348 |
| 201 | [usebruno/bruno](https://github.com/usebruno/bruno) | +218 | 41086 |
| 202 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +215 | 1205 |
| 203 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +214 | 36103 |
| 204 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +211 | 5879 |
| 205 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +210 | 1125 |
| 206 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +198 | 861 |
| 207 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +197 | 883 |
| 208 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +190 | 21764 |
| 209 | [decolua/9router](https://github.com/decolua/9router) | +185 | 1587 |
| 210 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +181 | 8985 |
| 211 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +174 | 1087 |
| 212 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +172 | 1812 |
| 213 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +172 | 2587 |
| 214 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2490 |
| 215 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +160 | 1148 |
| 216 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +154 | 2687 |
| 217 | [linlay/zenmind](https://github.com/linlay/zenmind) | +153 | 216 |
| 218 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +152 | 1654 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +152 | 40265 |
| 220 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +152 | 25419 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +152 | 2359 |
| 222 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +147 | 802 |
| 223 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +147 | 954 |
| 224 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 585 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +147 | 29239 |
| 226 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +144 | 0 |
| 227 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +137 | 757 |
| 228 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +136 | 1720 |
| 229 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +136 | 5427 |
| 230 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +136 | 1057 |
| 231 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 528 |
| 232 | [jgraph/drawio](https://github.com/jgraph/drawio) | +134 | 4517 |
| 233 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +134 | 1319 |
| 234 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +132 | 35473 |
| 235 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +131 | 664 |
| 236 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +126 | 13832 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +122 | 26343 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +121 | 12447 |
| 239 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +121 | 509 |
| 240 | [4ier/neo](https://github.com/4ier/neo) | +120 | 652 |
| 241 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +120 | 921 |
| 242 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +116 | 751 |
| 243 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10043 |
| 244 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +115 | 10463 |
| 245 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +114 | 2532 |
| 246 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +113 | 33000 |
| 247 | [dashersw/gea](https://github.com/dashersw/gea) | +110 | 818 |
| 248 | [robinebers/openusage](https://github.com/robinebers/openusage) | +110 | 1659 |
| 249 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +110 | 23049 |
| 250 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +109 | 1403 |
| 251 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +109 | 2231 |
| 252 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +108 | 1835 |
| 253 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 459 |
| 254 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +104 | 1530 |
| 255 | [skylot/jadx](https://github.com/skylot/jadx) | +104 | 47365 |
| 256 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 521 |
| 257 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +101 | 593 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +101 | 48784 |
| 259 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 446 |
| 260 | [microg/GmsCore](https://github.com/microg/GmsCore) | +97 | 12761 |
| 261 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +96 | 776 |
| 262 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +96 | 448 |
| 263 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +96 | 608 |
| 264 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +95 | 531 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +95 | 9049 |
| 266 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +92 | 1415 |
| 267 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +91 | 11419 |
| 268 | [idinging/freemail](https://github.com/idinging/freemail) | +89 | 1243 |
| 269 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +89 | 603 |
| 270 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 471 |
| 271 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +84 | 870 |
| 272 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +83 | 463 |
| 273 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +82 | 648 |
| 274 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +82 | 1148 |
| 275 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +80 | 438 |
| 276 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3459 |
| 277 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +80 | 684 |
| 278 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +79 | 1061 |
| 279 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +79 | 3352 |
| 280 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +78 | 993 |
| 281 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +78 | 426 |
| 282 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +77 | 3733 |
| 283 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +77 | 27101 |
| 284 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +70 | 8376 |
| 285 | [apache/kafka](https://github.com/apache/kafka) | +70 | 32043 |
| 286 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +70 | 37313 |
| 287 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +69 | 555 |
| 288 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +69 | 45263 |
| 289 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +67 | 420 |
| 290 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +67 | 31476 |
| 291 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +64 | 630 |
| 292 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +64 | 415 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1577 |
| 294 | [crimera/piko](https://github.com/crimera/piko) | +64 | 2993 |
| 295 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +64 | 26645 |
| 296 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +63 | 347 |
| 297 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1623 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +61 | 1438 |
| 299 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +60 | 7725 |
| 300 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +59 | 7151 |
