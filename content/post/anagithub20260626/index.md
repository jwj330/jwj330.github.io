---
title: "2026-06-26 GitHub增长趋势报告"
description: "1.OpenMontage+40 2.Anthropic-Cybersecurity-Skills+27 3.ai-berkshire+26 4.daily_stock_analysis+24 5.claude-code-best-practice+23"
date: 2026-06-26T21:20:38+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-26 21:20:38

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
        'daily': {"categories": ["bozhouDev/codex-orange-book", "rtk-ai/rtk", "every-app/open-seo", "colbymchenry/codegraph", "deekur/gaokaomath", "DeusData/codebase-memory-mcp", "tashfeenahmed/freellmapi", "alibaba/page-agent", "hugohe3/ppt-master", "chopratejas/headroom", "Leonxlnx/taste-skill", "mauriceboe/TREK", "stablyai/orca", "JCodesMore/ai-website-cloner-template", "Panniantong/Agent-Reach", "shanraisshan/claude-code-best-practice", "ZhuLinsen/daily_stock_analysis", "xbtlin/ai-berkshire", "mukul975/Anthropic-Cybersecurity-Skills", "calesthio/OpenMontage"], "data": [7, 8, 8, 9, 10, 11, 13, 13, 14, 17, 17, 18, 18, 20, 23, 23, 24, 26, 27, 40]},
        'weekly': {"categories": ["JCodesMore/ai-website-cloner-template", "asgeirtj/system_prompts_leaks", "rtk-ai/rtk", "EpicGames/lore", "mvanhorn/last30days-skill", "colbymchenry/codegraph", "zhaoxuya520/reverse-skill", "topoteretes/cognee", "jamiepine/voicebox", "mukul975/Anthropic-Cybersecurity-Skills", "apple/container", "Leonxlnx/taste-skill", "penpot/penpot", "StarTrail-org/PixelRAG", "ZhuLinsen/daily_stock_analysis", "Panniantong/Agent-Reach", "DeusData/codebase-memory-mcp", "palmier-io/palmier-pro", "calesthio/OpenMontage", "chopratejas/headroom"], "data": [65, 69, 69, 70, 70, 73, 81, 82, 94, 109, 112, 127, 130, 140, 165, 177, 193, 249, 334, 413]},
        'monthly': {"categories": ["Imbad0202/academic-research-skills", "unicity-astrid/astrid", "lfnovo/open-notebook", "RyanCodrai/turbovec", "alibaba/open-code-review", "apple/container", "BigPizzaV3/CodexPlusPlus", "rohitg00/ai-engineering-from-scratch", "elder-plinius/CL4R1T4S", "addyosmani/agent-skills", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "harry0703/MoneyPrinterTurbo", "Leonxlnx/taste-skill", "Egonex-AI/Understand-Anything", "DietrichGebert/ponytail", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [382, 404, 411, 421, 442, 479, 552, 590, 633, 671, 751, 853, 907, 1012, 1019, 1200, 1205, 1393, 1553, 2606]}
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
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +40 | 23480 |
| 2 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +27 | 21770 |
| 3 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +26 | 3056 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +24 | 50079 |
| 5 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +23 | 61111 |
| 6 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +23 | 42239 |
| 7 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +20 | 21287 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +18 | 7892 |
| 9 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +18 | 7575 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +17 | 51514 |
| 11 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +17 | 51908 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +14 | 32328 |
| 13 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +13 | 20200 |
| 14 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +13 | 13133 |
| 15 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +11 | 15498 |
| 16 | [deekur/gaokaomath](https://github.com/deekur/gaokaomath) | +10 | 998 |
| 17 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +9 | 55009 |
| 18 | [every-app/open-seo](https://github.com/every-app/open-seo) | +8 | 3041 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +8 | 66383 |
| 20 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +7 | 2128 |
| 21 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 440 |
| 22 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +7 | 6494 |
| 23 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +7 | 25887 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +7 | 31525 |
| 25 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | +7 | 17384 |
| 26 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +6 | 9186 |
| 27 | [harborstremio/harbor](https://github.com/harborstremio/harbor) | +6 | 597 |
| 28 | [anbeime/skill](https://github.com/anbeime/skill) | +6 | 2565 |
| 29 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 41637 |
| 30 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +6 | 10923 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +413 | 51908 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +334 | 23480 |
| 3 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +249 | 9097 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +193 | 15498 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +177 | 42239 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +165 | 50079 |
| 7 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +140 | 5411 |
| 8 | [penpot/penpot](https://github.com/penpot/penpot) | +130 | 44370 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +127 | 51514 |
| 10 | [apple/container](https://github.com/apple/container) | +112 | 43662 |
| 11 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +109 | 21770 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +94 | 34462 |
| 13 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +82 | 23157 |
| 14 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +81 | 6494 |
| 15 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +73 | 55009 |
| 16 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +70 | 46922 |
| 17 | [EpicGames/lore](https://github.com/EpicGames/lore) | +70 | 6404 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +69 | 66383 |
| 19 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +69 | 32872 |
| 20 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +65 | 21287 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +63 | 32328 |
| 22 | [stablyai/orca](https://github.com/stablyai/orca) | +61 | 7892 |
| 23 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +60 | 10923 |
| 24 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +60 | 13133 |
| 25 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +60 | 31525 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +59 | 23544 |
| 27 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +58 | 61111 |
| 28 | [google-research/timesfm](https://github.com/google-research/timesfm) | +58 | 25653 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +53 | 9397 |
| 30 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +49 | 43973 |
| 31 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +46 | 3056 |
| 32 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +42 | 3362 |
| 33 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +42 | 1711 |
| 34 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +40 | 2128 |
| 35 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +40 | 5552 |
| 36 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +39 | 34684 |
| 37 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +39 | 21881 |
| 38 | [blader/humanizer](https://github.com/blader/humanizer) | +39 | 26266 |
| 39 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1240 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +37 | 41637 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +37 | 37127 |
| 42 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +36 | 35100 |
| 43 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +36 | 14786 |
| 44 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +35 | 2909 |
| 45 | [withastro/flue](https://github.com/withastro/flue) | +35 | 6800 |
| 46 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +33 | 36462 |
| 47 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +33 | 9186 |
| 48 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +32 | 2510 |
| 49 | [alibaba/zvec](https://github.com/alibaba/zvec) | +32 | 12506 |
| 50 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +30 | 2761 |
| 51 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +29 | 37263 |
| 52 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +28 | 28862 |
| 53 | [multica-ai/multica](https://github.com/multica-ai/multica) | +28 | 38176 |
| 54 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +28 | 1059 |
| 55 | [nubjs/nub](https://github.com/nubjs/nub) | +27 | 2172 |
| 56 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +27 | 25887 |
| 57 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +27 | 4996 |
| 58 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +27 | 7479 |
| 59 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +27 | 29405 |
| 60 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +27 | 5706 |
| 61 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +26 | 20200 |
| 62 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +26 | 6269 |
| 63 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +26 | 6827 |
| 64 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +26 | 5279 |
| 65 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +26 | 18185 |
| 66 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +25 | 31161 |
| 67 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +25 | 43032 |
| 68 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +24 | 7575 |
| 69 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +24 | 19930 |
| 70 | [aidenybai/cnfast](https://github.com/aidenybai/cnfast) | +24 | 959 |
| 71 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +23 | 10857 |
| 72 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +23 | 9234 |
| 73 | [vercel/eve](https://github.com/vercel/eve) | +23 | 2664 |
| 74 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +22 | 23301 |
| 75 | [anbeime/skill](https://github.com/anbeime/skill) | +22 | 2565 |
| 76 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +22 | 24213 |
| 77 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +22 | 1966 |
| 78 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 20170 |
| 79 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +21 | 383 |
| 80 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +21 | 11136 |
| 81 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +21 | 1619 |
| 82 | [revfactory/harness](https://github.com/revfactory/harness) | +20 | 7997 |
| 83 | [antirez/ds4](https://github.com/antirez/ds4) | +20 | 15770 |
| 84 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +20 | 8108 |
| 85 | [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil) | +20 | 6368 |
| 86 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +20 | 1272 |
| 87 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +19 | 1377 |
| 88 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +19 | 13421 |
| 89 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +19 | 12921 |
| 90 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +19 | 38356 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +18 | 29235 |
| 92 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +18 | 31796 |
| 93 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +18 | 23672 |
| 94 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +18 | 28654 |
| 95 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +18 | 22042 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +17 | 7949 |
| 97 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +17 | 5302 |
| 98 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | +17 | 17384 |
| 99 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +17 | 7378 |
| 100 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +17 | 25382 |
| 101 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +17 | 3969 |
| 102 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +17 | 16019 |
| 103 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +17 | 8815 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +16 | 17624 |
| 105 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +16 | 24115 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +16 | 19139 |
| 107 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +16 | 4601 |
| 108 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +16 | 8711 |
| 109 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 27207 |
| 110 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +14 | 4727 |
| 111 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +14 | 2520 |
| 112 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +14 | 2581 |
| 113 | [QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | +13 | 564 |
| 114 | [Project-N-E-K-O/N.E.K.O](https://github.com/Project-N-E-K-O/N.E.K.O) | +13 | 1818 |
| 115 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +12 | 41770 |
| 116 | [ksimback/looper](https://github.com/ksimback/looper) | +12 | 459 |
| 117 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +12 | 31345 |
| 118 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +12 | 7115 |
| 119 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +12 | 15384 |
| 120 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +12 | 565 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2606 | 78200 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1553 | 51908 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1393 | 59994 |
| 4 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1205 | 68326 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1200 | 51514 |
| 6 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1019 | 49621 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1012 | 55009 |
| 8 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +907 | 182799 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +853 | 46922 |
| 10 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +751 | 42239 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +671 | 67029 |
| 12 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +633 | 43973 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +590 | 36462 |
| 14 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +552 | 21881 |
| 15 | [apple/container](https://github.com/apple/container) | +479 | 43662 |
| 16 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +442 | 9397 |
| 17 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +421 | 12222 |
| 18 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +411 | 33479 |
| 19 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +404 | 10347 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +382 | 34684 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +376 | 31796 |
| 22 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +372 | 23480 |
| 23 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +364 | 10857 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +347 | 31525 |
| 25 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8238 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +336 | 41637 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +334 | 66383 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +324 | 23544 |
| 29 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +322 | 50079 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +320 | 32328 |
| 31 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +310 | 21770 |
| 32 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +305 | 10923 |
| 33 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +290 | 15500 |
| 34 | [roboflow/supervision](https://github.com/roboflow/supervision) | +276 | 36553 |
| 35 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +268 | 9097 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +267 | 14786 |
| 37 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +266 | 13133 |
| 38 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +247 | 4850 |
| 39 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +233 | 15066 |
| 40 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +225 | 16976 |
| 41 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4341 |
| 42 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5446 |
| 43 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +210 | 37127 |
| 44 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +210 | 35546 |
| 45 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +203 | 24115 |
| 46 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +199 | 32052 |
| 47 | [shadcn/improve](https://github.com/shadcn/improve) | +198 | 6269 |
| 48 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +196 | 29235 |
| 49 | [penpot/penpot](https://github.com/penpot/penpot) | +196 | 44370 |
| 50 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +194 | 6269 |
| 51 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +192 | 21907 |
| 52 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +189 | 5302 |
| 53 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +188 | 24213 |
| 54 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +186 | 19930 |
| 55 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +184 | 22042 |
| 56 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +182 | 27207 |
| 57 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +182 | 33010 |
| 58 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +179 | 12754 |
| 59 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +174 | 4476 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +173 | 61111 |
| 61 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +173 | 10145 |
| 62 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +172 | 6827 |
| 63 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +171 | 32615 |
| 64 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +171 | 31098 |
| 65 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +169 | 13421 |
| 66 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +169 | 11915 |
| 67 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +164 | 34462 |
| 68 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +164 | 31345 |
| 69 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +163 | 22085 |
| 70 | [blader/humanizer](https://github.com/blader/humanizer) | +162 | 26266 |
| 71 | [multica-ai/multica](https://github.com/multica-ai/multica) | +161 | 38176 |
| 72 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +161 | 5324 |
| 73 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +160 | 32872 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +158 | 19093 |
| 75 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +158 | 26007 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +157 | 35100 |
| 77 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +154 | 5279 |
| 78 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +153 | 3664 |
| 79 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +153 | 11136 |
| 80 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +149 | 5411 |
| 81 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +147 | 4996 |
| 82 | [revfactory/harness](https://github.com/revfactory/harness) | +147 | 7997 |
| 83 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +146 | 7462 |
| 84 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +145 | 25887 |
| 85 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +145 | 5676 |
| 86 | [google/skills](https://github.com/google/skills) | +144 | 14144 |
| 87 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +143 | 7479 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +143 | 40230 |
| 89 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +142 | 16019 |
| 90 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +140 | 39060 |
| 91 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +138 | 23672 |
| 92 | [google-research/timesfm](https://github.com/google-research/timesfm) | +137 | 25653 |
| 93 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +134 | 6494 |
| 94 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +133 | 23301 |
| 95 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +131 | 25507 |
| 96 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +130 | 21287 |
| 97 | [EpicGames/lore](https://github.com/EpicGames/lore) | +127 | 6404 |
| 98 | [stablyai/orca](https://github.com/stablyai/orca) | +126 | 7892 |
| 99 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +125 | 38464 |
| 100 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +124 | 38356 |
| 101 | [decolua/9router](https://github.com/decolua/9router) | +124 | 18532 |
| 102 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +124 | 29405 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +122 | 43904 |
| 104 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +119 | 21063 |
| 105 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +112 | 5175 |
| 106 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +110 | 7666 |
| 107 | [openai/plugins](https://github.com/openai/plugins) | +109 | 3604 |
| 108 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +107 | 49639 |
| 109 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +104 | 31161 |
| 110 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +104 | 4805 |
| 111 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +101 | 7378 |
| 112 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +101 | 14206 |
| 113 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +100 | 5298 |
| 114 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +99 | 10682 |
| 115 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +99 | 17352 |
| 116 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +98 | 23158 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +97 | 17624 |
| 118 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +95 | 41770 |
| 119 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +94 | 9186 |
| 120 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +94 | 35833 |
| 121 | [openai/skills](https://github.com/openai/skills) | +92 | 22905 |
| 122 | [soxoj/maigret](https://github.com/soxoj/maigret) | +92 | 33717 |
| 123 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +89 | 9881 |
| 124 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +89 | 4601 |
| 125 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +89 | 3761 |
| 126 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +88 | 3536 |
| 127 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +88 | 6701 |
| 128 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +83 | 4836 |
| 129 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +82 | 47381 |
| 130 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +80 | 24248 |
| 131 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 4727 |
| 132 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +78 | 3842 |
| 133 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +77 | 4629 |
| 134 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +76 | 19139 |
| 135 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +76 | 1698 |
| 136 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +76 | 25811 |
| 137 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +76 | 5345 |
| 138 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +74 | 7950 |
| 139 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +74 | 25382 |
| 140 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +73 | 20170 |
| 141 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +72 | 8815 |
| 142 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +72 | 4528 |
| 143 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +71 | 2273 |
| 144 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +70 | 2909 |
| 145 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +70 | 25158 |
| 146 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +69 | 6974 |
| 147 | [browser-act/skills](https://github.com/browser-act/skills) | +66 | 3051 |
| 148 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +65 | 12678 |
| 149 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +63 | 2739 |
| 150 | [jundot/omlx](https://github.com/jundot/omlx) | +63 | 17129 |
| 151 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +62 | 16872 |
| 152 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +62 | 23992 |
| 153 | [browser-use/video-use](https://github.com/browser-use/video-use) | +62 | 10327 |
| 154 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +61 | 7115 |
| 155 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +61 | 11691 |
| 156 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +60 | 18894 |
| 157 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 158 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +59 | 5992 |
| 159 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +58 | 2837 |
| 160 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +58 | 0 |
| 161 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +58 | 7942 |
| 162 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +58 | 36103 |
| 163 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +57 | 3278 |
| 164 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +57 | 3367 |
| 165 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +56 | 8784 |
| 166 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +56 | 16368 |
| 167 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +55 | 3547 |
| 168 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +53 | 44773 |
| 169 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +53 | 7578 |
| 170 | [anbeime/skill](https://github.com/anbeime/skill) | +52 | 2565 |
| 171 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +52 | 26091 |
| 172 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +52 | 18935 |
| 173 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +52 | 2022 |
| 174 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +51 | 15384 |
| 175 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +51 | 2581 |
| 176 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +51 | 4655 |
| 177 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +51 | 21686 |
| 178 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +50 | 1840 |
| 179 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +49 | 2761 |
| 180 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +49 | 7205 |
| 181 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +48 | 20153 |
| 182 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +48 | 4827 |
| 183 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +47 | 3353 |
| 184 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +47 | 8036 |
| 185 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +47 | 17222 |
| 186 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +46 | 1801 |
| 187 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +45 | 3056 |
| 188 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1155 |
| 189 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +45 | 37564 |
| 190 | [floci-io/floci](https://github.com/floci-io/floci) | +43 | 14457 |
| 191 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +42 | 1711 |
| 192 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +42 | 3139 |
| 193 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +40 | 1240 |
| 194 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +36 | 5339 |
| 195 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +36 | 5860 |
| 196 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +35 | 882 |
| 197 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +35 | 1945 |
| 198 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +33 | 5877 |
| 199 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +32 | 1114 |
| 200 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +32 | 1252 |
| 201 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +32 | 8373 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +32 | 7898 |
| 203 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +32 | 4100 |
| 204 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +31 | 9458 |
| 205 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +30 | 28357 |
| 206 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +29 | 1883 |
| 207 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +28 | 3934 |
| 208 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +26 | 813 |
| 209 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +26 | 699 |
| 210 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +25 | 5522 |
| 211 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +24 | 1243 |
| 212 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +24 | 2401 |
| 213 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +24 | 13885 |
| 214 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +23 | 1710 |
| 215 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +23 | 11409 |
| 216 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 28 |
| 217 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +22 | 354 |
| 218 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +22 | 1089 |
| 219 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +22 | 4935 |
| 220 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +22 | 2897 |
| 221 | [zzzhhh1/free-nodes](https://github.com/zzzhhh1/free-nodes) | +21 | 0 |
| 222 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +21 | 383 |
| 223 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +21 | 3988 |
| 224 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 578 |
| 225 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +21 | 821 |
| 226 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 542 |
| 227 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 996 |
| 228 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +19 | 926 |
| 229 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +19 | 5399 |
| 230 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +19 | 2377 |
| 231 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1430 |
| 232 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +18 | 588 |
| 233 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +18 | 1110 |
| 234 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 533 |
| 235 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +17 | 2021 |
| 236 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +17 | 4609 |
| 237 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +17 | 856 |
| 238 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +17 | 467 |
| 239 | [robinebers/openusage](https://github.com/robinebers/openusage) | +16 | 3012 |
| 240 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +15 | 510 |
| 241 | [paraschopra/make-pages-interactive](https://github.com/paraschopra/make-pages-interactive) | +15 | 468 |
| 242 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +15 | 2668 |
| 243 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 445 |
| 244 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +14 | 1316 |
| 245 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2446 |
| 246 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +14 | 296 |
| 247 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 438 |
| 248 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +14 | 396 |
| 249 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +14 | 8327 |
| 250 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +14 | 2480 |
| 251 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +13 | 12191 |
| 252 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +13 | 0 |
| 253 | [Shiyao-Huang/awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) | +13 | 168 |
| 254 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 447 |
| 255 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +13 | 2253 |
| 256 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 574 |
| 257 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 312 |
| 258 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +12 | 2044 |
| 259 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +12 | 1523 |
| 260 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +12 | 253 |
| 261 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 262 |
| 262 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +12 | 2607 |
| 263 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +11 | 1183 |
| 264 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +10 | 4574 |
| 265 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3077 |
| 266 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +9 | 1221 |
| 267 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +9 | 440 |
| 268 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +9 | 2185 |
| 269 | [fcompc4/ecommerce-kushi](https://github.com/fcompc4/ecommerce-kushi) | +9 | 213 |
| 270 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3607 |
| 271 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 195 |
| 272 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +9 | 1710 |
| 273 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 369 |
| 274 | [emollick/concord](https://github.com/emollick/concord) | +8 | 196 |
| 275 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +8 | 1030 |
| 276 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +8 | 664 |
| 277 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2647 |
| 278 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 227 |
| 279 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 180 |
| 280 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +7 | 2541 |
| 281 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2638 |
| 282 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +7 | 1634 |
| 283 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2711 |
| 284 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +6 | 338 |
| 285 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 168 |
| 286 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +5 | 222 |
| 287 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 110 |
| 288 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 492 |
| 289 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 563 |
| 290 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +5 | 276 |
| 291 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +4 | 132 |
| 292 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 256 |
| 293 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +4 | 930 |
| 294 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 511 |
| 295 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 216 |
| 296 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +3 | 313 |
| 297 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 178 |
| 298 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +3 | 2179 |
| 299 | [sfee1212/moyutv](https://github.com/sfee1212/moyutv) | +3 | 42 |
| 300 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 412 |
