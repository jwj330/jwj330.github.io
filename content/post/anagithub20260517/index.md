---
title: "2026-05-17 GitHub增长趋势报告"
description: "1.openhuman+294 2.academic-research-skills+218 3.CloakBrowser+164 4.codegraph+155 5.compozy+153"
date: 2026-05-17T20:54:58+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-17 20:54:58

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
        'daily': {"categories": ["gi-dellav/zerostack", "neilsonnn/image-blaster", "decolua/9router", "Tencent/TencentDB-Agent-Memory", "orailnoor/DroidDesk", "NVlabs/Sana", "joeseesun/qiaomu-anything-to-notebooklm", "anthropics/financial-services", "datawhalechina/easy-vibe", "Yuan1z0825/nature-skills", "withcoral/coral", "rohitg00/agentmemory", "Anil-matcha/Open-Generative-AI", "Hmbown/DeepSeek-TUI", "K-Dense-AI/scientific-agent-skills", "compozy/compozy", "colbymchenry/codegraph", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman"], "data": [77, 78, 78, 85, 91, 92, 94, 95, 98, 99, 102, 128, 131, 131, 150, 153, 155, 164, 218, 294]},
        'weekly': {"categories": ["Yuan1z0825/nature-skills", "AIDC-AI/Pixelle-Video", "TwilitRealm/dusklight", "fathah/hermes-desktop", "yikart/AiToEarn", "datawhalechina/easy-vibe", "decolua/9router", "Imbad0202/academic-research-skills", "datawhalechina/hello-agents", "floci-io/floci", "addyosmani/agent-skills", "antirez/ds4", "rohitg00/agentmemory", "anthropics/financial-services", "Hmbown/DeepSeek-TUI", "farion1231/cc-switch", "CloakHQ/CloakBrowser", "tinyhumansai/openhuman", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [342, 354, 366, 386, 399, 422, 460, 464, 492, 537, 565, 570, 632, 693, 754, 809, 883, 1007, 1125, 1765]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "rtk-ai/rtk", "heygen-com/hyperframes", "ruvnet/ruflo", "safishamsi/graphify", "Fincept-Corporation/FinceptTerminal", "JuliusBrussee/caveman", "addyosmani/agent-skills", "VoltAgent/awesome-design-md", "Hmbown/DeepSeek-TUI", "warpdotdev/warp", "garrytan/gstack", "farion1231/cc-switch", "Alishahryar1/free-claude-code", "TauricResearch/TradingAgents", "affaan-m/everything-claude-code", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [2404, 2557, 2571, 2608, 2691, 2808, 3028, 3048, 3057, 3081, 3114, 3154, 3178, 3219, 3329, 3468, 4656, 7815, 8149, 11325]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +294 | 12851 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +218 | 9239 |
| 3 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +164 | 13581 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +155 | 3219 |
| 5 | [compozy/compozy](https://github.com/compozy/compozy) | +153 | 2043 |
| 6 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +150 | 23751 |
| 7 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +131 | 31191 |
| 8 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +131 | 14993 |
| 9 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +128 | 11162 |
| 10 | [withcoral/coral](https://github.com/withcoral/coral) | +102 | 2294 |
| 11 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +99 | 7643 |
| 12 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +98 | 12238 |
| 13 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +95 | 24312 |
| 14 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +94 | 3667 |
| 15 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +92 | 6091 |
| 16 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +91 | 1360 |
| 17 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +85 | 2889 |
| 18 | [decolua/9router](https://github.com/decolua/9router) | +78 | 11536 |
| 19 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +78 | 3126 |
| 20 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +77 | 503 |
| 21 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +72 | 2782 |
| 22 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +71 | 763 |
| 23 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +70 | 42837 |
| 24 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +63 | 1017 |
| 25 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +63 | 14642 |
| 26 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +62 | 16461 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +61 | 36565 |
| 28 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +60 | 21500 |
| 29 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +59 | 549 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +59 | 17743 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1765 | 88712 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1125 | 133837 |
| 3 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1007 | 12851 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +883 | 13581 |
| 5 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +809 | 73438 |
| 6 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +754 | 31191 |
| 7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +693 | 24312 |
| 8 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +632 | 11163 |
| 9 | [antirez/ds4](https://github.com/antirez/ds4) | +570 | 10310 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +565 | 42837 |
| 11 | [floci-io/floci](https://github.com/floci-io/floci) | +537 | 11876 |
| 12 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +492 | 50396 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +464 | 9239 |
| 14 | [decolua/9router](https://github.com/decolua/9router) | +460 | 11536 |
| 15 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +422 | 12238 |
| 16 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +399 | 14642 |
| 17 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +386 | 5563 |
| 18 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +366 | 3876 |
| 19 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +354 | 17743 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +342 | 7643 |
| 21 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +341 | 34378 |
| 22 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +339 | 3587 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +332 | 17567 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +324 | 49291 |
| 25 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +318 | 23751 |
| 26 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +314 | 3126 |
| 27 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +301 | 48763 |
| 28 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +283 | 2106 |
| 29 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +282 | 9483 |
| 30 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +271 | 2889 |
| 31 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +269 | 17824 |
| 32 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +258 | 14993 |
| 33 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +251 | 21500 |
| 34 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +249 | 3219 |
| 35 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +232 | 5072 |
| 36 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +223 | 18970 |
| 37 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +217 | 16461 |
| 38 | [multica-ai/multica](https://github.com/multica-ai/multica) | +217 | 28999 |
| 39 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +216 | 9918 |
| 40 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +215 | 3667 |
| 41 | [withcoral/coral](https://github.com/withcoral/coral) | +212 | 2294 |
| 42 | [soxoj/maigret](https://github.com/soxoj/maigret) | +205 | 29148 |
| 43 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +199 | 2782 |
| 44 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +197 | 21459 |
| 45 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +196 | 3758 |
| 46 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +185 | 48649 |
| 47 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +183 | 8249 |
| 48 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +182 | 33859 |
| 49 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +180 | 36565 |
| 50 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +177 | 58829 |
| 51 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +175 | 25204 |
| 52 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +174 | 10240 |
| 53 | [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) | +164 | 1271 |
| 54 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +159 | 28407 |
| 55 | [compozy/compozy](https://github.com/compozy/compozy) | +153 | 2043 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +149 | 29129 |
| 57 | [jundot/omlx](https://github.com/jundot/omlx) | +148 | 14396 |
| 58 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +147 | 7910 |
| 59 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +146 | 38730 |
| 60 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +145 | 16962 |
| 61 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +143 | 2389 |
| 62 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +143 | 11647 |
| 63 | [larksuite/cli](https://github.com/larksuite/cli) | +141 | 11205 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +140 | 33144 |
| 65 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +140 | 60961 |
| 66 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +138 | 14006 |
| 67 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +134 | 17794 |
| 68 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +133 | 9555 |
| 69 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +133 | 10904 |
| 70 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +133 | 4135 |
| 71 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +130 | 1360 |
| 72 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +130 | 35490 |
| 73 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +130 | 31752 |
| 74 | [santifer/career-ops](https://github.com/santifer/career-ops) | +128 | 45174 |
| 75 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +128 | 53421 |
| 76 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +124 | 33283 |
| 77 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +123 | 19047 |
| 78 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +123 | 26320 |
| 79 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +122 | 6091 |
| 80 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +119 | 42640 |
| 81 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +116 | 7769 |
| 82 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +115 | 25222 |
| 83 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +113 | 23741 |
| 84 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +113 | 13039 |
| 85 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +113 | 5167 |
| 86 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +113 | 19602 |
| 87 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +111 | 1574 |
| 88 | [blader/humanizer](https://github.com/blader/humanizer) | +111 | 19276 |
| 89 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +111 | 25442 |
| 90 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +110 | 22071 |
| 91 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +109 | 1544 |
| 92 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +108 | 18592 |
| 93 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +106 | 11465 |
| 94 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +102 | 18935 |
| 95 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +101 | 9690 |
| 96 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +99 | 5555 |
| 97 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +97 | 7512 |
| 98 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +96 | 587 |
| 99 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +95 | 7580 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +93 | 15171 |
| 101 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +91 | 31540 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +87 | 19056 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +85 | 44040 |
| 104 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +83 | 6788 |
| 105 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +81 | 21398 |
| 106 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +80 | 1507 |
| 107 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +79 | 503 |
| 108 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +77 | 36799 |
| 109 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +74 | 763 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +73 | 13598 |
| 111 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | +73 | 1325 |
| 112 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +73 | 1852 |
| 113 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +73 | 6094 |
| 114 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +72 | 7739 |
| 115 | [OpenSquilla/opensquilla](https://github.com/OpenSquilla/opensquilla) | +70 | 966 |
| 116 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +70 | 21484 |
| 117 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +69 | 549 |
| 118 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +68 | 1088 |
| 119 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +68 | 25490 |
| 120 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +67 | 13095 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +11325 | 133837 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8149 | 88713 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7815 | 154618 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4656 | 60312 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3468 | 51199 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3329 | 30590 |
| 7 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3219 | 25204 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3178 | 73438 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3154 | 98491 |
| 10 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3114 | 58829 |
| 11 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3081 | 31191 |
| 12 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3057 | 80302 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3048 | 42837 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +3028 | 61308 |
| 15 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2808 | 21398 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2691 | 48763 |
| 17 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2608 | 52317 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2571 | 18970 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2557 | 49291 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2404 | 99028 |
| 21 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2357 | 55070 |
| 22 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2250 | 30678 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2147 | 109881 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2010 | 74774 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1893 | 13039 |
| 26 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1800 | 28999 |
| 27 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1770 | 50760 |
| 28 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1752 | 24312 |
| 29 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1726 | 13095 |
| 30 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1654 | 50674 |
| 31 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1617 | 10937 |
| 32 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1615 | 17743 |
| 33 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1600 | 14058 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1554 | 50396 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1553 | 34148 |
| 36 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1526 | 26162 |
| 37 | [github/spec-kit](https://github.com/github/spec-kit) | +1521 | 71722 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1472 | 17567 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1447 | 38730 |
| 40 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1412 | 66086 |
| 41 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1354 | 85286 |
| 42 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1347 | 59129 |
| 43 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1344 | 45174 |
| 44 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1307 | 14993 |
| 45 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1304 | 29148 |
| 46 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1286 | 20277 |
| 47 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1208 | 17794 |
| 48 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1202 | 13581 |
| 49 | [antirez/ds4](https://github.com/antirez/ds4) | +1199 | 10310 |
| 50 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1189 | 11647 |
| 51 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1176 | 19047 |
| 52 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1139 | 9483 |
| 53 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1086 | 62723 |
| 54 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1074 | 12851 |
| 55 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1059 | 81521 |
| 56 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1043 | 10239 |
| 57 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1036 | 53421 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1029 | 21459 |
| 59 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1007 | 26320 |
| 60 | [decolua/9router](https://github.com/decolua/9router) | +977 | 11536 |
| 61 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +967 | 16461 |
| 62 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +960 | 19602 |
| 63 | [openai/codex](https://github.com/openai/codex) | +955 | 61744 |
| 64 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +955 | 14970 |
| 65 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +950 | 14366 |
| 66 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +948 | 28407 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +925 | 29129 |
| 68 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +924 | 47221 |
| 69 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +923 | 6397 |
| 70 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +918 | 11163 |
| 71 | [openai/symphony](https://github.com/openai/symphony) | +909 | 23984 |
| 72 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +891 | 24037 |
| 73 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +887 | 48649 |
| 74 | [browser-use/video-use](https://github.com/browser-use/video-use) | +883 | 7741 |
| 75 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +874 | 12238 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +865 | 31752 |
| 77 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +842 | 26398 |
| 78 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +825 | 14941 |
| 79 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +823 | 25222 |
| 80 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +819 | 33144 |
| 81 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +815 | 60961 |
| 82 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +813 | 33859 |
| 83 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +808 | 47122 |
| 84 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +808 | 16669 |
| 85 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +807 | 36376 |
| 86 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +798 | 6133 |
| 87 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +794 | 36565 |
| 88 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +787 | 33878 |
| 89 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +778 | 37330 |
| 90 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +776 | 7643 |
| 91 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +760 | 9239 |
| 92 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +756 | 7512 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +755 | 7769 |
| 94 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +751 | 68158 |
| 95 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +750 | 61044 |
| 96 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +746 | 52372 |
| 97 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +735 | 19056 |
| 98 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +734 | 33283 |
| 99 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +732 | 6270 |
| 100 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +714 | 51085 |
| 101 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +703 | 21500 |
| 102 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +699 | 10904 |
| 103 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +685 | 7462 |
| 104 | [floci-io/floci](https://github.com/floci-io/floci) | +680 | 11876 |
| 105 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +655 | 5514 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +633 | 7580 |
| 107 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +629 | 7910 |
| 108 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +588 | 34378 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +580 | 44040 |
| 110 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +557 | 35490 |
| 111 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +553 | 23751 |
| 112 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +549 | 37822 |
| 113 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +545 | 5293 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +523 | 13598 |
| 115 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +520 | 20309 |
| 116 | [jundot/omlx](https://github.com/jundot/omlx) | +519 | 14396 |
| 117 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +515 | 18903 |
| 118 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +513 | 26030 |
| 119 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +501 | 21344 |
| 120 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +484 | 17824 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +483 | 15171 |
| 122 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +479 | 31540 |
| 123 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +466 | 18059 |
| 124 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +463 | 5555 |
| 125 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +462 | 5111 |
| 126 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +448 | 36907 |
| 127 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +423 | 36799 |
| 128 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +419 | 3388 |
| 129 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2628 |
| 130 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +405 | 6788 |
| 131 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +401 | 23022 |
| 132 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +397 | 39841 |
| 133 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +390 | 3452 |
| 134 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +382 | 9177 |
| 135 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +379 | 27374 |
| 136 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +371 | 7739 |
| 137 | [browserbase/skills](https://github.com/browserbase/skills) | +371 | 3305 |
| 138 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +368 | 5175 |
| 139 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +363 | 3667 |
| 140 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +363 | 9830 |
| 141 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +358 | 42659 |
| 142 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +356 | 33198 |
| 143 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +354 | 4946 |
| 144 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +350 | 13415 |
| 145 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +349 | 21484 |
| 146 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +347 | 4363 |
| 147 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +345 | 2459 |
| 148 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +345 | 2957 |
| 149 | [PostHog/posthog](https://github.com/PostHog/posthog) | +343 | 31767 |
| 150 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +341 | 12638 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +330 | 32251 |
| 152 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +324 | 3878 |
| 153 | [z-lab/dflash](https://github.com/z-lab/dflash) | +322 | 4619 |
| 154 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +321 | 2635 |
| 155 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +316 | 1653 |
| 156 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +313 | 32456 |
| 157 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +311 | 21722 |
| 158 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3827 |
| 159 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +309 | 26851 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +307 | 25483 |
| 161 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +303 | 9690 |
| 162 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +303 | 19567 |
| 163 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +302 | 13459 |
| 164 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +299 | 18774 |
| 165 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +294 | 2190 |
| 166 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +293 | 4353 |
| 167 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +291 | 37564 |
| 168 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +287 | 2254 |
| 169 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +286 | 2163 |
| 170 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +281 | 2106 |
| 171 | [openai/skills](https://github.com/openai/skills) | +278 | 19363 |
| 172 | [microsoft/qlib](https://github.com/microsoft/qlib) | +275 | 37792 |
| 173 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +271 | 1743 |
| 174 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +270 | 19723 |
| 175 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +269 | 4114 |
| 176 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +263 | 6064 |
| 177 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +261 | 3740 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +259 | 27753 |
| 179 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +250 | 2782 |
| 180 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +249 | 3777 |
| 181 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +238 | 2378 |
| 182 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +238 | 1983 |
| 183 | [88lin/video_vip](https://github.com/88lin/video_vip) | +236 | 1830 |
| 184 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +232 | 6996 |
| 185 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +230 | 5015 |
| 186 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +229 | 1886 |
| 187 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +218 | 3299 |
| 188 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +216 | 14009 |
| 189 | [tiagozip/cap](https://github.com/tiagozip/cap) | +216 | 6385 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +209 | 4440 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +189 | 26704 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +185 | 3532 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +182 | 36103 |
| 194 | [eze-is/web-access](https://github.com/eze-is/web-access) | +166 | 6524 |
| 195 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +165 | 10270 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +164 | 2554 |
| 197 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +157 | 5943 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +153 | 16743 |
| 199 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +151 | 2971 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +145 | 15138 |
| 201 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +143 | 39596 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +139 | 8788 |
| 203 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +138 | 1306 |
| 204 | [playcanvas/engine](https://github.com/playcanvas/engine) | +138 | 15812 |
| 205 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +135 | 9891 |
| 206 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +134 | 7876 |
| 207 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +132 | 3373 |
| 208 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +131 | 22952 |
| 209 | [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | +116 | 775 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +113 | 41086 |
| 211 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +109 | 735 |
| 212 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 817 |
| 213 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +105 | 10305 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +104 | 40265 |
| 215 | [sandeco/reversa](https://github.com/sandeco/reversa) | +102 | 861 |
| 216 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 1850 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +99 | 35473 |
| 218 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +94 | 1017 |
| 219 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +94 | 7758 |
| 220 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +94 | 24043 |
| 221 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +92 | 877 |
| 222 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +92 | 3805 |
| 223 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +92 | 1438 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +88 | 11763 |
| 225 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +88 | 1336 |
| 226 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +83 | 927 |
| 227 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +83 | 689 |
| 228 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +80 | 3159 |
| 229 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +79 | 30112 |
| 230 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +78 | 8323 |
| 231 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +78 | 9901 |
| 232 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +74 | 1304 |
| 233 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +70 | 763 |
| 234 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +69 | 2423 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +67 | 13313 |
| 236 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +67 | 4245 |
| 237 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 238 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +67 | 37313 |
| 239 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +66 | 447 |
| 240 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +66 | 2544 |
| 241 | [halo-dev/halo](https://github.com/halo-dev/halo) | +64 | 37991 |
| 242 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +62 | 549 |
| 243 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +62 | 1793 |
| 244 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +62 | 48784 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +61 | 2124 |
| 246 | [robinebers/openusage](https://github.com/robinebers/openusage) | +59 | 2489 |
| 247 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +59 | 33000 |
| 248 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +59 | 27581 |
| 249 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +58 | 3093 |
| 250 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +57 | 11193 |
| 251 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +56 | 658 |
| 252 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +56 | 2117 |
| 253 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +55 | 811 |
| 254 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +54 | 4272 |
| 255 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +53 | 934 |
| 256 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +53 | 2120 |
| 257 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +53 | 319 |
| 258 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +52 | 4082 |
| 259 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +52 | 464 |
| 260 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +51 | 886 |
| 261 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +50 | 446 |
| 262 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 508 |
| 263 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 299 |
| 264 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +50 | 1432 |
| 265 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +49 | 3093 |
| 266 | [openmemind/memind](https://github.com/openmemind/memind) | +49 | 758 |
| 267 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +48 | 1704 |
| 268 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +47 | 4170 |
| 269 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +47 | 1218 |
| 270 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +46 | 468 |
| 271 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 321 |
| 272 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +43 | 12009 |
| 273 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +42 | 2160 |
| 274 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +41 | 597 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +40 | 1891 |
| 276 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +39 | 314 |
| 277 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +39 | 9635 |
| 278 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +38 | 5110 |
| 279 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +38 | 456 |
| 280 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +37 | 238 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +36 | 2377 |
| 282 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +36 | 319 |
| 283 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1406 |
| 284 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +34 | 5390 |
| 285 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +34 | 266 |
| 286 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +33 | 197 |
| 287 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +33 | 2215 |
| 288 | [intave/intave](https://github.com/intave/intave) | +31 | 255 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +30 | 1537 |
| 290 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 291 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +28 | 199 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2189 |
| 293 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +27 | 2632 |
| 294 | [is-a-dev/register](https://github.com/is-a-dev/register) | +25 | 10304 |
| 295 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +25 | 2944 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +24 | 1919 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +23 | 849 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +23 | 260 |
| 299 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +22 | 3230 |
| 300 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +22 | 439 |
