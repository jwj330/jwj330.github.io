---
title: "2026-04-14 GitHub增长趋势报告"
description: "1.hermes-agent+1130 2.andrej-karpathy-skills+1016 3.caveman+398 4.claude-mem+333 5.claude-code-best-practice+316"
date: 2026-04-14T20:57:17+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-14 20:57:17

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
        'daily': {"categories": ["addyosmani/agent-skills", "farion1231/cc-switch", "garrytan/gbrain", "OpenBMB/VoxCPM", "jamiepine/voicebox", "gsd-build/get-shit-done", "rtk-ai/rtk", "anthropics/claude-cookbooks", "alchaincyf/nuwa-skill", "virattt/ai-hedge-fund", "safishamsi/graphify", "multica-ai/multica", "NawfalMotii79/PLFM_RADAR", "google/magika", "VoltAgent/awesome-design-md", "shanraisshan/claude-code-best-practice", "thedotmack/claude-mem", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [80, 83, 89, 93, 99, 107, 109, 112, 116, 128, 158, 195, 199, 205, 288, 316, 333, 398, 1016, 1130]},
        'weekly': {"categories": ["opendataloader-project/opendataloader-pdf", "garrytan/gstack", "msitarzewski/agency-agents", "rtk-ai/rtk", "HKUDS/DeepTutor", "alchaincyf/zhangxuefeng-skill", "OpenBMB/VoxCPM", "addyosmani/agent-skills", "alchaincyf/nuwa-skill", "thedotmack/claude-mem", "garrytan/gbrain", "shanraisshan/claude-code-best-practice", "multica-ai/multica", "affaan-m/everything-claude-code", "obra/superpowers", "forrestchang/andrej-karpathy-skills", "safishamsi/graphify", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "NousResearch/hermes-agent"], "data": [987, 1066, 1070, 1155, 1184, 1279, 1289, 1379, 1473, 1497, 1635, 1958, 1975, 2174, 2299, 3490, 3753, 4124, 4293, 10051]},
        'monthly': {"categories": ["anthropics/skills", "siddharthvaddem/openscreen", "shareAI-lab/learn-claude-code", "safishamsi/graphify", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "paperclipai/paperclip", "JuliusBrussee/caveman", "anthropics/claude-code", "666ghj/MiroFish", "chenglou/pretext", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw", "VoltAgent/awesome-design-md", "garrytan/gstack", "obra/superpowers", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4077, 4214, 4463, 4480, 4659, 4812, 5265, 5287, 5392, 5888, 6634, 7010, 7085, 8707, 9925, 11103, 11587, 13307, 13712, 24574]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1130 | 83892 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1016 | 32564 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +398 | 29430 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +333 | 30678 |
| 5 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +316 | 43574 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +288 | 50520 |
| 7 | [google/magika](https://github.com/google/magika) | +205 | 12998 |
| 8 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +199 | 7022 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | +195 | 12335 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +158 | 26277 |
| 11 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +128 | 45886 |
| 12 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +116 | 10509 |
| 13 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +112 | 33311 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +109 | 26396 |
| 15 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +107 | 52912 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +99 | 17199 |
| 17 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +93 | 12890 |
| 18 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +89 | 7800 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +83 | 44681 |
| 20 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +80 | 15397 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +80 | 53313 |
| 22 | [snarktank/ralph](https://github.com/snarktank/ralph) | +77 | 16803 |
| 23 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +76 | 3257 |
| 24 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +66 | 14112 |
| 25 | [xming521/WeClone](https://github.com/xming521/WeClone) | +66 | 17389 |
| 26 | [patterniha/SNI-Spoofing](https://github.com/patterniha/SNI-Spoofing) | +65 | 535 |
| 27 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +59 | 9968 |
| 28 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +59 | 22648 |
| 29 | [pascalorg/editor](https://github.com/pascalorg/editor) | +58 | 11424 |
| 30 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +56 | 28783 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +10051 | 83892 |
| 2 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4293 | 29430 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +4124 | 50520 |
| 4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3753 | 26277 |
| 5 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3490 | 32568 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2299 | 60312 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2174 | 51199 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1975 | 12336 |
| 9 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1958 | 43574 |
| 10 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1635 | 7800 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1497 | 30678 |
| 12 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1473 | 10509 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1379 | 15397 |
| 14 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1289 | 12890 |
| 15 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1279 | 5742 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1184 | 18104 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1155 | 26396 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1070 | 79921 |
| 19 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1066 | 72353 |
| 20 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +987 | 16714 |
| 21 | [anthropics/skills](https://github.com/anthropics/skills) | +954 | 74774 |
| 22 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +886 | 29741 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +881 | 22648 |
| 24 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +842 | 72236 |
| 25 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +835 | 14112 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +832 | 53611 |
| 27 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +808 | 9968 |
| 28 | [coleam00/Archon](https://github.com/coleam00/Archon) | +801 | 17932 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +794 | 34148 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +778 | 44681 |
| 31 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +770 | 26384 |
| 32 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +738 | 55043 |
| 33 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +722 | 52912 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +716 | 53313 |
| 35 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +700 | 3928 |
| 36 | [farzaa/clicky](https://github.com/farzaa/clicky) | +687 | 4160 |
| 37 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +627 | 27343 |
| 38 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +599 | 45886 |
| 39 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +592 | 11334 |
| 40 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +561 | 28783 |
| 41 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +527 | 23915 |
| 42 | [block/goose](https://github.com/block/goose) | +524 | 31098 |
| 43 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +508 | 35557 |
| 44 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +507 | 21041 |
| 45 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +486 | 12375 |
| 46 | [chenglou/pretext](https://github.com/chenglou/pretext) | +478 | 43782 |
| 47 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +472 | 19223 |
| 48 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +460 | 3257 |
| 49 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +457 | 2676 |
| 50 | [snarktank/ralph](https://github.com/snarktank/ralph) | +446 | 16803 |
| 51 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +441 | 21851 |
| 52 | [tobi/qmd](https://github.com/tobi/qmd) | +439 | 21579 |
| 53 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +432 | 30590 |
| 54 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +431 | 26008 |
| 55 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +426 | 39505 |
| 56 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +421 | 2428 |
| 57 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +420 | 4987 |
| 58 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +416 | 2629 |
| 59 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +407 | 7804 |
| 60 | [mattpocock/skills](https://github.com/mattpocock/skills) | +389 | 14991 |
| 61 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +388 | 33311 |
| 62 | [markdown-viewer/skills](https://github.com/markdown-viewer/skills) | +379 | 1700 |
| 63 | [jackwener/opencli](https://github.com/jackwener/opencli) | +365 | 15770 |
| 64 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +362 | 4764 |
| 65 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +351 | 36930 |
| 66 | [tw93/Waza](https://github.com/tw93/Waza) | +351 | 3159 |
| 67 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +345 | 36451 |
| 68 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +341 | 12522 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +341 | 21144 |
| 70 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +340 | 17199 |
| 71 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +337 | 6324 |
| 72 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +333 | 37330 |
| 73 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +315 | 14295 |
| 74 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +313 | 30692 |
| 75 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +311 | 39929 |
| 76 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +307 | 34989 |
| 77 | [google-research/timesfm](https://github.com/google-research/timesfm) | +306 | 17277 |
| 78 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +305 | 33015 |
| 79 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +299 | 38720 |
| 80 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +297 | 23427 |
| 81 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +293 | 19123 |
| 82 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +292 | 7888 |
| 83 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +289 | 23643 |
| 84 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +288 | 1938 |
| 85 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +287 | 25795 |
| 86 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +276 | 9289 |
| 87 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +273 | 3075 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +271 | 26772 |
| 89 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +270 | 29860 |
| 90 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +270 | 17576 |
| 91 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +267 | 46015 |
| 92 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +266 | 27074 |
| 93 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | +264 | 8244 |
| 94 | [tw93/Mole](https://github.com/tw93/Mole) | +262 | 36870 |
| 95 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +259 | 31783 |
| 96 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +255 | 1678 |
| 97 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +250 | 19696 |
| 98 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +248 | 7023 |
| 99 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +245 | 15802 |
| 100 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +241 | 10777 |
| 101 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +236 | 11258 |
| 102 | [alejandrobalderas/claude-code-from-source](https://github.com/alejandrobalderas/claude-code-from-source) | +235 | 1445 |
| 103 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +227 | 17408 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +225 | 10573 |
| 105 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +224 | 4171 |
| 106 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +223 | 1677 |
| 107 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +212 | 3398 |
| 108 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +210 | 1709 |
| 109 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +210 | 11068 |
| 110 | [google/magika](https://github.com/google/magika) | +207 | 12998 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +207 | 9208 |
| 112 | [mattmireles/gemma-tuner-multimodal](https://github.com/mattmireles/gemma-tuner-multimodal) | +206 | 1278 |
| 113 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +204 | 20723 |
| 114 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +203 | 5145 |
| 115 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +203 | 10659 |
| 116 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +200 | 39513 |
| 117 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +195 | 4468 |
| 118 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +191 | 1829 |
| 119 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +188 | 6037 |
| 120 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +182 | 13371 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24574 | 184142 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +13712 | 83892 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13307 | 51199 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +11587 | 60312 |
| 5 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11103 | 72354 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +9925 | 50520 |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8707 | 224760 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +7085 | 79921 |
| 9 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +7010 | 72236 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6634 | 43782 |
| 11 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +5888 | 55043 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5392 | 69674 |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +5287 | 29430 |
| 14 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5265 | 53611 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4812 | 61484 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4659 | 43574 |
| 17 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4480 | 26277 |
| 18 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4463 | 53313 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4214 | 29741 |
| 20 | [anthropics/skills](https://github.com/anthropics/skills) | +4077 | 74774 |
| 21 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3903 | 52912 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3881 | 34148 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3873 | 26384 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3831 | 109881 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3739 | 23643 |
| 26 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3683 | 22648 |
| 27 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3565 | 32570 |
| 28 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3391 | 30692 |
| 29 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3347 | 30678 |
| 30 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3169 | 30590 |
| 31 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3088 | 15397 |
| 32 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3046 | 26396 |
| 33 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2996 | 28783 |
| 34 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2901 | 19211 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2858 | 44681 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2793 | 85286 |
| 37 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2710 | 15770 |
| 38 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2696 | 27343 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2632 | 15566 |
| 40 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2597 | 15802 |
| 41 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2585 | 16714 |
| 42 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2542 | 21852 |
| 43 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2464 | 22270 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2457 | 19124 |
| 45 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2429 | 39505 |
| 46 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2421 | 29552 |
| 47 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2393 | 28699 |
| 48 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2326 | 14112 |
| 49 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2233 | 12336 |
| 50 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2200 | 14295 |
| 51 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2168 | 14991 |
| 52 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2111 | 35557 |
| 53 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2108 | 33878 |
| 54 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1971 | 19223 |
| 55 | [github/spec-kit](https://github.com/github/spec-kit) | +1936 | 71722 |
| 56 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1917 | 48296 |
| 57 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1894 | 10509 |
| 58 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1889 | 11334 |
| 59 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1823 | 20723 |
| 60 | [block/goose](https://github.com/block/goose) | +1820 | 31098 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1808 | 23915 |
| 62 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1802 | 27074 |
| 63 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1749 | 9968 |
| 64 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1744 | 38720 |
| 65 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1743 | 11150 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1730 | 26008 |
| 67 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1723 | 16990 |
| 68 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1710 | 9320 |
| 69 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1707 | 31783 |
| 70 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1705 | 46670 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1693 | 29860 |
| 72 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1665 | 79656 |
| 73 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1665 | 37330 |
| 74 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1635 | 7800 |
| 75 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1635 | 46015 |
| 76 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1622 | 10494 |
| 77 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1577 | 39929 |
| 78 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1556 | 13658 |
| 79 | [openai/codex](https://github.com/openai/codex) | +1511 | 61744 |
| 80 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1503 | 11425 |
| 81 | [tanweai/pua](https://github.com/tanweai/pua) | +1492 | 16077 |
| 82 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1456 | 33015 |
| 83 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1429 | 17408 |
| 84 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1407 | 18104 |
| 85 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1404 | 11632 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1404 | 98536 |
| 87 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1395 | 36451 |
| 88 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1359 | 8793 |
| 89 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1345 | 73135 |
| 90 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1336 | 9497 |
| 91 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1324 | 12890 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1319 | 21144 |
| 93 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1315 | 6678 |
| 94 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1296 | 78902 |
| 95 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1284 | 5742 |
| 96 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1275 | 36930 |
| 97 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1275 | 52700 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1271 | 12522 |
| 99 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1249 | 17278 |
| 100 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1167 | 21041 |
| 101 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1155 | 19350 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1140 | 16933 |
| 103 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1134 | 5704 |
| 104 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1124 | 39513 |
| 105 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1068 | 12903 |
| 106 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1028 | 6601 |
| 107 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1020 | 29957 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1005 | 11068 |
| 109 | [cft0808/edict](https://github.com/cft0808/edict) | +1004 | 15091 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +976 | 9901 |
| 111 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +941 | 5985 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +934 | 10573 |
| 113 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +931 | 8858 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +908 | 45886 |
| 115 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +903 | 24043 |
| 116 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +900 | 49621 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +894 | 9208 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +880 | 39841 |
| 119 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +855 | 6238 |
| 120 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +839 | 27271 |
| 121 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +835 | 10659 |
| 122 | [coleam00/Archon](https://github.com/coleam00/Archon) | +821 | 17932 |
| 123 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +819 | 5197 |
| 124 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +801 | 23716 |
| 125 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +792 | 15334 |
| 126 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +787 | 4468 |
| 127 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +786 | 4761 |
| 128 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +758 | 4382 |
| 129 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +735 | 5514 |
| 130 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +733 | 43973 |
| 131 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +730 | 29672 |
| 132 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +716 | 9289 |
| 133 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +710 | 33223 |
| 134 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +700 | 38254 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +687 | 9517 |
| 136 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +677 | 10777 |
| 137 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +672 | 36799 |
| 138 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +672 | 37564 |
| 139 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +669 | 3398 |
| 140 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +662 | 59619 |
| 141 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +656 | 25211 |
| 142 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +651 | 4980 |
| 143 | [eze-is/web-access](https://github.com/eze-is/web-access) | +645 | 4877 |
| 144 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +622 | 54903 |
| 145 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +612 | 18454 |
| 146 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +611 | 47936 |
| 147 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +605 | 5881 |
| 148 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +603 | 3095 |
| 149 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +580 | 3075 |
| 150 | [floci-io/floci](https://github.com/floci-io/floci) | +580 | 3471 |
| 151 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +546 | 2494 |
| 152 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +543 | 5145 |
| 153 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +541 | 18736 |
| 154 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +540 | 4036 |
| 155 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +536 | 16142 |
| 156 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +535 | 6037 |
| 157 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +535 | 29256 |
| 158 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +530 | 11258 |
| 159 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +526 | 7692 |
| 160 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +510 | 44545 |
| 161 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +509 | 2762 |
| 162 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +495 | 4171 |
| 163 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +488 | 2991 |
| 164 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +486 | 2302 |
| 165 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +470 | 2753 |
| 166 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +461 | 4338 |
| 167 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +454 | 3161 |
| 168 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +453 | 18708 |
| 169 | [openai/skills](https://github.com/openai/skills) | +452 | 16816 |
| 170 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +446 | 1895 |
| 171 | [wshobson/agents](https://github.com/wshobson/agents) | +441 | 33614 |
| 172 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +427 | 2895 |
| 173 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +423 | 2629 |
| 174 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +422 | 8740 |
| 175 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +409 | 4764 |
| 176 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +405 | 2432 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +388 | 25074 |
| 178 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +386 | 2762 |
| 179 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +384 | 2782 |
| 180 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +364 | 1938 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +364 | 11840 |
| 182 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +358 | 1781 |
| 183 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +345 | 1808 |
| 184 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +333 | 1678 |
| 185 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +328 | 23261 |
| 186 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +324 | 1677 |
| 187 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +316 | 3017 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +313 | 2907 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +310 | 5188 |
| 190 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +276 | 1743 |
| 191 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +274 | 5698 |
| 192 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +272 | 6876 |
| 193 | [decolua/9router](https://github.com/decolua/9router) | +267 | 2464 |
| 194 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +260 | 11032 |
| 195 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +259 | 2286 |
| 196 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +258 | 6276 |
| 197 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +256 | 9610 |
| 198 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +242 | 2344 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +238 | 25678 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +236 | 36103 |
| 201 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +231 | 23621 |
| 202 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +223 | 1065 |
| 203 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +218 | 6310 |
| 204 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +215 | 15487 |
| 205 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +214 | 33712 |
| 206 | [usebruno/bruno](https://github.com/usebruno/bruno) | +204 | 41086 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +204 | 932 |
| 208 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +199 | 2691 |
| 209 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +197 | 2297 |
| 210 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +190 | 3539 |
| 211 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +186 | 14033 |
| 212 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +182 | 2928 |
| 213 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +178 | 666 |
| 214 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +178 | 1326 |
| 215 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +178 | 939 |
| 216 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +177 | 1118 |
| 217 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +163 | 1507 |
| 218 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +156 | 3824 |
| 219 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +154 | 767 |
| 220 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +154 | 40265 |
| 221 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +153 | 1361 |
| 222 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +150 | 22070 |
| 223 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +145 | 917 |
| 224 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +143 | 35473 |
| 225 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 954 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +131 | 29541 |
| 227 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +130 | 3698 |
| 228 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +127 | 815 |
| 229 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +125 | 29540 |
| 230 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +125 | 10722 |
| 231 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 810 |
| 232 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +121 | 23315 |
| 233 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +114 | 26549 |
| 234 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +113 | 12700 |
| 235 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +112 | 1072 |
| 236 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +111 | 5189 |
| 237 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +111 | 1277 |
| 238 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +110 | 764 |
| 239 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +108 | 500 |
| 240 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 241 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +107 | 860 |
| 242 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +106 | 1257 |
| 243 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +105 | 1753 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +102 | 2585 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +101 | 33000 |
| 246 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +99 | 2162 |
| 247 | [RemotePinee/AudioVisual](https://github.com/RemotePinee/AudioVisual) | +98 | 2994 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +98 | 1556 |
| 249 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +97 | 1137 |
| 250 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 251 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +96 | 496 |
| 252 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3892 |
| 253 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 1583 |
| 254 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +92 | 48784 |
| 255 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +91 | 534 |
| 256 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +88 | 1890 |
| 257 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +88 | 564 |
| 258 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +88 | 519 |
| 259 | [microg/GmsCore](https://github.com/microg/GmsCore) | +88 | 12928 |
| 260 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +87 | 1885 |
| 261 | [crimera/piko](https://github.com/crimera/piko) | +87 | 3187 |
| 262 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +86 | 971 |
| 263 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 3552 |
| 264 | [clawplays/ospec](https://github.com/clawplays/ospec) | +85 | 456 |
| 265 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +85 | 1061 |
| 266 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +83 | 1680 |
| 267 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +82 | 519 |
| 268 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +81 | 558 |
| 269 | [robinebers/openusage](https://github.com/robinebers/openusage) | +81 | 1913 |
| 270 | [meodai/heerich](https://github.com/meodai/heerich) | +80 | 482 |
| 271 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +80 | 9236 |
| 272 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +78 | 3658 |
| 273 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +73 | 4018 |
| 274 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +73 | 27217 |
| 275 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +72 | 341 |
| 276 | [idinging/freemail](https://github.com/idinging/freemail) | +71 | 1353 |
| 277 | [openmemind/memind](https://github.com/openmemind/memind) | +71 | 397 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +71 | 11602 |
| 279 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 280 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +70 | 723 |
| 281 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +69 | 433 |
| 282 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +67 | 1340 |
| 283 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7240 |
| 284 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +64 | 1571 |
| 285 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +62 | 390 |
| 286 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +61 | 31476 |
| 287 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +60 | 25399 |
| 288 | [apache/kafka](https://github.com/apache/kafka) | +59 | 32043 |
| 289 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 290 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +57 | 294 |
| 291 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +56 | 306 |
| 292 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +56 | 498 |
| 293 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +56 | 1765 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +53 | 28930 |
| 295 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +52 | 490 |
| 296 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +51 | 11639 |
| 297 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +51 | 8497 |
| 298 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +51 | 4671 |
| 299 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1686 |
| 300 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1673 |
