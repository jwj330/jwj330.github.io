---
title: "2026-03-26 GitHub增长趋势报告"
description: "1.deer-flow+293 2.last30days-skill+263 3.Claude-Code-Game-Studios+126 4.project-nomad+126 5.skills+123"
date: 2026-03-26T20:38:34+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-26 20:38:34

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
        'daily': {"categories": ["vectorize-io/hindsight", "datawhalechina/hello-agents", "farion1231/cc-switch", "FujiwaraChoki/MoneyPrinterV2", "msitarzewski/agency-agents", "rtk-ai/rtk", "shareAI-lab/learn-claude-code", "TauricResearch/TradingAgents", "ruvnet/RuView", "666ghj/MiroFish", "jackwener/opencli", "pascalorg/editor", "nextlevelbuilder/ui-ux-pro-max-skill", "ruvnet/ruflo", "gsd-build/get-shit-done", "MiniMax-AI/skills", "Crosstalk-Solutions/project-nomad", "Donchitos/Claude-Code-Game-Studios", "mvanhorn/last30days-skill", "bytedance/deer-flow"], "data": [63, 64, 66, 75, 81, 83, 87, 94, 96, 96, 100, 104, 107, 111, 121, 123, 126, 126, 263, 293]},
        'weekly': {"categories": ["jackwener/opencli", "nextlevelbuilder/ui-ux-pro-max-skill", "Donchitos/Claude-Code-Game-Studios", "MiniMax-AI/skills", "opendataloader-project/opendataloader-pdf", "anthropics/skills", "pascalorg/editor", "Lum1104/Understand-Anything", "shareAI-lab/learn-claude-code", "jarrodwatts/claude-hud", "gsd-build/get-shit-done", "666ghj/MiroFish", "msitarzewski/agency-agents", "TauricResearch/TradingAgents", "FujiwaraChoki/MoneyPrinterV2", "bytedance/deer-flow", "Crosstalk-Solutions/project-nomad", "karpathy/autoresearch", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [852, 854, 874, 924, 930, 948, 977, 986, 1002, 1003, 1215, 1327, 1467, 1601, 1737, 2329, 2381, 2408, 2809, 3716]},
        'monthly': {"categories": ["D4Vinci/Scrapling", "RightNow-AI/openfang", "anomalyco/opencode", "gsd-build/get-shit-done", "shareAI-lab/learn-claude-code", "moeru-ai/airi", "hesamsheikh/awesome-openclaw-usecases", "bytedance/deer-flow", "VoltAgent/awesome-openclaw-skills", "googleworkspace/cli", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3756, 4031, 4200, 4305, 4377, 4426, 4581, 4816, 4849, 4868, 5623, 6359, 7018, 7458, 8995, 10120, 11361, 11394, 12222, 25045]}
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
| 1 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +293 | 48142 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +263 | 9886 |
| 3 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +126 | 6002 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +126 | 17335 |
| 5 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +123 | 6005 |
| 6 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +121 | 42532 |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +111 | 26885 |
| 8 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +107 | 34148 |
| 9 | [pascalorg/editor](https://github.com/pascalorg/editor) | +104 | 7262 |
| 10 | [jackwener/opencli](https://github.com/jackwener/opencli) | +100 | 7533 |
| 11 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +96 | 43490 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +96 | 43036 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +94 | 30590 |
| 14 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +87 | 39686 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +83 | 13926 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +81 | 63216 |
| 17 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +75 | 26134 |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +66 | 33908 |
| 19 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +64 | 31171 |
| 20 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +63 | 6401 |
| 21 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +63 | 6033 |
| 22 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +63 | 12435 |
| 23 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +62 | 19530 |
| 24 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +61 | 36799 |
| 25 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +56 | 1518 |
| 26 | [usestrix/strix](https://github.com/usestrix/strix) | +56 | 22018 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +53 | 25938 |
| 28 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +53 | 13638 |
| 29 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +50 | 21653 |
| 30 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +50 | 34580 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3716 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2809 | 60312 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2408 | 57199 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2381 | 17335 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2329 | 48142 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1737 | 26134 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1601 | 30590 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1467 | 63216 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1327 | 43491 |
| 10 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1215 | 42532 |
| 11 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1003 | 13722 |
| 12 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1002 | 39686 |
| 13 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +986 | 6384 |
| 14 | [pascalorg/editor](https://github.com/pascalorg/editor) | +977 | 7262 |
| 15 | [anthropics/skills](https://github.com/anthropics/skills) | +948 | 74774 |
| 16 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +930 | 9608 |
| 17 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +924 | 6005 |
| 18 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +874 | 6002 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +854 | 34148 |
| 20 | [jackwener/opencli](https://github.com/jackwener/opencli) | +852 | 7533 |
| 21 | [mattpocock/skills](https://github.com/mattpocock/skills) | +822 | 10313 |
| 22 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +688 | 12483 |
| 23 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +683 | 13703 |
| 24 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +678 | 4673 |
| 25 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +659 | 43036 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +654 | 33526 |
| 27 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +639 | 13638 |
| 28 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +636 | 26885 |
| 29 | [louis-e/arnis](https://github.com/louis-e/arnis) | +589 | 13362 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +585 | 22304 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +572 | 33908 |
| 32 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +567 | 44300 |
| 33 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +564 | 19302 |
| 34 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +558 | 32751 |
| 35 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +539 | 14067 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +534 | 24967 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +502 | 13787 |
| 38 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +493 | 9887 |
| 39 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +458 | 13926 |
| 40 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +454 | 42186 |
| 41 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +452 | 20908 |
| 42 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +448 | 21653 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +423 | 25938 |
| 44 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +423 | 17637 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +419 | 28223 |
| 46 | [tw93/Mole](https://github.com/tw93/Mole) | +419 | 36870 |
| 47 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +408 | 3716 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +404 | 34580 |
| 49 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +398 | 2197 |
| 50 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +394 | 30678 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +391 | 33878 |
| 52 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +388 | 17281 |
| 53 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +388 | 8907 |
| 54 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +375 | 2383 |
| 55 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +370 | 20421 |
| 56 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +370 | 14852 |
| 57 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +365 | 31171 |
| 58 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +356 | 7008 |
| 59 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +348 | 39841 |
| 60 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +347 | 19530 |
| 61 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +338 | 19863 |
| 62 | [hectorvent/floci](https://github.com/hectorvent/floci) | +336 | 1828 |
| 63 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +334 | 37330 |
| 64 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +332 | 3649 |
| 65 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +324 | 11770 |
| 66 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +315 | 8560 |
| 67 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +310 | 13276 |
| 68 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +300 | 27613 |
| 69 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +299 | 36452 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +292 | 16756 |
| 71 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +290 | 5935 |
| 72 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +290 | 24926 |
| 73 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +281 | 1103 |
| 74 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +278 | 20295 |
| 75 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +277 | 27615 |
| 76 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +275 | 11977 |
| 77 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +274 | 1258 |
| 78 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +268 | 6401 |
| 79 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +266 | 3869 |
| 80 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +260 | 8665 |
| 81 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +259 | 33046 |
| 82 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +259 | 5090 |
| 83 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +254 | 12435 |
| 84 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +248 | 7688 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +239 | 23182 |
| 86 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +238 | 27534 |
| 87 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +227 | 2814 |
| 88 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +225 | 31733 |
| 89 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +225 | 25046 |
| 90 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +211 | 1829 |
| 91 | [eze-is/web-access](https://github.com/eze-is/web-access) | +210 | 1689 |
| 92 | [htdt/godogen](https://github.com/htdt/godogen) | +205 | 2147 |
| 93 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +204 | 25608 |
| 94 | [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | +204 | 1816 |
| 95 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +200 | 30622 |
| 96 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +199 | 1175 |
| 97 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +198 | 8364 |
| 98 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +198 | 908 |
| 99 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +194 | 17391 |
| 100 | [jundot/omlx](https://github.com/jundot/omlx) | +194 | 7001 |
| 101 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +192 | 36799 |
| 102 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +186 | 27193 |
| 103 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +181 | 1518 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +177 | 7143 |
| 105 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +176 | 36720 |
| 106 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +174 | 8146 |
| 107 | [wangziqi06/724-office](https://github.com/wangziqi06/724-office) | +169 | 888 |
| 108 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +168 | 1038 |
| 109 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +164 | 43973 |
| 110 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +163 | 1710 |
| 111 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +147 | 3544 |
| 112 | [Nunchi-trade/auto-researchtrading](https://github.com/Nunchi-trade/auto-researchtrading) | +143 | 643 |
| 113 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +142 | 3992 |
| 114 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +140 | 10882 |
| 115 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +138 | 3036 |
| 116 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +134 | 928 |
| 117 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +133 | 3908 |
| 118 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +132 | 2036 |
| 119 | [openai/skills](https://github.com/openai/skills) | +131 | 15427 |
| 120 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +131 | 2735 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +25045 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12222 | 63216 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11394 | 57201 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11361 | 51199 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10120 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8995 | 43036 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7458 | 43491 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7018 | 33526 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6359 | 44300 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5623 | 74774 |
| 11 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4868 | 22646 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4849 | 42186 |
| 13 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4816 | 48142 |
| 14 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4581 | 27534 |
| 15 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4426 | 35701 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4377 | 39686 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4305 | 42532 |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4200 | 109881 |
| 19 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4031 | 15657 |
| 20 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3756 | 33046 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3624 | 22304 |
| 22 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3493 | 13361 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3409 | 19863 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3054 | 34148 |
| 25 | [openai/symphony](https://github.com/openai/symphony) | +3053 | 14071 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3027 | 19302 |
| 27 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2974 | 19273 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2845 | 33908 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2805 | 14067 |
| 30 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2803 | 17335 |
| 31 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2786 | 10473 |
| 32 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2764 | 69674 |
| 33 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2602 | 25938 |
| 34 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2584 | 36452 |
| 35 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2574 | 85286 |
| 36 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2569 | 27613 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2568 | 13787 |
| 38 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2492 | 26885 |
| 39 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2464 | 28223 |
| 40 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2450 | 13638 |
| 41 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2427 | 24967 |
| 42 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2420 | 25608 |
| 43 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2336 | 28868 |
| 44 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2312 | 26134 |
| 45 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2235 | 13926 |
| 46 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2174 | 10882 |
| 47 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2166 | 37330 |
| 48 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2146 | 60117 |
| 49 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2063 | 122870 |
| 50 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2061 | 30590 |
| 51 | [github/spec-kit](https://github.com/github/spec-kit) | +2058 | 71722 |
| 52 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2052 | 34628 |
| 53 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2051 | 33878 |
| 54 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2050 | 12483 |
| 55 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2042 | 8220 |
| 56 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2035 | 7446 |
| 57 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2016 | 27615 |
| 58 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2002 | 11977 |
| 59 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1973 | 9340 |
| 60 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1948 | 25046 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1864 | 31171 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1843 | 20421 |
| 63 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1837 | 30678 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1785 | 34580 |
| 65 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1769 | 10948 |
| 66 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1767 | 8146 |
| 67 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1747 | 9056 |
| 68 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1697 | 13722 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1574 | 17391 |
| 70 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1568 | 147486 |
| 71 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1560 | 96919 |
| 72 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1533 | 9608 |
| 73 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1530 | 16326 |
| 74 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1502 | 17637 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1493 | 18573 |
| 76 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1485 | 98536 |
| 77 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1477 | 8004 |
| 78 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1462 | 36720 |
| 79 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1450 | 26247 |
| 80 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1426 | 32751 |
| 81 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1418 | 10313 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1411 | 16756 |
| 83 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1391 | 5938 |
| 84 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1387 | 6918 |
| 85 | [openai/skills](https://github.com/openai/skills) | +1385 | 15427 |
| 86 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1378 | 14852 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +1361 | 36870 |
| 88 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1355 | 8907 |
| 89 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1324 | 43973 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1305 | 8665 |
| 91 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1260 | 17281 |
| 92 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1250 | 7533 |
| 93 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1244 | 11770 |
| 94 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1231 | 87598 |
| 95 | [jundot/omlx](https://github.com/jundot/omlx) | +1185 | 7001 |
| 96 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1171 | 23013 |
| 97 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1159 | 78902 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1134 | 7688 |
| 99 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1130 | 6384 |
| 100 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1128 | 13703 |
| 101 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1105 | 7008 |
| 102 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1026 | 7262 |
| 103 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +992 | 17120 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +947 | 7143 |
| 105 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +933 | 6005 |
| 106 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +928 | 52700 |
| 107 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +920 | 35735 |
| 108 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +912 | 4248 |
| 109 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +877 | 37564 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +862 | 27193 |
| 111 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +859 | 7338 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +777 | 6401 |
| 113 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +775 | 9887 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +773 | 45886 |
| 115 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +772 | 36799 |
| 116 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +768 | 14379 |
| 117 | [huggingface/skills](https://github.com/huggingface/skills) | +765 | 9923 |
| 118 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +761 | 28824 |
| 119 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +743 | 39841 |
| 120 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +739 | 3374 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +728 | 20295 |
| 122 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +727 | 6781 |
| 123 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +700 | 21653 |
| 124 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +678 | 4673 |
| 125 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +651 | 3584 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +645 | 3740 |
| 127 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +639 | 15780 |
| 128 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +636 | 2243 |
| 129 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +635 | 14255 |
| 130 | [wshobson/agents](https://github.com/wshobson/agents) | +633 | 32317 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +631 | 47936 |
| 132 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +626 | 3716 |
| 133 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +620 | 3544 |
| 134 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +611 | 13201 |
| 135 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +607 | 2195 |
| 136 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +597 | 3992 |
| 137 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +589 | 47122 |
| 138 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +566 | 23915 |
| 139 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +564 | 10479 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +554 | 17349 |
| 141 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +547 | 4544 |
| 142 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +540 | 23622 |
| 143 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +535 | 3649 |
| 144 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +534 | 8560 |
| 145 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +534 | 2620 |
| 146 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +529 | 44545 |
| 147 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +520 | 44232 |
| 148 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +513 | 2478 |
| 149 | [eooce/python-ws](https://github.com/eooce/python-ws) | +509 | 1960 |
| 150 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +507 | 1850 |
| 151 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +502 | 3294 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +497 | 27583 |
| 153 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +493 | 10462 |
| 154 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +491 | 2735 |
| 155 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +490 | 7635 |
| 156 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +467 | 2282 |
| 157 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +458 | 2076 |
| 158 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +456 | 14657 |
| 159 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +455 | 3499 |
| 160 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +443 | 22943 |
| 161 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +421 | 6527 |
| 162 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +416 | 2628 |
| 163 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +415 | 6342 |
| 164 | [openclaw/skills](https://github.com/openclaw/skills) | +412 | 3454 |
| 165 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +406 | 3386 |
| 166 | [apify/agent-skills](https://github.com/apify/agent-skills) | +405 | 1751 |
| 167 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +399 | 10147 |
| 168 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +396 | 30622 |
| 169 | [aden-hive/hive](https://github.com/aden-hive/hive) | +379 | 9835 |
| 170 | [htdt/godogen](https://github.com/htdt/godogen) | +372 | 2147 |
| 171 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +369 | 13276 |
| 172 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +362 | 33712 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +348 | 6781 |
| 174 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +347 | 3573 |
| 175 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +344 | 1656 |
| 176 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +342 | 8364 |
| 177 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +341 | 1986 |
| 178 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +340 | 1637 |
| 179 | [hectorvent/floci](https://github.com/hectorvent/floci) | +337 | 1828 |
| 180 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +335 | 3749 |
| 181 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +328 | 1832 |
| 182 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +328 | 3654 |
| 183 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +313 | 1389 |
| 184 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +312 | 4471 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +311 | 24862 |
| 186 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +294 | 14773 |
| 187 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +285 | 1383 |
| 188 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +285 | 10719 |
| 189 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +279 | 29780 |
| 190 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +265 | 13627 |
| 191 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +257 | 1644 |
| 192 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +244 | 3973 |
| 193 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +242 | 5595 |
| 194 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +242 | 1765 |
| 195 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +231 | 1175 |
| 196 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +230 | 21923 |
| 197 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +229 | 0 |
| 198 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +219 | 36103 |
| 199 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +211 | 1062 |
| 200 | [eze-is/web-access](https://github.com/eze-is/web-access) | +210 | 1689 |
| 201 | [usebruno/bruno](https://github.com/usebruno/bruno) | +208 | 41086 |
| 202 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +195 | 863 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +194 | 7376 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +192 | 21578 |
| 205 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +188 | 776 |
| 206 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +186 | 954 |
| 207 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +178 | 8941 |
| 208 | [linlay/zenmind](https://github.com/linlay/zenmind) | +173 | 315 |
| 209 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +166 | 935 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +163 | 1278 |
| 211 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +163 | 989 |
| 212 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +163 | 25394 |
| 213 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +159 | 2477 |
| 214 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +158 | 1553 |
| 215 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +155 | 29101 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +149 | 40265 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +148 | 2221 |
| 218 | [es617/claude-replay](https://github.com/es617/claude-replay) | +146 | 573 |
| 219 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +144 | 985 |
| 220 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +143 | 1165 |
| 221 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +143 | 5319 |
| 222 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +139 | 2370 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +139 | 35473 |
| 224 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +138 | 2482 |
| 225 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +137 | 2555 |
| 226 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +135 | 1669 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +135 | 1260 |
| 228 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +132 | 522 |
| 229 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +132 | 642 |
| 230 | [jgraph/drawio](https://github.com/jgraph/drawio) | +131 | 4387 |
| 231 | [4ier/neo](https://github.com/4ier/neo) | +125 | 637 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +125 | 2191 |
| 233 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +122 | 1774 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +121 | 1625 |
| 235 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +120 | 1459 |
| 236 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +119 | 13783 |
| 237 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +119 | 1298 |
| 238 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +118 | 1375 |
| 239 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +116 | 463 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +115 | 12302 |
| 241 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +115 | 22924 |
| 242 | [is-a-dev/register](https://github.com/is-a-dev/register) | +114 | 10031 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +112 | 26206 |
| 244 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +111 | 48784 |
| 245 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +110 | 704 |
| 246 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +109 | 33000 |
| 247 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 448 |
| 248 | [skylot/jadx](https://github.com/skylot/jadx) | +108 | 47365 |
| 249 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +107 | 765 |
| 250 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +104 | 576 |
| 251 | [fmhy/edit](https://github.com/fmhy/edit) | +102 | 8701 |
| 252 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 253 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +102 | 10280 |
| 254 | [microg/GmsCore](https://github.com/microg/GmsCore) | +102 | 12709 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 572 |
| 256 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +99 | 436 |
| 257 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +97 | 1432 |
| 258 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11316 |
| 259 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +94 | 8954 |
| 260 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +91 | 3277 |
| 261 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +89 | 842 |
| 262 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +88 | 517 |
| 263 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 264 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +88 | 929 |
| 265 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +87 | 484 |
| 266 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +87 | 1020 |
| 267 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +86 | 647 |
| 268 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +86 | 442 |
| 269 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +85 | 696 |
| 270 | [idinging/freemail](https://github.com/idinging/freemail) | +83 | 1159 |
| 271 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +83 | 3602 |
| 272 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +82 | 369 |
| 273 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3382 |
| 274 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +80 | 666 |
| 275 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +79 | 848 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +77 | 27034 |
| 277 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +76 | 392 |
| 278 | [f/agentlytics](https://github.com/f/agentlytics) | +76 | 357 |
| 279 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +74 | 37313 |
| 280 | [dashersw/gea](https://github.com/dashersw/gea) | +73 | 638 |
| 281 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +73 | 399 |
| 282 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +72 | 45263 |
| 283 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +70 | 561 |
| 284 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +68 | 907 |
| 285 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +67 | 343 |
| 286 | [Kylsky/chatgpt-team-helper](https://github.com/Kylsky/chatgpt-team-helper) | +67 | 1017 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +67 | 8312 |
| 288 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +67 | 3141 |
| 289 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +67 | 12448 |
| 290 | [apache/kafka](https://github.com/apache/kafka) | +66 | 32043 |
| 291 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7102 |
| 292 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +63 | 470 |
| 293 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +62 | 11585 |
| 294 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +62 | 1524 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +62 | 1399 |
| 296 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +61 | 7694 |
| 297 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +60 | 330 |
| 298 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +60 | 1580 |
| 299 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +59 | 1047 |
| 300 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +58 | 4554 |
