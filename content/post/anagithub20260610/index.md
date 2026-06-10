---
title: "2026-06-10 GitHub增长趋势报告"
description: "1.last30days-skill+74 2.container+44 3.headroom+41 4.taste-skill+31 5.turbovec+28"
date: 2026-06-10T22:04:22+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-10 22:04:22

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
        'daily': {"categories": ["OpenHub-Store/GitHub-Store", "shanraisshan/claude-code-best-practice", "francescopace/espectre", "rohitg00/ai-engineering-from-scratch", "alchaincyf/huashu-design", "Yuan1z0825/nature-skills", "alibaba/open-code-review", "rtk-ai/rtk", "hugohe3/ppt-master", "Lum1104/Understand-Anything", "pbakaus/impeccable", "Panniantong/Agent-Reach", "refactoringhq/tolaria", "colbymchenry/codegraph", "santifer/career-ops", "RyanCodrai/turbovec", "Leonxlnx/taste-skill", "chopratejas/headroom", "apple/container", "mvanhorn/last30days-skill"], "data": [8, 8, 8, 8, 9, 9, 10, 11, 11, 16, 17, 20, 23, 24, 24, 28, 31, 41, 44, 74]},
        'weekly': {"categories": ["heygen-com/hyperframes", "CopilotKit/CopilotKit", "XingYu-Zhong/DeepSeek-GUI", "OpenBMB/VoxCPM", "rohitg00/ai-engineering-from-scratch", "santifer/career-ops", "unicity-astrid/sdk-rust", "roboflow/supervision", "Panniantong/Agent-Reach", "lfnovo/open-notebook", "Lum1104/Understand-Anything", "alibaba/open-code-review", "unicity-astrid/sdk-js", "RyanCodrai/turbovec", "colbymchenry/codegraph", "unicity-astrid/astrid", "Leonxlnx/taste-skill", "mvanhorn/last30days-skill", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [143, 172, 173, 174, 175, 176, 215, 220, 246, 249, 287, 290, 345, 357, 378, 380, 469, 567, 589, 1337]},
        'monthly': {"categories": ["VoltAgent/awesome-design-md", "safishamsi/graphify", "Hmbown/CodeWhale", "Leonxlnx/taste-skill", "github/spec-kit", "rohitg00/agentmemory", "ruvnet/RuView", "Imbad0202/academic-research-skills", "CloakHQ/CloakBrowser", "rohitg00/ai-engineering-from-scratch", "farion1231/cc-switch", "tinyhumansai/openhuman", "pewdiepie-archdaemon/odysseus", "affaan-m/ECC", "obra/superpowers", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1162, 1164, 1180, 1206, 1243, 1330, 1362, 1576, 1634, 1704, 1932, 2244, 2297, 2369, 2481, 2865, 3039, 3196, 3592, 3681]}
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
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +74 | 38997 |
| 2 | [apple/container](https://github.com/apple/container) | +44 | 29557 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +41 | 21655 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +31 | 40535 |
| 5 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +28 | 10766 |
| 6 | [santifer/career-ops](https://github.com/santifer/career-ops) | +24 | 52468 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +24 | 46698 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +23 | 14855 |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +20 | 26028 |
| 10 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +17 | 37168 |
| 11 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +16 | 56576 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 26088 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +11 | 61022 |
| 14 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +10 | 6045 |
| 15 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 18771 |
| 16 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +9 | 18059 |
| 17 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +8 | 31028 |
| 18 | [francescopace/espectre](https://github.com/francescopace/espectre) | +8 | 8480 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +8 | 57269 |
| 20 | [OpenHub-Store/GitHub-Store](https://github.com/OpenHub-Store/GitHub-Store) | +8 | 14905 |
| 21 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +8 | 16363 |
| 22 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +8 | 2150 |
| 23 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +7 | 25376 |
| 24 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 29882 |
| 25 | [revfactory/harness](https://github.com/revfactory/harness) | +7 | 6749 |
| 26 | [freestylefly/CodexGuide](https://github.com/freestylefly/CodexGuide) | +7 | 1610 |
| 27 | [NarratorAI-Studio/narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill) | +7 | 1192 |
| 28 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +7 | 20907 |
| 29 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +7 | 21368 |
| 30 | [agent0ai/dox](https://github.com/agent0ai/dox) | +7 | 531 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1337 | 66972 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +589 | 21655 |
| 3 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +567 | 38997 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +469 | 40535 |
| 5 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +380 | 8573 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +378 | 46698 |
| 7 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +357 | 10766 |
| 8 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8254 |
| 9 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +290 | 6045 |
| 10 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +287 | 56576 |
| 11 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +249 | 28948 |
| 12 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +246 | 26028 |
| 13 | [roboflow/supervision](https://github.com/roboflow/supervision) | +220 | 36553 |
| 14 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 15 | [santifer/career-ops](https://github.com/santifer/career-ops) | +176 | 52468 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +175 | 31028 |
| 17 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +174 | 28229 |
| 18 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +173 | 3634 |
| 19 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +172 | 34597 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +143 | 26506 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +140 | 37168 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +137 | 29882 |
| 23 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +135 | 3168 |
| 24 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +129 | 20472 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +121 | 30423 |
| 26 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +116 | 14855 |
| 27 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +111 | 3808 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +111 | 18771 |
| 29 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +109 | 31098 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +108 | 61022 |
| 31 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +104 | 18059 |
| 32 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +102 | 51565 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +101 | 9424 |
| 34 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +101 | 10845 |
| 35 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +98 | 1844 |
| 36 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +98 | 3009 |
| 37 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +91 | 26964 |
| 38 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +91 | 49230 |
| 39 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +88 | 11575 |
| 40 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +85 | 15236 |
| 41 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +85 | 6406 |
| 42 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +84 | 58275 |
| 43 | [openai/plugins](https://github.com/openai/plugins) | +83 | 2744 |
| 44 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +82 | 11733 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +80 | 11719 |
| 46 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +80 | 14172 |
| 47 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +76 | 22118 |
| 48 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +76 | 26088 |
| 49 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +75 | 20907 |
| 50 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +72 | 41796 |
| 51 | [revfactory/harness](https://github.com/revfactory/harness) | +70 | 6749 |
| 52 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +70 | 26243 |
| 53 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +68 | 25376 |
| 54 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +67 | 2101 |
| 55 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +66 | 30764 |
| 56 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +64 | 22243 |
| 57 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +62 | 33614 |
| 58 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +62 | 8830 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +59 | 23543 |
| 60 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +58 | 1330 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +58 | 37100 |
| 62 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +58 | 15755 |
| 63 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +57 | 13465 |
| 64 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +57 | 3743 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +56 | 32795 |
| 66 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +56 | 16363 |
| 67 | [withastro/flue](https://github.com/withastro/flue) | +55 | 4890 |
| 68 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +54 | 57269 |
| 69 | [decolua/9router](https://github.com/decolua/9router) | +54 | 17183 |
| 70 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +53 | 5283 |
| 71 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +52 | 6724 |
| 72 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +51 | 36494 |
| 73 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +50 | 20077 |
| 74 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +50 | 1810 |
| 75 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +50 | 16704 |
| 76 | [tinyfish-io/bigset](https://github.com/tinyfish-io/bigset) | +50 | 1302 |
| 77 | [multica-ai/multica](https://github.com/multica-ai/multica) | +49 | 36139 |
| 78 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +49 | 37870 |
| 79 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +49 | 3159 |
| 80 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +48 | 23698 |
| 81 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +47 | 9830 |
| 82 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +47 | 3409 |
| 83 | [Makisuo/maple](https://github.com/Makisuo/maple) | +46 | 1238 |
| 84 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +45 | 28037 |
| 85 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +45 | 9634 |
| 86 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +44 | 8486 |
| 87 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +43 | 2068 |
| 88 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +43 | 4054 |
| 89 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +43 | 14384 |
| 90 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +42 | 1303 |
| 91 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +42 | 29158 |
| 92 | [openai/skills](https://github.com/openai/skills) | +42 | 21878 |
| 93 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +42 | 2964 |
| 94 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +41 | 911 |
| 95 | [Ataraxy-Labs/sem](https://github.com/Ataraxy-Labs/sem) | +41 | 2589 |
| 96 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +40 | 42638 |
| 97 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +39 | 6777 |
| 98 | [browser-act/skills](https://github.com/browser-act/skills) | +39 | 2333 |
| 99 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +38 | 16471 |
| 100 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +37 | 5199 |
| 101 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +37 | 8606 |
| 102 | [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | +37 | 1967 |
| 103 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +36 | 21960 |
| 104 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +36 | 21368 |
| 105 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +36 | 2150 |
| 106 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +36 | 2818 |
| 107 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +35 | 24394 |
| 108 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +35 | 27868 |
| 109 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +35 | 16136 |
| 110 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +34 | 749 |
| 111 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +33 | 3559 |
| 112 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +31 | 2663 |
| 113 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +31 | 6521 |
| 114 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +31 | 40274 |
| 115 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 445 |
| 116 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +29 | 2252 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +29 | 6509 |
| 118 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +29 | 24118 |
| 119 | [browser-use/video-use](https://github.com/browser-use/video-use) | +28 | 9399 |
| 120 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +28 | 5841 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3681 | 172790 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3592 | 124301 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3196 | 189867 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3039 | 46698 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2865 | 56576 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2481 | 60312 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2369 | 51199 |
| 8 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2297 | 66972 |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2244 | 31357 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1932 | 97455 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1704 | 31028 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1634 | 25376 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1576 | 29882 |
| 14 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1362 | 72851 |
| 15 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1330 | 22243 |
| 16 | [github/spec-kit](https://github.com/github/spec-kit) | +1243 | 71722 |
| 17 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1206 | 40535 |
| 18 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +1180 | 37870 |
| 19 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1164 | 64922 |
| 20 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1162 | 89065 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1123 | 108938 |
| 22 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1077 | 30764 |
| 23 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1008 | 110262 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +955 | 51565 |
| 25 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +939 | 29831 |
| 26 | [earendil-works/pi](https://github.com/earendil-works/pi) | +934 | 61527 |
| 27 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +892 | 49621 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +855 | 30590 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +847 | 58275 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +843 | 18771 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +843 | 61022 |
| 32 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +827 | 71067 |
| 33 | [decolua/9router](https://github.com/decolua/9router) | +825 | 17183 |
| 34 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +818 | 34148 |
| 35 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +811 | 62735 |
| 36 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +805 | 58860 |
| 37 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +777 | 21655 |
| 38 | [antirez/ds4](https://github.com/antirez/ds4) | +758 | 13406 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +756 | 26088 |
| 40 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +739 | 11438 |
| 41 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +708 | 20472 |
| 42 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +708 | 16704 |
| 43 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +704 | 38997 |
| 44 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +679 | 11733 |
| 45 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +679 | 8198 |
| 46 | [floci-io/floci](https://github.com/floci-io/floci) | +671 | 13933 |
| 47 | [multica-ai/multica](https://github.com/multica-ai/multica) | +658 | 36139 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +655 | 33614 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +621 | 26506 |
| 50 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +605 | 21960 |
| 51 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +586 | 27868 |
| 52 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +576 | 10766 |
| 53 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +555 | 42638 |
| 54 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +545 | 16363 |
| 55 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +539 | 22118 |
| 56 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +524 | 37168 |
| 57 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +522 | 20077 |
| 58 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +516 | 15236 |
| 59 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +508 | 6950 |
| 60 | [santifer/career-ops](https://github.com/santifer/career-ops) | +496 | 52468 |
| 61 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +494 | 18755 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +493 | 26964 |
| 63 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +476 | 9424 |
| 64 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +471 | 11719 |
| 65 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +471 | 36280 |
| 66 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +465 | 5241 |
| 67 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +459 | 6552 |
| 68 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +454 | 26243 |
| 69 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +443 | 8207 |
| 70 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +428 | 28229 |
| 71 | [withcoral/coral](https://github.com/withcoral/coral) | +427 | 5135 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +426 | 41796 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +418 | 38172 |
| 74 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +409 | 9634 |
| 75 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +406 | 6777 |
| 76 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +404 | 13465 |
| 77 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +401 | 14172 |
| 78 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +401 | 4965 |
| 79 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +396 | 4533 |
| 80 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +392 | 21701 |
| 81 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +383 | 19506 |
| 82 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +381 | 8573 |
| 83 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +380 | 29702 |
| 84 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +380 | 23991 |
| 85 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +366 | 26028 |
| 86 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +365 | 5194 |
| 87 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +362 | 5199 |
| 88 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +351 | 41889 |
| 89 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +346 | 43290 |
| 90 | [soxoj/maigret](https://github.com/soxoj/maigret) | +346 | 31952 |
| 91 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8254 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +341 | 32795 |
| 93 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +336 | 57269 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +334 | 37100 |
| 95 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +332 | 6045 |
| 96 | [blader/humanizer](https://github.com/blader/humanizer) | +332 | 23543 |
| 97 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +320 | 5027 |
| 98 | [roboflow/supervision](https://github.com/roboflow/supervision) | +318 | 36553 |
| 99 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +316 | 18059 |
| 100 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +316 | 23698 |
| 101 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +304 | 29158 |
| 102 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +300 | 28948 |
| 103 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +299 | 3750 |
| 104 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +296 | 11575 |
| 105 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +292 | 14384 |
| 106 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2449 |
| 107 | [MinishLab/semble](https://github.com/MinishLab/semble) | +281 | 5042 |
| 108 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +264 | 8203 |
| 109 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +258 | 36494 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +255 | 16379 |
| 111 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +252 | 4329 |
| 112 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +242 | 4054 |
| 113 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +238 | 2890 |
| 114 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +237 | 3743 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +228 | 16223 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +222 | 16136 |
| 117 | [openai/skills](https://github.com/openai/skills) | +221 | 21878 |
| 118 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +218 | 3127 |
| 119 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +218 | 9161 |
| 120 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +217 | 5960 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +215 | 17736 |
| 122 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +212 | 16471 |
| 123 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +211 | 7738 |
| 124 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +210 | 11874 |
| 125 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +210 | 7184 |
| 126 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +205 | 36799 |
| 127 | [88lin/video_vip](https://github.com/88lin/video_vip) | +201 | 3874 |
| 128 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +200 | 4023 |
| 129 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +200 | 46145 |
| 130 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +198 | 40274 |
| 131 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +197 | 12759 |
| 132 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +194 | 24326 |
| 133 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +190 | 14621 |
| 134 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +185 | 5841 |
| 135 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +185 | 6573 |
| 136 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +183 | 2501 |
| 137 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +183 | 2593 |
| 138 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +181 | 34384 |
| 139 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +179 | 5300 |
| 140 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +174 | 3559 |
| 141 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +174 | 34368 |
| 142 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +173 | 2964 |
| 143 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +171 | 2847 |
| 144 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +170 | 24924 |
| 145 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6518 |
| 146 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +169 | 23242 |
| 147 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +169 | 20593 |
| 148 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +167 | 27047 |
| 149 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +160 | 23008 |
| 150 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +159 | 1948 |
| 151 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +158 | 49230 |
| 152 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +157 | 24118 |
| 153 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +156 | 10845 |
| 154 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +152 | 34782 |
| 155 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2404 |
| 156 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +150 | 18333 |
| 157 | [browser-use/video-use](https://github.com/browser-use/video-use) | +148 | 9399 |
| 158 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +146 | 26841 |
| 159 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +142 | 2150 |
| 160 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +140 | 7271 |
| 161 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +138 | 2818 |
| 162 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +133 | 6521 |
| 163 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +129 | 4190 |
| 164 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +129 | 5599 |
| 165 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1993 |
| 166 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +125 | 11007 |
| 167 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3009 |
| 168 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +122 | 37564 |
| 169 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +121 | 24394 |
| 170 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +121 | 44009 |
| 171 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +121 | 28206 |
| 172 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +120 | 4827 |
| 173 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +119 | 7298 |
| 174 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +118 | 8606 |
| 175 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +117 | 6763 |
| 176 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +116 | 25460 |
| 177 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +114 | 32872 |
| 178 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +112 | 36103 |
| 179 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +111 | 1618 |
| 180 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +110 | 4584 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +110 | 15515 |
| 182 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +108 | 4313 |
| 183 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +106 | 7802 |
| 184 | [openai/plugins](https://github.com/openai/plugins) | +104 | 2744 |
| 185 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +104 | 29172 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +103 | 27793 |
| 187 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +103 | 8549 |
| 188 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +101 | 17902 |
| 189 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +99 | 12057 |
| 190 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +98 | 1249 |
| 191 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 802 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +93 | 5108 |
| 193 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +92 | 4097 |
| 194 | [usebruno/bruno](https://github.com/usebruno/bruno) | +91 | 41086 |
| 195 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +85 | 5483 |
| 196 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +83 | 2568 |
| 197 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +83 | 1053 |
| 198 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +74 | 2185 |
| 199 | [eze-is/web-access](https://github.com/eze-is/web-access) | +71 | 7416 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +70 | 15804 |
| 201 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +68 | 2802 |
| 202 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +67 | 8486 |
| 203 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1209 |
| 204 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +66 | 2490 |
| 205 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +65 | 5050 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +63 | 10915 |
| 207 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +61 | 3537 |
| 208 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +57 | 2281 |
| 209 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +55 | 1614 |
| 210 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +54 | 15165 |
| 211 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +53 | 855 |
| 212 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +52 | 4952 |
| 213 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 385 |
| 214 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +48 | 12039 |
| 215 | [browserbase/skills](https://github.com/browserbase/skills) | +48 | 3543 |
| 216 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +48 | 35473 |
| 217 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 911 |
| 218 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +46 | 10214 |
| 219 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +46 | 3702 |
| 220 | [sandeco/reversa](https://github.com/sandeco/reversa) | +44 | 1204 |
| 221 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +44 | 518 |
| 222 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +44 | 2095 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +43 | 4345 |
| 224 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +43 | 2663 |
| 225 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +42 | 9385 |
| 226 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +41 | 8675 |
| 227 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +41 | 286 |
| 228 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +40 | 8205 |
| 229 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1318 |
| 230 | [robinebers/openusage](https://github.com/robinebers/openusage) | +36 | 2830 |
| 231 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4248 |
| 232 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 233 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 492 |
| 234 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +32 | 7846 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +32 | 13635 |
| 236 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +31 | 1824 |
| 237 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +31 | 1829 |
| 238 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +31 | 4386 |
| 239 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +31 | 2122 |
| 240 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +30 | 369 |
| 241 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +29 | 4915 |
| 242 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +28 | 2015 |
| 243 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +28 | 336 |
| 244 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +27 | 786 |
| 245 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +27 | 2557 |
| 246 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +26 | 3424 |
| 247 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +26 | 2469 |
| 248 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 202 |
| 249 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +24 | 3408 |
| 250 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +23 | 1060 |
| 251 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +23 | 1518 |
| 252 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +23 | 2079 |
| 253 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +22 | 755 |
| 254 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 399 |
| 255 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 131 |
| 256 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +22 | 2385 |
| 257 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +21 | 1922 |
| 258 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +21 | 1090 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +21 | 898 |
| 260 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +20 | 940 |
| 261 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 575 |
| 262 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +20 | 2410 |
| 263 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +20 | 294 |
| 264 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +20 | 353 |
| 265 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +19 | 501 |
| 266 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +19 | 683 |
| 267 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13548 |
| 268 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2987 |
| 269 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +18 | 352 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +18 | 2460 |
| 271 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 462 |
| 272 | [is-a-dev/register](https://github.com/is-a-dev/register) | +17 | 10446 |
| 273 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +17 | 334 |
| 274 | [WJZ-P/sona](https://github.com/WJZ-P/sona) | +17 | 636 |
| 275 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +17 | 626 |
| 276 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +15 | 305 |
| 277 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +15 | 1303 |
| 278 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +14 | 2537 |
| 279 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +14 | 2661 |
| 280 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 531 |
| 281 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +13 | 574 |
| 282 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +12 | 1113 |
| 283 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +12 | 860 |
| 284 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +12 | 1606 |
| 285 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +12 | 3256 |
| 286 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +11 | 109 |
| 287 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 110 |
| 288 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 225 |
| 289 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +10 | 2077 |
| 291 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1598 |
| 292 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +10 | 212 |
| 293 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +10 | 471 |
| 294 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +10 | 809 |
| 295 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +9 | 2271 |
| 296 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +9 | 994 |
| 297 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +9 | 305 |
| 298 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +8 | 128 |
| 299 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +8 | 545 |
| 300 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 63 |
