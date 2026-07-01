---
title: "2026-07-01 GitHub增长趋势报告"
description: "1.KittenTTS+12 2.ai-berkshire+11 3.Agent-Reach+9 4.Mineradio+8 5.strix+6"
date: 2026-07-01T21:39:29+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-01 21:39:29

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
        'daily': {"categories": ["makerspet/oomwoo", "simonlin1212/a-stock-data", "microsoft/SkillOpt", "deepseek-ai/DeepSpec", "millionco/react-doctor", "OthmanAdi/planning-with-files", "Robbyant/lingbot-map", "Yuan1z0825/nature-skills", "rtk-ai/rtk", "decolua/9router", "ogulcancelik/herdr", "hugohe3/ppt-master", "Yu9191/wloc", "browser-use/video-use", "facebook/astryx", "usestrix/strix", "XxHuberrr/Mineradio", "Panniantong/Agent-Reach", "xbtlin/ai-berkshire", "KittenML/KittenTTS"], "data": [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 8, 9, 11, 12]},
        'weekly': {"categories": ["jamiepine/voicebox", "mauriceboe/TREK", "zhaoxuya520/reverse-skill", "tashfeenahmed/freellmapi", "mukul975/Anthropic-Cybersecurity-Skills", "deepseek-ai/DeepSpec", "kunchenguid/no-mistakes", "stablyai/orca", "hugohe3/ppt-master", "apple/container", "bikini/exploitarium", "ZhuLinsen/daily_stock_analysis", "topoteretes/cognee", "JCodesMore/ai-website-cloner-template", "simplex-chat/simplex-chat", "xbtlin/ai-berkshire", "XxHuberrr/Mineradio", "Panniantong/Agent-Reach", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [54, 60, 61, 62, 67, 68, 72, 74, 82, 85, 89, 104, 105, 113, 129, 130, 152, 171, 200, 301]},
        'monthly': {"categories": ["unicity-astrid/sdk-js", "ZhuLinsen/daily_stock_analysis", "rohitg00/ai-engineering-from-scratch", "XiaomiMiMo/MiMo-Code", "RyanCodrai/turbovec", "unicity-astrid/astrid", "lfnovo/open-notebook", "alibaba/open-code-review", "BigPizzaV3/CodexPlusPlus", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "DietrichGebert/ponytail", "headroomlabs-ai/headroom", "pewdiepie-archdaemon/odysseus"], "data": [346, 347, 357, 368, 403, 404, 413, 419, 425, 453, 513, 529, 638, 723, 751, 846, 857, 1555, 1580, 2299]}
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
| 1 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +12 | 14631 |
| 2 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +11 | 8096 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +9 | 48266 |
| 4 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +8 | 6472 |
| 5 | [usestrix/strix](https://github.com/usestrix/strix) | +6 | 29542 |
| 6 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 2495 |
| 7 | [browser-use/video-use](https://github.com/browser-use/video-use) | +5 | 13177 |
| 8 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +4 | 2314 |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4 | 35757 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +4 | 9539 |
| 11 | [decolua/9router](https://github.com/decolua/9router) | +4 | 19310 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3 | 67662 |
| 13 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 24998 |
| 14 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +3 | 9205 |
| 15 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +3 | 24274 |
| 16 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +3 | 13317 |
| 17 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +3 | 5740 |
| 18 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +3 | 10328 |
| 19 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +3 | 6173 |
| 20 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +3 | 2315 |
| 21 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +3 | 6759 |
| 22 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 10222 |
| 23 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +3 | 35744 |
| 24 | [google/agents-cli](https://github.com/google/agents-cli) | +3 | 4566 |
| 25 | [chriswritescode-dev/opencode-manager](https://github.com/chriswritescode-dev/opencode-manager) | +3 | 670 |
| 26 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +3 | 20567 |
| 27 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +2 | 14546 |
| 28 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +2 | 29813 |
| 29 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +2 | 9653 |
| 30 | [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | +2 | 1029 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +301 | 30790 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +200 | 23730 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +171 | 48266 |
| 4 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +152 | 6472 |
| 5 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +130 | 8096 |
| 6 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +129 | 17547 |
| 7 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +113 | 24393 |
| 8 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +105 | 26375 |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +104 | 53048 |
| 10 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +89 | 3233 |
| 11 | [apple/container](https://github.com/apple/container) | +85 | 45625 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +82 | 35757 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +74 | 10222 |
| 14 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +72 | 4722 |
| 15 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +68 | 5740 |
| 16 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +67 | 23754 |
| 17 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +62 | 14546 |
| 18 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +61 | 7096 |
| 19 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +60 | 8777 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +54 | 36682 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +49 | 67662 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +43 | 61756 |
| 23 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +42 | 2315 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +41 | 42732 |
| 25 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +41 | 2492 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +40 | 24998 |
| 27 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +40 | 3690 |
| 28 | [every-app/open-seo](https://github.com/every-app/open-seo) | +40 | 3932 |
| 29 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +39 | 9539 |
| 30 | [EpicGames/lore](https://github.com/EpicGames/lore) | +38 | 7504 |
| 31 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +34 | 24232 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +34 | 32545 |
| 33 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +34 | 3297 |
| 34 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +34 | 48216 |
| 35 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +33 | 34056 |
| 36 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +33 | 9963 |
| 37 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +33 | 20919 |
| 38 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +33 | 4144 |
| 39 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +32 | 2314 |
| 40 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +32 | 35744 |
| 41 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +32 | 11740 |
| 42 | [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) | +32 | 1717 |
| 43 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +32 | 29276 |
| 44 | [antirez/ds4](https://github.com/antirez/ds4) | +31 | 17178 |
| 45 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +30 | 39053 |
| 46 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +30 | 9205 |
| 47 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +29 | 5432 |
| 48 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +29 | 10328 |
| 49 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +28 | 16461 |
| 50 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +28 | 26497 |
| 51 | [facebook/astryx](https://github.com/facebook/astryx) | +24 | 2495 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +24 | 37045 |
| 53 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +24 | 20567 |
| 54 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +23 | 8447 |
| 55 | [workweave/router](https://github.com/workweave/router) | +23 | 645 |
| 56 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +23 | 9729 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +23 | 27087 |
| 58 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +23 | 22838 |
| 59 | [browser-use/video-use](https://github.com/browser-use/video-use) | +22 | 13177 |
| 60 | [CyberStrikeus/CyberStrike](https://github.com/CyberStrikeus/CyberStrike) | +22 | 1068 |
| 61 | [nubjs/nub](https://github.com/nubjs/nub) | +22 | 2522 |
| 62 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +21 | 6173 |
| 63 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +21 | 9750 |
| 64 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 1674 |
| 65 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +20 | 9448 |
| 66 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 67 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +20 | 37991 |
| 68 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +20 | 22040 |
| 69 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +19 | 1667 |
| 70 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +18 | 24752 |
| 71 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +18 | 10500 |
| 72 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +18 | 1526 |
| 73 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +18 | 7749 |
| 74 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +18 | 5085 |
| 75 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +18 | 35721 |
| 76 | [revfactory/harness](https://github.com/revfactory/harness) | +18 | 8129 |
| 77 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +17 | 29813 |
| 78 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 5938 |
| 79 | [decolua/9router](https://github.com/decolua/9router) | +17 | 19310 |
| 80 | [deekur/gaokaomath](https://github.com/deekur/gaokaomath) | +17 | 1120 |
| 81 | [anbeime/skill](https://github.com/anbeime/skill) | +17 | 2896 |
| 82 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +16 | 1182 |
| 83 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +16 | 1553 |
| 84 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +16 | 870 |
| 85 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +16 | 27533 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +16 | 38730 |
| 87 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +16 | 5860 |
| 88 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +16 | 9748 |
| 89 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +15 | 5027 |
| 90 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +15 | 15495 |
| 91 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +15 | 537 |
| 92 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +14 | 14631 |
| 93 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +14 | 1170 |
| 94 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +14 | 24274 |
| 95 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +14 | 27037 |
| 96 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +14 | 24668 |
| 97 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +14 | 44426 |
| 98 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +14 | 11539 |
| 99 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +14 | 42162 |
| 100 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +14 | 5759 |
| 101 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +13 | 2827 |
| 102 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +13 | 31397 |
| 103 | [QwenLM/Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | +13 | 698 |
| 104 | [usestrix/strix](https://github.com/usestrix/strix) | +12 | 29542 |
| 105 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +12 | 1315 |
| 106 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +12 | 5271 |
| 107 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +12 | 14279 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +12 | 32295 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +11 | 10303 |
| 110 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +11 | 3074 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +11 | 19594 |
| 112 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +11 | 4856 |
| 113 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +10 | 32886 |
| 114 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +10 | 3681 |
| 115 | [openai/skills](https://github.com/openai/skills) | +10 | 23116 |
| 116 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +10 | 9077 |
| 117 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +10 | 2868 |
| 118 | [imbue-bit/AlphaGPT](https://github.com/imbue-bit/AlphaGPT) | +10 | 2681 |
| 119 | [Tejas-TA/predikit](https://github.com/Tejas-TA/predikit) | +9 | 392 |
| 120 | [hero8152/Infinite-Canvas](https://github.com/hero8152/Infinite-Canvas) | +9 | 1799 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2299 | 79938 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1580 | 55204 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1555 | 70367 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +857 | 48216 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +846 | 48266 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +751 | 56720 |
| 7 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +723 | 70087 |
| 8 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +638 | 44285 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +529 | 30790 |
| 10 | [apple/container](https://github.com/apple/container) | +513 | 45625 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +453 | 23730 |
| 12 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +425 | 22838 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +419 | 9748 |
| 14 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +413 | 34329 |
| 15 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +404 | 10314 |
| 16 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +403 | 12474 |
| 17 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +368 | 11205 |
| 18 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +357 | 37045 |
| 19 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +347 | 53048 |
| 20 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8213 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +331 | 32295 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +329 | 35757 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +326 | 42732 |
| 24 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +317 | 35744 |
| 25 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +315 | 32545 |
| 26 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +313 | 11740 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +304 | 67662 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +299 | 22040 |
| 29 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +292 | 24998 |
| 30 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +280 | 9750 |
| 31 | [roboflow/supervision](https://github.com/roboflow/supervision) | +275 | 36553 |
| 32 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +267 | 23754 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +262 | 14546 |
| 34 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +233 | 4949 |
| 35 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +219 | 18002 |
| 36 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4321 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +213 | 15495 |
| 38 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +207 | 35689 |
| 39 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +200 | 10328 |
| 40 | [shadcn/improve](https://github.com/shadcn/improve) | +199 | 6515 |
| 41 | [penpot/penpot](https://github.com/penpot/penpot) | +195 | 44370 |
| 42 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +191 | 5479 |
| 43 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +190 | 32516 |
| 44 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +189 | 6674 |
| 45 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +188 | 15287 |
| 46 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +187 | 24393 |
| 47 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +185 | 37991 |
| 48 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +182 | 36682 |
| 49 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +181 | 22499 |
| 50 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +180 | 20567 |
| 51 | [unicity-astrid/rfcs](https://github.com/unicity-astrid/rfcs) | +180 | 4307 |
| 52 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +177 | 29813 |
| 53 | [microsoft/coreutils](https://github.com/microsoft/coreutils) | +177 | 4574 |
| 54 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +176 | 16461 |
| 55 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +172 | 32872 |
| 56 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +171 | 24752 |
| 57 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +170 | 26375 |
| 58 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +167 | 12237 |
| 59 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +166 | 5860 |
| 60 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +165 | 61756 |
| 61 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +161 | 5938 |
| 62 | [EpicGames/lore](https://github.com/EpicGames/lore) | +158 | 7504 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +158 | 27087 |
| 64 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +155 | 7382 |
| 65 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +155 | 26219 |
| 66 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +153 | 5759 |
| 67 | [google-research/timesfm](https://github.com/google-research/timesfm) | +153 | 26336 |
| 68 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +152 | 6472 |
| 69 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3800 |
| 70 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +151 | 9539 |
| 71 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +149 | 35721 |
| 72 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +149 | 27533 |
| 73 | [stablyai/orca](https://github.com/stablyai/orca) | +147 | 10222 |
| 74 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +143 | 8096 |
| 75 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +143 | 12952 |
| 76 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +142 | 24419 |
| 77 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +141 | 34056 |
| 78 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +140 | 39053 |
| 79 | [google/skills](https://github.com/google/skills) | +138 | 14334 |
| 80 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +136 | 7096 |
| 81 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +136 | 19681 |
| 82 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +136 | 22411 |
| 83 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +135 | 26497 |
| 84 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +134 | 32886 |
| 85 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +134 | 22073 |
| 86 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +133 | 17547 |
| 87 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +129 | 16302 |
| 88 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +128 | 7936 |
| 89 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +126 | 31660 |
| 90 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +125 | 22262 |
| 91 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +124 | 24232 |
| 92 | [multica-ai/multica](https://github.com/multica-ai/multica) | +124 | 38730 |
| 93 | [revfactory/harness](https://github.com/revfactory/harness) | +121 | 8129 |
| 94 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +119 | 23970 |
| 95 | [withastro/flue](https://github.com/withastro/flue) | +116 | 7015 |
| 96 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 59 |
| 97 | [decolua/9router](https://github.com/decolua/9router) | +112 | 19310 |
| 98 | [openai/plugins](https://github.com/openai/plugins) | +112 | 3881 |
| 99 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +107 | 7749 |
| 100 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +106 | 5271 |
| 101 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +105 | 49836 |
| 102 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +104 | 9963 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +100 | 44426 |
| 104 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +96 | 4722 |
| 105 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +96 | 29748 |
| 106 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +94 | 25702 |
| 107 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +93 | 5632 |
| 108 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +92 | 5488 |
| 109 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +92 | 36239 |
| 110 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +91 | 4856 |
| 111 | [soxoj/maigret](https://github.com/soxoj/maigret) | +91 | 34748 |
| 112 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +90 | 3233 |
| 113 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +86 | 10303 |
| 114 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +86 | 47714 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +84 | 8447 |
| 116 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +84 | 42162 |
| 117 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +84 | 31396 |
| 118 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +84 | 10817 |
| 119 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +82 | 14443 |
| 120 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +81 | 17633 |
| 121 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +78 | 4008 |
| 122 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +77 | 4144 |
| 123 | [openai/skills](https://github.com/openai/skills) | +77 | 23116 |
| 124 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +76 | 1750 |
| 125 | [browser-use/video-use](https://github.com/browser-use/video-use) | +75 | 13177 |
| 126 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +75 | 4938 |
| 127 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +75 | 7794 |
| 128 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +75 | 3869 |
| 129 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +73 | 17864 |
| 130 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +72 | 9077 |
| 131 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +71 | 20408 |
| 132 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +70 | 19594 |
| 133 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +70 | 5611 |
| 134 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +68 | 5740 |
| 135 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +67 | 3672 |
| 136 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +67 | 4633 |
| 137 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +65 | 5218 |
| 138 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +65 | 25800 |
| 139 | [browser-act/skills](https://github.com/browser-act/skills) | +64 | 3416 |
| 140 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +63 | 25523 |
| 141 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +63 | 26033 |
| 142 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +62 | 24274 |
| 143 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +62 | 7385 |
| 144 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +62 | 6225 |
| 145 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +61 | 36103 |
| 146 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +59 | 1526 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +59 | 17360 |
| 148 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 149 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +57 | 11905 |
| 150 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +56 | 17068 |
| 151 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +56 | 7266 |
| 152 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +56 | 2868 |
| 153 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +56 | 3456 |
| 154 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +56 | 8835 |
| 155 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +55 | 3515 |
| 156 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +55 | 2990 |
| 157 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +53 | 3018 |
| 158 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +52 | 3824 |
| 159 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +52 | 2820 |
| 160 | [anbeime/skill](https://github.com/anbeime/skill) | +51 | 2896 |
| 161 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +51 | 26226 |
| 162 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +51 | 19244 |
| 163 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +50 | 1553 |
| 164 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +50 | 0 |
| 165 | [Forward-Future/loop-library](https://github.com/Forward-Future/loop-library) | +50 | 2250 |
| 166 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +49 | 44931 |
| 167 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +48 | 19071 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +48 | 7754 |
| 169 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +47 | 8088 |
| 170 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +46 | 22002 |
| 171 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +45 | 1939 |
| 172 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1178 |
| 173 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +44 | 15585 |
| 174 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +44 | 3500 |
| 175 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +44 | 16590 |
| 176 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +44 | 37564 |
| 177 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +43 | 3805 |
| 178 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +42 | 9205 |
| 179 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +42 | 4967 |
| 180 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +41 | 2827 |
| 181 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +40 | 1252 |
| 182 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +40 | 7339 |
| 183 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +37 | 1315 |
| 184 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +37 | 2042 |
| 185 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +36 | 1849 |
| 186 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +36 | 916 |
| 187 | [floci-io/floci](https://github.com/floci-io/floci) | +36 | 14645 |
| 188 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +35 | 1829 |
| 189 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +33 | 5429 |
| 190 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +33 | 5933 |
| 191 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9476 |
| 192 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +31 | 2314 |
| 193 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +31 | 28562 |
| 194 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1137 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +30 | 8513 |
| 196 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +29 | 4196 |
| 197 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +28 | 1195 |
| 198 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +27 | 837 |
| 199 | [eze-is/web-access](https://github.com/eze-is/web-access) | +26 | 8002 |
| 200 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +25 | 454 |
| 201 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +25 | 2011 |
| 202 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +24 | 1319 |
| 203 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +24 | 1352 |
| 204 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +24 | 769 |
| 205 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +23 | 1776 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +23 | 11512 |
| 207 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 28 |
| 208 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +22 | 422 |
| 209 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +21 | 598 |
| 210 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +21 | 2461 |
| 211 | [techjarves/Local-AI-Image-Generator](https://github.com/techjarves/Local-AI-Image-Generator) | +20 | 446 |
| 212 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +20 | 5599 |
| 213 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +20 | 2434 |
| 214 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +20 | 837 |
| 215 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 551 |
| 216 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +19 | 1311 |
| 217 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 624 |
| 218 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +18 | 5538 |
| 219 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 629 |
| 220 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +17 | 1461 |
| 221 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +16 | 4087 |
| 222 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +16 | 1170 |
| 223 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +16 | 537 |
| 224 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +16 | 13918 |
| 225 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +16 | 3939 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +16 | 2963 |
| 227 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2553 |
| 228 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +15 | 4955 |
| 229 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +15 | 4664 |
| 230 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +15 | 1112 |
| 231 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 461 |
| 232 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 525 |
| 233 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +14 | 12241 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +14 | 3069 |
| 235 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +14 | 2109 |
| 236 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +14 | 320 |
| 237 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +14 | 1014 |
| 238 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +14 | 8354 |
| 239 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +13 | 437 |
| 240 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 445 |
| 241 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +13 | 2721 |
| 242 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +13 | 856 |
| 243 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +12 | 473 |
| 244 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +12 | 1347 |
| 245 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 322 |
| 246 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +12 | 646 |
| 247 | [adamallcock/codex-chatgpt-control](https://github.com/adamallcock/codex-chatgpt-control) | +12 | 266 |
| 248 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +12 | 2656 |
| 249 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +12 | 2281 |
| 250 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +12 | 0 |
| 251 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +12 | 2525 |
| 252 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +11 | 0 |
| 253 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +11 | 753 |
| 254 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3612 |
| 255 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +11 | 587 |
| 256 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 187 |
| 257 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +10 | 2102 |
| 258 | [PatchMon/PatchMon](https://github.com/PatchMon/PatchMon) | +10 | 3046 |
| 259 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +9 | 1596 |
| 260 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +9 | 1111 |
| 261 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 211 |
| 262 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +9 | 1736 |
| 263 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 382 |
| 264 | [emollick/concord](https://github.com/emollick/concord) | +8 | 195 |
| 265 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +8 | 2228 |
| 266 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 3649 |
| 267 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +8 | 3088 |
| 268 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +8 | 669 |
| 269 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1252 |
| 270 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2680 |
| 271 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +7 | 273 |
| 272 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +7 | 419 |
| 273 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 188 |
| 274 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2683 |
| 275 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 314 |
| 276 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +6 | 160 |
| 277 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2708 |
| 278 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +6 | 1649 |
| 279 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +5 | 407 |
| 280 | [SecureBananaLabs/bug-bounty](https://github.com/SecureBananaLabs/bug-bounty) | +5 | 228 |
| 281 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +5 | 168 |
| 282 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2588 |
| 283 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 112 |
| 284 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +5 | 379 |
| 285 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 272 |
| 286 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 217 |
| 287 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 90 |
| 288 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 537 |
| 289 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +4 | 962 |
| 290 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 518 |
| 291 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +4 | 568 |
| 292 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 186 |
| 293 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 61 |
| 294 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 295 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 209 |
| 296 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 786 |
| 297 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +3 | 542 |
| 298 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 420 |
| 299 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +3 | 249 |
| 300 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
