---
title: "2026-04-06 GitHub增长趋势报告"
description: "1.awesome-design-md+2203 2.openscreen+586 3.caveman+537 4.agent-skills+520 5.hermes-agent+440"
date: 2026-04-06T20:39:53+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-06 20:39:53

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
        'daily': {"categories": ["badlogic/pi-mono", "Yeachan-Heo/oh-my-claudecode", "elebumm/RedditVideoMakerBot", "rtk-ai/rtk", "JackChen-me/open-multi-agent", "KeygraphHQ/shannon", "666ghj/MiroFish", "abhigyanpatwari/GitNexus", "onyx-dot-app/onyx", "paperclipai/paperclip", "Yeachan-Heo/oh-my-codex", "google-ai-edge/gallery", "luongnv89/claude-howto", "capcom6/android-sms-gateway", "block/goose", "NousResearch/hermes-agent", "addyosmani/agent-skills", "JuliusBrussee/caveman", "siddharthvaddem/openscreen", "VoltAgent/awesome-design-md"], "data": [143, 170, 173, 180, 182, 187, 224, 225, 226, 239, 257, 292, 326, 346, 432, 440, 520, 537, 586, 2203]},
        'weekly': {"categories": ["karpathy/autoresearch", "sherlock-project/sherlock", "addyosmani/agent-skills", "onyx-dot-app/onyx", "msitarzewski/agency-agents", "microsoft/VibeVoice", "Yeachan-Heo/oh-my-claudecode", "garrytan/gstack", "sanbuphy/learn-coding-agent", "paperclipai/paperclip", "NousResearch/hermes-agent", "openai/codex-plugin-cc", "luongnv89/claude-howto", "obra/superpowers", "Yeachan-Heo/oh-my-codex", "siddharthvaddem/openscreen", "anthropics/claude-code", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "ultraworkers/claw-code"], "data": [1002, 1034, 1115, 1159, 1190, 1210, 1298, 1328, 1344, 1368, 1664, 1795, 1876, 2005, 2490, 2818, 3454, 3789, 4319, 22338]},
        'monthly': {"categories": ["Crosstalk-Solutions/project-nomad", "nextlevelbuilder/ui-ux-pro-max-skill", "anomalyco/opencode", "gsd-build/get-shit-done", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "anthropics/claude-code", "HKUDS/CLI-Anything", "paperclipai/paperclip", "666ghj/MiroFish", "obra/superpowers", "garrytan/gstack", "msitarzewski/agency-agents", "karpathy/autoresearch", "affaan-m/everything-claude-code", "openclaw/openclaw", "ultraworkers/claw-code"], "data": [3488, 3625, 3941, 4054, 4291, 4321, 4631, 4774, 5303, 5322, 5333, 8500, 8508, 10961, 11252, 12084, 13013, 13840, 17319, 22339]}
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
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2203 | 21903 |
| 2 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +586 | 23806 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +537 | 3824 |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +520 | 5583 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +440 | 27848 |
| 6 | [block/goose](https://github.com/block/goose) | +432 | 31098 |
| 7 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +346 | 3426 |
| 8 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +326 | 21236 |
| 9 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +292 | 17767 |
| 10 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +257 | 17397 |
| 11 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +239 | 48594 |
| 12 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +226 | 25415 |
| 13 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +225 | 23309 |
| 14 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +224 | 50631 |
| 15 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +187 | 36390 |
| 16 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +182 | 5156 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +180 | 18957 |
| 18 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +173 | 9456 |
| 19 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +170 | 24986 |
| 20 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +143 | 32337 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +120 | 49033 |
| 22 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +119 | 30590 |
| 23 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +117 | 39710 |
| 24 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +116 | 30678 |
| 25 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +114 | 977 |
| 26 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +113 | 20382 |
| 27 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +112 | 19107 |
| 28 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +111 | 1950 |
| 29 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +111 | 5233 |
| 30 | [enzomanuelmangano/demos](https://github.com/enzomanuelmangano/demos) | +107 | 2467 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +22338 | 173557 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +4319 | 21903 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3789 | 51199 |
| 4 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3454 | 69674 |
| 5 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2818 | 23807 |
| 6 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2490 | 17397 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2005 | 60312 |
| 8 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1876 | 21236 |
| 9 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1795 | 12241 |
| 10 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1664 | 27848 |
| 11 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1368 | 48594 |
| 12 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1344 | 11390 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1328 | 65384 |
| 14 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1298 | 24986 |
| 15 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1210 | 36819 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1190 | 72983 |
| 17 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1159 | 25416 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1115 | 5583 |
| 19 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1034 | 73135 |
| 20 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1002 | 67170 |
| 21 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +998 | 5156 |
| 22 | [block/goose](https://github.com/block/goose) | +928 | 31098 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +908 | 74774 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +907 | 32406 |
| 25 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +871 | 8509 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +832 | 34148 |
| 27 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +822 | 50631 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +813 | 49033 |
| 29 | [jackwener/opencli](https://github.com/jackwener/opencli) | +807 | 13641 |
| 30 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +801 | 5226 |
| 31 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +788 | 58588 |
| 32 | [google-research/timesfm](https://github.com/google-research/timesfm) | +787 | 15153 |
| 33 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +699 | 33878 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +696 | 39710 |
| 35 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +657 | 5194 |
| 36 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +651 | 5753 |
| 37 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +641 | 3068 |
| 38 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +609 | 18957 |
| 39 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +604 | 30590 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +590 | 28669 |
| 41 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +554 | 3824 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +552 | 32337 |
| 43 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +528 | 19107 |
| 44 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +519 | 48380 |
| 45 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +515 | 2936 |
| 46 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +495 | 3404 |
| 47 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +490 | 32872 |
| 48 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +482 | 30678 |
| 49 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +471 | 17767 |
| 50 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +442 | 23309 |
| 51 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +441 | 3426 |
| 52 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +410 | 2002 |
| 53 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +410 | 2175 |
| 54 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +401 | 36921 |
| 55 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +397 | 37330 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +385 | 23539 |
| 57 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +382 | 27698 |
| 58 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +367 | 31082 |
| 59 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +364 | 4100 |
| 60 | [motiful/cc-gateway](https://github.com/motiful/cc-gateway) | +364 | 2423 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +360 | 20382 |
| 62 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +350 | 3780 |
| 63 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +349 | 17221 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +348 | 37628 |
| 65 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +331 | 15730 |
| 66 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +325 | 1744 |
| 67 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +320 | 46972 |
| 68 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +319 | 5233 |
| 69 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +308 | 30320 |
| 70 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +306 | 8059 |
| 71 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +302 | 1717 |
| 72 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +301 | 22016 |
| 73 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +299 | 1228 |
| 74 | [ponponon/claude_code_src](https://github.com/ponponon/claude_code_src) | +298 | 2056 |
| 75 | [chauncygu/collection-claude-code-source-code](https://github.com/chauncygu/collection-claude-code-source-code) | +296 | 1676 |
| 76 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +282 | 1536 |
| 77 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +282 | 33949 |
| 78 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +282 | 4368 |
| 79 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +278 | 21688 |
| 80 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +277 | 7235 |
| 81 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +277 | 44621 |
| 82 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +276 | 5351 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +269 | 19154 |
| 84 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +268 | 36390 |
| 85 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +268 | 2929 |
| 86 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +266 | 1224 |
| 87 | [mattpocock/skills](https://github.com/mattpocock/skills) | +266 | 12499 |
| 88 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +264 | 13119 |
| 89 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +262 | 9738 |
| 90 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +257 | 13333 |
| 91 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +251 | 2570 |
| 92 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +249 | 32417 |
| 93 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +238 | 9429 |
| 94 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +236 | 23549 |
| 95 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +236 | 5601 |
| 96 | [jarmuine/claude-code](https://github.com/jarmuine/claude-code) | +234 | 1857 |
| 97 | [tobi/qmd](https://github.com/tobi/qmd) | +231 | 18638 |
| 98 | [maaslalani/sheets](https://github.com/maaslalani/sheets) | +228 | 1365 |
| 99 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +227 | 977 |
| 100 | [lorryjovens-hub/claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust) | +227 | 1151 |
| 101 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +227 | 21304 |
| 102 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +221 | 28235 |
| 103 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) | +218 | 966 |
| 104 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +218 | 19514 |
| 105 | [jundot/omlx](https://github.com/jundot/omlx) | +216 | 8802 |
| 106 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +216 | 1171 |
| 107 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +212 | 28561 |
| 108 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +204 | 24392 |
| 109 | [openagents-org/openagents](https://github.com/openagents-org/openagents) | +199 | 3068 |
| 110 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +192 | 1871 |
| 111 | [tanbiralam/claude-code](https://github.com/tanbiralam/claude-code) | +191 | 1293 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +189 | 28683 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +187 | 9341 |
| 114 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +187 | 1648 |
| 115 | [roboflow/supervision](https://github.com/roboflow/supervision) | +184 | 36553 |
| 116 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +183 | 9456 |
| 117 | [rushindrasinha/youtube-shorts-pipeline](https://github.com/rushindrasinha/youtube-shorts-pipeline) | +183 | 1546 |
| 118 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +178 | 38180 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +177 | 7630 |
| 120 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +176 | 969 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +22339 | 173557 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +17319 | 224760 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13840 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +13013 | 67170 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12084 | 72983 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11252 | 65384 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +10961 | 60312 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8508 | 50631 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8500 | 48594 |
| 10 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5333 | 28669 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5322 | 69674 |
| 12 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5303 | 58588 |
| 13 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4774 | 49033 |
| 14 | [anthropics/skills](https://github.com/anthropics/skills) | +4631 | 74774 |
| 15 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +4321 | 21903 |
| 16 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4291 | 27848 |
| 17 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4054 | 48380 |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3941 | 109881 |
| 19 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3625 | 34148 |
| 20 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3488 | 22016 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3473 | 32406 |
| 22 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +3307 | 45905 |
| 23 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3121 | 21304 |
| 24 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +3092 | 44621 |
| 25 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3066 | 23807 |
| 26 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2998 | 15716 |
| 27 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2967 | 46972 |
| 28 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2900 | 21236 |
| 29 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2886 | 16261 |
| 30 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2835 | 85286 |
| 31 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2806 | 27350 |
| 32 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2783 | 30590 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2773 | 18599 |
| 34 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2771 | 17398 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2687 | 39710 |
| 36 | [tanweai/pua](https://github.com/tanweai/pua) | +2654 | 15255 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2584 | 18957 |
| 38 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2574 | 24986 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2400 | 23309 |
| 40 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2366 | 13998 |
| 41 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +2321 | 23956 |
| 42 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2298 | 28561 |
| 43 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2265 | 13642 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2226 | 28235 |
| 45 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2202 | 17221 |
| 46 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2184 | 8387 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2167 | 32337 |
| 48 | [cft0808/edict](https://github.com/cft0808/edict) | +2142 | 14514 |
| 49 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2123 | 30678 |
| 50 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2110 | 19107 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2110 | 33878 |
| 52 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2094 | 12627 |
| 53 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1993 | 34840 |
| 54 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1962 | 28828 |
| 55 | [github/spec-kit](https://github.com/github/spec-kit) | +1961 | 71722 |
| 56 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +1946 | 37168 |
| 57 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1928 | 36819 |
| 58 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1925 | 29149 |
| 59 | [openai/symphony](https://github.com/openai/symphony) | +1910 | 14626 |
| 60 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1879 | 31082 |
| 61 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1865 | 60117 |
| 62 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1855 | 37330 |
| 63 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1834 | 23539 |
| 64 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1819 | 21688 |
| 65 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1795 | 12241 |
| 66 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1795 | 38180 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1760 | 37628 |
| 68 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1756 | 30320 |
| 69 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1737 | 36921 |
| 70 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1714 | 19514 |
| 71 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1712 | 12499 |
| 72 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1688 | 15730 |
| 73 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1677 | 9488 |
| 74 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1625 | 11239 |
| 75 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1615 | 19614 |
| 76 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1599 | 18661 |
| 77 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1597 | 10509 |
| 78 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1556 | 27698 |
| 79 | [openai/codex](https://github.com/openai/codex) | +1554 | 61744 |
| 80 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1534 | 37245 |
| 81 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1489 | 25417 |
| 82 | [jundot/omlx](https://github.com/jundot/omlx) | +1461 | 8802 |
| 83 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1440 | 12864 |
| 84 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1433 | 33949 |
| 85 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1421 | 9413 |
| 86 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1412 | 26671 |
| 87 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1403 | 9010 |
| 88 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1397 | 79656 |
| 89 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1384 | 16141 |
| 90 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1379 | 9581 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1370 | 10550 |
| 92 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1366 | 20382 |
| 93 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1365 | 12757 |
| 94 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1354 | 7897 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1348 | 19154 |
| 96 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1346 | 43973 |
| 97 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1344 | 11390 |
| 98 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1304 | 8504 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1231 | 78902 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1217 | 9738 |
| 101 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1214 | 14553 |
| 102 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1209 | 73135 |
| 103 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1200 | 9341 |
| 104 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1197 | 8059 |
| 105 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1194 | 8247 |
| 106 | [block/goose](https://github.com/block/goose) | +1188 | 31098 |
| 107 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1128 | 5583 |
| 108 | [openai/skills](https://github.com/openai/skills) | +1089 | 16241 |
| 109 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1055 | 52700 |
| 110 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +998 | 5156 |
| 111 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +987 | 5634 |
| 112 | [google-research/timesfm](https://github.com/google-research/timesfm) | +910 | 15153 |
| 113 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +910 | 23549 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +890 | 7630 |
| 115 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +879 | 5233 |
| 116 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +871 | 8509 |
| 117 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +853 | 35735 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +838 | 39841 |
| 119 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +826 | 45886 |
| 120 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +816 | 49621 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +811 | 23057 |
| 122 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +804 | 28683 |
| 123 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +801 | 5226 |
| 124 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +779 | 37564 |
| 125 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +753 | 29098 |
| 126 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +752 | 17485 |
| 127 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +745 | 5753 |
| 128 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +740 | 9429 |
| 129 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +738 | 4687 |
| 130 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +733 | 4478 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +731 | 36799 |
| 132 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +717 | 4066 |
| 133 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +701 | 4833 |
| 134 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +692 | 18011 |
| 135 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +677 | 24392 |
| 136 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +676 | 4366 |
| 137 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +670 | 3682 |
| 138 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +657 | 5194 |
| 139 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +653 | 4368 |
| 140 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +640 | 32417 |
| 141 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +636 | 7906 |
| 142 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +636 | 9778 |
| 143 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +634 | 9240 |
| 144 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +631 | 3539 |
| 145 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +597 | 47936 |
| 146 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +567 | 3824 |
| 147 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +567 | 2803 |
| 148 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +558 | 5601 |
| 149 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +538 | 15205 |
| 150 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +532 | 47122 |
| 151 | [wshobson/agents](https://github.com/wshobson/agents) | +532 | 33069 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +526 | 28539 |
| 153 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +520 | 44545 |
| 154 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +515 | 2936 |
| 155 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +510 | 7183 |
| 156 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +507 | 2562 |
| 157 | [eze-is/web-access](https://github.com/eze-is/web-access) | +503 | 4062 |
| 158 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +488 | 44232 |
| 159 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +478 | 18133 |
| 160 | [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | +468 | 2417 |
| 161 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +463 | 8378 |
| 162 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +462 | 2871 |
| 163 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +449 | 8347 |
| 164 | [floci-io/floci](https://github.com/floci-io/floci) | +445 | 2740 |
| 165 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +442 | 3658 |
| 166 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +442 | 24557 |
| 167 | [htdt/godogen](https://github.com/htdt/godogen) | +441 | 2599 |
| 168 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +424 | 4100 |
| 169 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +422 | 2570 |
| 170 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +419 | 2608 |
| 171 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +408 | 2002 |
| 172 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +403 | 11311 |
| 173 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +402 | 2271 |
| 174 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +398 | 2929 |
| 175 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +398 | 12422 |
| 176 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +397 | 2169 |
| 177 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +384 | 2062 |
| 178 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +368 | 2701 |
| 179 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +352 | 2202 |
| 180 | [cnlimiter/codex-manager](https://github.com/cnlimiter/codex-manager) | +346 | 1842 |
| 181 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +334 | 3660 |
| 182 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +332 | 7236 |
| 183 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +326 | 3757 |
| 184 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +324 | 6644 |
| 185 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +323 | 1623 |
| 186 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +315 | 1817 |
| 187 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +314 | 2367 |
| 188 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +310 | 10964 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +309 | 4793 |
| 190 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +304 | 10700 |
| 191 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +303 | 2929 |
| 192 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +300 | 1228 |
| 193 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +298 | 1536 |
| 194 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +287 | 33712 |
| 195 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +283 | 2502 |
| 196 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +277 | 23461 |
| 197 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +271 | 1621 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +271 | 22536 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +270 | 25311 |
| 200 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +267 | 29780 |
| 201 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +264 | 1224 |
| 202 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +264 | 1376 |
| 203 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +261 | 5084 |
| 204 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +258 | 2047 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +250 | 7434 |
| 206 | [apify/agent-skills](https://github.com/apify/agent-skills) | +245 | 1836 |
| 207 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +236 | 15120 |
| 208 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +235 | 6134 |
| 209 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +232 | 13852 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +220 | 41086 |
| 211 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +216 | 36103 |
| 212 | [decolua/9router](https://github.com/decolua/9router) | +215 | 1808 |
| 213 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +213 | 984 |
| 214 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 899 |
| 215 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +201 | 1299 |
| 216 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +188 | 2638 |
| 217 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +182 | 21870 |
| 218 | [aandrew-me/ytDownloader](https://github.com/aandrew-me/ytDownloader) | +173 | 9026 |
| 219 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +165 | 866 |
| 220 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2493 |
| 221 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +154 | 2735 |
| 222 | [es617/claude-replay](https://github.com/es617/claude-replay) | +148 | 594 |
| 223 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +143 | 3656 |
| 224 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +138 | 2449 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +136 | 29337 |
| 226 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +131 | 529 |
| 227 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +131 | 12559 |
| 228 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +130 | 40265 |
| 229 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +130 | 1154 |
| 230 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +130 | 1359 |
| 231 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +129 | 788 |
| 232 | [dashersw/gea](https://github.com/dashersw/gea) | +127 | 889 |
| 233 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +127 | 529 |
| 234 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +125 | 1118 |
| 235 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +125 | 23170 |
| 236 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +124 | 5505 |
| 237 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +122 | 769 |
| 238 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +121 | 35473 |
| 239 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +120 | 10572 |
| 240 | [is-a-dev/register](https://github.com/is-a-dev/register) | +119 | 10082 |
| 241 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +118 | 1160 |
| 242 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +115 | 597 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +113 | 26421 |
| 244 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +111 | 695 |
| 245 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +110 | 742 |
| 246 | [linlay/zenmind](https://github.com/linlay/zenmind) | +109 | 88 |
| 247 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +109 | 33000 |
| 248 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +108 | 845 |
| 249 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +108 | 2083 |
| 250 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +105 | 711 |
| 251 | [Kilted-Kraken/-RohanKar-Launcher](https://github.com/Kilted-Kraken/-RohanKar-Launcher) | +105 | 463 |
| 252 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +104 | 543 |
| 253 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +104 | 481 |
| 254 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +102 | 1770 |
| 255 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +101 | 1033 |
| 256 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +101 | 437 |
| 257 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +100 | 1259 |
| 258 | [Penty-d/qq-farm-bot-ui](https://github.com/Penty-d/qq-farm-bot-ui) | +100 | 947 |
| 259 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 550 |
| 260 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +98 | 1860 |
| 261 | [microg/GmsCore](https://github.com/microg/GmsCore) | +98 | 12830 |
| 262 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +97 | 3250 |
| 263 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +97 | 800 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +97 | 1463 |
| 265 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1106 |
| 266 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +94 | 722 |
| 267 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +94 | 1608 |
| 268 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +93 | 48784 |
| 269 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +92 | 476 |
| 270 | [robinebers/openusage](https://github.com/robinebers/openusage) | +92 | 1715 |
| 271 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +92 | 567 |
| 272 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +92 | 3429 |
| 273 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +92 | 0 |
| 274 | [idinging/freemail](https://github.com/idinging/freemail) | +91 | 1305 |
| 275 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +89 | 3809 |
| 276 | [skylot/jadx](https://github.com/skylot/jadx) | +89 | 47365 |
| 277 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +86 | 487 |
| 278 | [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | +86 | 347 |
| 279 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +86 | 411 |
| 280 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +86 | 948 |
| 281 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +83 | 516 |
| 282 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +82 | 500 |
| 283 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +81 | 2609 |
| 284 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +79 | 3534 |
| 285 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +78 | 9106 |
| 286 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +75 | 27147 |
| 287 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +74 | 11480 |
| 288 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +72 | 703 |
| 289 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +69 | 45263 |
| 290 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +68 | 367 |
| 291 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +68 | 8431 |
| 292 | [crimera/piko](https://github.com/crimera/piko) | +68 | 3052 |
| 293 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +68 | 37313 |
| 294 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +66 | 391 |
| 295 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +65 | 7189 |
| 296 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +64 | 350 |
| 297 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +64 | 31476 |
| 298 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +64 | 26662 |
| 299 | [apache/kafka](https://github.com/apache/kafka) | +61 | 32043 |
| 300 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +60 | 4632 |
