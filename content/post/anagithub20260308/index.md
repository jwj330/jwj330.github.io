---
title: "2026-03-08 GitHub增长趋势报告"
description: "1.everything-claude-code+970 2.paperclip+944 3.t3code+700 4.cli+405 5.awesome-openclaw-skills+400"
date: 2026-03-08T20:29:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-08 20:29:45

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
        'daily': {"categories": ["HKUDS/nanobot", "rtk-ai/rtk", "RightNow-AI/openfang", "D4Vinci/Scrapling", "shareAI-lab/learn-claude-code", "ruvnet/RuView", "openai/skills", "hesamsheikh/awesome-openclaw-usecases", "alibaba/page-agent", "koala73/worldmonitor", "openai/symphony", "msitarzewski/agency-agents", "nearai/ironclaw", "moeru-ai/airi", "666ghj/MiroFish", "VoltAgent/awesome-openclaw-skills", "googleworkspace/cli", "pingdotgg/t3code", "paperclipai/paperclip", "affaan-m/everything-claude-code"], "data": [205, 207, 211, 214, 216, 237, 240, 272, 272, 279, 290, 321, 322, 327, 372, 400, 405, 700, 944, 970]},
        'weekly': {"categories": ["maderix/ANE", "pingdotgg/t3code", "shanraisshan/claude-code-best-practice", "KeygraphHQ/shannon", "D4Vinci/Scrapling", "RightNow-AI/openfang", "anthropics/skills", "hesamsheikh/awesome-openclaw-usecases", "agentscope-ai/CoPaw", "obra/superpowers", "VoltAgent/awesome-openclaw-skills", "openai/symphony", "paperclipai/paperclip", "msitarzewski/agency-agents", "moeru-ai/airi", "affaan-m/everything-claude-code", "koala73/worldmonitor", "googleworkspace/cli", "ruvnet/RuView", "openclaw/openclaw"], "data": [1318, 1348, 1406, 1501, 1563, 1652, 1739, 1751, 1768, 1863, 1905, 1988, 2367, 2445, 2758, 3001, 3502, 3558, 4295, 9747]},
        'monthly': {"categories": ["googleworkspace/cli", "sickn33/antigravity-awesome-skills", "badlogic/pi-mono", "gsd-build/get-shit-done", "qwibitai/nanoclaw", "D4Vinci/Scrapling", "x1xhlol/system-prompts-and-models-of-ai-tools", "HKUDS/nanobot", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "KeygraphHQ/shannon", "affaan-m/everything-claude-code", "sipeed/picoclaw", "ruvnet/RuView", "obra/superpowers", "zeroclaw-labs/zeroclaw", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3560, 3761, 3837, 3840, 4181, 4191, 4569, 5134, 5310, 5558, 5828, 6054, 6173, 6931, 7008, 7091, 7396, 7438, 8676, 30790]}
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
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +970 | 51199 |
| 2 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +944 | 10717 |
| 3 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +700 | 4163 |
| 4 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +405 | 16170 |
| 5 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +400 | 31680 |
| 6 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +372 | 6800 |
| 7 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +327 | 31177 |
| 8 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +322 | 7548 |
| 9 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +321 | 12255 |
| 10 | [openai/symphony](https://github.com/openai/symphony) | +290 | 9349 |
| 11 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +279 | 33772 |
| 12 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +272 | 1881 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +272 | 21162 |
| 14 | [openai/skills](https://github.com/openai/skills) | +240 | 13154 |
| 15 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +237 | 30628 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +216 | 23783 |
| 17 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +214 | 26135 |
| 18 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +211 | 12632 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +207 | 4708 |
| 20 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +205 | 30534 |
| 21 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +203 | 17466 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +203 | 26349 |
| 23 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +183 | 25970 |
| 24 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +175 | 14203 |
| 25 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +173 | 4264 |
| 26 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +158 | 8913 |
| 27 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +144 | 4290 |
| 28 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +139 | 22938 |
| 29 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +136 | 9664 |
| 30 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +135 | 7181 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9747 | 224760 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +4295 | 30630 |
| 3 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3558 | 16170 |
| 4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3502 | 33772 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3001 | 51199 |
| 6 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2758 | 31177 |
| 7 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2445 | 12255 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2367 | 10717 |
| 9 | [openai/symphony](https://github.com/openai/symphony) | +1988 | 9349 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1905 | 31680 |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | +1863 | 60312 |
| 12 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1768 | 9664 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1751 | 21162 |
| 14 | [anthropics/skills](https://github.com/anthropics/skills) | +1739 | 74774 |
| 15 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1652 | 12632 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1563 | 26135 |
| 17 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1501 | 32675 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1406 | 12597 |
| 19 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1348 | 4163 |
| 20 | [maderix/ANE](https://github.com/maderix/ANE) | +1318 | 5959 |
| 21 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +1267 | 8741 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1231 | 109881 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1071 | 11048 |
| 24 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1032 | 23783 |
| 25 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1021 | 4264 |
| 26 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1011 | 6898 |
| 27 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +969 | 21762 |
| 28 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +925 | 7181 |
| 29 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +905 | 7548 |
| 30 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +893 | 20398 |
| 31 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +883 | 5602 |
| 32 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +881 | 13766 |
| 33 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +880 | 30534 |
| 34 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +870 | 26349 |
| 35 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +829 | 25970 |
| 36 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +829 | 19975 |
| 37 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +827 | 24634 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +827 | 25306 |
| 39 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +809 | 69674 |
| 40 | [superset-sh/superset](https://github.com/superset-sh/superset) | +808 | 5868 |
| 41 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +771 | 19971 |
| 42 | [openai/skills](https://github.com/openai/skills) | +748 | 13154 |
| 43 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +722 | 37330 |
| 44 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +717 | 32225 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +715 | 21222 |
| 46 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +711 | 3328 |
| 47 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +701 | 4290 |
| 48 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +669 | 17466 |
| 49 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +656 | 3480 |
| 50 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +637 | 34148 |
| 51 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +607 | 5952 |
| 52 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +600 | 4708 |
| 53 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +598 | 6800 |
| 54 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +595 | 33878 |
| 55 | [srizzon/git-city](https://github.com/srizzon/git-city) | +574 | 3149 |
| 56 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +567 | 30412 |
| 57 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +554 | 25980 |
| 58 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +550 | 5946 |
| 59 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +545 | 14400 |
| 60 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +532 | 2956 |
| 61 | [tobi/qmd](https://github.com/tobi/qmd) | +509 | 13399 |
| 62 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +495 | 10437 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +481 | 28562 |
| 64 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +471 | 15176 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +441 | 11904 |
| 66 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +439 | 5695 |
| 67 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +436 | 10345 |
| 68 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +424 | 22921 |
| 69 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +420 | 1966 |
| 70 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +408 | 8913 |
| 71 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +398 | 7721 |
| 72 | [Justsenger/ExHyperV](https://github.com/Justsenger/ExHyperV) | +398 | 2129 |
| 73 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +381 | 10164 |
| 74 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +374 | 30678 |
| 75 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +372 | 6296 |
| 76 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +370 | 20845 |
| 77 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +364 | 1406 |
| 78 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +358 | 9091 |
| 79 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +345 | 19821 |
| 80 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +340 | 8681 |
| 81 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +338 | 1881 |
| 82 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +338 | 22938 |
| 83 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +336 | 4712 |
| 84 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +334 | 14939 |
| 85 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +326 | 5187 |
| 86 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +323 | 14546 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +315 | 36870 |
| 88 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +313 | 1494 |
| 89 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +310 | 3653 |
| 90 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +307 | 3067 |
| 91 | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | +306 | 2308 |
| 92 | [ILoveBingLu/CipherTalk](https://github.com/ILoveBingLu/CipherTalk) | +301 | 1801 |
| 93 | [Ed1s0nZ/CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | +300 | 2201 |
| 94 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 26878 |
| 95 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +295 | 10823 |
| 96 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +290 | 17809 |
| 97 | [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) | +285 | 14203 |
| 98 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +282 | 1129 |
| 99 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +281 | 28102 |
| 100 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +279 | 24140 |
| 101 | [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | +275 | 1559 |
| 102 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +267 | 2273 |
| 103 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +264 | 12682 |
| 104 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +261 | 10864 |
| 105 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +255 | 1672 |
| 106 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +255 | 12721 |
| 107 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +241 | 4550 |
| 108 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +229 | 7457 |
| 109 | [huggingface/skills](https://github.com/huggingface/skills) | +228 | 8525 |
| 110 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +222 | 9461 |
| 111 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +218 | 1611 |
| 112 | [wshobson/agents](https://github.com/wshobson/agents) | +210 | 30670 |
| 113 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +209 | 36799 |
| 114 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +203 | 842 |
| 115 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +203 | 905 |
| 116 | [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe) | +203 | 2022 |
| 117 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +200 | 12321 |
| 118 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +199 | 13590 |
| 119 | [microsoft/fara](https://github.com/microsoft/fara) | +197 | 4347 |
| 120 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +193 | 22411 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30790 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8676 | 33772 |
| 3 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7438 | 24634 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +7396 | 60312 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +7091 | 30631 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +7008 | 22921 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6931 | 51199 |
| 8 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +6173 | 32675 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6054 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5828 | 21162 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5558 | 31680 |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5310 | 109881 |
| 13 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +5134 | 30534 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4569 | 122870 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +4191 | 26135 |
| 16 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4181 | 20398 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3840 | 26349 |
| 18 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3837 | 21222 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3761 | 21762 |
| 20 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3560 | 16170 |
| 21 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3491 | 31177 |
| 22 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3463 | 12632 |
| 23 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3351 | 12682 |
| 24 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3061 | 60117 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2936 | 69674 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2911 | 11049 |
| 27 | [google/langextract](https://github.com/google/langextract) | +2843 | 33636 |
| 28 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2748 | 37330 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2737 | 12597 |
| 30 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2683 | 9664 |
| 31 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2643 | 9245 |
| 32 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2642 | 8748 |
| 33 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2567 | 85286 |
| 34 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2527 | 30678 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2525 | 34148 |
| 36 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2490 | 33878 |
| 37 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2452 | 12255 |
| 38 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2440 | 8741 |
| 39 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2409 | 25306 |
| 40 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2399 | 96919 |
| 41 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2368 | 10718 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2143 | 17466 |
| 43 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2076 | 7548 |
| 44 | [huggingface/skills](https://github.com/huggingface/skills) | +2076 | 8525 |
| 45 | [openai/skills](https://github.com/openai/skills) | +2007 | 13154 |
| 46 | [openai/symphony](https://github.com/openai/symphony) | +1992 | 9349 |
| 47 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1914 | 8681 |
| 48 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1902 | 9704 |
| 49 | [github/spec-kit](https://github.com/github/spec-kit) | +1893 | 71722 |
| 50 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1892 | 23783 |
| 51 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1848 | 20845 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1842 | 147486 |
| 53 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1839 | 6821 |
| 54 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1822 | 10864 |
| 55 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1819 | 7181 |
| 56 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1786 | 19971 |
| 57 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1783 | 19975 |
| 58 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1741 | 14546 |
| 59 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1728 | 25970 |
| 60 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1721 | 6063 |
| 61 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1708 | 8913 |
| 62 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1674 | 25980 |
| 63 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1670 | 149018 |
| 64 | [virattt/dexter](https://github.com/virattt/dexter) | +1651 | 17337 |
| 65 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1643 | 74887 |
| 66 | [tobi/qmd](https://github.com/tobi/qmd) | +1640 | 13399 |
| 67 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1632 | 5952 |
| 68 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1622 | 18199 |
| 69 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1600 | 5946 |
| 70 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1591 | 10437 |
| 71 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1576 | 6898 |
| 72 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1550 | 6296 |
| 73 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1544 | 28562 |
| 74 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1538 | 5435 |
| 75 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1529 | 5123 |
| 76 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1525 | 9080 |
| 77 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1523 | 33712 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1517 | 10345 |
| 79 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1508 | 5695 |
| 80 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1477 | 13766 |
| 81 | [tw93/Mole](https://github.com/tw93/Mole) | +1448 | 36870 |
| 82 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1421 | 5539 |
| 83 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1421 | 37564 |
| 84 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1412 | 13590 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1412 | 98536 |
| 86 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1410 | 5602 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1410 | 11904 |
| 88 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1408 | 28102 |
| 89 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1384 | 5895 |
| 90 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1348 | 4164 |
| 91 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1338 | 14400 |
| 92 | [openai/codex](https://github.com/openai/codex) | +1324 | 61744 |
| 93 | [maderix/ANE](https://github.com/maderix/ANE) | +1318 | 5959 |
| 94 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1275 | 4602 |
| 95 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1264 | 12721 |
| 96 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1225 | 22458 |
| 97 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1196 | 5868 |
| 98 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1193 | 4708 |
| 99 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1179 | 19821 |
| 100 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1162 | 87598 |
| 101 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1152 | 5050 |
| 102 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1085 | 3899 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1046 | 26878 |
| 104 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1026 | 4264 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +944 | 24140 |
| 106 | [aden-hive/hive](https://github.com/aden-hive/hive) | +912 | 9004 |
| 107 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +896 | 3480 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +884 | 61818 |
| 109 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +877 | 22395 |
| 110 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +853 | 12321 |
| 111 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +831 | 22411 |
| 112 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +803 | 7457 |
| 113 | [docling-project/docling](https://github.com/docling-project/docling) | +798 | 54041 |
| 114 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +778 | 9224 |
| 115 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +777 | 6800 |
| 116 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +770 | 47122 |
| 117 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +760 | 36799 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +753 | 9461 |
| 119 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +749 | 2957 |
| 120 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +734 | 18377 |
| 121 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +732 | 71086 |
| 122 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +713 | 4290 |
| 123 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +710 | 14085 |
| 124 | [wshobson/agents](https://github.com/wshobson/agents) | +708 | 30670 |
| 125 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +701 | 43973 |
| 126 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +698 | 4860 |
| 127 | [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) | +677 | 2574 |
| 128 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +663 | 7322 |
| 129 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +662 | 13718 |
| 130 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +654 | 15562 |
| 131 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +648 | 8760 |
| 132 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +648 | 4287 |
| 133 | [google-research/timesfm](https://github.com/google-research/timesfm) | +644 | 9985 |
| 134 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +641 | 2195 |
| 135 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +629 | 30590 |
| 136 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +627 | 47936 |
| 137 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +621 | 9218 |
| 138 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +613 | 2273 |
| 139 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +586 | 17616 |
| 140 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +570 | 3421 |
| 141 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +556 | 2350 |
| 142 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +545 | 39841 |
| 143 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +537 | 15176 |
| 144 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +534 | 1356 |
| 145 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +532 | 2154 |
| 146 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +524 | 1417 |
| 147 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +518 | 1672 |
| 148 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +512 | 11725 |
| 149 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +506 | 15893 |
| 150 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +505 | 1979 |
| 151 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +505 | 1674 |
| 152 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +492 | 1882 |
| 153 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +490 | 44545 |
| 154 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +485 | 1611 |
| 155 | [microsoft/qlib](https://github.com/microsoft/qlib) | +461 | 37792 |
| 156 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +455 | 14939 |
| 157 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +454 | 1444 |
| 158 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +446 | 11228 |
| 159 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +443 | 2571 |
| 160 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +439 | 6080 |
| 161 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +436 | 3653 |
| 162 | [samugit83/redamon](https://github.com/samugit83/redamon) | +435 | 1506 |
| 163 | [eooce/python-ws](https://github.com/eooce/python-ws) | +432 | 1597 |
| 164 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +430 | 3843 |
| 165 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +428 | 17809 |
| 166 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +427 | 3127 |
| 167 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +426 | 25879 |
| 168 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +410 | 1544 |
| 169 | [Free-TV/IPTV](https://github.com/Free-TV/IPTV) | +410 | 14592 |
| 170 | [openclaw/skills](https://github.com/openclaw/skills) | +406 | 2264 |
| 171 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +401 | 6282 |
| 172 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +401 | 5054 |
| 173 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +400 | 44232 |
| 174 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +399 | 10360 |
| 175 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +394 | 3279 |
| 176 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +393 | 10370 |
| 177 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +392 | 14026 |
| 178 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +383 | 1505 |
| 179 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +383 | 5518 |
| 180 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +378 | 36103 |
| 181 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +366 | 11215 |
| 182 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +364 | 1406 |
| 183 | [oraios/serena](https://github.com/oraios/serena) | +363 | 21150 |
| 184 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | +362 | 40916 |
| 185 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +358 | 35735 |
| 186 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +355 | 9129 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +355 | 24079 |
| 188 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +352 | 2185 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +341 | 3188 |
| 190 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +339 | 688 |
| 191 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +334 | 2909 |
| 192 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +331 | 1372 |
| 193 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +329 | 2459 |
| 194 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +313 | 36697 |
| 195 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +310 | 1494 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +307 | 4187 |
| 197 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +301 | 1264 |
| 198 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +300 | 2479 |
| 199 | [apify/agent-skills](https://github.com/apify/agent-skills) | +294 | 1284 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +292 | 9867 |
| 201 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +290 | 1056 |
| 202 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +289 | 1033 |
| 203 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +281 | 1929 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +277 | 21098 |
| 205 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +276 | 8779 |
| 206 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +269 | 3460 |
| 207 | [robinebers/openusage](https://github.com/robinebers/openusage) | +261 | 1311 |
| 208 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +253 | 5423 |
| 209 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +252 | 21303 |
| 210 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +251 | 841 |
| 211 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +251 | 8644 |
| 212 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +239 | 12845 |
| 213 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +233 | 1021 |
| 214 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 273 |
| 215 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +223 | 787 |
| 216 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +220 | 22593 |
| 217 | [usebruno/bruno](https://github.com/usebruno/bruno) | +218 | 41086 |
| 218 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +213 | 1345 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +213 | 40265 |
| 220 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +213 | 738 |
| 221 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +209 | 6626 |
| 222 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +206 | 29780 |
| 223 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 677 |
| 224 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +206 | 794 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +206 | 28640 |
| 226 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +199 | 595 |
| 227 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +193 | 686 |
| 228 | [VonChange/utao](https://github.com/VonChange/utao) | +184 | 3898 |
| 229 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +183 | 2254 |
| 230 | [qist/tvbox](https://github.com/qist/tvbox) | +179 | 8388 |
| 231 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +174 | 555 |
| 232 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +173 | 3362 |
| 233 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +169 | 668 |
| 234 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +163 | 607 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +162 | 1848 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +162 | 33000 |
| 237 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +161 | 515 |
| 238 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +161 | 645 |
| 239 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +158 | 4991 |
| 240 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +156 | 4844 |
| 241 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +156 | 1321 |
| 242 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +151 | 727 |
| 243 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +149 | 39596 |
| 244 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 515 |
| 245 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +148 | 25829 |
| 246 | [decolua/9router](https://github.com/decolua/9router) | +141 | 712 |
| 247 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +141 | 505 |
| 248 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +139 | 3081 |
| 249 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +138 | 834 |
| 250 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +137 | 11892 |
| 251 | [lklynet/aurral](https://github.com/lklynet/aurral) | +130 | 825 |
| 252 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +129 | 6917 |
| 253 | [expo/skills](https://github.com/expo/skills) | +129 | 1377 |
| 254 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +126 | 37313 |
| 255 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +124 | 1359 |
| 256 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +123 | 9882 |
| 257 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +122 | 471 |
| 258 | [microg/GmsCore](https://github.com/microg/GmsCore) | +121 | 12496 |
| 259 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +121 | 48784 |
| 260 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +119 | 411 |
| 261 | [fmhy/edit](https://github.com/fmhy/edit) | +119 | 8404 |
| 262 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +118 | 960 |
| 263 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +118 | 440 |
| 264 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +116 | 3112 |
| 265 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 387 |
| 266 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +114 | 748 |
| 267 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +113 | 1151 |
| 268 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +109 | 3253 |
| 269 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +105 | 377 |
| 270 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +104 | 35473 |
| 271 | [skylot/jadx](https://github.com/skylot/jadx) | +101 | 47365 |
| 272 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +96 | 1030 |
| 273 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +96 | 26769 |
| 274 | [4ier/neo](https://github.com/4ier/neo) | +95 | 502 |
| 275 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 338 |
| 276 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 10990 |
| 277 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +90 | 3046 |
| 278 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +88 | 1622 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +88 | 8624 |
| 280 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +86 | 557 |
| 281 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +85 | 4537 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +82 | 2896 |
| 283 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +82 | 3477 |
| 284 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +81 | 858 |
| 285 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +81 | 841 |
| 286 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +80 | 28672 |
| 287 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +79 | 893 |
| 288 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 302 |
| 289 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +77 | 676 |
| 290 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +77 | 243 |
| 291 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +76 | 5851 |
| 292 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +75 | 299 |
| 293 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1316 |
| 294 | [openjdk/jdk](https://github.com/openjdk/jdk) | +75 | 22710 |
| 295 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +75 | 45263 |
| 296 | [apache/kafka](https://github.com/apache/kafka) | +73 | 32043 |
| 297 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +73 | 26496 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +72 | 1240 |
| 299 | [FongMi/TV](https://github.com/FongMi/TV) | +72 | 7493 |
| 300 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +72 | 12315 |
