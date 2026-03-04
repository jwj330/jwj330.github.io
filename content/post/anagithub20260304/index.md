---
title: "2026-03-04 GitHub增长趋势报告"
description: "1.worldmonitor+860 2.RuView+634 3.agency-agents+503 4.shannon+484 5.everything-claude-code+451"
date: 2026-03-04T20:34:57+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-04 20:34:57

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
        'daily': {"categories": ["abhigyanpatwari/GitNexus", "superset-sh/superset", "alibaba/OpenSandbox", "K-Dense-AI/claude-scientific-skills", "smartcmd/MinecraftConsoles", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "pinchtab/pinchtab", "hesamsheikh/awesome-openclaw-usecases", "ItzCrazyKns/Perplexica", "moeru-ai/airi", "canopy-network/canopy", "maderix/ANE", "agentscope-ai/CoPaw", "shanraisshan/claude-code-best-practice", "affaan-m/everything-claude-code", "KeygraphHQ/shannon", "msitarzewski/agency-agents", "ruvnet/RuView", "koala73/worldmonitor"], "data": [187, 198, 204, 225, 227, 230, 231, 231, 253, 260, 282, 298, 311, 340, 343, 451, 484, 503, 634, 860]},
        'weekly': {"categories": ["zarazhangrui/frontend-slides", "bytedance/deer-flow", "zeroclaw-labs/zeroclaw", "anthropics/financial-services-plugins", "ruvnet/ruflo", "alibaba/OpenSandbox", "anomalyco/opencode", "moeru-ai/airi", "abhigyanpatwari/GitNexus", "VoltAgent/awesome-openclaw-skills", "D4Vinci/Scrapling", "anthropics/skills", "affaan-m/everything-claude-code", "agentscope-ai/CoPaw", "obra/superpowers", "RightNow-AI/openfang", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "ruvnet/RuView", "openclaw/openclaw"], "data": [1169, 1174, 1175, 1201, 1220, 1267, 1425, 1537, 1711, 1973, 2113, 2186, 2193, 2250, 2462, 2813, 2857, 3568, 5713, 8824]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "thedotmack/claude-mem", "gsd-build/get-shit-done", "badlogic/pi-mono", "qwibitai/nanoclaw", "x1xhlol/system-prompts-and-models-of-ai-tools", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anomalyco/opencode", "affaan-m/everything-claude-code", "anthropics/skills", "ruvnet/RuView", "sipeed/picoclaw", "zeroclaw-labs/zeroclaw", "HKUDS/nanobot", "obra/superpowers", "KeygraphHQ/shannon", "koala73/worldmonitor", "openclaw/openclaw"], "data": [3285, 3450, 3529, 3669, 3954, 4334, 4382, 5042, 5560, 5628, 5998, 6141, 6283, 6782, 7062, 7162, 7601, 7614, 7618, 30370]}
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
| 1 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +860 | 29660 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +634 | 26957 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +503 | 5220 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +484 | 29858 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +451 | 51199 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +343 | 8725 |
| 7 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +340 | 8004 |
| 8 | [maderix/ANE](https://github.com/maderix/ANE) | +311 | 5290 |
| 9 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +298 | 1778 |
| 10 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +282 | 24527 |
| 11 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +260 | 30735 |
| 12 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +253 | 18008 |
| 13 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +231 | 4211 |
| 14 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +231 | 27480 |
| 15 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +230 | 22058 |
| 16 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +227 | 2286 |
| 17 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +225 | 12644 |
| 18 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +204 | 5897 |
| 19 | [superset-sh/superset](https://github.com/superset-sh/superset) | +198 | 4781 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +187 | 9570 |
| 21 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +172 | 1387 |
| 22 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +171 | 19567 |
| 23 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +165 | 37330 |
| 24 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +164 | 18561 |
| 25 | [srizzon/git-city](https://github.com/srizzon/git-city) | +158 | 1944 |
| 26 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +156 | 18617 |
| 27 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +149 | 5098 |
| 28 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +148 | 22106 |
| 29 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +147 | 24400 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +135 | 23645 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8824 | 224760 |
| 2 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +5713 | 26957 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3568 | 29660 |
| 4 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2857 | 18008 |
| 5 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2813 | 10060 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2462 | 60312 |
| 7 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2250 | 8004 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2193 | 51199 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +2186 | 74774 |
| 10 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2113 | 22058 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1973 | 27480 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1711 | 9570 |
| 13 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1537 | 24527 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1425 | 109881 |
| 15 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1267 | 5897 |
| 16 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1220 | 18735 |
| 17 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1201 | 5344 |
| 18 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1175 | 22106 |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1174 | 24400 |
| 20 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1169 | 8002 |
| 21 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1136 | 24404 |
| 22 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1103 | 18617 |
| 23 | [maderix/ANE](https://github.com/maderix/ANE) | +1094 | 5290 |
| 24 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1039 | 28727 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1019 | 69674 |
| 26 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1010 | 19568 |
| 27 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +986 | 5939 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +958 | 19803 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +941 | 23645 |
| 30 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +927 | 21267 |
| 31 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +901 | 25120 |
| 32 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +851 | 29858 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +848 | 8725 |
| 34 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +846 | 5220 |
| 35 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +843 | 5383 |
| 36 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +830 | 13307 |
| 37 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +811 | 12644 |
| 38 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +800 | 3020 |
| 39 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +795 | 37330 |
| 40 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +795 | 20334 |
| 41 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +751 | 18561 |
| 42 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +743 | 33878 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +738 | 15934 |
| 44 | [superset-sh/superset](https://github.com/superset-sh/superset) | +731 | 4781 |
| 45 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +729 | 4212 |
| 46 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +646 | 22096 |
| 47 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +638 | 34148 |
| 48 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +621 | 5510 |
| 49 | [huggingface/skills](https://github.com/huggingface/skills) | +580 | 8134 |
| 50 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +578 | 6942 |
| 51 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +559 | 12527 |
| 52 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +555 | 22207 |
| 53 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +538 | 2286 |
| 54 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +531 | 9276 |
| 55 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +528 | 30678 |
| 56 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +510 | 3529 |
| 57 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +503 | 2794 |
| 58 | [tobi/qmd](https://github.com/tobi/qmd) | +493 | 12452 |
| 59 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +463 | 2061 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +459 | 27541 |
| 61 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +457 | 9554 |
| 62 | [taigrr/spank](https://github.com/taigrr/spank) | +453 | 1597 |
| 63 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +444 | 14010 |
| 64 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +419 | 1378 |
| 65 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +410 | 12191 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +406 | 13199 |
| 67 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +403 | 1827 |
| 68 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +395 | 8921 |
| 69 | [eooce/python-ws](https://github.com/eooce/python-ws) | +379 | 1349 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +364 | 10854 |
| 71 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +364 | 0 |
| 72 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +341 | 8207 |
| 73 | [block/goose](https://github.com/block/goose) | +334 | 31098 |
| 74 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +332 | 37564 |
| 75 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +330 | 25304 |
| 76 | [srizzon/git-city](https://github.com/srizzon/git-city) | +327 | 1944 |
| 77 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +319 | 1231 |
| 78 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +314 | 26228 |
| 79 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +309 | 9211 |
| 80 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +305 | 5098 |
| 81 | [tw93/Mole](https://github.com/tw93/Mole) | +305 | 36870 |
| 82 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +301 | 1778 |
| 83 | [ItzCrazyKns/Perplexica](https://github.com/ItzCrazyKns/Perplexica) | +299 | 30735 |
| 84 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +294 | 6485 |
| 85 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +292 | 4016 |
| 86 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +291 | 18965 |
| 87 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | +290 | 1935 |
| 88 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +287 | 12129 |
| 89 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +285 | 23580 |
| 90 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +278 | 1248 |
| 91 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +275 | 3399 |
| 92 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +272 | 12462 |
| 93 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +267 | 4076 |
| 94 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +265 | 1128 |
| 95 | [lochie/web-haptics](https://github.com/lochie/web-haptics) | +264 | 1387 |
| 96 | [xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) | +262 | 10177 |
| 97 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +252 | 6416 |
| 98 | [openai/skills](https://github.com/openai/skills) | +252 | 10712 |
| 99 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +243 | 11892 |
| 100 | [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | +242 | 1370 |
| 101 | [mengxi-ream/read-frog](https://github.com/mengxi-ream/read-frog) | +236 | 4415 |
| 102 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +235 | 917 |
| 103 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +229 | 36799 |
| 104 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +228 | 4632 |
| 105 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +220 | 4619 |
| 106 | [wshobson/agents](https://github.com/wshobson/agents) | +214 | 30213 |
| 107 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +212 | 22053 |
| 108 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +211 | 47122 |
| 109 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +197 | 17340 |
| 110 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +196 | 15230 |
| 111 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +196 | 7233 |
| 112 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +191 | 4683 |
| 113 | [puaclaw/PUAClaw](https://github.com/puaclaw/PUAClaw) | +190 | 842 |
| 114 | [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | +188 | 7965 |
| 115 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +185 | 13394 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +182 | 626 |
| 117 | [datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp) | +182 | 871 |
| 118 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +181 | 47936 |
| 119 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +176 | 2757 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +176 | 8980 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30370 | 224760 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7618 | 29660 |
| 3 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +7614 | 29858 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +7601 | 60312 |
| 5 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7162 | 28727 |
| 6 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +7062 | 22106 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6782 | 22096 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +6283 | 26957 |
| 9 | [anthropics/skills](https://github.com/anthropics/skills) | +6141 | 74774 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5998 | 51199 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5628 | 109881 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5560 | 27480 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5042 | 18008 |
| 14 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4382 | 122870 |
| 15 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4334 | 18617 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3954 | 19803 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3669 | 24404 |
| 18 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3529 | 30678 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3450 | 19568 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3285 | 12129 |
| 21 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3249 | 60117 |
| 22 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3228 | 22058 |
| 23 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3183 | 37330 |
| 24 | [google/langextract](https://github.com/google/langextract) | +3004 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2940 | 69674 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2840 | 34148 |
| 27 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2813 | 10060 |
| 28 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2680 | 33878 |
| 29 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2615 | 8641 |
| 30 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2587 | 9033 |
| 31 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2561 | 85286 |
| 32 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2526 | 9570 |
| 33 | [openai/skills](https://github.com/openai/skills) | +2431 | 10712 |
| 34 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2263 | 96919 |
| 35 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2260 | 8725 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2254 | 23645 |
| 37 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2250 | 8004 |
| 38 | [virattt/dexter](https://github.com/virattt/dexter) | +2191 | 17049 |
| 39 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2030 | 20334 |
| 40 | [huggingface/skills](https://github.com/huggingface/skills) | +1976 | 8134 |
| 41 | [github/spec-kit](https://github.com/github/spec-kit) | +1940 | 71722 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1917 | 15934 |
| 43 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1900 | 9590 |
| 44 | [pydantic/monty](https://github.com/pydantic/monty) | +1887 | 5946 |
| 45 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1853 | 9276 |
| 46 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1779 | 10095 |
| 47 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1770 | 8002 |
| 48 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1742 | 6416 |
| 49 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1732 | 8548 |
| 50 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1731 | 17810 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1723 | 147486 |
| 52 | [tobi/qmd](https://github.com/tobi/qmd) | +1717 | 12452 |
| 53 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1713 | 149018 |
| 54 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1696 | 6843 |
| 55 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1679 | 5910 |
| 56 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1660 | 25120 |
| 57 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1647 | 24527 |
| 58 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1644 | 14010 |
| 59 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1643 | 18561 |
| 60 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1516 | 37564 |
| 61 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1515 | 9018 |
| 62 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1512 | 27541 |
| 63 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1511 | 18735 |
| 64 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1504 | 5098 |
| 65 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1503 | 33712 |
| 66 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1502 | 12527 |
| 67 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1498 | 5510 |
| 68 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1496 | 5258 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1488 | 10854 |
| 70 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1469 | 5383 |
| 71 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1467 | 9554 |
| 72 | [tw93/Mole](https://github.com/tw93/Mole) | +1446 | 36870 |
| 73 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1444 | 5939 |
| 74 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1433 | 25304 |
| 75 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1431 | 74887 |
| 76 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1397 | 7811 |
| 77 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1383 | 5344 |
| 78 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1376 | 10151 |
| 79 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1375 | 21267 |
| 80 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1364 | 24400 |
| 81 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1363 | 13307 |
| 82 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1363 | 8761 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1363 | 98536 |
| 84 | [openai/codex](https://github.com/openai/codex) | +1337 | 61744 |
| 85 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1325 | 5897 |
| 86 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1321 | 27464 |
| 87 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1315 | 5489 |
| 88 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1283 | 12644 |
| 89 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1257 | 4632 |
| 90 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1240 | 4161 |
| 91 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1234 | 4447 |
| 92 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +1186 | 4683 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1184 | 13200 |
| 94 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1158 | 87598 |
| 95 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1130 | 4619 |
| 96 | [maderix/ANE](https://github.com/maderix/ANE) | +1095 | 5290 |
| 97 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1091 | 4212 |
| 98 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1087 | 6942 |
| 99 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1046 | 21543 |
| 100 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1017 | 18965 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +990 | 26228 |
| 102 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +989 | 22035 |
| 103 | [superset-sh/superset](https://github.com/superset-sh/superset) | +982 | 4781 |
| 104 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +968 | 3530 |
| 105 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +930 | 23580 |
| 106 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +909 | 11892 |
| 107 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +891 | 61818 |
| 108 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +861 | 5220 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +853 | 22053 |
| 110 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +836 | 18160 |
| 111 | [docling-project/docling](https://github.com/docling-project/docling) | +820 | 54041 |
| 112 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +797 | 3020 |
| 113 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +789 | 47122 |
| 114 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +784 | 8921 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +778 | 8980 |
| 116 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +746 | 13921 |
| 117 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +736 | 36799 |
| 118 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +736 | 43973 |
| 119 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +734 | 11593 |
| 120 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +703 | 15230 |
| 121 | [wshobson/agents](https://github.com/wshobson/agents) | +687 | 30213 |
| 122 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +685 | 7233 |
| 123 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +674 | 13394 |
| 124 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +663 | 30590 |
| 125 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +660 | 8992 |
| 126 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +646 | 4076 |
| 127 | [google-research/timesfm](https://github.com/google-research/timesfm) | +633 | 9950 |
| 128 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +633 | 47936 |
| 129 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +606 | 2063 |
| 130 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +582 | 17574 |
| 131 | [microsoft/qlib](https://github.com/microsoft/qlib) | +578 | 37792 |
| 132 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +559 | 3411 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +558 | 54903 |
| 134 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +549 | 39841 |
| 135 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +528 | 1197 |
| 136 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +527 | 2117 |
| 137 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +521 | 15769 |
| 138 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +520 | 1408 |
| 139 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +504 | 2602 |
| 140 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +500 | 1898 |
| 141 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +488 | 1614 |
| 142 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +488 | 7680 |
| 143 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +484 | 31182 |
| 144 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +483 | 1154 |
| 145 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +479 | 4197 |
| 146 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +472 | 1827 |
| 147 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +470 | 4848 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +460 | 44545 |
| 149 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +455 | 13961 |
| 150 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +455 | 15307 |
| 151 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +445 | 1413 |
| 152 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +445 | 3416 |
| 153 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +441 | 11184 |
| 154 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +435 | 1378 |
| 155 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +434 | 10191 |
| 156 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +430 | 3102 |
| 157 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +428 | 6025 |
| 158 | [samugit83/redamon](https://github.com/samugit83/redamon) | +411 | 1423 |
| 159 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +402 | 25564 |
| 160 | [openclaw/skills](https://github.com/openclaw/skills) | +399 | 1948 |
| 161 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +399 | 2059 |
| 162 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +399 | 36103 |
| 163 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +398 | 10326 |
| 164 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +396 | 5308 |
| 165 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +392 | 44232 |
| 166 | [oraios/serena](https://github.com/oraios/serena) | +387 | 20993 |
| 167 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +383 | 6140 |
| 168 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +380 | 2248 |
| 169 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +380 | 8726 |
| 170 | [eooce/python-ws](https://github.com/eooce/python-ws) | +379 | 1349 |
| 171 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +375 | 15021 |
| 172 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +370 | 3035 |
| 173 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +357 | 1242 |
| 174 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +356 | 1211 |
| 175 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +355 | 11073 |
| 176 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +354 | 1248 |
| 177 | [usestrix/strix](https://github.com/usestrix/strix) | +352 | 20732 |
| 178 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +344 | 8926 |
| 179 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | +343 | 40916 |
| 180 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +342 | 1311 |
| 181 | [DP-Skills/skill-compose](https://github.com/DP-Skills/skill-compose) | +335 | 1110 |
| 182 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +334 | 6977 |
| 183 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +331 | 12617 |
| 184 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +330 | 24078 |
| 185 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +326 | 630 |
| 186 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +326 | 36697 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +323 | 23868 |
| 188 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +321 | 1953 |
| 189 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +319 | 1231 |
| 190 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +313 | 1778 |
| 191 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +309 | 881 |
| 192 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +307 | 3984 |
| 193 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +305 | 1268 |
| 194 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +303 | 20989 |
| 195 | [robinebers/openusage](https://github.com/robinebers/openusage) | +296 | 1165 |
| 196 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +294 | 9752 |
| 197 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +290 | 2437 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +278 | 3286 |
| 199 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +275 | 2797 |
| 200 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +275 | 995 |
| 201 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +275 | 5406 |
| 202 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +266 | 1128 |
| 203 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +266 | 923 |
| 204 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +249 | 832 |
| 205 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +247 | 21160 |
| 206 | [usebruno/bruno](https://github.com/usebruno/bruno) | +247 | 41086 |
| 207 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +245 | 1818 |
| 208 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +241 | 3326 |
| 209 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +234 | 12767 |
| 210 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +233 | 922 |
| 211 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +233 | 22523 |
| 212 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +231 | 6560 |
| 213 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +226 | 2420 |
| 214 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 286 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +218 | 40265 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +218 | 28569 |
| 217 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +209 | 720 |
| 218 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +208 | 790 |
| 219 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 680 |
| 220 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +203 | 635 |
| 221 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +198 | 29780 |
| 222 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +193 | 579 |
| 223 | [VonChange/utao](https://github.com/VonChange/utao) | +186 | 3881 |
| 224 | [qist/tvbox](https://github.com/qist/tvbox) | +185 | 8347 |
| 225 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +180 | 2244 |
| 226 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +179 | 39596 |
| 227 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +178 | 542 |
| 228 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +178 | 8328 |
| 229 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +174 | 607 |
| 230 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +172 | 808 |
| 231 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +172 | 632 |
| 232 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +171 | 3037 |
| 233 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +170 | 33000 |
| 234 | [apify/agent-skills](https://github.com/apify/agent-skills) | +164 | 758 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +164 | 1812 |
| 236 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +160 | 1264 |
| 237 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +157 | 684 |
| 238 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +156 | 13510 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +155 | 25768 |
| 240 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +155 | 733 |
| 241 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +154 | 4751 |
| 242 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +154 | 489 |
| 243 | [bradygaster/squad](https://github.com/bradygaster/squad) | +153 | 611 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +150 | 11792 |
| 245 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +149 | 496 |
| 246 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +145 | 4804 |
| 247 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +143 | 37313 |
| 248 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +142 | 572 |
| 249 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +141 | 28719 |
| 250 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +140 | 6889 |
| 251 | [decolua/9router](https://github.com/decolua/9router) | +140 | 649 |
| 252 | [expo/skills](https://github.com/expo/skills) | +136 | 1324 |
| 253 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +135 | 469 |
| 254 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +128 | 3090 |
| 255 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +127 | 9825 |
| 256 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +126 | 716 |
| 257 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +125 | 1337 |
| 258 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +121 | 3232 |
| 259 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +121 | 48784 |
| 260 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +120 | 3063 |
| 261 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 386 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +114 | 1096 |
| 263 | [fmhy/edit](https://github.com/fmhy/edit) | +112 | 8325 |
| 264 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +109 | 385 |
| 265 | [microg/GmsCore](https://github.com/microg/GmsCore) | +109 | 12446 |
| 266 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +105 | 805 |
| 267 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +102 | 35473 |
| 268 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +101 | 26735 |
| 269 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +100 | 4502 |
| 270 | [skylot/jadx](https://github.com/skylot/jadx) | +99 | 47365 |
| 271 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +98 | 10945 |
| 272 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +97 | 8573 |
| 273 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +95 | 332 |
| 274 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +92 | 3036 |
| 275 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +90 | 2868 |
| 276 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +88 | 328 |
| 277 | [hj01857655/kiro-account-manager](https://github.com/hj01857655/kiro-account-manager) | +88 | 1047 |
| 278 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +88 | 1553 |
| 279 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +88 | 28649 |
| 280 | [iBUHub/AIStudioToAPI](https://github.com/iBUHub/AIStudioToAPI) | +84 | 654 |
| 281 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +84 | 795 |
| 282 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +83 | 276 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +81 | 1199 |
| 284 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +80 | 45263 |
| 285 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 291 |
| 286 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +78 | 3440 |
| 287 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +78 | 5830 |
| 288 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +77 | 240 |
| 289 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +77 | 21297 |
| 290 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +76 | 657 |
| 291 | [dataease/dataease](https://github.com/dataease/dataease) | +76 | 23501 |
| 292 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +75 | 857 |
| 293 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1311 |
| 294 | [FongMi/TV](https://github.com/FongMi/TV) | +75 | 7464 |
| 295 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +75 | 12276 |
| 296 | [apache/kafka](https://github.com/apache/kafka) | +74 | 32043 |
| 297 | [openjdk/jdk](https://github.com/openjdk/jdk) | +74 | 22694 |
| 298 | [maile456/qq-farm-bot](https://github.com/maile456/qq-farm-bot) | +72 | 230 |
| 299 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +71 | 794 |
| 300 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +71 | 686 |
