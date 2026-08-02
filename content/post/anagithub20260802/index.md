---
title: "2026-08-02 GitHub增长趋势报告"
description: "1.pdf-inspector+10 2.qm+6 3.colibri+4 4.decimen-optical-transfer+3 5.reverse-skill+3"
date: 2026-08-02T20:56:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-02 20:56:45

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
        'daily': {"categories": ["rahmanef63/os-vps", "cosmtrek/mindwalk", "rohitg00/ai-engineering-from-scratch", "lidge-jun/opencodex", "bryanthaboi/gen1recomp", "NomaDamas/k-skill", "esengine/DeepSeek-Reasonix", "ayghri/i-have-adhd", "tytsxai/IDM-Activation-Script-Chinese", "iOfficeAI/OfficeCLI", "antirez/ds4", "diegosouzapw/OmniRoute", "mchughalex/skate3recomp", "andrewyng/openworker", "emilkowalski/skills", "zhaoxuya520/reverse-skill", "bashalarmistalt/decimen-optical-transfer", "JustVugg/colibri", "yc-software/qm", "firecrawl/pdf-inspector"], "data": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 6, 10]},
        'weekly': {"categories": ["lidge-jun/opencodex", "opengeos/GeoLibre", "bryanthaboi/gen1recomp", "JustVugg/colibri", "1jehuang/jcode", "yc-software/qm", "herdrdev/herdr", "alibaba/open-code-review", "usestrix/strix", "pascalorg/editor", "firecrawl/pdf-inspector", "bradautomates/claude-video", "diegosouzapw/OmniRoute", "andrewyng/openworker", "agentscope-ai/QwenPaw", "img2threejs/img2threejs", "virgiliojr94/book-to-skill", "ayghri/i-have-adhd", "stablyai/orca", "block/buzz"], "data": [10, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 14, 14, 15, 16, 18, 20, 23, 24, 28]},
        'monthly': {"categories": ["erincatto/box3d", "iOfficeAI/OfficeCLI", "jamiepine/voicebox", "bradautomates/claude-video", "emilkowalski/skills", "teamchong/pxpipe", "HKUDS/Vibe-Trading", "k1tbyte/Wand-Enhancer", "facebook/astryx", "JustVugg/colibri", "DeusData/codebase-memory-mcp", "alibaba/page-agent", "calesthio/OpenMontage", "openai/codex-plugin-cc", "stablyai/orca", "herdrdev/herdr", "diegosouzapw/OmniRoute", "Zackriya-Solutions/meetily", "langchain-ai/openwiki", "usestrix/strix"], "data": [72, 73, 75, 77, 77, 81, 87, 90, 92, 96, 98, 104, 109, 113, 125, 126, 129, 140, 163, 198]}
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
| 1 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +10 | 5956 |
| 2 | [yc-software/qm](https://github.com/yc-software/qm) | +6 | 6918 |
| 3 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +4 | 22188 |
| 4 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +3 | 3589 |
| 5 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +3 | 13158 |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 23935 |
| 7 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +2 | 11932 |
| 8 | [mchughalex/skate3recomp](https://github.com/mchughalex/skate3recomp) | +2 | 1019 |
| 9 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 37783 |
| 10 | [antirez/ds4](https://github.com/antirez/ds4) | +2 | 19957 |
| 11 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +2 | 24274 |
| 12 | [tytsxai/IDM-Activation-Script-Chinese](https://github.com/tytsxai/IDM-Activation-Script-Chinese) | +2 | 1360 |
| 13 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +2 | 15630 |
| 14 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +2 | 28991 |
| 15 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +2 | 6867 |
| 16 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +2 | 1576 |
| 17 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +2 | 6661 |
| 18 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2 | 45508 |
| 19 | [cosmtrek/mindwalk](https://github.com/cosmtrek/mindwalk) | +2 | 1121 |
| 20 | [rahmanef63/os-vps](https://github.com/rahmanef63/os-vps) | +1 | 46 |
| 21 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +1 | 15241 |
| 22 | [github/gh-stack](https://github.com/github/gh-stack) | +1 | 915 |
| 23 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1 | 59869 |
| 24 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +1 | 2400 |
| 25 | [mudler/locate-anything.cpp](https://github.com/mudler/locate-anything.cpp) | +1 | 407 |
| 26 | [Ch1rpy2613/Mirrai](https://github.com/Ch1rpy2613/Mirrai) | +1 | 1292 |
| 27 | [AreevAI/flowcat](https://github.com/AreevAI/flowcat) | +1 | 79 |
| 28 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +1 | 27528 |
| 29 | [YouMind-OpenLab/ai-image-prompts-skill](https://github.com/YouMind-OpenLab/ai-image-prompts-skill) | +1 | 576 |
| 30 | [KimYx0207/AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh) | +1 | 5514 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +28 | 21022 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +24 | 35672 |
| 3 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +23 | 15630 |
| 4 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +20 | 15303 |
| 5 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +18 | 9081 |
| 6 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +16 | 32197 |
| 7 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +15 | 11932 |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +14 | 37783 |
| 9 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +14 | 13449 |
| 10 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +13 | 5956 |
| 11 | [pascalorg/editor](https://github.com/pascalorg/editor) | +12 | 20727 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +12 | 46638 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +12 | 17844 |
| 14 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +12 | 23602 |
| 15 | [yc-software/qm](https://github.com/yc-software/qm) | +11 | 6918 |
| 16 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 15241 |
| 17 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 22188 |
| 18 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 1576 |
| 19 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +10 | 4963 |
| 20 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 6661 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 42565 |
| 22 | [digimata/quill](https://github.com/digimata/quill) | +8 | 3598 |
| 23 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +8 | 23936 |
| 24 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +8 | 7275 |
| 25 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +8 | 4646 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +8 | 39185 |
| 27 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +7 | 3589 |
| 28 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +7 | 13158 |
| 29 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +7 | 18525 |
| 30 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +7 | 31982 |
| 31 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +7 | 2993 |
| 32 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +7 | 7642 |
| 33 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 45508 |
| 34 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 29327 |
| 35 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 16335 |
| 36 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +6 | 3251 |
| 37 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +6 | 21634 |
| 38 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +6 | 2716 |
| 39 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 42749 |
| 40 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +6 | 2345 |
| 41 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +6 | 2931 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 59869 |
| 43 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +5 | 24274 |
| 44 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 2918 |
| 45 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +5 | 8575 |
| 46 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | +5 | 1226 |
| 47 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +5 | 4131 |
| 48 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +5 | 2718 |
| 49 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 35600 |
| 50 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +5 | 346 |
| 51 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 12499 |
| 52 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +5 | 37114 |
| 53 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 20260 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +4 | 21258 |
| 55 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +4 | 28991 |
| 56 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 28055 |
| 57 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +4 | 48172 |
| 58 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 6480 |
| 59 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 60 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +4 | 2400 |
| 61 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +4 | 12994 |
| 62 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +4 | 13935 |
| 63 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +4 | 10138 |
| 64 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 2651 |
| 65 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +4 | 696 |
| 66 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 6029 |
| 67 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +4 | 3161 |
| 68 | [oblien/openship](https://github.com/oblien/openship) | +4 | 10152 |
| 69 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +4 | 442 |
| 70 | [nyblnet/bento](https://github.com/nyblnet/bento) | +4 | 3484 |
| 71 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 32721 |
| 72 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 5873 |
| 73 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 30831 |
| 74 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | +4 | 1131 |
| 75 | [every-app/open-seo](https://github.com/every-app/open-seo) | +4 | 10117 |
| 76 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +4 | 3803 |
| 77 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3 | 43271 |
| 78 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6867 |
| 79 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +3 | 1974 |
| 80 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +3 | 3106 |
| 81 | [Mangi-11/Eta](https://github.com/Mangi-11/Eta) | +3 | 720 |
| 82 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +3 | 625 |
| 83 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 8682 |
| 84 | [digimata/parrot](https://github.com/digimata/parrot) | +3 | 1081 |
| 85 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 29519 |
| 86 | [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem) | +3 | 1075 |
| 87 | [kunchenguid/dotfiles](https://github.com/kunchenguid/dotfiles) | +3 | 415 |
| 88 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +3 | 2472 |
| 89 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 8893 |
| 90 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 27745 |
| 91 | [xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp) | +3 | 639 |
| 92 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3122 |
| 93 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +3 | 5566 |
| 94 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 44675 |
| 95 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 993 |
| 96 | [yanhua1010/self-media-content-workflow](https://github.com/yanhua1010/self-media-content-workflow) | +3 | 325 |
| 97 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +2 | 688 |
| 98 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +2 | 7341 |
| 99 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 1298 |
| 100 | [agavra/tuicr](https://github.com/agavra/tuicr) | +2 | 2295 |
| 101 | [Steel-Foundation/SteelMC](https://github.com/Steel-Foundation/SteelMC) | +2 | 244 |
| 102 | [decolua/9router](https://github.com/decolua/9router) | +2 | 24461 |
| 103 | [mchughalex/skate3recomp](https://github.com/mchughalex/skate3recomp) | +2 | 1019 |
| 104 | [antirez/ds4](https://github.com/antirez/ds4) | +2 | 19957 |
| 105 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +2 | 188 |
| 106 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +2 | 14889 |
| 107 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +2 | 1448 |
| 108 | [gavamedia/deltafin](https://github.com/gavamedia/deltafin) | +2 | 612 |
| 109 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +2 | 12293 |
| 110 | [hardness1020/awesome-agent-architecture](https://github.com/hardness1020/awesome-agent-architecture) | +2 | 467 |
| 111 | [mikiarlo3/ai-copywriter](https://github.com/mikiarlo3/ai-copywriter) | +2 | 1012 |
| 112 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +2 | 960 |
| 113 | [sii-research/tau-0-vla](https://github.com/sii-research/tau-0-vla) | +2 | 260 |
| 114 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +2 | 10475 |
| 115 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +2 | 9783 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 46517 |
| 117 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +2 | 11769 |
| 118 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +2 | 40563 |
| 119 | [reflex-dev/xy](https://github.com/reflex-dev/xy) | +2 | 1279 |
| 120 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | +2 | 3794 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +198 | 46638 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +163 | 13935 |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +140 | 27988 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +129 | 37783 |
| 5 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +126 | 23602 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +125 | 35672 |
| 7 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +113 | 30966 |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +109 | 44675 |
| 9 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +104 | 28369 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +98 | 37114 |
| 11 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +96 | 22188 |
| 12 | [facebook/astryx](https://github.com/facebook/astryx) | +92 | 11294 |
| 13 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +90 | 14207 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +87 | 29327 |
| 15 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6902 |
| 16 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +77 | 23936 |
| 17 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +77 | 13449 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +75 | 48172 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +73 | 24274 |
| 20 | [erincatto/box3d](https://github.com/erincatto/box3d) | +72 | 5770 |
| 21 | [block/buzz](https://github.com/block/buzz) | +71 | 21022 |
| 22 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 12981 |
| 23 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +63 | 59869 |
| 24 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +56 | 18525 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +54 | 42565 |
| 26 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +51 | 15630 |
| 27 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +50 | 14889 |
| 28 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5357 |
| 29 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +49 | 39185 |
| 30 | [browser-use/video-use](https://github.com/browser-use/video-use) | +49 | 18337 |
| 31 | [oblien/openship](https://github.com/oblien/openship) | +48 | 10153 |
| 32 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +48 | 21634 |
| 33 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +48 | 30831 |
| 34 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +47 | 32197 |
| 35 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +44 | 15303 |
| 36 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +44 | 32815 |
| 37 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +43 | 11932 |
| 38 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +42 | 7341 |
| 39 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +42 | 45509 |
| 40 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +41 | 42749 |
| 41 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +41 | 8507 |
| 42 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +41 | 16059 |
| 43 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +38 | 9773 |
| 44 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +38 | 48385 |
| 45 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +37 | 43691 |
| 46 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5898 |
| 47 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +36 | 8682 |
| 48 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 9081 |
| 49 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +35 | 23761 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +34 | 15241 |
| 51 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +33 | 35600 |
| 52 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 43271 |
| 53 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +33 | 21258 |
| 54 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +33 | 7589 |
| 55 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +33 | 27528 |
| 56 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +33 | 26873 |
| 57 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +32 | 7275 |
| 58 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +32 | 40563 |
| 59 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +32 | 19515 |
| 60 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +31 | 6949 |
| 61 | [baairon/torlink](https://github.com/baairon/torlink) | +31 | 3958 |
| 62 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +30 | 7134 |
| 63 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +29 | 28055 |
| 64 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +29 | 15500 |
| 65 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2951 |
| 66 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +28 | 31982 |
| 67 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +28 | 23656 |
| 68 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8575 |
| 69 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +26 | 6661 |
| 70 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +26 | 3476 |
| 71 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +25 | 17844 |
| 72 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 18116 |
| 73 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +25 | 3161 |
| 74 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +25 | 11396 |
| 75 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +25 | 27158 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +24 | 32721 |
| 77 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +24 | 28991 |
| 78 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 4085 |
| 79 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +24 | 9261 |
| 80 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1922 |
| 81 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +23 | 7642 |
| 82 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +23 | 2651 |
| 83 | [decolua/9router](https://github.com/decolua/9router) | +23 | 24461 |
| 84 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +23 | 2472 |
| 85 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6842 |
| 86 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +22 | 12994 |
| 87 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +22 | 1518 |
| 88 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +22 | 9578 |
| 89 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +21 | 2918 |
| 90 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +20 | 6029 |
| 91 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4519 |
| 92 | [google-research/tabfm](https://github.com/google-research/tabfm) | +20 | 2304 |
| 93 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 4291 |
| 94 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4131 |
| 95 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +19 | 4653 |
| 96 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +19 | 46517 |
| 97 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +19 | 8036 |
| 98 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 7048 |
| 99 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +19 | 14068 |
| 100 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1983 |
| 101 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +18 | 7342 |
| 102 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 13104 |
| 103 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7994 |
| 104 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +18 | 4594 |
| 105 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 8964 |
| 106 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 12499 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +17 | 34777 |
| 108 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 3994 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +17 | 11769 |
| 110 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +17 | 6467 |
| 111 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +17 | 5157 |
| 112 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11076 |
| 113 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +16 | 26359 |
| 114 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +16 | 10297 |
| 115 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +16 | 1500 |
| 116 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 117 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +16 | 2807 |
| 118 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +16 | 0 |
| 119 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +16 | 2028 |
| 120 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 29519 |
| 121 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 5102 |
| 122 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +15 | 32403 |
| 123 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +15 | 25927 |
| 124 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3251 |
| 125 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2931 |
| 126 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +14 | 1974 |
| 127 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +14 | 29496 |
| 128 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +14 | 7630 |
| 129 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1037 |
| 130 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +14 | 26768 |
| 131 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 409 |
| 132 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +13 | 5956 |
| 133 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +13 | 9437 |
| 134 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +13 | 44305 |
| 135 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +13 | 27745 |
| 136 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +13 | 3122 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +13 | 18418 |
| 138 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 843 |
| 139 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +12 | 5693 |
| 140 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3803 |
| 141 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +12 | 18928 |
| 142 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 663 |
| 143 | [yc-software/qm](https://github.com/yc-software/qm) | +11 | 6918 |
| 144 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9598 |
| 145 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +11 | 40782 |
| 146 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +11 | 8598 |
| 147 | [anbeime/skill](https://github.com/anbeime/skill) | +11 | 4603 |
| 148 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1853 |
| 149 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 735 |
| 150 | [openai/plugins](https://github.com/openai/plugins) | +11 | 4882 |
| 151 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9783 |
| 152 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1448 |
| 153 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +10 | 6480 |
| 154 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 984 |
| 155 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +10 | 5822 |
| 156 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +10 | 5077 |
| 157 | [openai/skills](https://github.com/openai/skills) | +10 | 24429 |
| 158 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +10 | 5669 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +10 | 14130 |
| 160 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +10 | 2087 |
| 161 | [ascending-llc/jarvis-registry](https://github.com/ascending-llc/jarvis-registry) | +10 | 2715 |
| 162 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +10 | 3356 |
| 163 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +10 | 2209 |
| 164 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1753 |
| 165 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +10 | 7593 |
| 166 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 4840 |
| 167 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1988 |
| 168 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +9 | 15552 |
| 169 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +9 | 8893 |
| 170 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +9 | 2277 |
| 171 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1677 |
| 172 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +9 | 2477 |
| 173 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +9 | 1049 |
| 174 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +9 | 2952 |
| 175 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1826 |
| 176 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 3851 |
| 177 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +8 | 32972 |
| 178 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1457 |
| 179 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +8 | 1168 |
| 180 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +8 | 529 |
| 181 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +8 | 2600 |
| 182 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +8 | 9103 |
| 183 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +8 | 8260 |
| 184 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 27603 |
| 185 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +8 | 3890 |
| 186 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +8 | 5214 |
| 187 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +8 | 910 |
| 188 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +8 | 119 |
| 189 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1754 |
| 190 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 4950 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29694 |
| 192 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3269 |
| 193 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +7 | 1165 |
| 194 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +7 | 18705 |
| 195 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 706 |
| 196 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +7 | 28104 |
| 197 | [crimera/piko](https://github.com/crimera/piko) | +7 | 4541 |
| 198 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1855 |
| 199 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1034 |
| 200 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +6 | 6867 |
| 201 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5423 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +6 | 5777 |
| 203 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27028 |
| 204 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +6 | 3116 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5897 |
| 206 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3087 |
| 207 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1242 |
| 208 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 949 |
| 209 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 667 |
| 210 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4919 |
| 211 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1132 |
| 212 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 9031 |
| 213 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +5 | 7413 |
| 214 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 332 |
| 215 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2754 |
| 216 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 658 |
| 217 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 589 |
| 218 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14489 |
| 219 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 365 |
| 220 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +4 | 12146 |
| 221 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 486 |
| 222 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9313 |
| 223 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3196 |
| 224 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 719 |
| 225 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +4 | 6315 |
| 226 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 539 |
| 227 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1097 |
| 228 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 640 |
| 229 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 392 |
| 230 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 171 |
| 231 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +4 | 708 |
| 232 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 661 |
| 233 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 865 |
| 234 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +4 | 0 |
| 235 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5928 |
| 236 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +4 | 1484 |
| 237 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 780 |
| 238 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +3 | 2133 |
| 239 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 372 |
| 240 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 139 |
| 241 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 242 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 382 |
| 243 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 73 |
| 244 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 143 |
| 245 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 242 |
| 246 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 415 |
| 247 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +3 | 477 |
| 248 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 97 |
| 249 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +3 | 1032 |
| 250 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +3 | 2092 |
| 251 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4846 |
| 252 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9280 |
| 253 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2914 |
| 254 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +3 | 10332 |
| 255 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 3018 |
| 256 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 160 |
| 257 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10382 |
| 258 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11103 |
| 259 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6126 |
| 260 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +2 | 860 |
| 261 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +2 | 1152 |
| 262 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1232 |
| 263 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +2 | 580 |
| 264 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 70 |
| 265 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 48 |
| 266 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 145 |
| 267 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3405 |
| 268 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 366 |
| 269 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 270 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 105 |
| 271 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 431 |
| 272 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 813 |
| 273 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 126 |
| 274 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 96 |
| 275 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +2 | 1330 |
| 276 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 695 |
| 277 | [lunasaw/voglander](https://github.com/lunasaw/voglander) | +2 | 356 |
| 278 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 426 |
| 279 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 788 |
| 280 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2881 |
| 281 | [TechyCSR/OpenCluely](https://github.com/TechyCSR/OpenCluely) | +1 | 709 |
| 282 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 69 |
| 283 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 835 |
| 284 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 285 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 286 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 210 |
| 287 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 260 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2832 |
| 289 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 165 |
| 290 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1059 |
| 291 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 218 |
| 292 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 293 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 315 |
| 294 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 295 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3851 |
| 296 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 99 |
| 297 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 55 |
| 298 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 31 |
| 299 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1932 |
| 300 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 163 |
