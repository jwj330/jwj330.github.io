---
title: "2026-05-21 GitHub增长趋势报告"
description: "1.codegraph+273 2.academic-research-skills+155 3.ai-engineering-from-scratch+86 4.openhuman+84 5.streambert+69"
date: 2026-05-21T21:28:06+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-21 21:28:06

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
        'daily': {"categories": ["Thysrael/Horizon", "HKUDS/ViMax", "Yuan1z0825/nature-skills", "awslabs/aidlc-workflows", "rtk-ai/rtk", "anthropics/claude-plugins-official", "thananon/9arm-skills", "alchaincyf/nuwa-skill", "HKUDS/CLI-Anything", "withcoral/coral", "Lum1104/Understand-Anything", "rmyndharis/OpenWA", "CloakHQ/CloakBrowser", "rohitg00/agentmemory", "tashfeenahmed/freellmapi", "truelockmc/streambert", "tinyhumansai/openhuman", "rohitg00/ai-engineering-from-scratch", "Imbad0202/academic-research-skills", "colbymchenry/codegraph"], "data": [32, 33, 34, 34, 35, 35, 37, 38, 39, 40, 45, 45, 57, 61, 63, 69, 84, 86, 155, 273]},
        'weekly': {"categories": ["rtk-ai/rtk", "HKUDS/CLI-Anything", "Yuan1z0825/nature-skills", "rmyndharis/OpenWA", "anthropics/financial-services", "Tencent/TencentDB-Agent-Memory", "vercel-labs/zero", "K-Dense-AI/scientific-agent-skills", "neilsonnn/image-blaster", "Hmbown/DeepSeek-TUI", "supertone-inc/supertonic", "anthropics/claude-for-legal", "rohitg00/agentmemory", "ruvnet/RuView", "CloakHQ/CloakBrowser", "colbymchenry/codegraph", "Imbad0202/academic-research-skills", "forrestchang/andrej-karpathy-skills", "tinyhumansai/openhuman", "mattpocock/skills"], "data": [288, 300, 301, 304, 315, 344, 349, 358, 367, 401, 405, 497, 549, 605, 614, 735, 740, 1057, 1266, 1335]},
        'monthly': {"categories": ["anomalyco/opencode", "msitarzewski/agency-agents", "JuliusBrussee/caveman", "rtk-ai/rtk", "safishamsi/graphify", "VoltAgent/awesome-design-md", "garrytan/gstack", "Z4nzu/hackingtool", "ruvnet/ruflo", "addyosmani/agent-skills", "affaan-m/everything-claude-code", "farion1231/cc-switch", "warpdotdev/warp", "Hmbown/DeepSeek-TUI", "TauricResearch/TradingAgents", "Alishahryar1/free-claude-code", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1870, 2090, 2171, 2175, 2213, 2303, 2342, 2373, 2621, 2791, 3004, 3058, 3136, 3211, 3238, 3289, 3980, 6007, 8555, 8758]}
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
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +273 | 13136 |
| 2 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +155 | 18073 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +86 | 10636 |
| 4 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +84 | 24760 |
| 5 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +69 | 3891 |
| 6 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +63 | 3458 |
| 7 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +61 | 15752 |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +57 | 18160 |
| 9 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +45 | 5365 |
| 10 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +45 | 16507 |
| 11 | [withcoral/coral](https://github.com/withcoral/coral) | +40 | 3510 |
| 12 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +39 | 39055 |
| 13 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +38 | 20623 |
| 14 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +37 | 1155 |
| 15 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +35 | 22195 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +35 | 52369 |
| 17 | [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | +34 | 2343 |
| 18 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 10022 |
| 19 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +33 | 6437 |
| 20 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +32 | 4386 |
| 21 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +32 | 5809 |
| 22 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | +31 | 5681 |
| 23 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +30 | 18971 |
| 24 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +29 | 50697 |
| 25 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +26 | 1930 |
| 26 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +26 | 33148 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +26 | 30647 |
| 28 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +25 | 27417 |
| 29 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +24 | 3821 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +24 | 19385 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1335 | 98906 |
| 2 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1266 | 24760 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1057 | 142964 |
| 4 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +740 | 18073 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +735 | 13136 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +614 | 18160 |
| 7 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +605 | 62961 |
| 8 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +549 | 15753 |
| 9 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +497 | 7415 |
| 10 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +405 | 9139 |
| 11 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +401 | 33148 |
| 12 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +367 | 3903 |
| 13 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +358 | 25083 |
| 14 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +349 | 4188 |
| 15 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +344 | 3746 |
| 16 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +315 | 26475 |
| 17 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +304 | 5365 |
| 18 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +301 | 10022 |
| 19 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +300 | 39055 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +288 | 52369 |
| 21 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +287 | 16417 |
| 22 | [decolua/9router](https://github.com/decolua/9router) | +284 | 13203 |
| 23 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +273 | 13764 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +269 | 44568 |
| 25 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +251 | 4355 |
| 26 | [withcoral/coral](https://github.com/withcoral/coral) | +245 | 3510 |
| 27 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +238 | 3790 |
| 28 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +233 | 3891 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +227 | 19385 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +219 | 18971 |
| 31 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +217 | 15928 |
| 32 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +204 | 52165 |
| 33 | [floci-io/floci](https://github.com/floci-io/floci) | +199 | 12685 |
| 34 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +198 | 7227 |
| 35 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +196 | 17996 |
| 36 | [antirez/ds4](https://github.com/antirez/ds4) | +196 | 11166 |
| 37 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +187 | 22206 |
| 38 | [MinishLab/semble](https://github.com/MinishLab/semble) | +179 | 3548 |
| 39 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +179 | 2487 |
| 40 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +176 | 8586 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +175 | 38320 |
| 42 | [larksuite/cli](https://github.com/larksuite/cli) | +175 | 12239 |
| 43 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +173 | 50697 |
| 44 | [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) | +169 | 1362 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +166 | 20223 |
| 46 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +163 | 1447 |
| 47 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +162 | 10636 |
| 48 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +162 | 6437 |
| 49 | [compozy/compozy](https://github.com/compozy/compozy) | +160 | 2128 |
| 50 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +159 | 27417 |
| 51 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +156 | 4363 |
| 52 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +152 | 43470 |
| 53 | [multica-ai/multica](https://github.com/multica-ai/multica) | +147 | 30647 |
| 54 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +143 | 27382 |
| 55 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +143 | 10953 |
| 56 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +142 | 49802 |
| 57 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +142 | 1715 |
| 58 | [santifer/career-ops](https://github.com/santifer/career-ops) | +139 | 46548 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +127 | 22553 |
| 60 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +126 | 1570 |
| 61 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +126 | 40326 |
| 62 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +125 | 3458 |
| 63 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +124 | 17163 |
| 64 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +121 | 10633 |
| 65 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +120 | 34699 |
| 66 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +117 | 22195 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +117 | 29376 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +114 | 29916 |
| 69 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +114 | 6285 |
| 70 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +111 | 4364 |
| 71 | [soxoj/maigret](https://github.com/soxoj/maigret) | +111 | 29788 |
| 72 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +110 | 39577 |
| 73 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +107 | 864 |
| 74 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | +107 | 20360 |
| 75 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +105 | 12425 |
| 76 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +105 | 10820 |
| 77 | [blader/humanizer](https://github.com/blader/humanizer) | +104 | 20230 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +103 | 24747 |
| 79 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +102 | 18394 |
| 80 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +101 | 16507 |
| 81 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +100 | 1946 |
| 82 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +97 | 20623 |
| 83 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +97 | 61799 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +96 | 34007 |
| 85 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +95 | 32376 |
| 86 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +92 | 8731 |
| 87 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +91 | 1293 |
| 88 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +90 | 1729 |
| 89 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +90 | 54185 |
| 90 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +89 | 19560 |
| 91 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +88 | 1456 |
| 92 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +88 | 1930 |
| 93 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +87 | 18502 |
| 94 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +86 | 5809 |
| 95 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +85 | 1155 |
| 96 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +83 | 6430 |
| 97 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +82 | 686 |
| 98 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +81 | 18443 |
| 99 | [NVIDIA-AI-Blueprints/video-search-and-summarization](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) | +80 | 1412 |
| 100 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +79 | 33746 |
| 101 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +76 | 8172 |
| 102 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +74 | 15201 |
| 103 | [shang-zhu/violin](https://github.com/shang-zhu/violin) | +74 | 771 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +74 | 44459 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +72 | 15770 |
| 106 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +71 | 2003 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +71 | 1308 |
| 108 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +71 | 22111 |
| 109 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +70 | 4386 |
| 110 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +70 | 2364 |
| 111 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +70 | 25463 |
| 112 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +68 | 10297 |
| 113 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +68 | 13427 |
| 114 | [byrongamatos/slopsmith](https://github.com/byrongamatos/slopsmith) | +68 | 1017 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +67 | 14333 |
| 116 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +67 | 6138 |
| 117 | [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | +63 | 11645 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +60 | 14102 |
| 119 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +59 | 1294 |
| 120 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +57 | 1318 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8758 | 142964 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8555 | 98906 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +6007 | 161368 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3980 | 60312 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3289 | 27417 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3238 | 30590 |
| 7 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3211 | 33148 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3136 | 59425 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3058 | 77277 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3004 | 51199 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2791 | 44568 |
| 12 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2621 | 53888 |
| 13 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2373 | 55070 |
| 14 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2342 | 100439 |
| 15 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2303 | 82272 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2213 | 50697 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2175 | 52369 |
| 18 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2171 | 63239 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2090 | 103593 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1870 | 109881 |
| 21 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1863 | 26475 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +1774 | 74774 |
| 23 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1772 | 24760 |
| 24 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1733 | 15201 |
| 25 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1673 | 52568 |
| 26 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1631 | 11178 |
| 27 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1603 | 52548 |
| 28 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1578 | 18971 |
| 29 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1530 | 14545 |
| 30 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1491 | 22111 |
| 31 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1489 | 30678 |
| 32 | [github/spec-kit](https://github.com/github/spec-kit) | +1485 | 71722 |
| 33 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1462 | 18160 |
| 34 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1416 | 39577 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1409 | 52165 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1353 | 34148 |
| 37 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1346 | 16417 |
| 38 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1335 | 29788 |
| 39 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1309 | 30647 |
| 40 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1301 | 19385 |
| 41 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1296 | 20223 |
| 42 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1277 | 85286 |
| 43 | [antirez/ds4](https://github.com/antirez/ds4) | +1251 | 11166 |
| 44 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1245 | 62961 |
| 45 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1201 | 10953 |
| 46 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1176 | 15753 |
| 47 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1160 | 18073 |
| 48 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1124 | 13427 |
| 49 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1088 | 66988 |
| 50 | [decolua/9router](https://github.com/decolua/9router) | +1070 | 13203 |
| 51 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1066 | 10820 |
| 52 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1015 | 46548 |
| 53 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +938 | 13764 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +924 | 22553 |
| 55 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +922 | 13272 |
| 56 | [openai/symphony](https://github.com/openai/symphony) | +915 | 24395 |
| 57 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +912 | 18502 |
| 58 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +893 | 10022 |
| 59 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +880 | 63517 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +875 | 17996 |
| 61 | [openai/codex](https://github.com/openai/codex) | +867 | 61744 |
| 62 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +861 | 16507 |
| 63 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +852 | 82560 |
| 64 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +842 | 54185 |
| 65 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +835 | 29376 |
| 66 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +830 | 51085 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +814 | 29916 |
| 68 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +814 | 6435 |
| 69 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +810 | 13136 |
| 70 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +810 | 11940 |
| 71 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +809 | 47343 |
| 72 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +787 | 49802 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +780 | 38320 |
| 74 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +776 | 6257 |
| 75 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +765 | 15341 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +758 | 20623 |
| 77 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +741 | 6434 |
| 78 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +733 | 34699 |
| 79 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +726 | 7978 |
| 80 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +717 | 32376 |
| 81 | [floci-io/floci](https://github.com/floci-io/floci) | +713 | 12685 |
| 82 | [browser-use/video-use](https://github.com/browser-use/video-use) | +681 | 8166 |
| 83 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +680 | 61800 |
| 84 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +677 | 8731 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +676 | 34007 |
| 86 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +674 | 5791 |
| 87 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +666 | 37330 |
| 88 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +661 | 33878 |
| 89 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +654 | 5567 |
| 90 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +640 | 7415 |
| 91 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +637 | 22206 |
| 92 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +632 | 61484 |
| 93 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +620 | 33746 |
| 94 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +619 | 34910 |
| 95 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +619 | 25463 |
| 96 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +617 | 15928 |
| 97 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +603 | 11323 |
| 98 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +601 | 39055 |
| 99 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +587 | 47122 |
| 100 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +577 | 25083 |
| 101 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +573 | 10636 |
| 102 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +565 | 17104 |
| 103 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +553 | 9139 |
| 104 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +545 | 8172 |
| 105 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +541 | 6285 |
| 106 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +531 | 24179 |
| 107 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +515 | 4363 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +510 | 19340 |
| 109 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +493 | 18394 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +482 | 44459 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +466 | 6138 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +465 | 14804 |
| 113 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +458 | 31904 |
| 114 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +442 | 20489 |
| 115 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +440 | 19336 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +439 | 14102 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +435 | 38278 |
| 118 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +416 | 2750 |
| 119 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +388 | 3823 |
| 120 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +386 | 3601 |
| 121 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +386 | 5570 |
| 122 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +385 | 15770 |
| 123 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +376 | 7882 |
| 124 | [browserbase/skills](https://github.com/browserbase/skills) | +374 | 3395 |
| 125 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +371 | 26304 |
| 126 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +363 | 9953 |
| 127 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +362 | 36799 |
| 128 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +362 | 21452 |
| 129 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +351 | 27473 |
| 130 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +343 | 22195 |
| 131 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +338 | 9490 |
| 132 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +336 | 23394 |
| 133 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +333 | 5433 |
| 134 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +332 | 6531 |
| 135 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +326 | 6973 |
| 136 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +325 | 5087 |
| 137 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +319 | 1669 |
| 138 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +318 | 2593 |
| 139 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +317 | 26553 |
| 140 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +316 | 14333 |
| 141 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3902 |
| 142 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +309 | 2872 |
| 143 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +309 | 32620 |
| 144 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +308 | 5313 |
| 145 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +306 | 4355 |
| 146 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +306 | 4648 |
| 147 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +305 | 33557 |
| 148 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +304 | 21814 |
| 149 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +304 | 3776 |
| 150 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +298 | 2260 |
| 151 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +296 | 2307 |
| 152 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +292 | 42946 |
| 153 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +291 | 2550 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +286 | 27088 |
| 155 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +286 | 32761 |
| 156 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +284 | 4386 |
| 157 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +284 | 21954 |
| 158 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +284 | 2298 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +283 | 10297 |
| 160 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +279 | 1860 |
| 161 | [z-lab/dflash](https://github.com/z-lab/dflash) | +277 | 4687 |
| 162 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +276 | 3790 |
| 163 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +275 | 13563 |
| 164 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +275 | 25743 |
| 165 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +271 | 6437 |
| 166 | [openai/skills](https://github.com/openai/skills) | +269 | 19766 |
| 167 | [MinishLab/semble](https://github.com/MinishLab/semble) | +268 | 3548 |
| 168 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +259 | 39841 |
| 169 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +257 | 18316 |
| 170 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +252 | 4214 |
| 171 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +246 | 12900 |
| 172 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +245 | 37564 |
| 173 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +244 | 2446 |
| 174 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +239 | 20039 |
| 175 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +238 | 28036 |
| 176 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +234 | 3892 |
| 177 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +231 | 1926 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +228 | 6345 |
| 179 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +227 | 3593 |
| 180 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +224 | 4207 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +214 | 7130 |
| 182 | [tiagozip/cap](https://github.com/tiagozip/cap) | +214 | 6425 |
| 183 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +213 | 2003 |
| 184 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +202 | 7227 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +191 | 14274 |
| 186 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +188 | 2487 |
| 187 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +171 | 26921 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +170 | 3637 |
| 189 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +169 | 5124 |
| 190 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +161 | 7525 |
| 191 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +159 | 4639 |
| 192 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +159 | 2024 |
| 193 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +157 | 6106 |
| 194 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +145 | 36103 |
| 195 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +143 | 10388 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +139 | 2797 |
| 197 | [playcanvas/engine](https://github.com/playcanvas/engine) | +138 | 15859 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +133 | 16907 |
| 199 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +133 | 15230 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +127 | 0 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +123 | 6695 |
| 202 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +122 | 1465 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +122 | 9942 |
| 204 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +122 | 39596 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +119 | 41086 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +113 | 23087 |
| 207 | [sandeco/reversa](https://github.com/sandeco/reversa) | +111 | 911 |
| 208 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +107 | 4445 |
| 209 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 835 |
| 210 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +101 | 0 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +100 | 3070 |
| 212 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +100 | 7966 |
| 213 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +99 | 1293 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +96 | 1976 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +94 | 10359 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +89 | 40265 |
| 217 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +86 | 14809 |
| 218 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +85 | 24139 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +85 | 35473 |
| 220 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +82 | 686 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +81 | 1555 |
| 222 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +75 | 9958 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +71 | 3899 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +69 | 11838 |
| 225 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +68 | 2444 |
| 226 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +67 | 8400 |
| 227 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +65 | 3207 |
| 228 | [qist/tvbox](https://github.com/qist/tvbox) | +61 | 9406 |
| 229 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +60 | 13374 |
| 230 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +60 | 48784 |
| 231 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +59 | 30163 |
| 232 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +59 | 37313 |
| 233 | [88lin/video_vip](https://github.com/88lin/video_vip) | +57 | 1949 |
| 234 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +57 | 455 |
| 235 | [halo-dev/halo](https://github.com/halo-dev/halo) | +57 | 37991 |
| 236 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +56 | 45263 |
| 237 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +54 | 711 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +54 | 2543 |
| 239 | [robinebers/openusage](https://github.com/robinebers/openusage) | +53 | 2527 |
| 240 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +53 | 1820 |
| 241 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +53 | 2263 |
| 242 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +52 | 33000 |
| 243 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +51 | 975 |
| 244 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +50 | 832 |
| 245 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 514 |
| 246 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 302 |
| 247 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +50 | 970 |
| 248 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +50 | 3213 |
| 249 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +50 | 27625 |
| 250 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +49 | 468 |
| 251 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +49 | 2173 |
| 252 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +48 | 336 |
| 253 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +48 | 11225 |
| 254 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +47 | 776 |
| 255 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +47 | 263 |
| 256 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +46 | 580 |
| 257 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +45 | 1478 |
| 258 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +45 | 3129 |
| 259 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +44 | 4181 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +44 | 2177 |
| 261 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 328 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +43 | 4135 |
| 263 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +42 | 884 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +42 | 1760 |
| 265 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +42 | 917 |
| 266 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 329 |
| 267 | [openmemind/memind](https://github.com/openmemind/memind) | +41 | 799 |
| 268 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +40 | 493 |
| 269 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +39 | 1393 |
| 270 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +39 | 12055 |
| 271 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +37 | 1354 |
| 272 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +37 | 1940 |
| 273 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +37 | 243 |
| 274 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +36 | 616 |
| 275 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +35 | 5136 |
| 276 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1426 |
| 277 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +35 | 490 |
| 278 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +34 | 748 |
| 279 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +34 | 2211 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9688 |
| 281 | [intave/intave](https://github.com/intave/intave) | +32 | 259 |
| 282 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 753 |
| 283 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +29 | 218 |
| 284 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +27 | 2395 |
| 285 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 287 |
| 286 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +26 | 319 |
| 287 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2209 |
| 288 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +25 | 0 |
| 289 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +25 | 2637 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +24 | 1541 |
| 291 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +24 | 329 |
| 292 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +23 | 338 |
| 293 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +23 | 2952 |
| 294 | [is-a-dev/register](https://github.com/is-a-dev/register) | +22 | 10321 |
| 295 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 296 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +21 | 209 |
| 297 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +20 | 3235 |
| 298 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +19 | 446 |
| 299 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +18 | 863 |
| 300 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +17 | 464 |
