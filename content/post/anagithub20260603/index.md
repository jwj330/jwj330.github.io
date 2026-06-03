---
title: "2026-06-03 GitHub增长趋势报告"
description: "1.odysseus+376 2.headroom+110 3.Understand-Anything+51 4.codegraph+46 5.taste-skill+31"
date: 2026-06-03T22:29:02+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-03 22:29:02

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
        'daily': {"categories": ["jamwithai/production-agentic-rag-course", "CloakHQ/CloakBrowser", "anthropics/financial-services", "Yuan1z0825/nature-skills", "AlexsJones/llmfit", "getpaseo/paseo", "hugohe3/ppt-master", "rtk-ai/rtk", "can1357/oh-my-pi", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "fathah/hermes-desktop", "pbakaus/impeccable", "OpenBMB/VoxCPM", "nesquena/hermes-webui", "Leonxlnx/taste-skill", "colbymchenry/codegraph", "Lum1104/Understand-Anything", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [9, 9, 10, 10, 10, 10, 11, 12, 13, 17, 19, 19, 23, 27, 29, 31, 46, 51, 110, 376]},
        'weekly': {"categories": ["greensock/gsap-skills", "hugohe3/ppt-master", "heygen-com/hyperframes", "rohitg00/agentmemory", "Yuan1z0825/nature-skills", "rtk-ai/rtk", "supermemoryai/supermemory", "pbakaus/impeccable", "run-llama/liteparse", "safishamsi/graphify", "can1357/oh-my-pi", "Imbad0202/academic-research-skills", "OpenBMB/VoxCPM", "nesquena/hermes-webui", "chopratejas/headroom", "rohitg00/ai-engineering-from-scratch", "Leonxlnx/taste-skill", "colbymchenry/codegraph", "Lum1104/Understand-Anything", "pewdiepie-archdaemon/odysseus"], "data": [56, 59, 60, 61, 62, 65, 66, 68, 70, 74, 75, 84, 106, 120, 171, 175, 214, 268, 372, 968]},
        'monthly': {"categories": ["garrytan/gstack", "msitarzewski/agency-agents", "VoltAgent/awesome-design-md", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "TauricResearch/TradingAgents", "CloakHQ/CloakBrowser", "addyosmani/agent-skills", "anthropics/financial-services", "ruvnet/ruflo", "tinyhumansai/openhuman", "farion1231/cc-switch", "affaan-m/ECC", "colbymchenry/codegraph", "Lum1104/Understand-Anything", "obra/superpowers", "Hmbown/CodeWhale", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1473, 1498, 1559, 1588, 1609, 1829, 1850, 1871, 2012, 2066, 2251, 2408, 2601, 2702, 2949, 3015, 3175, 3913, 4629, 5180]}
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
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +376 | 42953 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +110 | 9478 |
| 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +51 | 51065 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +46 | 39251 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +31 | 32474 |
| 6 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +29 | 13074 |
| 7 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +27 | 25569 |
| 8 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +23 | 34052 |
| 9 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +19 | 9914 |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +19 | 27877 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 26703 |
| 12 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +13 | 10297 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +12 | 58412 |
| 14 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 24090 |
| 15 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +10 | 7600 |
| 16 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +10 | 27298 |
| 17 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +10 | 16059 |
| 18 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +10 | 29768 |
| 19 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +9 | 23632 |
| 20 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | +9 | 6662 |
| 21 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +9 | 58880 |
| 22 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +9 | 56016 |
| 23 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +9 | 20816 |
| 24 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +9 | 14702 |
| 25 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +9 | 13427 |
| 26 | [github/app](https://github.com/github/app) | +9 | 1288 |
| 27 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +9 | 9849 |
| 28 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +8 | 25101 |
| 29 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +8 | 2676 |
| 30 | [decolua/9router](https://github.com/decolua/9router) | +8 | 16122 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +968 | 42953 |
| 2 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +372 | 51065 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +268 | 39251 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +214 | 32474 |
| 5 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +175 | 27877 |
| 6 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +171 | 9478 |
| 7 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +120 | 13074 |
| 8 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +106 | 25569 |
| 9 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +84 | 26703 |
| 10 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +75 | 10297 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +74 | 58880 |
| 12 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +70 | 9047 |
| 13 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +68 | 34052 |
| 14 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +66 | 25125 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +65 | 58412 |
| 16 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +62 | 16059 |
| 17 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +61 | 20974 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +60 | 23945 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +59 | 24090 |
| 20 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +56 | 7635 |
| 21 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +55 | 13875 |
| 22 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +54 | 30610 |
| 23 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +52 | 4985 |
| 24 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +49 | 23418 |
| 25 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +46 | 9914 |
| 26 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +46 | 29768 |
| 27 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +46 | 4172 |
| 28 | [revfactory/harness](https://github.com/revfactory/harness) | +44 | 5676 |
| 29 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +43 | 13427 |
| 30 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +43 | 23632 |
| 31 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +42 | 19016 |
| 32 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +40 | 4914 |
| 33 | [freestylefly/CodexGuide](https://github.com/freestylefly/CodexGuide) | +39 | 1326 |
| 34 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +38 | 14702 |
| 35 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +37 | 41930 |
| 36 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +37 | 23216 |
| 37 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +36 | 1508 |
| 38 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +36 | 19592 |
| 39 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +35 | 64507 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +35 | 32069 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +35 | 34989 |
| 42 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +34 | 48039 |
| 43 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +33 | 25101 |
| 44 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +33 | 36889 |
| 45 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +33 | 5989 |
| 46 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +32 | 20816 |
| 47 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +32 | 900 |
| 48 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +32 | 56016 |
| 49 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +32 | 28318 |
| 50 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +32 | 7322 |
| 51 | [tw93/Kami](https://github.com/tw93/Kami) | +32 | 6988 |
| 52 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +32 | 8906 |
| 53 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +31 | 6666 |
| 54 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +30 | 4091 |
| 55 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +30 | 27019 |
| 56 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +29 | 9361 |
| 57 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +29 | 20878 |
| 58 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +29 | 12063 |
| 59 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +28 | 22544 |
| 60 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +28 | 27116 |
| 61 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +28 | 5294 |
| 62 | [decolua/9router](https://github.com/decolua/9router) | +27 | 16122 |
| 63 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +27 | 16183 |
| 64 | [antirez/ds4](https://github.com/antirez/ds4) | +27 | 12864 |
| 65 | [Chachamaru127/claude-code-harness](https://github.com/Chachamaru127/claude-code-harness) | +27 | 2592 |
| 66 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +26 | 1102 |
| 67 | [russellromney/honker](https://github.com/russellromney/honker) | +26 | 2729 |
| 68 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +25 | 28304 |
| 69 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +25 | 21248 |
| 70 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +25 | 2006 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +24 | 40234 |
| 72 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +24 | 15854 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +23 | 20193 |
| 74 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +22 | 9849 |
| 75 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +22 | 56236 |
| 76 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +22 | 41228 |
| 77 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +22 | 15585 |
| 78 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +21 | 7645 |
| 79 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +21 | 35949 |
| 80 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +21 | 29257 |
| 81 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +21 | 3920 |
| 82 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +21 | 4322 |
| 83 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +21 | 21180 |
| 84 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +21 | 12862 |
| 85 | [openai/skills](https://github.com/openai/skills) | +21 | 21259 |
| 86 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +20 | 7201 |
| 87 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +20 | 24120 |
| 88 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 8077 |
| 89 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +20 | 14181 |
| 90 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +20 | 7592 |
| 91 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +19 | 31787 |
| 92 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +19 | 35707 |
| 93 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +18 | 55609 |
| 94 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +18 | 16165 |
| 95 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +18 | 7600 |
| 96 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +18 | 10298 |
| 97 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +18 | 39619 |
| 98 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +18 | 16134 |
| 99 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +18 | 1922 |
| 100 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +18 | 2765 |
| 101 | [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | +18 | 1024 |
| 102 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +17 | 27298 |
| 103 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +17 | 4507 |
| 104 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 22232 |
| 105 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +17 | 6828 |
| 106 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +17 | 4154 |
| 107 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +17 | 2727 |
| 108 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +16 | 2218 |
| 109 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +16 | 11323 |
| 110 | [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | +15 | 2950 |
| 111 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +14 | 18940 |
| 112 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +14 | 7021 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +14 | 17046 |
| 114 | [tate233/todolist](https://github.com/tate233/todolist) | +14 | 1528 |
| 115 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +13 | 2676 |
| 116 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +13 | 34395 |
| 117 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +13 | 27125 |
| 118 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +12 | 2657 |
| 119 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +12 | 5420 |
| 120 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +11 | 4028 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5180 | 166834 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4629 | 116348 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3913 | 178992 |
| 4 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3175 | 36889 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +3015 | 60312 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2949 | 51065 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2702 | 39251 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2601 | 51199 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2408 | 90523 |
| 10 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2251 | 30610 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2066 | 57698 |
| 12 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2012 | 29768 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1871 | 48039 |
| 14 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1850 | 23632 |
| 15 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1829 | 30590 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1609 | 27877 |
| 17 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1588 | 26703 |
| 18 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1559 | 87121 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1498 | 107219 |
| 20 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1473 | 106733 |
| 21 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1472 | 20974 |
| 22 | [github/spec-kit](https://github.com/github/spec-kit) | +1397 | 71722 |
| 23 | [antirez/ds4](https://github.com/antirez/ds4) | +1366 | 12864 |
| 24 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1327 | 60158 |
| 25 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1321 | 70507 |
| 26 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1313 | 58880 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1233 | 58412 |
| 28 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1190 | 21248 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1184 | 56016 |
| 30 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1175 | 59386 |
| 31 | [decolua/9router](https://github.com/decolua/9router) | +1154 | 16122 |
| 32 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1149 | 68366 |
| 33 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1070 | 16059 |
| 34 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1028 | 24090 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1002 | 34148 |
| 36 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +976 | 29257 |
| 37 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +968 | 42953 |
| 38 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +946 | 32474 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +945 | 32069 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +880 | 34989 |
| 41 | [soxoj/maigret](https://github.com/soxoj/maigret) | +872 | 31247 |
| 42 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +844 | 15854 |
| 43 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +755 | 60960 |
| 44 | [floci-io/floci](https://github.com/floci-io/floci) | +740 | 13552 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +739 | 23945 |
| 46 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +734 | 11217 |
| 47 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +690 | 17833 |
| 48 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +676 | 49621 |
| 49 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +672 | 8020 |
| 50 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +663 | 36004 |
| 51 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +651 | 9914 |
| 52 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +650 | 55070 |
| 53 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +648 | 18009 |
| 54 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +646 | 20816 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +638 | 25101 |
| 56 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +629 | 6666 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +628 | 14702 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +617 | 34052 |
| 59 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +611 | 27116 |
| 60 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +601 | 41930 |
| 61 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +599 | 41228 |
| 62 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +593 | 52636 |
| 63 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +565 | 25217 |
| 64 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +561 | 12862 |
| 65 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +558 | 4485 |
| 66 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +551 | 36833 |
| 67 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +542 | 4094 |
| 68 | [santifer/career-ops](https://github.com/santifer/career-ops) | +509 | 48522 |
| 69 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +499 | 19134 |
| 70 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +498 | 19016 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +496 | 40234 |
| 72 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +492 | 64507 |
| 73 | [withcoral/coral](https://github.com/withcoral/coral) | +482 | 5154 |
| 74 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +466 | 23423 |
| 75 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +464 | 7201 |
| 76 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +462 | 9849 |
| 77 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +455 | 56236 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +454 | 42729 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +448 | 31787 |
| 80 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +447 | 13875 |
| 81 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +440 | 13427 |
| 82 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +439 | 8631 |
| 83 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +437 | 35949 |
| 84 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +436 | 13074 |
| 85 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +435 | 4702 |
| 86 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +434 | 5976 |
| 87 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +429 | 10297 |
| 88 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +425 | 29230 |
| 89 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +419 | 7645 |
| 90 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +418 | 14299 |
| 91 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +418 | 32499 |
| 92 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +417 | 20878 |
| 93 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +413 | 22544 |
| 94 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +401 | 7592 |
| 95 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +399 | 4832 |
| 96 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +399 | 28318 |
| 97 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +390 | 4420 |
| 98 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +389 | 15934 |
| 99 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +380 | 7322 |
| 100 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +371 | 5989 |
| 101 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +366 | 8349 |
| 102 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +361 | 12474 |
| 103 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +358 | 25569 |
| 104 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +355 | 5067 |
| 105 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +349 | 6954 |
| 106 | [jundot/omlx](https://github.com/jundot/omlx) | +347 | 15797 |
| 107 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +335 | 3640 |
| 108 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +332 | 5552 |
| 109 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +331 | 7191 |
| 110 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +325 | 4322 |
| 111 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +325 | 34891 |
| 112 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +310 | 4795 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +294 | 15585 |
| 114 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +288 | 5420 |
| 115 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +288 | 2414 |
| 116 | [MinishLab/semble](https://github.com/MinishLab/semble) | +287 | 4778 |
| 117 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +280 | 22769 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +279 | 15795 |
| 119 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +269 | 17046 |
| 120 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +267 | 2699 |
| 121 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +266 | 9029 |
| 122 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +266 | 3289 |
| 123 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +264 | 20202 |
| 124 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +260 | 39619 |
| 125 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +260 | 8113 |
| 126 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +259 | 10168 |
| 127 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +257 | 45614 |
| 128 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +256 | 17988 |
| 129 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +249 | 11323 |
| 130 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +249 | 36799 |
| 131 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +245 | 23216 |
| 132 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +244 | 4435 |
| 133 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +241 | 4154 |
| 134 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +239 | 26684 |
| 135 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 2035 |
| 136 | [openai/skills](https://github.com/openai/skills) | +234 | 21259 |
| 137 | [browserbase/skills](https://github.com/browserbase/skills) | +233 | 3486 |
| 138 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +228 | 33742 |
| 139 | [browser-use/video-use](https://github.com/browser-use/video-use) | +227 | 8949 |
| 140 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +226 | 27125 |
| 141 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +225 | 2770 |
| 142 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +223 | 6287 |
| 143 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +215 | 2409 |
| 144 | [z-lab/dflash](https://github.com/z-lab/dflash) | +212 | 4878 |
| 145 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +212 | 24394 |
| 146 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +207 | 2671 |
| 147 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +206 | 2884 |
| 148 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +206 | 2657 |
| 149 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +204 | 5322 |
| 150 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +200 | 9478 |
| 151 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +200 | 2676 |
| 152 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +197 | 22630 |
| 153 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +195 | 3938 |
| 154 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +194 | 33772 |
| 155 | [88lin/video_vip](https://github.com/88lin/video_vip) | +193 | 3451 |
| 156 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +191 | 7021 |
| 157 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +190 | 34395 |
| 158 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +189 | 2370 |
| 159 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +189 | 1723 |
| 160 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +187 | 27797 |
| 161 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +183 | 26445 |
| 162 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +181 | 2550 |
| 163 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +181 | 0 |
| 164 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +176 | 13543 |
| 165 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +175 | 20969 |
| 166 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +173 | 2218 |
| 167 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +172 | 1873 |
| 168 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +167 | 7337 |
| 169 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +167 | 6430 |
| 170 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +166 | 4709 |
| 171 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +166 | 37564 |
| 172 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +165 | 4985 |
| 173 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +163 | 43596 |
| 174 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +157 | 23418 |
| 175 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1887 |
| 176 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +154 | 7577 |
| 177 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +154 | 28822 |
| 178 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +152 | 15111 |
| 179 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +150 | 6352 |
| 180 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +150 | 10692 |
| 181 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +146 | 2346 |
| 182 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +143 | 6019 |
| 183 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +141 | 2765 |
| 184 | [playcanvas/engine](https://github.com/playcanvas/engine) | +130 | 15941 |
| 185 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +129 | 3920 |
| 186 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2006 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +124 | 5359 |
| 188 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +120 | 36103 |
| 189 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +119 | 27526 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +117 | 4969 |
| 191 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +116 | 17617 |
| 192 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +110 | 4110 |
| 193 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +110 | 4143 |
| 194 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +110 | 899 |
| 195 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +108 | 1464 |
| 196 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +107 | 8524 |
| 197 | [usebruno/bruno](https://github.com/usebruno/bruno) | +100 | 41086 |
| 198 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +99 | 3644 |
| 199 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +99 | 39596 |
| 200 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +96 | 1089 |
| 201 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +96 | 11987 |
| 202 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 790 |
| 203 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +93 | 2178 |
| 204 | [eze-is/web-access](https://github.com/eze-is/web-access) | +92 | 7103 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +92 | 23483 |
| 206 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +91 | 2116 |
| 207 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +87 | 15551 |
| 208 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +86 | 10160 |
| 209 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +80 | 10745 |
| 210 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +77 | 1508 |
| 211 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +75 | 15068 |
| 212 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +74 | 3305 |
| 213 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +73 | 898 |
| 214 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +73 | 4801 |
| 215 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +71 | 3380 |
| 216 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +70 | 1150 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +70 | 40265 |
| 218 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2470 |
| 219 | [sandeco/reversa](https://github.com/sandeco/reversa) | +66 | 1175 |
| 220 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +64 | 35473 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +60 | 1907 |
| 222 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +59 | 37313 |
| 223 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +57 | 8120 |
| 224 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +56 | 4790 |
| 225 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +53 | 2143 |
| 226 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +53 | 45263 |
| 227 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +52 | 11967 |
| 228 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 375 |
| 229 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 230 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +49 | 663 |
| 231 | [robinebers/openusage](https://github.com/robinebers/openusage) | +48 | 2735 |
| 232 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +46 | 8604 |
| 233 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 498 |
| 234 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +45 | 7691 |
| 235 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +45 | 3456 |
| 236 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +44 | 4189 |
| 237 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 365 |
| 238 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +44 | 697 |
| 239 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +43 | 535 |
| 240 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 345 |
| 241 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +42 | 2528 |
| 242 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +40 | 438 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +40 | 13572 |
| 244 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +39 | 1228 |
| 245 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +39 | 4812 |
| 246 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +37 | 4322 |
| 247 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +36 | 9870 |
| 248 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +34 | 1711 |
| 249 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +34 | 1709 |
| 250 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 291 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +34 | 2399 |
| 252 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +32 | 4214 |
| 253 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +32 | 816 |
| 254 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 277 |
| 255 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +32 | 1040 |
| 256 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +32 | 1095 |
| 257 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +32 | 2359 |
| 258 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +31 | 1702 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +31 | 896 |
| 260 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +31 | 3336 |
| 261 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +30 | 2059 |
| 262 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +29 | 558 |
| 263 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +29 | 2198 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +28 | 1935 |
| 265 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +28 | 2336 |
| 266 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 343 |
| 267 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +27 | 7640 |
| 268 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +27 | 5248 |
| 269 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +26 | 284 |
| 270 | [xu-xiang/everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh) | +24 | 919 |
| 271 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +24 | 1437 |
| 272 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +21 | 381 |
| 273 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +21 | 229 |
| 274 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +21 | 789 |
| 275 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +20 | 1540 |
| 276 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +19 | 266 |
| 277 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2977 |
| 278 | [is-a-dev/register](https://github.com/is-a-dev/register) | +18 | 10407 |
| 279 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +18 | 549 |
| 280 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2664 |
| 281 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +17 | 394 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +16 | 2475 |
| 283 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +16 | 817 |
| 284 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3257 |
| 285 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1076 |
| 286 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +14 | 1587 |
| 287 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +13 | 2028 |
| 288 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +12 | 528 |
| 289 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +11 | 2254 |
| 290 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 207 |
| 291 | [fengqiwby/Blockchain-assisted_TraceGuard](https://github.com/fengqiwby/Blockchain-assisted_TraceGuard) | +11 | 126 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +11 | 965 |
| 293 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 294 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +10 | 294 |
| 295 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +10 | 346 |
| 296 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +9 | 463 |
| 297 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 451 |
| 298 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 139 |
| 299 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +9 | 265 |
| 300 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +8 | 451 |
