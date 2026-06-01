---
title: "2026-06-01 GitHub增长趋势报告"
description: "1.codegraph+62 2.Understand-Anything+56 3.ai-engineering-from-scratch+45 4.VoxCPM+44 5.taste-skill+40"
date: 2026-06-01T22:33:41+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-01 22:33:41

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
        'daily': {"categories": ["can1357/oh-my-pi", "crynta/terax-ai", "mindfold-ai/Trellis", "Crosstalk-Solutions/project-nomad", "heygen-com/hyperframes", "CloakHQ/CloakBrowser", "0-AI-UG/cate", "run-llama/liteparse", "rohitg00/agentmemory", "Yuan1z0825/nature-skills", "greensock/gsap-skills", "revfactory/harness", "Imbad0202/academic-research-skills", "chopratejas/headroom", "nesquena/hermes-webui", "Leonxlnx/taste-skill", "OpenBMB/VoxCPM", "rohitg00/ai-engineering-from-scratch", "Lum1104/Understand-Anything", "colbymchenry/codegraph"], "data": [14, 15, 16, 16, 16, 17, 18, 18, 19, 19, 22, 23, 33, 33, 35, 40, 44, 45, 56, 62]},
        'weekly': {"categories": ["fathah/hermes-desktop", "hugohe3/ppt-master", "CloakHQ/CloakBrowser", "can1357/oh-my-pi", "rtk-ai/rtk", "greensock/gsap-skills", "rohitg00/agentmemory", "Yuan1z0825/nature-skills", "tinyhumansai/openhuman", "safishamsi/graphify", "mukul975/Anthropic-Cybersecurity-Skills", "Axorax/awesome-free-apps", "Imbad0202/academic-research-skills", "microsoft/Webwright", "anthropics/knowledge-work-plugins", "byoungd/English-level-up-tips", "rohitg00/ai-engineering-from-scratch", "Leonxlnx/taste-skill", "colbymchenry/codegraph", "Lum1104/Understand-Anything"], "data": [69, 71, 72, 77, 81, 87, 90, 100, 105, 113, 118, 126, 142, 143, 175, 240, 395, 413, 514, 789]},
        'monthly': {"categories": ["rohitg00/ai-engineering-from-scratch", "msitarzewski/agency-agents", "safishamsi/graphify", "VoltAgent/awesome-design-md", "D4Vinci/Scrapling", "CloakHQ/CloakBrowser", "addyosmani/agent-skills", "anthropics/financial-services", "tinyhumansai/openhuman", "farion1231/cc-switch", "ruvnet/ruflo", "colbymchenry/codegraph", "affaan-m/ECC", "TauricResearch/TradingAgents", "Lum1104/Understand-Anything", "obra/superpowers", "Hmbown/CodeWhale", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1614, 1653, 1676, 1706, 1762, 1840, 1935, 2001, 2236, 2590, 2604, 2620, 2720, 2786, 3044, 3309, 3330, 4338, 5477, 5834]}
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
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +62 | 36647 |
| 2 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +56 | 48688 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +45 | 26712 |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +44 | 24176 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +40 | 30910 |
| 6 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +35 | 11175 |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +33 | 4073 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +33 | 25689 |
| 9 | [revfactory/harness](https://github.com/revfactory/harness) | +23 | 5107 |
| 10 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +22 | 7137 |
| 11 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +19 | 14981 |
| 12 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +19 | 20481 |
| 13 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +18 | 8672 |
| 14 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +18 | 1054 |
| 15 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +17 | 23130 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +16 | 23162 |
| 17 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +16 | 27996 |
| 18 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +16 | 9125 |
| 19 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +15 | 6371 |
| 20 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +14 | 9432 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +13 | 57424 |
| 22 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +13 | 19075 |
| 23 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +13 | 3691 |
| 24 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +13 | 57918 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 23312 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +12 | 32632 |
| 27 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +11 | 20368 |
| 28 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +11 | 30284 |
| 29 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +11 | 1124 |
| 30 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +10 | 64078 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +789 | 48688 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +514 | 36647 |
| 3 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +413 | 30910 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +395 | 26712 |
| 5 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +240 | 41523 |
| 6 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +175 | 18644 |
| 7 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +143 | 4721 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +142 | 25689 |
| 9 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +126 | 6408 |
| 10 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +118 | 13245 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +113 | 57918 |
| 12 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +105 | 30284 |
| 13 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +100 | 14981 |
| 14 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +90 | 20481 |
| 15 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +87 | 7137 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +81 | 57424 |
| 17 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +77 | 9432 |
| 18 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +72 | 23130 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +71 | 23312 |
| 20 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +69 | 9119 |
| 21 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +65 | 31586 |
| 22 | [russellromney/honker](https://github.com/russellromney/honker) | +64 | 2688 |
| 23 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +63 | 11175 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +63 | 47624 |
| 25 | [multica-ai/multica](https://github.com/multica-ai/multica) | +63 | 34601 |
| 26 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +62 | 6978 |
| 27 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +61 | 23162 |
| 28 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +61 | 27953 |
| 29 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +60 | 23011 |
| 30 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +60 | 36449 |
| 31 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +60 | 2010 |
| 32 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +58 | 24176 |
| 33 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +58 | 29277 |
| 34 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +56 | 8672 |
| 35 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +55 | 41655 |
| 36 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +55 | 20685 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +52 | 55231 |
| 38 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +52 | 4064 |
| 39 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +51 | 29052 |
| 40 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +50 | 64078 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +50 | 32632 |
| 42 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +49 | 24952 |
| 43 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +48 | 3676 |
| 44 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +47 | 26850 |
| 45 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +45 | 14116 |
| 46 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +45 | 5565 |
| 47 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +44 | 20368 |
| 48 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +44 | 24740 |
| 49 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +43 | 5102 |
| 50 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +43 | 19913 |
| 51 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 20873 |
| 52 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +42 | 15408 |
| 53 | [Chachamaru127/claude-code-harness](https://github.com/Chachamaru127/claude-code-harness) | +41 | 2469 |
| 54 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +40 | 42516 |
| 55 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +39 | 19075 |
| 56 | [tate233/todolist](https://github.com/tate233/todolist) | +39 | 1534 |
| 57 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +38 | 4073 |
| 58 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +38 | 4071 |
| 59 | [decolua/9router](https://github.com/decolua/9router) | +38 | 15743 |
| 60 | [freestylefly/CodexGuide](https://github.com/freestylefly/CodexGuide) | +37 | 1196 |
| 61 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +37 | 15909 |
| 62 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +37 | 12869 |
| 63 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +35 | 3691 |
| 64 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +35 | 55904 |
| 65 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +35 | 12719 |
| 66 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +35 | 4150 |
| 67 | [antirez/ds4](https://github.com/antirez/ds4) | +35 | 12691 |
| 68 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +35 | 11103 |
| 69 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +34 | 35674 |
| 70 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +33 | 6371 |
| 71 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +33 | 22234 |
| 72 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +33 | 26698 |
| 73 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +33 | 11777 |
| 74 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +32 | 1054 |
| 75 | [yuanzhongqiao/deep-printfilm](https://github.com/yuanzhongqiao/deep-printfilm) | +32 | 1651 |
| 76 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +32 | 9371 |
| 77 | [revfactory/harness](https://github.com/revfactory/harness) | +31 | 5107 |
| 78 | [tw93/Kami](https://github.com/tw93/Kami) | +31 | 6755 |
| 79 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +31 | 15525 |
| 80 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +30 | 20937 |
| 81 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +30 | 2522 |
| 82 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +30 | 6902 |
| 83 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +30 | 7404 |
| 84 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +30 | 2176 |
| 85 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +29 | 7458 |
| 86 | [blader/humanizer](https://github.com/blader/humanizer) | +29 | 21970 |
| 87 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +29 | 41043 |
| 88 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +29 | 35501 |
| 89 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +29 | 2006 |
| 90 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +28 | 33937 |
| 91 | [openai/skills](https://github.com/openai/skills) | +28 | 21058 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +28 | 31500 |
| 93 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +27 | 15934 |
| 94 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +27 | 30138 |
| 95 | [santifer/career-ops](https://github.com/santifer/career-ops) | +26 | 48201 |
| 96 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +25 | 3929 |
| 97 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +25 | 11176 |
| 98 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +24 | 39775 |
| 99 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +24 | 23262 |
| 100 | [Video-Reason/VBVR-EvalKit](https://github.com/Video-Reason/VBVR-EvalKit) | +24 | 296 |
| 101 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +24 | 2640 |
| 102 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +23 | 39396 |
| 103 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +23 | 13383 |
| 104 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +22 | 9125 |
| 105 | [Zafer-Liu/Data-Analysis-Agent](https://github.com/Zafer-Liu/Data-Analysis-Agent) | +22 | 1248 |
| 106 | [JJLibra/CC-Pan](https://github.com/JJLibra/CC-Pan) | +22 | 267 |
| 107 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +21 | 27996 |
| 108 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +21 | 9332 |
| 109 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +20 | 20778 |
| 110 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +20 | 34258 |
| 111 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +20 | 26933 |
| 112 | [ai-infra-curriculum/ai-infra-engineer-learning](https://github.com/ai-infra-curriculum/ai-infra-engineer-learning) | +19 | 817 |
| 113 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +18 | 6660 |
| 114 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +18 | 2682 |
| 115 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +18 | 12405 |
| 116 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +18 | 2128 |
| 117 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +18 | 13072 |
| 118 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +18 | 3725 |
| 119 | [XiaoLuoLYG/GOD](https://github.com/XiaoLuoLYG/GOD) | +18 | 555 |
| 120 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +17 | 19045 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5834 | 164710 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5477 | 114134 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4338 | 175922 |
| 4 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3330 | 36449 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +3309 | 60312 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +3044 | 48688 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2786 | 30590 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2720 | 51199 |
| 9 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2620 | 36647 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2604 | 57271 |
| 11 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2590 | 87872 |
| 12 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2236 | 30284 |
| 13 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2001 | 29277 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1935 | 47624 |
| 15 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1840 | 23130 |
| 16 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1762 | 57940 |
| 17 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1706 | 86465 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1676 | 57918 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1653 | 106683 |
| 20 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1614 | 26712 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1589 | 105683 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1581 | 25689 |
| 23 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1464 | 20481 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +1448 | 74774 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1431 | 57424 |
| 26 | [github/spec-kit](https://github.com/github/spec-kit) | +1418 | 71722 |
| 27 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1366 | 69866 |
| 28 | [antirez/ds4](https://github.com/antirez/ds4) | +1359 | 12691 |
| 29 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1312 | 20873 |
| 30 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1294 | 67421 |
| 31 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1283 | 31184 |
| 32 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1256 | 58605 |
| 33 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1256 | 85286 |
| 34 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1244 | 60811 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1204 | 55231 |
| 36 | [decolua/9router](https://github.com/decolua/9router) | +1171 | 15743 |
| 37 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1142 | 31586 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1128 | 23312 |
| 39 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1103 | 14981 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1065 | 34148 |
| 41 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +988 | 29052 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +987 | 34601 |
| 43 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +975 | 30910 |
| 44 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +887 | 30678 |
| 45 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +865 | 55070 |
| 46 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +852 | 15525 |
| 47 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +797 | 41043 |
| 48 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +791 | 23162 |
| 49 | [floci-io/floci](https://github.com/floci-io/floci) | +740 | 13398 |
| 50 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +740 | 17799 |
| 51 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +730 | 11103 |
| 52 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +723 | 24952 |
| 53 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +719 | 68659 |
| 54 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +696 | 12719 |
| 55 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +687 | 17331 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +686 | 24740 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +681 | 20368 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +671 | 32632 |
| 59 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +670 | 7954 |
| 60 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +666 | 35866 |
| 61 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +662 | 14116 |
| 62 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +646 | 9119 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +646 | 52160 |
| 64 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +630 | 6815 |
| 65 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +625 | 41655 |
| 66 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +624 | 49621 |
| 67 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +623 | 26850 |
| 68 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +616 | 6371 |
| 69 | [santifer/career-ops](https://github.com/santifer/career-ops) | +602 | 48201 |
| 70 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +599 | 5102 |
| 71 | [virattt/dexter](https://github.com/virattt/dexter) | +592 | 26753 |
| 72 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +590 | 14174 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +586 | 36482 |
| 74 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +580 | 55904 |
| 75 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +569 | 9332 |
| 76 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +558 | 4455 |
| 77 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +542 | 4068 |
| 78 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +541 | 39775 |
| 79 | [openai/symphony](https://github.com/openai/symphony) | +521 | 24927 |
| 80 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +519 | 33937 |
| 81 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +517 | 64078 |
| 82 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +511 | 19045 |
| 83 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +501 | 18644 |
| 84 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +493 | 15838 |
| 85 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +492 | 23262 |
| 86 | [withcoral/coral](https://github.com/withcoral/coral) | +490 | 5159 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +488 | 31500 |
| 88 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +479 | 6894 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +477 | 35674 |
| 90 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +475 | 42516 |
| 91 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +468 | 24176 |
| 92 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +458 | 22234 |
| 93 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +454 | 6857 |
| 94 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +451 | 12405 |
| 95 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +444 | 29072 |
| 96 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +440 | 20685 |
| 97 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +439 | 13245 |
| 98 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +436 | 8516 |
| 99 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +436 | 27953 |
| 100 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +430 | 4529 |
| 101 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +429 | 5756 |
| 102 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +426 | 32415 |
| 103 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +422 | 9432 |
| 104 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +422 | 12388 |
| 105 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +413 | 7458 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +403 | 11175 |
| 107 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +390 | 8273 |
| 108 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +376 | 6978 |
| 109 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +370 | 34773 |
| 110 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +366 | 3602 |
| 111 | [jundot/omlx](https://github.com/jundot/omlx) | +365 | 15618 |
| 112 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +359 | 5565 |
| 113 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +353 | 5010 |
| 114 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +346 | 10140 |
| 115 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +345 | 17841 |
| 116 | [browserbase/skills](https://github.com/browserbase/skills) | +343 | 3475 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +339 | 15408 |
| 118 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +338 | 7090 |
| 119 | [MinishLab/semble](https://github.com/MinishLab/semble) | +328 | 4684 |
| 120 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +327 | 5432 |
| 121 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +311 | 4757 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +306 | 15672 |
| 123 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +301 | 20078 |
| 124 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +300 | 5356 |
| 125 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +298 | 45403 |
| 126 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +291 | 39396 |
| 127 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +289 | 8965 |
| 128 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +289 | 16836 |
| 129 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +287 | 2407 |
| 130 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +286 | 22673 |
| 131 | [browser-use/video-use](https://github.com/browser-use/video-use) | +277 | 8802 |
| 132 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +277 | 6135 |
| 133 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +267 | 2684 |
| 134 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +263 | 3068 |
| 135 | [openai/skills](https://github.com/openai/skills) | +262 | 21058 |
| 136 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +261 | 11176 |
| 137 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +261 | 36799 |
| 138 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +260 | 8048 |
| 139 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +251 | 33617 |
| 140 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +248 | 24241 |
| 141 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +245 | 26933 |
| 142 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +245 | 22012 |
| 143 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +244 | 4345 |
| 144 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +241 | 22495 |
| 145 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +241 | 26599 |
| 146 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +241 | 5207 |
| 147 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +237 | 4071 |
| 148 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 2013 |
| 149 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +234 | 2676 |
| 150 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +229 | 2640 |
| 151 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +221 | 4394 |
| 152 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +219 | 13506 |
| 153 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +219 | 0 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +216 | 27687 |
| 155 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +212 | 34258 |
| 156 | [z-lab/dflash](https://github.com/z-lab/dflash) | +212 | 4764 |
| 157 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +211 | 2273 |
| 158 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +211 | 24476 |
| 159 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +209 | 2609 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +207 | 26347 |
| 161 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +204 | 2798 |
| 162 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +202 | 7275 |
| 163 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +198 | 33579 |
| 164 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +197 | 6900 |
| 165 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +195 | 3775 |
| 166 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +194 | 3899 |
| 167 | [88lin/video_vip](https://github.com/88lin/video_vip) | +194 | 3361 |
| 168 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +193 | 1674 |
| 169 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +190 | 2212 |
| 170 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +189 | 2354 |
| 171 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +188 | 4676 |
| 172 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +187 | 20778 |
| 173 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +185 | 43482 |
| 174 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +182 | 6276 |
| 175 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +181 | 2540 |
| 176 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +180 | 4037 |
| 177 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +175 | 37564 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +171 | 28711 |
| 179 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +169 | 2128 |
| 180 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6408 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +169 | 7500 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +168 | 14992 |
| 183 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +163 | 10581 |
| 184 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +161 | 4721 |
| 185 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +161 | 6362 |
| 186 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +158 | 23011 |
| 187 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1872 |
| 188 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +155 | 5885 |
| 189 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +143 | 2327 |
| 190 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +134 | 5322 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +132 | 27425 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +131 | 4057 |
| 193 | [playcanvas/engine](https://github.com/playcanvas/engine) | +130 | 15922 |
| 194 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +128 | 36103 |
| 195 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +127 | 17540 |
| 196 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2010 |
| 197 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +125 | 4933 |
| 198 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +110 | 4064 |
| 199 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +110 | 894 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +109 | 8527 |
| 201 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +107 | 1414 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +107 | 39596 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +105 | 10147 |
| 204 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +103 | 3519 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +103 | 41086 |
| 206 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +100 | 2008 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +100 | 23419 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +97 | 10703 |
| 209 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +96 | 1057 |
| 210 | [sandeco/reversa](https://github.com/sandeco/reversa) | +96 | 1152 |
| 211 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +96 | 11950 |
| 212 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +94 | 2145 |
| 213 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +94 | 15511 |
| 214 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 781 |
| 215 | [eze-is/web-access](https://github.com/eze-is/web-access) | +93 | 7011 |
| 216 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +83 | 3337 |
| 217 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +81 | 2129 |
| 218 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +78 | 15039 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +76 | 40265 |
| 220 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +76 | 3274 |
| 221 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +75 | 1127 |
| 222 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +71 | 4725 |
| 223 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +70 | 819 |
| 224 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +68 | 1866 |
| 225 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2468 |
| 226 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +65 | 35473 |
| 227 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +63 | 4705 |
| 228 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +62 | 37313 |
| 229 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +60 | 8098 |
| 230 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +58 | 48784 |
| 231 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +55 | 45263 |
| 232 | [robinebers/openusage](https://github.com/robinebers/openusage) | +54 | 2699 |
| 233 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +53 | 531 |
| 234 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 367 |
| 235 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +51 | 11942 |
| 236 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 295 |
| 237 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +51 | 1125 |
| 238 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +51 | 7611 |
| 239 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +50 | 8574 |
| 240 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +49 | 33000 |
| 241 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +48 | 4130 |
| 242 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +48 | 640 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +46 | 13553 |
| 244 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 495 |
| 245 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 361 |
| 246 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +44 | 3415 |
| 247 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +43 | 306 |
| 248 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +43 | 626 |
| 249 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 343 |
| 250 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +43 | 3312 |
| 251 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +42 | 4791 |
| 252 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +41 | 2476 |
| 253 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +40 | 431 |
| 254 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +39 | 4297 |
| 255 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +39 | 545 |
| 256 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +39 | 1700 |
| 257 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +38 | 1177 |
| 258 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +37 | 2329 |
| 259 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +36 | 1037 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +36 | 2373 |
| 261 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +35 | 1652 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +35 | 895 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +34 | 1668 |
| 264 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 284 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9832 |
| 266 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +33 | 4198 |
| 267 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +33 | 1078 |
| 268 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +32 | 1922 |
| 269 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 277 |
| 270 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +32 | 2042 |
| 271 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +31 | 2311 |
| 272 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +31 | 1517 |
| 273 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +29 | 5234 |
| 274 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +28 | 1418 |
| 275 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +28 | 13476 |
| 276 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 334 |
| 277 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2247 |
| 278 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +26 | 275 |
| 279 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +23 | 755 |
| 280 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +23 | 539 |
| 281 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +22 | 786 |
| 282 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +21 | 372 |
| 283 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +21 | 213 |
| 284 | [is-a-dev/register](https://github.com/is-a-dev/register) | +19 | 10393 |
| 285 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2978 |
| 286 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +19 | 778 |
| 287 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +18 | 2463 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2664 |
| 289 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +17 | 343 |
| 290 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +16 | 194 |
| 291 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +16 | 373 |
| 292 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3258 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +16 | 1583 |
| 294 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1058 |
| 295 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +14 | 2012 |
| 296 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +14 | 519 |
| 297 | [fengqiwby/Blockchain-assisted_TraceGuard](https://github.com/fengqiwby/Blockchain-assisted_TraceGuard) | +12 | 126 |
| 298 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 197 |
| 299 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +11 | 958 |
| 300 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
