---
title: "2026-03-06 GitHub增长趋势报告"
description: "1.agency-agents+658 2.symphony+645 3.airi+618 4.paperclip+462 5.claude-code-best-practice+444"
date: 2026-03-06T20:34:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-06 20:34:49

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
        'daily': {"categories": ["ringhyacinth/Star-Office-UI", "abhigyanpatwari/GitNexus", "qwibitai/nanoclaw", "farion1231/cc-switch", "pinchtab/pinchtab", "openai/skills", "higress-group/hiclaw", "QwenLM/Qwen-Agent", "ruvnet/RuView", "KeygraphHQ/shannon", "hesamsheikh/awesome-openclaw-usecases", "RightNow-AI/openfang", "VoltAgent/awesome-openclaw-skills", "koala73/worldmonitor", "D4Vinci/Scrapling", "shanraisshan/claude-code-best-practice", "paperclipai/paperclip", "moeru-ai/airi", "openai/symphony", "msitarzewski/agency-agents"], "data": [117, 134, 136, 144, 159, 173, 174, 181, 195, 200, 212, 218, 222, 283, 350, 444, 462, 618, 645, 658]},
        'weekly': {"categories": ["openai/symphony", "maderix/ANE", "anomalyco/opencode", "shanraisshan/claude-code-best-practice", "alibaba/OpenSandbox", "KeygraphHQ/shannon", "D4Vinci/Scrapling", "msitarzewski/agency-agents", "anthropics/skills", "VoltAgent/awesome-openclaw-skills", "obra/superpowers", "affaan-m/everything-claude-code", "waoowaooAI/waoowaoo", "RightNow-AI/openfang", "agentscope-ai/CoPaw", "hesamsheikh/awesome-openclaw-usecases", "moeru-ai/airi", "koala73/worldmonitor", "ruvnet/RuView", "openclaw/openclaw"], "data": [1264, 1296, 1320, 1390, 1393, 1470, 1777, 1815, 1940, 1998, 2177, 2259, 2400, 2460, 2475, 2501, 2727, 3701, 6105, 9066]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "D4Vinci/Scrapling", "badlogic/pi-mono", "qwibitai/nanoclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "hesamsheikh/awesome-openclaw-usecases", "anomalyco/opencode", "VoltAgent/awesome-openclaw-skills", "HKUDS/nanobot", "anthropics/skills", "affaan-m/everything-claude-code", "ruvnet/RuView", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "obra/superpowers", "koala73/worldmonitor", "KeygraphHQ/shannon", "openclaw/openclaw"], "data": [3281, 3639, 3712, 3838, 3862, 4221, 4480, 5430, 5443, 5447, 5878, 6047, 6061, 6742, 6898, 7226, 7565, 8219, 8303, 29969]}
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
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +658 | 9665 |
| 2 | [openai/symphony](https://github.com/openai/symphony) | +645 | 7315 |
| 3 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +618 | 29394 |
| 4 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +462 | 5539 |
| 5 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +444 | 11917 |
| 6 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +350 | 24870 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +283 | 32346 |
| 8 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +222 | 29558 |
| 9 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +218 | 11467 |
| 10 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +212 | 19700 |
| 11 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +200 | 32293 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +195 | 28896 |
| 13 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +181 | 14546 |
| 14 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +174 | 923 |
| 15 | [openai/skills](https://github.com/openai/skills) | +173 | 11830 |
| 16 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +159 | 5375 |
| 17 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +144 | 24709 |
| 18 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +136 | 19690 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +134 | 10421 |
| 20 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +117 | 2820 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +117 | 22228 |
| 22 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +113 | 3348 |
| 23 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +112 | 13911 |
| 24 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +112 | 20692 |
| 25 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +111 | 20967 |
| 26 | [aidenybai/react-grab](https://github.com/aidenybai/react-grab) | +110 | 5947 |
| 27 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +109 | 4947 |
| 28 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +109 | 9001 |
| 29 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +108 | 19491 |
| 30 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +98 | 37330 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9066 | 224760 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6105 | 28896 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3701 | 32346 |
| 4 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2727 | 29395 |
| 5 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2501 | 19700 |
| 6 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2475 | 9001 |
| 7 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2460 | 11467 |
| 8 | [waoowaooAI/waoowaoo](https://github.com/waoowaooAI/waoowaoo) | +2400 | 8551 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2259 | 51199 |
| 10 | [obra/superpowers](https://github.com/obra/superpowers) | +2177 | 60312 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1998 | 29558 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +1940 | 74774 |
| 13 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1815 | 9665 |
| 14 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1777 | 24870 |
| 15 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1470 | 32293 |
| 16 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1393 | 6534 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1390 | 11917 |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1320 | 109881 |
| 19 | [maderix/ANE](https://github.com/maderix/ANE) | +1296 | 5887 |
| 20 | [openai/symphony](https://github.com/openai/symphony) | +1264 | 7315 |
| 21 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1224 | 10421 |
| 22 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1204 | 19457 |
| 23 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1101 | 20967 |
| 24 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1048 | 19690 |
| 25 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1008 | 23934 |
| 26 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1004 | 69674 |
| 27 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +982 | 25118 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +977 | 25307 |
| 29 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +973 | 13441 |
| 30 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +955 | 5375 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +933 | 24709 |
| 32 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +904 | 29593 |
| 33 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +895 | 5539 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +858 | 22228 |
| 35 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +855 | 20692 |
| 36 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +821 | 5751 |
| 37 | [superset-sh/superset](https://github.com/superset-sh/superset) | +803 | 5267 |
| 38 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +790 | 3184 |
| 39 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +776 | 37330 |
| 40 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +774 | 3348 |
| 41 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +742 | 19491 |
| 42 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +724 | 25646 |
| 43 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +661 | 34148 |
| 44 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +660 | 5459 |
| 45 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +657 | 33878 |
| 46 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +656 | 16522 |
| 47 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +630 | 2739 |
| 48 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +625 | 2820 |
| 49 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +584 | 5723 |
| 50 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +567 | 8461 |
| 51 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +565 | 20672 |
| 52 | [taigrr/spank](https://github.com/taigrr/spank) | +530 | 2021 |
| 53 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +519 | 22540 |
| 54 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +516 | 10123 |
| 55 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +514 | 6198 |
| 56 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +513 | 31615 |
| 57 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +506 | 13911 |
| 58 | [tobi/qmd](https://github.com/tobi/qmd) | +506 | 13009 |
| 59 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +505 | 2712 |
| 60 | [srizzon/git-city](https://github.com/srizzon/git-city) | +496 | 2727 |
| 61 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +472 | 30678 |
| 62 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +468 | 1596 |
| 63 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +463 | 1549 |
| 64 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +455 | 9960 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +452 | 28117 |
| 66 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +451 | 3690 |
| 67 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +445 | 12642 |
| 68 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +433 | 5689 |
| 69 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +412 | 7097 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +411 | 11477 |
| 71 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +409 | 13501 |
| 72 | [eooce/python-ws](https://github.com/eooce/python-ws) | +407 | 1514 |
| 73 | [openai/skills](https://github.com/openai/skills) | +398 | 11830 |
| 74 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +388 | 14280 |
| 75 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +359 | 8707 |
| 76 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +351 | 1801 |
| 77 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +348 | 1348 |
| 78 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +333 | 5226 |
| 79 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +331 | 4425 |
| 80 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +323 | 2892 |
| 81 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +315 | 5108 |
| 82 | [tw93/Mole](https://github.com/tw93/Mole) | +311 | 36870 |
| 83 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +310 | 26593 |
| 84 | [huggingface/skills](https://github.com/huggingface/skills) | +306 | 8340 |
| 85 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +297 | 12461 |
| 86 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +296 | 3794 |
| 87 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +292 | 19368 |
| 88 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | +290 | 2249 |
| 89 | [Justsenger/ExHyperV](https://github.com/Justsenger/ExHyperV) | +290 | 1810 |
| 90 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +286 | 7137 |
| 91 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +285 | 10554 |
| 92 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +281 | 23945 |
| 93 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +281 | 17670 |
| 94 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +267 | 22343 |
| 95 | [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | +264 | 4882 |
| 96 | [puaclaw/PUAClaw](https://github.com/puaclaw/PUAClaw) | +259 | 1087 |
| 97 | [mengxi-ream/read-frog](https://github.com/mengxi-ream/read-frog) | +258 | 4545 |
| 98 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +255 | 1459 |
| 99 | [slowmist/openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide) | +252 | 1242 |
| 100 | [ILoveBingLu/CipherTalk](https://github.com/ILoveBingLu/CipherTalk) | +250 | 1647 |
| 101 | [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | +246 | 2737 |
| 102 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +238 | 1313 |
| 103 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +238 | 36799 |
| 104 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +236 | 6679 |
| 105 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +232 | 14546 |
| 106 | [higress-group/hiclaw](https://github.com/higress-group/hiclaw) | +227 | 923 |
| 107 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +222 | 22246 |
| 108 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +215 | 12141 |
| 109 | [wshobson/agents](https://github.com/wshobson/agents) | +211 | 30414 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +204 | 3207 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +198 | 9256 |
| 112 | [agentscope-ai/ReMe](https://github.com/agentscope-ai/ReMe) | +197 | 1979 |
| 113 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +192 | 15436 |
| 114 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +185 | 4847 |
| 115 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +183 | 7306 |
| 116 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +183 | 47936 |
| 117 | [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | +181 | 8005 |
| 118 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +177 | 47122 |
| 119 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +177 | 13587 |
| 120 | [microsoft/fara](https://github.com/microsoft/fara) | +175 | 4274 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +29969 | 224760 |
| 2 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +8303 | 32293 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +8219 | 32346 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +7565 | 60312 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7226 | 23934 |
| 6 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6898 | 22540 |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6742 | 28896 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6061 | 51199 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6047 | 74774 |
| 10 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +5878 | 29593 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5447 | 29558 |
| 12 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5443 | 109881 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5430 | 19700 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4480 | 122870 |
| 15 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4221 | 19690 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3862 | 20692 |
| 17 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3838 | 24870 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3712 | 25307 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3639 | 20967 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3281 | 12272 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +3113 | 11467 |
| 22 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3094 | 60117 |
| 23 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3063 | 37330 |
| 24 | [google/langextract](https://github.com/google/langextract) | +3001 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2953 | 69674 |
| 26 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2942 | 11917 |
| 27 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2882 | 29395 |
| 28 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2817 | 30678 |
| 29 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2712 | 10421 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2679 | 34148 |
| 31 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2627 | 8703 |
| 32 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2617 | 9158 |
| 33 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2596 | 33878 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2577 | 85286 |
| 35 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2480 | 9001 |
| 36 | [waoowaooAI/waoowaoo](https://github.com/waoowaooAI/waoowaoo) | +2403 | 8551 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2367 | 24709 |
| 38 | [openai/skills](https://github.com/openai/skills) | +2307 | 11830 |
| 39 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2257 | 96919 |
| 40 | [virattt/dexter](https://github.com/virattt/dexter) | +2133 | 17226 |
| 41 | [huggingface/skills](https://github.com/huggingface/skills) | +2013 | 8340 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1939 | 16522 |
| 43 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1935 | 20672 |
| 44 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1899 | 9652 |
| 45 | [github/spec-kit](https://github.com/github/spec-kit) | +1895 | 71722 |
| 46 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1866 | 8461 |
| 47 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1842 | 10554 |
| 48 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1820 | 9665 |
| 49 | [pydantic/monty](https://github.com/pydantic/monty) | +1808 | 5982 |
| 50 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1794 | 6679 |
| 51 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1766 | 9960 |
| 52 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1758 | 147486 |
| 53 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1736 | 18001 |
| 54 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1734 | 19491 |
| 55 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1693 | 5982 |
| 56 | [tobi/qmd](https://github.com/tobi/qmd) | +1678 | 13009 |
| 57 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1676 | 14280 |
| 58 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1675 | 149018 |
| 59 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1658 | 19458 |
| 60 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1646 | 25646 |
| 61 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1559 | 5751 |
| 62 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1559 | 5723 |
| 63 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1553 | 10123 |
| 64 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1550 | 74887 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1543 | 11478 |
| 66 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1535 | 5689 |
| 67 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1521 | 9049 |
| 68 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1520 | 5357 |
| 69 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1518 | 5108 |
| 70 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1516 | 6198 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1511 | 28117 |
| 72 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1509 | 33712 |
| 73 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1491 | 22228 |
| 74 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1479 | 6534 |
| 75 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1471 | 25118 |
| 76 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1470 | 37564 |
| 77 | [tw93/Mole](https://github.com/tw93/Mole) | +1447 | 36870 |
| 78 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1445 | 13441 |
| 79 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1427 | 8011 |
| 80 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1405 | 5459 |
| 81 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1402 | 13501 |
| 82 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1372 | 98536 |
| 83 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1371 | 12642 |
| 84 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1364 | 5764 |
| 85 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1362 | 5226 |
| 86 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1329 | 27752 |
| 87 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1326 | 5375 |
| 88 | [openai/codex](https://github.com/openai/codex) | +1318 | 61744 |
| 89 | [maderix/ANE](https://github.com/maderix/ANE) | +1296 | 5887 |
| 90 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1290 | 25509 |
| 91 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1283 | 13911 |
| 92 | [openai/symphony](https://github.com/openai/symphony) | +1265 | 7315 |
| 93 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1246 | 4520 |
| 94 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1243 | 8912 |
| 95 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1201 | 22343 |
| 96 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1162 | 8673 |
| 97 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1145 | 87598 |
| 98 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1126 | 7097 |
| 99 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1120 | 4847 |
| 100 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1081 | 19368 |
| 101 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +1056 | 3794 |
| 102 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1033 | 5267 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1016 | 26593 |
| 104 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +976 | 7169 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +938 | 23945 |
| 106 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +909 | 22237 |
| 107 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +895 | 5539 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +888 | 61818 |
| 109 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +869 | 12141 |
| 110 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +847 | 22246 |
| 111 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +824 | 4791 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +822 | 18276 |
| 113 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +820 | 3184 |
| 114 | [docling-project/docling](https://github.com/docling-project/docling) | +805 | 54041 |
| 115 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +772 | 9107 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +771 | 9256 |
| 117 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +770 | 47122 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +744 | 36799 |
| 119 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +724 | 13998 |
| 120 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +694 | 7306 |
| 121 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +683 | 43973 |
| 122 | [wshobson/agents](https://github.com/wshobson/agents) | +680 | 30414 |
| 123 | [mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode) | +675 | 2739 |
| 124 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +673 | 15436 |
| 125 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +669 | 13587 |
| 126 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +651 | 4213 |
| 127 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +649 | 30590 |
| 128 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +639 | 2174 |
| 129 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +638 | 9115 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +638 | 47936 |
| 131 | [google-research/timesfm](https://github.com/google-research/timesfm) | +633 | 9968 |
| 132 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +596 | 11657 |
| 133 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +585 | 17600 |
| 134 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +568 | 3422 |
| 135 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +548 | 1287 |
| 136 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +540 | 39841 |
| 137 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +529 | 2132 |
| 138 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +525 | 15831 |
| 139 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +523 | 1414 |
| 140 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +517 | 2712 |
| 141 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +501 | 1945 |
| 142 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +501 | 1661 |
| 143 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +489 | 1596 |
| 144 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +480 | 1860 |
| 145 | [microsoft/qlib](https://github.com/microsoft/qlib) | +477 | 37792 |
| 146 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +463 | 44545 |
| 147 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +462 | 1549 |
| 148 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +452 | 1436 |
| 149 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +444 | 3748 |
| 150 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +443 | 2677 |
| 151 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +441 | 11210 |
| 152 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +437 | 6062 |
| 153 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +436 | 4210 |
| 154 | [samugit83/redamon](https://github.com/samugit83/redamon) | +429 | 1487 |
| 155 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +421 | 4961 |
| 156 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +415 | 25746 |
| 157 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +415 | 13999 |
| 158 | [eooce/python-ws](https://github.com/eooce/python-ws) | +406 | 1514 |
| 159 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +405 | 10297 |
| 160 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +403 | 3224 |
| 161 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +403 | 44232 |
| 162 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +397 | 10347 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +396 | 2102 |
| 164 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +394 | 17670 |
| 165 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +394 | 6220 |
| 166 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +391 | 2345 |
| 167 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +390 | 1459 |
| 168 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +388 | 5418 |
| 169 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +386 | 36103 |
| 170 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +383 | 15332 |
| 171 | [oraios/serena](https://github.com/oraios/serena) | +375 | 21091 |
| 172 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +374 | 8757 |
| 173 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +372 | 4947 |
| 174 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +365 | 1277 |
| 175 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +362 | 1424 |
| 176 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | +361 | 40916 |
| 177 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +361 | 11148 |
| 178 | [uqogihujomuwhiff/sora2-watermark-cleaner-pro](https://github.com/uqogihujomuwhiff/sora2-watermark-cleaner-pro) | +359 | 0 |
| 179 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +356 | 3123 |
| 180 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +354 | 9040 |
| 181 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +353 | 2375 |
| 182 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +348 | 1348 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +344 | 23980 |
| 184 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +341 | 3207 |
| 185 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +332 | 661 |
| 186 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +329 | 2049 |
| 187 | [usestrix/strix](https://github.com/usestrix/strix) | +321 | 20767 |
| 188 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +319 | 1310 |
| 189 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +315 | 36697 |
| 190 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +309 | 12690 |
| 191 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +309 | 881 |
| 192 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +305 | 4095 |
| 193 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +302 | 24173 |
| 194 | [robinebers/openusage](https://github.com/robinebers/openusage) | +301 | 1251 |
| 195 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +297 | 1309 |
| 196 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +293 | 9791 |
| 197 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +292 | 14546 |
| 198 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +292 | 2454 |
| 199 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +283 | 1162 |
| 200 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +282 | 1026 |
| 201 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +282 | 993 |
| 202 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +278 | 1192 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +278 | 21039 |
| 204 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +268 | 3374 |
| 205 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +264 | 5417 |
| 206 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +254 | 1846 |
| 207 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +251 | 838 |
| 208 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +239 | 21236 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +238 | 41086 |
| 210 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +235 | 1313 |
| 211 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +234 | 12804 |
| 212 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +230 | 22558 |
| 213 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 278 |
| 214 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +222 | 2432 |
| 215 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +218 | 6578 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +217 | 28609 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +213 | 40265 |
| 218 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +211 | 733 |
| 219 | [apify/agent-skills](https://github.com/apify/agent-skills) | +208 | 922 |
| 220 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +207 | 742 |
| 221 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +207 | 791 |
| 222 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 676 |
| 223 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +197 | 591 |
| 224 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +197 | 3348 |
| 225 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +195 | 907 |
| 226 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +194 | 29780 |
| 227 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +193 | 645 |
| 228 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +191 | 645 |
| 229 | [qist/tvbox](https://github.com/qist/tvbox) | +186 | 8364 |
| 230 | [VonChange/utao](https://github.com/VonChange/utao) | +182 | 3890 |
| 231 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +182 | 2251 |
| 232 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +181 | 556 |
| 233 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +177 | 8368 |
| 234 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +172 | 39596 |
| 235 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +166 | 33000 |
| 236 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +164 | 1302 |
| 237 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +159 | 704 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +159 | 1816 |
| 239 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +157 | 507 |
| 240 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +157 | 946 |
| 241 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +156 | 824 |
| 242 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +152 | 4803 |
| 243 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +152 | 635 |
| 244 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +152 | 4944 |
| 245 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +151 | 545 |
| 246 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +151 | 3057 |
| 247 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +151 | 25805 |
| 248 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 508 |
| 249 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +148 | 588 |
| 250 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +146 | 13531 |
| 251 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +141 | 6898 |
| 252 | [decolua/9router](https://github.com/decolua/9router) | +139 | 683 |
| 253 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +137 | 11821 |
| 254 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +136 | 494 |
| 255 | [expo/skills](https://github.com/expo/skills) | +135 | 1355 |
| 256 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +134 | 37313 |
| 257 | [lklynet/aurral](https://github.com/lklynet/aurral) | +126 | 797 |
| 258 | [fmhy/edit](https://github.com/fmhy/edit) | +125 | 8380 |
| 259 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +124 | 48784 |
| 260 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +122 | 9851 |
| 261 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +121 | 1344 |
| 262 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +121 | 734 |
| 263 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 387 |
| 264 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +115 | 3094 |
| 265 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +115 | 1130 |
| 266 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +114 | 395 |
| 267 | [yousifamanuel/terraink](https://github.com/yousifamanuel/terraink) | +112 | 485 |
| 268 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +111 | 3245 |
| 269 | [microg/GmsCore](https://github.com/microg/GmsCore) | +111 | 12474 |
| 270 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +110 | 3106 |
| 271 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +102 | 35473 |
| 272 | [skylot/jadx](https://github.com/skylot/jadx) | +102 | 47365 |
| 273 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +99 | 26754 |
| 274 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +97 | 4523 |
| 275 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +96 | 10972 |
| 276 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +95 | 349 |
| 277 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 335 |
| 278 | [docmd-io/docmd](https://github.com/docmd-io/docmd) | +93 | 1022 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +91 | 8609 |
| 280 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +86 | 291 |
| 281 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +86 | 822 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 2882 |
| 283 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +85 | 28658 |
| 284 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +81 | 1600 |
| 285 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +81 | 3458 |
| 286 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +80 | 1220 |
| 287 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 295 |
| 288 | [openjdk/jdk](https://github.com/openjdk/jdk) | +78 | 22707 |
| 289 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +77 | 837 |
| 290 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +77 | 243 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +76 | 877 |
| 292 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +76 | 1315 |
| 293 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +75 | 670 |
| 294 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +75 | 45263 |
| 295 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +75 | 5843 |
| 296 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +74 | 236 |
| 297 | [apache/kafka](https://github.com/apache/kafka) | +74 | 32043 |
| 298 | [4ier/neo](https://github.com/4ier/neo) | +73 | 453 |
| 299 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +72 | 21301 |
| 300 | [dataease/dataease](https://github.com/dataease/dataease) | +72 | 23507 |
