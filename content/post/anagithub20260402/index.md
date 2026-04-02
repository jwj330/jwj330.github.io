---
title: "2026-04-02 GitHub增长趋势报告"
description: "1.claude-code+1161 2.codex-plugin-cc+431 3.oh-my-codex+410 4.openscreen+382 5.claude-howto+270"
date: 2026-04-02T20:38:11+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-02 20:38:11

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
        'daily': {"categories": ["roboflow/supervision", "TheTom/turboquant_plus", "webadderall/Recordly", "666ghj/MiroFish", "multica-ai/multica", "shareAI-lab/learn-claude-code", "farion1231/cc-switch", "shanraisshan/claude-code-best-practice", "NousResearch/hermes-agent", "code-yeongyu/oh-my-openagent", "microsoft/VibeVoice", "jackwener/opencli", "paperclipai/paperclip", "google-research/timesfm", "Yeachan-Heo/oh-my-claudecode", "luongnv89/claude-howto", "siddharthvaddem/openscreen", "Yeachan-Heo/oh-my-codex", "openai/codex-plugin-cc", "anthropics/claude-code"], "data": [73, 80, 84, 86, 119, 120, 126, 127, 135, 140, 144, 146, 167, 170, 212, 270, 382, 410, 431, 1161]},
        'weekly': {"categories": ["msitarzewski/agency-agents", "siddharthvaddem/openscreen", "nextlevelbuilder/ui-ux-pro-max-skill", "Yeachan-Heo/oh-my-codex", "hacksider/Deep-Live-Cam", "shareAI-lab/learn-claude-code", "karpathy/autoresearch", "shanraisshan/claude-code-best-practice", "JCodesMore/ai-website-cloner-template", "NousResearch/hermes-agent", "Yeachan-Heo/oh-my-claudecode", "mvanhorn/last30days-skill", "bytedance/deer-flow", "openai/codex-plugin-cc", "paperclipai/paperclip", "microsoft/VibeVoice", "luongnv89/claude-howto", "obra/superpowers", "anthropics/claude-code", "affaan-m/everything-claude-code"], "data": [688, 704, 748, 875, 908, 946, 947, 973, 1002, 1035, 1114, 1127, 1197, 1294, 1430, 1432, 1879, 2196, 2528, 2746]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "moeru-ai/airi", "VoltAgent/awesome-openclaw-skills", "anomalyco/opencode", "gsd-build/get-shit-done", "shanraisshan/claude-code-best-practice", "anthropics/claude-code", "shareAI-lab/learn-claude-code", "googleworkspace/cli", "koala73/worldmonitor", "anthropics/skills", "bytedance/deer-flow", "ruvnet/RuView", "666ghj/MiroFish", "paperclipai/paperclip", "obra/superpowers", "karpathy/autoresearch", "msitarzewski/agency-agents", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [3422, 3564, 3807, 3989, 4111, 4214, 4632, 4750, 4992, 5001, 5043, 5224, 5308, 8041, 8445, 10800, 12328, 12636, 12919, 21751]}
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
| 1 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1161 | 69674 |
| 2 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +431 | 10539 |
| 3 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +410 | 11266 |
| 4 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +382 | 15440 |
| 5 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +270 | 16926 |
| 6 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +212 | 22050 |
| 7 | [google-research/timesfm](https://github.com/google-research/timesfm) | +170 | 13291 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +167 | 44941 |
| 9 | [jackwener/opencli](https://github.com/jackwener/opencli) | +146 | 11433 |
| 10 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +144 | 35149 |
| 11 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +140 | 33878 |
| 12 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +135 | 22610 |
| 13 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +127 | 30975 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +126 | 37813 |
| 15 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +120 | 47181 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +119 | 1615 |
| 17 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +86 | 48238 |
| 18 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +84 | 4874 |
| 19 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +80 | 5191 |
| 20 | [roboflow/supervision](https://github.com/roboflow/supervision) | +73 | 36553 |
| 21 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +67 | 30642 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +65 | 47022 |
| 23 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +61 | 2561 |
| 24 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +59 | 30590 |
| 25 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +54 | 37330 |
| 26 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +52 | 17642 |
| 27 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +51 | 32872 |
| 28 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +51 | 16326 |
| 29 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +50 | 2790 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +48 | 16756 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2746 | 51199 |
| 2 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2528 | 69674 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2196 | 60312 |
| 4 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1879 | 16926 |
| 5 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1432 | 35149 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1430 | 44941 |
| 7 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1294 | 10539 |
| 8 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1197 | 56643 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1127 | 17642 |
| 10 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1114 | 22050 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1035 | 22611 |
| 12 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1002 | 7095 |
| 13 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +973 | 30975 |
| 14 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +947 | 64239 |
| 15 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +946 | 47181 |
| 16 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +908 | 79656 |
| 17 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +875 | 11267 |
| 18 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +748 | 34148 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +704 | 15440 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +688 | 68911 |
| 21 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +614 | 48239 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +567 | 47022 |
| 23 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +552 | 5191 |
| 24 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +549 | 12274 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +528 | 14579 |
| 26 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +503 | 37813 |
| 27 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +503 | 30678 |
| 28 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +503 | 21232 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +490 | 30590 |
| 30 | [jackwener/opencli](https://github.com/jackwener/opencli) | +465 | 11433 |
| 31 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +392 | 35828 |
| 32 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +387 | 33878 |
| 33 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +382 | 29387 |
| 34 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +363 | 3074 |
| 35 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +345 | 16326 |
| 36 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +336 | 45282 |
| 37 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +334 | 8795 |
| 38 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +331 | 2860 |
| 39 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +324 | 3547 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +324 | 16756 |
| 41 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +316 | 8177 |
| 42 | [google-research/timesfm](https://github.com/google-research/timesfm) | +312 | 13291 |
| 43 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +312 | 4411 |
| 44 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +312 | 22836 |
| 45 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +299 | 21634 |
| 46 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +296 | 37330 |
| 47 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +293 | 40043 |
| 48 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +291 | 30061 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +281 | 30642 |
| 50 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +280 | 8822 |
| 51 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +280 | 28072 |
| 52 | [pascalorg/editor](https://github.com/pascalorg/editor) | +279 | 9240 |
| 53 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +273 | 7945 |
| 54 | [virattt/dexter](https://github.com/virattt/dexter) | +269 | 20810 |
| 55 | [tanweai/pua](https://github.com/tanweai/pua) | +258 | 14700 |
| 56 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +255 | 36674 |
| 57 | [millionco/expect](https://github.com/millionco/expect) | +252 | 3004 |
| 58 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +249 | 46054 |
| 59 | [revfactory/harness](https://github.com/revfactory/harness) | +235 | 1595 |
| 60 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +232 | 10991 |
| 61 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +229 | 26721 |
| 62 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +223 | 27748 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +223 | 33210 |
| 64 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +222 | 20831 |
| 65 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +219 | 43832 |
| 66 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +218 | 8913 |
| 67 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +218 | 2800 |
| 68 | [alvinunreal/awesome-opensource-ai](https://github.com/alvinunreal/awesome-opensource-ai) | +218 | 2253 |
| 69 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +216 | 22351 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +216 | 18435 |
| 71 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +213 | 15505 |
| 72 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +200 | 2561 |
| 73 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +198 | 18958 |
| 74 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +193 | 21289 |
| 75 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +192 | 13584 |
| 76 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +190 | 4874 |
| 77 | [eze-is/web-access](https://github.com/eze-is/web-access) | +187 | 3578 |
| 78 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +185 | 4176 |
| 79 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +181 | 1289 |
| 80 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +175 | 34431 |
| 81 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +173 | 39841 |
| 82 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +173 | 26295 |
| 83 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +164 | 12581 |
| 84 | [ilyamiro/nixos-configuration](https://github.com/ilyamiro/nixos-configuration) | +162 | 2111 |
| 85 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +162 | 7615 |
| 86 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +160 | 13003 |
| 87 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +160 | 18210 |
| 88 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +159 | 8085 |
| 89 | [chrisryugj/korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp) | +159 | 985 |
| 90 | [facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) | +159 | 1311 |
| 91 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +157 | 1383 |
| 92 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +156 | 20583 |
| 93 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +154 | 28743 |
| 94 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +153 | 37661 |
| 95 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +148 | 8296 |
| 96 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +147 | 9906 |
| 97 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +145 | 10049 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +144 | 8801 |
| 99 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +141 | 18808 |
| 100 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +139 | 22973 |
| 101 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +139 | 1547 |
| 102 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +135 | 9323 |
| 103 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +133 | 15791 |
| 104 | [jundot/omlx](https://github.com/jundot/omlx) | +133 | 8110 |
| 105 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +133 | 36799 |
| 106 | [punitarani/fli](https://github.com/punitarani/fli) | +132 | 972 |
| 107 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +131 | 5218 |
| 108 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +130 | 5300 |
| 109 | [multica-ai/multica](https://github.com/multica-ai/multica) | +129 | 1615 |
| 110 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +129 | 2719 |
| 111 | [usestrix/strix](https://github.com/usestrix/strix) | +127 | 23016 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +126 | 28184 |
| 113 | [lucas-maes/le-wm](https://github.com/lucas-maes/le-wm) | +120 | 1844 |
| 114 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +118 | 32872 |
| 115 | [jxnxts/mcp-brasil](https://github.com/jxnxts/mcp-brasil) | +118 | 1173 |
| 116 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +118 | 31558 |
| 117 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +117 | 3449 |
| 118 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +114 | 31182 |
| 119 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +113 | 17160 |
| 120 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +104 | 14267 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +21751 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12919 | 51199 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12636 | 68911 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12328 | 64239 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10800 | 60312 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8445 | 44941 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8041 | 48239 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +5308 | 45282 |
| 9 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5224 | 56643 |
| 10 | [anthropics/skills](https://github.com/anthropics/skills) | +5043 | 74774 |
| 11 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +5001 | 46054 |
| 12 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +4992 | 23588 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4750 | 47181 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +4632 | 69674 |
| 15 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4214 | 30975 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4111 | 47023 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3989 | 109881 |
| 18 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +3807 | 43832 |
| 19 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3564 | 36943 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3422 | 34148 |
| 21 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3302 | 21232 |
| 22 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3155 | 22611 |
| 23 | [openai/symphony](https://github.com/openai/symphony) | +3095 | 14460 |
| 24 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3051 | 20583 |
| 25 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2902 | 14986 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2850 | 34431 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2772 | 15505 |
| 28 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2768 | 28452 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2739 | 37813 |
| 30 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2713 | 85286 |
| 31 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2672 | 18210 |
| 32 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2643 | 26721 |
| 33 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2589 | 21289 |
| 34 | [tanweai/pua](https://github.com/tanweai/pua) | +2537 | 14700 |
| 35 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2449 | 28073 |
| 36 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2434 | 30590 |
| 37 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2393 | 27748 |
| 38 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2345 | 20831 |
| 39 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2333 | 16756 |
| 40 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2238 | 13584 |
| 41 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2222 | 30061 |
| 42 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2177 | 9323 |
| 43 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +2170 | 14267 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2155 | 30642 |
| 45 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2105 | 37661 |
| 46 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2088 | 7974 |
| 47 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2070 | 12480 |
| 48 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2032 | 14579 |
| 49 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2030 | 30678 |
| 50 | [github/spec-kit](https://github.com/github/spec-kit) | +2019 | 71722 |
| 51 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2003 | 16326 |
| 52 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2002 | 28743 |
| 53 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +2001 | 37330 |
| 54 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1975 | 33878 |
| 55 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1956 | 29387 |
| 56 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1944 | 22050 |
| 57 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1897 | 16926 |
| 58 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1896 | 35167 |
| 59 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1881 | 60117 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1842 | 22351 |
| 61 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1833 | 17642 |
| 62 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1833 | 8763 |
| 63 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1821 | 26294 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1785 | 36674 |
| 65 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1758 | 26295 |
| 66 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1734 | 16132 |
| 67 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1707 | 11433 |
| 68 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1704 | 9354 |
| 69 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1687 | 11316 |
| 70 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1652 | 35828 |
| 71 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1642 | 29248 |
| 72 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1600 | 18808 |
| 73 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1596 | 18130 |
| 74 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1583 | 10991 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1534 | 19142 |
| 76 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1529 | 11399 |
| 77 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1528 | 35149 |
| 78 | [openai/codex](https://github.com/openai/codex) | +1527 | 61744 |
| 79 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1509 | 33210 |
| 80 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1495 | 10049 |
| 81 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1484 | 37025 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1446 | 18435 |
| 83 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1415 | 122870 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1398 | 15791 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1389 | 98536 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +1359 | 36870 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1323 | 9906 |
| 88 | [jundot/omlx](https://github.com/jundot/omlx) | +1312 | 8110 |
| 89 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1307 | 43973 |
| 90 | [openai/skills](https://github.com/openai/skills) | +1303 | 16032 |
| 91 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1298 | 10539 |
| 92 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1293 | 7615 |
| 93 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1279 | 12274 |
| 94 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1272 | 9240 |
| 95 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1261 | 8795 |
| 96 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1252 | 8296 |
| 97 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1247 | 17160 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1245 | 8801 |
| 99 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +1210 | 9697 |
| 100 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1203 | 78902 |
| 101 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1183 | 11267 |
| 102 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1150 | 7945 |
| 103 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1125 | 96919 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1105 | 8913 |
| 105 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1050 | 79656 |
| 106 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1006 | 7095 |
| 107 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +961 | 22836 |
| 108 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +959 | 52700 |
| 109 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +955 | 15441 |
| 110 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +896 | 35735 |
| 111 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +893 | 5300 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +842 | 28184 |
| 113 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +830 | 39841 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +816 | 7017 |
| 115 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +803 | 45886 |
| 116 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +784 | 37564 |
| 117 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +779 | 7582 |
| 118 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +777 | 4577 |
| 119 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +775 | 22973 |
| 120 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +761 | 17722 |
| 121 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +754 | 3486 |
| 122 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +753 | 36799 |
| 123 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +751 | 29015 |
| 124 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +714 | 23696 |
| 125 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +700 | 4305 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +683 | 3987 |
| 127 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +682 | 4095 |
| 128 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +676 | 4713 |
| 129 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +661 | 3643 |
| 130 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +631 | 47936 |
| 131 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +630 | 15878 |
| 132 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +621 | 8822 |
| 133 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +609 | 3449 |
| 134 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +594 | 9029 |
| 135 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +582 | 14881 |
| 136 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +579 | 3997 |
| 137 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +574 | 5191 |
| 138 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +558 | 2767 |
| 139 | [wshobson/agents](https://github.com/wshobson/agents) | +553 | 32824 |
| 140 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +552 | 7081 |
| 141 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +541 | 47122 |
| 142 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +527 | 28258 |
| 143 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +525 | 4669 |
| 144 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +513 | 17891 |
| 145 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +513 | 44545 |
| 146 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +479 | 44232 |
| 147 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +475 | 24312 |
| 148 | [LeoYeAI/openclaw-master-skills](https://github.com/LeoYeAI/openclaw-master-skills) | +474 | 1895 |
| 149 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +472 | 2389 |
| 150 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +466 | 3547 |
| 151 | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | +461 | 2966 |
| 152 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +458 | 31558 |
| 153 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +456 | 24063 |
| 154 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +455 | 5218 |
| 155 | [huggingface/skills](https://github.com/huggingface/skills) | +452 | 10021 |
| 156 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +451 | 11070 |
| 157 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +434 | 8085 |
| 158 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +428 | 3549 |
| 159 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +426 | 10817 |
| 160 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +424 | 3532 |
| 161 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +417 | 8177 |
| 162 | [htdt/godogen](https://github.com/htdt/godogen) | +414 | 2473 |
| 163 | [hectorvent/floci](https://github.com/hectorvent/floci) | +412 | 2543 |
| 164 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +409 | 7191 |
| 165 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +408 | 23286 |
| 166 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +395 | 2030 |
| 167 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +393 | 2614 |
| 168 | [eze-is/web-access](https://github.com/eze-is/web-access) | +393 | 3578 |
| 169 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +388 | 3616 |
| 170 | [openclaw/skills](https://github.com/openclaw/skills) | +387 | 3725 |
| 171 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +383 | 2445 |
| 172 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +368 | 21634 |
| 173 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +361 | 13436 |
| 174 | [google-research/timesfm](https://github.com/google-research/timesfm) | +358 | 13291 |
| 175 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +355 | 2072 |
| 176 | [aden-hive/hive](https://github.com/aden-hive/hive) | +354 | 9997 |
| 177 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +341 | 6510 |
| 178 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +335 | 1816 |
| 179 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +324 | 3717 |
| 180 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +323 | 33712 |
| 181 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +319 | 1424 |
| 182 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +317 | 10561 |
| 183 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +314 | 1574 |
| 184 | [apify/agent-skills](https://github.com/apify/agent-skills) | +308 | 1813 |
| 185 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +307 | 2016 |
| 186 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +303 | 2561 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +297 | 10759 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +287 | 1898 |
| 189 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +285 | 25141 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +278 | 4960 |
| 191 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +276 | 2800 |
| 192 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +275 | 1643 |
| 193 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +270 | 1427 |
| 194 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +270 | 29780 |
| 195 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +268 | 2181 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +244 | 4366 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +243 | 14978 |
| 198 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +242 | 13768 |
| 199 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +238 | 22278 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +225 | 7311 |
| 201 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +222 | 5988 |
| 202 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +216 | 1169 |
| 203 | [usebruno/bruno](https://github.com/usebruno/bruno) | +211 | 41086 |
| 204 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +210 | 1230 |
| 205 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +209 | 36103 |
| 206 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +199 | 871 |
| 207 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +195 | 892 |
| 208 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +188 | 1289 |
| 209 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +188 | 21784 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +183 | 1646 |
| 211 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +181 | 8990 |
| 212 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +177 | 1096 |
| 213 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +174 | 2596 |
| 214 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +173 | 1994 |
| 215 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2491 |
| 216 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +152 | 2697 |
| 217 | [zhaoolee/ChromeAppHeroes](https://github.com/zhaoolee/ChromeAppHeroes) | +149 | 25421 |
| 218 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +148 | 832 |
| 219 | [linlay/zenmind](https://github.com/linlay/zenmind) | +147 | 195 |
| 220 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 588 |
| 221 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +145 | 40265 |
| 222 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +145 | 2391 |
| 223 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +142 | 1816 |
| 224 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +140 | 775 |
| 225 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +137 | 954 |
| 226 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +137 | 1078 |
| 227 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +135 | 5441 |
| 228 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +135 | 29256 |
| 229 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 529 |
| 230 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +131 | 1739 |
| 231 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +130 | 1323 |
| 232 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +127 | 0 |
| 233 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +126 | 13840 |
| 234 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +124 | 35473 |
| 235 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +122 | 514 |
| 236 | [4ier/neo](https://github.com/4ier/neo) | +121 | 654 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +120 | 12473 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +119 | 26370 |
| 239 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +117 | 757 |
| 240 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +116 | 644 |
| 241 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +115 | 23075 |
| 242 | [is-a-dev/register](https://github.com/is-a-dev/register) | +113 | 10048 |
| 243 | [dashersw/gea](https://github.com/dashersw/gea) | +112 | 839 |
| 244 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +112 | 10487 |
| 245 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +111 | 2556 |
| 246 | [robinebers/openusage](https://github.com/robinebers/openusage) | +109 | 1672 |
| 247 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 460 |
| 248 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +107 | 2097 |
| 249 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +107 | 33000 |
| 250 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +106 | 1417 |
| 251 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +102 | 1840 |
| 252 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +102 | 1551 |
| 253 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 519 |
| 254 | [skylot/jadx](https://github.com/skylot/jadx) | +102 | 47365 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +101 | 595 |
| 256 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 447 |
| 257 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +97 | 638 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +97 | 48784 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +97 | 12780 |
| 260 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +96 | 785 |
| 261 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +96 | 457 |
| 262 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +96 | 540 |
| 263 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +94 | 644 |
| 264 | [idinging/freemail](https://github.com/idinging/freemail) | +93 | 1267 |
| 265 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +91 | 1423 |
| 266 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +91 | 9067 |
| 267 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +89 | 684 |
| 268 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +88 | 401 |
| 269 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +86 | 603 |
| 270 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +85 | 3757 |
| 271 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +83 | 11433 |
| 272 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +82 | 3373 |
| 273 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +81 | 884 |
| 274 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +80 | 1021 |
| 275 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +80 | 440 |
| 276 | [khanhduytran0/coruna](https://github.com/khanhduytran0/coruna) | +79 | 429 |
| 277 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +78 | 687 |
| 278 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +77 | 615 |
| 279 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +76 | 1164 |
| 280 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +74 | 3480 |
| 281 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +74 | 1065 |
| 282 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +74 | 27109 |
| 283 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +73 | 3147 |
| 284 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +71 | 8393 |
| 285 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +68 | 436 |
| 286 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +68 | 45263 |
| 287 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +67 | 423 |
| 288 | [crimera/piko](https://github.com/crimera/piko) | +67 | 3003 |
| 289 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +67 | 37313 |
| 290 | [apache/kafka](https://github.com/apache/kafka) | +66 | 32043 |
| 291 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +63 | 347 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +63 | 31476 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +61 | 1585 |
| 294 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1634 |
| 295 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +61 | 26646 |
| 296 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +59 | 639 |
| 297 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +59 | 1443 |
| 298 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +58 | 629 |
| 299 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +58 | 376 |
| 300 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +58 | 4605 |
