---
title: "2026-06-24 GitHub增长趋势报告"
description: "1.OpenMontage+54 2.ponytail+42 3.container+33 4.daily_stock_analysis+21 5.codebase-memory-mcp+21"
date: 2026-06-24T21:24:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-24 21:24:23

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
        'daily': {"categories": ["rtk-ai/rtk", "Yuan1z0825/nature-skills", "googleworkspace/cli", "alibaba/open-code-review", "JCodesMore/ai-website-cloner-template", "NVIDIA/SkillSpector", "hugohe3/ppt-master", "StarTrail-org/PixelRAG", "xbtlin/ai-berkshire", "zhaoxuya520/reverse-skill", "mukul975/Anthropic-Cybersecurity-Skills", "chopratejas/headroom", "Panniantong/Agent-Reach", "jamiepine/voicebox", "shanraisshan/claude-code-best-practice", "DeusData/codebase-memory-mcp", "ZhuLinsen/daily_stock_analysis", "apple/container", "DietrichGebert/ponytail", "calesthio/OpenMontage"], "data": [7, 8, 9, 9, 10, 10, 10, 11, 12, 12, 14, 15, 16, 17, 21, 21, 21, 33, 42, 54]},
        'weekly': {"categories": ["rtk-ai/rtk", "mvanhorn/last30days-skill", "elder-plinius/CL4R1T4S", "tursodatabase/turso", "apple/container", "colbymchenry/codegraph", "jamiepine/voicebox", "mukul975/Anthropic-Cybersecurity-Skills", "Kilo-Org/kilocode", "google-research/timesfm", "ZhuLinsen/daily_stock_analysis", "Leonxlnx/taste-skill", "EpicGames/lore", "penpot/penpot", "StarTrail-org/PixelRAG", "Panniantong/Agent-Reach", "calesthio/OpenMontage", "DeusData/codebase-memory-mcp", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [56, 56, 58, 62, 64, 65, 74, 75, 76, 95, 103, 112, 114, 116, 122, 152, 193, 206, 428, 523]},
        'monthly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "apple/container", "alibaba/open-code-review", "anthropics/knowledge-work-plugins", "RyanCodrai/turbovec", "Imbad0202/academic-research-skills", "elder-plinius/CL4R1T4S", "addyosmani/agent-skills", "Panniantong/Agent-Reach", "safishamsi/graphify", "mvanhorn/last30days-skill", "rohitg00/ai-engineering-from-scratch", "harry0703/MoneyPrinterTurbo", "DietrichGebert/ponytail", "Leonxlnx/taste-skill", "forrestchang/andrej-karpathy-skills", "chopratejas/headroom", "colbymchenry/codegraph", "Egonex-AI/Understand-Anything", "pewdiepie-archdaemon/odysseus"], "data": [404, 427, 428, 432, 432, 518, 626, 697, 700, 709, 847, 1040, 1068, 1225, 1253, 1328, 1489, 1523, 2039, 2579]}
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
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +54 | 19046 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +42 | 54920 |
| 3 | [apple/container](https://github.com/apple/container) | +33 | 42055 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +21 | 48378 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +21 | 14044 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +21 | 60000 |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +17 | 33817 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +16 | 39532 |
| 9 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +15 | 49789 |
| 10 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +14 | 20515 |
| 11 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +12 | 5220 |
| 12 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +12 | 1317 |
| 13 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +11 | 5137 |
| 14 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 31069 |
| 15 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +10 | 10316 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +10 | 19221 |
| 17 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +9 | 9071 |
| 18 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +9 | 28286 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 22962 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +7 | 65759 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 41113 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 31013 |
| 23 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +6 | 31044 |
| 24 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +6 | 2108 |
| 25 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +5 | 54154 |
| 26 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +5 | 7290 |
| 27 | [imbue-bit/AlphaGPT](https://github.com/imbue-bit/AlphaGPT) | +4 | 2322 |
| 28 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 6700 |
| 29 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +4 | 19497 |
| 30 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +4 | 46367 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +523 | 54920 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +428 | 49789 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +206 | 14044 |
| 4 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +193 | 19046 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +152 | 39532 |
| 6 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +122 | 5137 |
| 7 | [penpot/penpot](https://github.com/penpot/penpot) | +116 | 44370 |
| 8 | [EpicGames/lore](https://github.com/EpicGames/lore) | +114 | 6021 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +112 | 50237 |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +103 | 48378 |
| 11 | [google-research/timesfm](https://github.com/google-research/timesfm) | +95 | 25436 |
| 12 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +76 | 24425 |
| 13 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +75 | 20515 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +74 | 33817 |
| 15 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +65 | 54154 |
| 16 | [apple/container](https://github.com/apple/container) | +64 | 42055 |
| 17 | [tursodatabase/turso](https://github.com/tursodatabase/turso) | +62 | 22059 |
| 18 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +58 | 43744 |
| 19 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +56 | 46367 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +56 | 65759 |
| 21 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +54 | 10316 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +51 | 31013 |
| 23 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +51 | 32872 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +49 | 31069 |
| 25 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +49 | 9071 |
| 26 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +47 | 21578 |
| 27 | [vercel/eve](https://github.com/vercel/eve) | +45 | 2526 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +43 | 22962 |
| 29 | [withastro/flue](https://github.com/withastro/flue) | +42 | 6608 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +40 | 36828 |
| 31 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +37 | 34194 |
| 32 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +37 | 5402 |
| 33 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +37 | 14478 |
| 34 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +36 | 5221 |
| 35 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +36 | 1586 |
| 36 | [alibaba/zvec](https://github.com/alibaba/zvec) | +36 | 12386 |
| 37 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +36 | 5044 |
| 38 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +35 | 4710 |
| 39 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +33 | 36184 |
| 40 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +33 | 12074 |
| 41 | [nubjs/nub](https://github.com/nubjs/nub) | +33 | 1707 |
| 42 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +32 | 60000 |
| 43 | [blader/humanizer](https://github.com/blader/humanizer) | +32 | 25965 |
| 44 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +31 | 1228 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +31 | 34871 |
| 46 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +31 | 2569 |
| 47 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +31 | 20013 |
| 48 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +29 | 41113 |
| 49 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +28 | 29241 |
| 50 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +27 | 2108 |
| 51 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +27 | 1047 |
| 52 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +26 | 1599 |
| 53 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +25 | 6000 |
| 54 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +24 | 37046 |
| 55 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +24 | 7121 |
| 56 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 19221 |
| 57 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +23 | 8773 |
| 58 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +22 | 18037 |
| 59 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +21 | 987 |
| 60 | [stablyai/orca](https://github.com/stablyai/orca) | +21 | 6700 |
| 61 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +21 | 10606 |
| 62 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +21 | 25586 |
| 63 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +20 | 42894 |
| 64 | [mysk-research/loupe](https://github.com/mysk-research/loupe) | +20 | 1243 |
| 65 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +20 | 12695 |
| 66 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +20 | 21900 |
| 67 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +20 | 24003 |
| 68 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +20 | 32429 |
| 69 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +19 | 348 |
| 70 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +19 | 31044 |
| 71 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +19 | 31557 |
| 72 | [open-pencil/open-pencil](https://github.com/open-pencil/open-pencil) | +19 | 6251 |
| 73 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +19 | 3283 |
| 74 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 7979 |
| 75 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +18 | 19664 |
| 76 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +18 | 13212 |
| 77 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +18 | 3195 |
| 78 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +17 | 31904 |
| 79 | [overflowy/make-look-scanned](https://github.com/overflowy/make-look-scanned) | +17 | 402 |
| 80 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +17 | 8711 |
| 81 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +17 | 10941 |
| 82 | [playRealmRumble/Realm-Rumble](https://github.com/playRealmRumble/Realm-Rumble) | +17 | 691 |
| 83 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +17 | 5603 |
| 84 | [tamnd/kage](https://github.com/tamnd/kage) | +17 | 2386 |
| 85 | [shadcn/improve](https://github.com/shadcn/improve) | +17 | 6145 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +16 | 37869 |
| 87 | [antirez/ds4](https://github.com/antirez/ds4) | +16 | 15291 |
| 88 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +16 | 23528 |
| 89 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +16 | 12978 |
| 90 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 15899 |
| 91 | [yuanzhongqiao/deep-printfilm](https://github.com/yuanzhongqiao/deep-printfilm) | +15 | 2438 |
| 92 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +14 | 7290 |
| 93 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +14 | 8816 |
| 94 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +14 | 6070 |
| 95 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +14 | 26355 |
| 96 | [decolua/9router](https://github.com/decolua/9router) | +14 | 18386 |
| 97 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 27062 |
| 98 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +14 | 43753 |
| 99 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +14 | 2190 |
| 100 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +14 | 1346 |
| 101 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 22849 |
| 102 | [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) | +13 | 1764 |
| 103 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +13 | 8649 |
| 104 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +12 | 1317 |
| 105 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +12 | 1086 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +12 | 17454 |
| 107 | [microsoft/fastcontext](https://github.com/microsoft/fastcontext) | +12 | 920 |
| 108 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +12 | 4579 |
| 109 | [Project-N-E-K-O/N.E.K.O](https://github.com/Project-N-E-K-O/N.E.K.O) | +12 | 1787 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +12 | 38110 |
| 111 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +12 | 15319 |
| 112 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +11 | 18974 |
| 113 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +11 | 7044 |
| 114 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +11 | 9719 |
| 115 | [RUC-NLPIR/Arbor](https://github.com/RUC-NLPIR/Arbor) | +11 | 700 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +11 | 7720 |
| 117 | [kernalix7/winpodx](https://github.com/kernalix7/winpodx) | +11 | 1295 |
| 118 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +11 | 2658 |
| 119 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +11 | 3273 |
| 120 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +11 | 505 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2579 | 77378 |
| 2 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2039 | 67405 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1523 | 54154 |
| 4 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1489 | 49789 |
| 5 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1328 | 181522 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1253 | 50237 |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1225 | 54921 |
| 8 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1068 | 49621 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1040 | 36184 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +847 | 46367 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +709 | 71581 |
| 12 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +700 | 39532 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +697 | 66397 |
| 14 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +626 | 43744 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +518 | 34194 |
| 16 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +432 | 12169 |
| 17 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +432 | 21900 |
| 18 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +428 | 9072 |
| 19 | [apple/container](https://github.com/apple/container) | +427 | 42056 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +404 | 20515 |
| 21 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +403 | 33102 |
| 22 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +400 | 10127 |
| 23 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +380 | 31557 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +374 | 22962 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +373 | 65759 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +367 | 41113 |
| 27 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +360 | 31013 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +357 | 31069 |
| 29 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +356 | 10606 |
| 30 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8244 |
| 31 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +310 | 32919 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +304 | 14478 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +294 | 12074 |
| 34 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +292 | 36828 |
| 35 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +287 | 10316 |
| 36 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +287 | 27062 |
| 37 | [roboflow/supervision](https://github.com/roboflow/supervision) | +281 | 36553 |
| 38 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +278 | 23895 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +272 | 48378 |
| 40 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +260 | 4778 |
| 41 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +258 | 14969 |
| 42 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +244 | 14044 |
| 43 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +233 | 12684 |
| 44 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +231 | 28962 |
| 45 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +228 | 16899 |
| 46 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +226 | 19046 |
| 47 | [multica-ai/multica](https://github.com/multica-ai/multica) | +224 | 37869 |
| 48 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +221 | 21807 |
| 49 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +215 | 24003 |
| 50 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4347 |
| 51 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5446 |
| 52 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +209 | 32429 |
| 53 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +209 | 38959 |
| 54 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +208 | 35466 |
| 55 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +202 | 9940 |
| 56 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +199 | 19664 |
| 57 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +199 | 31044 |
| 58 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +197 | 31905 |
| 59 | [shadcn/improve](https://github.com/shadcn/improve) | +196 | 6145 |
| 60 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +195 | 27444 |
| 61 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +193 | 31185 |
| 62 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +189 | 22853 |
| 63 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +188 | 6000 |
| 64 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +187 | 18808 |
| 65 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +184 | 5587 |
| 66 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +183 | 33817 |
| 67 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +181 | 13212 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +179 | 25965 |
| 69 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +179 | 5100 |
| 70 | [penpot/penpot](https://github.com/penpot/penpot) | +178 | 44370 |
| 71 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +175 | 43753 |
| 72 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +174 | 4445 |
| 73 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +174 | 29241 |
| 74 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +174 | 39932 |
| 75 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +173 | 34871 |
| 76 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +173 | 31098 |
| 77 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +172 | 21985 |
| 78 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +171 | 11829 |
| 79 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +170 | 60000 |
| 80 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +170 | 23528 |
| 81 | [decolua/9router](https://github.com/decolua/9router) | +166 | 18386 |
| 82 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +162 | 5290 |
| 83 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +162 | 25842 |
| 84 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +159 | 7121 |
| 85 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +153 | 3585 |
| 86 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +153 | 15899 |
| 87 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +153 | 4995 |
| 88 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +151 | 18037 |
| 89 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +149 | 5044 |
| 90 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +149 | 25586 |
| 91 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +149 | 22849 |
| 92 | [google/skills](https://github.com/google/skills) | +148 | 14094 |
| 93 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +148 | 7384 |
| 94 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +148 | 6686 |
| 95 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +147 | 38303 |
| 96 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +147 | 10941 |
| 97 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +147 | 25436 |
| 98 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +147 | 4574 |
| 99 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +143 | 4710 |
| 100 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +142 | 32872 |
| 101 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +139 | 14128 |
| 102 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +136 | 10618 |
| 103 | [google-research/timesfm](https://github.com/google-research/timesfm) | +133 | 25436 |
| 104 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +133 | 20662 |
| 105 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +132 | 38110 |
| 106 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +131 | 17292 |
| 107 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +130 | 5137 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +129 | 7553 |
| 109 | [soxoj/maigret](https://github.com/soxoj/maigret) | +125 | 33642 |
| 110 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +122 | 4688 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +119 | 17454 |
| 112 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +117 | 7290 |
| 113 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +117 | 2685 |
| 114 | [EpicGames/lore](https://github.com/EpicGames/lore) | +114 | 6021 |
| 115 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +113 | 3490 |
| 116 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +112 | 49591 |
| 117 | [openai/skills](https://github.com/openai/skills) | +109 | 22821 |
| 118 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +107 | 35659 |
| 119 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +106 | 41612 |
| 120 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +106 | 3689 |
| 121 | [openai/plugins](https://github.com/openai/plugins) | +106 | 3485 |
| 122 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +105 | 5233 |
| 123 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +96 | 6879 |
| 124 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +94 | 4699 |
| 125 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +93 | 8773 |
| 126 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +93 | 4503 |
| 127 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +91 | 9719 |
| 128 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +90 | 24112 |
| 129 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +87 | 4612 |
| 130 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +86 | 25165 |
| 131 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +84 | 4455 |
| 132 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +84 | 47210 |
| 133 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +83 | 7871 |
| 134 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +82 | 8711 |
| 135 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +82 | 18974 |
| 136 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +82 | 25712 |
| 137 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +80 | 35662 |
| 138 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3791 |
| 139 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +78 | 11582 |
| 140 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +76 | 7720 |
| 141 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +76 | 1974 |
| 142 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +75 | 1679 |
| 143 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +75 | 12585 |
| 144 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +75 | 5262 |
| 145 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +74 | 20013 |
| 146 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +74 | 25080 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +74 | 17056 |
| 148 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +73 | 4579 |
| 149 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +73 | 2763 |
| 150 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +72 | 16807 |
| 151 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +71 | 2232 |
| 152 | [88lin/video_vip](https://github.com/88lin/video_vip) | +71 | 4209 |
| 153 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +70 | 7044 |
| 154 | [browser-use/video-use](https://github.com/browser-use/video-use) | +70 | 10144 |
| 155 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +70 | 0 |
| 156 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +70 | 7144 |
| 157 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +68 | 23878 |
| 158 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +68 | 4625 |
| 159 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +68 | 5869 |
| 160 | [browser-act/skills](https://github.com/browser-act/skills) | +65 | 2894 |
| 161 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +65 | 18794 |
| 162 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +64 | 15319 |
| 163 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +61 | 7467 |
| 164 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +61 | 18863 |
| 165 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +61 | 16287 |
| 166 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +60 | 44696 |
| 167 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +60 | 20090 |
| 168 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +60 | 3931 |
| 169 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 170 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +59 | 36103 |
| 171 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +58 | 8758 |
| 172 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +58 | 21567 |
| 173 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +57 | 3173 |
| 174 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +57 | 3291 |
| 175 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +55 | 14125 |
| 176 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +55 | 4738 |
| 177 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +54 | 1974 |
| 178 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +53 | 26007 |
| 179 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +53 | 7952 |
| 180 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +53 | 3453 |
| 181 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +52 | 4477 |
| 182 | [floci-io/floci](https://github.com/floci-io/floci) | +52 | 14416 |
| 183 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +51 | 2466 |
| 184 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +50 | 1835 |
| 185 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +49 | 37564 |
| 186 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +48 | 28920 |
| 187 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +48 | 3273 |
| 188 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +48 | 5836 |
| 189 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +47 | 1785 |
| 190 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +47 | 17168 |
| 191 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1144 |
| 192 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +44 | 1689 |
| 193 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +43 | 2569 |
| 194 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +42 | 2995 |
| 195 | [eze-is/web-access](https://github.com/eze-is/web-access) | +40 | 7848 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +39 | 28286 |
| 197 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +38 | 5284 |
| 198 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +38 | 1886 |
| 199 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +37 | 1107 |
| 200 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +36 | 1586 |
| 201 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +35 | 1086 |
| 202 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +35 | 5832 |
| 203 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +35 | 8300 |
| 204 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +35 | 1831 |
| 205 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +35 | 5480 |
| 206 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +35 | 683 |
| 207 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +34 | 845 |
| 208 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +32 | 4299 |
| 209 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +31 | 1220 |
| 210 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +31 | 4927 |
| 211 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +31 | 4045 |
| 212 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +30 | 9445 |
| 213 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +26 | 1233 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +26 | 2392 |
| 215 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +23 | 3919 |
| 216 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +23 | 2864 |
| 217 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 27 |
| 218 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +22 | 1311 |
| 219 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +22 | 813 |
| 220 | [zzzhhh1/free-nodes](https://github.com/zzzhhh1/free-nodes) | +21 | 0 |
| 221 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 573 |
| 222 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +21 | 5371 |
| 223 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +21 | 11354 |
| 224 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +21 | 13866 |
| 225 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +21 | 856 |
| 226 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +21 | 2476 |
| 227 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +20 | 998 |
| 228 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 530 |
| 229 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 986 |
| 230 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +20 | 528 |
| 231 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +19 | 348 |
| 232 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +19 | 1406 |
| 233 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +19 | 1982 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +19 | 2947 |
| 235 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +19 | 1487 |
| 236 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +18 | 4582 |
| 237 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +17 | 2401 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +17 | 2649 |
| 239 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +16 | 836 |
| 240 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +16 | 2339 |
| 241 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +16 | 2025 |
| 242 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +16 | 3362 |
| 243 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +16 | 2839 |
| 244 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +16 | 462 |
| 245 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 296 |
| 246 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +15 | 495 |
| 247 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +15 | 8298 |
| 248 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 391 |
| 249 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +15 | 1172 |
| 250 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 432 |
| 251 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +14 | 1738 |
| 252 | [Shiyao-Huang/awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) | +14 | 168 |
| 253 | [paraschopra/make-pages-interactive](https://github.com/paraschopra/make-pages-interactive) | +14 | 466 |
| 254 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +14 | 2572 |
| 255 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +14 | 2239 |
| 256 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +13 | 446 |
| 257 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +13 | 2175 |
| 258 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +13 | 4548 |
| 259 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +13 | 712 |
| 260 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 442 |
| 261 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +13 | 573 |
| 262 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 309 |
| 263 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +12 | 403 |
| 264 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +12 | 12164 |
| 265 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 260 |
| 266 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +12 | 764 |
| 267 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +12 | 387 |
| 268 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3541 |
| 269 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +10 | 364 |
| 270 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3064 |
| 271 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1691 |
| 272 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +9 | 1209 |
| 273 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +9 | 1019 |
| 274 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +9 | 659 |
| 275 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +9 | 326 |
| 276 | [emollick/concord](https://github.com/emollick/concord) | +8 | 194 |
| 277 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 3579 |
| 278 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 187 |
| 279 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2622 |
| 280 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 173 |
| 281 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2627 |
| 282 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +7 | 915 |
| 283 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +6 | 221 |
| 284 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +6 | 2521 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +6 | 1631 |
| 286 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +6 | 254 |
| 287 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +6 | 272 |
| 288 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 164 |
| 289 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 107 |
| 290 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +5 | 560 |
| 291 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 480 |
| 292 | [openmemind/memind](https://github.com/openmemind/memind) | +5 | 901 |
| 293 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 214 |
| 294 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +4 | 2701 |
| 295 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +4 | 2167 |
| 296 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +4 | 1037 |
| 297 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +4 | 830 |
| 298 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 505 |
| 299 | [structurizr/structurizr](https://github.com/structurizr/structurizr) | +4 | 262 |
| 300 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +4 | 75 |
