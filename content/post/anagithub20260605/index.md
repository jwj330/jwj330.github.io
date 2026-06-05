---
title: "2026-06-05 GitHub增长趋势报告"
description: "1.odysseus+242 2.headroom+88 3.astrid+88 4.codegraph+65 5.open-notebook+42"
date: 2026-06-05T21:27:08+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-05 21:27:08

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
        'daily': {"categories": ["tashfeenahmed/freellmapi", "opensquilla/opensquilla", "rtk-ai/rtk", "Imbad0202/academic-research-skills", "openclaw/openclaw-windows-node", "fathah/hermes-desktop", "datawhalechina/Agent-Learning-Hub", "Yuan1z0825/nature-skills", "microsoft/VibeVoice", "rohitg00/ai-engineering-from-scratch", "Leonxlnx/taste-skill", "safishamsi/graphify", "heygen-com/hyperframes", "MadsLorentzen/ai-job-search", "mvanhorn/last30days-skill", "lfnovo/open-notebook", "colbymchenry/codegraph", "unicity-astrid/astrid", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [13, 14, 14, 14, 15, 16, 16, 16, 18, 19, 23, 24, 28, 29, 36, 42, 65, 88, 88, 242]},
        'weekly': {"categories": ["can1357/oh-my-pi", "MadsLorentzen/ai-job-search", "rtk-ai/rtk", "reconurge/flowsint", "Yuan1z0825/nature-skills", "Open-LLM-VTuber/Open-LLM-VTuber", "heygen-com/hyperframes", "safishamsi/graphify", "pbakaus/impeccable", "Imbad0202/academic-research-skills", "supermemoryai/supermemory", "rohitg00/ai-engineering-from-scratch", "OpenBMB/VoxCPM", "nesquena/hermes-webui", "Leonxlnx/taste-skill", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "unicity-astrid/astrid", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [61, 61, 63, 68, 68, 73, 77, 79, 80, 80, 83, 107, 119, 136, 136, 196, 266, 287, 371, 1526]},
        'monthly': {"categories": ["antirez/ds4", "github/spec-kit", "VoltAgent/awesome-design-md", "rohitg00/agentmemory", "pewdiepie-archdaemon/odysseus", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "addyosmani/agent-skills", "CloakHQ/CloakBrowser", "anthropics/financial-services", "tinyhumansai/openhuman", "farion1231/cc-switch", "affaan-m/ECC", "Hmbown/CodeWhale", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "obra/superpowers", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1369, 1389, 1400, 1481, 1528, 1549, 1627, 1726, 1853, 2022, 2264, 2293, 2520, 2736, 2796, 2816, 2827, 3576, 4147, 4449]}
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
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +242 | 55325 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +88 | 14410 |
| 3 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +88 | 7147 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +65 | 42219 |
| 5 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +42 | 25912 |
| 6 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +36 | 28160 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +29 | 2205 |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +28 | 24674 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +24 | 59735 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +23 | 33846 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +19 | 28798 |
| 12 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +18 | 48193 |
| 13 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +16 | 16989 |
| 14 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +16 | 2925 |
| 15 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +16 | 10545 |
| 16 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +15 | 1578 |
| 17 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +14 | 27668 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +14 | 59211 |
| 19 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +14 | 3246 |
| 20 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +13 | 7855 |
| 21 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +13 | 40959 |
| 22 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +13 | 6196 |
| 23 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +12 | 2330 |
| 24 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +12 | 10717 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +11 | 34767 |
| 26 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +11 | 32579 |
| 27 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +11 | 26400 |
| 28 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +10 | 14384 |
| 29 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 22865 |
| 30 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +10 | 507 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1526 | 55326 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +371 | 14410 |
| 3 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +287 | 7147 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +266 | 42219 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +196 | 52826 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +136 | 33846 |
| 7 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +136 | 13521 |
| 8 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +119 | 26400 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +107 | 28798 |
| 10 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +83 | 25680 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +80 | 27668 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +80 | 34767 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +79 | 59735 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +77 | 24674 |
| 15 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +73 | 9986 |
| 16 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +68 | 16989 |
| 17 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +68 | 5519 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +63 | 59211 |
| 19 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +61 | 2206 |
| 20 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +61 | 10717 |
| 21 | [revfactory/harness](https://github.com/revfactory/harness) | +57 | 6117 |
| 22 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +55 | 10830 |
| 23 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +55 | 10545 |
| 24 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +55 | 25912 |
| 25 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +55 | 23831 |
| 26 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +54 | 13759 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +51 | 40959 |
| 28 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +51 | 4292 |
| 29 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +50 | 8104 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +49 | 24630 |
| 31 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +47 | 14384 |
| 32 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +47 | 21387 |
| 33 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +45 | 24164 |
| 34 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +44 | 28160 |
| 35 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +44 | 28952 |
| 36 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +43 | 30900 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +41 | 56830 |
| 38 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +41 | 4574 |
| 39 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +38 | 25469 |
| 40 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +38 | 19918 |
| 41 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +37 | 64917 |
| 42 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +36 | 37197 |
| 43 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +36 | 15221 |
| 44 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +36 | 1558 |
| 45 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +36 | 9202 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +35 | 32579 |
| 47 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +35 | 7855 |
| 48 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +35 | 23772 |
| 49 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +35 | 947 |
| 50 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +34 | 21129 |
| 51 | [decolua/9router](https://github.com/decolua/9router) | +33 | 16466 |
| 52 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +33 | 30120 |
| 53 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +33 | 6784 |
| 54 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +32 | 9480 |
| 55 | [multica-ai/multica](https://github.com/multica-ai/multica) | +31 | 35458 |
| 56 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +31 | 3246 |
| 57 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +31 | 7846 |
| 58 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +29 | 2925 |
| 59 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +29 | 16350 |
| 60 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +28 | 22865 |
| 61 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +27 | 6196 |
| 62 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +27 | 27431 |
| 63 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +26 | 1578 |
| 64 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +26 | 48447 |
| 65 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +26 | 16395 |
| 66 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +26 | 42120 |
| 67 | [withastro/flue](https://github.com/withastro/flue) | +25 | 4490 |
| 68 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +25 | 8289 |
| 69 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +25 | 27460 |
| 70 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +24 | 48193 |
| 71 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +24 | 19275 |
| 72 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +24 | 56537 |
| 73 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +24 | 16208 |
| 74 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +24 | 21474 |
| 75 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +24 | 2364 |
| 76 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +24 | 1186 |
| 77 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +23 | 6238 |
| 78 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +23 | 55875 |
| 79 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +23 | 27360 |
| 80 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +23 | 21149 |
| 81 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +22 | 10534 |
| 82 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +21 | 28630 |
| 83 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +21 | 41469 |
| 84 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +21 | 21421 |
| 85 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +21 | 7391 |
| 86 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +21 | 36141 |
| 87 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +21 | 24336 |
| 88 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +20 | 7811 |
| 89 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +20 | 16377 |
| 90 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +20 | 4992 |
| 91 | [blader/humanizer](https://github.com/blader/humanizer) | +20 | 22518 |
| 92 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +20 | 12226 |
| 93 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +20 | 6974 |
| 94 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +19 | 2330 |
| 95 | [github/app](https://github.com/github/app) | +19 | 1391 |
| 96 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +19 | 15773 |
| 97 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +19 | 4027 |
| 98 | [MaxMiksa/Auto-Company](https://github.com/MaxMiksa/Auto-Company) | +18 | 1112 |
| 99 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +18 | 5481 |
| 100 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +18 | 6152 |
| 101 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +18 | 19048 |
| 102 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | +17 | 6743 |
| 103 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +17 | 5598 |
| 104 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +17 | 2993 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +17 | 39825 |
| 106 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +17 | 4542 |
| 107 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +16 | 3549 |
| 108 | [openai/skills](https://github.com/openai/skills) | +16 | 21423 |
| 109 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +16 | 21491 |
| 110 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +16 | 1984 |
| 111 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | +16 | 2197 |
| 112 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +15 | 11470 |
| 113 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 9110 |
| 114 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +15 | 7117 |
| 115 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +14 | 11321 |
| 116 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +14 | 23945 |
| 117 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +14 | 29434 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +14 | 17254 |
| 119 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +13 | 19328 |
| 120 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +13 | 6178 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4449 | 168667 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4147 | 118614 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3576 | 182967 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +2827 | 60312 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2816 | 42219 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2796 | 52826 |
| 7 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +2736 | 37197 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2520 | 51199 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2293 | 92602 |
| 10 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2264 | 30900 |
| 11 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2022 | 30120 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1853 | 24164 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1726 | 48447 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1627 | 28798 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1549 | 27668 |
| 16 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1528 | 55326 |
| 17 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1481 | 21387 |
| 18 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1400 | 87782 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +1389 | 71722 |
| 20 | [antirez/ds4](https://github.com/antirez/ds4) | +1369 | 13014 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1350 | 107394 |
| 22 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1307 | 71024 |
| 23 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1274 | 58039 |
| 24 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1183 | 107729 |
| 25 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1162 | 56830 |
| 26 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1144 | 30590 |
| 27 | [decolua/9router](https://github.com/decolua/9router) | +1130 | 16466 |
| 28 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1106 | 59735 |
| 29 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1102 | 60120 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1073 | 59211 |
| 31 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1038 | 61239 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1016 | 16989 |
| 33 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1012 | 69278 |
| 34 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +956 | 29434 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +956 | 24630 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +937 | 34148 |
| 37 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +888 | 21474 |
| 38 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +887 | 33846 |
| 39 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +838 | 16208 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +811 | 32579 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +805 | 35458 |
| 42 | [floci-io/floci](https://github.com/floci-io/floci) | +738 | 13666 |
| 43 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +735 | 11289 |
| 44 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +705 | 49621 |
| 45 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +698 | 18164 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +694 | 24674 |
| 47 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +672 | 8075 |
| 48 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +663 | 36111 |
| 49 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +659 | 10545 |
| 50 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +634 | 6784 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +611 | 21129 |
| 52 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +607 | 15221 |
| 53 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +598 | 27360 |
| 54 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +590 | 18195 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +580 | 25469 |
| 56 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +578 | 42120 |
| 57 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +562 | 34767 |
| 58 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +558 | 4511 |
| 59 | [soxoj/maigret](https://github.com/soxoj/maigret) | +556 | 31295 |
| 60 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +552 | 61082 |
| 61 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +543 | 4108 |
| 62 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +536 | 53109 |
| 63 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +515 | 37170 |
| 64 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +501 | 19275 |
| 65 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +499 | 19328 |
| 66 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +493 | 25391 |
| 67 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +478 | 40959 |
| 68 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +475 | 64917 |
| 69 | [withcoral/coral](https://github.com/withcoral/coral) | +475 | 5141 |
| 70 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +469 | 14384 |
| 71 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +467 | 41469 |
| 72 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +462 | 12965 |
| 73 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +448 | 4992 |
| 74 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +448 | 8842 |
| 75 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +448 | 7391 |
| 76 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +445 | 12226 |
| 77 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +440 | 6152 |
| 78 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +439 | 10717 |
| 79 | [santifer/career-ops](https://github.com/santifer/career-ops) | +437 | 48881 |
| 80 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +436 | 42920 |
| 81 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +436 | 23586 |
| 82 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +434 | 10830 |
| 83 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +432 | 13759 |
| 84 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +427 | 13521 |
| 85 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +426 | 7811 |
| 86 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +410 | 29376 |
| 87 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +409 | 21149 |
| 88 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +404 | 32629 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +403 | 36141 |
| 90 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +400 | 14410 |
| 91 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +399 | 4880 |
| 92 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +396 | 7855 |
| 93 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +395 | 56537 |
| 94 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +391 | 4461 |
| 95 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +386 | 22865 |
| 96 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +385 | 32065 |
| 97 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +378 | 6238 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +358 | 28630 |
| 99 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +357 | 5121 |
| 100 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +345 | 26400 |
| 101 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +329 | 4481 |
| 102 | [jundot/omlx](https://github.com/jundot/omlx) | +328 | 15999 |
| 103 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +323 | 3674 |
| 104 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +322 | 7298 |
| 105 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +316 | 16015 |
| 106 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +316 | 12609 |
| 107 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +312 | 8372 |
| 108 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +309 | 7034 |
| 109 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +307 | 4827 |
| 110 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +304 | 14386 |
| 111 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +292 | 35006 |
| 112 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2426 |
| 113 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +288 | 7147 |
| 114 | [MinishLab/semble](https://github.com/MinishLab/semble) | +274 | 4869 |
| 115 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +271 | 3549 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +271 | 5598 |
| 117 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +268 | 2711 |
| 118 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +260 | 8146 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +258 | 15773 |
| 120 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +255 | 15946 |
| 121 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +245 | 26749 |
| 122 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +245 | 23831 |
| 123 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +244 | 4226 |
| 124 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +244 | 22914 |
| 125 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +241 | 28160 |
| 126 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +240 | 45769 |
| 127 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +239 | 9062 |
| 128 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +239 | 11470 |
| 129 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +237 | 5678 |
| 130 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +234 | 17254 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +234 | 36799 |
| 132 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +233 | 39825 |
| 133 | [openai/skills](https://github.com/openai/skills) | +223 | 21423 |
| 134 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +222 | 20323 |
| 135 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +220 | 3246 |
| 136 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +217 | 2548 |
| 137 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +216 | 2785 |
| 138 | [z-lab/dflash](https://github.com/z-lab/dflash) | +213 | 4936 |
| 139 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +211 | 4515 |
| 140 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +209 | 2960 |
| 141 | [browser-use/video-use](https://github.com/browser-use/video-use) | +209 | 9110 |
| 142 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +203 | 33878 |
| 143 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +200 | 6369 |
| 144 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +198 | 18088 |
| 145 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +195 | 3970 |
| 146 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +194 | 24554 |
| 147 | [88lin/video_vip](https://github.com/88lin/video_vip) | +193 | 3489 |
| 148 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +190 | 2384 |
| 149 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +188 | 2699 |
| 150 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +188 | 22750 |
| 151 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +188 | 1750 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +185 | 33984 |
| 153 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +182 | 7117 |
| 154 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +182 | 2563 |
| 155 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +180 | 34530 |
| 156 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +173 | 2287 |
| 157 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +172 | 0 |
| 158 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +172 | 1890 |
| 159 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +169 | 5076 |
| 160 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +166 | 6464 |
| 161 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +165 | 21491 |
| 162 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +163 | 0 |
| 163 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +163 | 26561 |
| 164 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +160 | 23772 |
| 165 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +160 | 5412 |
| 166 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1890 |
| 167 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +155 | 7388 |
| 168 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +154 | 4737 |
| 169 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +149 | 2993 |
| 170 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +149 | 27898 |
| 171 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +148 | 43731 |
| 172 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +147 | 13575 |
| 173 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +147 | 2365 |
| 174 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +146 | 37564 |
| 175 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +145 | 7637 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +143 | 15212 |
| 177 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +140 | 19048 |
| 178 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +140 | 10758 |
| 179 | [browserbase/skills](https://github.com/browserbase/skills) | +139 | 3502 |
| 180 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +137 | 6974 |
| 181 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +135 | 28924 |
| 182 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +133 | 6178 |
| 183 | [playcanvas/engine](https://github.com/playcanvas/engine) | +130 | 15956 |
| 184 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +128 | 6454 |
| 185 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +127 | 4027 |
| 186 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2003 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +122 | 36103 |
| 188 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +114 | 5007 |
| 189 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +113 | 4234 |
| 190 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +108 | 1482 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +108 | 27613 |
| 192 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +107 | 8529 |
| 193 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +106 | 5390 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +104 | 17701 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +100 | 3794 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +100 | 4218 |
| 197 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +96 | 1109 |
| 198 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +95 | 11997 |
| 199 | [usebruno/bruno](https://github.com/usebruno/bruno) | +94 | 41086 |
| 200 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 791 |
| 201 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +92 | 39596 |
| 202 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +90 | 2210 |
| 203 | [eze-is/web-access](https://github.com/eze-is/web-access) | +87 | 7208 |
| 204 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +83 | 2242 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +80 | 23546 |
| 206 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +79 | 15598 |
| 207 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +76 | 1003 |
| 208 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +74 | 1558 |
| 209 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +74 | 10805 |
| 210 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +73 | 15088 |
| 211 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +68 | 1167 |
| 212 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +66 | 3413 |
| 213 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +66 | 10175 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +66 | 40265 |
| 215 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +66 | 2470 |
| 216 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +65 | 2043 |
| 217 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +65 | 4871 |
| 218 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +60 | 35473 |
| 219 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +59 | 37313 |
| 220 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +57 | 8149 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +55 | 1980 |
| 222 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +52 | 4842 |
| 223 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 378 |
| 224 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +52 | 45263 |
| 225 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 226 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +50 | 11988 |
| 227 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +49 | 758 |
| 228 | [sandeco/reversa](https://github.com/sandeco/reversa) | +48 | 1186 |
| 229 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +48 | 3555 |
| 230 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +45 | 4237 |
| 231 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +45 | 905 |
| 232 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +45 | 503 |
| 233 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 368 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +43 | 2761 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +43 | 2581 |
| 236 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 347 |
| 237 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +42 | 8623 |
| 238 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +41 | 542 |
| 239 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +40 | 457 |
| 240 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +40 | 8008 |
| 241 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +38 | 13600 |
| 242 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +37 | 9907 |
| 243 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1239 |
| 244 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +36 | 4830 |
| 245 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +36 | 3329 |
| 246 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +35 | 4337 |
| 247 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +34 | 1757 |
| 248 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 249 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +33 | 4229 |
| 250 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +33 | 1733 |
| 251 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +33 | 2161 |
| 252 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +33 | 2384 |
| 253 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 277 |
| 254 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +31 | 738 |
| 255 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +31 | 679 |
| 256 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +30 | 7726 |
| 257 | [openmemind/memind](https://github.com/openmemind/memind) | +30 | 896 |
| 258 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +30 | 2415 |
| 259 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +29 | 1094 |
| 260 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +28 | 2077 |
| 261 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 351 |
| 262 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +27 | 1042 |
| 263 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +27 | 2284 |
| 264 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +27 | 3357 |
| 265 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +26 | 1967 |
| 266 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +26 | 294 |
| 267 | [cv-cat/XHS_ALL_IN_ONE](https://github.com/cv-cat/XHS_ALL_IN_ONE) | +26 | 384 |
| 268 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +26 | 386 |
| 269 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +25 | 565 |
| 270 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +25 | 1467 |
| 271 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +25 | 2457 |
| 272 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +24 | 673 |
| 273 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +24 | 9209 |
| 274 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +24 | 2360 |
| 275 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +23 | 247 |
| 276 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 396 |
| 277 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +22 | 13498 |
| 278 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2979 |
| 279 | [is-a-dev/register](https://github.com/is-a-dev/register) | +18 | 10417 |
| 280 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +18 | 837 |
| 281 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 414 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2663 |
| 283 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +17 | 551 |
| 284 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +17 | 797 |
| 285 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3258 |
| 286 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1086 |
| 287 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +14 | 2490 |
| 288 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +14 | 1553 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +13 | 2043 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +12 | 532 |
| 291 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +11 | 499 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +11 | 2258 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +11 | 1595 |
| 294 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 211 |
| 295 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +11 | 297 |
| 296 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 297 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 458 |
| 298 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 142 |
| 299 | [liyupi/yu-ai-code-mother](https://github.com/liyupi/yu-ai-code-mother) | +9 | 1732 |
| 300 | [fengqiwby/Blockchain-assisted_TraceGuard](https://github.com/fengqiwby/Blockchain-assisted_TraceGuard) | +9 | 126 |
