---
title: "2026-06-25 GitHub增长趋势报告"
description: "1.OpenMontage+103 2.reverse-skill+41 3.Agent-Reach+40 4.daily_stock_analysis+34 5.orca+28"
date: 2026-06-25T21:44:44+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-25 21:44:44

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
        'daily': {"categories": ["fivetaku/insane-search", "jamiepine/voicebox", "mukul975/Anthropic-Cybersecurity-Skills", "mvanhorn/last30days-skill", "googleworkspace/cli", "rtk-ai/rtk", "colbymchenry/codegraph", "tashfeenahmed/freellmapi", "bozhouDev/codex-orange-book", "DeusData/codebase-memory-mcp", "interviewstreet/hiring-agent", "Leonxlnx/taste-skill", "JCodesMore/ai-website-cloner-template", "kunchenguid/no-mistakes", "chopratejas/headroom", "stablyai/orca", "ZhuLinsen/daily_stock_analysis", "Panniantong/Agent-Reach", "zhaoxuya520/reverse-skill", "calesthio/OpenMontage"], "data": [11, 11, 13, 13, 14, 14, 15, 15, 19, 21, 21, 23, 25, 26, 28, 28, 34, 40, 41, 103]},
        'weekly': {"categories": ["tursodatabase/turso", "topoteretes/cognee", "mvanhorn/last30days-skill", "Kilo-Org/kilocode", "colbymchenry/codegraph", "zhaoxuya520/reverse-skill", "google-research/timesfm", "EpicGames/lore", "jamiepine/voicebox", "mukul975/Anthropic-Cybersecurity-Skills", "apple/container", "Leonxlnx/taste-skill", "penpot/penpot", "StarTrail-org/PixelRAG", "ZhuLinsen/daily_stock_analysis", "Panniantong/Agent-Reach", "DeusData/codebase-memory-mcp", "palmier-io/palmier-pro", "calesthio/OpenMontage", "chopratejas/headroom"], "data": [64, 65, 65, 67, 67, 71, 75, 75, 82, 83, 88, 112, 114, 130, 132, 165, 179, 235, 285, 423]},
        'monthly': {"categories": ["unicity-astrid/astrid", "lfnovo/open-notebook", "Imbad0202/academic-research-skills", "RyanCodrai/turbovec", "alibaba/open-code-review", "apple/container", "BigPizzaV3/CodexPlusPlus", "elder-plinius/CL4R1T4S", "addyosmani/agent-skills", "rohitg00/ai-engineering-from-scratch", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "forrestchang/andrej-karpathy-skills", "harry0703/MoneyPrinterTurbo", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "DietrichGebert/ponytail", "Egonex-AI/Understand-Anything", "chopratejas/headroom", "pewdiepie-archdaemon/odysseus"], "data": [403, 409, 424, 428, 435, 454, 574, 630, 674, 723, 732, 851, 1029, 1066, 1217, 1251, 1303, 1475, 1516, 2594]}
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
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +103 | 21925 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +41 | 6310 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +40 | 41112 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +34 | 49465 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +28 | 7377 |
| 6 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +28 | 50905 |
| 7 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +26 | 2996 |
| 8 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 20331 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +23 | 50934 |
| 10 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +21 | 2720 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +21 | 14704 |
| 12 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +19 | 1920 |
| 13 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +15 | 12641 |
| 14 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +15 | 54553 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +14 | 66103 |
| 16 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +14 | 28666 |
| 17 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +13 | 46695 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +13 | 21147 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +11 | 34174 |
| 20 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +11 | 1245 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +10 | 31315 |
| 22 | [revfactory/harness](https://github.com/revfactory/harness) | +10 | 7939 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +9 | 41405 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 23267 |
| 25 | [xushanpei/open-file-viewer](https://github.com/xushanpei/open-file-viewer) | +8 | 556 |
| 26 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +8 | 5310 |
| 27 | [ziguishian/xhs-visual-director-skill](https://github.com/ziguishian/xhs-visual-director-skill) | +7 | 793 |
| 28 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +7 | 9274 |
| 29 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 1792 |
| 30 | [nubjs/nub](https://github.com/nubjs/nub) | +7 | 2035 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +423 | 50905 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +285 | 21925 |
| 3 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +235 | 8963 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +179 | 14704 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +165 | 41113 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +132 | 49465 |
| 7 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +130 | 5310 |
| 8 | [penpot/penpot](https://github.com/penpot/penpot) | +114 | 44370 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +112 | 50934 |
| 10 | [apple/container](https://github.com/apple/container) | +88 | 43148 |
| 11 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +83 | 21147 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +82 | 34174 |
| 13 | [EpicGames/lore](https://github.com/EpicGames/lore) | +75 | 6147 |
| 14 | [google-research/timesfm](https://github.com/google-research/timesfm) | +75 | 25559 |
| 15 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +71 | 6310 |
| 16 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +67 | 54553 |
| 17 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +67 | 24612 |
| 18 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +65 | 46695 |
| 19 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +65 | 22434 |
| 20 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | +64 | 22181 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +60 | 66103 |
| 22 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +54 | 32872 |
| 23 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +52 | 10657 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +51 | 31315 |
| 25 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +51 | 43874 |
| 26 | [stablyai/orca](https://github.com/stablyai/orca) | +48 | 7377 |
| 27 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +48 | 9274 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +47 | 23267 |
| 29 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +46 | 20331 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +45 | 31349 |
| 31 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +44 | 12641 |
| 32 | [withastro/flue](https://github.com/withastro/flue) | +42 | 6697 |
| 33 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +39 | 36985 |
| 34 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +38 | 1656 |
| 35 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +36 | 5481 |
| 36 | [blader/humanizer](https://github.com/blader/humanizer) | +34 | 26140 |
| 37 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +33 | 1920 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +33 | 41405 |
| 39 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +32 | 60448 |
| 40 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +32 | 2996 |
| 41 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +32 | 36353 |
| 42 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +32 | 34461 |
| 43 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +32 | 1235 |
| 44 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +32 | 5164 |
| 45 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +31 | 21666 |
| 46 | [alibaba/zvec](https://github.com/alibaba/zvec) | +31 | 12449 |
| 47 | [vercel/eve](https://github.com/vercel/eve) | +31 | 2592 |
| 48 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 34995 |
| 49 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +29 | 2720 |
| 50 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +29 | 14634 |
| 51 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +28 | 2319 |
| 52 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +28 | 2649 |
| 53 | [nubjs/nub](https://github.com/nubjs/nub) | +27 | 2035 |
| 54 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +26 | 4898 |
| 55 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +26 | 6774 |
| 56 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +26 | 1612 |
| 57 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +25 | 37162 |
| 58 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +25 | 8981 |
| 59 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +24 | 6136 |
| 60 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +24 | 20111 |
| 61 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +23 | 28666 |
| 62 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +23 | 31109 |
| 63 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +23 | 25734 |
| 64 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +23 | 29332 |
| 65 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +23 | 1072 |
| 66 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +22 | 42965 |
| 67 | [aidenybai/cnfast](https://github.com/aidenybai/cnfast) | +22 | 927 |
| 68 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +22 | 18101 |
| 69 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +21 | 1033 |
| 70 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +21 | 11057 |
| 71 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +21 | 7321 |
| 72 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +21 | 5662 |
| 73 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +20 | 10740 |
| 74 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +20 | 12826 |
| 75 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +20 | 1260 |
| 76 | [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil) | +20 | 6312 |
| 77 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +19 | 363 |
| 78 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +19 | 1792 |
| 79 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +19 | 1909 |
| 80 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +19 | 9035 |
| 81 | [multica-ai/multica](https://github.com/multica-ai/multica) | +19 | 38028 |
| 82 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +19 | 24100 |
| 83 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +19 | 8042 |
| 84 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +19 | 13274 |
| 85 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +19 | 21962 |
| 86 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +19 | 3346 |
| 87 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +18 | 19769 |
| 88 | [overflowy/make-look-scanned](https://github.com/overflowy/make-look-scanned) | +18 | 415 |
| 89 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +17 | 23039 |
| 90 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +17 | 28600 |
| 91 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +17 | 8754 |
| 92 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +16 | 1245 |
| 93 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +16 | 7337 |
| 94 | [decolua/9router](https://github.com/decolua/9router) | +16 | 18465 |
| 95 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 15965 |
| 96 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +16 | 23602 |
| 97 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +15 | 17567 |
| 98 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +15 | 31694 |
| 99 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +15 | 38209 |
| 100 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 27140 |
| 101 | [revfactory/harness](https://github.com/revfactory/harness) | +14 | 7939 |
| 102 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +14 | 24046 |
| 103 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +14 | 8690 |
| 104 | [anbeime/skill](https://github.com/anbeime/skill) | +13 | 2487 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +13 | 19065 |
| 106 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +12 | 2542 |
| 107 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +12 | 2681 |
| 108 | [Project-N-E-K-O/N.E.K.O](https://github.com/Project-N-E-K-O/N.E.K.O) | +12 | 1800 |
| 109 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +12 | 2316 |
| 110 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +11 | 9780 |
| 111 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +11 | 7844 |
| 112 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +11 | 3746 |
| 113 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +11 | 4657 |
| 114 | [RUC-NLPIR/Arbor](https://github.com/RUC-NLPIR/Arbor) | +11 | 753 |
| 115 | [kernalix7/winpodx](https://github.com/kernalix7/winpodx) | +11 | 1303 |
| 116 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +11 | 532 |
| 117 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +10 | 25121 |
| 118 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +10 | 7080 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +10 | 43814 |
| 120 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 7521 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2594 | 77843 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1516 | 50905 |
| 3 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1475 | 67916 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1303 | 57848 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1251 | 50934 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1217 | 54553 |
| 7 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1066 | 49621 |
| 8 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1029 | 182215 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +851 | 46695 |
| 10 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +732 | 41113 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +723 | 36353 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +674 | 66749 |
| 13 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +630 | 43874 |
| 14 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +574 | 21666 |
| 15 | [apple/container](https://github.com/apple/container) | +454 | 43148 |
| 16 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +435 | 9274 |
| 17 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +428 | 12197 |
| 18 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +424 | 34461 |
| 19 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +409 | 33322 |
| 20 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +403 | 10354 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +373 | 31694 |
| 22 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +359 | 10740 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +350 | 23267 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +349 | 31315 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +348 | 66103 |
| 26 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8244 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +342 | 41405 |
| 28 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +328 | 21147 |
| 29 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +322 | 21925 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +314 | 31349 |
| 31 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +293 | 49465 |
| 32 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +293 | 10657 |
| 33 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +291 | 21962 |
| 34 | [roboflow/supervision](https://github.com/roboflow/supervision) | +275 | 36553 |
| 35 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +274 | 12642 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +272 | 14634 |
| 37 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +259 | 14704 |
| 38 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +246 | 4815 |
| 39 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +245 | 8963 |
| 40 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +245 | 15025 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +233 | 36986 |
| 42 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +224 | 16939 |
| 43 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +222 | 24046 |
| 44 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +215 | 32961 |
| 45 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4347 |
| 46 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5447 |
| 47 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +210 | 29103 |
| 48 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +208 | 35512 |
| 49 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +204 | 27140 |
| 50 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +203 | 12721 |
| 51 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +201 | 21863 |
| 52 | [shadcn/improve](https://github.com/shadcn/improve) | +197 | 6206 |
| 53 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +196 | 31994 |
| 54 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +196 | 10024 |
| 55 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +195 | 24100 |
| 56 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +191 | 6136 |
| 57 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +184 | 19769 |
| 58 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +184 | 5251 |
| 59 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +182 | 32544 |
| 60 | [penpot/penpot](https://github.com/penpot/penpot) | +179 | 44370 |
| 61 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +177 | 31266 |
| 62 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +176 | 6774 |
| 63 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +174 | 4462 |
| 64 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +172 | 5661 |
| 65 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +171 | 13274 |
| 66 | [multica-ai/multica](https://github.com/multica-ai/multica) | +171 | 38028 |
| 67 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +171 | 31098 |
| 68 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +170 | 11881 |
| 69 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +168 | 18954 |
| 70 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +168 | 22031 |
| 71 | [blader/humanizer](https://github.com/blader/humanizer) | +165 | 26140 |
| 72 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +165 | 27485 |
| 73 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +163 | 34174 |
| 74 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +163 | 39012 |
| 75 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +161 | 5308 |
| 76 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +161 | 25952 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +159 | 34995 |
| 78 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +157 | 60448 |
| 79 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +154 | 23602 |
| 80 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +152 | 5164 |
| 81 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3607 |
| 82 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +152 | 11057 |
| 83 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +148 | 25478 |
| 84 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +147 | 6310 |
| 85 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +147 | 7321 |
| 86 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +146 | 7426 |
| 87 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +145 | 4898 |
| 88 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +145 | 32872 |
| 89 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +145 | 25734 |
| 90 | [google/skills](https://github.com/google/skills) | +144 | 14115 |
| 91 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +143 | 15965 |
| 92 | [revfactory/harness](https://github.com/revfactory/harness) | +142 | 7939 |
| 93 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +140 | 43814 |
| 94 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +138 | 5310 |
| 95 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +137 | 23039 |
| 96 | [decolua/9router](https://github.com/decolua/9router) | +136 | 18465 |
| 97 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +136 | 29332 |
| 98 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +136 | 6693 |
| 99 | [google-research/timesfm](https://github.com/google-research/timesfm) | +134 | 25559 |
| 100 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +134 | 38385 |
| 101 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +126 | 20762 |
| 102 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +124 | 5092 |
| 103 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +123 | 38209 |
| 104 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +123 | 31109 |
| 105 | [EpicGames/lore](https://github.com/EpicGames/lore) | +116 | 6147 |
| 106 | [stablyai/orca](https://github.com/stablyai/orca) | +116 | 7377 |
| 107 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +114 | 20331 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +114 | 7607 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +111 | 4759 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +111 | 17567 |
| 111 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +110 | 14169 |
| 112 | [openai/plugins](https://github.com/openai/plugins) | +110 | 3550 |
| 113 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +109 | 17320 |
| 114 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +108 | 49619 |
| 115 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +107 | 7337 |
| 116 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +105 | 5273 |
| 117 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +103 | 10644 |
| 118 | [soxoj/maigret](https://github.com/soxoj/maigret) | +102 | 33665 |
| 119 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +98 | 35743 |
| 120 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +95 | 3724 |
| 121 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +93 | 41702 |
| 122 | [openai/skills](https://github.com/openai/skills) | +93 | 22867 |
| 123 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +91 | 3514 |
| 124 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +89 | 8981 |
| 125 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +88 | 4769 |
| 126 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +87 | 9780 |
| 127 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +83 | 4535 |
| 128 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +82 | 47296 |
| 129 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +81 | 22434 |
| 130 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +81 | 4518 |
| 131 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +81 | 24177 |
| 132 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +80 | 4621 |
| 133 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3813 |
| 134 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +79 | 6926 |
| 135 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +77 | 8754 |
| 136 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +77 | 25763 |
| 137 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +76 | 25273 |
| 138 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +75 | 19065 |
| 139 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +75 | 1690 |
| 140 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +74 | 4657 |
| 141 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +74 | 2719 |
| 142 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +73 | 20111 |
| 143 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +73 | 25121 |
| 144 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +73 | 7844 |
| 145 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +72 | 11638 |
| 146 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +72 | 5300 |
| 147 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +71 | 2252 |
| 148 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +69 | 12629 |
| 149 | [jundot/omlx](https://github.com/jundot/omlx) | +68 | 17093 |
| 150 | [browser-act/skills](https://github.com/browser-act/skills) | +67 | 2969 |
| 151 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +66 | 4645 |
| 152 | [browser-use/video-use](https://github.com/browser-use/video-use) | +65 | 10186 |
| 153 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +64 | 2720 |
| 154 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +63 | 23948 |
| 155 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +63 | 5932 |
| 156 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +62 | 7080 |
| 157 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +62 | 16837 |
| 158 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +62 | 0 |
| 159 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +62 | 7916 |
| 160 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +62 | 18842 |
| 161 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +61 | 2797 |
| 162 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 163 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +59 | 16333 |
| 164 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +58 | 7176 |
| 165 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +58 | 36103 |
| 166 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +57 | 3232 |
| 167 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +57 | 3335 |
| 168 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +57 | 8773 |
| 169 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +56 | 44737 |
| 170 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +55 | 7521 |
| 171 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +55 | 21634 |
| 172 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +54 | 15350 |
| 173 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +54 | 18901 |
| 174 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +54 | 3507 |
| 175 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +53 | 4780 |
| 176 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +52 | 2542 |
| 177 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +51 | 26047 |
| 178 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +51 | 1995 |
| 179 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +50 | 28980 |
| 180 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +50 | 1838 |
| 181 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +50 | 20119 |
| 182 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +48 | 7994 |
| 183 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +48 | 37564 |
| 184 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +47 | 3303 |
| 185 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +47 | 1793 |
| 186 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +46 | 2649 |
| 187 | [floci-io/floci](https://github.com/floci-io/floci) | +46 | 14435 |
| 188 | [anbeime/skill](https://github.com/anbeime/skill) | +45 | 2487 |
| 189 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +45 | 4501 |
| 190 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1148 |
| 191 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +42 | 5848 |
| 192 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +40 | 3045 |
| 193 | [88lin/video_vip](https://github.com/88lin/video_vip) | +40 | 4223 |
| 194 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +38 | 3936 |
| 195 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +37 | 5310 |
| 196 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +36 | 1656 |
| 197 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +36 | 1097 |
| 198 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +35 | 1918 |
| 199 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +34 | 868 |
| 200 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +34 | 1108 |
| 201 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +33 | 5854 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +33 | 7868 |
| 203 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +33 | 693 |
| 204 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +32 | 28331 |
| 205 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +32 | 1855 |
| 206 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +31 | 1226 |
| 207 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +31 | 8341 |
| 208 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +31 | 4078 |
| 209 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +30 | 9450 |
| 210 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +28 | 5505 |
| 211 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +25 | 804 |
| 212 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +25 | 1701 |
| 213 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +24 | 1237 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +24 | 2395 |
| 215 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +24 | 4932 |
| 216 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +24 | 2886 |
| 217 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +23 | 1046 |
| 218 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 28 |
| 219 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +22 | 3954 |
| 220 | [zzzhhh1/free-nodes](https://github.com/zzzhhh1/free-nodes) | +21 | 0 |
| 221 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 575 |
| 222 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +21 | 11389 |
| 223 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +21 | 819 |
| 224 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +21 | 13878 |
| 225 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 530 |
| 226 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 994 |
| 227 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +19 | 363 |
| 228 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +19 | 5386 |
| 229 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1425 |
| 230 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +19 | 856 |
| 231 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +18 | 331 |
| 232 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +18 | 2002 |
| 233 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 526 |
| 234 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +17 | 2361 |
| 235 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +17 | 4598 |
| 236 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +17 | 1506 |
| 237 | [robinebers/openusage](https://github.com/robinebers/openusage) | +17 | 2966 |
| 238 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +17 | 465 |
| 239 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +16 | 886 |
| 240 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +16 | 1312 |
| 241 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +15 | 2037 |
| 242 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 439 |
| 243 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +14 | 500 |
| 244 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +14 | 536 |
| 245 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2425 |
| 246 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +14 | 397 |
| 247 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +14 | 8310 |
| 248 | [paraschopra/make-pages-interactive](https://github.com/paraschopra/make-pages-interactive) | +14 | 466 |
| 249 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +14 | 2655 |
| 250 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +14 | 2247 |
| 251 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +14 | 2478 |
| 252 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +13 | 0 |
| 253 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +13 | 2177 |
| 254 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +13 | 1178 |
| 255 | [Shiyao-Huang/awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) | +13 | 168 |
| 256 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 444 |
| 257 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +13 | 2589 |
| 258 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 574 |
| 259 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 310 |
| 260 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +12 | 12180 |
| 261 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +12 | 424 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +12 | 4563 |
| 263 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 261 |
| 264 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +12 | 1743 |
| 265 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +12 | 2846 |
| 266 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +12 | 767 |
| 267 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +11 | 243 |
| 268 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +11 | 721 |
| 269 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3077 |
| 270 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +9 | 368 |
| 271 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +9 | 1212 |
| 272 | [fcompc4/ecommerce-kushi](https://github.com/fcompc4/ecommerce-kushi) | +9 | 212 |
| 273 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3595 |
| 274 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +9 | 663 |
| 275 | [emollick/concord](https://github.com/emollick/concord) | +8 | 194 |
| 276 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 191 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +8 | 1702 |
| 278 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2637 |
| 279 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 227 |
| 280 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 175 |
| 281 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2634 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2711 |
| 283 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +6 | 1631 |
| 284 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +6 | 274 |
| 285 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +6 | 336 |
| 286 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 166 |
| 287 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +5 | 223 |
| 288 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 110 |
| 289 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2531 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +5 | 2175 |
| 291 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +5 | 923 |
| 292 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 561 |
| 293 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 487 |
| 294 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 215 |
| 295 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 507 |
| 296 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +4 | 155 |
| 297 | [openmemind/memind](https://github.com/openmemind/memind) | +4 | 901 |
| 298 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 172 |
| 299 | [sfee1212/moyutv](https://github.com/sfee1212/moyutv) | +3 | 42 |
| 300 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +3 | 255 |
