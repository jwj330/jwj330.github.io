---
title: "2026-02-27 GitHub增长趋势报告"
description: "1.clawdbot+1145 2.financial-services-plugins+478 3.awesome-openclaw-usecases+407 4.GitNexus+402 5.Scrapling+335"
date: 2026-02-27T20:30:43+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-27 20:30:43

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
        'daily': {"categories": ["moonshine-ai/moonshine", "vercel-labs/agent-browser", "qwibitai/nanoclaw", "clockworklabs/SpacetimeDB", "HKUDS/nanobot", "glittercowboy/get-shit-done", "VectifyAI/PageIndex", "zeroclaw-labs/zeroclaw", "bytedance/deer-flow", "farion1231/cc-switch", "muratcankoylan/Agent-Skills-for-Context-Engineering", "koala73/worldmonitor", "VoltAgent/awesome-openclaw-skills", "affaan-m/everything-claude-code", "zarazhangrui/frontend-slides", "D4Vinci/Scrapling", "abhigyanpatwari/GitNexus", "hesamsheikh/awesome-openclaw-usecases", "anthropics/financial-services-plugins", "clawdbot/clawdbot"], "data": [154, 158, 162, 163, 181, 184, 186, 191, 198, 200, 219, 220, 237, 260, 302, 335, 402, 407, 478, 1145]},
        'weekly': {"categories": ["HKUDS/nanobot", "sipeed/picoclaw", "VoltAgent/awesome-openclaw-skills", "zarazhangrui/frontend-slides", "glittercowboy/get-shit-done", "anomalyco/opencode", "affaan-m/everything-claude-code", "jamiepine/voicebox", "abhigyanpatwari/GitNexus", "zeroclaw-labs/zeroclaw", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "huggingface/skills", "qwibitai/nanoclaw", "koala73/worldmonitor", "vxcontrol/pentagi", "D4Vinci/Scrapling", "obra/superpowers", "x1xhlol/system-prompts-and-models-of-ai-tools", "clawdbot/clawdbot"], "data": [1167, 1177, 1238, 1276, 1307, 1363, 1414, 1420, 1437, 1492, 1573, 1681, 1685, 1893, 2003, 2013, 2041, 2334, 2976, 6764]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "sickn33/antigravity-awesome-skills", "ComposioHQ/awesome-claude-skills", "daytonaio/daytona", "glittercowboy/get-shit-done", "x1xhlol/system-prompts-and-models-of-ai-tools", "koala73/worldmonitor", "badlogic/pi-mono", "qwibitai/nanoclaw", "thedotmack/claude-mem", "VoltAgent/awesome-openclaw-skills", "zeroclaw-labs/zeroclaw", "sipeed/picoclaw", "affaan-m/everything-claude-code", "KeygraphHQ/shannon", "anthropics/skills", "anomalyco/opencode", "HKUDS/nanobot", "obra/superpowers", "clawdbot/clawdbot"], "data": [3430, 3506, 3625, 3692, 3751, 4290, 4530, 4558, 4744, 4912, 6128, 6237, 6395, 6772, 6940, 7073, 7130, 7817, 7922, 56789]}
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
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +1145 | 224760 |
| 2 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +478 | 3952 |
| 3 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +407 | 11098 |
| 4 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +402 | 6137 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +335 | 17893 |
| 6 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +302 | 6526 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +260 | 51199 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +237 | 21846 |
| 9 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +220 | 16780 |
| 10 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +219 | 12301 |
| 11 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +200 | 21256 |
| 12 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +198 | 21758 |
| 13 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +191 | 20419 |
| 14 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +186 | 18931 |
| 15 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +184 | 21585 |
| 16 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +181 | 26340 |
| 17 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +163 | 21340 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +162 | 15894 |
| 19 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +158 | 16453 |
| 20 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +154 | 5761 |
| 21 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +150 | 33878 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +146 | 17595 |
| 23 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +144 | 1401 |
| 24 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +144 | 20776 |
| 25 | [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) | +139 | 15464 |
| 26 | [huggingface/skills](https://github.com/huggingface/skills) | +132 | 7284 |
| 27 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +129 | 19023 |
| 28 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +125 | 16521 |
| 29 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +122 | 1691 |
| 30 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +116 | 1870 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +6764 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2976 | 122870 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2334 | 60312 |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2041 | 17893 |
| 5 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2013 | 8416 |
| 6 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2003 | 16781 |
| 7 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1893 | 15894 |
| 8 | [huggingface/skills](https://github.com/huggingface/skills) | +1685 | 7284 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +1681 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1573 | 11098 |
| 11 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1492 | 20419 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1437 | 6137 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1420 | 11334 |
| 14 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1414 | 51199 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1363 | 109881 |
| 16 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +1307 | 21585 |
| 17 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1276 | 6526 |
| 18 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1238 | 21846 |
| 19 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1177 | 20776 |
| 20 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1167 | 26340 |
| 21 | [alibaba/zvec](https://github.com/alibaba/zvec) | +943 | 8178 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +926 | 17595 |
| 23 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +916 | 12301 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +876 | 69674 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +827 | 16521 |
| 26 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +788 | 3952 |
| 27 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +768 | 18931 |
| 28 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +752 | 2672 |
| 29 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +723 | 60117 |
| 30 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +722 | 33878 |
| 31 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +707 | 5593 |
| 32 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +630 | 37330 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +629 | 34148 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +601 | 21256 |
| 35 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +595 | 30678 |
| 36 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +564 | 3368 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +547 | 14044 |
| 38 | [blader/humanizer](https://github.com/blader/humanizer) | +521 | 7062 |
| 39 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +520 | 37564 |
| 40 | [tw93/Mole](https://github.com/tw93/Mole) | +513 | 36870 |
| 41 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +505 | 2862 |
| 42 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +498 | 5701 |
| 43 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +487 | 2603 |
| 44 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +479 | 4980 |
| 45 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +468 | 7307 |
| 46 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +446 | 5668 |
| 47 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +443 | 25567 |
| 48 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +441 | 21340 |
| 49 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +434 | 16453 |
| 50 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +433 | 22969 |
| 51 | [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | +432 | 18855 |
| 52 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +429 | 11189 |
| 53 | [IgorShadurin/app.yumcut.com](https://github.com/IgorShadurin/app.yumcut.com) | +429 | 865 |
| 54 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +427 | 7981 |
| 55 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +406 | 26264 |
| 56 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +396 | 19023 |
| 57 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +387 | 21758 |
| 58 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +387 | 18227 |
| 59 | [tobi/qmd](https://github.com/tobi/qmd) | +383 | 10852 |
| 60 | [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | +383 | 23103 |
| 61 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +380 | 10111 |
| 62 | [google-research/timesfm](https://github.com/google-research/timesfm) | +375 | 9883 |
| 63 | [cloudflare/agents](https://github.com/cloudflare/agents) | +364 | 4334 |
| 64 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +360 | 3765 |
| 65 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +358 | 1439 |
| 66 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +358 | 1362 |
| 67 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +357 | 3126 |
| 68 | [ronitsingh10/FineTune](https://github.com/ronitsingh10/FineTune) | +350 | 3764 |
| 69 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +347 | 5761 |
| 70 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +341 | 1870 |
| 71 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +337 | 2783 |
| 72 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +335 | 8251 |
| 73 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +330 | 9820 |
| 74 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +326 | 1450 |
| 75 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +323 | 8222 |
| 76 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +319 | 2815 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +316 | 9736 |
| 78 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +312 | 12816 |
| 79 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +311 | 4150 |
| 80 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +303 | 11425 |
| 81 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +293 | 32872 |
| 82 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +289 | 4177 |
| 83 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +285 | 47122 |
| 84 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +285 | 11312 |
| 85 | [slopus/happy](https://github.com/slopus/happy) | +282 | 13755 |
| 86 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +278 | 5799 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +274 | 12027 |
| 88 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +273 | 25390 |
| 89 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +271 | 1253 |
| 90 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +269 | 24627 |
| 91 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +268 | 1481 |
| 92 | [ruvnet/claude-flow](https://github.com/ruvnet/claude-flow) | +259 | 15464 |
| 93 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +259 | 22854 |
| 94 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +257 | 7286 |
| 95 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +254 | 7662 |
| 96 | [openai/skills](https://github.com/openai/skills) | +251 | 10041 |
| 97 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +247 | 7301 |
| 98 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +247 | 11064 |
| 99 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +243 | 8543 |
| 100 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +242 | 8508 |
| 101 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +241 | 1401 |
| 102 | [olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer) | +222 | 828 |
| 103 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +215 | 1752 |
| 104 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +207 | 2327 |
| 105 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +196 | 36799 |
| 106 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +189 | 8719 |
| 107 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +187 | 2349 |
| 108 | [google/langextract](https://github.com/google/langextract) | +184 | 33636 |
| 109 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +179 | 2804 |
| 110 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +178 | 30590 |
| 111 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +178 | 6762 |
| 112 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +174 | 12890 |
| 113 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +170 | 14731 |
| 114 | [samugit83/redamon](https://github.com/samugit83/redamon) | +167 | 1297 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +166 | 29561 |
| 116 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +165 | 15517 |
| 117 | [usestrix/strix](https://github.com/usestrix/strix) | +163 | 20616 |
| 118 | [aden-hive/hive](https://github.com/aden-hive/hive) | +159 | 8463 |
| 119 | [shuaiplus/NodeWarden](https://github.com/shuaiplus/NodeWarden) | +158 | 868 |
| 120 | [whyzhow/Kaggle-NeurIPS---Open-Polymer-Prediction-2025-Silver-Algorithm-Overview](https://github.com/whyzhow/Kaggle-NeurIPS---Open-Polymer-Prediction-2025-Silver-Algorithm-Overview) | +148 | 775 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +56789 | 224760 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +7922 | 60312 |
| 3 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7817 | 26340 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +7130 | 109881 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +7073 | 74774 |
| 6 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +6940 | 25567 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6772 | 51199 |
| 8 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6395 | 20776 |
| 9 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6237 | 20419 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +6128 | 21846 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4912 | 30678 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4744 | 15894 |
| 13 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4558 | 17595 |
| 14 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +4530 | 16781 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4290 | 122870 |
| 16 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +3751 | 21585 |
| 17 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3692 | 60117 |
| 18 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3625 | 37330 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3506 | 16521 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3430 | 34148 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3255 | 11334 |
| 22 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +3187 | 33878 |
| 23 | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | +3023 | 9258 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3022 | 69674 |
| 25 | [google/langextract](https://github.com/google/langextract) | +3005 | 33636 |
| 26 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2961 | 11099 |
| 27 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2676 | 85286 |
| 28 | [openai/skills](https://github.com/openai/skills) | +2575 | 10041 |
| 29 | [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) | +2573 | 7880 |
| 30 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2559 | 18931 |
| 31 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2549 | 8178 |
| 32 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2498 | 14044 |
| 33 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2468 | 8170 |
| 34 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2411 | 96919 |
| 35 | [virattt/dexter](https://github.com/virattt/dexter) | +2409 | 16651 |
| 36 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +2398 | 32872 |
| 37 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2390 | 8416 |
| 38 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2345 | 7981 |
| 39 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2251 | 6975 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2215 | 21256 |
| 41 | [tobi/qmd](https://github.com/tobi/qmd) | +2209 | 10852 |
| 42 | [github/spec-kit](https://github.com/github/spec-kit) | +2190 | 71722 |
| 43 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2119 | 17893 |
| 44 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +2090 | 149018 |
| 45 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1996 | 8463 |
| 46 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1988 | 24627 |
| 47 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1918 | 26264 |
| 48 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1893 | 37564 |
| 49 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1877 | 17252 |
| 50 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1866 | 11189 |
| 51 | [pydantic/monty](https://github.com/pydantic/monty) | +1844 | 5738 |
| 52 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1841 | 6440 |
| 53 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1808 | 9021 |
| 54 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1766 | 37810 |
| 55 | [huggingface/skills](https://github.com/huggingface/skills) | +1746 | 7284 |
| 56 | [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | +1738 | 10976 |
| 57 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1723 | 10111 |
| 58 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1722 | 9820 |
| 59 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1617 | 5593 |
| 60 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1603 | 5668 |
| 61 | [tw93/Mole](https://github.com/tw93/Mole) | +1601 | 36870 |
| 62 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1600 | 16453 |
| 63 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1568 | 6526 |
| 64 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1556 | 5701 |
| 65 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1539 | 6137 |
| 66 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1535 | 7662 |
| 67 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1532 | 98536 |
| 68 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1506 | 8251 |
| 69 | [openai/codex](https://github.com/openai/codex) | +1487 | 61744 |
| 70 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1486 | 33712 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1471 | 9736 |
| 72 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1459 | 8850 |
| 73 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1439 | 4980 |
| 74 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1421 | 5109 |
| 75 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1418 | 26920 |
| 76 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1410 | 7301 |
| 77 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1402 | 21433 |
| 78 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1380 | 22969 |
| 79 | [slopus/happy](https://github.com/slopus/happy) | +1351 | 13755 |
| 80 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1340 | 12816 |
| 81 | [steveyegge/beads](https://github.com/steveyegge/beads) | +1329 | 17509 |
| 82 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1295 | 74887 |
| 83 | [steveyegge/gastown](https://github.com/steveyegge/gastown) | +1293 | 10493 |
| 84 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1283 | 7307 |
| 85 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1254 | 4150 |
| 86 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +1248 | 8543 |
| 87 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1203 | 3805 |
| 88 | [steipete/summarize](https://github.com/steipete/summarize) | +1185 | 4551 |
| 89 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1165 | 4177 |
| 90 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +1161 | 3673 |
| 91 | [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | +1146 | 22297 |
| 92 | [knadh/oat](https://github.com/knadh/oat) | +1144 | 3932 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1136 | 12027 |
| 94 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +1124 | 11312 |
| 95 | [blader/humanizer](https://github.com/blader/humanizer) | +1120 | 7062 |
| 96 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +1108 | 15209 |
| 97 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +1102 | 95547 |
| 98 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1099 | 3765 |
| 99 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1086 | 3805 |
| 100 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1085 | 8508 |
| 101 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1073 | 12301 |
| 102 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +1052 | 8719 |
| 103 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1044 | 21112 |
| 104 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +1044 | 11350 |
| 105 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1007 | 43973 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1004 | 25390 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +998 | 22854 |
| 108 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +975 | 3368 |
| 109 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +958 | 14731 |
| 110 | [docling-project/docling](https://github.com/docling-project/docling) | +954 | 54041 |
| 111 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +950 | 21441 |
| 112 | [Robbyant/lingbot-world](https://github.com/Robbyant/lingbot-world) | +950 | 2997 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +942 | 61818 |
| 114 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +925 | 18227 |
| 115 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +925 | 28632 |
| 116 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +903 | 47122 |
| 117 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +894 | 13636 |
| 118 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +888 | 6875 |
| 119 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +861 | 2804 |
| 120 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +855 | 71118 |
| 121 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +853 | 6762 |
| 122 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +835 | 17929 |
| 123 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +833 | 8222 |
| 124 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +806 | 71086 |
| 125 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +772 | 3952 |
| 126 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +768 | 2247 |
| 127 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +752 | 3171 |
| 128 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +746 | 54903 |
| 129 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +739 | 30590 |
| 130 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +737 | 36799 |
| 131 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +737 | 12890 |
| 132 | [wshobson/agents](https://github.com/wshobson/agents) | +729 | 29561 |
| 133 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +686 | 8869 |
| 134 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +686 | 31182 |
| 135 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +675 | 9440 |
| 136 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +661 | 4034 |
| 137 | [termux/termux-app](https://github.com/termux/termux-app) | +637 | 51073 |
| 138 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +624 | 47936 |
| 139 | [google-research/timesfm](https://github.com/google-research/timesfm) | +619 | 9883 |
| 140 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +619 | 58595 |
| 141 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +615 | 14186 |
| 142 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +608 | 39841 |
| 143 | [microsoft/qlib](https://github.com/microsoft/qlib) | +607 | 37792 |
| 144 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +602 | 9944 |
| 145 | [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | +595 | 2397 |
| 146 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +589 | 17514 |
| 147 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +589 | 1891 |
| 148 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +556 | 52081 |
| 149 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +553 | 3322 |
| 150 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +551 | 5553 |
| 151 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +539 | 52700 |
| 152 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +536 | 2349 |
| 153 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +528 | 1714 |
| 154 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +520 | 2001 |
| 155 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +514 | 3059 |
| 156 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +512 | 1392 |
| 157 | [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | +505 | 1723 |
| 158 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +503 | 3227 |
| 159 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +502 | 15517 |
| 160 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +483 | 44545 |
| 161 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +478 | 1134 |
| 162 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +474 | 4522 |
| 163 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +470 | 36103 |
| 164 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +467 | 1752 |
| 165 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +465 | 1800 |
| 166 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +461 | 13820 |
| 167 | [oraios/serena](https://github.com/oraios/serena) | +460 | 20740 |
| 168 | [openclaw/skills](https://github.com/openclaw/skills) | +450 | 1601 |
| 169 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +441 | 1450 |
| 170 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +438 | 2494 |
| 171 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +438 | 23949 |
| 172 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +434 | 7286 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +433 | 5018 |
| 174 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +432 | 1362 |
| 175 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +432 | 25215 |
| 176 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +429 | 11064 |
| 177 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +422 | 864 |
| 178 | [exo-explore/exo](https://github.com/exo-explore/exo) | +421 | 41758 |
| 179 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +418 | 2820 |
| 180 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +413 | 12391 |
| 181 | [usestrix/strix](https://github.com/usestrix/strix) | +408 | 20616 |
| 182 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +401 | 3257 |
| 183 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +386 | 5942 |
| 184 | [samugit83/redamon](https://github.com/samugit83/redamon) | +374 | 1297 |
| 185 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +373 | 44232 |
| 186 | [vnpy/vnpy](https://github.com/vnpy/vnpy) | +371 | 36870 |
| 187 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +371 | 10233 |
| 188 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +370 | 20844 |
| 189 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +368 | 23822 |
| 190 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +368 | 8644 |
| 191 | [scaledown-team/scaledown](https://github.com/scaledown-team/scaledown) | +365 | 897 |
| 192 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +365 | 14881 |
| 193 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +361 | 1749 |
| 194 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +357 | 5793 |
| 195 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +349 | 1060 |
| 196 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +346 | 36697 |
| 197 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +342 | 23634 |
| 198 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +339 | 3822 |
| 199 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +338 | 10743 |
| 200 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +327 | 1904 |
| 201 | [maxritter/claude-codepro](https://github.com/maxritter/claude-codepro) | +326 | 1449 |
| 202 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +324 | 1450 |
| 203 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +312 | 5363 |
| 204 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +310 | 849 |
| 205 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +308 | 9528 |
| 206 | [robinebers/openusage](https://github.com/robinebers/openusage) | +305 | 1066 |
| 207 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +303 | 8511 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +293 | 41086 |
| 209 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +288 | 37313 |
| 210 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +286 | 22421 |
| 211 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +281 | 20980 |
| 212 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +274 | 864 |
| 213 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +264 | 1073 |
| 214 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +262 | 12651 |
| 215 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +260 | 6418 |
| 216 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +256 | 2867 |
| 217 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +248 | 2270 |
| 218 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +246 | 2392 |
| 219 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +240 | 850 |
| 220 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +239 | 11692 |
| 221 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +236 | 791 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +236 | 28449 |
| 223 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +235 | 40265 |
| 224 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +235 | 39596 |
| 225 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 318 |
| 226 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +223 | 2949 |
| 227 | [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | +216 | 21277 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +215 | 3865 |
| 229 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +209 | 781 |
| 230 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +208 | 29780 |
| 231 | [qist/tvbox](https://github.com/qist/tvbox) | +203 | 8290 |
| 232 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +200 | 742 |
| 233 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +196 | 605 |
| 234 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +194 | 674 |
| 235 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +191 | 639 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +189 | 33000 |
| 237 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +188 | 1691 |
| 238 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +187 | 8287 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +185 | 25678 |
| 240 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +175 | 1711 |
| 241 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +174 | 633 |
| 242 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +173 | 2223 |
| 243 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +167 | 630 |
| 244 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | +166 | 8397 |
| 245 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +164 | 28633 |
| 246 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +163 | 557 |
| 247 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +162 | 483 |
| 248 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +162 | 464 |
| 249 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +161 | 13450 |
| 250 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +160 | 6829 |
| 251 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +158 | 4724 |
| 252 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +155 | 1220 |
| 253 | [imxv/Pretty-mermaid-skills](https://github.com/imxv/Pretty-mermaid-skills) | +152 | 503 |
| 254 | [expo/skills](https://github.com/expo/skills) | +149 | 1221 |
| 255 | [SeanWong17/Future-Style-Periodic-Table](https://github.com/SeanWong17/Future-Style-Periodic-Table) | +146 | 442 |
| 256 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +145 | 48784 |
| 257 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +141 | 1247 |
| 258 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +141 | 471 |
| 259 | [decolua/9router](https://github.com/decolua/9router) | +137 | 568 |
| 260 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +136 | 418 |
| 261 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +136 | 3210 |
| 262 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +136 | 988 |
| 263 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +135 | 9760 |
| 264 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +133 | 538 |
| 265 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +133 | 654 |
| 266 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +129 | 2971 |
| 267 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +128 | 1016 |
| 268 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +121 | 26692 |
| 269 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 542 |
| 270 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +118 | 4463 |
| 271 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +117 | 885 |
| 272 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +115 | 380 |
| 273 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +112 | 8489 |
| 274 | [skylot/jadx](https://github.com/skylot/jadx) | +112 | 47365 |
| 275 | [microg/GmsCore](https://github.com/microg/GmsCore) | +110 | 12394 |
| 276 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +107 | 4470 |
| 277 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +106 | 3011 |
| 278 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +105 | 396 |
| 279 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +105 | 360 |
| 280 | [bradygaster/squad](https://github.com/bradygaster/squad) | +103 | 450 |
| 281 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +102 | 35473 |
| 282 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +100 | 685 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +100 | 10859 |
| 284 | [iBUHub/AIStudioToAPI](https://github.com/iBUHub/AIStudioToAPI) | +99 | 623 |
| 285 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +98 | 1433 |
| 286 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +97 | 2797 |
| 287 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +95 | 28619 |
| 288 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +91 | 1153 |
| 289 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +88 | 12238 |
| 290 | [FongMi/TV](https://github.com/FongMi/TV) | +86 | 7450 |
| 291 | [eooce/node-ws](https://github.com/eooce/node-ws) | +84 | 5689 |
| 292 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +83 | 231 |
| 293 | [suyunkai/EVCam](https://github.com/suyunkai/EVCam) | +83 | 278 |
| 294 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +82 | 791 |
| 295 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +82 | 5804 |
| 296 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +81 | 236 |
| 297 | [xlrpa/FlowBot](https://github.com/xlrpa/FlowBot) | +81 | 899 |
| 298 | [dataease/dataease](https://github.com/dataease/dataease) | +81 | 23467 |
| 299 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +80 | 1302 |
| 300 | [apache/kafka](https://github.com/apache/kafka) | +80 | 32043 |
