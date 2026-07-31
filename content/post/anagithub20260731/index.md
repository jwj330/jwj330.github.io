---
title: "2026-07-31 GitHub增长趋势报告"
description: "1.buzz+5 2.orca+5 3.reverse-skill+3 4.Wilonity+3 5.openworker+3"
date: 2026-07-31T21:05:39+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-31 21:05:39

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
        'daily': {"categories": ["hardness1020/awesome-agent-architecture", "microsoft/TRELLIS.2", "pingdotgg/t3code", "usestrix/strix", "multica-ai/multica", "dramaclaw/dramaclaw", "1jehuang/jcode", "herdrdev/herdr", "bradautomates/claude-video", "Noelo-Lab/kuna", "virgiliojr94/book-to-skill", "agentscope-ai/QwenPaw", "pascalorg/editor", "hugohe3/ppt-master", "jamiepine/voicebox", "andrewyng/openworker", "WilonityLoader/Wilonity", "zhaoxuya520/reverse-skill", "stablyai/orca", "block/buzz"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5]},
        'weekly': {"categories": ["JustVugg/colibri", "opengeos/GeoLibre", "pascalorg/editor", "hugohe3/ppt-master", "slvDev/esp32-ai", "heygen-com/hyperframes", "citrolabs/ego-lite", "alibaba/open-code-review", "usestrix/strix", "herdrdev/herdr", "1jehuang/jcode", "CoreBunch/Instatic", "bradautomates/claude-video", "virgiliojr94/book-to-skill", "agentscope-ai/QwenPaw", "img2threejs/img2threejs", "diegosouzapw/OmniRoute", "stablyai/orca", "andrewyng/openworker", "block/buzz"], "data": [11, 11, 11, 12, 13, 13, 14, 14, 15, 15, 15, 16, 16, 21, 22, 22, 25, 30, 31, 38]},
        'monthly': {"categories": ["teamchong/pxpipe", "emilkowalski/skills", "ZhuLinsen/daily_stock_analysis", "k1tbyte/Wand-Enhancer", "JustVugg/colibri", "jamiepine/voicebox", "alibaba/page-agent", "hasaneyldrm/exercises-dataset", "openai/codex-plugin-cc", "HKUDS/Vibe-Trading", "erincatto/box3d", "facebook/astryx", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "Zackriya-Solutions/meetily", "herdrdev/herdr", "stablyai/orca", "diegosouzapw/OmniRoute", "langchain-ai/openwiki", "usestrix/strix"], "data": [81, 81, 81, 89, 92, 95, 105, 111, 122, 123, 127, 130, 130, 143, 148, 151, 152, 156, 191, 263]}
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
| 1 | [block/buzz](https://github.com/block/buzz) | +5 | 19344 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +5 | 34577 |
| 3 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +3 | 10579 |
| 4 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +3 | 0 |
| 5 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +3 | 11305 |
| 6 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3 | 47671 |
| 7 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 42190 |
| 8 | [pascalorg/editor](https://github.com/pascalorg/editor) | +2 | 20413 |
| 9 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +2 | 31453 |
| 10 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +2 | 14250 |
| 11 | [Noelo-Lab/kuna](https://github.com/Noelo-Lab/kuna) | +2 | 273 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 13095 |
| 13 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +2 | 23051 |
| 14 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 14570 |
| 15 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +2 | 2819 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2 | 42947 |
| 17 | [usestrix/strix](https://github.com/usestrix/strix) | +2 | 46168 |
| 18 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2 | 16063 |
| 19 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +2 | 9726 |
| 20 | [hardness1020/awesome-agent-architecture](https://github.com/hardness1020/awesome-agent-architecture) | +2 | 448 |
| 21 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +2 | 4697 |
| 22 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +2 | 2348 |
| 23 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +2 | 12911 |
| 24 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1 | 29460 |
| 25 | [mywwzh/oicpp](https://github.com/mywwzh/oicpp) | +1 | 166 |
| 26 | [crazygirl437/Polymarket-5min-bot](https://github.com/crazygirl437/Polymarket-5min-bot) | +1 | 80 |
| 27 | [OpenCoworkAI/open-cowork](https://github.com/OpenCoworkAI/open-cowork) | +1 | 1956 |
| 28 | [frknkrc44/HMA-OSS](https://github.com/frknkrc44/HMA-OSS) | +1 | 2645 |
| 29 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1 | 27896 |
| 30 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +1 | 15687 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +38 | 19344 |
| 2 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +31 | 11305 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +30 | 34577 |
| 4 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +25 | 36005 |
| 5 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +22 | 8768 |
| 6 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 31453 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +21 | 14250 |
| 8 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +16 | 13095 |
| 9 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +16 | 6949 |
| 10 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +15 | 14570 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +15 | 23052 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +15 | 46168 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +14 | 16984 |
| 14 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +14 | 6980 |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +13 | 38966 |
| 16 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +13 | 2622 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 42190 |
| 18 | [pascalorg/editor](https://github.com/pascalorg/editor) | +11 | 20413 |
| 19 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +11 | 4697 |
| 20 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 21469 |
| 21 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 6179 |
| 22 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +10 | 21042 |
| 23 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +10 | 3015 |
| 24 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +9 | 36838 |
| 25 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 18079 |
| 26 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +8 | 16063 |
| 27 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +8 | 1227 |
| 28 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +8 | 28966 |
| 29 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 18282 |
| 30 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +8 | 4487 |
| 31 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +8 | 2836 |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +8 | 31566 |
| 33 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +7 | 2613 |
| 34 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +7 | 2343 |
| 35 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +7 | 23808 |
| 36 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 32379 |
| 37 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 3653 |
| 38 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +6 | 10579 |
| 39 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 45318 |
| 40 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 23319 |
| 41 | [oblien/openship](https://github.com/oblien/openship) | +6 | 10014 |
| 42 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +6 | 47671 |
| 43 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 12222 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42947 |
| 45 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +6 | 6145 |
| 46 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 42544 |
| 47 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +6 | 44369 |
| 48 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 9821 |
| 49 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 6849 |
| 50 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 59697 |
| 51 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 2819 |
| 52 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +5 | 336 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 35424 |
| 54 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +5 | 14801 |
| 55 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 20899 |
| 56 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 5480 |
| 57 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 12911 |
| 58 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 40338 |
| 59 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +4 | 7177 |
| 60 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 61 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | +4 | 1126 |
| 62 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 19416 |
| 63 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +4 | 9726 |
| 64 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 30721 |
| 65 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | +4 | 1114 |
| 66 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +4 | 9639 |
| 67 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 5798 |
| 68 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +4 | 8573 |
| 69 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +4 | 2540 |
| 70 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +4 | 8300 |
| 71 | [egoist/kero](https://github.com/egoist/kero) | +4 | 719 |
| 72 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 12890 |
| 73 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +4 | 13149 |
| 74 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +3 | 1331 |
| 75 | [Mangi-11/Eta](https://github.com/Mangi-11/Eta) | +3 | 697 |
| 76 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +3 | 2348 |
| 77 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +3 | 6038 |
| 78 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 32495 |
| 79 | [kunchenguid/dotfiles](https://github.com/kunchenguid/dotfiles) | +3 | 360 |
| 80 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 29460 |
| 81 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 8665 |
| 82 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3122 |
| 83 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 13753 |
| 84 | [m5stack/StackChan](https://github.com/m5stack/StackChan) | +3 | 1093 |
| 85 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +3 | 5533 |
| 86 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +3 | 28318 |
| 87 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +3 | 2527 |
| 88 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +3 | 848 |
| 89 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +3 | 11291 |
| 90 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +3 | 654 |
| 91 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +3 | 1665 |
| 92 | [worldwonderer/novel-to-game](https://github.com/worldwonderer/novel-to-game) | +3 | 458 |
| 93 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +3 | 27896 |
| 94 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9058 |
| 95 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 957 |
| 96 | [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | +3 | 1637 |
| 97 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +3 | 19199 |
| 98 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +3 | 2979 |
| 99 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11725 |
| 100 | [yanhua1010/self-media-content-workflow](https://github.com/yanhua1010/self-media-content-workflow) | +3 | 321 |
| 101 | [anbeime/skill](https://github.com/anbeime/skill) | +3 | 4525 |
| 102 | [microsoft/mlvc](https://github.com/microsoft/mlvc) | +3 | 229 |
| 103 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 4066 |
| 104 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 12952 |
| 105 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +3 | 3789 |
| 106 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 5038 |
| 107 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29327 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +2 | 16000 |
| 109 | [hardness1020/awesome-agent-architecture](https://github.com/hardness1020/awesome-agent-architecture) | +2 | 448 |
| 110 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 23561 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 18859 |
| 112 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +2 | 1893 |
| 113 | [ZeroPointSix/outlookEmailPlus](https://github.com/ZeroPointSix/outlookEmailPlus) | +2 | 1821 |
| 114 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +2 | 3836 |
| 115 | [ryfineZ/codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) | +2 | 2441 |
| 116 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +2 | 2443 |
| 117 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +2 | 908 |
| 118 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +2 | 977 |
| 119 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +2 | 2123 |
| 120 | [inclusionAI/AReno](https://github.com/inclusionAI/AReno) | +2 | 259 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +263 | 46168 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +191 | 13753 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +156 | 36005 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +152 | 34577 |
| 5 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +151 | 23052 |
| 6 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +148 | 27667 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +143 | 44369 |
| 8 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +130 | 36838 |
| 9 | [facebook/astryx](https://github.com/facebook/astryx) | +130 | 11197 |
| 10 | [erincatto/box3d](https://github.com/erincatto/box3d) | +127 | 5713 |
| 11 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +123 | 28966 |
| 12 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +122 | 30683 |
| 13 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +111 | 18282 |
| 14 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +105 | 28318 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +95 | 47671 |
| 16 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +92 | 21469 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +89 | 13571 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +81 | 59697 |
| 19 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +81 | 23319 |
| 20 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6882 |
| 21 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +78 | 13095 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +74 | 14801 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +73 | 42190 |
| 24 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +72 | 23808 |
| 25 | [browser-use/video-use](https://github.com/browser-use/video-use) | +67 | 18211 |
| 26 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +65 | 30721 |
| 27 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 12890 |
| 28 | [block/buzz](https://github.com/block/buzz) | +63 | 19344 |
| 29 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +57 | 21042 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +55 | 8306 |
| 31 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +54 | 6849 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +53 | 38966 |
| 33 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +53 | 32495 |
| 34 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5324 |
| 35 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +50 | 7050 |
| 36 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 31453 |
| 37 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +49 | 14250 |
| 38 | [oblien/openship](https://github.com/oblien/openship) | +48 | 10014 |
| 39 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +47 | 16000 |
| 40 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +46 | 42544 |
| 41 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +46 | 9677 |
| 42 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +46 | 26811 |
| 43 | [baairon/torlink](https://github.com/baairon/torlink) | +46 | 3937 |
| 44 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +45 | 6949 |
| 45 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +45 | 43201 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +45 | 40338 |
| 47 | [google-research/tabfm](https://github.com/google-research/tabfm) | +44 | 2276 |
| 48 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9770 |
| 49 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +43 | 45318 |
| 50 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +43 | 27286 |
| 51 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +43 | 48278 |
| 52 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +43 | 9199 |
| 53 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +42 | 7177 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 20899 |
| 55 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +41 | 11306 |
| 56 | [multica-ai/multica](https://github.com/multica-ai/multica) | +39 | 42947 |
| 57 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +39 | 9467 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +38 | 35424 |
| 59 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +38 | 8300 |
| 60 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +38 | 27035 |
| 61 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10800 |
| 62 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5687 |
| 63 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 3454 |
| 64 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +36 | 15431 |
| 65 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +36 | 23708 |
| 66 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 8768 |
| 67 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +33 | 14570 |
| 68 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +33 | 19394 |
| 69 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +33 | 2443 |
| 70 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +31 | 23561 |
| 71 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +31 | 17421 |
| 72 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2776 |
| 73 | [floci-io/floci](https://github.com/floci-io/floci) | +30 | 18079 |
| 74 | [decolua/9router](https://github.com/decolua/9router) | +30 | 24209 |
| 75 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +30 | 27715 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +29 | 32379 |
| 77 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +29 | 1518 |
| 78 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2936 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 27896 |
| 80 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +28 | 6145 |
| 81 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +28 | 28234 |
| 82 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +28 | 11291 |
| 83 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +27 | 7280 |
| 84 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +27 | 14002 |
| 85 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +26 | 16984 |
| 86 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +26 | 31566 |
| 87 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +26 | 7986 |
| 88 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +25 | 2527 |
| 89 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15259 |
| 90 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +24 | 6179 |
| 91 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 6980 |
| 92 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +24 | 8573 |
| 93 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +24 | 2540 |
| 94 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 3905 |
| 95 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +24 | 7984 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +24 | 32275 |
| 97 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1909 |
| 98 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +24 | 2028 |
| 99 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +23 | 12911 |
| 100 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6795 |
| 101 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1494 |
| 102 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +21 | 2819 |
| 103 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +21 | 26310 |
| 104 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +21 | 25888 |
| 105 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +20 | 5798 |
| 106 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 12952 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +20 | 34653 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +20 | 46410 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +20 | 11725 |
| 110 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1159 |
| 111 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +20 | 6433 |
| 112 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 12223 |
| 113 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4468 |
| 114 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 4066 |
| 115 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 6965 |
| 116 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +19 | 29360 |
| 117 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 4502 |
| 118 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +19 | 10173 |
| 119 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +19 | 4149 |
| 120 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +19 | 26697 |
| 121 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +19 | 0 |
| 122 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1973 |
| 123 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +18 | 3789 |
| 124 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7963 |
| 125 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +17 | 44240 |
| 126 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2068 |
| 127 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +17 | 4983 |
| 128 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8689 |
| 129 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11049 |
| 130 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +16 | 29460 |
| 131 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 18859 |
| 132 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +16 | 7517 |
| 133 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3339 |
| 134 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +16 | 2380 |
| 135 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +16 | 6828 |
| 136 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 137 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 5025 |
| 138 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +16 | 7504 |
| 139 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +15 | 9355 |
| 140 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 5038 |
| 141 | [anbeime/skill](https://github.com/anbeime/skill) | +15 | 4525 |
| 142 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 18379 |
| 143 | [openai/plugins](https://github.com/openai/plugins) | +15 | 4849 |
| 144 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 409 |
| 145 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2622 |
| 146 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1029 |
| 147 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +13 | 5564 |
| 148 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 1893 |
| 149 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +13 | 40735 |
| 150 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +13 | 8565 |
| 151 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +13 | 5803 |
| 152 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +13 | 3122 |
| 153 | [openai/skills](https://github.com/openai/skills) | +13 | 24387 |
| 154 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +13 | 5612 |
| 155 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 845 |
| 156 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1046 |
| 157 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3653 |
| 158 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27695 |
| 159 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 5533 |
| 160 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +12 | 14085 |
| 161 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1780 |
| 162 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 662 |
| 163 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +12 | 3877 |
| 164 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4827 |
| 165 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9571 |
| 166 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2593 |
| 167 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1827 |
| 168 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +11 | 2194 |
| 169 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +11 | 27515 |
| 170 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +11 | 2420 |
| 171 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 733 |
| 172 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 119 |
| 173 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9639 |
| 174 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 977 |
| 175 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 3836 |
| 176 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +10 | 6038 |
| 177 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +10 | 32904 |
| 178 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +10 | 16394 |
| 179 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +10 | 8665 |
| 180 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +10 | 5168 |
| 181 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 908 |
| 182 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +10 | 2933 |
| 183 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 433 |
| 184 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1328 |
| 185 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +9 | 1405 |
| 186 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 16779 |
| 187 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1953 |
| 188 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 4976 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +9 | 9058 |
| 190 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1676 |
| 191 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1665 |
| 192 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5381 |
| 193 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +9 | 8219 |
| 194 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 2055 |
| 195 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1803 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +8 | 29652 |
| 197 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3197 |
| 198 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +8 | 5748 |
| 199 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +8 | 18658 |
| 200 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +8 | 28044 |
| 201 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +7 | 7384 |
| 202 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 26993 |
| 203 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 204 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 667 |
| 205 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 9001 |
| 206 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1016 |
| 207 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2725 |
| 208 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +6 | 3089 |
| 209 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +6 | 651 |
| 210 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1146 |
| 211 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5895 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3059 |
| 213 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 915 |
| 214 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 657 |
| 215 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4851 |
| 216 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12126 |
| 217 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +5 | 359 |
| 218 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1093 |
| 219 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 331 |
| 220 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 573 |
| 221 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +5 | 6298 |
| 222 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 468 |
| 223 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +5 | 708 |
| 224 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +5 | 1468 |
| 225 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14468 |
| 226 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9277 |
| 227 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 480 |
| 228 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +4 | 1146 |
| 229 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 6619 |
| 230 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3157 |
| 231 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 710 |
| 232 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 537 |
| 233 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1072 |
| 234 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 634 |
| 235 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5086 |
| 236 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 387 |
| 237 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 170 |
| 238 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 2979 |
| 239 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 2720 |
| 240 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 656 |
| 241 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 858 |
| 242 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5920 |
| 243 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 461 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +4 | 4832 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +4 | 3392 |
| 246 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 753 |
| 247 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10119 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2986 |
| 249 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +3 | 11017 |
| 250 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 365 |
| 251 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 252 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 138 |
| 253 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 143 |
| 254 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 367 |
| 255 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 71 |
| 256 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 407 |
| 257 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 239 |
| 258 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +3 | 145 |
| 259 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9279 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2905 |
| 261 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 159 |
| 262 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6106 |
| 263 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +2 | 464 |
| 264 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1199 |
| 265 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 469 |
| 266 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +2 | 569 |
| 267 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +2 | 1019 |
| 268 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 359 |
| 269 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1045 |
| 270 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +2 | 3838 |
| 271 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 91 |
| 272 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 581 |
| 273 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 103 |
| 274 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 429 |
| 275 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 807 |
| 276 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 116 |
| 277 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 286 |
| 278 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 96 |
| 279 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 678 |
| 280 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 712 |
| 281 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +1 | 464 |
| 282 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 835 |
| 283 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 68 |
| 284 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 258 |
| 285 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 286 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 186 |
| 287 | [opanel-mc/opanel](https://github.com/opanel-mc/opanel) | +1 | 275 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2833 |
| 289 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 165 |
| 290 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 291 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 315 |
| 292 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 293 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 86 |
| 294 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 295 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 30 |
| 296 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1924 |
| 297 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 162 |
| 298 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 299 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 181 |
| 300 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 43 |
