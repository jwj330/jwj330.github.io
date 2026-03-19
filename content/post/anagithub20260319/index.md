---
title: "2026-03-19 GitHub增长趋势报告"
description: "1.skills+350 2.claude-hud+305 3.OpenMAIC+288 4.agency-agents+259 5.autoresearch+258"
date: 2026-03-19T20:40:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-03-19 20:40:48

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
        'daily': {"categories": ["louis-e/arnis", "sgoudelis/ground-station", "jackwener/opencli", "langchain-ai/deepagents", "farion1231/cc-switch", "ZhuLinsen/daily_stock_analysis", "langchain-ai/open-swe", "paperclipai/paperclip", "aiming-lab/AutoResearchClaw", "nextlevelbuilder/ui-ux-pro-max-skill", "calesthio/Crucix", "opendataloader-project/opendataloader-pdf", "gsd-build/get-shit-done", "666ghj/MiroFish", "shareAI-lab/learn-claude-code", "karpathy/autoresearch", "msitarzewski/agency-agents", "THU-MAIC/OpenMAIC", "jarrodwatts/claude-hud", "mattpocock/skills"], "data": [106, 107, 108, 117, 117, 122, 135, 150, 154, 174, 178, 199, 230, 230, 234, 258, 259, 288, 305, 350]},
        'weekly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "aiming-lab/AutoResearchClaw", "p-e-w/heretic", "abhigyanpatwari/GitNexus", "shanraisshan/claude-code-best-practice", "anthropics/skills", "pbakaus/impeccable", "alibaba/page-agent", "gsd-build/get-shit-done", "THU-MAIC/OpenMAIC", "shareAI-lab/learn-claude-code", "paperclipai/paperclip", "lightpanda-io/browser", "volcengine/OpenViking", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "666ghj/MiroFish", "openclaw/openclaw", "msitarzewski/agency-agents"], "data": [933, 970, 1003, 1031, 1110, 1118, 1174, 1213, 1232, 1384, 1547, 1840, 1853, 2038, 2591, 2999, 3442, 3464, 3841, 4505]},
        'monthly': {"categories": ["AlexsJones/llmfit", "abhigyanpatwari/GitNexus", "moeru-ai/airi", "gsd-build/get-shit-done", "anomalyco/opencode", "x1xhlol/system-prompts-and-models-of-ai-tools", "googleworkspace/cli", "D4Vinci/Scrapling", "VoltAgent/awesome-openclaw-skills", "hesamsheikh/awesome-openclaw-usecases", "anthropics/skills", "666ghj/MiroFish", "paperclipai/paperclip", "koala73/worldmonitor", "ruvnet/RuView", "affaan-m/everything-claude-code", "karpathy/autoresearch", "obra/superpowers", "msitarzewski/agency-agents", "openclaw/openclaw"], "data": [4050, 4159, 4258, 4331, 4484, 4622, 4688, 5211, 5481, 5574, 6107, 6224, 6370, 7737, 8407, 8957, 9010, 9506, 10770, 29226]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +350 | 6149 |
| 2 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +305 | 8409 |
| 3 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +288 | 9061 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +259 | 55326 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +258 | 43527 |
| 6 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +234 | 33509 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +230 | 35685 |
| 8 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +230 | 35908 |
| 9 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +199 | 5388 |
| 10 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +178 | 5098 |
| 11 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +174 | 34148 |
| 12 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +154 | 6728 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +150 | 29798 |
| 14 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +135 | 6951 |
| 15 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +122 | 23278 |
| 16 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +117 | 30511 |
| 17 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +117 | 15538 |
| 18 | [jackwener/opencli](https://github.com/jackwener/opencli) | +108 | 2365 |
| 19 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +107 | 2782 |
| 20 | [louis-e/arnis](https://github.com/louis-e/arnis) | +106 | 10608 |
| 21 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +104 | 11766 |
| 22 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +97 | 22165 |
| 23 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | +95 | 1862 |
| 24 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +93 | 1772 |
| 25 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +90 | 17934 |
| 26 | [mobile-dev-inc/Maestro](https://github.com/mobile-dev-inc/Maestro) | +88 | 12374 |
| 27 | [Diolinux/PhotoGIMP](https://github.com/Diolinux/PhotoGIMP) | +86 | 7577 |
| 28 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +81 | 41109 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +81 | 10906 |
| 30 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +79 | 10579 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4505 | 55326 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3841 | 224760 |
| 3 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3464 | 35685 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3442 | 60312 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2999 | 43527 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2591 | 51199 |
| 7 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2038 | 16265 |
| 8 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1853 | 22165 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1840 | 29798 |
| 10 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1547 | 33509 |
| 11 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1384 | 9061 |
| 12 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1232 | 35908 |
| 13 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1213 | 11766 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1174 | 10903 |
| 15 | [anthropics/skills](https://github.com/anthropics/skills) | +1118 | 74774 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1110 | 18895 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1031 | 17934 |
| 18 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1003 | 16088 |
| 19 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +970 | 6728 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +933 | 34148 |
| 21 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +900 | 17642 |
| 22 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +885 | 15538 |
| 23 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +872 | 35857 |
| 24 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +858 | 41109 |
| 25 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +836 | 23278 |
| 26 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +795 | 10579 |
| 27 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +764 | 26009 |
| 28 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +756 | 5098 |
| 29 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +709 | 3398 |
| 30 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +678 | 39727 |
| 31 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +665 | 30678 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +651 | 30511 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +646 | 10906 |
| 34 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +644 | 9108 |
| 35 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +607 | 12774 |
| 36 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +601 | 38309 |
| 37 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +597 | 25897 |
| 38 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +593 | 3481 |
| 39 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +588 | 8409 |
| 40 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +572 | 43973 |
| 41 | [mattpocock/skills](https://github.com/mattpocock/skills) | +543 | 6149 |
| 42 | [systemdesign42/system-design-academy](https://github.com/systemdesign42/system-design-academy) | +534 | 23743 |
| 43 | [EdoStra/Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders) | +531 | 5778 |
| 44 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +531 | 17985 |
| 45 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +524 | 2595 |
| 46 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +515 | 37330 |
| 47 | [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | +504 | 2889 |
| 48 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +490 | 18228 |
| 49 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +485 | 8467 |
| 50 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +469 | 32353 |
| 51 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +469 | 2269 |
| 52 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +467 | 24339 |
| 53 | [jundot/omlx](https://github.com/jundot/omlx) | +464 | 5964 |
| 54 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +461 | 3379 |
| 55 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +458 | 31246 |
| 56 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +455 | 34934 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +453 | 7097 |
| 58 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +441 | 4935 |
| 59 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +438 | 26206 |
| 60 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +435 | 23622 |
| 61 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +428 | 33878 |
| 62 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +425 | 7353 |
| 63 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +424 | 31868 |
| 64 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +421 | 28292 |
| 65 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +412 | 25903 |
| 66 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +411 | 2631 |
| 67 | [jackwener/opencli](https://github.com/jackwener/opencli) | +410 | 2365 |
| 68 | [tw93/Mole](https://github.com/tw93/Mole) | +407 | 36870 |
| 69 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +407 | 21638 |
| 70 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +403 | 12703 |
| 71 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +394 | 5345 |
| 72 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +390 | 34647 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +383 | 5388 |
| 74 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +360 | 28028 |
| 75 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +356 | 5079 |
| 76 | [openai/symphony](https://github.com/openai/symphony) | +340 | 13509 |
| 77 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +339 | 3673 |
| 78 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +328 | 28745 |
| 79 | [novatic14/MANPADS-System-Launcher-and-Rocket](https://github.com/novatic14/MANPADS-System-Launcher-and-Rocket) | +327 | 1908 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +326 | 14806 |
| 81 | [kepano/defuddle](https://github.com/kepano/defuddle) | +324 | 5517 |
| 82 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +313 | 3790 |
| 83 | [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | +312 | 2487 |
| 84 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +307 | 1328 |
| 85 | [MoonshotAI/Attention-Residuals](https://github.com/MoonshotAI/Attention-Residuals) | +306 | 1990 |
| 86 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +294 | 1780 |
| 87 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +291 | 29175 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +290 | 21893 |
| 89 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +288 | 30313 |
| 90 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +286 | 5960 |
| 91 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +284 | 2782 |
| 92 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +282 | 13179 |
| 93 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +281 | 2598 |
| 94 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +279 | 2024 |
| 95 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +268 | 25492 |
| 96 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +263 | 10014 |
| 97 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +263 | 35735 |
| 98 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +262 | 14358 |
| 99 | [epiral/bb-browser](https://github.com/epiral/bb-browser) | +260 | 1434 |
| 100 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +256 | 4325 |
| 101 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +253 | 5968 |
| 102 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +252 | 1449 |
| 103 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +228 | 1444 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +225 | 6381 |
| 105 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +223 | 6951 |
| 106 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +210 | 8753 |
| 107 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +209 | 1772 |
| 108 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +203 | 45886 |
| 109 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +198 | 9998 |
| 110 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +197 | 3051 |
| 111 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +193 | 30590 |
| 112 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +192 | 16346 |
| 113 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +191 | 22306 |
| 114 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +186 | 2616 |
| 115 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +181 | 26071 |
| 116 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +179 | 47936 |
| 117 | [Janis174756/Binance-Futures-Trading-Bot](https://github.com/Janis174756/Binance-Futures-Trading-Bot) | +169 | 544 |
| 118 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +169 | 15539 |
| 119 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +166 | 1151 |
| 120 | [htdt/godogen](https://github.com/htdt/godogen) | +156 | 1117 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +29226 | 224760 |
| 2 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +10770 | 55326 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +9506 | 60312 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +9010 | 43527 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8957 | 51199 |
| 6 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +8407 | 38309 |
| 7 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +7737 | 41109 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6370 | 29798 |
| 9 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6224 | 35685 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +6107 | 74774 |
| 11 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +5574 | 26206 |
| 12 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +5481 | 39727 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +5211 | 31246 |
| 14 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4688 | 21638 |
| 15 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +4622 | 122870 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4484 | 109881 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4331 | 35909 |
| 18 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +4258 | 34647 |
| 19 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4159 | 17934 |
| 20 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4050 | 17985 |
| 21 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +4028 | 14984 |
| 22 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +4013 | 24339 |
| 23 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +3773 | 28028 |
| 24 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3681 | 33510 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3671 | 18895 |
| 26 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3400 | 34934 |
| 27 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +3374 | 12703 |
| 28 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +3085 | 25903 |
| 29 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3057 | 69674 |
| 30 | [openai/symphony](https://github.com/openai/symphony) | +2952 | 13509 |
| 31 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2939 | 25897 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2802 | 34148 |
| 33 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2778 | 16265 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2738 | 30511 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2709 | 23278 |
| 36 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2682 | 31868 |
| 37 | [saturndec/waoowaoo](https://github.com/saturndec/waoowaoo) | +2650 | 9795 |
| 38 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2629 | 10100 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2615 | 85286 |
| 40 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2547 | 13549 |
| 41 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | +2508 | 25492 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2419 | 37330 |
| 43 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +2411 | 34051 |
| 44 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2382 | 10014 |
| 45 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +2340 | 60117 |
| 46 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2297 | 33878 |
| 47 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2276 | 11766 |
| 48 | [huggingface/skills](https://github.com/huggingface/skills) | +2226 | 9415 |
| 49 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2153 | 10413 |
| 50 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2136 | 26009 |
| 51 | [f/prompts.chat](https://github.com/f/prompts.chat) | +2128 | 147486 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2083 | 10903 |
| 53 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2042 | 30678 |
| 54 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +2037 | 10489 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2033 | 23622 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1994 | 21853 |
| 57 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +1970 | 7767 |
| 58 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1912 | 22165 |
| 59 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1910 | 9108 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1908 | 6697 |
| 61 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1906 | 10906 |
| 62 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1906 | 8753 |
| 63 | [github/spec-kit](https://github.com/github/spec-kit) | +1857 | 71722 |
| 64 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1831 | 28745 |
| 65 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1809 | 16088 |
| 66 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1776 | 96919 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1762 | 32354 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1742 | 18228 |
| 69 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1729 | 10579 |
| 70 | [cloudflare/vinext](https://github.com/cloudflare/vinext) | +1682 | 6959 |
| 71 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +1676 | 22306 |
| 72 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1647 | 8467 |
| 73 | [nullclaw/nullclaw](https://github.com/nullclaw/nullclaw) | +1625 | 6576 |
| 74 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1611 | 7353 |
| 75 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1602 | 6401 |
| 76 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab) | +1578 | 7979 |
| 77 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +1552 | 13179 |
| 78 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1549 | 15539 |
| 79 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1545 | 98536 |
| 80 | [tobi/qmd](https://github.com/tobi/qmd) | +1541 | 16158 |
| 81 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1525 | 149018 |
| 82 | [Nagi-ovo/gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager) | +1499 | 12846 |
| 83 | [openai/skills](https://github.com/openai/skills) | +1497 | 14651 |
| 84 | [tw93/Mole](https://github.com/tw93/Mole) | +1459 | 36870 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1430 | 14806 |
| 86 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +1420 | 14033 |
| 87 | [superset-sh/superset](https://github.com/superset-sh/superset) | +1419 | 7455 |
| 88 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1385 | 9062 |
| 89 | [maderix/ANE](https://github.com/maderix/ANE) | +1367 | 6242 |
| 90 | [smartcmd/MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles) | +1353 | 5695 |
| 91 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1344 | 17642 |
| 92 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1316 | 35857 |
| 93 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1276 | 43973 |
| 94 | [openai/codex](https://github.com/openai/codex) | +1266 | 61744 |
| 95 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1236 | 12774 |
| 96 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1213 | 5345 |
| 97 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +1206 | 37564 |
| 98 | [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | +1187 | 7379 |
| 99 | [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | +1184 | 5513 |
| 100 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1150 | 15538 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +1144 | 16346 |
| 102 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1137 | 29175 |
| 103 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1127 | 7097 |
| 104 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1091 | 87598 |
| 105 | [jundot/omlx](https://github.com/jundot/omlx) | +999 | 5964 |
| 106 | [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | +990 | 13057 |
| 107 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +975 | 7033 |
| 108 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +974 | 6728 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +952 | 6381 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +930 | 26071 |
| 111 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +923 | 35735 |
| 112 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +811 | 13648 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +801 | 5960 |
| 114 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +791 | 61818 |
| 115 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +788 | 45886 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +771 | 36799 |
| 117 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +768 | 22828 |
| 118 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +755 | 8409 |
| 119 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +753 | 47122 |
| 120 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +746 | 5098 |
| 121 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +738 | 9860 |
| 122 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +713 | 52700 |
| 123 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +711 | 3162 |
| 124 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +692 | 28292 |
| 125 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +684 | 4336 |
| 126 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +665 | 5388 |
| 127 | [wshobson/agents](https://github.com/wshobson/agents) | +664 | 31727 |
| 128 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +655 | 23399 |
| 129 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +645 | 47936 |
| 130 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +644 | 15690 |
| 131 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +641 | 6090 |
| 132 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +631 | 5968 |
| 133 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +626 | 30590 |
| 134 | [docling-project/docling](https://github.com/docling-project/docling) | +623 | 54041 |
| 135 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +620 | 3379 |
| 136 | [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills) | +612 | 2129 |
| 137 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +602 | 23224 |
| 138 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +601 | 3481 |
| 139 | [ylytdeng/wechat-decrypt](https://github.com/ylytdeng/wechat-decrypt) | +590 | 2091 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +586 | 16553 |
| 141 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +582 | 15967 |
| 142 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +581 | 5079 |
| 143 | [peteromallet/desloppify](https://github.com/peteromallet/desloppify) | +564 | 2532 |
| 144 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +557 | 9998 |
| 145 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +548 | 33712 |
| 146 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +537 | 44545 |
| 147 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +534 | 44232 |
| 148 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +514 | 8016 |
| 149 | [peteromallet/dataclaw](https://github.com/peteromallet/dataclaw) | +514 | 1968 |
| 150 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +510 | 3365 |
| 151 | [aden-hive/hive](https://github.com/aden-hive/hive) | +497 | 9633 |
| 152 | [eooce/python-ws](https://github.com/eooce/python-ws) | +488 | 1863 |
| 153 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +483 | 18324 |
| 154 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +479 | 1931 |
| 155 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +478 | 39841 |
| 156 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +473 | 2269 |
| 157 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +473 | 26897 |
| 158 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +472 | 2598 |
| 159 | [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | +469 | 9737 |
| 160 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +462 | 2782 |
| 161 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +462 | 14516 |
| 162 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +449 | 14358 |
| 163 | [openclaw/skills](https://github.com/openclaw/skills) | +448 | 3126 |
| 164 | [open-webui/open-terminal](https://github.com/open-webui/open-terminal) | +444 | 1972 |
| 165 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +433 | 3874 |
| 166 | [google/langextract](https://github.com/google/langextract) | +429 | 33636 |
| 167 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +417 | 1644 |
| 168 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +404 | 5947 |
| 169 | [World-Open-Graph/br-acc](https://github.com/World-Open-Graph/br-acc) | +400 | 1577 |
| 170 | [searxng/searxng](https://github.com/searxng/searxng) | +400 | 26806 |
| 171 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +400 | 10505 |
| 172 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +398 | 9835 |
| 173 | [apify/agent-skills](https://github.com/apify/agent-skills) | +397 | 1687 |
| 174 | [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | +383 | 5272 |
| 175 | [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | +382 | 7485 |
| 176 | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) | +377 | 2350 |
| 177 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +371 | 24758 |
| 178 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +370 | 1780 |
| 179 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +370 | 3241 |
| 180 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +365 | 4395 |
| 181 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +364 | 18841 |
| 182 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +360 | 2024 |
| 183 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +355 | 3562 |
| 184 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +353 | 6177 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +344 | 24572 |
| 186 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +338 | 0 |
| 187 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +333 | 1591 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +329 | 1420 |
| 189 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +321 | 10398 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +311 | 4074 |
| 191 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +307 | 1328 |
| 192 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +307 | 13463 |
| 193 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +298 | 1320 |
| 194 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +295 | 2616 |
| 195 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +292 | 1391 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +282 | 3683 |
| 197 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +275 | 29780 |
| 198 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +268 | 2370 |
| 199 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +258 | 36103 |
| 200 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +252 | 21705 |
| 201 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +241 | 958 |
| 202 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +237 | 21386 |
| 203 | [Vvkmnn/claude-emporium](https://github.com/Vvkmnn/claude-emporium) | +225 | 145 |
| 204 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +221 | 1024 |
| 205 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +221 | 771 |
| 206 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +210 | 910 |
| 207 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +195 | 1299 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +195 | 41086 |
| 209 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +195 | 7147 |
| 210 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +194 | 8922 |
| 211 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +192 | 1385 |
| 212 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +191 | 1577 |
| 213 | [robinebers/openusage](https://github.com/robinebers/openusage) | +190 | 1554 |
| 214 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +190 | 659 |
| 215 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +188 | 5228 |
| 216 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +186 | 28967 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +183 | 40265 |
| 218 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +178 | 8859 |
| 219 | [dimartarmizi/map-to-poster](https://github.com/dimartarmizi/map-to-poster) | +177 | 701 |
| 220 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +176 | 25359 |
| 221 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +174 | 2626 |
| 222 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +170 | 941 |
| 223 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +157 | 730 |
| 224 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +156 | 2454 |
| 225 | [decolua/9router](https://github.com/decolua/9router) | +154 | 1090 |
| 226 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +153 | 904 |
| 227 | [jgraph/drawio](https://github.com/jgraph/drawio) | +153 | 4250 |
| 228 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +148 | 1419 |
| 229 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +144 | 1146 |
| 230 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +144 | 22807 |
| 231 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +143 | 5196 |
| 232 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +142 | 666 |
| 233 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +142 | 33000 |
| 234 | [yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | +141 | 580 |
| 235 | [es617/claude-replay](https://github.com/es617/claude-replay) | +140 | 548 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +140 | 2092 |
| 237 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +139 | 1678 |
| 238 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +139 | 2026 |
| 239 | [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | +135 | 897 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +133 | 25991 |
| 241 | [marswei/seaseed-clawerse](https://github.com/marswei/seaseed-clawerse) | +127 | 660 |
| 242 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +126 | 35473 |
| 243 | [is-a-dev/register](https://github.com/is-a-dev/register) | +123 | 9999 |
| 244 | [qist/tvbox](https://github.com/qist/tvbox) | +123 | 8546 |
| 245 | [4ier/neo](https://github.com/4ier/neo) | +122 | 618 |
| 246 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +121 | 486 |
| 247 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +117 | 12154 |
| 248 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +115 | 48784 |
| 249 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +112 | 582 |
| 250 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +112 | 407 |
| 251 | [fmhy/edit](https://github.com/fmhy/edit) | +111 | 8591 |
| 252 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +110 | 502 |
| 253 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +110 | 1315 |
| 254 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +109 | 3519 |
| 255 | [JingMatrix/LSPosed](https://github.com/JingMatrix/LSPosed) | +108 | 10098 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +108 | 12622 |
| 257 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +105 | 1032 |
| 258 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +105 | 3274 |
| 259 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +104 | 426 |
| 260 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +104 | 460 |
| 261 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +104 | 1044 |
| 262 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +103 | 552 |
| 263 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +103 | 11199 |
| 264 | [expo/skills](https://github.com/expo/skills) | +102 | 1507 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +102 | 8824 |
| 266 | [skylot/jadx](https://github.com/skylot/jadx) | +102 | 47365 |
| 267 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +100 | 3202 |
| 268 | [lklynet/aurral](https://github.com/lklynet/aurral) | +99 | 875 |
| 269 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +99 | 868 |
| 270 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +96 | 949 |
| 271 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +96 | 887 |
| 272 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +96 | 37313 |
| 273 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +95 | 621 |
| 274 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | +94 | 801 |
| 275 | [unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada](https://github.com/unipds-engenharia-de-ia-aplicada/engenharia-de-software-com-ia-aplicada) | +92 | 383 |
| 276 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +91 | 7045 |
| 277 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +90 | 520 |
| 278 | [sunnoy/openclaw-plugin-wecom](https://github.com/sunnoy/openclaw-plugin-wecom) | +86 | 593 |
| 279 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 3059 |
| 280 | [dingxiang-me/OpenClaw-Wechat](https://github.com/dingxiang-me/OpenClaw-Wechat) | +84 | 494 |
| 281 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +83 | 26939 |
| 282 | [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | +81 | 385 |
| 283 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +80 | 857 |
| 284 | [idinging/freemail](https://github.com/idinging/freemail) | +77 | 1064 |
| 285 | [chengtx809/exa-pool](https://github.com/chengtx809/exa-pool) | +76 | 433 |
| 286 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +74 | 8241 |
| 287 | [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) | +73 | 21376 |
| 288 | [katelya77/K-Vault](https://github.com/katelya77/K-Vault) | +72 | 433 |
| 289 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +72 | 262 |
| 290 | [apache/kafka](https://github.com/apache/kafka) | +72 | 32043 |
| 291 | [paohaijiao/jquick-curl](https://github.com/paohaijiao/jquick-curl) | +70 | 995 |
| 292 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +70 | 6103 |
| 293 | [inulute/medium-unlocker](https://github.com/inulute/medium-unlocker) | +69 | 1336 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +66 | 1341 |
| 295 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +65 | 45263 |
| 296 | [openjdk/jdk](https://github.com/openjdk/jdk) | +65 | 22707 |
| 297 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +64 | 912 |
| 298 | [freeok/so-novel](https://github.com/freeok/so-novel) | +64 | 6376 |
| 299 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +64 | 7642 |
| 300 | [LawnchairLauncher/lawnchair](https://github.com/LawnchairLauncher/lawnchair) | +63 | 12392 |
