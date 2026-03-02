---
title: "2026-03-02 GitHub增长趋势报告"
description: "1.wifi-densepose+1832 2.worldmonitor+811 3.openfang+720 4.CoPaw+564 5.awesome-openclaw-usecases+451"
date: 2026-03-02T20:40:18+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-02 20:40:18

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
        'daily': {"categories": ["qwibitai/nanoclaw", "zeroclaw-labs/zeroclaw", "ringhyacinth/Star-Office-UI", "datawhalechina/hello-agents", "K-Dense-AI/claude-scientific-skills", "D4Vinci/Scrapling", "pinchtab/pinchtab", "nullclaw/nullclaw", "ruvnet/ruflo", "nicobailon/visual-explainer", "abhigyanpatwari/GitNexus", "alibaba/OpenSandbox", "VoltAgent/awesome-openclaw-skills", "moeru-ai/airi", "affaan-m/everything-claude-code", "hesamsheikh/awesome-openclaw-usecases", "agentscope-ai/CoPaw", "RightNow-AI/openfang", "koala73/worldmonitor", "ruvnet/wifi-densepose"], "data": [198, 205, 210, 213, 220, 221, 254, 258, 259, 264, 284, 315, 418, 437, 440, 451, 564, 720, 811, 1832]},
        'weekly': {"categories": ["qwibitai/nanoclaw", "huggingface/skills", "gsd-build/get-shit-done", "zeroclaw-labs/zeroclaw", "anthropics/financial-services-plugins", "anomalyco/opencode", "agentscope-ai/CoPaw", "zarazhangrui/frontend-slides", "abhigyanpatwari/GitNexus", "VoltAgent/awesome-openclaw-skills", "affaan-m/everything-claude-code", "anthropics/skills", "x1xhlol/system-prompts-and-models-of-ai-tools", "obra/superpowers", "RightNow-AI/openfang", "D4Vinci/Scrapling", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "ruvnet/wifi-densepose", "openclaw/openclaw"], "data": [1226, 1233, 1318, 1318, 1326, 1468, 1480, 1576, 1671, 1829, 1950, 2069, 2310, 2411, 2532, 2586, 2691, 2696, 4124, 7701]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "badlogic/pi-mono", "x1xhlol/system-prompts-and-models-of-ai-tools", "thedotmack/claude-mem", "hesamsheikh/awesome-openclaw-usecases", "ruvnet/wifi-densepose", "qwibitai/nanoclaw", "VoltAgent/awesome-openclaw-skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "koala73/worldmonitor", "anthropics/skills", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "KeygraphHQ/shannon", "obra/superpowers", "HKUDS/nanobot", "openclaw/openclaw"], "data": [3333, 3378, 3602, 4063, 4309, 4432, 4528, 4694, 4907, 5518, 5751, 5765, 6000, 6081, 6677, 6819, 7070, 7439, 7987, 30829]}
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
| 1 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +1832 | 21356 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +811 | 22963 |
| 3 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +720 | 9005 |
| 4 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +564 | 5166 |
| 5 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +451 | 15754 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +440 | 51199 |
| 7 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +437 | 21312 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +418 | 25318 |
| 9 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +315 | 4141 |
| 10 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +284 | 8150 |
| 11 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +264 | 4844 |
| 12 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +259 | 17949 |
| 13 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +258 | 4464 |
| 14 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +254 | 2867 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +221 | 20037 |
| 16 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +220 | 10970 |
| 17 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +213 | 24500 |
| 18 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +210 | 1292 |
| 19 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +205 | 22193 |
| 20 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +198 | 17577 |
| 21 | [superset-sh/superset](https://github.com/superset-sh/superset) | +194 | 3416 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +189 | 23352 |
| 23 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +186 | 20378 |
| 24 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +178 | 37330 |
| 25 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +176 | 23443 |
| 26 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +172 | 27774 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +167 | 22673 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +164 | 18933 |
| 29 | [block/goose](https://github.com/block/goose) | +160 | 31098 |
| 30 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +159 | 12354 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +7701 | 224760 |
| 2 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +4124 | 21356 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2696 | 22963 |
| 4 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2691 | 15754 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2586 | 20037 |
| 6 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2532 | 9005 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2411 | 60312 |
| 8 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2310 | 122870 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +2069 | 74774 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1950 | 51199 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1829 | 25318 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1671 | 8150 |
| 13 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1576 | 7546 |
| 14 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1480 | 5166 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1468 | 109881 |
| 16 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1326 | 5181 |
| 17 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1318 | 22193 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1318 | 23352 |
| 19 | [huggingface/skills](https://github.com/huggingface/skills) | +1233 | 7891 |
| 20 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1226 | 17577 |
| 21 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1125 | 27774 |
| 22 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1124 | 13049 |
| 23 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1113 | 18933 |
| 24 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1095 | 21312 |
| 25 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1005 | 17949 |
| 26 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +994 | 69674 |
| 27 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +958 | 18058 |
| 28 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +950 | 23443 |
| 29 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +921 | 19919 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +877 | 22673 |
| 31 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +864 | 21613 |
| 32 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +851 | 24500 |
| 33 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +849 | 4141 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +798 | 20378 |
| 35 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +765 | 33878 |
| 36 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +743 | 37330 |
| 37 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +737 | 4464 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +712 | 15176 |
| 39 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +683 | 12354 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +663 | 34148 |
| 41 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +648 | 21961 |
| 42 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +636 | 6684 |
| 43 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +625 | 6439 |
| 44 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +584 | 60117 |
| 45 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +560 | 4844 |
| 46 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +525 | 17136 |
| 47 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +522 | 2477 |
| 48 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +520 | 30678 |
| 49 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +504 | 2874 |
| 50 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +490 | 8641 |
| 51 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +462 | 13658 |
| 52 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +461 | 10970 |
| 53 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +454 | 2867 |
| 54 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +449 | 1760 |
| 55 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +444 | 26929 |
| 56 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +427 | 8672 |
| 57 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +421 | 37564 |
| 58 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +421 | 3178 |
| 59 | [superset-sh/superset](https://github.com/superset-sh/superset) | +415 | 3416 |
| 60 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +406 | 11951 |
| 61 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +405 | 26130 |
| 62 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +402 | 0 |
| 63 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +391 | 1667 |
| 64 | [taigrr/spank](https://github.com/taigrr/spank) | +388 | 1129 |
| 65 | [kevinho/clawfeed](https://github.com/kevinho/clawfeed) | +387 | 1454 |
| 66 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +376 | 11917 |
| 67 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +375 | 8899 |
| 68 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +362 | 1152 |
| 69 | [tobi/qmd](https://github.com/tobi/qmd) | +354 | 11513 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +347 | 12684 |
| 71 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +346 | 8808 |
| 72 | [eooce/python-ws](https://github.com/eooce/python-ws) | +337 | 1199 |
| 73 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +336 | 1466 |
| 74 | [alibaba/zvec](https://github.com/alibaba/zvec) | +336 | 8460 |
| 75 | [block/goose](https://github.com/block/goose) | +325 | 31098 |
| 76 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +325 | 6133 |
| 77 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +324 | 25047 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +323 | 10290 |
| 79 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +317 | 18601 |
| 80 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +308 | 8912 |
| 81 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +307 | 7526 |
| 82 | [tw93/Mole](https://github.com/tw93/Mole) | +299 | 36870 |
| 83 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +290 | 7747 |
| 84 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +288 | 6092 |
| 85 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +287 | 25861 |
| 86 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +286 | 1292 |
| 87 | [openai/skills](https://github.com/openai/skills) | +286 | 10425 |
| 88 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +284 | 3049 |
| 89 | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | +281 | 25318 |
| 90 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +277 | 4420 |
| 91 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +266 | 12159 |
| 92 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +263 | 11647 |
| 93 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +258 | 2197 |
| 94 | [blader/humanizer](https://github.com/blader/humanizer) | +257 | 7466 |
| 95 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | +252 | 1646 |
| 96 | [steveyegge/beads](https://github.com/steveyegge/beads) | +250 | 17875 |
| 97 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +247 | 3583 |
| 98 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +247 | 36799 |
| 99 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +244 | 1115 |
| 100 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +236 | 3900 |
| 101 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +234 | 47122 |
| 102 | [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | +232 | 1297 |
| 103 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +227 | 4348 |
| 104 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +221 | 7098 |
| 105 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +208 | 14996 |
| 106 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +205 | 30590 |
| 107 | [wshobson/agents](https://github.com/wshobson/agents) | +201 | 29967 |
| 108 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +197 | 2360 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +193 | 21811 |
| 110 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +189 | 13192 |
| 111 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +188 | 4539 |
| 112 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +180 | 8417 |
| 113 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +178 | 9976 |
| 114 | [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | +173 | 7882 |
| 115 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +171 | 560 |
| 116 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +168 | 44232 |
| 117 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +167 | 2682 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +167 | 8763 |
| 119 | [google/langextract](https://github.com/google/langextract) | +167 | 33636 |
| 120 | [ndl-lab/ndlocr-lite](https://github.com/ndl-lab/ndlocr-lite) | +166 | 744 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30829 | 224760 |
| 2 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7987 | 27774 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +7439 | 60312 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +7070 | 26130 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6819 | 22193 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6677 | 21614 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills) | +6081 | 74774 |
| 8 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6000 | 22963 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5765 | 109881 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5751 | 51199 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5518 | 25318 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4907 | 17577 |
| 13 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +4694 | 21357 |
| 14 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4528 | 15754 |
| 15 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4432 | 30678 |
| 16 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4309 | 122870 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4063 | 18933 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3602 | 23352 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3378 | 18058 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3333 | 11951 |
| 21 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3267 | 60117 |
| 22 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3177 | 37330 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2996 | 34148 |
| 24 | [google/langextract](https://github.com/google/langextract) | +2994 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2900 | 69674 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2866 | 20037 |
| 27 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2724 | 33878 |
| 28 | [openai/skills](https://github.com/openai/skills) | +2635 | 10425 |
| 29 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2580 | 8460 |
| 30 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2547 | 8899 |
| 31 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2537 | 9005 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2524 | 85286 |
| 33 | [virattt/dexter](https://github.com/virattt/dexter) | +2305 | 16843 |
| 34 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2291 | 8417 |
| 35 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2246 | 96919 |
| 36 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2222 | 8641 |
| 37 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2158 | 19919 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2152 | 22673 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2128 | 8150 |
| 40 | [huggingface/skills](https://github.com/huggingface/skills) | +1926 | 7891 |
| 41 | [github/spec-kit](https://github.com/github/spec-kit) | +1918 | 71722 |
| 42 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1896 | 6567 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1877 | 15176 |
| 44 | [pydantic/monty](https://github.com/pydantic/monty) | +1877 | 5887 |
| 45 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1854 | 9399 |
| 46 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1847 | 6439 |
| 47 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1758 | 149018 |
| 48 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1747 | 9976 |
| 49 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1718 | 17630 |
| 50 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1712 | 7546 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1697 | 147486 |
| 52 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1685 | 6092 |
| 53 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1655 | 5817 |
| 54 | [tobi/qmd](https://github.com/tobi/qmd) | +1641 | 11513 |
| 55 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1627 | 24500 |
| 56 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1616 | 12354 |
| 57 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1577 | 13658 |
| 58 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1544 | 37564 |
| 59 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1530 | 26929 |
| 60 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1506 | 8979 |
| 61 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1502 | 10138 |
| 62 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1495 | 25047 |
| 63 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1488 | 33712 |
| 64 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1484 | 5166 |
| 65 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1478 | 5161 |
| 66 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1457 | 8558 |
| 67 | [tw93/Mole](https://github.com/tw93/Mole) | +1434 | 36870 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1411 | 10291 |
| 69 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1401 | 17136 |
| 70 | [openai/codex](https://github.com/openai/codex) | +1376 | 61744 |
| 71 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1367 | 74887 |
| 72 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1367 | 98536 |
| 73 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1352 | 7602 |
| 74 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1326 | 5181 |
| 75 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1325 | 8808 |
| 76 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1317 | 4844 |
| 77 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +1311 | 4539 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1306 | 27224 |
| 79 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1302 | 17949 |
| 80 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1301 | 13049 |
| 81 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1291 | 5301 |
| 82 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1287 | 4379 |
| 83 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1283 | 4464 |
| 84 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1235 | 7059 |
| 85 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1226 | 20378 |
| 86 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1219 | 4348 |
| 87 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1211 | 21313 |
| 88 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1203 | 4021 |
| 89 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1201 | 4420 |
| 90 | [slopus/happy](https://github.com/slopus/happy) | +1200 | 14008 |
| 91 | [knadh/oat](https://github.com/knadh/oat) | +1175 | 4028 |
| 92 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +1171 | 32872 |
| 93 | [steipete/summarize](https://github.com/steipete/summarize) | +1154 | 4648 |
| 94 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1154 | 4170 |
| 95 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1130 | 23443 |
| 96 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1118 | 12684 |
| 97 | [blader/humanizer](https://github.com/blader/humanizer) | +1117 | 7466 |
| 98 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1044 | 21276 |
| 99 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1032 | 87598 |
| 100 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1028 | 6684 |
| 101 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1019 | 21825 |
| 102 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +990 | 95547 |
| 103 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +987 | 11647 |
| 104 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +965 | 18601 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +946 | 25861 |
| 106 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +911 | 4141 |
| 107 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +911 | 10970 |
| 108 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +910 | 3049 |
| 109 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +909 | 43973 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +892 | 23235 |
| 111 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +885 | 61818 |
| 112 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +866 | 14996 |
| 113 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +855 | 21811 |
| 114 | [docling-project/docling](https://github.com/docling-project/docling) | +832 | 54041 |
| 115 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +825 | 18071 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +784 | 8763 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +778 | 47122 |
| 118 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +777 | 11500 |
| 119 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +766 | 13837 |
| 120 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +763 | 8672 |
| 121 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +730 | 36799 |
| 122 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +711 | 30590 |
| 123 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +701 | 8887 |
| 124 | [wshobson/agents](https://github.com/wshobson/agents) | +680 | 29967 |
| 125 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +678 | 7098 |
| 126 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +666 | 31182 |
| 127 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +664 | 13192 |
| 128 | [google-research/timesfm](https://github.com/google-research/timesfm) | +630 | 9938 |
| 129 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +629 | 15273 |
| 130 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +613 | 3900 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +606 | 47936 |
| 132 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +600 | 2001 |
| 133 | [microsoft/qlib](https://github.com/microsoft/qlib) | +590 | 37792 |
| 134 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +585 | 17551 |
| 135 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +566 | 54903 |
| 136 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +546 | 3373 |
| 137 | [termux/termux-app](https://github.com/termux/termux-app) | +542 | 51073 |
| 138 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +531 | 39841 |
| 139 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +521 | 2084 |
| 140 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +518 | 4186 |
| 141 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +517 | 1402 |
| 142 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +512 | 15679 |
| 143 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +501 | 1081 |
| 144 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +490 | 1850 |
| 145 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +487 | 2468 |
| 146 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +481 | 7527 |
| 147 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +479 | 1567 |
| 148 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +479 | 1145 |
| 149 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +475 | 1835 |
| 150 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +462 | 4713 |
| 151 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +459 | 10085 |
| 152 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +456 | 44545 |
| 153 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +452 | 13897 |
| 154 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +451 | 3299 |
| 155 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +448 | 23995 |
| 156 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +447 | 1760 |
| 157 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +443 | 1397 |
| 158 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +441 | 1912 |
| 159 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +440 | 2995 |
| 160 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +430 | 11133 |
| 161 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +421 | 5979 |
| 162 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +414 | 36103 |
| 163 | [samugit83/redamon](https://github.com/samugit83/redamon) | +397 | 1377 |
| 164 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +397 | 10314 |
| 165 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +392 | 1195 |
| 166 | [openclaw/skills](https://github.com/openclaw/skills) | +388 | 1777 |
| 167 | [oraios/serena](https://github.com/oraios/serena) | +388 | 20885 |
| 168 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +386 | 5196 |
| 169 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +385 | 14242 |
| 170 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +385 | 2948 |
| 171 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +383 | 25406 |
| 172 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +381 | 6935 |
| 173 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +379 | 44232 |
| 174 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +377 | 6053 |
| 175 | [usestrix/strix](https://github.com/usestrix/strix) | +375 | 20680 |
| 176 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +374 | 1152 |
| 177 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +373 | 8702 |
| 178 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +372 | 14967 |
| 179 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +368 | 2134 |
| 180 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +356 | 12840 |
| 181 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +355 | 11003 |
| 182 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +348 | 23967 |
| 183 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +344 | 1194 |
| 184 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +343 | 36697 |
| 185 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +340 | 12515 |
| 186 | [eooce/python-ws](https://github.com/eooce/python-ws) | +339 | 1199 |
| 187 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +336 | 28888 |
| 188 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +336 | 8827 |
| 189 | [vnpy/vnpy](https://github.com/vnpy/vnpy) | +335 | 36870 |
| 190 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +329 | 1207 |
| 191 | [robinebers/openusage](https://github.com/robinebers/openusage) | +322 | 1121 |
| 192 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +321 | 893 |
| 193 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +321 | 23774 |
| 194 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +317 | 1115 |
| 195 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +317 | 1876 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +316 | 3904 |
| 197 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +311 | 20931 |
| 198 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +309 | 878 |
| 199 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +283 | 5391 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +281 | 9632 |
| 201 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +278 | 1305 |
| 202 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +278 | 1141 |
| 203 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +277 | 2384 |
| 204 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +268 | 3162 |
| 205 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +262 | 922 |
| 206 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +254 | 3303 |
| 207 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +251 | 845 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +247 | 41086 |
| 209 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +244 | 824 |
| 210 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +244 | 891 |
| 211 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +243 | 21090 |
| 212 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +237 | 1789 |
| 213 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +237 | 22490 |
| 214 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +229 | 12729 |
| 215 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +227 | 2408 |
| 216 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +225 | 6508 |
| 217 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 305 |
| 218 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +222 | 28526 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +215 | 40265 |
| 220 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +210 | 789 |
| 221 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 680 |
| 222 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +206 | 702 |
| 223 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +202 | 621 |
| 224 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +188 | 39596 |
| 225 | [VonChange/utao](https://github.com/VonChange/utao) | +187 | 3875 |
| 226 | [qist/tvbox](https://github.com/qist/tvbox) | +186 | 8321 |
| 227 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +185 | 568 |
| 228 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +183 | 664 |
| 229 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +182 | 666 |
| 230 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +181 | 29780 |
| 231 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +179 | 2237 |
| 232 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +173 | 524 |
| 233 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +173 | 11746 |
| 234 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +173 | 33000 |
| 235 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +172 | 3004 |
| 236 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +171 | 8310 |
| 237 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +169 | 571 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +168 | 1774 |
| 239 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +163 | 548 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +161 | 25720 |
| 241 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +159 | 2281 |
| 242 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +157 | 1237 |
| 243 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +154 | 13479 |
| 244 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +148 | 468 |
| 245 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +147 | 6874 |
| 246 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +147 | 488 |
| 247 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +146 | 37313 |
| 248 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +145 | 4778 |
| 249 | [apify/agent-skills](https://github.com/apify/agent-skills) | +144 | 631 |
| 250 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +143 | 4686 |
| 251 | [decolua/9router](https://github.com/decolua/9router) | +141 | 624 |
| 252 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +141 | 3073 |
| 253 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +141 | 774 |
| 254 | [bradygaster/squad](https://github.com/bradygaster/squad) | +140 | 554 |
| 255 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +138 | 556 |
| 256 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +133 | 459 |
| 257 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | +133 | 8442 |
| 258 | [expo/skills](https://github.com/expo/skills) | +131 | 1269 |
| 259 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +127 | 1306 |
| 260 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +126 | 940 |
| 261 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +125 | 638 |
| 262 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +124 | 3028 |
| 263 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +124 | 694 |
| 264 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +122 | 3225 |
| 265 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 266 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +121 | 9793 |
| 267 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 545 |
| 268 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 385 |
| 269 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +112 | 1057 |
| 270 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +108 | 3030 |
| 271 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +108 | 376 |
| 272 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +105 | 26722 |
| 273 | [microg/GmsCore](https://github.com/microg/GmsCore) | +104 | 12424 |
| 274 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +103 | 4490 |
| 275 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +101 | 35473 |
| 276 | [skylot/jadx](https://github.com/skylot/jadx) | +98 | 47365 |
| 277 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 10902 |
| 278 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +95 | 1503 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +92 | 8536 |
| 280 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +92 | 2841 |
| 281 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +91 | 326 |
| 282 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +84 | 292 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +83 | 1175 |
| 284 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +83 | 235 |
| 285 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +83 | 28639 |
| 286 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 288 |
| 287 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +79 | 21277 |
| 288 | [dataease/dataease](https://github.com/dataease/dataease) | +78 | 23490 |
| 289 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +77 | 759 |
| 290 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +77 | 257 |
| 291 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +77 | 685 |
| 292 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +76 | 835 |
| 293 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +76 | 12271 |
| 294 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +75 | 719 |
| 295 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1308 |
| 296 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +75 | 3425 |
| 297 | [openjdk/jdk](https://github.com/openjdk/jdk) | +75 | 22665 |
| 298 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +75 | 45263 |
| 299 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +75 | 5820 |
| 300 | [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | +75 | 23975 |
