---
title: "2026-07-04 GitHub增长趋势报告"
description: "1.strix+41 2.box3d+36 3.page-agent+35 4.astryx+31 5.codebase-memory-mcp+22"
date: 2026-07-04T20:59:22+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-04 20:59:22

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
        'daily': {"categories": ["Emily2040/seedance-2.0", "xbtlin/ai-berkshire", "ZhuLinsen/daily_stock_analysis", "jamiepine/voicebox", "browser-use/video-use", "diegosouzapw/OmniRoute", "Panniantong/Agent-Reach", "Yu9191/wloc", "ctxrs/ctx", "langchain-ai/openwiki", "stablyai/orca", "calesthio/OpenMontage", "MadsLorentzen/ai-job-search", "ogulcancelik/herdr", "openai/codex-plugin-cc", "DeusData/codebase-memory-mcp", "facebook/astryx", "alibaba/page-agent", "erincatto/box3d", "usestrix/strix"], "data": [7, 7, 8, 10, 11, 11, 11, 12, 12, 13, 15, 16, 19, 20, 22, 22, 31, 35, 36, 41]},
        'weekly': {"categories": ["alibaba/page-agent", "langchain-ai/openwiki", "jamiepine/voicebox", "ogulcancelik/herdr", "deepseek-ai/DeepSpec", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "ZhuLinsen/daily_stock_analysis", "topoteretes/cognee", "hugohe3/ppt-master", "HKUDS/Vibe-Trading", "bikini/exploitarium", "facebook/astryx", "xbtlin/ai-berkshire", "XxHuberrr/Mineradio", "erincatto/box3d", "Panniantong/Agent-Reach", "calesthio/OpenMontage", "DeusData/codebase-memory-mcp", "usestrix/strix"], "data": [56, 58, 60, 62, 63, 64, 66, 68, 69, 71, 76, 78, 91, 93, 100, 105, 107, 152, 155, 160]},
        'monthly': {"categories": ["phuryn/pm-skills", "rohitg00/ai-engineering-from-scratch", "NVIDIA/SkillSpector", "hugohe3/ppt-master", "ZhuLinsen/daily_stock_analysis", "BigPizzaV3/CodexPlusPlus", "XiaomiMiMo/MiMo-Code", "RyanCodrai/turbovec", "alibaba/open-code-review", "lfnovo/open-notebook", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "colbymchenry/codegraph", "elder-plinius/CL4R1T4S", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "pewdiepie-archdaemon/odysseus", "DietrichGebert/ponytail"], "data": [304, 311, 314, 328, 353, 362, 372, 401, 405, 412, 508, 530, 585, 625, 648, 868, 887, 1370, 1376, 1643]}
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
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +41 | 35908 |
| 2 | [erincatto/box3d](https://github.com/erincatto/box3d) | +36 | 3327 |
| 3 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +35 | 23022 |
| 4 | [facebook/astryx](https://github.com/facebook/astryx) | +31 | 5286 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +22 | 26103 |
| 6 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +22 | 24225 |
| 7 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +20 | 11350 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 4586 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +16 | 33035 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +15 | 11987 |
| 11 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +13 | 2868 |
| 12 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +12 | 618 |
| 13 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +12 | 2929 |
| 14 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +11 | 50551 |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +11 | 11266 |
| 16 | [browser-use/video-use](https://github.com/browser-use/video-use) | +11 | 14655 |
| 17 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +10 | 37660 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +8 | 54235 |
| 19 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 9643 |
| 20 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +7 | 2076 |
| 21 | [baairon/torlink](https://github.com/baairon/torlink) | +7 | 2947 |
| 22 | [jaipreet15/tradingview-mcp](https://github.com/jaipreet15/tradingview-mcp) | +7 | 153 |
| 23 | [Maka-Agent/maka-agent](https://github.com/Maka-Agent/maka-agent) | +7 | 579 |
| 24 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +6 | 837 |
| 25 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +6 | 24363 |
| 26 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +6 | 1559 |
| 27 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +6 | 4092 |
| 28 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +6 | 560 |
| 29 | [infragate/capa](https://github.com/infragate/capa) | +6 | 668 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +6 | 36617 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +160 | 35908 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +155 | 26103 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +152 | 33035 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +107 | 50551 |
| 5 | [erincatto/box3d](https://github.com/erincatto/box3d) | +105 | 3327 |
| 6 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +100 | 7358 |
| 7 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +93 | 9643 |
| 8 | [facebook/astryx](https://github.com/facebook/astryx) | +91 | 5286 |
| 9 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +78 | 3645 |
| 10 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +76 | 17771 |
| 11 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +71 | 36617 |
| 12 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +69 | 26954 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +68 | 54235 |
| 14 | [stablyai/orca](https://github.com/stablyai/orca) | +66 | 11987 |
| 15 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +64 | 25516 |
| 16 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +63 | 6162 |
| 17 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +62 | 11350 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +60 | 37660 |
| 19 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +58 | 2868 |
| 20 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +56 | 23022 |
| 21 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +55 | 3452 |
| 22 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +53 | 11266 |
| 23 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | +53 | 45474 |
| 24 | [browser-use/video-use](https://github.com/browser-use/video-use) | +52 | 14655 |
| 25 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +46 | 24225 |
| 26 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +44 | 2929 |
| 27 | [apple/container](https://github.com/apple/container) | +44 | 46410 |
| 28 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +42 | 32872 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +41 | 68482 |
| 30 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +39 | 24363 |
| 31 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +37 | 6078 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +36 | 15082 |
| 33 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +35 | 26515 |
| 34 | [baairon/torlink](https://github.com/baairon/torlink) | +33 | 2947 |
| 35 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +32 | 13258 |
| 36 | [google-research/tabfm](https://github.com/google-research/tabfm) | +31 | 1135 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 25912 |
| 38 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +30 | 9719 |
| 39 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +30 | 15076 |
| 40 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +29 | 2583 |
| 41 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +29 | 5194 |
| 42 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +28 | 43469 |
| 43 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +27 | 1848 |
| 44 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +26 | 45734 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +26 | 33101 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +26 | 36232 |
| 47 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +25 | 48904 |
| 48 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +25 | 23323 |
| 49 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +25 | 39235 |
| 50 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +24 | 3237 |
| 51 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +24 | 11949 |
| 52 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +24 | 10234 |
| 53 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +23 | 14924 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +22 | 16035 |
| 55 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +22 | 5385 |
| 56 | [antirez/ds4](https://github.com/antirez/ds4) | +22 | 17544 |
| 57 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +22 | 6222 |
| 58 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +22 | 24526 |
| 59 | [every-app/open-seo](https://github.com/every-app/open-seo) | +22 | 4022 |
| 60 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +21 | 7284 |
| 61 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +21 | 1574 |
| 62 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +21 | 9133 |
| 63 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +20 | 4586 |
| 64 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +20 | 25017 |
| 65 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +20 | 25005 |
| 66 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +20 | 38566 |
| 67 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +19 | 4680 |
| 68 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +19 | 10596 |
| 69 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +19 | 20847 |
| 70 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +19 | 34153 |
| 71 | [decolua/9router](https://github.com/decolua/9router) | +18 | 19791 |
| 72 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +18 | 30209 |
| 73 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +18 | 16598 |
| 74 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +17 | 618 |
| 75 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +17 | 18308 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +17 | 26845 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +17 | 36090 |
| 78 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +17 | 9939 |
| 79 | [multica-ai/multica](https://github.com/multica-ai/multica) | +16 | 39040 |
| 80 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +16 | 1174 |
| 81 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +16 | 7805 |
| 82 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +16 | 24496 |
| 83 | [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | +16 | 11767 |
| 84 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +16 | 944 |
| 85 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +16 | 7838 |
| 86 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +15 | 4096 |
| 87 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +15 | 30143 |
| 88 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +15 | 4287 |
| 89 | [blader/humanizer](https://github.com/blader/humanizer) | +15 | 27473 |
| 90 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +14 | 837 |
| 91 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +14 | 9835 |
| 92 | [openai/plugins](https://github.com/openai/plugins) | +14 | 4020 |
| 93 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +14 | 42352 |
| 94 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +14 | 6161 |
| 95 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +14 | 8681 |
| 96 | [shadcn/improve](https://github.com/shadcn/improve) | +13 | 6843 |
| 97 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +13 | 3410 |
| 98 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +13 | 22478 |
| 99 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +13 | 44710 |
| 100 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +12 | 820 |
| 101 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +12 | 37831 |
| 102 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +12 | 456 |
| 103 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +12 | 3779 |
| 104 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +12 | 1586 |
| 105 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +11 | 452 |
| 106 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +11 | 24122 |
| 107 | [aquace/CVE-2026-41940-PoC](https://github.com/aquace/CVE-2026-41940-PoC) | +11 | 7 |
| 108 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 37307 |
| 109 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +11 | 1219 |
| 110 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +10 | 2076 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +10 | 20095 |
| 112 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +10 | 2705 |
| 113 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +10 | 9211 |
| 114 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +10 | 32466 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +10 | 31543 |
| 116 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +10 | 5445 |
| 117 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +9 | 27741 |
| 118 | [jundot/omlx](https://github.com/jundot/omlx) | +9 | 17490 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +9 | 17184 |
| 120 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +9 | 3022 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1643 | 73826 |
| 2 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1376 | 80688 |
| 3 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1370 | 56507 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +887 | 50551 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +868 | 48904 |
| 6 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +648 | 44593 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +625 | 57523 |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +585 | 33035 |
| 9 | [apple/container](https://github.com/apple/container) | +530 | 46410 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +508 | 26103 |
| 11 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +412 | 34804 |
| 12 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +405 | 9916 |
| 13 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +401 | 12535 |
| 14 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +372 | 11417 |
| 15 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +362 | 23323 |
| 16 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +353 | 54235 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +328 | 36617 |
| 18 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +314 | 11949 |
| 19 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +311 | 37307 |
| 20 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +304 | 22478 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +296 | 33101 |
| 22 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +292 | 36232 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +290 | 68482 |
| 24 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +287 | 9939 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +282 | 43469 |
| 26 | [roboflow/supervision](https://github.com/roboflow/supervision) | +277 | 36553 |
| 27 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +271 | 32466 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +269 | 25912 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +267 | 15082 |
| 30 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +259 | 24363 |
| 31 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +230 | 18308 |
| 32 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +229 | 5113 |
| 33 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +217 | 13258 |
| 34 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +211 | 37660 |
| 35 | [shadcn/improve](https://github.com/shadcn/improve) | +211 | 6843 |
| 36 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +205 | 10316 |
| 37 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +205 | 35751 |
| 38 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +204 | 25516 |
| 39 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +196 | 32872 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +194 | 16035 |
| 41 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +189 | 17771 |
| 42 | [stablyai/orca](https://github.com/stablyai/orca) | +187 | 11987 |
| 43 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +187 | 23072 |
| 44 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +184 | 11350 |
| 45 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +183 | 32789 |
| 46 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +182 | 26954 |
| 47 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +182 | 6933 |
| 48 | [usestrix/strix](https://github.com/usestrix/strix) | +181 | 35908 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +180 | 38566 |
| 50 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +177 | 10596 |
| 51 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +173 | 20847 |
| 52 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +172 | 6161 |
| 53 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +170 | 6222 |
| 54 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +169 | 7358 |
| 55 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +168 | 9643 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +163 | 30209 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +162 | 25005 |
| 58 | [EpicGames/lore](https://github.com/EpicGames/lore) | +161 | 7661 |
| 59 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +160 | 61965 |
| 60 | [blader/humanizer](https://github.com/blader/humanizer) | +158 | 27473 |
| 61 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +157 | 5867 |
| 62 | [google-research/timesfm](https://github.com/google-research/timesfm) | +157 | 26519 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +150 | 36090 |
| 64 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +143 | 17838 |
| 65 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +142 | 4586 |
| 66 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +139 | 39235 |
| 67 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +135 | 22370 |
| 68 | [google/skills](https://github.com/google/skills) | +135 | 14385 |
| 69 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +134 | 7805 |
| 70 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +131 | 7221 |
| 71 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +130 | 27741 |
| 72 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +129 | 26845 |
| 73 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +127 | 24551 |
| 74 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +124 | 12322 |
| 75 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +123 | 20087 |
| 76 | [openai/plugins](https://github.com/openai/plugins) | +121 | 4020 |
| 77 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +120 | 22613 |
| 78 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +118 | 24526 |
| 79 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +118 | 34153 |
| 80 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +116 | 31767 |
| 81 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +115 | 13071 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +114 | 39040 |
| 83 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +114 | 22336 |
| 84 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 59 |
| 85 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +113 | 5194 |
| 86 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +112 | 33014 |
| 87 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +111 | 24122 |
| 88 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +108 | 26298 |
| 89 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +107 | 23022 |
| 90 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +107 | 10234 |
| 91 | [facebook/astryx](https://github.com/facebook/astryx) | +106 | 5286 |
| 92 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +106 | 7838 |
| 93 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +106 | 49931 |
| 94 | [erincatto/box3d](https://github.com/erincatto/box3d) | +105 | 3327 |
| 95 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +105 | 5385 |
| 96 | [browser-use/video-use](https://github.com/browser-use/video-use) | +104 | 14655 |
| 97 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +104 | 8042 |
| 98 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +102 | 3645 |
| 99 | [decolua/9router](https://github.com/decolua/9router) | +101 | 19791 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +98 | 15456 |
| 101 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +96 | 30143 |
| 102 | [antirez/ds4](https://github.com/antirez/ds4) | +95 | 17544 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +95 | 44710 |
| 104 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +94 | 11266 |
| 105 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +92 | 2304 |
| 106 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +91 | 16476 |
| 107 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +88 | 5019 |
| 108 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 9133 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +87 | 48031 |
| 110 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +86 | 24225 |
| 111 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +84 | 42352 |
| 112 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +83 | 8681 |
| 113 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +83 | 36479 |
| 114 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +82 | 24968 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +81 | 31543 |
| 116 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +80 | 5550 |
| 117 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 4056 |
| 118 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +79 | 14556 |
| 119 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +79 | 5892 |
| 120 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +78 | 4680 |
| 121 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 5121 |
| 122 | [openai/skills](https://github.com/openai/skills) | +78 | 23235 |
| 123 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +75 | 10497 |
| 124 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +74 | 6162 |
| 125 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +73 | 20541 |
| 126 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +73 | 9211 |
| 127 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +72 | 17785 |
| 128 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +71 | 20095 |
| 129 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +70 | 5764 |
| 130 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +69 | 25794 |
| 131 | [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | +69 | 33682 |
| 132 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +66 | 24496 |
| 133 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +66 | 5445 |
| 134 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +66 | 1768 |
| 135 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +65 | 17979 |
| 136 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +64 | 3942 |
| 137 | [browser-act/skills](https://github.com/browser-act/skills) | +63 | 3629 |
| 138 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3410 |
| 139 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +62 | 1848 |
| 140 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +61 | 25680 |
| 141 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +61 | 2583 |
| 142 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +61 | 7571 |
| 143 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +61 | 26140 |
| 144 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +60 | 1586 |
| 145 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +60 | 4658 |
| 146 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +60 | 36103 |
| 147 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 148 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +58 | 17184 |
| 149 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +58 | 2929 |
| 150 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +57 | 4096 |
| 151 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +57 | 7869 |
| 152 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +57 | 3753 |
| 153 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +57 | 26008 |
| 154 | [jundot/omlx](https://github.com/jundot/omlx) | +56 | 17490 |
| 155 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +56 | 3084 |
| 156 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +56 | 3575 |
| 157 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +56 | 19408 |
| 158 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +54 | 3022 |
| 159 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +53 | 9719 |
| 160 | [anbeime/skill](https://github.com/anbeime/skill) | +53 | 3117 |
| 161 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +53 | 3555 |
| 162 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +53 | 11978 |
| 163 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +53 | 8850 |
| 164 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +52 | 3971 |
| 165 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +52 | 6367 |
| 166 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +51 | 7335 |
| 167 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +51 | 2399 |
| 168 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +49 | 2862 |
| 169 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +48 | 45008 |
| 170 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +47 | 26316 |
| 171 | [hexo-ai/sia](https://github.com/hexo-ai/sia) | +46 | 1956 |
| 172 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1189 |
| 173 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +44 | 19165 |
| 174 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +42 | 2890 |
| 175 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +42 | 15699 |
| 176 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +41 | 7850 |
| 177 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +41 | 3668 |
| 178 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +41 | 16785 |
| 179 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1368 |
| 180 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +40 | 8161 |
| 181 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +39 | 1261 |
| 182 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +37 | 2092 |
| 183 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +36 | 950 |
| 184 | [floci-io/floci](https://github.com/floci-io/floci) | +36 | 15046 |
| 185 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +35 | 7324 |
| 186 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +35 | 7419 |
| 187 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +35 | 5078 |
| 188 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +33 | 9480 |
| 189 | [google-research/tabfm](https://github.com/google-research/tabfm) | +31 | 1135 |
| 190 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +30 | 5481 |
| 191 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +28 | 1574 |
| 192 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1154 |
| 193 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +28 | 1557 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +28 | 28659 |
| 195 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +27 | 884 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +27 | 8615 |
| 197 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +27 | 5956 |
| 198 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +26 | 4249 |
| 199 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +25 | 1451 |
| 200 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +25 | 505 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +25 | 8062 |
| 202 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +24 | 1237 |
| 203 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +23 | 1377 |
| 204 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +22 | 428 |
| 205 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +22 | 11577 |
| 206 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 610 |
| 207 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +22 | 2077 |
| 208 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +21 | 2497 |
| 209 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +20 | 485 |
| 210 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 561 |
| 211 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +19 | 5650 |
| 212 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 635 |
| 213 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +18 | 662 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +18 | 2451 |
| 215 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 599 |
| 216 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +17 | 796 |
| 217 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +16 | 13951 |
| 218 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +16 | 4969 |
| 219 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +16 | 2994 |
| 220 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +15 | 5574 |
| 221 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +15 | 473 |
| 222 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +15 | 409 |
| 223 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +15 | 2746 |
| 224 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 486 |
| 225 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +14 | 1439 |
| 226 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 466 |
| 227 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +14 | 576 |
| 228 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +13 | 2616 |
| 229 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +13 | 2145 |
| 230 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +13 | 12282 |
| 231 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +13 | 1504 |
| 232 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +13 | 1014 |
| 233 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +13 | 1475 |
| 234 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +13 | 4702 |
| 235 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 450 |
| 236 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +12 | 456 |
| 237 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +12 | 182 |
| 238 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 326 |
| 239 | [robinebers/openusage](https://github.com/robinebers/openusage) | +12 | 3097 |
| 240 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +12 | 2294 |
| 241 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 659 |
| 242 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +11 | 696 |
| 243 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +11 | 889 |
| 244 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +11 | 3946 |
| 245 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3628 |
| 246 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +11 | 2677 |
| 247 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +11 | 0 |
| 248 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +11 | 856 |
| 249 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 200 |
| 250 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +10 | 1629 |
| 251 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +10 | 1144 |
| 252 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +10 | 1839 |
| 253 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +10 | 293 |
| 254 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 3757 |
| 255 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +10 | 2538 |
| 256 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +10 | 1115 |
| 257 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +9 | 298 |
| 258 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 259 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +9 | 838 |
| 260 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 216 |
| 261 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 392 |
| 262 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +8 | 392 |
| 263 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +8 | 464 |
| 264 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +8 | 315 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +8 | 2718 |
| 266 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +8 | 1754 |
| 267 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +8 | 28 |
| 268 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1275 |
| 269 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +7 | 2700 |
| 270 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 245 |
| 271 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +7 | 687 |
| 272 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 194 |
| 273 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 328 |
| 274 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 176 |
| 275 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +6 | 589 |
| 276 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +5 | 428 |
| 277 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 283 |
| 278 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2613 |
| 279 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 117 |
| 280 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 524 |
| 281 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +5 | 396 |
| 282 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +5 | 1667 |
| 283 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +4 | 68 |
| 284 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +4 | 218 |
| 285 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 93 |
| 286 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 561 |
| 287 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +4 | 572 |
| 288 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +3 | 440 |
| 289 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +3 | 194 |
| 290 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 215 |
| 291 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 801 |
| 293 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 427 |
| 294 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +3 | 251 |
| 295 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 296 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +3 | 978 |
| 297 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +3 | 5197 |
| 298 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 283 |
| 299 | [oneQAQone/QFun](https://github.com/oneQAQone/QFun) | +3 | 180 |
| 300 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 8603 |
