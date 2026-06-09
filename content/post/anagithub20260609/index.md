---
title: "2026-06-09 GitHub增长趋势报告"
description: "1.last30days-skill+77 2.headroom+52 3.turbovec+48 4.taste-skill+40 5.Agent-Reach+35"
date: 2026-06-09T21:48:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-09 21:48:45

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
        'daily': {"categories": ["addyosmani/agent-skills", "dmtrKovalenko/fff", "Wei-Shaw/sub2api", "tashfeenahmed/freellmapi", "XingYu-Zhong/DeepSeek-GUI", "alibaba/open-code-review", "router-for-me/CLIProxyAPI", "rohitg00/ai-engineering-from-scratch", "luongnv89/claude-howto", "santifer/career-ops", "Imbad0202/academic-research-skills", "epoko77-ai/im-not-ai", "refactoringhq/tolaria", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "Panniantong/Agent-Reach", "Leonxlnx/taste-skill", "RyanCodrai/turbovec", "chopratejas/headroom", "mvanhorn/last30days-skill"], "data": [12, 12, 12, 13, 13, 13, 13, 14, 18, 19, 19, 20, 22, 25, 27, 35, 40, 48, 52, 77]},
        'weekly': {"categories": ["Imbad0202/academic-research-skills", "santifer/career-ops", "CopilotKit/CopilotKit", "XingYu-Zhong/DeepSeek-GUI", "rohitg00/ai-engineering-from-scratch", "OpenBMB/VoxCPM", "roboflow/supervision", "unicity-astrid/sdk-rust", "Panniantong/Agent-Reach", "lfnovo/open-notebook", "alibaba/open-code-review", "Lum1104/Understand-Anything", "RyanCodrai/turbovec", "unicity-astrid/sdk-js", "unicity-astrid/astrid", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "mvanhorn/last30days-skill", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [146, 156, 168, 169, 185, 198, 206, 215, 227, 247, 287, 318, 332, 345, 377, 398, 467, 499, 658, 1675]},
        'monthly': {"categories": ["garrytan/gstack", "VoltAgent/awesome-design-md", "Hmbown/CodeWhale", "anthropics/financial-services", "ruvnet/RuView", "github/spec-kit", "rohitg00/agentmemory", "Imbad0202/academic-research-skills", "CloakHQ/CloakBrowser", "rohitg00/ai-engineering-from-scratch", "farion1231/cc-switch", "pewdiepie-archdaemon/odysseus", "tinyhumansai/openhuman", "affaan-m/ECC", "obra/superpowers", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1240, 1256, 1354, 1354, 1363, 1392, 1467, 1608, 1720, 1747, 2073, 2266, 2273, 2500, 2635, 2896, 3026, 3433, 3789, 3877]}
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
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +77 | 37115 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +52 | 20426 |
| 3 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +48 | 10081 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +40 | 39490 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +35 | 25511 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +27 | 45856 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +25 | 55873 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +22 | 14257 |
| 9 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +20 | 2523 |
| 10 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 29471 |
| 11 | [santifer/career-ops](https://github.com/santifer/career-ops) | +19 | 51535 |
| 12 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +18 | 36202 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +14 | 30720 |
| 14 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +13 | 36969 |
| 15 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +13 | 5746 |
| 16 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +13 | 3338 |
| 17 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +13 | 9109 |
| 18 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +12 | 26714 |
| 19 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +12 | 8157 |
| 20 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +12 | 49761 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 25570 |
| 22 | [agent0ai/dox](https://github.com/agent0ai/dox) | +11 | 399 |
| 23 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +11 | 17822 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +11 | 26065 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +10 | 36760 |
| 26 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +10 | 28021 |
| 27 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 2064 |
| 28 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +8 | 57084 |
| 29 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +8 | 8131 |
| 30 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +8 | 21875 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1675 | 65365 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +658 | 20426 |
| 3 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +499 | 37115 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +467 | 39490 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +398 | 45856 |
| 6 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +377 | 8436 |
| 7 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8253 |
| 8 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +332 | 10081 |
| 9 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +318 | 55873 |
| 10 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +287 | 5746 |
| 11 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +247 | 28545 |
| 12 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +227 | 25511 |
| 13 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 14 | [roboflow/supervision](https://github.com/roboflow/supervision) | +206 | 36553 |
| 15 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +198 | 28021 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +185 | 30720 |
| 17 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +169 | 3338 |
| 18 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +168 | 34446 |
| 19 | [santifer/career-ops](https://github.com/santifer/career-ops) | +156 | 51535 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +146 | 29471 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +145 | 36760 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +144 | 26065 |
| 23 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +135 | 3089 |
| 24 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +128 | 10722 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +123 | 30263 |
| 26 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +116 | 19869 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +112 | 18314 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +109 | 60586 |
| 29 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +109 | 14086 |
| 30 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +107 | 3672 |
| 31 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +104 | 9109 |
| 32 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +104 | 31098 |
| 33 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +103 | 6331 |
| 34 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +100 | 49761 |
| 35 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +99 | 17822 |
| 36 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +96 | 1794 |
| 37 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +94 | 26714 |
| 38 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +94 | 11438 |
| 39 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +93 | 14257 |
| 40 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +93 | 2923 |
| 41 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +92 | 11539 |
| 42 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +90 | 57901 |
| 43 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +89 | 49187 |
| 44 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +87 | 15049 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +87 | 11514 |
| 46 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +80 | 21875 |
| 47 | [openai/plugins](https://github.com/openai/plugins) | +79 | 2569 |
| 48 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +76 | 20753 |
| 49 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +76 | 25570 |
| 50 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +75 | 41527 |
| 51 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +75 | 26153 |
| 52 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +73 | 30685 |
| 53 | [revfactory/harness](https://github.com/revfactory/harness) | +70 | 6662 |
| 54 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +69 | 25163 |
| 55 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +68 | 22106 |
| 56 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +66 | 8705 |
| 57 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +66 | 3661 |
| 58 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +65 | 2066 |
| 59 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +65 | 33409 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +64 | 36969 |
| 61 | [blader/humanizer](https://github.com/blader/humanizer) | +60 | 23161 |
| 62 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +60 | 5170 |
| 63 | [decolua/9router](https://github.com/decolua/9router) | +59 | 17054 |
| 64 | [withastro/flue](https://github.com/withastro/flue) | +58 | 4851 |
| 65 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +57 | 13402 |
| 66 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +57 | 16037 |
| 67 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +57 | 16630 |
| 68 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +56 | 1244 |
| 69 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +55 | 15660 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +55 | 32651 |
| 71 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +53 | 37713 |
| 72 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +52 | 19918 |
| 73 | [multica-ai/multica](https://github.com/multica-ai/multica) | +52 | 35991 |
| 74 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +51 | 36202 |
| 75 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +51 | 57084 |
| 76 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +51 | 6599 |
| 77 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +49 | 23508 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +49 | 27905 |
| 79 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +49 | 14242 |
| 80 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +46 | 9710 |
| 81 | [Makisuo/maple](https://github.com/Makisuo/maple) | +46 | 1231 |
| 82 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +46 | 3952 |
| 83 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +46 | 3315 |
| 84 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +46 | 2784 |
| 85 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +46 | 2869 |
| 86 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +46 | 1791 |
| 87 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +45 | 29076 |
| 88 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +43 | 21034 |
| 89 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +42 | 1302 |
| 90 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +41 | 899 |
| 91 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +41 | 6719 |
| 92 | [openai/skills](https://github.com/openai/skills) | +41 | 21807 |
| 93 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +41 | 24807 |
| 94 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +41 | 42529 |
| 95 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +41 | 9460 |
| 96 | [Ataraxy-Labs/sem](https://github.com/Ataraxy-Labs/sem) | +40 | 2553 |
| 97 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +40 | 8544 |
| 98 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +39 | 5136 |
| 99 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +38 | 21870 |
| 100 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +38 | 16433 |
| 101 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +38 | 27745 |
| 102 | [browser-act/skills](https://github.com/browser-act/skills) | +38 | 2265 |
| 103 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +37 | 2687 |
| 104 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +37 | 3462 |
| 105 | [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | +36 | 1847 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +35 | 16080 |
| 107 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +35 | 24054 |
| 108 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +33 | 733 |
| 109 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +32 | 24306 |
| 110 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +32 | 40177 |
| 111 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 428 |
| 112 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +31 | 6446 |
| 113 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +30 | 6452 |
| 114 | [jundot/omlx](https://github.com/jundot/omlx) | +30 | 16319 |
| 115 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +30 | 7219 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +30 | 5802 |
| 117 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +28 | 1975 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +28 | 29739 |
| 119 | [browser-use/video-use](https://github.com/browser-use/video-use) | +28 | 9348 |
| 120 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +27 | 2523 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3877 | 172044 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3789 | 123094 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3433 | 188728 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3026 | 45857 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2896 | 55873 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2635 | 60312 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2500 | 51199 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2273 | 31253 |
| 9 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2266 | 65365 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2073 | 96284 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1747 | 30720 |
| 12 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1720 | 25163 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1608 | 29471 |
| 14 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1467 | 22106 |
| 15 | [github/spec-kit](https://github.com/github/spec-kit) | +1392 | 71722 |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1363 | 72413 |
| 17 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1354 | 30685 |
| 18 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +1354 | 37713 |
| 19 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1256 | 88800 |
| 20 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1240 | 108666 |
| 21 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1229 | 64171 |
| 22 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1201 | 39490 |
| 23 | [antirez/ds4](https://github.com/antirez/ds4) | +1137 | 13316 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1127 | 49761 |
| 25 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1070 | 108894 |
| 26 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1015 | 61253 |
| 27 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +993 | 57901 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +978 | 30590 |
| 29 | [decolua/9router](https://github.com/decolua/9router) | +957 | 17054 |
| 30 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +948 | 29739 |
| 31 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +935 | 58696 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +930 | 18314 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +896 | 60586 |
| 34 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +886 | 70589 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +883 | 34148 |
| 36 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +862 | 49621 |
| 37 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +851 | 62482 |
| 38 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +812 | 16630 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +807 | 25570 |
| 40 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +777 | 19869 |
| 41 | [floci-io/floci](https://github.com/floci-io/floci) | +745 | 13865 |
| 42 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +743 | 20426 |
| 43 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +738 | 11414 |
| 44 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +712 | 33409 |
| 45 | [multica-ai/multica](https://github.com/multica-ai/multica) | +695 | 35991 |
| 46 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +690 | 11539 |
| 47 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +679 | 8175 |
| 48 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +673 | 21870 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +662 | 26065 |
| 50 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +656 | 37116 |
| 51 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +620 | 6921 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +603 | 21875 |
| 53 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +596 | 27745 |
| 54 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +575 | 36265 |
| 55 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +567 | 42529 |
| 56 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +561 | 4558 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +558 | 16037 |
| 58 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +551 | 10081 |
| 59 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +541 | 18656 |
| 60 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +539 | 36760 |
| 61 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +530 | 26714 |
| 62 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +521 | 19918 |
| 63 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +517 | 15049 |
| 64 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +506 | 26153 |
| 65 | [santifer/career-ops](https://github.com/santifer/career-ops) | +501 | 51535 |
| 66 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +474 | 9109 |
| 67 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +474 | 11514 |
| 68 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +465 | 5190 |
| 69 | [withcoral/coral](https://github.com/withcoral/coral) | +459 | 5141 |
| 70 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +456 | 6496 |
| 71 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +451 | 37948 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +450 | 41527 |
| 73 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +449 | 28021 |
| 74 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +442 | 8131 |
| 75 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +431 | 14086 |
| 76 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +422 | 13402 |
| 77 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +414 | 7638 |
| 78 | [soxoj/maigret](https://github.com/soxoj/maigret) | +412 | 31492 |
| 79 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +411 | 19475 |
| 80 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +410 | 43198 |
| 81 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +409 | 9461 |
| 82 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +405 | 6719 |
| 83 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +401 | 21595 |
| 84 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +401 | 4949 |
| 85 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +399 | 29638 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +392 | 23927 |
| 87 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +378 | 8436 |
| 88 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +372 | 41806 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +368 | 36969 |
| 90 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +366 | 5187 |
| 91 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +360 | 5136 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +359 | 32651 |
| 93 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +358 | 25511 |
| 94 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +358 | 11438 |
| 95 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +355 | 57084 |
| 96 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8253 |
| 97 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +343 | 14242 |
| 98 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +342 | 23508 |
| 99 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +330 | 17822 |
| 100 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +323 | 29076 |
| 101 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +322 | 5746 |
| 102 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +322 | 5017 |
| 103 | [roboflow/supervision](https://github.com/roboflow/supervision) | +312 | 36553 |
| 104 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +311 | 3727 |
| 105 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +297 | 28546 |
| 106 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2443 |
| 107 | [MinishLab/semble](https://github.com/MinishLab/semble) | +279 | 4994 |
| 108 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +279 | 3952 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +279 | 16319 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +278 | 36202 |
| 111 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +264 | 8193 |
| 112 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +256 | 7672 |
| 113 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +251 | 4305 |
| 114 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +243 | 3661 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +240 | 16179 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +239 | 16080 |
| 117 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +236 | 2836 |
| 118 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +234 | 16433 |
| 119 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +234 | 24263 |
| 120 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +227 | 17631 |
| 121 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +227 | 11785 |
| 122 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +226 | 7167 |
| 123 | [openai/skills](https://github.com/openai/skills) | +224 | 21807 |
| 124 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +222 | 40177 |
| 125 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +222 | 46066 |
| 126 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +222 | 5872 |
| 127 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +221 | 9123 |
| 128 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +219 | 12730 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +218 | 36799 |
| 130 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +216 | 3098 |
| 131 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +210 | 14568 |
| 132 | [88lin/video_vip](https://github.com/88lin/video_vip) | +202 | 3852 |
| 133 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +199 | 4016 |
| 134 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +196 | 34295 |
| 135 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +195 | 6534 |
| 136 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +188 | 5802 |
| 137 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +185 | 34296 |
| 138 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +183 | 2588 |
| 139 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +180 | 2461 |
| 140 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +180 | 23192 |
| 141 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +180 | 26986 |
| 142 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +180 | 24784 |
| 143 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +180 | 20531 |
| 144 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +179 | 5264 |
| 145 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +178 | 2811 |
| 146 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +174 | 3462 |
| 147 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +173 | 2869 |
| 148 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +173 | 22953 |
| 149 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6508 |
| 150 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +169 | 32812 |
| 151 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +166 | 49187 |
| 152 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +163 | 26770 |
| 153 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +162 | 34718 |
| 154 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +161 | 18291 |
| 155 | [browser-use/video-use](https://github.com/browser-use/video-use) | +160 | 9348 |
| 156 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +159 | 1935 |
| 157 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +158 | 24054 |
| 158 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +158 | 10722 |
| 159 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2395 |
| 160 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +146 | 5565 |
| 161 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +145 | 7219 |
| 162 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +144 | 7774 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +142 | 6452 |
| 164 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +137 | 10949 |
| 165 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +135 | 2687 |
| 166 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +135 | 1975 |
| 167 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +135 | 4807 |
| 168 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +134 | 43954 |
| 169 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +134 | 7274 |
| 170 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +133 | 28146 |
| 171 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +131 | 4160 |
| 172 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +130 | 24306 |
| 173 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +129 | 37564 |
| 174 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +127 | 8544 |
| 175 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1994 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +124 | 15423 |
| 177 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +120 | 2923 |
| 178 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +120 | 6714 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +120 | 29124 |
| 180 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +119 | 36103 |
| 181 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +118 | 4300 |
| 182 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +118 | 2793 |
| 183 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +118 | 32872 |
| 184 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +113 | 4500 |
| 185 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +110 | 1599 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +109 | 27758 |
| 187 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +107 | 17864 |
| 188 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +103 | 1241 |
| 189 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +103 | 5086 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +103 | 8543 |
| 191 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +100 | 12055 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +98 | 4027 |
| 193 | [openai/plugins](https://github.com/openai/plugins) | +97 | 2569 |
| 194 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 801 |
| 195 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +92 | 5455 |
| 196 | [usebruno/bruno](https://github.com/usebruno/bruno) | +92 | 41086 |
| 197 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +88 | 2510 |
| 198 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +86 | 39596 |
| 199 | [browserbase/skills](https://github.com/browserbase/skills) | +83 | 3537 |
| 200 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +81 | 1032 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +78 | 7380 |
| 202 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +77 | 15784 |
| 203 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1203 |
| 204 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +67 | 10886 |
| 205 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +66 | 8341 |
| 206 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +66 | 3505 |
| 207 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +66 | 2485 |
| 208 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +63 | 5011 |
| 209 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +61 | 15142 |
| 210 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +61 | 40265 |
| 211 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +59 | 2272 |
| 212 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +58 | 1611 |
| 213 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 214 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +56 | 855 |
| 215 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +55 | 10204 |
| 216 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +53 | 4927 |
| 217 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +52 | 8189 |
| 218 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 385 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +51 | 2080 |
| 220 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +50 | 12026 |
| 221 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +49 | 286 |
| 222 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +48 | 3676 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +48 | 35473 |
| 224 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 899 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +46 | 4323 |
| 226 | [sandeco/reversa](https://github.com/sandeco/reversa) | +45 | 1198 |
| 227 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +44 | 509 |
| 228 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +44 | 8661 |
| 229 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +42 | 9380 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +42 | 2643 |
| 231 | [robinebers/openusage](https://github.com/robinebers/openusage) | +38 | 2817 |
| 232 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1303 |
| 233 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +35 | 13630 |
| 234 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +34 | 7823 |
| 235 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4245 |
| 236 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +34 | 1799 |
| 237 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +34 | 4375 |
| 238 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +34 | 509 |
| 239 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 240 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 470 |
| 241 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +32 | 1813 |
| 242 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +32 | 373 |
| 243 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +32 | 352 |
| 244 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +31 | 2111 |
| 245 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +30 | 4884 |
| 246 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +30 | 365 |
| 247 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +28 | 772 |
| 248 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +28 | 330 |
| 249 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +28 | 2529 |
| 250 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +28 | 2056 |
| 251 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +28 | 3406 |
| 252 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +27 | 2004 |
| 253 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +27 | 2454 |
| 254 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +26 | 1912 |
| 255 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +26 | 2372 |
| 256 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +26 | 3398 |
| 257 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +25 | 1091 |
| 258 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +25 | 280 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +25 | 898 |
| 260 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 202 |
| 261 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +24 | 1504 |
| 262 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +23 | 939 |
| 263 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +23 | 571 |
| 264 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +23 | 1055 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +23 | 2448 |
| 266 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +22 | 764 |
| 267 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 398 |
| 268 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 131 |
| 269 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +22 | 285 |
| 270 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +21 | 674 |
| 271 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +21 | 2400 |
| 272 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +21 | 2985 |
| 273 | [is-a-dev/register](https://github.com/is-a-dev/register) | +20 | 10440 |
| 274 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +19 | 490 |
| 275 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +18 | 343 |
| 276 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 454 |
| 277 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +17 | 324 |
| 278 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +17 | 2661 |
| 279 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +16 | 2529 |
| 280 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +16 | 300 |
| 281 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1107 |
| 282 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +15 | 3255 |
| 283 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 525 |
| 284 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +13 | 570 |
| 285 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +13 | 854 |
| 286 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +13 | 1588 |
| 287 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +12 | 1605 |
| 288 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +11 | 108 |
| 289 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 110 |
| 290 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +11 | 807 |
| 291 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 222 |
| 292 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +10 | 2070 |
| 294 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +10 | 469 |
| 295 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +10 | 991 |
| 296 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +9 | 2265 |
| 297 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 188 |
| 298 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +9 | 361 |
| 299 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +9 | 304 |
| 300 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +9 | 544 |
