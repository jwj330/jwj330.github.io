---
title: "2026-06-21 GitHub增长趋势报告"
description: "1.ponytail+157 2.headroom+140 3.codebase-memory-mcp+64 4.Agent-Reach+55 5.penpot+49"
date: 2026-06-21T21:15:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-21 21:15:54

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
        'daily': {"categories": ["Imbad0202/academic-research-skills", "Yuan1z0825/nature-skills", "heygen-com/hyperframes", "mvanhorn/last30days-skill", "Alishahryar1/free-claude-code", "colbymchenry/codegraph", "NVIDIA/SkillSpector", "playRealmRumble/Realm-Rumble", "rtk-ai/rtk", "mukul975/Anthropic-Cybersecurity-Skills", "jamiepine/voicebox", "lvy010/X-Plore", "ZhuLinsen/daily_stock_analysis", "Leonxlnx/taste-skill", "calesthio/OpenMontage", "penpot/penpot", "Panniantong/Agent-Reach", "DeusData/codebase-memory-mcp", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [14, 16, 16, 17, 17, 17, 18, 18, 20, 22, 24, 24, 29, 33, 47, 49, 55, 64, 140, 157]},
        'weekly': {"categories": ["apple/container", "Kilo-Org/kilocode", "rtk-ai/rtk", "hugohe3/ppt-master", "rohitg00/ai-engineering-from-scratch", "tamnd/kage", "calesthio/OpenMontage", "omnigent-ai/omnigent", "penpot/penpot", "mvanhorn/last30days-skill", "GoogleCloudPlatform/knowledge-catalog", "NVIDIA/SkillSpector", "colbymchenry/codegraph", "EpicGames/lore", "google-research/timesfm", "Leonxlnx/taste-skill", "DeusData/codebase-memory-mcp", "Panniantong/Agent-Reach", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [58, 62, 62, 63, 65, 72, 73, 80, 84, 91, 95, 98, 101, 103, 107, 134, 166, 231, 394, 962]},
        'monthly': {"categories": ["D4Vinci/Scrapling", "mukul975/Anthropic-Cybersecurity-Skills", "tinyhumansai/openhuman", "Panniantong/Agent-Reach", "addyosmani/agent-skills", "Imbad0202/academic-research-skills", "anthropics/claude-plugins-official", "mvanhorn/last30days-skill", "safishamsi/graphify", "harry0703/MoneyPrinterTurbo", "DietrichGebert/ponytail", "farion1231/cc-switch", "Leonxlnx/taste-skill", "chopratejas/headroom", "rohitg00/ai-engineering-from-scratch", "mattpocock/skills", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "pewdiepie-archdaemon/odysseus", "Egonex-AI/Understand-Anything"], "data": [537, 539, 595, 671, 746, 777, 809, 849, 932, 1066, 1069, 1179, 1286, 1382, 1551, 1726, 2236, 2505, 2556, 2964]}
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
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +157 | 45678 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +140 | 44033 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +64 | 10158 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +55 | 36759 |
| 5 | [penpot/penpot](https://github.com/penpot/penpot) | +49 | 44370 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +47 | 8430 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +33 | 48337 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +29 | 44338 |
| 9 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +24 | 1017 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +24 | 31565 |
| 11 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +22 | 17573 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +20 | 64544 |
| 13 | [playRealmRumble/Realm-Rumble](https://github.com/playRealmRumble/Realm-Rumble) | +18 | 694 |
| 14 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +18 | 8995 |
| 15 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +17 | 52579 |
| 16 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +17 | 36108 |
| 17 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +17 | 45337 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +16 | 29412 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +16 | 21777 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +14 | 33352 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +14 | 11317 |
| 22 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +13 | 8209 |
| 23 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +13 | 17805 |
| 24 | [EpicGames/lore](https://github.com/EpicGames/lore) | +13 | 5398 |
| 25 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +12 | 207 |
| 26 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +12 | 4969 |
| 27 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +12 | 8469 |
| 28 | [withastro/flue](https://github.com/withastro/flue) | +12 | 6275 |
| 29 | [blader/humanizer](https://github.com/blader/humanizer) | +12 | 25361 |
| 30 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +11 | 57997 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +962 | 45678 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +394 | 44034 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +231 | 36759 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +166 | 10158 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +134 | 48337 |
| 6 | [google-research/timesfm](https://github.com/google-research/timesfm) | +107 | 24853 |
| 7 | [EpicGames/lore](https://github.com/EpicGames/lore) | +103 | 5398 |
| 8 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +101 | 52579 |
| 9 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +98 | 8995 |
| 10 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +95 | 4621 |
| 11 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +91 | 45337 |
| 12 | [penpot/penpot](https://github.com/penpot/penpot) | +84 | 44370 |
| 13 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +80 | 4305 |
| 14 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +73 | 8430 |
| 15 | [tamnd/kage](https://github.com/tamnd/kage) | +72 | 2223 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +65 | 35304 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +63 | 29876 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +62 | 64544 |
| 19 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +62 | 23614 |
| 20 | [apple/container](https://github.com/apple/container) | +58 | 39253 |
| 21 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +54 | 36108 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +53 | 21777 |
| 23 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +52 | 33352 |
| 24 | [shadcn/improve](https://github.com/shadcn/improve) | +52 | 5867 |
| 25 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +52 | 32323 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +51 | 44338 |
| 27 | [alibaba/zvec](https://github.com/alibaba/zvec) | +51 | 11952 |
| 28 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +50 | 10174 |
| 29 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +48 | 31181 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +47 | 29412 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +45 | 40012 |
| 32 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +45 | 32872 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +44 | 8209 |
| 34 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | +43 | 20740 |
| 35 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +42 | 17573 |
| 36 | [vercel/eve](https://github.com/vercel/eve) | +40 | 2026 |
| 37 | [blader/humanizer](https://github.com/blader/humanizer) | +40 | 25362 |
| 38 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +39 | 13848 |
| 39 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +38 | 57997 |
| 40 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +38 | 11317 |
| 41 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +37 | 19718 |
| 42 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +34 | 31565 |
| 43 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +34 | 4969 |
| 44 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +34 | 30845 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 34442 |
| 46 | [withastro/flue](https://github.com/withastro/flue) | +32 | 6276 |
| 47 | [getkimchi/kimchi](https://github.com/getkimchi/kimchi) | +31 | 1841 |
| 48 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +31 | 4322 |
| 49 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +31 | 7180 |
| 50 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +30 | 23242 |
| 51 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +28 | 5525 |
| 52 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +28 | 5089 |
| 53 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +26 | 2090 |
| 54 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +26 | 23670 |
| 55 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +26 | 9692 |
| 56 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +25 | 32137 |
| 57 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +25 | 19362 |
| 58 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +24 | 1017 |
| 59 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +24 | 1494 |
| 60 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +24 | 21630 |
| 61 | [antirez/ds4](https://github.com/antirez/ds4) | +24 | 14874 |
| 62 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +24 | 26785 |
| 63 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +23 | 732 |
| 64 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +23 | 28953 |
| 65 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +23 | 6631 |
| 66 | [stablyai/orca](https://github.com/stablyai/orca) | +23 | 5783 |
| 67 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +23 | 22130 |
| 68 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +23 | 15653 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +22 | 25313 |
| 70 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +22 | 16800 |
| 71 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +21 | 17805 |
| 72 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +21 | 12328 |
| 73 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +21 | 5311 |
| 74 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +21 | 1292 |
| 75 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +21 | 8274 |
| 76 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +21 | 711 |
| 77 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +21 | 25170 |
| 78 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +21 | 43554 |
| 79 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +21 | 4669 |
| 80 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +20 | 36667 |
| 81 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +20 | 12899 |
| 82 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +20 | 28432 |
| 83 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +20 | 538 |
| 84 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +19 | 8469 |
| 85 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +19 | 23104 |
| 86 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 4326 |
| 87 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +19 | 6744 |
| 88 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +19 | 21856 |
| 89 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +19 | 22419 |
| 90 | [playRealmRumble/Realm-Rumble](https://github.com/playRealmRumble/Realm-Rumble) | +18 | 694 |
| 91 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +18 | 2271 |
| 92 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +18 | 38022 |
| 93 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +18 | 1215 |
| 94 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +18 | 12796 |
| 95 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +18 | 28573 |
| 96 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +17 | 10569 |
| 97 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +17 | 41314 |
| 98 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +16 | 42626 |
| 99 | [microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach) | +16 | 2855 |
| 100 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +16 | 7616 |
| 101 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +16 | 1467 |
| 102 | [RUC-NLPIR/Arbor](https://github.com/RUC-NLPIR/Arbor) | +15 | 596 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +15 | 18703 |
| 104 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +15 | 37737 |
| 105 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +15 | 7810 |
| 106 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +15 | 0 |
| 107 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +14 | 7246 |
| 108 | [learningCatHD/telos-sdk](https://github.com/learningCatHD/telos-sdk) | +14 | 0 |
| 109 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +13 | 207 |
| 110 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +13 | 30555 |
| 111 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +13 | 23723 |
| 112 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +13 | 884 |
| 113 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +12 | 2213 |
| 114 | [microsoft/fastcontext](https://github.com/microsoft/fastcontext) | +12 | 754 |
| 115 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +12 | 4512 |
| 116 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +12 | 3549 |
| 117 | [baskduf/FableCodex](https://github.com/baskduf/FableCodex) | +12 | 355 |
| 118 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +11 | 3304 |
| 119 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +11 | 8512 |
| 120 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +11 | 6865 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2964 | 65296 |
| 2 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2556 | 75663 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2505 | 52579 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2236 | 179666 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1726 | 139572 |
| 6 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1551 | 35304 |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1382 | 44034 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1286 | 48337 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1179 | 105653 |
| 10 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1069 | 45680 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1066 | 49621 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +932 | 70261 |
| 13 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +849 | 45337 |
| 14 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +809 | 30555 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +777 | 33352 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +746 | 64712 |
| 17 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +671 | 36759 |
| 18 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +595 | 32748 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +539 | 17573 |
| 20 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +537 | 65367 |
| 21 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +531 | 21630 |
| 22 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +531 | 26785 |
| 23 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +524 | 12054 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +475 | 64544 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +475 | 21777 |
| 26 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +471 | 36108 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +454 | 29876 |
| 28 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +452 | 23605 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +436 | 13848 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +432 | 11317 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +413 | 29413 |
| 32 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +413 | 40012 |
| 33 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +404 | 31181 |
| 34 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +403 | 8209 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +397 | 37363 |
| 36 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9340 |
| 37 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +394 | 32323 |
| 38 | [apple/container](https://github.com/apple/container) | +387 | 39253 |
| 39 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +386 | 4573 |
| 40 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +365 | 27258 |
| 41 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +348 | 10174 |
| 42 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8245 |
| 43 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +340 | 22595 |
| 44 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +330 | 38792 |
| 45 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +294 | 14803 |
| 46 | [roboflow/supervision](https://github.com/roboflow/supervision) | +294 | 36553 |
| 47 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +287 | 28573 |
| 48 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +287 | 32137 |
| 49 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +286 | 5873 |
| 50 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +284 | 12530 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +281 | 23670 |
| 52 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +275 | 8995 |
| 53 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +273 | 4669 |
| 54 | [decolua/9router](https://github.com/decolua/9router) | +263 | 18144 |
| 55 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +258 | 16800 |
| 56 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +258 | 21683 |
| 57 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +253 | 43554 |
| 58 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +248 | 10507 |
| 59 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +247 | 18304 |
| 60 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +246 | 44129 |
| 61 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +244 | 44338 |
| 62 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +242 | 9667 |
| 63 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +242 | 12550 |
| 64 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +231 | 30845 |
| 65 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +229 | 23242 |
| 66 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +228 | 12899 |
| 67 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +228 | 19362 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +228 | 25362 |
| 69 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +224 | 10158 |
| 70 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +221 | 31565 |
| 71 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +218 | 14001 |
| 72 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +217 | 35363 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +217 | 39520 |
| 74 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4347 |
| 75 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5446 |
| 76 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +212 | 4001 |
| 77 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +212 | 17175 |
| 78 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +208 | 28953 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +207 | 34442 |
| 80 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +202 | 4677 |
| 81 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +201 | 31466 |
| 82 | [88lin/video_vip](https://github.com/88lin/video_vip) | +197 | 4171 |
| 83 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +194 | 38022 |
| 84 | [shadcn/improve](https://github.com/shadcn/improve) | +193 | 5867 |
| 85 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +190 | 25170 |
| 86 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +190 | 6631 |
| 87 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +190 | 58471 |
| 88 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +188 | 31098 |
| 89 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +187 | 4322 |
| 90 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +185 | 4087 |
| 91 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +184 | 5532 |
| 92 | [google/skills](https://github.com/google/skills) | +180 | 14008 |
| 93 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +180 | 2604 |
| 94 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +179 | 5525 |
| 95 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +179 | 21856 |
| 96 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +179 | 15653 |
| 97 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +179 | 20306 |
| 98 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +176 | 9692 |
| 99 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +176 | 11717 |
| 100 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +173 | 4789 |
| 101 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +173 | 22419 |
| 102 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +171 | 25693 |
| 103 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +169 | 3922 |
| 104 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6647 |
| 105 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +168 | 3497 |
| 106 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +167 | 4512 |
| 107 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +162 | 37737 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +160 | 7381 |
| 109 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +159 | 25313 |
| 110 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +159 | 6744 |
| 111 | [soxoj/maigret](https://github.com/soxoj/maigret) | +158 | 33484 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +157 | 16694 |
| 113 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +153 | 3513 |
| 114 | [openai/skills](https://github.com/openai/skills) | +153 | 22649 |
| 115 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +152 | 7180 |
| 116 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +149 | 7765 |
| 117 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +148 | 3379 |
| 118 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +145 | 41314 |
| 119 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +145 | 3549 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +145 | 16821 |
| 121 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2648 |
| 122 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +143 | 4621 |
| 123 | [google-research/timesfm](https://github.com/google-research/timesfm) | +141 | 24853 |
| 124 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +136 | 5287 |
| 125 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +134 | 4305 |
| 126 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +133 | 35365 |
| 127 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +132 | 6865 |
| 128 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +131 | 32872 |
| 129 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1985 |
| 130 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +125 | 49525 |
| 131 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +122 | 2954 |
| 132 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +121 | 4595 |
| 133 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +117 | 4394 |
| 134 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +117 | 23728 |
| 135 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +116 | 18703 |
| 136 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +115 | 8274 |
| 137 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +115 | 46979 |
| 138 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +113 | 5097 |
| 139 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +113 | 4431 |
| 140 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +109 | 24907 |
| 141 | [openai/plugins](https://github.com/openai/plugins) | +107 | 3304 |
| 142 | [MinishLab/semble](https://github.com/MinishLab/semble) | +106 | 5342 |
| 143 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +105 | 8469 |
| 144 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +103 | 9414 |
| 145 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +101 | 12422 |
| 146 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +101 | 25521 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +100 | 16930 |
| 148 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +99 | 8430 |
| 149 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +98 | 3308 |
| 150 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +97 | 7038 |
| 151 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +96 | 2367 |
| 152 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +94 | 16867 |
| 153 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +93 | 11480 |
| 154 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +91 | 5088 |
| 155 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +89 | 6954 |
| 156 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +89 | 5677 |
| 157 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +89 | 5128 |
| 158 | [floci-io/floci](https://github.com/floci-io/floci) | +89 | 14336 |
| 159 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +87 | 4216 |
| 160 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +87 | 19938 |
| 161 | [browser-use/video-use](https://github.com/browser-use/video-use) | +85 | 10001 |
| 162 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +84 | 24915 |
| 163 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +84 | 7325 |
| 164 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +84 | 23723 |
| 165 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +83 | 7246 |
| 166 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +83 | 1104 |
| 167 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +81 | 3125 |
| 168 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +80 | 4540 |
| 169 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +80 | 18750 |
| 170 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +80 | 21392 |
| 171 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 4326 |
| 172 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +78 | 15188 |
| 173 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +78 | 18659 |
| 174 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +76 | 3642 |
| 175 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +76 | 19718 |
| 176 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +74 | 1617 |
| 177 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +74 | 2464 |
| 178 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +73 | 44513 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +71 | 29656 |
| 180 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +71 | 27478 |
| 181 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +70 | 2161 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +70 | 16119 |
| 183 | [browser-act/skills](https://github.com/browser-act/skills) | +68 | 2776 |
| 184 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +68 | 19649 |
| 185 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +67 | 28788 |
| 186 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +67 | 25863 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +65 | 36103 |
| 188 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +63 | 3304 |
| 189 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +63 | 5794 |
| 190 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +61 | 1931 |
| 191 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +61 | 4589 |
| 192 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +61 | 37564 |
| 193 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +60 | 3156 |
| 194 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +60 | 8727 |
| 195 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 196 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +59 | 3032 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +57 | 16967 |
| 198 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +55 | 1297 |
| 199 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +53 | 5216 |
| 200 | [Doorman11991/smallcode](https://github.com/Doorman11991/smallcode) | +53 | 1911 |
| 201 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +52 | 2830 |
| 202 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +51 | 28172 |
| 203 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +49 | 1722 |
| 204 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +47 | 1131 |
| 205 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +47 | 1643 |
| 206 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +47 | 520 |
| 207 | [eze-is/web-access](https://github.com/eze-is/web-access) | +46 | 7774 |
| 208 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +42 | 5771 |
| 209 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +42 | 4907 |
| 210 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +41 | 1785 |
| 211 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +40 | 8207 |
| 212 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +37 | 11274 |
| 213 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +37 | 656 |
| 214 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +35 | 1375 |
| 215 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +35 | 4293 |
| 216 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +34 | 800 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +34 | 3955 |
| 218 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +33 | 999 |
| 219 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +33 | 2369 |
| 220 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +32 | 5337 |
| 221 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9432 |
| 222 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +30 | 1174 |
| 223 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +30 | 855 |
| 224 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +29 | 2815 |
| 225 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +28 | 3832 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +28 | 2330 |
| 227 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +26 | 2830 |
| 228 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +25 | 800 |
| 229 | [Nieobie/game-icon-pack](https://github.com/Nieobie/game-icon-pack) | +25 | 508 |
| 230 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 205 |
| 231 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +23 | 875 |
| 232 | [robinebers/openusage](https://github.com/robinebers/openusage) | +23 | 2926 |
| 233 | [sandeco/reversa](https://github.com/sandeco/reversa) | +23 | 1245 |
| 234 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 27 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +22 | 13796 |
| 236 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +22 | 5129 |
| 237 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +21 | 1924 |
| 238 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +21 | 4535 |
| 239 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +21 | 3319 |
| 240 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 525 |
| 241 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 957 |
| 242 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +20 | 1715 |
| 243 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +20 | 2610 |
| 244 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1385 |
| 245 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +19 | 8267 |
| 246 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +19 | 4506 |
| 247 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +18 | 470 |
| 248 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +18 | 12140 |
| 249 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +18 | 2542 |
| 250 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +17 | 1987 |
| 251 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +16 | 2045 |
| 252 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +16 | 2861 |
| 253 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +16 | 1159 |
| 254 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +16 | 2696 |
| 255 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +16 | 13659 |
| 256 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +16 | 379 |
| 257 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +16 | 440 |
| 258 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 201 |
| 259 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +15 | 2132 |
| 260 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 374 |
| 261 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +15 | 2215 |
| 262 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 563 |
| 263 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +13 | 207 |
| 264 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +13 | 409 |
| 265 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +13 | 606 |
| 266 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +13 | 252 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +13 | 2589 |
| 268 | [openmemind/memind](https://github.com/openmemind/memind) | +13 | 903 |
| 269 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 296 |
| 270 | [buynao/aipath](https://github.com/buynao/aipath) | +12 | 340 |
| 271 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +12 | 392 |
| 272 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +12 | 3485 |
| 273 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +11 | 1190 |
| 274 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +11 | 3035 |
| 275 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +11 | 314 |
| 276 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 115 |
| 277 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +10 | 351 |
| 278 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +10 | 2601 |
| 279 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1676 |
| 280 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +9 | 121 |
| 281 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +9 | 646 |
| 282 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +9 | 272 |
| 283 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +9 | 295 |
| 284 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 160 |
| 285 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +8 | 2497 |
| 286 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +8 | 1632 |
| 287 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 247 |
| 288 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +7 | 899 |
| 289 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 67 |
| 290 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +6 | 218 |
| 291 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +6 | 757 |
| 292 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 165 |
| 293 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 104 |
| 294 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 162 |
| 295 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +5 | 213 |
| 296 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +5 | 3524 |
| 297 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +5 | 2145 |
| 298 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +5 | 1024 |
| 299 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 457 |
| 300 | [structurizr/structurizr](https://github.com/structurizr/structurizr) | +5 | 258 |
