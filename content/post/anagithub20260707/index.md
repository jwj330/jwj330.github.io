---
title: "2026-07-07 GitHub增长趋势报告"
description: "1.openwiki+15 2.ai-job-search+10 3.strix+10 4.OmniRoute+9 5.claude-video+6"
date: 2026-07-07T21:25:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-07 21:25:54

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
        'daily': {"categories": ["mvanhorn/last30days-skill", "Yuan1z0825/nature-skills", "ComPDFKit/compdf-self-hosted", "elder-plinius/T3MP3ST", "Emily2040/seedance-2.0", "agentscope-ai/QwenPaw", "xbtlin/ai-berkshire", "shadcn/improve", "creekchandlercord/VoiceMOD-Activated", "kangarooking/cangjie-skill", "teamchong/pxpipe", "ogulcancelik/herdr", "alibaba/page-agent", "iOfficeAI/OfficeCLI", "BraveAshNozzle/Adobe-Acrobat-Pro", "bradautomates/claude-video", "diegosouzapw/OmniRoute", "usestrix/strix", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki"], "data": [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 9, 10, 10, 15]},
        'weekly': {"categories": ["harvard-edge/cs249r_book", "jamiepine/voicebox", "xbtlin/ai-berkshire", "browser-use/video-use", "MadsLorentzen/ai-job-search", "ZhuLinsen/daily_stock_analysis", "stablyai/orca", "HKUDS/Vibe-Trading", "teamchong/pxpipe", "diegosouzapw/OmniRoute", "hasaneyldrm/exercises-dataset", "ogulcancelik/herdr", "alibaba/page-agent", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "Zackriya-Solutions/meetily", "facebook/astryx", "erincatto/box3d", "langchain-ai/openwiki", "usestrix/strix"], "data": [51, 56, 56, 58, 58, 61, 67, 68, 73, 74, 78, 85, 89, 95, 103, 108, 116, 122, 165, 216]},
        'monthly': {"categories": ["Imbad0202/academic-research-skills", "pbakaus/impeccable", "usestrix/strix", "RyanCodrai/turbovec", "BigPizzaV3/CodexPlusPlus", "lfnovo/open-notebook", "phuryn/pm-skills", "palmier-io/palmier-pro", "hugohe3/ppt-master", "NVIDIA/SkillSpector", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "DeusData/codebase-memory-mcp", "apple/container", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [227, 232, 235, 243, 248, 264, 279, 291, 305, 312, 344, 375, 536, 541, 612, 657, 703, 791, 1088, 1698]}
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
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +15 | 8947 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +10 | 10376 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +10 | 38513 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +9 | 13093 |
| 5 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 5073 |
| 6 | [BraveAshNozzle/Adobe-Acrobat-Pro](https://github.com/BraveAshNozzle/Adobe-Acrobat-Pro) | +5 | 319 |
| 7 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +5 | 9792 |
| 8 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +5 | 24895 |
| 9 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +5 | 13462 |
| 10 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +4 | 4727 |
| 11 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 1991 |
| 12 | [creekchandlercord/VoiceMOD-Activated](https://github.com/creekchandlercord/VoiceMOD-Activated) | +4 | 235 |
| 13 | [shadcn/improve](https://github.com/shadcn/improve) | +4 | 7423 |
| 14 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +4 | 11661 |
| 15 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 21272 |
| 16 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +4 | 3265 |
| 17 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +4 | 3225 |
| 18 | [ComPDFKit/compdf-self-hosted](https://github.com/ComPDFKit/compdf-self-hosted) | +3 | 105 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 26840 |
| 20 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +3 | 50295 |
| 21 | [sw33tLie/macshot](https://github.com/sw33tLie/macshot) | +3 | 2426 |
| 22 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +3 | 11400 |
| 23 | [alibaba/zvec](https://github.com/alibaba/zvec) | +3 | 13990 |
| 24 | [gastownhall/gastown](https://github.com/gastownhall/gastown) | +3 | 16855 |
| 25 | [Dryxio/auto-re-agent](https://github.com/Dryxio/auto-re-agent) | +2 | 787 |
| 26 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +2 | 975 |
| 27 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +2 | 1843 |
| 28 | [jay3-yy/BiliPai](https://github.com/jay3-yy/BiliPai) | +2 | 3640 |
| 29 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +2 | 13658 |
| 30 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +2 | 4278 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +216 | 38513 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +165 | 8947 |
| 3 | [erincatto/box3d](https://github.com/erincatto/box3d) | +122 | 4513 |
| 4 | [facebook/astryx](https://github.com/facebook/astryx) | +116 | 6818 |
| 5 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +108 | 20576 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +103 | 34969 |
| 7 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +95 | 27950 |
| 8 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +89 | 24895 |
| 9 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +85 | 13462 |
| 10 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +78 | 10679 |
| 11 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +74 | 13093 |
| 12 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +73 | 4727 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +68 | 18496 |
| 14 | [stablyai/orca](https://github.com/stablyai/orca) | +67 | 13446 |
| 15 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +61 | 55517 |
| 16 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +58 | 10376 |
| 17 | [browser-use/video-use](https://github.com/browser-use/video-use) | +58 | 15856 |
| 18 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +56 | 11661 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +56 | 38497 |
| 20 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +51 | 27121 |
| 21 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +46 | 4310 |
| 22 | [rommapp/romm](https://github.com/rommapp/romm) | +45 | 10811 |
| 23 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +44 | 3225 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +44 | 37472 |
| 25 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +42 | 26461 |
| 26 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +41 | 3870 |
| 27 | [baairon/torlink](https://github.com/baairon/torlink) | +40 | 3246 |
| 28 | [google-research/tabfm](https://github.com/google-research/tabfm) | +38 | 1503 |
| 29 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +37 | 46233 |
| 30 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +36 | 3260 |
| 31 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +35 | 6671 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 26840 |
| 33 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +32 | 13376 |
| 34 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +32 | 10186 |
| 35 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +32 | 24864 |
| 36 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +32 | 2951 |
| 37 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +31 | 5073 |
| 38 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +31 | 7791 |
| 39 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +28 | 3265 |
| 40 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +28 | 50295 |
| 41 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +27 | 23799 |
| 42 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +27 | 5303 |
| 43 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +27 | 36729 |
| 44 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +26 | 15445 |
| 45 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 21495 |
| 46 | [Augani/dory](https://github.com/Augani/dory) | +25 | 883 |
| 47 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 39028 |
| 48 | [Younesfdj/gitfut](https://github.com/Younesfdj/gitfut) | +24 | 1689 |
| 49 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +24 | 8409 |
| 50 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +23 | 44251 |
| 51 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +23 | 791 |
| 52 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +23 | 1843 |
| 53 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +23 | 37078 |
| 54 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +23 | 13612 |
| 55 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +23 | 33631 |
| 56 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 16550 |
| 57 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +23 | 14992 |
| 58 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +22 | 5080 |
| 59 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +22 | 8040 |
| 60 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +21 | 8347 |
| 61 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2792 |
| 62 | [decolua/9router](https://github.com/decolua/9router) | +21 | 20705 |
| 63 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +21 | 25377 |
| 64 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +20 | 2139 |
| 65 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +19 | 758 |
| 66 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +19 | 12293 |
| 67 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +19 | 719 |
| 68 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +19 | 24996 |
| 69 | [modiqo/skillspec](https://github.com/modiqo/skillspec) | +19 | 903 |
| 70 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +19 | 5493 |
| 71 | [0xNyk/council-of-high-intelligence](https://github.com/0xNyk/council-of-high-intelligence) | +19 | 3410 |
| 72 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +18 | 11400 |
| 73 | [floci-io/floci](https://github.com/floci-io/floci) | +18 | 15562 |
| 74 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +18 | 25351 |
| 75 | [shadcn/improve](https://github.com/shadcn/improve) | +18 | 7423 |
| 76 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +18 | 16807 |
| 77 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +18 | 989 |
| 78 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +18 | 6622 |
| 79 | [modiqo/cliare](https://github.com/modiqo/cliare) | +18 | 713 |
| 80 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +17 | 516 |
| 81 | [multica-ai/multica](https://github.com/multica-ai/multica) | +17 | 39412 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +16 | 30680 |
| 83 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +16 | 16999 |
| 84 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +16 | 1494 |
| 85 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +16 | 1380 |
| 86 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 242 |
| 87 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +16 | 9506 |
| 88 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +16 | 3766 |
| 89 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +16 | 5441 |
| 90 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +15 | 38025 |
| 91 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +15 | 22905 |
| 92 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +15 | 6380 |
| 93 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +15 | 10023 |
| 94 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +15 | 30403 |
| 95 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +15 | 4238 |
| 96 | [dotnet/skills](https://github.com/dotnet/skills) | +14 | 4274 |
| 97 | [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | +14 | 676 |
| 98 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +14 | 951 |
| 99 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 330 |
| 100 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +14 | 18752 |
| 101 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +14 | 2868 |
| 102 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +14 | 1945 |
| 103 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 3297 |
| 104 | [davidondrej/skills](https://github.com/davidondrej/skills) | +12 | 1773 |
| 105 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +12 | 5460 |
| 106 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +12 | 21272 |
| 107 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 27162 |
| 108 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +12 | 5680 |
| 109 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 37585 |
| 110 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +11 | 571 |
| 111 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 622 |
| 112 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 44937 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +11 | 17307 |
| 114 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +11 | 10481 |
| 115 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +11 | 24328 |
| 116 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 441 |
| 117 | [InternScience/Agents-A1](https://github.com/InternScience/Agents-A1) | +10 | 407 |
| 118 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +10 | 16639 |
| 119 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +10 | 42548 |
| 120 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +10 | 8958 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1698 | 76815 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1088 | 57502 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +791 | 52641 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +703 | 50295 |
| 5 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +657 | 44985 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +612 | 34969 |
| 7 | [apple/container](https://github.com/apple/container) | +541 | 46976 |
| 8 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +536 | 27950 |
| 9 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +375 | 11585 |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +344 | 55517 |
| 11 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +312 | 12293 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +305 | 37472 |
| 13 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +291 | 10087 |
| 14 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +279 | 22905 |
| 15 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +264 | 35106 |
| 16 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +248 | 23799 |
| 17 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +243 | 12595 |
| 18 | [usestrix/strix](https://github.com/usestrix/strix) | +235 | 38513 |
| 19 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +232 | 44251 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +227 | 36729 |
| 21 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +223 | 13612 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +223 | 33631 |
| 23 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +222 | 15445 |
| 24 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +219 | 10093 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +217 | 26840 |
| 26 | [shadcn/improve](https://github.com/shadcn/improve) | +217 | 7423 |
| 27 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +216 | 37585 |
| 28 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +214 | 24864 |
| 29 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +210 | 38497 |
| 30 | [roboflow/supervision](https://github.com/roboflow/supervision) | +208 | 36553 |
| 31 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +196 | 26461 |
| 32 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +195 | 18419 |
| 33 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +188 | 11661 |
| 34 | [stablyai/orca](https://github.com/stablyai/orca) | +188 | 13446 |
| 35 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +186 | 27311 |
| 36 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +179 | 13462 |
| 37 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 6622 |
| 38 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +177 | 6435 |
| 39 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +175 | 7791 |
| 40 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +165 | 8947 |
| 41 | [EpicGames/lore](https://github.com/EpicGames/lore) | +164 | 7754 |
| 42 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +158 | 39028 |
| 43 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26640 |
| 44 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +156 | 18496 |
| 45 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +156 | 6117 |
| 46 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +155 | 16550 |
| 47 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +154 | 11400 |
| 48 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +149 | 21035 |
| 49 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18074 |
| 50 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +141 | 62173 |
| 51 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +140 | 24895 |
| 52 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +139 | 23286 |
| 53 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +136 | 33040 |
| 54 | [facebook/astryx](https://github.com/facebook/astryx) | +135 | 6818 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +134 | 37078 |
| 56 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +133 | 32760 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +133 | 27891 |
| 58 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +127 | 25351 |
| 59 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +127 | 39383 |
| 60 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +126 | 7585 |
| 61 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +126 | 5171 |
| 62 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +125 | 22689 |
| 63 | [erincatto/box3d](https://github.com/erincatto/box3d) | +122 | 4513 |
| 64 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +119 | 20576 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +115 | 30680 |
| 66 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +115 | 8040 |
| 67 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +114 | 5493 |
| 68 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 52 |
| 69 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +113 | 13093 |
| 70 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +113 | 25764 |
| 71 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +105 | 3766 |
| 72 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +104 | 27162 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +103 | 24787 |
| 74 | [browser-use/video-use](https://github.com/browser-use/video-use) | +100 | 15856 |
| 75 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +100 | 4067 |
| 76 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +100 | 34385 |
| 77 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +100 | 24776 |
| 78 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +99 | 10679 |
| 79 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +98 | 7233 |
| 80 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +96 | 20513 |
| 81 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +95 | 10378 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +95 | 39412 |
| 83 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +94 | 27889 |
| 84 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +94 | 31888 |
| 85 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +93 | 22437 |
| 86 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +93 | 26374 |
| 87 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +92 | 10481 |
| 88 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +92 | 24328 |
| 89 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +90 | 8139 |
| 90 | [google/skills](https://github.com/google/skills) | +87 | 14438 |
| 91 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +86 | 9506 |
| 92 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +86 | 46233 |
| 93 | [alibaba/zvec](https://github.com/alibaba/zvec) | +86 | 13990 |
| 94 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +85 | 5460 |
| 95 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +84 | 7928 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +83 | 30403 |
| 97 | [antirez/ds4](https://github.com/antirez/ds4) | +81 | 17861 |
| 98 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6380 |
| 99 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +80 | 3870 |
| 100 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +80 | 44937 |
| 101 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +80 | 4278 |
| 102 | [openai/plugins](https://github.com/openai/plugins) | +80 | 4130 |
| 103 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +78 | 33218 |
| 104 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +77 | 21272 |
| 105 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +77 | 2467 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +76 | 21495 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +75 | 16639 |
| 108 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +74 | 4727 |
| 109 | [decolua/9router](https://github.com/decolua/9router) | +74 | 20705 |
| 110 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +73 | 36724 |
| 111 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +71 | 42548 |
| 112 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +70 | 8958 |
| 113 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +70 | 49041 |
| 114 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +70 | 26188 |
| 115 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +69 | 5080 |
| 116 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +68 | 10186 |
| 117 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +68 | 2951 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +67 | 31751 |
| 119 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +67 | 6096 |
| 120 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +66 | 5161 |
| 121 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +64 | 3260 |
| 122 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +63 | 9336 |
| 123 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3512 |
| 124 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +61 | 5632 |
| 125 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +61 | 27121 |
| 126 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +59 | 5441 |
| 127 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 128 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +58 | 25896 |
| 129 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2534 |
| 130 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +56 | 24996 |
| 131 | [openai/skills](https://github.com/openai/skills) | +56 | 23347 |
| 132 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +56 | 36103 |
| 133 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +55 | 15623 |
| 134 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +54 | 4238 |
| 135 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +54 | 26234 |
| 136 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +53 | 10744 |
| 137 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +53 | 3716 |
| 138 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +53 | 7779 |
| 139 | [anbeime/skill](https://github.com/anbeime/skill) | +52 | 3277 |
| 140 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +51 | 4312 |
| 141 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +51 | 5680 |
| 142 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +50 | 5073 |
| 143 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +50 | 17307 |
| 144 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +50 | 3218 |
| 145 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +50 | 3612 |
| 146 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +50 | 19572 |
| 147 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +49 | 5963 |
| 148 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +48 | 3265 |
| 149 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +48 | 12055 |
| 150 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +45 | 14679 |
| 151 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +45 | 26221 |
| 152 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +44 | 4105 |
| 153 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +44 | 18088 |
| 154 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +43 | 13376 |
| 155 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +43 | 1945 |
| 156 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 2981 |
| 157 | [jundot/omlx](https://github.com/jundot/omlx) | +42 | 17615 |
| 158 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +42 | 25871 |
| 159 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +42 | 26398 |
| 160 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +42 | 2904 |
| 161 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +41 | 3163 |
| 162 | [floci-io/floci](https://github.com/floci-io/floci) | +41 | 15562 |
| 163 | [browser-act/skills](https://github.com/browser-act/skills) | +40 | 3962 |
| 164 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1400 |
| 165 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +39 | 8000 |
| 166 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +39 | 15794 |
| 167 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +39 | 6522 |
| 168 | [google-research/tabfm](https://github.com/google-research/tabfm) | +38 | 1503 |
| 169 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1331 |
| 170 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +38 | 7400 |
| 171 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1843 |
| 172 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +37 | 45105 |
| 173 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +37 | 17901 |
| 174 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +36 | 7998 |
| 175 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +36 | 19276 |
| 176 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +35 | 1610 |
| 177 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +35 | 3813 |
| 178 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +34 | 1201 |
| 179 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +33 | 8242 |
| 180 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1843 |
| 181 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +31 | 1700 |
| 182 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1180 |
| 183 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +29 | 7405 |
| 184 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +28 | 1074 |
| 185 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1199 |
| 186 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 563 |
| 187 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +28 | 7479 |
| 188 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 899 |
| 189 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2333 |
| 190 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +27 | 2167 |
| 191 | [beltromatti/get-it](https://github.com/beltromatti/get-it) | +26 | 869 |
| 192 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +25 | 5556 |
| 193 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +24 | 28783 |
| 194 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 434 |
| 195 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +23 | 791 |
| 196 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +23 | 1278 |
| 197 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +23 | 5173 |
| 198 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 618 |
| 199 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +22 | 8866 |
| 200 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +21 | 958 |
| 201 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +20 | 5988 |
| 202 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +20 | 8691 |
| 203 | [eze-is/web-access](https://github.com/eze-is/web-access) | +20 | 8110 |
| 204 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +19 | 11650 |
| 205 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 648 |
| 206 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +18 | 701 |
| 207 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +18 | 2152 |
| 208 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +17 | 4233 |
| 209 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 622 |
| 210 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +17 | 4305 |
| 211 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +15 | 521 |
| 212 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1401 |
| 213 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 502 |
| 214 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +14 | 2665 |
| 215 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +14 | 2201 |
| 216 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 473 |
| 217 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +14 | 479 |
| 218 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +14 | 2770 |
| 219 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +13 | 692 |
| 220 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +13 | 5618 |
| 221 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 222 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +13 | 13981 |
| 223 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +13 | 3043 |
| 224 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 459 |
| 225 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +12 | 5745 |
| 226 | [AI-Builder-Club/skills](https://github.com/AI-Builder-Club/skills) | +12 | 784 |
| 227 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +12 | 4979 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +12 | 537 |
| 229 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 328 |
| 230 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +12 | 12303 |
| 231 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +12 | 389 |
| 232 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +11 | 1912 |
| 233 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 668 |
| 234 | [robinebers/openusage](https://github.com/robinebers/openusage) | +11 | 3147 |
| 235 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +11 | 2464 |
| 236 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +11 | 2720 |
| 237 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 425 |
| 238 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 326 |
| 239 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 733 |
| 240 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 423 |
| 241 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +10 | 1488 |
| 242 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +10 | 726 |
| 243 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 201 |
| 244 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +10 | 1160 |
| 245 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 298 |
| 246 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +10 | 3951 |
| 247 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 3808 |
| 248 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +10 | 819 |
| 249 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +9 | 1661 |
| 250 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +9 | 367 |
| 251 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 252 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +9 | 622 |
| 253 | [rezarahiminia/worldcup2026](https://github.com/rezarahiminia/worldcup2026) | +9 | 425 |
| 254 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 229 |
| 255 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 559 |
| 256 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 357 |
| 257 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +8 | 933 |
| 258 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 202 |
| 259 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +8 | 3653 |
| 260 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +8 | 1116 |
| 261 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +7 | 397 |
| 262 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +7 | 1293 |
| 263 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 158 |
| 264 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +7 | 621 |
| 265 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +7 | 717 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2756 |
| 267 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +7 | 1777 |
| 268 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 199 |
| 269 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 442 |
| 270 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 352 |
| 271 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 178 |
| 272 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +6 | 2543 |
| 273 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 9488 |
| 274 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +6 | 2314 |
| 275 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 74 |
| 276 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 298 |
| 277 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 117 |
| 278 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +5 | 530 |
| 279 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2637 |
| 280 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 483 |
| 281 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +4 | 591 |
| 282 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 283 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 95 |
| 284 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +4 | 856 |
| 285 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 222 |
| 286 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 394 |
| 287 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 112 |
| 288 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 811 |
| 289 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +3 | 219 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +3 | 1680 |
| 291 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 292 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 293 | [apache/phoenix-adapters](https://github.com/apache/phoenix-adapters) | +3 | 118 |
| 294 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +3 | 597 |
| 295 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 291 |
| 296 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +2 | 235 |
| 297 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 607 |
| 298 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3330 |
| 299 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 96 |
| 300 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 398 |
