---
title: "2026-03-31 GitHub增长趋势报告"
description: "1.VibeVoice+478 2.claude-howto+277 3.turboquant_plus+254 4.claude-code-best-practice+228 5.paperclip+193"
date: 2026-03-31T20:45:40+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-31 20:45:40

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
        'daily': {"categories": ["34306/vphone-aio", "jackwener/opencli", "zai-org/GLM-OCR", "electrikmilk/cherri", "Panniantong/Agent-Reach", "666ghj/MiroFish", "TauricResearch/TradingAgents", "thedotmack/claude-mem", "gsd-build/get-shit-done", "mvanhorn/last30days-skill", "farion1231/cc-switch", "doodlum/skyrim-community-shaders", "Yeachan-Heo/oh-my-claudecode", "shareAI-lab/learn-claude-code", "NousResearch/hermes-agent", "paperclipai/paperclip", "shanraisshan/claude-code-best-practice", "TheTom/turboquant_plus", "luongnv89/claude-howto", "microsoft/VibeVoice"], "data": [53, 58, 59, 61, 61, 67, 69, 69, 71, 72, 73, 75, 89, 125, 175, 193, 228, 254, 277, 478]},
        'weekly': {"categories": ["666ghj/MiroFish", "TauricResearch/TradingAgents", "gsd-build/get-shit-done", "msitarzewski/agency-agents", "Crosstalk-Solutions/project-nomad", "shanraisshan/claude-code-best-practice", "Yeachan-Heo/oh-my-claudecode", "nextlevelbuilder/ui-ux-pro-max-skill", "hacksider/Deep-Live-Cam", "shareAI-lab/learn-claude-code", "NousResearch/hermes-agent", "microsoft/VibeVoice", "microsoft/RustTraining", "karpathy/autoresearch", "paperclipai/paperclip", "luongnv89/claude-howto", "mvanhorn/last30days-skill", "bytedance/deer-flow", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [623, 647, 669, 695, 733, 737, 764, 796, 823, 878, 931, 1122, 1149, 1155, 1268, 1287, 1447, 1724, 2341, 2442]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "hesamsheikh/awesome-openclaw-usecases", "shanraisshan/claude-code-best-practice", "anomalyco/opencode", "moeru-ai/airi", "gsd-build/get-shit-done", "VoltAgent/awesome-openclaw-skills", "shareAI-lab/learn-claude-code", "googleworkspace/cli", "bytedance/deer-flow", "anthropics/skills", "koala73/worldmonitor", "666ghj/MiroFish", "paperclipai/paperclip", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3452, 3767, 4026, 4131, 4237, 4399, 4517, 4767, 4960, 5369, 5432, 6181, 7889, 8180, 8479, 11011, 12119, 12669, 12732, 23618]}
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
| 1 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +478 | 32921 |
| 2 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +277 | 12618 |
| 3 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +254 | 3674 |
| 4 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +228 | 28335 |
| 5 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +193 | 42439 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +175 | 20131 |
| 7 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +125 | 45037 |
| 8 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +89 | 18749 |
| 9 | [doodlum/skyrim-community-shaders](https://github.com/doodlum/skyrim-community-shaders) | +75 | 890 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +73 | 36345 |
| 11 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +72 | 16856 |
| 12 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +71 | 45955 |
| 13 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +69 | 30678 |
| 14 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +69 | 30590 |
| 15 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +67 | 46923 |
| 16 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +61 | 14149 |
| 17 | [electrikmilk/cherri](https://github.com/electrikmilk/cherri) | +61 | 1201 |
| 18 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +59 | 4625 |
| 19 | [jackwener/opencli](https://github.com/jackwener/opencli) | +58 | 9758 |
| 20 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +53 | 2021 |
| 21 | [pascalorg/editor](https://github.com/pascalorg/editor) | +48 | 8747 |
| 22 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +47 | 33878 |
| 23 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +47 | 15723 |
| 24 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +47 | 35020 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +45 | 29417 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +45 | 29710 |
| 27 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +44 | 3127 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +43 | 8960 |
| 29 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +42 | 28943 |
| 30 | [revfactory/harness](https://github.com/revfactory/harness) | +39 | 1171 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2442 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2341 | 60312 |
| 3 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1724 | 55171 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1447 | 16856 |
| 5 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1287 | 12618 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1268 | 42439 |
| 7 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1155 | 62641 |
| 8 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1149 | 11935 |
| 9 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1122 | 32921 |
| 10 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +931 | 20131 |
| 11 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +878 | 45037 |
| 12 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +823 | 79656 |
| 13 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +796 | 34148 |
| 14 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +764 | 18749 |
| 15 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +737 | 28335 |
| 16 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +733 | 20646 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +695 | 67375 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +669 | 45955 |
| 19 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +647 | 30590 |
| 20 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +623 | 46923 |
| 21 | [pascalorg/editor](https://github.com/pascalorg/editor) | +600 | 8747 |
| 22 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +546 | 8295 |
| 23 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +545 | 28943 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +526 | 44922 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +502 | 14149 |
| 26 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +465 | 30678 |
| 27 | [jackwener/opencli](https://github.com/jackwener/opencli) | +456 | 9758 |
| 28 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +453 | 22614 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +448 | 36345 |
| 30 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +443 | 7652 |
| 31 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +441 | 27651 |
| 32 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +426 | 35020 |
| 33 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +420 | 3127 |
| 34 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +391 | 15723 |
| 35 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +373 | 2925 |
| 36 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +373 | 8091 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +368 | 16057 |
| 38 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +347 | 3674 |
| 39 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +332 | 2417 |
| 40 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +323 | 40043 |
| 41 | [virattt/dexter](https://github.com/virattt/dexter) | +311 | 20670 |
| 42 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +303 | 10888 |
| 43 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +296 | 45739 |
| 44 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +290 | 4166 |
| 45 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +288 | 20757 |
| 46 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +286 | 20338 |
| 47 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +285 | 33878 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +278 | 36039 |
| 49 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +270 | 37330 |
| 50 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +265 | 32522 |
| 51 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +264 | 27338 |
| 52 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +263 | 29417 |
| 53 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +256 | 4870 |
| 54 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +253 | 26308 |
| 55 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +250 | 39841 |
| 56 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +247 | 29710 |
| 57 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +244 | 8389 |
| 58 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +244 | 43417 |
| 59 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +243 | 15103 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +238 | 21691 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +232 | 18609 |
| 62 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +231 | 13543 |
| 63 | [eze-is/web-access](https://github.com/eze-is/web-access) | +223 | 3145 |
| 64 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +221 | 2716 |
| 65 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +215 | 20985 |
| 66 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +211 | 17951 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +210 | 17882 |
| 68 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +210 | 2394 |
| 69 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +209 | 20459 |
| 70 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +208 | 2720 |
| 71 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +204 | 37323 |
| 72 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +201 | 36799 |
| 73 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +200 | 34030 |
| 74 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +199 | 8366 |
| 75 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +198 | 36735 |
| 76 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +195 | 9782 |
| 77 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +195 | 22408 |
| 78 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +190 | 7371 |
| 79 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +189 | 28470 |
| 80 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +188 | 20253 |
| 81 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +184 | 25987 |
| 82 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +178 | 3458 |
| 83 | [usestrix/strix](https://github.com/usestrix/strix) | +177 | 22916 |
| 84 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +175 | 1428 |
| 85 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +173 | 3397 |
| 86 | [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | +171 | 1482 |
| 87 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +170 | 8063 |
| 88 | [mattpocock/skills](https://github.com/mattpocock/skills) | +170 | 11117 |
| 89 | [revfactory/harness](https://github.com/revfactory/harness) | +166 | 1171 |
| 90 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +166 | 12570 |
| 91 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +166 | 5010 |
| 92 | [tw93/Mole](https://github.com/tw93/Mole) | +164 | 36870 |
| 93 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +161 | 28221 |
| 94 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +159 | 9499 |
| 95 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +156 | 1953 |
| 96 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +155 | 1649 |
| 97 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 17970 |
| 98 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +148 | 1466 |
| 99 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +146 | 15011 |
| 100 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +145 | 18388 |
| 101 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +142 | 3666 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +140 | 15561 |
| 103 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +139 | 12278 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +139 | 8473 |
| 105 | [facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) | +137 | 1148 |
| 106 | [chrisryugj/korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp) | +135 | 800 |
| 107 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +134 | 1500 |
| 108 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +131 | 6742 |
| 109 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +130 | 27886 |
| 110 | [punitarani/fli](https://github.com/punitarani/fli) | +126 | 931 |
| 111 | [google-research/timesfm](https://github.com/google-research/timesfm) | +115 | 11486 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +113 | 7744 |
| 113 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +113 | 4186 |
| 114 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +113 | 31287 |
| 115 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +108 | 16898 |
| 116 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +103 | 2483 |
| 117 | [jxnxts/mcp-brasil](https://github.com/jxnxts/mcp-brasil) | +102 | 979 |
| 118 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +99 | 13901 |
| 119 | [Soul-AILab/SoulX-LiveAct](https://github.com/Soul-AILab/SoulX-LiveAct) | +98 | 1239 |
| 120 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +98 | 3155 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +23618 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12732 | 67375 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12669 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12119 | 62641 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +11011 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8479 | 44922 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8180 | 42439 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7889 | 46923 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6181 | 45739 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5432 | 74774 |
| 11 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5369 | 55171 |
| 12 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4960 | 23353 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4767 | 45037 |
| 14 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4517 | 43417 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4399 | 45955 |
| 16 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4237 | 36735 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4131 | 109881 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4026 | 28335 |
| 19 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3767 | 28221 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3452 | 34148 |
| 21 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3271 | 34030 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3223 | 20646 |
| 23 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3210 | 13901 |
| 24 | [openai/symphony](https://github.com/openai/symphony) | +3083 | 14338 |
| 25 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3079 | 16034 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3074 | 20253 |
| 27 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3053 | 20131 |
| 28 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3010 | 20985 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2893 | 14818 |
| 30 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2847 | 20459 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2835 | 36345 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2828 | 85286 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2723 | 15103 |
| 34 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2712 | 69674 |
| 35 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2638 | 17951 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2608 | 26308 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2517 | 27338 |
| 38 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2493 | 27651 |
| 39 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2490 | 29417 |
| 40 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2440 | 28943 |
| 41 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2373 | 37323 |
| 42 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2367 | 30590 |
| 43 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2348 | 16057 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2334 | 29710 |
| 45 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2316 | 14151 |
| 46 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2202 | 13543 |
| 47 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2161 | 37330 |
| 48 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2150 | 26096 |
| 49 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2116 | 8960 |
| 50 | [github/spec-kit](https://github.com/github/spec-kit) | +2095 | 71722 |
| 51 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2085 | 30678 |
| 52 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2074 | 7856 |
| 53 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2061 | 28470 |
| 54 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2061 | 10669 |
| 55 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2057 | 12380 |
| 56 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2019 | 60117 |
| 57 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2013 | 0 |
| 58 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2009 | 33878 |
| 59 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1978 | 34987 |
| 60 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1947 | 15723 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1904 | 21691 |
| 62 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1900 | 9646 |
| 63 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1860 | 25987 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1820 | 36040 |
| 65 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1811 | 8548 |
| 66 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1776 | 9264 |
| 67 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1774 | 16856 |
| 68 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1734 | 11197 |
| 69 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1709 | 122870 |
| 70 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1699 | 32522 |
| 71 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1644 | 35020 |
| 72 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1614 | 17970 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1583 | 10888 |
| 74 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1570 | 18388 |
| 75 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1567 | 18749 |
| 76 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1516 | 9758 |
| 77 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1516 | 18921 |
| 78 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1510 | 11117 |
| 79 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1502 | 16898 |
| 80 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1479 | 36879 |
| 81 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1477 | 98536 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1476 | 17882 |
| 83 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1465 | 9782 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1426 | 15561 |
| 85 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1411 | 96919 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +1407 | 36870 |
| 87 | [openai/skills](https://github.com/openai/skills) | +1369 | 15857 |
| 88 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1359 | 9499 |
| 89 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1336 | 43973 |
| 90 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1309 | 12618 |
| 91 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1306 | 26908 |
| 92 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1291 | 18609 |
| 93 | [jundot/omlx](https://github.com/jundot/omlx) | +1263 | 7744 |
| 94 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1261 | 7371 |
| 95 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1253 | 11935 |
| 96 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1233 | 87598 |
| 97 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1227 | 8747 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1225 | 8473 |
| 99 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1222 | 8063 |
| 100 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1221 | 32921 |
| 101 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1219 | 8295 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1214 | 78902 |
| 103 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1120 | 7652 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1093 | 8366 |
| 105 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +990 | 22614 |
| 106 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +975 | 79656 |
| 107 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +964 | 52700 |
| 108 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +920 | 17552 |
| 109 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +911 | 23404 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +910 | 35735 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +887 | 27886 |
| 112 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +871 | 7523 |
| 113 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +862 | 5010 |
| 114 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +848 | 37564 |
| 115 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +845 | 4472 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +829 | 39841 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +812 | 45886 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +807 | 36799 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +801 | 6742 |
| 120 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +770 | 22408 |
| 121 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +762 | 28971 |
| 122 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +750 | 6992 |
| 123 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +749 | 3457 |
| 124 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +715 | 4870 |
| 125 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +689 | 4186 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +678 | 3917 |
| 127 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +665 | 4607 |
| 128 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +661 | 47936 |
| 129 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +658 | 3629 |
| 130 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +656 | 3851 |
| 131 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +636 | 15852 |
| 132 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +623 | 14661 |
| 133 | [wshobson/agents](https://github.com/wshobson/agents) | +617 | 32656 |
| 134 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +616 | 2260 |
| 135 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +603 | 8389 |
| 136 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +598 | 2325 |
| 137 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +579 | 8917 |
| 138 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +577 | 7138 |
| 139 | [huggingface/skills](https://github.com/huggingface/skills) | +571 | 9989 |
| 140 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +569 | 3885 |
| 141 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +568 | 3155 |
| 142 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +565 | 47122 |
| 143 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +555 | 17736 |
| 144 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +552 | 2729 |
| 145 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +546 | 24179 |
| 146 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +540 | 23910 |
| 147 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +539 | 44232 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +538 | 44545 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +531 | 28060 |
| 150 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +530 | 4637 |
| 151 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +519 | 3379 |
| 152 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +516 | 1922 |
| 153 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +508 | 10840 |
| 154 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +471 | 2355 |
| 155 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +463 | 10729 |
| 156 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +462 | 14818 |
| 157 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +453 | 31287 |
| 158 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +436 | 3589 |
| 159 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +429 | 23067 |
| 160 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +421 | 3501 |
| 161 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +418 | 3127 |
| 162 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +413 | 8091 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +406 | 3647 |
| 164 | [htdt/godogen](https://github.com/htdt/godogen) | +404 | 2406 |
| 165 | [apify/agent-skills](https://github.com/apify/agent-skills) | +398 | 1796 |
| 166 | [hectorvent/floci](https://github.com/hectorvent/floci) | +397 | 2360 |
| 167 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +390 | 4625 |
| 168 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +381 | 7371 |
| 169 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +380 | 1913 |
| 170 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +377 | 2483 |
| 171 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +375 | 2324 |
| 172 | [aden-hive/hive](https://github.com/aden-hive/hive) | +371 | 9949 |
| 173 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +371 | 13402 |
| 174 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +371 | 10419 |
| 175 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +367 | 6436 |
| 176 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +360 | 20338 |
| 177 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +355 | 33712 |
| 178 | [eze-is/web-access](https://github.com/eze-is/web-access) | +350 | 3145 |
| 179 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +347 | 1822 |
| 180 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +339 | 3674 |
| 181 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +330 | 4841 |
| 182 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +329 | 1780 |
| 183 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +328 | 3703 |
| 184 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +316 | 1417 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +314 | 25072 |
| 186 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +304 | 10682 |
| 187 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +301 | 1519 |
| 188 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +297 | 1936 |
| 189 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +279 | 29780 |
| 190 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +270 | 2720 |
| 191 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +263 | 14925 |
| 192 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +262 | 1389 |
| 193 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +260 | 13730 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +258 | 4232 |
| 195 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +245 | 22126 |
| 196 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +243 | 1953 |
| 197 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +223 | 36103 |
| 198 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +220 | 5792 |
| 199 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +219 | 7308 |
| 200 | [usebruno/bruno](https://github.com/usebruno/bruno) | +218 | 41086 |
| 201 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +215 | 1167 |
| 202 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +209 | 1108 |
| 203 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +206 | 1077 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +206 | 21744 |
| 205 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +198 | 857 |
| 206 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +197 | 879 |
| 207 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +195 | 1809 |
| 208 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +191 | 0 |
| 209 | [decolua/9router](https://github.com/decolua/9router) | +182 | 1529 |
| 210 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +182 | 8979 |
| 211 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +177 | 1075 |
| 212 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +171 | 2582 |
| 213 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +163 | 956 |
| 214 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +162 | 29232 |
| 215 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +160 | 2486 |
| 216 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +159 | 1637 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +159 | 40265 |
| 218 | [linlay/zenmind](https://github.com/linlay/zenmind) | +158 | 216 |
| 219 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +158 | 25413 |
| 220 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +151 | 2336 |
| 221 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +150 | 2673 |
| 222 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 579 |
| 223 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +143 | 1715 |
| 224 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +141 | 5400 |
| 225 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +140 | 774 |
| 226 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +139 | 1032 |
| 227 | [jgraph/drawio](https://github.com/jgraph/drawio) | +138 | 4489 |
| 228 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +137 | 35473 |
| 229 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 528 |
| 230 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +134 | 1310 |
| 231 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +132 | 2522 |
| 232 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +131 | 662 |
| 233 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +129 | 961 |
| 234 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +126 | 13830 |
| 235 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +124 | 868 |
| 236 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +124 | 12426 |
| 237 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +124 | 2258 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +122 | 1655 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +122 | 26328 |
| 240 | [4ier/neo](https://github.com/4ier/neo) | +121 | 651 |
| 241 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +118 | 498 |
| 242 | [is-a-dev/register](https://github.com/is-a-dev/register) | +117 | 10036 |
| 243 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +117 | 33000 |
| 244 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +115 | 740 |
| 245 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +115 | 1824 |
| 246 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +115 | 10422 |
| 247 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +114 | 23027 |
| 248 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +110 | 1385 |
| 249 | [dashersw/gea](https://github.com/dashersw/gea) | +109 | 800 |
| 250 | [skylot/jadx](https://github.com/skylot/jadx) | +109 | 47365 |
| 251 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 456 |
| 252 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +108 | 48784 |
| 253 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +105 | 1495 |
| 254 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +104 | 1519 |
| 255 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 521 |
| 256 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 603 |
| 257 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 443 |
| 258 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 588 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +100 | 12756 |
| 260 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +98 | 11400 |
| 261 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +97 | 1408 |
| 262 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +96 | 591 |
| 263 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +96 | 9032 |
| 264 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +95 | 439 |
| 265 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +94 | 765 |
| 266 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +92 | 514 |
| 267 | [idinging/freemail](https://github.com/idinging/freemail) | +88 | 1223 |
| 268 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 471 |
| 269 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +87 | 1058 |
| 270 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +85 | 3333 |
| 271 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +84 | 1137 |
| 272 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +84 | 847 |
| 273 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +84 | 3320 |
| 274 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +83 | 3699 |
| 275 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +83 | 464 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +83 | 27100 |
| 277 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +81 | 3446 |
| 278 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +81 | 682 |
| 279 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +80 | 431 |
| 280 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +79 | 976 |
| 281 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +79 | 619 |
| 282 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +78 | 425 |
| 283 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +72 | 8366 |
| 284 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +71 | 621 |
| 285 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 286 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +71 | 37313 |
| 287 | [apache/kafka](https://github.com/apache/kafka) | +70 | 32043 |
| 288 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +69 | 12491 |
| 289 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +67 | 419 |
| 290 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +65 | 408 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +65 | 31476 |
| 292 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7146 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1569 |
| 294 | [crimera/piko](https://github.com/crimera/piko) | +64 | 2983 |
| 295 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +64 | 26641 |
| 296 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +63 | 501 |
| 297 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +63 | 346 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +63 | 1433 |
| 299 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +63 | 7726 |
| 300 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1614 |
