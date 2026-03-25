---
title: "2026-03-25 GitHub增长趋势报告"
description: "1.deer-flow+490 2.editor+311 3.TradingAgents+208 4.project-nomad+191 5.JKVideo+188"
date: 2026-03-25T20:41:35+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-25 20:41:35

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
        'daily': {"categories": ["Donchitos/Claude-Code-Game-Studios", "666ghj/MiroFish", "supermemoryai/supermemory", "hesreallyhim/awesome-claude-code", "gsd-build/get-shit-done", "jackwener/opencli", "msitarzewski/agency-agents", "shareAI-lab/learn-claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "agentscope-ai/agentscope", "ruvnet/ruflo", "NousResearch/hermes-agent", "FujiwaraChoki/MoneyPrinterV2", "ruvnet/RuView", "mvanhorn/last30days-skill", "tiajinsha/JKVideo", "Crosstalk-Solutions/project-nomad", "TauricResearch/TradingAgents", "pascalorg/editor", "bytedance/deer-flow"], "data": [89, 91, 94, 103, 106, 107, 111, 121, 121, 122, 125, 126, 160, 165, 169, 188, 191, 208, 311, 490]},
        'weekly': {"categories": ["jackwener/opencli", "pascalorg/editor", "nextlevelbuilder/ui-ux-pro-max-skill", "THU-MAIC/OpenMAIC", "Lum1104/Understand-Anything", "anthropics/skills", "opendataloader-project/opendataloader-pdf", "mattpocock/skills", "shareAI-lab/learn-claude-code", "jarrodwatts/claude-hud", "gsd-build/get-shit-done", "666ghj/MiroFish", "TauricResearch/TradingAgents", "msitarzewski/agency-agents", "FujiwaraChoki/MoneyPrinterV2", "bytedance/deer-flow", "Crosstalk-Solutions/project-nomad", "karpathy/autoresearch", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [864, 900, 919, 934, 988, 992, 1087, 1129, 1133, 1244, 1317, 1443, 1565, 1639, 1686, 2110, 2301, 2500, 2952, 3788]},
        'monthly': {"categories": ["RightNow-AI/openfang", "anomalyco/opencode", "gsd-build/get-shit-done", "D4Vinci/Scrapling", "moeru-ai/airi", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "googleworkspace/cli", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4126, 4354, 4354, 4395, 4410, 4437, 4712, 4857, 4920, 5017, 5846, 6590, 6977, 7371, 8921, 10112, 11252, 11314, 12149, 25990]}
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
| 1 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +490 | 45973 |
| 2 | [pascalorg/editor](https://github.com/pascalorg/editor) | +311 | 6747 |
| 3 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +208 | 30590 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +191 | 16456 |
| 5 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +188 | 4424 |
| 6 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +169 | 7263 |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +165 | 42142 |
| 8 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +160 | 25505 |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +126 | 13154 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +125 | 26006 |
| 11 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +122 | 19840 |
| 12 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +121 | 34148 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +121 | 38735 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +111 | 62321 |
| 15 | [jackwener/opencli](https://github.com/jackwener/opencli) | +107 | 6812 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +106 | 41643 |
| 17 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +103 | 32361 |
| 18 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +94 | 19150 |
| 19 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +91 | 42586 |
| 20 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +89 | 4901 |
| 21 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +84 | 13165 |
| 22 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +80 | 33373 |
| 23 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +79 | 39841 |
| 24 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +72 | 741 |
| 25 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +71 | 17214 |
| 26 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +68 | 1448 |
| 27 | [cacggghp/vk-turn-proxy](https://github.com/cacggghp/vk-turn-proxy) | +67 | 1699 |
| 28 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +65 | 30696 |
| 29 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +65 | 33054 |
| 30 | [NoDeskAI/nodeskclaw](https://github.com/NoDeskAI/nodeskclaw) | +63 | 538 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3788 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2952 | 60312 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2500 | 55835 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2301 | 16456 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2110 | 45973 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1686 | 25505 |
| 7 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1639 | 62321 |
| 8 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1565 | 30590 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1443 | 42586 |
| 10 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1317 | 41643 |
| 11 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1244 | 13165 |
| 12 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1133 | 38735 |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1129 | 10093 |
| 14 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1087 | 9357 |
| 15 | [anthropics/skills](https://github.com/anthropics/skills) | +992 | 74774 |
| 16 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +988 | 6173 |
| 17 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +934 | 12300 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +919 | 34148 |
| 19 | [pascalorg/editor](https://github.com/pascalorg/editor) | +900 | 6747 |
| 20 | [jackwener/opencli](https://github.com/jackwener/opencli) | +864 | 6812 |
| 21 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +760 | 33054 |
| 22 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +755 | 4901 |
| 23 | [louis-e/arnis](https://github.com/louis-e/arnis) | +685 | 13262 |
| 24 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +678 | 13585 |
| 25 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +645 | 4424 |
| 26 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +640 | 13154 |
| 27 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +624 | 42142 |
| 28 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +620 | 13889 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +615 | 33373 |
| 30 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +613 | 19039 |
| 31 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +608 | 43944 |
| 32 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +608 | 24777 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +605 | 21962 |
| 34 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +559 | 26006 |
| 35 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +552 | 32361 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +544 | 13524 |
| 37 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +514 | 6855 |
| 38 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +513 | 8688 |
| 39 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +513 | 17470 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +496 | 25437 |
| 41 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +495 | 3547 |
| 42 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +488 | 41899 |
| 43 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +480 | 20795 |
| 44 | [tw93/Mole](https://github.com/tw93/Mole) | +460 | 36870 |
| 45 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +453 | 13319 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +445 | 27916 |
| 47 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +424 | 30678 |
| 48 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +424 | 8431 |
| 49 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +423 | 2135 |
| 50 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +421 | 34179 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +420 | 33878 |
| 52 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +410 | 21266 |
| 53 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +404 | 3564 |
| 54 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +395 | 19646 |
| 55 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +392 | 17056 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +392 | 20113 |
| 57 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +374 | 14638 |
| 58 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +373 | 37330 |
| 59 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +358 | 30696 |
| 60 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +354 | 2115 |
| 61 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +345 | 11919 |
| 62 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +344 | 3757 |
| 63 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +338 | 2627 |
| 64 | [hectorvent/floci](https://github.com/hectorvent/floci) | +336 | 1746 |
| 65 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +321 | 36246 |
| 66 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +320 | 5814 |
| 67 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +317 | 39841 |
| 68 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +315 | 11548 |
| 69 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +311 | 27362 |
| 70 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +307 | 13238 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +300 | 16446 |
| 72 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +296 | 24702 |
| 73 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +294 | 8438 |
| 74 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +293 | 19150 |
| 75 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +279 | 1085 |
| 76 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +273 | 32795 |
| 77 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +270 | 1229 |
| 78 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +265 | 27394 |
| 79 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +261 | 5035 |
| 80 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +258 | 2278 |
| 81 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +251 | 22988 |
| 82 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +248 | 7511 |
| 83 | [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | +248 | 1911 |
| 84 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +246 | 27372 |
| 85 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +244 | 6010 |
| 86 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +240 | 7264 |
| 87 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +238 | 19840 |
| 88 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +238 | 24852 |
| 89 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +231 | 31501 |
| 90 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +225 | 25460 |
| 91 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +222 | 1135 |
| 92 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +220 | 11548 |
| 93 | [jundot/omlx](https://github.com/jundot/omlx) | +217 | 6846 |
| 94 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +212 | 36601 |
| 95 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +210 | 1781 |
| 96 | [htdt/godogen](https://github.com/htdt/godogen) | +210 | 2081 |
| 97 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +209 | 19144 |
| 98 | [blitzdotdev/blitz-mac](https://github.com/blitzdotdev/blitz-mac) | +207 | 929 |
| 99 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +205 | 30532 |
| 100 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +204 | 17214 |
| 101 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +198 | 908 |
| 102 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +197 | 8238 |
| 103 | [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | +193 | 1742 |
| 104 | [eze-is/web-access](https://github.com/eze-is/web-access) | +188 | 1418 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +185 | 6924 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +181 | 27025 |
| 107 | [wangziqi06/724-office](https://github.com/wangziqi06/724-office) | +178 | 879 |
| 108 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +175 | 8018 |
| 109 | [newton-physics/newton](https://github.com/newton-physics/newton) | +174 | 3705 |
| 110 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +171 | 43973 |
| 111 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +170 | 3442 |
| 112 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +152 | 3880 |
| 113 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +151 | 36799 |
| 114 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +146 | 10750 |
| 115 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +144 | 2652 |
| 116 | [Nunchi-trade/auto-researchtrading](https://github.com/Nunchi-trade/auto-researchtrading) | +143 | 635 |
| 117 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +139 | 17013 |
| 118 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +138 | 1902 |
| 119 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +136 | 2908 |
| 120 | [openai/skills](https://github.com/openai/skills) | +134 | 15323 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +25990 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12149 | 62321 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11314 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11252 | 55835 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10112 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8921 | 42142 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7371 | 42586 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6977 | 33054 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6590 | 43944 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5846 | 74774 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5017 | 41899 |
| 12 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4920 | 27372 |
| 13 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4857 | 22522 |
| 14 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4712 | 45973 |
| 15 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4437 | 38735 |
| 16 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4410 | 35577 |
| 17 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4395 | 32795 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4354 | 41643 |
| 19 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4354 | 109881 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4126 | 15536 |
| 21 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3674 | 19646 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3622 | 21962 |
| 23 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3488 | 13274 |
| 24 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3173 | 19144 |
| 25 | [openai/symphony](https://github.com/openai/symphony) | +3049 | 14028 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3048 | 19039 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3043 | 34148 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2879 | 33373 |
| 29 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2819 | 69674 |
| 30 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2792 | 13889 |
| 31 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2771 | 10404 |
| 32 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2712 | 36246 |
| 33 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2682 | 16456 |
| 34 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2677 | 25437 |
| 35 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2649 | 27362 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2596 | 85286 |
| 37 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2588 | 27916 |
| 38 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2549 | 25460 |
| 39 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2544 | 13524 |
| 40 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2496 | 13154 |
| 41 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2481 | 28760 |
| 42 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2451 | 26006 |
| 43 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2409 | 24777 |
| 44 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2355 | 10750 |
| 45 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2323 | 122870 |
| 46 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2249 | 25505 |
| 47 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2223 | 37330 |
| 48 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2190 | 60117 |
| 49 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2170 | 13319 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2124 | 33878 |
| 51 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2110 | 34556 |
| 52 | [github/spec-kit](https://github.com/github/spec-kit) | +2088 | 71722 |
| 53 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2035 | 8158 |
| 54 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2031 | 12300 |
| 55 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2027 | 7366 |
| 56 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2021 | 27394 |
| 57 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2015 | 30590 |
| 58 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1995 | 11919 |
| 59 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1986 | 9292 |
| 60 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1984 | 24852 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1983 | 30696 |
| 62 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1878 | 30678 |
| 63 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1856 | 20113 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1804 | 34179 |
| 65 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1800 | 10892 |
| 66 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1750 | 8018 |
| 67 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1744 | 11271 |
| 68 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1740 | 8993 |
| 69 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1676 | 13165 |
| 70 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1617 | 147486 |
| 71 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1576 | 17214 |
| 72 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1576 | 96919 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1558 | 9357 |
| 74 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1553 | 26122 |
| 75 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1527 | 16210 |
| 76 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1502 | 6848 |
| 77 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1497 | 17470 |
| 78 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1493 | 18485 |
| 79 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1493 | 98536 |
| 80 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1480 | 7942 |
| 81 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1453 | 36601 |
| 82 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1450 | 32361 |
| 83 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1441 | 13952 |
| 84 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1437 | 16446 |
| 85 | [openai/skills](https://github.com/openai/skills) | +1417 | 15323 |
| 86 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1399 | 10093 |
| 87 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1389 | 5874 |
| 88 | [tw93/Mole](https://github.com/tw93/Mole) | +1385 | 36870 |
| 89 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1372 | 14638 |
| 90 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1331 | 8688 |
| 91 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1327 | 43973 |
| 92 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1317 | 17056 |
| 93 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1307 | 8438 |
| 94 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1294 | 22933 |
| 95 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1262 | 11548 |
| 96 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1202 | 87598 |
| 97 | [jundot/omlx](https://github.com/jundot/omlx) | +1171 | 6846 |
| 98 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1167 | 6812 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1164 | 78902 |
| 100 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1153 | 13585 |
| 101 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1124 | 7511 |
| 102 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1108 | 6173 |
| 103 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1093 | 6855 |
| 104 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1034 | 17013 |
| 105 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1022 | 14343 |
| 106 | [pascalorg/editor](https://github.com/pascalorg/editor) | +949 | 6747 |
| 107 | [huggingface/skills](https://github.com/huggingface/skills) | +948 | 9901 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +931 | 6924 |
| 109 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +926 | 52700 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +925 | 35735 |
| 111 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +920 | 37564 |
| 112 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +908 | 4205 |
| 113 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +878 | 27025 |
| 114 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +856 | 7296 |
| 115 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +780 | 45886 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +769 | 6010 |
| 117 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +759 | 28784 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +742 | 36799 |
| 119 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +734 | 3350 |
| 120 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +728 | 6733 |
| 121 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +712 | 39841 |
| 122 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +711 | 13178 |
| 123 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +701 | 19840 |
| 124 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +677 | 14178 |
| 125 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +675 | 21266 |
| 126 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +664 | 10340 |
| 127 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +650 | 3573 |
| 128 | [wshobson/agents](https://github.com/wshobson/agents) | +648 | 32251 |
| 129 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +646 | 47936 |
| 130 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +645 | 4424 |
| 131 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +644 | 3717 |
| 132 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +643 | 15770 |
| 133 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +633 | 2226 |
| 134 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +622 | 47122 |
| 135 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +614 | 3442 |
| 136 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +606 | 2186 |
| 137 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +605 | 3547 |
| 138 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +598 | 3880 |
| 139 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +580 | 23848 |
| 140 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +569 | 4520 |
| 141 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +567 | 17195 |
| 142 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +567 | 2612 |
| 143 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +552 | 23567 |
| 144 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +543 | 7264 |
| 145 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +534 | 44545 |
| 146 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +529 | 44232 |
| 147 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +528 | 7601 |
| 148 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +525 | 3564 |
| 149 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +520 | 8431 |
| 150 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +517 | 10380 |
| 151 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +512 | 2460 |
| 152 | [eooce/python-ws](https://github.com/eooce/python-ws) | +508 | 1941 |
| 153 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +507 | 1858 |
| 154 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +501 | 27469 |
| 155 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +499 | 3257 |
| 156 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +480 | 2652 |
| 157 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +472 | 3484 |
| 158 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +463 | 2257 |
| 159 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +460 | 14626 |
| 160 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +459 | 2055 |
| 161 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +457 | 22924 |
| 162 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +455 | 6418 |
| 163 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +429 | 8211 |
| 164 | [openclaw/skills](https://github.com/openclaw/skills) | +427 | 3409 |
| 165 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +424 | 6303 |
| 166 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +414 | 2612 |
| 167 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +407 | 10083 |
| 168 | [apify/agent-skills](https://github.com/apify/agent-skills) | +407 | 1739 |
| 169 | [aden-hive/hive](https://github.com/aden-hive/hive) | +403 | 9820 |
| 170 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +402 | 3348 |
| 171 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +401 | 30532 |
| 172 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +385 | 13238 |
| 173 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +371 | 33712 |
| 174 | [htdt/godogen](https://github.com/htdt/godogen) | +366 | 2081 |
| 175 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +351 | 3524 |
| 176 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +349 | 6667 |
| 177 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +348 | 1610 |
| 178 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +338 | 3719 |
| 179 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +337 | 3639 |
| 180 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +336 | 1615 |
| 181 | [hectorvent/floci](https://github.com/hectorvent/floci) | +336 | 1746 |
| 182 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +335 | 1926 |
| 183 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +331 | 8238 |
| 184 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +324 | 1805 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +316 | 24821 |
| 186 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +313 | 1386 |
| 187 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +312 | 14734 |
| 188 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +310 | 4368 |
| 189 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +286 | 29780 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +285 | 10658 |
| 191 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +282 | 13604 |
| 192 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +282 | 1748 |
| 193 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +274 | 1334 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +255 | 3939 |
| 195 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +253 | 1598 |
| 196 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +242 | 21893 |
| 197 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +240 | 0 |
| 198 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +238 | 5552 |
| 199 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +225 | 36103 |
| 200 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +211 | 1043 |
| 201 | [usebruno/bruno](https://github.com/usebruno/bruno) | +202 | 41086 |
| 202 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +199 | 955 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +198 | 7347 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +196 | 21552 |
| 205 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +195 | 859 |
| 206 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +187 | 752 |
| 207 | [linlay/zenmind](https://github.com/linlay/zenmind) | +185 | 280 |
| 208 | [eze-is/web-access](https://github.com/eze-is/web-access) | +177 | 1418 |
| 209 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +175 | 8935 |
| 210 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +168 | 25388 |
| 211 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +164 | 1528 |
| 212 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +162 | 879 |
| 213 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +161 | 960 |
| 214 | [decolua/9router](https://github.com/decolua/9router) | +160 | 1251 |
| 215 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +159 | 2476 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +157 | 40265 |
| 217 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +155 | 29075 |
| 218 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +153 | 2192 |
| 219 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +150 | 986 |
| 220 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +145 | 2466 |
| 221 | [es617/claude-replay](https://github.com/es617/claude-replay) | +145 | 571 |
| 222 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +144 | 5303 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +142 | 35473 |
| 224 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +140 | 1661 |
| 225 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +139 | 2368 |
| 226 | [jgraph/drawio](https://github.com/jgraph/drawio) | +137 | 4361 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +135 | 1251 |
| 228 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +131 | 522 |
| 229 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +130 | 628 |
| 230 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +127 | 1767 |
| 231 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +127 | 2175 |
| 232 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +125 | 2492 |
| 233 | [4ier/neo](https://github.com/4ier/neo) | +125 | 636 |
| 234 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +125 | 1455 |
| 235 | [robinebers/openusage](https://github.com/robinebers/openusage) | +124 | 1617 |
| 236 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +123 | 1281 |
| 237 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +122 | 1373 |
| 238 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +122 | 13777 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +118 | 26176 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +116 | 12286 |
| 241 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10028 |
| 242 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +115 | 461 |
| 243 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +114 | 22910 |
| 244 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +113 | 33000 |
| 245 | [skylot/jadx](https://github.com/skylot/jadx) | +112 | 47365 |
| 246 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +111 | 48784 |
| 247 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +110 | 756 |
| 248 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 445 |
| 249 | [fmhy/edit](https://github.com/fmhy/edit) | +105 | 8690 |
| 250 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +104 | 686 |
| 251 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +104 | 10250 |
| 252 | [microg/GmsCore](https://github.com/microg/GmsCore) | +103 | 12697 |
| 253 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +102 | 551 |
| 254 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 547 |
| 256 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +100 | 8930 |
| 257 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +99 | 435 |
| 258 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +98 | 785 |
| 259 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +98 | 1411 |
| 260 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 11291 |
| 261 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +94 | 3266 |
| 262 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +92 | 1010 |
| 263 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +92 | 435 |
| 264 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +90 | 834 |
| 265 | [silships/figma-cli](https://github.com/silships/figma-cli) | +90 | 478 |
| 266 | [lklynet/aurral](https://github.com/lklynet/aurral) | +89 | 891 |
| 267 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 471 |
| 268 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +88 | 640 |
| 269 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +88 | 927 |
| 270 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +86 | 469 |
| 271 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +86 | 499 |
| 272 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +86 | 834 |
| 273 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +85 | 3362 |
| 274 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +84 | 674 |
| 275 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +84 | 3581 |
| 276 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +83 | 703 |
| 277 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +83 | 660 |
| 278 | [idinging/freemail](https://github.com/idinging/freemail) | +81 | 1142 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +78 | 27021 |
| 280 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +77 | 323 |
| 281 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +76 | 37313 |
| 282 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +75 | 45263 |
| 283 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +74 | 902 |
| 284 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +73 | 548 |
| 285 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +73 | 468 |
| 286 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +72 | 394 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +71 | 8305 |
| 288 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +69 | 3125 |
| 289 | [apache/kafka](https://github.com/apache/kafka) | +68 | 32043 |
| 290 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +67 | 7098 |
| 291 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +66 | 325 |
| 292 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +66 | 12439 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +65 | 1510 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +64 | 1390 |
| 295 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +62 | 7689 |
| 296 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +60 | 329 |
| 297 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +60 | 1571 |
| 298 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +60 | 1047 |
| 299 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +60 | 31476 |
| 300 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +59 | 11559 |
