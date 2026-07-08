---
title: "2026-07-08 GitHub增长趋势报告"
description: "1.ai-job-search+39 2.OfficeCLI+12 3.knockoff+11 4.herdr+8 5.openwiki+8"
date: 2026-07-08T21:09:16+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-08 21:09:16

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
        'daily': {"categories": ["teamchong/pxpipe", "tutti-os/tutti", "ZhuLinsen/daily_stock_analysis", "openai/codex-plugin-cc", "AgriciDaniel/claude-obsidian", "Yuan1z0825/nature-skills", "oomol-lab/open-connector", "Imbad0202/academic-research-skills", "DeusData/codebase-memory-mcp", "xuchonglang/investing-for-beginners", "TencentCloud/CubeSandbox", "usestrix/strix", "kyutai-labs/pocket-tts", "calesthio/OpenMontage", "diegosouzapw/OmniRoute", "langchain-ai/openwiki", "ogulcancelik/herdr", "Shpigford/knockoff", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search"], "data": [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 7, 8, 8, 11, 12, 39]},
        'weekly': {"categories": ["harvard-edge/cs249r_book", "browser-use/video-use", "jamiepine/voicebox", "hasaneyldrm/exercises-dataset", "ZhuLinsen/daily_stock_analysis", "HKUDS/Vibe-Trading", "stablyai/orca", "diegosouzapw/OmniRoute", "teamchong/pxpipe", "ogulcancelik/herdr", "alibaba/page-agent", "DeusData/codebase-memory-mcp", "MadsLorentzen/ai-job-search", "calesthio/OpenMontage", "facebook/astryx", "openai/codex-plugin-cc", "Zackriya-Solutions/meetily", "erincatto/box3d", "langchain-ai/openwiki", "usestrix/strix"], "data": [50, 55, 58, 60, 62, 66, 66, 76, 76, 89, 90, 93, 97, 98, 112, 112, 114, 123, 171, 215]},
        'monthly': {"categories": ["BigPizzaV3/CodexPlusPlus", "Imbad0202/academic-research-skills", "jamiepine/voicebox", "shadcn/improve", "baidu/Unlimited-OCR", "usestrix/strix", "phuryn/pm-skills", "hugohe3/ppt-master", "palmier-io/palmier-pro", "NVIDIA/SkillSpector", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "mvanhorn/last30days-skill", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [205, 207, 209, 217, 223, 238, 270, 291, 291, 311, 337, 375, 468, 539, 542, 613, 656, 748, 1003, 1703]}
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
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +39 | 15116 |
| 2 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +12 | 11616 |
| 3 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +11 | 1375 |
| 4 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +8 | 14326 |
| 5 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +8 | 9731 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +7 | 13697 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +5 | 35569 |
| 8 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +5 | 6609 |
| 9 | [usestrix/strix](https://github.com/usestrix/strix) | +5 | 39007 |
| 10 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +5 | 8876 |
| 11 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +4 | 1176 |
| 12 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +4 | 28539 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +4 | 36935 |
| 14 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +4 | 991 |
| 15 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 27126 |
| 16 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +3 | 9031 |
| 17 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +3 | 26874 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 55871 |
| 19 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +3 | 1209 |
| 20 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +3 | 5041 |
| 21 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +3 | 17240 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3 | 38828 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3 | 44696 |
| 24 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 5974 |
| 25 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +3 | 10058 |
| 26 | [stablyai/orca](https://github.com/stablyai/orca) | +2 | 14132 |
| 27 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +2 | 10288 |
| 28 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +2 | 12975 |
| 29 | [Formsmith746/SketchForge-3D](https://github.com/Formsmith746/SketchForge-3D) | +2 | 338 |
| 30 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2 | 26440 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +215 | 39007 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +171 | 9731 |
| 3 | [erincatto/box3d](https://github.com/erincatto/box3d) | +123 | 4712 |
| 4 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +114 | 21578 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +112 | 26874 |
| 6 | [facebook/astryx](https://github.com/facebook/astryx) | +112 | 7145 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +98 | 35569 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +97 | 15117 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +93 | 28539 |
| 10 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +90 | 25188 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +89 | 14326 |
| 12 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +76 | 5041 |
| 13 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +76 | 13697 |
| 14 | [stablyai/orca](https://github.com/stablyai/orca) | +66 | 14132 |
| 15 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +66 | 18713 |
| 16 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +62 | 55871 |
| 17 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +60 | 11029 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +58 | 38828 |
| 19 | [browser-use/video-use](https://github.com/browser-use/video-use) | +55 | 16050 |
| 20 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +50 | 27152 |
| 21 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +47 | 4699 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +47 | 12013 |
| 23 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +44 | 3834 |
| 24 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +41 | 26751 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +41 | 37747 |
| 26 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +40 | 3958 |
| 27 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +39 | 8710 |
| 28 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +36 | 46375 |
| 29 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +35 | 5974 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +35 | 27126 |
| 31 | [google-research/tabfm](https://github.com/google-research/tabfm) | +35 | 1583 |
| 32 | [baairon/torlink](https://github.com/baairon/torlink) | +34 | 3308 |
| 33 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +33 | 50672 |
| 34 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +33 | 6869 |
| 35 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +32 | 3120 |
| 36 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +32 | 3431 |
| 37 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +31 | 13394 |
| 38 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +31 | 10288 |
| 39 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +30 | 3459 |
| 40 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +30 | 24957 |
| 41 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +28 | 36935 |
| 42 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +28 | 23964 |
| 43 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +27 | 5363 |
| 44 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +26 | 21673 |
| 45 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +26 | 44696 |
| 46 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +26 | 8876 |
| 47 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +26 | 7873 |
| 48 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +26 | 15544 |
| 49 | [Augani/dory](https://github.com/Augani/dory) | +25 | 915 |
| 50 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +25 | 33797 |
| 51 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 39186 |
| 52 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +24 | 37286 |
| 53 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +24 | 5187 |
| 54 | [Younesfdj/gitfut](https://github.com/Younesfdj/gitfut) | +24 | 1798 |
| 55 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +23 | 1176 |
| 56 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +23 | 823 |
| 57 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 16757 |
| 58 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +22 | 8383 |
| 59 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +22 | 1844 |
| 60 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +22 | 8213 |
| 61 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2804 |
| 62 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +21 | 13698 |
| 63 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +21 | 1753 |
| 64 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +21 | 25507 |
| 65 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +20 | 2201 |
| 66 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +19 | 17240 |
| 67 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +19 | 1008 |
| 68 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +19 | 733 |
| 69 | [modiqo/skillspec](https://github.com/modiqo/skillspec) | +19 | 904 |
| 70 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +19 | 3422 |
| 71 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 11616 |
| 72 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +18 | 11671 |
| 73 | [decolua/9router](https://github.com/decolua/9router) | +18 | 21117 |
| 74 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +18 | 25555 |
| 75 | [shadcn/improve](https://github.com/shadcn/improve) | +18 | 7505 |
| 76 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +18 | 12468 |
| 77 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +18 | 1020 |
| 78 | [modiqo/cliare](https://github.com/modiqo/cliare) | +18 | 711 |
| 79 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +18 | 5578 |
| 80 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +17 | 1572 |
| 81 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +17 | 590 |
| 82 | [floci-io/floci](https://github.com/floci-io/floci) | +17 | 15671 |
| 83 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 6760 |
| 84 | [multica-ai/multica](https://github.com/multica-ai/multica) | +17 | 39534 |
| 85 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +17 | 16877 |
| 86 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +17 | 9587 |
| 87 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +16 | 1409 |
| 88 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 256 |
| 89 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +16 | 23034 |
| 90 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +16 | 25055 |
| 91 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +15 | 989 |
| 92 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +15 | 3804 |
| 93 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +15 | 30482 |
| 94 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +15 | 4300 |
| 95 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +15 | 5495 |
| 96 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +14 | 30860 |
| 97 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +14 | 21492 |
| 98 | [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | +14 | 695 |
| 99 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 348 |
| 100 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +14 | 3349 |
| 101 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +14 | 38091 |
| 102 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +14 | 2909 |
| 103 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +14 | 1970 |
| 104 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 775 |
| 105 | [davidondrej/skills](https://github.com/davidondrej/skills) | +12 | 1903 |
| 106 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +12 | 5511 |
| 107 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 37652 |
| 108 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 9031 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +12 | 45009 |
| 110 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +12 | 6462 |
| 111 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +12 | 5775 |
| 112 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +11 | 4163 |
| 113 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +11 | 1375 |
| 114 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +11 | 27279 |
| 115 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +11 | 598 |
| 116 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 624 |
| 117 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +11 | 17419 |
| 118 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +11 | 10594 |
| 119 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +11 | 15017 |
| 120 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 455 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1703 | 77934 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1003 | 57859 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +748 | 53195 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +656 | 45049 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +613 | 35569 |
| 6 | [apple/container](https://github.com/apple/container) | +542 | 47134 |
| 7 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +539 | 28539 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +468 | 50672 |
| 9 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +375 | 11650 |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +337 | 55871 |
| 11 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +311 | 12468 |
| 12 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +291 | 10143 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +291 | 37747 |
| 14 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +270 | 23034 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +238 | 39007 |
| 16 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +223 | 13698 |
| 17 | [shadcn/improve](https://github.com/shadcn/improve) | +217 | 7505 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +209 | 38828 |
| 19 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +207 | 36935 |
| 20 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +205 | 23964 |
| 21 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +204 | 24957 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +201 | 27126 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +196 | 33797 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +196 | 44696 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +195 | 15544 |
| 26 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +193 | 35170 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +192 | 26751 |
| 28 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +189 | 12013 |
| 29 | [stablyai/orca](https://github.com/stablyai/orca) | +186 | 14132 |
| 30 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 27353 |
| 31 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +181 | 37652 |
| 32 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +180 | 14326 |
| 33 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 6760 |
| 34 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +178 | 6499 |
| 35 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 7873 |
| 36 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +171 | 9731 |
| 37 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7777 |
| 38 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +161 | 18448 |
| 39 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +158 | 6298 |
| 40 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26671 |
| 41 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +149 | 18713 |
| 42 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +149 | 11671 |
| 43 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +147 | 26874 |
| 44 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +146 | 10185 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +145 | 16757 |
| 46 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18140 |
| 47 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +139 | 25188 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +139 | 39186 |
| 49 | [facebook/astryx](https://github.com/facebook/astryx) | +136 | 7145 |
| 50 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +130 | 62276 |
| 51 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +126 | 21578 |
| 52 | [erincatto/box3d](https://github.com/erincatto/box3d) | +123 | 4712 |
| 53 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +122 | 22798 |
| 54 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +121 | 7626 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +121 | 37286 |
| 56 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +120 | 32835 |
| 57 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +119 | 12609 |
| 58 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +118 | 13697 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +117 | 28071 |
| 60 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +115 | 39438 |
| 61 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +114 | 15117 |
| 62 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 52 |
| 63 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +113 | 5578 |
| 64 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +113 | 25555 |
| 65 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +110 | 25841 |
| 66 | [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) | +106 | 4648 |
| 67 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +105 | 3804 |
| 68 | [roboflow/supervision](https://github.com/roboflow/supervision) | +105 | 36553 |
| 69 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +103 | 8213 |
| 70 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +102 | 30860 |
| 71 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +101 | 21093 |
| 72 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +100 | 4162 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +99 | 24882 |
| 74 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +98 | 11029 |
| 75 | [browser-use/video-use](https://github.com/browser-use/video-use) | +98 | 16050 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +97 | 27279 |
| 77 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +95 | 34468 |
| 78 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 9587 |
| 79 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +87 | 10594 |
| 80 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +86 | 8173 |
| 81 | [alibaba/zvec](https://github.com/alibaba/zvec) | +85 | 14353 |
| 82 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +85 | 24586 |
| 83 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +85 | 7320 |
| 84 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +85 | 31929 |
| 85 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +85 | 26581 |
| 86 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +84 | 46375 |
| 87 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +84 | 20646 |
| 88 | [multica-ai/multica](https://github.com/multica-ai/multica) | +83 | 39534 |
| 89 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +82 | 3958 |
| 90 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +82 | 7947 |
| 91 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +82 | 27936 |
| 92 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +82 | 22472 |
| 93 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6462 |
| 94 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +80 | 4345 |
| 95 | [antirez/ds4](https://github.com/antirez/ds4) | +79 | 17984 |
| 96 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +79 | 5511 |
| 97 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5042 |
| 98 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +77 | 21492 |
| 99 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +74 | 30482 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +70 | 21673 |
| 101 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +69 | 10288 |
| 102 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +69 | 45009 |
| 103 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +69 | 3120 |
| 104 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +68 | 5187 |
| 105 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +68 | 9031 |
| 106 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +68 | 33263 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +67 | 49525 |
| 108 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +66 | 16702 |
| 109 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +66 | 26391 |
| 110 | [decolua/9router](https://github.com/decolua/9router) | +65 | 21117 |
| 111 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 6869 |
| 112 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +64 | 3431 |
| 113 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +63 | 42633 |
| 114 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3546 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +60 | 31804 |
| 116 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +60 | 27152 |
| 117 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +59 | 6185 |
| 118 | [google/skills](https://github.com/google/skills) | +58 | 14457 |
| 119 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2566 |
| 120 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +56 | 5495 |
| 121 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +55 | 9374 |
| 122 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +55 | 25925 |
| 123 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +55 | 5205 |
| 124 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +55 | 36103 |
| 125 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +54 | 2491 |
| 126 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +53 | 14076 |
| 127 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +53 | 25055 |
| 128 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +53 | 5648 |
| 129 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +53 | 26310 |
| 130 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +52 | 4699 |
| 131 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +51 | 5974 |
| 132 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +51 | 4300 |
| 133 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +50 | 3459 |
| 134 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +50 | 3662 |
| 135 | [openai/plugins](https://github.com/openai/plugins) | +50 | 4149 |
| 136 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +50 | 19612 |
| 137 | [anbeime/skill](https://github.com/anbeime/skill) | +49 | 3330 |
| 138 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +48 | 7843 |
| 139 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +47 | 10825 |
| 140 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +47 | 12079 |
| 141 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +43 | 5775 |
| 142 | [openai/skills](https://github.com/openai/skills) | +43 | 23394 |
| 143 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3001 |
| 144 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +42 | 4163 |
| 145 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +42 | 13394 |
| 146 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 147 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +41 | 17419 |
| 148 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +41 | 26256 |
| 149 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1583 |
| 150 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +40 | 18140 |
| 151 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1441 |
| 152 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +40 | 3751 |
| 153 | [floci-io/floci](https://github.com/floci-io/floci) | +40 | 15671 |
| 154 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +39 | 3286 |
| 155 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1354 |
| 156 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1844 |
| 157 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +38 | 6014 |
| 158 | [browser-act/skills](https://github.com/browser-act/skills) | +37 | 4106 |
| 159 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +37 | 15667 |
| 160 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +37 | 26440 |
| 161 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +37 | 3920 |
| 162 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +37 | 4031 |
| 163 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +36 | 25935 |
| 164 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +36 | 45139 |
| 165 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +35 | 1970 |
| 166 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +35 | 8059 |
| 167 | [jundot/omlx](https://github.com/jundot/omlx) | +35 | 17651 |
| 168 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +34 | 15825 |
| 169 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2747 |
| 170 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +34 | 6595 |
| 171 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2051 |
| 172 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1863 |
| 173 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +32 | 8052 |
| 174 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +32 | 3858 |
| 175 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +31 | 19319 |
| 176 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +31 | 8277 |
| 177 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1197 |
| 178 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +30 | 1619 |
| 179 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +30 | 17943 |
| 180 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1118 |
| 181 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +29 | 1733 |
| 182 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1225 |
| 183 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 582 |
| 184 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 904 |
| 185 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +27 | 1753 |
| 186 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2349 |
| 187 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +26 | 15017 |
| 188 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +26 | 7445 |
| 189 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +25 | 7510 |
| 190 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 823 |
| 191 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +24 | 2200 |
| 192 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 436 |
| 193 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +23 | 5587 |
| 194 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 621 |
| 195 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +21 | 28826 |
| 196 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +21 | 1291 |
| 197 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +21 | 5198 |
| 198 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +19 | 11690 |
| 199 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +19 | 8733 |
| 200 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 654 |
| 201 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +19 | 964 |
| 202 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +18 | 2181 |
| 203 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 710 |
| 204 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 630 |
| 205 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +17 | 4327 |
| 206 | [eze-is/web-access](https://github.com/eze-is/web-access) | +16 | 8136 |
| 207 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +16 | 8872 |
| 208 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2687 |
| 209 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1405 |
| 210 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4249 |
| 211 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +14 | 5999 |
| 212 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 502 |
| 213 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 476 |
| 214 | [beltromatti/get-it](https://github.com/beltromatti/get-it) | +14 | 870 |
| 215 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +13 | 764 |
| 216 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +13 | 5669 |
| 217 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 218 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 402 |
| 219 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +13 | 3065 |
| 220 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +13 | 2777 |
| 221 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 460 |
| 222 | [AI-Builder-Club/skills](https://github.com/AI-Builder-Club/skills) | +12 | 802 |
| 223 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +12 | 532 |
| 224 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 13994 |
| 225 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 328 |
| 226 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +11 | 1375 |
| 227 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +11 | 0 |
| 228 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 670 |
| 229 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +11 | 2235 |
| 230 | [robinebers/openusage](https://github.com/robinebers/openusage) | +11 | 3172 |
| 231 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +11 | 2471 |
| 232 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 456 |
| 233 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 333 |
| 234 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 757 |
| 235 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 423 |
| 236 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +10 | 1917 |
| 237 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 201 |
| 238 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +10 | 4980 |
| 239 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +10 | 1165 |
| 240 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 306 |
| 241 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +10 | 481 |
| 242 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2740 |
| 243 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +9 | 740 |
| 244 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +9 | 385 |
| 245 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 246 | [rezarahiminia/worldcup2026](https://github.com/rezarahiminia/worldcup2026) | +9 | 426 |
| 247 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3849 |
| 248 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 235 |
| 249 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +8 | 1297 |
| 250 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 576 |
| 251 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 365 |
| 252 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +8 | 1681 |
| 253 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 203 |
| 254 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 570 |
| 255 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +8 | 3657 |
| 256 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +8 | 834 |
| 257 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +7 | 1492 |
| 258 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 160 |
| 259 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 950 |
| 260 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +7 | 622 |
| 261 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 248 |
| 262 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2763 |
| 263 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 200 |
| 264 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 444 |
| 265 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 359 |
| 266 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +6 | 400 |
| 267 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 178 |
| 268 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +6 | 1784 |
| 269 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2544 |
| 270 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 80 |
| 271 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9490 |
| 272 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +5 | 727 |
| 273 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 302 |
| 274 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +5 | 636 |
| 275 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 118 |
| 276 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2651 |
| 277 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 494 |
| 278 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2318 |
| 279 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 603 |
| 280 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 281 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +4 | 531 |
| 282 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 97 |
| 283 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +4 | 1117 |
| 284 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 222 |
| 285 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 395 |
| 286 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 115 |
| 287 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +3 | 580 |
| 288 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 813 |
| 289 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 220 |
| 290 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 291 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 292 | [apache/phoenix-adapters](https://github.com/apache/phoenix-adapters) | +3 | 118 |
| 293 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 294 |
| 294 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 610 |
| 295 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1681 |
| 296 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3332 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 95 |
| 298 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 398 |
| 299 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 849 |
| 300 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
