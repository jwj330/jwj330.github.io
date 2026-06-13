---
title: "2026-06-13 GitHub增长趋势报告"
description: "1.headroom+63 2.container+63 3.last30days-skill+44 4.taste-skill+34 5.Agent-Reach+33"
date: 2026-06-13T21:18:32+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-13 21:18:32

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
        'daily': {"categories": ["datawhalechina/hello-agents", "tinyhumansai/openhuman", "coreyhaines31/marketingskills", "Agents365-ai/drawio-skill", "pbakaus/impeccable", "QuantFunc/ComfyUI-QuantFunc", "Imbad0202/academic-research-skills", "masterking32/MasterDnsVPN", "rtk-ai/rtk", "zhukunpenglinyutong/desktop-cc-gui", "santifer/career-ops", "Lum1104/Understand-Anything", "refactoringhq/tolaria", "lfnovo/open-notebook", "colbymchenry/codegraph", "Panniantong/Agent-Reach", "Leonxlnx/taste-skill", "mvanhorn/last30days-skill", "apple/container", "chopratejas/headroom"], "data": [10, 11, 11, 11, 12, 12, 12, 13, 13, 16, 17, 18, 22, 26, 31, 33, 34, 44, 63, 63]},
        'weekly': {"categories": ["google/skills", "CopilotKit/CopilotKit", "pbakaus/impeccable", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "refactoringhq/tolaria", "KunAgent/Kun", "lfnovo/open-notebook", "santifer/career-ops", "alibaba/open-code-review", "roboflow/supervision", "Lum1104/Understand-Anything", "Panniantong/Agent-Reach", "colbymchenry/codegraph", "apple/container", "RyanCodrai/turbovec", "Leonxlnx/taste-skill", "chopratejas/headroom", "mvanhorn/last30days-skill", "pewdiepie-archdaemon/odysseus"], "data": [114, 117, 118, 121, 130, 162, 182, 183, 190, 206, 224, 235, 244, 251, 267, 352, 408, 437, 582, 632]},
        'monthly': {"categories": ["anthropics/claude-plugins-official", "github/spec-kit", "harry0703/MoneyPrinterTurbo", "msitarzewski/agency-agents", "safishamsi/graphify", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "Leonxlnx/taste-skill", "ruvnet/RuView", "Imbad0202/academic-research-skills", "farion1231/cc-switch", "rohitg00/ai-engineering-from-scratch", "affaan-m/ECC", "tinyhumansai/openhuman", "pewdiepie-archdaemon/odysseus", "NousResearch/hermes-agent", "Lum1104/Understand-Anything", "mattpocock/skills", "colbymchenry/codegraph", "forrestchang/andrej-karpathy-skills"], "data": [915, 923, 975, 1005, 1028, 1101, 1203, 1212, 1326, 1462, 1610, 1630, 1959, 2045, 2391, 2638, 2861, 2917, 3093, 3256]}
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
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +63 | 26055 |
| 2 | [apple/container](https://github.com/apple/container) | +63 | 36193 |
| 3 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +44 | 41156 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +34 | 43027 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +33 | 27328 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +31 | 48567 |
| 7 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +26 | 30075 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +22 | 16075 |
| 9 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +18 | 58482 |
| 10 | [santifer/career-ops](https://github.com/santifer/career-ops) | +17 | 53511 |
| 11 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +16 | 3042 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +13 | 62115 |
| 13 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +13 | 6175 |
| 14 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +12 | 31003 |
| 15 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +12 | 611 |
| 16 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +12 | 38035 |
| 17 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +11 | 2999 |
| 18 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +11 | 33173 |
| 19 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +11 | 31917 |
| 20 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +10 | 58919 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +10 | 10091 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 27226 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +10 | 27335 |
| 24 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +8 | 4232 |
| 25 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +8 | 11383 |
| 26 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +8 | 6190 |
| 27 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | +8 | 6900 |
| 28 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +8 | 10303 |
| 29 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +8 | 22673 |
| 30 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +7 | 28850 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +632 | 70060 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +582 | 41156 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +437 | 26055 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +408 | 43027 |
| 5 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +352 | 11383 |
| 6 | [apple/container](https://github.com/apple/container) | +267 | 36193 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +251 | 48568 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +244 | 27328 |
| 9 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +235 | 58483 |
| 10 | [roboflow/supervision](https://github.com/roboflow/supervision) | +224 | 36553 |
| 11 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +206 | 6620 |
| 12 | [santifer/career-ops](https://github.com/santifer/career-ops) | +190 | 53511 |
| 13 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +183 | 30075 |
| 14 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +182 | 4002 |
| 15 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +162 | 16075 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +130 | 31904 |
| 17 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +121 | 31003 |
| 18 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +118 | 38035 |
| 19 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +117 | 34989 |
| 20 | [google/skills](https://github.com/google/skills) | +114 | 13624 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +113 | 27335 |
| 22 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +111 | 28851 |
| 23 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +107 | 20998 |
| 24 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +106 | 31098 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +105 | 62115 |
| 26 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +101 | 10091 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +93 | 27226 |
| 28 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +93 | 30706 |
| 29 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +89 | 18576 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +78 | 19623 |
| 31 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +78 | 1939 |
| 32 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +77 | 27577 |
| 33 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +75 | 37076 |
| 34 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +75 | 12224 |
| 35 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +74 | 4232 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +73 | 58919 |
| 37 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +71 | 22593 |
| 38 | [openai/plugins](https://github.com/openai/plugins) | +70 | 2962 |
| 39 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +68 | 2159 |
| 40 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +67 | 21182 |
| 41 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +63 | 8869 |
| 42 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +62 | 11249 |
| 43 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +60 | 22673 |
| 44 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +60 | 3333 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +58 | 33173 |
| 46 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +58 | 1420 |
| 47 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +57 | 2051 |
| 48 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +57 | 3007 |
| 49 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +57 | 8256 |
| 50 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +57 | 26565 |
| 51 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +55 | 15605 |
| 52 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +54 | 3379 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +54 | 34275 |
| 54 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +54 | 49316 |
| 55 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +54 | 6016 |
| 56 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +53 | 12048 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +52 | 24028 |
| 58 | [revfactory/harness](https://github.com/revfactory/harness) | +52 | 6934 |
| 59 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +52 | 15895 |
| 60 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +51 | 12040 |
| 61 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +51 | 17009 |
| 62 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +51 | 14364 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +50 | 20539 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +50 | 37419 |
| 65 | [soxoj/maigret](https://github.com/soxoj/maigret) | +50 | 32997 |
| 66 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +49 | 25912 |
| 67 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +48 | 13630 |
| 68 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +47 | 6175 |
| 69 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +45 | 42404 |
| 70 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +45 | 9108 |
| 71 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +44 | 57627 |
| 72 | [Ataraxy-Labs/sem](https://github.com/Ataraxy-Labs/sem) | +44 | 2752 |
| 73 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +43 | 31030 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +43 | 24190 |
| 75 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +42 | 3113 |
| 76 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +42 | 1043 |
| 77 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +41 | 10004 |
| 78 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +41 | 2735 |
| 79 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +40 | 31917 |
| 80 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +40 | 3592 |
| 81 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +39 | 29603 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +38 | 36475 |
| 83 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +38 | 8438 |
| 84 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +38 | 4426 |
| 85 | [openai/skills](https://github.com/openai/skills) | +38 | 22098 |
| 86 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +37 | 4808 |
| 87 | [decolua/9router](https://github.com/decolua/9router) | +37 | 17432 |
| 88 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +36 | 2881 |
| 89 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +36 | 2556 |
| 90 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +35 | 2802 |
| 91 | [yukiyokotani/office-open-xml-viewer](https://github.com/yukiyokotani/office-open-xml-viewer) | +35 | 422 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +35 | 42945 |
| 93 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +35 | 16599 |
| 94 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +34 | 38240 |
| 95 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +34 | 2352 |
| 96 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +33 | 2999 |
| 97 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +33 | 2313 |
| 98 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +33 | 22227 |
| 99 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +33 | 4081 |
| 100 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +32 | 2311 |
| 101 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +32 | 11362 |
| 102 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +32 | 40618 |
| 103 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +31 | 12322 |
| 104 | [browser-act/skills](https://github.com/browser-act/skills) | +31 | 2458 |
| 105 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +30 | 10303 |
| 106 | [francescopace/espectre](https://github.com/francescopace/espectre) | +30 | 8581 |
| 107 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +29 | 22256 |
| 108 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +29 | 611 |
| 109 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +29 | 3127 |
| 110 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +28 | 28133 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +28 | 14678 |
| 112 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +27 | 24577 |
| 113 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +26 | 24428 |
| 114 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +24 | 6930 |
| 115 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +24 | 7959 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +23 | 6190 |
| 117 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +23 | 2665 |
| 118 | [pat-jj/harness-1](https://github.com/pat-jj/harness-1) | +23 | 597 |
| 119 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +23 | 3797 |
| 120 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +22 | 25609 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3256 | 174727 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3093 | 48568 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2917 | 127736 |
| 4 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2861 | 58483 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2638 | 192698 |
| 6 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2391 | 70060 |
| 7 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2045 | 31917 |
| 8 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +1959 | 51199 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1630 | 31904 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1610 | 100006 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1462 | 31003 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1326 | 73636 |
| 13 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1212 | 43027 |
| 14 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1203 | 25912 |
| 15 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1101 | 22673 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1028 | 66677 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1005 | 112849 |
| 18 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +975 | 49621 |
| 19 | [github/spec-kit](https://github.com/github/spec-kit) | +923 | 71722 |
| 20 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +915 | 30053 |
| 21 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +907 | 26055 |
| 22 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +810 | 58208 |
| 23 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +808 | 38240 |
| 24 | [earendil-works/pi](https://github.com/earendil-works/pi) | +783 | 62306 |
| 25 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +767 | 41156 |
| 26 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +755 | 63469 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +739 | 19623 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +730 | 62115 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +714 | 34148 |
| 30 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +680 | 11718 |
| 31 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +662 | 72151 |
| 32 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +651 | 27226 |
| 33 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +620 | 8260 |
| 34 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +614 | 31030 |
| 35 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +608 | 59298 |
| 36 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +592 | 11383 |
| 37 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +580 | 34276 |
| 38 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +576 | 28133 |
| 39 | [decolua/9router](https://github.com/decolua/9router) | +562 | 17432 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +549 | 36475 |
| 41 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +545 | 58919 |
| 42 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +541 | 20998 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +535 | 27335 |
| 44 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +532 | 42945 |
| 45 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +526 | 20539 |
| 46 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +524 | 15605 |
| 47 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +505 | 10091 |
| 48 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +486 | 16865 |
| 49 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +484 | 38035 |
| 50 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +472 | 5502 |
| 51 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +470 | 12224 |
| 52 | [santifer/career-ops](https://github.com/santifer/career-ops) | +464 | 53511 |
| 53 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +462 | 6701 |
| 54 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +456 | 22593 |
| 55 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +445 | 8404 |
| 56 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +440 | 19127 |
| 57 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +437 | 22227 |
| 58 | [google/skills](https://github.com/google/skills) | +432 | 13624 |
| 59 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +422 | 26565 |
| 60 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +413 | 12048 |
| 61 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +409 | 6930 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +408 | 27577 |
| 63 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +406 | 28851 |
| 64 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +404 | 5028 |
| 65 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +395 | 9934 |
| 66 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +395 | 4568 |
| 67 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +393 | 17009 |
| 68 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +389 | 27328 |
| 69 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +389 | 8869 |
| 70 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +380 | 21965 |
| 71 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +380 | 4425 |
| 72 | [withcoral/coral](https://github.com/withcoral/coral) | +379 | 5136 |
| 73 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +368 | 5220 |
| 74 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +363 | 14364 |
| 75 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +362 | 42404 |
| 76 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +360 | 5358 |
| 77 | [floci-io/floci](https://github.com/floci-io/floci) | +356 | 14045 |
| 78 | [antirez/ds4](https://github.com/antirez/ds4) | +350 | 13617 |
| 79 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8256 |
| 80 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +343 | 6620 |
| 81 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +338 | 13630 |
| 82 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +336 | 38653 |
| 83 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +335 | 29914 |
| 84 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +333 | 30075 |
| 85 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +319 | 5139 |
| 86 | [roboflow/supervision](https://github.com/roboflow/supervision) | +318 | 36553 |
| 87 | [blader/humanizer](https://github.com/blader/humanizer) | +298 | 24028 |
| 88 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +295 | 16075 |
| 89 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +295 | 43530 |
| 90 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +295 | 7067 |
| 91 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +295 | 24261 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +293 | 33173 |
| 93 | [apple/container](https://github.com/apple/container) | +285 | 36193 |
| 94 | [soxoj/maigret](https://github.com/soxoj/maigret) | +284 | 32997 |
| 95 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +282 | 42065 |
| 96 | [MinishLab/semble](https://github.com/MinishLab/semble) | +279 | 5133 |
| 97 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +276 | 37419 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +276 | 29603 |
| 99 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +270 | 57627 |
| 100 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +268 | 18576 |
| 101 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +268 | 24190 |
| 102 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +266 | 9108 |
| 103 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +264 | 8228 |
| 104 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +251 | 4378 |
| 105 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 2951 |
| 106 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +240 | 12040 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +237 | 4081 |
| 108 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +234 | 4002 |
| 109 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +231 | 37076 |
| 110 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +230 | 3859 |
| 111 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3340 |
| 112 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9218 |
| 113 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +212 | 14678 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +208 | 16336 |
| 115 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +206 | 6257 |
| 116 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +205 | 4426 |
| 117 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4045 |
| 118 | [88lin/video_vip](https://github.com/88lin/video_vip) | +201 | 3938 |
| 119 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +200 | 19671 |
| 120 | [openai/skills](https://github.com/openai/skills) | +195 | 22098 |
| 121 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +192 | 16272 |
| 122 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +182 | 7282 |
| 123 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +181 | 5404 |
| 124 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +180 | 17987 |
| 125 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +177 | 3797 |
| 126 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +176 | 11249 |
| 127 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +176 | 16599 |
| 128 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +175 | 46358 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +172 | 36799 |
| 130 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +171 | 6190 |
| 131 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +170 | 12026 |
| 132 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +169 | 3127 |
| 133 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6555 |
| 134 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +164 | 7959 |
| 135 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +163 | 40618 |
| 136 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +160 | 34646 |
| 137 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +158 | 34593 |
| 138 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 24428 |
| 139 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +155 | 1988 |
| 140 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2427 |
| 141 | [jundot/omlx](https://github.com/jundot/omlx) | +150 | 16555 |
| 142 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +148 | 23406 |
| 143 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +146 | 14769 |
| 144 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +145 | 27165 |
| 145 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +144 | 49316 |
| 146 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +143 | 2352 |
| 147 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +140 | 3027 |
| 148 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +140 | 25112 |
| 149 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +139 | 34967 |
| 150 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +137 | 20888 |
| 151 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +133 | 23234 |
| 152 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +132 | 3083 |
| 153 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +132 | 24529 |
| 154 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +128 | 18467 |
| 155 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +127 | 6698 |
| 156 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1989 |
| 157 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2059 |
| 158 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +125 | 7388 |
| 159 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3007 |
| 160 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +122 | 4266 |
| 161 | [browser-use/video-use](https://github.com/browser-use/video-use) | +121 | 9606 |
| 162 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +116 | 6658 |
| 163 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +115 | 6890 |
| 164 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +115 | 26990 |
| 165 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +113 | 2580 |
| 166 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +112 | 11134 |
| 167 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +109 | 8814 |
| 168 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1647 |
| 169 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +107 | 25609 |
| 170 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +107 | 4808 |
| 171 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +107 | 32872 |
| 172 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +106 | 24577 |
| 173 | [openai/plugins](https://github.com/openai/plugins) | +105 | 2962 |
| 174 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +104 | 44158 |
| 175 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +104 | 36103 |
| 176 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +102 | 7399 |
| 177 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +102 | 2325 |
| 178 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +102 | 5686 |
| 179 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +100 | 37564 |
| 180 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +99 | 15715 |
| 181 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +96 | 12084 |
| 182 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +95 | 4858 |
| 183 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 803 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +94 | 29318 |
| 185 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +92 | 18075 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +87 | 27890 |
| 187 | [usebruno/bruno](https://github.com/usebruno/bruno) | +86 | 41086 |
| 188 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +85 | 28366 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +85 | 4254 |
| 190 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +84 | 1264 |
| 191 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +84 | 1159 |
| 192 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +78 | 3592 |
| 193 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +76 | 2782 |
| 194 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +73 | 2400 |
| 195 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +70 | 2794 |
| 196 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +68 | 1228 |
| 197 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +61 | 8568 |
| 198 | [eze-is/web-access](https://github.com/eze-is/web-access) | +59 | 7546 |
| 199 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +58 | 5165 |
| 200 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +57 | 7930 |
| 201 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +57 | 5156 |
| 202 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +54 | 3603 |
| 203 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +52 | 11020 |
| 204 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +51 | 5570 |
| 205 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +49 | 5000 |
| 206 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +48 | 1640 |
| 207 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +48 | 2321 |
| 208 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 1043 |
| 209 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +46 | 855 |
| 210 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +45 | 2808 |
| 211 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +45 | 3779 |
| 212 | [sandeco/reversa](https://github.com/sandeco/reversa) | +41 | 1214 |
| 213 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +41 | 2707 |
| 214 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +37 | 7889 |
| 215 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +37 | 9400 |
| 216 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1345 |
| 217 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +35 | 4264 |
| 218 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +35 | 12081 |
| 219 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +35 | 8709 |
| 220 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +35 | 2456 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +34 | 2150 |
| 222 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +34 | 537 |
| 223 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 294 |
| 224 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +33 | 560 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +32 | 4390 |
| 226 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +31 | 10234 |
| 227 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +31 | 353 |
| 228 | [browserbase/skills](https://github.com/browserbase/skills) | +31 | 3550 |
| 229 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +30 | 1866 |
| 230 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +30 | 8222 |
| 231 | [robinebers/openusage](https://github.com/robinebers/openusage) | +29 | 2862 |
| 232 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +29 | 286 |
| 233 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +28 | 13665 |
| 234 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +28 | 2512 |
| 235 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +27 | 4408 |
| 236 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +26 | 2139 |
| 237 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +25 | 828 |
| 238 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +25 | 1885 |
| 239 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +25 | 376 |
| 240 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 723 |
| 241 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 202 |
| 242 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +23 | 1068 |
| 243 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +22 | 5019 |
| 244 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 100 |
| 245 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +21 | 2041 |
| 246 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +20 | 383 |
| 247 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 579 |
| 248 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +19 | 516 |
| 249 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +19 | 1952 |
| 250 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +19 | 2632 |
| 251 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13571 |
| 252 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +19 | 398 |
| 253 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +19 | 3455 |
| 254 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +19 | 3425 |
| 255 | [openmemind/memind](https://github.com/openmemind/memind) | +19 | 899 |
| 256 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +18 | 350 |
| 257 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +18 | 647 |
| 258 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +18 | 1543 |
| 259 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +18 | 2417 |
| 260 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +18 | 310 |
| 261 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +16 | 428 |
| 262 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +16 | 948 |
| 263 | [WJZ-P/sona](https://github.com/WJZ-P/sona) | +16 | 647 |
| 264 | [steven-jianhao-li/zotero-AI-Butler](https://github.com/steven-jianhao-li/zotero-AI-Butler) | +16 | 1434 |
| 265 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +16 | 2995 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +16 | 2491 |
| 267 | [is-a-dev/register](https://github.com/is-a-dev/register) | +15 | 10481 |
| 268 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +15 | 646 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +15 | 2445 |
| 270 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +14 | 1137 |
| 271 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 315 |
| 272 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +14 | 700 |
| 273 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +14 | 1323 |
| 274 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +14 | 609 |
| 275 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 539 |
| 276 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +14 | 460 |
| 277 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +13 | 8555 |
| 278 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +13 | 356 |
| 279 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +12 | 2554 |
| 280 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 254 |
| 281 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 220 |
| 282 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1613 |
| 283 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 111 |
| 284 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 110 |
| 285 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +10 | 869 |
| 286 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +10 | 1613 |
| 287 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +10 | 3256 |
| 288 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 481 |
| 289 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +9 | 387 |
| 290 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +9 | 2661 |
| 291 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +8 | 2092 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +8 | 1002 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 232 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +7 | 2283 |
| 295 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +7 | 5177 |
| 296 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 66 |
| 297 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +7 | 129 |
| 298 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +7 | 241 |
| 299 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +7 | 815 |
| 300 | [xup6jammy/Sales-AI](https://github.com/xup6jammy/Sales-AI) | +6 | 78 |
