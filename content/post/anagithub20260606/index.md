---
title: "2026-06-06 GitHub增长趋势报告"
description: "1.odysseus+237 2.taste-skill+115 3.headroom+83 4.VoxCPM+65 5.graphify+63"
date: 2026-06-06T21:06:51+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-06 21:06:51

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
        'weekly': {"categories": ["rtk-ai/rtk", "mvanhorn/last30days-skill", "supermemoryai/supermemory", "MadsLorentzen/ai-job-search", "heygen-com/hyperframes", "Open-LLM-VTuber/Open-LLM-VTuber", "Yuan1z0825/nature-skills", "pbakaus/impeccable", "Imbad0202/academic-research-skills", "lfnovo/open-notebook", "safishamsi/graphify", "nesquena/hermes-webui", "rohitg00/ai-engineering-from-scratch", "OpenBMB/VoxCPM", "Leonxlnx/taste-skill", "Lum1104/Understand-Anything", "unicity-astrid/astrid", "colbymchenry/codegraph", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [76, 82, 87, 92, 95, 96, 100, 109, 112, 124, 144, 146, 151, 186, 252, 255, 327, 361, 467, 1773]},
        'monthly': {"categories": ["antirez/ds4", "VoltAgent/awesome-design-md", "github/spec-kit", "rohitg00/agentmemory", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "addyosmani/agent-skills", "pewdiepie-archdaemon/odysseus", "CloakHQ/CloakBrowser", "anthropics/financial-services", "farion1231/cc-switch", "tinyhumansai/openhuman", "Hmbown/CodeWhale", "affaan-m/ECC", "obra/superpowers", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1374, 1383, 1403, 1493, 1571, 1668, 1716, 1773, 1874, 2014, 2265, 2266, 2281, 2526, 2769, 2810, 2907, 3618, 4034, 4246]}
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
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +237 | 58529 |
| 2 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +115 | 35157 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +83 | 15731 |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +65 | 27136 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +63 | 60537 |
| 6 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +61 | 26552 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +53 | 53513 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +51 | 22236 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +46 | 29364 |
| 10 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +44 | 33145 |
| 11 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +41 | 7799 |
| 12 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +40 | 3005 |
| 13 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +34 | 28701 |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +31 | 2592 |
| 15 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 17281 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +30 | 28050 |
| 17 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +29 | 35107 |
| 18 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +29 | 2348 |
| 19 | [withastro/flue](https://github.com/withastro/flue) | +26 | 4702 |
| 20 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +24 | 5222 |
| 21 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +23 | 8297 |
| 22 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 25716 |
| 23 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +22 | 1188 |
| 24 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +22 | 1012 |
| 25 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +22 | 24453 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +21 | 29254 |
| 27 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +21 | 8153 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +20 | 12137 |
| 29 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +20 | 9359 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +19 | 48664 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1773 | 58529 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +467 | 15731 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +361 | 43027 |
| 4 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +327 | 7799 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +255 | 53513 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +252 | 35157 |
| 7 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +186 | 27136 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +151 | 29364 |
| 9 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +146 | 13640 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +144 | 60537 |
| 11 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +124 | 26552 |
| 12 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +112 | 28050 |
| 13 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +109 | 35107 |
| 14 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +100 | 17281 |
| 15 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +96 | 10183 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +95 | 24968 |
| 17 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +92 | 2592 |
| 18 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +87 | 25824 |
| 19 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +82 | 28701 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +76 | 59440 |
| 21 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +74 | 5684 |
| 22 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +73 | 10773 |
| 23 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +72 | 8297 |
| 24 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +71 | 10980 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +69 | 22236 |
| 26 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +68 | 33145 |
| 27 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +67 | 14596 |
| 28 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +67 | 24453 |
| 29 | [revfactory/harness](https://github.com/revfactory/harness) | +66 | 6243 |
| 30 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +65 | 29254 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +65 | 24806 |
| 32 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +65 | 23948 |
| 33 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +64 | 3005 |
| 34 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +64 | 10892 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +62 | 41058 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +62 | 57058 |
| 37 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +61 | 25716 |
| 38 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +59 | 4773 |
| 39 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +59 | 13870 |
| 40 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +59 | 21559 |
| 41 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +52 | 21270 |
| 42 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +52 | 30240 |
| 43 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +51 | 8045 |
| 44 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +51 | 20065 |
| 45 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +51 | 25635 |
| 46 | [withastro/flue](https://github.com/withastro/flue) | +49 | 4702 |
| 47 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +49 | 37318 |
| 48 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +49 | 15382 |
| 49 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +47 | 30978 |
| 50 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +47 | 18379 |
| 51 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +46 | 48664 |
| 52 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +45 | 2348 |
| 53 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +44 | 48436 |
| 54 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +44 | 3351 |
| 55 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +43 | 32763 |
| 56 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +43 | 9327 |
| 57 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +42 | 16348 |
| 58 | [multica-ai/multica](https://github.com/multica-ai/multica) | +41 | 35576 |
| 59 | [decolua/9router](https://github.com/decolua/9router) | +41 | 16602 |
| 60 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +40 | 27516 |
| 61 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +39 | 3054 |
| 62 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +39 | 959 |
| 63 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +38 | 6820 |
| 64 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +38 | 1575 |
| 65 | [FufuLauncher/FufuLauncher](https://github.com/FufuLauncher/FufuLauncher) | +37 | 1474 |
| 66 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +37 | 22985 |
| 67 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +37 | 8372 |
| 68 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +37 | 23833 |
| 69 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +36 | 56675 |
| 70 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +36 | 2379 |
| 71 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +36 | 16533 |
| 72 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +35 | 7911 |
| 73 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +35 | 9512 |
| 74 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +34 | 1693 |
| 75 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +34 | 5222 |
| 76 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +34 | 6285 |
| 77 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +33 | 21577 |
| 78 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +33 | 6408 |
| 79 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +33 | 42201 |
| 80 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +32 | 5047 |
| 81 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +32 | 55916 |
| 82 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +32 | 10604 |
| 83 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +32 | 28797 |
| 84 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +31 | 1709 |
| 85 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +31 | 24427 |
| 86 | [santifer/career-ops](https://github.com/santifer/career-ops) | +30 | 49240 |
| 87 | [blader/humanizer](https://github.com/blader/humanizer) | +30 | 22647 |
| 88 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +30 | 15870 |
| 89 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +30 | 19355 |
| 90 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +30 | 41558 |
| 91 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +29 | 20671 |
| 92 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +29 | 7448 |
| 93 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +29 | 21523 |
| 94 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +28 | 9359 |
| 95 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +28 | 12137 |
| 96 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +28 | 16462 |
| 97 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +27 | 8153 |
| 98 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +27 | 3646 |
| 99 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +27 | 2394 |
| 100 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +27 | 5649 |
| 101 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +26 | 1012 |
| 102 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +26 | 27411 |
| 103 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +26 | 7027 |
| 104 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +24 | 29504 |
| 105 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +23 | 3070 |
| 106 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +23 | 11540 |
| 107 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 9170 |
| 108 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +23 | 4057 |
| 109 | [MaxMiksa/Auto-Company](https://github.com/MaxMiksa/Auto-Company) | +21 | 1139 |
| 110 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +21 | 13107 |
| 111 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +20 | 589 |
| 112 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +20 | 6254 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +20 | 17331 |
| 114 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +20 | 19082 |
| 115 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +19 | 24014 |
| 116 | [browser-act/skills](https://github.com/browser-act/skills) | +19 | 2044 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +19 | 39909 |
| 118 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +18 | 2314 |
| 119 | [openai/plugins](https://github.com/openai/plugins) | +18 | 1735 |
| 120 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +18 | 7162 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4246 | 169333 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4034 | 119425 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3618 | 184663 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2907 | 43027 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2810 | 53513 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2769 | 60312 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2526 | 51199 |
| 8 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +2281 | 37318 |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2266 | 30978 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2265 | 93392 |
| 11 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +2014 | 30240 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1874 | 24453 |
| 13 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1773 | 58529 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1716 | 48664 |
| 15 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1668 | 29364 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1571 | 28050 |
| 17 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1493 | 21559 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +1403 | 71722 |
| 19 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1383 | 87999 |
| 20 | [antirez/ds4](https://github.com/antirez/ds4) | +1374 | 13090 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1337 | 107648 |
| 22 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1333 | 71305 |
| 23 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1165 | 57058 |
| 24 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1133 | 60537 |
| 25 | [decolua/9router](https://github.com/decolua/9router) | +1126 | 16602 |
| 26 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1122 | 107923 |
| 27 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1116 | 58214 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1080 | 60364 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1065 | 30590 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1035 | 59440 |
| 31 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +994 | 61566 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +992 | 17281 |
| 33 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +989 | 35157 |
| 34 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +989 | 69505 |
| 35 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +959 | 29504 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +937 | 34148 |
| 37 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +922 | 24806 |
| 38 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +851 | 16348 |
| 39 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +796 | 21577 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +790 | 32763 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +779 | 35576 |
| 42 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +740 | 49621 |
| 43 | [floci-io/floci](https://github.com/floci-io/floci) | +739 | 13717 |
| 44 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +737 | 11315 |
| 45 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +721 | 18379 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +684 | 24968 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +673 | 10773 |
| 48 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +672 | 8092 |
| 49 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +669 | 36167 |
| 50 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +639 | 6820 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +612 | 21270 |
| 52 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +603 | 15382 |
| 53 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +595 | 27411 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +585 | 25716 |
| 55 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +577 | 18301 |
| 56 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +570 | 35107 |
| 57 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +569 | 42201 |
| 58 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +559 | 4525 |
| 59 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +544 | 4112 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +531 | 53204 |
| 61 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +506 | 37337 |
| 62 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +504 | 25635 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +503 | 19355 |
| 64 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +502 | 19356 |
| 65 | [soxoj/maigret](https://github.com/soxoj/maigret) | +497 | 31309 |
| 66 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +495 | 61131 |
| 67 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +494 | 15731 |
| 68 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +488 | 14596 |
| 69 | [withcoral/coral](https://github.com/withcoral/coral) | +476 | 5140 |
| 70 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +475 | 41058 |
| 71 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +460 | 5047 |
| 72 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +453 | 8919 |
| 73 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +451 | 7448 |
| 74 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +448 | 12267 |
| 75 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +445 | 13107 |
| 76 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +442 | 6208 |
| 77 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +441 | 41558 |
| 78 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +439 | 10892 |
| 79 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +431 | 7847 |
| 80 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +431 | 42995 |
| 81 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +430 | 10980 |
| 82 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +428 | 23661 |
| 83 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +427 | 13870 |
| 84 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +426 | 13640 |
| 85 | [santifer/career-ops](https://github.com/santifer/career-ops) | +425 | 49240 |
| 86 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +411 | 8045 |
| 87 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +408 | 29461 |
| 88 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +405 | 27136 |
| 89 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +403 | 21264 |
| 90 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +400 | 4902 |
| 91 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +391 | 4475 |
| 92 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +387 | 6408 |
| 93 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +387 | 56675 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +385 | 36269 |
| 95 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +384 | 22985 |
| 96 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +375 | 32172 |
| 97 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +360 | 5147 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +358 | 28797 |
| 99 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +331 | 4533 |
| 100 | [jundot/omlx](https://github.com/jundot/omlx) | +330 | 16078 |
| 101 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +328 | 7799 |
| 102 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +323 | 3682 |
| 103 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +319 | 7349 |
| 104 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +317 | 4922 |
| 105 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +309 | 12640 |
| 106 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +300 | 16052 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +298 | 32655 |
| 108 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2427 |
| 109 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +287 | 7055 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +284 | 35096 |
| 111 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +279 | 3646 |
| 112 | [MinishLab/semble](https://github.com/MinishLab/semble) | +275 | 4888 |
| 113 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +274 | 14422 |
| 114 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +269 | 8385 |
| 115 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +265 | 28701 |
| 116 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +262 | 8161 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +256 | 15870 |
| 118 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +248 | 5649 |
| 119 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +246 | 4247 |
| 120 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +246 | 15996 |
| 121 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +244 | 23948 |
| 122 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +243 | 11540 |
| 123 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +242 | 5725 |
| 124 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +241 | 22984 |
| 125 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +236 | 45840 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +234 | 17331 |
| 127 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +233 | 36799 |
| 128 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +230 | 3351 |
| 129 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +229 | 39909 |
| 130 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +228 | 9075 |
| 131 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +221 | 2597 |
| 132 | [openai/skills](https://github.com/openai/skills) | +214 | 21488 |
| 133 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +213 | 2787 |
| 134 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +212 | 2984 |
| 135 | [z-lab/dflash](https://github.com/z-lab/dflash) | +209 | 4952 |
| 136 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +206 | 22237 |
| 137 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +206 | 20358 |
| 138 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +205 | 6409 |
| 139 | [browser-use/video-use](https://github.com/browser-use/video-use) | +204 | 9170 |
| 140 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +202 | 33993 |
| 141 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +199 | 2713 |
| 142 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +197 | 3984 |
| 143 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +197 | 26774 |
| 144 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +192 | 24599 |
| 145 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +190 | 2393 |
| 146 | [88lin/video_vip](https://github.com/88lin/video_vip) | +190 | 3516 |
| 147 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +189 | 22790 |
| 148 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +188 | 1760 |
| 149 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +188 | 4546 |
| 150 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +186 | 2721 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +185 | 34034 |
| 152 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +182 | 2566 |
| 153 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +181 | 18135 |
| 154 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +176 | 34555 |
| 155 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +174 | 2298 |
| 156 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +174 | 1899 |
| 157 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +172 | 5136 |
| 158 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +168 | 6476 |
| 159 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +163 | 7162 |
| 160 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +163 | 0 |
| 161 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +161 | 26605 |
| 162 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +158 | 23833 |
| 163 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +157 | 0 |
| 164 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1897 |
| 165 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +155 | 3070 |
| 166 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +153 | 5454 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +150 | 27977 |
| 168 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +149 | 4747 |
| 169 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +149 | 2374 |
| 170 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +147 | 7665 |
| 171 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +146 | 43790 |
| 172 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +141 | 7027 |
| 173 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +139 | 6254 |
| 174 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +137 | 15247 |
| 175 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +136 | 48436 |
| 176 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +136 | 10795 |
| 177 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +136 | 37564 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +136 | 28982 |
| 179 | [playcanvas/engine](https://github.com/playcanvas/engine) | +133 | 15968 |
| 180 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +129 | 4057 |
| 181 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +127 | 6509 |
| 182 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 2003 |
| 183 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +123 | 2379 |
| 184 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +122 | 8372 |
| 185 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +120 | 36103 |
| 186 | [browserbase/skills](https://github.com/browserbase/skills) | +117 | 3513 |
| 187 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +114 | 4250 |
| 188 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +112 | 5020 |
| 189 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +108 | 1497 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +108 | 27655 |
| 191 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +108 | 17752 |
| 192 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +106 | 8534 |
| 193 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +105 | 4276 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +103 | 3835 |
| 195 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +103 | 12042 |
| 196 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +102 | 5403 |
| 197 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +99 | 1141 |
| 198 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 792 |
| 199 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +93 | 2219 |
| 200 | [usebruno/bruno](https://github.com/usebruno/bruno) | +92 | 41086 |
| 201 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +89 | 2314 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +89 | 39596 |
| 203 | [eze-is/web-access](https://github.com/eze-is/web-access) | +86 | 7249 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +81 | 23583 |
| 205 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +80 | 15625 |
| 206 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +77 | 1010 |
| 207 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +73 | 1575 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +71 | 10829 |
| 209 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +71 | 15101 |
| 210 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +66 | 1177 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +65 | 3423 |
| 212 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +65 | 2474 |
| 213 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +64 | 4902 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +63 | 40265 |
| 215 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +61 | 10184 |
| 216 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +59 | 8153 |
| 217 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +56 | 2002 |
| 219 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +54 | 8157 |
| 220 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +54 | 35473 |
| 221 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +52 | 4867 |
| 222 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 381 |
| 223 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 224 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +51 | 3573 |
| 225 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +50 | 11993 |
| 226 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +50 | 790 |
| 227 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +49 | 2048 |
| 228 | [sandeco/reversa](https://github.com/sandeco/reversa) | +48 | 1187 |
| 229 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +47 | 918 |
| 230 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +46 | 4251 |
| 231 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +46 | 505 |
| 232 | [robinebers/openusage](https://github.com/robinebers/openusage) | +45 | 2768 |
| 233 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +44 | 8634 |
| 234 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 368 |
| 235 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +44 | 9359 |
| 236 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +44 | 2598 |
| 237 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +43 | 466 |
| 238 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 349 |
| 239 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +37 | 13607 |
| 240 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1244 |
| 241 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +35 | 4345 |
| 242 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +34 | 7756 |
| 243 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +34 | 1754 |
| 244 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +34 | 1766 |
| 245 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +34 | 4834 |
| 246 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 247 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9910 |
| 248 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +33 | 4231 |
| 249 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 278 |
| 250 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +31 | 2428 |
| 251 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +30 | 2167 |
| 252 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +30 | 2085 |
| 253 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +29 | 1092 |
| 254 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +29 | 687 |
| 255 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +29 | 3334 |
| 256 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +29 | 359 |
| 257 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +29 | 2399 |
| 258 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +28 | 2302 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +28 | 896 |
| 260 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +27 | 1974 |
| 261 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +27 | 297 |
| 262 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +27 | 413 |
| 263 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +27 | 3363 |
| 264 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +26 | 1046 |
| 265 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +25 | 682 |
| 266 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +25 | 1477 |
| 267 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +25 | 2372 |
| 268 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 200 |
| 269 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +23 | 567 |
| 270 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +23 | 255 |
| 271 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 396 |
| 272 | [is-a-dev/register](https://github.com/is-a-dev/register) | +21 | 10426 |
| 273 | [cv-cat/XHS_ALL_IN_ONE](https://github.com/cv-cat/XHS_ALL_IN_ONE) | +21 | 388 |
| 274 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +20 | 738 |
| 275 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +19 | 656 |
| 276 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2981 |
| 277 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 421 |
| 278 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2663 |
| 279 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +16 | 1092 |
| 280 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +16 | 275 |
| 281 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +16 | 842 |
| 282 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +16 | 553 |
| 283 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +16 | 800 |
| 284 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3257 |
| 285 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +14 | 2500 |
| 286 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 286 |
| 287 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +14 | 1561 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +13 | 2044 |
| 289 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +12 | 504 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +12 | 536 |
| 291 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +11 | 2259 |
| 292 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +11 | 1600 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 213 |
| 294 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +11 | 299 |
| 295 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 296 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 460 |
| 297 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 143 |
| 298 | [liyupi/yu-ai-code-mother](https://github.com/liyupi/yu-ai-code-mother) | +9 | 1734 |
| 299 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +9 | 970 |
| 300 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +9 | 354 |
