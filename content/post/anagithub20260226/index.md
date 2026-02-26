---
title: "2026-02-26 GitHub增长趋势报告"
description: "1.clawdbot+1196 2.Scrapling+708 3.frontend-slides+444 4.awesome-openclaw-usecases+394 5.GitNexus+313"
date: 2026-02-26T20:40:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-26 20:40:49

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
        'daily': {"categories": ["VectifyAI/PageIndex", "bytedance/deer-flow", "glittercowboy/get-shit-done", "qwibitai/nanoclaw", "badlogic/pi-mono", "HKUDS/nanobot", "zeroclaw-labs/zeroclaw", "peteromallet/dataclaw", "datawhalechina/hello-agents", "huggingface/skills", "VoltAgent/awesome-openclaw-skills", "ComposioHQ/agent-orchestrator", "muratcankoylan/Agent-Skills-for-Context-Engineering", "koala73/worldmonitor", "affaan-m/everything-claude-code", "abhigyanpatwari/GitNexus", "hesamsheikh/awesome-openclaw-usecases", "zarazhangrui/frontend-slides", "D4Vinci/Scrapling", "clawdbot/clawdbot"], "data": [144, 156, 166, 166, 168, 175, 176, 194, 196, 204, 212, 266, 275, 281, 291, 313, 394, 444, 708, 1196]},
        'weekly': {"categories": ["zarazhangrui/frontend-slides", "VoltAgent/awesome-openclaw-skills", "abhigyanpatwari/GitNexus", "HKUDS/nanobot", "sipeed/picoclaw", "glittercowboy/get-shit-done", "hesamsheikh/awesome-openclaw-usecases", "anomalyco/opencode", "affaan-m/everything-claude-code", "anthropics/skills", "huggingface/skills", "zeroclaw-labs/zeroclaw", "D4Vinci/Scrapling", "qwibitai/nanoclaw", "koala73/worldmonitor", "jamiepine/voicebox", "obra/superpowers", "vxcontrol/pentagi", "x1xhlol/system-prompts-and-models-of-ai-tools", "clawdbot/clawdbot"], "data": [1006, 1090, 1102, 1120, 1205, 1230, 1256, 1267, 1299, 1457, 1571, 1614, 1759, 1817, 1955, 1971, 2171, 2187, 2801, 6550]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "sickn33/antigravity-awesome-skills", "daytonaio/daytona", "ComposioHQ/awesome-claude-skills", "glittercowboy/get-shit-done", "x1xhlol/system-prompts-and-models-of-ai-tools", "koala73/worldmonitor", "badlogic/pi-mono", "qwibitai/nanoclaw", "thedotmack/claude-mem", "zeroclaw-labs/zeroclaw", "VoltAgent/awesome-openclaw-skills", "sipeed/picoclaw", "KeygraphHQ/shannon", "affaan-m/everything-claude-code", "anthropics/skills", "anomalyco/opencode", "HKUDS/nanobot", "obra/superpowers", "clawdbot/clawdbot"], "data": [3508, 3551, 3681, 3700, 3703, 4137, 4327, 4468, 4605, 4867, 6061, 6139, 6263, 6889, 7029, 7145, 7284, 7650, 7820, 63712]}
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
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +1196 | 224760 |
| 2 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +708 | 16709 |
| 3 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +444 | 5590 |
| 4 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +394 | 9560 |
| 5 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +313 | 5013 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +291 | 51199 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +281 | 16157 |
| 8 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +275 | 11620 |
| 9 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +266 | 2596 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +212 | 20875 |
| 11 | [huggingface/skills](https://github.com/huggingface/skills) | +204 | 6920 |
| 12 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +196 | 22603 |
| 13 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +194 | 1283 |
| 14 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +176 | 19801 |
| 15 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +175 | 25723 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +168 | 17072 |
| 17 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +166 | 15263 |
| 18 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +166 | 20871 |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +156 | 21033 |
| 20 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +144 | 18306 |
| 21 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +137 | 8035 |
| 22 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +136 | 2278 |
| 23 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +125 | 20346 |
| 24 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +123 | 13759 |
| 25 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +122 | 7609 |
| 26 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +113 | 15979 |
| 27 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +112 | 33878 |
| 28 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +111 | 1529 |
| 29 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +110 | 11055 |
| 30 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +108 | 37330 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +6550 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2801 | 122870 |
| 3 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2187 | 8310 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +2171 | 60312 |
| 5 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1971 | 11210 |
| 6 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1955 | 16157 |
| 7 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1817 | 15263 |
| 8 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1759 | 16709 |
| 9 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1614 | 19801 |
| 10 | [huggingface/skills](https://github.com/huggingface/skills) | +1571 | 6920 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1457 | 74774 |
| 12 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1299 | 51199 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1267 | 109881 |
| 14 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1256 | 9560 |
| 15 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +1230 | 20871 |
| 16 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1205 | 20346 |
| 17 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1120 | 25723 |
| 18 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1102 | 5013 |
| 19 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1090 | 20875 |
| 20 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1006 | 5591 |
| 21 | [alibaba/zvec](https://github.com/alibaba/zvec) | +964 | 8049 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +897 | 17072 |
| 23 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +831 | 69674 |
| 24 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +821 | 15979 |
| 25 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +778 | 60117 |
| 26 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +761 | 5630 |
| 27 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +721 | 2596 |
| 28 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +713 | 11620 |
| 29 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +688 | 3263 |
| 30 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +673 | 2663 |
| 31 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +673 | 4887 |
| 32 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +644 | 33878 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +626 | 5041 |
| 34 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +618 | 18306 |
| 35 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +600 | 37330 |
| 36 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +600 | 30678 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +597 | 34148 |
| 38 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +550 | 2418 |
| 39 | [blader/humanizer](https://github.com/blader/humanizer) | +537 | 6882 |
| 40 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +531 | 7151 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +527 | 13759 |
| 42 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +520 | 5588 |
| 43 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +503 | 37564 |
| 44 | [tw93/Mole](https://github.com/tw93/Mole) | +503 | 36870 |
| 45 | [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | +481 | 23085 |
| 46 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +463 | 25322 |
| 47 | [google-research/timesfm](https://github.com/google-research/timesfm) | +457 | 9829 |
| 48 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +454 | 20597 |
| 49 | [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | +434 | 18797 |
| 50 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +427 | 9739 |
| 51 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +420 | 1340 |
| 52 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +417 | 10075 |
| 53 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +415 | 11055 |
| 54 | [IgorShadurin/app.yumcut.com](https://github.com/IgorShadurin/app.yumcut.com) | +400 | 805 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +399 | 18086 |
| 56 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +387 | 2587 |
| 57 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +384 | 2657 |
| 58 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +378 | 26000 |
| 59 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +371 | 11037 |
| 60 | [tobi/qmd](https://github.com/tobi/qmd) | +365 | 10699 |
| 61 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +361 | 3014 |
| 62 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +360 | 8071 |
| 63 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +358 | 7609 |
| 64 | [cloudflare/agents](https://github.com/cloudflare/agents) | +356 | 4282 |
| 65 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +351 | 3599 |
| 66 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +350 | 18686 |
| 67 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +346 | 22603 |
| 68 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +343 | 21027 |
| 69 | [ronitsingh10/FineTune](https://github.com/ronitsingh10/FineTune) | +341 | 3724 |
| 70 | [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) | +325 | 1942 |
| 71 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +324 | 10172 |
| 72 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +321 | 1343 |
| 73 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +321 | 8794 |
| 74 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +318 | 2279 |
| 75 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +316 | 9543 |
| 76 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +316 | 4019 |
| 77 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +313 | 16002 |
| 78 | [slopus/happy](https://github.com/slopus/happy) | +311 | 13652 |
| 79 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +304 | 8990 |
| 80 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +303 | 32872 |
| 81 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +294 | 4100 |
| 82 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +294 | 1686 |
| 83 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +282 | 12672 |
| 84 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +281 | 8035 |
| 85 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +281 | 20787 |
| 86 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +272 | 11171 |
| 87 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +269 | 25244 |
| 88 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +264 | 1283 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +261 | 11823 |
| 90 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +257 | 47122 |
| 91 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +254 | 22706 |
| 92 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +250 | 1355 |
| 93 | [openai/skills](https://github.com/openai/skills) | +247 | 9911 |
| 94 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +243 | 1176 |
| 95 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +241 | 7209 |
| 96 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +240 | 5779 |
| 97 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +237 | 11179 |
| 98 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +235 | 1529 |
| 99 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +234 | 5619 |
| 100 | [olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer) | +234 | 811 |
| 101 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +229 | 8422 |
| 102 | [virattt/dexter](https://github.com/virattt/dexter) | +224 | 16569 |
| 103 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +210 | 21033 |
| 104 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +194 | 2293 |
| 105 | [google/langextract](https://github.com/google/langextract) | +193 | 33636 |
| 106 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +189 | 36799 |
| 107 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +188 | 8632 |
| 108 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +177 | 6731 |
| 109 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +174 | 2294 |
| 110 | [aden-hive/hive](https://github.com/aden-hive/hive) | +172 | 8431 |
| 111 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +169 | 3776 |
| 112 | [samugit83/redamon](https://github.com/samugit83/redamon) | +166 | 1277 |
| 113 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +165 | 2754 |
| 114 | [usestrix/strix](https://github.com/usestrix/strix) | +165 | 20593 |
| 115 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +164 | 12792 |
| 116 | [shuaiplus/NodeWarden](https://github.com/shuaiplus/NodeWarden) | +163 | 818 |
| 117 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +162 | 30590 |
| 118 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +162 | 15469 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +160 | 14647 |
| 120 | [wshobson/agents](https://github.com/wshobson/agents) | +153 | 29467 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +63712 | 224760 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +7820 | 60312 |
| 3 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7650 | 25723 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +7284 | 109881 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +7145 | 74774 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7029 | 51199 |
| 7 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +6889 | 25322 |
| 8 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6263 | 20346 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +6139 | 20875 |
| 10 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6061 | 19801 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4867 | 30678 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4605 | 15263 |
| 13 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4468 | 17072 |
| 14 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +4327 | 16157 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4137 | 122870 |
| 16 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +3703 | 20871 |
| 17 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3700 | 37330 |
| 18 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3681 | 60117 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3551 | 15979 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3508 | 34148 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3234 | 11210 |
| 22 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +3206 | 33878 |
| 23 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3033 | 69674 |
| 24 | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | +3011 | 9236 |
| 25 | [google/langextract](https://github.com/google/langextract) | +2984 | 33636 |
| 26 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2658 | 85286 |
| 27 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2581 | 9560 |
| 28 | [openai/skills](https://github.com/openai/skills) | +2564 | 9911 |
| 29 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2559 | 13759 |
| 30 | [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) | +2553 | 7811 |
| 31 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2548 | 18306 |
| 32 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2514 | 8049 |
| 33 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2444 | 96919 |
| 34 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2434 | 8069 |
| 35 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +2414 | 32872 |
| 36 | [virattt/dexter](https://github.com/virattt/dexter) | +2406 | 16569 |
| 37 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2364 | 8310 |
| 38 | [tobi/qmd](https://github.com/tobi/qmd) | +2285 | 10699 |
| 39 | [aden-hive/hive](https://github.com/aden-hive/hive) | +2253 | 8431 |
| 40 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2251 | 7609 |
| 41 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2234 | 6938 |
| 42 | [github/spec-kit](https://github.com/github/spec-kit) | +2194 | 71722 |
| 43 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +2131 | 149018 |
| 44 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2089 | 20597 |
| 45 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2083 | 37810 |
| 46 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +2057 | 24458 |
| 47 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1947 | 17158 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1921 | 26000 |
| 49 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1908 | 37564 |
| 50 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1845 | 11055 |
| 51 | [pydantic/monty](https://github.com/pydantic/monty) | +1838 | 5714 |
| 52 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1833 | 16709 |
| 53 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1825 | 6403 |
| 54 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1809 | 8990 |
| 55 | [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | +1786 | 10964 |
| 56 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +1775 | 176173 |
| 57 | [lucasgelfond/zerobrew](https://github.com/lucasgelfond/zerobrew) | +1749 | 6536 |
| 58 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1730 | 10075 |
| 59 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1707 | 9739 |
| 60 | [huggingface/skills](https://github.com/huggingface/skills) | +1629 | 6920 |
| 61 | [tw93/Mole](https://github.com/tw93/Mole) | +1611 | 36870 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1580 | 5588 |
| 63 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1564 | 7525 |
| 64 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1533 | 5630 |
| 65 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1532 | 8071 |
| 66 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1529 | 16003 |
| 67 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1519 | 98536 |
| 68 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1512 | 5041 |
| 69 | [openai/codex](https://github.com/openai/codex) | +1484 | 61744 |
| 70 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1480 | 21315 |
| 71 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1476 | 33712 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1468 | 9543 |
| 73 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1445 | 8794 |
| 74 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1431 | 7120 |
| 75 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1417 | 5038 |
| 76 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1409 | 26802 |
| 77 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1408 | 4887 |
| 78 | [slopus/happy](https://github.com/slopus/happy) | +1381 | 13652 |
| 79 | [steveyegge/beads](https://github.com/steveyegge/beads) | +1366 | 17397 |
| 80 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1336 | 22603 |
| 81 | [steveyegge/gastown](https://github.com/steveyegge/gastown) | +1314 | 10398 |
| 82 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1302 | 12672 |
| 83 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1292 | 5591 |
| 84 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1284 | 74887 |
| 85 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1246 | 7151 |
| 86 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +1224 | 8348 |
| 87 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1215 | 4019 |
| 88 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1203 | 3792 |
| 89 | [steipete/summarize](https://github.com/steipete/summarize) | +1189 | 4485 |
| 90 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +1183 | 8632 |
| 91 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1162 | 5013 |
| 92 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +1155 | 3618 |
| 93 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1140 | 4100 |
| 94 | [blader/humanizer](https://github.com/blader/humanizer) | +1137 | 6882 |
| 95 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1133 | 11823 |
| 96 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +1129 | 11171 |
| 97 | [knadh/oat](https://github.com/knadh/oat) | +1121 | 3848 |
| 98 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +1108 | 95547 |
| 99 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +1105 | 15192 |
| 100 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +1091 | 11300 |
| 101 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1088 | 3776 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1082 | 8422 |
| 103 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1064 | 3599 |
| 104 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1039 | 21027 |
| 105 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1015 | 43973 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1012 | 25244 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +1001 | 22706 |
| 108 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +984 | 14647 |
| 109 | [docling-project/docling](https://github.com/docling-project/docling) | +965 | 54041 |
| 110 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +962 | 21374 |
| 111 | [Robbyant/lingbot-world](https://github.com/Robbyant/lingbot-world) | +946 | 2989 |
| 112 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +940 | 3263 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +940 | 61818 |
| 114 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +925 | 28619 |
| 115 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +920 | 13519 |
| 116 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +900 | 47122 |
| 117 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +891 | 18086 |
| 118 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +890 | 6832 |
| 119 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +880 | 11620 |
| 120 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +863 | 71118 |
| 121 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +861 | 8035 |
| 122 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +845 | 6731 |
| 123 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +845 | 2754 |
| 124 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +833 | 3107 |
| 125 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +830 | 17877 |
| 126 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +806 | 71086 |
| 127 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +760 | 2182 |
| 128 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +746 | 12792 |
| 129 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +743 | 54903 |
| 130 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +742 | 18340 |
| 131 | [wshobson/agents](https://github.com/wshobson/agents) | +741 | 29467 |
| 132 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +729 | 36799 |
| 133 | [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | +728 | 2381 |
| 134 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +726 | 30590 |
| 135 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +686 | 31182 |
| 136 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +679 | 14173 |
| 137 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +674 | 9361 |
| 138 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +674 | 3976 |
| 139 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +649 | 5535 |
| 140 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +632 | 47936 |
| 141 | [termux/termux-app](https://github.com/termux/termux-app) | +631 | 51073 |
| 142 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +625 | 58595 |
| 143 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +618 | 59619 |
| 144 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +617 | 39841 |
| 145 | [microsoft/qlib](https://github.com/microsoft/qlib) | +609 | 37792 |
| 146 | [google-research/timesfm](https://github.com/google-research/timesfm) | +602 | 9829 |
| 147 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +602 | 9898 |
| 148 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +600 | 7446 |
| 149 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +589 | 1867 |
| 150 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +586 | 17495 |
| 151 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +553 | 52081 |
| 152 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +551 | 3302 |
| 153 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +537 | 2294 |
| 154 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +536 | 52700 |
| 155 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +527 | 3054 |
| 156 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +525 | 1993 |
| 157 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +511 | 1385 |
| 158 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +509 | 1645 |
| 159 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +508 | 3192 |
| 160 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +498 | 15469 |
| 161 | [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | +498 | 1695 |
| 162 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +487 | 44545 |
| 163 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +473 | 36103 |
| 164 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +462 | 1784 |
| 165 | [oraios/serena](https://github.com/oraios/serena) | +462 | 20693 |
| 166 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +460 | 13791 |
| 167 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +450 | 4421 |
| 168 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +445 | 1686 |
| 169 | [openclaw/skills](https://github.com/openclaw/skills) | +444 | 1526 |
| 170 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +443 | 4979 |
| 171 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +438 | 23939 |
| 172 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +431 | 1385 |
| 173 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +430 | 25163 |
| 174 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +430 | 12327 |
| 175 | [exo-explore/exo](https://github.com/exo-explore/exo) | +424 | 41758 |
| 176 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +422 | 2773 |
| 177 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +421 | 11037 |
| 178 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +420 | 1340 |
| 179 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +420 | 3235 |
| 180 | [usestrix/strix](https://github.com/usestrix/strix) | +412 | 20593 |
| 181 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +405 | 7209 |
| 182 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +396 | 755 |
| 183 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +388 | 5904 |
| 184 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +383 | 44232 |
| 185 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +378 | 20821 |
| 186 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +376 | 23781 |
| 187 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +367 | 1717 |
| 188 | [samugit83/redamon](https://github.com/samugit83/redamon) | +366 | 1277 |
| 189 | [scaledown-team/scaledown](https://github.com/scaledown-team/scaledown) | +365 | 897 |
| 190 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +365 | 8629 |
| 191 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +364 | 10172 |
| 192 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +358 | 14859 |
| 193 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +353 | 5779 |
| 194 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +347 | 36697 |
| 195 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +346 | 23576 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +338 | 3798 |
| 197 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +337 | 1040 |
| 198 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +331 | 10688 |
| 199 | [maxritter/claude-codepro](https://github.com/maxritter/claude-codepro) | +324 | 1445 |
| 200 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +322 | 2279 |
| 201 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +315 | 1857 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +313 | 9489 |
| 203 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +312 | 5353 |
| 204 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +310 | 8432 |
| 205 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +308 | 833 |
| 206 | [robinebers/openusage](https://github.com/robinebers/openusage) | +302 | 1051 |
| 207 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +295 | 37313 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +293 | 41086 |
| 209 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +282 | 22393 |
| 210 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +276 | 20950 |
| 211 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +267 | 850 |
| 212 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +263 | 1059 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +262 | 12618 |
| 214 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +261 | 6384 |
| 215 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +260 | 1283 |
| 216 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +254 | 11675 |
| 217 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +251 | 2825 |
| 218 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +249 | 2383 |
| 219 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +245 | 2266 |
| 220 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +240 | 28421 |
| 221 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +238 | 40265 |
| 222 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +231 | 823 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +230 | 767 |
| 224 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +230 | 2928 |
| 225 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +229 | 39596 |
| 226 | [VonChange/utao](https://github.com/VonChange/utao) | +218 | 3860 |
| 227 | [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | +218 | 21270 |
| 228 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +209 | 778 |
| 229 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +205 | 29780 |
| 230 | [qist/tvbox](https://github.com/qist/tvbox) | +203 | 8279 |
| 231 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +198 | 727 |
| 232 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +195 | 602 |
| 233 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +193 | 33000 |
| 234 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +191 | 670 |
| 235 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +188 | 8279 |
| 236 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +186 | 25666 |
| 237 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +180 | 623 |
| 238 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | +175 | 8381 |
| 239 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +171 | 617 |
| 240 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +169 | 2216 |
| 241 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +169 | 1688 |
| 242 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +165 | 6821 |
| 243 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +164 | 28618 |
| 244 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +163 | 553 |
| 245 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +162 | 13441 |
| 246 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +161 | 451 |
| 247 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +159 | 463 |
| 248 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +158 | 598 |
| 249 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +158 | 4710 |
| 250 | [imxv/Pretty-mermaid-skills](https://github.com/imxv/Pretty-mermaid-skills) | +152 | 498 |
| 251 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +151 | 1211 |
| 252 | [expo/skills](https://github.com/expo/skills) | +148 | 1196 |
| 253 | [SeanWong17/Future-Style-Periodic-Table](https://github.com/SeanWong17/Future-Style-Periodic-Table) | +147 | 437 |
| 254 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +146 | 977 |
| 255 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +144 | 48784 |
| 256 | [decolua/9router](https://github.com/decolua/9router) | +135 | 554 |
| 257 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +135 | 439 |
| 258 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +134 | 3203 |
| 259 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +133 | 1227 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +133 | 9741 |
| 261 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +130 | 529 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +128 | 1002 |
| 263 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +127 | 390 |
| 264 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +127 | 641 |
| 265 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +126 | 2947 |
| 266 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +124 | 26681 |
| 267 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 542 |
| 268 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +119 | 8475 |
| 269 | [skylot/jadx](https://github.com/skylot/jadx) | +117 | 47365 |
| 270 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +116 | 4450 |
| 271 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +115 | 379 |
| 272 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +114 | 848 |
| 273 | [microg/GmsCore](https://github.com/microg/GmsCore) | +106 | 12374 |
| 274 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +105 | 3005 |
| 275 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +105 | 349 |
| 276 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +104 | 4460 |
| 277 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +101 | 685 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +101 | 10842 |
| 279 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +101 | 35473 |
| 280 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +100 | 1413 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +100 | 2788 |
| 282 | [bradygaster/squad](https://github.com/bradygaster/squad) | +98 | 412 |
| 283 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +97 | 361 |
| 284 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +97 | 1147 |
| 285 | [iBUHub/AIStudioToAPI](https://github.com/iBUHub/AIStudioToAPI) | +96 | 609 |
| 286 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +93 | 28606 |
| 287 | [suyunkai/EVCam](https://github.com/suyunkai/EVCam) | +89 | 277 |
| 288 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +89 | 12233 |
| 289 | [eooce/node-ws](https://github.com/eooce/node-ws) | +88 | 5685 |
| 290 | [xlrpa/FlowBot](https://github.com/xlrpa/FlowBot) | +86 | 895 |
| 291 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +83 | 26439 |
| 292 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +82 | 225 |
| 293 | [FongMi/TV](https://github.com/FongMi/TV) | +82 | 7438 |
| 294 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +81 | 1734 |
| 295 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +81 | 234 |
| 296 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +81 | 782 |
| 297 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +80 | 1299 |
| 298 | [apache/kafka](https://github.com/apache/kafka) | +80 | 32043 |
| 299 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +80 | 21246 |
| 300 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +80 | 3393 |
