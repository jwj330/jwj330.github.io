---
title: "2026-07-05 GitHub增长趋势报告"
description: "1.openwiki+71 2.codex-plugin-cc+55 3.meetily+53 4.system_prompts_leaks+49 5.strix+45"
date: 2026-07-05T21:02:27+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-05 21:02:27

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
        'daily': {"categories": ["erincatto/box3d", "bradautomates/claude-video", "Emily2040/seedance-2.0", "cloudflare/kumo", "ChromeDevTools/chrome-devtools-mcp", "facebook/astryx", "MadsLorentzen/ai-job-search", "ZhuLinsen/daily_stock_analysis", "ogulcancelik/herdr", "DeusData/codebase-memory-mcp", "Usagi-org/ai-goofish-monitor", "calesthio/OpenMontage", "alibaba/page-agent", "teamchong/pxpipe", "elder-plinius/T3MP3ST", "usestrix/strix", "asgeirtj/system_prompts_leaks", "Zackriya-Solutions/meetily", "openai/codex-plugin-cc", "langchain-ai/openwiki"], "data": [13, 13, 14, 16, 17, 19, 21, 21, 22, 24, 27, 28, 30, 32, 35, 45, 49, 53, 55, 71]},
        'weekly': {"categories": ["xbtlin/ai-berkshire", "browser-use/video-use", "jamiepine/voicebox", "teamchong/pxpipe", "diegosouzapw/OmniRoute", "stablyai/orca", "HKUDS/Vibe-Trading", "ZhuLinsen/daily_stock_analysis", "alibaba/page-agent", "ogulcancelik/herdr", "Zackriya-Solutions/meetily", "asgeirtj/system_prompts_leaks", "hasaneyldrm/exercises-dataset", "DeusData/codebase-memory-mcp", "openai/codex-plugin-cc", "calesthio/OpenMontage", "facebook/astryx", "erincatto/box3d", "langchain-ai/openwiki", "usestrix/strix"], "data": [46, 55, 55, 56, 57, 63, 65, 66, 77, 79, 81, 82, 87, 97, 98, 104, 106, 119, 129, 201]},
        'monthly': {"categories": ["palmier-io/palmier-pro", "rohitg00/ai-engineering-from-scratch", "phuryn/pm-skills", "NVIDIA/SkillSpector", "BigPizzaV3/CodexPlusPlus", "hugohe3/ppt-master", "alibaba/open-code-review", "ZhuLinsen/daily_stock_analysis", "lfnovo/open-notebook", "XiaomiMiMo/MiMo-Code", "RyanCodrai/turbovec", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "pewdiepie-archdaemon/odysseus", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [290, 300, 307, 317, 328, 328, 361, 361, 368, 374, 398, 530, 544, 611, 655, 833, 916, 1127, 1276, 1681]}
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
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +71 | 4933 |
| 2 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +55 | 25361 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +53 | 16703 |
| 4 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +49 | 32872 |
| 5 | [usestrix/strix](https://github.com/usestrix/strix) | +45 | 36976 |
| 6 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +35 | 1465 |
| 7 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +32 | 2828 |
| 8 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +30 | 23763 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +28 | 33597 |
| 10 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +27 | 13189 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +24 | 26660 |
| 12 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +22 | 11979 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +21 | 54669 |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +21 | 5433 |
| 15 | [facebook/astryx](https://github.com/facebook/astryx) | +19 | 5824 |
| 16 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +17 | 45946 |
| 17 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +16 | 2765 |
| 18 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +14 | 2461 |
| 19 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +13 | 3493 |
| 20 | [erincatto/box3d](https://github.com/erincatto/box3d) | +13 | 3669 |
| 21 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +13 | 279 |
| 22 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +12 | 9877 |
| 23 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +12 | 8224 |
| 24 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +12 | 649 |
| 25 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +11 | 25807 |
| 26 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +11 | 11779 |
| 27 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +11 | 37965 |
| 28 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +11 | 1952 |
| 29 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +11 | 6191 |
| 30 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +10 | 20483 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +201 | 36976 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +129 | 4933 |
| 3 | [erincatto/box3d](https://github.com/erincatto/box3d) | +119 | 3669 |
| 4 | [facebook/astryx](https://github.com/facebook/astryx) | +106 | 5824 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +104 | 33597 |
| 6 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +98 | 25361 |
| 7 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +97 | 26660 |
| 8 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +87 | 9996 |
| 9 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +82 | 32872 |
| 10 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +81 | 16703 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +79 | 11979 |
| 12 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +77 | 23764 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +66 | 54669 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +65 | 17940 |
| 15 | [stablyai/orca](https://github.com/stablyai/orca) | +63 | 12326 |
| 16 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +57 | 11779 |
| 17 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +56 | 2828 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +55 | 37965 |
| 19 | [browser-use/video-use](https://github.com/browser-use/video-use) | +55 | 14996 |
| 20 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +46 | 10250 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +46 | 36824 |
| 22 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +46 | 26802 |
| 23 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +45 | 25807 |
| 24 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +42 | 5433 |
| 25 | [apple/container](https://github.com/apple/container) | +42 | 46611 |
| 26 | [rommapp/romm](https://github.com/rommapp/romm) | +42 | 10485 |
| 27 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +40 | 3605 |
| 28 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +39 | 7524 |
| 29 | [google-research/tabfm](https://github.com/google-research/tabfm) | +38 | 1258 |
| 30 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +37 | 45946 |
| 31 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +37 | 6191 |
| 32 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +36 | 3058 |
| 33 | [baairon/torlink](https://github.com/baairon/torlink) | +36 | 3065 |
| 34 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +35 | 1465 |
| 35 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +31 | 68671 |
| 36 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 26151 |
| 37 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +31 | 2688 |
| 38 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +30 | 24601 |
| 39 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +29 | 9877 |
| 40 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +28 | 13189 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +25 | 38721 |
| 42 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +25 | 15182 |
| 43 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +24 | 7324 |
| 44 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +24 | 49124 |
| 45 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +23 | 2461 |
| 46 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +23 | 649 |
| 47 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +23 | 23462 |
| 48 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +23 | 33271 |
| 49 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +23 | 14947 |
| 50 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +22 | 16178 |
| 51 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +22 | 36378 |
| 52 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2765 |
| 53 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +21 | 4811 |
| 54 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +21 | 7893 |
| 55 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +21 | 1719 |
| 56 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +20 | 13348 |
| 57 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +20 | 43680 |
| 58 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +20 | 25116 |
| 59 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +20 | 6234 |
| 60 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +20 | 3681 |
| 61 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +19 | 8224 |
| 62 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +19 | 3493 |
| 63 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +19 | 661 |
| 64 | [modiqo/skillspec](https://github.com/modiqo/skillspec) | +19 | 857 |
| 65 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +19 | 5287 |
| 66 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +19 | 3298 |
| 67 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +19 | 12004 |
| 68 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +18 | 20483 |
| 69 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +18 | 16655 |
| 70 | [modiqo/cliare](https://github.com/modiqo/cliare) | +18 | 693 |
| 71 | [decolua/9router](https://github.com/decolua/9router) | +17 | 19983 |
| 72 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +17 | 1952 |
| 73 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +17 | 871 |
| 74 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 6308 |
| 75 | [HduSy/tokenscope](https://github.com/HduSy/tokenscope) | +17 | 210 |
| 76 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +17 | 5391 |
| 77 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +16 | 25082 |
| 78 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +16 | 1875 |
| 79 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +15 | 30321 |
| 80 | [floci-io/floci](https://github.com/floci-io/floci) | +15 | 15310 |
| 81 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +15 | 36368 |
| 82 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +15 | 24662 |
| 83 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +15 | 20915 |
| 84 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +15 | 4141 |
| 85 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +14 | 883 |
| 86 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 279 |
| 87 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +14 | 6237 |
| 88 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +14 | 22608 |
| 89 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +14 | 9867 |
| 90 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +14 | 30229 |
| 91 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 3100 |
| 92 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +13 | 1240 |
| 93 | [multica-ai/multica](https://github.com/multica-ai/multica) | +13 | 39115 |
| 94 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +13 | 37881 |
| 95 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +13 | 4156 |
| 96 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +13 | 2765 |
| 97 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 24615 |
| 98 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 37390 |
| 99 | [dorianborian/sesame-robot](https://github.com/dorianborian/sesame-robot) | +12 | 3321 |
| 100 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +12 | 10757 |
| 101 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +11 | 5306 |
| 102 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +11 | 26927 |
| 103 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 608 |
| 104 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +11 | 39280 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 44771 |
| 106 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +11 | 24162 |
| 107 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +10 | 2889 |
| 108 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 389 |
| 109 | [InternScience/Agents-A1](https://github.com/InternScience/Agents-A1) | +10 | 328 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +10 | 17222 |
| 111 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +10 | 42389 |
| 112 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +10 | 5514 |
| 113 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +10 | 10301 |
| 114 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +9 | 9254 |
| 115 | [jundot/omlx](https://github.com/jundot/omlx) | +9 | 17534 |
| 116 | [Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases) | +9 | 300 |
| 117 | [browser-act/skills](https://github.com/browser-act/skills) | +8 | 3720 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +8 | 31594 |
| 119 | [openai/skills](https://github.com/openai/skills) | +8 | 23275 |
| 120 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +8 | 3081 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1681 | 74718 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1276 | 56781 |
| 3 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +1127 | 80908 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +916 | 51214 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +833 | 49124 |
| 6 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +655 | 44711 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +611 | 33597 |
| 8 | [apple/container](https://github.com/apple/container) | +544 | 46611 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +530 | 26660 |
| 10 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +398 | 12558 |
| 11 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +374 | 11466 |
| 12 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +368 | 34942 |
| 13 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +361 | 54669 |
| 14 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +361 | 9946 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +328 | 36824 |
| 16 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +328 | 23462 |
| 17 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +317 | 12004 |
| 18 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +307 | 22608 |
| 19 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +300 | 37390 |
| 20 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +290 | 9998 |
| 21 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +281 | 36378 |
| 22 | [roboflow/supervision](https://github.com/roboflow/supervision) | +280 | 36553 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +279 | 68671 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +276 | 33272 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +275 | 43680 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +261 | 26151 |
| 27 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +259 | 32528 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +257 | 15182 |
| 29 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +252 | 24601 |
| 30 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +242 | 32872 |
| 31 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +231 | 5127 |
| 32 | [usestrix/strix](https://github.com/usestrix/strix) | +224 | 36976 |
| 33 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +224 | 18335 |
| 34 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +219 | 13348 |
| 35 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +218 | 37965 |
| 36 | [shadcn/improve](https://github.com/shadcn/improve) | +212 | 6935 |
| 37 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +209 | 25807 |
| 38 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +196 | 11979 |
| 39 | [stablyai/orca](https://github.com/stablyai/orca) | +195 | 12326 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +188 | 16178 |
| 41 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +186 | 17940 |
| 42 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +186 | 27099 |
| 43 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +179 | 23140 |
| 44 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +177 | 10250 |
| 45 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +177 | 6237 |
| 46 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +176 | 6308 |
| 47 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +176 | 32874 |
| 48 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +174 | 7524 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +174 | 38721 |
| 50 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +174 | 7008 |
| 51 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +170 | 20915 |
| 52 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +167 | 10757 |
| 53 | [EpicGames/lore](https://github.com/EpicGames/lore) | +163 | 7690 |
| 54 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +162 | 25082 |
| 55 | [google-research/timesfm](https://github.com/google-research/timesfm) | +162 | 26563 |
| 56 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +159 | 62031 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +158 | 30321 |
| 58 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +157 | 5903 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +157 | 27604 |
| 60 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +148 | 36368 |
| 61 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 17911 |
| 62 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +141 | 39280 |
| 63 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +137 | 22493 |
| 64 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +136 | 25361 |
| 65 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +135 | 5433 |
| 66 | [google/skills](https://github.com/google/skills) | +135 | 14399 |
| 67 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +134 | 23764 |
| 68 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +134 | 7893 |
| 69 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +129 | 4933 |
| 70 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +129 | 7358 |
| 71 | [facebook/astryx](https://github.com/facebook/astryx) | +125 | 5824 |
| 72 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +125 | 27792 |
| 73 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +125 | 24588 |
| 74 | [openai/plugins](https://github.com/openai/plugins) | +121 | 4068 |
| 75 | [erincatto/box3d](https://github.com/erincatto/box3d) | +119 | 3669 |
| 76 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +118 | 24615 |
| 77 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +118 | 26927 |
| 78 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +116 | 25612 |
| 79 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +115 | 20195 |
| 80 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +114 | 5287 |
| 81 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +114 | 34193 |
| 82 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 52 |
| 83 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +113 | 31809 |
| 84 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +112 | 22363 |
| 85 | [browser-use/video-use](https://github.com/browser-use/video-use) | +109 | 14996 |
| 86 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +109 | 24162 |
| 87 | [multica-ai/multica](https://github.com/multica-ai/multica) | +108 | 39115 |
| 88 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +108 | 33074 |
| 89 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +107 | 26316 |
| 90 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +104 | 3681 |
| 91 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +104 | 11779 |
| 92 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +104 | 10301 |
| 93 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +100 | 8072 |
| 94 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +97 | 9996 |
| 95 | [decolua/9router](https://github.com/decolua/9router) | +97 | 19983 |
| 96 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +97 | 7876 |
| 97 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +96 | 45946 |
| 98 | [antirez/ds4](https://github.com/antirez/ds4) | +96 | 17632 |
| 99 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +94 | 16703 |
| 100 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +93 | 2383 |
| 101 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +92 | 44771 |
| 102 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +91 | 30229 |
| 103 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +91 | 5391 |
| 104 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +89 | 9200 |
| 105 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +89 | 49945 |
| 106 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +89 | 25387 |
| 107 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +88 | 15513 |
| 108 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +87 | 16511 |
| 109 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +86 | 5306 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +85 | 48294 |
| 111 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +83 | 42389 |
| 112 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +82 | 4811 |
| 113 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +82 | 5577 |
| 114 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +82 | 36546 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +81 | 31594 |
| 116 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6234 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +80 | 8789 |
| 118 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 4095 |
| 119 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +78 | 20483 |
| 120 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +78 | 14590 |
| 121 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +76 | 3605 |
| 122 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +76 | 5072 |
| 123 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +76 | 5939 |
| 124 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +75 | 20571 |
| 125 | [openai/skills](https://github.com/openai/skills) | +73 | 23275 |
| 126 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +71 | 9254 |
| 127 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +70 | 10554 |
| 128 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +68 | 17819 |
| 129 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +67 | 2688 |
| 130 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +66 | 24662 |
| 131 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +65 | 9877 |
| 132 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +65 | 25813 |
| 133 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +64 | 5844 |
| 134 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +63 | 1875 |
| 135 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3449 |
| 136 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +62 | 5514 |
| 137 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +62 | 1773 |
| 138 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +62 | 3058 |
| 139 | [browser-act/skills](https://github.com/browser-act/skills) | +61 | 3720 |
| 140 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +60 | 7912 |
| 141 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +60 | 7607 |
| 142 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +60 | 36103 |
| 143 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +59 | 18006 |
| 144 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +59 | 3964 |
| 145 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 146 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +59 | 26061 |
| 147 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +59 | 19459 |
| 148 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +58 | 4141 |
| 149 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +58 | 26802 |
| 150 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +57 | 17222 |
| 151 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +57 | 2453 |
| 152 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +57 | 26157 |
| 153 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +56 | 3615 |
| 154 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +56 | 4667 |
| 155 | [jundot/omlx](https://github.com/jundot/omlx) | +55 | 17534 |
| 156 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +55 | 25720 |
| 157 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +55 | 3103 |
| 158 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +54 | 11994 |
| 159 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +53 | 1594 |
| 160 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +53 | 3081 |
| 161 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +52 | 4020 |
| 162 | [anbeime/skill](https://github.com/anbeime/skill) | +52 | 3151 |
| 163 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +51 | 3567 |
| 164 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +51 | 6398 |
| 165 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +50 | 8851 |
| 166 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +49 | 7359 |
| 167 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +49 | 2880 |
| 168 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +46 | 45034 |
| 169 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +46 | 26333 |
| 170 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1191 |
| 171 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +44 | 3493 |
| 172 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +44 | 19200 |
| 173 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 2943 |
| 174 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +42 | 2461 |
| 175 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +42 | 15733 |
| 176 | [floci-io/floci](https://github.com/floci-io/floci) | +42 | 15310 |
| 177 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +41 | 13189 |
| 178 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1383 |
| 179 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +40 | 3714 |
| 180 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +39 | 1270 |
| 181 | [beltromatti/get-it](https://github.com/beltromatti/get-it) | +39 | 865 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +39 | 16872 |
| 183 | [google-research/tabfm](https://github.com/google-research/tabfm) | +37 | 1258 |
| 184 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +37 | 8178 |
| 185 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +36 | 2113 |
| 186 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +35 | 1719 |
| 187 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +35 | 7442 |
| 188 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +32 | 7343 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +32 | 5101 |
| 190 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +31 | 1610 |
| 191 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1167 |
| 192 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 520 |
| 193 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +28 | 28705 |
| 194 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 887 |
| 195 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +28 | 5490 |
| 196 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +27 | 955 |
| 197 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +26 | 9481 |
| 198 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +25 | 8635 |
| 199 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +25 | 5964 |
| 200 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +24 | 1240 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +24 | 8080 |
| 202 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 429 |
| 203 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +23 | 11600 |
| 204 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +23 | 1381 |
| 205 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +23 | 4258 |
| 206 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 613 |
| 207 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +20 | 495 |
| 208 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +20 | 2508 |
| 209 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +20 | 2102 |
| 210 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +19 | 672 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +19 | 4190 |
| 212 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +19 | 5675 |
| 213 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 639 |
| 214 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 605 |
| 215 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +16 | 4976 |
| 216 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2631 |
| 217 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +15 | 13956 |
| 218 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +15 | 475 |
| 219 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +15 | 428 |
| 220 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +15 | 2454 |
| 221 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +15 | 803 |
| 222 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 491 |
| 223 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +14 | 5585 |
| 224 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +14 | 1455 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +14 | 2163 |
| 226 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 468 |
| 227 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +14 | 3002 |
| 228 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +14 | 2754 |
| 229 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +13 | 536 |
| 230 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 188 |
| 231 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +13 | 1858 |
| 232 | [robinebers/openusage](https://github.com/robinebers/openusage) | +13 | 3107 |
| 233 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +13 | 594 |
| 234 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +13 | 12287 |
| 235 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +13 | 1515 |
| 236 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +13 | 1015 |
| 237 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 454 |
| 238 | [AI-Builder-Club/skills](https://github.com/AI-Builder-Club/skills) | +12 | 771 |
| 239 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +12 | 703 |
| 240 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 326 |
| 241 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +12 | 4712 |
| 242 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +12 | 1477 |
| 243 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +12 | 324 |
| 244 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 661 |
| 245 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +11 | 894 |
| 246 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +11 | 2693 |
| 247 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3635 |
| 248 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 311 |
| 249 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 200 |
| 250 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +10 | 1638 |
| 251 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +10 | 1149 |
| 252 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 266 |
| 253 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 3762 |
| 254 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +10 | 2299 |
| 255 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +9 | 391 |
| 256 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +9 | 417 |
| 257 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +9 | 331 |
| 258 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 259 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +9 | 2540 |
| 260 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 215 |
| 261 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +9 | 1115 |
| 262 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 529 |
| 263 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +8 | 482 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +8 | 1761 |
| 265 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +8 | 29 |
| 266 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +8 | 0 |
| 267 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1280 |
| 268 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +7 | 286 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +7 | 2617 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2728 |
| 271 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +7 | 688 |
| 272 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 193 |
| 273 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +7 | 856 |
| 274 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 435 |
| 275 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 339 |
| 276 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 178 |
| 277 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 70 |
| 278 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 290 |
| 279 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +5 | 570 |
| 280 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 117 |
| 281 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 529 |
| 282 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +5 | 1674 |
| 283 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +4 | 195 |
| 284 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +4 | 804 |
| 285 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 93 |
| 286 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +4 | 573 |
| 287 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +4 | 590 |
| 288 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 220 |
| 289 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +3 | 452 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +3 | 607 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 215 |
| 292 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 396 |
| 293 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 294 | [Angais/minedit](https://github.com/Angais/minedit) | +3 | 122 |
| 295 | [egdels/makeacopy](https://github.com/egdels/makeacopy) | +3 | 430 |
| 296 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +3 | 253 |
| 297 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 298 | [apache/phoenix-adapters](https://github.com/apache/phoenix-adapters) | +3 | 118 |
| 299 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 285 |
| 300 | [oneQAQone/QFun](https://github.com/oneQAQone/QFun) | +3 | 180 |
