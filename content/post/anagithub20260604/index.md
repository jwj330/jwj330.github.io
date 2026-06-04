---
title: "2026-06-04 GitHub增长趋势报告"
description: "1.odysseus+335 2.astrid+199 3.headroom+117 4.codegraph+58 5.Vibe-Trading+28"
date: 2026-06-04T21:42:40+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-04 21:42:40

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
        'daily': {"categories": ["Yuan1z0825/nature-skills", "datawhalechina/hello-agents", "getpaseo/paseo", "Crosstalk-Solutions/project-nomad", "shareAI-lab/learn-claude-code", "rtk-ai/rtk", "pbakaus/impeccable", "rohitg00/ai-engineering-from-scratch", "mukul975/Anthropic-Cybersecurity-Skills", "nesquena/hermes-webui", "safishamsi/graphify", "ZhuLinsen/daily_stock_analysis", "Leonxlnx/taste-skill", "MadsLorentzen/ai-job-search", "Lum1104/Understand-Anything", "HKUDS/Vibe-Trading", "colbymchenry/codegraph", "chopratejas/headroom", "unicity-astrid/astrid", "pewdiepie-archdaemon/odysseus"], "data": [11, 12, 12, 12, 13, 16, 16, 16, 16, 16, 18, 18, 24, 25, 27, 28, 58, 117, 199, 335]},
        'weekly': {"categories": ["revfactory/harness", "can1357/oh-my-pi", "heygen-com/hyperframes", "rtk-ai/rtk", "opendataloader-project/opendataloader-pdf", "Yuan1z0825/nature-skills", "safishamsi/graphify", "reconurge/flowsint", "Imbad0202/academic-research-skills", "pbakaus/impeccable", "supermemoryai/supermemory", "rohitg00/ai-engineering-from-scratch", "OpenBMB/VoxCPM", "Leonxlnx/taste-skill", "nesquena/hermes-webui", "Lum1104/Understand-Anything", "unicity-astrid/astrid", "colbymchenry/codegraph", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [48, 49, 49, 49, 53, 53, 55, 56, 66, 69, 73, 89, 108, 113, 127, 169, 199, 201, 284, 1295]},
        'monthly': {"categories": ["github/spec-kit", "garrytan/gstack", "VoltAgent/awesome-design-md", "rohitg00/agentmemory", "ruvnet/ruflo", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "addyosmani/agent-skills", "CloakHQ/CloakBrowser", "anthropics/financial-services", "tinyhumansai/openhuman", "farion1231/cc-switch", "affaan-m/ECC", "colbymchenry/codegraph", "Lum1104/Understand-Anything", "obra/superpowers", "Hmbown/CodeWhale", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1379, 1389, 1433, 1474, 1547, 1556, 1610, 1814, 1847, 2018, 2259, 2318, 2520, 2755, 2873, 2881, 2994, 3665, 4312, 4682]}
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
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +335 | 50518 |
| 2 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +199 | 6391 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +117 | 12283 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +58 | 40816 |
| 5 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +28 | 10611 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +27 | 51957 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +25 | 1674 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +24 | 33080 |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +18 | 40750 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +18 | 59327 |
| 11 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +16 | 13373 |
| 12 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +16 | 14143 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +16 | 28356 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +16 | 34412 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +16 | 58847 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +13 | 64709 |
| 17 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +12 | 28706 |
| 18 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +12 | 7763 |
| 19 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +12 | 56461 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +11 | 16593 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +11 | 24293 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +10 | 27209 |
| 23 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +10 | 5960 |
| 24 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +10 | 10529 |
| 25 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +9 | 10252 |
| 26 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +9 | 25825 |
| 27 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +9 | 29943 |
| 28 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +9 | 25269 |
| 29 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 35250 |
| 30 | [MaxMiksa/Auto-Company](https://github.com/MaxMiksa/Auto-Company) | +8 | 1063 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1295 | 50519 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +284 | 12283 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +201 | 40816 |
| 4 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +199 | 6391 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +169 | 51957 |
| 6 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +127 | 13373 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +113 | 33080 |
| 8 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +108 | 25825 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +89 | 28356 |
| 10 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +73 | 25495 |
| 11 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +69 | 34412 |
| 12 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +66 | 27209 |
| 13 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +56 | 5256 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +55 | 59327 |
| 15 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +53 | 16593 |
| 16 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +53 | 23672 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +49 | 58847 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +49 | 24293 |
| 19 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +49 | 10529 |
| 20 | [revfactory/harness](https://github.com/revfactory/harness) | +48 | 5934 |
| 21 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +48 | 9530 |
| 22 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +47 | 4243 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +46 | 10611 |
| 24 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +46 | 13604 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +44 | 24373 |
| 26 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +43 | 7784 |
| 27 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +40 | 21191 |
| 28 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +39 | 10252 |
| 29 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +38 | 23885 |
| 30 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +37 | 40750 |
| 31 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +37 | 14143 |
| 32 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +37 | 30771 |
| 33 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +36 | 1529 |
| 34 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +35 | 28706 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +35 | 56461 |
| 36 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +34 | 9124 |
| 37 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +34 | 924 |
| 38 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +33 | 64709 |
| 39 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +33 | 19728 |
| 40 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +32 | 1674 |
| 41 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +32 | 20973 |
| 42 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +31 | 23663 |
| 43 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +31 | 4290 |
| 44 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +31 | 6732 |
| 45 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +30 | 25269 |
| 46 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +29 | 9418 |
| 47 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +28 | 29943 |
| 48 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +26 | 7763 |
| 49 | [decolua/9router](https://github.com/decolua/9router) | +26 | 16308 |
| 50 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +26 | 37051 |
| 51 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +26 | 14980 |
| 52 | [multica-ai/multica](https://github.com/multica-ai/multica) | +24 | 35250 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 32342 |
| 54 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +24 | 27398 |
| 55 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +24 | 16267 |
| 56 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +24 | 27301 |
| 57 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +23 | 1162 |
| 58 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +22 | 7478 |
| 59 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +21 | 16021 |
| 60 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +21 | 6133 |
| 61 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +21 | 21351 |
| 62 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +21 | 42033 |
| 63 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +20 | 56399 |
| 64 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +20 | 7306 |
| 65 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +20 | 20972 |
| 66 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +20 | 16227 |
| 67 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +19 | 48260 |
| 68 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +19 | 41331 |
| 69 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +19 | 10435 |
| 70 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +19 | 8174 |
| 71 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +19 | 19112 |
| 72 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +18 | 22695 |
| 73 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +18 | 28460 |
| 74 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +18 | 55806 |
| 75 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +18 | 2871 |
| 76 | [withastro/flue](https://github.com/withastro/flue) | +17 | 4371 |
| 77 | [github/app](https://github.com/github/app) | +17 | 1355 |
| 78 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +17 | 36062 |
| 79 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +17 | 24227 |
| 80 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +17 | 23514 |
| 81 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +17 | 2148 |
| 82 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +17 | 4526 |
| 83 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +16 | 7744 |
| 84 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +16 | 27251 |
| 85 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +16 | 16238 |
| 86 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +16 | 3976 |
| 87 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +16 | 19003 |
| 88 | [blader/humanizer](https://github.com/blader/humanizer) | +16 | 22367 |
| 89 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +16 | 6916 |
| 90 | [MaxMiksa/Auto-Company](https://github.com/MaxMiksa/Auto-Company) | +15 | 1063 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +15 | 39715 |
| 92 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | +15 | 6704 |
| 93 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +15 | 5960 |
| 94 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +15 | 4404 |
| 95 | [santifer/career-ops](https://github.com/santifer/career-ops) | +15 | 48694 |
| 96 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +15 | 21299 |
| 97 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +15 | 5375 |
| 98 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +15 | 6052 |
| 99 | [edison7009/EchoBird](https://github.com/edison7009/EchoBird) | +14 | 1776 |
| 100 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +14 | 20489 |
| 101 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +13 | 21174 |
| 102 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 15666 |
| 103 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +13 | 0 |
| 104 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | +13 | 2147 |
| 105 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +13 | 7068 |
| 106 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +12 | 4698 |
| 107 | [sandroandric/AgentHandover](https://github.com/sandroandric/AgentHandover) | +12 | 701 |
| 108 | [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | +12 | 3073 |
| 109 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +12 | 1695 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +12 | 11394 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +12 | 29347 |
| 112 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +12 | 5035 |
| 113 | [browser-use/video-use](https://github.com/browser-use/video-use) | +12 | 9001 |
| 114 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +11 | 3407 |
| 115 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +11 | 1409 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +11 | 17149 |
| 117 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +10 | 4061 |
| 118 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +10 | 5684 |
| 119 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +10 | 34463 |
| 120 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +10 | 5493 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4682 | 167692 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4312 | 117550 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3665 | 180851 |
| 4 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +2994 | 37051 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +2881 | 60312 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2873 | 51957 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2755 | 40816 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2520 | 51199 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2318 | 91645 |
| 10 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2259 | 30771 |
| 11 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2018 | 29943 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1847 | 23885 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1814 | 48260 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1610 | 28356 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1556 | 27209 |
| 16 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1547 | 57870 |
| 17 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1474 | 21191 |
| 18 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1433 | 87457 |
| 19 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1389 | 107084 |
| 20 | [github/spec-kit](https://github.com/github/spec-kit) | +1379 | 71722 |
| 21 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1376 | 30590 |
| 22 | [antirez/ds4](https://github.com/antirez/ds4) | +1369 | 12936 |
| 23 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1308 | 70752 |
| 24 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1295 | 50520 |
| 25 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1288 | 107451 |
| 26 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1168 | 59327 |
| 27 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1165 | 56461 |
| 28 | [decolua/9router](https://github.com/decolua/9router) | +1137 | 16308 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1135 | 58847 |
| 30 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1123 | 59757 |
| 31 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1107 | 60940 |
| 32 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1054 | 68864 |
| 33 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1047 | 16593 |
| 34 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +998 | 24373 |
| 35 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +971 | 21351 |
| 36 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +963 | 29347 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +953 | 34148 |
| 38 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +893 | 33080 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +852 | 32342 |
| 40 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +845 | 16021 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +828 | 35250 |
| 42 | [floci-io/floci](https://github.com/floci-io/floci) | +739 | 13626 |
| 43 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +734 | 11257 |
| 44 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +699 | 24293 |
| 45 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +693 | 18009 |
| 46 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +690 | 49621 |
| 47 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +672 | 8050 |
| 48 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +663 | 36050 |
| 49 | [soxoj/maigret](https://github.com/soxoj/maigret) | +661 | 31266 |
| 50 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +651 | 10252 |
| 51 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +632 | 6732 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +623 | 20973 |
| 53 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +616 | 14980 |
| 54 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +616 | 61025 |
| 55 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +610 | 18085 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +603 | 25269 |
| 57 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +594 | 27251 |
| 58 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +583 | 42033 |
| 59 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +573 | 34412 |
| 60 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +558 | 4498 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +548 | 52868 |
| 62 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +542 | 4103 |
| 63 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +530 | 37025 |
| 64 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +508 | 25314 |
| 65 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +507 | 41331 |
| 66 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +500 | 12918 |
| 67 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +498 | 19112 |
| 68 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +497 | 19225 |
| 69 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +481 | 64709 |
| 70 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +479 | 40750 |
| 71 | [withcoral/coral](https://github.com/withcoral/coral) | +478 | 5147 |
| 72 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +460 | 14143 |
| 73 | [santifer/career-ops](https://github.com/santifer/career-ops) | +455 | 48694 |
| 74 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +454 | 7306 |
| 75 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +446 | 23514 |
| 76 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +442 | 8724 |
| 77 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +442 | 4914 |
| 78 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +441 | 12160 |
| 79 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +439 | 42825 |
| 80 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +437 | 6052 |
| 81 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +436 | 10611 |
| 82 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +432 | 10529 |
| 83 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +432 | 13604 |
| 84 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +431 | 13373 |
| 85 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +422 | 7744 |
| 86 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +420 | 29292 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +420 | 36062 |
| 88 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +412 | 56399 |
| 89 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +410 | 20972 |
| 90 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +410 | 32555 |
| 91 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +401 | 31931 |
| 92 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +399 | 4859 |
| 93 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +391 | 4442 |
| 94 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +390 | 22695 |
| 95 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +385 | 7478 |
| 96 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +383 | 7670 |
| 97 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +376 | 6133 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +374 | 28460 |
| 99 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +356 | 5101 |
| 100 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +348 | 15977 |
| 101 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +341 | 25825 |
| 102 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +339 | 14347 |
| 103 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +337 | 6993 |
| 104 | [jundot/omlx](https://github.com/jundot/omlx) | +336 | 15899 |
| 105 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +334 | 12554 |
| 106 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +326 | 4404 |
| 107 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +325 | 3659 |
| 108 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +325 | 8359 |
| 109 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +320 | 7244 |
| 110 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +315 | 12284 |
| 111 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +308 | 4812 |
| 112 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +298 | 34956 |
| 113 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2421 |
| 114 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +278 | 5493 |
| 115 | [MinishLab/semble](https://github.com/MinishLab/semble) | +275 | 4825 |
| 116 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +269 | 22802 |
| 117 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +268 | 3407 |
| 118 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +267 | 2704 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +265 | 15666 |
| 120 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +261 | 15870 |
| 121 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +261 | 9045 |
| 122 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +260 | 8129 |
| 123 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +250 | 5611 |
| 124 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +250 | 23672 |
| 125 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +249 | 4481 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +246 | 17149 |
| 127 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +245 | 45678 |
| 128 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +242 | 4198 |
| 129 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +241 | 26720 |
| 130 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +240 | 11394 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +240 | 36799 |
| 132 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +240 | 10176 |
| 133 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +238 | 39715 |
| 134 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +232 | 20265 |
| 135 | [openai/skills](https://github.com/openai/skills) | +222 | 21336 |
| 136 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +222 | 2773 |
| 137 | [browser-use/video-use](https://github.com/browser-use/video-use) | +221 | 9001 |
| 138 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +217 | 33816 |
| 139 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +216 | 2474 |
| 140 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +210 | 27517 |
| 141 | [z-lab/dflash](https://github.com/z-lab/dflash) | +210 | 4897 |
| 142 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +206 | 2912 |
| 143 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +206 | 2871 |
| 144 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +206 | 18036 |
| 145 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +206 | 6321 |
| 146 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +196 | 24478 |
| 147 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +195 | 3956 |
| 148 | [88lin/video_vip](https://github.com/88lin/video_vip) | +194 | 3474 |
| 149 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +191 | 2683 |
| 150 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +190 | 2380 |
| 151 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +188 | 1737 |
| 152 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +186 | 7068 |
| 153 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +186 | 33892 |
| 154 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +185 | 22694 |
| 155 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +183 | 34463 |
| 156 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +181 | 2556 |
| 157 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +174 | 5365 |
| 158 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +173 | 2267 |
| 159 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +173 | 0 |
| 160 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +172 | 1884 |
| 161 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +170 | 5035 |
| 162 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +169 | 21174 |
| 163 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +169 | 26507 |
| 164 | [browserbase/skills](https://github.com/browserbase/skills) | +168 | 3495 |
| 165 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +166 | 6450 |
| 166 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +163 | 0 |
| 167 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +162 | 13561 |
| 168 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +160 | 4723 |
| 169 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +159 | 23663 |
| 170 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +158 | 27831 |
| 171 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +157 | 7369 |
| 172 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1890 |
| 173 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +153 | 37564 |
| 174 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +151 | 43668 |
| 175 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +148 | 7605 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +146 | 15155 |
| 177 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +146 | 2358 |
| 178 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +143 | 10728 |
| 179 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +141 | 2890 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +140 | 28873 |
| 181 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +137 | 6394 |
| 182 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +136 | 6916 |
| 183 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +135 | 2042 |
| 184 | [playcanvas/engine](https://github.com/playcanvas/engine) | +131 | 15945 |
| 185 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +129 | 3976 |
| 186 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +129 | 6091 |
| 187 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2003 |
| 188 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +120 | 36103 |
| 189 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +115 | 4988 |
| 190 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +112 | 4210 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +111 | 27574 |
| 192 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +110 | 5372 |
| 193 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +108 | 1470 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +108 | 17660 |
| 195 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +107 | 8526 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +99 | 4157 |
| 197 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +98 | 3721 |
| 198 | [usebruno/bruno](https://github.com/usebruno/bruno) | +97 | 41086 |
| 199 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +96 | 1102 |
| 200 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +95 | 11993 |
| 201 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +94 | 39596 |
| 202 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 790 |
| 203 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +89 | 2192 |
| 204 | [eze-is/web-access](https://github.com/eze-is/web-access) | +88 | 7172 |
| 205 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +86 | 2176 |
| 206 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +82 | 10170 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +82 | 23511 |
| 208 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +81 | 15570 |
| 209 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +77 | 1529 |
| 210 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +75 | 975 |
| 211 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +74 | 15079 |
| 212 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +73 | 10777 |
| 213 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +73 | 3316 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +69 | 3400 |
| 215 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +69 | 1157 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +69 | 40265 |
| 217 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2470 |
| 218 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +65 | 4837 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +60 | 35473 |
| 220 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +60 | 37313 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +58 | 1938 |
| 222 | [sandeco/reversa](https://github.com/sandeco/reversa) | +57 | 1182 |
| 223 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +56 | 8134 |
| 224 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +55 | 901 |
| 225 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +52 | 4813 |
| 226 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 377 |
| 227 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +52 | 45263 |
| 228 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 229 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +50 | 11976 |
| 230 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 503 |
| 231 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +45 | 722 |
| 232 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +44 | 4209 |
| 233 | [robinebers/openusage](https://github.com/robinebers/openusage) | +44 | 2752 |
| 234 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 365 |
| 235 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +44 | 3501 |
| 236 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +43 | 8612 |
| 237 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +43 | 2560 |
| 238 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 346 |
| 239 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +42 | 7810 |
| 240 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +41 | 2152 |
| 241 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +41 | 539 |
| 242 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +40 | 445 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +37 | 13591 |
| 244 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +37 | 4823 |
| 245 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +37 | 9891 |
| 246 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1233 |
| 247 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +36 | 4331 |
| 248 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +35 | 672 |
| 249 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 290 |
| 250 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +33 | 4221 |
| 251 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +33 | 1722 |
| 252 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +33 | 1730 |
| 253 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +33 | 2407 |
| 254 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 277 |
| 255 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +32 | 2373 |
| 256 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +31 | 1095 |
| 257 | [openmemind/memind](https://github.com/openmemind/memind) | +31 | 895 |
| 258 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +30 | 780 |
| 259 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +29 | 1042 |
| 260 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +28 | 2244 |
| 261 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 350 |
| 262 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +28 | 3342 |
| 263 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +27 | 2065 |
| 264 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +26 | 7682 |
| 265 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +26 | 291 |
| 266 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +26 | 5257 |
| 267 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +26 | 1458 |
| 268 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +26 | 2347 |
| 269 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +25 | 1947 |
| 270 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +25 | 559 |
| 271 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +24 | 655 |
| 272 | [xu-xiang/everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh) | +24 | 943 |
| 273 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +24 | 353 |
| 274 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 394 |
| 275 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +21 | 235 |
| 276 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2978 |
| 277 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +19 | 795 |
| 278 | [is-a-dev/register](https://github.com/is-a-dev/register) | +18 | 10415 |
| 279 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 407 |
| 280 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2664 |
| 281 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +17 | 550 |
| 282 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +17 | 8931 |
| 283 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +17 | 825 |
| 284 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +16 | 1547 |
| 285 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3257 |
| 286 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1080 |
| 287 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +15 | 2482 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +13 | 2037 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +12 | 1590 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +12 | 530 |
| 291 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +11 | 2257 |
| 292 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 209 |
| 293 | [fengqiwby/Blockchain-assisted_TraceGuard](https://github.com/fengqiwby/Blockchain-assisted_TraceGuard) | +11 | 126 |
| 294 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 295 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +10 | 967 |
| 296 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +10 | 294 |
| 297 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +10 | 348 |
| 298 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +9 | 485 |
| 299 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 456 |
| 300 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 139 |
