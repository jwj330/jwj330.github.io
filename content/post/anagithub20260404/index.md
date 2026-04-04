---
title: "2026-04-04 GitHub增长趋势报告"
description: "1.oh-my-codex+491 2.openscreen+394 3.onyx+318 4.boneyard+300 5.hermes-agent+230"
date: 2026-04-04T20:35:13+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-04 20:35:13

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
        'daily': {"categories": ["dmtrKovalenko/fff.nvim", "shareAI-lab/learn-claude-code", "openai/codex-plugin-cc", "badlogic/pi-mono", "k2-fsa/OmniVoice", "666ghj/MiroFish", "farion1231/cc-switch", "TauricResearch/TradingAgents", "code-yeongyu/oh-my-openagent", "google-research/timesfm", "jackwener/opencli", "Yeachan-Heo/oh-my-claudecode", "paperclipai/paperclip", "block/goose", "luongnv89/claude-howto", "NousResearch/hermes-agent", "0xGF/boneyard", "onyx-dot-app/onyx", "siddharthvaddem/openscreen", "Yeachan-Heo/oh-my-codex"], "data": [100, 105, 107, 107, 109, 114, 114, 117, 135, 162, 186, 196, 196, 204, 212, 230, 300, 318, 394, 491]},
        'weekly': {"categories": ["JCodesMore/ai-website-cloner-template", "ChinaSiro/claude-code-sourcemap", "anthropics/skills", "msitarzewski/agency-agents", "shareAI-lab/learn-claude-code", "karpathy/autoresearch", "bytedance/deer-flow", "shanraisshan/claude-code-best-practice", "Yeachan-Heo/oh-my-claudecode", "NousResearch/hermes-agent", "paperclipai/paperclip", "microsoft/VibeVoice", "garrytan/gstack", "siddharthvaddem/openscreen", "openai/codex-plugin-cc", "Yeachan-Heo/oh-my-codex", "luongnv89/claude-howto", "obra/superpowers", "affaan-m/everything-claude-code", "anthropics/claude-code"], "data": [804, 828, 863, 918, 944, 966, 1021, 1083, 1305, 1338, 1543, 1548, 1581, 1611, 1630, 1915, 1984, 2290, 3196, 3273]},
        'monthly': {"categories": ["koala73/worldmonitor", "nextlevelbuilder/ui-ux-pro-max-skill", "NousResearch/hermes-agent", "ruvnet/RuView", "anomalyco/opencode", "shanraisshan/claude-code-best-practice", "gsd-build/get-shit-done", "shareAI-lab/learn-claude-code", "anthropics/skills", "googleworkspace/cli", "bytedance/deer-flow", "anthropics/claude-code", "666ghj/MiroFish", "paperclipai/paperclip", "obra/superpowers", "garrytan/gstack", "msitarzewski/agency-agents", "karpathy/autoresearch", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [3474, 3477, 3557, 3724, 3955, 4016, 4074, 4750, 4804, 5029, 5198, 5229, 8262, 8865, 10856, 10904, 12557, 12606, 13121, 19140]}
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
| 1 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +491 | 15469 |
| 2 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +394 | 19424 |
| 3 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +318 | 24084 |
| 4 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +300 | 2325 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +230 | 24813 |
| 6 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +212 | 18872 |
| 7 | [block/goose](https://github.com/block/goose) | +204 | 31098 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +196 | 46871 |
| 9 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +196 | 23762 |
| 10 | [jackwener/opencli](https://github.com/jackwener/opencli) | +186 | 12985 |
| 11 | [google-research/timesfm](https://github.com/google-research/timesfm) | +162 | 14616 |
| 12 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +135 | 33878 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +117 | 30590 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +114 | 38844 |
| 15 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +114 | 49279 |
| 16 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +109 | 1326 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +107 | 31467 |
| 18 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +107 | 11592 |
| 19 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +105 | 48201 |
| 20 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +100 | 3456 |
| 21 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +93 | 26986 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +92 | 31771 |
| 23 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +90 | 4570 |
| 24 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +89 | 36064 |
| 25 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +89 | 1250 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +89 | 47740 |
| 27 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +85 | 12847 |
| 28 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +83 | 3540 |
| 29 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +81 | 30618 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +79 | 17547 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3273 | 69674 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3196 | 51199 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +2290 | 60312 |
| 4 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1984 | 18873 |
| 5 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1915 | 15470 |
| 6 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1630 | 11592 |
| 7 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1611 | 19424 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1581 | 63915 |
| 9 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1548 | 36064 |
| 10 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1543 | 46871 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1338 | 24813 |
| 12 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1305 | 23762 |
| 13 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1083 | 31771 |
| 14 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1021 | 57761 |
| 15 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +966 | 65534 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +944 | 48201 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +918 | 71007 |
| 18 | [anthropics/skills](https://github.com/anthropics/skills) | +863 | 74774 |
| 19 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +828 | 8373 |
| 20 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +804 | 7624 |
| 21 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +798 | 18375 |
| 22 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +796 | 24085 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +750 | 34148 |
| 24 | [jackwener/opencli](https://github.com/jackwener/opencli) | +735 | 12985 |
| 25 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +703 | 49279 |
| 26 | [google-research/timesfm](https://github.com/google-research/timesfm) | +665 | 14616 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +621 | 38844 |
| 28 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +620 | 5568 |
| 29 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +618 | 15068 |
| 30 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +598 | 30590 |
| 31 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +596 | 47740 |
| 32 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +592 | 33878 |
| 33 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +524 | 30678 |
| 34 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +425 | 36455 |
| 35 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +423 | 3181 |
| 36 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +417 | 21572 |
| 37 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +402 | 32872 |
| 38 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +394 | 3609 |
| 39 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +392 | 31467 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +390 | 17547 |
| 41 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +387 | 4053 |
| 42 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +376 | 37330 |
| 43 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +375 | 3286 |
| 44 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +371 | 2325 |
| 45 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +367 | 30618 |
| 46 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +356 | 16745 |
| 47 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +349 | 2403 |
| 48 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +334 | 9223 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +330 | 37254 |
| 50 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +318 | 29736 |
| 51 | [block/goose](https://github.com/block/goose) | +316 | 31098 |
| 52 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +313 | 4573 |
| 53 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +311 | 1933 |
| 54 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +301 | 23021 |
| 55 | [revfactory/harness](https://github.com/revfactory/harness) | +292 | 1810 |
| 56 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +288 | 9194 |
| 57 | [ponponon/claude_code_src](https://github.com/ponponon/claude_code_src) | +272 | 1988 |
| 58 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +268 | 46523 |
| 59 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +267 | 45637 |
| 60 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +264 | 4529 |
| 61 | [pascalorg/editor](https://github.com/pascalorg/editor) | +264 | 9429 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +262 | 19533 |
| 63 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +258 | 21222 |
| 64 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +257 | 5141 |
| 65 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +256 | 9341 |
| 66 | [tanweai/pua](https://github.com/tanweai/pua) | +255 | 15052 |
| 67 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +252 | 44224 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +251 | 33614 |
| 69 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +251 | 27081 |
| 70 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +247 | 3456 |
| 71 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +244 | 26986 |
| 72 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +233 | 1446 |
| 73 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +232 | 18798 |
| 74 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +230 | 23356 |
| 75 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +230 | 22965 |
| 76 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +225 | 1326 |
| 77 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +224 | 27994 |
| 78 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +223 | 3002 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +223 | 24826 |
| 80 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +223 | 28299 |
| 81 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +222 | 2749 |
| 82 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +220 | 13782 |
| 83 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +219 | 15860 |
| 84 | [chauncygu/collection-claude-code-source-code](https://github.com/chauncygu/collection-claude-code-source-code) | +216 | 1430 |
| 85 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +212 | 1551 |
| 86 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +208 | 1250 |
| 87 | [punitarani/fli](https://github.com/punitarani/fli) | +206 | 1383 |
| 88 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +205 | 1115 |
| 89 | [multica-ai/multica](https://github.com/multica-ai/multica) | +199 | 1968 |
| 90 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +197 | 20956 |
| 91 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +195 | 12847 |
| 92 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +193 | 5401 |
| 93 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +192 | 3540 |
| 94 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +192 | 1867 |
| 95 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +191 | 1903 |
| 96 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | +191 | 3017 |
| 97 | [lorryjovens-hub/claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust) | +190 | 1036 |
| 98 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +188 | 32079 |
| 99 | [mattpocock/skills](https://github.com/mattpocock/skills) | +186 | 11914 |
| 100 | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | +185 | 1119 |
| 101 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +180 | 10248 |
| 102 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +178 | 8236 |
| 103 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +177 | 905 |
| 104 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +177 | 39841 |
| 105 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +173 | 8305 |
| 106 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +172 | 37924 |
| 107 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +171 | 19120 |
| 108 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +167 | 9045 |
| 109 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +163 | 34626 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +158 | 28472 |
| 111 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +158 | 28944 |
| 112 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +153 | 10302 |
| 113 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +152 | 5479 |
| 114 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +151 | 12326 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +151 | 15983 |
| 116 | [jundot/omlx](https://github.com/jundot/omlx) | +143 | 8370 |
| 117 | [roboflow/supervision](https://github.com/roboflow/supervision) | +143 | 36553 |
| 118 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +142 | 14433 |
| 119 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +139 | 36799 |
| 120 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +138 | 17331 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +19140 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13121 | 51199 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12606 | 65534 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12557 | 71007 |
| 5 | [garrytan/gstack](https://github.com/garrytan/gstack) | +10904 | 63915 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +10856 | 60312 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8865 | 46871 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8262 | 49279 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5229 | 69674 |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5198 | 57761 |
| 11 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +5029 | 23787 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +4804 | 74774 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4750 | 48201 |
| 14 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4074 | 47740 |
| 15 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4016 | 31771 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3955 | 109881 |
| 17 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +3724 | 45637 |
| 18 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3557 | 24813 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3477 | 34148 |
| 20 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3474 | 46523 |
| 21 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +3411 | 44224 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3377 | 21572 |
| 23 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +3151 | 37057 |
| 24 | [openai/symphony](https://github.com/openai/symphony) | +3121 | 14558 |
| 25 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3076 | 20956 |
| 26 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2944 | 15147 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2830 | 15860 |
| 28 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2745 | 85286 |
| 29 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2733 | 18439 |
| 30 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2730 | 27081 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2728 | 38844 |
| 32 | [tanweai/pua](https://github.com/tanweai/pua) | +2602 | 15052 |
| 33 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2593 | 30590 |
| 34 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2557 | 34626 |
| 35 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2438 | 17547 |
| 36 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2397 | 28299 |
| 37 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2305 | 13782 |
| 38 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2289 | 23762 |
| 39 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2288 | 28644 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2272 | 27994 |
| 41 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2257 | 18873 |
| 42 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2242 | 21558 |
| 43 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2206 | 15470 |
| 44 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2142 | 9482 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2127 | 31467 |
| 46 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2115 | 16745 |
| 47 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +2109 | 30618 |
| 48 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2106 | 8129 |
| 49 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2086 | 12547 |
| 50 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2083 | 12985 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2070 | 33878 |
| 52 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2011 | 30678 |
| 53 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1975 | 18375 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1971 | 71722 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1966 | 28944 |
| 56 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1928 | 37924 |
| 57 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1918 | 37330 |
| 58 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1912 | 21222 |
| 59 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1901 | 15068 |
| 60 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1891 | 60117 |
| 61 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1867 | 19424 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1829 | 23021 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1790 | 37254 |
| 64 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1783 | 29736 |
| 65 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1730 | 36064 |
| 66 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1675 | 36455 |
| 67 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1667 | 9418 |
| 68 | [nearai/ironclaw](https://github.com/nearai/ironclaw) | +1660 | 11402 |
| 69 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1640 | 19120 |
| 70 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1630 | 11592 |
| 71 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1618 | 26476 |
| 72 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1602 | 18338 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1600 | 11095 |
| 74 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1596 | 8884 |
| 75 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1590 | 11914 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1574 | 61744 |
| 77 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1574 | 19381 |
| 78 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1565 | 26986 |
| 79 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1542 | 10302 |
| 80 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1506 | 37154 |
| 81 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1447 | 33614 |
| 82 | [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | +1441 | 29435 |
| 83 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1431 | 14433 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1399 | 15983 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1398 | 18798 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1392 | 98536 |
| 87 | [jundot/omlx](https://github.com/jundot/omlx) | +1360 | 8370 |
| 88 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1355 | 9194 |
| 89 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1336 | 10248 |
| 90 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1328 | 7777 |
| 91 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1319 | 12456 |
| 92 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1313 | 9429 |
| 93 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1306 | 43973 |
| 94 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1276 | 8408 |
| 95 | [openai/skills](https://github.com/openai/skills) | +1269 | 16145 |
| 96 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1251 | 19533 |
| 97 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1226 | 78902 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1199 | 9045 |
| 99 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1172 | 8125 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1154 | 9341 |
| 101 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1142 | 79656 |
| 102 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1087 | 7625 |
| 103 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1060 | 96919 |
| 104 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1031 | 52700 |
| 105 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +997 | 24086 |
| 106 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +944 | 5479 |
| 107 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +911 | 17331 |
| 108 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +899 | 73135 |
| 109 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +891 | 35735 |
| 110 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +888 | 22965 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +872 | 23356 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +845 | 7332 |
| 113 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +828 | 8373 |
| 114 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +821 | 49621 |
| 115 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +817 | 39841 |
| 116 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +809 | 28472 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +807 | 45886 |
| 118 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +789 | 9742 |
| 119 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +769 | 37564 |
| 120 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +763 | 3529 |
| 121 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +757 | 36799 |
| 122 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +753 | 29057 |
| 123 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +752 | 4639 |
| 124 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +721 | 4241 |
| 125 | [google-research/timesfm](https://github.com/google-research/timesfm) | +715 | 14616 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +712 | 4389 |
| 127 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +703 | 4040 |
| 128 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +702 | 17874 |
| 129 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +695 | 9223 |
| 130 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +694 | 4771 |
| 131 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +682 | 5568 |
| 132 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +681 | 4570 |
| 133 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +681 | 7636 |
| 134 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +668 | 3662 |
| 135 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +663 | 24024 |
| 136 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +619 | 3505 |
| 137 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +618 | 47936 |
| 138 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +616 | 9142 |
| 139 | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | +610 | 15895 |
| 140 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +581 | 4053 |
| 141 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +561 | 2788 |
| 142 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +559 | 15042 |
| 143 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +548 | 32079 |
| 144 | [wshobson/agents](https://github.com/wshobson/agents) | +536 | 32943 |
| 145 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +534 | 47122 |
| 146 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +523 | 44545 |
| 147 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +520 | 28410 |
| 148 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +520 | 7142 |
| 149 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +513 | 5401 |
| 150 | [BIT-DataLab/Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana) | +495 | 4687 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +487 | 18024 |
| 152 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +484 | 44232 |
| 153 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +474 | 2409 |
| 154 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +446 | 24420 |
| 155 | [eze-is/web-access](https://github.com/eze-is/web-access) | +442 | 3792 |
| 156 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +439 | 8236 |
| 157 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +439 | 3617 |
| 158 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +436 | 8305 |
| 159 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +432 | 3556 |
| 160 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +429 | 2737 |
| 161 | [htdt/godogen](https://github.com/htdt/godogen) | +429 | 2553 |
| 162 | [hectorvent/floci](https://github.com/hectorvent/floci) | +427 | 2634 |
| 163 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +425 | 24133 |
| 164 | [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | +415 | 3020 |
| 165 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +411 | 10892 |
| 166 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +407 | 2101 |
| 167 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +404 | 11180 |
| 168 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +402 | 2531 |
| 169 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +402 | 23357 |
| 170 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +397 | 12326 |
| 171 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +369 | 3647 |
| 172 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +367 | 2146 |
| 173 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +364 | 2403 |
| 174 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +355 | 2653 |
| 175 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +349 | 1903 |
| 176 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +341 | 2749 |
| 177 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +341 | 1834 |
| 178 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +326 | 6575 |
| 179 | [usestrix/strix](https://github.com/usestrix/strix) | +325 | 23144 |
| 180 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +325 | 2098 |
| 181 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +323 | 3730 |
| 182 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +322 | 1594 |
| 183 | [skernelx/tavily-key-generator](https://github.com/skernelx/tavily-key-generator) | +320 | 1429 |
| 184 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +314 | 10625 |
| 185 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +301 | 10862 |
| 186 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +299 | 33712 |
| 187 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +298 | 2303 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +296 | 4673 |
| 189 | [apify/agent-skills](https://github.com/apify/agent-skills) | +290 | 1820 |
| 190 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +289 | 2873 |
| 191 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +279 | 25237 |
| 192 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +278 | 1456 |
| 193 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +276 | 5029 |
| 194 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +268 | 2377 |
| 195 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +260 | 29780 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +259 | 1982 |
| 197 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +251 | 1719 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +244 | 22407 |
| 199 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +237 | 13809 |
| 200 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +235 | 15046 |
| 201 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +234 | 1271 |
| 202 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +231 | 1449 |
| 203 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +230 | 6072 |
| 204 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +230 | 7368 |
| 205 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +211 | 1264 |
| 206 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +207 | 36103 |
| 207 | [usebruno/bruno](https://github.com/usebruno/bruno) | +201 | 41086 |
| 208 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +200 | 889 |
| 209 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +199 | 944 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +195 | 1741 |
| 211 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +181 | 2618 |
| 212 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +180 | 1110 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +180 | 21828 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +177 | 905 |
| 215 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +174 | 9007 |
| 216 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2490 |
| 217 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +158 | 852 |
| 218 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +156 | 2710 |
| 219 | [es617/claude-replay](https://github.com/es617/claude-replay) | +148 | 592 |
| 220 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +147 | 817 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +142 | 2429 |
| 222 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +135 | 1115 |
| 223 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 529 |
| 224 | [linlay/zenmind](https://github.com/linlay/zenmind) | +134 | 130 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +133 | 29296 |
| 226 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +131 | 40265 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +129 | 1342 |
| 228 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +128 | 5473 |
| 229 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +124 | 950 |
| 230 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +124 | 521 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +123 | 12512 |
| 232 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +122 | 35473 |
| 233 | [dashersw/gea](https://github.com/dashersw/gea) | +121 | 858 |
| 234 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +120 | 764 |
| 235 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +119 | 23124 |
| 236 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10063 |
| 237 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +115 | 1827 |
| 238 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +114 | 10524 |
| 239 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +112 | 3563 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +112 | 26397 |
| 241 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +111 | 2586 |
| 242 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +109 | 463 |
| 243 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +109 | 0 |
| 244 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +108 | 671 |
| 245 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +108 | 1756 |
| 246 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +108 | 33000 |
| 247 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +107 | 2053 |
| 248 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +106 | 569 |
| 249 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +103 | 724 |
| 250 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +102 | 472 |
| 251 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +102 | 600 |
| 252 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +102 | 1441 |
| 253 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +102 | 516 |
| 254 | [robinebers/openusage](https://github.com/robinebers/openusage) | +101 | 1696 |
| 255 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +101 | 457 |
| 256 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +98 | 705 |
| 257 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +97 | 790 |
| 258 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +97 | 547 |
| 259 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +97 | 1579 |
| 260 | [skylot/jadx](https://github.com/skylot/jadx) | +97 | 47365 |
| 261 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +96 | 1849 |
| 262 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +96 | 564 |
| 263 | [idinging/freemail](https://github.com/idinging/freemail) | +95 | 1293 |
| 264 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +95 | 406 |
| 265 | [microg/GmsCore](https://github.com/microg/GmsCore) | +95 | 12805 |
| 266 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +94 | 3232 |
| 267 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +94 | 48784 |
| 268 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +87 | 3786 |
| 269 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +85 | 1213 |
| 270 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +85 | 916 |
| 271 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +84 | 9088 |
| 272 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +84 | 3400 |
| 273 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +83 | 1058 |
| 274 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +83 | 453 |
| 275 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +80 | 1428 |
| 276 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +79 | 387 |
| 277 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +79 | 11460 |
| 278 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +76 | 462 |
| 279 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +74 | 3502 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +73 | 27125 |
| 281 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +72 | 935 |
| 282 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +70 | 680 |
| 283 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +70 | 45263 |
| 284 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +69 | 439 |
| 285 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +69 | 689 |
| 286 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +67 | 37313 |
| 287 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +66 | 8409 |
| 288 | [crimera/piko](https://github.com/crimera/piko) | +66 | 3028 |
| 289 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +64 | 368 |
| 290 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +64 | 350 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +64 | 31476 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +63 | 1596 |
| 293 | [apache/kafka](https://github.com/apache/kafka) | +62 | 32043 |
| 294 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +60 | 383 |
| 295 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +59 | 662 |
| 296 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +59 | 4620 |
| 297 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +59 | 26652 |
| 298 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +58 | 1640 |
| 299 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1469 |
| 300 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +58 | 7742 |
