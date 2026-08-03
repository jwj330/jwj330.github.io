---
title: "2026-08-03 GitHub增长趋势报告"
description: "1.reverse-skill+6 2.qm+5 3.Unlimited-OCR+3 4.TencentDB-Agent-Memory+3 5.pdf-inspector+3"
date: 2026-08-03T21:04:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-03 21:04:19

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
        'daily': {"categories": ["calesthio/OpenMontage", "Orkas-AI/Orkas", "antirez/ds4", "diegosouzapw/OmniRoute", "opengeos/GeoLibre", "powerycy/goutoujunshi", "callstack/agent-device", "block/buzz", "decolua/9router", "can1357/oh-my-pi", "open-jarvis/OpenJarvis", "tirth8205/code-review-graph", "andrewyng/openworker", "huangruiteng/loopx", "Yuan1z0825/nature-skills", "firecrawl/pdf-inspector", "TencentCloud/TencentDB-Agent-Memory", "baidu/Unlimited-OCR", "yc-software/qm", "zhaoxuya520/reverse-skill"], "data": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 6]},
        'weekly': {"categories": ["img2threejs/img2threejs", "CoreBunch/Instatic", "herdrdev/herdr", "agentscope-ai/QwenPaw", "JustVugg/colibri", "bryanthaboi/gen1recomp", "pascalorg/editor", "opengeos/GeoLibre", "1jehuang/jcode", "bradautomates/claude-video", "zhaoxuya520/reverse-skill", "usestrix/strix", "diegosouzapw/OmniRoute", "andrewyng/openworker", "firecrawl/pdf-inspector", "yc-software/qm", "ayghri/i-have-adhd", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz"], "data": [9, 9, 10, 10, 10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 16, 16, 18, 20, 21, 25]},
        'monthly': {"categories": ["Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "block/buzz", "emilkowalski/skills", "facebook/astryx", "bradautomates/claude-video", "iOfficeAI/OfficeCLI", "teamchong/pxpipe", "DeusData/codebase-memory-mcp", "alibaba/page-agent", "calesthio/OpenMontage", "k1tbyte/Wand-Enhancer", "JustVugg/colibri", "openai/codex-plugin-cc", "herdrdev/herdr", "stablyai/orca", "diegosouzapw/OmniRoute", "Zackriya-Solutions/meetily", "langchain-ai/openwiki", "usestrix/strix"], "data": [64, 71, 71, 73, 74, 74, 74, 81, 86, 92, 92, 93, 96, 101, 115, 117, 126, 134, 147, 150]}
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
| 1 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +6 | 15545 |
| 2 | [yc-software/qm](https://github.com/yc-software/qm) | +5 | 9389 |
| 3 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 21869 |
| 4 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +3 | 11979 |
| 5 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +3 | 7914 |
| 6 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +2 | 33060 |
| 7 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +2 | 1085 |
| 8 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +2 | 12432 |
| 9 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +2 | 28285 |
| 10 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +2 | 8268 |
| 11 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +2 | 21559 |
| 12 | [decolua/9router](https://github.com/decolua/9router) | +2 | 24576 |
| 13 | [block/buzz](https://github.com/block/buzz) | +2 | 21761 |
| 14 | [callstack/agent-device](https://github.com/callstack/agent-device) | +2 | 3916 |
| 15 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +2 | 1595 |
| 16 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +2 | 5159 |
| 17 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 38712 |
| 18 | [antirez/ds4](https://github.com/antirez/ds4) | +2 | 20319 |
| 19 | [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | +2 | 975 |
| 20 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +1 | 44884 |
| 21 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +1 | 15862 |
| 22 | [Mekotofeuka/MTPROTO_FIX_By_MEKO](https://github.com/Mekotofeuka/MTPROTO_FIX_By_MEKO) | +1 | 861 |
| 23 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +1 | 5079 |
| 24 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1 | 40725 |
| 25 | [adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide) | +1 | 7775 |
| 26 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +1 | 6327 |
| 27 | [digimata/parrot](https://github.com/digimata/parrot) | +1 | 1100 |
| 28 | [amitshekhariitbhu/llm-internals](https://github.com/amitshekhariitbhu/llm-internals) | +1 | 1382 |
| 29 | [frknkrc44/HMA-OSS](https://github.com/frknkrc44/HMA-OSS) | +1 | 2686 |
| 30 | [xingwudao/xquant-learning](https://github.com/xingwudao/xquant-learning) | +1 | 335 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +25 | 21761 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +21 | 36563 |
| 3 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +20 | 15862 |
| 4 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +18 | 16230 |
| 5 | [yc-software/qm](https://github.com/yc-software/qm) | +16 | 9389 |
| 6 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +16 | 7915 |
| 7 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +13 | 12432 |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +13 | 38712 |
| 9 | [usestrix/strix](https://github.com/usestrix/strix) | +13 | 47063 |
| 10 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +12 | 15545 |
| 11 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +12 | 13659 |
| 12 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 15543 |
| 13 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +11 | 5159 |
| 14 | [pascalorg/editor](https://github.com/pascalorg/editor) | +11 | 20917 |
| 15 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 1731 |
| 16 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +10 | 22456 |
| 17 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +10 | 32499 |
| 18 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +10 | 23936 |
| 19 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +9 | 7438 |
| 20 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +9 | 9364 |
| 21 | [digimata/quill](https://github.com/digimata/quill) | +8 | 3639 |
| 22 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +8 | 21869 |
| 23 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +8 | 24339 |
| 24 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +8 | 18382 |
| 25 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 6935 |
| 26 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 18646 |
| 27 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +7 | 4217 |
| 28 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +7 | 45713 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +7 | 42769 |
| 30 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +7 | 4721 |
| 31 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +6 | 28285 |
| 32 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +6 | 24756 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +6 | 32210 |
| 34 | [kvcache-ai/AgentENV](https://github.com/kvcache-ai/AgentENV) | +6 | 2825 |
| 35 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 16486 |
| 36 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +6 | 2910 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 39330 |
| 38 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 21559 |
| 39 | [different-ai/openwork](https://github.com/different-ai/openwork) | +5 | 20651 |
| 40 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +5 | 29459 |
| 41 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 2997 |
| 42 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +5 | 8574 |
| 43 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | +5 | 1262 |
| 44 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +5 | 3413 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 42865 |
| 46 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +5 | 2347 |
| 47 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +5 | 2776 |
| 48 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +5 | 375 |
| 49 | [antirez/ds4](https://github.com/antirez/ds4) | +4 | 20319 |
| 50 | [decolua/9router](https://github.com/decolua/9router) | +4 | 24576 |
| 51 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 6574 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +4 | 59946 |
| 53 | [digimata/parrot](https://github.com/digimata/parrot) | +4 | 1100 |
| 54 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +4 | 29840 |
| 55 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 56 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +4 | 13035 |
| 57 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +4 | 4121 |
| 58 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +4 | 4190 |
| 59 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +4 | 3247 |
| 60 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +4 | 48602 |
| 61 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +4 | 14009 |
| 62 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +4 | 11476 |
| 63 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +4 | 10300 |
| 64 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 2748 |
| 65 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +4 | 722 |
| 66 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +4 | 35736 |
| 67 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +4 | 1515 |
| 68 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +4 | 3348 |
| 69 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +4 | 12672 |
| 70 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +4 | 478 |
| 71 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 6126 |
| 72 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | +4 | 1147 |
| 73 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3 | 43528 |
| 74 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 8268 |
| 75 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +3 | 785 |
| 76 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 33060 |
| 77 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +3 | 11979 |
| 78 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 44884 |
| 79 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +3 | 1595 |
| 80 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 7536 |
| 81 | [tytsxai/IDM-Activation-Script-Chinese](https://github.com/tytsxai/IDM-Activation-Script-Chinese) | +3 | 1431 |
| 82 | [oblien/openship](https://github.com/oblien/openship) | +3 | 10216 |
| 83 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 8873 |
| 84 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6977 |
| 85 | [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) | +3 | 5356 |
| 86 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +3 | 40725 |
| 87 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +3 | 2011 |
| 88 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +3 | 15806 |
| 89 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +3 | 3155 |
| 90 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +3 | 662 |
| 91 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +3 | 6191 |
| 92 | [Mangi-11/Eta](https://github.com/Mangi-11/Eta) | +3 | 745 |
| 93 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 4450 |
| 94 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +3 | 2439 |
| 95 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 8961 |
| 96 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 27821 |
| 97 | [xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp) | +3 | 653 |
| 98 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3124 |
| 99 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +3 | 5593 |
| 100 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +3 | 3882 |
| 101 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 1010 |
| 102 | [harbor-framework/harbor](https://github.com/harbor-framework/harbor) | +2 | 3788 |
| 103 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +2 | 1085 |
| 104 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 1304 |
| 105 | [callstack/agent-device](https://github.com/callstack/agent-device) | +2 | 3916 |
| 106 | [agavra/tuicr](https://github.com/agavra/tuicr) | +2 | 2339 |
| 107 | [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | +2 | 975 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 23731 |
| 109 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +2 | 216 |
| 110 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +2 | 4390 |
| 111 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +2 | 14179 |
| 112 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +2 | 4927 |
| 113 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +2 | 2452 |
| 114 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +2 | 1486 |
| 115 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29575 |
| 116 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +2 | 27070 |
| 117 | [gavamedia/deltafin](https://github.com/gavamedia/deltafin) | +2 | 655 |
| 118 | [daimon3332/Outlook-Oauth-GetToken](https://github.com/daimon3332/Outlook-Oauth-GetToken) | +2 | 155 |
| 119 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +2 | 2482 |
| 120 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +2 | 12317 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +150 | 47063 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +147 | 14009 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +134 | 28129 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +126 | 38712 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +117 | 36563 |
| 6 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +115 | 23936 |
| 7 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +101 | 31128 |
| 8 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +96 | 22456 |
| 9 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +93 | 14484 |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +92 | 44884 |
| 11 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +92 | 28392 |
| 12 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +86 | 37282 |
| 13 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6927 |
| 14 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +74 | 24756 |
| 15 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +74 | 13659 |
| 16 | [facebook/astryx](https://github.com/facebook/astryx) | +74 | 11424 |
| 17 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +73 | 24340 |
| 18 | [block/buzz](https://github.com/block/buzz) | +71 | 21761 |
| 19 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +71 | 29459 |
| 20 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 13072 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +62 | 48603 |
| 22 | [erincatto/box3d](https://github.com/erincatto/box3d) | +58 | 5792 |
| 23 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +53 | 59946 |
| 24 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +51 | 16230 |
| 25 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5383 |
| 26 | [oblien/openship](https://github.com/oblien/openship) | +49 | 10216 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +47 | 21869 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +46 | 42769 |
| 29 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +45 | 12432 |
| 30 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +45 | 32499 |
| 31 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +45 | 14947 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +44 | 39330 |
| 33 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +43 | 7536 |
| 34 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +42 | 45713 |
| 35 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +41 | 18646 |
| 36 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +41 | 30912 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +41 | 33060 |
| 38 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +39 | 15862 |
| 39 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +38 | 42865 |
| 40 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +38 | 8824 |
| 41 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +38 | 6034 |
| 42 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +36 | 43992 |
| 43 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +36 | 16103 |
| 44 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 9364 |
| 45 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +35 | 9819 |
| 46 | [browser-use/video-use](https://github.com/browser-use/video-use) | +34 | 18789 |
| 47 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +33 | 15543 |
| 48 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +32 | 21559 |
| 49 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +32 | 8873 |
| 50 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +32 | 27661 |
| 51 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +31 | 7293 |
| 52 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +31 | 7781 |
| 53 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +31 | 40725 |
| 54 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +31 | 19573 |
| 55 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +30 | 28285 |
| 56 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +29 | 32210 |
| 57 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +29 | 7438 |
| 58 | [multica-ai/multica](https://github.com/multica-ai/multica) | +29 | 43528 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +29 | 35736 |
| 60 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +29 | 23731 |
| 61 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +28 | 15545 |
| 62 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +28 | 23793 |
| 63 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +28 | 48469 |
| 64 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8574 |
| 65 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +26 | 7990 |
| 66 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +26 | 6935 |
| 67 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 18138 |
| 68 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +25 | 2977 |
| 69 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +24 | 3348 |
| 70 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +24 | 7020 |
| 71 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 4181 |
| 72 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +24 | 3494 |
| 73 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +23 | 18382 |
| 74 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +23 | 4121 |
| 75 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6883 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +22 | 32928 |
| 77 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +22 | 2748 |
| 78 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +22 | 1518 |
| 79 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +22 | 26920 |
| 80 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +21 | 29840 |
| 81 | [decolua/9router](https://github.com/decolua/9router) | +21 | 24576 |
| 82 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +21 | 11476 |
| 83 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +21 | 27226 |
| 84 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +20 | 4450 |
| 85 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +20 | 2997 |
| 86 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +20 | 13035 |
| 87 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4572 |
| 88 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +20 | 1928 |
| 89 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4190 |
| 90 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 6191 |
| 91 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +19 | 4692 |
| 92 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 7100 |
| 93 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +19 | 9630 |
| 94 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1985 |
| 95 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +18 | 34821 |
| 96 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 13201 |
| 97 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 8009 |
| 98 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 9046 |
| 99 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +17 | 2482 |
| 100 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 8073 |
| 101 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +17 | 5218 |
| 102 | [yc-software/qm](https://github.com/yc-software/qm) | +16 | 9390 |
| 103 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +16 | 7916 |
| 104 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11081 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 46566 |
| 106 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +16 | 4390 |
| 107 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +16 | 14107 |
| 108 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +16 | 4639 |
| 109 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +16 | 12672 |
| 110 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +15 | 15546 |
| 111 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +15 | 3247 |
| 112 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +14 | 5159 |
| 113 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3413 |
| 114 | [pascalorg/editor](https://github.com/pascalorg/editor) | +14 | 20917 |
| 115 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +14 | 2011 |
| 116 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +14 | 11791 |
| 117 | [browser-act/skills](https://github.com/browser-act/skills) | +14 | 5133 |
| 118 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +14 | 10335 |
| 119 | [google-research/tabfm](https://github.com/google-research/tabfm) | +14 | 2317 |
| 120 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +14 | 1504 |
| 121 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1041 |
| 122 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 410 |
| 123 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29575 |
| 124 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +13 | 9477 |
| 125 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +13 | 7716 |
| 126 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +13 | 25948 |
| 127 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 843 |
| 128 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +13 | 0 |
| 129 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +12 | 5755 |
| 130 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3882 |
| 131 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 32518 |
| 132 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27821 |
| 133 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +12 | 26403 |
| 134 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 29580 |
| 135 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +12 | 18437 |
| 136 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 664 |
| 137 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +12 | 2028 |
| 138 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +11 | 44368 |
| 139 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 14179 |
| 140 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +11 | 3124 |
| 141 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1877 |
| 142 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +11 | 26831 |
| 143 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 736 |
| 144 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9867 |
| 145 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +10 | 40809 |
| 146 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1486 |
| 147 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +10 | 18992 |
| 148 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 995 |
| 149 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +10 | 5708 |
| 150 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +10 | 2222 |
| 151 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1769 |
| 152 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 2821 |
| 153 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +10 | 7651 |
| 154 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +9 | 6574 |
| 155 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 9640 |
| 156 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +9 | 8619 |
| 157 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +9 | 5831 |
| 158 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 5115 |
| 159 | [anbeime/skill](https://github.com/anbeime/skill) | +9 | 4658 |
| 160 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 2083 |
| 161 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +9 | 15574 |
| 162 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1705 |
| 163 | [openai/plugins](https://github.com/openai/plugins) | +9 | 4897 |
| 164 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +9 | 2496 |
| 165 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +9 | 2954 |
| 166 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4854 |
| 167 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8268 |
| 168 | [openai/skills](https://github.com/openai/skills) | +8 | 24463 |
| 169 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1833 |
| 170 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 3856 |
| 171 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1467 |
| 172 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +8 | 1703 |
| 173 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +8 | 9138 |
| 174 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 27665 |
| 175 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +7 | 16902 |
| 176 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1763 |
| 177 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 4972 |
| 178 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +7 | 829 |
| 179 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +7 | 539 |
| 180 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +7 | 506 |
| 181 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29718 |
| 182 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3307 |
| 183 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +7 | 8278 |
| 184 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +7 | 3130 |
| 185 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +7 | 1174 |
| 186 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +7 | 1052 |
| 187 | [crimera/piko](https://github.com/crimera/piko) | +7 | 4557 |
| 188 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1868 |
| 189 | [harbor-framework/harbor](https://github.com/harbor-framework/harbor) | +6 | 3788 |
| 190 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +6 | 1595 |
| 191 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +6 | 33007 |
| 192 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +6 | 27070 |
| 193 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1047 |
| 194 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5450 |
| 195 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +6 | 3899 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27059 |
| 197 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +6 | 18721 |
| 198 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5899 |
| 199 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +5 | 10300 |
| 200 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1252 |
| 201 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 671 |
| 202 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 962 |
| 203 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 6977 |
| 204 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +5 | 5797 |
| 205 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4970 |
| 206 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1161 |
| 207 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 9056 |
| 208 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5251 |
| 209 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2773 |
| 210 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +5 | 7432 |
| 211 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +5 | 28139 |
| 212 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14505 |
| 213 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +4 | 1515 |
| 214 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 373 |
| 215 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 490 |
| 216 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +4 | 6327 |
| 217 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9336 |
| 218 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +4 | 332 |
| 219 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3219 |
| 220 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +4 | 665 |
| 221 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 726 |
| 222 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +4 | 602 |
| 223 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +4 | 913 |
| 224 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 641 |
| 225 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 172 |
| 226 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +4 | 706 |
| 227 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 664 |
| 228 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 786 |
| 229 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3091 |
| 230 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +4 | 722 |
| 231 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +3 | 2177 |
| 232 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +3 | 1231 |
| 233 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 379 |
| 234 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12154 |
| 235 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 141 |
| 236 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 237 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 386 |
| 238 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 75 |
| 239 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 143 |
| 240 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 242 |
| 241 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1121 |
| 242 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 415 |
| 243 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +3 | 479 |
| 244 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +3 | 392 |
| 245 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 97 |
| 246 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +3 | 1049 |
| 247 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +3 | 2102 |
| 248 | [cloud-hu2000/autoComment](https://github.com/cloud-hu2000/autoComment) | +3 | 91 |
| 249 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4866 |
| 250 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9285 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2926 |
| 252 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +3 | 10340 |
| 253 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 3030 |
| 254 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 161 |
| 255 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10396 |
| 256 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11131 |
| 257 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6135 |
| 258 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +2 | 1155 |
| 259 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1253 |
| 260 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +2 | 319 |
| 261 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +2 | 585 |
| 262 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 71 |
| 263 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 50 |
| 264 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 148 |
| 265 | [hiz0147/HizSteamButton](https://github.com/hiz0147/HizSteamButton) | +2 | 342 |
| 266 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 469 |
| 267 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 369 |
| 268 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 105 |
| 269 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 432 |
| 270 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 818 |
| 271 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 127 |
| 272 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 97 |
| 273 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 697 |
| 274 | [lunasaw/voglander](https://github.com/lunasaw/voglander) | +2 | 357 |
| 275 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 428 |
| 276 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 817 |
| 277 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2889 |
| 278 | [TechyCSR/OpenCluely](https://github.com/TechyCSR/OpenCluely) | +1 | 717 |
| 279 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3417 |
| 280 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 69 |
| 281 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 282 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 283 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 228 |
| 284 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 837 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2832 |
| 286 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 175 |
| 287 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1069 |
| 288 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 232 |
| 289 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 290 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 315 |
| 291 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 292 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3859 |
| 293 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 104 |
| 294 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 55 |
| 295 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 31 |
| 296 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1936 |
| 297 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 164 |
| 298 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 299 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 185 |
| 300 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +1 | 92 |
