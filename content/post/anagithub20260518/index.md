---
title: "2026-05-18 GitHub增长趋势报告"
description: "1.openhuman+317 2.academic-research-skills+126 3.semble+123 4.agentmemory+115 5.OpenWA+110"
date: 2026-05-18T21:13:55+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-18 21:13:55

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
        'daily': {"categories": ["KeygraphHQ/shannon", "decolua/9router", "vercel-labs/zero", "wechat-article/wechat-article-exporter", "Tencent/TencentDB-Agent-Memory", "Hmbown/DeepSeek-TUI", "plausible/analytics", "HKUDS/CLI-Anything", "tech-leads-club/agent-skills", "anthropics/financial-services", "supertone-inc/supertonic", "BigBodyCobain/Shadowbroker", "Anil-matcha/Open-Generative-AI", "colbymchenry/codegraph", "CloakHQ/CloakBrowser", "rmyndharis/OpenWA", "rohitg00/agentmemory", "MinishLab/semble", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman"], "data": [59, 60, 63, 64, 66, 70, 71, 72, 73, 74, 75, 77, 89, 104, 110, 110, 115, 123, 126, 317]},
        'weekly': {"categories": ["colbymchenry/codegraph", "Tencent/TencentDB-Agent-Memory", "neilsonnn/image-blaster", "addyosmani/agent-skills", "K-Dense-AI/scientific-agent-skills", "decolua/9router", "yikart/AiToEarn", "floci-io/floci", "anthropics/financial-services", "Imbad0202/academic-research-skills", "supertone-inc/supertonic", "Hmbown/DeepSeek-TUI", "ruvnet/RuView", "anthropics/claude-for-legal", "farion1231/cc-switch", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "forrestchang/andrej-karpathy-skills", "tinyhumansai/openhuman", "mattpocock/skills"], "data": [330, 332, 340, 351, 355, 359, 380, 430, 447, 460, 501, 616, 625, 625, 647, 649, 756, 977, 1246, 1685]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "Z4nzu/hackingtool", "rtk-ai/rtk", "safishamsi/graphify", "ruvnet/ruflo", "Fincept-Corporation/FinceptTerminal", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "addyosmani/agent-skills", "garrytan/gstack", "warpdotdev/warp", "Hmbown/DeepSeek-TUI", "farion1231/cc-switch", "Alishahryar1/free-claude-code", "TauricResearch/TradingAgents", "affaan-m/everything-claude-code", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [2374, 2379, 2547, 2601, 2622, 2705, 2876, 2926, 2997, 3039, 3126, 3141, 3200, 3239, 3326, 3411, 4557, 7577, 8329, 10921]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +317 | 16850 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +126 | 11479 |
| 3 | [MinishLab/semble](https://github.com/MinishLab/semble) | +123 | 2414 |
| 4 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +115 | 12645 |
| 5 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +110 | 2498 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +110 | 15065 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +104 | 4733 |
| 8 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +89 | 15737 |
| 9 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +77 | 7666 |
| 10 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +75 | 8265 |
| 11 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +74 | 25291 |
| 12 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +73 | 3985 |
| 13 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +72 | 36540 |
| 14 | [plausible/analytics](https://github.com/plausible/analytics) | +71 | 25905 |
| 15 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +70 | 31883 |
| 16 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +66 | 3318 |
| 17 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +64 | 10135 |
| 18 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +63 | 2251 |
| 19 | [decolua/9router](https://github.com/decolua/9router) | +60 | 12122 |
| 20 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +59 | 43000 |
| 21 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +58 | 12822 |
| 22 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +58 | 24334 |
| 23 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +56 | 15173 |
| 24 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +55 | 1464 |
| 25 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +54 | 17129 |
| 26 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +53 | 40326 |
| 27 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +52 | 2145 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +51 | 49934 |
| 29 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +50 | 1485 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +48 | 8339 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1685 | 91648 |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1246 | 16850 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +977 | 135816 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +756 | 15065 |
| 5 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +649 | 12646 |
| 6 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +647 | 74503 |
| 7 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +625 | 7113 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +625 | 59822 |
| 9 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +616 | 31883 |
| 10 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +501 | 8265 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +460 | 11479 |
| 12 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +447 | 25291 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +430 | 12254 |
| 14 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +380 | 15173 |
| 15 | [decolua/9router](https://github.com/decolua/9router) | +359 | 12122 |
| 16 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +355 | 24334 |
| 17 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +351 | 43301 |
| 18 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +340 | 3456 |
| 19 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +332 | 3318 |
| 20 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +330 | 4733 |
| 21 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +316 | 12822 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +307 | 8339 |
| 23 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +300 | 50848 |
| 24 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +297 | 5781 |
| 25 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +294 | 15737 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +293 | 49934 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +293 | 18097 |
| 28 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +273 | 2251 |
| 29 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +272 | 18077 |
| 30 | [antirez/ds4](https://github.com/antirez/ds4) | +269 | 10625 |
| 31 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +262 | 3824 |
| 32 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +246 | 3859 |
| 33 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +244 | 9819 |
| 34 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +229 | 3076 |
| 35 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +226 | 49107 |
| 36 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +213 | 21745 |
| 37 | [withcoral/coral](https://github.com/withcoral/coral) | +202 | 2511 |
| 38 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +197 | 17129 |
| 39 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +195 | 19333 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +185 | 36540 |
| 41 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +184 | 34613 |
| 42 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +181 | 3956 |
| 43 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +179 | 10156 |
| 44 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +174 | 18080 |
| 45 | [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) | +168 | 1305 |
| 46 | [multica-ai/multica](https://github.com/multica-ai/multica) | +168 | 29256 |
| 47 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +165 | 37016 |
| 48 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +162 | 48931 |
| 49 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +161 | 2145 |
| 50 | [compozy/compozy](https://github.com/compozy/compozy) | +158 | 2077 |
| 51 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +158 | 6466 |
| 52 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +157 | 10429 |
| 53 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +157 | 2227 |
| 54 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +154 | 43000 |
| 55 | [larksuite/cli](https://github.com/larksuite/cli) | +153 | 11591 |
| 56 | [soxoj/maigret](https://github.com/soxoj/maigret) | +153 | 29339 |
| 57 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +150 | 17056 |
| 58 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +147 | 26694 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +145 | 21725 |
| 60 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +144 | 34076 |
| 61 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +143 | 2498 |
| 62 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +143 | 25639 |
| 63 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +143 | 14097 |
| 64 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +140 | 1497 |
| 65 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +138 | 7666 |
| 66 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +136 | 958 |
| 67 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +133 | 58979 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +131 | 28619 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +127 | 29331 |
| 70 | [MinishLab/semble](https://github.com/MinishLab/semble) | +126 | 2414 |
| 71 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +122 | 33367 |
| 72 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +120 | 1464 |
| 73 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +120 | 38892 |
| 74 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +117 | 3826 |
| 75 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +113 | 31922 |
| 76 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +113 | 40326 |
| 77 | [santifer/career-ops](https://github.com/santifer/career-ops) | +112 | 45464 |
| 78 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +107 | 25286 |
| 79 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +107 | 33406 |
| 80 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +107 | 18001 |
| 81 | [blader/humanizer](https://github.com/blader/humanizer) | +106 | 19570 |
| 82 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +103 | 705 |
| 83 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +103 | 25681 |
| 84 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | +102 | 20190 |
| 85 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +102 | 19121 |
| 86 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +101 | 61170 |
| 87 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +100 | 53572 |
| 88 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +99 | 1309 |
| 89 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +95 | 24053 |
| 90 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +95 | 10135 |
| 91 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +94 | 1639 |
| 92 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +94 | 13150 |
| 93 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +93 | 11705 |
| 94 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +92 | 14931 |
| 95 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +90 | 3985 |
| 96 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +89 | 1224 |
| 97 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +89 | 9892 |
| 98 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +86 | 4825 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +85 | 15373 |
| 100 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +84 | 19738 |
| 101 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +82 | 19142 |
| 102 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +81 | 1197 |
| 103 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +81 | 6263 |
| 104 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +80 | 1485 |
| 105 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +79 | 11035 |
| 106 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +78 | 631 |
| 107 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +78 | 5714 |
| 108 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +78 | 7744 |
| 109 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | +78 | 1361 |
| 110 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +75 | 6829 |
| 111 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +74 | 7969 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +74 | 44152 |
| 113 | [OpenSquilla/opensquilla](https://github.com/OpenSquilla/opensquilla) | +73 | 1030 |
| 114 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +72 | 36799 |
| 115 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +70 | 21582 |
| 116 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +68 | 11733 |
| 117 | [jundot/omlx](https://github.com/jundot/omlx) | +67 | 14518 |
| 118 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +66 | 1014 |
| 119 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +64 | 13145 |
| 120 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +62 | 26109 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +10921 | 135816 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8329 | 91649 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7577 | 156311 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4557 | 60312 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3411 | 51199 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3326 | 30590 |
| 7 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3239 | 25639 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3200 | 74503 |
| 9 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3141 | 31883 |
| 10 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3126 | 58979 |
| 11 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3039 | 99058 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2997 | 43301 |
| 13 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2926 | 80844 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2876 | 61809 |
| 15 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2705 | 21582 |
| 16 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2622 | 52774 |
| 17 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2601 | 49107 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2547 | 49934 |
| 19 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2379 | 55070 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2374 | 99958 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2366 | 19333 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2118 | 109881 |
| 23 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2073 | 30678 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +1980 | 74774 |
| 25 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1913 | 14931 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1898 | 13150 |
| 27 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1811 | 25291 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1755 | 51182 |
| 29 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1728 | 13145 |
| 30 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1701 | 29256 |
| 31 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1659 | 51010 |
| 32 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1646 | 18077 |
| 33 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1621 | 11014 |
| 34 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1611 | 14191 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1538 | 50848 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1537 | 34148 |
| 37 | [github/spec-kit](https://github.com/github/spec-kit) | +1505 | 71722 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1447 | 18097 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1443 | 38892 |
| 40 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1379 | 16851 |
| 41 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1378 | 15737 |
| 42 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1373 | 66335 |
| 43 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1372 | 59823 |
| 44 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1347 | 85286 |
| 45 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1318 | 29339 |
| 46 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1307 | 45464 |
| 47 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1293 | 15065 |
| 48 | [antirez/ds4](https://github.com/antirez/ds4) | +1220 | 10625 |
| 49 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1168 | 9819 |
| 50 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1114 | 18002 |
| 51 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1083 | 20299 |
| 52 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1073 | 19121 |
| 53 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1056 | 10429 |
| 54 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1048 | 62914 |
| 55 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1046 | 11733 |
| 56 | [decolua/9router](https://github.com/decolua/9router) | +1029 | 12122 |
| 57 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1025 | 81742 |
| 58 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1013 | 12646 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1007 | 21725 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +992 | 53572 |
| 61 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +985 | 17129 |
| 62 | [openai/codex](https://github.com/openai/codex) | +950 | 61744 |
| 63 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +941 | 14391 |
| 64 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +928 | 15068 |
| 65 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +926 | 26694 |
| 66 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +924 | 12822 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +923 | 28620 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +919 | 29331 |
| 69 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +917 | 19738 |
| 70 | [openai/symphony](https://github.com/openai/symphony) | +910 | 24131 |
| 71 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +909 | 47258 |
| 72 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +882 | 48931 |
| 73 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +856 | 11479 |
| 74 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +848 | 31922 |
| 75 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +832 | 15044 |
| 76 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +829 | 6427 |
| 77 | [browser-use/video-use](https://github.com/browser-use/video-use) | +826 | 7801 |
| 78 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +814 | 8339 |
| 79 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +807 | 6231 |
| 80 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +804 | 37016 |
| 81 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +804 | 34076 |
| 82 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +794 | 61170 |
| 83 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +793 | 24083 |
| 84 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +791 | 51085 |
| 85 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +789 | 25286 |
| 86 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +789 | 16783 |
| 87 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +786 | 47122 |
| 88 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +781 | 33367 |
| 89 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +770 | 26437 |
| 90 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +768 | 33878 |
| 91 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +767 | 37330 |
| 92 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +742 | 7585 |
| 93 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +737 | 61172 |
| 94 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +733 | 6313 |
| 95 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +731 | 68470 |
| 96 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +720 | 7936 |
| 97 | [floci-io/floci](https://github.com/floci-io/floci) | +713 | 12254 |
| 98 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +713 | 33406 |
| 99 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +703 | 21745 |
| 100 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +698 | 52438 |
| 101 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +688 | 11035 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +674 | 19142 |
| 103 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +665 | 5596 |
| 104 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +625 | 7113 |
| 105 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +615 | 7969 |
| 106 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +612 | 34613 |
| 107 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +609 | 7744 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +608 | 36540 |
| 109 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +597 | 24335 |
| 110 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +587 | 15173 |
| 111 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +566 | 44152 |
| 112 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +527 | 37926 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +511 | 14518 |
| 114 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +511 | 20347 |
| 115 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +508 | 8265 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +508 | 13730 |
| 117 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +503 | 18993 |
| 118 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +502 | 26109 |
| 119 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +500 | 18080 |
| 120 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +477 | 5714 |
| 121 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +475 | 31644 |
| 122 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +471 | 7479 |
| 123 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +468 | 15374 |
| 124 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +461 | 5345 |
| 125 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +461 | 21381 |
| 126 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +453 | 36907 |
| 127 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +452 | 18144 |
| 128 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +422 | 5152 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +420 | 36799 |
| 130 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2632 |
| 131 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +399 | 3463 |
| 132 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +395 | 3508 |
| 133 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +393 | 3859 |
| 134 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +391 | 23125 |
| 135 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +388 | 6829 |
| 136 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +382 | 39841 |
| 137 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +382 | 9212 |
| 138 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +375 | 7796 |
| 139 | [browserbase/skills](https://github.com/browserbase/skills) | +375 | 3331 |
| 140 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +374 | 27394 |
| 141 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +365 | 9861 |
| 142 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +355 | 5253 |
| 143 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +353 | 3049 |
| 144 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +352 | 21582 |
| 145 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +348 | 33277 |
| 146 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +348 | 2484 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +348 | 4442 |
| 148 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +346 | 42721 |
| 149 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +345 | 4978 |
| 150 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +343 | 13497 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +335 | 32350 |
| 152 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +324 | 2695 |
| 153 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +322 | 12696 |
| 154 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +322 | 32541 |
| 155 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +318 | 1657 |
| 156 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +315 | 2515 |
| 157 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +313 | 9892 |
| 158 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +310 | 19692 |
| 159 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3854 |
| 160 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +309 | 26903 |
| 161 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +308 | 21800 |
| 162 | [z-lab/dflash](https://github.com/z-lab/dflash) | +307 | 4637 |
| 163 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +305 | 25547 |
| 164 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +295 | 2211 |
| 165 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +294 | 13493 |
| 166 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +293 | 37564 |
| 167 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +292 | 2196 |
| 168 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +292 | 4371 |
| 169 | [openai/skills](https://github.com/openai/skills) | +287 | 19483 |
| 170 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +282 | 2135 |
| 171 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +274 | 1780 |
| 172 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +271 | 4140 |
| 173 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +270 | 19822 |
| 174 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +268 | 3076 |
| 175 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +259 | 27819 |
| 176 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +257 | 6125 |
| 177 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +254 | 3861 |
| 178 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +249 | 3834 |
| 179 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +243 | 2409 |
| 180 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +230 | 1992 |
| 181 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +229 | 1899 |
| 182 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +225 | 3379 |
| 183 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +223 | 7027 |
| 184 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +220 | 5040 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +220 | 14076 |
| 186 | [tiagozip/cap](https://github.com/tiagozip/cap) | +217 | 6394 |
| 187 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +207 | 4483 |
| 188 | [88lin/video_vip](https://github.com/88lin/video_vip) | +204 | 1840 |
| 189 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +198 | 1639 |
| 190 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +186 | 3553 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +184 | 26769 |
| 192 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +171 | 2145 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +171 | 36103 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +168 | 2643 |
| 195 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +160 | 5995 |
| 196 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +159 | 10303 |
| 197 | [eze-is/web-access](https://github.com/eze-is/web-access) | +157 | 6577 |
| 198 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +150 | 2991 |
| 199 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +147 | 16790 |
| 200 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +141 | 39596 |
| 201 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +140 | 15169 |
| 202 | [playcanvas/engine](https://github.com/playcanvas/engine) | +139 | 15823 |
| 203 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +137 | 8799 |
| 204 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +135 | 1345 |
| 205 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +135 | 9909 |
| 206 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +132 | 1224 |
| 207 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +132 | 7895 |
| 208 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +129 | 3398 |
| 209 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +128 | 22976 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +124 | 41086 |
| 211 | [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | +117 | 779 |
| 212 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +111 | 737 |
| 213 | [sandeco/reversa](https://github.com/sandeco/reversa) | +106 | 879 |
| 214 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 821 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +106 | 10319 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +101 | 40265 |
| 217 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +100 | 1310 |
| 218 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 1896 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +95 | 35473 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +94 | 1465 |
| 221 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +92 | 14734 |
| 222 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +92 | 24071 |
| 223 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +90 | 879 |
| 224 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +90 | 7761 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +89 | 3830 |
| 226 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +88 | 11788 |
| 227 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +80 | 3172 |
| 228 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +78 | 631 |
| 229 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +78 | 9911 |
| 230 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +77 | 944 |
| 231 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +76 | 1354 |
| 232 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +75 | 30126 |
| 233 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +74 | 695 |
| 234 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +73 | 8344 |
| 235 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +68 | 2430 |
| 236 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +66 | 1309 |
| 237 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +65 | 13329 |
| 239 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +65 | 450 |
| 240 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +64 | 4261 |
| 241 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +64 | 37313 |
| 242 | [halo-dev/halo](https://github.com/halo-dev/halo) | +64 | 37991 |
| 243 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +63 | 2162 |
| 244 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +63 | 2543 |
| 245 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 246 | [robinebers/openusage](https://github.com/robinebers/openusage) | +60 | 2499 |
| 247 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +60 | 27593 |
| 248 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +59 | 33000 |
| 249 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +58 | 1802 |
| 250 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +58 | 11205 |
| 251 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +57 | 3129 |
| 252 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +55 | 816 |
| 253 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +55 | 2131 |
| 254 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +54 | 2135 |
| 255 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +53 | 322 |
| 256 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +52 | 4095 |
| 257 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +51 | 949 |
| 258 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 510 |
| 259 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 299 |
| 260 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +50 | 1441 |
| 261 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +50 | 3111 |
| 262 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +49 | 453 |
| 263 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +49 | 1720 |
| 264 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +49 | 4278 |
| 265 | [openmemind/memind](https://github.com/openmemind/memind) | +49 | 769 |
| 266 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +48 | 893 |
| 267 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +48 | 317 |
| 268 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +47 | 4172 |
| 269 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +44 | 473 |
| 270 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +43 | 637 |
| 271 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 324 |
| 272 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +42 | 12016 |
| 273 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +41 | 222 |
| 274 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +41 | 321 |
| 275 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +40 | 2176 |
| 276 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +39 | 1907 |
| 277 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +39 | 467 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +39 | 9649 |
| 279 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +37 | 5120 |
| 280 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +37 | 239 |
| 281 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +36 | 1409 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +35 | 2381 |
| 283 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +35 | 464 |
| 284 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +35 | 322 |
| 285 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +34 | 5404 |
| 286 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +33 | 2220 |
| 287 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +32 | 278 |
| 288 | [intave/intave](https://github.com/intave/intave) | +32 | 258 |
| 289 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 290 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +28 | 2190 |
| 291 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +28 | 1537 |
| 292 | [is-a-dev/register](https://github.com/is-a-dev/register) | +27 | 10308 |
| 293 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +27 | 2635 |
| 294 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 272 |
| 295 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +26 | 199 |
| 296 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +25 | 200 |
| 297 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +25 | 2949 |
| 298 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +23 | 228 |
| 299 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +23 | 3234 |
| 300 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +23 | 1926 |
