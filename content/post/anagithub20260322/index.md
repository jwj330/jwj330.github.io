---
title: "2026-03-22 GitHub增长趋势报告"
description: "1.everything-claude-code+887 2.autoresearch+620 3.project-nomad+618 4.agency-agents+454 5.deer-flow+423"
date: 2026-03-22T20:31:10+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-22 20:31:10

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
        'daily': {"categories": ["koala73/worldmonitor", "hectorvent/floci", "louis-e/arnis", "lightpanda-io/browser", "shareAI-lab/learn-claude-code", "opendataloader-project/opendataloader-pdf", "nextlevelbuilder/ui-ux-pro-max-skill", "jackwener/opencli", "Donchitos/Claude-Code-Game-Studios", "jarrodwatts/claude-hud", "gsd-build/get-shit-done", "vxcontrol/pentagi", "666ghj/MiroFish", "TauricResearch/TradingAgents", "FujiwaraChoki/MoneyPrinterV2", "bytedance/deer-flow", "msitarzewski/agency-agents", "Crosstalk-Solutions/project-nomad", "karpathy/autoresearch", "affaan-m/everything-claude-code"], "data": [153, 161, 167, 168, 170, 176, 177, 200, 224, 241, 244, 251, 338, 341, 417, 423, 454, 618, 620, 887]},
        'weekly': {"categories": ["langchain-ai/deepagents", "abhigyanpatwari/GitNexus", "anthropics/skills", "nextlevelbuilder/ui-ux-pro-max-skill", "opendataloader-project/opendataloader-pdf", "lightpanda-io/browser", "aiming-lab/AutoResearchClaw", "jarrodwatts/claude-hud", "mattpocock/skills", "volcengine/OpenViking", "Crosstalk-Solutions/project-nomad", "paperclipai/paperclip", "gsd-build/get-shit-done", "shareAI-lab/learn-claude-code", "THU-MAIC/OpenMAIC", "666ghj/MiroFish", "msitarzewski/agency-agents", "karpathy/autoresearch", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [978, 992, 996, 1044, 1056, 1104, 1151, 1174, 1179, 1207, 1339, 1415, 1476, 1504, 1815, 2493, 2633, 2640, 3544, 3569]},
        'monthly': {"categories": ["abhigyanpatwari/GitNexus", "shareAI-lab/learn-claude-code", "x1xhlol/system-prompts-and-models-of-ai-tools", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "googleworkspace/cli", "D4Vinci/Scrapling", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "paperclipai/paperclip", "666ghj/MiroFish", "koala73/worldmonitor", "ruvnet/RuView", "obra/superpowers", "karpathy/autoresearch", "affaan-m/everything-claude-code", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4106, 4112, 4330, 4349, 4566, 4587, 4776, 5310, 5402, 5408, 6051, 6752, 6917, 7759, 8488, 10030, 10361, 10403, 11694, 27975]}
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
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +887 | 51199 |
| 2 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +620 | 49751 |
| 3 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +618 | 9191 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +454 | 59363 |
| 5 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +423 | 34972 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +417 | 19363 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +341 | 30590 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +338 | 39520 |
| 9 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +251 | 11798 |
| 10 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +244 | 38763 |
| 11 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +241 | 11093 |
| 12 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +224 | 2055 |
| 13 | [jackwener/opencli](https://github.com/jackwener/opencli) | +200 | 4311 |
| 14 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +177 | 34148 |
| 15 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +176 | 8265 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +170 | 35871 |
| 17 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +168 | 23692 |
| 18 | [louis-e/arnis](https://github.com/louis-e/arnis) | +167 | 12643 |
| 19 | [hectorvent/floci](https://github.com/hectorvent/floci) | +161 | 912 |
| 20 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +153 | 42603 |
| 21 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +150 | 30194 |
| 22 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +148 | 1011 |
| 23 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +145 | 1773 |
| 24 | [blitzdotdev/blitz-mac](https://github.com/blitzdotdev/blitz-mac) | +143 | 743 |
| 25 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +142 | 11140 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +141 | 17881 |
| 27 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +139 | 31548 |
| 28 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +134 | 13269 |
| 29 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +133 | 12267 |
| 30 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +127 | 823 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3569 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +3544 | 60312 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2640 | 49751 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2633 | 59363 |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2493 | 39520 |
| 6 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1815 | 11140 |
| 7 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1504 | 35871 |
| 8 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1476 | 38763 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1415 | 31548 |
| 10 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1339 | 9192 |
| 11 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1207 | 17881 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1179 | 8841 |
| 13 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1174 | 11093 |
| 14 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1151 | 7632 |
| 15 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1104 | 23692 |
| 16 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1056 | 8265 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1044 | 34148 |
| 18 | [anthropics/skills](https://github.com/anthropics/skills) | +996 | 74774 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +992 | 18785 |
| 20 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +978 | 16676 |
| 21 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +866 | 6196 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +861 | 13269 |
| 23 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +804 | 30590 |
| 24 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +788 | 11500 |
| 25 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +753 | 24403 |
| 26 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +744 | 20436 |
| 27 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +733 | 42603 |
| 28 | [jackwener/opencli](https://github.com/jackwener/opencli) | +728 | 4311 |
| 29 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +717 | 30678 |
| 30 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +695 | 19363 |
| 31 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +680 | 34972 |
| 32 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +672 | 12267 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +636 | 31769 |
| 34 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +594 | 11988 |
| 35 | [louis-e/arnis](https://github.com/louis-e/arnis) | +585 | 12643 |
| 36 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +575 | 40858 |
| 37 | [tw93/Mole](https://github.com/tw93/Mole) | +572 | 36870 |
| 38 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +526 | 26937 |
| 39 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +496 | 14086 |
| 40 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +496 | 19106 |
| 41 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +486 | 10168 |
| 42 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +471 | 2741 |
| 43 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +463 | 3617 |
| 44 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +460 | 37330 |
| 45 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +451 | 8031 |
| 46 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +444 | 33088 |
| 47 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +430 | 16430 |
| 48 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +429 | 2494 |
| 49 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +426 | 33878 |
| 50 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +420 | 5283 |
| 51 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +411 | 19737 |
| 52 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +407 | 39212 |
| 53 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +381 | 35467 |
| 54 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +380 | 18153 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +377 | 7657 |
| 56 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +376 | 11798 |
| 57 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +372 | 2741 |
| 58 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +365 | 1773 |
| 59 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +359 | 3138 |
| 60 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +354 | 30194 |
| 61 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +353 | 31848 |
| 62 | [jundot/omlx](https://github.com/jundot/omlx) | +347 | 6462 |
| 63 | [novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket) | +340 | 2137 |
| 64 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +337 | 26576 |
| 65 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +334 | 6527 |
| 66 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +332 | 24879 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +332 | 15500 |
| 68 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +331 | 15746 |
| 69 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +328 | 24194 |
| 70 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +324 | 2897 |
| 71 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +323 | 2055 |
| 72 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +321 | 29371 |
| 73 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +318 | 26535 |
| 74 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +315 | 26769 |
| 75 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +314 | 22430 |
| 76 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +305 | 3175 |
| 77 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +302 | 2049 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +297 | 30798 |
| 79 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +295 | 2382 |
| 80 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +290 | 5738 |
| 81 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +290 | 3145 |
| 82 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +290 | 35165 |
| 83 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +288 | 2052 |
| 84 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +286 | 36334 |
| 85 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +281 | 4661 |
| 86 | [zerobootdev/zeroboot](https://github.com/zerobootdev/zeroboot) | +280 | 1742 |
| 87 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +277 | 1810 |
| 88 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +277 | 43973 |
| 89 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +277 | 12960 |
| 90 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +267 | 2259 |
| 91 | [Narcooo/inkos](https://github.com/Narcooo/inkos) | +267 | 2076 |
| 92 | [htdt/godogen](https://github.com/htdt/godogen) | +261 | 1718 |
| 93 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +260 | 22058 |
| 94 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +257 | 22362 |
| 95 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +254 | 12929 |
| 96 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +252 | 1011 |
| 97 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +251 | 28394 |
| 98 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +230 | 1482 |
| 99 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +228 | 24050 |
| 100 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +227 | 3436 |
| 101 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +224 | 8823 |
| 102 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +223 | 6959 |
| 103 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +222 | 9031 |
| 104 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +215 | 823 |
| 105 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +212 | 7611 |
| 106 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +212 | 28650 |
| 107 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +202 | 3980 |
| 108 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +198 | 907 |
| 109 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +194 | 10170 |
| 110 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +193 | 2074 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +192 | 19713 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +188 | 26494 |
| 113 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +188 | 10330 |
| 114 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +186 | 969 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +185 | 6352 |
| 116 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +184 | 22585 |
| 117 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +179 | 2410 |
| 118 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +179 | 1661 |
| 119 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +176 | 14488 |
| 120 | [newton-physics/newton](https://github.com/newton-physics/newton) | +175 | 3621 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +27975 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +11694 | 59363 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +10403 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +10361 | 49751 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10030 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8488 | 39212 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7759 | 42603 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6917 | 39520 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6752 | 31548 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +6051 | 74774 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5408 | 40858 |
| 12 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5402 | 26769 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5310 | 31848 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4776 | 22058 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4587 | 109881 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4566 | 38763 |
| 17 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4349 | 35165 |
| 18 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4330 | 122870 |
| 19 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4112 | 35871 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4106 | 18785 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4088 | 15243 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3852 | 20436 |
| 23 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3747 | 18495 |
| 24 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3433 | 12960 |
| 25 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +3402 | 24879 |
| 26 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +3163 | 34972 |
| 27 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3101 | 35467 |
| 28 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +3087 | 28394 |
| 29 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3016 | 17881 |
| 30 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3012 | 69674 |
| 31 | [openai/symphony](https://github.com/openai/symphony) | +3008 | 13769 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2967 | 34148 |
| 33 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2881 | 26937 |
| 34 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2869 | 26576 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2852 | 31769 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2765 | 24403 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2707 | 10048 |
| 38 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2647 | 13269 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2588 | 85286 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2450 | 10330 |
| 41 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2364 | 37330 |
| 42 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2359 | 12267 |
| 43 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2257 | 33878 |
| 44 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2249 | 60117 |
| 45 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2249 | 34238 |
| 46 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2242 | 23692 |
| 47 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2208 | 10810 |
| 48 | [huggingface/skills](https://github.com/huggingface/skills) | +2108 | 9673 |
| 49 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2101 | 10168 |
| 50 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2089 | 22362 |
| 51 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2064 | 26535 |
| 52 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2061 | 11988 |
| 53 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +2047 | 25801 |
| 54 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2017 | 24194 |
| 55 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2002 | 7941 |
| 56 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1968 | 7006 |
| 57 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1965 | 9031 |
| 58 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1955 | 30678 |
| 59 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1929 | 10680 |
| 60 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1918 | 11500 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1910 | 29371 |
| 62 | [github/spec-kit](https://github.com/github/spec-kit) | +1907 | 71722 |
| 63 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1887 | 147486 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1839 | 19106 |
| 65 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1819 | 11140 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1802 | 33088 |
| 67 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1717 | 8823 |
| 68 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1695 | 7611 |
| 69 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1672 | 96919 |
| 70 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1656 | 22585 |
| 71 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1654 | 16430 |
| 72 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1632 | 6628 |
| 73 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1565 | 98536 |
| 74 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1542 | 15844 |
| 75 | [tw93/Mole](https://github.com/tw93/Mole) | +1541 | 36870 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1521 | 13506 |
| 77 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1500 | 149018 |
| 78 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1493 | 8068 |
| 79 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1478 | 7728 |
| 80 | [openai/skills](https://github.com/openai/skills) | +1471 | 14962 |
| 81 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1461 | 9192 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1457 | 15500 |
| 83 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1446 | 18153 |
| 84 | [tobi/qmd](https://github.com/tobi/qmd) | +1445 | 16502 |
| 85 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1426 | 14165 |
| 86 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1417 | 36334 |
| 87 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1377 | 11093 |
| 88 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1373 | 5803 |
| 89 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1366 | 16676 |
| 90 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1363 | 14086 |
| 91 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1348 | 8265 |
| 92 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1314 | 43973 |
| 93 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1308 | 8841 |
| 94 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1272 | 5640 |
| 95 | [openai/codex](https://github.com/openai/codex) | +1260 | 61744 |
| 96 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1254 | 30195 |
| 97 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1247 | 30590 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1226 | 7657 |
| 99 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1180 | 19364 |
| 100 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1165 | 7632 |
| 101 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1147 | 87598 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1124 | 16636 |
| 103 | [jundot/omlx](https://github.com/jundot/omlx) | +1123 | 6462 |
| 104 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1068 | 37564 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1041 | 6959 |
| 106 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +984 | 6196 |
| 107 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +929 | 35735 |
| 108 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +907 | 13121 |
| 109 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +901 | 26494 |
| 110 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +872 | 7136 |
| 111 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +871 | 3980 |
| 112 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +857 | 6352 |
| 113 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +848 | 52700 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +788 | 45886 |
| 115 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +775 | 13888 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +767 | 36799 |
| 117 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +752 | 28650 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +739 | 10010 |
| 119 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +738 | 61818 |
| 120 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +733 | 6527 |
| 121 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +730 | 5738 |
| 122 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +726 | 3262 |
| 123 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +712 | 47122 |
| 124 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +696 | 7510 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +665 | 31985 |
| 126 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +655 | 4424 |
| 127 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +651 | 47936 |
| 128 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +646 | 3500 |
| 129 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +645 | 15728 |
| 130 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +632 | 3617 |
| 131 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +623 | 2185 |
| 132 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +614 | 23591 |
| 133 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +606 | 6283 |
| 134 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +599 | 2141 |
| 135 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +598 | 16815 |
| 136 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +581 | 23369 |
| 137 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +570 | 3606 |
| 138 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +570 | 2572 |
| 139 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +568 | 3145 |
| 140 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +552 | 44232 |
| 141 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +549 | 10170 |
| 142 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +544 | 22866 |
| 143 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +535 | 44545 |
| 144 | [docling-project/docling](https://github.com/docling-project/docling) | +532 | 54041 |
| 145 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +518 | 1987 |
| 146 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +503 | 3415 |
| 147 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +498 | 18465 |
| 148 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +497 | 2382 |
| 149 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +496 | 2002 |
| 150 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +496 | 27152 |
| 151 | [eooce/python-ws](https://github.com/eooce/python-ws) | +495 | 1901 |
| 152 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +494 | 3138 |
| 153 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +488 | 39841 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +485 | 19713 |
| 155 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +471 | 8111 |
| 156 | [aden-hive/hive](https://github.com/aden-hive/hive) | +468 | 9768 |
| 157 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +467 | 2741 |
| 158 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +463 | 8031 |
| 159 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +457 | 14488 |
| 160 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +456 | 2015 |
| 161 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +446 | 12929 |
| 162 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +444 | 6188 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +436 | 3255 |
| 164 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +430 | 2410 |
| 165 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +429 | 14637 |
| 166 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +428 | 2074 |
| 167 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +419 | 33712 |
| 168 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +418 | 9951 |
| 169 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +407 | 1599 |
| 170 | [apify/agent-skills](https://github.com/apify/agent-skills) | +407 | 1712 |
| 171 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +402 | 2534 |
| 172 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +382 | 7626 |
| 173 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +382 | 1691 |
| 174 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +373 | 2741 |
| 175 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +372 | 3367 |
| 176 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +367 | 3079 |
| 177 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +346 | 6320 |
| 178 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +344 | 3594 |
| 179 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +339 | 1529 |
| 180 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +318 | 1504 |
| 181 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +318 | 24697 |
| 182 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +309 | 1357 |
| 183 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +308 | 4161 |
| 184 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +308 | 0 |
| 185 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +304 | 10509 |
| 186 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +302 | 1345 |
| 187 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +298 | 1661 |
| 188 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +295 | 1697 |
| 189 | [htdt/godogen](https://github.com/htdt/godogen) | +294 | 1718 |
| 190 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +291 | 13523 |
| 191 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +286 | 29780 |
| 192 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +272 | 3819 |
| 193 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +262 | 10513 |
| 194 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +258 | 21795 |
| 195 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +252 | 1140 |
| 196 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +246 | 36103 |
| 197 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +228 | 979 |
| 198 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +226 | 961 |
| 199 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +226 | 21472 |
| 200 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +218 | 5391 |
| 201 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +202 | 2413 |
| 202 | [usebruno/bruno](https://github.com/usebruno/bruno) | +201 | 41086 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +201 | 7246 |
| 204 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +200 | 1376 |
| 205 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +194 | 1441 |
| 206 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +182 | 822 |
| 207 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +181 | 29033 |
| 208 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +180 | 8887 |
| 209 | [linlay/zenmind](https://github.com/linlay/zenmind) | +178 | 314 |
| 210 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +177 | 25383 |
| 211 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +171 | 40265 |
| 212 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +170 | 988 |
| 213 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +167 | 576 |
| 214 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +164 | 683 |
| 215 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +160 | 1623 |
| 216 | [decolua/9router](https://github.com/decolua/9router) | +159 | 1159 |
| 217 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +157 | 2462 |
| 218 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +156 | 933 |
| 219 | [hectorvent/floci](https://github.com/hectorvent/floci) | +152 | 912 |
| 220 | [jgraph/drawio](https://github.com/jgraph/drawio) | +150 | 4286 |
| 221 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +149 | 1441 |
| 222 | [robinebers/openusage](https://github.com/robinebers/openusage) | +144 | 1579 |
| 223 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +144 | 2070 |
| 224 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +143 | 2643 |
| 225 | [es617/claude-replay](https://github.com/es617/claude-replay) | +142 | 558 |
| 226 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +141 | 5235 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +141 | 1203 |
| 228 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +137 | 725 |
| 229 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +135 | 35473 |
| 230 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +134 | 2345 |
| 231 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +134 | 2133 |
| 232 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +131 | 22850 |
| 233 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +130 | 1713 |
| 234 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +129 | 511 |
| 235 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +129 | 33000 |
| 236 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +128 | 705 |
| 237 | [4ier/neo](https://github.com/4ier/neo) | +124 | 627 |
| 238 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +124 | 711 |
| 239 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +123 | 13745 |
| 240 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +121 | 814 |
| 241 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +121 | 26059 |
| 242 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +119 | 441 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +118 | 12239 |
| 244 | [fmhy/edit](https://github.com/fmhy/edit) | +117 | 8641 |
| 245 | [is-a-dev/register](https://github.com/is-a-dev/register) | +116 | 10010 |
| 246 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +115 | 48784 |
| 247 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +113 | 553 |
| 248 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +109 | 911 |
| 249 | [microg/GmsCore](https://github.com/microg/GmsCore) | +109 | 12659 |
| 250 | [skylot/jadx](https://github.com/skylot/jadx) | +108 | 47365 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +106 | 1163 |
| 252 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +106 | 10158 |
| 253 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +105 | 435 |
| 254 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 255 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +103 | 8857 |
| 256 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +102 | 3321 |
| 257 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +101 | 497 |
| 258 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 547 |
| 259 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +99 | 3550 |
| 260 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +98 | 11227 |
| 261 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +97 | 3225 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +97 | 1365 |
| 263 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +95 | 980 |
| 264 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +92 | 642 |
| 265 | [lklynet/aurral](https://github.com/lklynet/aurral) | +91 | 884 |
| 266 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +90 | 37313 |
| 267 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +89 | 822 |
| 268 | [silships/figma-cli](https://github.com/silships/figma-cli) | +89 | 462 |
| 269 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 270 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +86 | 614 |
| 271 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +86 | 408 |
| 272 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +85 | 524 |
| 273 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +85 | 879 |
| 274 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +83 | 3093 |
| 275 | [idinging/freemail](https://github.com/idinging/freemail) | +82 | 1108 |
| 276 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +82 | 430 |
| 277 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +82 | 1042 |
| 278 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +80 | 877 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +80 | 26990 |
| 280 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +78 | 7072 |
| 281 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +76 | 460 |
| 282 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +75 | 273 |
| 283 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +74 | 8266 |
| 284 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +73 | 609 |
| 285 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +71 | 424 |
| 286 | [apache/kafka](https://github.com/apache/kafka) | +69 | 32043 |
| 287 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +68 | 45263 |
| 288 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +67 | 1023 |
| 289 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +67 | 6117 |
| 290 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +66 | 7673 |
| 291 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +65 | 1365 |
| 292 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +65 | 918 |
| 293 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +64 | 329 |
| 294 | [freeok/so-novel](https://github.com/freeok/so-novel) | +63 | 6394 |
| 295 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +63 | 12420 |
| 296 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +62 | 402 |
| 297 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +62 | 2218 |
| 298 | [openjdk/jdk](https://github.com/openjdk/jdk) | +61 | 22753 |
| 299 | [ReVanced/revanced-patches](https://github.com/ReVanced/revanced-patches) | +60 | 5578 |
| 300 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +60 | 31476 |
