---
title: "2026-03-07 GitHub增长趋势报告"
description: "1.t3code+702 2.paperclip+592 3.symphony+490 4.cli+419 5.agency-agents+364"
date: 2026-03-07T20:28:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-07 20:28:23

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
        'daily': {"categories": ["rtk-ai/rtk", "QwenLM/Qwen-Agent", "sickn33/antigravity-awesome-skills", "blackboardsh/electrobun", "shanraisshan/claude-code-best-practice", "hesamsheikh/awesome-openclaw-usecases", "D4Vinci/Scrapling", "ruvnet/RuView", "RightNow-AI/openfang", "koala73/worldmonitor", "VoltAgent/awesome-openclaw-skills", "openai/skills", "shareAI-lab/learn-claude-code", "nearai/ironclaw", "moeru-ai/airi", "msitarzewski/agency-agents", "googleworkspace/cli", "openai/symphony", "paperclipai/paperclip", "pingdotgg/t3code"], "data": [129, 139, 139, 141, 161, 168, 169, 169, 172, 221, 223, 235, 259, 337, 364, 364, 419, 490, 592, 702]},
        'weekly': {"categories": ["alibaba/OpenSandbox", "shanraisshan/claude-code-best-practice", "paperclipai/paperclip", "KeygraphHQ/shannon", "D4Vinci/Scrapling", "saturndec/waoowaoo", "openai/symphony", "anthropics/skills", "VoltAgent/awesome-openclaw-skills", "obra/superpowers", "hesamsheikh/awesome-openclaw-usecases", "RightNow-AI/openfang", "msitarzewski/agency-agents", "agentscope-ai/CoPaw", "affaan-m/everything-claude-code", "moeru-ai/airi", "googleworkspace/cli", "koala73/worldmonitor", "ruvnet/RuView", "openclaw/openclaw"], "data": [1337, 1393, 1450, 1488, 1598, 1669, 1728, 1770, 1899, 1976, 2099, 2133, 2138, 2209, 2369, 2750, 3171, 3726, 5548, 9176]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "badlogic/pi-mono", "D4Vinci/Scrapling", "qwibitai/nanoclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "HKUDS/nanobot", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "affaan-m/everything-claude-code", "ruvnet/RuView", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "KeygraphHQ/shannon", "obra/superpowers", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3287, 3707, 3734, 3822, 3985, 4175, 4505, 5387, 5387, 5429, 5571, 6010, 6209, 6877, 6941, 7318, 7433, 7498, 8418, 30305]}
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
| 1 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +702 | 3221 |
| 2 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +592 | 7656 |
| 3 | [openai/symphony](https://github.com/openai/symphony) | +490 | 8427 |
| 4 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +419 | 15137 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +364 | 10677 |
| 6 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +364 | 30480 |
| 7 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +337 | 6801 |
| 8 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +259 | 23139 |
| 9 | [openai/skills](https://github.com/openai/skills) | +235 | 12635 |
| 10 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +223 | 30571 |
| 11 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +221 | 33126 |
| 12 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +172 | 11928 |
| 13 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +169 | 29432 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +169 | 25422 |
| 15 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +168 | 20409 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +161 | 12269 |
| 17 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +141 | 8623 |
| 18 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +139 | 21373 |
| 19 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +139 | 14973 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +129 | 4174 |
| 21 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +119 | 9971 |
| 22 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +112 | 25030 |
| 23 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +112 | 25545 |
| 24 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +104 | 24268 |
| 25 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +101 | 20035 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +101 | 10734 |
| 27 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +99 | 5547 |
| 28 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +98 | 7441 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +96 | 29941 |
| 30 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +95 | 32531 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9176 | 224760 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +5548 | 29432 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3726 | 33126 |
| 4 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3171 | 15137 |
| 5 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2750 | 30480 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2369 | 51199 |
| 7 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2209 | 9341 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2138 | 10677 |
| 9 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2133 | 11928 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2099 | 20409 |
| 11 | [obra/superpowers](https://github.com/obra/superpowers) | +1976 | 60312 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1899 | 30571 |
| 13 | [anthropics/skills](https://github.com/anthropics/skills) | +1770 | 74774 |
| 14 | [openai/symphony](https://github.com/openai/symphony) | +1728 | 8427 |
| 15 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +1669 | 8636 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1598 | 25422 |
| 17 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1488 | 32531 |
| 18 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1450 | 7658 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1393 | 12269 |
| 20 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1337 | 6696 |
| 21 | [maderix/ANE](https://github.com/maderix/ANE) | +1303 | 5917 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1257 | 109881 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1138 | 10734 |
| 24 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1073 | 21373 |
| 25 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1024 | 19746 |
| 26 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +986 | 5506 |
| 27 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +952 | 20035 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +943 | 23139 |
| 29 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +921 | 13587 |
| 30 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +905 | 24268 |
| 31 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +886 | 25693 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +881 | 25030 |
| 33 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +880 | 69674 |
| 34 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +851 | 3868 |
| 35 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +841 | 5849 |
| 36 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +838 | 25545 |
| 37 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +828 | 29941 |
| 38 | [superset-sh/superset](https://github.com/superset-sh/superset) | +802 | 5515 |
| 39 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +763 | 19761 |
| 40 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +762 | 20969 |
| 41 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +733 | 3321 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +722 | 37330 |
| 43 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +704 | 3221 |
| 44 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +674 | 2866 |
| 45 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +643 | 3105 |
| 46 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +633 | 34148 |
| 47 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +631 | 6801 |
| 48 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +627 | 33878 |
| 49 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +593 | 32009 |
| 50 | [openai/skills](https://github.com/openai/skills) | +585 | 12635 |
| 51 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +579 | 25806 |
| 52 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +570 | 5794 |
| 53 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +565 | 16993 |
| 54 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +562 | 2988 |
| 55 | [srizzon/git-city](https://github.com/srizzon/git-city) | +534 | 2985 |
| 56 | [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | +529 | 30412 |
| 57 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +516 | 14170 |
| 58 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +498 | 10281 |
| 59 | [tobi/qmd](https://github.com/tobi/qmd) | +483 | 13203 |
| 60 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +474 | 1582 |
| 61 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +467 | 4174 |
| 62 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +465 | 20754 |
| 63 | [taigrr/spank](https://github.com/taigrr/spank) | +465 | 2155 |
| 64 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +444 | 22727 |
| 65 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +442 | 10158 |
| 66 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +438 | 6245 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +437 | 28360 |
| 68 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +435 | 1638 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +425 | 11669 |
| 70 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +412 | 30678 |
| 71 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +399 | 14917 |
| 72 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +393 | 12680 |
| 73 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +392 | 5469 |
| 74 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +390 | 1907 |
| 75 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +384 | 8588 |
| 76 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +360 | 1383 |
| 77 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +359 | 14973 |
| 78 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +351 | 8893 |
| 79 | [Justsenger/ExHyperV](https://github.com/Justsenger/ExHyperV) | +340 | 2000 |
| 80 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +340 | 14432 |
| 81 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +337 | 4574 |
| 82 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +333 | 7441 |
| 83 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +329 | 9971 |
| 84 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +322 | 19592 |
| 85 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +317 | 5118 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +307 | 36870 |
| 87 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +303 | 5031 |
| 88 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +301 | 26721 |
| 89 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +292 | 3843 |
| 90 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +291 | 2016 |
| 91 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +287 | 8623 |
| 92 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +286 | 24044 |
| 93 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +283 | 17759 |
| 94 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +281 | 1433 |
| 95 | [slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide) | +278 | 1324 |
| 96 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +277 | 2922 |
| 97 | [ILoveBingLu/CipherTalk](https://github.com/ILoveBingLu/CipherTalk) | +276 | 1732 |
| 98 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +268 | 5491 |
| 99 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +266 | 10699 |
| 100 | [puaclaw/PUAClaw](https://github.com/puaclaw/PUAClaw) | +263 | 1129 |
| 101 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +256 | 13549 |
| 102 | [huggingface/skills](https://github.com/huggingface/skills) | +255 | 8452 |
| 103 | [eooce/python-ws](https://github.com/eooce/python-ws) | +254 | 1571 |
| 104 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +246 | 1041 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +246 | 3401 |
| 106 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +238 | 5547 |
| 107 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +234 | 1485 |
| 108 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +227 | 36799 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +226 | 22319 |
| 110 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +223 | 10730 |
| 111 | [inclusionAI/AReaL](https://github.com/inclusionAI/AReaL) | +221 | 4519 |
| 112 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +219 | 7384 |
| 113 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +205 | 12226 |
| 114 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +203 | 6743 |
| 115 | [wshobson/agents](https://github.com/wshobson/agents) | +199 | 30488 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +198 | 9364 |
| 117 | [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe) | +197 | 2009 |
| 118 | [microsoft/fara](https://github.com/microsoft/fara) | +190 | 4312 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +189 | 15499 |
| 120 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +186 | 4944 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30305 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8418 | 33126 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +7498 | 60312 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +7433 | 32531 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7318 | 24268 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6941 | 22727 |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6877 | 29432 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6209 | 51199 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6010 | 74774 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5571 | 20409 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5429 | 30571 |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5387 | 109881 |
| 13 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +5387 | 29941 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4505 | 122870 |
| 15 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4175 | 20035 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3985 | 25422 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3822 | 20969 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3734 | 25693 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3707 | 21373 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3287 | 12439 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3262 | 11928 |
| 22 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3186 | 30480 |
| 23 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3171 | 15137 |
| 24 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3072 | 60117 |
| 25 | [google/langextract](https://github.com/google/langextract) | +3004 | 33636 |
| 26 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2958 | 37330 |
| 27 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2918 | 69674 |
| 28 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2900 | 12269 |
| 29 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2799 | 10734 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2709 | 30678 |
| 31 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2632 | 9208 |
| 32 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2632 | 8732 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2607 | 34148 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2592 | 85286 |
| 35 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2560 | 9341 |
| 36 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2540 | 33878 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2417 | 8636 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2399 | 25030 |
| 39 | [openai/skills](https://github.com/openai/skills) | +2337 | 12635 |
| 40 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2284 | 96919 |
| 41 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2144 | 10677 |
| 42 | [huggingface/skills](https://github.com/huggingface/skills) | +2044 | 8452 |
| 43 | [virattt/dexter](https://github.com/virattt/dexter) | +2013 | 17291 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1987 | 16993 |
| 45 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1905 | 9686 |
| 46 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1901 | 20754 |
| 47 | [github/spec-kit](https://github.com/github/spec-kit) | +1898 | 71722 |
| 48 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1878 | 8588 |
| 49 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1878 | 10730 |
| 50 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1812 | 6743 |
| 51 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1778 | 19761 |
| 52 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1768 | 6801 |
| 53 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1746 | 147486 |
| 54 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1737 | 18123 |
| 55 | [openai/symphony](https://github.com/openai/symphony) | +1729 | 8427 |
| 56 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1716 | 23139 |
| 57 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1705 | 19746 |
| 58 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1701 | 6018 |
| 59 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1697 | 14432 |
| 60 | [tobi/qmd](https://github.com/tobi/qmd) | +1661 | 13203 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1658 | 25806 |
| 62 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1640 | 149018 |
| 63 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1605 | 5849 |
| 64 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1591 | 74887 |
| 65 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1588 | 10158 |
| 66 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1575 | 5794 |
| 67 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1565 | 8623 |
| 68 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1564 | 25545 |
| 69 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1561 | 10281 |
| 70 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1538 | 6245 |
| 71 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1530 | 5393 |
| 72 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1522 | 5118 |
| 73 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1520 | 9065 |
| 74 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1515 | 6696 |
| 75 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1515 | 33712 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1513 | 28360 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1501 | 11669 |
| 78 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1462 | 13587 |
| 79 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1451 | 7658 |
| 80 | [tw93/Mole](https://github.com/tw93/Mole) | +1450 | 36870 |
| 81 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1447 | 37564 |
| 82 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1419 | 5469 |
| 83 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1412 | 5491 |
| 84 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1411 | 13549 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1402 | 98536 |
| 86 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1374 | 5848 |
| 87 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1371 | 5506 |
| 88 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1336 | 27964 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1316 | 14170 |
| 90 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1308 | 12680 |
| 91 | [openai/codex](https://github.com/openai/codex) | +1304 | 61744 |
| 92 | [maderix/ANE](https://github.com/maderix/ANE) | +1303 | 5917 |
| 93 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1258 | 4577 |
| 94 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1218 | 22405 |
| 95 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1140 | 87598 |
| 96 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1137 | 4944 |
| 97 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1132 | 8962 |
| 98 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1132 | 7126 |
| 99 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1123 | 19592 |
| 100 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1078 | 5515 |
| 101 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1069 | 3843 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1028 | 26721 |
| 103 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +936 | 24044 |
| 104 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +891 | 22316 |
| 105 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +887 | 61818 |
| 106 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +882 | 7384 |
| 107 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +851 | 3868 |
| 108 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +851 | 12226 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +847 | 22319 |
| 110 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +829 | 3321 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +826 | 18323 |
| 112 | [docling-project/docling](https://github.com/docling-project/docling) | +797 | 54041 |
| 113 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +773 | 9168 |
| 114 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +772 | 47122 |
| 115 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +769 | 4819 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +761 | 36799 |
| 117 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +760 | 8720 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +748 | 9364 |
| 119 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +726 | 71086 |
| 120 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +719 | 14024 |
| 121 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +717 | 2866 |
| 122 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +688 | 7320 |
| 123 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +673 | 43973 |
| 124 | [wshobson/agents](https://github.com/wshobson/agents) | +671 | 30488 |
| 125 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +667 | 15499 |
| 126 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +666 | 13651 |
| 127 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +645 | 4246 |
| 128 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +639 | 30590 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +639 | 9974 |
| 130 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +638 | 2183 |
| 131 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +631 | 47936 |
| 132 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +629 | 9163 |
| 133 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +586 | 17611 |
| 134 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +573 | 2988 |
| 135 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +570 | 3422 |
| 136 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +546 | 2017 |
| 137 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +544 | 11697 |
| 138 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +541 | 39841 |
| 139 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +528 | 2138 |
| 140 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +526 | 1314 |
| 141 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +525 | 15863 |
| 142 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +523 | 1414 |
| 143 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +505 | 1670 |
| 144 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +504 | 1959 |
| 145 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +501 | 1638 |
| 146 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +484 | 1869 |
| 147 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +472 | 1582 |
| 148 | [microsoft/qlib](https://github.com/microsoft/qlib) | +471 | 37792 |
| 149 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +469 | 44545 |
| 150 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +452 | 1439 |
| 151 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +450 | 5547 |
| 152 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +446 | 14917 |
| 153 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +443 | 11218 |
| 154 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +440 | 3800 |
| 155 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +437 | 6076 |
| 156 | [samugit83/redamon](https://github.com/samugit83/redamon) | +433 | 1498 |
| 157 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +426 | 25809 |
| 158 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +423 | 14974 |
| 159 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +423 | 2473 |
| 160 | [eooce/python-ws](https://github.com/eooce/python-ws) | +418 | 1571 |
| 161 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +417 | 2703 |
| 162 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +417 | 4215 |
| 163 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +405 | 17759 |
| 164 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +404 | 14014 |
| 165 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +397 | 44232 |
| 166 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +396 | 1485 |
| 167 | [openclaw/skills](https://github.com/openclaw/skills) | +395 | 2190 |
| 168 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +395 | 5016 |
| 169 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +395 | 10357 |
| 170 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +394 | 6248 |
| 171 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +392 | 10333 |
| 172 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +388 | 3251 |
| 173 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +384 | 36103 |
| 174 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +383 | 5461 |
| 175 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +380 | 3401 |
| 176 | [oraios/serena](https://github.com/oraios/serena) | +372 | 21131 |
| 177 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +371 | 1296 |
| 178 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +370 | 1463 |
| 179 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +366 | 11179 |
| 180 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +365 | 8768 |
| 181 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +360 | 1383 |
| 182 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +358 | 2418 |
| 183 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | +358 | 40916 |
| 184 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +356 | 9075 |
| 185 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +355 | 15342 |
| 186 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +346 | 3159 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +341 | 24040 |
| 188 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +339 | 2121 |
| 189 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +336 | 671 |
| 190 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +321 | 35735 |
| 191 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +321 | 1336 |
| 192 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +311 | 36697 |
| 193 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +303 | 4141 |
| 194 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +301 | 24203 |
| 195 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +300 | 9838 |
| 196 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +293 | 2457 |
| 197 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +292 | 1229 |
| 198 | [robinebers/openusage](https://github.com/robinebers/openusage) | +292 | 1280 |
| 199 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +286 | 1042 |
| 200 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +286 | 1008 |
| 201 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +279 | 1433 |
| 202 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +273 | 3399 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +268 | 21069 |
| 204 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +255 | 1318 |
| 205 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +254 | 5419 |
| 206 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +254 | 1883 |
| 207 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +251 | 840 |
| 208 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +240 | 21270 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +235 | 41086 |
| 210 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +235 | 12825 |
| 211 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 275 |
| 212 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +223 | 22578 |
| 213 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +220 | 6600 |
| 214 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +216 | 777 |
| 215 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +212 | 737 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +211 | 40265 |
| 217 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +211 | 28620 |
| 218 | [apify/agent-skills](https://github.com/apify/agent-skills) | +208 | 1115 |
| 219 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +208 | 961 |
| 220 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +208 | 2662 |
| 221 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +207 | 791 |
| 222 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 676 |
| 223 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +198 | 593 |
| 224 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +193 | 29780 |
| 225 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +189 | 667 |
| 226 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +188 | 8573 |
| 227 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +184 | 560 |
| 228 | [qist/tvbox](https://github.com/qist/tvbox) | +183 | 8373 |
| 229 | [VonChange/utao](https://github.com/VonChange/utao) | +183 | 3895 |
| 230 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +182 | 2255 |
| 231 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +178 | 3354 |
| 232 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +170 | 39596 |
| 233 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +166 | 1167 |
| 234 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +165 | 33000 |
| 235 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +164 | 1310 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +160 | 1834 |
| 237 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +158 | 510 |
| 238 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +157 | 561 |
| 239 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +155 | 657 |
| 240 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +154 | 720 |
| 241 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +152 | 4831 |
| 242 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +152 | 4969 |
| 243 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +151 | 606 |
| 244 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +148 | 509 |
| 245 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +147 | 25819 |
| 246 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +145 | 832 |
| 247 | [yousifamanuel/terraink](https://github.com/yousifamanuel/terraink) | +144 | 709 |
| 248 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +144 | 3070 |
| 249 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +140 | 501 |
| 250 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +136 | 6907 |
| 251 | [decolua/9router](https://github.com/decolua/9router) | +136 | 701 |
| 252 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +134 | 11845 |
| 253 | [expo/skills](https://github.com/expo/skills) | +133 | 1367 |
| 254 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +131 | 37313 |
| 255 | [lklynet/aurral](https://github.com/lklynet/aurral) | +130 | 809 |
| 256 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +126 | 652 |
| 257 | [fmhy/edit](https://github.com/fmhy/edit) | +126 | 8384 |
| 258 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +125 | 955 |
| 259 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +123 | 1352 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +123 | 9867 |
| 261 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +123 | 48784 |
| 262 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +120 | 744 |
| 263 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 387 |
| 264 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +115 | 3102 |
| 265 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +115 | 406 |
| 266 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +115 | 1138 |
| 267 | [microg/GmsCore](https://github.com/microg/GmsCore) | +113 | 12487 |
| 268 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +107 | 3251 |
| 269 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +102 | 35473 |
| 270 | [skylot/jadx](https://github.com/skylot/jadx) | +101 | 47365 |
| 271 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +98 | 364 |
| 272 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +98 | 392 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +97 | 10981 |
| 274 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +96 | 26761 |
| 275 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +95 | 4535 |
| 276 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +93 | 1026 |
| 277 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +93 | 337 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +88 | 8615 |
| 279 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +87 | 1611 |
| 280 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +86 | 294 |
| 281 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +85 | 834 |
| 282 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +85 | 28664 |
| 283 | [4ier/neo](https://github.com/4ier/neo) | +80 | 476 |
| 284 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +80 | 846 |
| 285 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +80 | 2885 |
| 286 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +80 | 3466 |
| 287 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +79 | 884 |
| 288 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 299 |
| 289 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +79 | 1224 |
| 290 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +78 | 549 |
| 291 | [openjdk/jdk](https://github.com/openjdk/jdk) | +78 | 22710 |
| 292 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 293 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +76 | 672 |
| 294 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +76 | 5846 |
| 295 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1316 |
| 296 | [apache/kafka](https://github.com/apache/kafka) | +75 | 32043 |
| 297 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +74 | 238 |
| 298 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +74 | 244 |
| 299 | [FongMi/TV](https://github.com/FongMi/TV) | +74 | 7487 |
| 300 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +73 | 7536 |
