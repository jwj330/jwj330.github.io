---
title: "2026-07-02 GitHub增长趋势报告"
description: "1.strix+65 2.box3d+56 3.Vibe-Trading+36 4.astryx+34 5.OpenMontage+31"
date: 2026-07-02T21:09:30+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-02 21:09:30

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
        'daily': {"categories": ["BigPizzaV3/CodexPlusPlus", "Yu9191/wloc", "xbtlin/ai-berkshire", "altic-dev/FluidVoice", "TencentCloud/CubeSandbox", "ZhuLinsen/daily_stock_analysis", "tt-a1i/archify", "hugohe3/ppt-master", "jamiepine/voicebox", "ogulcancelik/herdr", "makerspet/oomwoo", "DeusData/codebase-memory-mcp", "Panniantong/Agent-Reach", "stablyai/orca", "diegosouzapw/OmniRoute", "calesthio/OpenMontage", "facebook/astryx", "HKUDS/Vibe-Trading", "erincatto/box3d", "usestrix/strix"], "data": [13, 14, 14, 15, 15, 17, 17, 19, 21, 22, 22, 25, 26, 28, 29, 31, 34, 36, 56, 65]},
        'weekly': {"categories": ["mauriceboe/TREK", "jamiepine/voicebox", "mukul975/Anthropic-Cybersecurity-Skills", "HKUDS/Vibe-Trading", "apple/container", "makerspet/oomwoo", "deepseek-ai/DeepSpec", "stablyai/orca", "usestrix/strix", "ZhuLinsen/daily_stock_analysis", "bikini/exploitarium", "topoteretes/cognee", "hugohe3/ppt-master", "JCodesMore/ai-website-cloner-template", "simplex-chat/simplex-chat", "xbtlin/ai-berkshire", "XxHuberrr/Mineradio", "Panniantong/Agent-Reach", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [59, 61, 63, 63, 64, 64, 70, 77, 77, 87, 94, 96, 97, 108, 131, 136, 151, 155, 199, 232]},
        'monthly': {"categories": ["rohitg00/ai-engineering-from-scratch", "unicity-astrid/sdk-js", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "RyanCodrai/turbovec", "unicity-astrid/astrid", "BigPizzaV3/CodexPlusPlus", "alibaba/open-code-review", "lfnovo/open-notebook", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail", "pewdiepie-archdaemon/odysseus"], "data": [341, 346, 361, 369, 403, 404, 411, 414, 417, 478, 521, 558, 641, 688, 721, 869, 871, 1569, 1590, 2060]}
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
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +65 | 31909 |
| 2 | [erincatto/box3d](https://github.com/erincatto/box3d) | +56 | 1879 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +36 | 17278 |
| 4 | [facebook/astryx](https://github.com/facebook/astryx) | +34 | 3481 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +31 | 31655 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +29 | 10193 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +28 | 10961 |
| 8 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +26 | 49061 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +25 | 24581 |
| 10 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +22 | 2972 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +22 | 10094 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +21 | 37040 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +19 | 36112 |
| 14 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +17 | 2234 |
| 15 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +17 | 53505 |
| 16 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +15 | 7002 |
| 17 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +15 | 5842 |
| 18 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +14 | 8622 |
| 19 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +14 | 2550 |
| 20 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +13 | 23026 |
| 21 | [browser-use/video-use](https://github.com/browser-use/video-use) | +13 | 13731 |
| 22 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +12 | 48483 |
| 23 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +12 | 3025 |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 22550 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +12 | 67968 |
| 26 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +11 | 14797 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +11 | 15678 |
| 28 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 29948 |
| 29 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +11 | 24794 |
| 30 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +11 | 23978 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +232 | 31655 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +199 | 24581 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +155 | 49062 |
| 4 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +151 | 6856 |
| 5 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +136 | 8622 |
| 6 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +131 | 17652 |
| 7 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +108 | 24866 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +97 | 36112 |
| 9 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +96 | 26602 |
| 10 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +94 | 3461 |
| 11 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +87 | 53505 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +77 | 31909 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +77 | 10962 |
| 14 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +70 | 5867 |
| 15 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +64 | 2972 |
| 16 | [apple/container](https://github.com/apple/container) | +64 | 45857 |
| 17 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +63 | 17278 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +63 | 23978 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +61 | 37040 |
| 20 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +59 | 8884 |
| 21 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +58 | 10094 |
| 22 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +57 | 14797 |
| 23 | [erincatto/box3d](https://github.com/erincatto/box3d) | +56 | 1879 |
| 24 | [facebook/astryx](https://github.com/facebook/astryx) | +56 | 3481 |
| 25 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +50 | 4892 |
| 26 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +47 | 10193 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +47 | 67968 |
| 28 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +44 | 2550 |
| 29 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +41 | 5842 |
| 30 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +40 | 3704 |
| 31 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +40 | 61856 |
| 32 | [antirez/ds4](https://github.com/antirez/ds4) | +39 | 17316 |
| 33 | [every-app/open-seo](https://github.com/every-app/open-seo) | +38 | 3972 |
| 34 | [EpicGames/lore](https://github.com/EpicGames/lore) | +38 | 7564 |
| 35 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +37 | 35949 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +37 | 43028 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +36 | 25318 |
| 38 | [browser-use/video-use](https://github.com/browser-use/video-use) | +35 | 13731 |
| 39 | [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) | +35 | 1788 |
| 40 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +33 | 48483 |
| 41 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +33 | 11819 |
| 42 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +33 | 10067 |
| 43 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +32 | 34090 |
| 44 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +31 | 23026 |
| 45 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +31 | 24358 |
| 46 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +31 | 9391 |
| 47 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +31 | 3363 |
| 48 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +31 | 21257 |
| 49 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +29 | 39125 |
| 50 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +29 | 32760 |
| 51 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +28 | 10451 |
| 52 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +27 | 20697 |
| 53 | [AlexandrosGounis/pdfx](https://github.com/AlexandrosGounis/pdfx) | +26 | 653 |
| 54 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +26 | 13229 |
| 55 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +25 | 2234 |
| 56 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +25 | 1741 |
| 57 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +25 | 26603 |
| 58 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +23 | 14854 |
| 59 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +23 | 24794 |
| 60 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 15678 |
| 61 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +23 | 38244 |
| 62 | [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | +23 | 1077 |
| 63 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +23 | 2537 |
| 64 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +23 | 8541 |
| 65 | [workweave/router](https://github.com/workweave/router) | +23 | 698 |
| 66 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +22 | 4381 |
| 67 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +22 | 1329 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +22 | 27239 |
| 69 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +21 | 24835 |
| 70 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +21 | 29313 |
| 71 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +20 | 3025 |
| 72 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +20 | 22550 |
| 73 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +20 | 889 |
| 74 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +20 | 6258 |
| 75 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +20 | 7170 |
| 76 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 77 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +20 | 9760 |
| 78 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +20 | 1729 |
| 79 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +19 | 6041 |
| 80 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +19 | 10592 |
| 81 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +19 | 10733 |
| 82 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +19 | 22189 |
| 83 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +18 | 7002 |
| 84 | [decolua/9router](https://github.com/decolua/9router) | +18 | 19497 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +18 | 35859 |
| 86 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +18 | 9814 |
| 87 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +18 | 1560 |
| 88 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +17 | 29948 |
| 89 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +17 | 18209 |
| 90 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +17 | 11652 |
| 91 | [multica-ai/multica](https://github.com/multica-ai/multica) | +17 | 38852 |
| 92 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +17 | 7780 |
| 93 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +16 | 5747 |
| 94 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +16 | 45057 |
| 95 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +16 | 5999 |
| 96 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +16 | 42235 |
| 97 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +16 | 37152 |
| 98 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +16 | 1198 |
| 99 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +16 | 27578 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +15 | 29969 |
| 101 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +15 | 1004 |
| 102 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +15 | 24354 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +15 | 44570 |
| 104 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +14 | 16419 |
| 105 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +14 | 32359 |
| 106 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +13 | 3949 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +13 | 5345 |
| 108 | [anbeime/skill](https://github.com/anbeime/skill) | +13 | 3020 |
| 109 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +13 | 4908 |
| 110 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +13 | 1336 |
| 111 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +13 | 2844 |
| 112 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +12 | 3720 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +12 | 19718 |
| 114 | [openai/skills](https://github.com/openai/skills) | +12 | 23170 |
| 115 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +12 | 3095 |
| 116 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +11 | 7565 |
| 117 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +11 | 10384 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +11 | 31453 |
| 119 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +11 | 9111 |
| 120 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +11 | 14288 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2060 | 80191 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1590 | 71621 |
| 3 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1569 | 55807 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +871 | 49062 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +869 | 48483 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +721 | 57034 |
| 7 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +688 | 70377 |
| 8 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +641 | 44368 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +558 | 31655 |
| 10 | [apple/container](https://github.com/apple/container) | +521 | 45857 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +478 | 24581 |
| 12 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +417 | 34511 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +414 | 9818 |
| 14 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +411 | 23026 |
| 15 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +404 | 10315 |
| 16 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +403 | 12489 |
| 17 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +369 | 11290 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +361 | 53505 |
| 19 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8213 |
| 20 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +341 | 37152 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +333 | 36112 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +315 | 35949 |
| 23 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +313 | 11819 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +310 | 43028 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +309 | 67968 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +308 | 32761 |
| 27 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +304 | 32359 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +302 | 22189 |
| 29 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +282 | 9814 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +279 | 25318 |
| 31 | [roboflow/supervision](https://github.com/roboflow/supervision) | +279 | 36553 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +271 | 14797 |
| 33 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +268 | 23978 |
| 34 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +228 | 4989 |
| 35 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +226 | 18209 |
| 36 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4321 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +213 | 15678 |
| 38 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +209 | 17278 |
| 39 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +207 | 35719 |
| 40 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +202 | 24866 |
| 41 | [shadcn/improve](https://github.com/shadcn/improve) | +202 | 6588 |
| 42 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +198 | 22882 |
| 43 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +197 | 37040 |
| 44 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +197 | 10451 |
| 45 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +195 | 32632 |
| 46 | [penpot/penpot](https://github.com/penpot/penpot) | +193 | 44370 |
| 47 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +188 | 5504 |
| 48 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +185 | 6774 |
| 49 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +184 | 32872 |
| 50 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +183 | 38244 |
| 51 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +181 | 26602 |
| 52 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +181 | 20697 |
| 53 | [unicity-astrid/rfcs](https://github.com/unicity-astrid/rfcs) | +180 | 4307 |
| 54 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +177 | 4585 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +174 | 29969 |
| 56 | [stablyai/orca](https://github.com/stablyai/orca) | +172 | 10962 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +172 | 24835 |
| 58 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +169 | 5999 |
| 59 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +167 | 10094 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +166 | 61856 |
| 61 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +166 | 12271 |
| 62 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +165 | 6041 |
| 63 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +161 | 6856 |
| 64 | [EpicGames/lore](https://github.com/EpicGames/lore) | +160 | 7564 |
| 65 | [blader/humanizer](https://github.com/blader/humanizer) | +160 | 27239 |
| 66 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +156 | 8622 |
| 67 | [google-research/timesfm](https://github.com/google-research/timesfm) | +155 | 26411 |
| 68 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +154 | 5796 |
| 69 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +152 | 35859 |
| 70 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +148 | 3806 |
| 71 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +145 | 7565 |
| 72 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +145 | 26254 |
| 73 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +143 | 15332 |
| 74 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +142 | 27578 |
| 75 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +141 | 39125 |
| 76 | [google/skills](https://github.com/google/skills) | +138 | 14360 |
| 77 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +137 | 13004 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +135 | 26603 |
| 79 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +135 | 17652 |
| 80 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +135 | 24473 |
| 81 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +135 | 22185 |
| 82 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +134 | 7170 |
| 83 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +131 | 22485 |
| 84 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +130 | 19829 |
| 85 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +129 | 34090 |
| 86 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +129 | 32943 |
| 87 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +126 | 24358 |
| 88 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +123 | 31701 |
| 89 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +122 | 22289 |
| 90 | [multica-ai/multica](https://github.com/multica-ai/multica) | +121 | 38852 |
| 91 | [openai/plugins](https://github.com/openai/plugins) | +116 | 3929 |
| 92 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +114 | 24033 |
| 93 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 59 |
| 94 | [decolua/9router](https://github.com/decolua/9router) | +108 | 19497 |
| 95 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +108 | 16359 |
| 96 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +108 | 7976 |
| 97 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +107 | 10067 |
| 98 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +107 | 5345 |
| 99 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +106 | 7780 |
| 100 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +106 | 49886 |
| 101 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +104 | 4892 |
| 102 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +102 | 29948 |
| 103 | [usestrix/strix](https://github.com/usestrix/strix) | +101 | 31909 |
| 104 | [antirez/ds4](https://github.com/antirez/ds4) | +99 | 17316 |
| 105 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +96 | 3461 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +95 | 44570 |
| 107 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +95 | 5747 |
| 108 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +93 | 4908 |
| 109 | [soxoj/maigret](https://github.com/soxoj/maigret) | +92 | 34807 |
| 110 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +91 | 36336 |
| 111 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +90 | 5513 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +90 | 47801 |
| 113 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +86 | 42235 |
| 114 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +85 | 8541 |
| 115 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +84 | 10193 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +84 | 31453 |
| 117 | [browser-use/video-use](https://github.com/browser-use/video-use) | +83 | 13731 |
| 118 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +82 | 10384 |
| 119 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +82 | 25738 |
| 120 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +82 | 10838 |
| 121 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +81 | 4020 |
| 122 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +81 | 14481 |
| 123 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +81 | 17685 |
| 124 | [openai/skills](https://github.com/openai/skills) | +80 | 23170 |
| 125 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +78 | 24550 |
| 126 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +77 | 4381 |
| 127 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +76 | 1765 |
| 128 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +75 | 4978 |
| 129 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +74 | 20455 |
| 130 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +72 | 3888 |
| 131 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +71 | 19718 |
| 132 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +71 | 9111 |
| 133 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +71 | 17896 |
| 134 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +70 | 5867 |
| 135 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +69 | 5672 |
| 136 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +68 | 7819 |
| 137 | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | +68 | 33504 |
| 138 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +67 | 5316 |
| 139 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +67 | 4643 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +65 | 24354 |
| 141 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +65 | 25874 |
| 142 | [browser-act/skills](https://github.com/browser-act/skills) | +64 | 3481 |
| 143 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +63 | 3700 |
| 144 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +63 | 26085 |
| 145 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +62 | 25584 |
| 146 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +62 | 36103 |
| 147 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +60 | 1560 |
| 148 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +60 | 6291 |
| 149 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +59 | 1741 |
| 150 | [jundot/omlx](https://github.com/jundot/omlx) | +59 | 17412 |
| 151 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 152 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +59 | 22550 |
| 153 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +59 | 7478 |
| 154 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +57 | 17099 |
| 155 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +57 | 7291 |
| 156 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +56 | 3507 |
| 157 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +56 | 3133 |
| 158 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +56 | 8843 |
| 159 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +55 | 3949 |
| 160 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +55 | 2933 |
| 161 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +54 | 3535 |
| 162 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +54 | 3027 |
| 163 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +54 | 11928 |
| 164 | [anbeime/skill](https://github.com/anbeime/skill) | +53 | 3020 |
| 165 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +52 | 3864 |
| 166 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +52 | 2234 |
| 167 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +51 | 2844 |
| 168 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +51 | 19300 |
| 169 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +50 | 26256 |
| 170 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +50 | 2276 |
| 171 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +48 | 44965 |
| 172 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +47 | 1952 |
| 173 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +46 | 19094 |
| 174 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +46 | 7774 |
| 175 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +46 | 8111 |
| 176 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +45 | 2550 |
| 177 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1182 |
| 178 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +44 | 9391 |
| 179 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +44 | 15627 |
| 180 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +43 | 3572 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +43 | 16661 |
| 182 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +43 | 37564 |
| 183 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +42 | 2844 |
| 184 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +40 | 1256 |
| 185 | [floci-io/floci](https://github.com/floci-io/floci) | +38 | 14703 |
| 186 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +37 | 7367 |
| 187 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +37 | 5013 |
| 188 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +37 | 2056 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +36 | 7281 |
| 190 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +36 | 931 |
| 191 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +33 | 5443 |
| 192 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +33 | 9478 |
| 193 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +32 | 5940 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +30 | 28598 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +30 | 8555 |
| 196 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +29 | 4224 |
| 197 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +28 | 1210 |
| 198 | [eze-is/web-access](https://github.com/eze-is/web-access) | +28 | 8028 |
| 199 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +27 | 863 |
| 200 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +26 | 1409 |
| 201 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +25 | 1368 |
| 202 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +25 | 474 |
| 203 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +25 | 2044 |
| 204 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +24 | 1366 |
| 205 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +23 | 1329 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +23 | 11527 |
| 207 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +23 | 781 |
| 208 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 28 |
| 209 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +22 | 422 |
| 210 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 600 |
| 211 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +21 | 1787 |
| 212 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +21 | 2473 |
| 213 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +20 | 457 |
| 214 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +20 | 5606 |
| 215 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 556 |
| 216 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +19 | 4109 |
| 217 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 631 |
| 218 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +19 | 2440 |
| 219 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 640 |
| 220 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 560 |
| 221 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +17 | 5550 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +17 | 2976 |
| 223 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +16 | 13923 |
| 224 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +16 | 4959 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +15 | 2122 |
| 226 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +15 | 3942 |
| 227 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +15 | 4675 |
| 228 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 480 |
| 229 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 463 |
| 230 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2581 |
| 231 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 548 |
| 232 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +14 | 12259 |
| 233 | [robinebers/openusage](https://github.com/robinebers/openusage) | +14 | 3081 |
| 234 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +14 | 367 |
| 235 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +14 | 1014 |
| 236 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +14 | 1466 |
| 237 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +13 | 846 |
| 238 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +13 | 1833 |
| 239 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 446 |
| 240 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +13 | 2724 |
| 241 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +13 | 1113 |
| 242 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +12 | 1382 |
| 243 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 325 |
| 244 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +12 | 8363 |
| 245 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +12 | 444 |
| 246 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 268 |
| 247 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +12 | 2661 |
| 248 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +12 | 2284 |
| 249 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +12 | 856 |
| 250 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +11 | 0 |
| 251 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3620 |
| 252 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +11 | 0 |
| 253 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 198 |
| 254 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +10 | 1609 |
| 255 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +10 | 656 |
| 256 | [PatchMon/PatchMon](https://github.com/PatchMon/PatchMon) | +10 | 3049 |
| 257 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 3711 |
| 258 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +10 | 2529 |
| 259 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +10 | 589 |
| 260 | [emollick/concord](https://github.com/emollick/concord) | +9 | 198 |
| 261 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +9 | 1120 |
| 262 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +9 | 209 |
| 263 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 212 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +9 | 1744 |
| 265 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 384 |
| 266 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +8 | 286 |
| 267 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +8 | 445 |
| 268 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +8 | 3087 |
| 269 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +8 | 673 |
| 270 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1262 |
| 271 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2684 |
| 272 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 244 |
| 273 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 189 |
| 274 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2701 |
| 275 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 317 |
| 276 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +6 | 228 |
| 277 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 171 |
| 278 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2708 |
| 279 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +6 | 1651 |
| 280 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +5 | 415 |
| 281 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2599 |
| 282 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 115 |
| 283 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 519 |
| 284 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +5 | 386 |
| 285 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +4 | 229 |
| 286 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +4 | 212 |
| 287 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 277 |
| 288 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 218 |
| 289 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 92 |
| 290 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 545 |
| 291 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +4 | 968 |
| 292 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +4 | 569 |
| 293 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +3 | 405 |
| 294 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 188 |
| 295 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 62 |
| 296 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 297 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 787 |
| 298 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 420 |
| 299 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +3 | 251 |
| 300 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
