---
title: "2026-03-23 GitHub增长趋势报告"
description: "1.project-nomad+835 2.deer-flow+639 3.MoneyPrinterV2+597 4.TradingAgents+471 5.Understand-Anything+436"
date: 2026-03-23T20:40:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-23 20:40:00

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
        'daily': {"categories": ["hectorvent/floci", "ruvnet/ruflo", "NousResearch/hermes-agent", "jackwener/opencli", "nextlevelbuilder/ui-ux-pro-max-skill", "shanraisshan/claude-code-best-practice", "jarrodwatts/claude-hud", "shareAI-lab/learn-claude-code", "ruvnet/RuView", "gsd-build/get-shit-done", "msitarzewski/agency-agents", "Donchitos/Claude-Code-Game-Studios", "vxcontrol/pentagi", "666ghj/MiroFish", "pascalorg/editor", "Lum1104/Understand-Anything", "TauricResearch/TradingAgents", "FujiwaraChoki/MoneyPrinterV2", "bytedance/deer-flow", "Crosstalk-Solutions/project-nomad"], "data": [132, 133, 144, 146, 153, 156, 175, 192, 199, 237, 259, 278, 286, 295, 435, 436, 471, 597, 639, 835]},
        'weekly': {"categories": ["Lum1104/Understand-Anything", "anthropics/skills", "nextlevelbuilder/ui-ux-pro-max-skill", "paperclipai/paperclip", "aiming-lab/AutoResearchClaw", "opendataloader-project/opendataloader-pdf", "bytedance/deer-flow", "TauricResearch/TradingAgents", "mattpocock/skills", "FujiwaraChoki/MoneyPrinterV2", "jarrodwatts/claude-hud", "shareAI-lab/learn-claude-code", "gsd-build/get-shit-done", "THU-MAIC/OpenMAIC", "666ghj/MiroFish", "Crosstalk-Solutions/project-nomad", "msitarzewski/agency-agents", "karpathy/autoresearch", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [951, 980, 1003, 1022, 1086, 1139, 1202, 1218, 1231, 1269, 1324, 1361, 1573, 1693, 1988, 2013, 2191, 2498, 3339, 3824]},
        'monthly': {"categories": ["abhigyanpatwari/GitNexus", "RightNow-AI/openfang", "shareAI-lab/learn-claude-code", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "googleworkspace/cli", "D4Vinci/Scrapling", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "paperclipai/paperclip", "666ghj/MiroFish", "koala73/worldmonitor", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3959, 4103, 4260, 4373, 4505, 4520, 4816, 5145, 5212, 5275, 6029, 6853, 7192, 7225, 8670, 10031, 10743, 11076, 11920, 27420]}
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
| 1 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +835 | 13090 |
| 2 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +639 | 38886 |
| 3 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +597 | 22566 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +471 | 30590 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +436 | 5424 |
| 6 | [pascalorg/editor](https://github.com/pascalorg/editor) | +435 | 3388 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +295 | 40767 |
| 8 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +286 | 12903 |
| 9 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +278 | 3224 |
| 10 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +259 | 60582 |
| 11 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +237 | 39754 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +199 | 40137 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +192 | 36968 |
| 14 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +175 | 11906 |
| 15 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +156 | 21070 |
| 16 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +153 | 34148 |
| 17 | [jackwener/opencli](https://github.com/jackwener/opencli) | +146 | 5177 |
| 18 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +144 | 11376 |
| 19 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +133 | 23744 |
| 20 | [hectorvent/floci](https://github.com/hectorvent/floci) | +132 | 1325 |
| 21 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +127 | 11639 |
| 22 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +124 | 17979 |
| 23 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +118 | 20277 |
| 24 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +118 | 18381 |
| 25 | [louis-e/arnis](https://github.com/louis-e/arnis) | +117 | 13037 |
| 26 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +116 | 3255 |
| 27 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +112 | 43137 |
| 28 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +109 | 32116 |
| 29 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +105 | 10723 |
| 30 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +104 | 12724 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3824 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +3339 | 60312 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2498 | 51913 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2191 | 60582 |
| 5 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2013 | 13090 |
| 6 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1988 | 40767 |
| 7 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1693 | 11639 |
| 8 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1573 | 39754 |
| 9 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1361 | 36968 |
| 10 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1324 | 11906 |
| 11 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1269 | 22566 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1231 | 9321 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1218 | 30590 |
| 14 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1202 | 38886 |
| 15 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1139 | 8593 |
| 16 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1086 | 7956 |
| 17 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1022 | 32116 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1003 | 34148 |
| 19 | [anthropics/skills](https://github.com/anthropics/skills) | +980 | 74774 |
| 20 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +951 | 5424 |
| 21 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +858 | 6385 |
| 22 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +850 | 18382 |
| 23 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +819 | 17050 |
| 24 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +794 | 13561 |
| 25 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +786 | 11720 |
| 26 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +781 | 24125 |
| 27 | [jackwener/opencli](https://github.com/jackwener/opencli) | +737 | 5177 |
| 28 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +726 | 60117 |
| 29 | [louis-e/arnis](https://github.com/louis-e/arnis) | +686 | 13037 |
| 30 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +683 | 43137 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +638 | 12724 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +635 | 32286 |
| 33 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +635 | 19104 |
| 34 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +610 | 21070 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +608 | 24656 |
| 36 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +594 | 12903 |
| 37 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +594 | 30678 |
| 38 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +583 | 3224 |
| 39 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +579 | 52700 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +574 | 12361 |
| 41 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +540 | 3129 |
| 42 | [tw93/Mole](https://github.com/tw93/Mole) | +540 | 36870 |
| 43 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +536 | 41260 |
| 44 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +502 | 11376 |
| 45 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +489 | 8170 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +487 | 27322 |
| 47 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +484 | 40137 |
| 48 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +465 | 20087 |
| 49 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +456 | 3255 |
| 50 | [pascalorg/editor](https://github.com/pascalorg/editor) | +455 | 3388 |
| 51 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +435 | 37330 |
| 52 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +435 | 33457 |
| 53 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +431 | 33878 |
| 54 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +425 | 19455 |
| 55 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +425 | 5518 |
| 56 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +414 | 2595 |
| 57 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +407 | 1968 |
| 58 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +401 | 30797 |
| 59 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +385 | 14293 |
| 60 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +368 | 3184 |
| 61 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +346 | 23744 |
| 62 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +338 | 3647 |
| 63 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +337 | 26830 |
| 64 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +336 | 29765 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +335 | 7926 |
| 66 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +333 | 35718 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +319 | 15863 |
| 68 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +318 | 2243 |
| 69 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +314 | 16252 |
| 70 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +307 | 32152 |
| 71 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +300 | 4862 |
| 72 | [htdt/godogen](https://github.com/htdt/godogen) | +297 | 1894 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +295 | 22622 |
| 74 | [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | +294 | 1824 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +289 | 18280 |
| 76 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +287 | 13086 |
| 77 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +287 | 2157 |
| 78 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +284 | 20277 |
| 79 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +284 | 5871 |
| 80 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +283 | 25053 |
| 81 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +278 | 24424 |
| 82 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +277 | 6596 |
| 83 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +276 | 36430 |
| 84 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +275 | 1054 |
| 85 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +274 | 2313 |
| 86 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +273 | 31044 |
| 87 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +271 | 26947 |
| 88 | [hectorvent/floci](https://github.com/hectorvent/floci) | +269 | 1325 |
| 89 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +261 | 26747 |
| 90 | [jundot/omlx](https://github.com/jundot/omlx) | +260 | 6596 |
| 91 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +259 | 1937 |
| 92 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +256 | 10723 |
| 93 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +252 | 24274 |
| 94 | [yazinsai/OpenOats](https://github.com/yazinsai/OpenOats) | +248 | 1648 |
| 95 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +246 | 16527 |
| 96 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +243 | 980 |
| 97 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +243 | 7207 |
| 98 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +227 | 3278 |
| 99 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +225 | 28521 |
| 100 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +225 | 3615 |
| 101 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +218 | 9126 |
| 102 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +208 | 1028 |
| 103 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +207 | 7933 |
| 104 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +199 | 43973 |
| 105 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +198 | 908 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +198 | 6543 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +196 | 26678 |
| 108 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +194 | 7741 |
| 109 | [blitzdotdev/blitz-mac](https://github.com/blitzdotdev/blitz-mac) | +194 | 856 |
| 110 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +182 | 30310 |
| 111 | [newton-physics/newton](https://github.com/newton-physics/newton) | +181 | 3654 |
| 112 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +180 | 1637 |
| 113 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +174 | 10515 |
| 114 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +172 | 8896 |
| 115 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +170 | 2513 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +166 | 39841 |
| 117 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +166 | 13063 |
| 118 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +154 | 16769 |
| 119 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +152 | 3193 |
| 120 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +151 | 1752 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +27420 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +11920 | 60582 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11076 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +10743 | 51913 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10031 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8670 | 40137 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7225 | 43137 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7192 | 40767 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6853 | 32116 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +6029 | 74774 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5275 | 41260 |
| 12 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5212 | 26947 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5145 | 32152 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4816 | 22225 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4520 | 109881 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4505 | 39754 |
| 17 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4373 | 35315 |
| 18 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4260 | 36968 |
| 19 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4103 | 15346 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3959 | 19104 |
| 21 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +3750 | 38886 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3703 | 21070 |
| 23 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +3553 | 122870 |
| 24 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3452 | 13063 |
| 25 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3432 | 18748 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3059 | 18382 |
| 27 | [openai/symphony](https://github.com/openai/symphony) | +3030 | 13880 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3014 | 34148 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2943 | 35718 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2891 | 32286 |
| 31 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2890 | 69674 |
| 32 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2886 | 25053 |
| 33 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2862 | 27322 |
| 34 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2845 | 28521 |
| 35 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2784 | 26830 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2752 | 24656 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2734 | 10150 |
| 38 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2731 | 13561 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2596 | 85286 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2478 | 10515 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2456 | 12724 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2329 | 37330 |
| 43 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2323 | 24125 |
| 44 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2290 | 60117 |
| 45 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2260 | 13090 |
| 46 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2238 | 11376 |
| 47 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2223 | 33878 |
| 48 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2200 | 23744 |
| 49 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2195 | 10978 |
| 50 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2186 | 34377 |
| 51 | [github/spec-kit](https://github.com/github/spec-kit) | +2123 | 71722 |
| 52 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2090 | 12361 |
| 53 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2033 | 24424 |
| 54 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2032 | 26747 |
| 55 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2016 | 8018 |
| 56 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1986 | 7097 |
| 57 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1985 | 9126 |
| 58 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1966 | 11721 |
| 59 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1944 | 29765 |
| 60 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1929 | 11639 |
| 61 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1919 | 30678 |
| 62 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1861 | 10749 |
| 63 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1844 | 25903 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1840 | 19455 |
| 65 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1833 | 147486 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1803 | 33457 |
| 67 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1751 | 22566 |
| 68 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1729 | 7741 |
| 69 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1729 | 8896 |
| 70 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1683 | 30590 |
| 71 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1666 | 6738 |
| 72 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1636 | 96919 |
| 73 | [huggingface/skills](https://github.com/huggingface/skills) | +1628 | 9801 |
| 74 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1590 | 16527 |
| 75 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1577 | 98536 |
| 76 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1548 | 15967 |
| 77 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1529 | 11906 |
| 78 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1517 | 22711 |
| 79 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1482 | 8097 |
| 80 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1481 | 13650 |
| 81 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1479 | 7809 |
| 82 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1475 | 18280 |
| 83 | [openai/skills](https://github.com/openai/skills) | +1474 | 15124 |
| 84 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1450 | 17050 |
| 85 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1447 | 149018 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1439 | 15863 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +1437 | 36870 |
| 88 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1436 | 36430 |
| 89 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1431 | 8593 |
| 90 | [tobi/qmd](https://github.com/tobi/qmd) | +1401 | 16652 |
| 91 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1387 | 14239 |
| 92 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1381 | 5831 |
| 93 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1372 | 14293 |
| 94 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1328 | 9321 |
| 95 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1319 | 43973 |
| 96 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1296 | 30797 |
| 97 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1293 | 5742 |
| 98 | [openai/codex](https://github.com/openai/codex) | +1260 | 61744 |
| 99 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1245 | 7926 |
| 100 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1213 | 7956 |
| 101 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1202 | 87598 |
| 102 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1187 | 12903 |
| 103 | [jundot/omlx](https://github.com/jundot/omlx) | +1140 | 6596 |
| 104 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1104 | 16769 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1087 | 7207 |
| 106 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1028 | 6386 |
| 107 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1019 | 37564 |
| 108 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1017 | 78902 |
| 109 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1014 | 5424 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +930 | 35735 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +894 | 6543 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +893 | 26678 |
| 113 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +887 | 52700 |
| 114 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +886 | 4067 |
| 115 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +868 | 13145 |
| 116 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +867 | 7194 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +790 | 45886 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +755 | 36799 |
| 119 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +754 | 28693 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +749 | 5871 |
| 121 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +741 | 10104 |
| 122 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +734 | 13983 |
| 123 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +730 | 3286 |
| 124 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +726 | 6596 |
| 125 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +677 | 47122 |
| 126 | [wshobson/agents](https://github.com/wshobson/agents) | +657 | 32086 |
| 127 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +656 | 47936 |
| 128 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +656 | 4465 |
| 129 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +648 | 3522 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +648 | 15744 |
| 131 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +638 | 3647 |
| 132 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +627 | 2195 |
| 133 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +608 | 7534 |
| 134 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +602 | 2153 |
| 135 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +597 | 3278 |
| 136 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +597 | 23682 |
| 137 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +593 | 16939 |
| 138 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +579 | 3691 |
| 139 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +576 | 20277 |
| 140 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +571 | 23426 |
| 141 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +570 | 2587 |
| 142 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +565 | 39841 |
| 143 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +560 | 44232 |
| 144 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +560 | 18829 |
| 145 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +550 | 6303 |
| 146 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +543 | 10231 |
| 147 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +541 | 3129 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +530 | 44545 |
| 149 | [docling-project/docling](https://github.com/docling-project/docling) | +513 | 54041 |
| 150 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +507 | 27259 |
| 151 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +506 | 2422 |
| 152 | [eooce/python-ws](https://github.com/eooce/python-ws) | +503 | 1914 |
| 153 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +502 | 2017 |
| 154 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +501 | 8170 |
| 155 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +501 | 22895 |
| 156 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +495 | 3184 |
| 157 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +492 | 3445 |
| 158 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +485 | 3255 |
| 159 | [aden-hive/hive](https://github.com/aden-hive/hive) | +465 | 9786 |
| 160 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +459 | 2513 |
| 161 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +459 | 14533 |
| 162 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +456 | 2034 |
| 163 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +450 | 8134 |
| 164 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +446 | 6224 |
| 165 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +444 | 2159 |
| 166 | [openclaw/skills](https://github.com/openclaw/skills) | +431 | 3309 |
| 167 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +416 | 2576 |
| 168 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +412 | 9990 |
| 169 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +407 | 13086 |
| 170 | [apify/agent-skills](https://github.com/apify/agent-skills) | +405 | 1724 |
| 171 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +403 | 30310 |
| 172 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +393 | 14666 |
| 173 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +389 | 3193 |
| 174 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +389 | 33712 |
| 175 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +378 | 1714 |
| 176 | [public-clis/twitter-cli](https://github.com/public-clis/twitter-cli) | +368 | 2094 |
| 177 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +365 | 3412 |
| 178 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +343 | 3609 |
| 179 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +343 | 1553 |
| 180 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +341 | 6419 |
| 181 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +333 | 3615 |
| 182 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +330 | 1545 |
| 183 | [htdt/godogen](https://github.com/htdt/godogen) | +327 | 1894 |
| 184 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +320 | 1752 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +317 | 24737 |
| 186 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +315 | 1781 |
| 187 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +311 | 1368 |
| 188 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +307 | 4195 |
| 189 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +295 | 10550 |
| 190 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +293 | 13541 |
| 191 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +292 | 29780 |
| 192 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +290 | 0 |
| 193 | [hectorvent/floci](https://github.com/hectorvent/floci) | +268 | 1325 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +267 | 3860 |
| 195 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +260 | 1182 |
| 196 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +250 | 21831 |
| 197 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +238 | 36103 |
| 198 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +234 | 1006 |
| 199 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +228 | 5456 |
| 200 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +228 | 1484 |
| 201 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +214 | 960 |
| 202 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +211 | 1354 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +205 | 21496 |
| 204 | [usebruno/bruno](https://github.com/usebruno/bruno) | +200 | 41086 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +200 | 7281 |
| 206 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +197 | 1466 |
| 207 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +194 | 845 |
| 208 | [linlay/zenmind](https://github.com/linlay/zenmind) | +184 | 311 |
| 209 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +180 | 8906 |
| 210 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +177 | 25382 |
| 211 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +177 | 636 |
| 212 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +176 | 2430 |
| 213 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +169 | 29040 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +167 | 40265 |
| 215 | [decolua/9router](https://github.com/decolua/9router) | +165 | 1181 |
| 216 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +161 | 10517 |
| 217 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +160 | 945 |
| 218 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +160 | 986 |
| 219 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +158 | 2467 |
| 220 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +151 | 779 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +151 | 2118 |
| 222 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +150 | 1637 |
| 223 | [jgraph/drawio](https://github.com/jgraph/drawio) | +146 | 4309 |
| 224 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +145 | 5253 |
| 225 | [es617/claude-replay](https://github.com/es617/claude-replay) | +144 | 562 |
| 226 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +137 | 1451 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +137 | 1216 |
| 228 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +137 | 2352 |
| 229 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +137 | 35473 |
| 230 | [robinebers/openusage](https://github.com/robinebers/openusage) | +135 | 1591 |
| 231 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +131 | 1734 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +131 | 2149 |
| 233 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +130 | 516 |
| 234 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +129 | 2653 |
| 235 | [4ier/neo](https://github.com/4ier/neo) | +125 | 629 |
| 236 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +125 | 26106 |
| 237 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +125 | 22868 |
| 238 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +124 | 595 |
| 239 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +122 | 13758 |
| 240 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +120 | 1218 |
| 241 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +119 | 690 |
| 242 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +119 | 719 |
| 243 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +117 | 33000 |
| 244 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +117 | 48784 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +116 | 12256 |
| 246 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10012 |
| 247 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +115 | 450 |
| 248 | [fmhy/edit](https://github.com/fmhy/edit) | +111 | 8655 |
| 249 | [skylot/jadx](https://github.com/skylot/jadx) | +108 | 47365 |
| 250 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +107 | 10200 |
| 251 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +106 | 439 |
| 252 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +104 | 8879 |
| 253 | [microg/GmsCore](https://github.com/microg/GmsCore) | +104 | 12667 |
| 254 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +103 | 2342 |
| 255 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +103 | 714 |
| 256 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 257 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +102 | 11246 |
| 258 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +101 | 3331 |
| 259 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 548 |
| 260 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +100 | 520 |
| 261 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +99 | 805 |
| 262 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +98 | 3565 |
| 263 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +95 | 996 |
| 264 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +94 | 920 |
| 265 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +94 | 1376 |
| 266 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +93 | 3228 |
| 267 | [lklynet/aurral](https://github.com/lklynet/aurral) | +93 | 886 |
| 268 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +93 | 911 |
| 269 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +89 | 828 |
| 270 | [silships/figma-cli](https://github.com/silships/figma-cli) | +89 | 466 |
| 271 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 471 |
| 272 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +87 | 420 |
| 273 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +87 | 646 |
| 274 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +86 | 623 |
| 275 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +86 | 37313 |
| 276 | [idinging/freemail](https://github.com/idinging/freemail) | +85 | 1122 |
| 277 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +85 | 450 |
| 278 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +81 | 534 |
| 279 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +78 | 406 |
| 280 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +78 | 629 |
| 281 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +78 | 457 |
| 282 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +78 | 26997 |
| 283 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +77 | 463 |
| 284 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +77 | 888 |
| 285 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +77 | 1044 |
| 286 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +77 | 3098 |
| 287 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +75 | 281 |
| 288 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +75 | 8279 |
| 289 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +73 | 7076 |
| 290 | [apache/kafka](https://github.com/apache/kafka) | +72 | 32043 |
| 291 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 292 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +66 | 1373 |
| 293 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +65 | 7681 |
| 294 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +64 | 920 |
| 295 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +64 | 6123 |
| 296 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +63 | 1032 |
| 297 | [freeok/so-novel](https://github.com/freeok/so-novel) | +62 | 6401 |
| 298 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +62 | 12428 |
| 299 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +61 | 1475 |
| 300 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +60 | 320 |
