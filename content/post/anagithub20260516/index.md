---
title: "2026-05-16 GitHub增长趋势报告"
description: "1.image-blaster+187 2.openhuman+182 3.CloakBrowser+90 4.agentmemory+81 5.scientific-agent-skills+79"
date: 2026-05-16T20:51:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-16 20:51:23

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
        'daily': {"categories": ["crynta/terax-ai", "badlogic/pi-mono", "Light-Heart-Labs/DreamServer", "Imbad0202/academic-research-skills", "hugohe3/ppt-master", "OpenCut-app/OpenCut", "floci-io/floci", "addyosmani/agent-skills", "anthropics/financial-services", "datawhalechina/easy-vibe", "withcoral/coral", "Tencent/TencentDB-Agent-Memory", "joeseesun/qiaomu-anything-to-notebooklm", "jackwener/OpenCLI", "Hmbown/DeepSeek-TUI", "K-Dense-AI/scientific-agent-skills", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "tinyhumansai/openhuman", "neilsonnn/image-blaster"], "data": [54, 54, 56, 57, 59, 60, 61, 62, 64, 67, 67, 73, 74, 77, 78, 79, 81, 90, 182, 187]},
        'weekly': {"categories": ["badlogic/pi-mono", "crynta/terax-ai", "bytedance/UI-TARS-desktop", "yikart/AiToEarn", "datawhalechina/easy-vibe", "ruvnet/ruflo", "TwilitRealm/dusklight", "decolua/9router", "floci-io/floci", "datawhalechina/hello-agents", "rohitg00/agentmemory", "addyosmani/agent-skills", "tinyhumansai/openhuman", "Hmbown/DeepSeek-TUI", "CloakHQ/CloakBrowser", "farion1231/cc-switch", "anthropics/financial-services", "antirez/ds4", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [380, 399, 418, 426, 441, 486, 492, 520, 560, 586, 650, 676, 767, 810, 822, 838, 885, 901, 1068, 1658]},
        'monthly': {"categories": ["thedotmack/claude-mem", "ruvnet/ruflo", "rtk-ai/rtk", "heygen-com/hyperframes", "safishamsi/graphify", "Fincept-Corporation/FinceptTerminal", "Hmbown/DeepSeek-TUI", "addyosmani/agent-skills", "warpdotdev/warp", "farion1231/cc-switch", "garrytan/gstack", "Alishahryar1/free-claude-code", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "TauricResearch/TradingAgents", "affaan-m/everything-claude-code", "obra/superpowers", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2544, 2557, 2576, 2760, 2771, 2823, 2963, 3040, 3087, 3099, 3157, 3191, 3202, 3274, 3325, 3448, 4655, 7864, 7981, 11822]}
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
| 1 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +187 | 2749 |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +182 | 10563 |
| 3 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +90 | 12527 |
| 4 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +81 | 10227 |
| 5 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +79 | 23053 |
| 6 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +78 | 30480 |
| 7 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +77 | 21218 |
| 8 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +74 | 3172 |
| 9 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +73 | 2300 |
| 10 | [withcoral/coral](https://github.com/withcoral/coral) | +67 | 1953 |
| 11 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +67 | 11705 |
| 12 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +64 | 23760 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +62 | 42463 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +61 | 11526 |
| 15 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +60 | 46013 |
| 16 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +59 | 17219 |
| 17 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +57 | 8051 |
| 18 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +56 | 886 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +54 | 50343 |
| 20 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +54 | 3312 |
| 21 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +52 | 51880 |
| 22 | [decolua/9router](https://github.com/decolua/9router) | +51 | 11063 |
| 23 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +51 | 2409 |
| 24 | [amruthpillai/reactive-resume](https://github.com/amruthpillai/reactive-resume) | +51 | 35410 |
| 25 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +50 | 42363 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +48 | 48897 |
| 27 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +45 | 2272 |
| 28 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +42 | 35113 |
| 29 | [larksuite/cli](https://github.com/larksuite/cli) | +41 | 11007 |
| 30 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +40 | 1298 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1658 | 86687 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1068 | 132378 |
| 3 | [antirez/ds4](https://github.com/antirez/ds4) | +901 | 10019 |
| 4 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +885 | 23760 |
| 5 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +838 | 72612 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +822 | 12527 |
| 7 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +810 | 30480 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +767 | 10563 |
| 9 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +676 | 42463 |
| 10 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +650 | 10227 |
| 11 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +586 | 50116 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +560 | 11526 |
| 13 | [decolua/9router](https://github.com/decolua/9router) | +520 | 11063 |
| 14 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +492 | 3801 |
| 15 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +486 | 51880 |
| 16 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +441 | 11705 |
| 17 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +426 | 14259 |
| 18 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +418 | 34222 |
| 19 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +399 | 3312 |
| 20 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +380 | 50343 |
| 21 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +375 | 3686 |
| 22 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +369 | 5352 |
| 23 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +367 | 17427 |
| 24 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +353 | 48546 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +350 | 7079 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +348 | 17219 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +337 | 48897 |
| 28 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +296 | 8051 |
| 29 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +279 | 9235 |
| 30 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +271 | 17534 |
| 31 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +271 | 8144 |
| 32 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +261 | 4980 |
| 33 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +255 | 9758 |
| 34 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +248 | 2749 |
| 35 | [soxoj/maigret](https://github.com/soxoj/maigret) | +246 | 28977 |
| 36 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +238 | 3373 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +230 | 18654 |
| 38 | [multica-ai/multica](https://github.com/multica-ai/multica) | +226 | 28841 |
| 39 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +226 | 16131 |
| 40 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +221 | 2323 |
| 41 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +206 | 21218 |
| 42 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +204 | 24996 |
| 43 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +203 | 21283 |
| 44 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +195 | 33726 |
| 45 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +191 | 2300 |
| 46 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +187 | 58730 |
| 47 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +182 | 23053 |
| 48 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +181 | 7806 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +179 | 48478 |
| 50 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +174 | 14339 |
| 51 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +171 | 10828 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +160 | 28218 |
| 53 | [jundot/omlx](https://github.com/jundot/omlx) | +160 | 14304 |
| 54 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +159 | 11592 |
| 55 | [openai/symphony](https://github.com/openai/symphony) | +157 | 23939 |
| 56 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +156 | 46013 |
| 57 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +156 | 10033 |
| 58 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +153 | 39770 |
| 59 | [withcoral/coral](https://github.com/withcoral/coral) | +152 | 1953 |
| 60 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +151 | 38627 |
| 61 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +150 | 60811 |
| 62 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +147 | 36211 |
| 63 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +147 | 7444 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +146 | 28954 |
| 65 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +146 | 4410 |
| 66 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +143 | 31592 |
| 67 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +143 | 9468 |
| 68 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +142 | 17646 |
| 69 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +141 | 4505 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +139 | 32951 |
| 71 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +138 | 14852 |
| 72 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +136 | 4070 |
| 73 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +134 | 53287 |
| 74 | [santifer/career-ops](https://github.com/santifer/career-ops) | +133 | 45018 |
| 75 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +130 | 5404 |
| 76 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +129 | 3172 |
| 77 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +128 | 2272 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +128 | 19479 |
| 79 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +126 | 25145 |
| 80 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +126 | 26022 |
| 81 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +126 | 18936 |
| 82 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +125 | 33167 |
| 83 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +125 | 6217 |
| 84 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +122 | 1379 |
| 85 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +122 | 21301 |
| 86 | [larksuite/cli](https://github.com/larksuite/cli) | +118 | 11007 |
| 87 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +118 | 7684 |
| 88 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +118 | 5021 |
| 89 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +117 | 35113 |
| 90 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +114 | 25306 |
| 91 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +111 | 18475 |
| 92 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +108 | 13889 |
| 93 | [blader/humanizer](https://github.com/blader/humanizer) | +107 | 19155 |
| 94 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +107 | 12925 |
| 95 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +105 | 2409 |
| 96 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +104 | 16799 |
| 97 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +104 | 42363 |
| 98 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +104 | 3266 |
| 99 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +104 | 2353 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +102 | 7451 |
| 101 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +101 | 21957 |
| 102 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +100 | 1462 |
| 103 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +100 | 31466 |
| 104 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +99 | 11255 |
| 105 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +98 | 1321 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +91 | 43945 |
| 107 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +91 | 7685 |
| 108 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +90 | 9485 |
| 109 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +90 | 18966 |
| 110 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +88 | 15054 |
| 111 | [z-lab/dflash](https://github.com/z-lab/dflash) | +87 | 4602 |
| 112 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +84 | 37719 |
| 113 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +82 | 36799 |
| 114 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +81 | 6747 |
| 115 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +78 | 21409 |
| 116 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +76 | 1298 |
| 117 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +75 | 970 |
| 118 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +73 | 1826 |
| 119 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +73 | 1795 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +70 | 13502 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +11822 | 132379 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7981 | 153269 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7864 | 86688 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4655 | 60312 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3448 | 51199 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3325 | 30590 |
| 7 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3274 | 79800 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +3202 | 60993 |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3191 | 24996 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3157 | 97979 |
| 11 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3099 | 72612 |
| 12 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3087 | 58730 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3040 | 42463 |
| 14 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +2963 | 30480 |
| 15 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2823 | 21301 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2771 | 48546 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2760 | 18654 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2576 | 48897 |
| 19 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2557 | 51880 |
| 20 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2544 | 30678 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2401 | 98390 |
| 22 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2317 | 55070 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2151 | 109881 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2029 | 74774 |
| 25 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1897 | 28841 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1866 | 12925 |
| 27 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1753 | 50343 |
| 28 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1712 | 13037 |
| 29 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1674 | 23760 |
| 30 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1661 | 50398 |
| 31 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1612 | 20242 |
| 32 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1599 | 10875 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1592 | 34148 |
| 34 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1588 | 13962 |
| 35 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1566 | 17427 |
| 36 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1562 | 26145 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1552 | 50116 |
| 38 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1464 | 65866 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1451 | 38627 |
| 40 | [github/spec-kit](https://github.com/github/spec-kit) | +1449 | 71722 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1446 | 17220 |
| 42 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1428 | 45018 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1331 | 85286 |
| 44 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1279 | 11592 |
| 45 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1277 | 28977 |
| 46 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1231 | 69674 |
| 47 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1223 | 17646 |
| 48 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1202 | 58237 |
| 49 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1191 | 14339 |
| 50 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1190 | 18936 |
| 51 | [antirez/ds4](https://github.com/antirez/ds4) | +1153 | 10019 |
| 52 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1116 | 62564 |
| 53 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1115 | 9235 |
| 54 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1096 | 81382 |
| 55 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1082 | 26022 |
| 56 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1068 | 53287 |
| 57 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1044 | 12527 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1024 | 21283 |
| 59 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1008 | 10033 |
| 60 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1004 | 19479 |
| 61 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +981 | 6375 |
| 62 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +968 | 28218 |
| 63 | [openai/codex](https://github.com/openai/codex) | +966 | 61744 |
| 64 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +965 | 14324 |
| 65 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +953 | 16131 |
| 66 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +950 | 14879 |
| 67 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +938 | 47181 |
| 68 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +923 | 24016 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +915 | 28954 |
| 70 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +913 | 26361 |
| 71 | [decolua/9router](https://github.com/decolua/9router) | +910 | 11063 |
| 72 | [openai/symphony](https://github.com/openai/symphony) | +908 | 23939 |
| 73 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +887 | 48478 |
| 74 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +881 | 31592 |
| 75 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +853 | 25145 |
| 76 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +849 | 60811 |
| 77 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +845 | 36314 |
| 78 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +830 | 16619 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +824 | 33726 |
| 80 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +821 | 32951 |
| 81 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +814 | 14852 |
| 82 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +809 | 47122 |
| 83 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +806 | 33878 |
| 84 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +804 | 10563 |
| 85 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +802 | 10227 |
| 86 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +794 | 11705 |
| 87 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +790 | 52330 |
| 88 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +788 | 37330 |
| 89 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +777 | 5994 |
| 90 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +772 | 7442 |
| 91 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +771 | 60921 |
| 92 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +766 | 67999 |
| 93 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +760 | 18966 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +759 | 33167 |
| 95 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +757 | 5984 |
| 96 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +752 | 36212 |
| 97 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +749 | 7444 |
| 98 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +745 | 7684 |
| 99 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +718 | 6217 |
| 100 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +718 | 10828 |
| 101 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +696 | 7806 |
| 102 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +689 | 7079 |
| 103 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +667 | 21218 |
| 104 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +642 | 5437 |
| 105 | [floci-io/floci](https://github.com/floci-io/floci) | +637 | 11526 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +636 | 7451 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +594 | 43945 |
| 108 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +580 | 37719 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +562 | 35113 |
| 110 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +561 | 8051 |
| 111 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +551 | 5245 |
| 112 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +534 | 18822 |
| 113 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +533 | 21319 |
| 114 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +531 | 20275 |
| 115 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +526 | 25964 |
| 116 | [jundot/omlx](https://github.com/jundot/omlx) | +523 | 14304 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +507 | 13502 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +490 | 15054 |
| 119 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +483 | 18020 |
| 120 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +481 | 31466 |
| 121 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +463 | 5071 |
| 122 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +453 | 5404 |
| 123 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +451 | 17534 |
| 124 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +447 | 36907 |
| 125 | [google/magika](https://github.com/google/magika) | +444 | 17007 |
| 126 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +435 | 6747 |
| 127 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +433 | 23053 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +422 | 36799 |
| 129 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +414 | 3315 |
| 130 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +410 | 22939 |
| 131 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2624 |
| 132 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +402 | 39841 |
| 133 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +386 | 3388 |
| 134 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +376 | 27331 |
| 135 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +373 | 9151 |
| 136 | [browserbase/skills](https://github.com/browserbase/skills) | +368 | 3275 |
| 137 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +367 | 33134 |
| 138 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +364 | 7685 |
| 139 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +364 | 12610 |
| 140 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +360 | 9803 |
| 141 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +357 | 4923 |
| 142 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +356 | 42591 |
| 143 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +355 | 5079 |
| 144 | [z-lab/dflash](https://github.com/z-lab/dflash) | +353 | 4602 |
| 145 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +353 | 13344 |
| 146 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +350 | 21409 |
| 147 | [PostHog/posthog](https://github.com/PostHog/posthog) | +342 | 31767 |
| 148 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +342 | 2907 |
| 149 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +340 | 2425 |
| 150 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +340 | 4299 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +326 | 32188 |
| 152 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +324 | 3877 |
| 153 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +316 | 13435 |
| 154 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +315 | 2584 |
| 155 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +315 | 1643 |
| 156 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +310 | 21648 |
| 157 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +310 | 32378 |
| 158 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +309 | 3810 |
| 159 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +308 | 26798 |
| 160 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +304 | 18719 |
| 161 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +302 | 19488 |
| 162 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +300 | 25419 |
| 163 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +294 | 9485 |
| 164 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +293 | 4335 |
| 165 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +292 | 37564 |
| 166 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +290 | 2169 |
| 167 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +286 | 2136 |
| 168 | [openai/skills](https://github.com/openai/skills) | +285 | 19238 |
| 169 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +284 | 2133 |
| 170 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +278 | 3687 |
| 171 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +277 | 3172 |
| 172 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +276 | 22849 |
| 173 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +275 | 19662 |
| 174 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +270 | 1721 |
| 175 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +263 | 6019 |
| 176 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +261 | 4094 |
| 177 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +260 | 1977 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +250 | 27694 |
| 179 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +245 | 5000 |
| 180 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +236 | 2353 |
| 181 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +235 | 3686 |
| 182 | [88lin/video_vip](https://github.com/88lin/video_vip) | +233 | 1816 |
| 183 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +229 | 1875 |
| 184 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +228 | 2372 |
| 185 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +227 | 6965 |
| 186 | [tiagozip/cap](https://github.com/tiagozip/cap) | +217 | 6378 |
| 187 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +216 | 13964 |
| 188 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +208 | 4393 |
| 189 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +205 | 3220 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +203 | 36103 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +192 | 26658 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +185 | 3502 |
| 193 | [eze-is/web-access](https://github.com/eze-is/web-access) | +176 | 6494 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +167 | 2522 |
| 195 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +163 | 10238 |
| 196 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +151 | 5892 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +145 | 16695 |
| 198 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +142 | 2931 |
| 199 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +142 | 39596 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +142 | 8783 |
| 201 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +140 | 3370 |
| 202 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +137 | 7866 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +137 | 15103 |
| 204 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +136 | 9856 |
| 205 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +135 | 1257 |
| 206 | [playcanvas/engine](https://github.com/playcanvas/engine) | +134 | 15797 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +129 | 22920 |
| 208 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +123 | 875 |
| 209 | [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | +116 | 772 |
| 210 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +109 | 684 |
| 211 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +109 | 729 |
| 212 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +104 | 40265 |
| 213 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +103 | 802 |
| 214 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +100 | 7756 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +99 | 10289 |
| 216 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +97 | 3784 |
| 217 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +97 | 1330 |
| 218 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +97 | 35473 |
| 219 | [sandeco/reversa](https://github.com/sandeco/reversa) | +95 | 837 |
| 220 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 1827 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +94 | 1413 |
| 222 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +92 | 24023 |
| 223 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +91 | 11745 |
| 224 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +83 | 1292 |
| 225 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +82 | 903 |
| 226 | [usebruno/bruno](https://github.com/usebruno/bruno) | +80 | 41086 |
| 227 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +80 | 3139 |
| 228 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +79 | 30099 |
| 229 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +75 | 3751 |
| 230 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +75 | 8318 |
| 231 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +74 | 9893 |
| 232 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 445 |
| 233 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +69 | 482 |
| 234 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +68 | 37313 |
| 235 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2417 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +67 | 2544 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +66 | 13301 |
| 238 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 239 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +65 | 2115 |
| 240 | [halo-dev/halo](https://github.com/halo-dev/halo) | +65 | 37991 |
| 241 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +62 | 1786 |
| 242 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +61 | 2110 |
| 243 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 244 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +59 | 4210 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +58 | 33000 |
| 246 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +57 | 655 |
| 247 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +57 | 11177 |
| 248 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2470 |
| 249 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +55 | 797 |
| 250 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +55 | 4262 |
| 251 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +54 | 27567 |
| 252 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +53 | 1423 |
| 253 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 464 |
| 254 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +52 | 925 |
| 255 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +52 | 3074 |
| 256 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +52 | 2093 |
| 257 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 314 |
| 258 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +51 | 2723 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +51 | 749 |
| 260 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 297 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +50 | 4076 |
| 262 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +50 | 363 |
| 263 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 505 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +49 | 1695 |
| 265 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +49 | 4168 |
| 266 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 438 |
| 267 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +48 | 881 |
| 268 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +48 | 3084 |
| 269 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +44 | 465 |
| 270 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +44 | 12005 |
| 271 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 318 |
| 272 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +40 | 2144 |
| 273 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +40 | 1881 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +39 | 9632 |
| 275 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +38 | 5105 |
| 276 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +37 | 566 |
| 277 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +37 | 448 |
| 278 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +36 | 303 |
| 279 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +36 | 237 |
| 280 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +35 | 2369 |
| 281 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1399 |
| 282 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +35 | 5363 |
| 283 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +35 | 317 |
| 284 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +34 | 502 |
| 285 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +33 | 196 |
| 286 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +33 | 2214 |
| 287 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +32 | 260 |
| 288 | [intave/intave](https://github.com/intave/intave) | +31 | 255 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +31 | 1534 |
| 290 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +28 | 751 |
| 291 | [is-a-dev/register](https://github.com/is-a-dev/register) | +27 | 10295 |
| 292 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +26 | 193 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +26 | 1916 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +25 | 2188 |
| 295 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +24 | 2629 |
| 296 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +24 | 2941 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +22 | 849 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +22 | 241 |
| 299 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +21 | 3228 |
| 300 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +21 | 436 |
