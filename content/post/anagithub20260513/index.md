---
title: "2026-05-13 GitHub增长趋势报告"
description: "1.CloakBrowser+122 2.agentmemory+88 3.openhuman+86 4.hermes-desktop+72 5.floci+63"
date: 2026-05-13T21:27:15+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-13 21:27:15

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
        'daily': {"categories": ["ComposioHQ/trustclaw", "Wei-Shaw/sub2api", "badlogic/pi-mono", "decolua/9router", "op7418/guizang-ppt-skill", "hugohe3/ppt-master", "safishamsi/graphify", "millionco/react-doctor", "rtk-ai/rtk", "addyosmani/agent-skills", "yikart/AiToEarn", "ruvnet/ruflo", "HKUDS/AI-Trader", "datawhalechina/hello-agents", "anthropics/financial-services-plugins", "floci-io/floci", "fathah/hermes-desktop", "tinyhumansai/openhuman", "rohitg00/agentmemory", "CloakHQ/CloakBrowser"], "data": [24, 25, 30, 30, 32, 33, 35, 36, 39, 40, 42, 42, 44, 49, 50, 63, 72, 86, 88, 122]},
        'weekly': {"categories": ["modem-dev/hunk", "badlogic/pi-mono", "safishamsi/graphify", "datawhalechina/easy-vibe", "AIDC-AI/Pixelle-Video", "floci-io/floci", "rtk-ai/rtk", "rohitg00/agentmemory", "vercel-labs/zero-native", "bytedance/UI-TARS-desktop", "TauricResearch/TradingAgents", "ruvnet/ruflo", "decolua/9router", "datawhalechina/hello-agents", "CloakHQ/CloakBrowser", "farion1231/cc-switch", "addyosmani/agent-skills", "forrestchang/andrej-karpathy-skills", "mattpocock/skills", "anthropics/financial-services-plugins"], "data": [360, 377, 389, 393, 394, 404, 411, 452, 460, 480, 559, 562, 607, 694, 728, 939, 1194, 1242, 1440, 1442]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "ruvnet/ruflo", "heygen-com/hyperframes", "rtk-ai/rtk", "Fincept-Corporation/FinceptTerminal", "warpdotdev/warp", "farion1231/cc-switch", "safishamsi/graphify", "addyosmani/agent-skills", "Alishahryar1/free-claude-code", "garrytan/gstack", "TauricResearch/TradingAgents", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "obra/superpowers", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2446, 2494, 2692, 2758, 2798, 3043, 3091, 3120, 3126, 3148, 3278, 3312, 3326, 3670, 4014, 4104, 5005, 7332, 9957, 14585]}
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
| 1 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +122 | 9384 |
| 2 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +88 | 7456 |
| 3 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +86 | 5200 |
| 4 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +72 | 4582 |
| 5 | [floci-io/floci](https://github.com/floci-io/floci) | +63 | 9598 |
| 6 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +50 | 22209 |
| 7 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +49 | 48998 |
| 8 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +44 | 17021 |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +42 | 50276 |
| 10 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +42 | 12845 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +40 | 41003 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +39 | 47340 |
| 13 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +36 | 9230 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +35 | 47617 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +33 | 15881 |
| 16 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +32 | 8319 |
| 17 | [decolua/9router](https://github.com/decolua/9router) | +30 | 9837 |
| 18 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +30 | 49012 |
| 19 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +25 | 20575 |
| 20 | [ComposioHQ/trustclaw](https://github.com/ComposioHQ/trustclaw) | +24 | 556 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +24 | 18693 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +22 | 5363 |
| 23 | [tracewayapp/traceway](https://github.com/tracewayapp/traceway) | +21 | 677 |
| 24 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +21 | 2703 |
| 25 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +20 | 24382 |
| 26 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +20 | 15456 |
| 27 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +20 | 46013 |
| 28 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +19 | 4707 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +18 | 24349 |
| 30 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +18 | 3256 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1442 | 22209 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1440 | 78781 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1242 | 128285 |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1194 | 41003 |
| 5 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +939 | 69747 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +728 | 9384 |
| 7 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +694 | 48998 |
| 8 | [decolua/9router](https://github.com/decolua/9router) | +607 | 9837 |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +562 | 50276 |
| 10 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +559 | 30590 |
| 11 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +480 | 33711 |
| 12 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +460 | 3256 |
| 13 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +452 | 7456 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +411 | 47340 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +404 | 9598 |
| 16 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +394 | 16129 |
| 17 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +393 | 10535 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +389 | 47617 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +377 | 49012 |
| 20 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +360 | 3923 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +359 | 15881 |
| 22 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +353 | 2703 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +331 | 5363 |
| 24 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +327 | 7825 |
| 25 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +326 | 49304 |
| 26 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +319 | 17021 |
| 27 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +314 | 4582 |
| 28 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +301 | 3303 |
| 29 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +289 | 12845 |
| 30 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +274 | 4616 |
| 31 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +270 | 42334 |
| 32 | [multica-ai/multica](https://github.com/multica-ai/multica) | +268 | 28050 |
| 33 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +267 | 58212 |
| 34 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +266 | 5201 |
| 35 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +265 | 9230 |
| 36 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +264 | 24349 |
| 37 | [soxoj/maigret](https://github.com/soxoj/maigret) | +263 | 28380 |
| 38 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +261 | 8319 |
| 39 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +259 | 17873 |
| 40 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +254 | 20575 |
| 41 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +242 | 10506 |
| 42 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +238 | 7242 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +226 | 15456 |
| 44 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +226 | 11213 |
| 45 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +225 | 6785 |
| 46 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +221 | 33115 |
| 47 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +218 | 31125 |
| 48 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +213 | 7481 |
| 49 | [jundot/omlx](https://github.com/jundot/omlx) | +203 | 13952 |
| 50 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +203 | 16502 |
| 51 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +201 | 27521 |
| 52 | [openai/symphony](https://github.com/openai/symphony) | +195 | 23636 |
| 53 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +195 | 6004 |
| 54 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +191 | 60236 |
| 55 | [strukto-ai/mirage](https://github.com/strukto-ai/mirage) | +191 | 2144 |
| 56 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +188 | 47719 |
| 57 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +181 | 38170 |
| 58 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +181 | 14502 |
| 59 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +181 | 2735 |
| 60 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +179 | 1711 |
| 61 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +179 | 4980 |
| 62 | [z-lab/dflash](https://github.com/z-lab/dflash) | +179 | 4528 |
| 63 | [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | +171 | 1751 |
| 64 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +169 | 2328 |
| 65 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +168 | 17176 |
| 66 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +166 | 4347 |
| 67 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +166 | 13215 |
| 68 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +161 | 7566 |
| 69 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +160 | 52852 |
| 70 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +160 | 9045 |
| 71 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +159 | 32521 |
| 72 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +159 | 39480 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +158 | 35769 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +158 | 18987 |
| 75 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +158 | 31046 |
| 76 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +156 | 2262 |
| 77 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +155 | 9218 |
| 78 | [santifer/career-ops](https://github.com/santifer/career-ops) | +148 | 44460 |
| 79 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +148 | 20438 |
| 80 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +146 | 12479 |
| 81 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +145 | 4200 |
| 82 | [virattt/dexter](https://github.com/virattt/dexter) | +143 | 25601 |
| 83 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +143 | 2784 |
| 84 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +141 | 1145 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +139 | 28352 |
| 86 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +138 | 9691 |
| 87 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +133 | 18618 |
| 88 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +133 | 3412 |
| 89 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +133 | 23102 |
| 90 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +132 | 21028 |
| 91 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +129 | 32672 |
| 92 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +128 | 9713 |
| 93 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +127 | 13549 |
| 94 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +127 | 1328 |
| 95 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +125 | 1218 |
| 96 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +124 | 24382 |
| 97 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +123 | 36087 |
| 98 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +120 | 7233 |
| 99 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +119 | 7071 |
| 100 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +119 | 4707 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +119 | 21412 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +104 | 18693 |
| 103 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +101 | 1719 |
| 104 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +101 | 3518 |
| 105 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +98 | 837 |
| 106 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +96 | 37444 |
| 107 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +95 | 3878 |
| 108 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +92 | 44232 |
| 109 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +88 | 9217 |
| 110 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +88 | 36799 |
| 111 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +87 | 1207 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +87 | 43609 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +83 | 13234 |
| 114 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +81 | 6594 |
| 115 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +80 | 3263 |
| 116 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +79 | 25749 |
| 117 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +78 | 39841 |
| 118 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +76 | 1689 |
| 119 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +74 | 26617 |
| 120 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +74 | 4848 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +14585 | 128285 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +9957 | 148517 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7332 | 78781 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +5005 | 60312 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4104 | 59597 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +4014 | 77701 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3670 | 51199 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3326 | 30678 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3312 | 30590 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3278 | 95653 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3148 | 24349 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3126 | 41003 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3120 | 47617 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3091 | 69747 |
| 15 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3043 | 58212 |
| 16 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2798 | 21028 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2758 | 47340 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2692 | 17873 |
| 19 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2494 | 50276 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2446 | 96784 |
| 21 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2329 | 28050 |
| 22 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2248 | 55070 |
| 23 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2240 | 20148 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2232 | 109881 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2127 | 74774 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1832 | 12479 |
| 27 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1760 | 49012 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1712 | 34148 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1670 | 52852 |
| 30 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1669 | 12550 |
| 31 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1653 | 44460 |
| 32 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1630 | 49304 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1628 | 48998 |
| 34 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1601 | 65128 |
| 35 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1569 | 10555 |
| 36 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1563 | 13549 |
| 37 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1562 | 26091 |
| 38 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1552 | 22209 |
| 39 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1502 | 16130 |
| 40 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1470 | 38170 |
| 41 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1447 | 11213 |
| 42 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1419 | 18618 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1418 | 85286 |
| 44 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1384 | 15881 |
| 45 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1357 | 25577 |
| 46 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1332 | 69674 |
| 47 | [github/spec-kit](https://github.com/github/spec-kit) | +1324 | 71722 |
| 48 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1304 | 61969 |
| 49 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1275 | 80888 |
| 50 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1241 | 17176 |
| 51 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1240 | 18987 |
| 52 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1215 | 28380 |
| 53 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1170 | 13215 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1091 | 20575 |
| 55 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +1090 | 52130 |
| 56 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1084 | 15456 |
| 57 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1043 | 23865 |
| 58 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1039 | 24382 |
| 59 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1029 | 8319 |
| 60 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1025 | 27521 |
| 61 | [openai/codex](https://github.com/openai/codex) | +1004 | 61744 |
| 62 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1001 | 47076 |
| 63 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +993 | 14132 |
| 64 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +992 | 6259 |
| 65 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +982 | 60236 |
| 66 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +965 | 36087 |
| 67 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +964 | 18693 |
| 68 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +962 | 14621 |
| 69 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +958 | 31046 |
| 70 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +946 | 16357 |
| 71 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +943 | 9219 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +943 | 28352 |
| 73 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +931 | 26276 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +924 | 47719 |
| 75 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +923 | 10506 |
| 76 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +921 | 28507 |
| 77 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +912 | 32521 |
| 78 | [openai/symphony](https://github.com/openai/symphony) | +899 | 23636 |
| 79 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +894 | 7407 |
| 80 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +888 | 33878 |
| 81 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +883 | 54166 |
| 82 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +881 | 45886 |
| 83 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +860 | 60515 |
| 84 | [google/magika](https://github.com/google/magika) | +848 | 16992 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +845 | 33115 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +839 | 37330 |
| 87 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +838 | 32672 |
| 88 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +825 | 67479 |
| 89 | [decolua/9router](https://github.com/decolua/9router) | +821 | 9837 |
| 90 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +811 | 54116 |
| 91 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +809 | 47122 |
| 92 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +802 | 14502 |
| 93 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +781 | 35769 |
| 94 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +776 | 9384 |
| 95 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +774 | 21569 |
| 96 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +756 | 7242 |
| 97 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +754 | 5644 |
| 98 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +740 | 5798 |
| 99 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +738 | 7233 |
| 100 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +711 | 10535 |
| 101 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +706 | 7566 |
| 102 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +705 | 6004 |
| 103 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +675 | 7071 |
| 104 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +670 | 21208 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +666 | 37444 |
| 106 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +648 | 20438 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +633 | 43610 |
| 108 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +606 | 7456 |
| 109 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +603 | 17862 |
| 110 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +599 | 6594 |
| 111 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +595 | 25749 |
| 112 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +586 | 4994 |
| 113 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +586 | 18456 |
| 114 | [jundot/omlx](https://github.com/jundot/omlx) | +583 | 13952 |
| 115 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +560 | 34386 |
| 116 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +559 | 5363 |
| 117 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +553 | 20146 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +533 | 14668 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +525 | 13234 |
| 120 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +525 | 4941 |
| 121 | [floci-io/floci](https://github.com/floci-io/floci) | +525 | 9598 |
| 122 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +500 | 22656 |
| 123 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +491 | 6785 |
| 124 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +491 | 31125 |
| 125 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +475 | 12467 |
| 126 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +447 | 36799 |
| 127 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +441 | 36907 |
| 128 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +429 | 4878 |
| 129 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +425 | 4980 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +421 | 39841 |
| 131 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +418 | 17021 |
| 132 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +405 | 2618 |
| 133 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +401 | 3160 |
| 134 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +394 | 42366 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +393 | 32874 |
| 136 | [z-lab/dflash](https://github.com/z-lab/dflash) | +390 | 4528 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +386 | 13159 |
| 138 | [google-research/timesfm](https://github.com/google-research/timesfm) | +385 | 19756 |
| 139 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +380 | 27249 |
| 140 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +377 | 3263 |
| 141 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +376 | 2929 |
| 142 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +370 | 9032 |
| 143 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +366 | 4848 |
| 144 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +361 | 9713 |
| 145 | [browserbase/skills](https://github.com/browserbase/skills) | +359 | 3184 |
| 146 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +359 | 4089 |
| 147 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +358 | 29361 |
| 148 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +357 | 31983 |
| 149 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +347 | 7481 |
| 150 | [PostHog/posthog](https://github.com/PostHog/posthog) | +345 | 31767 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +344 | 21135 |
| 152 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +344 | 13218 |
| 153 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +332 | 2328 |
| 154 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +332 | 3527 |
| 155 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +325 | 3873 |
| 156 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +324 | 18531 |
| 157 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +322 | 21412 |
| 158 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +321 | 19287 |
| 159 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +319 | 21057 |
| 160 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +318 | 2562 |
| 161 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +317 | 37564 |
| 162 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +314 | 26617 |
| 163 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +314 | 22756 |
| 164 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +313 | 1623 |
| 165 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +309 | 4899 |
| 166 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +307 | 3749 |
| 167 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +306 | 25202 |
| 168 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +304 | 5866 |
| 169 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +303 | 2417 |
| 170 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +303 | 9217 |
| 171 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +301 | 19430 |
| 172 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +295 | 4291 |
| 173 | [openai/skills](https://github.com/openai/skills) | +291 | 19024 |
| 174 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +286 | 2110 |
| 175 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +281 | 2067 |
| 176 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +278 | 2059 |
| 177 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +271 | 1938 |
| 178 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +265 | 4016 |
| 179 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +264 | 1620 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +259 | 27536 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +237 | 6851 |
| 182 | [88lin/video_vip](https://github.com/88lin/video_vip) | +236 | 1785 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +229 | 13745 |
| 184 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +227 | 1826 |
| 185 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +225 | 2262 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +217 | 4211 |
| 187 | [tiagozip/cap](https://github.com/tiagozip/cap) | +216 | 6350 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +210 | 26517 |
| 189 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +200 | 3010 |
| 190 | [eze-is/web-access](https://github.com/eze-is/web-access) | +199 | 6352 |
| 191 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +196 | 10177 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +194 | 2431 |
| 193 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +188 | 3418 |
| 194 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +185 | 36103 |
| 195 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +162 | 7741 |
| 196 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +154 | 7794 |
| 197 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +151 | 2818 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +150 | 16549 |
| 199 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +149 | 5780 |
| 200 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +148 | 1260 |
| 201 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +147 | 9777 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +142 | 8780 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +140 | 15016 |
| 204 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +138 | 3315 |
| 205 | [playcanvas/engine](https://github.com/playcanvas/engine) | +134 | 15746 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +134 | 22836 |
| 207 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +133 | 39596 |
| 208 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +131 | 1134 |
| 209 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +123 | 862 |
| 210 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +113 | 40265 |
| 211 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +110 | 1282 |
| 212 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +109 | 840 |
| 213 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +109 | 3109 |
| 214 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +108 | 846 |
| 215 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +108 | 672 |
| 216 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +107 | 3691 |
| 217 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +107 | 716 |
| 218 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +106 | 35473 |
| 219 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +101 | 775 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +101 | 1315 |
| 221 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +97 | 11693 |
| 222 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +96 | 10126 |
| 223 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +95 | 23907 |
| 224 | [sandeco/reversa](https://github.com/sandeco/reversa) | +93 | 770 |
| 225 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +92 | 1750 |
| 226 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +92 | 8241 |
| 227 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +91 | 727 |
| 228 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +86 | 30053 |
| 229 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +84 | 4238 |
| 230 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +79 | 2081 |
| 231 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +75 | 3719 |
| 232 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +73 | 642 |
| 233 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +73 | 2046 |
| 234 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +73 | 2634 |
| 235 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +70 | 457 |
| 236 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 433 |
| 237 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +69 | 37313 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +68 | 13251 |
| 239 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +66 | 3076 |
| 240 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +65 | 1764 |
| 241 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +65 | 2369 |
| 242 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +65 | 48784 |
| 243 | [robinebers/openusage](https://github.com/robinebers/openusage) | +64 | 2405 |
| 244 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +63 | 1762 |
| 245 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +63 | 45263 |
| 246 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +62 | 2705 |
| 247 | [halo-dev/halo](https://github.com/halo-dev/halo) | +62 | 37991 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +61 | 2053 |
| 249 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +59 | 27541 |
| 250 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +58 | 769 |
| 251 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +58 | 851 |
| 252 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +58 | 11138 |
| 253 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +56 | 1378 |
| 254 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +56 | 33000 |
| 255 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +54 | 1645 |
| 256 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +54 | 4047 |
| 257 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +54 | 455 |
| 258 | [openmemind/memind](https://github.com/openmemind/memind) | +54 | 732 |
| 259 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 260 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +52 | 853 |
| 261 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +52 | 2954 |
| 262 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 309 |
| 263 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +51 | 1656 |
| 264 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +50 | 897 |
| 265 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +50 | 4082 |
| 266 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +50 | 342 |
| 267 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 500 |
| 268 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 413 |
| 269 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +48 | 4156 |
| 270 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +47 | 286 |
| 271 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +47 | 307 |
| 272 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +47 | 9591 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +47 | 11989 |
| 274 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +45 | 3647 |
| 275 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +43 | 2109 |
| 276 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +43 | 29161 |
| 277 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +41 | 304 |
| 278 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +39 | 5092 |
| 279 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +38 | 5363 |
| 280 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +37 | 1380 |
| 281 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +37 | 1845 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +36 | 2352 |
| 283 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +36 | 233 |
| 284 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +36 | 429 |
| 285 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +36 | 191 |
| 286 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +34 | 2207 |
| 287 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +33 | 1528 |
| 288 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +33 | 653 |
| 289 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +31 | 253 |
| 290 | [intave/intave](https://github.com/intave/intave) | +30 | 247 |
| 291 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +29 | 1899 |
| 292 | [is-a-dev/register](https://github.com/is-a-dev/register) | +28 | 10279 |
| 293 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +28 | 177 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +28 | 2179 |
| 295 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 749 |
| 296 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +25 | 204 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +23 | 841 |
| 298 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +23 | 429 |
| 299 | [supermalparit/Towns](https://github.com/supermalparit/Towns) | +21 | 143 |
| 300 | [vincentchen2026/claude-code-java](https://github.com/vincentchen2026/claude-code-java) | +21 | 116 |
