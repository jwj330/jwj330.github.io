---
title: "2026-03-15 GitHub增长趋势报告"
description: "1.agency-agents+1044 2.MiroFish+855 3.autoresearch+771 4.OpenViking+595 5.browser+447"
date: 2026-03-15T20:32:33+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-15 20:32:33

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
        'daily': {"categories": ["promptfoo/promptfoo", "InsForge/InsForge", "mukul975/Anthropic-Cybersecurity-Skills", "anthropics/claude-plugins-official", "alibaba/page-agent", "koala73/worldmonitor", "pbakaus/impeccable", "systemdesign42/system-design-academy", "NawfalMotii79/PLFM_RADAR", "EdoStra/Marketing-for-Founders", "Martian-Engineering/lossless-claw", "shareAI-lab/learn-claude-code", "shanraisshan/claude-code-best-practice", "paperclipai/paperclip", "p-e-w/heretic", "lightpanda-io/browser", "volcengine/OpenViking", "karpathy/autoresearch", "666ghj/MiroFish", "msitarzewski/agency-agents"], "data": [160, 164, 166, 180, 185, 196, 207, 229, 238, 251, 267, 282, 286, 288, 324, 447, 595, 771, 855, 1044]},
        'weekly': {"categories": ["andrewyng/context-hub", "NousResearch/hermes-agent", "koala73/worldmonitor", "microsoft/BitNet", "AstrBotDevs/AstrBot", "lightpanda-io/browser", "VoltAgent/awesome-openclaw-skills", "nikopueringer/CorridorKey", "volcengine/OpenViking", "anthropics/skills", "pbakaus/impeccable", "alibaba/page-agent", "ruvnet/RuView", "obra/superpowers", "affaan-m/everything-claude-code", "paperclipai/paperclip", "666ghj/MiroFish", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [1012, 1014, 1036, 1075, 1090, 1133, 1346, 1348, 1357, 1425, 1449, 1465, 1513, 2189, 2273, 3053, 3917, 6194, 6701, 8086]},
        'monthly': {"categories": ["AlexsJones/llmfit", "qwibitai/nanoclaw", "googleworkspace/cli", "666ghj/MiroFish", "x1xhlol/system-prompts-and-models-of-ai-tools", "anomalyco/opencode", "sipeed/picoclaw", "D4Vinci/Scrapling", "paperclipai/paperclip", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "zeroclaw-labs/zeroclaw", "karpathy/autoresearch", "affaan-m/everything-claude-code", "koala73/worldmonitor", "obra/superpowers", "ruvnet/RuView", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4118, 4122, 4522, 4592, 4636, 4688, 4799, 5015, 5355, 5687, 5976, 6035, 7273, 7775, 7804, 8127, 8179, 8421, 9136, 32116]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1044 | 46106 |
| 2 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +855 | 26708 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +771 | 35994 |
| 4 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +595 | 12048 |
| 5 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +447 | 18262 |
| 6 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +324 | 14564 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +288 | 24044 |
| 8 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +286 | 16818 |
| 9 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +282 | 27785 |
| 10 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +267 | 1692 |
| 11 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +251 | 4286 |
| 12 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +238 | 2404 |
| 13 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +229 | 23155 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +207 | 8666 |
| 15 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +196 | 38530 |
| 16 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +185 | 8794 |
| 17 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +180 | 11803 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +166 | 852 |
| 19 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +164 | 4530 |
| 20 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +160 | 16345 |
| 21 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +151 | 37791 |
| 22 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +150 | 24857 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +149 | 34148 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +144 | 37009 |
| 25 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +144 | 6459 |
| 26 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +142 | 2942 |
| 27 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +141 | 30483 |
| 28 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +136 | 11867 |
| 29 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +134 | 24131 |
| 30 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +130 | 11432 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8086 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +6701 | 46106 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +6194 | 35994 |
| 4 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3917 | 26708 |
| 5 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3053 | 24044 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2273 | 51199 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2189 | 60312 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1513 | 37009 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1465 | 8794 |
| 10 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1449 | 8666 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +1425 | 74774 |
| 12 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1357 | 12048 |
| 13 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1348 | 7556 |
| 14 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1346 | 37791 |
| 15 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1133 | 18262 |
| 16 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1090 | 24857 |
| 17 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1075 | 34696 |
| 18 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1036 | 38530 |
| 19 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1014 | 7485 |
| 20 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1012 | 6188 |
| 21 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1006 | 16345 |
| 22 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +983 | 20543 |
| 23 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +978 | 27785 |
| 24 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +903 | 25060 |
| 25 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +893 | 30837 |
| 26 | [openai/symphony](https://github.com/openai/symphony) | +879 | 12747 |
| 27 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +861 | 16818 |
| 28 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +855 | 29923 |
| 29 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +819 | 30484 |
| 30 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +818 | 16925 |
| 31 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +803 | 6459 |
| 32 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +766 | 43973 |
| 33 | [jundot/omlx](https://github.com/jundot/omlx) | +760 | 4902 |
| 34 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +744 | 14564 |
| 35 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +729 | 33698 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +694 | 20581 |
| 37 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +666 | 33791 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +653 | 28427 |
| 39 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +649 | 34148 |
| 40 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +634 | 27194 |
| 41 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +634 | 7979 |
| 42 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +623 | 24575 |
| 43 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +616 | 10089 |
| 44 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +612 | 3014 |
| 45 | [m1k1o/neko](https://github.com/m1k1o/neko) | +606 | 20007 |
| 46 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +605 | 23166 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +605 | 24131 |
| 48 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +575 | 16214 |
| 49 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +539 | 2942 |
| 50 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +525 | 37330 |
| 51 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +519 | 35735 |
| 52 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +516 | 6372 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +512 | 16661 |
| 54 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +511 | 14500 |
| 55 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +497 | 11867 |
| 56 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +491 | 11803 |
| 57 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +489 | 13966 |
| 58 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +487 | 27525 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +484 | 5696 |
| 60 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +482 | 33878 |
| 61 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +473 | 5233 |
| 62 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +465 | 30776 |
| 63 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +465 | 5837 |
| 64 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +457 | 22307 |
| 65 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +448 | 9299 |
| 66 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +446 | 4530 |
| 67 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +446 | 24857 |
| 68 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +432 | 2404 |
| 69 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +426 | 7143 |
| 70 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +421 | 2912 |
| 71 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +404 | 12201 |
| 72 | [tobi/qmd](https://github.com/tobi/qmd) | +399 | 15484 |
| 73 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +382 | 27646 |
| 74 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +371 | 23155 |
| 75 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +369 | 1692 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +367 | 13620 |
| 77 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +365 | 12103 |
| 78 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +339 | 4657 |
| 79 | [openai/skills](https://github.com/openai/skills) | +335 | 14267 |
| 80 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +330 | 4147 |
| 81 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +316 | 7647 |
| 82 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +308 | 4789 |
| 83 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +306 | 28379 |
| 84 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +304 | 30678 |
| 85 | [superset-sh/superset](https://github.com/superset-sh/superset) | +299 | 7064 |
| 86 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +296 | 5989 |
| 87 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +293 | 9013 |
| 88 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +288 | 5263 |
| 89 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +287 | 5432 |
| 90 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +286 | 20869 |
| 91 | [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | +284 | 24646 |
| 92 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +284 | 10331 |
| 93 | [google/A2UI](https://github.com/google/A2UI) | +279 | 13231 |
| 94 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +272 | 6803 |
| 95 | [thesysdev/crayon](https://github.com/thesysdev/crayon) | +270 | 1710 |
| 96 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +269 | 3994 |
| 97 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +265 | 4441 |
| 98 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +260 | 14993 |
| 99 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +258 | 4286 |
| 100 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +252 | 11432 |
| 101 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +251 | 1281 |
| 102 | [blader/humanizer](https://github.com/blader/humanizer) | +249 | 9325 |
| 103 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +249 | 15828 |
| 104 | [gsd-build/gsd-2](https://github.com/gsd-build/gsd-2) | +232 | 1332 |
| 105 | [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | +227 | 1200 |
| 106 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +217 | 1151 |
| 107 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +201 | 7869 |
| 108 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +197 | 2047 |
| 109 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +197 | 1815 |
| 110 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +194 | 14609 |
| 111 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +193 | 2161 |
| 112 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +189 | 2381 |
| 113 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +183 | 44232 |
| 114 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +174 | 36799 |
| 115 | [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli) | +173 | 1105 |
| 116 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +173 | 47936 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +171 | 47122 |
| 118 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +171 | 13176 |
| 119 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +167 | 852 |
| 120 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +147 | 21581 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32116 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +9136 | 46107 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8421 | 37009 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +8179 | 60312 |
| 5 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8127 | 38530 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7804 | 51199 |
| 7 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +7775 | 35994 |
| 8 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7273 | 27194 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6035 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5976 | 25060 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5687 | 37791 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5355 | 24044 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5015 | 29923 |
| 14 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +4799 | 24857 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4688 | 109881 |
| 16 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4636 | 122870 |
| 17 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +4592 | 26708 |
| 18 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4522 | 20544 |
| 19 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4122 | 23166 |
| 20 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4118 | 16925 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4100 | 33791 |
| 22 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +4045 | 24575 |
| 23 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4041 | 30484 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3941 | 14500 |
| 25 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3928 | 33698 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3380 | 13966 |
| 27 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3374 | 13271 |
| 28 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3241 | 16818 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3165 | 11867 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3096 | 24131 |
| 31 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2974 | 69674 |
| 32 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2851 | 60117 |
| 33 | [openai/symphony](https://github.com/openai/symphony) | +2837 | 12747 |
| 34 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2759 | 33626 |
| 35 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2729 | 27785 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2709 | 85286 |
| 37 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2707 | 9571 |
| 38 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2593 | 34148 |
| 39 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2580 | 9387 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2554 | 28427 |
| 41 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2538 | 30837 |
| 42 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2424 | 14564 |
| 43 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2407 | 37330 |
| 44 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2365 | 12048 |
| 45 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2300 | 10090 |
| 46 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2290 | 8952 |
| 47 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2285 | 20581 |
| 48 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2278 | 33878 |
| 49 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2263 | 9299 |
| 50 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2189 | 24857 |
| 51 | [huggingface/skills](https://github.com/huggingface/skills) | +2173 | 9069 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2080 | 147486 |
| 53 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2035 | 9439 |
| 54 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1990 | 96919 |
| 55 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1941 | 7220 |
| 56 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1927 | 22307 |
| 57 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1921 | 21131 |
| 58 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1891 | 9908 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1849 | 6372 |
| 60 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1844 | 7143 |
| 61 | [github/spec-kit](https://github.com/github/spec-kit) | +1839 | 71722 |
| 62 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1806 | 30678 |
| 63 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1793 | 8794 |
| 64 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1760 | 6565 |
| 65 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1755 | 7869 |
| 66 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1726 | 7647 |
| 67 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1718 | 6343 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1707 | 27646 |
| 69 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1702 | 8666 |
| 70 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1694 | 74887 |
| 71 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1679 | 21581 |
| 72 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1674 | 7979 |
| 73 | [tobi/qmd](https://github.com/tobi/qmd) | +1658 | 15484 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1642 | 30776 |
| 75 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1642 | 6760 |
| 76 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1626 | 7485 |
| 77 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1579 | 149018 |
| 78 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1572 | 12103 |
| 79 | [openai/skills](https://github.com/openai/skills) | +1558 | 14267 |
| 80 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1543 | 16661 |
| 81 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1541 | 12201 |
| 82 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1523 | 5970 |
| 83 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1510 | 14993 |
| 84 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1492 | 6459 |
| 85 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1491 | 7556 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1471 | 98536 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1429 | 13620 |
| 88 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1422 | 13888 |
| 89 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1415 | 7064 |
| 90 | [tw93/Mole](https://github.com/tw93/Mole) | +1385 | 36870 |
| 91 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1374 | 33712 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1357 | 6182 |
| 93 | [openai/codex](https://github.com/openai/codex) | +1345 | 61744 |
| 94 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1343 | 37564 |
| 95 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1307 | 5432 |
| 96 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1201 | 43973 |
| 97 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1194 | 22730 |
| 98 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1187 | 18262 |
| 99 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1172 | 34696 |
| 100 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1168 | 15828 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1159 | 28379 |
| 102 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1134 | 6188 |
| 103 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1123 | 6803 |
| 104 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1115 | 16345 |
| 105 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1089 | 87598 |
| 106 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1088 | 4789 |
| 107 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1085 | 4657 |
| 108 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1079 | 11803 |
| 109 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1020 | 12943 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +870 | 5837 |
| 111 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +839 | 13176 |
| 112 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +802 | 61818 |
| 113 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +799 | 35735 |
| 114 | [jundot/omlx](https://github.com/jundot/omlx) | +791 | 4902 |
| 115 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +772 | 22960 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +765 | 36799 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +753 | 47122 |
| 118 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +742 | 9660 |
| 119 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +707 | 5233 |
| 120 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +707 | 5088 |
| 121 | [docling-project/docling](https://github.com/docling-project/docling) | +698 | 54041 |
| 122 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +697 | 4147 |
| 123 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +681 | 23035 |
| 124 | [wshobson/agents](https://github.com/wshobson/agents) | +679 | 31301 |
| 125 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +667 | 2879 |
| 126 | [google/langextract](https://github.com/google/langextract) | +657 | 33636 |
| 127 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +656 | 14609 |
| 128 | [google-research/timesfm](https://github.com/google-research/timesfm) | +651 | 10043 |
| 129 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +635 | 15617 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +616 | 47936 |
| 131 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +593 | 2022 |
| 132 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +589 | 7881 |
| 133 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +582 | 16114 |
| 134 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +581 | 17718 |
| 135 | [aden-hive/hive](https://github.com/aden-hive/hive) | +577 | 9462 |
| 136 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +576 | 2010 |
| 137 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +568 | 27525 |
| 138 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +564 | 2381 |
| 139 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +559 | 2942 |
| 140 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +552 | 30590 |
| 141 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +550 | 14373 |
| 142 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +523 | 9546 |
| 143 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +516 | 2093 |
| 144 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +513 | 44545 |
| 145 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +511 | 2303 |
| 146 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +507 | 1939 |
| 147 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +506 | 3222 |
| 148 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +502 | 44232 |
| 149 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +484 | 15028 |
| 150 | [eooce/python-ws](https://github.com/eooce/python-ws) | +473 | 1782 |
| 151 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +470 | 4796 |
| 152 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +466 | 39841 |
| 153 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +464 | 1476 |
| 154 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +463 | 18140 |
| 155 | [openclaw/skills](https://github.com/openclaw/skills) | +459 | 2889 |
| 156 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +457 | 3994 |
| 157 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +456 | 11433 |
| 158 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +453 | 9349 |
| 159 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +448 | 11278 |
| 160 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +445 | 7381 |
| 161 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +440 | 16124 |
| 162 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +433 | 1312 |
| 163 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +431 | 26452 |
| 164 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +426 | 1812 |
| 165 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +421 | 5127 |
| 166 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +411 | 3525 |
| 167 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +411 | 1565 |
| 168 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +410 | 1815 |
| 169 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +410 | 3665 |
| 170 | [searxng/searxng](https://github.com/searxng/searxng) | +403 | 26555 |
| 171 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +397 | 10468 |
| 172 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +394 | 4189 |
| 173 | [apify/agent-skills](https://github.com/apify/agent-skills) | +391 | 1631 |
| 174 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +390 | 1548 |
| 175 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +389 | 18679 |
| 176 | [microsoft/qlib](https://github.com/microsoft/qlib) | +389 | 37792 |
| 177 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +387 | 9539 |
| 178 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +386 | 1827 |
| 179 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +377 | 12095 |
| 180 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +377 | 11278 |
| 181 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +373 | 2548 |
| 182 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +366 | 5900 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +360 | 24378 |
| 184 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +358 | 10844 |
| 185 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +354 | 5423 |
| 186 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +351 | 2906 |
| 187 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +340 | 2161 |
| 188 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +328 | 10210 |
| 189 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +323 | 1511 |
| 190 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +314 | 1302 |
| 191 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +307 | 1429 |
| 192 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +305 | 13303 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +302 | 3493 |
| 194 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +290 | 3892 |
| 195 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +290 | 1969 |
| 196 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +289 | 1250 |
| 197 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +287 | 1006 |
| 198 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +284 | 713 |
| 199 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +273 | 36103 |
| 200 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +271 | 4508 |
| 201 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +253 | 29780 |
| 202 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +250 | 21281 |
| 203 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +249 | 2578 |
| 204 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +246 | 21577 |
| 205 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +244 | 1077 |
| 206 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +243 | 940 |
| 207 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +240 | 1281 |
| 208 | [robinebers/openusage](https://github.com/robinebers/openusage) | +228 | 1494 |
| 209 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +226 | 877 |
| 210 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 146 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +211 | 41086 |
| 212 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +208 | 6917 |
| 213 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +205 | 665 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +202 | 40265 |
| 215 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +201 | 28872 |
| 216 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +196 | 8855 |
| 217 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +192 | 608 |
| 218 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +191 | 8827 |
| 219 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +184 | 857 |
| 220 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +181 | 5104 |
| 221 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +176 | 690 |
| 222 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +176 | 25334 |
| 223 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +174 | 716 |
| 224 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +173 | 614 |
| 225 | [decolua/9router](https://github.com/decolua/9router) | +164 | 952 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +164 | 22723 |
| 227 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +155 | 33000 |
| 228 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +153 | 1400 |
| 229 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +153 | 559 |
| 230 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +151 | 1977 |
| 231 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +150 | 2379 |
| 232 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +149 | 704 |
| 233 | [jgraph/drawio](https://github.com/jgraph/drawio) | +149 | 4150 |
| 234 | [VonChange/utao](https://github.com/VonChange/utao) | +147 | 3920 |
| 235 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +145 | 671 |
| 236 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +144 | 851 |
| 237 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +144 | 5128 |
| 238 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +143 | 1440 |
| 239 | [qist/tvbox](https://github.com/qist/tvbox) | +140 | 8512 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +140 | 25939 |
| 241 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +137 | 1572 |
| 242 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +134 | 1035 |
| 243 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +130 | 538 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +128 | 12058 |
| 245 | [is-a-dev/register](https://github.com/is-a-dev/register) | +126 | 9978 |
| 246 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +126 | 28935 |
| 247 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +125 | 459 |
| 248 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +125 | 832 |
| 249 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +123 | 1871 |
| 250 | [lklynet/aurral](https://github.com/lklynet/aurral) | +121 | 868 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +120 | 1256 |
| 252 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +119 | 48784 |
| 253 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +118 | 3441 |
| 254 | [4ier/neo](https://github.com/4ier/neo) | +117 | 591 |
| 255 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +116 | 3227 |
| 256 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +116 | 10023 |
| 257 | [microg/GmsCore](https://github.com/microg/GmsCore) | +115 | 12567 |
| 258 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +114 | 6995 |
| 259 | [expo/skills](https://github.com/expo/skills) | +113 | 1462 |
| 260 | [fmhy/edit](https://github.com/fmhy/edit) | +113 | 8488 |
| 261 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +111 | 35473 |
| 262 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +110 | 3160 |
| 263 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +110 | 37313 |
| 264 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +104 | 756 |
| 265 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +102 | 867 |
| 266 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +101 | 800 |
| 267 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +99 | 398 |
| 268 | [skylot/jadx](https://github.com/skylot/jadx) | +99 | 47365 |
| 269 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +98 | 818 |
| 270 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 11124 |
| 271 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +95 | 400 |
| 272 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +93 | 497 |
| 273 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 975 |
| 274 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +88 | 573 |
| 275 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +87 | 325 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +86 | 26866 |
| 277 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +85 | 8739 |
| 278 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +83 | 810 |
| 279 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +83 | 460 |
| 280 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +82 | 893 |
| 281 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +81 | 523 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +81 | 2995 |
| 283 | [apache/kafka](https://github.com/apache/kafka) | +81 | 32043 |
| 284 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +80 | 326 |
| 285 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +79 | 416 |
| 286 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +78 | 1013 |
| 287 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +77 | 374 |
| 288 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +77 | 687 |
| 289 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +77 | 964 |
| 290 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +76 | 409 |
| 291 | [openjdk/jdk](https://github.com/openjdk/jdk) | +76 | 22725 |
| 292 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +74 | 1329 |
| 293 | [idinging/freemail](https://github.com/idinging/freemail) | +72 | 1018 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +71 | 1313 |
| 295 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +70 | 413 |
| 296 | [f/agentlytics](https://github.com/f/agentlytics) | +70 | 334 |
| 297 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +70 | 8196 |
| 298 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +69 | 21353 |
| 299 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +69 | 7598 |
| 300 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +66 | 6060 |
