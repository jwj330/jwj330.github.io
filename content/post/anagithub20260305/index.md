---
title: "2026-03-05 GitHub增长趋势报告"
description: "1.airi+714 2.symphony+699 3.shannon+601 4.worldmonitor+431 5.agency-agents+388"
date: 2026-03-05T20:40:04+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-05 20:40:04

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
        'daily': {"categories": ["alibaba/OpenSandbox", "farion1231/cc-switch", "smartcmd/MinecraftConsoles", "canopy-network/canopy", "agentscope-ai/CoPaw", "K-Dense-AI/claude-scientific-skills", "srizzon/git-city", "maderix/ANE", "ItzCrazyKns/Perplexica", "hesamsheikh/awesome-openclaw-usecases", "sickn33/antigravity-awesome-skills", "VoltAgent/awesome-openclaw-skills", "D4Vinci/Scrapling", "shanraisshan/claude-code-best-practice", "ruvnet/RuView", "msitarzewski/agency-agents", "koala73/worldmonitor", "KeygraphHQ/shannon", "openai/symphony", "moeru-ai/airi"], "data": [129, 136, 142, 150, 158, 161, 164, 179, 190, 218, 251, 259, 305, 309, 338, 388, 431, 601, 699, 714]},
        'weekly': {"categories": ["msitarzewski/agency-agents", "ruvnet/ruflo", "maderix/ANE", "anomalyco/opencode", "KeygraphHQ/shannon", "alibaba/OpenSandbox", "abhigyanpatwari/GitNexus", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "anthropics/skills", "affaan-m/everything-claude-code", "moeru-ai/airi", "waoowaooAI/waoowaoo", "agentscope-ai/CoPaw", "obra/superpowers", "hesamsheikh/awesome-openclaw-usecases", "RightNow-AI/openfang", "koala73/worldmonitor", "ruvnet/RuView", "openclaw/openclaw"], "data": [1166, 1251, 1264, 1326, 1363, 1367, 1477, 1736, 2007, 2097, 2168, 2216, 2340, 2382, 2383, 2688, 2779, 3660, 6014, 8874]},
        'monthly': {"categories": ["jamiepine/voicebox", "D4Vinci/Scrapling", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "badlogic/pi-mono", "qwibitai/nanoclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anomalyco/opencode", "affaan-m/everything-claude-code", "anthropics/skills", "ruvnet/RuView", "HKUDS/nanobot", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "obra/superpowers", "koala73/worldmonitor", "KeygraphHQ/shannon", "openclaw/openclaw"], "data": [3275, 3507, 3606, 3697, 3926, 4293, 4363, 5241, 5513, 5522, 6005, 6101, 6582, 6613, 6842, 7146, 7632, 7974, 8185, 30102]}
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
| 1 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +714 | 27172 |
| 2 | [openai/symphony](https://github.com/openai/symphony) | +699 | 4815 |
| 3 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +601 | 31712 |
| 4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +431 | 31217 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +388 | 7016 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +338 | 28116 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +309 | 10560 |
| 8 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +305 | 23689 |
| 9 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +259 | 28502 |
| 10 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +251 | 20427 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +218 | 18918 |
| 12 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +190 | 31253 |
| 13 | [maderix/ANE](https://github.com/maderix/ANE) | +179 | 5805 |
| 14 | [srizzon/git-city](https://github.com/srizzon/git-city) | +164 | 2479 |
| 15 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +161 | 13216 |
| 16 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +158 | 8536 |
| 17 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +150 | 2364 |
| 18 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +142 | 2821 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +136 | 24166 |
| 20 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +129 | 6360 |
| 21 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +126 | 19225 |
| 22 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +125 | 4960 |
| 23 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +120 | 29182 |
| 24 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +120 | 19031 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +119 | 3238 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +116 | 34148 |
| 27 | [waoowaooAI/waoowaoo](https://github.com/waoowaooAI/waoowaoo) | +115 | 8318 |
| 28 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +103 | 23514 |
| 29 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +103 | 37330 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +99 | 20265 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8874 | 224760 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6014 | 28116 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3660 | 31217 |
| 4 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2779 | 10451 |
| 5 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2688 | 18918 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2383 | 60312 |
| 7 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2382 | 8536 |
| 8 | [waoowaooAI/waoowaoo](https://github.com/waoowaooAI/waoowaoo) | +2340 | 8318 |
| 9 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2216 | 27172 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2168 | 51199 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +2097 | 74774 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +2007 | 28502 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1736 | 23689 |
| 14 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1477 | 10026 |
| 15 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1367 | 6360 |
| 16 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1363 | 31712 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1326 | 109881 |
| 18 | [maderix/ANE](https://github.com/maderix/ANE) | +1264 | 5805 |
| 19 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1251 | 19145 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1166 | 7016 |
| 21 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1120 | 20427 |
| 22 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1104 | 23514 |
| 23 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1100 | 24679 |
| 24 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1088 | 5411 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1074 | 10560 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1068 | 24870 |
| 27 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1062 | 19225 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1009 | 69674 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +983 | 29182 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +972 | 24166 |
| 31 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +934 | 13216 |
| 32 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +889 | 20265 |
| 33 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +867 | 21716 |
| 34 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +858 | 5617 |
| 35 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +807 | 8264 |
| 36 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +805 | 3112 |
| 37 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +802 | 19031 |
| 38 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +800 | 4960 |
| 39 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +784 | 37330 |
| 40 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +784 | 25402 |
| 41 | [superset-sh/superset](https://github.com/superset-sh/superset) | +757 | 5010 |
| 42 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +718 | 33878 |
| 43 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +706 | 20540 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +701 | 16212 |
| 45 | [openai/symphony](https://github.com/openai/symphony) | +701 | 4815 |
| 46 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +667 | 2822 |
| 47 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +661 | 34148 |
| 48 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +631 | 6100 |
| 49 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +605 | 2591 |
| 50 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +596 | 13416 |
| 51 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +595 | 5634 |
| 52 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +590 | 22295 |
| 53 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +537 | 7032 |
| 54 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +536 | 2388 |
| 55 | [tobi/qmd](https://github.com/tobi/qmd) | +505 | 12735 |
| 56 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +501 | 30678 |
| 57 | [taigrr/spank](https://github.com/taigrr/spank) | +492 | 1801 |
| 58 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +479 | 12586 |
| 59 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +478 | 9893 |
| 60 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +469 | 22303 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +465 | 27834 |
| 62 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +464 | 31253 |
| 63 | [srizzon/git-city](https://github.com/srizzon/git-city) | +464 | 2479 |
| 64 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +464 | 9639 |
| 65 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +443 | 1487 |
| 66 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +431 | 2364 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +428 | 13506 |
| 68 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +412 | 2860 |
| 69 | [huggingface/skills](https://github.com/huggingface/skills) | +412 | 8255 |
| 70 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +405 | 14158 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +394 | 11250 |
| 72 | [eooce/python-ws](https://github.com/eooce/python-ws) | +387 | 1452 |
| 73 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +373 | 3238 |
| 74 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +363 | 12314 |
| 75 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +350 | 8470 |
| 76 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +337 | 1295 |
| 77 | [block/goose](https://github.com/block/goose) | +334 | 31098 |
| 78 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +326 | 3732 |
| 79 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +323 | 4268 |
| 80 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +320 | 1626 |
| 81 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +317 | 5101 |
| 82 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +302 | 25414 |
| 83 | [tw93/Mole](https://github.com/tw93/Mole) | +301 | 36870 |
| 84 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +299 | 26422 |
| 85 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +296 | 37564 |
| 86 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +296 | 19169 |
| 87 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +293 | 6776 |
| 88 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +291 | 4997 |
| 89 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | +291 | 2118 |
| 90 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +279 | 23791 |
| 91 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +276 | 4145 |
| 92 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +275 | 9342 |
| 93 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +270 | 1424 |
| 94 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +264 | 12599 |
| 95 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +263 | 10360 |
| 96 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +263 | 17588 |
| 97 | [openai/skills](https://github.com/openai/skills) | +256 | 10902 |
| 98 | [mengxi-ream/read-frog](https://github.com/mengxi-ream/read-frog) | +250 | 4514 |
| 99 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +243 | 945 |
| 100 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +238 | 36799 |
| 101 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +235 | 6575 |
| 102 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +226 | 1847 |
| 103 | [slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide) | +225 | 1118 |
| 104 | [puaclaw/PUAClaw](https://github.com/puaclaw/PUAClaw) | +220 | 963 |
| 105 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +216 | 12026 |
| 106 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +215 | 22157 |
| 107 | [ILoveBingLu/CipherTalk](https://github.com/ILoveBingLu/CipherTalk) | +214 | 1554 |
| 108 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +213 | 1119 |
| 109 | [wshobson/agents](https://github.com/wshobson/agents) | +211 | 30324 |
| 110 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +199 | 4714 |
| 111 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +196 | 47122 |
| 112 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +192 | 15340 |
| 113 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +187 | 9095 |
| 114 | [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | +186 | 7985 |
| 115 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +185 | 13490 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +185 | 647 |
| 117 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +178 | 47936 |
| 118 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +177 | 4748 |
| 119 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +176 | 7276 |
| 120 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +176 | 1155 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30102 | 224760 |
| 2 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +8185 | 31713 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7974 | 31217 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +7632 | 60312 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7146 | 23514 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6842 | 22295 |
| 7 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +6613 | 29182 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6582 | 28116 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6101 | 74774 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6005 | 51199 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5522 | 109881 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5513 | 28502 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5241 | 18918 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4363 | 122870 |
| 15 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4293 | 19225 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3926 | 20265 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3697 | 24870 |
| 18 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3606 | 20427 |
| 19 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3507 | 23689 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3275 | 12197 |
| 21 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3210 | 60117 |
| 22 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3156 | 37330 |
| 23 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3065 | 30678 |
| 24 | [google/langextract](https://github.com/google/langextract) | +2999 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2981 | 69674 |
| 26 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2893 | 10451 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2763 | 34148 |
| 28 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2653 | 33878 |
| 29 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2623 | 8680 |
| 30 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2598 | 9095 |
| 31 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2581 | 10026 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2562 | 85286 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2531 | 10560 |
| 34 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2383 | 8536 |
| 35 | [waoowaooAI/waoowaoo](https://github.com/waoowaooAI/waoowaoo) | +2347 | 8318 |
| 36 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2320 | 27172 |
| 37 | [openai/skills](https://github.com/openai/skills) | +2307 | 10902 |
| 38 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2305 | 24166 |
| 39 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2258 | 96919 |
| 40 | [virattt/dexter](https://github.com/virattt/dexter) | +2158 | 17146 |
| 41 | [huggingface/skills](https://github.com/huggingface/skills) | +1992 | 8255 |
| 42 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1988 | 20540 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1957 | 16212 |
| 44 | [github/spec-kit](https://github.com/github/spec-kit) | +1919 | 71722 |
| 45 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1899 | 9620 |
| 46 | [pydantic/monty](https://github.com/pydantic/monty) | +1894 | 5959 |
| 47 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1821 | 8264 |
| 48 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1800 | 9639 |
| 49 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1792 | 10346 |
| 50 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1763 | 6575 |
| 51 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1735 | 17905 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1724 | 147486 |
| 53 | [tobi/qmd](https://github.com/tobi/qmd) | +1704 | 12735 |
| 54 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1703 | 149018 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1699 | 19031 |
| 56 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1684 | 5946 |
| 57 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1677 | 25402 |
| 58 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1654 | 14158 |
| 59 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1593 | 19145 |
| 60 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1535 | 5634 |
| 61 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1534 | 5617 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1527 | 11250 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1522 | 27834 |
| 64 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1519 | 9893 |
| 65 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1518 | 5101 |
| 66 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1518 | 9031 |
| 67 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1512 | 5309 |
| 68 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1506 | 74887 |
| 69 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1503 | 33712 |
| 70 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1492 | 6100 |
| 71 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1483 | 37564 |
| 72 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1476 | 8611 |
| 73 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1450 | 12586 |
| 74 | [tw93/Mole](https://github.com/tw93/Mole) | +1447 | 36870 |
| 75 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1441 | 6360 |
| 76 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1422 | 24679 |
| 77 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1414 | 6899 |
| 78 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1413 | 7880 |
| 79 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1407 | 21716 |
| 80 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1403 | 13216 |
| 81 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1394 | 5411 |
| 82 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1384 | 13416 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1373 | 98536 |
| 84 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1363 | 25414 |
| 85 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1348 | 8795 |
| 86 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1338 | 5668 |
| 87 | [openai/codex](https://github.com/openai/codex) | +1335 | 61744 |
| 88 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1326 | 27600 |
| 89 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1321 | 4997 |
| 90 | [maderix/ANE](https://github.com/maderix/ANE) | +1264 | 5805 |
| 91 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1264 | 4251 |
| 92 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1238 | 4478 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1211 | 13506 |
| 94 | [slopus/happy](https://github.com/slopus/happy) | +1198 | 14282 |
| 95 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1172 | 4960 |
| 96 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1171 | 7016 |
| 97 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1160 | 87598 |
| 98 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1131 | 22168 |
| 99 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1109 | 4714 |
| 100 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1108 | 7032 |
| 101 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1055 | 19169 |
| 102 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1037 | 3732 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1017 | 26422 |
| 104 | [superset-sh/superset](https://github.com/superset-sh/superset) | +998 | 5010 |
| 105 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +992 | 4748 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +949 | 23791 |
| 107 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +947 | 22136 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +888 | 61818 |
| 109 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +887 | 12026 |
| 110 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +854 | 22157 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +828 | 18228 |
| 112 | [docling-project/docling](https://github.com/docling-project/docling) | +812 | 54041 |
| 113 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +804 | 3112 |
| 114 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +785 | 47122 |
| 115 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +773 | 9016 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +770 | 9095 |
| 117 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +752 | 36799 |
| 118 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +741 | 13955 |
| 119 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +703 | 11629 |
| 120 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +699 | 15340 |
| 121 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +699 | 43973 |
| 122 | [wshobson/agents](https://github.com/wshobson/agents) | +684 | 30324 |
| 123 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +681 | 13490 |
| 124 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +680 | 7276 |
| 125 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +655 | 30590 |
| 126 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +653 | 4145 |
| 127 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +648 | 9050 |
| 128 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +647 | 2591 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +632 | 9961 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +632 | 47936 |
| 131 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +628 | 2154 |
| 132 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +587 | 17587 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +568 | 54903 |
| 134 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +566 | 3409 |
| 135 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +548 | 39841 |
| 136 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +537 | 1241 |
| 137 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +528 | 2127 |
| 138 | [microsoft/qlib](https://github.com/microsoft/qlib) | +526 | 37792 |
| 139 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +524 | 15804 |
| 140 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +520 | 1409 |
| 141 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +516 | 7853 |
| 142 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +500 | 1923 |
| 143 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +497 | 1648 |
| 144 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +482 | 1157 |
| 145 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +476 | 1847 |
| 146 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +476 | 2641 |
| 147 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +467 | 4904 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +466 | 44545 |
| 149 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +454 | 1487 |
| 150 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +454 | 13981 |
| 151 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +454 | 4207 |
| 152 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +450 | 1422 |
| 153 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +447 | 2364 |
| 154 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +442 | 11197 |
| 155 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +434 | 6045 |
| 156 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +433 | 3610 |
| 157 | [samugit83/redamon](https://github.com/samugit83/redamon) | +420 | 1474 |
| 158 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +415 | 10247 |
| 159 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +412 | 3190 |
| 160 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +407 | 25653 |
| 161 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +403 | 15325 |
| 162 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +401 | 2151 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +398 | 2032 |
| 164 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +398 | 5362 |
| 165 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +398 | 36103 |
| 166 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +396 | 10340 |
| 167 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +394 | 6174 |
| 168 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +393 | 44232 |
| 169 | [eooce/python-ws](https://github.com/eooce/python-ws) | +386 | 1452 |
| 170 | [oraios/serena](https://github.com/oraios/serena) | +381 | 21048 |
| 171 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +380 | 8742 |
| 172 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +379 | 1424 |
| 173 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +379 | 15055 |
| 174 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +377 | 17588 |
| 175 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +370 | 2311 |
| 176 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +369 | 3075 |
| 177 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | +361 | 40916 |
| 178 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +358 | 1260 |
| 179 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +357 | 11110 |
| 180 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +356 | 1368 |
| 181 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +352 | 8977 |
| 182 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +338 | 1295 |
| 183 | [usestrix/strix](https://github.com/usestrix/strix) | +338 | 20752 |
| 184 | [dp-archive/archive](https://github.com/dp-archive/archive) | +335 | 1108 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +334 | 23932 |
| 186 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +333 | 1267 |
| 187 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +329 | 648 |
| 188 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +327 | 2004 |
| 189 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +325 | 12661 |
| 190 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +321 | 6994 |
| 191 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +319 | 36697 |
| 192 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +315 | 1295 |
| 193 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +311 | 24127 |
| 194 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +310 | 4043 |
| 195 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +309 | 881 |
| 196 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +306 | 2998 |
| 197 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +296 | 9787 |
| 198 | [robinebers/openusage](https://github.com/robinebers/openusage) | +295 | 1224 |
| 199 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +292 | 2450 |
| 200 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +290 | 21005 |
| 201 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +279 | 1013 |
| 202 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +277 | 967 |
| 203 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +273 | 1155 |
| 204 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +270 | 5413 |
| 205 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +269 | 3331 |
| 206 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +250 | 1838 |
| 207 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +249 | 837 |
| 208 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +245 | 21194 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +245 | 41086 |
| 210 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +233 | 22542 |
| 211 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +232 | 12787 |
| 212 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +227 | 6582 |
| 213 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +225 | 2425 |
| 214 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 277 |
| 215 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +220 | 28588 |
| 216 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +219 | 3334 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +213 | 40265 |
| 218 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +210 | 725 |
| 219 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +209 | 1119 |
| 220 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +208 | 791 |
| 221 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 679 |
| 222 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +204 | 642 |
| 223 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +197 | 705 |
| 224 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +197 | 937 |
| 225 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +196 | 29780 |
| 226 | [apify/agent-skills](https://github.com/apify/agent-skills) | +195 | 887 |
| 227 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +195 | 586 |
| 228 | [qist/tvbox](https://github.com/qist/tvbox) | +188 | 8356 |
| 229 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +187 | 861 |
| 230 | [VonChange/utao](https://github.com/VonChange/utao) | +184 | 3889 |
| 231 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +184 | 624 |
| 232 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +181 | 551 |
| 233 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +181 | 2248 |
| 234 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +177 | 39596 |
| 235 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +177 | 8333 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +168 | 33000 |
| 237 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +164 | 801 |
| 238 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +163 | 1281 |
| 239 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +162 | 1813 |
| 240 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +159 | 3052 |
| 241 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +157 | 501 |
| 242 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +154 | 696 |
| 243 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +153 | 4767 |
| 244 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +152 | 633 |
| 245 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +152 | 13520 |
| 246 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +150 | 25788 |
| 247 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 501 |
| 248 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +146 | 580 |
| 249 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +145 | 11806 |
| 250 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +144 | 4908 |
| 251 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +143 | 37313 |
| 252 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +140 | 6898 |
| 253 | [decolua/9router](https://github.com/decolua/9router) | +138 | 668 |
| 254 | [expo/skills](https://github.com/expo/skills) | +136 | 1342 |
| 255 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +135 | 478 |
| 256 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +126 | 723 |
| 257 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +125 | 1341 |
| 258 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +125 | 9837 |
| 259 | [fmhy/edit](https://github.com/fmhy/edit) | +124 | 8361 |
| 260 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +122 | 3238 |
| 261 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +122 | 48784 |
| 262 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +117 | 3096 |
| 263 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 387 |
| 264 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +113 | 3081 |
| 265 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +111 | 390 |
| 266 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +110 | 1116 |
| 267 | [microg/GmsCore](https://github.com/microg/GmsCore) | +110 | 12459 |
| 268 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +102 | 26745 |
| 269 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +101 | 4514 |
| 270 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +101 | 10959 |
| 271 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +100 | 817 |
| 272 | [skylot/jadx](https://github.com/skylot/jadx) | +100 | 47365 |
| 273 | [yousifamanuel/terraink](https://github.com/yousifamanuel/terraink) | +99 | 427 |
| 274 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +99 | 35473 |
| 275 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 332 |
| 276 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +93 | 334 |
| 277 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +91 | 3037 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +91 | 8594 |
| 279 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +89 | 2877 |
| 280 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +86 | 28651 |
| 281 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +85 | 1583 |
| 282 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +85 | 286 |
| 283 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +85 | 815 |
| 284 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +84 | 1009 |
| 285 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +80 | 1210 |
| 286 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 293 |
| 287 | [openjdk/jdk](https://github.com/openjdk/jdk) | +78 | 22698 |
| 288 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +78 | 3447 |
| 289 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +77 | 242 |
| 290 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 291 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +76 | 667 |
| 292 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +76 | 813 |
| 293 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +76 | 871 |
| 294 | [apache/kafka](https://github.com/apache/kafka) | +76 | 32043 |
| 295 | [dataease/dataease](https://github.com/dataease/dataease) | +76 | 23504 |
| 296 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +76 | 5834 |
| 297 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1312 |
| 298 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +75 | 21299 |
| 299 | [FongMi/TV](https://github.com/FongMi/TV) | +74 | 7467 |
| 300 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +73 | 235 |
