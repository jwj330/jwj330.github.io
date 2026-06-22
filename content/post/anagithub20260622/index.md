---
title: "2026-06-22 GitHub增长趋势报告"
description: "1.headroom+92 2.ponytail+88 3.OpenMontage+62 4.daily_stock_analysis+39 5.codebase-memory-mcp+36"
date: 2026-06-22T22:04:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-22 22:04:19

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
        'daily': {"categories": ["jakubkrehel/make-interfaces-feel-better", "heygen-com/hyperframes", "hugohe3/ppt-master", "yuanzhongqiao/deep-printfilm", "Yuan1z0825/nature-skills", "Forward-Future/loop-library", "zai-org/GLM-5", "alibaba/open-code-review", "rtk-ai/rtk", "jamiepine/voicebox", "mvanhorn/last30days-skill", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "mukul975/Anthropic-Cybersecurity-Skills", "StarTrail-org/PixelRAG", "DeusData/codebase-memory-mcp", "ZhuLinsen/daily_stock_analysis", "calesthio/OpenMontage", "DietrichGebert/ponytail", "chopratejas/headroom"], "data": [9, 9, 9, 9, 9, 10, 10, 11, 12, 14, 15, 16, 24, 24, 35, 36, 39, 62, 88, 92]},
        'weekly': {"categories": ["hugohe3/ppt-master", "mukul975/Anthropic-Cybersecurity-Skills", "rtk-ai/rtk", "omnigent-ai/omnigent", "Kilo-Org/kilocode", "GoogleCloudPlatform/knowledge-catalog", "mvanhorn/last30days-skill", "ZhuLinsen/daily_stock_analysis", "colbymchenry/codegraph", "StarTrail-org/PixelRAG", "elder-plinius/CL4R1T4S", "google-research/timesfm", "penpot/penpot", "EpicGames/lore", "calesthio/OpenMontage", "Leonxlnx/taste-skill", "DeusData/codebase-memory-mcp", "Panniantong/Agent-Reach", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [60, 62, 63, 72, 73, 73, 78, 86, 93, 96, 103, 107, 112, 112, 126, 136, 189, 221, 437, 795]},
        'monthly': {"categories": ["anthropics/knowledge-work-plugins", "mukul975/Anthropic-Cybersecurity-Skills", "elder-plinius/CL4R1T4S", "anthropics/claude-plugins-official", "Panniantong/Agent-Reach", "Imbad0202/academic-research-skills", "addyosmani/agent-skills", "mvanhorn/last30days-skill", "safishamsi/graphify", "harry0703/MoneyPrinterTurbo", "farion1231/cc-switch", "DietrichGebert/ponytail", "Leonxlnx/taste-skill", "chopratejas/headroom", "rohitg00/ai-engineering-from-scratch", "mattpocock/skills", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "pewdiepie-archdaemon/odysseus", "Egonex-AI/Understand-Anything"], "data": [535, 551, 621, 666, 692, 728, 751, 859, 894, 1077, 1142, 1152, 1299, 1461, 1496, 1663, 2092, 2279, 2575, 2880]}
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
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +92 | 46933 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +88 | 49528 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +62 | 11756 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 45732 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +36 | 11424 |
| 6 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +35 | 3410 |
| 7 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +24 | 18601 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +24 | 49026 |
| 9 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +16 | 53149 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +15 | 45772 |
| 11 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +14 | 32140 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +12 | 65036 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +11 | 8443 |
| 14 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +10 | 5166 |
| 15 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +10 | 1033 |
| 16 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 22193 |
| 17 | [yuanzhongqiao/deep-printfilm](https://github.com/yuanzhongqiao/deep-printfilm) | +9 | 2284 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 30346 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 29916 |
| 20 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +9 | 1503 |
| 21 | [EpicGames/lore](https://github.com/EpicGames/lore) | +9 | 5719 |
| 22 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +9 | 1169 |
| 23 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +8 | 4455 |
| 24 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +8 | 25304 |
| 25 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 34599 |
| 26 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 25601 |
| 27 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +7 | 36821 |
| 28 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +7 | 30633 |
| 29 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 35658 |
| 30 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +6 | 5983 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +795 | 49528 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +437 | 46933 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +221 | 37760 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +189 | 11425 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +136 | 49026 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +126 | 11756 |
| 7 | [EpicGames/lore](https://github.com/EpicGames/lore) | +112 | 5719 |
| 8 | [penpot/penpot](https://github.com/penpot/penpot) | +112 | 44370 |
| 9 | [google-research/timesfm](https://github.com/google-research/timesfm) | +107 | 25124 |
| 10 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +103 | 43404 |
| 11 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +96 | 3410 |
| 12 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +93 | 53149 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +86 | 45733 |
| 14 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +78 | 45772 |
| 15 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +73 | 4814 |
| 16 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +73 | 23953 |
| 17 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +72 | 4455 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +63 | 65036 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +62 | 18601 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +60 | 30346 |
| 21 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +57 | 32872 |
| 22 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | +57 | 21403 |
| 23 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +56 | 9371 |
| 24 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +54 | 35658 |
| 25 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +52 | 36369 |
| 26 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +52 | 33670 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +50 | 22193 |
| 28 | [alibaba/zvec](https://github.com/alibaba/zvec) | +49 | 12152 |
| 29 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +48 | 32140 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +47 | 29916 |
| 31 | [vercel/eve](https://github.com/vercel/eve) | +47 | 2263 |
| 32 | [blader/humanizer](https://github.com/blader/humanizer) | +43 | 25601 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +42 | 8443 |
| 34 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +41 | 5166 |
| 35 | [withastro/flue](https://github.com/withastro/flue) | +38 | 6421 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +38 | 14110 |
| 37 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +38 | 19831 |
| 38 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +36 | 34599 |
| 39 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +36 | 31291 |
| 40 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +35 | 10342 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +35 | 40328 |
| 42 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +34 | 11558 |
| 43 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +31 | 1033 |
| 44 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +31 | 29056 |
| 45 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +28 | 25304 |
| 46 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +27 | 1202 |
| 47 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +27 | 5690 |
| 48 | [tamnd/kage](https://github.com/tamnd/kage) | +27 | 2281 |
| 49 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +26 | 36821 |
| 50 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +26 | 806 |
| 51 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +26 | 6815 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +26 | 23777 |
| 53 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +25 | 1555 |
| 54 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +25 | 32208 |
| 55 | [shadcn/improve](https://github.com/shadcn/improve) | +25 | 5981 |
| 56 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +25 | 30897 |
| 57 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +23 | 13051 |
| 58 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +23 | 21739 |
| 59 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +23 | 12447 |
| 60 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +22 | 17888 |
| 61 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +22 | 8406 |
| 62 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +22 | 9746 |
| 63 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +22 | 2146 |
| 64 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +21 | 19458 |
| 65 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +21 | 1564 |
| 66 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +21 | 22225 |
| 67 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +21 | 15734 |
| 68 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +21 | 788 |
| 69 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +21 | 552 |
| 70 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +21 | 58868 |
| 71 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +20 | 42730 |
| 72 | [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil) | +20 | 6103 |
| 73 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +20 | 5431 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +20 | 18455 |
| 75 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +20 | 28715 |
| 76 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +20 | 26900 |
| 77 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +20 | 22522 |
| 78 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +19 | 1169 |
| 79 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +19 | 2977 |
| 80 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +19 | 28488 |
| 81 | [multica-ai/multica](https://github.com/multica-ai/multica) | +19 | 37530 |
| 82 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +19 | 23335 |
| 83 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 7775 |
| 84 | [stablyai/orca](https://github.com/stablyai/orca) | +18 | 6009 |
| 85 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +18 | 3175 |
| 86 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +18 | 30633 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +18 | 38097 |
| 88 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +18 | 12863 |
| 89 | [antirez/ds4](https://github.com/antirez/ds4) | +18 | 15019 |
| 90 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +18 | 1253 |
| 91 | [playRealmRumble/Realm-Rumble](https://github.com/playRealmRumble/Realm-Rumble) | +17 | 694 |
| 92 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +17 | 8544 |
| 93 | [microsoft/fastcontext](https://github.com/microsoft/fastcontext) | +17 | 800 |
| 94 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +17 | 1511 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 43629 |
| 96 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +16 | 290 |
| 97 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +16 | 9700 |
| 98 | [decolua/9router](https://github.com/decolua/9router) | +15 | 18236 |
| 99 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +14 | 5983 |
| 100 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +14 | 31635 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +14 | 18791 |
| 102 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +14 | 4414 |
| 103 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +14 | 2319 |
| 104 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +14 | 4571 |
| 105 | [dongshuyan/compass-skills](https://github.com/dongshuyan/compass-skills) | +13 | 467 |
| 106 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +12 | 6984 |
| 107 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +12 | 25364 |
| 108 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +12 | 8582 |
| 109 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +12 | 15233 |
| 110 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 7343 |
| 111 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +12 | 7852 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +11 | 16934 |
| 113 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +11 | 2617 |
| 114 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +11 | 7374 |
| 115 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +11 | 24970 |
| 116 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +11 | 37852 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +11 | 41411 |
| 118 | [kernalix7/winpodx](https://github.com/kernalix7/winpodx) | +10 | 1258 |
| 119 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 3186 |
| 120 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +10 | 417 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2880 | 66122 |
| 2 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2575 | 76340 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2279 | 53149 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2092 | 180384 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1663 | 141529 |
| 6 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1496 | 35658 |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1461 | 46933 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1299 | 49026 |
| 9 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1152 | 49528 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1142 | 106379 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1077 | 49621 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +894 | 70692 |
| 13 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +859 | 45772 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +751 | 65359 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +728 | 33670 |
| 16 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +692 | 37760 |
| 17 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +666 | 30633 |
| 18 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +621 | 43404 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +551 | 18601 |
| 20 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +535 | 21739 |
| 21 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +522 | 32803 |
| 22 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +492 | 26900 |
| 23 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +473 | 12099 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +462 | 65036 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +451 | 22193 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +442 | 30346 |
| 27 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +434 | 36369 |
| 28 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +414 | 14110 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +413 | 8443 |
| 30 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +406 | 31291 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +406 | 40328 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +404 | 29916 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +404 | 11558 |
| 34 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +404 | 23700 |
| 35 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +400 | 32585 |
| 36 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9382 |
| 37 | [apple/container](https://github.com/apple/container) | +393 | 39507 |
| 38 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +388 | 4602 |
| 39 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +356 | 10342 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +352 | 37530 |
| 41 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +351 | 27323 |
| 42 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8245 |
| 43 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +335 | 22680 |
| 44 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +317 | 38849 |
| 45 | [roboflow/supervision](https://github.com/roboflow/supervision) | +291 | 36553 |
| 46 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +288 | 14876 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +283 | 12590 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +277 | 23778 |
| 49 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +274 | 9372 |
| 50 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +273 | 32208 |
| 51 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +272 | 4706 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +270 | 45733 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +269 | 28715 |
| 54 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +268 | 5983 |
| 55 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +258 | 16840 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +250 | 11425 |
| 57 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +249 | 21727 |
| 58 | [decolua/9router](https://github.com/decolua/9router) | +237 | 18236 |
| 59 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +233 | 10561 |
| 60 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +231 | 18455 |
| 61 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +231 | 9739 |
| 62 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +230 | 12596 |
| 63 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +225 | 30897 |
| 64 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +225 | 32140 |
| 65 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +224 | 23335 |
| 66 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +221 | 44202 |
| 67 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +219 | 43629 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +217 | 25601 |
| 69 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +216 | 19458 |
| 70 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4347 |
| 71 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5446 |
| 72 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +211 | 29056 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +211 | 39659 |
| 74 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +211 | 35402 |
| 75 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +209 | 14047 |
| 76 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +208 | 13051 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +204 | 34599 |
| 78 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +204 | 4803 |
| 79 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +201 | 31635 |
| 80 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +199 | 17216 |
| 81 | [shadcn/improve](https://github.com/shadcn/improve) | +196 | 5981 |
| 82 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +188 | 25304 |
| 83 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +188 | 4370 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +187 | 38097 |
| 85 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +186 | 31098 |
| 86 | [penpot/penpot](https://github.com/penpot/penpot) | +186 | 44370 |
| 87 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +186 | 6815 |
| 88 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +184 | 5538 |
| 89 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +182 | 5690 |
| 90 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +178 | 21893 |
| 91 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +178 | 15734 |
| 92 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +176 | 4828 |
| 93 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +176 | 58868 |
| 94 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +176 | 2643 |
| 95 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +174 | 4421 |
| 96 | [google/skills](https://github.com/google/skills) | +173 | 14041 |
| 97 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +173 | 11751 |
| 98 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +173 | 25745 |
| 99 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +172 | 4092 |
| 100 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6656 |
| 101 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +168 | 22522 |
| 102 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +168 | 20430 |
| 103 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +164 | 4571 |
| 104 | [88lin/video_vip](https://github.com/88lin/video_vip) | +159 | 4184 |
| 105 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +158 | 11756 |
| 106 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +155 | 37852 |
| 107 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 25364 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +155 | 7435 |
| 109 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +154 | 9746 |
| 110 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +153 | 3530 |
| 111 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +152 | 7291 |
| 112 | [soxoj/maigret](https://github.com/soxoj/maigret) | +151 | 33564 |
| 113 | [openai/skills](https://github.com/openai/skills) | +149 | 22723 |
| 114 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +148 | 32872 |
| 115 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +148 | 3928 |
| 116 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +147 | 4814 |
| 117 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +146 | 2687 |
| 118 | [google-research/timesfm](https://github.com/google-research/timesfm) | +145 | 25124 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +145 | 16934 |
| 120 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +144 | 7809 |
| 121 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +142 | 4455 |
| 122 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +140 | 41411 |
| 123 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +140 | 3423 |
| 124 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +137 | 3614 |
| 125 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +133 | 6800 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +132 | 16735 |
| 127 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +126 | 3514 |
| 128 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +124 | 49545 |
| 129 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +122 | 35452 |
| 130 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +120 | 6982 |
| 131 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +119 | 2954 |
| 132 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +116 | 18791 |
| 133 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +114 | 47062 |
| 134 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +113 | 4499 |
| 135 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +112 | 4599 |
| 136 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +112 | 23759 |
| 137 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +111 | 8406 |
| 138 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +109 | 5150 |
| 139 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +108 | 1981 |
| 140 | [openai/plugins](https://github.com/openai/plugins) | +108 | 3354 |
| 141 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +105 | 4450 |
| 142 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +103 | 24992 |
| 143 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +102 | 3410 |
| 144 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +99 | 8544 |
| 145 | [MinishLab/semble](https://github.com/MinishLab/semble) | +99 | 5359 |
| 146 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +98 | 9527 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +96 | 16979 |
| 148 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +94 | 3324 |
| 149 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +93 | 6984 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +92 | 35533 |
| 151 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +92 | 11518 |
| 152 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +92 | 25585 |
| 153 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +91 | 12486 |
| 154 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +91 | 5137 |
| 155 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +89 | 16907 |
| 156 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +87 | 4301 |
| 157 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +86 | 7086 |
| 158 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +85 | 24970 |
| 159 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +82 | 7343 |
| 160 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +82 | 7374 |
| 161 | [browser-use/video-use](https://github.com/browser-use/video-use) | +81 | 10045 |
| 162 | [floci-io/floci](https://github.com/floci-io/floci) | +81 | 14364 |
| 163 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +80 | 23765 |
| 164 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +80 | 5740 |
| 165 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +79 | 19831 |
| 166 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +79 | 1103 |
| 167 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 4414 |
| 168 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +78 | 4566 |
| 169 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +78 | 18703 |
| 170 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +77 | 15233 |
| 171 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +76 | 3722 |
| 172 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +76 | 19968 |
| 173 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +76 | 18796 |
| 174 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +75 | 1644 |
| 175 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +75 | 21441 |
| 176 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +72 | 44583 |
| 177 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +71 | 27535 |
| 178 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +70 | 2180 |
| 179 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +70 | 5329 |
| 180 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +69 | 3150 |
| 181 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +69 | 36103 |
| 182 | [browser-act/skills](https://github.com/browser-act/skills) | +68 | 2802 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +67 | 29706 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +66 | 16182 |
| 185 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +65 | 25921 |
| 186 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +63 | 28833 |
| 187 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +61 | 3353 |
| 188 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +61 | 4631 |
| 189 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +60 | 4403 |
| 190 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +60 | 2469 |
| 191 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 192 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +59 | 37564 |
| 193 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +58 | 8737 |
| 194 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +58 | 5805 |
| 195 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +57 | 3074 |
| 196 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +57 | 3189 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +56 | 16992 |
| 198 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +53 | 3186 |
| 199 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +50 | 2876 |
| 200 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +50 | 5237 |
| 201 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +50 | 28201 |
| 202 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +50 | 1305 |
| 203 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +49 | 1735 |
| 204 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +47 | 524 |
| 205 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +46 | 1662 |
| 206 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1133 |
| 207 | [eze-is/web-access](https://github.com/eze-is/web-access) | +44 | 7796 |
| 208 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +42 | 1776 |
| 209 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +41 | 8231 |
| 210 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +40 | 1810 |
| 211 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +38 | 4912 |
| 212 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +37 | 5796 |
| 213 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +37 | 11292 |
| 214 | [Doorman11991/smallcode](https://github.com/Doorman11991/smallcode) | +37 | 1915 |
| 215 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +37 | 666 |
| 216 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +36 | 1032 |
| 217 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +34 | 813 |
| 218 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4298 |
| 219 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +32 | 1219 |
| 220 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9436 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +32 | 3986 |
| 222 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +31 | 1034 |
| 223 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +30 | 2371 |
| 224 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +30 | 5347 |
| 225 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +30 | 856 |
| 226 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +29 | 1210 |
| 227 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +29 | 2833 |
| 228 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +28 | 1430 |
| 229 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +27 | 3870 |
| 230 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +27 | 1403 |
| 231 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +25 | 2349 |
| 232 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 805 |
| 233 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +24 | 2830 |
| 234 | [Nieobie/game-icon-pack](https://github.com/Nieobie/game-icon-pack) | +24 | 510 |
| 235 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 207 |
| 236 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +23 | 919 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +23 | 13834 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +23 | 2932 |
| 239 | [sandeco/reversa](https://github.com/sandeco/reversa) | +23 | 1249 |
| 240 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 27 |
| 241 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +21 | 4550 |
| 242 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 527 |
| 243 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +20 | 1940 |
| 244 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 965 |
| 245 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +20 | 3333 |
| 246 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +20 | 1728 |
| 247 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1393 |
| 248 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +19 | 8283 |
| 249 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +19 | 2620 |
| 250 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +18 | 4519 |
| 251 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +17 | 1996 |
| 252 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +17 | 479 |
| 253 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +17 | 12145 |
| 254 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +17 | 13686 |
| 255 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +16 | 290 |
| 256 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +16 | 2079 |
| 257 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +16 | 381 |
| 258 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +16 | 2554 |
| 259 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +16 | 447 |
| 260 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 238 |
| 261 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +15 | 2150 |
| 262 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 380 |
| 263 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +15 | 1164 |
| 264 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +15 | 2864 |
| 265 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +15 | 2225 |
| 266 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +14 | 696 |
| 267 | [buynao/aipath](https://github.com/buynao/aipath) | +13 | 368 |
| 268 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +13 | 430 |
| 269 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 425 |
| 270 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 567 |
| 271 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +13 | 2606 |
| 272 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 302 |
| 273 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +12 | 3493 |
| 274 | [openmemind/memind](https://github.com/openmemind/memind) | +12 | 902 |
| 275 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +11 | 1196 |
| 276 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +10 | 355 |
| 277 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3044 |
| 278 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1681 |
| 279 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +10 | 318 |
| 280 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +9 | 118 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +9 | 2610 |
| 282 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +9 | 649 |
| 283 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +9 | 114 |
| 284 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 171 |
| 285 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +8 | 2504 |
| 286 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +8 | 269 |
| 287 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 248 |
| 288 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 169 |
| 289 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +7 | 902 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +7 | 1632 |
| 291 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 68 |
| 292 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +7 | 294 |
| 293 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +6 | 218 |
| 294 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 3539 |
| 295 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 104 |
| 296 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 163 |
| 297 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +5 | 214 |
| 298 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 558 |
| 299 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +5 | 1024 |
| 300 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 463 |
