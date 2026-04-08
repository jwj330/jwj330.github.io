---
title: "2026-04-08 GitHub增长趋势报告"
description: "1.awesome-design-md+1130 2.hermes-agent+924 3.graphify+837 4.caveman+285 5.agent-skills+232"
date: 2026-04-08T20:46:37+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-08 20:46:37

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
        'daily': {"categories": ["paperclipai/paperclip", "OpenCloudGaming/OpenNOW", "chenglou/pretext", "rtk-ai/rtk", "shareAI-lab/learn-claude-code", "block/goose", "siddharthvaddem/openscreen", "tobi/qmd", "Yeachan-Heo/oh-my-codex", "google-ai-edge/gallery", "luongnv89/claude-howto", "HughYau/qiushi-skill", "abhigyanpatwari/GitNexus", "tirth8205/code-review-graph", "HKUDS/DeepTutor", "addyosmani/agent-skills", "JuliusBrussee/caveman", "safishamsi/graphify", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md"], "data": [106, 111, 114, 116, 122, 124, 131, 132, 148, 149, 152, 160, 177, 177, 198, 232, 285, 837, 924, 1130]},
        'weekly': {"categories": ["Yeachan-Heo/oh-my-claudecode", "block/goose", "onyx-dot-app/onyx", "JuliusBrussee/caveman", "ultraworkers/claw-code-parity", "garrytan/gstack", "paperclipai/paperclip", "msitarzewski/agency-agents", "safishamsi/graphify", "luongnv89/claude-howto", "addyosmani/agent-skills", "obra/superpowers", "Yeachan-Heo/oh-my-codex", "chenglou/pretext", "anthropics/claude-code", "NousResearch/hermes-agent", "siddharthvaddem/openscreen", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "ultraworkers/claw-code"], "data": [1201, 1261, 1264, 1278, 1298, 1314, 1328, 1555, 1567, 1639, 1927, 2187, 2372, 2469, 2541, 2649, 2948, 3369, 6930, 14934]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "anomalyco/opencode", "gsd-build/get-shit-done", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "anthropics/claude-code", "HKUDS/CLI-Anything", "NousResearch/hermes-agent", "chenglou/pretext", "VoltAgent/awesome-design-md", "paperclipai/paperclip", "666ghj/MiroFish", "obra/superpowers", "garrytan/gstack", "karpathy/autoresearch", "msitarzewski/agency-agents", "affaan-m/everything-claude-code", "openclaw/openclaw", "ultraworkers/claw-code"], "data": [3725, 3882, 3953, 4466, 4563, 5219, 5355, 5469, 5491, 6272, 6935, 7303, 8306, 11235, 11591, 11720, 11939, 13391, 14832, 23307]}
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
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1130 | 34523 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +924 | 37024 |
| 3 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +837 | 12154 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +285 | 7326 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +232 | 9199 |
| 6 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +198 | 13376 |
| 7 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +177 | 6660 |
| 8 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +177 | 25221 |
| 9 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +160 | 1407 |
| 10 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +152 | 23189 |
| 11 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +149 | 19432 |
| 12 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +148 | 19006 |
| 13 | [tobi/qmd](https://github.com/tobi/qmd) | +132 | 20037 |
| 14 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +131 | 26018 |
| 15 | [block/goose](https://github.com/block/goose) | +124 | 31098 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +122 | 50245 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +116 | 20672 |
| 18 | [chenglou/pretext](https://github.com/chenglou/pretext) | +114 | 41759 |
| 19 | [OpenCloudGaming/OpenNOW](https://github.com/OpenCloudGaming/OpenNOW) | +111 | 1638 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +106 | 49970 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +106 | 41077 |
| 22 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +104 | 12580 |
| 23 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +102 | 37647 |
| 24 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +100 | 1455 |
| 25 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +100 | 3484 |
| 26 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +99 | 1733 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +96 | 9098 |
| 28 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +95 | 8842 |
| 29 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +95 | 2942 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +94 | 49423 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +14934 | 178156 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +6930 | 34523 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3369 | 51199 |
| 4 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2948 | 26018 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2649 | 37024 |
| 6 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2541 | 69674 |
| 7 | [chenglou/pretext](https://github.com/chenglou/pretext) | +2469 | 41759 |
| 8 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2372 | 19006 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | +2187 | 60312 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1927 | 9199 |
| 11 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1639 | 23189 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1567 | 12154 |
| 13 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1555 | 75740 |
| 14 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1328 | 49970 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1314 | 67278 |
| 16 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1298 | 6624 |
| 17 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1278 | 7326 |
| 18 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1264 | 26027 |
| 19 | [block/goose](https://github.com/block/goose) | +1261 | 31098 |
| 20 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1201 | 26267 |
| 21 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1108 | 68766 |
| 22 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1089 | 12925 |
| 23 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +958 | 5396 |
| 24 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +950 | 73135 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +937 | 74774 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +936 | 34148 |
| 27 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +883 | 51913 |
| 28 | [jackwener/opencli](https://github.com/jackwener/opencli) | +867 | 14390 |
| 29 | [google-research/timesfm](https://github.com/google-research/timesfm) | +834 | 15636 |
| 30 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +823 | 25221 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +788 | 41077 |
| 32 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +787 | 20672 |
| 33 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +777 | 19432 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +774 | 50245 |
| 35 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +762 | 3800 |
| 36 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +761 | 33878 |
| 37 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +758 | 59537 |
| 38 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +709 | 37621 |
| 39 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +648 | 29412 |
| 40 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +631 | 30590 |
| 41 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +630 | 33280 |
| 42 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +628 | 5540 |
| 43 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +593 | 33054 |
| 44 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +590 | 21735 |
| 45 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +590 | 49423 |
| 46 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +583 | 3689 |
| 47 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +549 | 6660 |
| 48 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +539 | 19707 |
| 49 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +519 | 32872 |
| 50 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +517 | 3697 |
| 51 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +513 | 37647 |
| 52 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +497 | 5326 |
| 53 | [tobi/qmd](https://github.com/tobi/qmd) | +496 | 20037 |
| 54 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +494 | 8364 |
| 55 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +494 | 2457 |
| 56 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +465 | 28183 |
| 57 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +460 | 30678 |
| 58 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +454 | 24159 |
| 59 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +421 | 9098 |
| 60 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +421 | 16480 |
| 61 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +414 | 37330 |
| 62 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +393 | 37507 |
| 63 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +384 | 4194 |
| 64 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +376 | 2014 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +375 | 38318 |
| 66 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +373 | 2942 |
| 67 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +371 | 10423 |
| 68 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +368 | 3873 |
| 69 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +366 | 31595 |
| 70 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +365 | 13376 |
| 71 | [mattpocock/skills](https://github.com/mattpocock/skills) | +365 | 13147 |
| 72 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +360 | 17731 |
| 73 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +353 | 30766 |
| 74 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +353 | 1403 |
| 75 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +348 | 47369 |
| 76 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +325 | 2415 |
| 77 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +324 | 8648 |
| 78 | [maaslalani/sheets](https://github.com/maaslalani/sheets) | +322 | 1632 |
| 79 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +320 | 34604 |
| 80 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +317 | 17280 |
| 81 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +303 | 1875 |
| 82 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +301 | 22052 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +299 | 19684 |
| 84 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +296 | 16386 |
| 85 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +296 | 11509 |
| 86 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +294 | 1418 |
| 87 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +293 | 45043 |
| 88 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +292 | 1667 |
| 89 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +289 | 4739 |
| 90 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) | +288 | 1361 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +287 | 10064 |
| 92 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +286 | 1733 |
| 93 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +285 | 5915 |
| 94 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +283 | 19952 |
| 95 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +282 | 5058 |
| 96 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +276 | 1235 |
| 97 | [xandemon/developer-icons](https://github.com/xandemon/developer-icons) | +274 | 1907 |
| 98 | [chauncygu/collection-claude-code-source-code](https://github.com/chauncygu/collection-claude-code-source-code) | +272 | 1870 |
| 99 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +268 | 32680 |
| 100 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +263 | 1478 |
| 101 | [memvid/memvid](https://github.com/memvid/memvid) | +255 | 14735 |
| 102 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +237 | 21656 |
| 103 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +233 | 24646 |
| 104 | [jundot/omlx](https://github.com/jundot/omlx) | +229 | 9135 |
| 105 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +229 | 23693 |
| 106 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +228 | 1455 |
| 107 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +228 | 1230 |
| 108 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +226 | 28627 |
| 109 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +223 | 28855 |
| 110 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +222 | 2731 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +210 | 8514 |
| 112 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +206 | 38570 |
| 113 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | +206 | 9153 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +204 | 9571 |
| 115 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +199 | 9677 |
| 116 | [roboflow/supervision](https://github.com/roboflow/supervision) | +199 | 36553 |
| 117 | [Pika-Labs/Pika-Skills](https://github.com/Pika-Labs/Pika-Skills) | +195 | 932 |
| 118 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +192 | 28962 |
| 119 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +188 | 3045 |
| 120 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +188 | 35068 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +23307 | 178156 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +14832 | 224760 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13391 | 51199 |
| 4 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +11939 | 75740 |
| 5 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +11720 | 68766 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11591 | 67278 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +11235 | 60312 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8306 | 51913 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +7303 | 49970 |
| 10 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +6935 | 34523 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6272 | 41759 |
| 12 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5491 | 37024 |
| 13 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5469 | 29412 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5355 | 69674 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5219 | 59537 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4563 | 50245 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +4466 | 74774 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3953 | 49423 |
| 19 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3882 | 109881 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3725 | 34148 |
| 21 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3548 | 22403 |
| 22 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3487 | 26018 |
| 23 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3334 | 33054 |
| 24 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3262 | 23189 |
| 25 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3120 | 21656 |
| 26 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3037 | 19006 |
| 27 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2964 | 46091 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2903 | 30590 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2874 | 16386 |
| 30 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2860 | 27691 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2831 | 17280 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2830 | 85286 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2802 | 18776 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2730 | 41077 |
| 35 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2727 | 26267 |
| 36 | [tanweai/pua](https://github.com/tanweai/pua) | +2706 | 15539 |
| 37 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2613 | 25221 |
| 38 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +2592 | 45043 |
| 39 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2573 | 47369 |
| 40 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2517 | 20672 |
| 41 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2447 | 14550 |
| 42 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2425 | 14390 |
| 43 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2323 | 28855 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2259 | 17731 |
| 45 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2200 | 19707 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2150 | 33281 |
| 47 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2137 | 30678 |
| 48 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2107 | 33878 |
| 49 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2064 | 37621 |
| 50 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2019 | 28627 |
| 51 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1994 | 12732 |
| 52 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1951 | 12925 |
| 53 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1942 | 9199 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1940 | 71722 |
| 55 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1839 | 29369 |
| 56 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1829 | 13147 |
| 57 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1798 | 37330 |
| 58 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1791 | 24159 |
| 59 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1787 | 19952 |
| 60 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1740 | 37507 |
| 61 | [cft0808/edict](https://github.com/cft0808/edict) | +1724 | 14710 |
| 62 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1720 | 31595 |
| 63 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1711 | 12581 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1709 | 38318 |
| 65 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1697 | 30766 |
| 66 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1682 | 22052 |
| 67 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1681 | 35068 |
| 68 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1671 | 9543 |
| 69 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1644 | 10784 |
| 70 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1629 | 16480 |
| 71 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1613 | 60117 |
| 72 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1608 | 37857 |
| 73 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1597 | 38570 |
| 74 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1594 | 26027 |
| 75 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1588 | 29027 |
| 76 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1568 | 12154 |
| 77 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1562 | 21735 |
| 78 | [openai/codex](https://github.com/openai/codex) | +1526 | 61744 |
| 79 | [jundot/omlx](https://github.com/jundot/omlx) | +1520 | 9135 |
| 80 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1514 | 28183 |
| 81 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1505 | 18840 |
| 82 | [block/goose](https://github.com/block/goose) | +1503 | 31098 |
| 83 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1466 | 79656 |
| 84 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1466 | 9654 |
| 85 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1437 | 13222 |
| 86 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1426 | 34604 |
| 87 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1423 | 13090 |
| 88 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1408 | 9716 |
| 89 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1393 | 9098 |
| 90 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1377 | 11509 |
| 91 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1371 | 98536 |
| 92 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1367 | 7996 |
| 93 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1349 | 11029 |
| 94 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1349 | 16352 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1326 | 19684 |
| 96 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1317 | 8588 |
| 97 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1298 | 6624 |
| 98 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1297 | 43973 |
| 99 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1280 | 7326 |
| 100 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1280 | 73135 |
| 101 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1241 | 26901 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1240 | 78902 |
| 103 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1227 | 8420 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1226 | 10064 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1136 | 9571 |
| 106 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1124 | 6660 |
| 107 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1110 | 52700 |
| 108 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1074 | 5396 |
| 109 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1066 | 14851 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1037 | 5859 |
| 111 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1002 | 15636 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +938 | 8514 |
| 113 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +898 | 23693 |
| 114 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +892 | 8648 |
| 115 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +866 | 5540 |
| 116 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +844 | 49621 |
| 117 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +841 | 39841 |
| 118 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +787 | 35735 |
| 119 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +786 | 23182 |
| 120 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +783 | 28962 |
| 121 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +781 | 5915 |
| 122 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +757 | 37564 |
| 123 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +754 | 29164 |
| 124 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +752 | 4579 |
| 125 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +750 | 45886 |
| 126 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +745 | 9677 |
| 127 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +736 | 4745 |
| 128 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +732 | 4739 |
| 129 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +723 | 4140 |
| 130 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +711 | 17712 |
| 131 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +699 | 4905 |
| 132 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +693 | 36799 |
| 133 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +689 | 5326 |
| 134 | [openai/skills](https://github.com/openai/skills) | +673 | 16412 |
| 135 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +673 | 3726 |
| 136 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +669 | 32680 |
| 137 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +665 | 24646 |
| 138 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +649 | 9318 |
| 139 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +644 | 3689 |
| 140 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +638 | 3565 |
| 141 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +634 | 18235 |
| 142 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +632 | 4506 |
| 143 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +590 | 47936 |
| 144 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +584 | 5722 |
| 145 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +572 | 2823 |
| 146 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +548 | 15449 |
| 147 | [eze-is/web-access](https://github.com/eze-is/web-access) | +546 | 4356 |
| 148 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +541 | 8364 |
| 149 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +538 | 2790 |
| 150 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +537 | 9841 |
| 151 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +529 | 47122 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +522 | 28722 |
| 153 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +505 | 8004 |
| 154 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +504 | 7244 |
| 155 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +502 | 44545 |
| 156 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +493 | 2457 |
| 157 | [floci-io/floci](https://github.com/floci-io/floci) | +491 | 3008 |
| 158 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +489 | 44232 |
| 159 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +485 | 3016 |
| 160 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +478 | 8442 |
| 161 | [wshobson/agents](https://github.com/wshobson/agents) | +470 | 33181 |
| 162 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +467 | 18323 |
| 163 | [htdt/godogen](https://github.com/htdt/godogen) | +451 | 2659 |
| 164 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +447 | 3685 |
| 165 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +446 | 8475 |
| 166 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +442 | 13376 |
| 167 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +441 | 2731 |
| 168 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +441 | 4194 |
| 169 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +438 | 2308 |
| 170 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +434 | 3045 |
| 171 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +426 | 24722 |
| 172 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +424 | 2695 |
| 173 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +388 | 11493 |
| 174 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +381 | 4047 |
| 175 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +376 | 10423 |
| 176 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +371 | 2722 |
| 177 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +368 | 2272 |
| 178 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +355 | 1403 |
| 179 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +354 | 2249 |
| 180 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +342 | 1962 |
| 181 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +338 | 2468 |
| 182 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +326 | 1935 |
| 183 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +321 | 1668 |
| 184 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +319 | 1667 |
| 185 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +310 | 4895 |
| 186 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +307 | 2960 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +304 | 11067 |
| 188 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +300 | 6714 |
| 189 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +299 | 1418 |
| 190 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +296 | 2580 |
| 191 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +296 | 10809 |
| 192 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +280 | 29780 |
| 193 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +272 | 1486 |
| 194 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +271 | 22715 |
| 195 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +261 | 3672 |
| 196 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +260 | 5180 |
| 197 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +259 | 7538 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +252 | 25414 |
| 199 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +249 | 23509 |
| 200 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +238 | 6190 |
| 201 | [decolua/9router](https://github.com/decolua/9router) | +233 | 2013 |
| 202 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +233 | 33712 |
| 203 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +230 | 2094 |
| 204 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +223 | 13896 |
| 205 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +222 | 36103 |
| 206 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +222 | 1056 |
| 207 | [usebruno/bruno](https://github.com/usebruno/bruno) | +220 | 41086 |
| 208 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +219 | 15203 |
| 209 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 910 |
| 210 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +196 | 3822 |
| 211 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +190 | 2646 |
| 212 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +173 | 1348 |
| 213 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +169 | 888 |
| 214 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +162 | 2808 |
| 215 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +161 | 3484 |
| 216 | [apify/agent-skills](https://github.com/apify/agent-skills) | +157 | 1871 |
| 217 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +153 | 21924 |
| 218 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +149 | 2495 |
| 219 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +145 | 3711 |
| 220 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +145 | 891 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +140 | 2497 |
| 222 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +136 | 1189 |
| 223 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +136 | 29378 |
| 224 | [dashersw/gea](https://github.com/dashersw/gea) | +133 | 926 |
| 225 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +132 | 35473 |
| 226 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +130 | 1237 |
| 227 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +127 | 640 |
| 228 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +127 | 533 |
| 229 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +126 | 1377 |
| 230 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +124 | 795 |
| 231 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +123 | 10604 |
| 232 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +120 | 12612 |
| 233 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +120 | 23204 |
| 234 | [is-a-dev/register](https://github.com/is-a-dev/register) | +118 | 10098 |
| 235 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +117 | 602 |
| 236 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +117 | 5542 |
| 237 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +115 | 762 |
| 238 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +115 | 33000 |
| 239 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +114 | 721 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +110 | 26448 |
| 241 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +109 | 746 |
| 242 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +106 | 1054 |
| 243 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +105 | 485 |
| 244 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +102 | 1142 |
| 245 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +101 | 1300 |
| 246 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +101 | 1119 |
| 247 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +101 | 2090 |
| 248 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +100 | 3267 |
| 249 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +100 | 819 |
| 250 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +99 | 574 |
| 251 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 553 |
| 252 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +99 | 48784 |
| 253 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +97 | 1878 |
| 254 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 516 |
| 255 | [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | +95 | 368 |
| 256 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +95 | 1787 |
| 257 | [idinging/freemail](https://github.com/idinging/freemail) | +93 | 1319 |
| 258 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +93 | 421 |
| 259 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +93 | 879 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +93 | 1625 |
| 261 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +92 | 484 |
| 262 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 1492 |
| 263 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +90 | 3464 |
| 264 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +89 | 3838 |
| 265 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +87 | 1594 |
| 266 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +87 | 976 |
| 267 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +86 | 762 |
| 268 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +86 | 537 |
| 269 | [microg/GmsCore](https://github.com/microg/GmsCore) | +86 | 12863 |
| 270 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +82 | 3569 |
| 271 | [zmeyer44/Locker](https://github.com/zmeyer44/Locker) | +79 | 540 |
| 272 | [meodai/heerich](https://github.com/meodai/heerich) | +79 | 450 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +79 | 11516 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +78 | 9143 |
| 275 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +76 | 438 |
| 276 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +76 | 1799 |
| 277 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +76 | 2638 |
| 278 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +75 | 530 |
| 279 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +75 | 720 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +73 | 27158 |
| 281 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +70 | 8450 |
| 282 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +70 | 0 |
| 283 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +68 | 482 |
| 284 | [crimera/piko](https://github.com/crimera/piko) | +68 | 3078 |
| 285 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +67 | 399 |
| 286 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 287 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7204 |
| 288 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +64 | 353 |
| 289 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +64 | 516 |
| 290 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +64 | 37313 |
| 291 | [apache/kafka](https://github.com/apache/kafka) | +63 | 32043 |
| 292 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +61 | 4644 |
| 293 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +60 | 262 |
| 294 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +60 | 384 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1505 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +60 | 31476 |
| 297 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +58 | 390 |
| 298 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11611 |
| 299 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +55 | 1628 |
| 300 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +51 | 266 |
