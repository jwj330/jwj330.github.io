---
title: "2026-07-10 GitHub增长趋势报告"
description: "1.ai-job-search+13 2.native+6 3.OfficeCLI+5 4.Pixelle-Video+4 5.claude-video+4"
date: 2026-07-10T21:06:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-10 21:06:54

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
        'daily': {"categories": ["alchaincyf/nuwa-skill", "gastownhall/gastown", "Alpha-Dojo/DojoAgents", "langchain-ai/openwiki", "Shpigford/knockoff", "larksuite/cli", "NVIDIA/OpenShell", "DeusData/codebase-memory-mcp", "JCodesMore/ai-website-cloner-template", "usestrix/strix", "microsoft/flint-chart", "kyutai-labs/pocket-tts", "Robbyant/lingbot-world-v2", "steipete/agent-scripts", "ogulcancelik/herdr", "bradautomates/claude-video", "AIDC-AI/Pixelle-Video", "iOfficeAI/OfficeCLI", "vercel-labs/native", "MadsLorentzen/ai-job-search"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 13]},
        'weekly': {"categories": ["Usagi-org/ai-goofish-monitor", "xbtlin/ai-berkshire", "stablyai/orca", "ZhuLinsen/daily_stock_analysis", "bradautomates/claude-video", "elder-plinius/T3MP3ST", "diegosouzapw/OmniRoute", "k1tbyte/Wand-Enhancer", "erincatto/box3d", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "facebook/astryx", "ogulcancelik/herdr", "teamchong/pxpipe", "alibaba/page-agent", "openai/codex-plugin-cc", "Zackriya-Solutions/meetily", "usestrix/strix", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki"], "data": [32, 32, 35, 38, 40, 46, 49, 51, 55, 59, 60, 63, 66, 77, 79, 92, 105, 111, 114, 127]},
        'monthly': {"categories": ["xbtlin/ai-berkshire", "mukul975/Anthropic-Cybersecurity-Skills", "jamiepine/voicebox", "shadcn/improve", "baidu/Unlimited-OCR", "usestrix/strix", "phuryn/pm-skills", "hugohe3/ppt-master", "palmier-io/palmier-pro", "NVIDIA/SkillSpector", "mvanhorn/last30days-skill", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "apple/container", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [193, 199, 208, 217, 224, 242, 246, 270, 291, 302, 324, 330, 376, 498, 540, 616, 647, 701, 914, 1714]}
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
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +13 | 20532 |
| 2 | [vercel-labs/native](https://github.com/vercel-labs/native) | +6 | 5684 |
| 3 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +5 | 14356 |
| 4 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +4 | 25026 |
| 5 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +4 | 7138 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 15175 |
| 7 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +3 | 6268 |
| 8 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +3 | 686 |
| 9 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +3 | 7246 |
| 10 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +3 | 1200 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | +3 | 40069 |
| 12 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2 | 27485 |
| 13 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 29642 |
| 14 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +2 | 7613 |
| 15 | [larksuite/cli](https://github.com/larksuite/cli) | +2 | 15463 |
| 16 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +2 | 1678 |
| 17 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +2 | 10314 |
| 18 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +2 | 366 |
| 19 | [gastownhall/gastown](https://github.com/gastownhall/gastown) | +2 | 16956 |
| 20 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2 | 27464 |
| 21 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +2 | 5908 |
| 22 | [MengTo/Skills](https://github.com/MengTo/Skills) | +2 | 1460 |
| 23 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +2 | 23008 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2 | 8365 |
| 25 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +2 | 12630 |
| 26 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +2 | 4307 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1 | 45395 |
| 28 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +1 | 9986 |
| 29 | [fbsamples/whatsapp-business-jaspers-market](https://github.com/fbsamples/whatsapp-business-jaspers-market) | +1 | 582 |
| 30 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +1 | 36649 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +127 | 10314 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +114 | 20532 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +111 | 40069 |
| 4 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +105 | 22619 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +92 | 27404 |
| 6 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +79 | 25796 |
| 7 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5464 |
| 8 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +66 | 15175 |
| 9 | [facebook/astryx](https://github.com/facebook/astryx) | +63 | 7705 |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +60 | 36649 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +59 | 29642 |
| 12 | [erincatto/box3d](https://github.com/erincatto/box3d) | +55 | 4942 |
| 13 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +51 | 5585 |
| 14 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +49 | 14973 |
| 15 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4307 |
| 16 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +40 | 7138 |
| 17 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +38 | 56492 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +35 | 15887 |
| 19 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +32 | 12630 |
| 20 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +32 | 13498 |
| 21 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +31 | 3810 |
| 22 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +30 | 14356 |
| 23 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +28 | 40436 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +26 | 27659 |
| 25 | [browser-use/video-use](https://github.com/browser-use/video-use) | +26 | 16472 |
| 26 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +25 | 46624 |
| 27 | [Augani/dory](https://github.com/Augani/dory) | +25 | 951 |
| 28 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 27485 |
| 29 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +24 | 22876 |
| 30 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +23 | 10469 |
| 31 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +22 | 22057 |
| 32 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +21 | 51451 |
| 33 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +21 | 8990 |
| 34 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2819 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +20 | 45395 |
| 36 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +19 | 17473 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +19 | 34148 |
| 38 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +19 | 1755 |
| 39 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +19 | 8365 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +19 | 3779 |
| 41 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +19 | 1474 |
| 42 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +18 | 37535 |
| 43 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +18 | 8433 |
| 44 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +18 | 38232 |
| 45 | [baairon/torlink](https://github.com/baairon/torlink) | +18 | 3430 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +17 | 39524 |
| 47 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 37239 |
| 48 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +17 | 19073 |
| 49 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +17 | 752 |
| 50 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +17 | 899 |
| 51 | [Younesfdj/gitfut](https://github.com/Younesfdj/gitfut) | +17 | 1945 |
| 52 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +16 | 1678 |
| 53 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +16 | 9572 |
| 54 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +16 | 1638 |
| 55 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +16 | 24495 |
| 56 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +16 | 7216 |
| 57 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +16 | 2312 |
| 58 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +15 | 12085 |
| 59 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +15 | 3418 |
| 60 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +15 | 25239 |
| 61 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +14 | 7246 |
| 62 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +14 | 4043 |
| 63 | [dotnet/skills](https://github.com/dotnet/skills) | +14 | 4540 |
| 64 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 362 |
| 65 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +14 | 774 |
| 66 | [davidondrej/skills](https://github.com/davidondrej/skills) | +13 | 2221 |
| 67 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +13 | 5620 |
| 68 | [floci-io/floci](https://github.com/floci-io/floci) | +13 | 16184 |
| 69 | [shadcn/improve](https://github.com/shadcn/improve) | +13 | 7607 |
| 70 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 927 |
| 71 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1712 |
| 72 | [alibaba/zvec](https://github.com/alibaba/zvec) | +12 | 14712 |
| 73 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +12 | 5468 |
| 74 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +12 | 25831 |
| 75 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +12 | 8043 |
| 76 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +12 | 17171 |
| 77 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +12 | 38249 |
| 78 | [dorianborian/sesame-robot](https://github.com/dorianborian/sesame-robot) | +12 | 3474 |
| 79 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +11 | 9986 |
| 80 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +11 | 1235 |
| 81 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +11 | 6994 |
| 82 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +11 | 1845 |
| 83 | [decolua/9router](https://github.com/decolua/9router) | +11 | 21632 |
| 84 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +11 | 1050 |
| 85 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 3462 |
| 86 | [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | +11 | 728 |
| 87 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +11 | 13923 |
| 88 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +11 | 632 |
| 89 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +11 | 1092 |
| 90 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +11 | 25166 |
| 91 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 643 |
| 92 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +10 | 31363 |
| 93 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +10 | 1200 |
| 94 | [multica-ai/multica](https://github.com/multica-ai/multica) | +10 | 39802 |
| 95 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +10 | 37851 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +10 | 9148 |
| 97 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +10 | 12758 |
| 98 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +10 | 3112 |
| 99 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +10 | 23445 |
| 100 | [google-research/tabfm](https://github.com/google-research/tabfm) | +10 | 1659 |
| 101 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +10 | 289 |
| 102 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +10 | 8413 |
| 103 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +9 | 17074 |
| 104 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +9 | 29781 |
| 105 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +9 | 11282 |
| 106 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +9 | 1297 |
| 107 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 21794 |
| 108 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +9 | 5960 |
| 109 | [browser-act/skills](https://github.com/browser-act/skills) | +9 | 4266 |
| 110 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 4258 |
| 111 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +8 | 1827 |
| 112 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +8 | 27464 |
| 113 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +8 | 3857 |
| 114 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +8 | 1292 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +8 | 17547 |
| 116 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +8 | 6523 |
| 117 | [vercel-labs/native](https://github.com/vercel-labs/native) | +7 | 5684 |
| 118 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +7 | 8231 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 45100 |
| 120 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +7 | 10740 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1714 | 80092 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +914 | 58370 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +701 | 54425 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +647 | 45195 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +616 | 36649 |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +540 | 29642 |
| 7 | [apple/container](https://github.com/apple/container) | +498 | 47455 |
| 8 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +376 | 11764 |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +330 | 56493 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +324 | 51451 |
| 11 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +302 | 12759 |
| 12 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +291 | 10234 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +270 | 38232 |
| 14 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +246 | 23445 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +242 | 40069 |
| 16 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +224 | 13923 |
| 17 | [shadcn/improve](https://github.com/shadcn/improve) | +217 | 7607 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +208 | 40436 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +199 | 25240 |
| 20 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +193 | 12630 |
| 21 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +191 | 27485 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +189 | 27659 |
| 23 | [stablyai/orca](https://github.com/stablyai/orca) | +186 | 15887 |
| 24 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +186 | 27543 |
| 25 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +183 | 15175 |
| 26 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +182 | 37239 |
| 27 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +180 | 34148 |
| 28 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 6994 |
| 29 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +178 | 6617 |
| 30 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +177 | 35412 |
| 31 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 8043 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +176 | 15770 |
| 33 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +176 | 24495 |
| 34 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +172 | 10314 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +171 | 45395 |
| 36 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7816 |
| 37 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +161 | 37851 |
| 38 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +159 | 6431 |
| 39 | [google-research/timesfm](https://github.com/google-research/timesfm) | +159 | 26722 |
| 40 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +149 | 12085 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +146 | 27404 |
| 42 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +145 | 18362 |
| 43 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +141 | 19073 |
| 44 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +140 | 25796 |
| 45 | [facebook/astryx](https://github.com/facebook/astryx) | +138 | 7705 |
| 46 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +132 | 17171 |
| 47 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +131 | 39524 |
| 48 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +129 | 22619 |
| 49 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +127 | 20532 |
| 50 | [erincatto/box3d](https://github.com/erincatto/box3d) | +124 | 4942 |
| 51 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +124 | 10363 |
| 52 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +120 | 23025 |
| 53 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +117 | 7885 |
| 54 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +116 | 14973 |
| 55 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +116 | 62405 |
| 56 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +116 | 18529 |
| 57 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 58 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +112 | 37535 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +109 | 28609 |
| 60 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +109 | 33041 |
| 61 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +109 | 25988 |
| 62 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +107 | 3857 |
| 63 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +107 | 5811 |
| 64 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4316 |
| 65 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +100 | 25831 |
| 66 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +99 | 11282 |
| 67 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +98 | 8413 |
| 68 | [browser-use/video-use](https://github.com/browser-use/video-use) | +94 | 16472 |
| 69 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +94 | 34610 |
| 70 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +93 | 27464 |
| 71 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +93 | 39623 |
| 72 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +89 | 31363 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +88 | 25058 |
| 74 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 9986 |
| 75 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +87 | 10740 |
| 76 | [alibaba/zvec](https://github.com/alibaba/zvec) | +86 | 14712 |
| 77 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +84 | 21231 |
| 78 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +83 | 4043 |
| 79 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +83 | 25026 |
| 80 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +83 | 26949 |
| 81 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +82 | 46624 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +81 | 39802 |
| 83 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +81 | 8054 |
| 84 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6523 |
| 85 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +80 | 7458 |
| 86 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +79 | 32035 |
| 87 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +78 | 5464 |
| 88 | [antirez/ds4](https://github.com/antirez/ds4) | +78 | 18150 |
| 89 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +78 | 8230 |
| 90 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +76 | 21794 |
| 91 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +76 | 5620 |
| 92 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +75 | 14356 |
| 93 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +74 | 28034 |
| 94 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +71 | 22520 |
| 95 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +70 | 3419 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +70 | 30637 |
| 97 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +69 | 10469 |
| 98 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +69 | 5468 |
| 99 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +68 | 26727 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +67 | 22057 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +67 | 49728 |
| 102 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +66 | 3779 |
| 103 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +66 | 9148 |
| 104 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 7216 |
| 105 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +63 | 22876 |
| 106 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3592 |
| 107 | [decolua/9router](https://github.com/decolua/9router) | +62 | 21632 |
| 108 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +62 | 4453 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +61 | 45100 |
| 110 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +61 | 16840 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +59 | 31952 |
| 112 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +58 | 7138 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +58 | 42805 |
| 114 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +58 | 33352 |
| 115 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +58 | 27366 |
| 116 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2630 |
| 117 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +57 | 5585 |
| 118 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +56 | 6326 |
| 119 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +54 | 5676 |
| 120 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +54 | 36103 |
| 121 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +52 | 14168 |
| 122 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +51 | 3810 |
| 123 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +51 | 26429 |
| 124 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +50 | 25166 |
| 125 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +50 | 9434 |
| 126 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +49 | 25988 |
| 127 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +48 | 10955 |
| 128 | [anbeime/skill](https://github.com/anbeime/skill) | +48 | 3443 |
| 129 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +47 | 19674 |
| 130 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4307 |
| 131 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +46 | 5278 |
| 132 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +46 | 7960 |
| 133 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +46 | 2530 |
| 134 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +45 | 4362 |
| 135 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +43 | 13498 |
| 136 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3022 |
| 137 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 138 | [openai/skills](https://github.com/openai/skills) | +41 | 23491 |
| 139 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +41 | 1596 |
| 140 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +41 | 12127 |
| 141 | [openai/plugins](https://github.com/openai/plugins) | +41 | 4281 |
| 142 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1659 |
| 143 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +39 | 4258 |
| 144 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +39 | 17547 |
| 145 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +39 | 5960 |
| 146 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1358 |
| 147 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1845 |
| 148 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +37 | 3406 |
| 149 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +36 | 15791 |
| 150 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +36 | 18215 |
| 151 | [google/skills](https://github.com/google/skills) | +36 | 14498 |
| 152 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +36 | 26313 |
| 153 | [jundot/omlx](https://github.com/jundot/omlx) | +34 | 17729 |
| 154 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2787 |
| 155 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +34 | 3936 |
| 156 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +33 | 2004 |
| 157 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +33 | 26552 |
| 158 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2062 |
| 159 | [floci-io/floci](https://github.com/floci-io/floci) | +33 | 16184 |
| 160 | [browser-act/skills](https://github.com/browser-act/skills) | +32 | 4266 |
| 161 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +32 | 8231 |
| 162 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1910 |
| 163 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +32 | 15869 |
| 164 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +32 | 6127 |
| 165 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +31 | 5731 |
| 166 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1245 |
| 167 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +30 | 26063 |
| 168 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +30 | 18033 |
| 169 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +30 | 8325 |
| 170 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1168 |
| 171 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +29 | 1627 |
| 172 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +29 | 8166 |
| 173 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1087 |
| 174 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +29 | 3222 |
| 175 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +29 | 1463 |
| 176 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 1876 |
| 177 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1265 |
| 178 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +28 | 3929 |
| 179 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 611 |
| 180 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 909 |
| 181 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2415 |
| 182 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +27 | 6726 |
| 183 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +26 | 3462 |
| 184 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15054 |
| 185 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +25 | 7599 |
| 186 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 899 |
| 187 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +24 | 1789 |
| 188 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +24 | 5657 |
| 189 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +24 | 7548 |
| 190 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 441 |
| 191 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1474 |
| 192 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +23 | 2257 |
| 193 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 623 |
| 194 | [rpamis/comet](https://github.com/rpamis/comet) | +20 | 2155 |
| 195 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +19 | 28909 |
| 196 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +19 | 1310 |
| 197 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +19 | 2436 |
| 198 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +19 | 5259 |
| 199 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +19 | 8797 |
| 200 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +18 | 2314 |
| 201 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +18 | 973 |
| 202 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 725 |
| 203 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 642 |
| 204 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +17 | 11742 |
| 205 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +17 | 669 |
| 206 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +16 | 1678 |
| 207 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +16 | 2738 |
| 208 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +15 | 894 |
| 209 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1424 |
| 210 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4307 |
| 211 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +14 | 6025 |
| 212 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 505 |
| 213 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 476 |
| 214 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 215 | [eze-is/web-access](https://github.com/eze-is/web-access) | +13 | 8179 |
| 216 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 417 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +13 | 4384 |
| 218 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +13 | 2801 |
| 219 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 475 |
| 220 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 14008 |
| 221 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +12 | 8883 |
| 222 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 328 |
| 223 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +12 | 3093 |
| 224 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +11 | 5730 |
| 225 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +11 | 0 |
| 226 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +11 | 555 |
| 227 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 681 |
| 228 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 348 |
| 229 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 472 |
| 230 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 341 |
| 231 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 801 |
| 232 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 425 |
| 233 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +10 | 761 |
| 234 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 424 |
| 235 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +10 | 2279 |
| 236 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 203 |
| 237 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 363 |
| 238 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +10 | 485 |
| 239 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2762 |
| 240 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 1930 |
| 241 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +9 | 4989 |
| 242 | [robinebers/openusage](https://github.com/robinebers/openusage) | +9 | 3204 |
| 243 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3962 |
| 244 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 240 |
| 245 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +8 | 1306 |
| 246 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 595 |
| 247 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 368 |
| 248 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +8 | 1702 |
| 249 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 250 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +8 | 1172 |
| 251 | [Spanky96/glm-coding-grabber](https://github.com/Spanky96/glm-coding-grabber) | +8 | 464 |
| 252 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +8 | 852 |
| 253 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +8 | 2782 |
| 254 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +7 | 1509 |
| 255 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 160 |
| 256 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 971 |
| 257 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 328 |
| 258 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 250 |
| 259 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +7 | 3667 |
| 260 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 454 |
| 261 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 377 |
| 262 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 628 |
| 263 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 179 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +6 | 1791 |
| 265 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 205 |
| 266 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +5 | 406 |
| 267 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 319 |
| 268 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 516 |
| 269 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2560 |
| 270 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 83 |
| 271 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9500 |
| 272 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 308 |
| 273 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +5 | 748 |
| 274 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 118 |
| 275 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2664 |
| 276 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2337 |
| 277 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +4 | 647 |
| 278 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 279 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 101 |
| 280 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 185 |
| 281 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 78 |
| 282 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 397 |
| 283 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 117 |
| 284 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 626 |
| 285 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 222 |
| 286 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 537 |
| 287 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 288 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 289 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 612 |
| 290 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 220 |
| 291 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 820 |
| 292 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1684 |
| 293 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3341 |
| 294 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 295 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 412 |
| 296 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 144 |
| 297 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 852 |
| 298 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
| 299 | [itwanger/PaiAgent](https://github.com/itwanger/PaiAgent) | +2 | 560 |
| 300 | [Angais/minedit](https://github.com/Angais/minedit) | +2 | 136 |
