---
title: "2026-05-11 GitHub增长趋势报告"
description: "1.financial-services-plugins+322 2.agent-skills+266 3.hello-agents+235 4.CloakBrowser+232 5.UI-TARS-desktop+192"
date: 2026-05-11T21:19:31+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-11 21:19:31

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
        'daily': {"categories": ["jundot/omlx", "rohitg00/agentmemory", "playcanvas/supersplat", "crynta/terax-ai", "badlogic/pi-mono", "fathah/hermes-desktop", "safishamsi/graphify", "Imbad0202/academic-research-skills", "ruvnet/ruflo", "AIDC-AI/Pixelle-Video", "HKUDS/AI-Trader", "ConardLi/garden-skills", "floci-io/floci", "decolua/9router", "datawhalechina/easy-vibe", "bytedance/UI-TARS-desktop", "CloakHQ/CloakBrowser", "datawhalechina/hello-agents", "addyosmani/agent-skills", "anthropics/financial-services-plugins"], "data": [92, 93, 99, 101, 102, 108, 110, 118, 126, 126, 143, 149, 150, 165, 167, 192, 232, 235, 266, 322]},
        'weekly': {"categories": ["Yuan1z0825/nature-skills", "badlogic/pi-mono", "hugohe3/ppt-master", "bytedance/UI-TARS-desktop", "soxoj/maigret", "vercel-labs/zero-native", "safishamsi/graphify", "D4Vinci/Scrapling", "rtk-ai/rtk", "CloakHQ/CloakBrowser", "AIDC-AI/Pixelle-Video", "decolua/9router", "datawhalechina/hello-agents", "TauricResearch/TradingAgents", "ruvnet/ruflo", "farion1231/cc-switch", "addyosmani/agent-skills", "anthropics/financial-services-plugins", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [384, 389, 390, 404, 405, 409, 429, 450, 469, 507, 524, 525, 624, 804, 934, 941, 1221, 1321, 1347, 1587]},
        'monthly': {"categories": ["heygen-com/hyperframes", "msitarzewski/agency-agents", "Fincept-Corporation/FinceptTerminal", "warpdotdev/warp", "Alishahryar1/free-claude-code", "rtk-ai/rtk", "farion1231/cc-switch", "multica-ai/multica", "TauricResearch/TradingAgents", "addyosmani/agent-skills", "garrytan/gstack", "safishamsi/graphify", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "obra/superpowers", "JuliusBrussee/caveman", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2655, 2693, 2797, 3000, 3124, 3167, 3200, 3216, 3378, 3565, 3583, 3951, 4138, 4314, 5043, 5573, 6112, 7025, 14287, 16110]}
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
| 1 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +322 | 20188 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +266 | 39384 |
| 3 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +235 | 47549 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +232 | 5985 |
| 5 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +192 | 32931 |
| 6 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +167 | 9836 |
| 7 | [decolua/9router](https://github.com/decolua/9router) | +165 | 8214 |
| 8 | [floci-io/floci](https://github.com/floci-io/floci) | +150 | 6355 |
| 9 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +149 | 4196 |
| 10 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +143 | 16116 |
| 11 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +126 | 15151 |
| 12 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +126 | 49045 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +118 | 6038 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +110 | 46652 |
| 15 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +108 | 2670 |
| 16 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +102 | 48136 |
| 17 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +101 | 1880 |
| 18 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +99 | 7288 |
| 19 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +93 | 4637 |
| 20 | [jundot/omlx](https://github.com/jundot/omlx) | +92 | 13636 |
| 21 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +88 | 8759 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +85 | 46078 |
| 23 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +85 | 2583 |
| 24 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +84 | 3169 |
| 25 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +82 | 7106 |
| 26 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +81 | 3640 |
| 27 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +81 | 7311 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +79 | 14749 |
| 29 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +79 | 10888 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +79 | 4577 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1587 | 125183 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1347 | 72009 |
| 3 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1321 | 20188 |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1221 | 39384 |
| 5 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +941 | 67232 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +934 | 49045 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +804 | 30590 |
| 8 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +624 | 47549 |
| 9 | [decolua/9router](https://github.com/decolua/9router) | +525 | 8214 |
| 10 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +524 | 15151 |
| 11 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +507 | 5986 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +469 | 46078 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +450 | 48853 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +429 | 46652 |
| 15 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +409 | 2583 |
| 16 | [soxoj/maigret](https://github.com/soxoj/maigret) | +405 | 27797 |
| 17 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +404 | 32931 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +390 | 14749 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +389 | 48136 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +384 | 4577 |
| 21 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +347 | 57606 |
| 22 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +345 | 9836 |
| 23 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +336 | 16359 |
| 24 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +332 | 3640 |
| 25 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +317 | 30641 |
| 26 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +314 | 23803 |
| 27 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +309 | 14167 |
| 28 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +295 | 3169 |
| 29 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +293 | 4637 |
| 30 | [multica-ai/multica](https://github.com/multica-ai/multica) | +290 | 27273 |
| 31 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +288 | 7288 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +282 | 17223 |
| 33 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +274 | 16116 |
| 34 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +270 | 42334 |
| 35 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +260 | 19926 |
| 36 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +253 | 6964 |
| 37 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +251 | 4196 |
| 38 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +251 | 2651 |
| 39 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +251 | 7211 |
| 40 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +245 | 5756 |
| 41 | [openai/symphony](https://github.com/openai/symphony) | +240 | 23344 |
| 42 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +237 | 1880 |
| 43 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +237 | 10090 |
| 44 | [floci-io/floci](https://github.com/floci-io/floci) | +231 | 6355 |
| 45 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +231 | 37722 |
| 46 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +229 | 10888 |
| 47 | [virattt/dexter](https://github.com/virattt/dexter) | +228 | 25278 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +227 | 14867 |
| 49 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +225 | 6038 |
| 50 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +220 | 32516 |
| 51 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +219 | 26982 |
| 52 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +216 | 2135 |
| 53 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +207 | 7106 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +196 | 46991 |
| 55 | [jundot/omlx](https://github.com/jundot/omlx) | +195 | 13636 |
| 56 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +194 | 59787 |
| 57 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +194 | 12821 |
| 58 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +193 | 9605 |
| 59 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +190 | 12170 |
| 60 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +186 | 16842 |
| 61 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +185 | 7968 |
| 62 | [strukto-ai/mirage](https://github.com/strukto-ai/mirage) | +183 | 1916 |
| 63 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +182 | 30458 |
| 64 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +182 | 8445 |
| 65 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +179 | 10649 |
| 66 | [z-lab/dflash](https://github.com/z-lab/dflash) | +175 | 4386 |
| 67 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +174 | 52386 |
| 68 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +170 | 1482 |
| 69 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +170 | 2219 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +170 | 32087 |
| 71 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +169 | 4633 |
| 72 | [santifer/career-ops](https://github.com/santifer/career-ops) | +167 | 44096 |
| 73 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +166 | 22794 |
| 74 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +166 | 14358 |
| 75 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +165 | 4045 |
| 76 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +165 | 2563 |
| 77 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +162 | 39237 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +159 | 18594 |
| 79 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +157 | 8603 |
| 80 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +157 | 4976 |
| 81 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +155 | 20846 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +154 | 27884 |
| 83 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +153 | 2670 |
| 84 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +151 | 4022 |
| 85 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +150 | 21269 |
| 86 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +148 | 35319 |
| 87 | [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | +147 | 1497 |
| 88 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +146 | 7311 |
| 89 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +143 | 20075 |
| 90 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +141 | 3335 |
| 91 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +141 | 9446 |
| 92 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +138 | 21092 |
| 93 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +134 | 35827 |
| 94 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +133 | 1296 |
| 95 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +133 | 3360 |
| 96 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +130 | 1026 |
| 97 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +129 | 12102 |
| 98 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +128 | 13216 |
| 99 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +128 | 23976 |
| 100 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +126 | 2100 |
| 101 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +123 | 6717 |
| 102 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +120 | 32371 |
| 103 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +109 | 24964 |
| 104 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +107 | 1345 |
| 105 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +97 | 3953 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +96 | 13052 |
| 107 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +96 | 1641 |
| 108 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +96 | 43384 |
| 109 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +95 | 3086 |
| 110 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +94 | 1146 |
| 111 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +93 | 1605 |
| 112 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +93 | 44232 |
| 113 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +92 | 37187 |
| 114 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +92 | 16128 |
| 115 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +91 | 5743 |
| 116 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +90 | 18200 |
| 117 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +87 | 3752 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +86 | 36799 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +85 | 34233 |
| 120 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +85 | 1704 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +16110 | 125183 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +14287 | 144573 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7025 | 72009 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +6112 | 58260 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +5573 | 60312 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5043 | 75714 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4314 | 51199 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4138 | 30678 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3951 | 46652 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3583 | 93817 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3565 | 39384 |
| 12 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3378 | 30590 |
| 13 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3216 | 27273 |
| 14 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3200 | 67232 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3167 | 46078 |
| 16 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3124 | 23803 |
| 17 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3000 | 57606 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2797 | 20846 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2693 | 96139 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2655 | 17223 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2622 | 52386 |
| 22 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2488 | 49045 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2464 | 109881 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2410 | 74774 |
| 25 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2279 | 20058 |
| 26 | [santifer/career-ops](https://github.com/santifer/career-ops) | +2236 | 44096 |
| 27 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2228 | 55070 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2000 | 34148 |
| 29 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +1962 | 51966 |
| 30 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1947 | 14867 |
| 31 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1889 | 64410 |
| 32 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1889 | 23976 |
| 33 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1882 | 48136 |
| 34 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1807 | 12170 |
| 35 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1774 | 18594 |
| 36 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1736 | 48853 |
| 37 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1692 | 85286 |
| 38 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1665 | 12414 |
| 39 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1657 | 47549 |
| 40 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1609 | 37722 |
| 41 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1585 | 18200 |
| 42 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1568 | 26049 |
| 43 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1562 | 61549 |
| 44 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1560 | 10324 |
| 45 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1546 | 25110 |
| 46 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1537 | 13216 |
| 47 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1518 | 80435 |
| 48 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1512 | 69674 |
| 49 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1473 | 15151 |
| 50 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1423 | 10888 |
| 51 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1423 | 18253 |
| 52 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1414 | 20188 |
| 53 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1408 | 14749 |
| 54 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1372 | 23811 |
| 55 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1283 | 35827 |
| 56 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1280 | 16128 |
| 57 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1277 | 16842 |
| 58 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1275 | 12822 |
| 59 | [github/spec-kit](https://github.com/github/spec-kit) | +1271 | 71722 |
| 60 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1205 | 45886 |
| 61 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1200 | 59787 |
| 62 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1200 | 10090 |
| 63 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1193 | 28271 |
| 64 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1191 | 27797 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1182 | 19926 |
| 66 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1175 | 46994 |
| 67 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1170 | 30458 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1140 | 26982 |
| 69 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1098 | 60146 |
| 70 | [openai/codex](https://github.com/openai/codex) | +1087 | 61744 |
| 71 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1070 | 33878 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1041 | 27884 |
| 73 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1039 | 32371 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1038 | 32087 |
| 75 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1028 | 14003 |
| 76 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1001 | 21092 |
| 77 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +998 | 46991 |
| 78 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +988 | 6113 |
| 79 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +975 | 6964 |
| 80 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +973 | 14358 |
| 81 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +960 | 66921 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +949 | 37330 |
| 83 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +939 | 7106 |
| 84 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +935 | 26196 |
| 85 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +912 | 8445 |
| 86 | [openai/symphony](https://github.com/openai/symphony) | +901 | 23344 |
| 87 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +901 | 32516 |
| 88 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +896 | 26379 |
| 89 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +896 | 7373 |
| 90 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +889 | 53968 |
| 91 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +879 | 6197 |
| 92 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +869 | 52483 |
| 93 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +853 | 35319 |
| 94 | [google/magika](https://github.com/google/magika) | +848 | 16972 |
| 95 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +835 | 47122 |
| 96 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +823 | 21268 |
| 97 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +818 | 22794 |
| 98 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +810 | 14167 |
| 99 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +800 | 6874 |
| 100 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +798 | 17735 |
| 101 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +775 | 6717 |
| 102 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +771 | 25533 |
| 103 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +766 | 37187 |
| 104 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +749 | 5475 |
| 105 | [decolua/9router](https://github.com/decolua/9router) | +747 | 8214 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +739 | 43384 |
| 107 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +726 | 7311 |
| 108 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +711 | 9836 |
| 109 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +711 | 20075 |
| 110 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +684 | 5756 |
| 111 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +671 | 18218 |
| 112 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +642 | 34233 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +613 | 13636 |
| 114 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +613 | 12353 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +607 | 4751 |
| 116 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +606 | 22389 |
| 117 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +592 | 14445 |
| 118 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +582 | 4820 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +570 | 13052 |
| 120 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +565 | 20059 |
| 121 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +558 | 5986 |
| 122 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +552 | 13130 |
| 123 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +519 | 30641 |
| 124 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +511 | 4577 |
| 125 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +485 | 6038 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +480 | 13027 |
| 127 | [google-research/timesfm](https://github.com/google-research/timesfm) | +470 | 19662 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +465 | 36799 |
| 129 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +465 | 4709 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +460 | 39841 |
| 131 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +456 | 3432 |
| 132 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +451 | 36907 |
| 133 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +449 | 29308 |
| 134 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +442 | 42215 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +434 | 32679 |
| 136 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +428 | 16116 |
| 137 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +428 | 4724 |
| 138 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +418 | 3641 |
| 139 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +410 | 4633 |
| 140 | [floci-io/floci](https://github.com/floci-io/floci) | +408 | 6355 |
| 141 | [z-lab/dflash](https://github.com/z-lab/dflash) | +398 | 4386 |
| 142 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +396 | 27172 |
| 143 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +396 | 31784 |
| 144 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +396 | 2875 |
| 145 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +395 | 3070 |
| 146 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +390 | 2428 |
| 147 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +383 | 22643 |
| 148 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +381 | 3936 |
| 149 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +372 | 5743 |
| 150 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +371 | 8956 |
| 151 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +370 | 3086 |
| 152 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +369 | 18377 |
| 153 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +360 | 20659 |
| 154 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +360 | 4778 |
| 155 | [browserbase/skills](https://github.com/browserbase/skills) | +356 | 3141 |
| 156 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +354 | 19108 |
| 157 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +354 | 21269 |
| 158 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +353 | 20901 |
| 159 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +353 | 19215 |
| 160 | [PostHog/posthog](https://github.com/PostHog/posthog) | +352 | 31767 |
| 161 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +351 | 9605 |
| 162 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +347 | 37564 |
| 163 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +343 | 8854 |
| 164 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +340 | 25104 |
| 165 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +327 | 7211 |
| 166 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +327 | 3869 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +324 | 26349 |
| 168 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +323 | 2219 |
| 169 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +315 | 1992 |
| 170 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +312 | 1604 |
| 171 | [openai/skills](https://github.com/openai/skills) | +311 | 18846 |
| 172 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +309 | 2408 |
| 173 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +308 | 4246 |
| 174 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +302 | 3668 |
| 175 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +298 | 2309 |
| 176 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +282 | 3953 |
| 177 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +278 | 2033 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +276 | 27397 |
| 179 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +268 | 1906 |
| 180 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +258 | 1545 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +251 | 6719 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +243 | 13582 |
| 183 | [88lin/video_vip](https://github.com/88lin/video_vip) | +242 | 1766 |
| 184 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +237 | 4220 |
| 185 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +236 | 26418 |
| 186 | [eze-is/web-access](https://github.com/eze-is/web-access) | +231 | 6277 |
| 187 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +228 | 4110 |
| 188 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +222 | 1771 |
| 189 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +216 | 2135 |
| 190 | [tiagozip/cap](https://github.com/tiagozip/cap) | +215 | 6332 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +215 | 36103 |
| 192 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +209 | 10114 |
| 193 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +206 | 2888 |
| 194 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +196 | 3320 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +193 | 2352 |
| 196 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +178 | 3278 |
| 197 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +177 | 1231 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +174 | 16464 |
| 199 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +171 | 2768 |
| 200 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +166 | 7726 |
| 201 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +161 | 7713 |
| 202 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +159 | 9728 |
| 203 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +149 | 5689 |
| 204 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +144 | 22784 |
| 206 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +144 | 8759 |
| 207 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +143 | 14963 |
| 208 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +142 | 815 |
| 209 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +135 | 1049 |
| 210 | [playcanvas/engine](https://github.com/playcanvas/engine) | +133 | 15698 |
| 211 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +125 | 4423 |
| 212 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +124 | 3581 |
| 213 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +124 | 8206 |
| 214 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +124 | 3078 |
| 215 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +122 | 849 |
| 216 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +122 | 39596 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +117 | 35473 |
| 218 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +111 | 1241 |
| 219 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +109 | 11649 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +109 | 1260 |
| 221 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +109 | 5776 |
| 222 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +107 | 828 |
| 223 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +107 | 650 |
| 224 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +106 | 703 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +104 | 30030 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +102 | 23879 |
| 227 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +98 | 632 |
| 228 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +98 | 3060 |
| 229 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +97 | 756 |
| 230 | [sandeco/reversa](https://github.com/sandeco/reversa) | +92 | 745 |
| 231 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +92 | 1681 |
| 232 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 2057 |
| 233 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +90 | 716 |
| 234 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +86 | 14539 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +85 | 2007 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +82 | 2599 |
| 237 | [robinebers/openusage](https://github.com/robinebers/openusage) | +80 | 2376 |
| 238 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +80 | 2017 |
| 239 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +77 | 1753 |
| 240 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +76 | 37313 |
| 241 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +73 | 3675 |
| 242 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +73 | 13198 |
| 243 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +71 | 11106 |
| 244 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 245 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +70 | 48784 |
| 246 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 423 |
| 247 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +69 | 2692 |
| 248 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +69 | 850 |
| 249 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +67 | 433 |
| 250 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +66 | 1759 |
| 251 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +66 | 13232 |
| 252 | [openmemind/memind](https://github.com/openmemind/memind) | +66 | 718 |
| 253 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +64 | 754 |
| 254 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +63 | 27502 |
| 255 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +61 | 1617 |
| 256 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +61 | 1650 |
| 257 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +61 | 1349 |
| 258 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +61 | 33000 |
| 259 | [crimera/piko](https://github.com/crimera/piko) | +60 | 3513 |
| 260 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +59 | 837 |
| 261 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +59 | 4134 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +59 | 2080 |
| 263 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +58 | 4026 |
| 264 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +57 | 2918 |
| 265 | [halo-dev/halo](https://github.com/halo-dev/halo) | +56 | 37991 |
| 266 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +55 | 445 |
| 267 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +54 | 9554 |
| 268 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 269 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 302 |
| 270 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +52 | 5360 |
| 271 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +51 | 29153 |
| 272 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 491 |
| 273 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +49 | 3972 |
| 274 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +49 | 11948 |
| 275 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 324 |
| 276 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +47 | 5080 |
| 277 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 374 |
| 278 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +46 | 298 |
| 279 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +45 | 263 |
| 280 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +45 | 1822 |
| 281 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +40 | 1989 |
| 282 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +39 | 1367 |
| 283 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +38 | 2341 |
| 284 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +37 | 252 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +36 | 1523 |
| 286 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +36 | 185 |
| 287 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +35 | 213 |
| 288 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +35 | 413 |
| 289 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 651 |
| 290 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +34 | 2205 |
| 291 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +33 | 4053 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +32 | 1885 |
| 293 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +31 | 1989 |
| 294 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +30 | 172 |
| 295 | [intave/intave](https://github.com/intave/intave) | +30 | 243 |
| 296 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +29 | 226 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +28 | 836 |
| 298 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +28 | 203 |
| 299 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 747 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +27 | 10263 |
