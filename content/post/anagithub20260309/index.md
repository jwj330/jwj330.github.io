---
title: "2026-03-09 GitHub增长趋势报告"
description: "1.openclaw+2560 2.agency-agents+1223 3.paperclip+1147 4.everything-claude-code+723 5.RuView+674"
date: 2026-03-09T20:37:50+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-09 20:37:50

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
        'daily': {"categories": ["pingdotgg/t3code", "shareAI-lab/learn-claude-code", "koala73/worldmonitor", "nearai/ironclaw", "googleworkspace/cli", "D4Vinci/Scrapling", "hesamsheikh/awesome-openclaw-usecases", "GoogleCloudPlatform/generative-ai", "openai/symphony", "pbakaus/impeccable", "canopy-network/canopy", "m1k1o/neko", "VoltAgent/awesome-openclaw-skills", "666ghj/MiroFish", "nikopueringer/CorridorKey", "ruvnet/RuView", "affaan-m/everything-claude-code", "paperclipai/paperclip", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [237, 261, 281, 293, 294, 313, 313, 335, 339, 352, 401, 434, 441, 588, 608, 674, 723, 1147, 1223, 2560]},
        'weekly': {"categories": ["anomalyco/opencode", "maderix/ANE", "agentscope-ai/CoPaw", "shanraisshan/claude-code-best-practice", "KeygraphHQ/shannon", "pingdotgg/t3code", "hesamsheikh/awesome-openclaw-usecases", "D4Vinci/Scrapling", "anthropics/skills", "obra/superpowers", "VoltAgent/awesome-openclaw-skills", "openai/symphony", "moeru-ai/airi", "koala73/worldmonitor", "affaan-m/everything-claude-code", "ruvnet/RuView", "msitarzewski/agency-agents", "paperclipai/paperclip", "googleworkspace/cli", "openclaw/openclaw"], "data": [1195, 1274, 1371, 1443, 1523, 1571, 1628, 1647, 1680, 1732, 1932, 2298, 2573, 3033, 3207, 3215, 3393, 3447, 3831, 10964]},
        'monthly': {"categories": ["sickn33/antigravity-awesome-skills", "badlogic/pi-mono", "googleworkspace/cli", "gsd-build/get-shit-done", "qwibitai/nanoclaw", "D4Vinci/Scrapling", "x1xhlol/system-prompts-and-models-of-ai-tools", "KeygraphHQ/shannon", "HKUDS/nanobot", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "sipeed/picoclaw", "obra/superpowers", "affaan-m/everything-claude-code", "zeroclaw-labs/zeroclaw", "ruvnet/RuView", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3801, 3827, 3831, 3885, 4210, 4481, 4590, 4807, 4808, 5222, 5714, 6025, 6051, 7088, 7298, 7323, 7613, 7743, 8947, 32028]}
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
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +2560 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1223 | 17895 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1147 | 13939 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +723 | 51199 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +674 | 33096 |
| 6 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +608 | 3749 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +588 | 10459 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +441 | 33155 |
| 9 | [m1k1o/neko](https://github.com/m1k1o/neko) | +434 | 19158 |
| 10 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +401 | 4708 |
| 11 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +352 | 2831 |
| 12 | [openai/symphony](https://github.com/openai/symphony) | +339 | 10226 |
| 13 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +335 | 15209 |
| 14 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +313 | 22113 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +313 | 27100 |
| 16 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +294 | 17090 |
| 17 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +293 | 8494 |
| 18 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +281 | 34673 |
| 19 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +261 | 24486 |
| 20 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +237 | 5131 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +228 | 31744 |
| 22 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +222 | 31313 |
| 23 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +221 | 3656 |
| 24 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +218 | 13192 |
| 25 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +208 | 13626 |
| 26 | [openai/skills](https://github.com/openai/skills) | +195 | 13578 |
| 27 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +184 | 26968 |
| 28 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +183 | 25249 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +181 | 5372 |
| 30 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +161 | 17897 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +10964 | 224760 |
| 2 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3831 | 17090 |
| 3 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3447 | 13939 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3393 | 17895 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +3215 | 33096 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3207 | 51199 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3033 | 34673 |
| 8 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2573 | 31744 |
| 9 | [openai/symphony](https://github.com/openai/symphony) | +2298 | 10226 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1932 | 33155 |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | +1732 | 60312 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +1680 | 74774 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1647 | 27100 |
| 14 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1628 | 22113 |
| 15 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1571 | 5131 |
| 16 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1523 | 32899 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1443 | 12899 |
| 18 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1371 | 10102 |
| 19 | [maderix/ANE](https://github.com/maderix/ANE) | +1274 | 6021 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1195 | 109881 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1166 | 13192 |
| 22 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1157 | 8494 |
| 23 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1152 | 13626 |
| 24 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1116 | 10459 |
| 25 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1102 | 24486 |
| 26 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1080 | 4708 |
| 27 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +965 | 4624 |
| 28 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +945 | 22286 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +928 | 31313 |
| 30 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +918 | 7671 |
| 31 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +917 | 11388 |
| 32 | [openai/skills](https://github.com/openai/skills) | +889 | 13578 |
| 33 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +873 | 20937 |
| 34 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +869 | 26968 |
| 35 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +810 | 25249 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +806 | 25813 |
| 37 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +784 | 27154 |
| 38 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +784 | 7171 |
| 39 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +778 | 69674 |
| 40 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +772 | 20355 |
| 41 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +766 | 32444 |
| 42 | [superset-sh/superset](https://github.com/superset-sh/superset) | +764 | 6316 |
| 43 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +752 | 14071 |
| 44 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +734 | 5372 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +729 | 17897 |
| 46 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +688 | 5865 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +682 | 21695 |
| 48 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +676 | 3749 |
| 49 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +674 | 37330 |
| 50 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +659 | 34148 |
| 51 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +651 | 20189 |
| 52 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +615 | 15209 |
| 53 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +605 | 2549 |
| 54 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +604 | 33878 |
| 55 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +601 | 3782 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +594 | 14813 |
| 57 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +592 | 8920 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +580 | 2831 |
| 59 | [srizzon/git-city](https://github.com/srizzon/git-city) | +579 | 3330 |
| 60 | [tobi/qmd](https://github.com/tobi/qmd) | +522 | 13634 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +516 | 28918 |
| 62 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +506 | 15260 |
| 63 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +503 | 10678 |
| 64 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +487 | 30412 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +473 | 12233 |
| 66 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +470 | 2459 |
| 67 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +464 | 10717 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +458 | 26290 |
| 69 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +449 | 9185 |
| 70 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +448 | 8005 |
| 71 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +448 | 5920 |
| 72 | [m1k1o/neko](https://github.com/m1k1o/neko) | +447 | 19158 |
| 73 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +439 | 2029 |
| 74 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +431 | 2595 |
| 75 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +422 | 23239 |
| 76 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +412 | 4138 |
| 77 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +399 | 9332 |
| 78 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +385 | 20200 |
| 79 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +382 | 6162 |
| 80 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +380 | 10379 |
| 81 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +380 | 6046 |
| 82 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +367 | 5012 |
| 83 | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | +355 | 2583 |
| 84 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +352 | 5278 |
| 85 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +349 | 30678 |
| 86 | [duoan/TorchCode](https://github.com/duoan/TorchCode) | +348 | 1404 |
| 87 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +346 | 1896 |
| 88 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +346 | 23044 |
| 89 | [slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide) | +344 | 1537 |
| 90 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +329 | 3266 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +328 | 3991 |
| 92 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +327 | 1355 |
| 93 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +324 | 3656 |
| 94 | [cyxzdev/Uncodixfy](https://github.com/cyxzdev/Uncodixfy) | +321 | 1201 |
| 95 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +313 | 27126 |
| 96 | [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) | +312 | 1785 |
| 97 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +303 | 14950 |
| 98 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +300 | 10993 |
| 99 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +295 | 20982 |
| 100 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +293 | 3592 |
| 101 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +287 | 35735 |
| 102 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +284 | 2839 |
| 103 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +282 | 1340 |
| 104 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +273 | 24312 |
| 105 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +273 | 17867 |
| 106 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +271 | 11004 |
| 107 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +271 | 14810 |
| 108 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +265 | 3391 |
| 109 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +250 | 4579 |
| 110 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +227 | 7511 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +224 | 9574 |
| 112 | [wshobson/agents](https://github.com/wshobson/agents) | +222 | 30801 |
| 113 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +221 | 43973 |
| 114 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +213 | 36799 |
| 115 | [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe) | +212 | 2083 |
| 116 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +207 | 924 |
| 117 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +203 | 5318 |
| 118 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +203 | 12482 |
| 119 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +201 | 1161 |
| 120 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +198 | 995 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +32028 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8947 | 34673 |
| 3 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +7743 | 33097 |
| 4 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7613 | 25249 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7323 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +7298 | 60312 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +7088 | 23239 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +6051 | 74774 |
| 9 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +6025 | 22113 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5714 | 33155 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5222 | 109881 |
| 12 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4808 | 31313 |
| 13 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +4807 | 32900 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4590 | 122870 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4481 | 27100 |
| 16 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4210 | 20937 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3885 | 26968 |
| 18 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3831 | 17090 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3827 | 21695 |
| 20 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3801 | 22286 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3686 | 31744 |
| 22 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3667 | 17898 |
| 23 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3648 | 13192 |
| 24 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +3510 | 13626 |
| 25 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3448 | 13939 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3345 | 12796 |
| 27 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3030 | 11388 |
| 28 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2993 | 60117 |
| 29 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2957 | 69674 |
| 30 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2796 | 10102 |
| 31 | [google/langextract](https://github.com/google/langextract) | +2687 | 33636 |
| 32 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2672 | 12900 |
| 33 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2660 | 9307 |
| 34 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2648 | 8787 |
| 35 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2635 | 85286 |
| 36 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2624 | 37330 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2484 | 34148 |
| 38 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2479 | 8920 |
| 39 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2463 | 33878 |
| 40 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2444 | 25813 |
| 41 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2400 | 96919 |
| 42 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2356 | 8494 |
| 43 | [openai/symphony](https://github.com/openai/symphony) | +2299 | 10226 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2249 | 17897 |
| 45 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2224 | 30678 |
| 46 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2105 | 24487 |
| 47 | [huggingface/skills](https://github.com/huggingface/skills) | +2100 | 8626 |
| 48 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1938 | 8784 |
| 49 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1936 | 7671 |
| 50 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1903 | 147486 |
| 51 | [github/spec-kit](https://github.com/github/spec-kit) | +1901 | 71722 |
| 52 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1895 | 9723 |
| 53 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1871 | 6920 |
| 54 | [openai/skills](https://github.com/openai/skills) | +1836 | 13578 |
| 55 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1835 | 20190 |
| 56 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1825 | 27154 |
| 57 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1799 | 20355 |
| 58 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1797 | 11004 |
| 59 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1790 | 20982 |
| 60 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1780 | 9186 |
| 61 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1765 | 14810 |
| 62 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1731 | 6132 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1727 | 26290 |
| 64 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1688 | 6162 |
| 65 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1664 | 74887 |
| 66 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1658 | 6046 |
| 67 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1658 | 149018 |
| 68 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1643 | 7171 |
| 69 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1632 | 10678 |
| 70 | [tobi/qmd](https://github.com/tobi/qmd) | +1621 | 13634 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1573 | 28918 |
| 72 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1571 | 5131 |
| 73 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1563 | 6365 |
| 74 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1556 | 5530 |
| 75 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1535 | 5143 |
| 76 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1534 | 5921 |
| 77 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1522 | 33712 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1504 | 10717 |
| 79 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1493 | 14071 |
| 80 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1462 | 18313 |
| 81 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1454 | 5865 |
| 82 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1440 | 5588 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1434 | 98536 |
| 84 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1421 | 28230 |
| 85 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1420 | 13676 |
| 86 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1400 | 6024 |
| 87 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1397 | 37564 |
| 88 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1395 | 14813 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1388 | 12234 |
| 90 | [tw93/Mole](https://github.com/tw93/Mole) | +1385 | 36870 |
| 91 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1358 | 5372 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1329 | 6021 |
| 93 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1328 | 6316 |
| 94 | [openai/codex](https://github.com/openai/codex) | +1324 | 61744 |
| 95 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1315 | 10460 |
| 96 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1296 | 4666 |
| 97 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1259 | 20200 |
| 98 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1216 | 12765 |
| 99 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1199 | 22496 |
| 100 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1188 | 5318 |
| 101 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1170 | 87598 |
| 102 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1136 | 4625 |
| 103 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1097 | 4708 |
| 104 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +1089 | 8005 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1057 | 27126 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +956 | 24312 |
| 107 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +923 | 3592 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +867 | 61818 |
| 109 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +863 | 22517 |
| 110 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +846 | 12482 |
| 111 | [aden-hive/hive](https://github.com/aden-hive/hive) | +822 | 9023 |
| 112 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +816 | 22550 |
| 113 | [docling-project/docling](https://github.com/docling-project/docling) | +784 | 54041 |
| 114 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +779 | 3082 |
| 115 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +773 | 9294 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +759 | 36799 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +756 | 47122 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +748 | 9574 |
| 119 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +747 | 71086 |
| 120 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +738 | 3750 |
| 121 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +733 | 43973 |
| 122 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +727 | 7511 |
| 123 | [wshobson/agents](https://github.com/wshobson/agents) | +710 | 30801 |
| 124 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +708 | 2839 |
| 125 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +703 | 18430 |
| 126 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +686 | 14116 |
| 127 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +662 | 7332 |
| 128 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +659 | 13799 |
| 129 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +647 | 2205 |
| 130 | [google-research/timesfm](https://github.com/google-research/timesfm) | +646 | 9995 |
| 131 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +630 | 15648 |
| 132 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +626 | 30590 |
| 133 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +624 | 3656 |
| 134 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +619 | 4331 |
| 135 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +615 | 47936 |
| 136 | [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) | +613 | 2593 |
| 137 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +604 | 2549 |
| 138 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +595 | 9274 |
| 139 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +589 | 8827 |
| 140 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +586 | 17629 |
| 141 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +579 | 15260 |
| 142 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +577 | 2831 |
| 143 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +571 | 4918 |
| 144 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +555 | 3421 |
| 145 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +546 | 39841 |
| 146 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +545 | 4138 |
| 147 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +539 | 2165 |
| 148 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +530 | 1734 |
| 149 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +526 | 1819 |
| 150 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +525 | 1361 |
| 151 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +508 | 1686 |
| 152 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +505 | 1999 |
| 153 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +504 | 44545 |
| 154 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +494 | 1892 |
| 155 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +488 | 15923 |
| 156 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +482 | 1406 |
| 157 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +478 | 35735 |
| 158 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +470 | 2721 |
| 159 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +460 | 14950 |
| 160 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +460 | 11759 |
| 161 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +456 | 1447 |
| 162 | [microsoft/qlib](https://github.com/microsoft/qlib) | +449 | 37792 |
| 163 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +447 | 11234 |
| 164 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +443 | 6095 |
| 165 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +439 | 3391 |
| 166 | [eooce/python-ws](https://github.com/eooce/python-ws) | +438 | 1627 |
| 167 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +435 | 1599 |
| 168 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +434 | 17867 |
| 169 | [openclaw/skills](https://github.com/openclaw/skills) | +429 | 2387 |
| 170 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +425 | 25980 |
| 171 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +425 | 14672 |
| 172 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +415 | 3908 |
| 173 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +414 | 44232 |
| 174 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +400 | 6332 |
| 175 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +399 | 1558 |
| 176 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +399 | 10388 |
| 177 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +393 | 10515 |
| 178 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +390 | 5142 |
| 179 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +389 | 3340 |
| 180 | [samugit83/redamon](https://github.com/samugit83/redamon) | +383 | 1521 |
| 181 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +378 | 5569 |
| 182 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +373 | 11260 |
| 183 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +372 | 1431 |
| 184 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +364 | 2249 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +364 | 24131 |
| 186 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +354 | 9201 |
| 187 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +344 | 695 |
| 188 | [apify/agent-skills](https://github.com/apify/agent-skills) | +343 | 1410 |
| 189 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +337 | 1406 |
| 190 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +332 | 3239 |
| 191 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +331 | 1340 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +330 | 36103 |
| 193 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +320 | 2521 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +316 | 3229 |
| 195 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +314 | 1303 |
| 196 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +311 | 9963 |
| 197 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +305 | 2501 |
| 198 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +301 | 1078 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +300 | 4239 |
| 200 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +291 | 1067 |
| 201 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +285 | 1937 |
| 202 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +282 | 36697 |
| 203 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +275 | 3551 |
| 204 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +267 | 8723 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +263 | 21126 |
| 206 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +261 | 1161 |
| 207 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +257 | 1074 |
| 208 | [robinebers/openusage](https://github.com/robinebers/openusage) | +252 | 1354 |
| 209 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +252 | 844 |
| 210 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +251 | 21349 |
| 211 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +245 | 5426 |
| 212 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +236 | 8789 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +231 | 12863 |
| 214 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +227 | 808 |
| 215 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 146 |
| 216 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +221 | 22609 |
| 217 | [usebruno/bruno](https://github.com/usebruno/bruno) | +214 | 41086 |
| 218 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +214 | 740 |
| 219 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +211 | 29780 |
| 220 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +209 | 6652 |
| 221 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +207 | 40265 |
| 222 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 677 |
| 223 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +201 | 597 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +199 | 28656 |
| 225 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +194 | 724 |
| 226 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +185 | 701 |
| 227 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +182 | 2258 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +180 | 3901 |
| 229 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +179 | 1362 |
| 230 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +179 | 680 |
| 231 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +169 | 672 |
| 232 | [qist/tvbox](https://github.com/qist/tvbox) | +169 | 8400 |
| 233 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +163 | 1008 |
| 234 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +162 | 1373 |
| 235 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +161 | 524 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +161 | 33000 |
| 237 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +160 | 4926 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +160 | 1870 |
| 239 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +159 | 5010 |
| 240 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +157 | 3378 |
| 241 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +151 | 556 |
| 242 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 517 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +148 | 25850 |
| 244 | [decolua/9router](https://github.com/decolua/9router) | +144 | 751 |
| 245 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +144 | 519 |
| 246 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +143 | 39596 |
| 247 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +138 | 11923 |
| 248 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +138 | 742 |
| 249 | [lklynet/aurral](https://github.com/lklynet/aurral) | +136 | 843 |
| 250 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +130 | 3090 |
| 251 | [expo/skills](https://github.com/expo/skills) | +128 | 1394 |
| 252 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +127 | 6931 |
| 253 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +127 | 37313 |
| 254 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +125 | 481 |
| 255 | [is-a-dev/register](https://github.com/is-a-dev/register) | +124 | 9922 |
| 256 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +123 | 843 |
| 257 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +123 | 1372 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +120 | 12500 |
| 260 | [fmhy/edit](https://github.com/fmhy/edit) | +119 | 8417 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +117 | 3127 |
| 262 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +116 | 9900 |
| 263 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +113 | 1164 |
| 264 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +111 | 3262 |
| 265 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +110 | 761 |
| 266 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +109 | 385 |
| 267 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +109 | 35473 |
| 268 | [4ier/neo](https://github.com/4ier/neo) | +102 | 518 |
| 269 | [skylot/jadx](https://github.com/skylot/jadx) | +98 | 47365 |
| 270 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +97 | 3059 |
| 271 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +97 | 11005 |
| 272 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +96 | 968 |
| 273 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +96 | 1031 |
| 274 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 339 |
| 275 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +95 | 1649 |
| 276 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +94 | 26777 |
| 277 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +91 | 572 |
| 278 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +86 | 306 |
| 279 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +86 | 877 |
| 280 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +85 | 2911 |
| 281 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +84 | 8644 |
| 282 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +82 | 845 |
| 283 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +81 | 295 |
| 284 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +81 | 307 |
| 285 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +79 | 4549 |
| 286 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +79 | 678 |
| 287 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +78 | 903 |
| 288 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +78 | 28679 |
| 289 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 246 |
| 290 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +76 | 45263 |
| 291 | [openjdk/jdk](https://github.com/openjdk/jdk) | +76 | 22764 |
| 292 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +75 | 301 |
| 293 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +75 | 3491 |
| 294 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +74 | 1317 |
| 295 | [apache/kafka](https://github.com/apache/kafka) | +74 | 32043 |
| 296 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +73 | 256 |
| 297 | [FongMi/TV](https://github.com/FongMi/TV) | +72 | 7502 |
| 298 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +72 | 21312 |
| 299 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +71 | 718 |
| 300 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +71 | 510 |
