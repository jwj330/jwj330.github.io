---
title: "2026-05-20 GitHub增长趋势报告"
description: "1.openhuman+160 2.codegraph+76 3.academic-research-skills+59 4.agentmemory+55 5.CloakBrowser+54"
date: 2026-05-20T21:56:46+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-20 21:56:46

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
        'daily': {"categories": ["santifer/career-ops", "MinishLab/semble", "safishamsi/graphify", "abhigyanpatwari/GitNexus", "datawhalechina/hello-agents", "Hmbown/DeepSeek-TUI", "rohitg00/ai-engineering-from-scratch", "HKUDS/ViMax", "wiltodelta/remove-ai-watermarks", "rmyndharis/OpenWA", "anthropics/claude-plugins-official", "tashfeenahmed/freellmapi", "rtk-ai/rtk", "vercel-labs/zero", "HKUDS/CLI-Anything", "CloakHQ/CloakBrowser", "rohitg00/agentmemory", "Imbad0202/academic-research-skills", "colbymchenry/codegraph", "tinyhumansai/openhuman"], "data": [23, 24, 24, 24, 25, 27, 30, 33, 39, 40, 40, 41, 42, 46, 47, 54, 55, 59, 76, 160]},
        'weekly': {"categories": ["addyosmani/agent-skills", "Anil-matcha/Open-Generative-AI", "decolua/9router", "Yuan1z0825/nature-skills", "vercel-labs/zero", "anthropics/financial-services", "neilsonnn/image-blaster", "Tencent/TencentDB-Agent-Memory", "K-Dense-AI/scientific-agent-skills", "colbymchenry/codegraph", "supertone-inc/supertonic", "Hmbown/DeepSeek-TUI", "anthropics/claude-for-legal", "Imbad0202/academic-research-skills", "rohitg00/agentmemory", "ruvnet/RuView", "CloakHQ/CloakBrowser", "forrestchang/andrej-karpathy-skills", "tinyhumansai/openhuman", "mattpocock/skills"], "data": [289, 295, 296, 299, 331, 339, 356, 359, 384, 465, 472, 479, 568, 609, 614, 648, 657, 992, 1403, 1421]},
        'monthly': {"categories": ["anomalyco/opencode", "msitarzewski/agency-agents", "rtk-ai/rtk", "safishamsi/graphify", "JuliusBrussee/caveman", "Z4nzu/hackingtool", "VoltAgent/awesome-design-md", "garrytan/gstack", "ruvnet/ruflo", "addyosmani/agent-skills", "farion1231/cc-switch", "affaan-m/everything-claude-code", "warpdotdev/warp", "Hmbown/DeepSeek-TUI", "TauricResearch/TradingAgents", "Alishahryar1/free-claude-code", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1916, 2101, 2235, 2273, 2376, 2384, 2418, 2434, 2614, 2819, 3095, 3100, 3133, 3188, 3235, 3269, 4099, 6311, 8444, 9360]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +160 | 23512 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +76 | 9240 |
| 3 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +59 | 16012 |
| 4 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +55 | 15047 |
| 5 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +54 | 17542 |
| 6 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +47 | 38477 |
| 7 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +46 | 3948 |
| 8 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +42 | 51824 |
| 9 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +41 | 2670 |
| 10 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +40 | 20724 |
| 11 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +40 | 4783 |
| 12 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +39 | 1006 |
| 13 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +33 | 5995 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +30 | 9446 |
| 15 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +27 | 32808 |
| 16 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +25 | 51802 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +24 | 39315 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +24 | 50203 |
| 19 | [MinishLab/semble](https://github.com/MinishLab/semble) | +24 | 3305 |
| 20 | [santifer/career-ops](https://github.com/santifer/career-ops) | +23 | 46380 |
| 21 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +22 | 26215 |
| 22 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +22 | 26922 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +21 | 9427 |
| 24 | [decolua/9router](https://github.com/decolua/9router) | +21 | 12868 |
| 25 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +20 | 44225 |
| 26 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +20 | 8505 |
| 27 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +19 | 8488 |
| 28 | [pascalorg/editor](https://github.com/pascalorg/editor) | +18 | 16084 |
| 29 | [multica-ai/multica](https://github.com/multica-ai/multica) | +17 | 29966 |
| 30 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +17 | 13515 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1421 | 96825 |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1403 | 23512 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +992 | 140633 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +657 | 17542 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +648 | 61834 |
| 6 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +614 | 15047 |
| 7 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +609 | 16012 |
| 8 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +568 | 7338 |
| 9 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +479 | 32808 |
| 10 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +472 | 8969 |
| 11 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +465 | 9240 |
| 12 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +384 | 24930 |
| 13 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +359 | 3651 |
| 14 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +356 | 3798 |
| 15 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +339 | 26215 |
| 16 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +331 | 3948 |
| 17 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +299 | 9427 |
| 18 | [decolua/9router](https://github.com/decolua/9router) | +296 | 12868 |
| 19 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +295 | 16224 |
| 20 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +289 | 44225 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +287 | 51824 |
| 22 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +285 | 15760 |
| 23 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +276 | 13515 |
| 24 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +268 | 38477 |
| 25 | [floci-io/floci](https://github.com/floci-io/floci) | +267 | 12600 |
| 26 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +259 | 4783 |
| 27 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +252 | 4188 |
| 28 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +249 | 3642 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +248 | 18996 |
| 30 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +231 | 51802 |
| 31 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +224 | 18670 |
| 32 | [withcoral/coral](https://github.com/withcoral/coral) | +209 | 3007 |
| 33 | [antirez/ds4](https://github.com/antirez/ds4) | +198 | 10989 |
| 34 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +195 | 17727 |
| 35 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +194 | 7160 |
| 36 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +191 | 22061 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +176 | 19932 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +174 | 38117 |
| 39 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +171 | 2401 |
| 40 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +169 | 8488 |
| 41 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +169 | 50203 |
| 42 | [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) | +169 | 1350 |
| 43 | [larksuite/cli](https://github.com/larksuite/cli) | +167 | 12077 |
| 44 | [MinishLab/semble](https://github.com/MinishLab/semble) | +166 | 3305 |
| 45 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +164 | 2904 |
| 46 | [compozy/compozy](https://github.com/compozy/compozy) | +159 | 2116 |
| 47 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +158 | 1342 |
| 48 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +155 | 43359 |
| 49 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +155 | 10652 |
| 50 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +153 | 49529 |
| 51 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +152 | 4195 |
| 52 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +149 | 1638 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +148 | 26922 |
| 54 | [multica-ai/multica](https://github.com/multica-ai/multica) | +147 | 29966 |
| 55 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +139 | 27225 |
| 56 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +138 | 6127 |
| 57 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +137 | 17134 |
| 58 | [santifer/career-ops](https://github.com/santifer/career-ops) | +136 | 46380 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +133 | 22253 |
| 60 | [soxoj/maigret](https://github.com/soxoj/maigret) | +133 | 29663 |
| 61 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +132 | 5995 |
| 62 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +125 | 1547 |
| 63 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +123 | 18315 |
| 64 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +123 | 10701 |
| 65 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +122 | 34480 |
| 66 | [plausible/analytics](https://github.com/plausible/analytics) | +121 | 26183 |
| 67 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +119 | 10564 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +118 | 29181 |
| 69 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +113 | 39315 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +113 | 29752 |
| 71 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +113 | 40326 |
| 72 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +112 | 34845 |
| 73 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +111 | 4345 |
| 74 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +111 | 10446 |
| 75 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +107 | 845 |
| 76 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +105 | 2340 |
| 77 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | +103 | 20313 |
| 78 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +102 | 12144 |
| 79 | [blader/humanizer](https://github.com/blader/humanizer) | +102 | 20010 |
| 80 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +101 | 32229 |
| 81 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +99 | 24525 |
| 82 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +97 | 54018 |
| 83 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +97 | 1787 |
| 84 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +97 | 8505 |
| 85 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +96 | 14236 |
| 86 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +94 | 20724 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +94 | 33796 |
| 88 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +92 | 18360 |
| 89 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +91 | 1282 |
| 90 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +89 | 61563 |
| 91 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +87 | 19422 |
| 92 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +86 | 25403 |
| 93 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +84 | 9446 |
| 94 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +84 | 1575 |
| 95 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +84 | 15129 |
| 96 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +82 | 33633 |
| 97 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +82 | 6366 |
| 98 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +81 | 678 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +79 | 15663 |
| 100 | [OpenSquilla/opensquilla](https://github.com/OpenSquilla/opensquilla) | +79 | 1212 |
| 101 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | +79 | 1398 |
| 102 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +77 | 1831 |
| 103 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +76 | 1020 |
| 104 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +76 | 19447 |
| 105 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +76 | 10178 |
| 106 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +75 | 13347 |
| 107 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +73 | 6056 |
| 108 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +73 | 8017 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +70 | 44368 |
| 110 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +68 | 20112 |
| 111 | [byrongamatos/slopsmith](https://github.com/byrongamatos/slopsmith) | +67 | 989 |
| 112 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +66 | 13233 |
| 113 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +65 | 21865 |
| 114 | [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | +63 | 11626 |
| 115 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +62 | 2670 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +61 | 36799 |
| 117 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +60 | 21748 |
| 118 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +59 | 11220 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +57 | 14093 |
| 120 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +57 | 19273 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +9360 | 140633 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8444 | 96825 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +6311 | 159497 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4099 | 60312 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3269 | 26922 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3235 | 30590 |
| 7 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3188 | 32808 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3133 | 59308 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3100 | 51199 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3095 | 76426 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2819 | 44225 |
| 12 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2614 | 53578 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2434 | 99999 |
| 14 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2418 | 81770 |
| 15 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2384 | 55070 |
| 16 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2376 | 62764 |
| 17 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2273 | 50203 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2235 | 51824 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2101 | 102758 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1916 | 109881 |
| 21 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1849 | 26215 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +1813 | 74774 |
| 23 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1802 | 21865 |
| 24 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1764 | 15129 |
| 25 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1692 | 23512 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1634 | 51743 |
| 27 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1630 | 11138 |
| 28 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1625 | 14458 |
| 29 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1623 | 52086 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1617 | 18670 |
| 31 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1615 | 30678 |
| 32 | [github/spec-kit](https://github.com/github/spec-kit) | +1484 | 71722 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1439 | 51802 |
| 34 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1423 | 39315 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1409 | 29966 |
| 36 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1408 | 17542 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1400 | 34148 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1370 | 19932 |
| 39 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1350 | 16224 |
| 40 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1328 | 29663 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1321 | 18996 |
| 42 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1290 | 61834 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1281 | 85286 |
| 44 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1251 | 13233 |
| 45 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1247 | 13347 |
| 46 | [antirez/ds4](https://github.com/antirez/ds4) | +1239 | 10989 |
| 47 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1183 | 10652 |
| 48 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1143 | 66808 |
| 49 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1120 | 15047 |
| 50 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1118 | 46380 |
| 51 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1060 | 10701 |
| 52 | [decolua/9router](https://github.com/decolua/9router) | +1058 | 12868 |
| 53 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1012 | 16012 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +942 | 22253 |
| 55 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +929 | 13515 |
| 56 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +924 | 18360 |
| 57 | [openai/symphony](https://github.com/openai/symphony) | +914 | 24335 |
| 58 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +912 | 63324 |
| 59 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +899 | 17727 |
| 60 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +893 | 82316 |
| 61 | [openai/codex](https://github.com/openai/codex) | +886 | 61744 |
| 62 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +876 | 11868 |
| 63 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +868 | 54018 |
| 64 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +858 | 9427 |
| 65 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +850 | 29181 |
| 66 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +840 | 51085 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +832 | 29752 |
| 68 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +831 | 47329 |
| 69 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +824 | 15603 |
| 70 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +813 | 6378 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +809 | 49529 |
| 72 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +800 | 15263 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +787 | 38117 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +787 | 20112 |
| 75 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +777 | 6216 |
| 76 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +740 | 34480 |
| 77 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +739 | 6397 |
| 78 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +734 | 32229 |
| 79 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +725 | 7741 |
| 80 | [floci-io/floci](https://github.com/floci-io/floci) | +720 | 12600 |
| 81 | [browser-use/video-use](https://github.com/browser-use/video-use) | +709 | 8068 |
| 82 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +704 | 61563 |
| 83 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +701 | 8505 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +693 | 33796 |
| 85 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +685 | 33878 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +682 | 37330 |
| 87 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +673 | 5732 |
| 88 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +654 | 25403 |
| 89 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +651 | 47122 |
| 90 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +648 | 22061 |
| 91 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +647 | 61391 |
| 92 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +646 | 5464 |
| 93 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +638 | 33633 |
| 94 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +631 | 7338 |
| 95 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +622 | 16997 |
| 96 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +621 | 34845 |
| 97 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +615 | 11220 |
| 98 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +602 | 15760 |
| 99 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +586 | 38477 |
| 100 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +584 | 24930 |
| 101 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +560 | 24152 |
| 102 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +558 | 8017 |
| 103 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +556 | 52571 |
| 104 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +543 | 8969 |
| 105 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +540 | 9241 |
| 106 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +540 | 6127 |
| 107 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +535 | 9447 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +527 | 19273 |
| 109 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +505 | 4195 |
| 110 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +493 | 18315 |
| 111 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +490 | 44368 |
| 112 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +472 | 6056 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +468 | 14695 |
| 114 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +462 | 31832 |
| 115 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +458 | 20441 |
| 116 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +454 | 19213 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +446 | 38167 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +445 | 13989 |
| 119 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +436 | 6506 |
| 120 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +416 | 2749 |
| 121 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +407 | 26252 |
| 122 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +401 | 26506 |
| 123 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +400 | 5488 |
| 124 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +399 | 21426 |
| 125 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +395 | 3575 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +393 | 15663 |
| 127 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +377 | 9395 |
| 128 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +375 | 7869 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +375 | 36799 |
| 130 | [browserbase/skills](https://github.com/browserbase/skills) | +374 | 3362 |
| 131 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +364 | 9923 |
| 132 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +364 | 3224 |
| 133 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +358 | 27444 |
| 134 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +351 | 23316 |
| 135 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +347 | 6933 |
| 136 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +337 | 4591 |
| 137 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +336 | 5366 |
| 138 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +333 | 5255 |
| 139 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +329 | 3677 |
| 140 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +325 | 20724 |
| 141 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +323 | 14093 |
| 142 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +323 | 5027 |
| 143 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +318 | 1663 |
| 144 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +317 | 2575 |
| 145 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +314 | 32541 |
| 146 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +312 | 2828 |
| 147 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +310 | 33472 |
| 148 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +310 | 21748 |
| 149 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3885 |
| 150 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +309 | 4188 |
| 151 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +301 | 18243 |
| 152 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +301 | 2535 |
| 153 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +299 | 42853 |
| 154 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +297 | 2246 |
| 155 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +295 | 2270 |
| 156 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +294 | 27022 |
| 157 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +292 | 32677 |
| 158 | [z-lab/dflash](https://github.com/z-lab/dflash) | +290 | 4669 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +289 | 10178 |
| 160 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +285 | 21914 |
| 161 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +284 | 39841 |
| 162 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +284 | 2286 |
| 163 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +277 | 1831 |
| 164 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +277 | 13543 |
| 165 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +276 | 25679 |
| 166 | [openai/skills](https://github.com/openai/skills) | +271 | 19689 |
| 167 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +270 | 3642 |
| 168 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +265 | 4195 |
| 169 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +265 | 12839 |
| 170 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +257 | 37564 |
| 171 | [MinishLab/semble](https://github.com/MinishLab/semble) | +255 | 3305 |
| 172 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +254 | 4139 |
| 173 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +248 | 19974 |
| 174 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +243 | 2440 |
| 175 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +240 | 5995 |
| 176 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +238 | 27965 |
| 177 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +230 | 1918 |
| 178 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +228 | 3516 |
| 179 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +221 | 4111 |
| 180 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +214 | 7091 |
| 181 | [tiagozip/cap](https://github.com/tiagozip/cap) | +214 | 6414 |
| 182 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +206 | 2017 |
| 183 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +204 | 7517 |
| 184 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +202 | 1831 |
| 185 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +198 | 7160 |
| 186 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +191 | 14214 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +184 | 5103 |
| 188 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +181 | 2401 |
| 189 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +173 | 26884 |
| 190 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +170 | 3610 |
| 191 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +164 | 2904 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +163 | 4559 |
| 193 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +157 | 6082 |
| 194 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +146 | 10358 |
| 195 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +146 | 36103 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +143 | 2756 |
| 197 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +143 | 4424 |
| 198 | [playcanvas/engine](https://github.com/playcanvas/engine) | +139 | 15849 |
| 199 | [eze-is/web-access](https://github.com/eze-is/web-access) | +132 | 6663 |
| 200 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +132 | 16871 |
| 201 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +132 | 15212 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +132 | 0 |
| 203 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +125 | 1427 |
| 204 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +125 | 9933 |
| 205 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +125 | 39596 |
| 206 | [usebruno/bruno](https://github.com/usebruno/bruno) | +120 | 41086 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +114 | 23058 |
| 208 | [sandeco/reversa](https://github.com/sandeco/reversa) | +110 | 904 |
| 209 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +108 | 0 |
| 210 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 828 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +103 | 3045 |
| 212 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +102 | 7954 |
| 213 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +99 | 1282 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +97 | 1948 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +97 | 10349 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +91 | 40265 |
| 217 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +85 | 14785 |
| 218 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +85 | 24114 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +85 | 35473 |
| 220 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +81 | 678 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +81 | 1528 |
| 222 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +80 | 3879 |
| 223 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +76 | 9943 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +75 | 11818 |
| 225 | [88lin/video_vip](https://github.com/88lin/video_vip) | +73 | 1860 |
| 226 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +72 | 7768 |
| 227 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +68 | 2440 |
| 228 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +67 | 8381 |
| 229 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +67 | 3196 |
| 230 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +61 | 13364 |
| 231 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +61 | 4329 |
| 232 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 233 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +60 | 45263 |
| 234 | [halo-dev/halo](https://github.com/halo-dev/halo) | +60 | 37991 |
| 235 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +59 | 708 |
| 236 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +59 | 37313 |
| 237 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +58 | 30154 |
| 238 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +57 | 453 |
| 239 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +57 | 2219 |
| 240 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +57 | 33000 |
| 241 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +56 | 2543 |
| 242 | [robinebers/openusage](https://github.com/robinebers/openusage) | +55 | 2513 |
| 243 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +54 | 1816 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +54 | 3184 |
| 245 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +53 | 11220 |
| 246 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +52 | 883 |
| 247 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +52 | 960 |
| 248 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +51 | 831 |
| 249 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +51 | 968 |
| 250 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +51 | 27618 |
| 251 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 511 |
| 252 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 302 |
| 253 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +50 | 2159 |
| 254 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +49 | 465 |
| 255 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +49 | 2158 |
| 256 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +48 | 332 |
| 257 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +46 | 3125 |
| 258 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +45 | 908 |
| 259 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +45 | 4119 |
| 260 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +44 | 710 |
| 261 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +44 | 4177 |
| 262 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +44 | 1252 |
| 263 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +43 | 242 |
| 264 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 328 |
| 265 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +43 | 1376 |
| 266 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +42 | 1748 |
| 267 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +42 | 488 |
| 268 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 331 |
| 269 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +42 | 746 |
| 270 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +41 | 1329 |
| 271 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +41 | 12038 |
| 272 | [ethanashi/fbm-sniper-community](https://github.com/ethanashi/fbm-sniper-community) | +40 | 255 |
| 273 | [openmemind/memind](https://github.com/openmemind/memind) | +40 | 788 |
| 274 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +40 | 484 |
| 275 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +37 | 242 |
| 276 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +36 | 5129 |
| 277 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +36 | 2195 |
| 278 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +36 | 1421 |
| 279 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +35 | 601 |
| 280 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +34 | 1928 |
| 281 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9673 |
| 282 | [intave/intave](https://github.com/intave/intave) | +32 | 258 |
| 283 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 753 |
| 284 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +29 | 2394 |
| 285 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +28 | 327 |
| 286 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 212 |
| 287 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +27 | 0 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +27 | 2637 |
| 289 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +27 | 335 |
| 290 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +27 | 464 |
| 291 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 281 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2199 |
| 293 | [is-a-dev/register](https://github.com/is-a-dev/register) | +24 | 10312 |
| 294 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +24 | 289 |
| 295 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +24 | 2952 |
| 296 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +24 | 1542 |
| 297 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +23 | 3234 |
| 298 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 304 |
| 299 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +21 | 209 |
| 300 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +20 | 861 |
