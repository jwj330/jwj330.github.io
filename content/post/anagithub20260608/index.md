---
title: "2026-06-08 GitHub增长趋势报告"
description: "1.last30days-skill+247 2.taste-skill+138 3.turbovec+125 4.supervision+108 5.headroom+90"
date: 2026-06-08T21:50:59+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-08 21:50:59

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
        'daily': {"categories": ["openai/plugins", "santifer/career-ops", "refactoringhq/tolaria", "pbakaus/impeccable", "rohitg00/ai-engineering-from-scratch", "aaif-goose/goose", "yikart/AiToEarn", "Panniantong/Agent-Reach", "Crosstalk-Solutions/project-nomad", "alchaincyf/huashu-design", "XingYu-Zhong/DeepSeek-GUI", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "lfnovo/open-notebook", "alibaba/open-code-review", "chopratejas/headroom", "roboflow/supervision", "RyanCodrai/turbovec", "Leonxlnx/taste-skill", "mvanhorn/last30days-skill"], "data": [31, 32, 34, 39, 39, 44, 47, 49, 49, 49, 51, 54, 68, 72, 75, 90, 108, 125, 138, 247]},
        'weekly': {"categories": ["santifer/career-ops", "heygen-com/hyperframes", "nesquena/hermes-webui", "CopilotKit/CopilotKit", "pbakaus/impeccable", "XingYu-Zhong/DeepSeek-GUI", "rohitg00/ai-engineering-from-scratch", "roboflow/supervision", "Panniantong/Agent-Reach", "OpenBMB/VoxCPM", "lfnovo/open-notebook", "alibaba/open-code-review", "RyanCodrai/turbovec", "Lum1104/Understand-Anything", "unicity-astrid/astrid", "colbymchenry/codegraph", "mvanhorn/last30days-skill", "Leonxlnx/taste-skill", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [140, 144, 154, 154, 156, 161, 184, 190, 193, 218, 237, 282, 285, 335, 376, 416, 429, 453, 636, 1896]},
        'monthly': {"categories": ["VoltAgent/awesome-design-md", "ruvnet/RuView", "addyosmani/agent-skills", "github/spec-kit", "rohitg00/agentmemory", "Hmbown/CodeWhale", "Imbad0202/academic-research-skills", "anthropics/financial-services", "rohitg00/ai-engineering-from-scratch", "CloakHQ/CloakBrowser", "farion1231/cc-switch", "pewdiepie-archdaemon/odysseus", "tinyhumansai/openhuman", "affaan-m/ECC", "obra/superpowers", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "NousResearch/hermes-agent", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [1321, 1372, 1420, 1459, 1505, 1534, 1596, 1713, 1737, 1848, 2209, 2235, 2277, 2552, 2752, 2893, 3008, 3580, 3929, 4081]}
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
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +247 | 34296 |
| 2 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +138 | 38372 |
| 3 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +125 | 8703 |
| 4 | [roboflow/supervision](https://github.com/roboflow/supervision) | +108 | 36553 |
| 5 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +90 | 18712 |
| 6 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +75 | 5314 |
| 7 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +72 | 27942 |
| 8 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +68 | 44788 |
| 9 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +54 | 55161 |
| 10 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +51 | 2902 |
| 11 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +49 | 17517 |
| 12 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +49 | 30053 |
| 13 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +49 | 24009 |
| 14 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +47 | 19411 |
| 15 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +44 | 31098 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +39 | 30316 |
| 17 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +39 | 36230 |
| 18 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +34 | 13518 |
| 19 | [santifer/career-ops](https://github.com/santifer/career-ops) | +32 | 50426 |
| 20 | [openai/plugins](https://github.com/openai/plugins) | +31 | 2299 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +31 | 8843 |
| 22 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +30 | 1989 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +29 | 25713 |
| 24 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +28 | 869 |
| 25 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +25 | 28968 |
| 26 | [yukiyokotani/office-open-xml-viewer](https://github.com/yukiyokotani/office-open-xml-viewer) | +25 | 244 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +23 | 60135 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +20 | 3001 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +20 | 33201 |
| 30 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +20 | 1657 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1896 | 63658 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +636 | 18712 |
| 3 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +453 | 38372 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +429 | 34296 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +416 | 44788 |
| 6 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +376 | 8266 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +335 | 55161 |
| 8 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +285 | 8703 |
| 9 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +282 | 5314 |
| 10 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +237 | 27942 |
| 11 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +218 | 27727 |
| 12 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +193 | 24010 |
| 13 | [roboflow/supervision](https://github.com/roboflow/supervision) | +190 | 36553 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +184 | 30316 |
| 15 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +161 | 2902 |
| 16 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +156 | 36230 |
| 17 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +154 | 34087 |
| 18 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +154 | 14003 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +144 | 25713 |
| 20 | [santifer/career-ops](https://github.com/santifer/career-ops) | +140 | 50426 |
| 21 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +138 | 28968 |
| 22 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +135 | 3001 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +124 | 17929 |
| 24 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +123 | 10520 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +118 | 30053 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +113 | 60135 |
| 27 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +111 | 19411 |
| 28 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +109 | 3519 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +95 | 8843 |
| 30 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +95 | 6230 |
| 31 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +94 | 49237 |
| 32 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +94 | 2762 |
| 33 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +94 | 11273 |
| 34 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +94 | 11220 |
| 35 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | +94 | 26189 |
| 36 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +93 | 17517 |
| 37 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +93 | 14899 |
| 38 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +92 | 1657 |
| 39 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +91 | 31098 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +91 | 11275 |
| 41 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +90 | 26355 |
| 42 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +88 | 57554 |
| 43 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +85 | 48922 |
| 44 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +83 | 20578 |
| 45 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +79 | 25281 |
| 46 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +76 | 21685 |
| 47 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +76 | 24917 |
| 48 | [revfactory/harness](https://github.com/revfactory/harness) | +76 | 6548 |
| 49 | [openai/plugins](https://github.com/openai/plugins) | +75 | 2299 |
| 50 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +74 | 14120 |
| 51 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +73 | 26040 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +72 | 41379 |
| 53 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +72 | 30524 |
| 54 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +72 | 8555 |
| 55 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +71 | 13518 |
| 56 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +71 | 21916 |
| 57 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +70 | 33201 |
| 58 | [decolua/9router](https://github.com/decolua/9router) | +65 | 16929 |
| 59 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +65 | 3563 |
| 60 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +62 | 1989 |
| 61 | [withastro/flue](https://github.com/withastro/flue) | +62 | 4821 |
| 62 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +62 | 15815 |
| 63 | [multica-ai/multica](https://github.com/multica-ai/multica) | +60 | 35848 |
| 64 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +60 | 5038 |
| 65 | [baojie/shiji-kb](https://github.com/baojie/shiji-kb) | +58 | 1971 |
| 66 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +57 | 16568 |
| 67 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +57 | 37574 |
| 68 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +56 | 13332 |
| 69 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +54 | 36669 |
| 70 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +54 | 9611 |
| 71 | [blader/humanizer](https://github.com/blader/humanizer) | +54 | 22994 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +52 | 32505 |
| 73 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +52 | 31173 |
| 74 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +51 | 6525 |
| 75 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +50 | 19718 |
| 76 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +50 | 15388 |
| 77 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +50 | 3224 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +49 | 23326 |
| 79 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +48 | 29002 |
| 80 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +47 | 6623 |
| 81 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +46 | 12593 |
| 82 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +46 | 27741 |
| 83 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +45 | 3843 |
| 84 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +45 | 21761 |
| 85 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +45 | 56927 |
| 86 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +45 | 1924 |
| 87 | [Makisuo/maple](https://github.com/Makisuo/maple) | +44 | 1213 |
| 88 | [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | +44 | 1764 |
| 89 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +43 | 42383 |
| 90 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +43 | 16657 |
| 91 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +43 | 8481 |
| 92 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +43 | 24003 |
| 93 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +42 | 1295 |
| 94 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +42 | 20924 |
| 95 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +42 | 24676 |
| 96 | [openai/skills](https://github.com/openai/skills) | +41 | 21707 |
| 97 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +41 | 2630 |
| 98 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +41 | 2557 |
| 99 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +40 | 8330 |
| 100 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +39 | 869 |
| 101 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +39 | 16395 |
| 102 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +39 | 23124 |
| 103 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +37 | 27599 |
| 104 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +36 | 4979 |
| 105 | [browser-act/skills](https://github.com/browser-act/skills) | +36 | 2212 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +36 | 16001 |
| 107 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +34 | 35716 |
| 108 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +34 | 3338 |
| 109 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +33 | 24205 |
| 110 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +33 | 710 |
| 111 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +32 | 40093 |
| 112 | [browser-use/video-use](https://github.com/browser-use/video-use) | +32 | 9279 |
| 113 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +32 | 5755 |
| 114 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +31 | 29657 |
| 115 | [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | +31 | 1653 |
| 116 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +30 | 6380 |
| 117 | [jundot/omlx](https://github.com/jundot/omlx) | +30 | 16245 |
| 118 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +29 | 391 |
| 119 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +28 | 6381 |
| 120 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +28 | 7143 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4081 | 171299 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3929 | 121562 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3580 | 187288 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3008 | 44788 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2893 | 55161 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2752 | 60312 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2552 | 51199 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2277 | 31173 |
| 9 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2235 | 63659 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2209 | 95144 |
| 11 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1848 | 24917 |
| 12 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1737 | 30316 |
| 13 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1713 | 30524 |
| 14 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1596 | 28968 |
| 15 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +1534 | 37574 |
| 16 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1505 | 21916 |
| 17 | [github/spec-kit](https://github.com/github/spec-kit) | +1459 | 71722 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1420 | 49237 |
| 19 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1372 | 71987 |
| 20 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1321 | 88499 |
| 21 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1294 | 108354 |
| 22 | [antirez/ds4](https://github.com/antirez/ds4) | +1272 | 13242 |
| 23 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1257 | 63307 |
| 24 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1188 | 38372 |
| 25 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1099 | 57554 |
| 26 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1089 | 108496 |
| 27 | [decolua/9router](https://github.com/decolua/9router) | +1064 | 16929 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1050 | 60926 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1046 | 30590 |
| 30 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1004 | 58539 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +964 | 17929 |
| 32 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +959 | 29657 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +954 | 60135 |
| 34 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +927 | 34148 |
| 35 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +921 | 70161 |
| 36 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +901 | 62178 |
| 37 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +860 | 25281 |
| 38 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +846 | 16568 |
| 39 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +838 | 49621 |
| 40 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +783 | 19411 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +762 | 33201 |
| 42 | [floci-io/floci](https://github.com/floci-io/floci) | +743 | 13806 |
| 43 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +739 | 11375 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +731 | 35848 |
| 45 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +731 | 21761 |
| 46 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +692 | 18712 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +690 | 11220 |
| 48 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +680 | 8143 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +677 | 25713 |
| 50 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +644 | 6886 |
| 51 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +623 | 36216 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +615 | 21685 |
| 53 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +601 | 27599 |
| 54 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +598 | 34297 |
| 55 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +579 | 15815 |
| 56 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +574 | 36230 |
| 57 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +572 | 42383 |
| 58 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +561 | 4545 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +556 | 26355 |
| 60 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +556 | 18544 |
| 61 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +544 | 4125 |
| 62 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +518 | 19718 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +515 | 53566 |
| 64 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +514 | 14899 |
| 65 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +512 | 26040 |
| 66 | [santifer/career-ops](https://github.com/santifer/career-ops) | +509 | 50426 |
| 67 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +504 | 8703 |
| 68 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +499 | 19430 |
| 69 | [withcoral/coral](https://github.com/withcoral/coral) | +473 | 5141 |
| 70 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +470 | 11275 |
| 71 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +469 | 37724 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +465 | 41379 |
| 73 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +463 | 8843 |
| 74 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +463 | 5155 |
| 75 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +462 | 27727 |
| 76 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +455 | 7573 |
| 77 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +455 | 12436 |
| 78 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +454 | 6389 |
| 79 | [soxoj/maigret](https://github.com/soxoj/maigret) | +450 | 31363 |
| 80 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +448 | 14003 |
| 81 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +438 | 13332 |
| 82 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +434 | 7967 |
| 83 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +423 | 43124 |
| 84 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +418 | 9115 |
| 85 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +409 | 21507 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +409 | 23834 |
| 87 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +408 | 29574 |
| 88 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +403 | 11273 |
| 89 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +403 | 6623 |
| 90 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +401 | 41719 |
| 91 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +401 | 4915 |
| 92 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +389 | 14120 |
| 93 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +379 | 36669 |
| 94 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +377 | 8266 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +372 | 32505 |
| 96 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +366 | 5174 |
| 97 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +365 | 56927 |
| 98 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +362 | 23326 |
| 99 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +353 | 4979 |
| 100 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +337 | 29002 |
| 101 | [jundot/omlx](https://github.com/jundot/omlx) | +334 | 16245 |
| 102 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +333 | 24010 |
| 103 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +322 | 5004 |
| 104 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +322 | 3711 |
| 105 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +310 | 5314 |
| 106 | [roboflow/supervision](https://github.com/roboflow/supervision) | +301 | 36553 |
| 107 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +301 | 3843 |
| 108 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +297 | 12691 |
| 109 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +289 | 2436 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +288 | 35716 |
| 111 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +287 | 27943 |
| 112 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +283 | 7579 |
| 113 | [MinishLab/semble](https://github.com/MinishLab/semble) | +279 | 4942 |
| 114 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +267 | 16395 |
| 115 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +263 | 8180 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +252 | 16001 |
| 117 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +249 | 4290 |
| 118 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +249 | 3563 |
| 119 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +249 | 7140 |
| 120 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +247 | 24164 |
| 121 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +246 | 16131 |
| 122 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +239 | 45998 |
| 123 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +237 | 11675 |
| 124 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +234 | 2767 |
| 125 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +233 | 17523 |
| 126 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +232 | 40093 |
| 127 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +232 | 5830 |
| 128 | [openai/skills](https://github.com/openai/skills) | +229 | 21707 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +229 | 36799 |
| 130 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +222 | 9104 |
| 131 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +222 | 14521 |
| 132 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +216 | 3054 |
| 133 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +206 | 2790 |
| 134 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +205 | 6496 |
| 135 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +202 | 34178 |
| 136 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +200 | 5755 |
| 137 | [88lin/video_vip](https://github.com/88lin/video_vip) | +199 | 3786 |
| 138 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +198 | 4010 |
| 139 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +194 | 23124 |
| 140 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +193 | 20471 |
| 141 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +188 | 34190 |
| 142 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +187 | 26940 |
| 143 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +187 | 32773 |
| 144 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +186 | 24720 |
| 145 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +183 | 2753 |
| 146 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +183 | 2585 |
| 147 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +182 | 22903 |
| 148 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +180 | 5222 |
| 149 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +180 | 2421 |
| 150 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +175 | 18230 |
| 151 | [browser-use/video-use](https://github.com/browser-use/video-use) | +172 | 9279 |
| 152 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +171 | 34643 |
| 153 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +171 | 26718 |
| 154 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +170 | 3338 |
| 155 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6493 |
| 156 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +164 | 48922 |
| 157 | [AvenueSleuth/delta-exec](https://github.com/AvenueSleuth/delta-exec) | +163 | 0 |
| 158 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +159 | 24003 |
| 159 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +158 | 1925 |
| 160 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +155 | 5525 |
| 161 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +154 | 10520 |
| 162 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2390 |
| 163 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +149 | 7143 |
| 164 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +146 | 28088 |
| 165 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +146 | 7737 |
| 166 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +144 | 6380 |
| 167 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +144 | 7244 |
| 168 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +142 | 43877 |
| 169 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +142 | 4780 |
| 170 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +138 | 10890 |
| 171 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +137 | 37564 |
| 172 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +134 | 24205 |
| 173 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +133 | 2557 |
| 174 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +133 | 1812 |
| 175 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +131 | 4120 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +129 | 15359 |
| 177 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +128 | 29077 |
| 178 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +127 | 8481 |
| 179 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1995 |
| 180 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +125 | 6664 |
| 181 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +124 | 32872 |
| 182 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +121 | 36103 |
| 183 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +118 | 4457 |
| 184 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +118 | 4288 |
| 185 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +117 | 2762 |
| 186 | [playcanvas/engine](https://github.com/playcanvas/engine) | +117 | 15986 |
| 187 | [browserbase/skills](https://github.com/browserbase/skills) | +112 | 3533 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +111 | 27723 |
| 189 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +110 | 1519 |
| 190 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +109 | 17820 |
| 191 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +107 | 5049 |
| 192 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +104 | 1206 |
| 193 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +104 | 8539 |
| 194 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +102 | 12055 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +101 | 3957 |
| 196 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +101 | 5427 |
| 197 | [openai/plugins](https://github.com/openai/plugins) | +97 | 2299 |
| 198 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 800 |
| 199 | [usebruno/bruno](https://github.com/usebruno/bruno) | +92 | 41086 |
| 200 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +90 | 2437 |
| 201 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +88 | 39596 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +85 | 7339 |
| 203 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +82 | 23635 |
| 204 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +81 | 15756 |
| 205 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +81 | 1032 |
| 206 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +72 | 2247 |
| 207 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +69 | 10868 |
| 208 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +69 | 15123 |
| 209 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +67 | 8330 |
| 210 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1192 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +66 | 3479 |
| 212 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +66 | 2480 |
| 213 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +63 | 4974 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +61 | 40265 |
| 215 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +60 | 37313 |
| 216 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +59 | 1600 |
| 217 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +56 | 850 |
| 218 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +55 | 4906 |
| 219 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +55 | 10198 |
| 220 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +54 | 8177 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +54 | 35473 |
| 222 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +53 | 2050 |
| 223 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +52 | 12003 |
| 224 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +52 | 384 |
| 225 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 286 |
| 226 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +50 | 3637 |
| 227 | [sandeco/reversa](https://github.com/sandeco/reversa) | +46 | 1195 |
| 228 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +46 | 4294 |
| 229 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 869 |
| 230 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +45 | 372 |
| 231 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +44 | 492 |
| 232 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +44 | 8649 |
| 233 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +43 | 9379 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +43 | 2630 |
| 235 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +40 | 508 |
| 236 | [robinebers/openusage](https://github.com/robinebers/openusage) | +39 | 2801 |
| 237 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +38 | 1278 |
| 238 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +38 | 350 |
| 239 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +36 | 1786 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +36 | 13622 |
| 241 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +34 | 7804 |
| 242 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4242 |
| 243 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 292 |
| 244 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +33 | 1796 |
| 245 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +33 | 4362 |
| 246 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +33 | 2051 |
| 247 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 459 |
| 248 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 278 |
| 249 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +32 | 2105 |
| 250 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +31 | 4861 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +29 | 2445 |
| 252 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +29 | 361 |
| 253 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +28 | 1993 |
| 254 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +28 | 322 |
| 255 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +28 | 2524 |
| 256 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +28 | 3395 |
| 257 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +28 | 2345 |
| 258 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +27 | 722 |
| 259 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +27 | 1092 |
| 260 | [openmemind/memind](https://github.com/openmemind/memind) | +27 | 898 |
| 261 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +26 | 934 |
| 262 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +26 | 1889 |
| 263 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +26 | 1492 |
| 264 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +26 | 3389 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +26 | 2437 |
| 266 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 201 |
| 267 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +24 | 1052 |
| 268 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +24 | 273 |
| 269 | [is-a-dev/register](https://github.com/is-a-dev/register) | +23 | 10439 |
| 270 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +23 | 569 |
| 271 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +22 | 880 |
| 272 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +22 | 671 |
| 273 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +22 | 398 |
| 274 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 131 |
| 275 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +22 | 2386 |
| 276 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +22 | 2982 |
| 277 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +18 | 481 |
| 278 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +18 | 314 |
| 279 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +18 | 564 |
| 280 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +18 | 442 |
| 281 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +18 | 2661 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +17 | 2523 |
| 283 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +16 | 296 |
| 284 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +16 | 849 |
| 285 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +16 | 3255 |
| 286 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +15 | 1100 |
| 287 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +14 | 1581 |
| 288 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 520 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +12 | 1603 |
| 290 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +12 | 805 |
| 291 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +12 | 540 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +11 | 2059 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +11 | 218 |
| 294 | [quarkiverse/quarkus-flow](https://github.com/quarkiverse/quarkus-flow) | +11 | 94 |
| 295 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +10 | 2259 |
| 296 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +10 | 985 |
| 297 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +10 | 301 |
| 298 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +9 | 466 |
| 299 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 164 |
| 300 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 465 |
