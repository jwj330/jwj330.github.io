---
title: "2026-06-02 GitHub增长趋势报告"
description: "1.hermes-webui+50 2.codegraph+47 3.Understand-Anything+45 4.VoxCPM+33 5.headroom+29"
date: 2026-06-02T22:23:37+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-02 22:23:37

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
        'daily': {"categories": ["greensock/gsap-skills", "Imbad0202/academic-research-skills", "heygen-com/hyperframes", "run-llama/liteparse", "revfactory/harness", "tinyhumansai/openhuman", "rohitg00/ai-engineering-from-scratch", "safishamsi/graphify", "p-e-w/heretic", "hugohe3/ppt-master", "Yuan1z0825/nature-skills", "thcp/stemdeck", "Leonxlnx/taste-skill", "pbakaus/impeccable", "KKKKhazix/khazix-skills", "chopratejas/headroom", "OpenBMB/VoxCPM", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "nesquena/hermes-webui"], "data": [12, 12, 12, 12, 12, 14, 14, 15, 15, 16, 18, 21, 23, 23, 27, 29, 33, 45, 47, 50]},
        'weekly': {"categories": ["run-llama/liteparse", "greensock/gsap-skills", "hugohe3/ppt-master", "Yuan1z0825/nature-skills", "anthropics/knowledge-work-plugins", "can1357/oh-my-pi", "rohitg00/agentmemory", "Axorax/awesome-free-apps", "mukul975/Anthropic-Cybersecurity-Skills", "tinyhumansai/openhuman", "OpenBMB/VoxCPM", "safishamsi/graphify", "Imbad0202/academic-research-skills", "nesquena/hermes-webui", "microsoft/Webwright", "byoungd/English-level-up-tips", "rohitg00/ai-engineering-from-scratch", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "Lum1104/Understand-Anything"], "data": [67, 68, 71, 71, 72, 76, 77, 78, 79, 85, 87, 89, 100, 100, 115, 236, 263, 336, 356, 549]},
        'monthly': {"categories": ["Imbad0202/academic-research-skills", "msitarzewski/agency-agents", "D4Vinci/Scrapling", "rohitg00/ai-engineering-from-scratch", "VoltAgent/awesome-design-md", "CloakHQ/CloakBrowser", "addyosmani/agent-skills", "anthropics/financial-services", "tinyhumansai/openhuman", "ruvnet/ruflo", "TauricResearch/TradingAgents", "farion1231/cc-switch", "colbymchenry/codegraph", "affaan-m/ECC", "Lum1104/Understand-Anything", "obra/superpowers", "Hmbown/CodeWhale", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1580, 1601, 1608, 1620, 1651, 1847, 1898, 2004, 2247, 2415, 2506, 2509, 2661, 2677, 2974, 3171, 3244, 4155, 5043, 5574]}
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
| 1 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +50 | 12495 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +47 | 37886 |
| 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +45 | 50039 |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +33 | 25060 |
| 5 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +29 | 6185 |
| 6 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +27 | 13104 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +23 | 33455 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +23 | 31716 |
| 9 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +21 | 1441 |
| 10 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +18 | 15579 |
| 11 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +16 | 23762 |
| 12 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +15 | 23284 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +15 | 58381 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +14 | 27344 |
| 15 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +14 | 30438 |
| 16 | [revfactory/harness](https://github.com/revfactory/harness) | +12 | 5507 |
| 17 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +12 | 8926 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 23565 |
| 19 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +12 | 26201 |
| 20 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +12 | 7444 |
| 21 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +11 | 13580 |
| 22 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +11 | 9957 |
| 23 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +10 | 7093 |
| 24 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +10 | 19368 |
| 25 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +10 | 23389 |
| 26 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +9 | 36691 |
| 27 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +9 | 21063 |
| 28 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +9 | 6550 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +9 | 31844 |
| 30 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +8 | 5744 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +549 | 50039 |
| 2 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +356 | 31716 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +336 | 37886 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +263 | 27344 |
| 5 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +236 | 41523 |
| 6 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +115 | 4884 |
| 7 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +100 | 12495 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +100 | 26201 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +89 | 58381 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +87 | 25060 |
| 11 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +85 | 30438 |
| 12 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +79 | 13580 |
| 13 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +78 | 6423 |
| 14 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +77 | 20751 |
| 15 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +76 | 9957 |
| 16 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +72 | 18851 |
| 17 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +71 | 15579 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +71 | 23762 |
| 19 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +68 | 7444 |
| 20 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +67 | 8926 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +64 | 57932 |
| 22 | [russellromney/honker](https://github.com/russellromney/honker) | +64 | 2715 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +61 | 23565 |
| 24 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +60 | 6185 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +59 | 33455 |
| 26 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +55 | 23389 |
| 27 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +55 | 23284 |
| 28 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +52 | 9393 |
| 29 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +52 | 47796 |
| 30 | [multica-ai/multica](https://github.com/multica-ai/multica) | +51 | 34810 |
| 31 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +49 | 24586 |
| 32 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +48 | 29503 |
| 33 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +48 | 31844 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +47 | 64292 |
| 35 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +47 | 28166 |
| 36 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +47 | 5744 |
| 37 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +44 | 36691 |
| 38 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +44 | 4068 |
| 39 | [revfactory/harness](https://github.com/revfactory/harness) | +42 | 5507 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +42 | 41828 |
| 41 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +42 | 5172 |
| 42 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +41 | 13104 |
| 43 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +41 | 3808 |
| 44 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +41 | 2011 |
| 45 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +40 | 19368 |
| 46 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +40 | 55547 |
| 47 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +39 | 20776 |
| 48 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +38 | 14433 |
| 49 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +38 | 7141 |
| 50 | [freestylefly/CodexGuide](https://github.com/freestylefly/CodexGuide) | +38 | 1257 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +37 | 20617 |
| 52 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +37 | 11959 |
| 53 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +36 | 6550 |
| 54 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +35 | 20048 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +34 | 24927 |
| 56 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +34 | 26981 |
| 57 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +33 | 1441 |
| 58 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +33 | 867 |
| 59 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +33 | 12937 |
| 60 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +32 | 21063 |
| 61 | [decolua/9router](https://github.com/decolua/9router) | +31 | 15947 |
| 62 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +30 | 7550 |
| 63 | [tw93/Kami](https://github.com/tw93/Kami) | +30 | 6906 |
| 64 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +30 | 4083 |
| 65 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +29 | 3859 |
| 66 | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | +29 | 1074 |
| 67 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +29 | 22388 |
| 68 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +29 | 16047 |
| 69 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +29 | 15535 |
| 70 | [Chachamaru127/claude-code-harness](https://github.com/Chachamaru127/claude-code-harness) | +29 | 2532 |
| 71 | [antirez/ds4](https://github.com/antirez/ds4) | +28 | 12787 |
| 72 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +28 | 29165 |
| 73 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +28 | 42623 |
| 74 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +27 | 7093 |
| 75 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +27 | 41141 |
| 76 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +27 | 4116 |
| 77 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +27 | 7035 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +27 | 26853 |
| 79 | [tate233/todolist](https://github.com/tate233/todolist) | +27 | 1534 |
| 80 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +26 | 12783 |
| 81 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +26 | 16050 |
| 82 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +26 | 7505 |
| 83 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +25 | 9275 |
| 84 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +25 | 4226 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +25 | 35806 |
| 86 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +25 | 2651 |
| 87 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +24 | 39916 |
| 88 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +24 | 56081 |
| 89 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +24 | 34045 |
| 90 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +24 | 3251 |
| 91 | [Zafer-Liu/Data-Analysis-Agent](https://github.com/Zafer-Liu/Data-Analysis-Agent) | +24 | 1260 |
| 92 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +23 | 11146 |
| 93 | [Video-Reason/VBVR-EvalKit](https://github.com/Video-Reason/VBVR-EvalKit) | +23 | 296 |
| 94 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +22 | 28100 |
| 95 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +22 | 4229 |
| 96 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +22 | 30238 |
| 97 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +22 | 39495 |
| 98 | [santifer/career-ops](https://github.com/santifer/career-ops) | +22 | 48387 |
| 99 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +22 | 21058 |
| 100 | [openai/skills](https://github.com/openai/skills) | +22 | 21140 |
| 101 | [JJLibra/CC-Pan](https://github.com/JJLibra/CC-Pan) | +22 | 267 |
| 102 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +21 | 24024 |
| 103 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +21 | 31631 |
| 104 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +21 | 11236 |
| 105 | [ai-infra-curriculum/ai-infra-engineer-learning](https://github.com/ai-infra-curriculum/ai-infra-engineer-learning) | +21 | 839 |
| 106 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +20 | 9546 |
| 107 | [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | +18 | 1012 |
| 108 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +18 | 2700 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 7956 |
| 110 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +16 | 18872 |
| 111 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +16 | 2179 |
| 112 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +16 | 34318 |
| 113 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +15 | 55491 |
| 114 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +15 | 4465 |
| 115 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +15 | 3997 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +15 | 16944 |
| 117 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +14 | 6758 |
| 118 | [Xiangyue-Zhang/auto-deep-researcher-24x7](https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7) | +14 | 1134 |
| 119 | [browser-use/video-use](https://github.com/browser-use/video-use) | +14 | 8890 |
| 120 | [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | +14 | 2880 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5574 | 165807 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5043 | 115202 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4155 | 177261 |
| 4 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3244 | 36691 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +3171 | 60312 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2974 | 50039 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2677 | 51199 |
| 8 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2661 | 37886 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2509 | 89244 |
| 10 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2506 | 30590 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2415 | 57519 |
| 12 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2247 | 30438 |
| 13 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2004 | 29503 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1898 | 47796 |
| 15 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1847 | 23389 |
| 16 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1651 | 86820 |
| 17 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1620 | 27344 |
| 18 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1608 | 59090 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1601 | 106971 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1580 | 26202 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1560 | 106285 |
| 22 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1494 | 58381 |
| 23 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1469 | 20751 |
| 24 | [github/spec-kit](https://github.com/github/spec-kit) | +1407 | 71722 |
| 25 | [antirez/ds4](https://github.com/antirez/ds4) | +1364 | 12787 |
| 26 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1351 | 70201 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1340 | 57932 |
| 28 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1270 | 21063 |
| 29 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1242 | 67928 |
| 30 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1216 | 59001 |
| 31 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1198 | 55547 |
| 32 | [decolua/9router](https://github.com/decolua/9router) | +1160 | 15947 |
| 33 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1133 | 31222 |
| 34 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1092 | 15579 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1071 | 23762 |
| 36 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1065 | 31844 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1042 | 34148 |
| 38 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +979 | 29165 |
| 39 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +975 | 60881 |
| 40 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +972 | 31716 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +946 | 34810 |
| 42 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +845 | 15654 |
| 43 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +834 | 30678 |
| 44 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +772 | 55070 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +760 | 23565 |
| 46 | [floci-io/floci](https://github.com/floci-io/floci) | +743 | 13495 |
| 47 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +743 | 41141 |
| 48 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +731 | 11146 |
| 49 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +701 | 17929 |
| 50 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +685 | 17534 |
| 51 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +672 | 7986 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +669 | 20617 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +668 | 24927 |
| 54 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +663 | 35940 |
| 55 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +657 | 33455 |
| 56 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +649 | 14433 |
| 57 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +648 | 49621 |
| 58 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +645 | 25081 |
| 59 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +642 | 9393 |
| 60 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +637 | 12783 |
| 61 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +625 | 6550 |
| 62 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +620 | 41828 |
| 63 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +619 | 26981 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +619 | 52398 |
| 65 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +574 | 36672 |
| 66 | [santifer/career-ops](https://github.com/santifer/career-ops) | +562 | 48387 |
| 67 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +559 | 6836 |
| 68 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +558 | 4467 |
| 69 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +541 | 4082 |
| 70 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +540 | 56081 |
| 71 | [virattt/dexter](https://github.com/virattt/dexter) | +540 | 26795 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +527 | 39916 |
| 73 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +519 | 14241 |
| 74 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +515 | 64292 |
| 75 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +512 | 9546 |
| 76 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +507 | 19093 |
| 77 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +499 | 18851 |
| 78 | [withcoral/coral](https://github.com/withcoral/coral) | +484 | 5163 |
| 79 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +480 | 23339 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +476 | 31631 |
| 81 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +475 | 34045 |
| 82 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +472 | 7093 |
| 83 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +458 | 42623 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +454 | 35806 |
| 85 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +451 | 13104 |
| 86 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +451 | 15889 |
| 87 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +449 | 13581 |
| 88 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +442 | 22388 |
| 89 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +439 | 8577 |
| 90 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +438 | 29160 |
| 91 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +436 | 12495 |
| 92 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +432 | 5876 |
| 93 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +431 | 4624 |
| 94 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +430 | 20776 |
| 95 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +427 | 9957 |
| 96 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +425 | 7505 |
| 97 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +424 | 32466 |
| 98 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +420 | 7550 |
| 99 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +419 | 28166 |
| 100 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +409 | 25060 |
| 101 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +399 | 4809 |
| 102 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +390 | 12411 |
| 103 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +387 | 8320 |
| 104 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +386 | 6907 |
| 105 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +375 | 7141 |
| 106 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +367 | 5744 |
| 107 | [jundot/omlx](https://github.com/jundot/omlx) | +360 | 15686 |
| 108 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +356 | 34821 |
| 109 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +353 | 5037 |
| 110 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +344 | 3615 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +333 | 7146 |
| 112 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +332 | 5509 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +317 | 15535 |
| 114 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +311 | 4778 |
| 115 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +307 | 10154 |
| 116 | [MinishLab/semble](https://github.com/MinishLab/semble) | +306 | 4739 |
| 117 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +302 | 17908 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +293 | 15734 |
| 119 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +293 | 5394 |
| 120 | [browserbase/skills](https://github.com/browserbase/skills) | +292 | 3481 |
| 121 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +288 | 2412 |
| 122 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +285 | 39495 |
| 123 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +285 | 22713 |
| 124 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +283 | 20143 |
| 125 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +281 | 45498 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +280 | 16944 |
| 127 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +275 | 8997 |
| 128 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +267 | 2688 |
| 129 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +263 | 3179 |
| 130 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +261 | 8085 |
| 131 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +255 | 11236 |
| 132 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +255 | 36799 |
| 133 | [openai/skills](https://github.com/openai/skills) | +252 | 21140 |
| 134 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +250 | 6232 |
| 135 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +250 | 22698 |
| 136 | [browser-use/video-use](https://github.com/browser-use/video-use) | +248 | 8890 |
| 137 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +243 | 4392 |
| 138 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +241 | 4116 |
| 139 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +240 | 26640 |
| 140 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +237 | 33686 |
| 141 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 2026 |
| 142 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +235 | 24330 |
| 143 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +234 | 26980 |
| 144 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +231 | 2736 |
| 145 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +226 | 2651 |
| 146 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +223 | 5261 |
| 147 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +217 | 22567 |
| 148 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +213 | 2340 |
| 149 | [z-lab/dflash](https://github.com/z-lab/dflash) | +211 | 4822 |
| 150 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +210 | 27745 |
| 151 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +210 | 2628 |
| 152 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +205 | 2843 |
| 153 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +203 | 13526 |
| 154 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +203 | 0 |
| 155 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +199 | 33675 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +198 | 34318 |
| 157 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +197 | 26387 |
| 158 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +194 | 3919 |
| 159 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +193 | 7310 |
| 160 | [88lin/video_vip](https://github.com/88lin/video_vip) | +192 | 3370 |
| 161 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +191 | 2296 |
| 162 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +191 | 1702 |
| 163 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +189 | 6967 |
| 164 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +189 | 2367 |
| 165 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +184 | 20867 |
| 166 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +183 | 3781 |
| 167 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +181 | 2545 |
| 168 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +180 | 24498 |
| 169 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +176 | 4694 |
| 170 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +173 | 37564 |
| 171 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +172 | 1860 |
| 172 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +171 | 2179 |
| 173 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +171 | 4047 |
| 174 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +170 | 43539 |
| 175 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +170 | 6316 |
| 176 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +167 | 6423 |
| 177 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +165 | 28762 |
| 178 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +163 | 23284 |
| 179 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +162 | 4884 |
| 180 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +162 | 6387 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +162 | 7539 |
| 182 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +161 | 10645 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +159 | 15054 |
| 184 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1880 |
| 185 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +148 | 5957 |
| 186 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +145 | 2335 |
| 187 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +138 | 2651 |
| 188 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +134 | 5350 |
| 189 | [playcanvas/engine](https://github.com/playcanvas/engine) | +130 | 15930 |
| 190 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2011 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +124 | 27478 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +124 | 36103 |
| 193 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +123 | 4104 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +123 | 17578 |
| 195 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +120 | 4951 |
| 196 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +110 | 896 |
| 197 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +109 | 4083 |
| 198 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +108 | 8523 |
| 199 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +107 | 1440 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +103 | 3577 |
| 201 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +102 | 10155 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +102 | 39596 |
| 203 | [usebruno/bruno](https://github.com/usebruno/bruno) | +101 | 41086 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +98 | 23454 |
| 205 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +97 | 2066 |
| 206 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +97 | 11961 |
| 207 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +96 | 1076 |
| 208 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +94 | 2165 |
| 209 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 788 |
| 210 | [eze-is/web-access](https://github.com/eze-is/web-access) | +93 | 7051 |
| 211 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +93 | 15535 |
| 212 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +90 | 10726 |
| 213 | [sandeco/reversa](https://github.com/sandeco/reversa) | +79 | 1160 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +76 | 3364 |
| 215 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +76 | 15053 |
| 216 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +76 | 3283 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +74 | 40265 |
| 218 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +73 | 1441 |
| 219 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +72 | 839 |
| 220 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +71 | 1141 |
| 221 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +70 | 4764 |
| 222 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2469 |
| 223 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +66 | 2138 |
| 224 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +64 | 1887 |
| 225 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +63 | 35473 |
| 226 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +61 | 37313 |
| 227 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +59 | 8109 |
| 228 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +58 | 4760 |
| 229 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +53 | 48784 |
| 230 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 373 |
| 231 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +51 | 11964 |
| 232 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 295 |
| 233 | [robinebers/openusage](https://github.com/robinebers/openusage) | +51 | 2710 |
| 234 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +51 | 45263 |
| 235 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +50 | 8592 |
| 236 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +49 | 7618 |
| 237 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +48 | 4159 |
| 238 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +48 | 651 |
| 239 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +47 | 533 |
| 240 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 496 |
| 241 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +45 | 3431 |
| 242 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 364 |
| 243 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +44 | 669 |
| 244 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 345 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +42 | 13564 |
| 246 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +42 | 2504 |
| 247 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +41 | 4803 |
| 248 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +40 | 1219 |
| 249 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +40 | 434 |
| 250 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +39 | 4310 |
| 251 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +37 | 2346 |
| 252 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +36 | 1038 |
| 253 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +36 | 3322 |
| 254 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +35 | 1671 |
| 255 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +35 | 1690 |
| 256 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +35 | 1701 |
| 257 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +35 | 2386 |
| 258 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 291 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +34 | 895 |
| 260 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9851 |
| 261 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +33 | 4208 |
| 262 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +33 | 548 |
| 263 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +33 | 2172 |
| 264 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +32 | 1930 |
| 265 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 276 |
| 266 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +32 | 1085 |
| 267 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +30 | 2324 |
| 268 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +29 | 5243 |
| 269 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +29 | 2049 |
| 270 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +28 | 1433 |
| 271 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +28 | 846 |
| 272 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 341 |
| 273 | [xu-xiang/everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh) | +26 | 895 |
| 274 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +26 | 279 |
| 275 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +24 | 7569 |
| 276 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +24 | 1529 |
| 277 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +21 | 226 |
| 278 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +21 | 786 |
| 279 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2976 |
| 280 | [is-a-dev/register](https://github.com/is-a-dev/register) | +18 | 10402 |
| 281 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +18 | 225 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2663 |
| 283 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +17 | 2469 |
| 284 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +17 | 541 |
| 285 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +16 | 785 |
| 286 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +16 | 382 |
| 287 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3257 |
| 288 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1067 |
| 289 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +15 | 344 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +14 | 2022 |
| 291 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +14 | 1585 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +13 | 2250 |
| 293 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +13 | 525 |
| 294 | [fengqiwby/Blockchain-assisted_TraceGuard](https://github.com/fengqiwby/Blockchain-assisted_TraceGuard) | +12 | 126 |
| 295 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 205 |
| 296 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +11 | 960 |
| 297 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 298 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +10 | 448 |
| 299 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +10 | 293 |
| 300 | [Minecraft-Radiance/Radiance](https://github.com/Minecraft-Radiance/Radiance) | +10 | 1018 |
