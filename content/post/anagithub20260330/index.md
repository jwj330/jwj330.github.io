---
title: "2026-03-30 GitHub增长趋势报告"
description: "1.claude-howto+597 2.VibeVoice+406 3.paperclip+343 4.hermes-agent+290 5.last30days-skill+239"
date: 2026-03-30T20:49:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-30 20:49:48

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
        'daily': {"categories": ["revfactory/harness", "hesreallyhim/awesome-claude-code", "Crosstalk-Solutions/project-nomad", "nidhinjs/prompt-master", "vas3k/TaxHacker", "rtk-ai/rtk", "666ghj/MiroFish", "TauricResearch/TradingAgents", "gsd-build/get-shit-done", "mauriceboe/TREK", "thedotmack/claude-mem", "shanraisshan/claude-code-best-practice", "Panniantong/Agent-Reach", "shareAI-lab/learn-claude-code", "Yeachan-Heo/oh-my-claudecode", "mvanhorn/last30days-skill", "NousResearch/hermes-agent", "paperclipai/paperclip", "microsoft/VibeVoice", "luongnv89/claude-howto"], "data": [88, 90, 97, 99, 103, 103, 110, 113, 113, 151, 163, 172, 174, 203, 226, 239, 290, 343, 406, 597]},
        'weekly': {"categories": ["666ghj/MiroFish", "Yeachan-Heo/oh-my-claudecode", "pascalorg/editor", "tiajinsha/JKVideo", "gsd-build/get-shit-done", "msitarzewski/agency-agents", "FujiwaraChoki/MoneyPrinterV2", "TauricResearch/TradingAgents", "nextlevelbuilder/ui-ux-pro-max-skill", "NousResearch/hermes-agent", "shareAI-lab/learn-claude-code", "Crosstalk-Solutions/project-nomad", "luongnv89/claude-howto", "paperclipai/paperclip", "microsoft/RustTraining", "karpathy/autoresearch", "mvanhorn/last30days-skill", "bytedance/deer-flow", "affaan-m/everything-claude-code", "obra/superpowers"], "data": [667, 698, 712, 712, 738, 750, 777, 797, 799, 900, 909, 953, 1034, 1147, 1229, 1288, 1403, 2126, 2252, 2439]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "hesamsheikh/awesome-openclaw-usecases", "shanraisshan/claude-code-best-practice", "anomalyco/opencode", "moeru-ai/airi", "gsd-build/get-shit-done", "VoltAgent/awesome-openclaw-skills", "shareAI-lab/learn-claude-code", "googleworkspace/cli", "bytedance/deer-flow", "anthropics/skills", "koala73/worldmonitor", "666ghj/MiroFish", "paperclipai/paperclip", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3360, 3755, 3803, 4074, 4226, 4326, 4489, 4657, 4945, 5247, 5307, 6154, 7824, 7998, 8457, 10758, 12014, 12100, 12668, 23470]}
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
| 1 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +597 | 9643 |
| 2 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +406 | 29675 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +343 | 40831 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +290 | 18345 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +239 | 16329 |
| 6 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +226 | 17477 |
| 7 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +203 | 43817 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +174 | 13810 |
| 9 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +172 | 25780 |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +163 | 30678 |
| 11 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +151 | 2754 |
| 12 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +113 | 45292 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +113 | 30590 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +110 | 46215 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +103 | 15682 |
| 16 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +103 | 3341 |
| 17 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +99 | 3981 |
| 18 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +97 | 20205 |
| 19 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +90 | 34482 |
| 20 | [revfactory/harness](https://github.com/revfactory/harness) | +88 | 743 |
| 21 | [google-research/timesfm](https://github.com/google-research/timesfm) | +80 | 10938 |
| 22 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +80 | 40043 |
| 23 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +77 | 28890 |
| 24 | [ilyamiro/nixos-configuration](https://github.com/ilyamiro/nixos-configuration) | +69 | 1134 |
| 25 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +69 | 2828 |
| 26 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +68 | 35687 |
| 27 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +68 | 36610 |
| 28 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +66 | 8011 |
| 29 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +62 | 20233 |
| 30 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +61 | 28619 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | +2439 | 60312 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2252 | 51199 |
| 3 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2126 | 53960 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1403 | 16329 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1288 | 61663 |
| 6 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1229 | 11663 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1147 | 40831 |
| 8 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1034 | 9643 |
| 9 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +953 | 20205 |
| 10 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +909 | 43817 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +900 | 18345 |
| 12 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +799 | 34148 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +797 | 30590 |
| 14 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +777 | 27434 |
| 15 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +750 | 66466 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +738 | 45292 |
| 17 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +712 | 4851 |
| 18 | [pascalorg/editor](https://github.com/pascalorg/editor) | +712 | 8470 |
| 19 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +698 | 17477 |
| 20 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +667 | 46215 |
| 21 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +662 | 28619 |
| 22 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +650 | 29675 |
| 23 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +649 | 8011 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +606 | 44682 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +572 | 25780 |
| 26 | [jackwener/opencli](https://github.com/jackwener/opencli) | +538 | 9186 |
| 27 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +513 | 7467 |
| 28 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +503 | 34482 |
| 29 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +467 | 13810 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +460 | 30678 |
| 31 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +452 | 22415 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +451 | 35687 |
| 33 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +428 | 15344 |
| 34 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +384 | 15682 |
| 35 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +378 | 2828 |
| 36 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +368 | 8034 |
| 37 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +355 | 10783 |
| 38 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +350 | 2754 |
| 39 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +326 | 45508 |
| 40 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +315 | 40043 |
| 41 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +314 | 2226 |
| 42 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +314 | 39841 |
| 43 | [virattt/dexter](https://github.com/virattt/dexter) | +306 | 20585 |
| 44 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +306 | 35652 |
| 45 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +305 | 20544 |
| 46 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +303 | 18379 |
| 47 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +299 | 32196 |
| 48 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +284 | 33878 |
| 49 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +280 | 3981 |
| 50 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +279 | 20230 |
| 51 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +271 | 26029 |
| 52 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +266 | 37330 |
| 53 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +264 | 17795 |
| 54 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +263 | 14846 |
| 55 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +262 | 27087 |
| 56 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +260 | 28890 |
| 57 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +260 | 43191 |
| 58 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +260 | 22275 |
| 59 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +257 | 2583 |
| 60 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +254 | 13366 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +252 | 21385 |
| 62 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +245 | 29354 |
| 63 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +245 | 20800 |
| 64 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +242 | 2302 |
| 65 | [eze-is/web-access](https://github.com/eze-is/web-access) | +240 | 2772 |
| 66 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +240 | 9608 |
| 67 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +239 | 33872 |
| 68 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +234 | 7156 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +231 | 17625 |
| 70 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +225 | 28314 |
| 71 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +224 | 20233 |
| 72 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +222 | 12438 |
| 73 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +217 | 37105 |
| 74 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +211 | 20068 |
| 75 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +208 | 8019 |
| 76 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +207 | 36610 |
| 77 | [mattpocock/skills](https://github.com/mattpocock/skills) | +205 | 10985 |
| 78 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +203 | 8133 |
| 79 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +203 | 36799 |
| 80 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +195 | 2597 |
| 81 | [usestrix/strix](https://github.com/usestrix/strix) | +190 | 22823 |
| 82 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +190 | 25784 |
| 83 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +187 | 9334 |
| 84 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +187 | 1339 |
| 85 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +185 | 4841 |
| 86 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +184 | 3367 |
| 87 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +180 | 1499 |
| 88 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +177 | 28090 |
| 89 | [tw93/Mole](https://github.com/tw93/Mole) | +173 | 36870 |
| 90 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +172 | 3303 |
| 91 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +169 | 18223 |
| 92 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +167 | 32398 |
| 93 | [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | +163 | 1421 |
| 94 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +161 | 1388 |
| 95 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +160 | 1878 |
| 96 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +157 | 7697 |
| 97 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +157 | 8319 |
| 98 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +153 | 17852 |
| 99 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +142 | 4100 |
| 100 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +138 | 15406 |
| 101 | [revfactory/harness](https://github.com/revfactory/harness) | +130 | 743 |
| 102 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +130 | 27691 |
| 103 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +130 | 6664 |
| 104 | [facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) | +128 | 1034 |
| 105 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +126 | 992 |
| 106 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +122 | 1406 |
| 107 | [jundot/omlx](https://github.com/jundot/omlx) | +119 | 7552 |
| 108 | [punitarani/fli](https://github.com/punitarani/fli) | +115 | 892 |
| 109 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +113 | 31157 |
| 110 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +112 | 2415 |
| 111 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +112 | 2941 |
| 112 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +107 | 16758 |
| 113 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +105 | 25992 |
| 114 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +104 | 3338 |
| 115 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +99 | 4547 |
| 116 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +99 | 17658 |
| 117 | [mozilla-ai/cq](https://github.com/mozilla-ai/cq) | +95 | 876 |
| 118 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +94 | 13719 |
| 119 | [jxnxts/mcp-brasil](https://github.com/jxnxts/mcp-brasil) | +94 | 926 |
| 120 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +94 | 1056 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +23470 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12668 | 66466 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12100 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12014 | 61663 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10758 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8457 | 44682 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7998 | 40831 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7824 | 46216 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6154 | 45508 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5307 | 74774 |
| 11 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5247 | 53960 |
| 12 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4945 | 23201 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4657 | 43817 |
| 14 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4489 | 43191 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4326 | 45292 |
| 16 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4226 | 36610 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4074 | 109881 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3803 | 25780 |
| 19 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3755 | 28090 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3360 | 34148 |
| 21 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3259 | 33872 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3190 | 20205 |
| 23 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3190 | 13719 |
| 24 | [openai/symphony](https://github.com/openai/symphony) | +3080 | 14288 |
| 25 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3068 | 15925 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3050 | 20068 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2994 | 20800 |
| 28 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2880 | 18345 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2876 | 14691 |
| 30 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2823 | 20233 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2766 | 35688 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2744 | 85286 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2695 | 14846 |
| 34 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2666 | 69674 |
| 35 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2622 | 17795 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2583 | 26029 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2484 | 27087 |
| 38 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2471 | 27434 |
| 39 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2446 | 28890 |
| 40 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2400 | 28619 |
| 41 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2352 | 37105 |
| 42 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2316 | 15682 |
| 43 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2305 | 30590 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2292 | 29354 |
| 45 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2257 | 13810 |
| 46 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2178 | 13366 |
| 47 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2142 | 25992 |
| 48 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2124 | 37330 |
| 49 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2073 | 8468 |
| 50 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2070 | 7789 |
| 51 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2057 | 10630 |
| 52 | [github/spec-kit](https://github.com/github/spec-kit) | +2051 | 71722 |
| 53 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2046 | 12314 |
| 54 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2042 | 28314 |
| 55 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2023 | 30678 |
| 56 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2013 | 0 |
| 57 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2012 | 60117 |
| 58 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1969 | 34928 |
| 59 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1962 | 33878 |
| 60 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1901 | 15344 |
| 61 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1898 | 9594 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1881 | 21385 |
| 63 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1843 | 25784 |
| 64 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1806 | 8443 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1785 | 35652 |
| 66 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1769 | 9222 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1731 | 11152 |
| 68 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1707 | 16330 |
| 69 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1697 | 122870 |
| 70 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1677 | 32196 |
| 71 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1604 | 17852 |
| 72 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1602 | 34482 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1567 | 10783 |
| 74 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1556 | 18223 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1514 | 18798 |
| 76 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1498 | 10985 |
| 77 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1490 | 16758 |
| 78 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1484 | 17477 |
| 79 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1474 | 36859 |
| 80 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1464 | 98536 |
| 81 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1460 | 9186 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1458 | 17625 |
| 83 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1450 | 9608 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1406 | 15406 |
| 85 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1399 | 96919 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +1397 | 36870 |
| 87 | [openai/skills](https://github.com/openai/skills) | +1355 | 15761 |
| 88 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1341 | 9334 |
| 89 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1326 | 43973 |
| 90 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1285 | 26787 |
| 91 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1259 | 18379 |
| 92 | [jundot/omlx](https://github.com/jundot/omlx) | +1251 | 7552 |
| 93 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1239 | 7157 |
| 94 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1229 | 11663 |
| 95 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1218 | 87598 |
| 96 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1217 | 12438 |
| 97 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1213 | 8319 |
| 98 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1192 | 8011 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1192 | 78902 |
| 100 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1185 | 7697 |
| 101 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1179 | 8470 |
| 102 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1102 | 7467 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1076 | 8133 |
| 104 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1056 | 9643 |
| 105 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +963 | 22415 |
| 106 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +956 | 52700 |
| 107 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +916 | 17467 |
| 108 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +906 | 35735 |
| 109 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +903 | 23333 |
| 110 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +884 | 79656 |
| 111 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +865 | 7490 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +863 | 27691 |
| 113 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +845 | 4841 |
| 114 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +842 | 4423 |
| 115 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +831 | 37564 |
| 116 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +805 | 45886 |
| 117 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +794 | 39841 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +791 | 36799 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +785 | 6664 |
| 120 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +758 | 28939 |
| 121 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +752 | 22275 |
| 122 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +749 | 29675 |
| 123 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +748 | 3443 |
| 124 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +746 | 6938 |
| 125 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +712 | 4851 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +683 | 4100 |
| 127 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +673 | 3880 |
| 128 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +661 | 4547 |
| 129 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +657 | 3620 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +651 | 47936 |
| 131 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +650 | 3782 |
| 132 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +635 | 15842 |
| 133 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +614 | 2246 |
| 134 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +612 | 14558 |
| 135 | [wshobson/agents](https://github.com/wshobson/agents) | +611 | 32581 |
| 136 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +596 | 2298 |
| 137 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +576 | 7109 |
| 138 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +573 | 8862 |
| 139 | [huggingface/skills](https://github.com/huggingface/skills) | +570 | 9983 |
| 140 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +566 | 8019 |
| 141 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +561 | 3830 |
| 142 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +550 | 47122 |
| 143 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +549 | 17658 |
| 144 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +548 | 3023 |
| 145 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +548 | 2692 |
| 146 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +539 | 24123 |
| 147 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +532 | 44232 |
| 148 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +531 | 23830 |
| 149 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +529 | 4613 |
| 150 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +527 | 44545 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +519 | 27957 |
| 152 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +515 | 1912 |
| 153 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +514 | 3366 |
| 154 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +504 | 10771 |
| 155 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +471 | 2342 |
| 156 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +460 | 10671 |
| 157 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +458 | 14792 |
| 158 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +432 | 31157 |
| 159 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +431 | 3561 |
| 160 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +418 | 3476 |
| 161 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +418 | 22990 |
| 162 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +408 | 8034 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +402 | 3603 |
| 164 | [apify/agent-skills](https://github.com/apify/agent-skills) | +397 | 1787 |
| 165 | [htdt/godogen](https://github.com/htdt/godogen) | +396 | 2349 |
| 166 | [hectorvent/floci](https://github.com/hectorvent/floci) | +387 | 2273 |
| 167 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +377 | 2829 |
| 168 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +372 | 7106 |
| 169 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +371 | 2237 |
| 170 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +370 | 2415 |
| 171 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +370 | 1836 |
| 172 | [aden-hive/hive](https://github.com/aden-hive/hive) | +369 | 9954 |
| 173 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +369 | 13378 |
| 174 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +367 | 10363 |
| 175 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +365 | 6414 |
| 176 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +357 | 8438 |
| 177 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +354 | 20230 |
| 178 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +352 | 1973 |
| 179 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +352 | 33712 |
| 180 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +344 | 1795 |
| 181 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +327 | 4782 |
| 182 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +326 | 1752 |
| 183 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +326 | 3694 |
| 184 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +315 | 1408 |
| 185 | [eze-is/web-access](https://github.com/eze-is/web-access) | +315 | 2772 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +312 | 25026 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +301 | 10624 |
| 188 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +300 | 1485 |
| 189 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +288 | 1893 |
| 190 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +278 | 29780 |
| 191 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +260 | 13713 |
| 192 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +258 | 1351 |
| 193 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +255 | 2597 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +255 | 14896 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +247 | 4173 |
| 196 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +238 | 1878 |
| 197 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +238 | 22069 |
| 198 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +217 | 36103 |
| 199 | [usebruno/bruno](https://github.com/usebruno/bruno) | +216 | 41086 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +216 | 7279 |
| 201 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +214 | 5744 |
| 202 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +210 | 1137 |
| 203 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +205 | 1037 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +203 | 21721 |
| 205 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +198 | 1040 |
| 206 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +197 | 878 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +197 | 843 |
| 208 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +195 | 1799 |
| 209 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +191 | 0 |
| 210 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +181 | 8973 |
| 211 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +174 | 1056 |
| 212 | [decolua/9router](https://github.com/decolua/9router) | +173 | 1411 |
| 213 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +170 | 2567 |
| 214 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +163 | 955 |
| 215 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +160 | 2485 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +159 | 29195 |
| 217 | [linlay/zenmind](https://github.com/linlay/zenmind) | +158 | 216 |
| 218 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +158 | 25407 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +157 | 40265 |
| 220 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +156 | 1622 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +150 | 2305 |
| 222 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +148 | 2644 |
| 223 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 578 |
| 224 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +143 | 1710 |
| 225 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +140 | 5379 |
| 226 | [jgraph/drawio](https://github.com/jgraph/drawio) | +136 | 4462 |
| 227 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +136 | 993 |
| 228 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +136 | 35473 |
| 229 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +135 | 685 |
| 230 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 527 |
| 231 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +134 | 1300 |
| 232 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +131 | 2516 |
| 233 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +131 | 659 |
| 234 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +129 | 968 |
| 235 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +125 | 13819 |
| 236 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +121 | 12404 |
| 237 | [4ier/neo](https://github.com/4ier/neo) | +121 | 649 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +121 | 2246 |
| 239 | [robinebers/openusage](https://github.com/robinebers/openusage) | +119 | 1645 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +119 | 26312 |
| 241 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +118 | 480 |
| 242 | [is-a-dev/register](https://github.com/is-a-dev/register) | +117 | 10034 |
| 243 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +116 | 811 |
| 244 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +115 | 10394 |
| 245 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +114 | 735 |
| 246 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +113 | 1811 |
| 247 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +113 | 33000 |
| 248 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +111 | 23002 |
| 249 | [skylot/jadx](https://github.com/skylot/jadx) | +110 | 47365 |
| 250 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 455 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +107 | 1369 |
| 252 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +106 | 48784 |
| 253 | [dashersw/gea](https://github.com/dashersw/gea) | +105 | 782 |
| 254 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +105 | 1480 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +103 | 1504 |
| 256 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +102 | 440 |
| 257 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 521 |
| 258 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 603 |
| 259 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 587 |
| 260 | [microg/GmsCore](https://github.com/microg/GmsCore) | +98 | 12746 |
| 261 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +97 | 1397 |
| 262 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 11385 |
| 263 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +95 | 574 |
| 264 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +93 | 750 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +93 | 9009 |
| 266 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +91 | 426 |
| 267 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +91 | 510 |
| 268 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 269 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +87 | 1056 |
| 270 | [idinging/freemail](https://github.com/idinging/freemail) | +85 | 1199 |
| 271 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +84 | 3312 |
| 272 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +83 | 650 |
| 273 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +82 | 3677 |
| 274 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +82 | 1109 |
| 275 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +82 | 834 |
| 276 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +81 | 449 |
| 277 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3431 |
| 278 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +80 | 679 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +80 | 27090 |
| 280 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +78 | 595 |
| 281 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +78 | 423 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +78 | 3302 |
| 283 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +77 | 418 |
| 284 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +75 | 955 |
| 285 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +71 | 37313 |
| 286 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +70 | 609 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +69 | 8352 |
| 288 | [apache/kafka](https://github.com/apache/kafka) | +69 | 32043 |
| 289 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +69 | 12481 |
| 290 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +68 | 45263 |
| 291 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +66 | 417 |
| 292 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7141 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1561 |
| 294 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +64 | 31476 |
| 295 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +63 | 342 |
| 296 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +63 | 1424 |
| 297 | [crimera/piko](https://github.com/crimera/piko) | +63 | 2970 |
| 298 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +62 | 26623 |
| 299 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +61 | 462 |
| 300 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1605 |
