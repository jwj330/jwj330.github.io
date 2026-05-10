---
title: "2026-05-10 GitHub增长趋势报告"
description: "1.financial-services-plugins+300 2.agent-skills+198 3.zero-native+198 4.hello-agents+157 5.ruflo+156"
date: 2026-05-10T20:51:41+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-10 20:51:41

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
        'daily': {"categories": ["floci-io/floci", "walkinglabs/learn-harness-engineering", "safishamsi/graphify", "yikart/AiToEarn", "CloakHQ/CloakBrowser", "badlogic/pi-mono", "jackwener/wx-cli", "bytedance/UI-TARS-desktop", "Yuan1z0825/nature-skills", "datawhalechina/easy-vibe", "bannedbook/fanqiang", "playcanvas/supersplat", "masterking32/MasterDnsVPN", "rohitg00/agentmemory", "decolua/9router", "ruvnet/ruflo", "datawhalechina/hello-agents", "vercel-labs/zero-native", "addyosmani/agent-skills", "anthropics/financial-services-plugins"], "data": [85, 85, 86, 92, 98, 101, 106, 110, 110, 111, 118, 124, 142, 150, 155, 156, 157, 198, 198, 300]},
        'weekly': {"categories": ["badlogic/pi-mono", "Alishahryar1/free-claude-code", "Lum1104/Understand-Anything", "bwya77/vscode-dark-islands", "decolua/9router", "docusealco/docuseal", "datawhalechina/hello-agents", "warpdotdev/warp", "safishamsi/graphify", "rtk-ai/rtk", "soxoj/maigret", "AIDC-AI/Pixelle-Video", "D4Vinci/Scrapling", "farion1231/cc-switch", "anthropics/financial-services-plugins", "addyosmani/agent-skills", "TauricResearch/TradingAgents", "ruvnet/ruflo", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [354, 358, 370, 373, 402, 427, 429, 435, 489, 500, 546, 626, 652, 827, 1021, 1037, 1131, 1351, 1406, 1844]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "Fincept-Corporation/FinceptTerminal", "shanraisshan/claude-code-best-practice", "warpdotdev/warp", "farion1231/cc-switch", "Alishahryar1/free-claude-code", "rtk-ai/rtk", "TauricResearch/TradingAgents", "multica-ai/multica", "addyosmani/agent-skills", "garrytan/gstack", "safishamsi/graphify", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "obra/superpowers", "mattpocock/skills", "JuliusBrussee/caveman", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2717, 2765, 2852, 2949, 3056, 3073, 3237, 3294, 3519, 3535, 3537, 4213, 4215, 4259, 5307, 5646, 6782, 7060, 15168, 16062]}
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
| 1 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +300 | 18623 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +198 | 38273 |
| 3 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +198 | 2236 |
| 4 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +157 | 46402 |
| 5 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +156 | 48420 |
| 6 | [decolua/9router](https://github.com/decolua/9router) | +155 | 7191 |
| 7 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +150 | 3905 |
| 8 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +142 | 2970 |
| 9 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +124 | 6731 |
| 10 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +118 | 42334 |
| 11 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +111 | 9064 |
| 12 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +110 | 4110 |
| 13 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +110 | 32015 |
| 14 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +106 | 1206 |
| 15 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +101 | 47640 |
| 16 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +98 | 4554 |
| 17 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +92 | 9953 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +86 | 46042 |
| 19 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +85 | 3864 |
| 20 | [floci-io/floci](https://github.com/floci-io/floci) | +85 | 5243 |
| 21 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +76 | 14524 |
| 22 | [soxoj/maigret](https://github.com/soxoj/maigret) | +75 | 27312 |
| 23 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +72 | 14464 |
| 24 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +71 | 7496 |
| 25 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +70 | 3872 |
| 26 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +70 | 39085 |
| 27 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +69 | 3233 |
| 28 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +68 | 6760 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +68 | 23489 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +66 | 45570 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1844 | 123474 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1406 | 68949 |
| 3 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1351 | 48420 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1131 | 30590 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1037 | 38273 |
| 6 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1021 | 18623 |
| 7 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +827 | 65901 |
| 8 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +652 | 48484 |
| 9 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +626 | 14524 |
| 10 | [soxoj/maigret](https://github.com/soxoj/maigret) | +546 | 27312 |
| 11 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +500 | 45570 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +489 | 46042 |
| 13 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +435 | 57272 |
| 14 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +429 | 46402 |
| 15 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +427 | 16213 |
| 16 | [decolua/9router](https://github.com/decolua/9router) | +402 | 7191 |
| 17 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +373 | 8395 |
| 18 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +370 | 13962 |
| 19 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +358 | 23489 |
| 20 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +354 | 47640 |
| 21 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +351 | 4110 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +350 | 14241 |
| 23 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +335 | 2236 |
| 24 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +314 | 5523 |
| 25 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +289 | 30415 |
| 26 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +287 | 4554 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +278 | 26853 |
| 28 | [virattt/dexter](https://github.com/virattt/dexter) | +278 | 25149 |
| 29 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +278 | 37435 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +268 | 16837 |
| 31 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +268 | 7055 |
| 32 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +265 | 2970 |
| 33 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +257 | 6760 |
| 34 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +252 | 3138 |
| 35 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +250 | 11949 |
| 36 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +248 | 42334 |
| 37 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +242 | 19526 |
| 38 | [openai/symphony](https://github.com/openai/symphony) | +240 | 23131 |
| 39 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +232 | 26728 |
| 40 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +220 | 32015 |
| 41 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +216 | 3905 |
| 42 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +215 | 7933 |
| 43 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +215 | 13931 |
| 44 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +213 | 1704 |
| 45 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +212 | 16567 |
| 46 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +209 | 2528 |
| 47 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +205 | 14247 |
| 48 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +200 | 6731 |
| 49 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +197 | 9772 |
| 50 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +197 | 32198 |
| 51 | [santifer/career-ops](https://github.com/santifer/career-ops) | +194 | 43906 |
| 52 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +194 | 20509 |
| 53 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +193 | 46692 |
| 54 | [browserbase/skills](https://github.com/browserbase/skills) | +193 | 3073 |
| 55 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +192 | 9064 |
| 56 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +189 | 5467 |
| 57 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +189 | 12078 |
| 58 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +187 | 12617 |
| 59 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +186 | 14464 |
| 60 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +186 | 20691 |
| 61 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +183 | 9467 |
| 62 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +181 | 10478 |
| 63 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +180 | 30197 |
| 64 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +177 | 1996 |
| 65 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +173 | 52135 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +171 | 31832 |
| 67 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +165 | 22598 |
| 68 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +164 | 59529 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +163 | 27678 |
| 70 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +163 | 35700 |
| 71 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +159 | 2115 |
| 72 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +155 | 5692 |
| 73 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +152 | 4862 |
| 74 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +152 | 1614 |
| 75 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +150 | 4451 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +148 | 18406 |
| 77 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +147 | 2468 |
| 78 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +147 | 21193 |
| 79 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +146 | 3233 |
| 80 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +143 | 34992 |
| 81 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +143 | 3864 |
| 82 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +141 | 2068 |
| 83 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +140 | 3872 |
| 84 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +140 | 5409 |
| 85 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +140 | 6235 |
| 86 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +139 | 23867 |
| 87 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +138 | 7496 |
| 88 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +136 | 15461 |
| 89 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +136 | 13010 |
| 90 | [z-lab/dflash](https://github.com/z-lab/dflash) | +135 | 4220 |
| 91 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +133 | 3305 |
| 92 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +132 | 39085 |
| 93 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +128 | 9324 |
| 94 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +127 | 16027 |
| 95 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +125 | 8354 |
| 96 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +124 | 3598 |
| 97 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +123 | 32191 |
| 98 | [jundot/omlx](https://github.com/jundot/omlx) | +119 | 13225 |
| 99 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +115 | 6532 |
| 100 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +114 | 1206 |
| 101 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +114 | 9953 |
| 102 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +112 | 6688 |
| 103 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +108 | 18124 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +107 | 12871 |
| 105 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +104 | 2978 |
| 106 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +99 | 24870 |
| 107 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +98 | 23777 |
| 108 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +97 | 3908 |
| 109 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +95 | 37039 |
| 110 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +90 | 25359 |
| 111 | [nikzad-avasam/downloader](https://github.com/nikzad-avasam/downloader) | +89 | 835 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +89 | 43252 |
| 113 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +88 | 34136 |
| 114 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +86 | 26172 |
| 115 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +85 | 1097 |
| 116 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +84 | 1682 |
| 117 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +83 | 5658 |
| 118 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +80 | 6947 |
| 119 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +80 | 36799 |
| 120 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +79 | 14328 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +16062 | 123474 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +15168 | 142298 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7060 | 57439 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6782 | 68949 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +5646 | 60312 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5307 | 74723 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4259 | 51199 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4215 | 30678 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4213 | 46042 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3537 | 92908 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3535 | 38273 |
| 12 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3519 | 26853 |
| 13 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3294 | 30590 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3237 | 45570 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3073 | 23489 |
| 16 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3056 | 65901 |
| 17 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2949 | 57272 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2852 | 52135 |
| 19 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2765 | 20691 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2717 | 95782 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2591 | 16837 |
| 22 | [santifer/career-ops](https://github.com/santifer/career-ops) | +2474 | 43906 |
| 23 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +2449 | 51863 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2447 | 109881 |
| 25 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2443 | 14464 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +2422 | 74774 |
| 27 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2414 | 48420 |
| 28 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2265 | 19994 |
| 29 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2207 | 55070 |
| 30 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2009 | 190952 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2008 | 34148 |
| 32 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1974 | 23867 |
| 33 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1916 | 63976 |
| 34 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1892 | 18406 |
| 35 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1857 | 47640 |
| 36 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1793 | 18124 |
| 37 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1784 | 11949 |
| 38 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1774 | 48484 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1682 | 85286 |
| 40 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1658 | 12358 |
| 41 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1642 | 37435 |
| 42 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1602 | 61308 |
| 43 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1578 | 80188 |
| 44 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1562 | 26030 |
| 45 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1547 | 10281 |
| 46 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1532 | 25001 |
| 47 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1526 | 23777 |
| 48 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1525 | 69674 |
| 49 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1507 | 13010 |
| 50 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1470 | 46402 |
| 51 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1416 | 17995 |
| 52 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1367 | 35700 |
| 53 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1362 | 14241 |
| 54 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1355 | 14524 |
| 55 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1344 | 10478 |
| 56 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1326 | 16027 |
| 57 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1288 | 28121 |
| 58 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1257 | 12617 |
| 59 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1247 | 16567 |
| 60 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1228 | 46935 |
| 61 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1222 | 59529 |
| 62 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1220 | 45886 |
| 63 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1188 | 30197 |
| 64 | [github/spec-kit](https://github.com/github/spec-kit) | +1180 | 71722 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1167 | 19526 |
| 66 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1162 | 59939 |
| 67 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1162 | 9772 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1146 | 26728 |
| 69 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1124 | 27312 |
| 70 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1119 | 32191 |
| 71 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1113 | 18624 |
| 72 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1107 | 20943 |
| 73 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1081 | 33878 |
| 74 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1076 | 13931 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1074 | 61744 |
| 76 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1066 | 31832 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1049 | 27678 |
| 78 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +995 | 5813 |
| 79 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +982 | 6760 |
| 80 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +979 | 6050 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +977 | 46692 |
| 82 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +962 | 14247 |
| 83 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +950 | 37330 |
| 84 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +942 | 66474 |
| 85 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +936 | 26307 |
| 86 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +926 | 26145 |
| 87 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +911 | 33287 |
| 88 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +893 | 53906 |
| 89 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +892 | 7352 |
| 90 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +885 | 7933 |
| 91 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +877 | 17655 |
| 92 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +875 | 32198 |
| 93 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +875 | 52363 |
| 94 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +858 | 6235 |
| 95 | [openai/symphony](https://github.com/openai/symphony) | +856 | 23132 |
| 96 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +846 | 34992 |
| 97 | [google/magika](https://github.com/google/magika) | +843 | 16955 |
| 98 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +830 | 21100 |
| 99 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +823 | 47122 |
| 100 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +823 | 6688 |
| 101 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +823 | 22598 |
| 102 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +814 | 25359 |
| 103 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +787 | 6532 |
| 104 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +783 | 13962 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +776 | 37039 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +755 | 43252 |
| 107 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +737 | 5409 |
| 108 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +693 | 19579 |
| 109 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +685 | 18107 |
| 110 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +683 | 6947 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +663 | 34136 |
| 112 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +644 | 5523 |
| 113 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +644 | 12286 |
| 114 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +620 | 22266 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +610 | 4670 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +609 | 14328 |
| 117 | [decolua/9router](https://github.com/decolua/9router) | +586 | 7191 |
| 118 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +578 | 4792 |
| 119 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +568 | 20013 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +568 | 12871 |
| 121 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +552 | 13107 |
| 122 | [jundot/omlx](https://github.com/jundot/omlx) | +549 | 13225 |
| 123 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +541 | 9064 |
| 124 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +506 | 12974 |
| 125 | [google-research/timesfm](https://github.com/google-research/timesfm) | +502 | 19614 |
| 126 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +501 | 30415 |
| 127 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +501 | 3332 |
| 128 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +482 | 29265 |
| 129 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +478 | 4667 |
| 130 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +470 | 36799 |
| 131 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +462 | 42142 |
| 132 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +462 | 39841 |
| 133 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +450 | 4544 |
| 134 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +445 | 32598 |
| 135 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +438 | 4110 |
| 136 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +430 | 3619 |
| 137 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +425 | 36907 |
| 138 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +395 | 27124 |
| 139 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +394 | 22583 |
| 140 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +393 | 3830 |
| 141 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +392 | 31672 |
| 142 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +389 | 2855 |
| 143 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +387 | 3002 |
| 144 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +387 | 5658 |
| 145 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +383 | 18303 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +382 | 20561 |
| 147 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +378 | 5692 |
| 148 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +376 | 4451 |
| 149 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +369 | 19134 |
| 150 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +363 | 20813 |
| 151 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +362 | 4683 |
| 152 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +361 | 21193 |
| 153 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +361 | 8902 |
| 154 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +359 | 2978 |
| 155 | [z-lab/dflash](https://github.com/z-lab/dflash) | +358 | 4220 |
| 156 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +358 | 2544 |
| 157 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +358 | 4207 |
| 158 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +357 | 2313 |
| 159 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +356 | 19031 |
| 160 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +353 | 31806 |
| 161 | [PostHog/posthog](https://github.com/PostHog/posthog) | +352 | 31767 |
| 162 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +341 | 15461 |
| 163 | [browserbase/skills](https://github.com/browserbase/skills) | +341 | 3073 |
| 164 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +340 | 4557 |
| 165 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +340 | 8704 |
| 166 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +340 | 37564 |
| 167 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +333 | 25025 |
| 168 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +328 | 3868 |
| 169 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +324 | 3602 |
| 170 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +321 | 9467 |
| 171 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +320 | 26172 |
| 172 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +311 | 1598 |
| 173 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +310 | 4229 |
| 174 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +308 | 2115 |
| 175 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +302 | 7055 |
| 176 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +301 | 1944 |
| 177 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +299 | 2345 |
| 178 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +290 | 2249 |
| 179 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +288 | 3611 |
| 180 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +286 | 3908 |
| 181 | [floci-io/floci](https://github.com/floci-io/floci) | +279 | 5243 |
| 182 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +271 | 27335 |
| 183 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +267 | 1890 |
| 184 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +251 | 1509 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +242 | 13499 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +241 | 26369 |
| 187 | [88lin/video_vip](https://github.com/88lin/video_vip) | +240 | 1752 |
| 188 | [eze-is/web-access](https://github.com/eze-is/web-access) | +236 | 6224 |
| 189 | [tiagozip/cap](https://github.com/tiagozip/cap) | +214 | 6317 |
| 190 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +213 | 1704 |
| 191 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +213 | 6600 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +211 | 36103 |
| 193 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +208 | 4013 |
| 194 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +203 | 10086 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +193 | 2315 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +193 | 3284 |
| 197 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +186 | 2809 |
| 198 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +180 | 3254 |
| 199 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +176 | 2738 |
| 200 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +176 | 1222 |
| 201 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +169 | 16425 |
| 202 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +160 | 7678 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +159 | 9686 |
| 204 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +149 | 40265 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +144 | 22763 |
| 206 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +143 | 810 |
| 207 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +138 | 14922 |
| 208 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +134 | 3529 |
| 209 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +131 | 7650 |
| 210 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +129 | 5611 |
| 211 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +128 | 8190 |
| 212 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +128 | 4388 |
| 213 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +127 | 1016 |
| 214 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +126 | 3064 |
| 215 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +121 | 845 |
| 216 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +120 | 39596 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +120 | 35473 |
| 218 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +115 | 3053 |
| 219 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +110 | 1224 |
| 220 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +110 | 5752 |
| 221 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +108 | 11616 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +107 | 30019 |
| 223 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +106 | 826 |
| 224 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +105 | 627 |
| 225 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +105 | 636 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +104 | 1228 |
| 227 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +104 | 694 |
| 228 | [playcanvas/engine](https://github.com/playcanvas/engine) | +102 | 15636 |
| 229 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +99 | 23863 |
| 230 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +98 | 751 |
| 231 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +91 | 1630 |
| 232 | [sandeco/reversa](https://github.com/sandeco/reversa) | +90 | 731 |
| 233 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +90 | 705 |
| 234 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +89 | 2038 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +87 | 1986 |
| 236 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +84 | 2002 |
| 237 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +79 | 2585 |
| 238 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +78 | 1749 |
| 239 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +75 | 14488 |
| 240 | [robinebers/openusage](https://github.com/robinebers/openusage) | +74 | 2349 |
| 241 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +72 | 850 |
| 242 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +71 | 3656 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +71 | 13180 |
| 244 | [openmemind/memind](https://github.com/openmemind/memind) | +71 | 705 |
| 245 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +70 | 13226 |
| 246 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +69 | 2683 |
| 247 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +69 | 11090 |
| 248 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 249 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +66 | 1753 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +66 | 48784 |
| 251 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +65 | 414 |
| 252 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +65 | 428 |
| 253 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +64 | 27491 |
| 254 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +63 | 748 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +63 | 2067 |
| 256 | [crimera/piko](https://github.com/crimera/piko) | +63 | 3499 |
| 257 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +62 | 1647 |
| 258 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +62 | 5355 |
| 259 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +62 | 37313 |
| 260 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +59 | 825 |
| 261 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +59 | 4125 |
| 262 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +59 | 8305 |
| 263 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +59 | 33000 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +58 | 1601 |
| 265 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +57 | 437 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +55 | 4012 |
| 267 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +55 | 2896 |
| 268 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +54 | 9536 |
| 269 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 29147 |
| 270 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +53 | 865 |
| 271 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 272 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +52 | 3631 |
| 273 | [jimmysu0309/shinkansen](https://github.com/jimmysu0309/shinkansen) | +52 | 302 |
| 274 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 298 |
| 275 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 323 |
| 276 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +48 | 5060 |
| 277 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +48 | 486 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +47 | 11930 |
| 279 | [openswarm-ai/openswarm](https://github.com/openswarm-ai/openswarm) | +45 | 557 |
| 280 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +45 | 292 |
| 281 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +45 | 1814 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +45 | 3950 |
| 283 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +41 | 1366 |
| 284 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +41 | 1982 |
| 285 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +40 | 350 |
| 286 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +40 | 31476 |
| 287 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +38 | 2335 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +37 | 1516 |
| 289 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +35 | 213 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +35 | 408 |
| 291 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 648 |
| 292 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 175 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +32 | 1880 |
| 294 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +31 | 169 |
| 295 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +31 | 2198 |
| 296 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +31 | 4051 |
| 297 | [intave/intave](https://github.com/intave/intave) | +30 | 242 |
| 298 | [is-a-dev/register](https://github.com/is-a-dev/register) | +29 | 10257 |
| 299 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 747 |
| 300 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +27 | 833 |
