---
title: "2026-06-07 GitHub增长趋势报告"
description: "1.odysseus+237 2.taste-skill+115 3.headroom+83 4.VoxCPM+65 5.graphify+63"
date: 2026-06-07T21:15:13+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-07 21:15:13

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
        'daily': {"categories": ["RyanCodrai/turbovec", "withastro/flue", "next-1688/1688-shopkeeper", "pbakaus/impeccable", "Imbad0202/academic-research-skills", "Yuan1z0825/nature-skills", "MadsLorentzen/ai-job-search", "mvanhorn/last30days-skill", "helloianneo/ian-xiaohei-illustrations", "unicity-astrid/astrid", "CopilotKit/CopilotKit", "rohitg00/ai-engineering-from-scratch", "Panniantong/Agent-Reach", "Lum1104/Understand-Anything", "lfnovo/open-notebook", "safishamsi/graphify", "OpenBMB/VoxCPM", "chopratejas/headroom", "Leonxlnx/taste-skill", "pewdiepie-archdaemon/odysseus"], "data": [24, 26, 29, 29, 30, 30, 31, 34, 40, 41, 44, 46, 51, 53, 61, 63, 65, 83, 115, 237]},
        'weekly': {"categories": ["Yuan1z0825/nature-skills", "santifer/career-ops", "CopilotKit/CopilotKit", "pbakaus/impeccable", "heygen-com/hyperframes", "Imbad0202/academic-research-skills", "Panniantong/Agent-Reach", "nesquena/hermes-webui", "lfnovo/open-notebook", "RyanCodrai/turbovec", "rohitg00/ai-engineering-from-scratch", "mvanhorn/last30days-skill", "alibaba/open-code-review", "OpenBMB/VoxCPM", "Lum1104/Understand-Anything", "unicity-astrid/astrid", "Leonxlnx/taste-skill", "colbymchenry/codegraph", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [119, 122, 128, 132, 138, 151, 164, 170, 172, 185, 196, 200, 228, 248, 338, 363, 369, 409, 580, 2073]},
        'monthly': {"categories": ["VoltAgent/awesome-design-md", "antirez/ds4", "github/spec-kit", "rohitg00/agentmemory", "addyosmani/agent-skills", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "Hmbown/CodeWhale", "CloakHQ/CloakBrowser", "anthropics/financial-services", "pewdiepie-archdaemon/odysseus", "farion1231/cc-switch", "tinyhumansai/openhuman", "affaan-m/ECC", "obra/superpowers", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1363, 1386, 1430, 1502, 1543, 1597, 1710, 1849, 1878, 1947, 2073, 2253, 2275, 2551, 2777, 2869, 2950, 3587, 3972, 4168]}
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
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +237 | 61372 |
| 2 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +115 | 36436 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +83 | 16822 |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +65 | 27489 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +63 | 61704 |
| 6 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +61 | 27143 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +53 | 54311 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +51 | 23114 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +46 | 29835 |
| 10 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +44 | 33632 |
| 11 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +41 | 8043 |
| 12 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +40 | 3348 |
| 13 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +34 | 30590 |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +31 | 2842 |
| 15 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 17572 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +30 | 28507 |
| 17 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +29 | 35512 |
| 18 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +29 | 2621 |
| 19 | [withastro/flue](https://github.com/withastro/flue) | +26 | 4771 |
| 20 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +24 | 6970 |
| 21 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +23 | 8404 |
| 22 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 25940 |
| 23 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +22 | 1283 |
| 24 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +22 | 1482 |
| 25 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +22 | 24666 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +21 | 29645 |
| 27 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +21 | 8238 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +20 | 12246 |
| 29 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +20 | 9369 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +19 | 48921 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2073 | 61375 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +580 | 16822 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +409 | 43695 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +369 | 36436 |
| 5 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +363 | 8043 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +338 | 54311 |
| 7 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +248 | 27489 |
| 8 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +228 | 4630 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +200 | 30590 |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +196 | 29835 |
| 11 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +185 | 6970 |
| 12 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +172 | 27143 |
| 13 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +170 | 13818 |
| 14 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +164 | 23114 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +151 | 28507 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +138 | 25340 |
| 17 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +132 | 35512 |
| 18 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +128 | 33632 |
| 19 | [santifer/career-ops](https://github.com/santifer/career-ops) | +122 | 49797 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +119 | 17572 |
| 21 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +118 | 2842 |
| 22 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +109 | 10333 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +106 | 59742 |
| 24 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +105 | 3348 |
| 25 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +103 | 25999 |
| 26 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +98 | 5860 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +96 | 11074 |
| 28 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +94 | 14757 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +91 | 57275 |
| 30 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +90 | 11116 |
| 31 | [roboflow/supervision](https://github.com/roboflow/supervision) | +90 | 36553 |
| 32 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +89 | 29645 |
| 33 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +89 | 10990 |
| 34 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +88 | 2621 |
| 35 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +87 | 48921 |
| 36 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +87 | 8404 |
| 37 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +86 | 48653 |
| 38 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +84 | 25940 |
| 39 | [revfactory/harness](https://github.com/revfactory/harness) | +84 | 6405 |
| 40 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +80 | 24666 |
| 41 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +79 | 8484 |
| 42 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +79 | 20345 |
| 43 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +79 | 25011 |
| 44 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +77 | 1482 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +76 | 41154 |
| 46 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +74 | 21441 |
| 47 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +74 | 24059 |
| 48 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +73 | 25866 |
| 49 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +72 | 21723 |
| 50 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +69 | 13973 |
| 51 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +68 | 30378 |
| 52 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +67 | 4886 |
| 53 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +65 | 18700 |
| 54 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +63 | 3450 |
| 55 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +61 | 9474 |
| 56 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +59 | 16483 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +59 | 15557 |
| 58 | [decolua/9router](https://github.com/decolua/9router) | +58 | 16760 |
| 59 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +57 | 31064 |
| 60 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +56 | 37438 |
| 61 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +55 | 32993 |
| 62 | [withastro/flue](https://github.com/withastro/flue) | +54 | 4771 |
| 63 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +54 | 16968 |
| 64 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +52 | 31098 |
| 65 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +50 | 27601 |
| 66 | [multica-ai/multica](https://github.com/multica-ai/multica) | +49 | 35687 |
| 67 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +48 | 16574 |
| 68 | [openai/plugins](https://github.com/openai/plugins) | +47 | 1992 |
| 69 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +47 | 3119 |
| 70 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +47 | 23138 |
| 71 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +45 | 6546 |
| 72 | [blader/humanizer](https://github.com/blader/humanizer) | +45 | 22784 |
| 73 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +44 | 28915 |
| 74 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +44 | 19523 |
| 75 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +44 | 56796 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +43 | 32329 |
| 77 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +43 | 12797 |
| 78 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +43 | 13234 |
| 79 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +43 | 8414 |
| 80 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 21651 |
| 81 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +42 | 1283 |
| 82 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +42 | 7966 |
| 83 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +42 | 6395 |
| 84 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +42 | 23912 |
| 85 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +41 | 15178 |
| 86 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +41 | 24553 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +40 | 36397 |
| 88 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +40 | 1832 |
| 89 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +40 | 2453 |
| 90 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +40 | 42259 |
| 91 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +39 | 3742 |
| 92 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +39 | 1732 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +39 | 10659 |
| 94 | [FufuLauncher/FufuLauncher](https://github.com/FufuLauncher/FufuLauncher) | +38 | 1493 |
| 95 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +38 | 9012 |
| 96 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +37 | 1674 |
| 97 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +37 | 12246 |
| 98 | [Makisuo/maple](https://github.com/Makisuo/maple) | +37 | 1077 |
| 99 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +37 | 15949 |
| 100 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +36 | 21371 |
| 101 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +36 | 21607 |
| 102 | [openai/skills](https://github.com/openai/skills) | +36 | 21601 |
| 103 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +36 | 23068 |
| 104 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +35 | 20776 |
| 105 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +35 | 16524 |
| 106 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +34 | 8238 |
| 107 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +34 | 7075 |
| 108 | [browser-act/skills](https://github.com/browser-act/skills) | +32 | 2118 |
| 109 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +32 | 5695 |
| 110 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +31 | 3188 |
| 111 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +31 | 27488 |
| 112 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +30 | 29576 |
| 113 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +30 | 39980 |
| 114 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +30 | 2447 |
| 115 | [browser-use/video-use](https://github.com/browser-use/video-use) | +30 | 9220 |
| 116 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +29 | 652 |
| 117 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +28 | 24113 |
| 118 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +27 | 16301 |
| 119 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +27 | 11588 |
| 120 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +26 | 35302 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4168 | 170308 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3972 | 120312 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3587 | 185804 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2950 | 43695 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2869 | 54311 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2777 | 60312 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2551 | 51199 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2275 | 31064 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2253 | 94124 |
| 10 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2073 | 61376 |
| 11 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1947 | 30378 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1878 | 24666 |
| 13 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +1849 | 37438 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1710 | 29835 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1597 | 28507 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1543 | 48921 |
| 17 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1502 | 21723 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +1430 | 71722 |
| 19 | [antirez/ds4](https://github.com/antirez/ds4) | +1386 | 13160 |
| 20 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1363 | 88211 |
| 21 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1351 | 71634 |
| 22 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1309 | 107993 |
| 23 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1181 | 61705 |
| 24 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1143 | 57275 |
| 25 | [decolua/9router](https://github.com/decolua/9router) | +1136 | 16760 |
| 26 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1111 | 108110 |
| 27 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1089 | 36437 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1082 | 60615 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1062 | 30590 |
| 30 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1051 | 58373 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1018 | 59742 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +974 | 17572 |
| 33 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +961 | 29576 |
| 34 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +953 | 69745 |
| 35 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +942 | 61898 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +936 | 34148 |
| 37 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +901 | 25011 |
| 38 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +857 | 16483 |
| 39 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +792 | 49621 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +773 | 32993 |
| 41 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +757 | 21651 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +745 | 35687 |
| 43 | [floci-io/floci](https://github.com/floci-io/floci) | +743 | 13755 |
| 44 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +738 | 11349 |
| 45 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +738 | 18700 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +693 | 25340 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +684 | 10990 |
| 48 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +676 | 8116 |
| 49 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +670 | 36199 |
| 50 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +640 | 6846 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +618 | 21441 |
| 52 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +606 | 16822 |
| 53 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +599 | 27488 |
| 54 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +588 | 15557 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +574 | 25940 |
| 56 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +573 | 35511 |
| 57 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +569 | 18410 |
| 58 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +561 | 42259 |
| 59 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +560 | 4536 |
| 60 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +544 | 4117 |
| 61 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +525 | 53332 |
| 62 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +515 | 19523 |
| 63 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +513 | 25866 |
| 64 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +510 | 14757 |
| 65 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +506 | 19389 |
| 66 | [santifer/career-ops](https://github.com/santifer/career-ops) | +500 | 49797 |
| 67 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +493 | 37487 |
| 68 | [withcoral/coral](https://github.com/withcoral/coral) | +476 | 5138 |
| 69 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +474 | 41154 |
| 70 | [soxoj/maigret](https://github.com/soxoj/maigret) | +469 | 31332 |
| 71 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +464 | 11074 |
| 72 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +460 | 27489 |
| 73 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +460 | 5092 |
| 74 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +457 | 61193 |
| 75 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +454 | 9012 |
| 76 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +447 | 7516 |
| 77 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +447 | 12317 |
| 78 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +446 | 6261 |
| 79 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +444 | 13818 |
| 80 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +439 | 8484 |
| 81 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +437 | 13234 |
| 82 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +431 | 7886 |
| 83 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +428 | 13973 |
| 84 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +427 | 11116 |
| 85 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +427 | 43052 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +415 | 23740 |
| 87 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +413 | 41615 |
| 88 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +411 | 29520 |
| 89 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +405 | 21371 |
| 90 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +401 | 6970 |
| 91 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +400 | 4913 |
| 92 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +399 | 6546 |
| 93 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +383 | 32329 |
| 94 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +381 | 56796 |
| 95 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +379 | 30590 |
| 96 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +379 | 36397 |
| 97 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +369 | 23138 |
| 98 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +365 | 5164 |
| 99 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +364 | 8043 |
| 100 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +349 | 28915 |
| 101 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +338 | 4612 |
| 102 | [jundot/omlx](https://github.com/jundot/omlx) | +332 | 16173 |
| 103 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +323 | 3694 |
| 104 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +322 | 4974 |
| 105 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +303 | 12657 |
| 106 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +302 | 23114 |
| 107 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +297 | 7453 |
| 108 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +297 | 16301 |
| 109 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +292 | 3742 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +291 | 35302 |
| 111 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2430 |
| 112 | [MinishLab/semble](https://github.com/MinishLab/semble) | +277 | 4911 |
| 113 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +263 | 8168 |
| 114 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +259 | 7101 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +258 | 15949 |
| 116 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +252 | 3450 |
| 117 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +248 | 4263 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +244 | 16067 |
| 119 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +241 | 11588 |
| 120 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +240 | 14453 |
| 121 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +240 | 24059 |
| 122 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +236 | 32700 |
| 123 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +235 | 45916 |
| 124 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +232 | 17409 |
| 125 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +232 | 5765 |
| 126 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +231 | 36799 |
| 127 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +230 | 2670 |
| 128 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +229 | 39980 |
| 129 | [openai/skills](https://github.com/openai/skills) | +225 | 21601 |
| 130 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +225 | 9093 |
| 131 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +222 | 8395 |
| 132 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +218 | 5695 |
| 133 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +213 | 3013 |
| 134 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +210 | 2786 |
| 135 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +206 | 20396 |
| 136 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +203 | 6445 |
| 137 | [roboflow/supervision](https://github.com/roboflow/supervision) | +202 | 36553 |
| 138 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +201 | 23068 |
| 139 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +201 | 34087 |
| 140 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +198 | 3994 |
| 141 | [88lin/video_vip](https://github.com/88lin/video_vip) | +192 | 3572 |
| 142 | [browser-use/video-use](https://github.com/browser-use/video-use) | +191 | 9220 |
| 143 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +191 | 22842 |
| 144 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +187 | 26868 |
| 145 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +185 | 34092 |
| 146 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +185 | 24643 |
| 147 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +184 | 2699 |
| 148 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +183 | 18183 |
| 149 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +182 | 2572 |
| 150 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +180 | 2716 |
| 151 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +177 | 34594 |
| 152 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +176 | 5184 |
| 153 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +174 | 2349 |
| 154 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6485 |
| 155 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +168 | 26668 |
| 156 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +164 | 48653 |
| 157 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +163 | 3188 |
| 158 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +163 | 0 |
| 159 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +159 | 23912 |
| 160 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1903 |
| 161 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +156 | 5481 |
| 162 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +153 | 7203 |
| 163 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +150 | 2384 |
| 164 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +148 | 7075 |
| 165 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +148 | 7698 |
| 166 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +146 | 28031 |
| 167 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +144 | 43829 |
| 168 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +144 | 4763 |
| 169 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +138 | 6308 |
| 170 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +137 | 10333 |
| 171 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +137 | 10851 |
| 172 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +137 | 37564 |
| 173 | [playcanvas/engine](https://github.com/playcanvas/engine) | +134 | 15977 |
| 174 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +132 | 29025 |
| 175 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +131 | 24113 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +131 | 15294 |
| 177 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +130 | 4095 |
| 178 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +126 | 2453 |
| 179 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +126 | 1742 |
| 180 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1995 |
| 181 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +126 | 8414 |
| 182 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +126 | 6569 |
| 183 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +124 | 32872 |
| 184 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +121 | 36103 |
| 185 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +116 | 4273 |
| 186 | [browserbase/skills](https://github.com/browserbase/skills) | +113 | 3526 |
| 187 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +111 | 27685 |
| 188 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +110 | 17790 |
| 189 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +109 | 2621 |
| 190 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1505 |
| 191 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +108 | 5033 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +107 | 4328 |
| 193 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +106 | 8535 |
| 194 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +103 | 12052 |
| 195 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +100 | 1158 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +100 | 3896 |
| 197 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +100 | 5414 |
| 198 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 800 |
| 199 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +93 | 2231 |
| 200 | [usebruno/bruno](https://github.com/usebruno/bruno) | +91 | 41086 |
| 201 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +88 | 2370 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +87 | 7290 |
| 203 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +86 | 39596 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +83 | 23611 |
| 205 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +82 | 15714 |
| 206 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +77 | 1025 |
| 207 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +72 | 10844 |
| 208 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1185 |
| 209 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +67 | 15114 |
| 210 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +66 | 2480 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +65 | 3459 |
| 212 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +65 | 4941 |
| 213 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +64 | 8238 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +64 | 40265 |
| 215 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +62 | 1590 |
| 216 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +60 | 37313 |
| 217 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +58 | 10192 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +55 | 2027 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +54 | 35473 |
| 220 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +53 | 4889 |
| 221 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +53 | 8167 |
| 222 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +52 | 822 |
| 223 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +52 | 3595 |
| 224 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 382 |
| 225 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 289 |
| 226 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +50 | 11996 |
| 227 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +47 | 507 |
| 228 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +46 | 4265 |
| 229 | [sandeco/reversa](https://github.com/sandeco/reversa) | +45 | 1190 |
| 230 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +44 | 479 |
| 231 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 368 |
| 232 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +43 | 8642 |
| 233 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +43 | 9369 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +42 | 2616 |
| 235 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +41 | 349 |
| 236 | [robinebers/openusage](https://github.com/robinebers/openusage) | +40 | 2782 |
| 237 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +40 | 2049 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +38 | 13611 |
| 239 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +37 | 1246 |
| 240 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +36 | 1775 |
| 241 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +34 | 7781 |
| 242 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4238 |
| 243 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +34 | 1777 |
| 244 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 245 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +33 | 4355 |
| 246 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +33 | 9912 |
| 247 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +32 | 4841 |
| 248 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 278 |
| 249 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +31 | 439 |
| 250 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +31 | 2098 |
| 251 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +30 | 695 |
| 252 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +30 | 2437 |
| 253 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +29 | 929 |
| 254 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +29 | 359 |
| 255 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +28 | 1989 |
| 256 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +28 | 308 |
| 257 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +28 | 3340 |
| 258 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +28 | 2317 |
| 259 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +27 | 2505 |
| 260 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +27 | 1092 |
| 261 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +27 | 2173 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +27 | 896 |
| 263 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +27 | 3377 |
| 264 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +27 | 2419 |
| 265 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +26 | 1867 |
| 266 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +26 | 1482 |
| 267 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +26 | 2376 |
| 268 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +25 | 695 |
| 269 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 200 |
| 270 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +24 | 262 |
| 271 | [is-a-dev/register](https://github.com/is-a-dev/register) | +23 | 10436 |
| 272 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 398 |
| 273 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +22 | 567 |
| 274 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +22 | 2981 |
| 275 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +21 | 661 |
| 276 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +20 | 748 |
| 277 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +18 | 299 |
| 278 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 433 |
| 279 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2661 |
| 280 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +16 | 1097 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +16 | 2514 |
| 282 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +16 | 556 |
| 283 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +16 | 846 |
| 284 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3255 |
| 285 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +15 | 293 |
| 286 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +14 | 1574 |
| 287 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +14 | 800 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +13 | 2050 |
| 289 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +13 | 538 |
| 290 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +12 | 509 |
| 291 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +11 | 1602 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +11 | 2258 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 216 |
| 294 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 295 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +10 | 976 |
| 296 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +10 | 299 |
| 297 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 462 |
| 298 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 144 |
| 299 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +9 | 356 |
| 300 | [liyupi/yu-ai-code-mother](https://github.com/liyupi/yu-ai-code-mother) | +9 | 1736 |
