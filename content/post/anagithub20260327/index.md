---
title: "2026-03-27 GitHub增长趋势报告"
description: "1.last30days-skill+301 2.deer-flow+252 3.paperclip+132 4.oh-my-claudecode+128 5.learn-claude-code+120"
date: 2026-03-27T20:41:40+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-27 20:41:40

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
        'daily': {"categories": ["virattt/dexter", "thedotmack/claude-mem", "jackwener/opencli", "agentscope-ai/agentscope", "Crosstalk-Solutions/project-nomad", "ruvnet/ruflo", "666ghj/MiroFish", "gsd-build/get-shit-done", "datalab-to/chandra", "MiniMax-AI/skills", "luongnv89/claude-howto", "Donchitos/Claude-Code-Game-Studios", "ruvnet/RuView", "msitarzewski/agency-agents", "nextlevelbuilder/ui-ux-pro-max-skill", "shareAI-lab/learn-claude-code", "Yeachan-Heo/oh-my-claudecode", "paperclipai/paperclip", "bytedance/deer-flow", "mvanhorn/last30days-skill"], "data": [67, 69, 69, 75, 78, 78, 78, 81, 82, 91, 97, 103, 107, 110, 111, 120, 128, 132, 252, 301]},
        'weekly': {"categories": ["mvanhorn/last30days-skill", "jackwener/opencli", "nextlevelbuilder/ui-ux-pro-max-skill", "anthropics/skills", "jarrodwatts/claude-hud", "shareAI-lab/learn-claude-code", "Donchitos/Claude-Code-Game-Studios", "Lum1104/Understand-Anything", "pascalorg/editor", "MiniMax-AI/skills", "gsd-build/get-shit-done", "666ghj/MiroFish", "msitarzewski/agency-agents", "TauricResearch/TradingAgents", "FujiwaraChoki/MoneyPrinterV2", "karpathy/autoresearch", "Crosstalk-Solutions/project-nomad", "bytedance/deer-flow", "obra/superpowers", "affaan-m/everything-claude-code"], "data": [770, 821, 844, 889, 892, 945, 972, 991, 996, 1001, 1067, 1190, 1370, 1587, 1695, 2283, 2387, 2531, 2693, 3543]},
        'monthly': {"categories": ["RightNow-AI/openfang", "shanraisshan/claude-code-best-practice", "anomalyco/opencode", "gsd-build/get-shit-done", "hesamsheikh/awesome-openclaw-usecases", "moeru-ai/airi", "shareAI-lab/learn-claude-code", "VoltAgent/awesome-openclaw-skills", "bytedance/deer-flow", "googleworkspace/cli", "anthropics/skills", "koala73/worldmonitor", "paperclipai/paperclip", "666ghj/MiroFish", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [3510, 3562, 4052, 4198, 4224, 4375, 4375, 4681, 4873, 4882, 5325, 6188, 7148, 7521, 9010, 10005, 11327, 11516, 12326, 24154]}
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
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +301 | 12414 |
| 2 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +252 | 50038 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +132 | 35310 |
| 4 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +128 | 13817 |
| 5 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +120 | 40793 |
| 6 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +111 | 34148 |
| 7 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +110 | 64229 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +107 | 43783 |
| 9 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +103 | 6726 |
| 10 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +97 | 2816 |
| 11 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +91 | 6774 |
| 12 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +82 | 6925 |
| 13 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +81 | 43356 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +78 | 44205 |
| 15 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +78 | 27431 |
| 16 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +78 | 18192 |
| 17 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +75 | 21159 |
| 18 | [jackwener/opencli](https://github.com/jackwener/opencli) | +69 | 8046 |
| 19 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +69 | 30678 |
| 20 | [virattt/dexter](https://github.com/virattt/dexter) | +67 | 19604 |
| 21 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +66 | 14469 |
| 22 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +62 | 14232 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +61 | 14524 |
| 24 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +61 | 26668 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +60 | 34449 |
| 26 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +51 | 30590 |
| 27 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +50 | 1188 |
| 28 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +50 | 40043 |
| 29 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +47 | 1848 |
| 30 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +46 | 33263 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3543 | 51199 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +2693 | 60312 |
| 3 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2531 | 50038 |
| 4 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2387 | 18192 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2283 | 58375 |
| 6 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1695 | 26668 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1587 | 30590 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1370 | 64229 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1190 | 44205 |
| 10 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1067 | 43356 |
| 11 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1001 | 6774 |
| 12 | [pascalorg/editor](https://github.com/pascalorg/editor) | +996 | 7585 |
| 13 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +991 | 6589 |
| 14 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +972 | 6726 |
| 15 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +945 | 40793 |
| 16 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +892 | 14232 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +889 | 74774 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +844 | 34148 |
| 19 | [jackwener/opencli](https://github.com/jackwener/opencli) | +821 | 8046 |
| 20 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +770 | 12414 |
| 21 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +743 | 43783 |
| 22 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +697 | 4782 |
| 23 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +677 | 13781 |
| 24 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +667 | 14469 |
| 25 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +655 | 9846 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +652 | 35311 |
| 27 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +645 | 27431 |
| 28 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +580 | 33263 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +552 | 22636 |
| 30 | [mattpocock/skills](https://github.com/mattpocock/skills) | +550 | 10510 |
| 31 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +540 | 44615 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +528 | 34449 |
| 33 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +513 | 25292 |
| 34 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +506 | 12638 |
| 35 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +481 | 19518 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +477 | 14101 |
| 37 | [louis-e/arnis](https://github.com/louis-e/arnis) | +476 | 13692 |
| 38 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +471 | 14237 |
| 39 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +459 | 21816 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +445 | 14524 |
| 41 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +428 | 42477 |
| 42 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +424 | 30678 |
| 43 | [gofr-dev/gofr](https://github.com/gofr-dev/gofr) | +401 | 21016 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +392 | 26330 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +382 | 28495 |
| 46 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +379 | 17549 |
| 47 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +365 | 19852 |
| 48 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +364 | 17782 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +361 | 34902 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +358 | 33878 |
| 51 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +356 | 39841 |
| 52 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +350 | 3810 |
| 53 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +346 | 13817 |
| 54 | [hectorvent/floci](https://github.com/hectorvent/floci) | +344 | 1938 |
| 55 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +342 | 31473 |
| 56 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +340 | 21159 |
| 57 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +333 | 2255 |
| 58 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +330 | 9099 |
| 59 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +325 | 37330 |
| 60 | [tw93/Mole](https://github.com/tw93/Mole) | +319 | 36870 |
| 61 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +316 | 20168 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +312 | 20681 |
| 63 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +311 | 11922 |
| 64 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +297 | 2780 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +296 | 16992 |
| 66 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +294 | 7121 |
| 67 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +286 | 3699 |
| 68 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +281 | 36622 |
| 69 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +280 | 15023 |
| 70 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +278 | 27865 |
| 71 | [nikilster/clawflows](https://github.com/nikilster/clawflows) | +278 | 1287 |
| 72 | [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | +276 | 25101 |
| 73 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +273 | 6028 |
| 74 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +271 | 27804 |
| 75 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +269 | 33360 |
| 76 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +255 | 7837 |
| 77 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +239 | 12114 |
| 78 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +233 | 8674 |
| 79 | [eze-is/web-access](https://github.com/eze-is/web-access) | +231 | 1883 |
| 80 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +230 | 8848 |
| 81 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +227 | 23398 |
| 82 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +223 | 1848 |
| 83 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +220 | 27655 |
| 84 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +218 | 3939 |
| 85 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +216 | 31953 |
| 86 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +213 | 30774 |
| 87 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +211 | 1858 |
| 88 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +210 | 25238 |
| 89 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +210 | 5126 |
| 90 | [math-inc/OpenGauss](https://github.com/math-inc/OpenGauss) | +208 | 1132 |
| 91 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +196 | 36799 |
| 92 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +190 | 6485 |
| 93 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +188 | 17490 |
| 94 | [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) | +187 | 2024 |
| 95 | [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | +185 | 1856 |
| 96 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +185 | 13308 |
| 97 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +182 | 1140 |
| 98 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +182 | 8444 |
| 99 | [jundot/omlx](https://github.com/jundot/omlx) | +180 | 7171 |
| 100 | [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | +177 | 2931 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +176 | 7400 |
| 102 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +173 | 25718 |
| 103 | [cacggghp/vk-turn-proxy](https://github.com/cacggghp/vk-turn-proxy) | +171 | 2202 |
| 104 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +171 | 1198 |
| 105 | [htdt/godogen](https://github.com/htdt/godogen) | +171 | 2221 |
| 106 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +168 | 2844 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +167 | 27347 |
| 108 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +159 | 6925 |
| 109 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +158 | 36774 |
| 110 | [GAIR-NLP/daVinci-MagiHuman](https://github.com/GAIR-NLP/daVinci-MagiHuman) | +148 | 1009 |
| 111 | [wangziqi06/724-office](https://github.com/wangziqi06/724-office) | +148 | 898 |
| 112 | [Nunchi-trade/auto-researchtrading](https://github.com/Nunchi-trade/auto-researchtrading) | +143 | 647 |
| 113 | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) | +142 | 908 |
| 114 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +141 | 3108 |
| 115 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +135 | 10977 |
| 116 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +134 | 17215 |
| 117 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +133 | 3615 |
| 118 | [win4r/ClawTeam-OpenClaw](https://github.com/win4r/ClawTeam-OpenClaw) | +131 | 825 |
| 119 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +126 | 3977 |
| 120 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +124 | 17462 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +24154 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12326 | 64229 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11516 | 58376 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11327 | 51199 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10005 | 60312 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +9010 | 43783 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7521 | 44206 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7148 | 35311 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6188 | 44615 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5325 | 74774 |
| 11 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4882 | 22785 |
| 12 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4873 | 50038 |
| 13 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +4681 | 42477 |
| 14 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4375 | 40793 |
| 15 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4375 | 35845 |
| 16 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4224 | 27655 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4198 | 43356 |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4052 | 109881 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3562 | 22636 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3510 | 15757 |
| 21 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3504 | 13479 |
| 22 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3502 | 33360 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3082 | 34148 |
| 24 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3065 | 20168 |
| 25 | [openai/symphony](https://github.com/openai/symphony) | +3062 | 14139 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3000 | 19518 |
| 27 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2879 | 18192 |
| 28 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2850 | 19423 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2813 | 14237 |
| 30 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2788 | 10532 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2725 | 34449 |
| 32 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2687 | 69674 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2586 | 14101 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2558 | 85286 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2553 | 26330 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2459 | 25292 |
| 37 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2458 | 27865 |
| 38 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2441 | 36622 |
| 39 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2436 | 27431 |
| 40 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2425 | 14470 |
| 41 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2370 | 26668 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2357 | 28495 |
| 43 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +2281 | 25717 |
| 44 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2274 | 14524 |
| 45 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2172 | 28978 |
| 46 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2106 | 37330 |
| 47 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2076 | 30590 |
| 48 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2073 | 60117 |
| 49 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2064 | 12638 |
| 50 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2053 | 8272 |
| 51 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2038 | 7519 |
| 52 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2017 | 12114 |
| 53 | [github/spec-kit](https://github.com/github/spec-kit) | +2010 | 71722 |
| 54 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2004 | 10977 |
| 55 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1999 | 34688 |
| 56 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1989 | 27804 |
| 57 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1961 | 9382 |
| 58 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1941 | 33878 |
| 59 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1856 | 122870 |
| 60 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1848 | 30678 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1843 | 20681 |
| 62 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1807 | 25238 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1786 | 31473 |
| 64 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1770 | 8211 |
| 65 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1750 | 9094 |
| 66 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1748 | 14232 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1747 | 34902 |
| 68 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1741 | 11008 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1569 | 17490 |
| 70 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1524 | 16453 |
| 71 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1512 | 96919 |
| 72 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1510 | 17782 |
| 73 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1497 | 18634 |
| 74 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1476 | 8085 |
| 75 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1463 | 36774 |
| 76 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1441 | 33263 |
| 77 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1439 | 10510 |
| 78 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1436 | 98536 |
| 79 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1426 | 9846 |
| 80 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1396 | 5957 |
| 81 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1394 | 16993 |
| 82 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1369 | 9099 |
| 83 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1367 | 15023 |
| 84 | [openai/skills](https://github.com/openai/skills) | +1359 | 15521 |
| 85 | [tw93/Mole](https://github.com/tw93/Mole) | +1343 | 36870 |
| 86 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1331 | 26345 |
| 87 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1317 | 43973 |
| 88 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1311 | 8046 |
| 89 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1295 | 8848 |
| 90 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1229 | 87598 |
| 91 | [jundot/omlx](https://github.com/jundot/omlx) | +1203 | 7171 |
| 92 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1200 | 11922 |
| 93 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1184 | 17549 |
| 94 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1160 | 78902 |
| 95 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1156 | 6589 |
| 96 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1139 | 7837 |
| 97 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1115 | 7121 |
| 98 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1106 | 13781 |
| 99 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1051 | 12414 |
| 100 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1047 | 7585 |
| 101 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1019 | 6774 |
| 102 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1004 | 23120 |
| 103 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +984 | 6726 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +962 | 7400 |
| 105 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +959 | 17215 |
| 106 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +944 | 6979 |
| 107 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +926 | 52700 |
| 108 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +920 | 35735 |
| 109 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +863 | 4307 |
| 110 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +856 | 7381 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +841 | 27347 |
| 112 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +817 | 37564 |
| 113 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +794 | 21159 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +769 | 45886 |
| 115 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +767 | 36799 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +766 | 6485 |
| 117 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +755 | 28851 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +740 | 39841 |
| 119 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +740 | 3389 |
| 120 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +735 | 6838 |
| 121 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +704 | 21816 |
| 122 | [tiajinsha/JKVideo](https://github.com/tiajinsha/JKVideo) | +697 | 4782 |
| 123 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +651 | 3594 |
| 124 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +649 | 3771 |
| 125 | [huggingface/skills](https://github.com/huggingface/skills) | +649 | 9944 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +638 | 3810 |
| 127 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +638 | 2259 |
| 128 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +635 | 15793 |
| 129 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +629 | 47936 |
| 130 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +626 | 3615 |
| 131 | [wshobson/agents](https://github.com/wshobson/agents) | +616 | 32397 |
| 132 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +611 | 4105 |
| 133 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +610 | 2211 |
| 134 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +607 | 14340 |
| 135 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +569 | 13224 |
| 136 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +561 | 14402 |
| 137 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +557 | 47122 |
| 138 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +544 | 8674 |
| 139 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +543 | 3699 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +543 | 17462 |
| 141 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +538 | 23977 |
| 142 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +534 | 4563 |
| 143 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +531 | 23690 |
| 144 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +527 | 10565 |
| 145 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +526 | 2582 |
| 146 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +523 | 44232 |
| 147 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +517 | 44545 |
| 148 | [eooce/python-ws](https://github.com/eooce/python-ws) | +512 | 1971 |
| 149 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +511 | 1890 |
| 150 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +508 | 2628 |
| 151 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +505 | 3314 |
| 152 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +503 | 2817 |
| 153 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +496 | 27693 |
| 154 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +469 | 2310 |
| 155 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +469 | 10523 |
| 156 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +461 | 7663 |
| 157 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +459 | 2089 |
| 158 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +451 | 14692 |
| 159 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +437 | 3514 |
| 160 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +433 | 22954 |
| 161 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +415 | 6771 |
| 162 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +407 | 3410 |
| 163 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +404 | 2643 |
| 164 | [apify/agent-skills](https://github.com/apify/agent-skills) | +404 | 1757 |
| 165 | [openclaw/skills](https://github.com/openclaw/skills) | +402 | 3503 |
| 166 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +400 | 10210 |
| 167 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +394 | 30774 |
| 168 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +388 | 6364 |
| 169 | [htdt/godogen](https://github.com/htdt/godogen) | +378 | 2221 |
| 170 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +367 | 13308 |
| 171 | [aden-hive/hive](https://github.com/aden-hive/hive) | +363 | 9851 |
| 172 | [MiroMindAI/MiroThinker](https://github.com/MiroMindAI/MiroThinker) | +352 | 8444 |
| 173 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +350 | 33712 |
| 174 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +346 | 2048 |
| 175 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +345 | 1668 |
| 176 | [hectorvent/floci](https://github.com/hectorvent/floci) | +344 | 1938 |
| 177 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +342 | 1686 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +341 | 6858 |
| 179 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +339 | 3606 |
| 180 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +335 | 3774 |
| 181 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +333 | 1858 |
| 182 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +327 | 3660 |
| 183 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +314 | 4634 |
| 184 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +313 | 1388 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +304 | 24892 |
| 186 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +301 | 1638 |
| 187 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +291 | 1416 |
| 188 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +285 | 10768 |
| 189 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +273 | 29780 |
| 190 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +267 | 14797 |
| 191 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +261 | 1735 |
| 192 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +256 | 13642 |
| 193 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +242 | 5642 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +239 | 4011 |
| 195 | [eze-is/web-access](https://github.com/eze-is/web-access) | +234 | 1883 |
| 196 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +220 | 21952 |
| 197 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +218 | 1777 |
| 198 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +215 | 0 |
| 199 | [usebruno/bruno](https://github.com/usebruno/bruno) | +209 | 41086 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +209 | 36103 |
| 201 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +204 | 1084 |
| 202 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +195 | 867 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +192 | 21604 |
| 204 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +189 | 791 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +189 | 7406 |
| 206 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +177 | 958 |
| 207 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +177 | 8947 |
| 208 | [linlay/zenmind](https://github.com/linlay/zenmind) | +172 | 326 |
| 209 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +169 | 1423 |
| 210 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +169 | 982 |
| 211 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +167 | 1005 |
| 212 | [decolua/9router](https://github.com/decolua/9router) | +166 | 1322 |
| 213 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +161 | 25396 |
| 214 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +159 | 2480 |
| 215 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +154 | 1575 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +150 | 40265 |
| 217 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +150 | 29115 |
| 218 | [es617/claude-replay](https://github.com/es617/claude-replay) | +146 | 578 |
| 219 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +146 | 2436 |
| 220 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +145 | 2244 |
| 221 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +138 | 986 |
| 222 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +138 | 35473 |
| 223 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +137 | 2578 |
| 224 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +136 | 5338 |
| 225 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +134 | 1676 |
| 226 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +133 | 659 |
| 227 | [jgraph/drawio](https://github.com/jgraph/drawio) | +133 | 4411 |
| 228 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +132 | 524 |
| 229 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +130 | 2494 |
| 230 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +130 | 1264 |
| 231 | [4ier/neo](https://github.com/4ier/neo) | +123 | 639 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +121 | 2210 |
| 233 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +120 | 13794 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +118 | 1630 |
| 235 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +116 | 468 |
| 236 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +116 | 1781 |
| 237 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10037 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +114 | 12319 |
| 239 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +114 | 1316 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +113 | 26234 |
| 241 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +110 | 711 |
| 242 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +110 | 808 |
| 243 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +109 | 1379 |
| 244 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +109 | 1462 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +109 | 33000 |
| 246 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 451 |
| 247 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +106 | 48784 |
| 248 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +105 | 22941 |
| 249 | [skylot/jadx](https://github.com/skylot/jadx) | +104 | 47365 |
| 250 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +103 | 597 |
| 251 | [fmhy/edit](https://github.com/fmhy/edit) | +103 | 8726 |
| 252 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +103 | 10311 |
| 253 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 552 |
| 254 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 438 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +100 | 572 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +96 | 12715 |
| 257 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11342 |
| 258 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +94 | 8974 |
| 259 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +93 | 1447 |
| 260 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +92 | 1588 |
| 261 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +90 | 493 |
| 262 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +89 | 3290 |
| 263 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +88 | 708 |
| 264 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +88 | 530 |
| 265 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +88 | 470 |
| 266 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +88 | 931 |
| 267 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +86 | 851 |
| 268 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +85 | 649 |
| 269 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +84 | 398 |
| 270 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +84 | 1028 |
| 271 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +82 | 443 |
| 272 | [idinging/freemail](https://github.com/idinging/freemail) | +80 | 1162 |
| 273 | [dashersw/gea](https://github.com/dashersw/gea) | +79 | 681 |
| 274 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +79 | 3613 |
| 275 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +79 | 670 |
| 276 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +78 | 3392 |
| 277 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +78 | 858 |
| 278 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +76 | 409 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +75 | 27048 |
| 280 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +74 | 411 |
| 281 | [mauriceboe/NOMAD](https://github.com/mauriceboe/NOMAD) | +72 | 1193 |
| 282 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +72 | 37313 |
| 283 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +71 | 366 |
| 284 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +71 | 924 |
| 285 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +69 | 573 |
| 286 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +69 | 8326 |
| 287 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +68 | 3164 |
| 288 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +68 | 45263 |
| 289 | [Kylsky/chatgpt-team-helper](https://github.com/Kylsky/chatgpt-team-helper) | +67 | 1024 |
| 290 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +66 | 12459 |
| 291 | [apache/kafka](https://github.com/apache/kafka) | +65 | 32043 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1533 |
| 293 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7108 |
| 294 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1591 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +61 | 1403 |
| 296 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +61 | 7701 |
| 297 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +60 | 332 |
| 298 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +60 | 4562 |
| 299 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +59 | 472 |
| 300 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +59 | 11598 |
