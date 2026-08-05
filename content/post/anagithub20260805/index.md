---
title: "2026-08-05 GitHub增长趋势报告"
description: "1.reverse-skill+7 2.iFixAi+5 3.TencentDB-Agent-Memory+5 4.video-use+3 5.DeepSeek-Reasonix+3"
date: 2026-08-05T21:10:53+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-05 21:10:53

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
        'daily': {"categories": ["omnigent-ai/omnigent", "productdevbook/hucre", "Yuan1z0825/nature-skills", "Osmantic/ODS", "virgiliojr94/book-to-skill", "autonomous-ai/autonomous-computer", "makerspet/oomwoo", "earthtojake/text-to-cad", "chuspeeism/dashi-ppt-skill", "usestrix/strix", "mcncarl/yichen-skills", "Yu9191/wloc", "crazyykhllc-bit/CyberPPT", "Jaycheng1103/chatgpt-video-editing-skills", "diegosouzapw/OmniRoute", "esengine/DeepSeek-Reasonix", "browser-use/video-use", "TencentCloud/TencentDB-Agent-Memory", "ifixai-ai/iFixAi", "zhaoxuya520/reverse-skill"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 7]},
        'weekly': {"categories": ["emilkowalski/skills", "iOfficeAI/OfficeCLI", "andrewyng/openworker", "ifixai-ai/iFixAi", "opengeos/GeoLibre", "pascalorg/editor", "esengine/DeepSeek-Reasonix", "bashalarmistalt/decimen-optical-transfer", "TencentCloud/TencentDB-Agent-Memory", "usestrix/strix", "diegosouzapw/OmniRoute", "ayghri/i-have-adhd", "openai/codex-security", "MoonshotAI/Kimi-K3", "stablyai/orca", "block/buzz", "virgiliojr94/book-to-skill", "yc-software/qm", "zhaoxuya520/reverse-skill", "firecrawl/pdf-inspector"], "data": [8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 11, 13, 17, 18, 18, 19, 23, 26, 28]},
        'monthly': {"categories": ["x4gKing/X4G", "agentscope-ai/QwenPaw", "andrewyng/openworker", "oblien/openship", "calesthio/OpenMontage", "ayghri/i-have-adhd", "k1tbyte/Wand-Enhancer", "HKUDS/Vibe-Trading", "bradautomates/claude-video", "emilkowalski/skills", "langchain-ai/openwiki", "Fei-Away/Codex-Dream-Skin", "usestrix/strix", "Zackriya-Solutions/meetily", "block/buzz", "herdrdev/herdr", "iOfficeAI/OfficeCLI", "stablyai/orca", "JustVugg/colibri", "diegosouzapw/OmniRoute"], "data": [44, 45, 46, 49, 50, 52, 58, 60, 61, 62, 63, 64, 68, 69, 72, 75, 77, 93, 96, 108]}
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
| 1 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +7 | 19019 |
| 2 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5 | 5689 |
| 3 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 14965 |
| 4 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 19710 |
| 5 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +3 | 31524 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 40650 |
| 7 | [Jaycheng1103/chatgpt-video-editing-skills](https://github.com/Jaycheng1103/chatgpt-video-editing-skills) | +3 | 373 |
| 8 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +2 | 1525 |
| 9 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +2 | 8196 |
| 10 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +2 | 1711 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | +2 | 48911 |
| 12 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +2 | 4737 |
| 13 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +2 | 12902 |
| 14 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +2 | 7856 |
| 15 | [autonomous-ai/autonomous-computer](https://github.com/autonomous-ai/autonomous-computer) | +2 | 1114 |
| 16 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +2 | 16950 |
| 17 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +2 | 4009 |
| 18 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +2 | 33546 |
| 19 | [productdevbook/hucre](https://github.com/productdevbook/hucre) | +2 | 1799 |
| 20 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +2 | 8175 |
| 21 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +2 | 3259 |
| 22 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2 | 25656 |
| 23 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 19225 |
| 24 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +2 | 557 |
| 25 | [blader/humanizer](https://github.com/blader/humanizer) | +2 | 33733 |
| 26 | [block/buzz](https://github.com/block/buzz) | +1 | 23045 |
| 27 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +1 | 4706 |
| 28 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +1 | 4320 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +1 | 19110 |
| 30 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +1 | 1629 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +28 | 11313 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +26 | 19019 |
| 3 | [yc-software/qm](https://github.com/yc-software/qm) | +23 | 11645 |
| 4 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +19 | 16950 |
| 5 | [block/buzz](https://github.com/block/buzz) | +18 | 23045 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +18 | 38085 |
| 7 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +17 | 8099 |
| 8 | [openai/codex-security](https://github.com/openai/codex-security) | +13 | 8607 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +11 | 17231 |
| 10 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +10 | 40651 |
| 11 | [usestrix/strix](https://github.com/usestrix/strix) | +10 | 48911 |
| 12 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +9 | 14965 |
| 13 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +9 | 4680 |
| 14 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +9 | 31524 |
| 15 | [pascalorg/editor](https://github.com/pascalorg/editor) | +9 | 21142 |
| 16 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +9 | 5455 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +8 | 5689 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +8 | 13091 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +8 | 25813 |
| 20 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +8 | 25656 |
| 21 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +8 | 16070 |
| 22 | [digimata/quill](https://github.com/digimata/quill) | +8 | 3694 |
| 23 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +7 | 28672 |
| 24 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +7 | 19110 |
| 25 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +7 | 3259 |
| 26 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +7 | 7599 |
| 27 | [browser-use/video-use](https://github.com/browser-use/video-use) | +6 | 19710 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 33547 |
| 29 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +6 | 22209 |
| 30 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +6 | 49386 |
| 31 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +6 | 33546 |
| 32 | [different-ai/openwork](https://github.com/different-ai/openwork) | +6 | 21085 |
| 33 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +6 | 2050 |
| 34 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 22844 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +6 | 43246 |
| 36 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 14068 |
| 37 | [multica-ai/multica](https://github.com/multica-ai/multica) | +5 | 44227 |
| 38 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +5 | 46014 |
| 39 | [antirez/ds4](https://github.com/antirez/ds4) | +5 | 20663 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 22169 |
| 41 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +5 | 7604 |
| 42 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +5 | 18925 |
| 43 | [digimata/parrot](https://github.com/digimata/parrot) | +5 | 1125 |
| 44 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +5 | 8574 |
| 45 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +4 | 27950 |
| 46 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +4 | 5093 |
| 47 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +4 | 37602 |
| 48 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 6642 |
| 49 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +4 | 7908 |
| 50 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +4 | 3293 |
| 51 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 29832 |
| 52 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +4 | 24644 |
| 53 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 54 | [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | +3 | 255 |
| 55 | [snekxs/openmouse](https://github.com/snekxs/openmouse) | +3 | 874 |
| 56 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +3 | 8196 |
| 57 | [Jaycheng1103/chatgpt-video-editing-skills](https://github.com/Jaycheng1103/chatgpt-video-editing-skills) | +3 | 373 |
| 58 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +3 | 879 |
| 59 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 45297 |
| 60 | [autonomous-ai/autonomous-computer](https://github.com/autonomous-ai/autonomous-computer) | +3 | 1114 |
| 61 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +3 | 23872 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +3 | 33734 |
| 63 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +3 | 2032 |
| 64 | [decolua/9router](https://github.com/decolua/9router) | +3 | 24737 |
| 65 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +3 | 12902 |
| 66 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 8347 |
| 67 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +3 | 944 |
| 68 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +3 | 4009 |
| 69 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +3 | 1722 |
| 70 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +3 | 22509 |
| 71 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +3 | 6641 |
| 72 | [tytsxai/IDM-Activation-Script-Chinese](https://github.com/tytsxai/IDM-Activation-Script-Chinese) | +3 | 1509 |
| 73 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +3 | 14290 |
| 74 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +3 | 3566 |
| 75 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 29645 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +3 | 43127 |
| 77 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +3 | 16791 |
| 78 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +3 | 1656 |
| 79 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +3 | 2469 |
| 80 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 9236 |
| 81 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 32580 |
| 82 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +3 | 3128 |
| 83 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +3 | 2074 |
| 84 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +3 | 10406 |
| 85 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +2 | 4706 |
| 86 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2 | 44511 |
| 87 | [EKKOLearnAI/hermes-studio](https://github.com/EKKOLearnAI/hermes-studio) | +2 | 9779 |
| 88 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +2 | 4423 |
| 89 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +2 | 1525 |
| 90 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +2 | 1711 |
| 91 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +2 | 4737 |
| 92 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +2 | 7856 |
| 93 | [productdevbook/hucre](https://github.com/productdevbook/hucre) | +2 | 1799 |
| 94 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +2 | 8175 |
| 95 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 13423 |
| 96 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +2 | 6396 |
| 97 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +2 | 6538 |
| 98 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +2 | 3493 |
| 99 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 19225 |
| 100 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +2 | 557 |
| 101 | [voicetreelab/voicetree](https://github.com/voicetreelab/voicetree) | +2 | 907 |
| 102 | [malisper/pgrust](https://github.com/malisper/pgrust) | +2 | 4004 |
| 103 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +2 | 1629 |
| 104 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +2 | 1741 |
| 105 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +2 | 6154 |
| 106 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +2 | 5792 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2 | 34955 |
| 108 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 60185 |
| 109 | [openai/skills](https://github.com/openai/skills) | +2 | 24551 |
| 110 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +2 | 7895 |
| 111 | [suleimanodetoro/skills](https://github.com/suleimanodetoro/skills) | +2 | 769 |
| 112 | [xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp) | +2 | 663 |
| 113 | [gadievron/raptor](https://github.com/gadievron/raptor) | +2 | 3523 |
| 114 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +2 | 6004 |
| 115 | [yangtiming/Fast-SAM-3D-Body](https://github.com/yangtiming/Fast-SAM-3D-Body) | +2 | 354 |
| 116 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +2 | 41030 |
| 117 | [123panNextGen/123pan](https://github.com/123panNextGen/123pan) | +2 | 271 |
| 118 | [reflex-dev/xy](https://github.com/reflex-dev/xy) | +2 | 1529 |
| 119 | [frenzymath/Danus](https://github.com/frenzymath/Danus) | +2 | 143 |
| 120 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +2 | 258 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +108 | 40651 |
| 2 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +96 | 22844 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +93 | 38085 |
| 4 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +77 | 25813 |
| 5 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +75 | 24644 |
| 6 | [block/buzz](https://github.com/block/buzz) | +72 | 23045 |
| 7 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +69 | 28317 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | +68 | 48911 |
| 9 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 13263 |
| 10 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +63 | 14204 |
| 11 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +62 | 25656 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +61 | 14068 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +60 | 29832 |
| 14 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +58 | 14962 |
| 15 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +52 | 17231 |
| 16 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +50 | 45297 |
| 17 | [oblien/openship](https://github.com/oblien/openship) | +49 | 10330 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +46 | 13091 |
| 19 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +45 | 33546 |
| 20 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +44 | 7908 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +44 | 49386 |
| 22 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +44 | 37602 |
| 23 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +43 | 22209 |
| 24 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +38 | 18925 |
| 25 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +37 | 46014 |
| 26 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +36 | 8099 |
| 27 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +35 | 16950 |
| 28 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 9881 |
| 29 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 43127 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 39611 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +33 | 43246 |
| 32 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +31 | 16070 |
| 33 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +31 | 7593 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +29 | 28672 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +29 | 44227 |
| 36 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +29 | 32580 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +29 | 33547 |
| 38 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +29 | 28452 |
| 39 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +28 | 19019 |
| 40 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +28 | 11313 |
| 41 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +28 | 9422 |
| 42 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +28 | 15051 |
| 43 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8574 |
| 44 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +27 | 9236 |
| 45 | [openai/codex-security](https://github.com/openai/codex-security) | +26 | 8607 |
| 46 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +26 | 7604 |
| 47 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +26 | 15648 |
| 48 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +26 | 6958 |
| 49 | [facebook/astryx](https://github.com/facebook/astryx) | +25 | 11720 |
| 50 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +25 | 41030 |
| 51 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +25 | 19683 |
| 52 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +25 | 31378 |
| 53 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 8682 |
| 54 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31038 |
| 55 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +24 | 31524 |
| 56 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 44511 |
| 57 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +24 | 22170 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +24 | 35949 |
| 59 | [yc-software/qm](https://github.com/yc-software/qm) | +23 | 11645 |
| 60 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +23 | 60185 |
| 61 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +23 | 19110 |
| 62 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +23 | 7599 |
| 63 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +23 | 4299 |
| 64 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +23 | 27950 |
| 65 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +23 | 4320 |
| 66 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +22 | 4737 |
| 67 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +21 | 4706 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +20 | 33734 |
| 69 | [browser-use/video-use](https://github.com/browser-use/video-use) | +20 | 19710 |
| 70 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +20 | 6954 |
| 71 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +20 | 3444 |
| 72 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +19 | 8196 |
| 73 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4281 |
| 74 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 6396 |
| 75 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +19 | 14965 |
| 76 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +19 | 16237 |
| 77 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +19 | 7856 |
| 78 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +19 | 4774 |
| 79 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +19 | 5627 |
| 80 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1990 |
| 81 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +18 | 3259 |
| 82 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +18 | 6641 |
| 83 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5354 |
| 84 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 13423 |
| 85 | [malisper/pgrust](https://github.com/malisper/pgrust) | +18 | 4004 |
| 86 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11105 |
| 87 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 9204 |
| 88 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +17 | 6154 |
| 89 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +16 | 3566 |
| 90 | [floci-io/floci](https://github.com/floci-io/floci) | +16 | 18256 |
| 91 | [decolua/9router](https://github.com/decolua/9router) | +16 | 24737 |
| 92 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +16 | 34955 |
| 93 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +15 | 5689 |
| 94 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +15 | 12902 |
| 95 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +15 | 23872 |
| 96 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +15 | 3512 |
| 97 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +14 | 5455 |
| 98 | [pascalorg/editor](https://github.com/pascalorg/editor) | +14 | 21142 |
| 99 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3621 |
| 100 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +14 | 2531 |
| 101 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +14 | 2074 |
| 102 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +13 | 16791 |
| 103 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +12 | 2050 |
| 104 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 4094 |
| 105 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 10445 |
| 106 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +11 | 19225 |
| 107 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +11 | 29645 |
| 108 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +11 | 2586 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46667 |
| 110 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 32745 |
| 111 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +11 | 14235 |
| 112 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1913 |
| 113 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +11 | 9893 |
| 114 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +10 | 8175 |
| 115 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1512 |
| 116 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +10 | 2302 |
| 117 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +10 | 11835 |
| 118 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 1017 |
| 119 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +10 | 5792 |
| 120 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 29787 |
| 121 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +10 | 26496 |
| 122 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1810 |
| 123 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +10 | 9699 |
| 124 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4009 |
| 125 | [anbeime/skill](https://github.com/anbeime/skill) | +9 | 4784 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +9 | 27342 |
| 127 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 27969 |
| 128 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1966 |
| 129 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +9 | 26989 |
| 130 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4832 |
| 131 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +8 | 10068 |
| 132 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +8 | 9567 |
| 133 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +8 | 44520 |
| 134 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9712 |
| 135 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6642 |
| 136 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +8 | 5849 |
| 137 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +8 | 5166 |
| 138 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 7895 |
| 139 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1478 |
| 140 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +8 | 7208 |
| 141 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +8 | 15624 |
| 142 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +8 | 0 |
| 143 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 7775 |
| 144 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +7 | 5093 |
| 145 | [openai/skills](https://github.com/openai/skills) | +7 | 24551 |
| 146 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +7 | 14290 |
| 147 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1781 |
| 148 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +7 | 1525 |
| 149 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 5000 |
| 150 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +7 | 831 |
| 151 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +7 | 3127 |
| 152 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +7 | 558 |
| 153 | [browser-act/skills](https://github.com/browser-act/skills) | +7 | 5209 |
| 154 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +7 | 1983 |
| 155 | [google-research/tabfm](https://github.com/google-research/tabfm) | +7 | 2356 |
| 156 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 5876 |
| 157 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3388 |
| 158 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 2890 |
| 159 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29775 |
| 160 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1896 |
| 161 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +6 | 8347 |
| 162 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +6 | 16989 |
| 163 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +6 | 1558 |
| 164 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +6 | 1722 |
| 165 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +6 | 8656 |
| 166 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +6 | 2089 |
| 167 | [mcncarl/yichen-skills](https://github.com/mcncarl/yichen-skills) | +6 | 1711 |
| 168 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +6 | 6538 |
| 169 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +6 | 809 |
| 170 | [jacob-bd/gemini-notebook-mcp-cli](https://github.com/jacob-bd/gemini-notebook-mcp-cli) | +6 | 5744 |
| 171 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +6 | 924 |
| 172 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +6 | 2133 |
| 173 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +6 | 878 |
| 174 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +6 | 539 |
| 175 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +6 | 9242 |
| 176 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1140 |
| 177 | [openai/plugins](https://github.com/openai/plugins) | +6 | 4938 |
| 178 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5856 |
| 179 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +5 | 2469 |
| 180 | [google/skills](https://github.com/google/skills) | +5 | 15631 |
| 181 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +5 | 10406 |
| 182 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +5 | 1096 |
| 183 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +5 | 1656 |
| 184 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1270 |
| 185 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 681 |
| 186 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 989 |
| 187 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 496 |
| 188 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +5 | 3171 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +5 | 5834 |
| 190 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1204 |
| 191 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 9230 |
| 192 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5329 |
| 193 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4 | 40862 |
| 194 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +4 | 23891 |
| 195 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14519 |
| 196 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7012 |
| 197 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8348 |
| 198 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 390 |
| 199 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5483 |
| 200 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +4 | 27753 |
| 201 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1172 |
| 202 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +4 | 27133 |
| 203 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 394 |
| 204 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3256 |
| 205 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 733 |
| 206 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +4 | 7491 |
| 207 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +4 | 2028 |
| 208 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 651 |
| 209 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +4 | 741 |
| 210 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +4 | 1054 |
| 211 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 820 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3117 |
| 213 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28183 |
| 214 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4583 |
| 215 | [dataease/dataease](https://github.com/dataease/dataease) | +4 | 24300 |
| 216 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +3 | 2255 |
| 217 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +3 | 1400 |
| 218 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +3 | 879 |
| 219 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 591 |
| 220 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 389 |
| 221 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9384 |
| 222 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 142 |
| 223 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 334 |
| 224 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +3 | 6346 |
| 225 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 391 |
| 226 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +3 | 681 |
| 227 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 76 |
| 228 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2561 |
| 229 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +3 | 626 |
| 230 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9245 |
| 231 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10413 |
| 232 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +3 | 27654 |
| 233 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11165 |
| 234 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6166 |
| 235 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +2 | 5098 |
| 236 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 412 |
| 237 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +2 | 261 |
| 238 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +2 | 1166 |
| 239 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1272 |
| 240 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +2 | 376 |
| 241 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3909 |
| 242 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 72 |
| 243 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +2 | 298 |
| 244 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +2 | 428 |
| 245 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 53 |
| 246 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +2 | 2822 |
| 247 | [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer) | +2 | 710 |
| 248 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1198 |
| 249 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 158 |
| 250 | [hiz0147/HizSteamButton](https://github.com/hiz0147/HizSteamButton) | +2 | 343 |
| 251 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +2 | 5108 |
| 252 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +2 | 540 |
| 253 | [XunMengWinter/xiaohongshu-assistant](https://github.com/XunMengWinter/xiaohongshu-assistant) | +2 | 109 |
| 254 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +2 | 6337 |
| 255 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +2 | 148 |
| 256 | [hzm0321/real-time-fund](https://github.com/hzm0321/real-time-fund) | +2 | 1626 |
| 257 | [shlokkhemani/rabbithole](https://github.com/shlokkhemani/rabbithole) | +2 | 296 |
| 258 | [InterfaceX-co-jp/genshijin](https://github.com/InterfaceX-co-jp/genshijin) | +2 | 295 |
| 259 | [Kirakun0328/text-to-vrma](https://github.com/Kirakun0328/text-to-vrma) | +2 | 119 |
| 260 | [callie0313/dylan-heartbeat](https://github.com/callie0313/dylan-heartbeat) | +2 | 267 |
| 261 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 4905 |
| 262 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1235 |
| 263 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10352 |
| 264 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 370 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3052 |
| 266 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 433 |
| 267 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 98 |
| 268 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 429 |
| 269 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +2 | 9250 |
| 270 | [iss4cf0ng/Alien](https://github.com/iss4cf0ng/Alien) | +2 | 253 |
| 271 | [FongMi/TV](https://github.com/FongMi/TV) | +2 | 8888 |
| 272 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 861 |
| 273 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2901 |
| 274 | [angieruiz17/claude-fintech-skills](https://github.com/angieruiz17/claude-fintech-skills) | +1 | 136 |
| 275 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +1 | 12194 |
| 276 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1026 |
| 277 | [fzrilsh/bercocok-tanam](https://github.com/fzrilsh/bercocok-tanam) | +1 | 229 |
| 278 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3441 |
| 279 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 72 |
| 280 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 281 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 282 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 241 |
| 283 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2832 |
| 284 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 183 |
| 285 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1089 |
| 286 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 262 |
| 287 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 8 |
| 288 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 317 |
| 289 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 290 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3883 |
| 291 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 106 |
| 292 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 56 |
| 293 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 33 |
| 294 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1947 |
| 295 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 166 |
| 296 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 297 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 186 |
| 298 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +1 | 93 |
| 299 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +1 | 2942 |
| 300 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 839 |
