---
title: "2026-03-03 GitHub增长趋势报告"
description: "1.wifi-densepose+1146 2.worldmonitor+903 3.ANE+779 4.CoPaw+553 5.everything-claude-code+350"
date: 2026-03-03T20:35:33+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-03 20:35:33

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
        'daily': {"categories": ["qwibitai/nanoclaw", "farion1231/cc-switch", "HKUDS/nanobot", "D4Vinci/Scrapling", "mengxi-ream/read-frog", "superset-sh/superset", "ruvnet/ruflo", "vercel-labs/agent-browser", "K-Dense-AI/claude-scientific-skills", "RightNow-AI/openfang", "moeru-ai/airi", "abhigyanpatwari/GitNexus", "alibaba/OpenSandbox", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "affaan-m/everything-claude-code", "agentscope-ai/CoPaw", "maderix/ANE", "koala73/worldmonitor", "ruvnet/wifi-densepose"], "data": [130, 132, 141, 151, 155, 159, 186, 187, 200, 221, 227, 234, 256, 315, 333, 350, 553, 779, 903, 1146]},
        'weekly': {"categories": ["zeroclaw-labs/zeroclaw", "gsd-build/get-shit-done", "moeru-ai/airi", "anthropics/financial-services-plugins", "cloudflare/vinext", "x1xhlol/system-prompts-and-models-of-ai-tools", "anomalyco/opencode", "zarazhangrui/frontend-slides", "abhigyanpatwari/GitNexus", "VoltAgent/awesome-openclaw-skills", "agentscope-ai/CoPaw", "affaan-m/everything-claude-code", "anthropics/skills", "D4Vinci/Scrapling", "obra/superpowers", "RightNow-AI/openfang", "hesamsheikh/awesome-openclaw-usecases", "koala73/worldmonitor", "ruvnet/wifi-densepose", "openclaw/openclaw"], "data": [1221, 1229, 1276, 1356, 1378, 1472, 1475, 1501, 1767, 1951, 1980, 1995, 2091, 2308, 2390, 2704, 2857, 3096, 5171, 8228]},
        'monthly': {"categories": ["jamiepine/voicebox", "sickn33/antigravity-awesome-skills", "gsd-build/get-shit-done", "badlogic/pi-mono", "thedotmack/claude-mem", "x1xhlol/system-prompts-and-models-of-ai-tools", "qwibitai/nanoclaw", "hesamsheikh/awesome-openclaw-usecases", "VoltAgent/awesome-openclaw-skills", "anomalyco/opencode", "ruvnet/wifi-densepose", "affaan-m/everything-claude-code", "anthropics/skills", "sipeed/picoclaw", "koala73/worldmonitor", "zeroclaw-labs/zeroclaw", "KeygraphHQ/shannon", "HKUDS/nanobot", "obra/superpowers", "openclaw/openclaw"], "data": [3281, 3371, 3614, 3972, 4010, 4359, 4396, 4826, 5536, 5667, 5751, 5797, 6058, 6735, 6826, 6919, 7166, 7424, 7469, 30101]}
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
| 1 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +1146 | 25029 |
| 2 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +903 | 26989 |
| 3 | [maderix/ANE](https://github.com/maderix/ANE) | +779 | 4374 |
| 4 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +553 | 7128 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +350 | 51199 |
| 6 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +333 | 17056 |
| 7 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +315 | 26423 |
| 8 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +256 | 5265 |
| 9 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +234 | 9068 |
| 10 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +227 | 22083 |
| 11 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +221 | 9605 |
| 12 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +200 | 11796 |
| 13 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +187 | 17957 |
| 14 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +186 | 18508 |
| 15 | [superset-sh/superset](https://github.com/superset-sh/superset) | +159 | 4010 |
| 16 | [mengxi-ream/read-frog](https://github.com/mengxi-ream/read-frog) | +155 | 4215 |
| 17 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +151 | 20851 |
| 18 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +141 | 28264 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +132 | 23154 |
| 20 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +130 | 18082 |
| 21 | [tobi/qmd](https://github.com/tobi/qmd) | +128 | 12059 |
| 22 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +124 | 20804 |
| 23 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +119 | 23975 |
| 24 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +118 | 15646 |
| 25 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +117 | 21653 |
| 26 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +117 | 5712 |
| 27 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +116 | 5234 |
| 28 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +113 | 1736 |
| 29 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +107 | 33878 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +107 | 23895 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8228 | 224760 |
| 2 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +5171 | 25029 |
| 3 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3096 | 26989 |
| 4 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2857 | 17056 |
| 5 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2704 | 9605 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2390 | 60312 |
| 7 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2308 | 20851 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +2091 | 74774 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1995 | 51199 |
| 10 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1980 | 7128 |
| 11 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1951 | 26423 |
| 12 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1767 | 9068 |
| 13 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1501 | 7707 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1475 | 109881 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1472 | 122870 |
| 16 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1378 | 5712 |
| 17 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1356 | 5289 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1276 | 22083 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1229 | 23895 |
| 20 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1221 | 21653 |
| 21 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1165 | 18508 |
| 22 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1141 | 18082 |
| 23 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1089 | 28264 |
| 24 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1087 | 5265 |
| 25 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1045 | 23975 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1041 | 19382 |
| 27 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1024 | 13184 |
| 28 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1023 | 69674 |
| 29 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +968 | 18545 |
| 30 | [huggingface/skills](https://github.com/huggingface/skills) | +944 | 8008 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +911 | 23154 |
| 32 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +883 | 24830 |
| 33 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +875 | 20804 |
| 34 | [maderix/ANE](https://github.com/maderix/ANE) | +836 | 4374 |
| 35 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +817 | 20118 |
| 36 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +794 | 4966 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +763 | 15646 |
| 38 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +763 | 33878 |
| 39 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +734 | 21857 |
| 40 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +729 | 37330 |
| 41 | [clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB) | +684 | 22091 |
| 42 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +675 | 17957 |
| 43 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +668 | 6838 |
| 44 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +642 | 34148 |
| 45 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +626 | 11796 |
| 46 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +601 | 5234 |
| 47 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +588 | 12436 |
| 48 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +558 | 7198 |
| 49 | [superset-sh/superset](https://github.com/superset-sh/superset) | +553 | 4010 |
| 50 | [ruvnet/ruvector](https://github.com/ruvnet/ruvector) | +540 | 2643 |
| 51 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +511 | 30678 |
| 52 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +511 | 8952 |
| 53 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +510 | 3145 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +469 | 27272 |
| 55 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +459 | 1793 |
| 56 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +457 | 13850 |
| 57 | [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | +457 | 3054 |
| 58 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +443 | 27479 |
| 59 | [tobi/qmd](https://github.com/tobi/qmd) | +433 | 12059 |
| 60 | [taigrr/spank](https://github.com/taigrr/spank) | +423 | 1333 |
| 61 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +410 | 1302 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +404 | 12058 |
| 63 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +404 | 8794 |
| 64 | [KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh](https://github.com/KimYx0207/Claude-Code-x-OpenClaw-Guide-Zh) | +393 | 0 |
| 65 | [netease-youdao/LobsterAI](https://github.com/netease-youdao/LobsterAI) | +391 | 3296 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +388 | 12960 |
| 67 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +387 | 1736 |
| 68 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +384 | 9194 |
| 69 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +374 | 37564 |
| 70 | [eooce/python-ws](https://github.com/eooce/python-ws) | +369 | 1283 |
| 71 | [Polymarket/polymarket-cli](https://github.com/Polymarket/polymarket-cli) | +344 | 1511 |
| 72 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +337 | 25168 |
| 73 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +333 | 10510 |
| 74 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +329 | 1688 |
| 75 | [block/goose](https://github.com/block/goose) | +327 | 31098 |
| 76 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +327 | 12035 |
| 77 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +315 | 7971 |
| 78 | [kevinho/clawfeed](https://github.com/kevinho/clawfeed) | +310 | 1496 |
| 79 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +306 | 9049 |
| 80 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +303 | 8977 |
| 81 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +298 | 1167 |
| 82 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 26051 |
| 83 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +296 | 6277 |
| 84 | [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | +285 | 1796 |
| 85 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +283 | 18759 |
| 86 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +281 | 6292 |
| 87 | [tw93/Mole](https://github.com/tw93/Mole) | +279 | 36870 |
| 88 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +275 | 12339 |
| 89 | [alibaba/zvec](https://github.com/alibaba/zvec) | +274 | 8598 |
| 90 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +270 | 11770 |
| 91 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +267 | 1208 |
| 92 | [openai/skills](https://github.com/openai/skills) | +264 | 10566 |
| 93 | [openclaw/clawhub](https://github.com/openclaw/clawhub) | +263 | 3759 |
| 94 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +262 | 2298 |
| 95 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +261 | 4519 |
| 96 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +255 | 4002 |
| 97 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +252 | 23411 |
| 98 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +246 | 3105 |
| 99 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +244 | 36799 |
| 100 | [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | +243 | 1331 |
| 101 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +239 | 1053 |
| 102 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +234 | 9529 |
| 103 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +227 | 47122 |
| 104 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +221 | 7167 |
| 105 | [wshobson/agents](https://github.com/wshobson/agents) | +212 | 30086 |
| 106 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +203 | 15119 |
| 107 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +202 | 21950 |
| 108 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +194 | 4603 |
| 109 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +194 | 30590 |
| 110 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +192 | 4408 |
| 111 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +184 | 13283 |
| 112 | [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent) | +184 | 7933 |
| 113 | [KuekHaoYang/KVideo](https://github.com/KuekHaoYang/KVideo) | +180 | 2731 |
| 114 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +180 | 8482 |
| 115 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +177 | 2379 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +176 | 8851 |
| 117 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +175 | 597 |
| 118 | [datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp) | +172 | 836 |
| 119 | [google/langextract](https://github.com/google/langextract) | +168 | 33636 |
| 120 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +165 | 47936 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +30101 | 224760 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | +7469 | 60312 |
| 3 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +7424 | 28264 |
| 4 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +7166 | 27480 |
| 5 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +6919 | 21653 |
| 6 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +6826 | 26990 |
| 7 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +6735 | 21857 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills) | +6058 | 74774 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5797 | 51199 |
| 10 | [ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose) | +5751 | 25030 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5667 | 109881 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5536 | 26423 |
| 13 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +4826 | 17056 |
| 14 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4396 | 18082 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4359 | 122870 |
| 16 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4010 | 30678 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +3972 | 19382 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3614 | 23895 |
| 19 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3371 | 18545 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3281 | 12035 |
| 21 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +3252 | 60117 |
| 22 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +3123 | 37330 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +3004 | 20851 |
| 24 | [google/langextract](https://github.com/google/langextract) | +3000 | 33636 |
| 25 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2908 | 69674 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2865 | 34148 |
| 27 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +2704 | 9605 |
| 28 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +2702 | 33878 |
| 29 | [alibaba/zvec](https://github.com/alibaba/zvec) | +2615 | 8598 |
| 30 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2569 | 8977 |
| 31 | [openai/skills](https://github.com/openai/skills) | +2560 | 10566 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2522 | 85286 |
| 33 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2356 | 9068 |
| 34 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +2258 | 96919 |
| 35 | [virattt/dexter](https://github.com/virattt/dexter) | +2250 | 16898 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2200 | 23154 |
| 37 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +2036 | 20118 |
| 38 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1986 | 7129 |
| 39 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1984 | 8952 |
| 40 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1962 | 8482 |
| 41 | [huggingface/skills](https://github.com/huggingface/skills) | +1950 | 8008 |
| 42 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1922 | 7198 |
| 43 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +1917 | 6748 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1901 | 15646 |
| 45 | [accomplish-ai/accomplish](https://github.com/accomplish-ai/accomplish) | +1893 | 9529 |
| 46 | [github/spec-kit](https://github.com/github/spec-kit) | +1888 | 71722 |
| 47 | [pydantic/monty](https://github.com/pydantic/monty) | +1880 | 5916 |
| 48 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1754 | 10042 |
| 49 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +1731 | 7707 |
| 50 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1731 | 149018 |
| 51 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1724 | 6292 |
| 52 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1724 | 17722 |
| 53 | [f/prompts.chat](https://github.com/f/prompts.chat) | +1720 | 147486 |
| 54 | [tobi/qmd](https://github.com/tobi/qmd) | +1680 | 12059 |
| 55 | [fluxerapp/fluxer](https://github.com/fluxerapp/fluxer) | +1664 | 5867 |
| 56 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1645 | 24830 |
| 57 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1621 | 13850 |
| 58 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +1568 | 12436 |
| 59 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1537 | 17957 |
| 60 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1523 | 37564 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1521 | 27272 |
| 62 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +1510 | 9006 |
| 63 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +1500 | 33712 |
| 64 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +1489 | 5207 |
| 65 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1457 | 18508 |
| 66 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | +1453 | 25168 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1437 | 10510 |
| 68 | [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | +1420 | 5234 |
| 69 | [tw93/Mole](https://github.com/tw93/Mole) | +1418 | 36870 |
| 70 | [RunanywhereAI/runanywhere-sdks](https://github.com/RunanywhereAI/runanywhere-sdks) | +1415 | 10145 |
| 71 | [aden-hive/hive](https://github.com/aden-hive/hive) | +1400 | 8689 |
| 72 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1390 | 22083 |
| 73 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +1383 | 74887 |
| 74 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1382 | 4966 |
| 75 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1381 | 5712 |
| 76 | [blackboardsh/electrobun](https://github.com/blackboardsh/electrobun) | +1380 | 7705 |
| 77 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1378 | 9194 |
| 78 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1367 | 98536 |
| 79 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +1358 | 4732 |
| 80 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1356 | 5289 |
| 81 | [openai/codex](https://github.com/openai/codex) | +1343 | 61744 |
| 82 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1341 | 13184 |
| 83 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +1313 | 27356 |
| 84 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1303 | 20804 |
| 85 | [steipete/gogcli](https://github.com/steipete/gogcli) | +1295 | 5374 |
| 86 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +1265 | 4603 |
| 87 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +1229 | 4408 |
| 88 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1225 | 23975 |
| 89 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1220 | 4099 |
| 90 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +1191 | 4362 |
| 91 | [slopus/happy](https://github.com/slopus/happy) | +1178 | 14109 |
| 92 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1159 | 12960 |
| 93 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1152 | 4519 |
| 94 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1149 | 5265 |
| 95 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +1136 | 32872 |
| 96 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1133 | 87598 |
| 97 | [blader/humanizer](https://github.com/blader/humanizer) | +1106 | 7573 |
| 98 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1087 | 11797 |
| 99 | [moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine) | +1066 | 6838 |
| 100 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +1034 | 21333 |
| 101 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +998 | 21939 |
| 102 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +984 | 95547 |
| 103 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +977 | 18759 |
| 104 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +971 | 11770 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +963 | 26051 |
| 106 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +930 | 3105 |
| 107 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +909 | 23411 |
| 108 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +883 | 61818 |
| 109 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +843 | 21950 |
| 110 | [maderix/ANE](https://github.com/maderix/ANE) | +840 | 4374 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +828 | 18116 |
| 112 | [docling-project/docling](https://github.com/docling-project/docling) | +812 | 54041 |
| 113 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +790 | 43973 |
| 114 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +785 | 47122 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +781 | 8851 |
| 116 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +771 | 8794 |
| 117 | [originalankur/maptoposter](https://github.com/originalankur/maptoposter) | +768 | 11549 |
| 118 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +753 | 13869 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +741 | 15119 |
| 120 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +726 | 36799 |
| 121 | [wshobson/agents](https://github.com/wshobson/agents) | +682 | 30086 |
| 122 | [GetStream/Vision-Agents](https://github.com/GetStream/Vision-Agents) | +681 | 7167 |
| 123 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +678 | 8945 |
| 124 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +670 | 30590 |
| 125 | [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn) | +666 | 13283 |
| 126 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +635 | 4002 |
| 127 | [google-research/timesfm](https://github.com/google-research/timesfm) | +633 | 9946 |
| 128 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +613 | 47936 |
| 129 | [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | +599 | 2022 |
| 130 | [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot) | +585 | 17564 |
| 131 | [microsoft/qlib](https://github.com/microsoft/qlib) | +580 | 37792 |
| 132 | [thu-pacman/chitu](https://github.com/thu-pacman/chitu) | +550 | 3388 |
| 133 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +538 | 39841 |
| 134 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +537 | 31182 |
| 135 | [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) | +522 | 15289 |
| 136 | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) | +521 | 2099 |
| 137 | [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | +520 | 1407 |
| 138 | [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero) | +517 | 15721 |
| 139 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +514 | 1146 |
| 140 | [RichardAtCT/claude-code-telegram](https://github.com/RichardAtCT/claude-code-telegram) | +499 | 1872 |
| 141 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +498 | 2543 |
| 142 | [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | +496 | 7592 |
| 143 | [HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) | +494 | 4191 |
| 144 | [HKUDS/FastCode](https://github.com/HKUDS/FastCode) | +486 | 1586 |
| 145 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +480 | 1150 |
| 146 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +467 | 4793 |
| 147 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +460 | 1793 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +458 | 44545 |
| 149 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +450 | 13925 |
| 150 | [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | +448 | 24008 |
| 151 | [ShinMegamiBoson/OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter) | +444 | 1404 |
| 152 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +443 | 3349 |
| 153 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +440 | 10128 |
| 154 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +434 | 11154 |
| 155 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +426 | 3039 |
| 156 | [freemocap/freemocap](https://github.com/freemocap/freemocap) | +423 | 6005 |
| 157 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +416 | 1302 |
| 158 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +407 | 1849 |
| 159 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +406 | 36103 |
| 160 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +404 | 1976 |
| 161 | [samugit83/redamon](https://github.com/samugit83/redamon) | +402 | 1398 |
| 162 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +397 | 10322 |
| 163 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +395 | 25489 |
| 164 | [openclaw/skills](https://github.com/openclaw/skills) | +392 | 1865 |
| 165 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +387 | 6099 |
| 166 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +387 | 1204 |
| 167 | [oraios/serena](https://github.com/oraios/serena) | +386 | 20937 |
| 168 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +384 | 5250 |
| 169 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +382 | 44232 |
| 170 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +380 | 2986 |
| 171 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | +375 | 14991 |
| 172 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +375 | 8714 |
| 173 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +371 | 2190 |
| 174 | [eooce/python-ws](https://github.com/eooce/python-ws) | +366 | 1283 |
| 175 | [usestrix/strix](https://github.com/usestrix/strix) | +366 | 20706 |
| 176 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +357 | 12876 |
| 177 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +351 | 6956 |
| 178 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +351 | 11038 |
| 179 | [aeromomo/claw-compactor](https://github.com/aeromomo/claw-compactor) | +349 | 1217 |
| 180 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +343 | 8881 |
| 181 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +342 | 24028 |
| 182 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +337 | 1208 |
| 183 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +334 | 1259 |
| 184 | [vnpy/vnpy](https://github.com/vnpy/vnpy) | +334 | 36870 |
| 185 | [Anionex/banana-slides](https://github.com/Anionex/banana-slides) | +332 | 12552 |
| 186 | [drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) | +330 | 36697 |
| 187 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +329 | 28917 |
| 188 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +325 | 611 |
| 189 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +321 | 23820 |
| 190 | [jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli) | +315 | 1909 |
| 191 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +313 | 3941 |
| 192 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +309 | 879 |
| 193 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +302 | 20958 |
| 194 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +297 | 1167 |
| 195 | [robinebers/openusage](https://github.com/robinebers/openusage) | +296 | 1147 |
| 196 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +285 | 1323 |
| 197 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +283 | 2414 |
| 198 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +282 | 1157 |
| 199 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +281 | 9696 |
| 200 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +277 | 5399 |
| 201 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +272 | 3226 |
| 202 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +267 | 960 |
| 203 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +256 | 878 |
| 204 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +247 | 831 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +247 | 41086 |
| 206 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +246 | 3318 |
| 207 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +245 | 1802 |
| 208 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +244 | 21126 |
| 209 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +242 | 902 |
| 210 | [mgechev/skills-best-practices](https://github.com/mgechev/skills-best-practices) | +239 | 1053 |
| 211 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +237 | 22508 |
| 212 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +233 | 12750 |
| 213 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +227 | 6533 |
| 214 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +226 | 2417 |
| 215 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +224 | 299 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +219 | 28550 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +216 | 40265 |
| 218 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +209 | 710 |
| 219 | [deepentropy/tvscreener](https://github.com/deepentropy/tvscreener) | +208 | 790 |
| 220 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +206 | 680 |
| 221 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +204 | 625 |
| 222 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +193 | 576 |
| 223 | [VonChange/utao](https://github.com/VonChange/utao) | +187 | 3880 |
| 224 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +186 | 29780 |
| 225 | [qist/tvbox](https://github.com/qist/tvbox) | +183 | 8331 |
| 226 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +180 | 39596 |
| 227 | [stoatchat/self-hosted](https://github.com/stoatchat/self-hosted) | +180 | 2239 |
| 228 | [linguo2625469/qq-farm-bot](https://github.com/linguo2625469/qq-farm-bot) | +177 | 533 |
| 229 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +174 | 8316 |
| 230 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +172 | 33000 |
| 231 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +171 | 575 |
| 232 | [tonyqinatcmu/SlideBot-AI](https://github.com/tonyqinatcmu/SlideBot-AI) | +171 | 673 |
| 233 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +171 | 3021 |
| 234 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +168 | 1796 |
| 235 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +165 | 571 |
| 236 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +162 | 684 |
| 237 | [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw) | +161 | 1249 |
| 238 | [apify/agent-skills](https://github.com/apify/agent-skills) | +158 | 679 |
| 239 | [ConardLi/easy-dataset](https://github.com/ConardLi/easy-dataset) | +158 | 13500 |
| 240 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +157 | 737 |
| 241 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +155 | 25748 |
| 242 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +152 | 479 |
| 243 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +151 | 4718 |
| 244 | [Aitenry/IIMS-By-AI](https://github.com/Aitenry/IIMS-By-AI) | +150 | 492 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +149 | 11771 |
| 246 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +146 | 6880 |
| 247 | [bradygaster/squad](https://github.com/bradygaster/squad) | +146 | 583 |
| 248 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +146 | 4792 |
| 249 | [decolua/9router](https://github.com/decolua/9router) | +143 | 635 |
| 250 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +141 | 565 |
| 251 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +141 | 28704 |
| 252 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +141 | 37313 |
| 253 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +133 | 461 |
| 254 | [expo/skills](https://github.com/expo/skills) | +132 | 1302 |
| 255 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +132 | 3082 |
| 256 | [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys) | +130 | 8449 |
| 257 | [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | +129 | 707 |
| 258 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +127 | 1319 |
| 259 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +125 | 9811 |
| 260 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +124 | 48784 |
| 261 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +121 | 3227 |
| 262 | [ailyProject/aily-blockly-libraries](https://github.com/ailyProject/aily-blockly-libraries) | +120 | 546 |
| 263 | [journey-ad/gemini-watermark-remover](https://github.com/journey-ad/gemini-watermark-remover) | +119 | 3044 |
| 264 | [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | +116 | 385 |
| 265 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +111 | 792 |
| 266 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +110 | 1078 |
| 267 | [microg/GmsCore](https://github.com/microg/GmsCore) | +110 | 12434 |
| 268 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +109 | 381 |
| 269 | [cporter202/scraping-apis-for-devs](https://github.com/cporter202/scraping-apis-for-devs) | +105 | 3033 |
| 270 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +103 | 26728 |
| 271 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +102 | 4496 |
| 272 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +100 | 35473 |
| 273 | [skylot/jadx](https://github.com/skylot/jadx) | +96 | 47365 |
| 274 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +95 | 10922 |
| 275 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +94 | 8551 |
| 276 | [nicobailon/surf-cli](https://github.com/nicobailon/surf-cli) | +93 | 329 |
| 277 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +90 | 2852 |
| 278 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +89 | 1529 |
| 279 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +88 | 308 |
| 280 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +84 | 28646 |
| 281 | [zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | +80 | 264 |
| 282 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +79 | 290 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +78 | 1185 |
| 284 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +78 | 21289 |
| 285 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +78 | 12273 |
| 286 | [shiroha-233/MC-MMD-rust](https://github.com/shiroha-233/MC-MMD-rust) | +77 | 236 |
| 287 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +77 | 3436 |
| 288 | [Archmage83/tvapk](https://github.com/Archmage83/tvapk) | +77 | 5826 |
| 289 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +76 | 45263 |
| 290 | [dataease/dataease](https://github.com/dataease/dataease) | +76 | 23497 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +75 | 848 |
| 292 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +75 | 758 |
| 293 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +75 | 1309 |
| 294 | [openjdk/jdk](https://github.com/openjdk/jdk) | +75 | 22654 |
| 295 | [shining-stars-l/javaup](https://github.com/shining-stars-l/javaup) | +74 | 686 |
| 296 | [FongMi/TV](https://github.com/FongMi/TV) | +74 | 7462 |
| 297 | [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) | +74 | 23980 |
| 298 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +73 | 643 |
| 299 | [apache/kafka](https://github.com/apache/kafka) | +72 | 32043 |
| 300 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +71 | 779 |
