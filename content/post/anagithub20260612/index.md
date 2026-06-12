---
title: "2026-06-12 GitHub增长趋势报告"
description: "1.container+105 2.headroom+38 3.agentsview+24 4.taste-skill+23 5.codegraph+23"
date: 2026-06-12T21:47:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-12 21:47:23

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
        'daily': {"categories": ["mindfold-ai/Trellis", "luongnv89/claude-howto", "tashfeenahmed/freellmapi", "masterking32/MasterDnsVPN", "steipete/agent-scripts", "Agents365-ai/drawio-skill", "alchaincyf/zhangxuefeng-skill", "Wei-Shaw/sub2api", "rohitg00/ai-engineering-from-scratch", "refactoringhq/tolaria", "rtk-ai/rtk", "mvanhorn/last30days-skill", "hugohe3/ppt-master", "maziyarpanahi/openmed", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "kenn-io/agentsview", "chopratejas/headroom", "apple/container"], "data": [9, 9, 10, 10, 10, 10, 12, 12, 12, 15, 16, 17, 17, 18, 21, 23, 23, 24, 38, 105]},
        'weekly': {"categories": ["pbakaus/impeccable", "Imbad0202/academic-research-skills", "refactoringhq/tolaria", "CopilotKit/CopilotKit", "OpenBMB/VoxCPM", "rohitg00/ai-engineering-from-scratch", "KunAgent/Kun", "santifer/career-ops", "apple/container", "lfnovo/open-notebook", "roboflow/supervision", "alibaba/open-code-review", "Panniantong/Agent-Reach", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "RyanCodrai/turbovec", "chopratejas/headroom", "Leonxlnx/taste-skill", "mvanhorn/last30days-skill", "pewdiepie-archdaemon/odysseus"], "data": [130, 132, 151, 152, 164, 165, 181, 182, 205, 213, 223, 249, 254, 266, 293, 363, 441, 474, 565, 821]},
        'monthly': {"categories": ["VoltAgent/awesome-design-md", "harry0703/MoneyPrinterTurbo", "github/spec-kit", "msitarzewski/agency-agents", "safishamsi/graphify", "rohitg00/agentmemory", "Leonxlnx/taste-skill", "CloakHQ/CloakBrowser", "ruvnet/RuView", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "farion1231/cc-switch", "affaan-m/ECC", "tinyhumansai/openhuman", "pewdiepie-archdaemon/odysseus", "NousResearch/hermes-agent", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [927, 955, 978, 984, 1047, 1181, 1191, 1307, 1362, 1461, 1630, 1648, 1987, 2116, 2357, 2701, 2853, 3065, 3074, 3313]}
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
| 1 | [apple/container](https://github.com/apple/container) | +105 | 34962 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +38 | 24527 |
| 3 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +24 | 2056 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +23 | 42319 |
| 5 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +23 | 48178 |
| 6 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +21 | 58083 |
| 7 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +18 | 3169 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +17 | 26983 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +17 | 40261 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +16 | 61901 |
| 11 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +15 | 15718 |
| 12 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 31669 |
| 13 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +12 | 27442 |
| 14 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +12 | 8193 |
| 15 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +10 | 2677 |
| 16 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +10 | 4810 |
| 17 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +10 | 5978 |
| 18 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +10 | 9925 |
| 19 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +9 | 37001 |
| 20 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +9 | 10174 |
| 21 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +9 | 30662 |
| 22 | [santifer/career-ops](https://github.com/santifer/career-ops) | +8 | 53186 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 19370 |
| 24 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +8 | 16878 |
| 25 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +8 | 31745 |
| 26 | [yukiyokotani/office-open-xml-viewer](https://github.com/yukiyokotani/office-open-xml-viewer) | +8 | 402 |
| 27 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +7 | 58760 |
| 28 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +7 | 30982 |
| 29 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +7 | 2603 |
| 30 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +6 | 26734 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +821 | 69280 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +565 | 40261 |
| 3 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +474 | 42320 |
| 4 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +441 | 24527 |
| 5 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +363 | 11262 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +293 | 48178 |
| 7 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +266 | 58083 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +254 | 26734 |
| 9 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +249 | 6442 |
| 10 | [roboflow/supervision](https://github.com/roboflow/supervision) | +223 | 36553 |
| 11 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +213 | 29490 |
| 12 | [apple/container](https://github.com/apple/container) | +205 | 34962 |
| 13 | [santifer/career-ops](https://github.com/santifer/career-ops) | +182 | 53186 |
| 14 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +181 | 3855 |
| 15 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +165 | 31669 |
| 16 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +164 | 28625 |
| 17 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +152 | 34868 |
| 18 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +151 | 15718 |
| 19 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +132 | 30662 |
| 20 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +130 | 37813 |
| 21 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +126 | 20926 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +119 | 27089 |
| 23 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +110 | 31098 |
| 24 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +108 | 30622 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +104 | 9925 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +103 | 61901 |
| 27 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +102 | 3975 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +101 | 19370 |
| 29 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +99 | 8805 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +96 | 26983 |
| 31 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +95 | 18485 |
| 32 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +95 | 1917 |
| 33 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +92 | 27442 |
| 34 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +87 | 3319 |
| 35 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +86 | 3007 |
| 36 | [openai/plugins](https://github.com/openai/plugins) | +84 | 2884 |
| 37 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +79 | 8255 |
| 38 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +78 | 22454 |
| 39 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +77 | 58760 |
| 40 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +75 | 21119 |
| 41 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +74 | 37001 |
| 42 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +74 | 11164 |
| 43 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +72 | 12097 |
| 44 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +71 | 26471 |
| 45 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +70 | 49290 |
| 46 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +69 | 15509 |
| 47 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +68 | 2145 |
| 48 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +63 | 22531 |
| 49 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +63 | 9047 |
| 50 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +62 | 11990 |
| 51 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +60 | 11952 |
| 52 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +60 | 30982 |
| 53 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +60 | 25736 |
| 54 | [blader/humanizer](https://github.com/blader/humanizer) | +59 | 23913 |
| 55 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +58 | 16878 |
| 56 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +58 | 1408 |
| 57 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +58 | 13600 |
| 58 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +57 | 14316 |
| 59 | [revfactory/harness](https://github.com/revfactory/harness) | +57 | 6892 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +54 | 57558 |
| 61 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +53 | 42321 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +53 | 37337 |
| 63 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +53 | 15862 |
| 64 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +52 | 34096 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +52 | 33059 |
| 66 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +52 | 1968 |
| 67 | [soxoj/maigret](https://github.com/soxoj/maigret) | +52 | 32948 |
| 68 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +51 | 20423 |
| 69 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +50 | 3169 |
| 70 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +46 | 9950 |
| 71 | [multica-ai/multica](https://github.com/multica-ai/multica) | +45 | 36411 |
| 72 | [decolua/9router](https://github.com/decolua/9router) | +45 | 17361 |
| 73 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +44 | 2250 |
| 74 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +43 | 3525 |
| 75 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +43 | 4376 |
| 76 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +43 | 5502 |
| 77 | [Ataraxy-Labs/sem](https://github.com/Ataraxy-Labs/sem) | +43 | 2730 |
| 78 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +42 | 935 |
| 79 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +41 | 29386 |
| 80 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +41 | 8361 |
| 81 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +41 | 4750 |
| 82 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +41 | 4048 |
| 83 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +40 | 3061 |
| 84 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +40 | 24088 |
| 85 | [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | +40 | 2131 |
| 86 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +39 | 38155 |
| 87 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +38 | 2705 |
| 88 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +38 | 16569 |
| 89 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +37 | 2300 |
| 90 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +37 | 6926 |
| 91 | [openai/skills](https://github.com/openai/skills) | +37 | 22032 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +37 | 42838 |
| 93 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +37 | 3076 |
| 94 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +36 | 5978 |
| 95 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +36 | 11283 |
| 96 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +35 | 21506 |
| 97 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +34 | 31745 |
| 98 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +34 | 2851 |
| 99 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +34 | 22130 |
| 100 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +33 | 6880 |
| 101 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +33 | 14608 |
| 102 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +32 | 5291 |
| 103 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +32 | 28074 |
| 104 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +31 | 2056 |
| 105 | [browser-act/skills](https://github.com/browser-act/skills) | +31 | 2398 |
| 106 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 475 |
| 107 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +30 | 2448 |
| 108 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +30 | 24553 |
| 109 | [francescopace/espectre](https://github.com/francescopace/espectre) | +29 | 8564 |
| 110 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +29 | 40487 |
| 111 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +29 | 8766 |
| 112 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +28 | 30000 |
| 113 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +28 | 3727 |
| 114 | [browser-use/video-use](https://github.com/browser-use/video-use) | +27 | 9569 |
| 115 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +26 | 2603 |
| 116 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +26 | 2977 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +26 | 16223 |
| 118 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +26 | 786 |
| 119 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +25 | 6625 |
| 120 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +24 | 7897 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3313 | 174152 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3074 | 126872 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3065 | 48178 |
| 4 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2853 | 58083 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2701 | 191919 |
| 6 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2357 | 69280 |
| 7 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2116 | 31746 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +1987 | 51199 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1648 | 99347 |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1630 | 31669 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1461 | 30662 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1362 | 73459 |
| 13 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1307 | 25736 |
| 14 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1191 | 42321 |
| 15 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1181 | 22531 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1047 | 66261 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +984 | 112330 |
| 18 | [github/spec-kit](https://github.com/github/spec-kit) | +978 | 71722 |
| 19 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +955 | 49621 |
| 20 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +927 | 89788 |
| 21 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +917 | 30000 |
| 22 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +889 | 38155 |
| 23 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +844 | 24527 |
| 24 | [earendil-works/pi](https://github.com/earendil-works/pi) | +806 | 62062 |
| 25 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +790 | 56682 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +758 | 63284 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +755 | 61901 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +754 | 19370 |
| 29 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +740 | 11563 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +731 | 34148 |
| 31 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +726 | 40261 |
| 32 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +682 | 71932 |
| 33 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +682 | 8240 |
| 34 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +675 | 26983 |
| 35 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +664 | 30982 |
| 36 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +640 | 59145 |
| 37 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +588 | 34096 |
| 38 | [decolua/9router](https://github.com/decolua/9router) | +587 | 17361 |
| 39 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +584 | 11262 |
| 40 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +582 | 58760 |
| 41 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +578 | 20926 |
| 42 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +577 | 28074 |
| 43 | [multica-ai/multica](https://github.com/multica-ai/multica) | +561 | 36411 |
| 44 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +538 | 27089 |
| 45 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +536 | 42838 |
| 46 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +523 | 15509 |
| 47 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +523 | 20423 |
| 48 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +495 | 9925 |
| 49 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +488 | 16828 |
| 50 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +483 | 37813 |
| 51 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +475 | 11990 |
| 52 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +468 | 5297 |
| 53 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +467 | 22454 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +463 | 12097 |
| 55 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +461 | 6666 |
| 56 | [santifer/career-ops](https://github.com/santifer/career-ops) | +453 | 53186 |
| 57 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +445 | 22130 |
| 58 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +444 | 8324 |
| 59 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +444 | 19017 |
| 60 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +425 | 27442 |
| 61 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +423 | 28625 |
| 62 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +420 | 26471 |
| 63 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +420 | 16878 |
| 64 | [floci-io/floci](https://github.com/floci-io/floci) | +415 | 14024 |
| 65 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +408 | 6880 |
| 66 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +403 | 5006 |
| 67 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +396 | 9823 |
| 68 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +395 | 4564 |
| 69 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +386 | 8805 |
| 70 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +381 | 21911 |
| 71 | [antirez/ds4](https://github.com/antirez/ds4) | +379 | 13522 |
| 72 | [withcoral/coral](https://github.com/withcoral/coral) | +379 | 5137 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +374 | 42321 |
| 74 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +367 | 5212 |
| 75 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +364 | 26734 |
| 76 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +364 | 14316 |
| 77 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +362 | 5291 |
| 78 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +352 | 13600 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +351 | 38525 |
| 80 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8255 |
| 81 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +342 | 6442 |
| 82 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +334 | 29815 |
| 83 | [roboflow/supervision](https://github.com/roboflow/supervision) | +324 | 36553 |
| 84 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +319 | 5113 |
| 85 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +316 | 7038 |
| 86 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +308 | 29490 |
| 87 | [blader/humanizer](https://github.com/blader/humanizer) | +301 | 23913 |
| 88 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +301 | 24191 |
| 89 | [soxoj/maigret](https://github.com/soxoj/maigret) | +296 | 32948 |
| 90 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +294 | 43471 |
| 91 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +294 | 42026 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +293 | 33059 |
| 93 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +286 | 29386 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +285 | 37337 |
| 95 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +281 | 15718 |
| 96 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +280 | 57558 |
| 97 | [MinishLab/semble](https://github.com/MinishLab/semble) | +279 | 5110 |
| 98 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +274 | 24088 |
| 99 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +273 | 18485 |
| 100 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +265 | 9047 |
| 101 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +264 | 8216 |
| 102 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +250 | 4372 |
| 103 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +245 | 11952 |
| 104 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +239 | 37001 |
| 105 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +239 | 2937 |
| 106 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +237 | 19631 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +236 | 4048 |
| 108 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +230 | 3855 |
| 109 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +230 | 3832 |
| 110 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +225 | 14608 |
| 111 | [apple/container](https://github.com/apple/container) | +222 | 34962 |
| 112 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +222 | 3312 |
| 113 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +215 | 4376 |
| 114 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9195 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +213 | 16299 |
| 116 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +206 | 6201 |
| 117 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4038 |
| 118 | [88lin/video_vip](https://github.com/88lin/video_vip) | +199 | 3917 |
| 119 | [openai/skills](https://github.com/openai/skills) | +197 | 22032 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +195 | 16223 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +187 | 17926 |
| 122 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +187 | 7252 |
| 123 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +183 | 2596 |
| 124 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +182 | 11989 |
| 125 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +181 | 5380 |
| 126 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +179 | 16569 |
| 127 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +179 | 36799 |
| 128 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +178 | 46296 |
| 129 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +175 | 3727 |
| 130 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +172 | 5986 |
| 131 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +170 | 11164 |
| 132 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +170 | 3076 |
| 133 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +169 | 7897 |
| 134 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6547 |
| 135 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +166 | 40487 |
| 136 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +158 | 34553 |
| 137 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +158 | 34541 |
| 138 | [jundot/omlx](https://github.com/jundot/omlx) | +156 | 16497 |
| 139 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +155 | 1981 |
| 140 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +153 | 14716 |
| 141 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +153 | 23351 |
| 142 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2415 |
| 143 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +150 | 24221 |
| 144 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +150 | 27134 |
| 145 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +145 | 49290 |
| 146 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +145 | 25077 |
| 147 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +143 | 2300 |
| 148 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +143 | 20806 |
| 149 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +140 | 2977 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +136 | 34919 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +135 | 23105 |
| 152 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +135 | 2999 |
| 153 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +135 | 24470 |
| 154 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +131 | 7355 |
| 155 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +131 | 2560 |
| 156 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +128 | 18439 |
| 157 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +127 | 6660 |
| 158 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1990 |
| 159 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2059 |
| 160 | [browser-use/video-use](https://github.com/browser-use/video-use) | +125 | 9569 |
| 161 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3007 |
| 162 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +122 | 4254 |
| 163 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +119 | 1745 |
| 164 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +118 | 6625 |
| 165 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +117 | 26947 |
| 166 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +116 | 6831 |
| 167 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +114 | 11085 |
| 168 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +114 | 4810 |
| 169 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +113 | 24553 |
| 170 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +111 | 8766 |
| 171 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1639 |
| 172 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +108 | 25566 |
| 173 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +108 | 4750 |
| 174 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +108 | 36103 |
| 175 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +107 | 44118 |
| 176 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +107 | 32872 |
| 177 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +105 | 5672 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +104 | 7355 |
| 179 | [openai/plugins](https://github.com/openai/plugins) | +103 | 2884 |
| 180 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +102 | 37564 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +101 | 15669 |
| 182 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +97 | 12076 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +96 | 29278 |
| 184 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +94 | 4848 |
| 185 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 803 |
| 186 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +94 | 18009 |
| 187 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +91 | 28314 |
| 188 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +90 | 6627 |
| 189 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +88 | 27853 |
| 190 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +87 | 4208 |
| 191 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +87 | 1264 |
| 192 | [usebruno/bruno](https://github.com/usebruno/bruno) | +86 | 41086 |
| 193 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +84 | 1158 |
| 194 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +76 | 2777 |
| 195 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +72 | 2341 |
| 196 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +71 | 2712 |
| 197 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +68 | 1224 |
| 198 | [eze-is/web-access](https://github.com/eze-is/web-access) | +64 | 7513 |
| 199 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +61 | 5146 |
| 200 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +60 | 8541 |
| 201 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +59 | 7883 |
| 202 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +58 | 5554 |
| 203 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +58 | 5116 |
| 204 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +55 | 3577 |
| 205 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +55 | 10998 |
| 206 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +50 | 4984 |
| 207 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +49 | 1634 |
| 208 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +49 | 2312 |
| 209 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +48 | 2805 |
| 210 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 935 |
| 211 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +46 | 3765 |
| 212 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +46 | 855 |
| 213 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +43 | 2702 |
| 214 | [sandeco/reversa](https://github.com/sandeco/reversa) | +41 | 1209 |
| 215 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +40 | 2454 |
| 216 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +37 | 1339 |
| 217 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +36 | 2138 |
| 218 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +36 | 9395 |
| 219 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +35 | 4263 |
| 220 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +35 | 12067 |
| 221 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +35 | 8702 |
| 222 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +35 | 286 |
| 223 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +34 | 7872 |
| 224 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +34 | 4377 |
| 225 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +34 | 10225 |
| 226 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +34 | 545 |
| 227 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 294 |
| 228 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 522 |
| 229 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +31 | 8221 |
| 230 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +31 | 350 |
| 231 | [browserbase/skills](https://github.com/browserbase/skills) | +31 | 3550 |
| 232 | [robinebers/openusage](https://github.com/robinebers/openusage) | +30 | 2855 |
| 233 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +30 | 376 |
| 234 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +29 | 1854 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +29 | 13658 |
| 236 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +28 | 2140 |
| 237 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +28 | 2491 |
| 238 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +27 | 4403 |
| 239 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +25 | 822 |
| 240 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +25 | 1875 |
| 241 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 202 |
| 242 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +23 | 1063 |
| 243 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +22 | 2033 |
| 244 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 123 |
| 245 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +21 | 713 |
| 246 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +21 | 4974 |
| 247 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +20 | 375 |
| 248 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +20 | 1946 |
| 249 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +20 | 2623 |
| 250 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 577 |
| 251 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +20 | 1532 |
| 252 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +20 | 3451 |
| 253 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +20 | 307 |
| 254 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +20 | 3419 |
| 255 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +19 | 513 |
| 256 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13560 |
| 257 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +19 | 398 |
| 258 | [openmemind/memind](https://github.com/openmemind/memind) | +19 | 899 |
| 259 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +18 | 349 |
| 260 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +18 | 2408 |
| 261 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +17 | 637 |
| 262 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +17 | 417 |
| 263 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +17 | 944 |
| 264 | [WJZ-P/sona](https://github.com/WJZ-P/sona) | +16 | 646 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +16 | 2480 |
| 266 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +16 | 461 |
| 267 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +15 | 695 |
| 268 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +15 | 638 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +15 | 2438 |
| 270 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +15 | 2994 |
| 271 | [is-a-dev/register](https://github.com/is-a-dev/register) | +14 | 10474 |
| 272 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 311 |
| 273 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +14 | 1317 |
| 274 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 539 |
| 275 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +13 | 2548 |
| 276 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +13 | 599 |
| 277 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +13 | 8554 |
| 278 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +13 | 354 |
| 279 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 253 |
| 280 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 218 |
| 281 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +11 | 1128 |
| 282 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 111 |
| 283 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 109 |
| 284 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +10 | 865 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +10 | 1609 |
| 286 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1606 |
| 287 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +10 | 387 |
| 288 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +10 | 3256 |
| 289 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +9 | 2661 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +8 | 2090 |
| 291 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +8 | 2282 |
| 292 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +8 | 479 |
| 293 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +8 | 1002 |
| 294 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 232 |
| 295 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +7 | 5178 |
| 296 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 65 |
| 297 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +7 | 128 |
| 298 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +7 | 241 |
| 299 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +7 | 1041 |
| 300 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +7 | 815 |
