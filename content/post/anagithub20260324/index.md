---
title: "2026-03-24 GitHub增长趋势报告"
description: "1.deer-flow+565 2.JKVideo+483 3.MoneyPrinterV2+386 4.project-nomad+275 5.TradingAgents+225"
date: 2026-03-24T20:43:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-24 20:43:49

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
        'daily': {"categories": ["vxcontrol/pentagi", "jingyaogong/minimind", "nextlevelbuilder/ui-ux-pro-max-skill", "Donchitos/Claude-Code-Game-Studios", "kepano/obsidian-skills", "ruvnet/RuView", "666ghj/MiroFish", "hesreallyhim/awesome-claude-code", "msitarzewski/agency-agents", "gsd-build/get-shit-done", "NousResearch/hermes-agent", "jackwener/opencli", "shareAI-lab/learn-claude-code", "ruvnet/ruflo", "pascalorg/editor", "TauricResearch/TradingAgents", "Crosstalk-Solutions/project-nomad", "FujiwaraChoki/MoneyPrinterV2", "tiajinsha/JKVideo", "bytedance/deer-flow"], "data": [95, 97, 102, 103, 108, 108, 118, 120, 134, 148, 150, 151, 156, 163, 177, 225, 275, 386, 483, 565]},
        'weekly': {"categories": ["paperclipai/paperclip", "aiming-lab/AutoResearchClaw", "Lum1104/Understand-Anything", "nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/skills", "opendataloader-project/opendataloader-pdf", "mattpocock/skills", "jarrodwatts/claude-hud", "shareAI-lab/learn-claude-code", "THU-MAIC/OpenMAIC", "TauricResearch/TradingAgents", "666ghj/MiroFish", "FujiwaraChoki/MoneyPrinterV2", "gsd-build/get-shit-done", "bytedance/deer-flow", "msitarzewski/agency-agents", "Crosstalk-Solutions/project-nomad", "karpathy/autoresearch", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [843, 950, 973, 993, 1008, 1213, 1248, 1323, 1329, 1376, 1399, 1629, 1638, 1652, 1705, 1945, 2164, 2464, 3264, 3790]},
        'monthly': {"categories": ["RightNow-AI/openfang", "bytedance/deer-flow", "shareAI-lab/learn-claude-code", "moeru-ai/airi", "anomalyco/opencode", "gsd-build/get-shit-done", "D4Vinci/Scrapling", "googleworkspace/cli", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4111, 4276, 4375, 4392, 4455, 4468, 4779, 4836, 5104, 5144, 5951, 6854, 6913, 7293, 8768, 10120, 10982, 11171, 12052, 26778]}
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
| 1 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +565 | 42898 |
| 2 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +483 | 3577 |
| 3 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +386 | 24666 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +275 | 15067 |
| 5 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +225 | 30590 |
| 6 | [pascalorg/editor](https://github.com/pascalorg/editor) | +177 | 4966 |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +163 | 24906 |
| 8 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +156 | 37932 |
| 9 | [jackwener/opencli](https://github.com/jackwener/opencli) | +151 | 6102 |
| 10 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +150 | 12414 |
| 11 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +148 | 40715 |
| 12 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +134 | 61498 |
| 13 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +120 | 31717 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +118 | 41743 |
| 15 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +108 | 41148 |
| 16 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +108 | 16823 |
| 17 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +103 | 3930 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +102 | 34148 |
| 19 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +97 | 39841 |
| 20 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +95 | 13414 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +88 | 32848 |
| 22 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +86 | 20858 |
| 23 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +85 | 11307 |
| 24 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +85 | 12597 |
| 25 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +75 | 9043 |
| 26 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +72 | 5891 |
| 27 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +69 | 994 |
| 28 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +68 | 33869 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +67 | 30136 |
| 30 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +63 | 8385 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3790 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +3264 | 60312 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2464 | 54018 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2164 | 15067 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1945 | 61498 |
| 6 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1705 | 42899 |
| 7 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1652 | 40715 |
| 8 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1638 | 24666 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1629 | 41743 |
| 10 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1399 | 30590 |
| 11 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1376 | 11997 |
| 12 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1329 | 37932 |
| 13 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1323 | 12597 |
| 14 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1248 | 9800 |
| 15 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1213 | 9043 |
| 16 | [anthropics/skills](https://github.com/anthropics/skills) | +1008 | 74774 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +993 | 34148 |
| 18 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +973 | 5891 |
| 19 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +950 | 8386 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +843 | 32584 |
| 21 | [jackwener/opencli](https://github.com/jackwener/opencli) | +821 | 6102 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +724 | 13724 |
| 23 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +686 | 18739 |
| 24 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +681 | 3930 |
| 25 | [louis-e/arnis](https://github.com/louis-e/arnis) | +680 | 13140 |
| 26 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +673 | 24516 |
| 27 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +672 | 17288 |
| 28 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +661 | 13414 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +645 | 32848 |
| 30 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +637 | 6604 |
| 31 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +629 | 43533 |
| 32 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +610 | 21530 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +607 | 13224 |
| 34 | [pascalorg/editor](https://github.com/pascalorg/editor) | +604 | 4966 |
| 35 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +601 | 52700 |
| 36 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +584 | 12414 |
| 37 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +578 | 3374 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +555 | 25004 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +546 | 19403 |
| 40 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +527 | 11841 |
| 41 | [tw93/Mole](https://github.com/tw93/Mole) | +521 | 36870 |
| 42 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +520 | 41148 |
| 43 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +504 | 41615 |
| 44 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +493 | 12803 |
| 45 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +492 | 8307 |
| 46 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +490 | 20496 |
| 47 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +484 | 3577 |
| 48 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +479 | 31717 |
| 49 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +472 | 24906 |
| 50 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +467 | 3448 |
| 51 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +464 | 30678 |
| 52 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +464 | 27622 |
| 53 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +432 | 33869 |
| 54 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +431 | 33878 |
| 55 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +415 | 2090 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +409 | 19774 |
| 57 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +409 | 37330 |
| 58 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +389 | 16823 |
| 59 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +382 | 14481 |
| 60 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +375 | 5696 |
| 61 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +371 | 3227 |
| 62 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +359 | 20858 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +351 | 30136 |
| 64 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +347 | 27089 |
| 65 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +339 | 2407 |
| 66 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +338 | 1995 |
| 67 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +337 | 35978 |
| 68 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +335 | 8225 |
| 69 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +321 | 3683 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +316 | 16141 |
| 71 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +312 | 11307 |
| 72 | [hectorvent/floci](https://github.com/hectorvent/floci) | +312 | 1641 |
| 73 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +302 | 13179 |
| 74 | [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | +302 | 1880 |
| 75 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +298 | 32591 |
| 76 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +298 | 2666 |
| 77 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +280 | 2376 |
| 78 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +278 | 1076 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +278 | 22815 |
| 80 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +277 | 2226 |
| 81 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +274 | 4954 |
| 82 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +271 | 24451 |
| 83 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +262 | 27173 |
| 84 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +261 | 5937 |
| 85 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +260 | 25285 |
| 86 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +259 | 1144 |
| 87 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +259 | 31255 |
| 88 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +256 | 27114 |
| 89 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +250 | 39841 |
| 90 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +250 | 24641 |
| 91 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +244 | 7400 |
| 92 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +242 | 36494 |
| 93 | [jundot/omlx](https://github.com/jundot/omlx) | +241 | 6723 |
| 94 | [htdt/godogen](https://github.com/htdt/godogen) | +237 | 1994 |
| 95 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +236 | 19016 |
| 96 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +216 | 9236 |
| 97 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +214 | 1064 |
| 98 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +210 | 3355 |
| 99 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +209 | 18459 |
| 100 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +204 | 1710 |
| 101 | [blitzdotdev/blitz-mac](https://github.com/blitzdotdev/blitz-mac) | +203 | 914 |
| 102 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +201 | 30444 |
| 103 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +199 | 8110 |
| 104 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +198 | 908 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +198 | 6730 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +195 | 26844 |
| 107 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +195 | 3682 |
| 108 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +193 | 43973 |
| 109 | [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | +191 | 1653 |
| 110 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +189 | 7879 |
| 111 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +188 | 16764 |
| 112 | [newton-physics/newton](https://github.com/newton-physics/newton) | +176 | 3679 |
| 113 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +172 | 2597 |
| 114 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +167 | 1772 |
| 115 | [wangziqi06/724-office](https://github.com/wangziqi06/724-office) | +166 | 856 |
| 116 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +166 | 10657 |
| 117 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +154 | 16896 |
| 118 | [openai/skills](https://github.com/openai/skills) | +152 | 15246 |
| 119 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +148 | 8948 |
| 120 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +147 | 13153 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +26778 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12052 | 61498 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11171 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +10982 | 54019 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10120 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8768 | 41148 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7293 | 41743 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6913 | 32584 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6854 | 43533 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5951 | 74774 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5144 | 41615 |
| 12 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5104 | 27173 |
| 13 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4836 | 22380 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4779 | 32591 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4468 | 40715 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4455 | 109881 |
| 17 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4392 | 35441 |
| 18 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4375 | 37932 |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4276 | 42899 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4111 | 15434 |
| 21 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3881 | 19403 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3613 | 21530 |
| 23 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3463 | 13153 |
| 24 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3308 | 19016 |
| 25 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3066 | 18739 |
| 26 | [openai/symphony](https://github.com/openai/symphony) | +3038 | 13958 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3032 | 34148 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2899 | 32848 |
| 29 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2874 | 69674 |
| 30 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2822 | 35978 |
| 31 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2765 | 13724 |
| 32 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2746 | 27622 |
| 33 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2745 | 27089 |
| 34 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2744 | 10232 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2731 | 25004 |
| 36 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2723 | 25285 |
| 37 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2652 | 28655 |
| 38 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2634 | 122870 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2591 | 85286 |
| 40 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2513 | 15067 |
| 41 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2500 | 10657 |
| 42 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2499 | 13224 |
| 43 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2381 | 12414 |
| 44 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2360 | 24516 |
| 45 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2342 | 24906 |
| 46 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2262 | 37330 |
| 47 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2218 | 60117 |
| 48 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2169 | 33878 |
| 49 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2153 | 34480 |
| 50 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2138 | 12803 |
| 51 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2122 | 24666 |
| 52 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2102 | 11123 |
| 53 | [github/spec-kit](https://github.com/github/spec-kit) | +2094 | 71722 |
| 54 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2029 | 8091 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2029 | 24641 |
| 56 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2023 | 27114 |
| 57 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2007 | 7250 |
| 58 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1987 | 9236 |
| 59 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1985 | 11841 |
| 60 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1978 | 11997 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1966 | 30136 |
| 62 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1909 | 30678 |
| 63 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1855 | 30590 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1841 | 19774 |
| 65 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1840 | 10825 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1814 | 33869 |
| 67 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1740 | 7879 |
| 68 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1734 | 8948 |
| 69 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1697 | 147486 |
| 70 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1681 | 26030 |
| 71 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1675 | 6795 |
| 72 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1597 | 96919 |
| 73 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1594 | 12597 |
| 74 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1553 | 16764 |
| 75 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1537 | 16096 |
| 76 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1530 | 98536 |
| 77 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1505 | 9043 |
| 78 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1485 | 18385 |
| 79 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1483 | 17288 |
| 80 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1483 | 7871 |
| 81 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1466 | 13811 |
| 82 | [openai/skills](https://github.com/openai/skills) | +1453 | 15246 |
| 83 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1439 | 36494 |
| 84 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1437 | 16141 |
| 85 | [tw93/Mole](https://github.com/tw93/Mole) | +1394 | 36870 |
| 86 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1386 | 31717 |
| 87 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1385 | 5855 |
| 88 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1380 | 14481 |
| 89 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1368 | 9800 |
| 90 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1368 | 22824 |
| 91 | [huggingface/skills](https://github.com/huggingface/skills) | +1335 | 9873 |
| 92 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1322 | 43973 |
| 93 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1315 | 16823 |
| 94 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1303 | 5826 |
| 95 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1289 | 8225 |
| 96 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1273 | 8386 |
| 97 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1270 | 11307 |
| 98 | [openai/codex](https://github.com/openai/codex) | +1249 | 61744 |
| 99 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1240 | 14304 |
| 100 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1206 | 87598 |
| 101 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1181 | 13414 |
| 102 | [jundot/omlx](https://github.com/jundot/omlx) | +1160 | 6723 |
| 103 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1143 | 78902 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1109 | 7400 |
| 105 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1076 | 5891 |
| 106 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1075 | 6102 |
| 107 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1064 | 16896 |
| 108 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1051 | 6604 |
| 109 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +972 | 37564 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +931 | 35735 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +912 | 6730 |
| 112 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +901 | 52700 |
| 113 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +896 | 4136 |
| 114 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +886 | 26844 |
| 115 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +859 | 7253 |
| 116 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +786 | 45886 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +762 | 5937 |
| 118 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +758 | 28745 |
| 119 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +752 | 13172 |
| 120 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +750 | 36799 |
| 121 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +731 | 3325 |
| 122 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +725 | 6653 |
| 123 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +717 | 14097 |
| 124 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +696 | 10200 |
| 125 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +657 | 39841 |
| 126 | [wshobson/agents](https://github.com/wshobson/agents) | +655 | 32181 |
| 127 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +650 | 3551 |
| 128 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +649 | 47936 |
| 129 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +647 | 47122 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +646 | 15758 |
| 131 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +641 | 3683 |
| 132 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +641 | 20858 |
| 133 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +630 | 2213 |
| 134 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +620 | 4498 |
| 135 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +605 | 3355 |
| 136 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +604 | 2172 |
| 137 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +594 | 23764 |
| 138 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +587 | 3791 |
| 139 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +586 | 17061 |
| 140 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +583 | 18944 |
| 141 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +579 | 3374 |
| 142 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +568 | 2603 |
| 143 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +567 | 23506 |
| 144 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +565 | 7561 |
| 145 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +544 | 44232 |
| 146 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +543 | 10311 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +531 | 44545 |
| 148 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +513 | 3448 |
| 149 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +509 | 2445 |
| 150 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +508 | 27369 |
| 151 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +507 | 2010 |
| 152 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +506 | 8307 |
| 153 | [eooce/python-ws](https://github.com/eooce/python-ws) | +503 | 1926 |
| 154 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +501 | 6319 |
| 155 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +495 | 3227 |
| 156 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +486 | 3472 |
| 157 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +476 | 22908 |
| 158 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +470 | 2597 |
| 159 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +457 | 14578 |
| 160 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +456 | 2042 |
| 161 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +455 | 2216 |
| 162 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +447 | 8179 |
| 163 | [aden-hive/hive](https://github.com/aden-hive/hive) | +445 | 9806 |
| 164 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +433 | 6261 |
| 165 | [openclaw/skills](https://github.com/openclaw/skills) | +430 | 3376 |
| 166 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +419 | 2593 |
| 167 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +411 | 10040 |
| 168 | [apify/agent-skills](https://github.com/apify/agent-skills) | +406 | 1731 |
| 169 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +400 | 30444 |
| 170 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +396 | 3286 |
| 171 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +387 | 13179 |
| 172 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +377 | 33712 |
| 173 | [public-clis/twitter-cli](https://github.com/public-clis/twitter-cli) | +368 | 2102 |
| 174 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +354 | 3471 |
| 175 | [htdt/godogen](https://github.com/htdt/godogen) | +353 | 1994 |
| 176 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +350 | 1728 |
| 177 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +349 | 14696 |
| 178 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +343 | 1579 |
| 179 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +339 | 3682 |
| 180 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +339 | 6513 |
| 181 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +339 | 3627 |
| 182 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +335 | 1589 |
| 183 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +325 | 1778 |
| 184 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +325 | 1857 |
| 185 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +318 | 8110 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +318 | 24783 |
| 187 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +312 | 1380 |
| 188 | [hectorvent/floci](https://github.com/hectorvent/floci) | +312 | 1641 |
| 189 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +304 | 4255 |
| 190 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +292 | 29780 |
| 191 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +288 | 13559 |
| 192 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +288 | 10597 |
| 193 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +283 | 0 |
| 194 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +261 | 1231 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +256 | 3903 |
| 196 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +246 | 21859 |
| 197 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +243 | 1552 |
| 198 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +233 | 36103 |
| 199 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +232 | 5505 |
| 200 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +219 | 1025 |
| 201 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +207 | 953 |
| 202 | [usebruno/bruno](https://github.com/usebruno/bruno) | +202 | 41086 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +201 | 21524 |
| 204 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +201 | 7316 |
| 205 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +195 | 854 |
| 206 | [linlay/zenmind](https://github.com/linlay/zenmind) | +186 | 250 |
| 207 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +181 | 8925 |
| 208 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +181 | 716 |
| 209 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +180 | 1507 |
| 210 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +176 | 25386 |
| 211 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +163 | 29063 |
| 212 | [decolua/9router](https://github.com/decolua/9router) | +161 | 1212 |
| 213 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +161 | 951 |
| 214 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +161 | 2447 |
| 215 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +159 | 829 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +159 | 40265 |
| 217 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +158 | 2470 |
| 218 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +156 | 2164 |
| 219 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +155 | 986 |
| 220 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +145 | 1366 |
| 221 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +145 | 5272 |
| 222 | [es617/claude-replay](https://github.com/es617/claude-replay) | +144 | 566 |
| 223 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +142 | 1653 |
| 224 | [jgraph/drawio](https://github.com/jgraph/drawio) | +142 | 4330 |
| 225 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +139 | 2363 |
| 226 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +139 | 35473 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +135 | 1232 |
| 228 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +131 | 520 |
| 229 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +130 | 1758 |
| 230 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +129 | 613 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +128 | 1455 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +128 | 2159 |
| 233 | [4ier/neo](https://github.com/4ier/neo) | +125 | 633 |
| 234 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +124 | 13767 |
| 235 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +123 | 1250 |
| 236 | [robinebers/openusage](https://github.com/robinebers/openusage) | +122 | 1600 |
| 237 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +120 | 22889 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +119 | 26148 |
| 239 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +116 | 33000 |
| 240 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +116 | 48784 |
| 241 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10018 |
| 242 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +114 | 456 |
| 243 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +113 | 2413 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +113 | 12271 |
| 245 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +112 | 734 |
| 246 | [skylot/jadx](https://github.com/skylot/jadx) | +111 | 47365 |
| 247 | [fmhy/edit](https://github.com/fmhy/edit) | +109 | 8679 |
| 248 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +106 | 442 |
| 249 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +105 | 10225 |
| 250 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +104 | 8911 |
| 251 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 252 | [microg/GmsCore](https://github.com/microg/GmsCore) | +101 | 12680 |
| 253 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 548 |
| 254 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +99 | 536 |
| 255 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +99 | 698 |
| 256 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +99 | 11267 |
| 257 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +96 | 3255 |
| 258 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +95 | 1390 |
| 259 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +93 | 3350 |
| 260 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +92 | 1003 |
| 261 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +90 | 3572 |
| 262 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +90 | 830 |
| 263 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +90 | 428 |
| 264 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +90 | 922 |
| 265 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +89 | 517 |
| 266 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +89 | 635 |
| 267 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +89 | 820 |
| 268 | [silships/figma-cli](https://github.com/silships/figma-cli) | +89 | 473 |
| 269 | [lklynet/aurral](https://github.com/lklynet/aurral) | +89 | 889 |
| 270 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 472 |
| 271 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +88 | 913 |
| 272 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +86 | 462 |
| 273 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +85 | 479 |
| 274 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +85 | 658 |
| 275 | [idinging/freemail](https://github.com/idinging/freemail) | +84 | 1134 |
| 276 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +82 | 658 |
| 277 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +82 | 37313 |
| 278 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +79 | 27010 |
| 279 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +78 | 895 |
| 280 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +77 | 541 |
| 281 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +77 | 283 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +77 | 3110 |
| 283 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +76 | 466 |
| 284 | [f/agentlytics](https://github.com/f/agentlytics) | +76 | 353 |
| 285 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +73 | 8288 |
| 286 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +72 | 7085 |
| 287 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +72 | 387 |
| 288 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 289 | [apache/kafka](https://github.com/apache/kafka) | +69 | 32043 |
| 290 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +65 | 12438 |
| 291 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +63 | 1496 |
| 292 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +63 | 1382 |
| 293 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +63 | 7684 |
| 294 | [freeok/so-novel](https://github.com/freeok/so-novel) | +61 | 6410 |
| 295 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +60 | 294 |
| 296 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +60 | 324 |
| 297 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +60 | 1554 |
| 298 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +59 | 1043 |
| 299 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +59 | 4537 |
| 300 | [openjdk/jdk](https://github.com/openjdk/jdk) | +59 | 22734 |
