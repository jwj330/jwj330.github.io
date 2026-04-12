---
title: "2026-04-12 GitHub增长趋势报告"
description: "1.hermes-agent+2170 2.caveman+1266 3.andrej-karpathy-skills+619 4.awesome-design-md+567 5.multica+559"
date: 2026-04-12T20:39:35+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-12 20:39:35

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
        'daily': {"categories": ["siddharthvaddem/openscreen", "thedotmack/claude-mem", "coleam00/Archon", "GetBindu/Bindu", "JCodesMore/ai-website-cloner-template", "tirth8205/code-review-graph", "opendataloader-project/opendataloader-pdf", "addyosmani/agent-skills", "HKUDS/DeepTutor", "rtk-ai/rtk", "OpenBMB/VoxCPM", "alchaincyf/nuwa-skill", "shanraisshan/claude-code-best-practice", "safishamsi/graphify", "alchaincyf/zhangxuefeng-skill", "multica-ai/multica", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "JuliusBrussee/caveman", "NousResearch/hermes-agent"], "data": [186, 187, 192, 197, 197, 199, 226, 226, 243, 311, 322, 323, 431, 519, 546, 559, 567, 619, 1266, 2170]},
        'weekly': {"categories": ["Yeachan-Heo/oh-my-codex", "garrytan/gstack", "HKUDS/DeepTutor", "alchaincyf/zhangxuefeng-skill", "luongnv89/claude-howto", "rtk-ai/rtk", "shanraisshan/claude-code-best-practice", "forrestchang/andrej-karpathy-skills", "msitarzewski/agency-agents", "multica-ai/multica", "alchaincyf/nuwa-skill", "siddharthvaddem/openscreen", "addyosmani/agent-skills", "obra/superpowers", "affaan-m/everything-claude-code", "ultraworkers/claw-code", "safishamsi/graphify", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent"], "data": [1109, 1132, 1133, 1133, 1159, 1193, 1231, 1397, 1430, 1448, 1524, 1578, 2093, 2349, 2734, 2881, 3925, 4050, 6933, 7317]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "JuliusBrussee/caveman", "anthropics/skills", "shanraisshan/claude-code-best-practice", "HKUDS/CLI-Anything", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "anthropics/claude-code", "paperclipai/paperclip", "chenglou/pretext", "666ghj/MiroFish", "karpathy/autoresearch", "msitarzewski/agency-agents", "VoltAgent/awesome-design-md", "openclaw/openclaw", "NousResearch/hermes-agent", "obra/superpowers", "garrytan/gstack", "affaan-m/everything-claude-code", "ultraworkers/claw-code"], "data": [4035, 4068, 4143, 4159, 4375, 4490, 4825, 5354, 5559, 6539, 6641, 7764, 8728, 9046, 9559, 10410, 11654, 12207, 13184, 24203]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2170 | 65659 |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1266 | 21264 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +619 | 15981 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +567 | 45442 |
| 5 | [multica-ai/multica](https://github.com/multica-ai/multica) | +559 | 9211 |
| 6 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +546 | 5268 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +519 | 23410 |
| 8 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +431 | 38785 |
| 9 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +323 | 8436 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +322 | 11132 |
| 11 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +311 | 24441 |
| 12 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +243 | 17191 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +226 | 13532 |
| 14 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +226 | 16068 |
| 15 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +199 | 8877 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +197 | 10768 |
| 17 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +197 | 4211 |
| 18 | [coleam00/Archon](https://github.com/coleam00/Archon) | +192 | 16955 |
| 19 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +187 | 30678 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +186 | 28726 |
| 21 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +180 | 45886 |
| 22 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +167 | 2163 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +163 | 21582 |
| 24 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +161 | 3171 |
| 25 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +156 | 51240 |
| 26 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +134 | 43397 |
| 27 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +130 | 25587 |
| 28 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +118 | 2082 |
| 29 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | +117 | 7792 |
| 30 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +115 | 15312 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7317 | 65660 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +6933 | 45442 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4050 | 21264 |
| 4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3925 | 23410 |
| 5 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2881 | 182383 |
| 6 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2734 | 51199 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2349 | 60312 |
| 8 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2093 | 13532 |
| 9 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1578 | 28726 |
| 10 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1524 | 8436 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1448 | 9211 |
| 12 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1430 | 78818 |
| 13 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1397 | 15982 |
| 14 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1231 | 38785 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1193 | 24441 |
| 16 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1159 | 25587 |
| 17 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1133 | 5268 |
| 18 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1133 | 17191 |
| 19 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1132 | 70532 |
| 20 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1109 | 21582 |
| 21 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1106 | 13299 |
| 22 | [block/goose](https://github.com/block/goose) | +1069 | 31098 |
| 23 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +983 | 26831 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +972 | 74774 |
| 25 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +972 | 52218 |
| 26 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +962 | 70939 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +918 | 34148 |
| 28 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +901 | 54112 |
| 29 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +885 | 20651 |
| 30 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +876 | 11132 |
| 31 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +862 | 16068 |
| 32 | [chenglou/pretext](https://github.com/chenglou/pretext) | +801 | 43203 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +797 | 43397 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +780 | 8877 |
| 35 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +733 | 28001 |
| 36 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +719 | 52166 |
| 37 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +672 | 51240 |
| 38 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +660 | 30678 |
| 39 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +654 | 23152 |
| 40 | [farzaa/clicky](https://github.com/farzaa/clicky) | +628 | 3922 |
| 41 | [tobi/qmd](https://github.com/tobi/qmd) | +603 | 21136 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +596 | 34808 |
| 43 | [coleam00/Archon](https://github.com/coleam00/Archon) | +594 | 16955 |
| 44 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +590 | 10768 |
| 45 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +573 | 3171 |
| 46 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +555 | 38096 |
| 47 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +539 | 60757 |
| 48 | [Arthur-Ficial/apfel](https://github.com/Arthur-Ficial/apfel) | +530 | 4285 |
| 49 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +520 | 39003 |
| 50 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +515 | 30590 |
| 51 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +510 | 11094 |
| 52 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +500 | 26744 |
| 53 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +481 | 18686 |
| 54 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +480 | 4013 |
| 55 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +473 | 20997 |
| 56 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +464 | 4593 |
| 57 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +453 | 12194 |
| 58 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +449 | 9075 |
| 59 | [jackwener/opencli](https://github.com/jackwener/opencli) | +447 | 15272 |
| 60 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +438 | 2553 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +432 | 25338 |
| 62 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +425 | 3530 |
| 63 | [mattpocock/skills](https://github.com/mattpocock/skills) | +424 | 14337 |
| 64 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +420 | 7632 |
| 65 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +405 | 45886 |
| 66 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +402 | 13776 |
| 67 | [tw93/Waza](https://github.com/tw93/Waza) | +395 | 2768 |
| 68 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +387 | 30302 |
| 69 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +384 | 5888 |
| 70 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +373 | 17139 |
| 71 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +372 | 2257 |
| 72 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +369 | 2072 |
| 73 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +365 | 9076 |
| 74 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +358 | 2046 |
| 75 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +356 | 4580 |
| 76 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +353 | 2082 |
| 77 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +350 | 23050 |
| 78 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +348 | 31423 |
| 79 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +347 | 37330 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +344 | 20548 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +343 | 39302 |
| 82 | [google-research/timesfm](https://github.com/google-research/timesfm) | +342 | 16459 |
| 83 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +338 | 36431 |
| 84 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +337 | 35537 |
| 85 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +337 | 28824 |
| 86 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +333 | 32417 |
| 87 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +333 | 16848 |
| 88 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +319 | 4346 |
| 89 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +316 | 4540 |
| 90 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +313 | 2163 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +308 | 11967 |
| 92 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +307 | 18586 |
| 93 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +305 | 38270 |
| 94 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +301 | 3122 |
| 95 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +295 | 2867 |
| 96 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +294 | 7564 |
| 97 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +285 | 45722 |
| 98 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +275 | 23203 |
| 99 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +267 | 29500 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +251 | 1482 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +244 | 10689 |
| 102 | [snarktank/ralph](https://github.com/snarktank/ralph) | +243 | 15855 |
| 103 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +241 | 4211 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +237 | 10307 |
| 105 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +236 | 20479 |
| 106 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +232 | 1491 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +228 | 9034 |
| 108 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +228 | 1825 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +224 | 9637 |
| 110 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +214 | 39200 |
| 111 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +206 | 10335 |
| 112 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +195 | 22103 |
| 113 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +194 | 29280 |
| 114 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +190 | 25070 |
| 115 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +188 | 4685 |
| 116 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +179 | 29422 |
| 117 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +178 | 1730 |
| 118 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +177 | 13229 |
| 119 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +177 | 15905 |
| 120 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +175 | 39841 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24203 | 182383 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13184 | 51199 |
| 3 | [garrytan/gstack](https://github.com/garrytan/gstack) | +12207 | 70532 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +11654 | 60312 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +10410 | 65660 |
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9559 | 224760 |
| 7 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +9046 | 45442 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +8728 | 78818 |
| 9 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +7764 | 70939 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6641 | 54112 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6539 | 43203 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5559 | 52218 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5354 | 69674 |
| 14 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4825 | 60757 |
| 15 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4490 | 52166 |
| 16 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4375 | 30302 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4159 | 38786 |
| 18 | [anthropics/skills](https://github.com/anthropics/skills) | +4143 | 74774 |
| 19 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4068 | 21264 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4035 | 28726 |
| 21 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3925 | 23410 |
| 22 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3905 | 51240 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3850 | 109881 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3788 | 34148 |
| 25 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3730 | 25588 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3709 | 23203 |
| 27 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3529 | 21582 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3084 | 30590 |
| 29 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3059 | 22103 |
| 30 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +3028 | 28551 |
| 31 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2929 | 28001 |
| 32 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2919 | 24441 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2864 | 19053 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2817 | 43397 |
| 35 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2791 | 85286 |
| 36 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2707 | 26831 |
| 37 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2699 | 13532 |
| 38 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2619 | 15272 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2573 | 15251 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2453 | 18686 |
| 41 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2432 | 16068 |
| 42 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2413 | 30678 |
| 43 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2401 | 20997 |
| 44 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2390 | 29280 |
| 45 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2373 | 18586 |
| 46 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2321 | 39003 |
| 47 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2236 | 16848 |
| 48 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2153 | 13299 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2138 | 34808 |
| 50 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2105 | 47960 |
| 51 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2104 | 13776 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2068 | 33878 |
| 53 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2041 | 14337 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1947 | 71722 |
| 55 | [tanweai/pua](https://github.com/tanweai/pua) | +1906 | 15879 |
| 56 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1868 | 46485 |
| 57 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1827 | 29500 |
| 58 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1793 | 20479 |
| 59 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1775 | 45722 |
| 60 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1761 | 10768 |
| 61 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1741 | 26744 |
| 62 | [block/goose](https://github.com/block/goose) | +1738 | 31098 |
| 63 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1729 | 38270 |
| 64 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1720 | 11032 |
| 65 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1705 | 25338 |
| 66 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1694 | 31423 |
| 67 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1689 | 23152 |
| 68 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1677 | 9076 |
| 69 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1673 | 37330 |
| 70 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1666 | 9211 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1631 | 39302 |
| 72 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1570 | 10140 |
| 73 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1553 | 79656 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1547 | 8436 |
| 75 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1545 | 8877 |
| 76 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1524 | 13499 |
| 77 | [openai/codex](https://github.com/openai/codex) | +1522 | 61744 |
| 78 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1502 | 32417 |
| 79 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1469 | 19088 |
| 80 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1465 | 15982 |
| 81 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1453 | 17139 |
| 82 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1442 | 13783 |
| 83 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1438 | 9890 |
| 84 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1434 | 23050 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1417 | 98536 |
| 86 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1393 | 28824 |
| 87 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1391 | 11574 |
| 88 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1382 | 29782 |
| 89 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1367 | 35537 |
| 90 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1346 | 8726 |
| 91 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1336 | 73135 |
| 92 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1335 | 7632 |
| 93 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1325 | 16758 |
| 94 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1310 | 6663 |
| 95 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1302 | 38166 |
| 96 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1299 | 36431 |
| 97 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1297 | 20548 |
| 98 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1282 | 78902 |
| 99 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1275 | 17191 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1273 | 11967 |
| 101 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1243 | 52700 |
| 102 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1210 | 12849 |
| 103 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1190 | 39200 |
| 104 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1149 | 16459 |
| 105 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1135 | 5268 |
| 106 | [cft0808/edict](https://github.com/cft0808/edict) | +1135 | 14944 |
| 107 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1124 | 5664 |
| 108 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1100 | 20651 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +1090 | 9637 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1084 | 6303 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +1044 | 9034 |
| 112 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1041 | 10689 |
| 113 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +972 | 43973 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +953 | 10307 |
| 115 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +951 | 27173 |
| 116 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +922 | 5854 |
| 117 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +918 | 8791 |
| 118 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +902 | 23925 |
| 119 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +900 | 11132 |
| 120 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +881 | 49621 |
| 121 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +878 | 39841 |
| 122 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +832 | 6153 |
| 123 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +827 | 10335 |
| 124 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +814 | 15105 |
| 125 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +795 | 23476 |
| 126 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +791 | 5058 |
| 127 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +777 | 4712 |
| 128 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +764 | 4346 |
| 129 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +754 | 29422 |
| 130 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +745 | 4300 |
| 131 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +720 | 5471 |
| 132 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +716 | 45886 |
| 133 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +707 | 37564 |
| 134 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +690 | 33019 |
| 135 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +685 | 9075 |
| 136 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +684 | 9485 |
| 137 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +675 | 36799 |
| 138 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +669 | 9981 |
| 139 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +659 | 59619 |
| 140 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +658 | 25070 |
| 141 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +652 | 4848 |
| 142 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +632 | 3122 |
| 143 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +628 | 18225 |
| 144 | [coleam00/Archon](https://github.com/coleam00/Archon) | +615 | 16955 |
| 145 | [eze-is/web-access](https://github.com/eze-is/web-access) | +613 | 4657 |
| 146 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +608 | 2965 |
| 147 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +606 | 47936 |
| 148 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +601 | 5828 |
| 149 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +593 | 3048 |
| 150 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +569 | 3375 |
| 151 | [floci-io/floci](https://github.com/floci-io/floci) | +560 | 3325 |
| 152 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +556 | 18572 |
| 153 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +539 | 4852 |
| 154 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +534 | 2867 |
| 155 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +532 | 15905 |
| 156 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +520 | 29052 |
| 157 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +517 | 2349 |
| 158 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +514 | 11094 |
| 159 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +513 | 44545 |
| 160 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +510 | 2739 |
| 161 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +507 | 5378 |
| 162 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +504 | 3969 |
| 163 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +502 | 7457 |
| 164 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +490 | 8532 |
| 165 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +489 | 4211 |
| 166 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +480 | 4685 |
| 167 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +470 | 2891 |
| 168 | [openai/skills](https://github.com/openai/skills) | +463 | 16670 |
| 169 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +457 | 18576 |
| 170 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +456 | 4297 |
| 171 | [wshobson/agents](https://github.com/wshobson/agents) | +450 | 33467 |
| 172 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +448 | 3131 |
| 173 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +438 | 2461 |
| 174 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +433 | 1825 |
| 175 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +427 | 8624 |
| 176 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +427 | 2838 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +389 | 24951 |
| 178 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +387 | 2361 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +383 | 2753 |
| 180 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +377 | 2257 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +376 | 11711 |
| 182 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +361 | 2613 |
| 183 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +352 | 4540 |
| 184 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +342 | 1705 |
| 185 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +334 | 1772 |
| 186 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +323 | 1669 |
| 187 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +317 | 5089 |
| 188 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +315 | 3005 |
| 189 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +302 | 23088 |
| 190 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +301 | 2790 |
| 191 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +281 | 2311 |
| 192 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +276 | 1721 |
| 193 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +275 | 6238 |
| 194 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +272 | 9650 |
| 195 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +271 | 6814 |
| 196 | [decolua/9router](https://github.com/decolua/9router) | +268 | 2326 |
| 197 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +264 | 10942 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +257 | 5464 |
| 199 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +248 | 1065 |
| 200 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +231 | 23569 |
| 201 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +225 | 25571 |
| 202 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +224 | 6272 |
| 203 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +223 | 1996 |
| 204 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +220 | 13980 |
| 205 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +213 | 15398 |
| 206 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +213 | 36103 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 928 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +202 | 41086 |
| 209 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +198 | 2227 |
| 210 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +194 | 2675 |
| 211 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +191 | 33712 |
| 212 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +178 | 665 |
| 213 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +178 | 909 |
| 214 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +177 | 1302 |
| 215 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +176 | 2887 |
| 216 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +173 | 1436 |
| 217 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +160 | 980 |
| 218 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +159 | 22029 |
| 219 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +152 | 3693 |
| 220 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +150 | 747 |
| 221 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +148 | 3787 |
| 222 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +144 | 1303 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +140 | 35473 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +139 | 29512 |
| 225 | [dashersw/gea](https://github.com/dashersw/gea) | +136 | 947 |
| 226 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +136 | 40265 |
| 227 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +133 | 871 |
| 228 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +131 | 549 |
| 229 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +130 | 10684 |
| 230 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +127 | 810 |
| 231 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +126 | 29490 |
| 232 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +119 | 785 |
| 233 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +119 | 23274 |
| 234 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +116 | 12674 |
| 235 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +116 | 1251 |
| 236 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +115 | 1204 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +113 | 26510 |
| 238 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +112 | 753 |
| 239 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +110 | 1067 |
| 240 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +109 | 33000 |
| 241 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +108 | 2549 |
| 242 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +108 | 1723 |
| 243 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 244 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +107 | 495 |
| 245 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +106 | 851 |
| 246 | [RemotePinee/AudioVisual](https://github.com/RemotePinee/AudioVisual) | +103 | 2988 |
| 247 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +103 | 1502 |
| 248 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +100 | 2130 |
| 249 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +97 | 1118 |
| 250 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +96 | 48784 |
| 252 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +95 | 491 |
| 253 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3872 |
| 254 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +90 | 1664 |
| 255 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +90 | 1543 |
| 256 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +89 | 3508 |
| 257 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +88 | 1865 |
| 258 | [microg/GmsCore](https://github.com/microg/GmsCore) | +88 | 12906 |
| 259 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +87 | 488 |
| 260 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +87 | 1033 |
| 261 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +85 | 491 |
| 262 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +85 | 1847 |
| 263 | [robinebers/openusage](https://github.com/robinebers/openusage) | +84 | 1855 |
| 264 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +83 | 810 |
| 265 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +82 | 932 |
| 266 | [idinging/freemail](https://github.com/idinging/freemail) | +81 | 1338 |
| 267 | [clawplays/ospec](https://github.com/clawplays/ospec) | +81 | 400 |
| 268 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +80 | 531 |
| 269 | [meodai/heerich](https://github.com/meodai/heerich) | +80 | 466 |
| 270 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +79 | 3628 |
| 271 | [cosmiciron/vmprint](https://github.com/cosmiciron/vmprint) | +78 | 646 |
| 272 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +77 | 734 |
| 273 | [crimera/piko](https://github.com/crimera/piko) | +76 | 3145 |
| 274 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +74 | 2685 |
| 275 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +71 | 9185 |
| 276 | [openmemind/memind](https://github.com/openmemind/memind) | +70 | 380 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +70 | 27193 |
| 278 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +69 | 326 |
| 279 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +69 | 713 |
| 280 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +69 | 11565 |
| 281 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +69 | 45263 |
| 282 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +68 | 412 |
| 283 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +67 | 419 |
| 284 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +66 | 1556 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +63 | 7230 |
| 286 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +63 | 8485 |
| 287 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +62 | 531 |
| 288 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +62 | 391 |
| 289 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +61 | 490 |
| 290 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +59 | 25388 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +58 | 31476 |
| 292 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +56 | 283 |
| 293 | [apache/kafka](https://github.com/apache/kafka) | +56 | 32043 |
| 294 | [MuntashirAkon/AppManager](https://github.com/MuntashirAkon/AppManager) | +56 | 7807 |
| 295 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11628 |
| 296 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +54 | 268 |
| 297 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +53 | 1663 |
| 298 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +52 | 1734 |
| 299 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +52 | 4661 |
| 300 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +51 | 26687 |
