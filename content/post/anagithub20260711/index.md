---
title: "2026-07-11 GitHub增长趋势报告"
description: "1.skills+6 2.openwiki+3 3.ai-job-search+3 4.destructive_command_guard+3 5.DNSHE-FreeDomains+2"
date: 2026-07-11T20:50:40+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-11 20:50:40

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
        'daily': {"categories": ["shadcn/improve", "PDFCraftTool/pdfcraft", "x4gKing/3x-ui-Upgrade", "yayuuu/hyprland-scroll-overview", "stablyai/orca", "OluOlus/ops-agent-controller", "imchine/FinTech-Wallet", "altic-dev/FluidVoice", "mauriceboe/TREK", "JCodesMore/ai-website-cloner-template", "usestrix/strix", "bradautomates/claude-video", "interviewstreet/hiring-agent", "AprilNEA/OpenLogi", "alibaba/page-agent", "dnshe/DNSHE-FreeDomains", "Dicklesworthstone/destructive_command_guard", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki", "emilkowalski/skills"], "data": [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 6]},
        'weekly': {"categories": ["stablyai/orca", "xbtlin/ai-berkshire", "ZhuLinsen/daily_stock_analysis", "iOfficeAI/OfficeCLI", "Usagi-org/ai-goofish-monitor", "facebook/astryx", "DeusData/codebase-memory-mcp", "diegosouzapw/OmniRoute", "bradautomates/claude-video", "ogulcancelik/herdr", "calesthio/OpenMontage", "elder-plinius/T3MP3ST", "k1tbyte/Wand-Enhancer", "alibaba/page-agent", "teamchong/pxpipe", "openai/codex-plugin-cc", "usestrix/strix", "Zackriya-Solutions/meetily", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki"], "data": [23, 25, 30, 30, 32, 32, 38, 38, 41, 46, 46, 46, 47, 48, 53, 72, 73, 93, 94, 117]},
        'monthly': {"categories": ["JCodesMore/ai-website-cloner-template", "shadcn/improve", "mukul975/Anthropic-Cybersecurity-Skills", "xbtlin/ai-berkshire", "jamiepine/voicebox", "baidu/Unlimited-OCR", "usestrix/strix", "hugohe3/ppt-master", "XiaomiMiMo/MiMo-Code", "palmier-io/palmier-pro", "NVIDIA/SkillSpector", "mvanhorn/last30days-skill", "ZhuLinsen/daily_stock_analysis", "apple/container", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [191, 193, 193, 193, 206, 224, 243, 253, 285, 292, 295, 296, 320, 444, 539, 615, 627, 687, 882, 1717]}
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
| 1 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 9751 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 10549 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 21052 |
| 4 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +3 | 2128 |
| 5 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 5212 |
| 6 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2 | 26027 |
| 7 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +2 | 6334 |
| 8 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +2 | 5556 |
| 9 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 7520 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | +2 | 40514 |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2 | 27770 |
| 12 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +2 | 10083 |
| 13 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +2 | 7427 |
| 14 | [imchine/FinTech-Wallet](https://github.com/imchine/FinTech-Wallet) | +2 | 152 |
| 15 | [OluOlus/ops-agent-controller](https://github.com/OluOlus/ops-agent-controller) | +2 | 667 |
| 16 | [stablyai/orca](https://github.com/stablyai/orca) | +2 | 16326 |
| 17 | [yayuuu/hyprland-scroll-overview](https://github.com/yayuuu/hyprland-scroll-overview) | +2 | 257 |
| 18 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +1 | 783 |
| 19 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +1 | 7482 |
| 20 | [shadcn/improve](https://github.com/shadcn/improve) | +1 | 7785 |
| 21 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +1 | 29839 |
| 22 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +1 | 5298 |
| 23 | [yami-inc/ai-death-game](https://github.com/yami-inc/ai-death-game) | +1 | 30 |
| 24 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +1 | 7536 |
| 25 | [android/skills](https://github.com/android/skills) | +1 | 6141 |
| 26 | [Soju06/codex-lb](https://github.com/Soju06/codex-lb) | +1 | 2258 |
| 27 | [Studio-Saelix/sencho](https://github.com/Studio-Saelix/sencho) | +1 | 222 |
| 28 | [Tubo2333/obsidian-knowledge-brain](https://github.com/Tubo2333/obsidian-knowledge-brain) | +1 | 74 |
| 29 | [prehisle/relay-pulse](https://github.com/prehisle/relay-pulse) | +1 | 1056 |
| 30 | [jayin92/Skyfall-GS](https://github.com/jayin92/Skyfall-GS) | +1 | 926 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +117 | 10549 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +94 | 21052 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +93 | 23131 |
| 4 | [usestrix/strix](https://github.com/usestrix/strix) | +73 | 40514 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +72 | 27638 |
| 6 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +53 | 5571 |
| 7 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +48 | 26027 |
| 8 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +47 | 6254 |
| 9 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4422 |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +46 | 37086 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +46 | 15484 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +41 | 7520 |
| 13 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +38 | 15643 |
| 14 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +38 | 30091 |
| 15 | [facebook/astryx](https://github.com/facebook/astryx) | +32 | 7898 |
| 16 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +32 | 13539 |
| 17 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +30 | 15028 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +30 | 56675 |
| 19 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +25 | 12753 |
| 20 | [stablyai/orca](https://github.com/stablyai/orca) | +23 | 16326 |
| 21 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +22 | 3886 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +21 | 27834 |
| 23 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +20 | 27770 |
| 24 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +20 | 46690 |
| 25 | [Augani/dory](https://github.com/Augani/dory) | +20 | 961 |
| 26 | [erincatto/box3d](https://github.com/erincatto/box3d) | +19 | 5032 |
| 27 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +18 | 22201 |
| 28 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +18 | 40662 |
| 29 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1759 |
| 30 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +17 | 37664 |
| 31 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +17 | 17675 |
| 32 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +17 | 10515 |
| 33 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +17 | 791 |
| 34 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +16 | 51584 |
| 35 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 37344 |
| 36 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +16 | 1656 |
| 37 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +16 | 7427 |
| 38 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +16 | 8437 |
| 39 | [browser-use/video-use](https://github.com/browser-use/video-use) | +16 | 16606 |
| 40 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +16 | 2826 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +15 | 45671 |
| 42 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +15 | 12207 |
| 43 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +15 | 1809 |
| 44 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +15 | 22911 |
| 45 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +14 | 7351 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +14 | 34307 |
| 47 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +14 | 9107 |
| 48 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 368 |
| 49 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +14 | 2327 |
| 50 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +13 | 9751 |
| 51 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +13 | 5556 |
| 52 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +13 | 39639 |
| 53 | [davidondrej/skills](https://github.com/davidondrej/skills) | +13 | 2285 |
| 54 | [floci-io/floci](https://github.com/floci-io/floci) | +13 | 16343 |
| 55 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +13 | 934 |
| 56 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1718 |
| 57 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +12 | 19628 |
| 58 | [baairon/torlink](https://github.com/baairon/torlink) | +12 | 3470 |
| 59 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +12 | 4090 |
| 60 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 38395 |
| 61 | [dotnet/skills](https://github.com/dotnet/skills) | +12 | 4573 |
| 62 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +11 | 10083 |
| 63 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +11 | 9689 |
| 64 | [alibaba/zvec](https://github.com/alibaba/zvec) | +11 | 14750 |
| 65 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +11 | 5654 |
| 66 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +11 | 25315 |
| 67 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 3496 |
| 68 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +11 | 659 |
| 69 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +10 | 29839 |
| 70 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +10 | 9197 |
| 71 | [multica-ai/multica](https://github.com/multica-ai/multica) | +10 | 39880 |
| 72 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +10 | 12883 |
| 73 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +10 | 1377 |
| 74 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +10 | 37975 |
| 75 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +10 | 3661 |
| 76 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +10 | 24658 |
| 77 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +10 | 25837 |
| 78 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +10 | 1845 |
| 79 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +10 | 3131 |
| 80 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +10 | 1512 |
| 81 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 519 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +9 | 31497 |
| 83 | [shadcn/improve](https://github.com/shadcn/improve) | +9 | 7786 |
| 84 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +9 | 1339 |
| 85 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 21938 |
| 86 | [gastownhall/gastown](https://github.com/gastownhall/gastown) | +9 | 16973 |
| 87 | [decolua/9router](https://github.com/decolua/9router) | +9 | 21750 |
| 88 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +9 | 8471 |
| 89 | [google-research/tabfm](https://github.com/google-research/tabfm) | +9 | 1696 |
| 90 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +8 | 1899 |
| 91 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +8 | 1308 |
| 92 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +8 | 1058 |
| 93 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +8 | 23514 |
| 94 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +8 | 7077 |
| 95 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 6014 |
| 96 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +8 | 1313 |
| 97 | [vercel-labs/native](https://github.com/vercel-labs/native) | +7 | 5793 |
| 98 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 3900 |
| 99 | [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1) | +7 | 1474 |
| 100 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +7 | 14018 |
| 101 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +7 | 8277 |
| 102 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +7 | 1110 |
| 103 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +7 | 306 |
| 104 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 1826 |
| 105 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +6 | 6325 |
| 106 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +6 | 27532 |
| 107 | [smittix/intercept](https://github.com/smittix/intercept) | +6 | 2068 |
| 108 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +6 | 39659 |
| 109 | [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course) | +6 | 7753 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +6 | 17599 |
| 111 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +6 | 6540 |
| 112 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +5 | 17127 |
| 113 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +5 | 787 |
| 114 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +5 | 25113 |
| 115 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +5 | 33129 |
| 116 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +5 | 26583 |
| 117 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 2412 |
| 118 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 30693 |
| 119 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +5 | 11060 |
| 120 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +5 | 1395 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1717 | 80711 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +882 | 58558 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +687 | 54890 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +627 | 45255 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +615 | 37086 |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +539 | 30091 |
| 7 | [apple/container](https://github.com/apple/container) | +444 | 47562 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +320 | 56675 |
| 9 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +296 | 51584 |
| 10 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +295 | 12883 |
| 11 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +292 | 10273 |
| 12 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +285 | 11814 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +253 | 38395 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | +243 | 40513 |
| 15 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +224 | 14018 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +206 | 40662 |
| 17 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +193 | 12753 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +193 | 25315 |
| 19 | [shadcn/improve](https://github.com/shadcn/improve) | +193 | 7786 |
| 20 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +191 | 27770 |
| 21 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +191 | 23514 |
| 22 | [stablyai/orca](https://github.com/stablyai/orca) | +189 | 16326 |
| 23 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +186 | 27580 |
| 24 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +181 | 15484 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +179 | 27834 |
| 26 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 7077 |
| 27 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +178 | 6719 |
| 28 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 8116 |
| 29 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +175 | 10549 |
| 30 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +169 | 37344 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +168 | 34307 |
| 32 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +168 | 35470 |
| 33 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +167 | 24658 |
| 34 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7831 |
| 35 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +164 | 15833 |
| 36 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +159 | 6503 |
| 37 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26763 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +157 | 45671 |
| 39 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +151 | 37975 |
| 40 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +145 | 12207 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +144 | 27638 |
| 42 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18421 |
| 43 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +141 | 26027 |
| 44 | [facebook/astryx](https://github.com/facebook/astryx) | +138 | 7898 |
| 45 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +136 | 19628 |
| 46 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +130 | 23131 |
| 47 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +129 | 39639 |
| 48 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5032 |
| 49 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +125 | 17301 |
| 50 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +123 | 21052 |
| 51 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +121 | 10417 |
| 52 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +117 | 23112 |
| 53 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +116 | 8104 |
| 54 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +115 | 15643 |
| 55 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 56 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +112 | 62446 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +110 | 37664 |
| 58 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +109 | 26029 |
| 59 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +107 | 3870 |
| 60 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +106 | 5908 |
| 61 | [blader/humanizer](https://github.com/blader/humanizer) | +105 | 28736 |
| 62 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +103 | 33129 |
| 63 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4369 |
| 64 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +99 | 11519 |
| 65 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +94 | 8471 |
| 66 | [browser-use/video-use](https://github.com/browser-use/video-use) | +92 | 16606 |
| 67 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +92 | 25905 |
| 68 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +89 | 34660 |
| 69 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +89 | 18552 |
| 70 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +88 | 25119 |
| 71 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10083 |
| 72 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +87 | 10803 |
| 73 | [alibaba/zvec](https://github.com/alibaba/zvec) | +87 | 14750 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +86 | 27532 |
| 75 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +84 | 31497 |
| 76 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +83 | 4090 |
| 77 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +82 | 46690 |
| 78 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +81 | 25113 |
| 79 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6540 |
| 80 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +80 | 21278 |
| 81 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +80 | 27003 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +79 | 39880 |
| 83 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +79 | 8082 |
| 84 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5571 |
| 85 | [antirez/ds4](https://github.com/antirez/ds4) | +77 | 18234 |
| 86 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +77 | 39659 |
| 87 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +77 | 5654 |
| 88 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +77 | 32069 |
| 89 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +76 | 21938 |
| 90 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +71 | 5556 |
| 91 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +70 | 15028 |
| 92 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +70 | 3661 |
| 93 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +70 | 25837 |
| 94 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +70 | 28069 |
| 95 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +68 | 10515 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +67 | 9197 |
| 97 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +67 | 30693 |
| 98 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +66 | 3900 |
| 99 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +66 | 7427 |
| 100 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +66 | 26820 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +65 | 22201 |
| 102 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +65 | 22534 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +64 | 49813 |
| 104 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +63 | 9751 |
| 105 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +62 | 22911 |
| 106 | [decolua/9router](https://github.com/decolua/9router) | +61 | 21750 |
| 107 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +61 | 45151 |
| 108 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +60 | 7520 |
| 109 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +60 | 3601 |
| 110 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +59 | 16870 |
| 111 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2649 |
| 112 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +57 | 6254 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +57 | 42890 |
| 114 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +57 | 33395 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +57 | 31986 |
| 116 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +57 | 27401 |
| 117 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +54 | 5753 |
| 118 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +51 | 3886 |
| 119 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +51 | 6395 |
| 120 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +51 | 36103 |
| 121 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +50 | 25204 |
| 122 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +50 | 4485 |
| 123 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +49 | 9474 |
| 124 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +49 | 26485 |
| 125 | [anbeime/skill](https://github.com/anbeime/skill) | +48 | 3482 |
| 126 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +47 | 11060 |
| 127 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +47 | 26046 |
| 128 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4422 |
| 129 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +46 | 19724 |
| 130 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +45 | 8010 |
| 131 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +44 | 2538 |
| 132 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +43 | 13539 |
| 133 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3028 |
| 134 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 135 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +41 | 1618 |
| 136 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1696 |
| 137 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +40 | 6014 |
| 138 | [openai/skills](https://github.com/openai/skills) | +40 | 23542 |
| 139 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +40 | 12160 |
| 140 | [openai/plugins](https://github.com/openai/plugins) | +40 | 4374 |
| 141 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +39 | 4387 |
| 142 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +38 | 4321 |
| 143 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +38 | 17599 |
| 144 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1357 |
| 145 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +38 | 5307 |
| 146 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1845 |
| 147 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +37 | 3446 |
| 148 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +36 | 26331 |
| 149 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +35 | 2952 |
| 150 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +34 | 15877 |
| 151 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +34 | 18241 |
| 152 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2809 |
| 153 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +33 | 2020 |
| 154 | [jundot/omlx](https://github.com/jundot/omlx) | +33 | 17758 |
| 155 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2064 |
| 156 | [browser-act/skills](https://github.com/browser-act/skills) | +32 | 4285 |
| 157 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1926 |
| 158 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +32 | 15886 |
| 159 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +32 | 3941 |
| 160 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +31 | 5747 |
| 161 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +30 | 8277 |
| 162 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1249 |
| 163 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +30 | 26102 |
| 164 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +30 | 26583 |
| 165 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +30 | 6185 |
| 166 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +30 | 8339 |
| 167 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1189 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +29 | 8232 |
| 169 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1098 |
| 170 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +29 | 3238 |
| 171 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +29 | 1486 |
| 172 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +29 | 18060 |
| 173 | [floci-io/floci](https://github.com/floci-io/floci) | +29 | 16343 |
| 174 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +28 | 1632 |
| 175 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 19431 |
| 176 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 1900 |
| 177 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +28 | 6760 |
| 178 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1269 |
| 179 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +28 | 3965 |
| 180 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 619 |
| 181 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2432 |
| 182 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15075 |
| 183 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +25 | 3496 |
| 184 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +25 | 913 |
| 185 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 934 |
| 186 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +24 | 1813 |
| 187 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +24 | 5683 |
| 188 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 441 |
| 189 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1512 |
| 190 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +23 | 7728 |
| 191 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +23 | 7578 |
| 192 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 623 |
| 193 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +21 | 2279 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +19 | 28945 |
| 195 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +19 | 1311 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +19 | 5277 |
| 197 | [rpamis/comet](https://github.com/rpamis/comet) | +19 | 2179 |
| 198 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +18 | 2459 |
| 199 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +18 | 8825 |
| 200 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +18 | 978 |
| 201 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1759 |
| 202 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 745 |
| 203 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 646 |
| 204 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +17 | 2366 |
| 205 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +15 | 1004 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +15 | 11757 |
| 207 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2766 |
| 208 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1427 |
| 209 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +15 | 675 |
| 210 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4325 |
| 211 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 508 |
| 212 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 476 |
| 213 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +13 | 6033 |
| 214 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 215 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +13 | 329 |
| 216 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 427 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +13 | 4401 |
| 218 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 479 |
| 219 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 14018 |
| 220 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +11 | 5745 |
| 221 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +11 | 564 |
| 222 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 683 |
| 223 | [eze-is/web-access](https://github.com/eze-is/web-access) | +11 | 8193 |
| 224 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +11 | 8884 |
| 225 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 351 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +11 | 3102 |
| 227 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2817 |
| 228 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 828 |
| 229 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 519 |
| 230 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 344 |
| 231 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 425 |
| 232 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +10 | 0 |
| 233 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 443 |
| 234 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +10 | 2297 |
| 235 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 202 |
| 236 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 381 |
| 237 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2776 |
| 238 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 1933 |
| 239 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +9 | 765 |
| 240 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +9 | 4991 |
| 241 | [robinebers/openusage](https://github.com/robinebers/openusage) | +9 | 3217 |
| 242 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +9 | 486 |
| 243 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3976 |
| 244 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 240 |
| 245 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +8 | 1313 |
| 246 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 640 |
| 247 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 371 |
| 248 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 249 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +8 | 1711 |
| 250 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +8 | 1174 |
| 251 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +8 | 855 |
| 252 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +8 | 2789 |
| 253 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 161 |
| 254 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 973 |
| 255 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +7 | 342 |
| 256 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 328 |
| 257 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 250 |
| 258 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +7 | 3673 |
| 259 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 454 |
| 260 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 430 |
| 261 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1519 |
| 262 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 628 |
| 263 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 180 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +6 | 1795 |
| 265 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +5 | 411 |
| 266 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 331 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 529 |
| 268 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2564 |
| 269 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 85 |
| 270 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9501 |
| 271 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 312 |
| 272 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +5 | 753 |
| 273 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 118 |
| 274 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2673 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2344 |
| 276 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 277 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +4 | 204 |
| 278 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 185 |
| 279 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 81 |
| 280 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 398 |
| 281 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 117 |
| 282 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 164 |
| 283 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 636 |
| 284 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +3 | 652 |
| 285 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 224 |
| 286 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 539 |
| 287 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 845 |
| 288 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +3 | 102 |
| 289 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 615 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 228 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 821 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1684 |
| 294 | [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | +2 | 215 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3348 |
| 296 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 297 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 418 |
| 298 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 146 |
| 299 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 853 |
| 300 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
