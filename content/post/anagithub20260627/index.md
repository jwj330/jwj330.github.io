---
title: "2026-06-27 GitHub增长趋势报告"
description: "1.OpenMontage+85 2.codebase-memory-mcp+76 3.simplex-chat+63 4.Agent-Reach+55 5.ai-website-cloner-template+38"
date: 2026-06-27T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-29 21:34:42

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
        'daily': {"categories": ["CyberStrikeus/CyberStrike", "ZhuLinsen/daily_stock_analysis", "tinyhumansai/openhuman", "alchaincyf/zhangxuefeng-skill", "antirez/ds4", "tashfeenahmed/freellmapi", "workweave/router", "ogulcancelik/herdr", "EpicGames/lore", "Leonxlnx/taste-skill", "kunchenguid/no-mistakes", "hugohe3/ppt-master", "mauriceboe/TREK", "Lakr233/AssppWeb", "xbtlin/ai-berkshire", "JCodesMore/ai-website-cloner-template", "Panniantong/Agent-Reach", "simplex-chat/simplex-chat", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [14, 14, 16, 16, 16, 17, 18, 20, 21, 22, 24, 25, 28, 28, 33, 38, 55, 63, 76, 85]},
        'weekly': {"categories": ["stablyai/orca", "asgeirtj/system_prompts_leaks", "mvanhorn/last30days-skill", "rtk-ai/rtk", "xbtlin/ai-berkshire", "hugohe3/ppt-master", "zhaoxuya520/reverse-skill", "JCodesMore/ai-website-cloner-template", "jamiepine/voicebox", "topoteretes/cognee", "mukul975/Anthropic-Cybersecurity-Skills", "apple/container", "penpot/penpot", "Leonxlnx/taste-skill", "StarTrail-org/PixelRAG", "ZhuLinsen/daily_stock_analysis", "Panniantong/Agent-Reach", "palmier-io/palmier-pro", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [71, 73, 73, 75, 78, 81, 85, 99, 104, 114, 114, 118, 119, 137, 142, 174, 221, 229, 243, 409]},
        'monthly': {"categories": ["DeusData/codebase-memory-mcp", "OpenBMB/VoxCPM", "unicity-astrid/astrid", "RyanCodrai/turbovec", "lfnovo/open-notebook", "alibaba/open-code-review", "calesthio/OpenMontage", "rohitg00/ai-engineering-from-scratch", "apple/container", "BigPizzaV3/CodexPlusPlus", "elder-plinius/CL4R1T4S", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "colbymchenry/codegraph", "Egonex-AI/Understand-Anything", "harry0703/MoneyPrinterTurbo", "Leonxlnx/taste-skill", "DietrichGebert/ponytail", "headroomlabs-ai/headroom", "pewdiepie-archdaemon/odysseus"], "data": [367, 375, 404, 414, 415, 437, 458, 489, 491, 510, 637, 804, 861, 917, 992, 998, 1049, 1481, 1590, 2615]}
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
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +85 | 25115 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +76 | 17370 |
| 3 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +63 | 13728 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +55 | 43381 |
| 5 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +38 | 22052 |
| 6 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +33 | 4030 |
| 7 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +28 | 3545 |
| 8 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +28 | 8040 |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +25 | 32991 |
| 10 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +24 | 3773 |
| 11 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +22 | 51989 |
| 12 | [EpicGames/lore](https://github.com/EpicGames/lore) | +21 | 6881 |
| 13 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +20 | 7715 |
| 14 | [workweave/router](https://github.com/workweave/router) | +18 | 454 |
| 15 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +17 | 13456 |
| 16 | [antirez/ds4](https://github.com/antirez/ds4) | +16 | 16207 |
| 17 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +16 | 9435 |
| 18 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +16 | 33331 |
| 19 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +14 | 50494 |
| 20 | [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | +14 | 953 |
| 21 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +14 | 2703 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +13 | 34847 |
| 23 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +13 | 10194 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +13 | 41816 |
| 25 | [stablyai/orca](https://github.com/stablyai/orca) | +13 | 8302 |
| 26 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +11 | 47154 |
| 27 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +11 | 20358 |
| 28 | [every-app/open-seo](https://github.com/every-app/open-seo) | +10 | 3333 |
| 29 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +10 | 9394 |
| 30 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +10 | 28982 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +409 | 25115 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +243 | 17370 |
| 3 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +229 | 9181 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +221 | 43381 |
| 5 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +174 | 50494 |
| 6 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +142 | 5487 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +137 | 51989 |
| 8 | [penpot/penpot](https://github.com/penpot/penpot) | +119 | 44370 |
| 9 | [apple/container](https://github.com/apple/container) | +118 | 43919 |
| 10 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +114 | 22136 |
| 11 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +114 | 23922 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +104 | 34847 |
| 13 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +99 | 22052 |
| 14 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +85 | 6582 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +81 | 32991 |
| 16 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +78 | 4030 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +75 | 66568 |
| 18 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +73 | 47154 |
| 19 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +73 | 32872 |
| 20 | [stablyai/orca](https://github.com/stablyai/orca) | +71 | 8302 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +70 | 13456 |
| 22 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +70 | 13728 |
| 23 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +66 | 3773 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +64 | 61302 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +64 | 23771 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +64 | 31739 |
| 27 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +60 | 11111 |
| 28 | [EpicGames/lore](https://github.com/EpicGames/lore) | +55 | 6881 |
| 29 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +52 | 8040 |
| 30 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +52 | 9451 |
| 31 | [google-research/timesfm](https://github.com/google-research/timesfm) | +51 | 25763 |
| 32 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +50 | 34873 |
| 33 | [unicity-astrid/book](https://github.com/unicity-astrid/book) | +49 | 7557 |
| 34 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +48 | 7715 |
| 35 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +46 | 2205 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +46 | 41816 |
| 37 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +40 | 9394 |
| 38 | [blader/humanizer](https://github.com/blader/humanizer) | +40 | 26407 |
| 39 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +39 | 2703 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +39 | 37280 |
| 41 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +39 | 22037 |
| 42 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +38 | 28982 |
| 43 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +38 | 3034 |
| 44 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1242 |
| 45 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +36 | 20358 |
| 46 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +36 | 9435 |
| 47 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +36 | 1798 |
| 48 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +35 | 14879 |
| 49 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +34 | 3545 |
| 50 | [antirez/ds4](https://github.com/antirez/ds4) | +34 | 16207 |
| 51 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +34 | 35200 |
| 52 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +34 | 5619 |
| 53 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +32 | 36575 |
| 54 | [nubjs/nub](https://github.com/nubjs/nub) | +32 | 2269 |
| 55 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +31 | 26023 |
| 56 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +30 | 23459 |
| 57 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +29 | 1077 |
| 58 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +29 | 18227 |
| 59 | [alibaba/zvec](https://github.com/alibaba/zvec) | +29 | 12546 |
| 60 | [withastro/flue](https://github.com/withastro/flue) | +29 | 6848 |
| 61 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +27 | 33331 |
| 62 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +27 | 29463 |
| 63 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +26 | 9498 |
| 64 | [multica-ai/multica](https://github.com/multica-ai/multica) | +26 | 38247 |
| 65 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +26 | 20061 |
| 66 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +26 | 43087 |
| 67 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +26 | 6330 |
| 68 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +25 | 24304 |
| 69 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +24 | 31202 |
| 70 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +24 | 5375 |
| 71 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +23 | 10931 |
| 72 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +23 | 8906 |
| 73 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +23 | 1995 |
| 74 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +22 | 10194 |
| 75 | [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) | +22 | 1313 |
| 76 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +22 | 8033 |
| 77 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +22 | 4042 |
| 78 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +22 | 1448 |
| 79 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +22 | 19213 |
| 80 | [anbeime/skill](https://github.com/anbeime/skill) | +22 | 2608 |
| 81 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +22 | 5113 |
| 82 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +21 | 22077 |
| 83 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +20 | 394 |
| 84 | [revfactory/harness](https://github.com/revfactory/harness) | +20 | 8017 |
| 85 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +20 | 38574 |
| 86 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +20 | 7495 |
| 87 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +20 | 19190 |
| 88 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +20 | 6865 |
| 89 | [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | +19 | 953 |
| 90 | [every-app/open-seo](https://github.com/every-app/open-seo) | +19 | 3333 |
| 91 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +19 | 4889 |
| 92 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | +19 | 17420 |
| 93 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +19 | 5348 |
| 94 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +19 | 31889 |
| 95 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +19 | 25461 |
| 96 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +19 | 20211 |
| 97 | [workweave/router](https://github.com/workweave/router) | +18 | 454 |
| 98 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +18 | 5756 |
| 99 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +18 | 23711 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +17 | 29360 |
| 101 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +17 | 41864 |
| 102 | [openai/skills](https://github.com/openai/skills) | +17 | 22948 |
| 103 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +16 | 626 |
| 104 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +16 | 27279 |
| 105 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +16 | 4769 |
| 106 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 16066 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +15 | 17674 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +15 | 43983 |
| 109 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 13659 |
| 110 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +15 | 4639 |
| 111 | [deekur/gaokaomath](https://github.com/deekur/gaokaomath) | +14 | 1055 |
| 112 | [QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | +14 | 590 |
| 113 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +14 | 32653 |
| 114 | [Project-N-E-K-O/N.E.K.O](https://github.com/Project-N-E-K-O/N.E.K.O) | +14 | 1836 |
| 115 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +13 | 1126 |
| 116 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +13 | 1472 |
| 117 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +13 | 7790 |
| 118 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +13 | 2999 |
| 119 | [ksimback/looper](https://github.com/ksimback/looper) | +13 | 488 |
| 120 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +13 | 2635 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2615 | 78537 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1590 | 52540 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1481 | 61655 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1049 | 51989 |
| 5 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +998 | 49621 |
| 6 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +992 | 68639 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +917 | 55358 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +861 | 47154 |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +804 | 43381 |
| 10 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +637 | 44027 |
| 11 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +510 | 22037 |
| 12 | [apple/container](https://github.com/apple/container) | +491 | 43919 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +489 | 36575 |
| 14 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +458 | 25115 |
| 15 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +437 | 9451 |
| 16 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +415 | 33628 |
| 17 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +414 | 12268 |
| 18 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +404 | 10336 |
| 19 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +375 | 31889 |
| 20 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +367 | 17371 |
| 21 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +366 | 10931 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +363 | 34873 |
| 23 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8227 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +344 | 31739 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +337 | 41816 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +332 | 66568 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +328 | 50494 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +323 | 32992 |
| 29 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +313 | 11111 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +313 | 23771 |
| 31 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +292 | 22136 |
| 32 | [roboflow/supervision](https://github.com/roboflow/supervision) | +277 | 36553 |
| 33 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +271 | 9181 |
| 34 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +269 | 13456 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +257 | 14879 |
| 36 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +246 | 4871 |
| 37 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +232 | 9498 |
| 38 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +229 | 15098 |
| 39 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +222 | 17015 |
| 40 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4333 |
| 41 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5438 |
| 42 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +209 | 35570 |
| 43 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +199 | 32119 |
| 44 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +198 | 37280 |
| 45 | [shadcn/improve](https://github.com/shadcn/improve) | +198 | 6319 |
| 46 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +198 | 6330 |
| 47 | [penpot/penpot](https://github.com/penpot/penpot) | +197 | 44370 |
| 48 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +192 | 5348 |
| 49 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +187 | 29360 |
| 50 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +186 | 24158 |
| 51 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +186 | 21958 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +182 | 24304 |
| 53 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +180 | 20061 |
| 54 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +176 | 4526 |
| 55 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +174 | 31098 |
| 56 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +173 | 61302 |
| 57 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +171 | 34847 |
| 58 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +170 | 27279 |
| 59 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +168 | 11949 |
| 60 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +167 | 32872 |
| 61 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +166 | 6865 |
| 62 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +164 | 22052 |
| 63 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +164 | 5336 |
| 64 | [blader/humanizer](https://github.com/blader/humanizer) | +163 | 26407 |
| 65 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +163 | 32653 |
| 66 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +163 | 33331 |
| 67 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +162 | 13659 |
| 68 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +160 | 10233 |
| 69 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +159 | 5375 |
| 70 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +159 | 12782 |
| 71 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +158 | 7715 |
| 72 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +157 | 26047 |
| 73 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +155 | 22144 |
| 74 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +155 | 11171 |
| 75 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +154 | 3676 |
| 76 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +154 | 22077 |
| 77 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +154 | 19190 |
| 78 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +153 | 5487 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +153 | 35200 |
| 80 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +149 | 7528 |
| 81 | [EpicGames/lore](https://github.com/EpicGames/lore) | +148 | 6881 |
| 82 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +148 | 5113 |
| 83 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +146 | 26023 |
| 84 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +143 | 31431 |
| 85 | [revfactory/harness](https://github.com/revfactory/harness) | +143 | 8017 |
| 86 | [google/skills](https://github.com/google/skills) | +142 | 14182 |
| 87 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +142 | 40312 |
| 88 | [google-research/timesfm](https://github.com/google-research/timesfm) | +140 | 25763 |
| 89 | [multica-ai/multica](https://github.com/multica-ai/multica) | +140 | 38247 |
| 90 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +137 | 6582 |
| 91 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +137 | 16066 |
| 92 | [stablyai/orca](https://github.com/stablyai/orca) | +136 | 8302 |
| 93 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +130 | 23923 |
| 94 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +128 | 23711 |
| 95 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +126 | 23459 |
| 96 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +125 | 39095 |
| 97 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +124 | 38574 |
| 98 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +124 | 21337 |
| 99 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +121 | 25540 |
| 100 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +120 | 43983 |
| 101 | [withastro/flue](https://github.com/withastro/flue) | +117 | 6848 |
| 102 | [decolua/9router](https://github.com/decolua/9router) | +115 | 18610 |
| 103 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +114 | 38556 |
| 104 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +113 | 29463 |
| 105 | [openai/plugins](https://github.com/openai/plugins) | +111 | 3664 |
| 106 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +108 | 49663 |
| 107 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +104 | 7495 |
| 108 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +102 | 4873 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +101 | 9394 |
| 110 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +100 | 10194 |
| 111 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +100 | 5339 |
| 112 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +100 | 5248 |
| 113 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +99 | 35897 |
| 114 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +98 | 10715 |
| 115 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +97 | 14230 |
| 116 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +96 | 9959 |
| 117 | [openai/skills](https://github.com/openai/skills) | +95 | 22948 |
| 118 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +95 | 17381 |
| 119 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +93 | 41864 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +92 | 31202 |
| 121 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +92 | 7692 |
| 122 | [soxoj/maigret](https://github.com/soxoj/maigret) | +91 | 33822 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +89 | 17674 |
| 124 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +89 | 4639 |
| 125 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +84 | 47447 |
| 126 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +81 | 5695 |
| 127 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +80 | 4769 |
| 128 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +80 | 3783 |
| 129 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +79 | 3559 |
| 130 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +78 | 19213 |
| 131 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +78 | 24304 |
| 132 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +77 | 8033 |
| 133 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +77 | 3863 |
| 134 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +76 | 1708 |
| 135 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +76 | 5398 |
| 136 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +75 | 4030 |
| 137 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +75 | 4894 |
| 138 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +74 | 20211 |
| 139 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +74 | 4635 |
| 140 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +72 | 3034 |
| 141 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +72 | 8906 |
| 142 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +72 | 25461 |
| 143 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +71 | 2281 |
| 144 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +71 | 25843 |
| 145 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +70 | 7077 |
| 146 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +66 | 25193 |
| 147 | [browser-use/video-use](https://github.com/browser-use/video-use) | +65 | 10475 |
| 148 | [browser-act/skills](https://github.com/browser-act/skills) | +65 | 3088 |
| 149 | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | +65 | 33169 |
| 150 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +61 | 7147 |
| 151 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +61 | 6028 |
| 152 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +60 | 24023 |
| 153 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +59 | 16911 |
| 154 | [jundot/omlx](https://github.com/jundot/omlx) | +59 | 17165 |
| 155 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +59 | 2747 |
| 156 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 157 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +58 | 2866 |
| 158 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +58 | 3386 |
| 159 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +58 | 3304 |
| 160 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +58 | 12703 |
| 161 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +58 | 11727 |
| 162 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +58 | 36103 |
| 163 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +56 | 0 |
| 164 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +56 | 8799 |
| 165 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +56 | 18994 |
| 166 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +54 | 3599 |
| 167 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +53 | 2615 |
| 168 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +52 | 1337 |
| 169 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +52 | 7970 |
| 170 | [anbeime/skill](https://github.com/anbeime/skill) | +51 | 2608 |
| 171 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +51 | 18952 |
| 172 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +51 | 16396 |
| 173 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +50 | 44795 |
| 174 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +50 | 1842 |
| 175 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +50 | 26109 |
| 176 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +50 | 2806 |
| 177 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +49 | 7627 |
| 178 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +49 | 2075 |
| 179 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +49 | 17262 |
| 180 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +48 | 21755 |
| 181 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +48 | 4855 |
| 182 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +48 | 7229 |
| 183 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +46 | 3386 |
| 184 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +46 | 15411 |
| 185 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +46 | 1804 |
| 186 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +45 | 20179 |
| 187 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1156 |
| 188 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +44 | 37564 |
| 189 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +43 | 1798 |
| 190 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +43 | 3180 |
| 191 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +40 | 1242 |
| 192 | [floci-io/floci](https://github.com/floci-io/floci) | +40 | 14483 |
| 193 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +37 | 5872 |
| 194 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +35 | 889 |
| 195 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +34 | 5363 |
| 196 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +34 | 1979 |
| 197 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +33 | 4116 |
| 198 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9464 |
| 199 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +31 | 1296 |
| 200 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +31 | 28397 |
| 201 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +30 | 1123 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +30 | 7910 |
| 203 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +29 | 8400 |
| 204 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +27 | 1899 |
| 205 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +26 | 815 |
| 206 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +25 | 1248 |
| 207 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +25 | 715 |
| 208 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +24 | 1730 |
| 209 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +24 | 11430 |
| 210 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +24 | 2407 |
| 211 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 28 |
| 212 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +22 | 369 |
| 213 | [zzzhhh1/free-nodes](https://github.com/zzzhhh1/free-nodes) | +21 | 0 |
| 214 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +21 | 394 |
| 215 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 586 |
| 216 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +21 | 992 |
| 217 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +21 | 5539 |
| 218 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +21 | 4938 |
| 219 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +21 | 819 |
| 220 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +21 | 1000 |
| 221 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +20 | 4005 |
| 222 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +20 | 1125 |
| 223 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +20 | 2387 |
| 224 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 545 |
| 225 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +19 | 5408 |
| 226 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +19 | 3932 |
| 227 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +18 | 596 |
| 228 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +18 | 13890 |
| 229 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +18 | 1436 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +18 | 2900 |
| 231 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +18 | 0 |
| 232 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +18 | 1110 |
| 233 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 539 |
| 234 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +17 | 4619 |
| 235 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +16 | 626 |
| 236 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +16 | 2035 |
| 237 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +15 | 516 |
| 238 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +15 | 856 |
| 239 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 450 |
| 240 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2470 |
| 241 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +14 | 12194 |
| 242 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +14 | 301 |
| 243 | [robinebers/openusage](https://github.com/robinebers/openusage) | +14 | 3020 |
| 244 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 459 |
| 245 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +14 | 398 |
| 246 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +14 | 2684 |
| 247 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +13 | 1320 |
| 248 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +13 | 294 |
| 249 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +13 | 8332 |
| 250 | [Shiyao-Huang/awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) | +13 | 168 |
| 251 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 451 |
| 252 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +13 | 2256 |
| 253 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +13 | 2500 |
| 254 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 575 |
| 255 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 315 |
| 256 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +12 | 1534 |
| 257 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +12 | 0 |
| 258 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 263 |
| 259 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +12 | 2615 |
| 260 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +11 | 400 |
| 261 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +11 | 2054 |
| 262 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +11 | 733 |
| 263 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +11 | 2854 |
| 264 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +9 | 1227 |
| 265 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +9 | 2191 |
| 266 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +9 | 1036 |
| 267 | [fcompc4/ecommerce-kushi](https://github.com/fcompc4/ecommerce-kushi) | +9 | 213 |
| 268 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +9 | 2894 |
| 269 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3608 |
| 270 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 199 |
| 271 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +9 | 1718 |
| 272 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 374 |
| 273 | [emollick/concord](https://github.com/emollick/concord) | +8 | 196 |
| 274 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +8 | 3081 |
| 275 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +8 | 666 |
| 276 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 233 |
| 277 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +7 | 155 |
| 278 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 180 |
| 279 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +7 | 2548 |
| 280 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2649 |
| 281 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +7 | 1639 |
| 282 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +6 | 224 |
| 283 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +6 | 2654 |
| 284 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +6 | 141 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2711 |
| 286 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +5 | 143 |
| 287 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 110 |
| 288 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +5 | 348 |
| 289 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 563 |
| 290 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +5 | 277 |
| 291 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +5 | 169 |
| 292 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 216 |
| 293 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 258 |
| 294 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 86 |
| 295 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +4 | 935 |
| 296 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 505 |
| 297 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 512 |
| 298 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +3 | 364 |
| 299 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 180 |
| 300 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +3 | 2183 |
