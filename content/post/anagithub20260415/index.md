---
title: "2026-04-15 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+1263 2.hermes-agent+778 3.caveman+431 4.awesome-design-md+376 5.claude-mem+311"
date: 2026-04-15T20:52:57+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-15 20:52:57

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
        'daily': {"categories": ["gsd-build/get-shit-done", "OpenBMB/VoxCPM", "alchaincyf/nuwa-skill", "datawhalechina/hello-agents", "Yeachan-Heo/oh-my-codex", "anthropics/claude-cookbooks", "farion1231/cc-switch", "rtk-ai/rtk", "google/magika", "jamiepine/voicebox", "multica-ai/multica", "safishamsi/graphify", "pascalorg/editor", "shanraisshan/claude-code-best-practice", "NawfalMotii79/PLFM_RADAR", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [85, 86, 87, 88, 90, 92, 97, 110, 115, 127, 157, 168, 173, 242, 264, 311, 376, 431, 778, 1263]},
        'weekly': {"categories": ["opendataloader-project/opendataloader-pdf", "anthropics/skills", "HKUDS/DeepTutor", "garrytan/gstack", "rtk-ai/rtk", "addyosmani/agent-skills", "alchaincyf/zhangxuefeng-skill", "OpenBMB/VoxCPM", "alchaincyf/nuwa-skill", "garrytan/gbrain", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "multica-ai/multica", "shanraisshan/claude-code-best-practice", "obra/superpowers", "safishamsi/graphify", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [931, 945, 1038, 1052, 1155, 1237, 1287, 1297, 1375, 1671, 1749, 2061, 2112, 2135, 2260, 3111, 3398, 4432, 4634, 9894]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "shareAI-lab/learn-claude-code", "shanraisshan/claude-code-best-practice", "safishamsi/graphify", "bytedance/deer-flow", "forrestchang/andrej-karpathy-skills", "paperclipai/paperclip", "666ghj/MiroFish", "anthropics/claude-code", "JuliusBrussee/caveman", "msitarzewski/agency-agents", "karpathy/autoresearch", "chenglou/pretext", "openclaw/openclaw", "garrytan/gstack", "VoltAgent/awesome-design-md", "obra/superpowers", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4205, 4267, 4620, 4638, 4759, 4790, 5071, 5136, 5366, 5696, 6178, 6369, 6667, 8114, 10045, 10275, 11320, 13179, 14309, 24662]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1263 | 42209 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +778 | 89175 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +431 | 32370 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +376 | 53528 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +311 | 30678 |
| 6 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +264 | 9084 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +242 | 44881 |
| 8 | [pascalorg/editor](https://github.com/pascalorg/editor) | +173 | 12518 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +168 | 27299 |
| 10 | [multica-ai/multica](https://github.com/multica-ai/multica) | +157 | 13470 |
| 11 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +127 | 18117 |
| 12 | [google/magika](https://github.com/google/magika) | +115 | 13669 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +110 | 27222 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +97 | 45327 |
| 15 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +92 | 33311 |
| 16 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +90 | 23184 |
| 17 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +88 | 37081 |
| 18 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +87 | 11201 |
| 19 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +86 | 13389 |
| 20 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +85 | 53485 |
| 21 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +76 | 15836 |
| 22 | [google-research/timesfm](https://github.com/google-research/timesfm) | +75 | 17742 |
| 23 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +71 | 53769 |
| 24 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +69 | 10272 |
| 25 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +65 | 1847 |
| 26 | [tw93/Mole](https://github.com/tw93/Mole) | +63 | 36870 |
| 27 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +62 | 1898 |
| 28 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +62 | 2566 |
| 29 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +62 | 3537 |
| 30 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +58 | 4996 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +9894 | 89175 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4634 | 42210 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4432 | 32371 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3398 | 53528 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3111 | 27300 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2260 | 60312 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2135 | 44881 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2112 | 13470 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2061 | 51199 |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1749 | 30678 |
| 11 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1671 | 8265 |
| 12 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1375 | 11201 |
| 13 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1297 | 13389 |
| 14 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1287 | 5912 |
| 15 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1237 | 15836 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1155 | 27222 |
| 17 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1052 | 73174 |
| 18 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1038 | 18412 |
| 19 | [anthropics/skills](https://github.com/anthropics/skills) | +945 | 74774 |
| 20 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +931 | 17181 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +883 | 80336 |
| 22 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +830 | 23184 |
| 23 | [coleam00/Archon](https://github.com/coleam00/Archon) | +826 | 18198 |
| 24 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +811 | 30082 |
| 25 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +807 | 54120 |
| 26 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +783 | 72758 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +764 | 45327 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +736 | 34148 |
| 29 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +732 | 45886 |
| 30 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +724 | 4123 |
| 31 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +723 | 53486 |
| 32 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +718 | 14401 |
| 33 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +703 | 10314 |
| 34 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +693 | 55358 |
| 35 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +669 | 53769 |
| 36 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +649 | 26663 |
| 37 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +534 | 29094 |
| 38 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +522 | 11522 |
| 39 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +515 | 3537 |
| 40 | [Keychron/Keychron-Keyboards-Hardware-Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design) | +515 | 3062 |
| 41 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +502 | 9084 |
| 42 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +493 | 24289 |
| 43 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +480 | 27532 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +473 | 35907 |
| 45 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +463 | 12439 |
| 46 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +461 | 33311 |
| 47 | [farzaa/clicky](https://github.com/farzaa/clicky) | +457 | 4239 |
| 48 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +456 | 18117 |
| 49 | [snarktank/ralph](https://github.com/snarktank/ralph) | +443 | 16941 |
| 50 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +431 | 22086 |
| 51 | [block/goose](https://github.com/block/goose) | +428 | 31098 |
| 52 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +426 | 2546 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +413 | 26277 |
| 54 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +413 | 7876 |
| 55 | [chenglou/pretext](https://github.com/chenglou/pretext) | +411 | 44015 |
| 56 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +409 | 39729 |
| 57 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +400 | 19496 |
| 58 | [markdown-viewer/skills](https://github.com/markdown-viewer/skills) | +390 | 1768 |
| 59 | [mattpocock/skills](https://github.com/mattpocock/skills) | +388 | 15326 |
| 60 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +386 | 5089 |
| 61 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +386 | 2839 |
| 62 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +380 | 37081 |
| 63 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +378 | 21192 |
| 64 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +363 | 37212 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +349 | 12823 |
| 66 | [tobi/qmd](https://github.com/tobi/qmd) | +338 | 21725 |
| 67 | [google-research/timesfm](https://github.com/google-research/timesfm) | +337 | 17742 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +327 | 21383 |
| 69 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +320 | 37330 |
| 70 | [google/magika](https://github.com/google/magika) | +318 | 13669 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +318 | 40268 |
| 72 | [jackwener/opencli](https://github.com/jackwener/opencli) | +314 | 15942 |
| 73 | [tw93/Waza](https://github.com/tw93/Waza) | +308 | 3247 |
| 74 | [tw93/Mole](https://github.com/tw93/Mole) | +307 | 36870 |
| 75 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +302 | 35238 |
| 76 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +302 | 8078 |
| 77 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +299 | 23813 |
| 78 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +297 | 19390 |
| 79 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +297 | 23602 |
| 80 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +296 | 25910 |
| 81 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +295 | 33225 |
| 82 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +281 | 14540 |
| 83 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +281 | 17775 |
| 84 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +280 | 38927 |
| 85 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +280 | 6477 |
| 86 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | +279 | 8406 |
| 87 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +274 | 30855 |
| 88 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +273 | 3270 |
| 89 | [pascalorg/editor](https://github.com/pascalorg/editor) | +272 | 12518 |
| 90 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +269 | 2129 |
| 91 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +266 | 30055 |
| 92 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +262 | 10881 |
| 93 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +261 | 1759 |
| 94 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +257 | 19795 |
| 95 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +251 | 1386 |
| 96 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +250 | 46153 |
| 97 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +248 | 26963 |
| 98 | [alejandrobalderas/claude-code-from-source](https://github.com/alejandrobalderas/claude-code-from-source) | +243 | 1517 |
| 99 | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | +242 | 23305 |
| 100 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +233 | 27188 |
| 101 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +232 | 2566 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +223 | 11244 |
| 103 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +223 | 4187 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +217 | 10685 |
| 105 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +213 | 9350 |
| 106 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +207 | 5379 |
| 107 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +205 | 10776 |
| 108 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +203 | 9316 |
| 109 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +202 | 1760 |
| 110 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +200 | 17511 |
| 111 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +196 | 6105 |
| 112 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +192 | 39661 |
| 113 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +191 | 1806 |
| 114 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +189 | 3503 |
| 115 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +187 | 11408 |
| 116 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +179 | 20828 |
| 117 | [joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui) | +167 | 910 |
| 118 | [jundot/omlx](https://github.com/jundot/omlx) | +166 | 10205 |
| 119 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +166 | 2554 |
| 120 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +162 | 39841 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24662 | 184745 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +14309 | 89175 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13179 | 51199 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +11320 | 60312 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +10275 | 53529 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +10045 | 73175 |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +8114 | 224760 |
| 8 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6667 | 44015 |
| 9 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +6369 | 72758 |
| 10 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +6178 | 80336 |
| 11 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +5696 | 32371 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5366 | 69674 |
| 13 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +5136 | 55358 |
| 14 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5071 | 54120 |
| 15 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4790 | 42211 |
| 16 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4759 | 61785 |
| 17 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4638 | 27300 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4620 | 44881 |
| 19 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4267 | 53769 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4205 | 30082 |
| 21 | [anthropics/skills](https://github.com/anthropics/skills) | +3996 | 74774 |
| 22 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3897 | 26663 |
| 23 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3854 | 53486 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3815 | 34148 |
| 25 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3757 | 109881 |
| 26 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3754 | 23184 |
| 27 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3727 | 23813 |
| 28 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3581 | 30678 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3178 | 30590 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3159 | 15836 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3039 | 27222 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3007 | 29094 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2905 | 19269 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2851 | 45327 |
| 35 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2828 | 30855 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2738 | 85286 |
| 37 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2663 | 15942 |
| 38 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2655 | 15675 |
| 39 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2627 | 17181 |
| 40 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2620 | 15927 |
| 41 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2596 | 27532 |
| 42 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2560 | 22086 |
| 43 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2491 | 19390 |
| 44 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2457 | 39729 |
| 45 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2437 | 29681 |
| 46 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2385 | 13470 |
| 47 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2375 | 14401 |
| 48 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2227 | 14540 |
| 49 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2207 | 15326 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2072 | 33878 |
| 51 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2019 | 35907 |
| 52 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1983 | 28758 |
| 53 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1973 | 11201 |
| 54 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1912 | 22339 |
| 55 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1911 | 11522 |
| 56 | [github/spec-kit](https://github.com/github/spec-kit) | +1911 | 71722 |
| 57 | [block/goose](https://github.com/block/goose) | +1826 | 31098 |
| 58 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1811 | 24289 |
| 59 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1808 | 27188 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1804 | 10314 |
| 61 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1790 | 19496 |
| 62 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1758 | 48402 |
| 63 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1735 | 11204 |
| 64 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1727 | 9402 |
| 65 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1724 | 20828 |
| 66 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1704 | 38927 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1696 | 26277 |
| 68 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1687 | 31969 |
| 69 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1680 | 79656 |
| 70 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1678 | 8265 |
| 71 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1675 | 12518 |
| 72 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1633 | 10618 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1597 | 30055 |
| 74 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1590 | 37330 |
| 75 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1587 | 46791 |
| 76 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1565 | 13719 |
| 77 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1563 | 40268 |
| 78 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1553 | 17053 |
| 79 | [openai/codex](https://github.com/openai/codex) | +1507 | 61744 |
| 80 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1506 | 46153 |
| 81 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1445 | 18412 |
| 82 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1425 | 37081 |
| 83 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1410 | 13389 |
| 84 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1405 | 11647 |
| 85 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1405 | 10272 |
| 86 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1402 | 33225 |
| 87 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1377 | 17511 |
| 88 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1374 | 98536 |
| 89 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1358 | 73135 |
| 90 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1323 | 17742 |
| 91 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1317 | 6682 |
| 92 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1309 | 5912 |
| 93 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1293 | 78902 |
| 94 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1286 | 21383 |
| 95 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1277 | 52700 |
| 96 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1244 | 8813 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1226 | 12823 |
| 98 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1192 | 37212 |
| 99 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1179 | 21192 |
| 100 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1135 | 5715 |
| 101 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1067 | 39661 |
| 102 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1028 | 12923 |
| 103 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1014 | 45886 |
| 104 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +985 | 17020 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +975 | 11244 |
| 106 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +951 | 6041 |
| 107 | [cft0808/edict](https://github.com/cft0808/edict) | +938 | 15160 |
| 108 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +934 | 8874 |
| 109 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +927 | 6728 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +920 | 10205 |
| 111 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +896 | 49621 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +894 | 24103 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +892 | 10685 |
| 114 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +886 | 30037 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +873 | 9316 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +871 | 39841 |
| 117 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +863 | 6269 |
| 118 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +853 | 19407 |
| 119 | [coleam00/Archon](https://github.com/coleam00/Archon) | +852 | 18198 |
| 120 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +838 | 10776 |
| 121 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +827 | 5250 |
| 122 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +806 | 23804 |
| 123 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +793 | 4516 |
| 124 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +789 | 4788 |
| 125 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +737 | 5529 |
| 126 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +732 | 27334 |
| 127 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +728 | 9350 |
| 128 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +721 | 29869 |
| 129 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +714 | 33345 |
| 130 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +692 | 9557 |
| 131 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +683 | 3503 |
| 132 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +680 | 15416 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +672 | 36799 |
| 134 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +663 | 59619 |
| 135 | [eze-is/web-access](https://github.com/eze-is/web-access) | +656 | 4972 |
| 136 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +652 | 37564 |
| 137 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +649 | 25290 |
| 138 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +632 | 38310 |
| 139 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +628 | 43973 |
| 140 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +620 | 54903 |
| 141 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +605 | 3114 |
| 142 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +604 | 18556 |
| 143 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +603 | 4440 |
| 144 | [floci-io/floci](https://github.com/floci-io/floci) | +600 | 3795 |
| 145 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +596 | 5927 |
| 146 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +594 | 3270 |
| 147 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +589 | 47936 |
| 148 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +586 | 10881 |
| 149 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +584 | 5047 |
| 150 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +562 | 11408 |
| 151 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +559 | 5379 |
| 152 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +544 | 4061 |
| 153 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +533 | 16258 |
| 154 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +533 | 29361 |
| 155 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +512 | 2529 |
| 156 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +510 | 6105 |
| 157 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +509 | 2778 |
| 158 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +506 | 18813 |
| 159 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +503 | 7721 |
| 160 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +497 | 4187 |
| 161 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +494 | 44545 |
| 162 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +491 | 3013 |
| 163 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +488 | 2342 |
| 164 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +486 | 2831 |
| 165 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +465 | 4362 |
| 166 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +456 | 3178 |
| 167 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +451 | 1911 |
| 168 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +447 | 18775 |
| 169 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +445 | 8971 |
| 170 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +435 | 2839 |
| 171 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +418 | 2912 |
| 172 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +410 | 4886 |
| 173 | [usestrix/strix](https://github.com/usestrix/strix) | +406 | 23972 |
| 174 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +406 | 2498 |
| 175 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +392 | 2834 |
| 176 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +391 | 19795 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +389 | 25163 |
| 178 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +387 | 2129 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +386 | 2771 |
| 180 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +365 | 1830 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +363 | 11917 |
| 182 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +347 | 1824 |
| 183 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +341 | 1759 |
| 184 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +332 | 23344 |
| 185 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +330 | 1806 |
| 186 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +312 | 2945 |
| 187 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +309 | 2566 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +304 | 5237 |
| 189 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +287 | 3023 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +274 | 5786 |
| 191 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +271 | 6913 |
| 192 | [decolua/9router](https://github.com/decolua/9router) | +267 | 2504 |
| 193 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +249 | 11066 |
| 194 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +245 | 9609 |
| 195 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +242 | 6277 |
| 196 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +232 | 36103 |
| 197 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +231 | 2365 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +227 | 25729 |
| 199 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +216 | 6328 |
| 200 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +216 | 1065 |
| 201 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +213 | 15522 |
| 202 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +213 | 1757 |
| 203 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +205 | 33712 |
| 204 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +204 | 937 |
| 205 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +198 | 23640 |
| 206 | [usebruno/bruno](https://github.com/usebruno/bruno) | +198 | 41086 |
| 207 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +198 | 2699 |
| 208 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +197 | 1215 |
| 209 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +191 | 3544 |
| 210 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +187 | 1443 |
| 211 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +185 | 2316 |
| 212 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +183 | 2961 |
| 213 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +178 | 599 |
| 214 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +162 | 938 |
| 215 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +157 | 776 |
| 216 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +155 | 3833 |
| 217 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +151 | 1537 |
| 218 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +148 | 1373 |
| 219 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +148 | 941 |
| 220 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 221 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +145 | 22091 |
| 222 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +145 | 35473 |
| 223 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 957 |
| 224 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +127 | 818 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +127 | 29567 |
| 226 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +126 | 14048 |
| 227 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 812 |
| 228 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +121 | 29556 |
| 229 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +121 | 10744 |
| 230 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +115 | 3701 |
| 231 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +113 | 1076 |
| 232 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +113 | 12714 |
| 233 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +113 | 5225 |
| 234 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +112 | 23334 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +111 | 26556 |
| 236 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +110 | 1289 |
| 237 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +109 | 765 |
| 238 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +108 | 869 |
| 239 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +104 | 33000 |
| 240 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +102 | 1768 |
| 241 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +101 | 0 |
| 242 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +100 | 1141 |
| 243 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +100 | 2599 |
| 244 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +99 | 1276 |
| 245 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 246 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +96 | 498 |
| 247 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +96 | 1605 |
| 248 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +95 | 547 |
| 249 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +95 | 2172 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +94 | 48784 |
| 251 | [clawplays/ospec](https://github.com/clawplays/ospec) | +93 | 492 |
| 252 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +93 | 3931 |
| 253 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +88 | 1578 |
| 254 | [crimera/piko](https://github.com/crimera/piko) | +88 | 3201 |
| 255 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +87 | 1902 |
| 256 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +87 | 567 |
| 257 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +87 | 538 |
| 258 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +86 | 535 |
| 259 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +85 | 3561 |
| 260 | [microg/GmsCore](https://github.com/microg/GmsCore) | +85 | 12937 |
| 261 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +83 | 563 |
| 262 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +83 | 1893 |
| 263 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +81 | 1076 |
| 264 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +81 | 988 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +81 | 9254 |
| 266 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +80 | 770 |
| 267 | [robinebers/openusage](https://github.com/robinebers/openusage) | +78 | 1927 |
| 268 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +78 | 841 |
| 269 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +76 | 3685 |
| 270 | [openmemind/memind](https://github.com/openmemind/memind) | +75 | 409 |
| 271 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +74 | 45263 |
| 272 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +73 | 345 |
| 273 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +72 | 4025 |
| 274 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +72 | 27243 |
| 275 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +70 | 725 |
| 276 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +70 | 11618 |
| 277 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +69 | 490 |
| 278 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +69 | 441 |
| 279 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +69 | 1686 |
| 280 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +66 | 7250 |
| 281 | [idinging/freemail](https://github.com/idinging/freemail) | +66 | 1358 |
| 282 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +65 | 1357 |
| 283 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +61 | 516 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +61 | 31476 |
| 285 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +59 | 316 |
| 286 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +59 | 25403 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1579 |
| 288 | [apache/kafka](https://github.com/apache/kafka) | +58 | 32043 |
| 289 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +57 | 297 |
| 290 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +56 | 1773 |
| 291 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +54 | 37313 |
| 292 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +53 | 11646 |
| 293 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +52 | 391 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +52 | 28935 |
| 295 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +48 | 1693 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +46 | 8503 |
| 297 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +46 | 4677 |
| 298 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1676 |
| 299 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +43 | 489 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +38 | 10122 |
