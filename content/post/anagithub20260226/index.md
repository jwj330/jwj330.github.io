---
title: "2026-02-26 GitHub增长趋势报告"
description: "1.clawdbot+1126 2.Scrapling+450 3.frontend-slides+425 4.skills+416 5.worldmonitor+338"
date: 2026-02-26T03:06:46+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-26 03:06:46

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
        'daily': {"categories": ["sickn33/antigravity-awesome-skills", "sipeed/picoclaw", "netease-youdao/LobsterAI", "Lakr233/AssppWeb", "clockworklabs/SpacetimeDB", "VoltAgent/awesome-openclaw-skills", "qwibitai/nanoclaw", "HKUDS/nanobot", "zeroclaw-labs/zeroclaw", "badlogic/pi-mono", "affaan-m/everything-claude-code", "glittercowboy/get-shit-done", "muratcankoylan/Agent-Skills-for-Context-Engineering", "hesamsheikh/awesome-openclaw-usecases", "abhigyanpatwari/GitNexus", "koala73/worldmonitor", "huggingface/skills", "zarazhangrui/frontend-slides", "D4Vinci/Scrapling", "clawdbot/clawdbot"], "data": [135, 144, 152, 183, 188, 191, 191, 192, 209, 216, 220, 222, 238, 240, 241, 338, 416, 425, 450, 1126]},
        'weekly': {"categories": ["VoltAgent/awesome-openclaw-skills", "alibaba/zvec", "HKUDS/ClawWork", "millionco/react-doctor", "D4Vinci/Scrapling", "HKUDS/nanobot", "affaan-m/everything-claude-code", "anomalyco/opencode", "glittercowboy/get-shit-done", "anthropics/skills", "sipeed/picoclaw", "huggingface/skills", "qwibitai/nanoclaw", "koala73/worldmonitor", "obra/superpowers", "vxcontrol/pentagi", "jamiepine/voicebox", "zeroclaw-labs/zeroclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "clawdbot/clawdbot"], "data": [1022, 1025, 1038, 1045, 1084, 1128, 1153, 1204, 1206, 1274, 1369, 1399, 1696, 1891, 2079, 2189, 2291, 2307, 2562, 6457]},
        'monthly': {"categories": ["daytonaio/daytona", "nextlevelbuilder/ui-ux-pro-max-skill", "glittercowboy/get-shit-done", "sickn33/antigravity-awesome-skills", "ComposioHQ/awesome-claude-skills", "x1xhlol/system-prompts-and-models-of-ai-tools", "koala73/worldmonitor", "badlogic/pi-mono", "qwibitai/nanoclaw", "thedotmack/claude-mem", "zeroclaw-labs/zeroclaw", "sipeed/picoclaw", "VoltAgent/awesome-openclaw-skills", "KeygraphHQ/shannon", "anthropics/skills", "HKUDS/nanobot", "anomalyco/opencode", "obra/superpowers", "affaan-m/everything-claude-code", "clawdbot/clawdbot"], "data": [3651, 3658, 3788, 3795, 3821, 3942, 4059, 4362, 4447, 4836, 5906, 6146, 6150, 6828, 7299, 7502, 7559, 7861, 8089, 69701]}
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
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +1126 | 224760 |
| 2 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +450 | 14467 |
| 3 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +425 | 4157 |
| 4 | [huggingface/skills](https://github.com/huggingface/skills) | +416 | 6248 |
| 5 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +338 | 14875 |
| 6 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +241 | 3517 |
| 7 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +240 | 7956 |
| 8 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +238 | 10533 |
| 9 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +222 | 20119 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +220 | 51199 |
| 11 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +216 | 16518 |
| 12 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +209 | 19139 |
| 13 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +192 | 25073 |
| 14 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +191 | 14600 |
| 15 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +191 | 20079 |
| 16 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +188 | 20309 |
| 17 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +183 | 1195 |
| 18 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +152 | 2449 |
| 19 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +144 | 19841 |
| 20 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +135 | 15498 |
| 21 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +125 | 4857 |
| 22 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +121 | 2231 |
| 23 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +113 | 33878 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +112 | 34148 |
| 25 | [generalaction/emdash](https://github.com/generalaction/emdash) | +110 | 2087 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +106 | 13320 |
| 27 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +98 | 1217 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +96 | 20099 |
| 29 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +95 | 1079 |
| 30 | [vercel/chat](https://github.com/vercel/chat) | +92 | 539 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +6457 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2562 | 122870 |
| 3 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +2307 | 19139 |
| 4 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2291 | 11061 |
| 5 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2189 | 8177 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2079 | 60312 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1891 | 14875 |
| 8 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1696 | 14601 |
| 9 | [huggingface/skills](https://github.com/huggingface/skills) | +1399 | 6248 |
| 10 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +1369 | 19841 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1274 | 74774 |
| 12 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +1206 | 20119 |
| 13 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1204 | 109881 |
| 14 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1153 | 51199 |
| 15 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1128 | 25073 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1084 | 14467 |
| 17 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1045 | 4760 |
| 18 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1038 | 5522 |
| 19 | [alibaba/zvec](https://github.com/alibaba/zvec) | +1025 | 7860 |
| 20 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1022 | 20079 |
| 21 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +952 | 60117 |
| 22 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +949 | 15498 |
| 23 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +943 | 7956 |
| 24 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +888 | 7010 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +861 | 16518 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +809 | 3517 |
| 27 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +752 | 69674 |
| 28 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +692 | 2449 |
| 29 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +679 | 5477 |
| 30 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +675 | 3038 |
| 31 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +628 | 2154 |
| 32 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +622 | 30678 |
| 33 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +609 | 4157 |
| 34 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +601 | 9636 |
| 35 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +593 | 33878 |
| 36 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +591 | 4850 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +586 | 34148 |
| 38 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +554 | 37330 |
| 39 | [google-research/timesfm](https://github.com/google-research/timesfm) | +550 | 9739 |
| 40 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +542 | 2457 |
| 41 | [blader/humanizer](https://github.com/blader/humanizer) | +530 | 6790 |
| 42 | [tw93/Mole](https://github.com/tw93/Mole) | +529 | 36870 |
| 43 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +519 | 20968 |
| 44 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +507 | 17575 |
| 45 | [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | +501 | 23040 |
| 46 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +498 | 37564 |
| 47 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +470 | 25043 |
| 48 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +463 | 10533 |
| 49 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +459 | 2000 |
| 50 | [HailToDodongo/pyrite64](https://github.com/HailToDodongo/pyrite64) | +455 | 2445 |
| 51 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +451 | 9994 |
| 52 | [agenticnotetaking/arscontexta](https://github.com/agenticnotetaking/arscontexta) | +446 | 1861 |
| 53 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +429 | 13320 |
| 54 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +427 | 2550 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +425 | 17942 |
| 56 | [stan-smith/FossFLOW](https://github.com/stan-smith/FossFLOW) | +423 | 18754 |
| 57 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +418 | 1313 |
| 58 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +403 | 20099 |
| 59 | [IgorShadurin/app.yumcut.com](https://github.com/IgorShadurin/app.yumcut.com) | +380 | 880 |
| 60 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +379 | 2891 |
| 61 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +375 | 10975 |
| 62 | [tobi/qmd](https://github.com/tobi/qmd) | +371 | 10533 |
| 63 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +364 | 1643 |
| 64 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +354 | 3846 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +348 | 25720 |
| 66 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +347 | 7909 |
| 67 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +346 | 3463 |
| 68 | [cloudflare/agents](https://github.com/cloudflare/agents) | +338 | 4229 |
| 69 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +337 | 8726 |
| 70 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +333 | 8880 |
| 71 | [ronitsingh10/FineTune](https://github.com/ronitsingh10/FineTune) | +326 | 3650 |
| 72 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +316 | 10699 |
| 73 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +312 | 10117 |
| 74 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +310 | 32872 |
| 75 | [p2r3/convert](https://github.com/p2r3/convert) | +305 | 2136 |
| 76 | [slopus/happy](https://github.com/slopus/happy) | +296 | 13470 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +295 | 9328 |
| 78 | [rudrankriyam/App-Store-Connect-CLI](https://github.com/rudrankriyam/App-Store-Connect-CLI) | +295 | 2313 |
| 79 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +284 | 5764 |
| 80 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +282 | 15530 |
| 81 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +281 | 3945 |
| 82 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +277 | 7280 |
| 83 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +275 | 1195 |
| 84 | [steipete/summarize](https://github.com/steipete/summarize) | +268 | 4442 |
| 85 | [steipete/gogcli](https://github.com/steipete/gogcli) | +264 | 4957 |
| 86 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +259 | 11001 |
| 87 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +259 | 22544 |
| 88 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +258 | 12415 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +255 | 11653 |
| 90 | [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools) | +253 | 1532 |
| 91 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +251 | 25053 |
| 92 | [memovai/mimiclaw](https://github.com/memovai/mimiclaw) | +250 | 3294 |
| 93 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +245 | 47122 |
| 94 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +238 | 8339 |
| 95 | [openai/skills](https://github.com/openai/skills) | +232 | 9755 |
| 96 | [google/langextract](https://github.com/google/langextract) | +230 | 33636 |
| 97 | [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) | +226 | 1217 |
| 98 | [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | +212 | 902 |
| 99 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +211 | 5400 |
| 100 | [virattt/dexter](https://github.com/virattt/dexter) | +208 | 16451 |
| 101 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +208 | 3740 |
| 102 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +195 | 8537 |
| 103 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +184 | 772 |
| 104 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +172 | 36799 |
| 105 | [aden-hive/hive](https://github.com/aden-hive/hive) | +171 | 8332 |
| 106 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +169 | 6356 |
| 107 | [samugit83/redamon](https://github.com/samugit83/redamon) | +166 | 1256 |
| 108 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +166 | 21886 |
| 109 | [usestrix/strix](https://github.com/usestrix/strix) | +164 | 20568 |
| 110 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +163 | 2244 |
| 111 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +162 | 2231 |
| 112 | [shuaiplus/NodeWarden](https://github.com/shuaiplus/NodeWarden) | +158 | 755 |
| 113 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +157 | 6625 |
| 114 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +155 | 15417 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +154 | 29376 |
| 116 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +151 | 14544 |
| 117 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +151 | 12680 |
| 118 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +149 | 30590 |
| 119 | [PostHog/posthog](https://github.com/PostHog/posthog) | +149 | 31767 |
| 120 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +146 | 2689 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) | +69701 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8089 | 51199 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +7861 | 60312 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +7559 | 109881 |
| 5 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7502 | 25073 |
| 6 | [anthropics/skills](https://github.com/anthropics/skills) | +7299 | 74774 |
| 7 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +6828 | 25043 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +6150 | 20079 |
| 9 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6146 | 19841 |
| 10 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +5906 | 19139 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4836 | 30678 |
| 12 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4447 | 14601 |
| 13 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +4362 | 16518 |
| 14 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +4059 | 14876 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +3942 | 122870 |
| 16 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3821 | 37330 |
| 17 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3795 | 15498 |
| 18 | [glittercowboy/get-shit-done](https://github.com/glittercowboy/get-shit-done) | +3788 | 20119 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3658 | 34148 |
| 20 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3651 | 60117 |
| 21 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +3397 | 33878 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3192 | 11061 |
| 23 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3068 | 69674 |
| 24 | [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | +3004 | 9195 |
| 25 | [google/langextract](https://github.com/google/langextract) | +2979 | 33636 |
| 26 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2693 | 17575 |
| 27 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2675 | 85286 |
| 28 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2577 | 37810 |
| 29 | [openai/skills](https://github.com/openai/skills) | +2541 | 9755 |
| 30 | [aden-hive/hive](https://github.com/aden-hive/hive) | +2537 | 8332 |
| 31 | [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) | +2535 | 7727 |
| 32 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2526 | 13320 |
| 33 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2519 | 96919 |
| 34 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2475 | 7860 |
| 35 | [virattt/dexter](https://github.com/virattt/dexter) | +2429 | 16451 |
| 36 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2408 | 7955 |
| 37 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +2391 | 32872 |
| 38 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2328 | 8177 |
| 39 | [tobi/qmd](https://github.com/tobi/qmd) | +2299 | 10533 |
| 40 | [github/spec-kit](https://github.com/github/spec-kit) | +2225 | 71722 |
| 41 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2225 | 6889 |
| 42 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2214 | 7956 |
| 43 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +2180 | 24292 |
| 44 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +2167 | 149018 |
| 45 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +2138 | 7280 |
| 46 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2118 | 20099 |
| 47 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +2109 | 17078 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1929 | 25720 |
| 49 | [tambo-ai/tambo](https://github.com/tambo-ai/tambo) | +1908 | 10951 |
| 50 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1904 | 37564 |
| 51 | [lucasgelfond/zerobrew](https://github.com/lucasgelfond/zerobrew) | +1837 | 6522 |
| 52 | [pydantic/monty](https://github.com/pydantic/monty) | +1833 | 5686 |
| 53 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1815 | 6356 |
| 54 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +1799 | 176173 |
| 55 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1787 | 8880 |
| 56 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1745 | 9994 |
| 57 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1743 | 10700 |
| 58 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1693 | 9636 |
| 59 | [tw93/Mole](https://github.com/tw93/Mole) | +1670 | 36870 |
| 60 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1620 | 7379 |
| 61 | [openai/codex](https://github.com/openai/codex) | +1598 | 61744 |
| 62 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1598 | 15530 |
| 63 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +1579 | 21210 |
| 64 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1554 | 5477 |
| 65 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1553 | 98536 |
| 66 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1547 | 7909 |
| 67 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +1503 | 8537 |
| 68 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +1492 | 148393 |
| 69 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1488 | 5522 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1486 | 9328 |
| 71 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1475 | 33712 |
| 72 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1469 | 4850 |
| 73 | [huggingface/skills](https://github.com/huggingface/skills) | +1459 | 6248 |
| 74 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1438 | 26685 |
| 75 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1425 | 8726 |
| 76 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1413 | 6950 |
| 77 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1412 | 4957 |
| 78 | [slopus/happy](https://github.com/slopus/happy) | +1402 | 13470 |
| 79 | [steveyegge/beads](https://github.com/steveyegge/beads) | +1389 | 17235 |
| 80 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1382 | 4760 |
| 81 | [steveyegge/gastown](https://github.com/steveyegge/gastown) | +1329 | 10309 |
| 82 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1272 | 74887 |
| 83 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1260 | 12415 |
| 84 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1226 | 7010 |
| 85 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1213 | 21886 |
| 86 | [blader/humanizer](https://github.com/blader/humanizer) | +1205 | 6790 |
| 87 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1199 | 3786 |
| 88 | [steipete/summarize](https://github.com/steipete/summarize) | +1187 | 4442 |
| 89 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1172 | 3846 |
| 90 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +1168 | 11240 |
| 91 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1161 | 14467 |
| 92 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +1142 | 95547 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1141 | 11653 |
| 94 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +1132 | 11001 |
| 95 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +1123 | 3519 |
| 96 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +1111 | 15175 |
| 97 | [knadh/oat](https://github.com/knadh/oat) | +1108 | 3771 |
| 98 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1107 | 3945 |
| 99 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1107 | 8339 |
| 100 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1082 | 3740 |
| 101 | [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | +1064 | 30612 |
| 102 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1049 | 20968 |
| 103 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1030 | 43973 |
| 104 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1028 | 3463 |
| 105 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +1020 | 14544 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +1016 | 22544 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1005 | 25053 |
| 108 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +989 | 21305 |
| 109 | [docling-project/docling](https://github.com/docling-project/docling) | +970 | 54041 |
| 110 | [Robbyant/lingbot-world](https://github.com/Robbyant/lingbot-world) | +943 | 2978 |
| 111 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +941 | 13446 |
| 112 | [HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) | +936 | 23040 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +935 | 61818 |
| 114 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +935 | 47122 |
| 115 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +926 | 28599 |
| 116 | [Blaizzy/mlx-audio](https://github.com/Blaizzy/mlx-audio) | +907 | 6070 |
| 117 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +877 | 6777 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +874 | 7639 |
| 119 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +873 | 3049 |
| 120 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +869 | 17942 |
| 121 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | +857 | 71118 |
| 122 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +828 | 17821 |
| 123 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +822 | 2689 |
| 124 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +822 | 14151 |
| 125 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +820 | 71086 |
| 126 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +818 | 6625 |
| 127 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +803 | 5518 |
| 128 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +768 | 12680 |
| 129 | [wshobson/agents](https://github.com/wshobson/agents) | +764 | 29376 |
| 130 | [supermemoryai/claude-supermemory](https://github.com/supermemoryai/claude-supermemory) | +759 | 2179 |
| 131 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +740 | 54903 |
| 132 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +727 | 4216 |
| 133 | [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | +725 | 2367 |
| 134 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +725 | 18226 |
| 135 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +721 | 30590 |
| 136 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +720 | 36799 |
| 137 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +695 | 9291 |
| 138 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +680 | 31182 |
| 139 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +663 | 59619 |
| 140 | [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | +646 | 58595 |
| 141 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +641 | 10533 |
| 142 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +639 | 47936 |
| 143 | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | +637 | 5325 |
| 144 | [termux/termux-app](https://github.com/termux/termux-app) | +634 | 51073 |
| 145 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +618 | 9845 |
| 146 | [microsoft/qlib](https://github.com/microsoft/qlib) | +616 | 37792 |
| 147 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +614 | 3087 |
| 148 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +612 | 39841 |
| 149 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +607 | 7276 |
| 150 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +582 | 17478 |
| 151 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +580 | 1819 |
| 152 | [google-research/timesfm](https://github.com/google-research/timesfm) | +578 | 9739 |
| 153 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | +568 | 52081 |
| 154 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +550 | 23458 |
| 155 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +544 | 3365 |
| 156 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +538 | 2244 |
| 157 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +538 | 52700 |
| 158 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +524 | 1983 |
| 159 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +515 | 3159 |
| 160 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +508 | 1491 |
| 161 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +507 | 3212 |
| 162 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +498 | 44545 |
| 163 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +492 | 1568 |
| 164 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +490 | 15417 |
| 165 | [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | +490 | 1669 |
| 166 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +485 | 12262 |
| 167 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +483 | 36103 |
| 168 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +459 | 13767 |
| 169 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +458 | 1772 |
| 170 | [oraios/serena](https://github.com/oraios/serena) | +456 | 20649 |
| 171 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +447 | 4938 |
| 172 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +442 | 1643 |
| 173 | [openclaw/skills](https://github.com/openclaw/skills) | +441 | 1449 |
| 174 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +439 | 25095 |
| 175 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +439 | 23922 |
| 176 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +439 | 4358 |
| 177 | [exo-explore/exo](https://github.com/exo-explore/exo) | +423 | 41758 |
| 178 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +419 | 1313 |
| 179 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +419 | 2732 |
| 180 | [usestrix/strix](https://github.com/usestrix/strix) | +408 | 20568 |
| 181 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +406 | 10975 |
| 182 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +404 | 5869 |
| 183 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +402 | 1310 |
| 184 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +391 | 23767 |
| 185 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +391 | 20788 |
| 186 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +390 | 1692 |
| 187 | [scaledown-team/scaledown](https://github.com/scaledown-team/scaledown) | +365 | 897 |
| 188 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +365 | 14835 |
| 189 | [samugit83/redamon](https://github.com/samugit83/redamon) | +361 | 1256 |
| 190 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +359 | 8597 |
| 191 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +355 | 10623 |
| 192 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +352 | 23529 |
| 193 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +350 | 5764 |
| 194 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +350 | 10117 |
| 195 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +347 | 643 |
| 196 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +347 | 36697 |
| 197 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +339 | 6934 |
| 198 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +333 | 1001 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +331 | 3756 |
| 200 | [maxritter/claude-codepro](https://github.com/maxritter/claude-codepro) | +322 | 1440 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +315 | 9964 |
| 202 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +313 | 5340 |
| 203 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +312 | 8379 |
| 204 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +310 | 1808 |
| 205 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +303 | 37313 |
| 206 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +301 | 807 |
| 207 | [robinebers/openusage](https://github.com/robinebers/openusage) | +301 | 1035 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +298 | 41086 |
| 209 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +295 | 22369 |
| 210 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +282 | 11653 |
| 211 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +276 | 20918 |
| 212 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +269 | 6883 |
| 213 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +259 | 838 |
| 214 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +257 | 1043 |
| 215 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +256 | 2803 |
| 216 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +249 | 2915 |
| 217 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +248 | 2358 |
| 218 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +247 | 12566 |
| 219 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +244 | 39596 |
| 220 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +242 | 28403 |
| 221 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +239 | 2236 |
| 222 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +238 | 40265 |
| 223 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +227 | 772 |
| 224 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +222 | 741 |
| 225 | [VonChange/utao](https://github.com/VonChange/utao) | +220 | 3850 |
| 226 | [pedroslopez/whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js) | +215 | 21255 |
| 227 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +208 | 776 |
| 228 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +205 | 29780 |
| 229 | [qist/tvbox](https://github.com/qist/tvbox) | +200 | 8265 |
| 230 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +196 | 718 |
| 231 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +193 | 8272 |
| 232 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +191 | 25631 |
| 233 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +189 | 663 |
| 234 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +189 | 33000 |
| 235 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +188 | 577 |
| 236 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | +185 | 8356 |
| 237 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +171 | 28594 |
| 238 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +170 | 621 |
| 239 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +169 | 6809 |
| 240 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +169 | 573 |
| 241 | [ashishps1/awesome-leetcode-resources](https://github.com/ashishps1/awesome-leetcode-resources) | +169 | 15931 |
| 242 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +167 | 1658 |
| 243 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +165 | 4695 |
| 244 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +164 | 551 |
| 245 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +164 | 13428 |
| 246 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +163 | 2197 |
| 247 | [imjszhang/Deepseek-Cowork](https://github.com/imjszhang/Deepseek-Cowork) | +163 | 438 |
| 248 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +161 | 513 |
| 249 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +158 | 586 |
| 250 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +156 | 440 |
| 251 | [expo/skills](https://github.com/expo/skills) | +150 | 1166 |
| 252 | [imxv/Pretty-mermaid-skills](https://github.com/imxv/Pretty-mermaid-skills) | +150 | 494 |
| 253 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +150 | 48784 |
| 254 | [SeanWong17/Future-Style-Periodic-Table](https://github.com/SeanWong17/Future-Style-Periodic-Table) | +147 | 436 |
| 255 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +146 | 1192 |
| 256 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +146 | 972 |
| 257 | [decolua/9router](https://github.com/decolua/9router) | +135 | 537 |
| 258 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +135 | 3196 |
| 259 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +135 | 9719 |
| 260 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +131 | 2930 |
| 261 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +130 | 1203 |
| 262 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +129 | 414 |
| 263 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +128 | 518 |
| 264 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +127 | 984 |
| 265 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +125 | 4442 |
| 266 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +125 | 26675 |
| 267 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +124 | 6176 |
| 268 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +122 | 617 |
| 269 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +119 | 539 |
| 270 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +118 | 8459 |
| 271 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +117 | 4450 |
| 272 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +114 | 342 |
| 273 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +114 | 377 |
| 274 | [skylot/jadx](https://github.com/skylot/jadx) | +110 | 47365 |
| 275 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +108 | 336 |
| 276 | [microg/GmsCore](https://github.com/microg/GmsCore) | +106 | 12364 |
| 277 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +105 | 2993 |
| 278 | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) | +104 | 816 |
| 279 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +103 | 1394 |
| 280 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +101 | 685 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +101 | 10833 |
| 282 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +101 | 35473 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +100 | 1135 |
| 284 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +100 | 2769 |
| 285 | [eooce/node-ws](https://github.com/eooce/node-ws) | +98 | 5676 |
| 286 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +97 | 352 |
| 287 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +96 | 12224 |
| 288 | [suyunkai/EVCam](https://github.com/suyunkai/EVCam) | +93 | 277 |
| 289 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +93 | 28603 |
| 290 | [bradygaster/squad](https://github.com/bradygaster/squad) | +92 | 359 |
| 291 | [xlrpa/FlowBot](https://github.com/xlrpa/FlowBot) | +85 | 884 |
| 292 | [FongMi/TV](https://github.com/FongMi/TV) | +85 | 7428 |
| 293 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +84 | 45263 |
| 294 | [openjdk/jdk](https://github.com/openjdk/jdk) | +83 | 22644 |
| 295 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +83 | 26437 |
| 296 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +82 | 1724 |
| 297 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +82 | 773 |
| 298 | [apache/kafka](https://github.com/apache/kafka) | +82 | 32043 |
| 299 | [dataease/dataease](https://github.com/dataease/dataease) | +82 | 23444 |
| 300 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +82 | 5788 |
