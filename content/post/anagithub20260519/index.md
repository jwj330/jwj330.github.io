---
title: "2026-05-19 GitHub增长趋势报告"
description: "1.openhuman+170 2.academic-research-skills+140 3.OpenWA+82 4.agentmemory+77 5.codegraph+69"
date: 2026-05-19T21:21:18+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-19 21:21:18

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
        'daily': {"categories": ["Yuan1z0825/nature-skills", "tech-leads-club/agent-skills", "supertone-inc/supertonic", "can1357/oh-my-pi", "addyosmani/agent-skills", "rtk-ai/rtk", "MinishLab/semble", "santifer/career-ops", "decolua/9router", "K-Dense-AI/scientific-agent-skills", "anthropics/financial-services", "ZhuLinsen/daily_stock_analysis", "truelockmc/streambert", "HKUDS/CLI-Anything", "CloakHQ/CloakBrowser", "colbymchenry/codegraph", "rohitg00/agentmemory", "rmyndharis/OpenWA", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman"], "data": [22, 22, 23, 24, 25, 28, 29, 29, 30, 30, 35, 43, 48, 60, 63, 69, 77, 82, 140, 170]},
        'weekly': {"categories": ["Anil-matcha/Open-Generative-AI", "decolua/9router", "addyosmani/agent-skills", "yikart/AiToEarn", "floci-io/floci", "Tencent/TencentDB-Agent-Memory", "neilsonnn/image-blaster", "anthropics/financial-services", "K-Dense-AI/scientific-agent-skills", "colbymchenry/codegraph", "supertone-inc/supertonic", "Hmbown/DeepSeek-TUI", "Imbad0202/academic-research-skills", "anthropics/claude-for-legal", "rohitg00/agentmemory", "ruvnet/RuView", "CloakHQ/CloakBrowser", "forrestchang/andrej-karpathy-skills", "tinyhumansai/openhuman", "mattpocock/skills"], "data": [297, 301, 309, 315, 322, 345, 347, 368, 379, 393, 522, 537, 569, 628, 647, 656, 713, 947, 1330, 1489]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "Z4nzu/hackingtool", "Fincept-Corporation/FinceptTerminal", "rtk-ai/rtk", "safishamsi/graphify", "ruvnet/ruflo", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "garrytan/gstack", "addyosmani/agent-skills", "warpdotdev/warp", "farion1231/cc-switch", "Hmbown/DeepSeek-TUI", "affaan-m/everything-claude-code", "Alishahryar1/free-claude-code", "TauricResearch/TradingAgents", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [2228, 2380, 2399, 2402, 2402, 2616, 2622, 2642, 2669, 2893, 3129, 3154, 3161, 3251, 3254, 3290, 4300, 6936, 8359, 10129]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +170 | 20880 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +140 | 14000 |
| 3 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +82 | 4069 |
| 4 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +77 | 14037 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +69 | 6422 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +63 | 16456 |
| 7 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +60 | 37627 |
| 8 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +48 | 2138 |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +43 | 37790 |
| 10 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +35 | 25887 |
| 11 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +30 | 24771 |
| 12 | [decolua/9router](https://github.com/decolua/9router) | +30 | 12503 |
| 13 | [santifer/career-ops](https://github.com/santifer/career-ops) | +29 | 46101 |
| 14 | [MinishLab/semble](https://github.com/MinishLab/semble) | +29 | 3001 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +28 | 50771 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +25 | 43811 |
| 17 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +24 | 5038 |
| 18 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +23 | 8755 |
| 19 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +22 | 4302 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +22 | 8863 |
| 21 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +21 | 26275 |
| 22 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +21 | 8222 |
| 23 | [laishiwen/sven-family](https://github.com/laishiwen/sven-family) | +21 | 705 |
| 24 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +21 | 51381 |
| 25 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +19 | 21983 |
| 26 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +19 | 32401 |
| 27 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +19 | 17498 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +17 | 18592 |
| 29 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 19807 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +16 | 1606 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1489 | 94243 |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1330 | 20880 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +947 | 137818 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +713 | 16457 |
| 5 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +656 | 60742 |
| 6 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +647 | 14037 |
| 7 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +628 | 7246 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +569 | 14000 |
| 9 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +537 | 32401 |
| 10 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +522 | 8755 |
| 11 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +393 | 6422 |
| 12 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +379 | 24771 |
| 13 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +368 | 25887 |
| 14 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +347 | 3667 |
| 15 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +345 | 3516 |
| 16 | [floci-io/floci](https://github.com/floci-io/floci) | +322 | 12451 |
| 17 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +315 | 15489 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +309 | 43811 |
| 19 | [decolua/9router](https://github.com/decolua/9router) | +301 | 12503 |
| 20 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +297 | 16028 |
| 21 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +294 | 8863 |
| 22 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +285 | 3049 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +283 | 50771 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +268 | 18592 |
| 25 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +266 | 13214 |
| 26 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +251 | 51381 |
| 27 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +248 | 3950 |
| 28 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +240 | 3434 |
| 29 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +236 | 37627 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +233 | 18406 |
| 31 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +222 | 4069 |
| 32 | [antirez/ds4](https://github.com/antirez/ds4) | +217 | 10815 |
| 33 | [withcoral/coral](https://github.com/withcoral/coral) | +204 | 2646 |
| 34 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +200 | 17498 |
| 35 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +200 | 5969 |
| 36 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +194 | 21890 |
| 37 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +183 | 7001 |
| 38 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +179 | 49617 |
| 39 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +178 | 19668 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +176 | 37790 |
| 41 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +175 | 10278 |
| 42 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +170 | 3987 |
| 43 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +169 | 2313 |
| 44 | [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) | +169 | 1335 |
| 45 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +163 | 2289 |
| 46 | [larksuite/cli](https://github.com/larksuite/cli) | +161 | 11863 |
| 47 | [compozy/compozy](https://github.com/compozy/compozy) | +158 | 2104 |
| 48 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +156 | 18230 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +155 | 49202 |
| 50 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +152 | 8222 |
| 51 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +150 | 17106 |
| 52 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +149 | 43158 |
| 53 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +147 | 2138 |
| 54 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +147 | 1201 |
| 55 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +146 | 26275 |
| 56 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +146 | 1582 |
| 57 | [multica-ai/multica](https://github.com/multica-ai/multica) | +144 | 29533 |
| 58 | [MinishLab/semble](https://github.com/MinishLab/semble) | +143 | 3001 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +143 | 21983 |
| 60 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +140 | 10317 |
| 61 | [soxoj/maigret](https://github.com/soxoj/maigret) | +140 | 29486 |
| 62 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +135 | 10591 |
| 63 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +133 | 34294 |
| 64 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +130 | 4026 |
| 65 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +128 | 26943 |
| 66 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +128 | 34758 |
| 67 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +124 | 1530 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +122 | 28928 |
| 69 | [plausible/analytics](https://github.com/plausible/analytics) | +121 | 26159 |
| 70 | [santifer/career-ops](https://github.com/santifer/career-ops) | +119 | 46101 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +116 | 29532 |
| 72 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +113 | 40326 |
| 73 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +111 | 4302 |
| 74 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +111 | 32095 |
| 75 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +108 | 10430 |
| 76 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +107 | 801 |
| 77 | [blader/humanizer](https://github.com/blader/humanizer) | +107 | 19807 |
| 78 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +105 | 14174 |
| 79 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +105 | 39064 |
| 80 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +103 | 33573 |
| 81 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +103 | 5354 |
| 82 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | +102 | 20270 |
| 83 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +101 | 25341 |
| 84 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +96 | 24291 |
| 85 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +95 | 18192 |
| 86 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +94 | 61359 |
| 87 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +94 | 11932 |
| 88 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +94 | 53846 |
| 89 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +92 | 1263 |
| 90 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +91 | 33525 |
| 91 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +89 | 19284 |
| 92 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +88 | 1640 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +88 | 8235 |
| 94 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +88 | 1733 |
| 95 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +86 | 10060 |
| 96 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +86 | 5435 |
| 97 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +83 | 25858 |
| 98 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +83 | 13249 |
| 99 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +82 | 1408 |
| 100 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +82 | 15031 |
| 101 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +82 | 6322 |
| 102 | [OpenSquilla/opensquilla](https://github.com/OpenSquilla/opensquilla) | +81 | 1142 |
| 103 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +80 | 656 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +80 | 15521 |
| 105 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +79 | 19215 |
| 106 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | +79 | 1386 |
| 107 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +77 | 19920 |
| 108 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +75 | 5939 |
| 109 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +73 | 7900 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +70 | 44271 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +68 | 11127 |
| 112 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +67 | 13194 |
| 113 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +67 | 1078 |
| 114 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +66 | 36799 |
| 115 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +63 | 21741 |
| 116 | [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | +62 | 11581 |
| 117 | [byrongamatos/slopsmith](https://github.com/byrongamatos/slopsmith) | +62 | 949 |
| 118 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +61 | 21681 |
| 119 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +58 | 8626 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +57 | 20103 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +10129 | 137818 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8359 | 94243 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +6936 | 157898 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4300 | 60312 |
| 5 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3290 | 30590 |
| 6 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3254 | 26276 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3251 | 51199 |
| 8 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3161 | 32401 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3154 | 75527 |
| 10 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3129 | 59155 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2893 | 43811 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2669 | 99522 |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2642 | 62289 |
| 14 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2622 | 81305 |
| 15 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2616 | 53166 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2402 | 49617 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2402 | 50771 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2399 | 21741 |
| 19 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2380 | 55070 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2228 | 101450 |
| 21 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2024 | 109881 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +1904 | 74774 |
| 23 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1837 | 15031 |
| 24 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1831 | 25887 |
| 25 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1827 | 30678 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1772 | 19668 |
| 27 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1695 | 51703 |
| 28 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1664 | 13194 |
| 29 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1643 | 51323 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1637 | 18406 |
| 31 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1626 | 11075 |
| 32 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1618 | 14323 |
| 33 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1588 | 13249 |
| 34 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1547 | 29533 |
| 35 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1538 | 20881 |
| 36 | [github/spec-kit](https://github.com/github/spec-kit) | +1497 | 71722 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1484 | 51381 |
| 38 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1474 | 34148 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1426 | 39064 |
| 40 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1377 | 60743 |
| 41 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1368 | 16028 |
| 42 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1364 | 18592 |
| 43 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1355 | 16457 |
| 44 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1325 | 29486 |
| 45 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1317 | 85286 |
| 46 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1258 | 66578 |
| 47 | [antirez/ds4](https://github.com/antirez/ds4) | +1229 | 10815 |
| 48 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1210 | 46101 |
| 49 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1172 | 10278 |
| 50 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1076 | 14037 |
| 51 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1057 | 10591 |
| 52 | [decolua/9router](https://github.com/decolua/9router) | +1049 | 12503 |
| 53 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +993 | 63136 |
| 54 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +977 | 14000 |
| 55 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +973 | 18192 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +968 | 21983 |
| 57 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +962 | 81987 |
| 58 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +959 | 11814 |
| 59 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +945 | 17498 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +938 | 53846 |
| 61 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +923 | 13214 |
| 62 | [openai/symphony](https://github.com/openai/symphony) | +916 | 24261 |
| 63 | [openai/codex](https://github.com/openai/codex) | +910 | 61744 |
| 64 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +895 | 19280 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +894 | 29532 |
| 66 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +889 | 28928 |
| 67 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +882 | 15172 |
| 68 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +875 | 47300 |
| 69 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +858 | 19920 |
| 70 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +849 | 49202 |
| 71 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +835 | 8863 |
| 72 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +830 | 15241 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +813 | 37790 |
| 74 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +810 | 6304 |
| 75 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +806 | 51085 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +783 | 32095 |
| 77 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +778 | 34294 |
| 78 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +773 | 26943 |
| 79 | [browser-use/video-use](https://github.com/browser-use/video-use) | +773 | 7925 |
| 80 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +773 | 6163 |
| 81 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +769 | 14425 |
| 82 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +753 | 47122 |
| 83 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +746 | 33573 |
| 84 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +740 | 61359 |
| 85 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +736 | 6362 |
| 86 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +731 | 7658 |
| 87 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +726 | 33878 |
| 88 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +723 | 37330 |
| 89 | [floci-io/floci](https://github.com/floci-io/floci) | +719 | 12453 |
| 90 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +711 | 16902 |
| 91 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +709 | 25341 |
| 92 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +708 | 8235 |
| 93 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +684 | 61279 |
| 94 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +677 | 21890 |
| 95 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +671 | 5657 |
| 96 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +668 | 33525 |
| 97 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +655 | 24114 |
| 98 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +651 | 11127 |
| 99 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +642 | 5363 |
| 100 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +629 | 52498 |
| 101 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +628 | 7246 |
| 102 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +623 | 34758 |
| 103 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +606 | 24771 |
| 104 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +595 | 15489 |
| 105 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +590 | 26477 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +588 | 37627 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +587 | 19215 |
| 108 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +580 | 8626 |
| 109 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +579 | 7900 |
| 110 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +561 | 6466 |
| 111 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +530 | 8755 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +528 | 44271 |
| 113 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +502 | 20399 |
| 114 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +498 | 18230 |
| 115 | [jundot/omlx](https://github.com/jundot/omlx) | +490 | 14605 |
| 116 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +480 | 19097 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +478 | 38030 |
| 118 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +475 | 5939 |
| 119 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +469 | 31740 |
| 120 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +465 | 26186 |
| 121 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +462 | 13853 |
| 122 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +431 | 18197 |
| 123 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +427 | 5409 |
| 124 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +421 | 15521 |
| 125 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +417 | 21402 |
| 126 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2667 |
| 127 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +394 | 3545 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +391 | 36799 |
| 129 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +378 | 9285 |
| 130 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +377 | 5203 |
| 131 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +375 | 7840 |
| 132 | [browserbase/skills](https://github.com/browserbase/skills) | +375 | 3348 |
| 133 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +370 | 23227 |
| 134 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +368 | 6877 |
| 135 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +368 | 3554 |
| 136 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +368 | 36907 |
| 137 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +366 | 27413 |
| 138 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +365 | 9898 |
| 139 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +359 | 3163 |
| 140 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +348 | 2513 |
| 141 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +344 | 4524 |
| 142 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +344 | 5312 |
| 143 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +341 | 3950 |
| 144 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +333 | 5004 |
| 145 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +331 | 13892 |
| 146 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +329 | 33385 |
| 147 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +329 | 21681 |
| 148 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +328 | 2757 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +327 | 32431 |
| 150 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +323 | 42790 |
| 151 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +318 | 1658 |
| 152 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +317 | 2555 |
| 153 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +314 | 39841 |
| 154 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +314 | 7496 |
| 155 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3875 |
| 156 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +309 | 32604 |
| 157 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +304 | 10060 |
| 158 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +301 | 20103 |
| 159 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +299 | 26983 |
| 160 | [z-lab/dflash](https://github.com/z-lab/dflash) | +298 | 4651 |
| 161 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +297 | 21872 |
| 162 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +296 | 2231 |
| 163 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +293 | 2229 |
| 164 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +288 | 12767 |
| 165 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +283 | 13525 |
| 166 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +283 | 2248 |
| 167 | [openai/skills](https://github.com/openai/skills) | +282 | 19598 |
| 168 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +282 | 25618 |
| 169 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +279 | 4393 |
| 170 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +276 | 37564 |
| 171 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +274 | 1798 |
| 172 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +270 | 4171 |
| 173 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +269 | 3434 |
| 174 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +256 | 19897 |
| 175 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +251 | 3957 |
| 176 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +245 | 27874 |
| 177 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +243 | 2421 |
| 178 | [MinishLab/semble](https://github.com/MinishLab/semble) | +231 | 3001 |
| 179 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +229 | 3457 |
| 180 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +229 | 1908 |
| 181 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +224 | 3926 |
| 182 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +218 | 2011 |
| 183 | [tiagozip/cap](https://github.com/tiagozip/cap) | +217 | 6401 |
| 184 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +214 | 7056 |
| 185 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +210 | 5354 |
| 186 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +205 | 14144 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +202 | 5072 |
| 188 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +200 | 1734 |
| 189 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +187 | 4517 |
| 190 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +179 | 2314 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +178 | 26826 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +177 | 3578 |
| 193 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +161 | 6050 |
| 194 | [88lin/video_vip](https://github.com/88lin/video_vip) | +158 | 1851 |
| 195 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +155 | 36103 |
| 196 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +152 | 10334 |
| 197 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +150 | 2138 |
| 198 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +148 | 2693 |
| 199 | [eze-is/web-access](https://github.com/eze-is/web-access) | +142 | 6621 |
| 200 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +141 | 16834 |
| 201 | [playcanvas/engine](https://github.com/playcanvas/engine) | +139 | 15835 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +133 | 39596 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +132 | 15189 |
| 204 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +132 | 0 |
| 205 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +131 | 1391 |
| 206 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +126 | 9928 |
| 207 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +125 | 3019 |
| 208 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +125 | 23018 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +121 | 41086 |
| 210 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +119 | 0 |
| 211 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +109 | 7927 |
| 212 | [sandeco/reversa](https://github.com/sandeco/reversa) | +108 | 888 |
| 213 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 824 |
| 214 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +104 | 1263 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +102 | 10329 |
| 216 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 1920 |
| 217 | [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | +99 | 780 |
| 218 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +96 | 40265 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +91 | 24097 |
| 220 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +91 | 35473 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +89 | 1502 |
| 222 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +84 | 14761 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +84 | 3857 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +81 | 11800 |
| 225 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +80 | 656 |
| 226 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +78 | 7768 |
| 227 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +77 | 9927 |
| 228 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +71 | 3187 |
| 229 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +69 | 8365 |
| 230 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +69 | 30141 |
| 231 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +68 | 2436 |
| 232 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +65 | 952 |
| 233 | [halo-dev/halo](https://github.com/halo-dev/halo) | +64 | 37991 |
| 234 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +63 | 45263 |
| 235 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +62 | 882 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +62 | 2543 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +61 | 13349 |
| 238 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +61 | 703 |
| 239 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +61 | 4306 |
| 240 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 453 |
| 241 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +60 | 48784 |
| 242 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +59 | 2188 |
| 243 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +59 | 37313 |
| 244 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +58 | 1367 |
| 245 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +57 | 3166 |
| 246 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +57 | 33000 |
| 247 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2506 |
| 248 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +56 | 11212 |
| 249 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +55 | 27607 |
| 250 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +54 | 1806 |
| 251 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +54 | 741 |
| 252 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +53 | 821 |
| 253 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +53 | 2151 |
| 254 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +51 | 1321 |
| 255 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +51 | 962 |
| 256 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +51 | 2144 |
| 257 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 511 |
| 258 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 301 |
| 259 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +50 | 3120 |
| 260 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +49 | 460 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +49 | 4105 |
| 262 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +48 | 897 |
| 263 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +48 | 327 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +46 | 1736 |
| 265 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +46 | 4172 |
| 266 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +46 | 1449 |
| 267 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +44 | 482 |
| 268 | [openmemind/memind](https://github.com/openmemind/memind) | +44 | 781 |
| 269 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +43 | 688 |
| 270 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +43 | 242 |
| 271 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 328 |
| 272 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +43 | 1244 |
| 273 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 327 |
| 274 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +41 | 12026 |
| 275 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +40 | 480 |
| 276 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +38 | 5124 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +37 | 1416 |
| 278 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +37 | 242 |
| 279 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +36 | 2180 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +36 | 9663 |
| 281 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +35 | 331 |
| 282 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +34 | 1914 |
| 283 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +33 | 2223 |
| 284 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +32 | 2390 |
| 285 | [intave/intave](https://github.com/intave/intave) | +32 | 257 |
| 286 | [FongMi/TV](https://github.com/FongMi/TV) | +31 | 8026 |
| 287 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +30 | 323 |
| 288 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 289 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +29 | 464 |
| 290 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 208 |
| 291 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +27 | 0 |
| 292 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +27 | 2635 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +27 | 1540 |
| 294 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 277 |
| 295 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2196 |
| 296 | [is-a-dev/register](https://github.com/is-a-dev/register) | +25 | 10309 |
| 297 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +25 | 2951 |
| 298 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +24 | 288 |
| 299 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +23 | 255 |
| 300 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +23 | 3233 |
