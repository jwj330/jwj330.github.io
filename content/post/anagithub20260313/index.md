---
title: "2026-03-13 GitHub增长趋势报告"
description: "1.agency-agents+1071 2.MiroFish+528 3.autoresearch+507 4.impeccable+372 5.BitNet+364"
date: 2026-03-13T20:37:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-13 20:37:49

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
        'daily': {"categories": ["nikopueringer/CorridorKey", "AlexsJones/llmfit", "VoltAgent/awesome-openclaw-skills", "gsd-build/get-shit-done", "langflow-ai/openrag", "NousResearch/hermes-agent", "koala73/worldmonitor", "karpathy/nanochat", "p-e-w/heretic", "AstrBotDevs/AstrBot", "promptfoo/promptfoo", "paperclipai/paperclip", "lightpanda-io/browser", "alibaba/page-agent", "volcengine/OpenViking", "microsoft/BitNet", "pbakaus/impeccable", "karpathy/autoresearch", "666ghj/MiroFish", "msitarzewski/agency-agents"], "data": [118, 118, 120, 137, 153, 157, 157, 168, 231, 252, 292, 311, 313, 314, 355, 364, 372, 507, 528, 1071]},
        'weekly': {"categories": ["nikopueringer/CorridorKey", "moeru-ai/airi", "nearai/ironclaw", "koala73/worldmonitor", "pbakaus/impeccable", "phuryn/pm-skills", "alibaba/page-agent", "openai/symphony", "anthropics/skills", "googleworkspace/cli", "ruvnet/RuView", "VoltAgent/awesome-openclaw-skills", "obra/superpowers", "pingdotgg/t3code", "affaan-m/everything-claude-code", "666ghj/MiroFish", "paperclipai/paperclip", "msitarzewski/agency-agents", "karpathy/autoresearch", "openclaw/openclaw"], "data": [1151, 1178, 1198, 1213, 1218, 1282, 1337, 1449, 1498, 1615, 1660, 1671, 1739, 1783, 2922, 3073, 3985, 5569, 6514, 9771]},
        'monthly': {"categories": ["gsd-build/get-shit-done", "HKUDS/nanobot", "qwibitai/nanoclaw", "googleworkspace/cli", "x1xhlol/system-prompts-and-models-of-ai-tools", "anomalyco/opencode", "D4Vinci/Scrapling", "paperclipai/paperclip", "VoltAgent/awesome-openclaw-skills", "sipeed/picoclaw", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "karpathy/autoresearch", "msitarzewski/agency-agents", "affaan-m/everything-claude-code", "obra/superpowers", "zeroclaw-labs/zeroclaw", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3997, 4105, 4120, 4368, 4603, 4775, 4842, 4842, 5719, 5998, 6002, 6052, 6516, 7349, 7570, 7658, 7934, 8335, 8803, 32658]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1071 | 39525 |
| 2 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +528 | 21568 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +507 | 31243 |
| 4 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +372 | 7281 |
| 5 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +364 | 33775 |
| 6 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +355 | 8782 |
| 7 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +314 | 7338 |
| 8 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +313 | 15172 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +311 | 22211 |
| 10 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +292 | 15102 |
| 11 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +252 | 23743 |
| 12 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +231 | 12846 |
| 13 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +168 | 43973 |
| 14 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +157 | 37272 |
| 15 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +157 | 6673 |
| 16 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +153 | 2164 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +137 | 29436 |
| 18 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +120 | 36885 |
| 19 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +118 | 16110 |
| 20 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +118 | 6755 |
| 21 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +109 | 10713 |
| 22 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +105 | 27793 |
| 23 | [google/A2UI](https://github.com/google/A2UI) | +104 | 13006 |
| 24 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +101 | 3577 |
| 25 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +100 | 26787 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +98 | 19558 |
| 27 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +98 | 14788 |
| 28 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +97 | 36159 |
| 29 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +92 | 5809 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +90 | 34148 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9771 | 224760 |
| 2 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +6514 | 31243 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5569 | 39525 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3985 | 22211 |
| 5 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3073 | 21568 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2922 | 51199 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1783 | 6160 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +1739 | 60312 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1671 | 36885 |
| 10 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1660 | 36159 |
| 11 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +1615 | 19939 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +1498 | 74774 |
| 13 | [openai/symphony](https://github.com/openai/symphony) | +1449 | 12212 |
| 14 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1337 | 7338 |
| 15 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1282 | 6874 |
| 16 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1218 | 7282 |
| 17 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1213 | 37272 |
| 18 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1198 | 9894 |
| 19 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1178 | 33290 |
| 20 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1151 | 6755 |
| 21 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1150 | 24399 |
| 22 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1036 | 29260 |
| 23 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1012 | 5809 |
| 24 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +993 | 30217 |
| 25 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +972 | 26014 |
| 26 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +924 | 6673 |
| 27 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +896 | 23743 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +860 | 29436 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +851 | 33217 |
| 30 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +816 | 16126 |
| 31 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +788 | 16110 |
| 32 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +777 | 5663 |
| 33 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +758 | 14174 |
| 34 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +742 | 33775 |
| 35 | [openai/skills](https://github.com/openai/skills) | +737 | 14122 |
| 36 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +727 | 7135 |
| 37 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +720 | 26787 |
| 38 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +716 | 24016 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +715 | 19558 |
| 40 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +661 | 15102 |
| 41 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +655 | 27793 |
| 42 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +626 | 34148 |
| 43 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +625 | 43973 |
| 44 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +617 | 22391 |
| 45 | [jundot/omlx](https://github.com/jundot/omlx) | +600 | 4218 |
| 46 | [m1k1o/neko](https://github.com/m1k1o/neko) | +591 | 19919 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +585 | 8945 |
| 48 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +576 | 14788 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +566 | 23296 |
| 50 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +555 | 8782 |
| 51 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +543 | 16180 |
| 52 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +541 | 11158 |
| 53 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +539 | 37330 |
| 54 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +517 | 35735 |
| 55 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +510 | 33878 |
| 56 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +501 | 5241 |
| 57 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +499 | 12485 |
| 58 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +481 | 5484 |
| 59 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +473 | 2570 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +472 | 30308 |
| 61 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +469 | 21656 |
| 62 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +464 | 9774 |
| 63 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +459 | 24521 |
| 64 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +445 | 11849 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +436 | 5147 |
| 66 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +427 | 12846 |
| 67 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +420 | 4878 |
| 68 | [tobi/qmd](https://github.com/tobi/qmd) | +419 | 15131 |
| 69 | [viperrcrypto/Siftly](https://github.com/viperrcrypto/Siftly) | +419 | 1462 |
| 70 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +417 | 4578 |
| 71 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +412 | 8789 |
| 72 | [superset-sh/superset](https://github.com/superset-sh/superset) | +407 | 6844 |
| 73 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +402 | 27335 |
| 74 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +399 | 11149 |
| 75 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +387 | 11806 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +382 | 13221 |
| 77 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +377 | 32900 |
| 78 | [cyxzdev/Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | +373 | 1490 |
| 79 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +371 | 4079 |
| 80 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +363 | 2587 |
| 81 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +361 | 2813 |
| 82 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +357 | 7429 |
| 83 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +354 | 6561 |
| 84 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +354 | 15580 |
| 85 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +344 | 20872 |
| 86 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +339 | 5794 |
| 87 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +339 | 2809 |
| 88 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +337 | 15172 |
| 89 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +322 | 33443 |
| 90 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +318 | 4173 |
| 91 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +307 | 10081 |
| 92 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +305 | 26787 |
| 93 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +301 | 2164 |
| 94 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +297 | 14762 |
| 95 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +291 | 10713 |
| 96 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +288 | 20626 |
| 97 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +287 | 27940 |
| 98 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +286 | 2384 |
| 99 | [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) | +286 | 2141 |
| 100 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +286 | 30678 |
| 101 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +271 | 7733 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +258 | 15548 |
| 103 | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) | +254 | 1983 |
| 104 | [thesysdev/crayon](https://github.com/thesysdev/crayon) | +237 | 1571 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +211 | 25045 |
| 106 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +204 | 1976 |
| 107 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +203 | 36799 |
| 108 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +189 | 1506 |
| 109 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +183 | 47122 |
| 110 | [wshobson/agents](https://github.com/wshobson/agents) | +180 | 31166 |
| 111 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +180 | 1371 |
| 112 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +176 | 13011 |
| 113 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +175 | 7805 |
| 114 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +172 | 15136 |
| 115 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +170 | 1896 |
| 116 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +168 | 14355 |
| 117 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +161 | 21418 |
| 118 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +158 | 943 |
| 119 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +158 | 44232 |
| 120 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +158 | 47936 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32658 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8803 | 37272 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8335 | 36159 |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7934 | 26787 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +7658 | 60312 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7570 | 51199 |
| 7 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +7349 | 39527 |
| 8 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +6516 | 31243 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6052 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +6002 | 24399 |
| 11 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +5998 | 24521 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5719 | 36885 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4842 | 22211 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4842 | 29260 |
| 15 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4775 | 109881 |
| 16 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4603 | 122870 |
| 17 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4368 | 19939 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4120 | 22391 |
| 19 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4105 | 33217 |
| 20 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3997 | 29436 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3964 | 33290 |
| 22 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3958 | 24016 |
| 23 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3885 | 16110 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3845 | 14174 |
| 25 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3369 | 21568 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3368 | 13160 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3191 | 12485 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3155 | 23296 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3009 | 11158 |
| 30 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +3003 | 33443 |
| 31 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2958 | 69674 |
| 32 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2837 | 60117 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2752 | 14789 |
| 34 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2691 | 9472 |
| 35 | [openai/symphony](https://github.com/openai/symphony) | +2686 | 12212 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2673 | 85286 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2561 | 9302 |
| 38 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2554 | 8912 |
| 39 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2525 | 27793 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2480 | 34148 |
| 41 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2473 | 9894 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2428 | 37330 |
| 43 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2391 | 30217 |
| 44 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2307 | 26014 |
| 45 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2297 | 33878 |
| 46 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2168 | 8945 |
| 47 | [huggingface/skills](https://github.com/huggingface/skills) | +2145 | 8945 |
| 48 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2117 | 19558 |
| 49 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2089 | 96919 |
| 50 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2047 | 12846 |
| 51 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1989 | 9281 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1953 | 147486 |
| 53 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1922 | 7153 |
| 54 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1894 | 30678 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1893 | 23743 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1885 | 20872 |
| 57 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1871 | 9774 |
| 58 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1852 | 21656 |
| 59 | [github/spec-kit](https://github.com/github/spec-kit) | +1848 | 71722 |
| 60 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1801 | 6874 |
| 61 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1783 | 6160 |
| 62 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1737 | 6472 |
| 63 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1719 | 7733 |
| 64 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1705 | 11806 |
| 65 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1701 | 6270 |
| 66 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1685 | 6307 |
| 67 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1684 | 21418 |
| 68 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1682 | 74887 |
| 69 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1678 | 7429 |
| 70 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1674 | 27335 |
| 71 | [tobi/qmd](https://github.com/tobi/qmd) | +1658 | 15131 |
| 72 | [openai/skills](https://github.com/openai/skills) | +1628 | 14122 |
| 73 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1626 | 8782 |
| 74 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1622 | 6674 |
| 75 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1595 | 5727 |
| 76 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1590 | 149018 |
| 77 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1574 | 30309 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1526 | 11849 |
| 79 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1514 | 7135 |
| 80 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1508 | 33712 |
| 81 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1496 | 14762 |
| 82 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1492 | 16180 |
| 83 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1486 | 5811 |
| 84 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1432 | 98536 |
| 85 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1426 | 6673 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1420 | 13221 |
| 87 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1415 | 13830 |
| 88 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1384 | 6844 |
| 89 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1380 | 7338 |
| 90 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1379 | 15548 |
| 91 | [tw93/Mole](https://github.com/tw93/Mole) | +1360 | 36870 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1351 | 6160 |
| 93 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1339 | 37564 |
| 94 | [openai/codex](https://github.com/openai/codex) | +1324 | 61744 |
| 95 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1285 | 7282 |
| 96 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1280 | 6756 |
| 97 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1271 | 5663 |
| 98 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1260 | 5241 |
| 99 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1256 | 6561 |
| 100 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1163 | 22576 |
| 101 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1107 | 87598 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1099 | 27940 |
| 103 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1044 | 12892 |
| 104 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1037 | 43973 |
| 105 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1032 | 4578 |
| 106 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1025 | 5809 |
| 107 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +971 | 3849 |
| 108 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +948 | 25045 |
| 109 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +893 | 3992 |
| 110 | [google/langextract](https://github.com/google/langextract) | +860 | 33636 |
| 111 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +850 | 33776 |
| 112 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +845 | 13011 |
| 113 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +837 | 61818 |
| 114 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +836 | 10713 |
| 115 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +832 | 4977 |
| 116 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +785 | 5484 |
| 117 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +778 | 22875 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +768 | 36799 |
| 119 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +751 | 9604 |
| 120 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +750 | 47122 |
| 121 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +750 | 22941 |
| 122 | [docling-project/docling](https://github.com/docling-project/docling) | +737 | 54041 |
| 123 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +731 | 35735 |
| 124 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +696 | 4079 |
| 125 | [wshobson/agents](https://github.com/wshobson/agents) | +689 | 31166 |
| 126 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +652 | 14355 |
| 127 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +651 | 2809 |
| 128 | [google-research/timesfm](https://github.com/google-research/timesfm) | +649 | 10026 |
| 129 | [jundot/omlx](https://github.com/jundot/omlx) | +632 | 4218 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +628 | 15580 |
| 131 | [aden-hive/hive](https://github.com/aden-hive/hive) | +624 | 9378 |
| 132 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +623 | 14291 |
| 133 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +619 | 2259 |
| 134 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +615 | 4878 |
| 135 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +609 | 7805 |
| 136 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +587 | 47936 |
| 137 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +585 | 15978 |
| 138 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +579 | 17690 |
| 139 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +565 | 1984 |
| 140 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +560 | 1910 |
| 141 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +553 | 30590 |
| 142 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +551 | 7373 |
| 143 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +547 | 9459 |
| 144 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +521 | 1779 |
| 145 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +507 | 2047 |
| 146 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +504 | 1927 |
| 147 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +503 | 2189 |
| 148 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +500 | 3158 |
| 149 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +493 | 44545 |
| 150 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +488 | 4498 |
| 151 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +483 | 15014 |
| 152 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +481 | 16068 |
| 153 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +477 | 44232 |
| 154 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +467 | 9048 |
| 155 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +466 | 3506 |
| 156 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +464 | 39841 |
| 157 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +461 | 1466 |
| 158 | [eooce/python-ws](https://github.com/eooce/python-ws) | +455 | 1718 |
| 159 | [openclaw/skills](https://github.com/openclaw/skills) | +455 | 2789 |
| 160 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +449 | 18080 |
| 161 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +443 | 11261 |
| 162 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +434 | 5062 |
| 163 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +433 | 1311 |
| 164 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +421 | 26328 |
| 165 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +409 | 1525 |
| 166 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +408 | 18585 |
| 167 | [microsoft/qlib](https://github.com/microsoft/qlib) | +405 | 37792 |
| 168 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +402 | 4096 |
| 169 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +399 | 1746 |
| 170 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +398 | 10448 |
| 171 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +396 | 3601 |
| 172 | [apify/agent-skills](https://github.com/apify/agent-skills) | +386 | 1610 |
| 173 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +385 | 1635 |
| 174 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +383 | 26787 |
| 175 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +383 | 2467 |
| 176 | [searxng/searxng](https://github.com/searxng/searxng) | +382 | 26448 |
| 177 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +380 | 1516 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +374 | 5822 |
| 179 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +371 | 9460 |
| 180 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +363 | 10782 |
| 181 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +363 | 11265 |
| 182 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +359 | 24295 |
| 183 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +357 | 5357 |
| 184 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +350 | 1479 |
| 185 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +338 | 712 |
| 186 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +333 | 2774 |
| 187 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +331 | 2164 |
| 188 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +330 | 10126 |
| 189 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +327 | 10692 |
| 190 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +324 | 3544 |
| 191 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +321 | 1506 |
| 192 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +309 | 2550 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +304 | 3414 |
| 194 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +298 | 1371 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +289 | 1232 |
| 196 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +289 | 1963 |
| 197 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +275 | 1191 |
| 198 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +275 | 36103 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +271 | 4427 |
| 200 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +269 | 3791 |
| 201 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +258 | 1239 |
| 202 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +254 | 852 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +254 | 21222 |
| 204 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +253 | 21514 |
| 205 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +243 | 29780 |
| 206 | [robinebers/openusage](https://github.com/robinebers/openusage) | +236 | 1458 |
| 207 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +230 | 5451 |
| 208 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +224 | 854 |
| 209 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 144 |
| 210 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +222 | 878 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +210 | 41086 |
| 212 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +208 | 12935 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +207 | 40265 |
| 214 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +207 | 664 |
| 215 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +204 | 8839 |
| 216 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +203 | 6796 |
| 217 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +201 | 604 |
| 218 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +197 | 28791 |
| 219 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +193 | 8805 |
| 220 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +183 | 816 |
| 221 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +176 | 5053 |
| 222 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +174 | 687 |
| 223 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +173 | 25318 |
| 224 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +168 | 22688 |
| 225 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +165 | 550 |
| 226 | [VonChange/utao](https://github.com/VonChange/utao) | +159 | 3915 |
| 227 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +156 | 33000 |
| 228 | [qist/tvbox](https://github.com/qist/tvbox) | +153 | 8491 |
| 229 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +152 | 1429 |
| 230 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +151 | 552 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +150 | 1388 |
| 232 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +150 | 1929 |
| 233 | [decolua/9router](https://github.com/decolua/9router) | +149 | 897 |
| 234 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +147 | 5101 |
| 235 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +146 | 2371 |
| 236 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +143 | 612 |
| 237 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +142 | 647 |
| 238 | [jgraph/drawio](https://github.com/jgraph/drawio) | +141 | 4108 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +140 | 25911 |
| 240 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +137 | 834 |
| 241 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +137 | 795 |
| 242 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +136 | 531 |
| 243 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +135 | 39596 |
| 244 | [lklynet/aurral](https://github.com/lklynet/aurral) | +134 | 864 |
| 245 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +132 | 1535 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +132 | 12017 |
| 247 | [is-a-dev/register](https://github.com/is-a-dev/register) | +128 | 9963 |
| 248 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +124 | 6973 |
| 249 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +123 | 3425 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +123 | 48784 |
| 251 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +118 | 1847 |
| 252 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +117 | 1217 |
| 253 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +117 | 37313 |
| 254 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +116 | 437 |
| 255 | [fmhy/edit](https://github.com/fmhy/edit) | +116 | 8470 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +116 | 12538 |
| 257 | [expo/skills](https://github.com/expo/skills) | +115 | 1445 |
| 258 | [4ier/neo](https://github.com/4ier/neo) | +114 | 573 |
| 259 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +114 | 3208 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +113 | 9975 |
| 261 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +110 | 746 |
| 262 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +109 | 3141 |
| 263 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +109 | 780 |
| 264 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +109 | 35473 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +108 | 945 |
| 266 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +107 | 862 |
| 267 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +98 | 1041 |
| 268 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +98 | 798 |
| 269 | [skylot/jadx](https://github.com/skylot/jadx) | +96 | 47365 |
| 270 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +95 | 3073 |
| 271 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +95 | 1366 |
| 272 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +95 | 463 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 11092 |
| 274 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +92 | 369 |
| 275 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 948 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +91 | 26842 |
| 277 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +86 | 368 |
| 278 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +84 | 449 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +84 | 8718 |
| 280 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +83 | 509 |
| 281 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +83 | 552 |
| 282 | [apache/kafka](https://github.com/apache/kafka) | +83 | 32043 |
| 283 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +82 | 403 |
| 284 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +81 | 317 |
| 285 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +80 | 2973 |
| 286 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +79 | 298 |
| 287 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +79 | 687 |
| 288 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +79 | 1014 |
| 289 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 237 |
| 290 | [openjdk/jdk](https://github.com/openjdk/jdk) | +77 | 22698 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +75 | 943 |
| 292 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +73 | 1327 |
| 293 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +72 | 21341 |
| 294 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +72 | 3519 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +71 | 1292 |
| 296 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 297 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +70 | 393 |
| 298 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +68 | 7580 |
| 299 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +67 | 12349 |
| 300 | [dataease/dataease](https://github.com/dataease/dataease) | +66 | 23590 |
