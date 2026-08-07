---
title: "2026-08-07 GitHub增长趋势报告"
description: "1.TencentDB-Agent-Memory+5 2.crm+4 3.OmniRoute+4 4.opencodex+4 5.QwenPaw+4"
date: 2026-08-07T00:53:07+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-07 00:53:07

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
        'daily': {"categories": ["rocketride-org/rocketride-server", "nestjs-redisx/nestjs-redisx", "KKKKhazix/human-writing", "getpaseo/paseo", "pranshuparmar/witr", "multica-ai/multica", "tt-a1i/archify", "stablyai/orca", "block/buzz", "brightdata/cli", "herdrdev/herdr", "MadsLorentzen/ai-job-search", "makerspet/oomwoo", "ben-z/findphone", "hugohe3/ppt-master", "agentscope-ai/QwenPaw", "lidge-jun/opencodex", "diegosouzapw/OmniRoute", "trycompai/crm", "TencentCloud/TencentDB-Agent-Memory"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]},
        'weekly': {"categories": ["tirth8205/code-review-graph", "multica-ai/multica", "Yuan1z0825/nature-skills", "ayghri/i-have-adhd", "hugohe3/ppt-master", "iOfficeAI/OfficeCLI", "lidge-jun/opencodex", "agentscope-ai/QwenPaw", "andrewyng/openworker", "ifixai-ai/iFixAi", "bashalarmistalt/decimen-optical-transfer", "stablyai/orca", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute", "TencentCloud/TencentDB-Agent-Memory", "trycompai/crm", "block/buzz", "yc-software/qm", "zhaoxuya520/reverse-skill", "firecrawl/pdf-inspector"], "data": [7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 10, 11, 11, 13, 14, 15, 16, 24, 26, 27]},
        'monthly': {"categories": ["calesthio/OpenMontage", "x4gKing/X4G", "andrewyng/openworker", "agentscope-ai/QwenPaw", "oblien/openship", "k1tbyte/Wand-Enhancer", "ayghri/i-have-adhd", "Zackriya-Solutions/meetily", "bradautomates/claude-video", "HKUDS/Vibe-Trading", "emilkowalski/skills", "usestrix/strix", "Fei-Away/Codex-Dream-Skin", "herdrdev/herdr", "block/buzz", "iOfficeAI/OfficeCLI", "stablyai/orca", "JustVugg/colibri", "diegosouzapw/OmniRoute", "MadsLorentzen/ai-job-search"], "data": [44, 44, 47, 48, 49, 52, 53, 54, 56, 59, 60, 61, 64, 74, 74, 78, 93, 97, 103, 122]}
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
| 1 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 16375 |
| 2 | [trycompai/crm](https://github.com/trycompai/crm) | +4 | 7196 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4 | 41702 |
| 4 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 8062 |
| 5 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 34150 |
| 6 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 43519 |
| 7 | [ben-z/findphone](https://github.com/ben-z/findphone) | +3 | 831 |
| 8 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +3 | 8006 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2 | 30513 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +2 | 25116 |
| 11 | [brightdata/cli](https://github.com/brightdata/cli) | +2 | 1300 |
| 12 | [block/buzz](https://github.com/block/buzz) | +2 | 24245 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +2 | 38958 |
| 14 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +2 | 9850 |
| 15 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2 | 44497 |
| 16 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +2 | 19252 |
| 17 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +2 | 12481 |
| 18 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +2 | 1569 |
| 19 | [nestjs-redisx/nestjs-redisx](https://github.com/nestjs-redisx/nestjs-redisx) | +2 | 50 |
| 20 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +2 | 5711 |
| 21 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +2 | 1013 |
| 22 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +2 | 4578 |
| 23 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +2 | 17628 |
| 24 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +2 | 19836 |
| 25 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29723 |
| 26 | [uber/ADR](https://github.com/uber/ADR) | +2 | 1241 |
| 27 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +2 | 6255 |
| 28 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +1 | 4616 |
| 29 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +1 | 3986 |
| 30 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +1 | 2278 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +27 | 12433 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +26 | 19836 |
| 3 | [yc-software/qm](https://github.com/yc-software/qm) | +24 | 12042 |
| 4 | [block/buzz](https://github.com/block/buzz) | +16 | 24245 |
| 5 | [trycompai/crm](https://github.com/trycompai/crm) | +15 | 7196 |
| 6 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +14 | 16375 |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +13 | 41702 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +11 | 17628 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +11 | 38958 |
| 10 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +10 | 4937 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +9 | 6255 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +9 | 13315 |
| 13 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 34150 |
| 14 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 8062 |
| 15 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +8 | 26184 |
| 16 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 43519 |
| 17 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +8 | 17760 |
| 18 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 33772 |
| 19 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 44497 |
| 20 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +7 | 29021 |
| 21 | [digimata/quill](https://github.com/digimata/quill) | +7 | 3715 |
| 22 | [browser-use/video-use](https://github.com/browser-use/video-use) | +6 | 19881 |
| 23 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 26374 |
| 24 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +6 | 3317 |
| 25 | [openai/codex-security](https://github.com/openai/codex-security) | +6 | 9052 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +6 | 49589 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +5 | 30513 |
| 28 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +5 | 8006 |
| 29 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 1013 |
| 30 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +5 | 25116 |
| 31 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +5 | 22361 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 22478 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +5 | 19376 |
| 34 | [antirez/ds4](https://github.com/antirez/ds4) | +5 | 20798 |
| 35 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +5 | 23028 |
| 36 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 14281 |
| 37 | [pascalorg/editor](https://github.com/pascalorg/editor) | +5 | 21177 |
| 38 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +5 | 5505 |
| 39 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +4 | 4578 |
| 40 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +4 | 2278 |
| 41 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +4 | 16221 |
| 42 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 46113 |
| 43 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +4 | 19252 |
| 44 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +4 | 1050 |
| 45 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +4 | 28070 |
| 46 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 30062 |
| 47 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +4 | 8146 |
| 48 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 19045 |
| 49 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +3 | 3986 |
| 50 | [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | +3 | 261 |
| 51 | [ben-z/findphone](https://github.com/ben-z/findphone) | +3 | 831 |
| 52 | [brightdata/cli](https://github.com/brightdata/cli) | +3 | 1300 |
| 53 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +3 | 5711 |
| 54 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +3 | 8233 |
| 55 | [uber/ADR](https://github.com/uber/ADR) | +3 | 1241 |
| 56 | [snekxs/openmouse](https://github.com/snekxs/openmouse) | +3 | 959 |
| 57 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +3 | 8287 |
| 58 | [Jaycheng1103/chatgpt-video-editing-skills](https://github.com/Jaycheng1103/chatgpt-video-editing-skills) | +3 | 394 |
| 59 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +3 | 3672 |
| 60 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +3 | 9079 |
| 61 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 8012 |
| 62 | [autonomous-ai/autonomous-computer](https://github.com/autonomous-ai/autonomous-computer) | +3 | 1159 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +3 | 34025 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +3 | 43351 |
| 65 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +3 | 5158 |
| 66 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 60263 |
| 67 | [different-ai/openwork](https://github.com/different-ai/openwork) | +3 | 21283 |
| 68 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +3 | 2862 |
| 69 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +3 | 12974 |
| 70 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +3 | 4034 |
| 71 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +3 | 1748 |
| 72 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +3 | 22573 |
| 73 | [decolua/9router](https://github.com/decolua/9router) | +3 | 24832 |
| 74 | [tytsxai/IDM-Activation-Script-Chinese](https://github.com/tytsxai/IDM-Activation-Script-Chinese) | +3 | 23 |
| 75 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +3 | 7665 |
| 76 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +3 | 2957 |
| 77 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +3 | 2489 |
| 78 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 32747 |
| 79 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +2 | 4616 |
| 80 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 17042 |
| 81 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +2 | 4816 |
| 82 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2 | 44633 |
| 83 | [EKKOLearnAI/hermes-studio](https://github.com/EKKOLearnAI/hermes-studio) | +2 | 9812 |
| 84 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2 | 45549 |
| 85 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 23932 |
| 86 | [oblien/openship](https://github.com/oblien/openship) | +2 | 10373 |
| 87 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +2 | 12481 |
| 88 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +2 | 1569 |
| 89 | [nestjs-redisx/nestjs-redisx](https://github.com/nestjs-redisx/nestjs-redisx) | +2 | 50 |
| 90 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +2 | 3199 |
| 91 | [itayinbarr/little-coder](https://github.com/itayinbarr/little-coder) | +2 | 2305 |
| 92 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29723 |
| 93 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +2 | 7839 |
| 94 | [qwen-code-dev-bot/oh-my-cli](https://github.com/qwen-code-dev-bot/oh-my-cli) | +2 | 650 |
| 95 | [EgalitarianMonkey/hometube](https://github.com/EgalitarianMonkey/hometube) | +2 | 1219 |
| 96 | [gajus/zod-compiler](https://github.com/gajus/zod-compiler) | +2 | 627 |
| 97 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +2 | 1951 |
| 98 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +2 | 1530 |
| 99 | [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) | +2 | 892 |
| 100 | [xuzhougeng/wisp-science](https://github.com/xuzhougeng/wisp-science) | +2 | 980 |
| 101 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 13516 |
| 102 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2 | 29901 |
| 103 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +2 | 1796 |
| 104 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +2 | 8392 |
| 105 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +2 | 10139 |
| 106 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +2 | 6563 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 19309 |
| 108 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +2 | 32837 |
| 109 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +2 | 1646 |
| 110 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +2 | 1811 |
| 111 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +2 | 6209 |
| 112 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2 | 35013 |
| 113 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +2 | 14336 |
| 114 | [openai/skills](https://github.com/openai/skills) | +2 | 24582 |
| 115 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +2 | 6664 |
| 116 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +2 | 7974 |
| 117 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29690 |
| 118 | [suleimanodetoro/skills](https://github.com/suleimanodetoro/skills) | +2 | 782 |
| 119 | [xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp) | +2 | 672 |
| 120 | [OrangesHuang/Resonance](https://github.com/OrangesHuang/Resonance) | +2 | 126 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +122 | 30513 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +103 | 41702 |
| 3 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +97 | 23028 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +93 | 38958 |
| 5 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +78 | 26184 |
| 6 | [block/buzz](https://github.com/block/buzz) | +74 | 24246 |
| 7 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +74 | 25116 |
| 8 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 13334 |
| 9 | [usestrix/strix](https://github.com/usestrix/strix) | +61 | 49375 |
| 10 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +60 | 26374 |
| 11 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +59 | 30062 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +56 | 14281 |
| 13 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +54 | 28394 |
| 14 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +53 | 17760 |
| 15 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +52 | 15236 |
| 16 | [oblien/openship](https://github.com/oblien/openship) | +49 | 10373 |
| 17 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +48 | 34150 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +47 | 13315 |
| 19 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +44 | 8012 |
| 20 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +44 | 45549 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +43 | 49589 |
| 22 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +42 | 14273 |
| 23 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +40 | 22361 |
| 24 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +38 | 37838 |
| 25 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +37 | 19045 |
| 26 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +36 | 8146 |
| 27 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +36 | 17628 |
| 28 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +36 | 46113 |
| 29 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 10056 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +35 | 43519 |
| 31 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +31 | 16221 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +31 | 39793 |
| 33 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +31 | 7678 |
| 34 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +30 | 8062 |
| 35 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 33772 |
| 36 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +30 | 9850 |
| 37 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +29 | 19836 |
| 38 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +29 | 29021 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +29 | 32747 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +28 | 44497 |
| 41 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +28 | 43351 |
| 42 | [openai/codex-security](https://github.com/openai/codex-security) | +27 | 9052 |
| 43 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +27 | 12433 |
| 44 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8574 |
| 45 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +26 | 9418 |
| 46 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +25 | 9079 |
| 47 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +25 | 32400 |
| 48 | [yc-software/qm](https://github.com/yc-software/qm) | +24 | 12042 |
| 49 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +24 | 16375 |
| 50 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +24 | 22478 |
| 51 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31120 |
| 52 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +23 | 19376 |
| 53 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +23 | 7665 |
| 54 | [marcelroed/gigatoken](https://github.com/marcelroed/gigatoken) | +23 | 3927 |
| 55 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +23 | 44633 |
| 56 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +23 | 4370 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36110 |
| 58 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +22 | 60263 |
| 59 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +22 | 15706 |
| 60 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +22 | 28480 |
| 61 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +22 | 15118 |
| 62 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +22 | 4805 |
| 63 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +21 | 4816 |
| 64 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +21 | 28070 |
| 65 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +20 | 4808 |
| 66 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +20 | 7005 |
| 67 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +20 | 41177 |
| 68 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +20 | 3473 |
| 69 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +20 | 4374 |
| 70 | [blader/humanizer](https://github.com/blader/humanizer) | +19 | 34025 |
| 71 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +19 | 8006 |
| 72 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4306 |
| 73 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 6504 |
| 74 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +19 | 19733 |
| 75 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +19 | 5663 |
| 76 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1991 |
| 77 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +18 | 3317 |
| 78 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +18 | 6871 |
| 79 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 13516 |
| 80 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5394 |
| 81 | [malisper/pgrust](https://github.com/malisper/pgrust) | +18 | 4019 |
| 82 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 6255 |
| 83 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +17 | 3672 |
| 84 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +17 | 8287 |
| 85 | [browser-use/video-use](https://github.com/browser-use/video-use) | +17 | 19881 |
| 86 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +17 | 16291 |
| 87 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11113 |
| 88 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 9263 |
| 89 | [facebook/astryx](https://github.com/facebook/astryx) | +16 | 11795 |
| 90 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +16 | 35013 |
| 91 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +16 | 31443 |
| 92 | [trycompai/crm](https://github.com/trycompai/crm) | +15 | 7196 |
| 93 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +15 | 6209 |
| 94 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +15 | 3520 |
| 95 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +14 | 5505 |
| 96 | [pascalorg/editor](https://github.com/pascalorg/editor) | +14 | 21177 |
| 97 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3727 |
| 98 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +14 | 2527 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +14 | 12974 |
| 100 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +14 | 2116 |
| 101 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +13 | 2278 |
| 102 | [every-app/open-seo](https://github.com/every-app/open-seo) | +13 | 10747 |
| 103 | [decolua/9router](https://github.com/decolua/9router) | +13 | 24832 |
| 104 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +12 | 17022 |
| 105 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 4370 |
| 106 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 32837 |
| 107 | [floci-io/floci](https://github.com/floci-io/floci) | +12 | 18286 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +11 | 29690 |
| 109 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +11 | 2623 |
| 110 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1933 |
| 111 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +10 | 4937 |
| 112 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +10 | 46732 |
| 113 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1521 |
| 114 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 29901 |
| 115 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +10 | 2329 |
| 116 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 1035 |
| 117 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +10 | 26540 |
| 118 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +10 | 10492 |
| 119 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1822 |
| 120 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 9932 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +9 | 23932 |
| 122 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +9 | 8233 |
| 123 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4034 |
| 124 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +9 | 11850 |
| 125 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28012 |
| 126 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +9 | 14305 |
| 127 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2116 |
| 128 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +9 | 27043 |
| 129 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4846 |
| 130 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +8 | 10139 |
| 131 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19309 |
| 132 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +8 | 44567 |
| 133 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +8 | 9620 |
| 134 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9740 |
| 135 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6664 |
| 136 | [anbeime/skill](https://github.com/anbeime/skill) | +8 | 4865 |
| 137 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +8 | 5858 |
| 138 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1481 |
| 139 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +8 | 9735 |
| 140 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +8 | 0 |
| 141 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +7 | 17042 |
| 142 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +7 | 5158 |
| 143 | [openai/skills](https://github.com/openai/skills) | +7 | 24582 |
| 144 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +7 | 27404 |
| 145 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +7 | 14336 |
| 146 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1793 |
| 147 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +7 | 5203 |
| 148 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 5018 |
| 149 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +7 | 7974 |
| 150 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +7 | 834 |
| 151 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +7 | 566 |
| 152 | [browser-act/skills](https://github.com/browser-act/skills) | +7 | 5237 |
| 153 | [littledivy/mimic](https://github.com/littledivy/mimic) | +7 | 1517 |
| 154 | [anthropics/jacobian-lens](https://github.com/anthropics/jacobian-lens) | +7 | 1694 |
| 155 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +7 | 7250 |
| 156 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +7 | 5826 |
| 157 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +7 | 15658 |
| 158 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +7 | 2019 |
| 159 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +7 | 7839 |
| 160 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3455 |
| 161 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 2910 |
| 162 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1904 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +6 | 8392 |
| 164 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +6 | 1748 |
| 165 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +6 | 1597 |
| 166 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +6 | 2192 |
| 167 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +6 | 8668 |
| 168 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +6 | 6563 |
| 169 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +6 | 3128 |
| 170 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +6 | 927 |
| 171 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +6 | 2155 |
| 172 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +6 | 883 |
| 173 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +6 | 553 |
| 174 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 5957 |
| 175 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +6 | 9289 |
| 176 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1159 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 29806 |
| 178 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5856 |
| 179 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +5 | 2957 |
| 180 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +5 | 2489 |
| 181 | [google/skills](https://github.com/google/skills) | +5 | 15776 |
| 182 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +5 | 10435 |
| 183 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +5 | 1796 |
| 184 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +5 | 1135 |
| 185 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +5 | 1530 |
| 186 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 1013 |
| 187 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +5 | 1708 |
| 188 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1281 |
| 189 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 682 |
| 190 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 1017 |
| 191 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 500 |
| 192 | [openai/plugins](https://github.com/openai/plugins) | +5 | 4958 |
| 193 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +5 | 3198 |
| 194 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1224 |
| 195 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 9714 |
| 196 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5372 |
| 197 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +4 | 2313 |
| 198 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4 | 40878 |
| 199 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +4 | 23953 |
| 200 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14536 |
| 201 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7035 |
| 202 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8374 |
| 203 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 391 |
| 204 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5509 |
| 205 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5852 |
| 206 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +4 | 27820 |
| 207 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +4 | 27187 |
| 208 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 395 |
| 209 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3281 |
| 210 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 737 |
| 211 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +4 | 7520 |
| 212 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 654 |
| 213 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 838 |
| 214 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28216 |
| 215 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4591 |
| 216 | [dataease/dataease](https://github.com/dataease/dataease) | +4 | 24300 |
| 217 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +3 | 1529 |
| 218 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 596 |
| 219 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 392 |
| 220 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9416 |
| 221 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 144 |
| 222 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 335 |
| 223 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1194 |
| 224 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 394 |
| 225 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 76 |
| 226 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +3 | 2028 |
| 227 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2593 |
| 228 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +3 | 643 |
| 229 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +3 | 1055 |
| 230 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9248 |
| 231 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +3 | 3130 |
| 232 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10425 |
| 233 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +3 | 27785 |
| 234 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11175 |
| 235 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6176 |
| 236 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +2 | 5155 |
| 237 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +2 | 201 |
| 238 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 430 |
| 239 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +2 | 281 |
| 240 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +2 | 895 |
| 241 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1285 |
| 242 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +2 | 405 |
| 243 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3919 |
| 244 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 74 |
| 245 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +2 | 300 |
| 246 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +2 | 6359 |
| 247 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +2 | 434 |
| 248 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 54 |
| 249 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +2 | 2839 |
| 250 | [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer) | +2 | 724 |
| 251 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1209 |
| 252 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 158 |
| 253 | [hiz0147/HizSteamButton](https://github.com/hiz0147/HizSteamButton) | +2 | 344 |
| 254 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +2 | 5126 |
| 255 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +2 | 690 |
| 256 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +2 | 540 |
| 257 | [XunMengWinter/xiaohongshu-assistant](https://github.com/XunMengWinter/xiaohongshu-assistant) | +2 | 111 |
| 258 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +2 | 6338 |
| 259 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +2 | 149 |
| 260 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +2 | 1627 |
| 261 | [shlokkhemani/rabbithole](https://github.com/shlokkhemani/rabbithole) | +2 | 299 |
| 262 | [InterfaceX-co-jp/genshijin](https://github.com/InterfaceX-co-jp/genshijin) | +2 | 300 |
| 263 | [Kirakun0328/text-to-vrma](https://github.com/Kirakun0328/text-to-vrma) | +2 | 119 |
| 264 | [callie0313/dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat) | +2 | 274 |
| 265 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 4924 |
| 266 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1248 |
| 267 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10355 |
| 268 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3060 |
| 269 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 98 |
| 270 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 271 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +2 | 9258 |
| 272 | [iss4cf0ng/Alien](https://github.com/iss4cf0ng/Alien) | +2 | 255 |
| 273 | [FongMi/TV](https://github.com/FongMi/TV) | +2 | 8941 |
| 274 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 869 |
| 275 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2905 |
| 276 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +1 | 12203 |
| 277 | [angieruiz17/claude-fintech-skills](https://github.com/angieruiz17/claude-fintech-skills) | +1 | 136 |
| 278 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1029 |
| 279 | [fzrilsh/bercocok-tanam](https://github.com/fzrilsh/bercocok-tanam) | +1 | 236 |
| 280 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 72 |
| 281 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +1 | 252 |
| 282 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3451 |
| 283 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 284 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 285 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 247 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2839 |
| 287 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 187 |
| 288 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1096 |
| 289 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +1 | 371 |
| 290 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 272 |
| 291 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 8 |
| 292 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 317 |
| 293 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 294 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3889 |
| 295 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 107 |
| 296 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 57 |
| 297 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 34 |
| 298 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1953 |
| 299 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 169 |
| 300 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
