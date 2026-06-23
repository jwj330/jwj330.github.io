---
title: "2026-06-23 GitHub增长趋势报告"
description: "1.headroom+92 2.ponytail+88 3.OpenMontage+62 4.daily_stock_analysis+39 5.codebase-memory-mcp+36"
date: 2026-06-23T21:44:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-23 21:44:05

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
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +92 | 48399 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +88 | 52267 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +62 | 15372 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 46947 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +36 | 12768 |
| 6 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +35 | 4379 |
| 7 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +24 | 19578 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +24 | 49617 |
| 9 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +16 | 53668 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +15 | 46071 |
| 11 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +14 | 33068 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +12 | 65422 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +11 | 8587 |
| 14 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +10 | 5293 |
| 15 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +10 | 1448 |
| 16 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 22579 |
| 17 | [yuanzhongqiao/deep-printfilm](https://github.com/yuanzhongqiao/deep-printfilm) | +9 | 2367 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 30721 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 30605 |
| 20 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +9 | 1640 |
| 21 | [EpicGames/lore](https://github.com/EpicGames/lore) | +9 | 5912 |
| 22 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +9 | 1218 |
| 23 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +8 | 4571 |
| 24 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +8 | 25432 |
| 25 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 34738 |
| 26 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 25778 |
| 27 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +7 | 36936 |
| 28 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +7 | 30808 |
| 29 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 35970 |
| 30 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +6 | 6027 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +795 | 52267 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +437 | 48399 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +221 | 38574 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +189 | 12768 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +136 | 49617 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +126 | 15372 |
| 7 | [EpicGames/lore](https://github.com/EpicGames/lore) | +112 | 5912 |
| 8 | [penpot/penpot](https://github.com/penpot/penpot) | +112 | 44370 |
| 9 | [google-research/timesfm](https://github.com/google-research/timesfm) | +107 | 25294 |
| 10 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +103 | 43604 |
| 11 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +96 | 4379 |
| 12 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +93 | 53668 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +86 | 46947 |
| 14 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +78 | 46072 |
| 15 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +73 | 4945 |
| 16 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +73 | 24211 |
| 17 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +72 | 4571 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +63 | 65422 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +62 | 19578 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +60 | 30721 |
| 21 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +57 | 32872 |
| 22 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | +57 | 21894 |
| 23 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +56 | 9789 |
| 24 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +54 | 35970 |
| 25 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +52 | 36618 |
| 26 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +52 | 33943 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +50 | 22579 |
| 28 | [alibaba/zvec](https://github.com/alibaba/zvec) | +49 | 12291 |
| 29 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +48 | 33068 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +47 | 30605 |
| 31 | [vercel/eve](https://github.com/vercel/eve) | +47 | 2419 |
| 32 | [blader/humanizer](https://github.com/blader/humanizer) | +43 | 25778 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +42 | 8587 |
| 34 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +41 | 5293 |
| 35 | [withastro/flue](https://github.com/withastro/flue) | +38 | 6521 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +38 | 14333 |
| 37 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +38 | 19931 |
| 38 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +36 | 34738 |
| 39 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +36 | 31408 |
| 40 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +35 | 10485 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +35 | 40714 |
| 42 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +34 | 11810 |
| 43 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +31 | 1448 |
| 44 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +31 | 29149 |
| 45 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +28 | 25432 |
| 46 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +27 | 1215 |
| 47 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +27 | 5877 |
| 48 | [tamnd/kage](https://github.com/tamnd/kage) | +27 | 2339 |
| 49 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +26 | 36936 |
| 50 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +26 | 984 |
| 51 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +26 | 6932 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +26 | 23889 |
| 53 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +25 | 1577 |
| 54 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +25 | 32312 |
| 55 | [shadcn/improve](https://github.com/shadcn/improve) | +25 | 6056 |
| 56 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +25 | 31090 |
| 57 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +23 | 13142 |
| 58 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +23 | 21840 |
| 59 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +23 | 12569 |
| 60 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +22 | 17972 |
| 61 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +22 | 8580 |
| 62 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +22 | 9808 |
| 63 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +22 | 2172 |
| 64 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +21 | 19562 |
| 65 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +21 | 1883 |
| 66 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +21 | 22314 |
| 67 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +21 | 15820 |
| 68 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +21 | 868 |
| 69 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +21 | 571 |
| 70 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +21 | 59360 |
| 71 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +20 | 42818 |
| 72 | [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil) | +20 | 6183 |
| 73 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +20 | 5515 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +20 | 18620 |
| 75 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +20 | 28825 |
| 76 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +20 | 26979 |
| 77 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +20 | 22649 |
| 78 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +19 | 1218 |
| 79 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +19 | 3924 |
| 80 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +19 | 28524 |
| 81 | [multica-ai/multica](https://github.com/multica-ai/multica) | +19 | 37696 |
| 82 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +19 | 23442 |
| 83 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 7909 |
| 84 | [stablyai/orca](https://github.com/stablyai/orca) | +18 | 6290 |
| 85 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +18 | 3235 |
| 86 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +18 | 30808 |
| 87 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +18 | 38199 |
| 88 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +18 | 12920 |
| 89 | [antirez/ds4](https://github.com/antirez/ds4) | +18 | 15175 |
| 90 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +18 | 1316 |
| 91 | [playRealmRumble/Realm-Rumble](https://github.com/playRealmRumble/Realm-Rumble) | +17 | 692 |
| 92 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +17 | 8628 |
| 93 | [microsoft/fastcontext](https://github.com/microsoft/fastcontext) | +17 | 888 |
| 94 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +17 | 1543 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 43693 |
| 96 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +16 | 319 |
| 97 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +16 | 9734 |
| 98 | [decolua/9router](https://github.com/decolua/9router) | +15 | 18312 |
| 99 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +14 | 6027 |
| 100 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +14 | 31792 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +14 | 18892 |
| 102 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +14 | 4493 |
| 103 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +14 | 2388 |
| 104 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +14 | 4628 |
| 105 | [dongshuyan/compass-skills](https://github.com/dongshuyan/compass-skills) | +13 | 480 |
| 106 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +12 | 7007 |
| 107 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +12 | 25405 |
| 108 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +12 | 8611 |
| 109 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +12 | 15275 |
| 110 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 7582 |
| 111 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +12 | 7909 |
| 112 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +11 | 17182 |
| 113 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +11 | 2641 |
| 114 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +11 | 7418 |
| 115 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +11 | 25014 |
| 116 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +11 | 37987 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +11 | 41501 |
| 118 | [kernalix7/winpodx](https://github.com/kernalix7/winpodx) | +10 | 1283 |
| 119 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 3231 |
| 120 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +10 | 466 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2880 | 66788 |
| 2 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2575 | 76868 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2279 | 53668 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2092 | 180973 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1663 | 143202 |
| 6 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1496 | 35970 |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1461 | 48400 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1299 | 49617 |
| 9 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1152 | 52268 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1142 | 107041 |
| 11 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1077 | 49621 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +894 | 71151 |
| 13 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +859 | 46072 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +751 | 65904 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +728 | 33943 |
| 16 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +692 | 38574 |
| 17 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +666 | 30808 |
| 18 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +621 | 43604 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +551 | 19578 |
| 20 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +535 | 21840 |
| 21 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +522 | 32870 |
| 22 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +492 | 26979 |
| 23 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +473 | 12130 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +462 | 65423 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +451 | 22579 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +442 | 30721 |
| 27 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +434 | 36618 |
| 28 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +414 | 14333 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +413 | 8587 |
| 30 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +406 | 31408 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +406 | 40714 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +404 | 30605 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +404 | 11810 |
| 34 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +404 | 23809 |
| 35 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +400 | 32842 |
| 36 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9760 |
| 37 | [apple/container](https://github.com/apple/container) | +393 | 40619 |
| 38 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +388 | 4610 |
| 39 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +356 | 10485 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +352 | 37696 |
| 41 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +351 | 27377 |
| 42 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8244 |
| 43 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +335 | 22760 |
| 44 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +317 | 38905 |
| 45 | [roboflow/supervision](https://github.com/roboflow/supervision) | +291 | 36553 |
| 46 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +288 | 14917 |
| 47 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +283 | 12647 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +277 | 23889 |
| 49 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +274 | 9789 |
| 50 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +273 | 32312 |
| 51 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +272 | 4741 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +270 | 46947 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +269 | 28825 |
| 54 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +268 | 6027 |
| 55 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +258 | 16857 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +250 | 12769 |
| 57 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +249 | 21764 |
| 58 | [decolua/9router](https://github.com/decolua/9router) | +237 | 18312 |
| 59 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +233 | 10590 |
| 60 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +231 | 18620 |
| 61 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +231 | 9837 |
| 62 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +230 | 12628 |
| 63 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +225 | 31090 |
| 64 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +225 | 33068 |
| 65 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +224 | 23442 |
| 66 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +221 | 44267 |
| 67 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +219 | 43693 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +217 | 25778 |
| 69 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +216 | 19562 |
| 70 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4346 |
| 71 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5446 |
| 72 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +211 | 29149 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +211 | 39791 |
| 74 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +211 | 35431 |
| 75 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +209 | 14082 |
| 76 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +208 | 13142 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +204 | 34738 |
| 78 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +204 | 4905 |
| 79 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +201 | 31792 |
| 80 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +199 | 17260 |
| 81 | [shadcn/improve](https://github.com/shadcn/improve) | +196 | 6056 |
| 82 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +188 | 25432 |
| 83 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +188 | 4411 |
| 84 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +187 | 38199 |
| 85 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +186 | 31098 |
| 86 | [penpot/penpot](https://github.com/penpot/penpot) | +186 | 44370 |
| 87 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +186 | 6932 |
| 88 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +184 | 5550 |
| 89 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +182 | 5877 |
| 90 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +178 | 21931 |
| 91 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +178 | 15820 |
| 92 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +176 | 4861 |
| 93 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +176 | 59360 |
| 94 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +176 | 2668 |
| 95 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +174 | 4433 |
| 96 | [google/skills](https://github.com/google/skills) | +173 | 14075 |
| 97 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +173 | 11802 |
| 98 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +173 | 25781 |
| 99 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +172 | 4098 |
| 100 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6673 |
| 101 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +168 | 22649 |
| 102 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +168 | 20561 |
| 103 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +164 | 4628 |
| 104 | [88lin/video_vip](https://github.com/88lin/video_vip) | +159 | 4198 |
| 105 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +158 | 15373 |
| 106 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +155 | 37987 |
| 107 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 25405 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +155 | 7493 |
| 109 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +154 | 9808 |
| 110 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +153 | 3549 |
| 111 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +152 | 7350 |
| 112 | [soxoj/maigret](https://github.com/soxoj/maigret) | +151 | 33612 |
| 113 | [openai/skills](https://github.com/openai/skills) | +149 | 22773 |
| 114 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +148 | 32872 |
| 115 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +148 | 3932 |
| 116 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +147 | 4945 |
| 117 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +146 | 2723 |
| 118 | [google-research/timesfm](https://github.com/google-research/timesfm) | +145 | 25294 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +145 | 17182 |
| 120 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +144 | 7836 |
| 121 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +142 | 4571 |
| 122 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +140 | 41501 |
| 123 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +140 | 3460 |
| 124 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +137 | 3654 |
| 125 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +133 | 6847 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +132 | 16776 |
| 127 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +126 | 3527 |
| 128 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +124 | 49562 |
| 129 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +122 | 35555 |
| 130 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +120 | 7118 |
| 131 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +119 | 2955 |
| 132 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +116 | 18892 |
| 133 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +114 | 47138 |
| 134 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +113 | 4600 |
| 135 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +112 | 4604 |
| 136 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +112 | 23960 |
| 137 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +111 | 8580 |
| 138 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +109 | 5190 |
| 139 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +108 | 1976 |
| 140 | [openai/plugins](https://github.com/openai/plugins) | +108 | 3427 |
| 141 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +105 | 4486 |
| 142 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +103 | 25088 |
| 143 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +102 | 4379 |
| 144 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +99 | 8628 |
| 145 | [MinishLab/semble](https://github.com/MinishLab/semble) | +99 | 5369 |
| 146 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +98 | 9637 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +96 | 17026 |
| 148 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +94 | 3341 |
| 149 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +93 | 7007 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +92 | 35601 |
| 151 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +92 | 11555 |
| 152 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +92 | 25650 |
| 153 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +91 | 12542 |
| 154 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +91 | 5203 |
| 155 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +89 | 16939 |
| 156 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +87 | 4387 |
| 157 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +86 | 7119 |
| 158 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +85 | 25014 |
| 159 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +82 | 7582 |
| 160 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +82 | 7418 |
| 161 | [browser-use/video-use](https://github.com/browser-use/video-use) | +81 | 10091 |
| 162 | [floci-io/floci](https://github.com/floci-io/floci) | +81 | 14400 |
| 163 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +80 | 23813 |
| 164 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +80 | 5793 |
| 165 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +79 | 19931 |
| 166 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +79 | 1107 |
| 167 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 4493 |
| 168 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +78 | 4597 |
| 169 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +78 | 18751 |
| 170 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +77 | 15275 |
| 171 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +76 | 3764 |
| 172 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +76 | 20044 |
| 173 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +76 | 18831 |
| 174 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +75 | 1665 |
| 175 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +75 | 21491 |
| 176 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +72 | 44641 |
| 177 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +71 | 27585 |
| 178 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +70 | 2200 |
| 179 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +70 | 5457 |
| 180 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +69 | 3166 |
| 181 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +69 | 36103 |
| 182 | [browser-act/skills](https://github.com/browser-act/skills) | +68 | 2846 |
| 183 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +67 | 29758 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +66 | 16233 |
| 185 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +65 | 25960 |
| 186 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +63 | 28880 |
| 187 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +61 | 3403 |
| 188 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +61 | 4688 |
| 189 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +60 | 4440 |
| 190 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +60 | 2471 |
| 191 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 192 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +59 | 37564 |
| 193 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +58 | 8746 |
| 194 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +58 | 5826 |
| 195 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +57 | 3120 |
| 196 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +57 | 3237 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +56 | 17129 |
| 198 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +53 | 3231 |
| 199 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +50 | 2942 |
| 200 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +50 | 5261 |
| 201 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +50 | 28253 |
| 202 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +50 | 1308 |
| 203 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +49 | 1778 |
| 204 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +47 | 525 |
| 205 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +46 | 1678 |
| 206 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1140 |
| 207 | [eze-is/web-access](https://github.com/eze-is/web-access) | +44 | 7824 |
| 208 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +42 | 1811 |
| 209 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +41 | 8269 |
| 210 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +40 | 1850 |
| 211 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +38 | 4921 |
| 212 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +37 | 5815 |
| 213 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +37 | 11328 |
| 214 | [Doorman11991/smallcode](https://github.com/Doorman11991/smallcode) | +37 | 1922 |
| 215 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +37 | 673 |
| 216 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +36 | 1064 |
| 217 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +34 | 824 |
| 218 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4300 |
| 219 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +32 | 1221 |
| 220 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9441 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +32 | 4018 |
| 222 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +31 | 1448 |
| 223 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +30 | 2386 |
| 224 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +30 | 5359 |
| 225 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +30 | 856 |
| 226 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +29 | 1223 |
| 227 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +29 | 2846 |
| 228 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +28 | 1461 |
| 229 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +27 | 3897 |
| 230 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +27 | 1417 |
| 231 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +25 | 2380 |
| 232 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 809 |
| 233 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +24 | 2834 |
| 234 | [Nieobie/game-icon-pack](https://github.com/Nieobie/game-icon-pack) | +24 | 513 |
| 235 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 207 |
| 236 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +23 | 964 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +23 | 13853 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +23 | 2940 |
| 239 | [sandeco/reversa](https://github.com/sandeco/reversa) | +23 | 1254 |
| 240 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 27 |
| 241 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +21 | 4565 |
| 242 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 529 |
| 243 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +20 | 1960 |
| 244 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 981 |
| 245 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +20 | 3344 |
| 246 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +20 | 1734 |
| 247 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1398 |
| 248 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +19 | 8291 |
| 249 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +19 | 2634 |
| 250 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +18 | 4534 |
| 251 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +17 | 2010 |
| 252 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +17 | 490 |
| 253 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +17 | 12156 |
| 254 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +17 | 13702 |
| 255 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +16 | 319 |
| 256 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +16 | 2184 |
| 257 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +16 | 385 |
| 258 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +16 | 2563 |
| 259 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +16 | 453 |
| 260 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 263 |
| 261 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +15 | 2163 |
| 262 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 389 |
| 263 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +15 | 1168 |
| 264 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +15 | 2865 |
| 265 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +15 | 2230 |
| 266 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +14 | 766 |
| 267 | [buynao/aipath](https://github.com/buynao/aipath) | +13 | 414 |
| 268 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +13 | 440 |
| 269 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 440 |
| 270 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 569 |
| 271 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +13 | 2621 |
| 272 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 307 |
| 273 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +12 | 3502 |
| 274 | [openmemind/memind](https://github.com/openmemind/memind) | +12 | 901 |
| 275 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +11 | 1199 |
| 276 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +10 | 357 |
| 277 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3053 |
| 278 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1688 |
| 279 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +10 | 323 |
| 280 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +9 | 119 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +9 | 2615 |
| 282 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +9 | 654 |
| 283 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +9 | 114 |
| 284 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 177 |
| 285 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +8 | 2518 |
| 286 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +8 | 272 |
| 287 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 252 |
| 288 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 172 |
| 289 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +7 | 909 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +7 | 1632 |
| 291 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 72 |
| 292 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +7 | 294 |
| 293 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +6 | 220 |
| 294 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 3562 |
| 295 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 107 |
| 296 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 164 |
| 297 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +5 | 214 |
| 298 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 559 |
| 299 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +5 | 1031 |
| 300 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 472 |
