---
title: "2026-07-06 GitHub增长趋势报告"
description: "1.openwiki+22 2.pxpipe+14 3.claude-design-system-prompt+14 4.OmniRoute+11 5.astryx+9"
date: 2026-07-06T21:38:30+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-06 21:38:30

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
        'daily': {"categories": ["mauriceboe/TREK", "OthmanAdi/planning-with-files", "alibaba/zvec", "microsoft/SkillOpt", "Imbad0202/academic-research-skills", "alirezarezvani/claude-skills", "elder-plinius/T3MP3ST", "steipete/CodexBar", "DeusData/codebase-memory-mcp", "coreyhaines31/marketingskills", "usestrix/strix", "calesthio/OpenMontage", "MadsLorentzen/ai-job-search", "alibaba/page-agent", "openai/codex-plugin-cc", "facebook/astryx", "diegosouzapw/OmniRoute", "Trystan-SA/claude-design-system-prompt", "teamchong/pxpipe", "langchain-ai/openwiki"], "data": [4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 11, 14, 14, 22]},
        'weekly': {"categories": ["harvard-edge/cs249r_book", "xbtlin/ai-berkshire", "jamiepine/voicebox", "browser-use/video-use", "ZhuLinsen/daily_stock_analysis", "stablyai/orca", "HKUDS/Vibe-Trading", "diegosouzapw/OmniRoute", "teamchong/pxpipe", "hasaneyldrm/exercises-dataset", "ogulcancelik/herdr", "alibaba/page-agent", "DeusData/codebase-memory-mcp", "Zackriya-Solutions/meetily", "calesthio/OpenMontage", "openai/codex-plugin-cc", "facebook/astryx", "erincatto/box3d", "langchain-ai/openwiki", "usestrix/strix"], "data": [50, 54, 55, 56, 61, 65, 67, 67, 69, 77, 80, 84, 94, 95, 102, 107, 114, 122, 151, 206]},
        'monthly': {"categories": ["roboflow/supervision", "phuryn/pm-skills", "palmier-io/palmier-pro", "BigPizzaV3/CodexPlusPlus", "lfnovo/open-notebook", "hugohe3/ppt-master", "alibaba/open-code-review", "NVIDIA/SkillSpector", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "RyanCodrai/turbovec", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "pewdiepie-archdaemon/odysseus", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [278, 288, 290, 294, 313, 316, 317, 317, 353, 375, 379, 535, 542, 614, 657, 807, 872, 903, 1212, 1690]}
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
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +22 | 7367 |
| 2 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +14 | 4033 |
| 3 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +14 | 1254 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +11 | 12518 |
| 5 | [facebook/astryx](https://github.com/facebook/astryx) | +9 | 6391 |
| 6 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +9 | 26228 |
| 7 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +8 | 24574 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +7 | 6915 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +7 | 34270 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | +7 | 37935 |
| 11 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 36827 |
| 12 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +6 | 27316 |
| 13 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +6 | 16698 |
| 14 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +5 | 2564 |
| 15 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +5 | 21101 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 36571 |
| 17 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +4 | 11127 |
| 18 | [alibaba/zvec](https://github.com/alibaba/zvec) | +4 | 13441 |
| 19 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +4 | 24915 |
| 20 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +4 | 9417 |
| 21 | [floci-io/floci](https://github.com/floci-io/floci) | +4 | 15492 |
| 22 | [Augani/dory](https://github.com/Augani/dory) | +4 | 819 |
| 23 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 15418 |
| 24 | [dungngminh/simutil](https://github.com/dungngminh/simutil) | +3 | 799 |
| 25 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +3 | 10055 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3 | 43924 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 13489 |
| 28 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 12792 |
| 29 | [happier-dev/happier](https://github.com/happier-dev/happier) | +3 | 1254 |
| 30 | [baairon/torlink](https://github.com/baairon/torlink) | +3 | 3180 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +206 | 37935 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +151 | 7367 |
| 3 | [erincatto/box3d](https://github.com/erincatto/box3d) | +122 | 4180 |
| 4 | [facebook/astryx](https://github.com/facebook/astryx) | +114 | 6391 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +107 | 26228 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +102 | 34270 |
| 7 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +95 | 19189 |
| 8 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +94 | 27316 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +84 | 24574 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +80 | 12793 |
| 11 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +77 | 10172 |
| 12 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +69 | 4033 |
| 13 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +67 | 12518 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +67 | 18170 |
| 15 | [stablyai/orca](https://github.com/stablyai/orca) | +65 | 12826 |
| 16 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +61 | 55101 |
| 17 | [browser-use/video-use](https://github.com/browser-use/video-use) | +56 | 15418 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +55 | 38256 |
| 19 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +54 | 11098 |
| 20 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +50 | 27053 |
| 21 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +49 | 6915 |
| 22 | [rommapp/romm](https://github.com/rommapp/romm) | +45 | 10752 |
| 23 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +44 | 3908 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +43 | 37143 |
| 25 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +41 | 26201 |
| 26 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +40 | 2564 |
| 27 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +40 | 3754 |
| 28 | [baairon/torlink](https://github.com/baairon/torlink) | +39 | 3180 |
| 29 | [google-research/tabfm](https://github.com/google-research/tabfm) | +38 | 1394 |
| 30 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +37 | 46072 |
| 31 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +36 | 3140 |
| 32 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +35 | 6369 |
| 33 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +33 | 26521 |
| 34 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +32 | 24767 |
| 35 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +31 | 13331 |
| 36 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +31 | 10055 |
| 37 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +31 | 2811 |
| 38 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +31 | 7667 |
| 39 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +27 | 5178 |
| 40 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +26 | 4138 |
| 41 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +26 | 36571 |
| 42 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +26 | 15299 |
| 43 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +25 | 2964 |
| 44 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +25 | 49678 |
| 45 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +25 | 23625 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 38904 |
| 47 | [Augani/dory](https://github.com/Augani/dory) | +24 | 819 |
| 48 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +24 | 7814 |
| 49 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 21101 |
| 50 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +23 | 757 |
| 51 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +23 | 14972 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +22 | 43924 |
| 53 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +22 | 13489 |
| 54 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +22 | 4948 |
| 55 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +22 | 16374 |
| 56 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +22 | 33476 |
| 57 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +22 | 1806 |
| 58 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +22 | 7977 |
| 59 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +21 | 8321 |
| 60 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2782 |
| 61 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +21 | 36827 |
| 62 | [decolua/9router](https://github.com/decolua/9router) | +20 | 20305 |
| 63 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +20 | 2059 |
| 64 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +20 | 25234 |
| 65 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +19 | 702 |
| 66 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +19 | 24915 |
| 67 | [modiqo/skillspec](https://github.com/modiqo/skillspec) | +19 | 885 |
| 68 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +19 | 5396 |
| 69 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +19 | 3377 |
| 70 | [floci-io/floci](https://github.com/floci-io/floci) | +18 | 15492 |
| 71 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +18 | 16733 |
| 72 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +18 | 945 |
| 73 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +18 | 12129 |
| 74 | [modiqo/cliare](https://github.com/modiqo/cliare) | +18 | 707 |
| 75 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +17 | 30499 |
| 76 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +17 | 25205 |
| 77 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 6420 |
| 78 | [HduSy/tokenscope](https://github.com/HduSy/tokenscope) | +17 | 216 |
| 79 | [multica-ai/multica](https://github.com/multica-ai/multica) | +16 | 39258 |
| 80 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 222 |
| 81 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +16 | 9417 |
| 82 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +16 | 3737 |
| 83 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +16 | 20977 |
| 84 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +16 | 5418 |
| 85 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +15 | 16698 |
| 86 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +15 | 1254 |
| 87 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +15 | 11127 |
| 88 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +15 | 6317 |
| 89 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +15 | 9908 |
| 90 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +15 | 4191 |
| 91 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +14 | 1316 |
| 92 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +14 | 917 |
| 93 | [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | +14 | 653 |
| 94 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 310 |
| 95 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +14 | 22757 |
| 96 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +14 | 18380 |
| 97 | [shadcn/improve](https://github.com/shadcn/improve) | +14 | 7038 |
| 98 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +14 | 30320 |
| 99 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +14 | 1921 |
| 100 | [dotnet/skills](https://github.com/dotnet/skills) | +13 | 4174 |
| 101 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 3200 |
| 102 | [dorianborian/sesame-robot](https://github.com/dorianborian/sesame-robot) | +13 | 3360 |
| 103 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +13 | 2831 |
| 104 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +12 | 5387 |
| 105 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 37504 |
| 106 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +11 | 27035 |
| 107 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 44859 |
| 108 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 611 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +11 | 17266 |
| 110 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +11 | 5594 |
| 111 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +11 | 24228 |
| 112 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +11 | 10392 |
| 113 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +10 | 2924 |
| 114 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 413 |
| 115 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +10 | 504 |
| 116 | [InternScience/Agents-A1](https://github.com/InternScience/Agents-A1) | +10 | 379 |
| 117 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +10 | 16576 |
| 118 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +10 | 42473 |
| 119 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +9 | 39334 |
| 120 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +9 | 9299 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1690 | 75865 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1212 | 57126 |
| 3 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +903 | 81161 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +872 | 51982 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +807 | 49678 |
| 6 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +657 | 44853 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +614 | 34270 |
| 8 | [apple/container](https://github.com/apple/container) | +542 | 46789 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +535 | 27316 |
| 10 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +379 | 12576 |
| 11 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +375 | 11530 |
| 12 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +353 | 55101 |
| 13 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +317 | 12129 |
| 14 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +317 | 10014 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +316 | 37143 |
| 16 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +313 | 35047 |
| 17 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +294 | 23625 |
| 18 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +290 | 10041 |
| 19 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +288 | 22757 |
| 20 | [roboflow/supervision](https://github.com/roboflow/supervision) | +278 | 36553 |
| 21 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +263 | 36571 |
| 22 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +262 | 37504 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +261 | 33476 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +254 | 43924 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +245 | 15299 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +239 | 26521 |
| 27 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +238 | 24767 |
| 28 | [usestrix/strix](https://github.com/usestrix/strix) | +229 | 37935 |
| 29 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +228 | 5150 |
| 30 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +222 | 13489 |
| 31 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +215 | 38256 |
| 32 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +214 | 18380 |
| 33 | [shadcn/improve](https://github.com/shadcn/improve) | +213 | 7039 |
| 34 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +203 | 26201 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +198 | 32631 |
| 36 | [stablyai/orca](https://github.com/stablyai/orca) | +192 | 12826 |
| 37 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +186 | 11098 |
| 38 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +185 | 12793 |
| 39 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 27250 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +183 | 16374 |
| 41 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +177 | 6420 |
| 42 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +177 | 6351 |
| 43 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +175 | 7667 |
| 44 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +175 | 18170 |
| 45 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +168 | 38904 |
| 46 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +164 | 11127 |
| 47 | [EpicGames/lore](https://github.com/EpicGames/lore) | +163 | 7722 |
| 48 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +162 | 20977 |
| 49 | [google-research/timesfm](https://github.com/google-research/timesfm) | +160 | 26610 |
| 50 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +157 | 32963 |
| 51 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +156 | 5938 |
| 52 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +156 | 23214 |
| 53 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +151 | 7367 |
| 54 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +148 | 36827 |
| 55 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +147 | 62106 |
| 56 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +147 | 25205 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +147 | 27749 |
| 58 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +145 | 18001 |
| 59 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +144 | 26228 |
| 60 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +142 | 24574 |
| 61 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +141 | 7123 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +139 | 30499 |
| 63 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +139 | 39334 |
| 64 | [facebook/astryx](https://github.com/facebook/astryx) | +133 | 6391 |
| 65 | [google/skills](https://github.com/google/skills) | +133 | 14418 |
| 66 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +131 | 22586 |
| 67 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +129 | 7531 |
| 68 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +126 | 7977 |
| 69 | [erincatto/box3d](https://github.com/erincatto/box3d) | +122 | 4180 |
| 70 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +116 | 27035 |
| 71 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +115 | 25681 |
| 72 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +114 | 6915 |
| 73 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +114 | 5396 |
| 74 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +114 | 24690 |
| 75 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 52 |
| 76 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +112 | 24718 |
| 77 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +110 | 34285 |
| 78 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +108 | 12518 |
| 79 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +107 | 19189 |
| 80 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +107 | 27838 |
| 81 | [openai/plugins](https://github.com/openai/plugins) | +107 | 4100 |
| 82 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +106 | 22407 |
| 83 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +106 | 20339 |
| 84 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +105 | 3737 |
| 85 | [browser-use/video-use](https://github.com/browser-use/video-use) | +105 | 15418 |
| 86 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +105 | 31858 |
| 87 | [multica-ai/multica](https://github.com/multica-ai/multica) | +102 | 39258 |
| 88 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +101 | 24228 |
| 89 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +99 | 10392 |
| 90 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +98 | 10172 |
| 91 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +97 | 8103 |
| 92 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +97 | 26344 |
| 93 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +93 | 9417 |
| 94 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +93 | 2439 |
| 95 | [decolua/9router](https://github.com/decolua/9router) | +92 | 20305 |
| 96 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +92 | 46072 |
| 97 | [antirez/ds4](https://github.com/antirez/ds4) | +91 | 17736 |
| 98 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +90 | 33168 |
| 99 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +88 | 7902 |
| 100 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +88 | 30320 |
| 101 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +87 | 44859 |
| 102 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +86 | 5387 |
| 103 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +83 | 4948 |
| 104 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +83 | 16576 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +81 | 42473 |
| 106 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6317 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +80 | 21101 |
| 108 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +80 | 5418 |
| 109 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +80 | 5598 |
| 110 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +79 | 3754 |
| 111 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +79 | 48715 |
| 112 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +79 | 25851 |
| 113 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +78 | 15578 |
| 114 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +78 | 4222 |
| 115 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +78 | 36639 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +75 | 8884 |
| 117 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +74 | 20934 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +72 | 31670 |
| 119 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +72 | 6024 |
| 120 | [openai/skills](https://github.com/openai/skills) | +71 | 23312 |
| 121 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +71 | 49958 |
| 122 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +70 | 4033 |
| 123 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +69 | 9299 |
| 124 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +69 | 5129 |
| 125 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +68 | 10055 |
| 126 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +67 | 14640 |
| 127 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +67 | 2811 |
| 128 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +65 | 24915 |
| 129 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +64 | 3140 |
| 130 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +63 | 25848 |
| 131 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3487 |
| 132 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +60 | 27053 |
| 133 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +60 | 36103 |
| 134 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +59 | 10644 |
| 135 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 136 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2498 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +57 | 17266 |
| 138 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +57 | 5594 |
| 139 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +57 | 26151 |
| 140 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +56 | 4191 |
| 141 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +56 | 7708 |
| 142 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +56 | 5897 |
| 143 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +55 | 3659 |
| 144 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +55 | 12023 |
| 145 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +54 | 1921 |
| 146 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +54 | 19522 |
| 147 | [anbeime/skill](https://github.com/anbeime/skill) | +53 | 3213 |
| 148 | [browser-act/skills](https://github.com/browser-act/skills) | +53 | 3816 |
| 149 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +53 | 3150 |
| 150 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +53 | 26193 |
| 151 | [jundot/omlx](https://github.com/jundot/omlx) | +52 | 17569 |
| 152 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +52 | 18050 |
| 153 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +52 | 3139 |
| 154 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +52 | 1779 |
| 155 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +51 | 3908 |
| 156 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +51 | 25808 |
| 157 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +51 | 3987 |
| 158 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +51 | 17856 |
| 159 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +49 | 7967 |
| 160 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +49 | 3589 |
| 161 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +47 | 4138 |
| 162 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +47 | 6457 |
| 163 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +46 | 4068 |
| 164 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +45 | 2893 |
| 165 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +45 | 1195 |
| 166 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +44 | 2964 |
| 167 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +44 | 26366 |
| 168 | [floci-io/floci](https://github.com/floci-io/floci) | +44 | 15493 |
| 169 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +43 | 13331 |
| 170 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +43 | 1602 |
| 171 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 2954 |
| 172 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +43 | 7375 |
| 173 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +42 | 15769 |
| 174 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +41 | 19237 |
| 175 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +41 | 7941 |
| 176 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +41 | 45074 |
| 177 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1394 |
| 178 | [beltromatti/get-it](https://github.com/beltromatti/get-it) | +39 | 868 |
| 179 | [google-research/tabfm](https://github.com/google-research/tabfm) | +38 | 1394 |
| 180 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1279 |
| 181 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +37 | 3758 |
| 182 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +36 | 8213 |
| 183 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +35 | 1806 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +35 | 16933 |
| 185 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +32 | 2140 |
| 186 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +31 | 1658 |
| 187 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +31 | 7379 |
| 188 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +31 | 7459 |
| 189 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +29 | 8859 |
| 190 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1188 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +28 | 28740 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +28 | 5149 |
| 193 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 894 |
| 194 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2319 |
| 195 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +27 | 545 |
| 196 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +26 | 5529 |
| 197 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +25 | 5979 |
| 198 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +24 | 956 |
| 199 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 434 |
| 200 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +23 | 1259 |
| 201 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +22 | 8669 |
| 202 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 616 |
| 203 | [eze-is/web-access](https://github.com/eze-is/web-access) | +22 | 8096 |
| 204 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +21 | 11623 |
| 205 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +20 | 2124 |
| 206 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +20 | 513 |
| 207 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +19 | 1393 |
| 208 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 645 |
| 209 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +19 | 4282 |
| 210 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +18 | 685 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +18 | 4217 |
| 212 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 613 |
| 213 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +17 | 5719 |
| 214 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +17 | 2528 |
| 215 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +16 | 479 |
| 216 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +15 | 480 |
| 217 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 498 |
| 218 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +14 | 5600 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2645 |
| 220 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +14 | 2178 |
| 221 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +14 | 13965 |
| 222 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 471 |
| 223 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +14 | 2763 |
| 224 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +14 | 810 |
| 225 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +13 | 599 |
| 226 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +13 | 1902 |
| 227 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 189 |
| 228 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +13 | 4980 |
| 229 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +13 | 12299 |
| 230 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +13 | 1526 |
| 231 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +13 | 2458 |
| 232 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +13 | 3019 |
| 233 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 457 |
| 234 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +12 | 1477 |
| 235 | [AI-Builder-Club/skills](https://github.com/AI-Builder-Club/skills) | +12 | 779 |
| 236 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 326 |
| 237 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +12 | 605 |
| 238 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +12 | 1478 |
| 239 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +12 | 372 |
| 240 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 664 |
| 241 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +11 | 717 |
| 242 | [robinebers/openusage](https://github.com/robinebers/openusage) | +11 | 3119 |
| 243 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +11 | 2707 |
| 244 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 320 |
| 245 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 421 |
| 246 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 201 |
| 247 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +10 | 907 |
| 248 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +10 | 1650 |
| 249 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +10 | 1156 |
| 250 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 288 |
| 251 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +10 | 4720 |
| 252 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 3774 |
| 253 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +9 | 380 |
| 254 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +9 | 657 |
| 255 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +9 | 348 |
| 256 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 257 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +9 | 3644 |
| 258 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 222 |
| 259 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +8 | 395 |
| 260 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 547 |
| 261 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 201 |
| 262 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +8 | 29 |
| 263 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +8 | 1115 |
| 264 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1285 |
| 265 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +7 | 2540 |
| 266 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +7 | 2304 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2743 |
| 268 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +7 | 1768 |
| 269 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +7 | 702 |
| 270 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 195 |
| 271 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 438 |
| 272 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 348 |
| 273 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +6 | 2625 |
| 274 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 179 |
| 275 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 9485 |
| 276 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +6 | 856 |
| 277 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 73 |
| 278 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 295 |
| 279 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 117 |
| 280 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 529 |
| 281 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 468 |
| 282 | [yuqing2026/ruoyi-office](https://github.com/yuqing2026/ruoyi-office) | +4 | 198 |
| 283 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 585 |
| 284 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 285 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +4 | 809 |
| 286 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +4 | 1677 |
| 287 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 94 |
| 288 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +3 | 607 |
| 289 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 221 |
| 290 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 391 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 216 |
| 292 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 293 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 398 |
| 294 | [Angais/minedit](https://github.com/Angais/minedit) | +3 | 133 |
| 295 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 296 | [apache/phoenix-adapters](https://github.com/apache/phoenix-adapters) | +3 | 118 |
| 297 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +3 | 594 |
| 298 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 286 |
| 299 | [oneQAQone/QFun](https://github.com/oneQAQone/QFun) | +3 | 183 |
| 300 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +2 | 232 |
