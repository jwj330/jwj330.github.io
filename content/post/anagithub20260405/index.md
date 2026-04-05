---
title: "2026-04-05 GitHub增长趋势报告"
description: "1.awesome-design-md+1274 2.openscreen+723 3.agent-skills+605 4.claude-howto+389 5.oh-my-codex+381"
date: 2026-04-05T20:36:58+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-05 20:36:58

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
        'daily': {"categories": ["microsoft/VibeVoice", "OpenHub-Store/GitHub-Store", "google-research/timesfm", "farion1231/cc-switch", "666ghj/MiroFish", "capcom6/android-sms-gateway", "abhigyanpatwari/GitNexus", "rtk-ai/rtk", "NVIDIA/personaplex", "0xGF/boneyard", "Yeachan-Heo/oh-my-claudecode", "block/goose", "paperclipai/paperclip", "onyx-dot-app/onyx", "NousResearch/hermes-agent", "Yeachan-Heo/oh-my-codex", "luongnv89/claude-howto", "addyosmani/agent-skills", "siddharthvaddem/openscreen", "VoltAgent/awesome-design-md"], "data": [117, 126, 131, 131, 142, 147, 158, 200, 207, 218, 222, 224, 276, 297, 358, 381, 389, 605, 723, 1274]},
        'weekly': {"categories": ["bytedance/deer-flow", "sherlock-project/sherlock", "onyx-dot-app/onyx", "karpathy/autoresearch", "shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "sanbuphy/learn-coding-agent", "Yeachan-Heo/oh-my-claudecode", "garrytan/gstack", "paperclipai/paperclip", "microsoft/VibeVoice", "NousResearch/hermes-agent", "openai/codex-plugin-cc", "obra/superpowers", "luongnv89/claude-howto", "VoltAgent/awesome-design-md", "Yeachan-Heo/oh-my-codex", "siddharthvaddem/openscreen", "anthropics/claude-code", "affaan-m/everything-claude-code"], "data": [941, 967, 994, 1005, 1012, 1073, 1334, 1364, 1464, 1479, 1519, 1537, 1713, 2158, 2175, 2246, 2267, 2322, 3371, 3411]},
        'monthly': {"categories": ["ruvnet/RuView", "Crosstalk-Solutions/project-nomad", "googleworkspace/cli", "nextlevelbuilder/ui-ux-pro-max-skill", "shanraisshan/claude-code-best-practice", "NousResearch/hermes-agent", "anomalyco/opencode", "gsd-build/get-shit-done", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "anthropics/claude-code", "666ghj/MiroFish", "paperclipai/paperclip", "obra/superpowers", "garrytan/gstack", "msitarzewski/agency-agents", "karpathy/autoresearch", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [3445, 3450, 3475, 3510, 3831, 3894, 3976, 4052, 4696, 4777, 5272, 5273, 8394, 8703, 10892, 11092, 12442, 12846, 13453, 18207]}
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
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1274 | 13947 |
| 2 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +723 | 22311 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +605 | 3301 |
| 4 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +389 | 20244 |
| 5 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +381 | 16529 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +358 | 26111 |
| 7 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +297 | 24911 |
| 8 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +276 | 47766 |
| 9 | [block/goose](https://github.com/block/goose) | +224 | 31098 |
| 10 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +222 | 24417 |
| 11 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +218 | 2775 |
| 12 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +207 | 6852 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +200 | 18168 |
| 14 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +158 | 22482 |
| 15 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +147 | 2844 |
| 16 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +142 | 49922 |
| 17 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +131 | 39279 |
| 18 | [google-research/timesfm](https://github.com/google-research/timesfm) | +131 | 14910 |
| 19 | [OpenHub-Store/GitHub-Store](https://github.com/OpenHub-Store/GitHub-Store) | +126 | 10718 |
| 20 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +117 | 36423 |
| 21 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +116 | 1722 |
| 22 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +114 | 48588 |
| 23 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +114 | 30590 |
| 24 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +113 | 3879 |
| 25 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +111 | 979 |
| 26 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +109 | 4909 |
| 27 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +106 | 33878 |
| 28 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +103 | 46777 |
| 29 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +103 | 27338 |
| 30 | [jackwener/opencli](https://github.com/jackwener/opencli) | +102 | 13353 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3411 | 51199 |
| 2 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3371 | 69674 |
| 3 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2322 | 22312 |
| 4 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2267 | 16529 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2246 | 13947 |
| 6 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2175 | 20244 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2158 | 60312 |
| 8 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1713 | 11869 |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1537 | 26112 |
| 10 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1519 | 36422 |
| 11 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1479 | 47766 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1464 | 64538 |
| 13 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1364 | 24417 |
| 14 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1334 | 11331 |
| 15 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1073 | 71937 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1012 | 32098 |
| 17 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1005 | 66343 |
| 18 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +994 | 24911 |
| 19 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +967 | 73135 |
| 20 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +941 | 58209 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +894 | 48588 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +883 | 74774 |
| 23 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +846 | 8445 |
| 24 | [google-research/timesfm](https://github.com/google-research/timesfm) | +791 | 14910 |
| 25 | [jackwener/opencli](https://github.com/jackwener/opencli) | +769 | 13353 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +755 | 34148 |
| 27 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +717 | 49922 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +668 | 39279 |
| 29 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +656 | 18685 |
| 30 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +652 | 33878 |
| 31 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +644 | 3301 |
| 32 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +636 | 5678 |
| 33 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +598 | 30590 |
| 34 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +575 | 2775 |
| 35 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +561 | 7793 |
| 36 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +548 | 18168 |
| 37 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +542 | 48009 |
| 38 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +528 | 30678 |
| 39 | [block/goose](https://github.com/block/goose) | +520 | 31098 |
| 40 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +466 | 3285 |
| 41 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +454 | 32872 |
| 42 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +452 | 2705 |
| 43 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +443 | 31846 |
| 44 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +431 | 15203 |
| 45 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +429 | 36704 |
| 46 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +393 | 37330 |
| 47 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +390 | 2093 |
| 48 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +384 | 30850 |
| 49 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +356 | 21832 |
| 50 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +346 | 3690 |
| 51 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +345 | 23289 |
| 52 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +337 | 1722 |
| 53 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +336 | 37431 |
| 54 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +336 | 16895 |
| 55 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +316 | 46777 |
| 56 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +312 | 4206 |
| 57 | [vas3k/TaxHacker](https://github.com/vas3k/TaxHacker) | +308 | 4673 |
| 58 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +304 | 27338 |
| 59 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +292 | 3879 |
| 60 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +290 | 30059 |
| 61 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +289 | 22482 |
| 62 | [ponponon/claude_code_src](https://github.com/ponponon/claude_code_src) | +288 | 2032 |
| 63 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +288 | 19838 |
| 64 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +285 | 2496 |
| 65 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +280 | 21417 |
| 66 | [revfactory/harness](https://github.com/revfactory/harness) | +279 | 1893 |
| 67 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +275 | 1601 |
| 68 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +272 | 1553 |
| 69 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +272 | 44412 |
| 70 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +270 | 3650 |
| 71 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +269 | 9285 |
| 72 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +268 | 33753 |
| 73 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +268 | 5224 |
| 74 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +267 | 9349 |
| 75 | [chauncygu/collection-claude-code-source-code](https://github.com/chauncygu/collection-claude-code-source-code) | +261 | 1566 |
| 76 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +259 | 1426 |
| 77 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +256 | 2841 |
| 78 | [pascalorg/editor](https://github.com/pascalorg/editor) | +256 | 9513 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +255 | 18977 |
| 80 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +254 | 13103 |
| 81 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +251 | 3400 |
| 82 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +249 | 9545 |
| 83 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +246 | 23473 |
| 84 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +243 | 45776 |
| 85 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +236 | 3036 |
| 86 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +235 | 12979 |
| 87 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +230 | 1110 |
| 88 | [jarmuine/claude-code](https://github.com/jarmuine/claude-code) | +224 | 1831 |
| 89 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +222 | 4909 |
| 90 | [lorryjovens-hub/claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust) | +219 | 1100 |
| 91 | [mattpocock/skills](https://github.com/mattpocock/skills) | +215 | 12175 |
| 92 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +213 | 6852 |
| 93 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +213 | 10388 |
| 94 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +212 | 1140 |
| 95 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +208 | 28123 |
| 96 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +208 | 32268 |
| 97 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +208 | 28440 |
| 98 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +203 | 979 |
| 99 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +202 | 5470 |
| 100 | [chatgptprojects/clear-code](https://github.com/chatgptprojects/clear-code) | +201 | 1990 |
| 101 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +201 | 21144 |
| 102 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | +200 | 3039 |
| 103 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +196 | 19324 |
| 104 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +196 | 1595 |
| 105 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +194 | 1871 |
| 106 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +184 | 39841 |
| 107 | [tanbiralam/claude-code](https://github.com/tanbiralam/claude-code) | +182 | 1261 |
| 108 | [punitarani/fli](https://github.com/punitarani/fli) | +182 | 1465 |
| 109 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +176 | 38043 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +170 | 9228 |
| 111 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +163 | 28575 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +162 | 7464 |
| 113 | [rushindrasinha/youtube-shorts-pipeline](https://github.com/rushindrasinha/youtube-shorts-pipeline) | +161 | 1506 |
| 114 | [github/copilot-cli-for-beginners](https://github.com/github/copilot-cli-for-beginners) | +158 | 1945 |
| 115 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +157 | 12360 |
| 116 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +155 | 24188 |
| 117 | [jundot/omlx](https://github.com/jundot/omlx) | +154 | 8506 |
| 118 | [cft0808/edict](https://github.com/cft0808/edict) | +152 | 14428 |
| 119 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +150 | 10401 |
| 120 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +150 | 34720 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +18207 | 224760 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13453 | 51199 |
| 3 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +12846 | 66343 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12442 | 71937 |
| 5 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11092 | 64538 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +10892 | 60312 |
| 7 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8703 | 47766 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8394 | 49922 |
| 9 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5273 | 69674 |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5272 | 58209 |
| 11 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4777 | 48588 |
| 12 | [anthropics/skills](https://github.com/anthropics/skills) | +4696 | 74774 |
| 13 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4052 | 48009 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3976 | 109881 |
| 15 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3894 | 26112 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3831 | 32098 |
| 17 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3510 | 34148 |
| 18 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +3475 | 23860 |
| 19 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3450 | 21832 |
| 20 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +3445 | 45776 |
| 21 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +3238 | 44412 |
| 22 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +3181 | 46777 |
| 23 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3102 | 21144 |
| 24 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2957 | 15177 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2854 | 16008 |
| 26 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2792 | 85286 |
| 27 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2773 | 27236 |
| 28 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2751 | 18515 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2728 | 39279 |
| 30 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2687 | 30590 |
| 31 | [tanweai/pua](https://github.com/tanweai/pua) | +2630 | 15151 |
| 32 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2629 | 20244 |
| 33 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2573 | 22313 |
| 34 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2555 | 16529 |
| 35 | [cft0808/edict](https://github.com/cft0808/edict) | +2526 | 14428 |
| 36 | [openai/symphony](https://github.com/openai/symphony) | +2518 | 14596 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2509 | 18168 |
| 38 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +2494 | 37116 |
| 39 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2450 | 24417 |
| 40 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2346 | 28440 |
| 41 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2338 | 13891 |
| 42 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2328 | 22482 |
| 43 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +2293 | 34720 |
| 44 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2253 | 13947 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2224 | 28123 |
| 46 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2177 | 13353 |
| 47 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2154 | 8250 |
| 48 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2146 | 16895 |
| 49 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +2133 | 9543 |
| 50 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2129 | 31846 |
| 51 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +2115 | 28735 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2097 | 33878 |
| 53 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2093 | 12586 |
| 54 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2043 | 30678 |
| 55 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2041 | 18685 |
| 56 | [github/spec-kit](https://github.com/github/spec-kit) | +1963 | 71722 |
| 57 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1929 | 29053 |
| 58 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1924 | 30850 |
| 59 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1912 | 21417 |
| 60 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1908 | 60117 |
| 61 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1886 | 37330 |
| 62 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1846 | 38043 |
| 63 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1845 | 23289 |
| 64 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1838 | 36422 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1760 | 37431 |
| 66 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1757 | 15203 |
| 67 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1755 | 30059 |
| 68 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1714 | 36704 |
| 69 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1713 | 11869 |
| 70 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1682 | 19324 |
| 71 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1671 | 9447 |
| 72 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1641 | 12175 |
| 73 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1608 | 11174 |
| 74 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1603 | 18419 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1593 | 19489 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1581 | 61744 |
| 77 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1578 | 10401 |
| 78 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1558 | 27338 |
| 79 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1520 | 37198 |
| 80 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1519 | 26585 |
| 81 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1461 | 8913 |
| 82 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1430 | 33753 |
| 83 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1393 | 9285 |
| 84 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1393 | 16045 |
| 85 | [jundot/omlx](https://github.com/jundot/omlx) | +1392 | 8506 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1384 | 98536 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1364 | 10388 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1362 | 18977 |
| 89 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1356 | 9513 |
| 90 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1347 | 79656 |
| 91 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1343 | 12569 |
| 92 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1340 | 7840 |
| 93 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1334 | 11331 |
| 94 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1319 | 43973 |
| 95 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1296 | 8458 |
| 96 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1291 | 14487 |
| 97 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1290 | 19838 |
| 98 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1285 | 24911 |
| 99 | [openai/skills](https://github.com/openai/skills) | +1238 | 16186 |
| 100 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1228 | 78902 |
| 101 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1207 | 9228 |
| 102 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1182 | 8178 |
| 103 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1177 | 7793 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1174 | 9545 |
| 105 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1139 | 73135 |
| 106 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1037 | 52700 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +960 | 5550 |
| 108 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +895 | 23474 |
| 109 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +890 | 35735 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +878 | 7464 |
| 111 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +846 | 8445 |
| 112 | [google-research/timesfm](https://github.com/google-research/timesfm) | +835 | 14910 |
| 113 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +827 | 39841 |
| 114 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +823 | 23005 |
| 115 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +806 | 49621 |
| 116 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +799 | 28575 |
| 117 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +796 | 45886 |
| 118 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +791 | 17411 |
| 119 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +775 | 4909 |
| 120 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +769 | 37564 |
| 121 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +753 | 29073 |
| 122 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +741 | 36799 |
| 123 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +740 | 4669 |
| 124 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +726 | 4435 |
| 125 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +723 | 9349 |
| 126 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +709 | 5678 |
| 127 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +709 | 4055 |
| 128 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +696 | 4793 |
| 129 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +696 | 17932 |
| 130 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +682 | 4310 |
| 131 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +672 | 9754 |
| 132 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +670 | 3669 |
| 133 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +652 | 7841 |
| 134 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +650 | 24188 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +629 | 9192 |
| 136 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +625 | 3527 |
| 137 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +618 | 4206 |
| 138 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +605 | 47936 |
| 139 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +594 | 3545 |
| 140 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +591 | 32268 |
| 141 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +567 | 2794 |
| 142 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +553 | 15113 |
| 143 | [wshobson/agents](https://github.com/wshobson/agents) | +534 | 33005 |
| 144 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +531 | 28478 |
| 145 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +529 | 47122 |
| 146 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +523 | 5470 |
| 147 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +520 | 7158 |
| 148 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +517 | 44545 |
| 149 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +496 | 2537 |
| 150 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +486 | 44232 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +485 | 18084 |
| 152 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +473 | 2410 |
| 153 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +456 | 8344 |
| 154 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +453 | 2705 |
| 155 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +446 | 24487 |
| 156 | [eze-is/web-access](https://github.com/eze-is/web-access) | +442 | 3913 |
| 157 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +440 | 2802 |
| 158 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +439 | 8283 |
| 159 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +439 | 3640 |
| 160 | [floci-io/floci](https://github.com/floci-io/floci) | +435 | 2678 |
| 161 | [htdt/godogen](https://github.com/htdt/godogen) | +434 | 2575 |
| 162 | [ysharma3501/LuxTTS](https://github.com/ysharma3501/LuxTTS) | +434 | 3562 |
| 163 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +407 | 2138 |
| 164 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +406 | 10916 |
| 165 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +404 | 11258 |
| 166 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +402 | 2573 |
| 167 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +402 | 23398 |
| 168 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +399 | 12360 |
| 169 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +395 | 2496 |
| 170 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +378 | 2841 |
| 171 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +378 | 2213 |
| 172 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +369 | 3656 |
| 173 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +367 | 1975 |
| 174 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +355 | 2677 |
| 175 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +343 | 1839 |
| 176 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +341 | 3879 |
| 177 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +339 | 2158 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +331 | 1722 |
| 179 | [usestrix/strix](https://github.com/usestrix/strix) | +330 | 23170 |
| 180 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +326 | 6609 |
| 181 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +323 | 3742 |
| 182 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +322 | 1608 |
| 183 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +314 | 10670 |
| 184 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +310 | 10907 |
| 185 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +300 | 33712 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +298 | 2326 |
| 187 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +296 | 4741 |
| 188 | [apify/agent-skills](https://github.com/apify/agent-skills) | +290 | 1827 |
| 189 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +289 | 2903 |
| 190 | [lxf746/any-auto-register](https://github.com/lxf746/any-auto-register) | +286 | 1465 |
| 191 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +279 | 25271 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +276 | 5054 |
| 193 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +268 | 2430 |
| 194 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +264 | 1426 |
| 195 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +260 | 29780 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +259 | 2018 |
| 197 | [dou-jiang/codex-console](https://github.com/dou-jiang/codex-console) | +258 | 1748 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +244 | 22475 |
| 199 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +240 | 7396 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +237 | 13827 |
| 201 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +235 | 15085 |
| 202 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +234 | 1321 |
| 203 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +231 | 1491 |
| 204 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +230 | 6095 |
| 205 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +212 | 1281 |
| 206 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +207 | 36103 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 894 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +201 | 41086 |
| 209 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +199 | 973 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +195 | 1770 |
| 211 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +181 | 2626 |
| 212 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +180 | 1112 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +180 | 21856 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +177 | 1110 |
| 215 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +174 | 9015 |
| 216 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2492 |
| 217 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +158 | 859 |
| 218 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +156 | 2719 |
| 219 | [es617/claude-replay](https://github.com/es617/claude-replay) | +148 | 592 |
| 220 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +147 | 834 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +140 | 2435 |
| 222 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +134 | 529 |
| 223 | [linlay/zenmind](https://github.com/linlay/zenmind) | +134 | 111 |
| 224 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +133 | 1138 |
| 225 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +131 | 40265 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +131 | 29317 |
| 227 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +128 | 5489 |
| 228 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +127 | 1347 |
| 229 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +124 | 949 |
| 230 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +124 | 527 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +123 | 12539 |
| 232 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +123 | 35473 |
| 233 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +122 | 23144 |
| 234 | [dashersw/gea](https://github.com/dashersw/gea) | +121 | 872 |
| 235 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +120 | 765 |
| 236 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +116 | 10551 |
| 237 | [is-a-dev/register](https://github.com/is-a-dev/register) | +115 | 10068 |
| 238 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +115 | 1830 |
| 239 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +112 | 3623 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +112 | 26410 |
| 241 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +111 | 2596 |
| 242 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +111 | 33000 |
| 243 | [gradenGnostic/LegacyLauncher](https://github.com/gradenGnostic/LegacyLauncher) | +109 | 464 |
| 244 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +108 | 681 |
| 245 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +108 | 1763 |
| 246 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +106 | 2070 |
| 247 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +103 | 736 |
| 248 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +102 | 475 |
| 249 | [KeyID-AI/agent-kit](https://github.com/KeyID-AI/agent-kit) | +102 | 604 |
| 250 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +102 | 1452 |
| 251 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +102 | 0 |
| 252 | [robinebers/openusage](https://github.com/robinebers/openusage) | +101 | 1703 |
| 253 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +101 | 460 |
| 254 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +100 | 1596 |
| 255 | [microg/GmsCore](https://github.com/microg/GmsCore) | +99 | 12816 |
| 256 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +98 | 762 |
| 257 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +97 | 796 |
| 258 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +97 | 549 |
| 259 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +97 | 568 |
| 260 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +96 | 1854 |
| 261 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +96 | 587 |
| 262 | [idinging/freemail](https://github.com/idinging/freemail) | +95 | 1296 |
| 263 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +95 | 420 |
| 264 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +95 | 516 |
| 265 | [skylot/jadx](https://github.com/skylot/jadx) | +95 | 47365 |
| 266 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +94 | 3241 |
| 267 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +94 | 48784 |
| 268 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +89 | 3413 |
| 269 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +87 | 3799 |
| 270 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +85 | 1236 |
| 271 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +85 | 930 |
| 272 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +83 | 1087 |
| 273 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +83 | 465 |
| 274 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +80 | 1429 |
| 275 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +80 | 9095 |
| 276 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +79 | 397 |
| 277 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +76 | 470 |
| 278 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +74 | 3515 |
| 279 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +74 | 11467 |
| 280 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +72 | 1060 |
| 281 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +72 | 27136 |
| 282 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 283 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +70 | 692 |
| 284 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +69 | 464 |
| 285 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +68 | 8418 |
| 286 | [crimera/piko](https://github.com/crimera/piko) | +67 | 3043 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +67 | 37313 |
| 288 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +64 | 431 |
| 289 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +64 | 350 |
| 290 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +64 | 31476 |
| 291 | [karthikreddy-7/TCS-NQT-CODING-SHEET](https://github.com/karthikreddy-7/TCS-NQT-CODING-SHEET) | +62 | 690 |
| 292 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +62 | 26658 |
| 293 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +61 | 387 |
| 294 | [apache/kafka](https://github.com/apache/kafka) | +61 | 32043 |
| 295 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +60 | 1602 |
| 296 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1471 |
| 297 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +60 | 4625 |
| 298 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +59 | 664 |
| 299 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +58 | 376 |
| 300 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +57 | 7179 |
