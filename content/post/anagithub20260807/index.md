---
title: "2026-08-07 GitHub增长趋势报告"
description: "1.herdr+4 2.code-review-graph+4 3.ppt-master+3 4.cli+3 5.DeepSeek-Reasonix+3"
date: 2026-08-07T20:42:02+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-07 20:42:02

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
        'daily': {"categories": ["diegosouzapw/OmniRoute", "can1357/oh-my-pi", "atilaahmettaner/tradingview-mcp", "heygen-com/hyperframes", "MadsLorentzen/ai-job-search", "magicrew/doc7", "huangruiteng/loopx", "agentscope-ai/QwenPaw", "garrytan/gbrain", "tashfeenahmed/freellmapi", "openJiuwen-ai/jiuwenswarm", "emilkowalski/skills", "ymichael/bb", "firecrawl/pdf-inspector", "AtomicBot-ai/atomic-agent", "esengine/DeepSeek-Reasonix", "brightdata/cli", "hugohe3/ppt-master", "tirth8205/code-review-graph", "herdrdev/herdr"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4]},
        'weekly': {"categories": ["MadsLorentzen/ai-job-search", "herdrdev/herdr", "lidge-jun/opencodex", "emilkowalski/skills", "agentscope-ai/QwenPaw", "thebuggeddev/anatomy", "virgiliojr94/book-to-skill", "tirth8205/code-review-graph", "ifixai-ai/iFixAi", "bashalarmistalt/decimen-optical-transfer", "xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer", "esengine/DeepSeek-Reasonix", "block/buzz", "stablyai/orca", "trycompai/crm", "diegosouzapw/OmniRoute", "TencentCloud/TencentDB-Agent-Memory", "yc-software/qm", "zhaoxuya520/reverse-skill", "firecrawl/pdf-inspector"], "data": [7, 7, 8, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 14, 14, 15, 24, 24, 30]},
        'monthly': {"categories": ["jamiepine/voicebox", "calesthio/OpenMontage", "x4gKing/X4G", "agentscope-ai/QwenPaw", "andrewyng/openworker", "oblien/openship", "bradautomates/claude-video", "k1tbyte/Wand-Enhancer", "usestrix/strix", "ayghri/i-have-adhd", "HKUDS/Vibe-Trading", "emilkowalski/skills", "Fei-Away/Codex-Dream-Skin", "iOfficeAI/OfficeCLI", "herdrdev/herdr", "block/buzz", "stablyai/orca", "diegosouzapw/OmniRoute", "JustVugg/colibri", "MadsLorentzen/ai-job-search"], "data": [42, 43, 43, 46, 48, 49, 51, 51, 53, 54, 58, 63, 64, 73, 73, 74, 96, 96, 97, 114]}
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
| 1 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +4 | 25579 |
| 2 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 29340 |
| 3 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 43784 |
| 4 | [brightdata/cli](https://github.com/brightdata/cli) | +3 | 1791 |
| 5 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +3 | 32877 |
| 6 | [AtomicBot-ai/atomic-agent](https://github.com/AtomicBot-ai/atomic-agent) | +3 | 1633 |
| 7 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +3 | 13007 |
| 8 | [ymichael/bb](https://github.com/ymichael/bb) | +3 | 1368 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 26843 |
| 10 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +2 | 2296 |
| 11 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +2 | 18024 |
| 12 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2 | 27951 |
| 13 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +2 | 34237 |
| 14 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +2 | 3354 |
| 15 | [magicrew/doc7](https://github.com/magicrew/doc7) | +2 | 608 |
| 16 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2 | 30684 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 39938 |
| 18 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +2 | 3871 |
| 19 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +2 | 22749 |
| 20 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 42446 |
| 21 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +1 | 407 |
| 22 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +1 | 19649 |
| 23 | [FeijiangHan/PaperForge](https://github.com/FeijiangHan/PaperForge) | +1 | 439 |
| 24 | [YuKongA/ghostlock-oplus](https://github.com/YuKongA/ghostlock-oplus) | +1 | 80 |
| 25 | [assafkip/kipi-system](https://github.com/assafkip/kipi-system) | +1 | 101 |
| 26 | [cloudflare/vibesdk](https://github.com/cloudflare/vibesdk) | +1 | 5253 |
| 27 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +1 | 9755 |
| 28 | [Rizzo-AI-Academy/rizzo-pii](https://github.com/Rizzo-AI-Academy/rizzo-pii) | +1 | 659 |
| 29 | [t8y2/dbx](https://github.com/t8y2/dbx) | +1 | 13632 |
| 30 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +1 | 3752 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +30 | 13007 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +24 | 20490 |
| 3 | [yc-software/qm](https://github.com/yc-software/qm) | +24 | 12265 |
| 4 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +15 | 17448 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +14 | 42446 |
| 6 | [trycompai/crm](https://github.com/trycompai/crm) | +14 | 7462 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +11 | 39576 |
| 8 | [block/buzz](https://github.com/block/buzz) | +11 | 24878 |
| 9 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +11 | 32877 |
| 10 | [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | +11 | 3537 |
| 11 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +11 | 5136 |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +10 | 6646 |
| 13 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +10 | 29340 |
| 14 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +9 | 18227 |
| 15 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +9 | 1969 |
| 16 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 34237 |
| 17 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +9 | 26843 |
| 18 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 8363 |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +7 | 25579 |
| 20 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +7 | 30684 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +7 | 43784 |
| 22 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +7 | 13547 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 33949 |
| 24 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +7 | 26493 |
| 25 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 22749 |
| 26 | [browser-use/video-use](https://github.com/browser-use/video-use) | +6 | 19964 |
| 27 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +6 | 18105 |
| 28 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +6 | 22451 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +6 | 19556 |
| 30 | [multica-ai/multica](https://github.com/multica-ai/multica) | +5 | 44688 |
| 31 | [brightdata/cli](https://github.com/brightdata/cli) | +5 | 1791 |
| 32 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +5 | 19649 |
| 33 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +5 | 8153 |
| 34 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 13632 |
| 35 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 1220 |
| 36 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +5 | 3355 |
| 37 | [antirez/ds4](https://github.com/antirez/ds4) | +5 | 20882 |
| 38 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +5 | 23168 |
| 39 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +4 | 4388 |
| 40 | [ymichael/bb](https://github.com/ymichael/bb) | +4 | 1368 |
| 41 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +4 | 4668 |
| 42 | [AtomicBot-ai/atomic-agent](https://github.com/AtomicBot-ai/atomic-agent) | +4 | 1633 |
| 43 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +4 | 2388 |
| 44 | [magicrew/doc7](https://github.com/magicrew/doc7) | +4 | 608 |
| 45 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +4 | 3752 |
| 46 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4 | 18024 |
| 47 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +4 | 9229 |
| 48 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 34214 |
| 49 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +4 | 43452 |
| 50 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +4 | 3333 |
| 51 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +4 | 14418 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 46219 |
| 53 | [decolua/9router](https://github.com/decolua/9router) | +4 | 24908 |
| 54 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +3 | 4696 |
| 55 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 4918 |
| 56 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +3 | 1865 |
| 57 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +3 | 3871 |
| 58 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +3 | 3224 |
| 59 | [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | +3 | 266 |
| 60 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +3 | 2296 |
| 61 | [ben-z/findphone](https://github.com/ben-z/findphone) | +3 | 919 |
| 62 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +3 | 13039 |
| 63 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +3 | 5799 |
| 64 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +3 | 8274 |
| 65 | [uber/ADR](https://github.com/uber/ADR) | +3 | 1278 |
| 66 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +3 | 8438 |
| 67 | [Jaycheng1103/chatgpt-video-editing-skills](https://github.com/Jaycheng1103/chatgpt-video-editing-skills) | +3 | 398 |
| 68 | [adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide) | +3 | 7965 |
| 69 | [snekxs/openmouse](https://github.com/snekxs/openmouse) | +3 | 1013 |
| 70 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +3 | 0 |
| 71 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 8086 |
| 72 | [autonomous-ai/autonomous-computer](https://github.com/autonomous-ai/autonomous-computer) | +3 | 1172 |
| 73 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3 | 49694 |
| 74 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +3 | 5189 |
| 75 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +3 | 28192 |
| 76 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 7041 |
| 77 | [pascalorg/editor](https://github.com/pascalorg/editor) | +3 | 21200 |
| 78 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 30229 |
| 79 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +3 | 19114 |
| 80 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +3 | 1771 |
| 81 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 32936 |
| 82 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2 | 45873 |
| 83 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2 | 27951 |
| 84 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 16336 |
| 85 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 38038 |
| 86 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29725 |
| 87 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 17077 |
| 88 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +2 | 27095 |
| 89 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2 | 44769 |
| 90 | [EKKOLearnAI/hermes-studio](https://github.com/EKKOLearnAI/hermes-studio) | +2 | 9840 |
| 91 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 39938 |
| 92 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +2 | 776 |
| 93 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2 | 29991 |
| 94 | [mintdotgg/mint-threejs-skills](https://github.com/mintdotgg/mint-threejs-skills) | +2 | 104 |
| 95 | [chaseai-yt/grill-me-codex](https://github.com/chaseai-yt/grill-me-codex) | +2 | 1030 |
| 96 | [google/skills](https://github.com/google/skills) | +2 | 16174 |
| 97 | [brycewang-stanford/Auto-Research-Skills](https://github.com/brycewang-stanford/Auto-Research-Skills) | +2 | 109 |
| 98 | [ArcadeAI/blueprint-mcp](https://github.com/ArcadeAI/blueprint-mcp) | +2 | 718 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 24074 |
| 100 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +2 | 3133 |
| 101 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 60452 |
| 102 | [EgalitarianMonkey/hometube](https://github.com/EgalitarianMonkey/hometube) | +2 | 1221 |
| 103 | [reflex-dev/xy](https://github.com/reflex-dev/xy) | +2 | 1610 |
| 104 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +2 | 1536 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 13616 |
| 106 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +2 | 1810 |
| 107 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +2 | 4047 |
| 108 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +2 | 10174 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +2 | 6575 |
| 110 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +2 | 3030 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 19358 |
| 112 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +2 | 32920 |
| 113 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +2 | 1659 |
| 114 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +2 | 8422 |
| 115 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +2 | 1855 |
| 116 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +2 | 6244 |
| 117 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +2 | 5220 |
| 118 | [pg83/shitty](https://github.com/pg83/shitty) | +2 | 267 |
| 119 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2 | 35069 |
| 120 | [gavamedia/deltafin](https://github.com/gavamedia/deltafin) | +2 | 718 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +114 | 30684 |
| 2 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +97 | 23168 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +96 | 42446 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +96 | 39576 |
| 5 | [block/buzz](https://github.com/block/buzz) | +74 | 24878 |
| 6 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +73 | 25579 |
| 7 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +73 | 26493 |
| 8 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 13392 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +63 | 26843 |
| 10 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +58 | 30229 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +54 | 18105 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +53 | 49619 |
| 13 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +51 | 15469 |
| 14 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +51 | 14418 |
| 15 | [oblien/openship](https://github.com/oblien/openship) | +49 | 10413 |
| 16 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +48 | 13547 |
| 17 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +46 | 34237 |
| 18 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +43 | 8086 |
| 19 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +43 | 45873 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +42 | 49694 |
| 21 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +41 | 22451 |
| 22 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +37 | 38038 |
| 23 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +36 | 18227 |
| 24 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +36 | 8185 |
| 25 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +36 | 46219 |
| 26 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +36 | 19114 |
| 27 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 10161 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +35 | 43784 |
| 29 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +33 | 29340 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +32 | 39938 |
| 31 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +31 | 8363 |
| 32 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +31 | 7736 |
| 33 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +30 | 13007 |
| 34 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +30 | 16336 |
| 35 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +30 | 10105 |
| 36 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +29 | 20490 |
| 37 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +29 | 32936 |
| 38 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 14515 |
| 39 | [openai/codex-security](https://github.com/openai/codex-security) | +27 | 9260 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +27 | 44688 |
| 41 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +27 | 43452 |
| 42 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8575 |
| 43 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +26 | 9229 |
| 44 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +26 | 32877 |
| 45 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +26 | 33949 |
| 46 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +26 | 9590 |
| 47 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +25 | 22749 |
| 48 | [yc-software/qm](https://github.com/yc-software/qm) | +24 | 12265 |
| 49 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +24 | 4398 |
| 50 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +23 | 19556 |
| 51 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +23 | 17448 |
| 52 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +23 | 7699 |
| 53 | [marcelroed/gigatoken](https://github.com/marcelroed/gigatoken) | +23 | 3934 |
| 54 | [t8y2/dbx](https://github.com/t8y2/dbx) | +23 | 13632 |
| 55 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 31172 |
| 56 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +23 | 44769 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36246 |
| 58 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +22 | 60452 |
| 59 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +22 | 4918 |
| 60 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +22 | 4859 |
| 61 | [blader/humanizer](https://github.com/blader/humanizer) | +20 | 34214 |
| 62 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +20 | 3495 |
| 63 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4326 |
| 64 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +19 | 15743 |
| 65 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +19 | 28192 |
| 66 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +19 | 7050 |
| 67 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +19 | 15179 |
| 68 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +19 | 4826 |
| 69 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 41286 |
| 70 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +19 | 5677 |
| 71 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1994 |
| 72 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +18 | 6646 |
| 73 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +18 | 3752 |
| 74 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +18 | 8153 |
| 75 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +18 | 7080 |
| 76 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5443 |
| 77 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +18 | 4425 |
| 78 | [malisper/pgrust](https://github.com/malisper/pgrust) | +18 | 4110 |
| 79 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +17 | 8438 |
| 80 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +17 | 3333 |
| 81 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11131 |
| 82 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 13616 |
| 83 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 6598 |
| 84 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +16 | 16315 |
| 85 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +16 | 28501 |
| 86 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +16 | 3516 |
| 87 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 19964 |
| 88 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +15 | 9356 |
| 89 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +15 | 35069 |
| 90 | [trycompai/crm](https://github.com/trycompai/crm) | +14 | 7462 |
| 91 | [pascalorg/editor](https://github.com/pascalorg/editor) | +14 | 21200 |
| 92 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +14 | 5608 |
| 93 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3946 |
| 94 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +14 | 13039 |
| 95 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +14 | 2526 |
| 96 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +14 | 31504 |
| 97 | [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | +13 | 3537 |
| 98 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +13 | 2388 |
| 99 | [every-app/open-seo](https://github.com/every-app/open-seo) | +13 | 10843 |
| 100 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +13 | 17221 |
| 101 | [floci-io/floci](https://github.com/floci-io/floci) | +13 | 18552 |
| 102 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2131 |
| 103 | [decolua/9router](https://github.com/decolua/9router) | +13 | 24908 |
| 104 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +12 | 4388 |
| 105 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 4464 |
| 106 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +11 | 5136 |
| 107 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +11 | 6244 |
| 108 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 32920 |
| 109 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1952 |
| 110 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +10 | 46756 |
| 111 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1526 |
| 112 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +10 | 2654 |
| 113 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +10 | 2348 |
| 114 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 1042 |
| 115 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +10 | 26569 |
| 116 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1830 |
| 117 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 9954 |
| 118 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +9 | 8274 |
| 119 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +9 | 29725 |
| 120 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4047 |
| 121 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +9 | 29991 |
| 122 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +9 | 11858 |
| 123 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28062 |
| 124 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 10522 |
| 125 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +9 | 27095 |
| 126 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2122 |
| 127 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4855 |
| 128 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +8 | 24074 |
| 129 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +8 | 10174 |
| 130 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +8 | 2296 |
| 131 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19358 |
| 132 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +8 | 44605 |
| 133 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +8 | 9714 |
| 134 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9777 |
| 135 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +8 | 5220 |
| 136 | [anbeime/skill](https://github.com/anbeime/skill) | +8 | 4930 |
| 137 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +8 | 5862 |
| 138 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14342 |
| 139 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1482 |
| 140 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +8 | 9755 |
| 141 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +8 | 0 |
| 142 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +7 | 5189 |
| 143 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6676 |
| 144 | [openai/skills](https://github.com/openai/skills) | +7 | 24619 |
| 145 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +7 | 27440 |
| 146 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +7 | 14378 |
| 147 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1798 |
| 148 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 5029 |
| 149 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +7 | 834 |
| 150 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +7 | 568 |
| 151 | [browser-act/skills](https://github.com/browser-act/skills) | +7 | 5262 |
| 152 | [littledivy/mimic](https://github.com/littledivy/mimic) | +7 | 1520 |
| 153 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +7 | 7287 |
| 154 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +7 | 5860 |
| 155 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +7 | 15681 |
| 156 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +7 | 2047 |
| 157 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3479 |
| 158 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +6 | 17077 |
| 159 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1910 |
| 160 | [google/skills](https://github.com/google/skills) | +6 | 16174 |
| 161 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +6 | 8422 |
| 162 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +6 | 1771 |
| 163 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +6 | 1629 |
| 164 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +6 | 8690 |
| 165 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +6 | 8033 |
| 166 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +6 | 6575 |
| 167 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +6 | 3122 |
| 168 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +6 | 930 |
| 169 | [anthropics/jacobian-lens](https://github.com/anthropics/jacobian-lens) | +6 | 1701 |
| 170 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +6 | 889 |
| 171 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +6 | 567 |
| 172 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +6 | 9313 |
| 173 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +6 | 7884 |
| 174 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 9868 |
| 175 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +6 | 2921 |
| 176 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 29838 |
| 177 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5852 |
| 178 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +5 | 3355 |
| 179 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +5 | 2495 |
| 180 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +5 | 10465 |
| 181 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +5 | 1810 |
| 182 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +5 | 1162 |
| 183 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +5 | 1536 |
| 184 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +5 | 6009 |
| 185 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 1220 |
| 186 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +5 | 1744 |
| 187 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1172 |
| 188 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7041 |
| 189 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1288 |
| 190 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 683 |
| 191 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 1035 |
| 192 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 513 |
| 193 | [openai/plugins](https://github.com/openai/plugins) | +5 | 4978 |
| 194 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +5 | 3220 |
| 195 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1226 |
| 196 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5396 |
| 197 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +4 | 2353 |
| 198 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4 | 40902 |
| 199 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +4 | 23990 |
| 200 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +4 | 3030 |
| 201 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14550 |
| 202 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8398 |
| 203 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 396 |
| 204 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5865 |
| 205 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +4 | 27870 |
| 206 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +4 | 27210 |
| 207 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 396 |
| 208 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 744 |
| 209 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 658 |
| 210 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 838 |
| 211 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4599 |
| 212 | [dataease/dataease](https://github.com/dataease/dataease) | +4 | 24302 |
| 213 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +3 | 1582 |
| 214 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 598 |
| 215 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 398 |
| 216 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +3 | 5529 |
| 217 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9436 |
| 218 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 144 |
| 219 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 335 |
| 220 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1213 |
| 221 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +3 | 3299 |
| 222 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 395 |
| 223 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 76 |
| 224 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +3 | 7544 |
| 225 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2614 |
| 226 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9244 |
| 227 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +3 | 3143 |
| 228 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28252 |
| 229 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10436 |
| 230 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +3 | 27842 |
| 231 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11180 |
| 232 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6187 |
| 233 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +2 | 5213 |
| 234 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +2 | 204 |
| 235 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 440 |
| 236 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +2 | 302 |
| 237 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +2 | 900 |
| 238 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1289 |
| 239 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +2 | 418 |
| 240 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3925 |
| 241 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 74 |
| 242 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +2 | 301 |
| 243 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +2 | 6366 |
| 244 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +2 | 435 |
| 245 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 54 |
| 246 | [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer) | +2 | 734 |
| 247 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +2 | 2852 |
| 248 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1226 |
| 249 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 159 |
| 250 | [hiz0147/HizSteamButton](https://github.com/hiz0147/HizSteamButton) | +2 | 344 |
| 251 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +2 | 5134 |
| 252 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +2 | 698 |
| 253 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +2 | 541 |
| 254 | [XunMengWinter/xiaohongshu-assistant](https://github.com/XunMengWinter/xiaohongshu-assistant) | +2 | 111 |
| 255 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +2 | 6341 |
| 256 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +2 | 1629 |
| 257 | [shlokkhemani/rabbithole](https://github.com/shlokkhemani/rabbithole) | +2 | 299 |
| 258 | [InterfaceX-co-jp/genshijin](https://github.com/InterfaceX-co-jp/genshijin) | +2 | 302 |
| 259 | [Kirakun0328/text-to-vrma](https://github.com/Kirakun0328/text-to-vrma) | +2 | 122 |
| 260 | [callie0313/dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat) | +2 | 279 |
| 261 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +2 | 243 |
| 262 | [alex-durango/pingfusi](https://github.com/alex-durango/pingfusi) | +2 | 91 |
| 263 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1256 |
| 264 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 4948 |
| 265 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10359 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3074 |
| 267 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 492 |
| 268 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 98 |
| 269 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 270 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +2 | 9265 |
| 271 | [iss4cf0ng/Alien](https://github.com/iss4cf0ng/Alien) | +2 | 259 |
| 272 | [FongMi/TV](https://github.com/FongMi/TV) | +2 | 8964 |
| 273 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +1 | 917 |
| 274 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 883 |
| 275 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +1 | 481 |
| 276 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2909 |
| 277 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +1 | 12214 |
| 278 | [angieruiz17/claude-fintech-skills](https://github.com/angieruiz17/claude-fintech-skills) | +1 | 136 |
| 279 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1031 |
| 280 | [fzrilsh/bercocok-tanam](https://github.com/fzrilsh/bercocok-tanam) | +1 | 237 |
| 281 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +1 | 405 |
| 282 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +1 | 255 |
| 283 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 72 |
| 284 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3460 |
| 285 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 286 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 287 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 256 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2840 |
| 289 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 193 |
| 290 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1099 |
| 291 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +1 | 372 |
| 292 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 276 |
| 293 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 8 |
| 294 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 317 |
| 295 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 296 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3893 |
| 297 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 110 |
| 298 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 57 |
| 299 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 35 |
| 300 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1962 |
