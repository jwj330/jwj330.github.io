---
title: "2026-07-03 GitHub增长趋势报告"
description: "1.strix+50 2.OpenMontage+19 3.astryx+18 4.openwiki+17 5.Vibe-Trading+17"
date: 2026-07-03T21:09:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-03 21:09:05

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
        'daily': {"categories": ["makerspet/oomwoo", "hugohe3/ppt-master", "baairon/torlink", "ChromeDevTools/chrome-devtools-mcp", "openai/codex-plugin-cc", "ZhuLinsen/daily_stock_analysis", "stablyai/orca", "ogulcancelik/herdr", "DeusData/codebase-memory-mcp", "opensquilla/opensquilla", "jamiepine/voicebox", "alibaba/page-agent", "browser-use/video-use", "Panniantong/Agent-Reach", "erincatto/box3d", "HKUDS/Vibe-Trading", "langchain-ai/openwiki", "facebook/astryx", "calesthio/OpenMontage", "usestrix/strix"], "data": [8, 8, 8, 10, 10, 10, 11, 11, 12, 13, 13, 13, 15, 16, 16, 17, 17, 18, 19, 50]},
        'weekly': {"categories": ["ogulcancelik/herdr", "jamiepine/voicebox", "stablyai/orca", "facebook/astryx", "makerspet/oomwoo", "erincatto/box3d", "deepseek-ai/DeepSpec", "HKUDS/Vibe-Trading", "ZhuLinsen/daily_stock_analysis", "topoteretes/cognee", "hugohe3/ppt-master", "JCodesMore/ai-website-cloner-template", "bikini/exploitarium", "xbtlin/ai-berkshire", "usestrix/strix", "simplex-chat/simplex-chat", "Panniantong/Agent-Reach", "XxHuberrr/Mineradio", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [62, 63, 68, 68, 70, 70, 72, 73, 74, 88, 88, 94, 97, 116, 121, 129, 145, 147, 201, 204]},
        'monthly': {"categories": ["hugohe3/ppt-master", "unicity-astrid/sdk-js", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "BigPizzaV3/CodexPlusPlus", "RyanCodrai/turbovec", "unicity-astrid/astrid", "alibaba/open-code-review", "lfnovo/open-notebook", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail", "pewdiepie-archdaemon/odysseus"], "data": [327, 346, 364, 369, 381, 402, 404, 409, 414, 487, 523, 571, 645, 648, 681, 867, 883, 1471, 1610, 1693]}
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
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +50 | 34425 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +19 | 32353 |
| 3 | [facebook/astryx](https://github.com/facebook/astryx) | +18 | 4491 |
| 4 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +17 | 1739 |
| 5 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +17 | 17676 |
| 6 | [erincatto/box3d](https://github.com/erincatto/box3d) | +16 | 2683 |
| 7 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +16 | 49793 |
| 8 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 14344 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +13 | 22337 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +13 | 37305 |
| 11 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +13 | 5372 |
| 12 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +12 | 25487 |
| 13 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +11 | 10673 |
| 14 | [stablyai/orca](https://github.com/stablyai/orca) | +11 | 11636 |
| 15 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +10 | 53835 |
| 16 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +10 | 23140 |
| 17 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +10 | 45451 |
| 18 | [baairon/torlink](https://github.com/baairon/torlink) | +8 | 2812 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 36421 |
| 20 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +8 | 3260 |
| 21 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +7 | 25265 |
| 22 | [google-research/tabfm](https://github.com/google-research/tabfm) | +6 | 1036 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 25640 |
| 24 | [Jamonygr/azure-landing-zone-lab](https://github.com/Jamonygr/azure-landing-zone-lab) | +6 | 425 |
| 25 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +6 | 7711 |
| 26 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +5 | 3626 |
| 27 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +5 | 10759 |
| 28 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +5 | 9121 |
| 29 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5 | 32951 |
| 30 | [flyfish-dev/file-viewer](https://github.com/flyfish-dev/file-viewer) | +5 | 844 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +204 | 32353 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +201 | 25487 |
| 3 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +147 | 7152 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +145 | 49793 |
| 5 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +129 | 17752 |
| 6 | [usestrix/strix](https://github.com/usestrix/strix) | +121 | 34426 |
| 7 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +116 | 9121 |
| 8 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +97 | 3594 |
| 9 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +94 | 25265 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +88 | 36421 |
| 11 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +88 | 26799 |
| 12 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +74 | 53835 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +73 | 17676 |
| 14 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +72 | 6046 |
| 15 | [erincatto/box3d](https://github.com/erincatto/box3d) | +70 | 2683 |
| 16 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +70 | 3260 |
| 17 | [facebook/astryx](https://github.com/facebook/astryx) | +68 | 4491 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +68 | 11636 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +63 | 37305 |
| 20 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +62 | 10673 |
| 21 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +62 | 13166 |
| 22 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +52 | 14966 |
| 23 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +51 | 5075 |
| 24 | [browser-use/video-use](https://github.com/browser-use/video-use) | +50 | 14344 |
| 25 | [apple/container](https://github.com/apple/container) | +49 | 46166 |
| 26 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | +49 | 45474 |
| 27 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +46 | 1739 |
| 28 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +46 | 9056 |
| 29 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +45 | 10759 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +43 | 68263 |
| 31 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +41 | 5953 |
| 32 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +41 | 24153 |
| 33 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +39 | 2749 |
| 34 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +36 | 9553 |
| 35 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +35 | 36104 |
| 36 | [antirez/ds4](https://github.com/antirez/ds4) | +35 | 17438 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +34 | 43269 |
| 38 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +34 | 3714 |
| 39 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +33 | 25640 |
| 40 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +33 | 34126 |
| 41 | [EpicGames/lore](https://github.com/EpicGames/lore) | +33 | 7636 |
| 42 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +32 | 22337 |
| 43 | [every-app/open-seo](https://github.com/every-app/open-seo) | +32 | 3997 |
| 44 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +31 | 24457 |
| 45 | [google-research/tabfm](https://github.com/google-research/tabfm) | +30 | 1036 |
| 46 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +30 | 48701 |
| 47 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +30 | 11903 |
| 48 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +30 | 10157 |
| 49 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +28 | 39179 |
| 50 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +27 | 23140 |
| 51 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +27 | 1808 |
| 52 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +27 | 32951 |
| 53 | [AlexandrosGounis/pdfx](https://github.com/AlexandrosGounis/pdfx) | +27 | 679 |
| 54 | [baairon/torlink](https://github.com/baairon/torlink) | +26 | 2812 |
| 55 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +26 | 3415 |
| 56 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +25 | 2449 |
| 57 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +25 | 5372 |
| 58 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +25 | 23186 |
| 59 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +24 | 14901 |
| 60 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +24 | 45451 |
| 61 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +24 | 10552 |
| 62 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +24 | 20798 |
| 63 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +23 | 3177 |
| 64 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +23 | 24929 |
| 65 | [workweave/router](https://github.com/workweave/router) | +23 | 718 |
| 66 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +22 | 38421 |
| 67 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +22 | 1415 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +22 | 27383 |
| 69 | [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | +22 | 1086 |
| 70 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +21 | 4539 |
| 71 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +21 | 15826 |
| 72 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +21 | 6158 |
| 73 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +21 | 24947 |
| 74 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +21 | 61923 |
| 75 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +21 | 8612 |
| 76 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +20 | 914 |
| 77 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 78 | [decolua/9router](https://github.com/decolua/9router) | +19 | 19667 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +19 | 26752 |
| 80 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +19 | 4201 |
| 81 | [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) | +19 | 1820 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +18 | 35976 |
| 83 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +18 | 2579 |
| 84 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +18 | 44667 |
| 85 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +18 | 6336 |
| 86 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +18 | 7822 |
| 87 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +18 | 1580 |
| 88 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +17 | 7140 |
| 89 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +17 | 18273 |
| 90 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +17 | 6093 |
| 91 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +17 | 11727 |
| 92 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +17 | 1213 |
| 93 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +17 | 1756 |
| 94 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +16 | 30125 |
| 95 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +16 | 30058 |
| 96 | [multica-ai/multica](https://github.com/multica-ai/multica) | +16 | 38990 |
| 97 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +16 | 16524 |
| 98 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +16 | 24437 |
| 99 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +16 | 1103 |
| 100 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +15 | 7711 |
| 101 | [openai/plugins](https://github.com/openai/plugins) | +15 | 3972 |
| 102 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +15 | 42293 |
| 103 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +15 | 22345 |
| 104 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +15 | 37248 |
| 105 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 27672 |
| 106 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +14 | 9164 |
| 107 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +14 | 1348 |
| 108 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +13 | 3981 |
| 109 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +12 | 24079 |
| 110 | [openai/skills](https://github.com/openai/skills) | +12 | 23205 |
| 111 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +12 | 3744 |
| 112 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +12 | 32412 |
| 113 | [aquace/CVE-2026-41940-PoC](https://github.com/aquace/CVE-2026-41940-PoC) | +11 | 6 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +11 | 19834 |
| 115 | [Pluviobyte/video-production-skills](https://github.com/Pluviobyte/video-production-skills) | +11 | 500 |
| 116 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +11 | 14293 |
| 117 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +10 | 31503 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +10 | 17145 |
| 119 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +10 | 3112 |
| 120 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +10 | 5397 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1693 | 80433 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1610 | 72912 |
| 3 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1471 | 56224 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +883 | 49793 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +867 | 48701 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +681 | 57332 |
| 7 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +648 | 70649 |
| 8 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +645 | 44496 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +571 | 32353 |
| 10 | [apple/container](https://github.com/apple/container) | +523 | 46166 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +487 | 25487 |
| 12 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +414 | 34661 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +409 | 9881 |
| 14 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +404 | 10312 |
| 15 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +402 | 12516 |
| 16 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +381 | 23186 |
| 17 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +369 | 11363 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +364 | 53835 |
| 19 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8210 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +327 | 36421 |
| 21 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +326 | 37248 |
| 22 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +313 | 11903 |
| 23 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +304 | 22345 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +303 | 32951 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +301 | 68263 |
| 26 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +301 | 36104 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +291 | 43269 |
| 28 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +284 | 9871 |
| 29 | [roboflow/supervision](https://github.com/roboflow/supervision) | +279 | 36553 |
| 30 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +277 | 32412 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +275 | 25640 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +272 | 14966 |
| 33 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +269 | 24153 |
| 34 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +229 | 18273 |
| 35 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +229 | 5032 |
| 36 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4321 |
| 37 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +213 | 13166 |
| 38 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +213 | 17676 |
| 39 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +207 | 35728 |
| 40 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +206 | 37305 |
| 41 | [shadcn/improve](https://github.com/shadcn/improve) | +204 | 6738 |
| 42 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +201 | 25265 |
| 43 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +200 | 15826 |
| 44 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +192 | 22995 |
| 45 | [penpot/penpot](https://github.com/penpot/penpot) | +191 | 44370 |
| 46 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +190 | 32699 |
| 47 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +188 | 10552 |
| 48 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +187 | 5528 |
| 49 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +186 | 6874 |
| 50 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +185 | 32872 |
| 51 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +181 | 20798 |
| 52 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +180 | 26799 |
| 53 | [unicity-astrid/rfcs](https://github.com/unicity-astrid/rfcs) | +180 | 4307 |
| 54 | [stablyai/orca](https://github.com/stablyai/orca) | +178 | 11636 |
| 55 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +176 | 38421 |
| 56 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +171 | 6093 |
| 57 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +170 | 10673 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +170 | 30125 |
| 59 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +168 | 6158 |
| 60 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +164 | 7152 |
| 61 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +164 | 24947 |
| 62 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +163 | 61923 |
| 63 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +161 | 9121 |
| 64 | [EpicGames/lore](https://github.com/EpicGames/lore) | +160 | 7636 |
| 65 | [blader/humanizer](https://github.com/blader/humanizer) | +159 | 27383 |
| 66 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +156 | 5840 |
| 67 | [google-research/timesfm](https://github.com/google-research/timesfm) | +156 | 26474 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +150 | 35976 |
| 69 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +148 | 3835 |
| 70 | [usestrix/strix](https://github.com/usestrix/strix) | +143 | 34426 |
| 71 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +140 | 7711 |
| 72 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +140 | 12291 |
| 73 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +138 | 39179 |
| 74 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +138 | 17752 |
| 75 | [google/skills](https://github.com/google/skills) | +137 | 14373 |
| 76 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +136 | 27672 |
| 77 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +135 | 22286 |
| 78 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +134 | 7204 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +133 | 26752 |
| 80 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +133 | 24510 |
| 81 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +127 | 26276 |
| 82 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +125 | 24457 |
| 83 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +125 | 34126 |
| 84 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +122 | 13041 |
| 85 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +121 | 19962 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +120 | 38990 |
| 87 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +120 | 32979 |
| 88 | [openai/plugins](https://github.com/openai/plugins) | +119 | 3972 |
| 89 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +117 | 22315 |
| 90 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +117 | 31730 |
| 91 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +114 | 15391 |
| 92 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 59 |
| 93 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +113 | 24079 |
| 94 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +111 | 5372 |
| 95 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +110 | 5075 |
| 96 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +107 | 49910 |
| 97 | [decolua/9router](https://github.com/decolua/9router) | +106 | 19667 |
| 98 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +105 | 10157 |
| 99 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +105 | 7822 |
| 100 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +105 | 8012 |
| 101 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +101 | 30058 |
| 102 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +100 | 16422 |
| 103 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +99 | 3594 |
| 104 | [antirez/ds4](https://github.com/antirez/ds4) | +96 | 17438 |
| 105 | [browser-use/video-use](https://github.com/browser-use/video-use) | +96 | 14344 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +94 | 44667 |
| 107 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +94 | 4960 |
| 108 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +92 | 2258 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +88 | 47902 |
| 110 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +86 | 9056 |
| 111 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +86 | 36414 |
| 112 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +85 | 42293 |
| 113 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +85 | 8612 |
| 114 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +84 | 5536 |
| 115 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +83 | 10759 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +82 | 31503 |
| 117 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +82 | 5826 |
| 118 | [openai/skills](https://github.com/openai/skills) | +80 | 23205 |
| 119 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +80 | 4032 |
| 120 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +80 | 14520 |
| 121 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +79 | 10447 |
| 122 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +79 | 10864 |
| 123 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +77 | 4539 |
| 124 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +76 | 17735 |
| 125 | [facebook/astryx](https://github.com/facebook/astryx) | +75 | 4491 |
| 126 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +75 | 5020 |
| 127 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +75 | 25764 |
| 128 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +73 | 20510 |
| 129 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +72 | 6046 |
| 130 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +72 | 9164 |
| 131 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +70 | 19834 |
| 132 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +70 | 17946 |
| 133 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +69 | 1766 |
| 134 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +69 | 5714 |
| 135 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +68 | 3906 |
| 136 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +66 | 24437 |
| 137 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +65 | 23141 |
| 138 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +64 | 25652 |
| 139 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +64 | 7850 |
| 140 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +64 | 5397 |
| 141 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +64 | 4652 |
| 142 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +64 | 36103 |
| 143 | [browser-act/skills](https://github.com/browser-act/skills) | +62 | 3554 |
| 144 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +62 | 25961 |
| 145 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +61 | 1808 |
| 146 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +60 | 1580 |
| 147 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +60 | 7534 |
| 148 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +60 | 26114 |
| 149 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +59 | 3734 |
| 150 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 151 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +59 | 3348 |
| 152 | [jundot/omlx](https://github.com/jundot/omlx) | +58 | 17448 |
| 153 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +57 | 17145 |
| 154 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +57 | 3059 |
| 155 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +56 | 7312 |
| 156 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +56 | 2987 |
| 157 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +56 | 3540 |
| 158 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +56 | 8848 |
| 159 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +55 | 3981 |
| 160 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +55 | 2449 |
| 161 | [anbeime/skill](https://github.com/anbeime/skill) | +54 | 3087 |
| 162 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +54 | 3549 |
| 163 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +54 | 19351 |
| 164 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +53 | 6343 |
| 165 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +51 | 11950 |
| 166 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +50 | 2853 |
| 167 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +50 | 3919 |
| 168 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +50 | 2344 |
| 169 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +48 | 9553 |
| 170 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +48 | 44987 |
| 171 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +48 | 26296 |
| 172 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +47 | 1955 |
| 173 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +47 | 2749 |
| 174 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +45 | 19134 |
| 175 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1186 |
| 176 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +45 | 37564 |
| 177 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +44 | 15670 |
| 178 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +44 | 7813 |
| 179 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +43 | 16742 |
| 180 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +42 | 2859 |
| 181 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +42 | 3630 |
| 182 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +42 | 8137 |
| 183 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +39 | 1258 |
| 184 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +39 | 1348 |
| 185 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +38 | 7387 |
| 186 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +36 | 5044 |
| 187 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +36 | 2071 |
| 188 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +36 | 948 |
| 189 | [floci-io/floci](https://github.com/floci-io/floci) | +36 | 14833 |
| 190 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +33 | 7307 |
| 191 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +33 | 9480 |
| 192 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +32 | 5467 |
| 193 | [google-research/tabfm](https://github.com/google-research/tabfm) | +30 | 1036 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +29 | 28624 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +29 | 8581 |
| 196 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +29 | 5950 |
| 197 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +27 | 1415 |
| 198 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +27 | 1134 |
| 199 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +27 | 1227 |
| 200 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +27 | 877 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +27 | 8050 |
| 202 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +27 | 4238 |
| 203 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +25 | 1416 |
| 204 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +25 | 1468 |
| 205 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +25 | 496 |
| 206 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +24 | 2064 |
| 207 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +24 | 1371 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +23 | 11554 |
| 209 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +22 | 427 |
| 210 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 608 |
| 211 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +22 | 792 |
| 212 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +21 | 2485 |
| 213 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +20 | 469 |
| 214 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +20 | 1798 |
| 215 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 561 |
| 216 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 632 |
| 217 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +19 | 5639 |
| 218 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +18 | 2448 |
| 219 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 649 |
| 220 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +17 | 4140 |
| 221 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 584 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +17 | 2987 |
| 223 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +16 | 13939 |
| 224 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +16 | 4960 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +16 | 4693 |
| 226 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +15 | 5564 |
| 227 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +15 | 470 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +15 | 399 |
| 229 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +15 | 2737 |
| 230 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 485 |
| 231 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +14 | 1415 |
| 232 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 466 |
| 233 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2597 |
| 234 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 562 |
| 235 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +14 | 2134 |
| 236 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +14 | 3940 |
| 237 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +13 | 12276 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +13 | 3094 |
| 239 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +13 | 1494 |
| 240 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +13 | 1015 |
| 241 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +13 | 1470 |
| 242 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 450 |
| 243 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +12 | 176 |
| 244 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 326 |
| 245 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +12 | 8368 |
| 246 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +12 | 2290 |
| 247 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +12 | 856 |
| 248 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +12 | 1114 |
| 249 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +11 | 0 |
| 250 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 3745 |
| 251 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3624 |
| 252 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +11 | 2669 |
| 253 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +11 | 0 |
| 254 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 198 |
| 255 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +10 | 1620 |
| 256 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +10 | 679 |
| 257 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +10 | 1836 |
| 258 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +10 | 2534 |
| 259 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +9 | 292 |
| 260 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +9 | 295 |
| 261 | [emollick/concord](https://github.com/emollick/concord) | +9 | 199 |
| 262 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +9 | 835 |
| 263 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +9 | 269 |
| 264 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 215 |
| 265 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 388 |
| 266 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +8 | 450 |
| 267 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +8 | 1746 |
| 268 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +8 | 28 |
| 269 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1272 |
| 270 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2691 |
| 271 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 244 |
| 272 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 190 |
| 273 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2708 |
| 274 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 321 |
| 275 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 172 |
| 276 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +6 | 679 |
| 277 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +6 | 1654 |
| 278 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +6 | 590 |
| 279 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +5 | 426 |
| 280 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2607 |
| 281 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 116 |
| 282 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 521 |
| 283 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +5 | 395 |
| 284 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +4 | 214 |
| 285 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 280 |
| 286 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 218 |
| 287 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 93 |
| 288 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 552 |
| 289 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +4 | 976 |
| 290 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +4 | 571 |
| 291 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +3 | 426 |
| 292 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 189 |
| 293 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 65 |
| 294 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 295 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 799 |
| 296 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 423 |
| 297 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +3 | 251 |
| 298 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 299 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +3 | 5192 |
| 300 | [huxuehao/apboa](https://github.com/huxuehao/apboa) | +3 | 167 |
