---
title: "2026-04-11 GitHub增长趋势报告"
description: "1.hermes-agent+1331 2.caveman+1110 3.awesome-design-md+501 4.multica+384 5.graphify+381"
date: 2026-04-11T20:36:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-11 20:36:48

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
        'daily': {"categories": ["Yeachan-Heo/oh-my-codex", "getpaseo/paseo", "siddharthvaddem/openscreen", "aloshdenny/reverse-SynthID", "thedotmack/claude-mem", "rtk-ai/rtk", "opendataloader-project/opendataloader-pdf", "alchaincyf/nuwa-skill", "HKUDS/DeepTutor", "QuipNetwork/quip-node-manager", "OpenBMB/VoxCPM", "addyosmani/agent-skills", "forrestchang/andrej-karpathy-skills", "coleam00/Archon", "shanraisshan/claude-code-best-practice", "safishamsi/graphify", "multica-ai/multica", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "NousResearch/hermes-agent"], "data": [115, 118, 127, 131, 155, 160, 161, 161, 175, 198, 216, 226, 241, 272, 292, 381, 384, 501, 1110, 1331]},
        'weekly': {"categories": ["abhigyanpatwari/GitNexus", "chenglou/pretext", "karpathy/autoresearch", "paperclipai/paperclip", "rtk-ai/rtk", "garrytan/gstack", "block/goose", "alchaincyf/nuwa-skill", "Yeachan-Heo/oh-my-codex", "luongnv89/claude-howto", "msitarzewski/agency-agents", "siddharthvaddem/openscreen", "obra/superpowers", "addyosmani/agent-skills", "JuliusBrussee/caveman", "affaan-m/everything-claude-code", "safishamsi/graphify", "ultraworkers/claw-code", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md"], "data": [1025, 1038, 1049, 1059, 1068, 1115, 1218, 1222, 1314, 1375, 1526, 2038, 2296, 2435, 2863, 2931, 3420, 3851, 5547, 7555]},
        'monthly': {"categories": ["anomalyco/opencode", "gsd-build/get-shit-done", "siddharthvaddem/openscreen", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "HKUDS/CLI-Anything", "anthropics/claude-code", "paperclipai/paperclip", "chenglou/pretext", "666ghj/MiroFish", "karpathy/autoresearch", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md", "msitarzewski/agency-agents", "openclaw/openclaw", "obra/superpowers", "garrytan/gstack", "affaan-m/everything-claude-code", "ultraworkers/claw-code"], "data": [3808, 3849, 3850, 4211, 4441, 4858, 4914, 5336, 5832, 6477, 6844, 8135, 8514, 8523, 9344, 10110, 11577, 12004, 13092, 23961]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1331 | 58290 |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1110 | 17965 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +501 | 43545 |
| 4 | [multica-ai/multica](https://github.com/multica-ai/multica) | +384 | 7695 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +381 | 21875 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +292 | 36916 |
| 7 | [coleam00/Archon](https://github.com/coleam00/Archon) | +272 | 16391 |
| 8 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +241 | 13217 |
| 9 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +226 | 12660 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +216 | 9755 |
| 11 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +198 | 2764 |
| 12 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +175 | 16661 |
| 13 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +161 | 7360 |
| 14 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +161 | 15532 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +160 | 23725 |
| 16 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +155 | 30678 |
| 17 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +131 | 2105 |
| 18 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +127 | 28074 |
| 19 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +118 | 1722 |
| 20 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +115 | 21050 |
| 21 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +113 | 4178 |
| 22 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +111 | 25154 |
| 23 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +109 | 12056 |
| 24 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +103 | 10223 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +98 | 42944 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +96 | 36168 |
| 27 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +93 | 22859 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +91 | 50633 |
| 29 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +81 | 26574 |
| 30 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +79 | 51709 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +7555 | 43545 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5547 | 58290 |
| 3 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +3851 | 181451 |
| 4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3420 | 21875 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2931 | 51199 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2863 | 17965 |
| 7 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2435 | 12660 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +2296 | 60312 |
| 9 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2038 | 28074 |
| 10 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1526 | 78346 |
| 11 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1375 | 25154 |
| 12 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1314 | 21050 |
| 13 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1222 | 7360 |
| 14 | [block/goose](https://github.com/block/goose) | +1218 | 31098 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1115 | 69821 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1068 | 23725 |
| 17 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1059 | 51703 |
| 18 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1049 | 70446 |
| 19 | [chenglou/pretext](https://github.com/chenglou/pretext) | +1038 | 42963 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1025 | 26574 |
| 21 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +973 | 16661 |
| 22 | [multica-ai/multica](https://github.com/multica-ai/multica) | +919 | 7695 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +914 | 74774 |
| 24 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +898 | 20417 |
| 25 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +897 | 36916 |
| 26 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +894 | 53670 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +886 | 34148 |
| 28 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +845 | 27701 |
| 29 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +801 | 13217 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +781 | 42944 |
| 31 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +726 | 26574 |
| 32 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +723 | 51709 |
| 33 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +678 | 7977 |
| 34 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +653 | 15532 |
| 35 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +611 | 22624 |
| 36 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +610 | 9005 |
| 37 | [tobi/qmd](https://github.com/tobi/qmd) | +606 | 20929 |
| 38 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +596 | 60455 |
| 39 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +594 | 34466 |
| 40 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +591 | 4178 |
| 41 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +585 | 50633 |
| 42 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +581 | 5617 |
| 43 | [farzaa/clicky](https://github.com/farzaa/clicky) | +576 | 3761 |
| 44 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +558 | 9755 |
| 45 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +558 | 3977 |
| 46 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +543 | 38014 |
| 47 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +542 | 30678 |
| 48 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +537 | 30590 |
| 49 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +537 | 4497 |
| 50 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +529 | 38687 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +514 | 33878 |
| 52 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +498 | 11060 |
| 53 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +496 | 20654 |
| 54 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +496 | 8975 |
| 55 | [jackwener/opencli](https://github.com/jackwener/opencli) | +494 | 15115 |
| 56 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +484 | 10223 |
| 57 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +451 | 25065 |
| 58 | [google-research/timesfm](https://github.com/google-research/timesfm) | +447 | 16367 |
| 59 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +436 | 18457 |
| 60 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +429 | 13588 |
| 61 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +423 | 2504 |
| 62 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +423 | 3409 |
| 63 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +422 | 30078 |
| 64 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +420 | 2764 |
| 65 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +413 | 7536 |
| 66 | [coleam00/Archon](https://github.com/coleam00/Archon) | +410 | 16391 |
| 67 | [mattpocock/skills](https://github.com/mattpocock/skills) | +405 | 14070 |
| 68 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +393 | 28663 |
| 69 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +392 | 4325 |
| 70 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +389 | 12056 |
| 71 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +389 | 4265 |
| 72 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +380 | 17000 |
| 73 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +373 | 5768 |
| 74 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +355 | 2987 |
| 75 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +354 | 31257 |
| 76 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +350 | 37330 |
| 77 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +350 | 22859 |
| 78 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +348 | 2016 |
| 79 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +346 | 2006 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +338 | 20343 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +336 | 39117 |
| 82 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +330 | 38043 |
| 83 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +329 | 32210 |
| 84 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +326 | 1779 |
| 85 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +322 | 16784 |
| 86 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +320 | 35351 |
| 87 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +313 | 2105 |
| 88 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +312 | 47813 |
| 89 | [tw93/Waza](https://github.com/tw93/Waza) | +310 | 2522 |
| 90 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +293 | 18381 |
| 91 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +288 | 45569 |
| 92 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +287 | 11767 |
| 93 | [slavingia/skills](https://github.com/slavingia/skills) | +287 | 7695 |
| 94 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +282 | 36168 |
| 95 | [hotcoffeeshake/tong-jincheng-skill](https://github.com/hotcoffeeshake/tong-jincheng-skill) | +268 | 1557 |
| 96 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +265 | 7397 |
| 97 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +260 | 2786 |
| 98 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +254 | 20344 |
| 99 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +246 | 8925 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +244 | 10522 |
| 101 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +238 | 1805 |
| 102 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +236 | 29332 |
| 103 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +236 | 45886 |
| 104 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +234 | 4279 |
| 105 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +232 | 15113 |
| 106 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +228 | 39075 |
| 107 | [jundot/omlx](https://github.com/jundot/omlx) | +224 | 9516 |
| 108 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +218 | 22040 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +217 | 10104 |
| 110 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +208 | 1288 |
| 111 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | +205 | 9329 |
| 112 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +204 | 24984 |
| 113 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +195 | 29190 |
| 114 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +194 | 32935 |
| 115 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +192 | 4977 |
| 116 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +182 | 2388 |
| 117 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +177 | 38109 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +177 | 39841 |
| 119 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +175 | 1660 |
| 120 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +174 | 29336 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +23961 | 181451 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13092 | 51199 |
| 3 | [garrytan/gstack](https://github.com/garrytan/gstack) | +12004 | 69821 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +11577 | 60312 |
| 5 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +10110 | 224760 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +9344 | 78346 |
| 7 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +8523 | 43545 |
| 8 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +8514 | 58291 |
| 9 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +8135 | 70446 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6844 | 53670 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6477 | 42963 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5832 | 51703 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5336 | 69674 |
| 14 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4914 | 30078 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4858 | 60455 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4441 | 51709 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +4211 | 74774 |
| 18 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3850 | 28074 |
| 19 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3849 | 50633 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3808 | 109881 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3789 | 36916 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3701 | 34148 |
| 23 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3623 | 22800 |
| 24 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3607 | 25154 |
| 25 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3421 | 21875 |
| 26 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3380 | 21050 |
| 27 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3069 | 22040 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3010 | 30590 |
| 29 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2984 | 28423 |
| 30 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2864 | 17965 |
| 31 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2864 | 27701 |
| 32 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2840 | 18961 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2798 | 42944 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2732 | 85286 |
| 35 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2680 | 26574 |
| 36 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2650 | 23725 |
| 37 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2569 | 15115 |
| 38 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2536 | 15113 |
| 39 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2482 | 12660 |
| 40 | [tanweai/pua](https://github.com/tanweai/pua) | +2477 | 15837 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2467 | 18457 |
| 42 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2462 | 16784 |
| 43 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2372 | 29190 |
| 44 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2340 | 20654 |
| 45 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2325 | 18381 |
| 46 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2268 | 30678 |
| 47 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2223 | 38687 |
| 48 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2210 | 15532 |
| 49 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2189 | 47813 |
| 50 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2107 | 34466 |
| 51 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2058 | 13588 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2032 | 33878 |
| 53 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1977 | 46403 |
| 54 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1972 | 14070 |
| 55 | [github/spec-kit](https://github.com/github/spec-kit) | +1941 | 71722 |
| 56 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1885 | 45569 |
| 57 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1851 | 29332 |
| 58 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1780 | 20344 |
| 59 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1711 | 38043 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1709 | 25065 |
| 61 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1698 | 10948 |
| 62 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1692 | 26574 |
| 63 | [block/goose](https://github.com/block/goose) | +1690 | 31098 |
| 64 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1683 | 29684 |
| 65 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1673 | 37330 |
| 66 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1669 | 31257 |
| 67 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1664 | 38109 |
| 68 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1644 | 39117 |
| 69 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1642 | 8975 |
| 70 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1604 | 22624 |
| 71 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1594 | 60117 |
| 72 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1561 | 10223 |
| 73 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1545 | 10032 |
| 74 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1539 | 32210 |
| 75 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1490 | 79656 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1489 | 61744 |
| 77 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1485 | 13427 |
| 78 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1476 | 17000 |
| 79 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1471 | 19033 |
| 80 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1451 | 12809 |
| 81 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1437 | 13661 |
| 82 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1432 | 9852 |
| 83 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1423 | 22859 |
| 84 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1414 | 28663 |
| 85 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1391 | 8137 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1389 | 98536 |
| 87 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1388 | 11564 |
| 88 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1370 | 35351 |
| 89 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1343 | 7977 |
| 90 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1338 | 16672 |
| 91 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1336 | 8699 |
| 92 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1323 | 73135 |
| 93 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1309 | 6664 |
| 94 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1307 | 7536 |
| 95 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1297 | 36168 |
| 96 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1284 | 20343 |
| 97 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1275 | 39075 |
| 98 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1257 | 8640 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1251 | 78902 |
| 100 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1223 | 7360 |
| 101 | [cft0808/edict](https://github.com/cft0808/edict) | +1217 | 14896 |
| 102 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1213 | 52700 |
| 103 | [jundot/omlx](https://github.com/jundot/omlx) | +1151 | 9516 |
| 104 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1131 | 16367 |
| 105 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1115 | 5617 |
| 106 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1115 | 7695 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1067 | 6183 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1046 | 10522 |
| 109 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1045 | 16661 |
| 110 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1044 | 20417 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +1044 | 8925 |
| 112 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1004 | 43973 |
| 113 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +986 | 27121 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +944 | 10104 |
| 115 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +911 | 8771 |
| 116 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +905 | 5797 |
| 117 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +899 | 23862 |
| 118 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +868 | 49621 |
| 119 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +860 | 39841 |
| 120 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +845 | 15042 |
| 121 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +822 | 6109 |
| 122 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +789 | 23424 |
| 123 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +781 | 10164 |
| 124 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +780 | 9598 |
| 125 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +774 | 4977 |
| 126 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +769 | 4688 |
| 127 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +752 | 29336 |
| 128 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +741 | 4265 |
| 129 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +735 | 4263 |
| 130 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +714 | 5450 |
| 131 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +711 | 37564 |
| 132 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +695 | 29253 |
| 133 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +680 | 32935 |
| 134 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +678 | 36799 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +673 | 9454 |
| 136 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +658 | 9005 |
| 137 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +653 | 24984 |
| 138 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +640 | 18135 |
| 139 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +639 | 45886 |
| 140 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +635 | 4775 |
| 141 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +619 | 4817 |
| 142 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +605 | 47936 |
| 143 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +605 | 3366 |
| 144 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +597 | 5810 |
| 145 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +597 | 3793 |
| 146 | [eze-is/web-access](https://github.com/eze-is/web-access) | +596 | 4595 |
| 147 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +587 | 9756 |
| 148 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +577 | 2987 |
| 149 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +573 | 2981 |
| 150 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +557 | 18485 |
| 151 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +532 | 15809 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +513 | 28980 |
| 153 | [floci-io/floci](https://github.com/floci-io/floci) | +511 | 3224 |
| 154 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +509 | 2299 |
| 155 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +507 | 2732 |
| 156 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +502 | 11060 |
| 157 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +502 | 5192 |
| 158 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +501 | 44545 |
| 159 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +497 | 7357 |
| 160 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +492 | 2786 |
| 161 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +489 | 8523 |
| 162 | [openai/skills](https://github.com/openai/skills) | +474 | 16617 |
| 163 | [htdt/godogen](https://github.com/htdt/godogen) | +464 | 2749 |
| 164 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +461 | 3782 |
| 165 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +458 | 2852 |
| 166 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +457 | 18528 |
| 167 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +455 | 44232 |
| 168 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +449 | 4279 |
| 169 | [wshobson/agents](https://github.com/wshobson/agents) | +448 | 33402 |
| 170 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +445 | 3112 |
| 171 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +441 | 4535 |
| 172 | [coleam00/Archon](https://github.com/coleam00/Archon) | +439 | 16391 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +426 | 8592 |
| 174 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +422 | 2809 |
| 175 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +420 | 1779 |
| 176 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +413 | 2388 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +387 | 24904 |
| 178 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +381 | 2335 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +379 | 2743 |
| 180 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +375 | 11661 |
| 181 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +357 | 2577 |
| 182 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +331 | 1754 |
| 183 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +329 | 1654 |
| 184 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +320 | 2105 |
| 185 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +316 | 3001 |
| 186 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +312 | 1651 |
| 187 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +311 | 5044 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +295 | 2751 |
| 189 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +291 | 2301 |
| 190 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +288 | 23010 |
| 191 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +286 | 4349 |
| 192 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +281 | 6798 |
| 193 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +281 | 1713 |
| 194 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +277 | 9643 |
| 195 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +273 | 10926 |
| 196 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +271 | 6226 |
| 197 | [decolua/9router](https://github.com/decolua/9router) | +262 | 2278 |
| 198 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +256 | 1064 |
| 199 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +242 | 5288 |
| 200 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +235 | 23559 |
| 201 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +233 | 25537 |
| 202 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +225 | 6253 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +220 | 13963 |
| 204 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +207 | 36103 |
| 205 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +206 | 1901 |
| 206 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +206 | 15351 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 921 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +202 | 41086 |
| 209 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +197 | 33712 |
| 210 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +196 | 2199 |
| 211 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +191 | 2669 |
| 212 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +178 | 1288 |
| 213 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +175 | 909 |
| 214 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +172 | 1415 |
| 215 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +169 | 2875 |
| 216 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +162 | 3689 |
| 217 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +160 | 959 |
| 218 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +153 | 21997 |
| 219 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +144 | 3768 |
| 220 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +143 | 734 |
| 221 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +141 | 1284 |
| 222 | [dashersw/gea](https://github.com/dashersw/gea) | +136 | 947 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +135 | 35473 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +135 | 29482 |
| 225 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +128 | 544 |
| 226 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +127 | 844 |
| 227 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +126 | 808 |
| 228 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +126 | 2541 |
| 229 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +125 | 10657 |
| 230 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +124 | 29474 |
| 231 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +121 | 1244 |
| 232 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +120 | 40265 |
| 233 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +118 | 779 |
| 234 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +117 | 599 |
| 235 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +117 | 23252 |
| 236 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +115 | 12667 |
| 237 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +113 | 750 |
| 238 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +112 | 33000 |
| 239 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +111 | 1187 |
| 240 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +110 | 1094 |
| 241 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +108 | 1065 |
| 242 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +108 | 26497 |
| 243 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 244 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +107 | 493 |
| 245 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +105 | 846 |
| 246 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +105 | 1465 |
| 247 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +103 | 48784 |
| 248 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 557 |
| 249 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +97 | 1655 |
| 250 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 251 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +96 | 2113 |
| 252 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +96 | 1686 |
| 253 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +93 | 490 |
| 254 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3867 |
| 255 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +92 | 1119 |
| 256 | [microg/GmsCore](https://github.com/microg/GmsCore) | +88 | 12893 |
| 257 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +87 | 3495 |
| 258 | [idinging/freemail](https://github.com/idinging/freemail) | +85 | 1335 |
| 259 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +85 | 1847 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +85 | 1529 |
| 261 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +84 | 481 |
| 262 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +84 | 1820 |
| 263 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +83 | 1019 |
| 264 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +83 | 524 |
| 265 | [meodai/heerich](https://github.com/meodai/heerich) | +79 | 464 |
| 266 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +79 | 924 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +78 | 3611 |
| 268 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +78 | 646 |
| 269 | [clawplays/ospec](https://github.com/clawplays/ospec) | +77 | 384 |
| 270 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +77 | 525 |
| 271 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +77 | 732 |
| 272 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +75 | 2678 |
| 273 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +74 | 9174 |
| 274 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +73 | 448 |
| 275 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +73 | 11556 |
| 276 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +71 | 8479 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +71 | 27178 |
| 278 | [crimera/piko](https://github.com/crimera/piko) | +70 | 3124 |
| 279 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +68 | 708 |
| 280 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +68 | 491 |
| 281 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +67 | 412 |
| 282 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 283 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +66 | 313 |
| 284 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +63 | 531 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +63 | 7226 |
| 286 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +62 | 411 |
| 287 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +62 | 392 |
| 288 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1539 |
| 289 | [openmemind/memind](https://github.com/openmemind/memind) | +59 | 363 |
| 290 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +59 | 31476 |
| 291 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +58 | 25389 |
| 292 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +58 | 7795 |
| 293 | [apache/kafka](https://github.com/apache/kafka) | +56 | 32043 |
| 294 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +55 | 284 |
| 295 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11625 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +54 | 1655 |
| 297 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +54 | 4654 |
| 298 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +51 | 26685 |
| 299 | [risin42/NagramX](https://github.com/risin42/NagramX) | +49 | 1667 |
| 300 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +48 | 1716 |
