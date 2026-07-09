---
title: "2026-07-09 GitHub增长趋势报告"
description: "1.ai-job-search+8 2.mellea+6 3.claude-video+6 4.herdr+6 5.OpenMontage+5"
date: 2026-07-09T21:25:02+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-09 21:25:02

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
        'daily': {"categories": ["shepherd-agents/shepherd", "chriswritescode-dev/opencode-manager", "kyutai-labs/pocket-tts", "K-Dense-AI/scientific-agent-skills", "Astro-Han/karpathy-llm-wiki", "mvanhorn/last30days-skill", "openai/codex-plugin-cc", "Shpigford/knockoff", "stablyai/orca", "paullarionov/claude-certified-architect", "TencentCloud/CubeSandbox", "microsoft/flint-chart", "ZhuLinsen/daily_stock_analysis", "Wei-Shaw/sub2api", "JCodesMore/ai-website-cloner-template", "calesthio/OpenMontage", "ogulcancelik/herdr", "bradautomates/claude-video", "generative-computing/mellea", "MadsLorentzen/ai-job-search"], "data": [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 8]},
        'weekly': {"categories": ["bradautomates/claude-video", "jamiepine/voicebox", "browser-use/video-use", "stablyai/orca", "elder-plinius/T3MP3ST", "k1tbyte/Wand-Enhancer", "ZhuLinsen/daily_stock_analysis", "diegosouzapw/OmniRoute", "DeusData/codebase-memory-mcp", "erincatto/box3d", "ogulcancelik/herdr", "teamchong/pxpipe", "calesthio/OpenMontage", "facebook/astryx", "alibaba/page-agent", "openai/codex-plugin-cc", "MadsLorentzen/ai-job-search", "Zackriya-Solutions/meetily", "langchain-ai/openwiki", "usestrix/strix"], "data": [38, 40, 41, 43, 44, 46, 48, 54, 69, 70, 74, 76, 77, 80, 90, 101, 102, 112, 141, 157]},
        'monthly': {"categories": ["Yuan1z0825/nature-skills", "mukul975/Anthropic-Cybersecurity-Skills", "jamiepine/voicebox", "shadcn/improve", "baidu/Unlimited-OCR", "usestrix/strix", "phuryn/pm-skills", "hugohe3/ppt-master", "palmier-io/palmier-pro", "NVIDIA/SkillSpector", "ZhuLinsen/daily_stock_analysis", "XiaomiMiMo/MiMo-Code", "mvanhorn/last30days-skill", "apple/container", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "elder-plinius/CL4R1T4S", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [197, 200, 207, 217, 223, 239, 257, 280, 291, 310, 334, 376, 394, 540, 540, 616, 656, 715, 954, 1711]}
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
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +8 | 18639 |
| 2 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +6 | 1712 |
| 3 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 6623 |
| 4 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +6 | 14780 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +5 | 36124 |
| 6 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 27175 |
| 7 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +4 | 31102 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 56207 |
| 9 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +3 | 893 |
| 10 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +3 | 9314 |
| 11 | [paullarionov/claude-certified-architect](https://github.com/paullarionov/claude-certified-architect) | +3 | 3620 |
| 12 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 14999 |
| 13 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +3 | 1551 |
| 14 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2 | 27141 |
| 15 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2 | 51193 |
| 16 | [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | +2 | 1459 |
| 17 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +2 | 30578 |
| 18 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +2 | 6934 |
| 19 | [chriswritescode-dev/opencode-manager](https://github.com/chriswritescode-dev/opencode-manager) | +2 | 810 |
| 20 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +2 | 1235 |
| 21 | [halilkirazkaya/arsenal-ng](https://github.com/halilkirazkaya/arsenal-ng) | +2 | 476 |
| 22 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 10893 |
| 23 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 37420 |
| 24 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +2 | 1849 |
| 25 | [erincatto/box3d](https://github.com/erincatto/box3d) | +2 | 4832 |
| 26 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 29116 |
| 27 | [usestrix/strix](https://github.com/usestrix/strix) | +2 | 39577 |
| 28 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +2 | 8835 |
| 29 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +2 | 11936 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +2 | 27434 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +157 | 39577 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +141 | 10068 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +112 | 22169 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +102 | 18639 |
| 5 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +101 | 27141 |
| 6 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +90 | 25485 |
| 7 | [facebook/astryx](https://github.com/facebook/astryx) | +80 | 7452 |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +77 | 36124 |
| 9 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +76 | 5273 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +74 | 14780 |
| 11 | [erincatto/box3d](https://github.com/erincatto/box3d) | +70 | 4832 |
| 12 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +69 | 29116 |
| 13 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +54 | 14238 |
| 14 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +48 | 56207 |
| 15 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +46 | 5092 |
| 16 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +44 | 4145 |
| 17 | [stablyai/orca](https://github.com/stablyai/orca) | +43 | 14999 |
| 18 | [browser-use/video-use](https://github.com/browser-use/video-use) | +41 | 16244 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +40 | 39974 |
| 20 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +38 | 6623 |
| 21 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +36 | 46497 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +34 | 12333 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 18896 |
| 24 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +31 | 13446 |
| 25 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +31 | 3657 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 27434 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +29 | 27175 |
| 28 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +28 | 13315 |
| 29 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +27 | 10362 |
| 30 | [baairon/torlink](https://github.com/baairon/torlink) | +26 | 3383 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +26 | 38014 |
| 32 | [Augani/dory](https://github.com/Augani/dory) | +25 | 932 |
| 33 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +25 | 8835 |
| 34 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +25 | 11193 |
| 35 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 21853 |
| 36 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +24 | 51193 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +23 | 45053 |
| 38 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +23 | 1624 |
| 39 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +21 | 2812 |
| 40 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +21 | 4010 |
| 41 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +21 | 33984 |
| 42 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +21 | 6708 |
| 43 | [Younesfdj/gitfut](https://github.com/Younesfdj/gitfut) | +21 | 1890 |
| 44 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +20 | 17348 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +20 | 37420 |
| 46 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +20 | 3639 |
| 47 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 37115 |
| 48 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +19 | 8412 |
| 49 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +19 | 25103 |
| 50 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +18 | 39358 |
| 51 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +18 | 6996 |
| 52 | [Gitlawb/zero](https://github.com/Gitlawb/zero) | +18 | 1034 |
| 53 | [ctxrs/ctx](https://github.com/ctxrs/ctx) | +18 | 754 |
| 54 | [modiqo/cliare](https://github.com/modiqo/cliare) | +18 | 711 |
| 55 | [modiqo/skillspec](https://github.com/modiqo/skillspec) | +18 | 910 |
| 56 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +17 | 9314 |
| 57 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +17 | 863 |
| 58 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +17 | 24109 |
| 59 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +17 | 3228 |
| 60 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +17 | 684 |
| 61 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +17 | 2264 |
| 62 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +16 | 1614 |
| 63 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +16 | 5303 |
| 64 | [google-research/tabfm](https://github.com/google-research/tabfm) | +16 | 1621 |
| 65 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 270 |
| 66 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +16 | 8339 |
| 67 | [decolua/9router](https://github.com/decolua/9router) | +15 | 21389 |
| 68 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +15 | 1847 |
| 69 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +15 | 7974 |
| 70 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +15 | 17006 |
| 71 | [shadcn/improve](https://github.com/shadcn/improve) | +15 | 7559 |
| 72 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +15 | 9726 |
| 73 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +14 | 1551 |
| 74 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +14 | 31102 |
| 75 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 11936 |
| 76 | [multica-ai/multica](https://github.com/multica-ai/multica) | +14 | 39651 |
| 77 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +14 | 25734 |
| 78 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 357 |
| 79 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +14 | 13815 |
| 80 | [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) | +14 | 709 |
| 81 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +14 | 3409 |
| 82 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +14 | 1055 |
| 83 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +13 | 1712 |
| 84 | [davidondrej/skills](https://github.com/davidondrej/skills) | +13 | 2048 |
| 85 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +13 | 5566 |
| 86 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +13 | 3834 |
| 87 | [floci-io/floci](https://github.com/floci-io/floci) | +13 | 15949 |
| 88 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 6921 |
| 89 | [dotnet/skills](https://github.com/dotnet/skills) | +13 | 4479 |
| 90 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +13 | 38181 |
| 91 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +13 | 25120 |
| 92 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 815 |
| 93 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +13 | 5559 |
| 94 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +12 | 1030 |
| 95 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +12 | 1849 |
| 96 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +12 | 12608 |
| 97 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 9097 |
| 98 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 6934 |
| 99 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 37747 |
| 100 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +11 | 1108 |
| 101 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +11 | 21655 |
| 102 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +11 | 618 |
| 103 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +11 | 635 |
| 104 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +10 | 16972 |
| 105 | [browser-act/skills](https://github.com/browser-act/skills) | +10 | 4223 |
| 106 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +10 | 5877 |
| 107 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +10 | 45058 |
| 108 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +10 | 10681 |
| 109 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +10 | 6495 |
| 110 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +9 | 4203 |
| 111 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +9 | 1235 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +9 | 17481 |
| 113 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +8 | 1716 |
| 114 | [Dryxio/auto-re-agent](https://github.com/Dryxio/auto-re-agent) | +8 | 917 |
| 115 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +8 | 27381 |
| 116 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +8 | 30578 |
| 117 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +8 | 1267 |
| 118 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +8 | 2946 |
| 119 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +7 | 8168 |
| 120 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +7 | 27981 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1711 | 79107 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +954 | 58156 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +715 | 53837 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +656 | 45124 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +616 | 36124 |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +540 | 29117 |
| 7 | [apple/container](https://github.com/apple/container) | +540 | 47292 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +394 | 51193 |
| 9 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +376 | 11702 |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +334 | 56207 |
| 11 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +310 | 12608 |
| 12 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +291 | 10190 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +280 | 38014 |
| 14 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +257 | 23209 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +239 | 39577 |
| 16 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +223 | 13815 |
| 17 | [shadcn/improve](https://github.com/shadcn/improve) | +217 | 7559 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +207 | 39974 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +200 | 25103 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +197 | 27434 |
| 21 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +193 | 24109 |
| 22 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +192 | 27175 |
| 23 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +190 | 12333 |
| 24 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +188 | 37115 |
| 25 | [stablyai/orca](https://github.com/stablyai/orca) | +187 | 14999 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +187 | 45053 |
| 27 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +185 | 33984 |
| 28 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 27427 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +181 | 15679 |
| 30 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +181 | 35267 |
| 31 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +180 | 14780 |
| 32 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 6921 |
| 33 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +178 | 6560 |
| 34 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 7974 |
| 35 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +170 | 10068 |
| 36 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +169 | 37747 |
| 37 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7797 |
| 38 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +159 | 6388 |
| 39 | [google-research/timesfm](https://github.com/google-research/timesfm) | +159 | 26698 |
| 40 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +149 | 11936 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +147 | 27142 |
| 42 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +144 | 18896 |
| 43 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18220 |
| 44 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +139 | 25485 |
| 45 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +139 | 18484 |
| 46 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +138 | 17006 |
| 47 | [facebook/astryx](https://github.com/facebook/astryx) | +137 | 7452 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +136 | 39358 |
| 49 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +134 | 10267 |
| 50 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +129 | 22169 |
| 51 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 4832 |
| 52 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +122 | 62354 |
| 53 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +119 | 7667 |
| 54 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +119 | 22932 |
| 55 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +118 | 14238 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +117 | 37420 |
| 57 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +116 | 18639 |
| 58 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +112 | 32927 |
| 60 | [blader/humanizer](https://github.com/blader/humanizer) | +111 | 28450 |
| 61 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +109 | 3834 |
| 62 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +109 | 25924 |
| 63 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +107 | 5662 |
| 64 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +106 | 25734 |
| 65 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4232 |
| 66 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +100 | 8339 |
| 67 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +99 | 11193 |
| 68 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +97 | 39517 |
| 69 | [browser-use/video-use](https://github.com/browser-use/video-use) | +96 | 16244 |
| 70 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +95 | 31102 |
| 71 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +95 | 27381 |
| 72 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +95 | 34550 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +94 | 24975 |
| 74 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +92 | 21162 |
| 75 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 9726 |
| 76 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +87 | 10681 |
| 77 | [roboflow/supervision](https://github.com/roboflow/supervision) | +87 | 36553 |
| 78 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +86 | 46497 |
| 79 | [alibaba/zvec](https://github.com/alibaba/zvec) | +86 | 14638 |
| 80 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +84 | 7397 |
| 81 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +84 | 26839 |
| 82 | [makers-pet/oomwoo](https://github.com/makers-pet/oomwoo) | +83 | 4010 |
| 83 | [multica-ai/multica](https://github.com/multica-ai/multica) | +83 | 39651 |
| 84 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +83 | 24745 |
| 85 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +83 | 32008 |
| 86 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +82 | 7970 |
| 87 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6495 |
| 88 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +80 | 27981 |
| 89 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +79 | 8202 |
| 90 | [antirez/ds4](https://github.com/antirez/ds4) | +78 | 18070 |
| 91 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +78 | 5566 |
| 92 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5273 |
| 93 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +76 | 21655 |
| 94 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +76 | 4403 |
| 95 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +75 | 13315 |
| 96 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +75 | 22491 |
| 97 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +73 | 25638 |
| 98 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +72 | 30579 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +70 | 21853 |
| 100 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +69 | 5303 |
| 101 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +69 | 49639 |
| 102 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +69 | 3228 |
| 103 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +68 | 10362 |
| 104 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +68 | 26583 |
| 105 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +66 | 9097 |
| 106 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +65 | 3639 |
| 107 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 6996 |
| 108 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +65 | 16778 |
| 109 | [decolua/9router](https://github.com/decolua/9router) | +64 | 21389 |
| 110 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +64 | 45058 |
| 111 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +63 | 3579 |
| 112 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +61 | 42724 |
| 113 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +61 | 31872 |
| 114 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +60 | 33303 |
| 115 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +60 | 27232 |
| 116 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2597 |
| 117 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +57 | 6259 |
| 118 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +56 | 6624 |
| 119 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +56 | 36103 |
| 120 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +54 | 5559 |
| 121 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +52 | 5092 |
| 122 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +52 | 14122 |
| 123 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +52 | 25120 |
| 124 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +52 | 26375 |
| 125 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +51 | 3657 |
| 126 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +51 | 9406 |
| 127 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +51 | 25957 |
| 128 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +49 | 5243 |
| 129 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +49 | 2511 |
| 130 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +49 | 19636 |
| 131 | [anbeime/skill](https://github.com/anbeime/skill) | +48 | 3393 |
| 132 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +47 | 10894 |
| 133 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +47 | 7904 |
| 134 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +46 | 4338 |
| 135 | [openai/plugins](https://github.com/openai/plugins) | +46 | 4189 |
| 136 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +44 | 4145 |
| 137 | [openai/skills](https://github.com/openai/skills) | +44 | 23437 |
| 138 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +43 | 13446 |
| 139 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3010 |
| 140 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +43 | 12094 |
| 141 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 142 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +41 | 5877 |
| 143 | [google/skills](https://github.com/google/skills) | +41 | 14487 |
| 144 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1621 |
| 145 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +40 | 17481 |
| 146 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +40 | 1563 |
| 147 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +40 | 26293 |
| 148 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +39 | 4203 |
| 149 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +39 | 5702 |
| 150 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +38 | 18183 |
| 151 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1358 |
| 152 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1847 |
| 153 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +37 | 3358 |
| 154 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +37 | 3927 |
| 155 | [floci-io/floci](https://github.com/floci-io/floci) | +37 | 15950 |
| 156 | [browser-act/skills](https://github.com/browser-act/skills) | +36 | 4223 |
| 157 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +36 | 15717 |
| 158 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +35 | 8168 |
| 159 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +35 | 26479 |
| 160 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +35 | 6059 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +34 | 17699 |
| 162 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2769 |
| 163 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +33 | 1994 |
| 164 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +33 | 26008 |
| 165 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +33 | 15853 |
| 166 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2058 |
| 167 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1883 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +31 | 8096 |
| 169 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +31 | 8309 |
| 170 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1233 |
| 171 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +30 | 1624 |
| 172 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +30 | 3684 |
| 173 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +30 | 6658 |
| 174 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +30 | 3906 |
| 175 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +30 | 17989 |
| 176 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1146 |
| 177 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1080 |
| 178 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +29 | 1433 |
| 179 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +29 | 3210 |
| 180 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 1849 |
| 181 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1243 |
| 182 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 596 |
| 183 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +28 | 908 |
| 184 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2359 |
| 185 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +26 | 15036 |
| 186 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +26 | 3409 |
| 187 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +26 | 7495 |
| 188 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +25 | 1768 |
| 189 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 863 |
| 190 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +24 | 5618 |
| 191 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +24 | 7531 |
| 192 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 439 |
| 193 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +23 | 2230 |
| 194 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 623 |
| 195 | [rpamis/comet](https://github.com/rpamis/comet) | +22 | 2115 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +20 | 28879 |
| 197 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +20 | 1302 |
| 198 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +19 | 2394 |
| 199 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +19 | 11718 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +19 | 5224 |
| 201 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +19 | 8774 |
| 202 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +19 | 660 |
| 203 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +18 | 2222 |
| 204 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +18 | 969 |
| 205 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 717 |
| 206 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 635 |
| 207 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +16 | 8879 |
| 208 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +15 | 834 |
| 209 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2708 |
| 210 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1411 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4275 |
| 212 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +14 | 1551 |
| 213 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +14 | 6013 |
| 214 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +14 | 5709 |
| 215 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 503 |
| 216 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 476 |
| 217 | [eze-is/web-access](https://github.com/eze-is/web-access) | +14 | 8162 |
| 218 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +14 | 4357 |
| 219 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 220 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 414 |
| 221 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +13 | 3081 |
| 222 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +13 | 2791 |
| 223 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 461 |
| 224 | [AI-Builder-Club/skills](https://github.com/AI-Builder-Club/skills) | +12 | 821 |
| 225 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +12 | 546 |
| 226 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 14004 |
| 227 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 328 |
| 228 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +11 | 0 |
| 229 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 674 |
| 230 | [robinebers/openusage](https://github.com/robinebers/openusage) | +11 | 3190 |
| 231 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 348 |
| 232 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 466 |
| 233 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 338 |
| 234 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 774 |
| 235 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 424 |
| 236 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +10 | 1921 |
| 237 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +10 | 748 |
| 238 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 405 |
| 239 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +10 | 2258 |
| 240 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 202 |
| 241 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +10 | 312 |
| 242 | [anonymousRAID/OSINT-Mapping-Tool](https://github.com/anonymousRAID/OSINT-Mapping-Tool) | +10 | 482 |
| 243 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2754 |
| 244 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +9 | 4987 |
| 245 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) | +9 | 1170 |
| 246 | [emollick/concord](https://github.com/emollick/concord) | +9 | 200 |
| 247 | [rezarahiminia/worldcup2026](https://github.com/rezarahiminia/worldcup2026) | +9 | 431 |
| 248 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3880 |
| 249 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +9 | 239 |
| 250 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +8 | 1304 |
| 251 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 590 |
| 252 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 367 |
| 253 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +8 | 1688 |
| 254 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 255 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 596 |
| 256 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +8 | 845 |
| 257 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +7 | 1501 |
| 258 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 160 |
| 259 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 958 |
| 260 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 324 |
| 261 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 248 |
| 262 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +7 | 3661 |
| 263 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +7 | 2774 |
| 264 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +7 | 203 |
| 265 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 452 |
| 266 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +6 | 370 |
| 267 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +6 | 404 |
| 268 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 179 |
| 269 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +6 | 1785 |
| 270 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2553 |
| 271 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 81 |
| 272 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9496 |
| 273 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 305 |
| 274 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +5 | 738 |
| 275 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 118 |
| 276 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2659 |
| 277 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 506 |
| 278 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2326 |
| 279 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +4 | 642 |
| 280 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 281 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +4 | 98 |
| 282 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +4 | 1117 |
| 283 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +3 | 395 |
| 284 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 116 |
| 285 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 615 |
| 286 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 222 |
| 287 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +3 | 820 |
| 288 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 535 |
| 289 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 843 |
| 290 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 291 | [apache/phoenix-adapters](https://github.com/apache/phoenix-adapters) | +3 | 118 |
| 292 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +3 | 295 |
| 293 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 611 |
| 294 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 220 |
| 295 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1681 |
| 296 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3336 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 399 |
| 299 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 852 |
| 300 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
