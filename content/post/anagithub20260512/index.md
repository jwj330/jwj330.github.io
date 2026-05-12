---
title: "2026-05-12 GitHub增长趋势报告"
description: "1.floci+118 2.financial-services-plugins+111 3.CloakBrowser+109 4.hermes-desktop+106 5.terax-ai+102"
date: 2026-05-12T21:22:04+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-12 21:22:04

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
        'daily': {"categories": ["badlogic/pi-mono", "hugohe3/ppt-master", "millionco/react-doctor", "AIDC-AI/Pixelle-Video", "ruvnet/ruflo", "safishamsi/graphify", "datawhalechina/hello-agents", "datawhalechina/easy-vibe", "addyosmani/agent-skills", "bytedance/UI-TARS-desktop", "op7418/guizang-ppt-skill", "tinyhumansai/openhuman", "yikart/AiToEarn", "rohitg00/agentmemory", "decolua/9router", "crynta/terax-ai", "fathah/hermes-desktop", "CloakHQ/CloakBrowser", "anthropics/financial-services-plugins", "floci-io/floci"], "data": [42, 43, 46, 51, 52, 58, 64, 65, 67, 68, 74, 77, 80, 80, 89, 102, 106, 109, 111, 118]},
        'weekly': {"categories": ["hugohe3/ppt-master", "D4Vinci/Scrapling", "badlogic/pi-mono", "datawhalechina/easy-vibe", "safishamsi/graphify", "rtk-ai/rtk", "vercel-labs/zero-native", "bytedance/UI-TARS-desktop", "AIDC-AI/Pixelle-Video", "decolua/9router", "CloakHQ/CloakBrowser", "TauricResearch/TradingAgents", "datawhalechina/hello-agents", "ruvnet/ruflo", "farion1231/cc-switch", "addyosmani/agent-skills", "NousResearch/hermes-agent", "mattpocock/skills", "anthropics/financial-services-plugins", "forrestchang/andrej-karpathy-skills"], "data": [381, 385, 393, 394, 397, 428, 443, 459, 479, 591, 608, 615, 663, 695, 949, 1184, 1347, 1412, 1420, 1421]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "heygen-com/hyperframes", "multica-ai/multica", "Fincept-Corporation/FinceptTerminal", "rtk-ai/rtk", "warpdotdev/warp", "Alishahryar1/free-claude-code", "farion1231/cc-switch", "TauricResearch/TradingAgents", "addyosmani/agent-skills", "garrytan/gstack", "safishamsi/graphify", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "obra/superpowers", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2557, 2681, 2707, 2797, 2899, 3031, 3136, 3152, 3348, 3407, 3431, 3496, 3987, 4038, 4539, 4913, 5311, 7219, 12355, 15615]}
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
| 1 | [floci-io/floci](https://github.com/floci-io/floci) | +118 | 8236 |
| 2 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +111 | 21402 |
| 3 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +109 | 7668 |
| 4 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +106 | 3794 |
| 5 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +102 | 2580 |
| 6 | [decolua/9router](https://github.com/decolua/9router) | +89 | 9288 |
| 7 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +80 | 5728 |
| 8 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +80 | 11771 |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +77 | 2540 |
| 10 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +74 | 7874 |
| 11 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +68 | 33500 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +67 | 40341 |
| 13 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +65 | 10394 |
| 14 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +64 | 48168 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +58 | 47188 |
| 16 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +52 | 49681 |
| 17 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +51 | 15587 |
| 18 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +46 | 8703 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +43 | 15264 |
| 20 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +42 | 48581 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +41 | 46691 |
| 22 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +40 | 12893 |
| 23 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +39 | 6471 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +36 | 27687 |
| 25 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | +36 | 4810 |
| 26 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +35 | 46013 |
| 27 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +34 | 2881 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +33 | 4953 |
| 29 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +32 | 35586 |
| 30 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +32 | 24877 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1421 | 126849 |
| 2 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1420 | 21402 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1412 | 75749 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1347 | 146733 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1184 | 40341 |
| 6 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +949 | 68587 |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +695 | 49681 |
| 8 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +663 | 48168 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +615 | 30590 |
| 10 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +608 | 7668 |
| 11 | [decolua/9router](https://github.com/decolua/9router) | +591 | 9288 |
| 12 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +479 | 15587 |
| 13 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +459 | 33500 |
| 14 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +443 | 2881 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +428 | 46691 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +397 | 47188 |
| 17 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +394 | 10394 |
| 18 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +393 | 48581 |
| 19 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +385 | 49111 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +381 | 15264 |
| 21 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +367 | 5728 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +364 | 4953 |
| 23 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +350 | 3806 |
| 24 | [floci-io/floci](https://github.com/floci-io/floci) | +341 | 8236 |
| 25 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +339 | 2580 |
| 26 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +321 | 30831 |
| 27 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +316 | 7680 |
| 28 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +314 | 57939 |
| 29 | [soxoj/maigret](https://github.com/soxoj/maigret) | +313 | 28093 |
| 30 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +296 | 3257 |
| 31 | [multica-ai/multica](https://github.com/multica-ai/multica) | +289 | 27687 |
| 32 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +277 | 24087 |
| 33 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +276 | 16524 |
| 34 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +276 | 17590 |
| 35 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +269 | 4411 |
| 36 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +267 | 42334 |
| 37 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +258 | 16446 |
| 38 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +252 | 11771 |
| 39 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +250 | 7357 |
| 40 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +248 | 3794 |
| 41 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +248 | 7118 |
| 42 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +247 | 20264 |
| 43 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +247 | 7874 |
| 44 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +238 | 10319 |
| 45 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +229 | 8703 |
| 46 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +225 | 11064 |
| 47 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +224 | 2209 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +223 | 15154 |
| 49 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +222 | 6349 |
| 50 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +219 | 32826 |
| 51 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +219 | 2701 |
| 52 | [openai/symphony](https://github.com/openai/symphony) | +219 | 23513 |
| 53 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +214 | 14309 |
| 54 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +213 | 5910 |
| 55 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +208 | 27252 |
| 56 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +200 | 37967 |
| 57 | [jundot/omlx](https://github.com/jundot/omlx) | +198 | 13789 |
| 58 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +194 | 60031 |
| 59 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +191 | 47310 |
| 60 | [strukto-ai/mirage](https://github.com/strukto-ai/mirage) | +188 | 2052 |
| 61 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +184 | 2540 |
| 62 | [z-lab/dflash](https://github.com/z-lab/dflash) | +183 | 4480 |
| 63 | [virattt/dexter](https://github.com/virattt/dexter) | +181 | 25464 |
| 64 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +177 | 4794 |
| 65 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +174 | 12998 |
| 66 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +173 | 1614 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +171 | 32314 |
| 68 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +171 | 16999 |
| 69 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +169 | 2290 |
| 70 | [santifer/career-ops](https://github.com/santifer/career-ops) | +168 | 44268 |
| 71 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +168 | 30689 |
| 72 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +168 | 8826 |
| 73 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +167 | 52649 |
| 74 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +166 | 12302 |
| 75 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +164 | 4227 |
| 76 | [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | +162 | 1674 |
| 77 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +161 | 7452 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +161 | 39363 |
| 79 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +161 | 2624 |
| 80 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +160 | 35586 |
| 81 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +160 | 8843 |
| 82 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +156 | 14512 |
| 83 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +156 | 9671 |
| 84 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +155 | 22954 |
| 85 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +154 | 18792 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +152 | 20300 |
| 87 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +146 | 4115 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +145 | 28105 |
| 89 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +144 | 20937 |
| 90 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +140 | 21165 |
| 91 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +140 | 9561 |
| 92 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +135 | 18508 |
| 93 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +135 | 1086 |
| 94 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +134 | 3378 |
| 95 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +133 | 13401 |
| 96 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +129 | 1309 |
| 97 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +128 | 21336 |
| 98 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +126 | 32528 |
| 99 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +126 | 35967 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +122 | 6914 |
| 101 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +122 | 3415 |
| 102 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +118 | 25145 |
| 103 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +115 | 24050 |
| 104 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +111 | 12137 |
| 105 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +99 | 1675 |
| 106 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +98 | 1174 |
| 107 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +96 | 37314 |
| 108 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +93 | 43514 |
| 109 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +93 | 44232 |
| 110 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +92 | 3837 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +91 | 13140 |
| 112 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +91 | 16247 |
| 113 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +89 | 18453 |
| 114 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +89 | 5808 |
| 115 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +88 | 3168 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +86 | 36799 |
| 117 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +85 | 3988 |
| 118 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +84 | 1722 |
| 119 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +83 | 25640 |
| 120 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +81 | 34308 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +15615 | 126849 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +12355 | 146733 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7219 | 75749 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +5311 | 60312 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4913 | 58961 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +4539 | 76474 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4038 | 51199 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3987 | 30678 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3496 | 47188 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3431 | 94664 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3407 | 40341 |
| 12 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3348 | 30590 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3152 | 68587 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3136 | 24087 |
| 15 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3031 | 57939 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2899 | 46692 |
| 17 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2797 | 20937 |
| 18 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2707 | 27687 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2681 | 17591 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2557 | 96455 |
| 21 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2487 | 49681 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2369 | 109881 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +2281 | 74774 |
| 24 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2279 | 20104 |
| 25 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2245 | 55070 |
| 26 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2223 | 52649 |
| 27 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1912 | 44268 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1866 | 34148 |
| 29 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1826 | 48581 |
| 30 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1821 | 12302 |
| 31 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1746 | 64781 |
| 32 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1677 | 49111 |
| 33 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1666 | 12501 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1647 | 48168 |
| 35 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1564 | 26073 |
| 36 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1562 | 10382 |
| 37 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1554 | 13401 |
| 38 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1546 | 85286 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1535 | 37967 |
| 40 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1510 | 15587 |
| 41 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1509 | 21402 |
| 42 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +1506 | 52060 |
| 43 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1474 | 18792 |
| 44 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1470 | 25459 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1455 | 15154 |
| 46 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1436 | 11064 |
| 47 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1436 | 61760 |
| 48 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1432 | 18508 |
| 49 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1418 | 69674 |
| 50 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1413 | 80674 |
| 51 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1398 | 15264 |
| 52 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1392 | 24050 |
| 53 | [github/spec-kit](https://github.com/github/spec-kit) | +1340 | 71722 |
| 54 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1288 | 18453 |
| 55 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1260 | 16999 |
| 56 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1210 | 12998 |
| 57 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1203 | 28093 |
| 58 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1178 | 10319 |
| 59 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1140 | 23840 |
| 60 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1133 | 20264 |
| 61 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1110 | 60031 |
| 62 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1107 | 35967 |
| 63 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1098 | 16247 |
| 64 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1082 | 47031 |
| 65 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1078 | 27252 |
| 66 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1077 | 30689 |
| 67 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1054 | 28388 |
| 68 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1033 | 45886 |
| 69 | [openai/codex](https://github.com/openai/codex) | +1031 | 61744 |
| 70 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1005 | 14075 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +999 | 28105 |
| 72 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +998 | 7874 |
| 73 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +992 | 33878 |
| 74 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +990 | 6161 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +989 | 32314 |
| 76 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +977 | 60329 |
| 77 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +971 | 14512 |
| 78 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +965 | 47310 |
| 79 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +934 | 26234 |
| 80 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +932 | 8826 |
| 81 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +928 | 32528 |
| 82 | [openai/symphony](https://github.com/openai/symphony) | +905 | 23513 |
| 83 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +904 | 37330 |
| 84 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +898 | 67169 |
| 85 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +895 | 7387 |
| 86 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +871 | 32826 |
| 87 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +858 | 54050 |
| 88 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +850 | 52568 |
| 89 | [google/magika](https://github.com/google/magika) | +849 | 16978 |
| 90 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +847 | 7118 |
| 91 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +825 | 47122 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +822 | 35586 |
| 93 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +819 | 26443 |
| 94 | [decolua/9router](https://github.com/decolua/9router) | +814 | 9288 |
| 95 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +809 | 14309 |
| 96 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +809 | 21427 |
| 97 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +790 | 21165 |
| 98 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +781 | 7030 |
| 99 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +751 | 5569 |
| 100 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +740 | 5725 |
| 101 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +732 | 10394 |
| 102 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +730 | 6914 |
| 103 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +720 | 6471 |
| 104 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +718 | 37314 |
| 105 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +716 | 7452 |
| 106 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +712 | 17809 |
| 107 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +706 | 25640 |
| 108 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +703 | 5910 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +694 | 43514 |
| 110 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +687 | 20300 |
| 111 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +659 | 7668 |
| 112 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +640 | 18327 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +602 | 13789 |
| 114 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +596 | 34308 |
| 115 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +583 | 4883 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +566 | 4820 |
| 117 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +565 | 14554 |
| 118 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +561 | 20099 |
| 119 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +557 | 22523 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +553 | 13140 |
| 121 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +553 | 12425 |
| 122 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +541 | 4953 |
| 123 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +541 | 13145 |
| 124 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +511 | 30831 |
| 125 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +494 | 6349 |
| 126 | [floci-io/floci](https://github.com/floci-io/floci) | +479 | 8236 |
| 127 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +457 | 4818 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +455 | 36799 |
| 129 | [google-research/timesfm](https://github.com/google-research/timesfm) | +455 | 19715 |
| 130 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +446 | 36907 |
| 131 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +439 | 39841 |
| 132 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +431 | 42274 |
| 133 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +419 | 4794 |
| 134 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +419 | 13081 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +410 | 32768 |
| 136 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +403 | 4796 |
| 137 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +401 | 3144 |
| 138 | [z-lab/dflash](https://github.com/z-lab/dflash) | +400 | 4480 |
| 139 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +398 | 2570 |
| 140 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +396 | 16524 |
| 141 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +395 | 27218 |
| 142 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +395 | 2904 |
| 143 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +394 | 29328 |
| 144 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +392 | 3483 |
| 145 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +379 | 31879 |
| 146 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +376 | 3168 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +375 | 4016 |
| 148 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +369 | 8995 |
| 149 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +359 | 9671 |
| 150 | [browserbase/skills](https://github.com/browserbase/skills) | +359 | 3166 |
| 151 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +357 | 22701 |
| 152 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +354 | 21015 |
| 153 | [PostHog/posthog](https://github.com/PostHog/posthog) | +348 | 31767 |
| 154 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +343 | 18449 |
| 155 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +341 | 7357 |
| 156 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +338 | 20762 |
| 157 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +336 | 19205 |
| 158 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +336 | 21336 |
| 159 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +329 | 2290 |
| 160 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +329 | 37564 |
| 161 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +327 | 4850 |
| 162 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +326 | 8995 |
| 163 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +325 | 3872 |
| 164 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +325 | 19332 |
| 165 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +324 | 26520 |
| 166 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +324 | 25155 |
| 167 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +321 | 5808 |
| 168 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +316 | 2474 |
| 169 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +313 | 1616 |
| 170 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +305 | 3711 |
| 171 | [openai/skills](https://github.com/openai/skills) | +302 | 18942 |
| 172 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +301 | 4261 |
| 173 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +300 | 2364 |
| 174 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +287 | 2032 |
| 175 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +281 | 2071 |
| 176 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +274 | 3988 |
| 177 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +271 | 27458 |
| 178 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +270 | 1956 |
| 179 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +270 | 1923 |
| 180 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +261 | 1574 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +241 | 6803 |
| 182 | [88lin/video_vip](https://github.com/88lin/video_vip) | +240 | 1779 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +231 | 13664 |
| 184 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +229 | 4179 |
| 185 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +226 | 1803 |
| 186 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +224 | 2209 |
| 187 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +221 | 26463 |
| 188 | [eze-is/web-access](https://github.com/eze-is/web-access) | +219 | 6320 |
| 189 | [tiagozip/cap](https://github.com/tiagozip/cap) | +216 | 6347 |
| 190 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +206 | 2945 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +206 | 36103 |
| 192 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +202 | 10152 |
| 193 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +199 | 2399 |
| 194 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +189 | 3353 |
| 195 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +178 | 1248 |
| 196 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +169 | 3289 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +162 | 16502 |
| 198 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +162 | 7734 |
| 199 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +160 | 7757 |
| 200 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +159 | 2790 |
| 201 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +153 | 4228 |
| 202 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +152 | 9759 |
| 203 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +150 | 5738 |
| 204 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +143 | 8766 |
| 205 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +142 | 825 |
| 206 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +142 | 14993 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +139 | 22813 |
| 208 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +136 | 39596 |
| 209 | [playcanvas/engine](https://github.com/playcanvas/engine) | +132 | 15720 |
| 210 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +131 | 40265 |
| 211 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +130 | 1087 |
| 212 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +123 | 855 |
| 213 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +117 | 8222 |
| 214 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +117 | 3093 |
| 215 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +116 | 3632 |
| 216 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +111 | 1262 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +111 | 35473 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +109 | 1293 |
| 219 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +108 | 835 |
| 220 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +107 | 664 |
| 221 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +107 | 711 |
| 222 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +105 | 11676 |
| 223 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +100 | 765 |
| 224 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +98 | 23896 |
| 225 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +97 | 10092 |
| 226 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +96 | 5796 |
| 227 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +94 | 30036 |
| 228 | [sandeco/reversa](https://github.com/sandeco/reversa) | +93 | 758 |
| 229 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +90 | 722 |
| 230 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +89 | 1711 |
| 231 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +85 | 2073 |
| 232 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +83 | 637 |
| 233 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +81 | 3067 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +80 | 2024 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +78 | 2614 |
| 236 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +75 | 3700 |
| 237 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +74 | 1760 |
| 238 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +74 | 37313 |
| 239 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +72 | 2039 |
| 240 | [robinebers/openusage](https://github.com/robinebers/openusage) | +70 | 2394 |
| 241 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +69 | 13223 |
| 242 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 430 |
| 243 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +69 | 445 |
| 244 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +68 | 48784 |
| 245 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +66 | 2701 |
| 246 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +65 | 45263 |
| 247 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +64 | 1759 |
| 248 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +63 | 850 |
| 249 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +63 | 11123 |
| 250 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +62 | 27524 |
| 251 | [halo-dev/halo](https://github.com/halo-dev/halo) | +62 | 37991 |
| 252 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +60 | 1652 |
| 253 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +60 | 1368 |
| 254 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +59 | 762 |
| 255 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +59 | 1632 |
| 256 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +58 | 33000 |
| 257 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +57 | 843 |
| 258 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +57 | 2934 |
| 259 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +56 | 4145 |
| 260 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +56 | 4036 |
| 261 | [crimera/piko](https://github.com/crimera/piko) | +56 | 3530 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +55 | 732 |
| 263 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +54 | 449 |
| 264 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +53 | 9567 |
| 266 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 304 |
| 267 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +50 | 887 |
| 268 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 498 |
| 269 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 340 |
| 270 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +48 | 3998 |
| 271 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +48 | 29157 |
| 272 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +47 | 393 |
| 273 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +46 | 3642 |
| 274 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +46 | 2099 |
| 275 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +46 | 301 |
| 276 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +46 | 11964 |
| 277 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +45 | 280 |
| 278 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +43 | 5087 |
| 279 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +41 | 288 |
| 280 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +41 | 2175 |
| 281 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +40 | 1835 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +38 | 2347 |
| 283 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +38 | 1374 |
| 284 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +38 | 5360 |
| 285 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +36 | 228 |
| 286 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +36 | 186 |
| 287 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +35 | 425 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +34 | 1527 |
| 289 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +34 | 2208 |
| 290 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +33 | 651 |
| 291 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +31 | 241 |
| 292 | [is-a-dev/register](https://github.com/is-a-dev/register) | +30 | 10275 |
| 293 | [intave/intave](https://github.com/intave/intave) | +30 | 247 |
| 294 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +30 | 4063 |
| 295 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +29 | 174 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +29 | 1890 |
| 297 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 748 |
| 298 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2173 |
| 299 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +27 | 204 |
| 300 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +25 | 839 |
