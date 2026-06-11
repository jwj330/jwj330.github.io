---
title: "2026-06-11 GitHub增长趋势报告"
description: "1.agent-skills+85 2.container+53 3.headroom+37 4.taste-skill+34 5.last30days-skill+28"
date: 2026-06-11T22:03:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-11 22:03:54

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
        'daily': {"categories": ["heygen-com/hyperframes", "activeloopai/hivemind", "ZhuLinsen/daily_stock_analysis", "masterking32/MasterDnsVPN", "datawhalechina/hello-agents", "Panniantong/Agent-Reach", "pbakaus/impeccable", "tashfeenahmed/freellmapi", "extend-hq/ui", "Imbad0202/academic-research-skills", "hugohe3/ppt-master", "luongnv89/claude-howto", "Lum1104/Understand-Anything", "colbymchenry/codegraph", "refactoringhq/tolaria", "mvanhorn/last30days-skill", "Leonxlnx/taste-skill", "chopratejas/headroom", "apple/container", "addyosmani/agent-skills"], "data": [11, 11, 11, 12, 12, 14, 14, 14, 15, 16, 17, 17, 20, 22, 27, 28, 34, 37, 53, 85]},
        'weekly': {"categories": ["refactoringhq/tolaria", "unicity-astrid/sdk-js", "CopilotKit/CopilotKit", "rohitg00/ai-engineering-from-scratch", "OpenBMB/VoxCPM", "XingYu-Zhong/DeepSeek-GUI", "santifer/career-ops", "addyosmani/agent-skills", "unicity-astrid/astrid", "roboflow/supervision", "Panniantong/Agent-Reach", "lfnovo/open-notebook", "Lum1104/Understand-Anything", "alibaba/open-code-review", "colbymchenry/codegraph", "RyanCodrai/turbovec", "Leonxlnx/taste-skill", "chopratejas/headroom", "mvanhorn/last30days-skill", "pewdiepie-archdaemon/odysseus"], "data": [143, 152, 171, 171, 172, 177, 177, 181, 184, 227, 253, 256, 280, 288, 340, 364, 477, 510, 589, 1051]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "Hmbown/CodeWhale", "safishamsi/graphify", "github/spec-kit", "Leonxlnx/taste-skill", "rohitg00/agentmemory", "ruvnet/RuView", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "farion1231/cc-switch", "affaan-m/ECC", "tinyhumansai/openhuman", "obra/superpowers", "pewdiepie-archdaemon/odysseus", "Lum1104/Understand-Anything", "NousResearch/hermes-agent", "colbymchenry/codegraph", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [977, 986, 1081, 1098, 1187, 1251, 1357, 1411, 1479, 1636, 1720, 2057, 2184, 2282, 2334, 2844, 2858, 3046, 3321, 3408]}
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
| 1 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +85 | 54535 |
| 2 | [apple/container](https://github.com/apple/container) | +53 | 32167 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +37 | 23083 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +34 | 41496 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +28 | 39677 |
| 6 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +27 | 15354 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +22 | 47427 |
| 8 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +20 | 57353 |
| 9 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +17 | 36871 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +17 | 26634 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 30254 |
| 12 | [extend-hq/ui](https://github.com/extend-hq/ui) | +15 | 835 |
| 13 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +14 | 9742 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +14 | 37543 |
| 15 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +14 | 26351 |
| 16 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +12 | 58515 |
| 17 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +12 | 5651 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +11 | 42177 |
| 19 | [activeloopai/hivemind](https://github.com/activeloopai/hivemind) | +11 | 1050 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +11 | 26816 |
| 21 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 31354 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +11 | 61474 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +11 | 19104 |
| 24 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +10 | 16636 |
| 25 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +9 | 11057 |
| 26 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +8 | 22309 |
| 27 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +8 | 3396 |
| 28 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +7 | 2994 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +7 | 11917 |
| 30 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +7 | 22379 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1051 | 68308 |
| 2 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +589 | 39677 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +510 | 23083 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +477 | 41496 |
| 5 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +364 | 11057 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +340 | 47427 |
| 7 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +288 | 6224 |
| 8 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +280 | 57353 |
| 9 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +256 | 29257 |
| 10 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +253 | 26351 |
| 11 | [roboflow/supervision](https://github.com/roboflow/supervision) | +227 | 36553 |
| 12 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +184 | 8705 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +181 | 54535 |
| 14 | [santifer/career-ops](https://github.com/santifer/career-ops) | +177 | 52777 |
| 15 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +177 | 3786 |
| 16 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +172 | 28454 |
| 17 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +171 | 31354 |
| 18 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +171 | 34718 |
| 19 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +152 | 8256 |
| 20 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +143 | 15354 |
| 21 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +142 | 30254 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +142 | 26816 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +138 | 37543 |
| 24 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +132 | 20761 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +115 | 30550 |
| 26 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +114 | 3264 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +112 | 19104 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +110 | 9742 |
| 29 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +109 | 31098 |
| 30 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +107 | 3881 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +103 | 61474 |
| 32 | [apple/container](https://github.com/apple/container) | +99 | 32168 |
| 33 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +99 | 18288 |
| 34 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +99 | 1885 |
| 35 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +93 | 10974 |
| 36 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +90 | 27198 |
| 37 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +90 | 3009 |
| 38 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +89 | 49255 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +87 | 26634 |
| 40 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +86 | 58515 |
| 41 | [openai/plugins](https://github.com/openai/plugins) | +83 | 2809 |
| 42 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +77 | 11917 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +76 | 22309 |
| 44 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +76 | 15395 |
| 45 | [reconurge/flowsint](https://github.com/reconurge/flowsint) | +76 | 6469 |
| 46 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +75 | 21035 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +75 | 11863 |
| 48 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +69 | 26361 |
| 49 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +68 | 36871 |
| 50 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +68 | 2121 |
| 51 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +66 | 11790 |
| 52 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +66 | 14239 |
| 53 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +64 | 42177 |
| 54 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +64 | 22379 |
| 55 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +64 | 25568 |
| 56 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +63 | 16636 |
| 57 | [revfactory/harness](https://github.com/revfactory/harness) | +63 | 6820 |
| 58 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +62 | 8952 |
| 59 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +60 | 33870 |
| 60 | [blader/humanizer](https://github.com/blader/humanizer) | +60 | 23760 |
| 61 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +59 | 30894 |
| 62 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +58 | 1386 |
| 63 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +58 | 15825 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +57 | 32932 |
| 65 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +57 | 13538 |
| 66 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +53 | 57448 |
| 67 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +52 | 20282 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +52 | 37227 |
| 69 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +52 | 3941 |
| 70 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +51 | 3396 |
| 71 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +50 | 23891 |
| 72 | [withastro/flue](https://github.com/withastro/flue) | +50 | 4920 |
| 73 | [decolua/9router](https://github.com/decolua/9router) | +49 | 17271 |
| 74 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +48 | 38034 |
| 75 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +48 | 6830 |
| 76 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +48 | 5399 |
| 77 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +47 | 1865 |
| 78 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +46 | 9884 |
| 79 | [Makisuo/maple](https://github.com/Makisuo/maple) | +46 | 1243 |
| 80 | [multica-ai/multica](https://github.com/multica-ai/multica) | +45 | 36287 |
| 81 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +44 | 2166 |
| 82 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +44 | 9732 |
| 83 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +43 | 4245 |
| 84 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +43 | 4632 |
| 85 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +42 | 29262 |
| 86 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +42 | 921 |
| 87 | [openai/skills](https://github.com/openai/skills) | +42 | 21971 |
| 88 | [Ataraxy-Labs/sem](https://github.com/Ataraxy-Labs/sem) | +42 | 2691 |
| 89 | [cclank/cell-architecture-studio](https://github.com/cclank/cell-architecture-studio) | +42 | 1305 |
| 90 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +41 | 8312 |
| 91 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +40 | 3013 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +39 | 42745 |
| 93 | [Sumanth077/Hands-On-AI-Engineering](https://github.com/Sumanth077/Hands-On-AI-Engineering) | +39 | 2057 |
| 94 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +38 | 2651 |
| 95 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +38 | 2994 |
| 96 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +38 | 16531 |
| 97 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +37 | 22044 |
| 98 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +37 | 21421 |
| 99 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +37 | 11193 |
| 100 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +37 | 2908 |
| 101 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +36 | 5250 |
| 102 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +36 | 2224 |
| 103 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +36 | 14505 |
| 104 | [browser-act/skills](https://github.com/browser-act/skills) | +36 | 2357 |
| 105 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +35 | 27973 |
| 106 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +35 | 771 |
| 107 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +34 | 2777 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +34 | 6828 |
| 109 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +34 | 3643 |
| 110 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +34 | 8689 |
| 111 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +32 | 24486 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +32 | 16174 |
| 113 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 464 |
| 114 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +29 | 2349 |
| 115 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +29 | 40386 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +28 | 5874 |
| 117 | [francescopace/espectre](https://github.com/francescopace/espectre) | +27 | 8535 |
| 118 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +27 | 6571 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +27 | 16263 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +27 | 29918 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3408 | 173487 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3321 | 125646 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3046 | 47427 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2858 | 190941 |
| 5 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2844 | 57353 |
| 6 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2334 | 68308 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2282 | 60312 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2184 | 31538 |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2057 | 51199 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1720 | 98480 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1636 | 31354 |
| 12 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1479 | 30254 |
| 13 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1411 | 25568 |
| 14 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1357 | 73196 |
| 15 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1251 | 22379 |
| 16 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1187 | 41496 |
| 17 | [github/spec-kit](https://github.com/github/spec-kit) | +1098 | 71722 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1081 | 65615 |
| 19 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +986 | 38034 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +977 | 111460 |
| 21 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +971 | 89407 |
| 22 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +941 | 49621 |
| 23 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +919 | 29918 |
| 24 | [earendil-works/pi](https://github.com/earendil-works/pi) | +842 | 61778 |
| 25 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +812 | 23083 |
| 26 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +783 | 54535 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +781 | 19104 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +775 | 61474 |
| 29 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +768 | 63063 |
| 30 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +767 | 30894 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +759 | 34148 |
| 32 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +739 | 11479 |
| 33 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +728 | 71516 |
| 34 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +718 | 39677 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +698 | 26634 |
| 36 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +686 | 58993 |
| 37 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +681 | 8222 |
| 38 | [decolua/9router](https://github.com/decolua/9router) | +669 | 17271 |
| 39 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +652 | 20761 |
| 40 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +641 | 58515 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +602 | 33870 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +589 | 36287 |
| 43 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +582 | 11057 |
| 44 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +579 | 27973 |
| 45 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +576 | 11863 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +563 | 26816 |
| 47 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +550 | 16782 |
| 48 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +538 | 42745 |
| 49 | [floci-io/floci](https://github.com/floci-io/floci) | +533 | 13985 |
| 50 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +524 | 20282 |
| 51 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +520 | 15395 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +494 | 37543 |
| 53 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +494 | 22044 |
| 54 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +487 | 9742 |
| 55 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +487 | 16636 |
| 56 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +476 | 22309 |
| 57 | [santifer/career-ops](https://github.com/santifer/career-ops) | +467 | 52777 |
| 58 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +466 | 5268 |
| 59 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +461 | 11917 |
| 60 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +459 | 6610 |
| 61 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +447 | 18866 |
| 62 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +444 | 8259 |
| 63 | [antirez/ds4](https://github.com/antirez/ds4) | +438 | 13466 |
| 64 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +436 | 27198 |
| 65 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +424 | 28454 |
| 66 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +424 | 26361 |
| 67 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +409 | 6994 |
| 68 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +407 | 6828 |
| 69 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +402 | 4995 |
| 70 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +401 | 42177 |
| 71 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +400 | 9732 |
| 72 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +395 | 4552 |
| 73 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +385 | 21801 |
| 74 | [withcoral/coral](https://github.com/withcoral/coral) | +385 | 5139 |
| 75 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +384 | 8705 |
| 76 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +375 | 13538 |
| 77 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +374 | 14239 |
| 78 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +372 | 38351 |
| 79 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +366 | 26351 |
| 80 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +366 | 5204 |
| 81 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +363 | 29774 |
| 82 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +362 | 5250 |
| 83 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +345 | 8256 |
| 84 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +335 | 6224 |
| 85 | [roboflow/supervision](https://github.com/roboflow/supervision) | +326 | 36553 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +319 | 24080 |
| 87 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +319 | 5038 |
| 88 | [blader/humanizer](https://github.com/blader/humanizer) | +312 | 23760 |
| 89 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +310 | 41960 |
| 90 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +306 | 29257 |
| 91 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +306 | 32932 |
| 92 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +305 | 37227 |
| 93 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +299 | 43378 |
| 94 | [soxoj/maigret](https://github.com/soxoj/maigret) | +296 | 32560 |
| 95 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +295 | 57448 |
| 96 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +288 | 29262 |
| 97 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +287 | 23891 |
| 98 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +286 | 18288 |
| 99 | [MinishLab/semble](https://github.com/MinishLab/semble) | +279 | 5072 |
| 100 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +269 | 15354 |
| 101 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +264 | 8210 |
| 102 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +259 | 8952 |
| 103 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +257 | 19578 |
| 104 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +253 | 11790 |
| 105 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +252 | 4351 |
| 106 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +247 | 36871 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +238 | 14505 |
| 108 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +238 | 2921 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +234 | 3941 |
| 110 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +229 | 3802 |
| 111 | [XingYu-Zhong/DeepSeek-GUI](https://github.com/XingYu-Zhong/DeepSeek-GUI) | +226 | 3786 |
| 112 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +219 | 3263 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +218 | 16263 |
| 114 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +218 | 4245 |
| 115 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +215 | 9181 |
| 116 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +210 | 6112 |
| 117 | [openai/skills](https://github.com/openai/skills) | +203 | 21971 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +202 | 16174 |
| 119 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +200 | 4032 |
| 120 | [88lin/video_vip](https://github.com/88lin/video_vip) | +199 | 3903 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +196 | 17835 |
| 122 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +191 | 16531 |
| 123 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +191 | 7220 |
| 124 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +188 | 36799 |
| 125 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +187 | 11949 |
| 126 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +183 | 2594 |
| 127 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +181 | 2535 |
| 128 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +180 | 5335 |
| 129 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +180 | 46209 |
| 130 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +178 | 7840 |
| 131 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +175 | 40386 |
| 132 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +175 | 3643 |
| 133 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +173 | 3013 |
| 134 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +173 | 5874 |
| 135 | [jundot/omlx](https://github.com/jundot/omlx) | +173 | 16426 |
| 136 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6533 |
| 137 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +167 | 14658 |
| 138 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +167 | 34451 |
| 139 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +161 | 10974 |
| 140 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +159 | 34460 |
| 141 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +158 | 23292 |
| 142 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +158 | 27094 |
| 143 | [Fokkyp/SoftwareCopyright-Skill](https://github.com/Fokkyp/SoftwareCopyright-Skill) | +158 | 3771 |
| 144 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +156 | 1971 |
| 145 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +151 | 24187 |
| 146 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +151 | 20698 |
| 147 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2413 |
| 148 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +149 | 23047 |
| 149 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +148 | 49255 |
| 150 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +148 | 24994 |
| 151 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +144 | 2930 |
| 152 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +144 | 24417 |
| 153 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +141 | 2224 |
| 154 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +140 | 2908 |
| 155 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +139 | 34843 |
| 156 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +135 | 6621 |
| 157 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +132 | 18386 |
| 158 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +130 | 7308 |
| 159 | [browser-use/video-use](https://github.com/browser-use/video-use) | +128 | 9516 |
| 160 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1990 |
| 161 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2059 |
| 162 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3009 |
| 163 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +123 | 4227 |
| 164 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +122 | 26881 |
| 165 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +121 | 12780 |
| 166 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6571 |
| 167 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +115 | 24486 |
| 168 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +115 | 11044 |
| 169 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +115 | 32872 |
| 170 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +113 | 6798 |
| 171 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +112 | 5626 |
| 172 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +110 | 8689 |
| 173 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +109 | 25515 |
| 174 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1634 |
| 175 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +108 | 44069 |
| 176 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +107 | 28247 |
| 177 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +107 | 37564 |
| 178 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +106 | 4632 |
| 179 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +106 | 36103 |
| 180 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +105 | 7326 |
| 181 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +105 | 4561 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +103 | 15609 |
| 183 | [openai/plugins](https://github.com/openai/plugins) | +102 | 2809 |
| 184 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +99 | 4840 |
| 185 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +98 | 2449 |
| 186 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +98 | 12068 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +96 | 29223 |
| 188 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 803 |
| 189 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +91 | 1260 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +90 | 27821 |
| 191 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +90 | 17955 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +87 | 4152 |
| 193 | [usebruno/bruno](https://github.com/usebruno/bruno) | +86 | 41086 |
| 194 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +83 | 1157 |
| 195 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +79 | 2769 |
| 196 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +73 | 2637 |
| 197 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +70 | 2237 |
| 198 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +67 | 5133 |
| 199 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1216 |
| 200 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +65 | 5537 |
| 201 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +64 | 8518 |
| 202 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +64 | 7832 |
| 203 | [eze-is/web-access](https://github.com/eze-is/web-access) | +63 | 7464 |
| 204 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +59 | 5079 |
| 205 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +56 | 3555 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +55 | 10953 |
| 207 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +53 | 2802 |
| 208 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +52 | 2303 |
| 209 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +50 | 1627 |
| 210 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +50 | 4968 |
| 211 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 921 |
| 212 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +46 | 855 |
| 213 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +43 | 3725 |
| 214 | [sandeco/reversa](https://github.com/sandeco/reversa) | +42 | 1207 |
| 215 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +42 | 2687 |
| 216 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +40 | 12050 |
| 217 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +39 | 532 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +39 | 2120 |
| 219 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +38 | 1330 |
| 220 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +38 | 8687 |
| 221 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +38 | 286 |
| 222 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +38 | 9392 |
| 223 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +37 | 10219 |
| 224 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4253 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +34 | 4360 |
| 226 | [browserbase/skills](https://github.com/browserbase/skills) | +34 | 3547 |
| 227 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 294 |
| 228 | [eooce/nodejs-argo](https://github.com/eooce/nodejs-argo) | +33 | 7857 |
| 229 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +33 | 8207 |
| 230 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 508 |
| 231 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +31 | 1838 |
| 232 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +31 | 347 |
| 233 | [robinebers/openusage](https://github.com/robinebers/openusage) | +30 | 2846 |
| 234 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +30 | 371 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +29 | 13648 |
| 236 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +28 | 2131 |
| 237 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +28 | 2479 |
| 238 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +27 | 1853 |
| 239 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +27 | 4394 |
| 240 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 794 |
| 241 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +24 | 2024 |
| 242 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 202 |
| 243 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +23 | 2595 |
| 244 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +23 | 1064 |
| 245 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +22 | 4962 |
| 246 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 123 |
| 247 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +21 | 716 |
| 248 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +21 | 1525 |
| 249 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +20 | 1934 |
| 250 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +20 | 944 |
| 251 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 576 |
| 252 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +20 | 399 |
| 253 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +20 | 1090 |
| 254 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +20 | 3433 |
| 255 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +20 | 2397 |
| 256 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +20 | 300 |
| 257 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +20 | 3412 |
| 258 | [openmemind/memind](https://github.com/openmemind/memind) | +20 | 899 |
| 259 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +19 | 511 |
| 260 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +19 | 364 |
| 261 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13556 |
| 262 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +18 | 340 |
| 263 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +17 | 694 |
| 264 | [WJZ-P/sona](https://github.com/WJZ-P/sona) | +17 | 645 |
| 265 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +17 | 2423 |
| 266 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +17 | 2990 |
| 267 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +17 | 461 |
| 268 | [is-a-dev/register](https://github.com/is-a-dev/register) | +16 | 10455 |
| 269 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +16 | 633 |
| 270 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +15 | 1311 |
| 271 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +15 | 620 |
| 272 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +15 | 8551 |
| 273 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +15 | 2468 |
| 274 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +15 | 353 |
| 275 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 308 |
| 276 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 534 |
| 277 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +14 | 387 |
| 278 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +13 | 2544 |
| 279 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +13 | 576 |
| 280 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 216 |
| 281 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +12 | 2661 |
| 282 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +11 | 1121 |
| 283 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 110 |
| 284 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +10 | 862 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +10 | 1608 |
| 286 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1606 |
| 287 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +10 | 233 |
| 288 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +10 | 3256 |
| 289 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +9 | 111 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +9 | 2085 |
| 291 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 477 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +9 | 997 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +9 | 230 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +8 | 2276 |
| 295 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +8 | 127 |
| 296 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +8 | 811 |
| 297 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 64 |
| 298 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +7 | 1038 |
| 299 | [basic-framework/web-backend](https://github.com/basic-framework/web-backend) | +7 | 305 |
| 300 | [Keeperorowner/NagramXF](https://github.com/Keeperorowner/NagramXF) | +7 | 357 |
