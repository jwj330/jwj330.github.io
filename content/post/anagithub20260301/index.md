---
title: "2026-03-01 GitHub增长趋势报告"
description: "1.wifi-densepose+1713 2.openfang+731 3.awesome-openclaw-usecases+652 4.CoPaw+603 5.worldmonitor+522"
date: 2026-03-01T20:30:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-01 20:30:00

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
        'daily': {"categories": ["pinchtab/pinchtab", "bytedance/deer-flow", "qwibitai/nanoclaw", "abhigyanpatwari/GitNexus", "white0dew/XiaohongshuSkills", "gsd-build/get-shit-done", "zeroclaw-labs/zeroclaw", "sickn33/antigravity-awesome-skills", "D4Vinci/Scrapling", "nullclaw/nullclaw", "moeru-ai/airi", "ruvnet/ruflo", "affaan-m/everything-claude-code", "VoltAgent/awesome-openclaw-skills", "alibaba/OpenSandbox", "koala73/worldmonitor", "agentscope-ai/CoPaw", "hesamsheikh/awesome-openclaw-usecases", "RightNow-AI/openfang", "ruvnet/wifi-densepose"], "data": [181, 192, 195, 199, 207, 212, 219, 235, 264, 269, 315, 318, 355, 407, 423, 522, 603, 652, 731, 1713]},
        'weekly': {"categories": ["HKUDS/nanobot", "anthropics/financial-services-plugins", "zeroclaw-labs/zeroclaw", "gsd-build/get-shit-done", "anomalyco/opencode", "zarazhangrui/frontend-slides", "abhigyanpatwari/GitNexus", "qwibitai/nanoclaw", "VoltAgent/awesome-openclaw-skills", "huggingface/skills", "affaan-m/everything-claude-code", "RightNow-AI/openfang", "anthropics/skills", "hesamsheikh/awesome-openclaw-usecases", "obra/superpowers", "ruvnet/wifi-densepose", "koala73/worldmonitor", "D4Vinci/Scrapling", "x1xhlol/system-prompts-and-models-of-ai-tools", "openclaw/openclaw"], "data": [1163, 1273, 1411, 1414, 1432, 1525, 1590, 1595, 1658, 1664, 1710, 1860, 1939, 2505, 2518, 2542, 2552, 2587, 2997, 7410]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "daytonaio/daytona", "gsd-build/get-shit-done", "hesamsheikh/awesome-openclaw-usecases", "badlogic/pi-mono", "x1xhlol/system-prompts-and-models-of-ai-tools", "thedotmack/claude-mem", "qwibitai/nanoclaw", "koala73/worldmonitor", "VoltAgent/awesome-openclaw-skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "anthropics/skills", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "KeygraphHQ/shannon", "obra/superpowers", "HKUDS/nanobot", "openclaw/openclaw"], "data": [3332, 3335, 3360, 3529, 4123, 4233, 4280, 4835, 5107, 5216, 5622, 5683, 5885, 6062, 6590, 6632, 7014, 7413, 8119, 33588]}
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
| 1 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +1713 | 16706 |
| 2 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +731 | 7233 |
| 3 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +652 | 14438 |
| 4 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +603 | 3141 |
| 5 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +522 | 19469 |
| 6 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +423 | 3235 |
| 7 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +407 | 24010 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +355 | 51199 |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +318 | 17181 |
| 10 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +315 | 20062 |
| 11 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +269 | 3911 |
| 12 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +264 | 19482 |
| 13 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +235 | 17663 |
| 14 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +219 | 21619 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +212 | 22782 |
| 16 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +207 | 893 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +199 | 7304 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +195 | 16942 |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +192 | 22907 |
| 20 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +181 | 2224 |
| 21 | [taigrr/spank](https://github.com/taigrr/spank) | +169 | 1003 |
| 22 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +160 | 27206 |
| 23 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +160 | 22147 |
| 24 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +153 | 11966 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +146 | 18440 |
| 26 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +138 | 5042 |
| 27 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +135 | 3760 |
| 28 | [eooce/python-ws](https://github.com/eooce/python-ws) | +134 | 1056 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +130 | 34148 |
| 30 | [superset-sh/superset](https://github.com/superset-sh/superset) | +129 | 2807 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +7410 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2997 | 122870 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2587 | 19482 |
| 4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2552 | 19469 |
| 5 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +2542 | 16706 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2518 | 60312 |
| 7 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2505 | 14438 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +1939 | 74774 |
| 9 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1860 | 7233 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1710 | 51199 |
| 11 | [huggingface/skills](https://github.com/huggingface/skills) | +1664 | 7691 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1658 | 24010 |
| 13 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1595 | 16942 |
| 14 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1590 | 7304 |
| 15 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1525 | 7281 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1432 | 109881 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1414 | 22782 |
| 18 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1411 | 21619 |
| 19 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1273 | 5042 |
| 20 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1163 | 27206 |
| 21 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1121 | 12857 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1054 | 18440 |
| 23 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1050 | 69674 |
| 24 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1009 | 21308 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +967 | 17663 |
| 26 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +965 | 19624 |
| 27 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +956 | 3141 |
| 28 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +889 | 8796 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +866 | 6190 |
| 30 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +795 | 22907 |
| 31 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +791 | 17181 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +784 | 22147 |
| 33 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +769 | 33878 |
| 34 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +673 | 14819 |
| 35 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +672 | 20062 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +665 | 23782 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +661 | 34148 |
| 38 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +659 | 37330 |
| 39 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +655 | 60117 |
| 40 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +645 | 19835 |
| 41 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +591 | 21767 |
| 42 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +574 | 6453 |
| 43 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +571 | 11966 |
| 44 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +571 | 30678 |
| 45 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +568 | 3235 |
| 46 | [alibaba/zvec](https://github.com/alibaba/zvec) | +567 | 8382 |
| 47 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +562 | 11767 |
| 48 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +555 | 3911 |
| 49 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +545 | 2774 |
| 50 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +482 | 16830 |
| 51 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +482 | 8365 |
| 52 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +462 | 2273 |
| 53 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +455 | 37564 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +430 | 26628 |
| 55 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +423 | 25899 |
| 56 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +417 | 3036 |
| 57 | [tw93/Mole](https://github.com/tw93/Mole) | +412 | 36870 |
| 58 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +407 | 1675 |
| 59 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +404 | 1804 |
| 60 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +399 | 0 |
| 61 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +397 | 1591 |
| 62 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +394 | 8523 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +390 | 7363 |
| 64 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +389 | 13301 |
| 65 | [tobi/qmd](https://github.com/tobi/qmd) | +374 | 11245 |
| 66 | [kevinho/clawfeed](https://github.com/kevinho/clawfeed) | +369 | 1400 |
| 67 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +362 | 11717 |
| 68 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +359 | 3977 |
| 69 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +354 | 5974 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +336 | 10095 |
| 71 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +336 | 8577 |
| 72 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +332 | 18467 |
| 73 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +326 | 5769 |
| 74 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +313 | 1397 |
| 75 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +311 | 6005 |
| 76 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +307 | 12404 |
| 77 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +306 | 3941 |
| 78 | [taigrr/spank](https://github.com/taigrr/spank) | +300 | 1003 |
| 79 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +299 | 7474 |
| 80 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 25686 |
| 81 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +298 | 2961 |
| 82 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +298 | 4303 |
| 83 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +295 | 24894 |
| 84 | [eooce/python-ws](https://github.com/eooce/python-ws) | +294 | 1056 |
| 85 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +287 | 3353 |
| 86 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +284 | 8770 |
| 87 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +283 | 7563 |
| 88 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +283 | 11519 |
| 89 | [openai/skills](https://github.com/openai/skills) | +278 | 10280 |
| 90 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +272 | 4295 |
| 91 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +261 | 1601 |
| 92 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +260 | 10155 |
| 93 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +258 | 2224 |
| 94 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +258 | 7215 |
| 95 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +257 | 893 |
| 96 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +256 | 2104 |
| 97 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +250 | 47122 |
| 98 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +247 | 11986 |
| 99 | [superset-sh/superset](https://github.com/superset-sh/superset) | +246 | 2808 |
| 100 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +246 | 36799 |
| 101 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +245 | 9911 |
| 102 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +237 | 7067 |
| 103 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +216 | 1024 |
| 104 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +213 | 2345 |
| 105 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +198 | 30590 |
| 106 | [wshobson/agents](https://github.com/wshobson/agents) | +197 | 29850 |
| 107 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +196 | 14895 |
| 108 | [olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer) | +186 | 877 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +179 | 21699 |
| 110 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +179 | 13072 |
| 111 | [google-research/timesfm](https://github.com/google-research/timesfm) | +177 | 9910 |
| 112 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +174 | 8337 |
| 113 | [google/langextract](https://github.com/google/langextract) | +174 | 33636 |
| 114 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +166 | 2611 |
| 115 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +166 | 1544 |
| 116 | [runesleo/x-reader](https://github.com/runesleo/x-reader) | +164 | 638 |
| 117 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +162 | 8683 |
| 118 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +159 | 2418 |
| 119 | [ndl-lab/ndlocr-lite](https://github.com/ndl-lab/ndlocr-lite) | +158 | 729 |
| 120 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +157 | 8833 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +33588 | 224760 |
| 2 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +8119 | 27206 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +7413 | 60312 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +7014 | 25899 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6632 | 21619 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6590 | 21308 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | +6062 | 74774 |
| 8 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5885 | 109881 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5683 | 51199 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5622 | 24010 |
| 11 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +5216 | 19470 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +5107 | 16942 |
| 13 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4835 | 30678 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4280 | 122870 |
| 15 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4233 | 18440 |
| 16 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4123 | 14438 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3529 | 22782 |
| 18 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3360 | 60117 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3335 | 17663 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3332 | 11767 |
| 21 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3136 | 37330 |
| 22 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +3117 | 16706 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3050 | 34148 |
| 24 | [google/langextract](https://github.com/google/langextract) | +2999 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2871 | 69674 |
| 26 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2772 | 33878 |
| 27 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2667 | 19482 |
| 28 | [openai/skills](https://github.com/openai/skills) | +2606 | 10280 |
| 29 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2553 | 8382 |
| 30 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2513 | 8796 |
| 31 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2485 | 85286 |
| 32 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2373 | 8337 |
| 33 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2347 | 8365 |
| 34 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2340 | 19624 |
| 35 | [virattt/dexter](https://github.com/virattt/dexter) | +2336 | 16783 |
| 36 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2179 | 96919 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2102 | 22147 |
| 38 | [github/spec-kit](https://github.com/github/spec-kit) | +1930 | 71722 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1927 | 14819 |
| 40 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1876 | 6518 |
| 41 | [huggingface/skills](https://github.com/huggingface/skills) | +1872 | 7691 |
| 42 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1865 | 7304 |
| 43 | [pydantic/monty](https://github.com/pydantic/monty) | +1862 | 5851 |
| 44 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1861 | 7233 |
| 45 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1794 | 6190 |
| 46 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1789 | 9110 |
| 47 | [tobi/qmd](https://github.com/tobi/qmd) | +1781 | 11245 |
| 48 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1753 | 149018 |
| 49 | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | +1752 | 9319 |
| 50 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1733 | 9911 |
| 51 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1719 | 17519 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1657 | 147486 |
| 53 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1656 | 5974 |
| 54 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1655 | 7281 |
| 55 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1644 | 5769 |
| 56 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1593 | 37564 |
| 57 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1563 | 10129 |
| 58 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1556 | 26628 |
| 59 | [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | +1554 | 10984 |
| 60 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1552 | 24894 |
| 61 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1532 | 11966 |
| 62 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1493 | 8504 |
| 63 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1489 | 8940 |
| 64 | [tw93/Mole](https://github.com/tw93/Mole) | +1483 | 36870 |
| 65 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1474 | 33712 |
| 66 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1471 | 5100 |
| 67 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1469 | 13301 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1465 | 23782 |
| 69 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1395 | 16830 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1394 | 10095 |
| 71 | [openai/codex](https://github.com/openai/codex) | +1379 | 61744 |
| 72 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1359 | 98536 |
| 73 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1333 | 74887 |
| 74 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1313 | 7478 |
| 75 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1311 | 8577 |
| 76 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1299 | 5227 |
| 77 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1295 | 27100 |
| 78 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1273 | 5042 |
| 79 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1264 | 12857 |
| 80 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +1263 | 32872 |
| 81 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1256 | 7023 |
| 82 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1221 | 7844 |
| 83 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1216 | 4303 |
| 84 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1212 | 3823 |
| 85 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1207 | 4295 |
| 86 | [slopus/happy](https://github.com/slopus/happy) | +1207 | 13915 |
| 87 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1176 | 3941 |
| 88 | [knadh/oat](https://github.com/knadh/oat) | +1171 | 3998 |
| 89 | [steipete/summarize](https://github.com/steipete/summarize) | +1151 | 4623 |
| 90 | [blader/humanizer](https://github.com/blader/humanizer) | +1125 | 7363 |
| 91 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1116 | 4029 |
| 92 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1095 | 17181 |
| 93 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1083 | 19835 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1081 | 12404 |
| 95 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1063 | 3977 |
| 96 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1049 | 21728 |
| 97 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1037 | 21236 |
| 98 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1035 | 3911 |
| 99 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +985 | 11519 |
| 100 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +975 | 95547 |
| 101 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +967 | 22907 |
| 102 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +965 | 43973 |
| 103 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +956 | 3141 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +947 | 25686 |
| 105 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +926 | 18467 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +887 | 23050 |
| 107 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +885 | 61818 |
| 108 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +877 | 2961 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +870 | 21699 |
| 110 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +867 | 14895 |
| 111 | [docling-project/docling](https://github.com/docling-project/docling) | +860 | 54041 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +819 | 18026 |
| 113 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +817 | 8683 |
| 114 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +792 | 11428 |
| 115 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +783 | 47122 |
| 116 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +777 | 15245 |
| 117 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +775 | 13774 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +751 | 8523 |
| 119 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +750 | 8833 |
| 120 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +726 | 71086 |
| 121 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +717 | 10155 |
| 122 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +715 | 36799 |
| 123 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +711 | 30590 |
| 124 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +682 | 31182 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +681 | 29850 |
| 126 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +671 | 7067 |
| 127 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +657 | 13072 |
| 128 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +643 | 3235 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +627 | 9910 |
| 130 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +600 | 1976 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +589 | 47936 |
| 132 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +588 | 54903 |
| 133 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +582 | 3760 |
| 134 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +579 | 17541 |
| 135 | [microsoft/qlib](https://github.com/microsoft/qlib) | +576 | 37792 |
| 136 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +560 | 39841 |
| 137 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +558 | 3359 |
| 138 | [termux/termux-app](https://github.com/termux/termux-app) | +549 | 51073 |
| 139 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +533 | 4155 |
| 140 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +515 | 1397 |
| 141 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +512 | 2035 |
| 142 | [Robbyant/lingbot-world](https://github.com/Robbyant/lingbot-world) | +508 | 3010 |
| 143 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +502 | 1834 |
| 144 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +489 | 15618 |
| 145 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +486 | 2418 |
| 146 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +482 | 1806 |
| 147 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +479 | 1544 |
| 148 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +479 | 1142 |
| 149 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +478 | 2611 |
| 150 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +477 | 2277 |
| 151 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +473 | 1822 |
| 152 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +472 | 1013 |
| 153 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +470 | 2897 |
| 154 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +468 | 7474 |
| 155 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +462 | 10020 |
| 156 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +458 | 4649 |
| 157 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +456 | 3262 |
| 158 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +454 | 44545 |
| 159 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +447 | 13874 |
| 160 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +444 | 23973 |
| 161 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +440 | 1375 |
| 162 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +424 | 36103 |
| 163 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +423 | 11111 |
| 164 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +420 | 6909 |
| 165 | [openclaw/skills](https://github.com/openclaw/skills) | +413 | 1697 |
| 166 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +412 | 5941 |
| 167 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +412 | 28653 |
| 168 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +408 | 1675 |
| 169 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +399 | 14216 |
| 170 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +392 | 10290 |
| 171 | [oraios/serena](https://github.com/oraios/serena) | +391 | 20828 |
| 172 | [samugit83/redamon](https://github.com/samugit83/redamon) | +388 | 1346 |
| 173 | [usestrix/strix](https://github.com/usestrix/strix) | +387 | 20663 |
| 174 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +382 | 1177 |
| 175 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +380 | 2905 |
| 176 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +377 | 25303 |
| 177 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +373 | 5993 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +370 | 5096 |
| 179 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +367 | 8686 |
| 180 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +360 | 14938 |
| 181 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +357 | 44232 |
| 182 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +353 | 10959 |
| 183 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +350 | 2046 |
| 184 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +347 | 23924 |
| 185 | [vnpy/vnpy](https://github.com/vnpy/vnpy) | +343 | 36870 |
| 186 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +342 | 12465 |
| 187 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +342 | 36697 |
| 188 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +338 | 1168 |
| 189 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +334 | 28850 |
| 190 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +328 | 1836 |
| 191 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +323 | 8752 |
| 192 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +321 | 20902 |
| 193 | [robinebers/openusage](https://github.com/robinebers/openusage) | +319 | 1108 |
| 194 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +317 | 880 |
| 195 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +317 | 23729 |
| 196 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +314 | 5568 |
| 197 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +314 | 3863 |
| 198 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +310 | 1155 |
| 199 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +293 | 5380 |
| 200 | [eooce/python-ws](https://github.com/eooce/python-ws) | +285 | 1056 |
| 201 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +284 | 877 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +284 | 9597 |
| 203 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +281 | 1024 |
| 204 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +272 | 1111 |
| 205 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +271 | 2346 |
| 206 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +270 | 3291 |
| 207 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +270 | 881 |
| 208 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +265 | 893 |
| 209 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +260 | 895 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +255 | 41086 |
| 211 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +247 | 830 |
| 212 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +245 | 22467 |
| 213 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +242 | 808 |
| 214 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +237 | 21057 |
| 215 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +232 | 12706 |
| 216 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +231 | 1775 |
| 217 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +230 | 28505 |
| 218 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +229 | 6476 |
| 219 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +228 | 2406 |
| 220 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +228 | 3010 |
| 221 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 306 |
| 222 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +215 | 40265 |
| 223 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +210 | 787 |
| 224 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +204 | 680 |
| 225 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +201 | 615 |
| 226 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +199 | 39596 |
| 227 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +197 | 689 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +192 | 3868 |
| 229 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +188 | 756 |
| 230 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +186 | 11722 |
| 231 | [qist/tvbox](https://github.com/qist/tvbox) | +185 | 8304 |
| 232 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +180 | 656 |
| 233 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +180 | 2987 |
| 234 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +177 | 29780 |
| 235 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +175 | 2230 |
| 236 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +174 | 644 |
| 237 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +172 | 513 |
| 238 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +170 | 8297 |
| 239 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +170 | 1760 |
| 240 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +169 | 566 |
| 241 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +169 | 33000 |
| 242 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +163 | 25701 |
| 243 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +158 | 1230 |
| 244 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +158 | 515 |
| 245 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +158 | 37313 |
| 246 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +154 | 13468 |
| 247 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +154 | 3067 |
| 248 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +151 | 6861 |
| 249 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +148 | 485 |
| 250 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +146 | 513 |
| 251 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +145 | 449 |
| 252 | [decolua/9router](https://github.com/decolua/9router) | +140 | 601 |
| 253 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +139 | 4761 |
| 254 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +138 | 4645 |
| 255 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +136 | 546 |
| 256 | [expo/skills](https://github.com/expo/skills) | +135 | 1252 |
| 257 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +129 | 451 |
| 258 | [bradygaster/squad](https://github.com/bradygaster/squad) | +128 | 527 |
| 259 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +128 | 679 |
| 260 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +127 | 1293 |
| 261 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +126 | 3219 |
| 262 | [apify/agent-skills](https://github.com/apify/agent-skills) | +124 | 565 |
| 263 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 264 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +121 | 9783 |
| 265 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +120 | 922 |
| 266 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 544 |
| 267 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +119 | 3002 |
| 268 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 384 |
| 269 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +113 | 1044 |
| 270 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +112 | 26716 |
| 271 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +108 | 372 |
| 272 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +106 | 3024 |
| 273 | [microg/GmsCore](https://github.com/microg/GmsCore) | +105 | 12408 |
| 274 | [skylot/jadx](https://github.com/skylot/jadx) | +105 | 47365 |
| 275 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +104 | 4483 |
| 276 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +96 | 35473 |
| 277 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +91 | 10880 |
| 278 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +90 | 2825 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +88 | 8510 |
| 280 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +87 | 514 |
| 281 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +87 | 1452 |
| 282 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +87 | 28632 |
| 283 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +86 | 323 |
| 284 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +86 | 234 |
| 285 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +83 | 685 |
| 286 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +81 | 1168 |
| 287 | [dataease/dataease](https://github.com/dataease/dataease) | +80 | 23483 |
| 288 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +78 | 287 |
| 289 | [FongMi/TV](https://github.com/FongMi/TV) | +78 | 7454 |
| 290 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +77 | 276 |
| 291 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +77 | 714 |
| 292 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +77 | 21270 |
| 293 | [openjdk/jdk](https://github.com/openjdk/jdk) | +77 | 22657 |
| 294 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +77 | 12261 |
| 295 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +76 | 45263 |
| 296 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +76 | 5811 |
| 297 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +75 | 251 |
| 298 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1306 |
| 299 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +74 | 826 |
| 300 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +74 | 3420 |
