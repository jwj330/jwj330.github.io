---
title: "2026-07-12 GitHub增长趋势报告"
description: "1.pgrust+4 2.free-claude-code+3 3.video-autopilot-kit+3 4.X4G+2 5.zeus+2"
date: 2026-07-12T20:51:41+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-12 20:51:41

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
        'daily': {"categories": ["zgwl/chinese-buy-us-stock-guide", "wuyoscar/GPT-Image2-Skill", "hgmzhn/manga-translator-ui", "EvanBacon/serve-sim", "HKUDS/Vibe-Trading", "MadsLorentzen/ai-job-search", "JCodesMore/ai-website-cloner-template", "Manoj-engineer/k8squest", "dnshe/DNSHE-FreeDomains", "rosemarycox5334-debug/PA_Agent", "DeusData/codebase-memory-mcp", "baairon/torlink", "decolua/9router", "openai/plugins", "steipete/CodexBar", "IR-NETLIFY/zeus", "x4gKing/X4G", "Hao0321/video-autopilot-kit", "Alishahryar1/free-claude-code", "malisper/pgrust"], "data": [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4]},
        'weekly': {"categories": ["microsoft/SkillOpt", "stablyai/orca", "Trystan-SA/claude-design-system-prompt", "openai/codex-plugin-cc", "xbtlin/ai-berkshire", "DeusData/codebase-memory-mcp", "Shpigford/knockoff", "k1tbyte/Wand-Enhancer", "alibaba/page-agent", "calesthio/OpenMontage", "teamchong/pxpipe", "x4gKing/X4G", "ogulcancelik/herdr", "diegosouzapw/OmniRoute", "bradautomates/claude-video", "usestrix/strix", "iOfficeAI/OfficeCLI", "Zackriya-Solutions/meetily", "langchain-ai/openwiki", "MadsLorentzen/ai-job-search"], "data": [14, 14, 16, 16, 16, 16, 17, 18, 18, 18, 22, 23, 25, 27, 28, 29, 31, 44, 47, 74]},
        'monthly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "stablyai/orca", "JCodesMore/ai-website-cloner-template", "xbtlin/ai-berkshire", "XiaomiMiMo/MiMo-Code", "jamiepine/voicebox", "baidu/Unlimited-OCR", "hugohe3/ppt-master", "usestrix/strix", "NVIDIA/SkillSpector", "mvanhorn/last30days-skill", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "apple/container", "DeusData/codebase-memory-mcp", "elder-plinius/CL4R1T4S", "calesthio/OpenMontage", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [187, 188, 191, 194, 195, 205, 225, 237, 241, 270, 279, 294, 317, 338, 538, 575, 615, 680, 846, 1709]}
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
| 1 | [malisper/pgrust](https://github.com/malisper/pgrust) | +4 | 2406 |
| 2 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 39784 |
| 3 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +3 | 1131 |
| 4 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +2 | 4797 |
| 5 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +2 | 1136 |
| 6 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +2 | 17937 |
| 7 | [openai/plugins](https://github.com/openai/plugins) | +2 | 4500 |
| 8 | [decolua/9router](https://github.com/decolua/9router) | +2 | 21898 |
| 9 | [baairon/torlink](https://github.com/baairon/torlink) | +2 | 3509 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 30559 |
| 11 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +2 | 991 |
| 12 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 5395 |
| 13 | [Manoj-engineer/k8squest](https://github.com/Manoj-engineer/k8squest) | +1 | 1356 |
| 14 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1 | 27915 |
| 15 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +1 | 21385 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +1 | 20434 |
| 17 | [EvanBacon/serve-sim](https://github.com/EvanBacon/serve-sim) | +1 | 2448 |
| 18 | [hgmzhn/manga-translator-ui](https://github.com/hgmzhn/manga-translator-ui) | +1 | 2146 |
| 19 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | +1 | 3673 |
| 20 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +1 | 5926 |
| 21 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +1 | 11241 |
| 22 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +1 | 1653 |
| 23 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1 | 22553 |
| 24 | [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | +1 | 1463 |
| 25 | [kenchangh/kensat](https://github.com/kenchangh/kensat) | +1 | 77 |
| 26 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +1 | 29954 |
| 27 | [hero8152/LTX2.3-Multifunctional](https://github.com/hero8152/LTX2.3-Multifunctional) | +1 | 98 |
| 28 | [Lampese/codex-switcher](https://github.com/Lampese/codex-switcher) | +1 | 514 |
| 29 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +1 | 1615 |
| 30 | [hkfires/EmbyProxy](https://github.com/hkfires/EmbyProxy) | +1 | 76 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +74 | 21385 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +47 | 10731 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +44 | 23527 |
| 4 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +31 | 15389 |
| 5 | [usestrix/strix](https://github.com/usestrix/strix) | +29 | 40820 |
| 6 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +28 | 7803 |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +27 | 16155 |
| 8 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 15756 |
| 9 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +23 | 4797 |
| 10 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +22 | 5654 |
| 11 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +18 | 37487 |
| 12 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +18 | 26200 |
| 13 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +18 | 6870 |
| 14 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1817 |
| 15 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +16 | 30559 |
| 16 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +16 | 12882 |
| 17 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +16 | 28006 |
| 18 | [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt) | +16 | 1670 |
| 19 | [stablyai/orca](https://github.com/stablyai/orca) | +14 | 16807 |
| 20 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 12332 |
| 21 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +14 | 17937 |
| 22 | [facebook/astryx](https://github.com/facebook/astryx) | +14 | 8121 |
| 23 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 11241 |
| 24 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +12 | 7416 |
| 25 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1721 |
| 26 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +12 | 37897 |
| 27 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +12 | 37480 |
| 28 | [davidondrej/skills](https://github.com/davidondrej/skills) | +12 | 2381 |
| 29 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +11 | 4515 |
| 30 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +11 | 51707 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +11 | 28017 |
| 32 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +10 | 27915 |
| 33 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +10 | 4014 |
| 34 | [alibaba/zvec](https://github.com/alibaba/zvec) | +10 | 14806 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +9 | 56866 |
| 36 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +9 | 10161 |
| 37 | [multica-ai/multica](https://github.com/multica-ai/multica) | +9 | 39948 |
| 38 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 9245 |
| 39 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +9 | 1615 |
| 40 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +9 | 1368 |
| 41 | [malisper/pgrust](https://github.com/malisper/pgrust) | +8 | 2406 |
| 42 | [vercel-labs/native](https://github.com/vercel-labs/native) | +8 | 5939 |
| 43 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +8 | 45935 |
| 44 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +8 | 1976 |
| 45 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +8 | 9791 |
| 46 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +8 | 40835 |
| 47 | [decolua/9router](https://github.com/decolua/9router) | +8 | 21898 |
| 48 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +8 | 22355 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +7 | 39784 |
| 50 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +7 | 5640 |
| 51 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +7 | 31639 |
| 52 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +7 | 29901 |
| 53 | [shadcn/improve](https://github.com/shadcn/improve) | +7 | 8025 |
| 54 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +7 | 20434 |
| 55 | [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | +7 | 1463 |
| 56 | [baairon/torlink](https://github.com/baairon/torlink) | +7 | 3509 |
| 57 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +7 | 34462 |
| 58 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +7 | 1844 |
| 59 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +7 | 22022 |
| 60 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +7 | 4127 |
| 61 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 5395 |
| 62 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 1382 |
| 63 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 1962 |
| 64 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +6 | 6344 |
| 65 | [wouterdebie/davit](https://github.com/wouterdebie/davit) | +6 | 888 |
| 66 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +6 | 6675 |
| 67 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +6 | 12997 |
| 68 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +6 | 14100 |
| 69 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +6 | 8651 |
| 70 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +6 | 2029 |
| 71 | [gastownhall/gastown](https://github.com/gastownhall/gastown) | +6 | 16984 |
| 72 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +6 | 9215 |
| 73 | [erincatto/box3d](https://github.com/erincatto/box3d) | +6 | 5091 |
| 74 | [browser-use/video-use](https://github.com/browser-use/video-use) | +6 | 16691 |
| 75 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 1153 |
| 76 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +5 | 11936 |
| 77 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +5 | 913 |
| 78 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 38541 |
| 79 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +5 | 7621 |
| 80 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 2530 |
| 81 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +5 | 27602 |
| 82 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +5 | 23554 |
| 83 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +5 | 10569 |
| 84 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +5 | 1459 |
| 85 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +4 | 1136 |
| 86 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +4 | 14366 |
| 87 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +4 | 25220 |
| 88 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +4 | 13719 |
| 89 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4 | 3883 |
| 90 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +4 | 10300 |
| 91 | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | +4 | 1823 |
| 92 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +4 | 6329 |
| 93 | [kurikomi-labs/komi-store](https://github.com/kurikomi-labs/komi-store) | +4 | 16482 |
| 94 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +4 | 4093 |
| 95 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 30749 |
| 96 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +4 | 26620 |
| 97 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +4 | 33202 |
| 98 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 11154 |
| 99 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 5206 |
| 100 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 38093 |
| 101 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +4 | 13558 |
| 102 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +4 | 25392 |
| 103 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +4 | 1555 |
| 104 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +4 | 25232 |
| 105 | [Stalkeroestudio76/CCleaner-PRO](https://github.com/Stalkeroestudio76/CCleaner-PRO) | +4 | 0 |
| 106 | [Pluviobyte/rnskill](https://github.com/Pluviobyte/rnskill) | +4 | 411 |
| 107 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +3 | 46757 |
| 108 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +3 | 1131 |
| 109 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +3 | 991 |
| 110 | [turnstonelabs/turnstone](https://github.com/turnstonelabs/turnstone) | +3 | 837 |
| 111 | [tiantianGPU/reg-factory](https://github.com/tiantianGPU/reg-factory) | +3 | 1408 |
| 112 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +3 | 628 |
| 113 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +3 | 4504 |
| 114 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +3 | 576 |
| 115 | [Robbyant/lingbot-vla-v2](https://github.com/Robbyant/lingbot-vla-v2) | +3 | 466 |
| 116 | [mira-wm/mira](https://github.com/mira-wm/mira) | +3 | 369 |
| 117 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +3 | 14906 |
| 118 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +3 | 5670 |
| 119 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 6572 |
| 120 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 10871 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1709 | 81267 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +846 | 58720 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +680 | 55296 |
| 4 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +615 | 37487 |
| 5 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +575 | 45297 |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +538 | 30559 |
| 7 | [apple/container](https://github.com/apple/container) | +338 | 47629 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +317 | 56866 |
| 9 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +294 | 10314 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +279 | 51707 |
| 11 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +270 | 12997 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +241 | 40820 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +237 | 38541 |
| 14 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +225 | 14100 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +205 | 40835 |
| 16 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +195 | 11851 |
| 17 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +194 | 12882 |
| 18 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +191 | 27915 |
| 19 | [stablyai/orca](https://github.com/stablyai/orca) | +188 | 16807 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +187 | 25392 |
| 21 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 27640 |
| 22 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +178 | 15756 |
| 23 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +178 | 7135 |
| 24 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +178 | 6778 |
| 25 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +176 | 10731 |
| 26 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 8180 |
| 27 | [shadcn/improve](https://github.com/shadcn/improve) | +176 | 8025 |
| 28 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +175 | 23554 |
| 29 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +171 | 28017 |
| 30 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7851 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +163 | 34462 |
| 32 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +162 | 35521 |
| 33 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +161 | 37480 |
| 34 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26805 |
| 35 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +157 | 6572 |
| 36 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +154 | 15909 |
| 37 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +154 | 24803 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +153 | 45935 |
| 39 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +148 | 7188 |
| 40 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18501 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +142 | 28006 |
| 42 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +142 | 12332 |
| 43 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +141 | 38093 |
| 44 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +140 | 26200 |
| 45 | [facebook/astryx](https://github.com/facebook/astryx) | +138 | 8121 |
| 46 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +133 | 20434 |
| 47 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +131 | 23527 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +129 | 39784 |
| 49 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5091 |
| 50 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +122 | 21385 |
| 51 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +118 | 17424 |
| 52 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +116 | 8142 |
| 53 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +116 | 10444 |
| 54 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +114 | 16155 |
| 55 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +114 | 23216 |
| 56 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +108 | 37897 |
| 58 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +108 | 62482 |
| 59 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +107 | 3881 |
| 60 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +107 | 26073 |
| 61 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +105 | 6004 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +102 | 28862 |
| 63 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4421 |
| 64 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +99 | 11936 |
| 65 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +98 | 33202 |
| 66 | [browser-use/video-use](https://github.com/browser-use/video-use) | +88 | 16691 |
| 67 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +88 | 26016 |
| 68 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10161 |
| 69 | [alibaba/zvec](https://github.com/alibaba/zvec) | +87 | 14806 |
| 70 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +87 | 8521 |
| 71 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +85 | 25319 |
| 72 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +84 | 10871 |
| 73 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4127 |
| 74 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +83 | 27602 |
| 75 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +82 | 34727 |
| 76 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +81 | 46757 |
| 77 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6576 |
| 78 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +80 | 27042 |
| 79 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +79 | 25220 |
| 80 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5654 |
| 81 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +77 | 21306 |
| 82 | [antirez/ds4](https://github.com/antirez/ds4) | +76 | 18326 |
| 83 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +76 | 8106 |
| 84 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +74 | 22022 |
| 85 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +73 | 31639 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +73 | 39948 |
| 87 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +73 | 32095 |
| 88 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +71 | 5640 |
| 89 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +71 | 3883 |
| 90 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +70 | 25928 |
| 91 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +69 | 15389 |
| 92 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +68 | 39702 |
| 93 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +68 | 5670 |
| 94 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +67 | 28119 |
| 95 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +66 | 4093 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +66 | 9245 |
| 97 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 7621 |
| 98 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +65 | 30749 |
| 99 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +64 | 10569 |
| 100 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +64 | 11241 |
| 101 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +64 | 26901 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +63 | 22355 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +62 | 49865 |
| 104 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +61 | 6870 |
| 105 | [decolua/9router](https://github.com/decolua/9router) | +61 | 21899 |
| 106 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +61 | 22553 |
| 107 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +60 | 22945 |
| 108 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +59 | 7803 |
| 109 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +59 | 3608 |
| 110 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2661 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +57 | 45201 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +57 | 16911 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +56 | 42998 |
| 114 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +56 | 27421 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +54 | 32027 |
| 116 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +52 | 4014 |
| 117 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +51 | 5817 |
| 118 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +50 | 33416 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +49 | 25232 |
| 120 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +48 | 36103 |
| 121 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +47 | 9531 |
| 122 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4515 |
| 123 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +46 | 6448 |
| 124 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +46 | 26536 |
| 125 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +45 | 11154 |
| 126 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +45 | 26135 |
| 127 | [anbeime/skill](https://github.com/anbeime/skill) | +43 | 3514 |
| 128 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3036 |
| 129 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +43 | 19776 |
| 130 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 131 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +42 | 8045 |
| 132 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +42 | 2548 |
| 133 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +41 | 13558 |
| 134 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +41 | 1630 |
| 135 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1703 |
| 136 | [openai/plugins](https://github.com/openai/plugins) | +40 | 4500 |
| 137 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +39 | 12194 |
| 138 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1358 |
| 139 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1847 |
| 140 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +37 | 4367 |
| 141 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +37 | 17646 |
| 142 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +37 | 6063 |
| 143 | [openai/skills](https://github.com/openai/skills) | +37 | 23581 |
| 144 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +35 | 3489 |
| 145 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2819 |
| 146 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +33 | 2031 |
| 147 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +33 | 4412 |
| 148 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +33 | 18268 |
| 149 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2068 |
| 150 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +33 | 2956 |
| 151 | [browser-act/skills](https://github.com/browser-act/skills) | +32 | 4320 |
| 152 | [jundot/omlx](https://github.com/jundot/omlx) | +32 | 17776 |
| 153 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +32 | 15936 |
| 154 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1932 |
| 155 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +32 | 5344 |
| 156 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +32 | 4504 |
| 157 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +32 | 26353 |
| 158 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1255 |
| 159 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +30 | 15902 |
| 160 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +29 | 8316 |
| 161 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1206 |
| 162 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1108 |
| 163 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +29 | 3251 |
| 164 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +29 | 26620 |
| 165 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +29 | 1509 |
| 166 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +29 | 8356 |
| 167 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 1943 |
| 168 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1275 |
| 169 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +28 | 18085 |
| 170 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +28 | 625 |
| 171 | [floci-io/floci](https://github.com/floci-io/floci) | +28 | 16390 |
| 172 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +27 | 1634 |
| 173 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +27 | 5763 |
| 174 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2446 |
| 175 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +26 | 26138 |
| 176 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +26 | 4002 |
| 177 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15090 |
| 178 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +25 | 3536 |
| 179 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +25 | 8318 |
| 180 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +25 | 6236 |
| 181 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +25 | 916 |
| 182 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 968 |
| 183 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +24 | 5200 |
| 184 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +24 | 6789 |
| 185 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +24 | 5701 |
| 186 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 441 |
| 187 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +23 | 4797 |
| 188 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1555 |
| 189 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 1833 |
| 190 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +22 | 624 |
| 191 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +21 | 2308 |
| 192 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +20 | 7895 |
| 193 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +20 | 7611 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +18 | 28977 |
| 195 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +18 | 1313 |
| 196 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +18 | 2498 |
| 197 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1817 |
| 198 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 777 |
| 199 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 649 |
| 200 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +17 | 8851 |
| 201 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +16 | 1136 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +16 | 5302 |
| 203 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +16 | 2420 |
| 204 | [rpamis/comet](https://github.com/rpamis/comet) | +16 | 2197 |
| 205 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2794 |
| 206 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1431 |
| 207 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4336 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +14 | 11774 |
| 209 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 511 |
| 210 | [buynao/aipath](https://github.com/buynao/aipath) | +14 | 477 |
| 211 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 212 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +13 | 329 |
| 213 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 441 |
| 214 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 486 |
| 215 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +12 | 679 |
| 216 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 14024 |
| 217 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +11 | 6045 |
| 218 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +11 | 5777 |
| 219 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +11 | 573 |
| 220 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 684 |
| 221 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +11 | 8888 |
| 222 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 351 |
| 223 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2829 |
| 224 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 869 |
| 225 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 583 |
| 226 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 346 |
| 227 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 426 |
| 228 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 447 |
| 229 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 202 |
| 230 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +10 | 4416 |
| 231 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2784 |
| 232 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +9 | 0 |
| 233 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 1941 |
| 234 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +9 | 2312 |
| 235 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +9 | 4990 |
| 236 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +9 | 390 |
| 237 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +9 | 3110 |
| 238 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 3987 |
| 239 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 762 |
| 240 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +8 | 1317 |
| 241 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 774 |
| 242 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 372 |
| 243 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4780 |
| 244 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 245 | [eze-is/web-access](https://github.com/eze-is/web-access) | +8 | 8201 |
| 246 | [robinebers/openusage](https://github.com/robinebers/openusage) | +8 | 3247 |
| 247 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +8 | 1531 |
| 248 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +8 | 868 |
| 249 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +8 | 243 |
| 250 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 517 |
| 251 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 161 |
| 252 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +7 | 534 |
| 253 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 975 |
| 254 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +7 | 348 |
| 255 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 331 |
| 256 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1719 |
| 257 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 250 |
| 258 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 455 |
| 259 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1526 |
| 260 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 629 |
| 261 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +6 | 3680 |
| 262 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 179 |
| 263 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +6 | 2801 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +6 | 1798 |
| 265 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 338 |
| 266 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 544 |
| 267 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2565 |
| 268 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 88 |
| 269 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9502 |
| 270 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 315 |
| 271 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +5 | 757 |
| 272 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 119 |
| 273 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2678 |
| 274 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2348 |
| 275 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +4 | 0 |
| 276 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 185 |
| 277 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 82 |
| 278 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 116 |
| 279 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 179 |
| 280 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 641 |
| 281 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +3 | 655 |
| 282 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +3 | 223 |
| 283 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 541 |
| 284 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 846 |
| 285 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +3 | 103 |
| 286 | [DevYangJC/intelli_hub](https://github.com/DevYangJC/intelli_hub) | +3 | 76 |
| 287 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 641 |
| 288 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 399 |
| 289 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +2 | 137 |
| 290 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 236 |
| 291 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 823 |
| 292 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1683 |
| 293 | [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | +2 | 215 |
| 294 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3354 |
| 295 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 296 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 93 |
| 297 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 418 |
| 298 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 853 |
| 299 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 149 |
| 300 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
