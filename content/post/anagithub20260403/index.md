---
title: "2026-04-03 GitHub增长趋势报告"
description: "1.oh-my-codex+612 2.openscreen+575 3.onyx+333 4.codex-plugin-cc+268 5.system_prompts_leaks+251"
date: 2026-04-03T20:39:02+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-03 20:39:02

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
        'daily': {"categories": ["dmtrKovalenko/fff.nvim", "drona23/claude-token-efficient", "shanraisshan/claude-code-best-practice", "k2-fsa/OmniVoice", "shareAI-lab/learn-claude-code", "666ghj/MiroFish", "farion1231/cc-switch", "microsoft/VibeVoice", "code-yeongyu/oh-my-openagent", "luongnv89/claude-howto", "google-research/timesfm", "jackwener/opencli", "Yeachan-Heo/oh-my-claudecode", "NousResearch/hermes-agent", "paperclipai/paperclip", "asgeirtj/system_prompts_leaks", "openai/codex-plugin-cc", "onyx-dot-app/onyx", "siddharthvaddem/openscreen", "Yeachan-Heo/oh-my-codex"], "data": [101, 101, 111, 113, 128, 132, 137, 141, 149, 174, 205, 207, 220, 237, 251, 251, 268, 333, 575, 612]},
        'weekly': {"categories": ["msitarzewski/agency-agents", "nextlevelbuilder/ui-ux-pro-max-skill", "ChinaSiro/claude-code-sourcemap", "mvanhorn/last30days-skill", "shareAI-lab/learn-claude-code", "JCodesMore/ai-website-cloner-template", "karpathy/autoresearch", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "NousResearch/hermes-agent", "Yeachan-Heo/oh-my-claudecode", "siddharthvaddem/openscreen", "Yeachan-Heo/oh-my-codex", "openai/codex-plugin-cc", "paperclipai/paperclip", "microsoft/VibeVoice", "luongnv89/claude-howto", "obra/superpowers", "affaan-m/everything-claude-code", "anthropics/claude-code"], "data": [741, 763, 796, 944, 948, 949, 971, 1042, 1092, 1198, 1208, 1260, 1454, 1539, 1541, 1543, 1940, 2265, 3005, 3041]},
        'monthly': {"categories": ["moeru-ai/airi", "nextlevelbuilder/ui-ux-pro-max-skill", "VoltAgent/awesome-openclaw-skills", "anomalyco/opencode", "gsd-build/get-shit-done", "koala73/worldmonitor", "shanraisshan/claude-code-best-practice", "ruvnet/RuView", "shareAI-lab/learn-claude-code", "anthropics/skills", "googleworkspace/cli", "anthropics/claude-code", "bytedance/deer-flow", "666ghj/MiroFish", "paperclipai/paperclip", "obra/superpowers", "karpathy/autoresearch", "msitarzewski/agency-agents", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [3382, 3478, 3582, 3986, 4103, 4187, 4243, 4295, 4752, 4939, 5010, 5064, 5246, 8160, 8685, 10926, 12479, 12726, 13078, 20547]}
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
| 1 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +612 | 13898 |
| 2 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +575 | 17973 |
| 3 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +333 | 23111 |
| 4 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +268 | 11244 |
| 5 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +251 | 32872 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +251 | 46059 |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +237 | 23687 |
| 8 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +220 | 23051 |
| 9 | [jackwener/opencli](https://github.com/jackwener/opencli) | +207 | 12507 |
| 10 | [google-research/timesfm](https://github.com/google-research/timesfm) | +205 | 14015 |
| 11 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +174 | 17637 |
| 12 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +149 | 33878 |
| 13 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +141 | 35636 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +137 | 38458 |
| 15 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +132 | 48867 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +128 | 47841 |
| 17 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +113 | 894 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +111 | 31431 |
| 19 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +101 | 2952 |
| 20 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +101 | 3188 |
| 21 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +100 | 23257 |
| 22 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +96 | 1009 |
| 23 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +92 | 18004 |
| 24 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +92 | 30590 |
| 25 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +91 | 8260 |
| 26 | [lemonade-sdk/lemonade](https://github.com/lemonade-sdk/lemonade) | +90 | 3208 |
| 27 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +89 | 1199 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +89 | 47443 |
| 29 | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | +84 | 1073 |
| 30 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +82 | 2308 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3041 | 69674 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3005 | 51199 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2265 | 60312 |
| 4 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1940 | 17637 |
| 5 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1543 | 35636 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1541 | 46059 |
| 7 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1539 | 11244 |
| 8 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1454 | 13899 |
| 9 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1260 | 17973 |
| 10 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1208 | 23051 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1198 | 23687 |
| 12 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1092 | 57257 |
| 13 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1042 | 31431 |
| 14 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +971 | 64980 |
| 15 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +949 | 7252 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +948 | 47841 |
| 17 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +944 | 18004 |
| 18 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +796 | 8260 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +763 | 34148 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +741 | 69771 |
| 21 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +665 | 48867 |
| 22 | [jackwener/opencli](https://github.com/jackwener/opencli) | +604 | 12507 |
| 23 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +603 | 5447 |
| 24 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +597 | 23111 |
| 25 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +587 | 47443 |
| 26 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +573 | 14916 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +564 | 38458 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +530 | 30590 |
| 29 | [google-research/timesfm](https://github.com/google-research/timesfm) | +506 | 14015 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +499 | 30678 |
| 31 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +497 | 33878 |
| 32 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +472 | 21399 |
| 33 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +396 | 36187 |
| 34 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +388 | 3460 |
| 35 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +371 | 3152 |
| 36 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +365 | 16612 |
| 37 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +360 | 32872 |
| 38 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +356 | 29577 |
| 39 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +355 | 3855 |
| 40 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +351 | 2952 |
| 41 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +341 | 17074 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +340 | 37330 |
| 43 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +325 | 4483 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +320 | 31068 |
| 45 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +320 | 30346 |
| 46 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +308 | 9061 |
| 47 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +303 | 8989 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +285 | 36996 |
| 49 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +284 | 45507 |
| 50 | [pascalorg/editor](https://github.com/pascalorg/editor) | +283 | 9315 |
| 51 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +274 | 2634 |
| 52 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +267 | 1677 |
| 53 | [revfactory/harness](https://github.com/revfactory/harness) | +266 | 1715 |
| 54 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +260 | 22720 |
| 55 | [tanweai/pua](https://github.com/tanweai/pua) | +259 | 14962 |
| 56 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +256 | 12377 |
| 57 | [ponponon/claude_code_src](https://github.com/ponponon/claude_code_src) | +254 | 1909 |
| 58 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +248 | 22925 |
| 59 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +248 | 8231 |
| 60 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +247 | 44077 |
| 61 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +246 | 33471 |
| 62 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +245 | 28170 |
| 63 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +243 | 5071 |
| 64 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +243 | 26928 |
| 65 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +241 | 20964 |
| 66 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +240 | 9179 |
| 67 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +238 | 46196 |
| 68 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +229 | 19236 |
| 69 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +229 | 15728 |
| 70 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +228 | 11048 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +226 | 18636 |
| 72 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +225 | 4362 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +223 | 27893 |
| 74 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +217 | 23257 |
| 75 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +208 | 2656 |
| 76 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +205 | 13693 |
| 77 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +201 | 24704 |
| 78 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +195 | 1498 |
| 79 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +194 | 2938 |
| 80 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +189 | 12699 |
| 81 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +188 | 1855 |
| 82 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +185 | 8062 |
| 83 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +184 | 20790 |
| 84 | [eze-is/web-access](https://github.com/eze-is/web-access) | +182 | 3716 |
| 85 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +180 | 1818 |
| 86 | [ilyamiro/nixos-configuration](https://github.com/ilyamiro/nixos-configuration) | +180 | 2242 |
| 87 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +178 | 34546 |
| 88 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +177 | 1412 |
| 89 | [multica-ai/multica](https://github.com/multica-ai/multica) | +175 | 1857 |
| 90 | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | +173 | 1073 |
| 91 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +171 | 8175 |
| 92 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +170 | 39841 |
| 93 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +169 | 5348 |
| 94 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +166 | 1009 |
| 95 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +166 | 10119 |
| 96 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +165 | 37816 |
| 97 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +163 | 3188 |
| 98 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +162 | 1199 |
| 99 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +161 | 19004 |
| 100 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +160 | 28856 |
| 101 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +156 | 8932 |
| 102 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +150 | 10173 |
| 103 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +149 | 5413 |
| 104 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +147 | 15895 |
| 105 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +147 | 31848 |
| 106 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +146 | 28365 |
| 107 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | +144 | 2920 |
| 108 | [usestrix/strix](https://github.com/usestrix/strix) | +141 | 23121 |
| 109 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +139 | 12256 |
| 110 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +135 | 36799 |
| 111 | [punitarani/fli](https://github.com/punitarani/fli) | +134 | 1068 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +132 | 8260 |
| 113 | [lorryjovens-hub/claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust) | +131 | 870 |
| 114 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +130 | 14371 |
| 115 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +124 | 17257 |
| 116 | [roboflow/supervision](https://github.com/roboflow/supervision) | +122 | 36553 |
| 117 | [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | +122 | 1570 |
| 118 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +116 | 26382 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +116 | 7103 |
| 120 | [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | +116 | 31182 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +20547 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13078 | 51199 |
| 3 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12726 | 69771 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12479 | 64980 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10926 | 60312 |
| 6 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8685 | 46059 |
| 7 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8160 | 48867 |
| 8 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5246 | 57257 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5064 | 69674 |
| 10 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +5010 | 23705 |
| 11 | [anthropics/skills](https://github.com/anthropics/skills) | +4939 | 74774 |
| 12 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4752 | 47841 |
| 13 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +4295 | 45507 |
| 14 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4243 | 31432 |
| 15 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +4187 | 46196 |
| 16 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4103 | 47443 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3986 | 109881 |
| 18 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +3582 | 44077 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3478 | 34148 |
| 20 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3382 | 37006 |
| 21 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3348 | 23687 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3346 | 21399 |
| 23 | [openai/symphony](https://github.com/openai/symphony) | +3111 | 14530 |
| 24 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3068 | 20790 |
| 25 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2929 | 15090 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2807 | 15728 |
| 27 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2745 | 34546 |
| 28 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2742 | 85286 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2740 | 38458 |
| 30 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2703 | 18346 |
| 31 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2686 | 26928 |
| 32 | [tanweai/pua](https://github.com/tanweai/pua) | +2585 | 14962 |
| 33 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2499 | 30590 |
| 34 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2490 | 28562 |
| 35 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2404 | 28170 |
| 36 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2401 | 21442 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2393 | 17074 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2332 | 27893 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2270 | 13693 |
| 40 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2174 | 9437 |
| 41 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2167 | 30346 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2130 | 31068 |
| 43 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2127 | 23051 |
| 44 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2095 | 8017 |
| 45 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2075 | 12532 |
| 46 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2071 | 16612 |
| 47 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2050 | 17637 |
| 48 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +2048 | 20964 |
| 49 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +2045 | 14916 |
| 50 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2028 | 30678 |
| 51 | [github/spec-kit](https://github.com/github/spec-kit) | +2023 | 71722 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2022 | 33878 |
| 53 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2016 | 37816 |
| 54 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1996 | 37330 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1991 | 28856 |
| 56 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1921 | 18004 |
| 57 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1907 | 12507 |
| 58 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1885 | 60117 |
| 59 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1854 | 8841 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1840 | 22720 |
| 61 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1832 | 35239 |
| 62 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1824 | 29577 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1771 | 36996 |
| 64 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1755 | 13899 |
| 65 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1740 | 26382 |
| 66 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1727 | 14371 |
| 67 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1673 | 9386 |
| 68 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1672 | 11370 |
| 69 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1659 | 35636 |
| 70 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1654 | 36187 |
| 71 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1626 | 26596 |
| 72 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1625 | 19004 |
| 73 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1608 | 18254 |
| 74 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1593 | 11048 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1563 | 61744 |
| 76 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1557 | 19276 |
| 77 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1554 | 29359 |
| 78 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1552 | 11657 |
| 79 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1539 | 11244 |
| 80 | [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | +1539 | 16194 |
| 81 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1521 | 17973 |
| 82 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1517 | 10173 |
| 83 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1498 | 37102 |
| 84 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1475 | 33471 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1427 | 18636 |
| 86 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1399 | 15895 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1394 | 98536 |
| 88 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +1354 | 122870 |
| 89 | [tw93/Mole](https://github.com/tw93/Mole) | +1335 | 36870 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1334 | 10119 |
| 91 | [jundot/omlx](https://github.com/jundot/omlx) | +1330 | 8260 |
| 92 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1323 | 9061 |
| 93 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1316 | 7712 |
| 94 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1306 | 9315 |
| 95 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1306 | 43973 |
| 96 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1304 | 12377 |
| 97 | [openai/skills](https://github.com/openai/skills) | +1295 | 16100 |
| 98 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1267 | 8361 |
| 99 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1237 | 8932 |
| 100 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1225 | 78902 |
| 101 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1159 | 8062 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1129 | 9179 |
| 103 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1101 | 79656 |
| 104 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +1088 | 17257 |
| 105 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1080 | 96919 |
| 106 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1040 | 7252 |
| 107 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1000 | 52700 |
| 108 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +976 | 9731 |
| 109 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +957 | 22925 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +926 | 5413 |
| 111 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +892 | 35735 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +861 | 23257 |
| 113 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +833 | 28365 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +828 | 7103 |
| 115 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +827 | 49621 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +822 | 39841 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +802 | 45886 |
| 118 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +796 | 8260 |
| 119 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +782 | 37564 |
| 120 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +766 | 4610 |
| 121 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +760 | 3507 |
| 122 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +755 | 36799 |
| 123 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +753 | 29044 |
| 124 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +739 | 7612 |
| 125 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +715 | 17800 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +708 | 4355 |
| 127 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +704 | 4179 |
| 128 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +691 | 4014 |
| 129 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +686 | 23111 |
| 130 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +685 | 4752 |
| 131 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +680 | 23851 |
| 132 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +666 | 3653 |
| 133 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +652 | 8989 |
| 134 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +642 | 5447 |
| 135 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +624 | 47936 |
| 136 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +618 | 15887 |
| 137 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +613 | 3476 |
| 138 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +606 | 9083 |
| 139 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +587 | 4134 |
| 140 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +568 | 14976 |
| 141 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +560 | 2780 |
| 142 | [google-research/timesfm](https://github.com/google-research/timesfm) | +552 | 14015 |
| 143 | [wshobson/agents](https://github.com/wshobson/agents) | +540 | 32892 |
| 144 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +530 | 47122 |
| 145 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +529 | 3855 |
| 146 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +528 | 7116 |
| 147 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +519 | 28347 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +517 | 44545 |
| 149 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +508 | 4678 |
| 150 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +503 | 31848 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +496 | 17959 |
| 152 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +489 | 5348 |
| 153 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +483 | 44232 |
| 154 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +477 | 2400 |
| 155 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +459 | 24375 |
| 156 | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | +447 | 3000 |
| 157 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +446 | 24104 |
| 158 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +442 | 8175 |
| 159 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +433 | 3598 |
| 160 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +431 | 3547 |
| 161 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +427 | 11136 |
| 162 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +422 | 8231 |
| 163 | [htdt/godogen](https://github.com/htdt/godogen) | +422 | 2515 |
| 164 | [hectorvent/floci](https://github.com/hectorvent/floci) | +419 | 2595 |
| 165 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +418 | 23331 |
| 166 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +416 | 10862 |
| 167 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +415 | 2672 |
| 168 | [eze-is/web-access](https://github.com/eze-is/web-access) | +415 | 3716 |
| 169 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +405 | 2067 |
| 170 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +394 | 12256 |
| 171 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +393 | 2488 |
| 172 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +385 | 7224 |
| 173 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +380 | 3637 |
| 174 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +361 | 13445 |
| 175 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +357 | 2111 |
| 176 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +350 | 2634 |
| 177 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +339 | 1827 |
| 178 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +333 | 6544 |
| 179 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +325 | 1819 |
| 180 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +323 | 2656 |
| 181 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +323 | 3724 |
| 182 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +319 | 1427 |
| 183 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +319 | 1590 |
| 184 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +317 | 10604 |
| 185 | [usestrix/strix](https://github.com/usestrix/strix) | +316 | 23121 |
| 186 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +313 | 2052 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +307 | 10817 |
| 188 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +303 | 33712 |
| 189 | [apify/agent-skills](https://github.com/apify/agent-skills) | +296 | 1817 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +290 | 2260 |
| 191 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +282 | 2842 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +280 | 5004 |
| 193 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +279 | 25201 |
| 194 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +275 | 1450 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +271 | 1940 |
| 196 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +268 | 29780 |
| 197 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +259 | 4595 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +251 | 22342 |
| 199 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +250 | 2308 |
| 200 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +246 | 1692 |
| 201 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +239 | 15008 |
| 202 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +237 | 13790 |
| 203 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +228 | 6051 |
| 204 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +226 | 7345 |
| 205 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +223 | 1412 |
| 206 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +221 | 1218 |
| 207 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +210 | 36103 |
| 208 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +210 | 1251 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +208 | 41086 |
| 210 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +199 | 879 |
| 211 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +198 | 896 |
| 212 | [decolua/9router](https://github.com/decolua/9router) | +187 | 1699 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +185 | 21805 |
| 214 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +179 | 1104 |
| 215 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +178 | 8994 |
| 216 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +176 | 2608 |
| 217 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2489 |
| 218 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +154 | 2705 |
| 219 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +153 | 843 |
| 220 | [es617/claude-replay](https://github.com/es617/claude-replay) | +147 | 589 |
| 221 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +146 | 785 |
| 222 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +144 | 2421 |
| 223 | [linlay/zenmind](https://github.com/linlay/zenmind) | +143 | 195 |
| 224 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +141 | 40265 |
| 225 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +140 | 1102 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +136 | 29270 |
| 227 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 529 |
| 228 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +132 | 1824 |
| 229 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +131 | 1752 |
| 230 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +131 | 1333 |
| 231 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +130 | 5459 |
| 232 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +129 | 951 |
| 233 | [cockpit-project/cockpit](https://github.com/cockpit-project/cockpit) | +126 | 13845 |
| 234 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +124 | 12495 |
| 235 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +123 | 519 |
| 236 | [4ier/neo](https://github.com/4ier/neo) | +121 | 656 |
| 237 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +121 | 35473 |
| 238 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +119 | 762 |
| 239 | [dashersw/gea](https://github.com/dashersw/gea) | +118 | 849 |
| 240 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +118 | 0 |
| 241 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +117 | 23097 |
| 242 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +116 | 26387 |
| 243 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10056 |
| 244 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +114 | 2576 |
| 245 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +114 | 581 |
| 246 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +113 | 10511 |
| 247 | [robinebers/openusage](https://github.com/robinebers/openusage) | +108 | 1682 |
| 248 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +108 | 462 |
| 249 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +107 | 2052 |
| 250 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +106 | 656 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +104 | 1432 |
| 252 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +104 | 33000 |
| 253 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 516 |
| 254 | [skylot/jadx](https://github.com/skylot/jadx) | +102 | 47365 |
| 255 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +101 | 598 |
| 256 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +100 | 448 |
| 257 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +99 | 1565 |
| 258 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +98 | 709 |
| 259 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +98 | 467 |
| 260 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +97 | 788 |
| 261 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +97 | 1843 |
| 262 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +96 | 545 |
| 263 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +94 | 48784 |
| 264 | [idinging/freemail](https://github.com/idinging/freemail) | +93 | 1283 |
| 265 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +92 | 395 |
| 266 | [microg/GmsCore](https://github.com/microg/GmsCore) | +92 | 12795 |
| 267 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +91 | 649 |
| 268 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +90 | 3218 |
| 269 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +87 | 9082 |
| 270 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +85 | 1423 |
| 271 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +84 | 3779 |
| 272 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +83 | 901 |
| 273 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +83 | 3382 |
| 274 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +82 | 446 |
| 275 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +82 | 11450 |
| 276 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +81 | 1034 |
| 277 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +79 | 3511 |
| 278 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +78 | 377 |
| 279 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +77 | 1181 |
| 280 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +76 | 3491 |
| 281 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +75 | 27119 |
| 282 | [ingriddaleusag-dotcom/PeekPiliRelease](https://github.com/ingriddaleusag-dotcom/PeekPiliRelease) | +74 | 1067 |
| 283 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +73 | 458 |
| 284 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +71 | 688 |
| 285 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +70 | 861 |
| 286 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +69 | 425 |
| 287 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +69 | 45263 |
| 288 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +69 | 37313 |
| 289 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +68 | 671 |
| 290 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +68 | 8403 |
| 291 | [crimera/piko](https://github.com/crimera/piko) | +66 | 3012 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +64 | 1594 |
| 293 | [apache/kafka](https://github.com/apache/kafka) | +64 | 32043 |
| 294 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +63 | 348 |
| 295 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +61 | 1638 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +61 | 31476 |
| 297 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +60 | 11613 |
| 298 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1451 |
| 299 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +59 | 381 |
| 300 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +59 | 26650 |
