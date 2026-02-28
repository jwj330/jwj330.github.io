---
title: "2026-02-28 GitHub增长趋势报告"
description: "1.wifi-densepose+762 2.awesome-openclaw-usecases+583 3.openfang+510 4.financial-services-plugins+427 5.Scrapling+357"
date: 2026-02-28T20:28:51+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-28 20:28:51

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
        'daily': {"categories": ["shareAI-lab/learn-claude-code", "HKUDS/nanobot", "koala73/worldmonitor", "abhigyanpatwari/GitNexus", "badlogic/pi-mono", "qwibitai/nanoclaw", "gsd-build/get-shit-done", "zeroclaw-labs/zeroclaw", "zarazhangrui/frontend-slides", "datawhalechina/hello-agents", "affaan-m/everything-claude-code", "bytedance/deer-flow", "ruvnet/ruflo", "moeru-ai/airi", "VoltAgent/awesome-openclaw-skills", "D4Vinci/Scrapling", "anthropics/financial-services-plugins", "RightNow-AI/openfang", "hesamsheikh/awesome-openclaw-usecases", "ruvnet/wifi-densepose"], "data": [178, 178, 180, 181, 182, 196, 206, 213, 214, 226, 226, 265, 266, 299, 327, 357, 427, 510, 583, 762]},
        'weekly': {"categories": ["RightNow-AI/openfang", "anthropics/financial-services-plugins", "HKUDS/nanobot", "gsd-build/get-shit-done", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "zarazhangrui/frontend-slides", "affaan-m/everything-claude-code", "zeroclaw-labs/zeroclaw", "vxcontrol/pentagi", "abhigyanpatwari/GitNexus", "huggingface/skills", "anthropics/skills", "qwibitai/nanoclaw", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "D4Vinci/Scrapling", "obra/superpowers", "x1xhlol/system-prompts-and-models-of-ai-tools", "openclaw/openclaw"], "data": [1157, 1170, 1218, 1398, 1424, 1445, 1461, 1504, 1507, 1520, 1559, 1696, 1884, 1924, 2059, 2096, 2349, 2515, 3132, 7316]},
        'monthly': {"categories": ["hesamsheikh/awesome-openclaw-usecases", "sickn33/antigravity-awesome-skills", "ComposioHQ/awesome-claude-skills", "daytonaio/daytona", "gsd-build/get-shit-done", "x1xhlol/system-prompts-and-models-of-ai-tools", "badlogic/pi-mono", "koala73/worldmonitor", "qwibitai/nanoclaw", "thedotmack/claude-mem", "VoltAgent/awesome-openclaw-skills", "zeroclaw-labs/zeroclaw", "sipeed/picoclaw", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "KeygraphHQ/shannon", "HKUDS/nanobot", "obra/superpowers", "openclaw/openclaw"], "data": [3514, 3524, 3559, 3725, 3864, 4441, 4610, 4700, 4927, 4973, 6158, 6435, 6510, 6539, 6947, 6989, 6997, 7980, 7992, 51824]}
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
| 1 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +762 | 10929 |
| 2 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +583 | 13044 |
| 3 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +510 | 5353 |
| 4 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +427 | 4848 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +357 | 18804 |
| 6 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +327 | 22956 |
| 7 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +299 | 19258 |
| 8 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +266 | 16444 |
| 9 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +265 | 22554 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +226 | 51199 |
| 11 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +226 | 23546 |
| 12 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +214 | 7028 |
| 13 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +213 | 21116 |
| 14 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +206 | 22218 |
| 15 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +196 | 16531 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +182 | 18139 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +181 | 6707 |
| 18 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +180 | 17727 |
| 19 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +178 | 26873 |
| 20 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +178 | 19528 |
| 21 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +177 | 14599 |
| 22 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +174 | 12738 |
| 23 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +174 | 21778 |
| 24 | [eooce/python-ws](https://github.com/eooce/python-ws) | +172 | 811 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +169 | 17157 |
| 26 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +145 | 6200 |
| 27 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +140 | 6021 |
| 28 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +137 | 1757 |
| 29 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +134 | 19303 |
| 30 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +131 | 21104 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +7316 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +3132 | 122870 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2515 | 60312 |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2349 | 18804 |
| 5 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2096 | 17727 |
| 6 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2059 | 13044 |
| 7 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1924 | 16531 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +1884 | 74774 |
| 9 | [huggingface/skills](https://github.com/huggingface/skills) | +1696 | 7516 |
| 10 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1559 | 6707 |
| 11 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1520 | 8686 |
| 12 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1507 | 21116 |
| 13 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1504 | 51199 |
| 14 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1461 | 7028 |
| 15 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1445 | 22956 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1424 | 109881 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1398 | 22218 |
| 18 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1218 | 26873 |
| 19 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1170 | 4848 |
| 20 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1157 | 5353 |
| 21 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1136 | 21104 |
| 22 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1077 | 12738 |
| 23 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1054 | 11611 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1016 | 69674 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1014 | 18139 |
| 26 | [alibaba/zvec](https://github.com/alibaba/zvec) | +929 | 8291 |
| 27 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +898 | 17157 |
| 28 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +880 | 10929 |
| 29 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +868 | 19303 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +802 | 6021 |
| 31 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +771 | 60117 |
| 32 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +753 | 33878 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +714 | 21778 |
| 34 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +665 | 2713 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +653 | 14599 |
| 36 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +643 | 37330 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +639 | 34148 |
| 38 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +637 | 23546 |
| 39 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +634 | 22554 |
| 40 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +622 | 30678 |
| 41 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +556 | 19528 |
| 42 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +519 | 21558 |
| 43 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +505 | 16444 |
| 44 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +501 | 37564 |
| 45 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +480 | 11643 |
| 46 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +477 | 6200 |
| 47 | [tnm/zclaw](https://github.com/tnm/zclaw) | +466 | 1544 |
| 48 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +464 | 16675 |
| 49 | [blader/humanizer](https://github.com/blader/humanizer) | +454 | 7254 |
| 50 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +448 | 8181 |
| 51 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +448 | 2997 |
| 52 | [tw93/Mole](https://github.com/tw93/Mole) | +448 | 36870 |
| 53 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +443 | 25747 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +430 | 26490 |
| 55 | [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | +427 | 18878 |
| 56 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +424 | 5903 |
| 57 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +416 | 3463 |
| 58 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +415 | 2780 |
| 59 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +404 | 2080 |
| 60 | [IgorShadurin/app.yumcut.com](https://github.com/IgorShadurin/app.yumcut.com) | +392 | 914 |
| 61 | [tobi/qmd](https://github.com/tobi/qmd) | +387 | 11106 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +386 | 5717 |
| 63 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +379 | 19258 |
| 64 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +379 | 1537 |
| 65 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +379 | 18341 |
| 66 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +372 | 5046 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +369 | 3866 |
| 68 | [cloudflare/agents](https://github.com/cloudflare/agents) | +368 | 4378 |
| 69 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +366 | 8413 |
| 70 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +362 | 13032 |
| 71 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +358 | 1757 |
| 72 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +347 | 3272 |
| 73 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +340 | 1599 |
| 74 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +334 | 8429 |
| 75 | [kevinho/clawfeed](https://github.com/kevinho/clawfeed) | +333 | 1341 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +325 | 11574 |
| 77 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +312 | 2892 |
| 78 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +312 | 4240 |
| 79 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +307 | 5932 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +303 | 9913 |
| 81 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +303 | 12251 |
| 82 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +298 | 11431 |
| 83 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +295 | 9868 |
| 84 | [google-research/timesfm](https://github.com/google-research/timesfm) | +293 | 9900 |
| 85 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +291 | 24795 |
| 86 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +289 | 25549 |
| 87 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +287 | 1332 |
| 88 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +284 | 47122 |
| 89 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +284 | 2919 |
| 90 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +282 | 1568 |
| 91 | [slopus/happy](https://github.com/slopus/happy) | +282 | 13855 |
| 92 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +282 | 4248 |
| 93 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +281 | 7407 |
| 94 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +275 | 32872 |
| 95 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +266 | 7445 |
| 96 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +265 | 8669 |
| 97 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +264 | 7763 |
| 98 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +263 | 7166 |
| 99 | [openai/skills](https://github.com/openai/skills) | +263 | 10181 |
| 100 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +244 | 1368 |
| 101 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +224 | 36799 |
| 102 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +221 | 1755 |
| 103 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +216 | 9783 |
| 104 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +211 | 2340 |
| 105 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +197 | 30590 |
| 106 | [olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer) | +196 | 860 |
| 107 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +192 | 11091 |
| 108 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +189 | 2386 |
| 109 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +186 | 12986 |
| 110 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +183 | 14811 |
| 111 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +183 | 1785 |
| 112 | [google/langextract](https://github.com/google/langextract) | +181 | 33636 |
| 113 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +179 | 8587 |
| 114 | [wshobson/agents](https://github.com/wshobson/agents) | +175 | 29708 |
| 115 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +175 | 2871 |
| 116 | [eooce/python-ws](https://github.com/eooce/python-ws) | +174 | 811 |
| 117 | [shuaiplus/NodeWarden](https://github.com/shuaiplus/NodeWarden) | +164 | 896 |
| 118 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +164 | 8780 |
| 119 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +162 | 8255 |
| 120 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +161 | 6981 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +51824 | 224760 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +7992 | 60312 |
| 3 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7980 | 26873 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +6997 | 25747 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +6989 | 74774 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +6947 | 109881 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6539 | 51199 |
| 8 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6510 | 21104 |
| 9 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6435 | 21116 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +6158 | 22956 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4973 | 30678 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4927 | 16531 |
| 13 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +4700 | 17728 |
| 14 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4610 | 18139 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4441 | 122870 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3864 | 22218 |
| 17 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3725 | 60117 |
| 18 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3559 | 37330 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3524 | 17157 |
| 20 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +3514 | 13044 |
| 21 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3363 | 34148 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3319 | 11611 |
| 23 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +3148 | 33878 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3107 | 69674 |
| 25 | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | +3034 | 9300 |
| 26 | [google/langextract](https://github.com/google/langextract) | +3027 | 33636 |
| 27 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2689 | 85286 |
| 28 | [openai/skills](https://github.com/openai/skills) | +2600 | 10181 |
| 29 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2598 | 19303 |
| 30 | [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) | +2586 | 7925 |
| 31 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2585 | 8291 |
| 32 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2545 | 14599 |
| 33 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2495 | 8255 |
| 34 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2462 | 8686 |
| 35 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2428 | 18804 |
| 36 | [virattt/dexter](https://github.com/virattt/dexter) | +2404 | 16710 |
| 37 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2403 | 8181 |
| 38 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +2366 | 32872 |
| 39 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2350 | 96919 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2270 | 21778 |
| 41 | [github/spec-kit](https://github.com/github/spec-kit) | +2158 | 71722 |
| 42 | [tobi/qmd](https://github.com/tobi/qmd) | +2077 | 11106 |
| 43 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +2070 | 149018 |
| 44 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1962 | 6990 |
| 45 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1932 | 24795 |
| 46 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1891 | 11643 |
| 47 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1884 | 37564 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1882 | 26490 |
| 49 | [pydantic/monty](https://github.com/pydantic/monty) | +1862 | 5821 |
| 50 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1848 | 6481 |
| 51 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1828 | 17397 |
| 52 | [huggingface/skills](https://github.com/huggingface/skills) | +1818 | 7516 |
| 53 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1806 | 9047 |
| 54 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1794 | 8487 |
| 55 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1748 | 6021 |
| 56 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1741 | 7028 |
| 57 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1728 | 9868 |
| 58 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1717 | 10126 |
| 59 | [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | +1707 | 10979 |
| 60 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1703 | 6707 |
| 61 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1625 | 5903 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1618 | 5717 |
| 63 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1606 | 37810 |
| 64 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1600 | 147486 |
| 65 | [tw93/Mole](https://github.com/tw93/Mole) | +1599 | 36870 |
| 66 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1597 | 16675 |
| 67 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1556 | 23546 |
| 68 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1545 | 98536 |
| 69 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1503 | 8429 |
| 70 | [openai/codex](https://github.com/openai/codex) | +1493 | 61744 |
| 71 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1491 | 33712 |
| 72 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1480 | 7763 |
| 73 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1475 | 9913 |
| 74 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1474 | 8894 |
| 75 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1455 | 5046 |
| 76 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +1449 | 10929 |
| 77 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1416 | 13032 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1413 | 27022 |
| 79 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1397 | 5170 |
| 80 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1352 | 7445 |
| 81 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1332 | 21580 |
| 82 | [slopus/happy](https://github.com/slopus/happy) | +1329 | 13855 |
| 83 | [steveyegge/beads](https://github.com/steveyegge/beads) | +1323 | 17665 |
| 84 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1304 | 74887 |
| 85 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1301 | 7380 |
| 86 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1287 | 4240 |
| 87 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +1261 | 8669 |
| 88 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1227 | 12738 |
| 89 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1205 | 3809 |
| 90 | [steipete/summarize](https://github.com/steipete/summarize) | +1185 | 4604 |
| 91 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1185 | 4248 |
| 92 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1170 | 4848 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1161 | 12251 |
| 94 | [knadh/oat](https://github.com/knadh/oat) | +1159 | 3972 |
| 95 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1158 | 5353 |
| 96 | [blader/humanizer](https://github.com/blader/humanizer) | +1146 | 7254 |
| 97 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1138 | 3866 |
| 98 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +1117 | 11431 |
| 99 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1113 | 19528 |
| 100 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +1098 | 15226 |
| 101 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +1093 | 95547 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1090 | 8587 |
| 103 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1085 | 3872 |
| 104 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1052 | 21191 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1016 | 25549 |
| 106 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1011 | 43973 |
| 107 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1007 | 3463 |
| 108 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +996 | 22963 |
| 109 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +975 | 8780 |
| 110 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +956 | 14811 |
| 111 | [Robbyant/lingbot-world](https://github.com/Robbyant/lingbot-world) | +955 | 3005 |
| 112 | [docling-project/docling](https://github.com/docling-project/docling) | +951 | 54041 |
| 113 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +949 | 21550 |
| 114 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +949 | 11386 |
| 115 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +947 | 18341 |
| 116 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +924 | 28647 |
| 117 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +923 | 61818 |
| 118 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +891 | 47122 |
| 119 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +861 | 2871 |
| 120 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +857 | 13717 |
| 121 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +851 | 71118 |
| 122 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +847 | 8413 |
| 123 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +837 | 17986 |
| 124 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +836 | 6982 |
| 125 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +830 | 6892 |
| 126 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +815 | 71086 |
| 127 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +784 | 2269 |
| 128 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +763 | 30590 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +758 | 36799 |
| 130 | [wshobson/agents](https://github.com/wshobson/agents) | +739 | 29708 |
| 131 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +738 | 12986 |
| 132 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +736 | 9783 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +704 | 54903 |
| 134 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +692 | 31182 |
| 135 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +646 | 4099 |
| 136 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +638 | 47936 |
| 137 | [termux/termux-app](https://github.com/termux/termux-app) | +634 | 51073 |
| 138 | [google-research/timesfm](https://github.com/google-research/timesfm) | +622 | 9900 |
| 139 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +615 | 58595 |
| 140 | [microsoft/qlib](https://github.com/microsoft/qlib) | +611 | 37792 |
| 141 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +608 | 39841 |
| 142 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +593 | 1950 |
| 143 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +588 | 17532 |
| 144 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +574 | 3220 |
| 145 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +572 | 9983 |
| 146 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +562 | 3345 |
| 147 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +554 | 52081 |
| 148 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +545 | 1781 |
| 149 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +532 | 52700 |
| 150 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +528 | 2386 |
| 151 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +518 | 2010 |
| 152 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +515 | 1394 |
| 153 | [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | +511 | 1748 |
| 154 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +503 | 15550 |
| 155 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +503 | 3063 |
| 156 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +497 | 4616 |
| 157 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +497 | 3463 |
| 158 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +492 | 44545 |
| 159 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +486 | 5559 |
| 160 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +479 | 1138 |
| 161 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +473 | 1785 |
| 162 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +471 | 1814 |
| 163 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +471 | 14203 |
| 164 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +468 | 1525 |
| 165 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +465 | 36103 |
| 166 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +462 | 13851 |
| 167 | [oraios/serena](https://github.com/oraios/serena) | +461 | 20796 |
| 168 | [openclaw/skills](https://github.com/openclaw/skills) | +460 | 1656 |
| 169 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +456 | 7407 |
| 170 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +444 | 23967 |
| 171 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +443 | 942 |
| 172 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +437 | 1368 |
| 173 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +436 | 11091 |
| 174 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +428 | 25270 |
| 175 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +419 | 2862 |
| 176 | [usestrix/strix](https://github.com/usestrix/strix) | +417 | 20642 |
| 177 | [exo-explore/exo](https://github.com/exo-explore/exo) | +412 | 41758 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +411 | 5051 |
| 179 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +403 | 12433 |
| 180 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +397 | 5925 |
| 181 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +392 | 10281 |
| 182 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +389 | 5976 |
| 183 | [vnpy/vnpy](https://github.com/vnpy/vnpy) | +384 | 36870 |
| 184 | [samugit83/redamon](https://github.com/samugit83/redamon) | +380 | 1314 |
| 185 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +369 | 20877 |
| 186 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +368 | 23880 |
| 187 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +368 | 44232 |
| 188 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +367 | 8669 |
| 189 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +366 | 1794 |
| 190 | [scaledown-team/scaledown](https://github.com/scaledown-team/scaledown) | +365 | 897 |
| 191 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +363 | 14911 |
| 192 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +358 | 28820 |
| 193 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +356 | 3280 |
| 194 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +352 | 1103 |
| 195 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +350 | 36697 |
| 196 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +347 | 10880 |
| 197 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +344 | 1599 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +342 | 23691 |
| 199 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +338 | 1954 |
| 200 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +338 | 3847 |
| 201 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +329 | 8679 |
| 202 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +328 | 1145 |
| 203 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +313 | 861 |
| 204 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +309 | 9567 |
| 205 | [robinebers/openusage](https://github.com/robinebers/openusage) | +308 | 1092 |
| 206 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +306 | 5370 |
| 207 | [usebruno/bruno](https://github.com/usebruno/bruno) | +295 | 41086 |
| 208 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +279 | 872 |
| 209 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +279 | 22454 |
| 210 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +278 | 21018 |
| 211 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +273 | 37313 |
| 212 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +265 | 1094 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +262 | 12674 |
| 214 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +260 | 2889 |
| 215 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +260 | 6452 |
| 216 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +256 | 2325 |
| 217 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +254 | 876 |
| 218 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +245 | 2405 |
| 219 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +242 | 811 |
| 220 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +240 | 806 |
| 221 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +238 | 39596 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +238 | 28468 |
| 223 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +237 | 40265 |
| 224 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +228 | 11709 |
| 225 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +226 | 1755 |
| 226 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 312 |
| 227 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +224 | 2970 |
| 228 | [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | +216 | 21282 |
| 229 | [VonChange/utao](https://github.com/VonChange/utao) | +214 | 3866 |
| 230 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +210 | 29780 |
| 231 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +209 | 787 |
| 232 | [qist/tvbox](https://github.com/qist/tvbox) | +206 | 8299 |
| 233 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +203 | 746 |
| 234 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +197 | 609 |
| 235 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +195 | 677 |
| 236 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +191 | 659 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +190 | 33000 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +186 | 25690 |
| 239 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +185 | 8293 |
| 240 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +182 | 1739 |
| 241 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +177 | 642 |
| 242 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +175 | 2225 |
| 243 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +171 | 639 |
| 244 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +168 | 476 |
| 245 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +167 | 505 |
| 246 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +166 | 564 |
| 247 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +162 | 13465 |
| 248 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +161 | 28642 |
| 249 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +160 | 6844 |
| 250 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +157 | 1227 |
| 251 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +156 | 4738 |
| 252 | [expo/skills](https://github.com/expo/skills) | +153 | 1237 |
| 253 | [imxv/Pretty-mermaid-skills](https://github.com/imxv/Pretty-mermaid-skills) | +153 | 506 |
| 254 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +151 | 4613 |
| 255 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +150 | 496 |
| 256 | [SeanWong17/Future-Style-Periodic-Table](https://github.com/SeanWong17/Future-Style-Periodic-Table) | +147 | 444 |
| 257 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +146 | 1273 |
| 258 | [decolua/9router](https://github.com/decolua/9router) | +144 | 586 |
| 259 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +141 | 438 |
| 260 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +140 | 48784 |
| 261 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +136 | 3214 |
| 262 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +134 | 542 |
| 263 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +134 | 9771 |
| 264 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +131 | 996 |
| 265 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +130 | 668 |
| 266 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +130 | 1029 |
| 267 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +126 | 2984 |
| 268 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +124 | 906 |
| 269 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +124 | 26710 |
| 270 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 544 |
| 271 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +119 | 4476 |
| 272 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +116 | 437 |
| 273 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +115 | 384 |
| 274 | [skylot/jadx](https://github.com/skylot/jadx) | +114 | 47365 |
| 275 | [microg/GmsCore](https://github.com/microg/GmsCore) | +111 | 12407 |
| 276 | [bradygaster/squad](https://github.com/bradygaster/squad) | +110 | 474 |
| 277 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +110 | 8508 |
| 278 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +108 | 369 |
| 279 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +107 | 3017 |
| 280 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +107 | 35473 |
| 281 | [iBUHub/AIStudioToAPI](https://github.com/iBUHub/AIStudioToAPI) | +100 | 634 |
| 282 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +100 | 685 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +99 | 10871 |
| 284 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +96 | 1447 |
| 285 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +94 | 28626 |
| 286 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +94 | 2806 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +92 | 1162 |
| 288 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +86 | 233 |
| 289 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +85 | 816 |
| 290 | [FongMi/TV](https://github.com/FongMi/TV) | +85 | 7452 |
| 291 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +85 | 12249 |
| 292 | [dataease/dataease](https://github.com/dataease/dataease) | +84 | 23476 |
| 293 | [eooce/node-ws](https://github.com/eooce/node-ws) | +83 | 5696 |
| 294 | [openjdk/jdk](https://github.com/openjdk/jdk) | +83 | 22656 |
| 295 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +83 | 5807 |
| 296 | [xlrpa/FlowBot](https://github.com/xlrpa/FlowBot) | +82 | 903 |
| 297 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +82 | 45263 |
| 298 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +81 | 718 |
| 299 | [suyunkai/EVCam](https://github.com/suyunkai/EVCam) | +81 | 278 |
| 300 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +80 | 1749 |
