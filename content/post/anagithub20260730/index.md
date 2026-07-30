---
title: "2026-07-30 GitHub增长趋势报告"
description: "1.book-to-skill+10 2.orca+9 3.buzz+4 4.jcode+4 5.GeoLibre+4"
date: 2026-07-30T21:11:44+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-30 21:11:44

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
        'daily': {"categories": ["alibaba/open-code-review", "zhaoxuya520/reverse-skill", "Wei-Shaw/sub2api", "UditAkhourii/adhd", "langchain-ai/openwiki", "DeusData/codebase-memory-mcp", "meituan-longcat/LongCat-Video", "NodePassProject/Nowhere", "dramaclaw/dramaclaw", "unicity-aos/aos-ce", "bryanthaboi/gen1recomp", "different-ai/openwork", "usestrix/strix", "CoreBunch/Instatic", "pascalorg/editor", "opengeos/GeoLibre", "1jehuang/jcode", "block/buzz", "stablyai/orca", "virgiliojr94/book-to-skill"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 9, 10]},
        'weekly': {"categories": ["baidu/Unlimited-OCR", "JustVugg/colibri", "lidge-jun/opencodex", "Vincentwei1021/video-shotcraft", "heygen-com/hyperframes", "slvDev/esp32-ai", "usestrix/strix", "1jehuang/jcode", "bradautomates/claude-video", "alibaba/open-code-review", "herdrdev/herdr", "CoreBunch/Instatic", "virgiliojr94/book-to-skill", "agentscope-ai/QwenPaw", "citrolabs/ego-lite", "img2threejs/img2threejs", "stablyai/orca", "diegosouzapw/OmniRoute", "andrewyng/openworker", "block/buzz"], "data": [11, 11, 12, 13, 13, 14, 14, 14, 16, 16, 16, 17, 19, 21, 22, 25, 29, 30, 38, 45]},
        'monthly': {"categories": ["ZhuLinsen/daily_stock_analysis", "teamchong/pxpipe", "emilkowalski/skills", "k1tbyte/Wand-Enhancer", "jamiepine/voicebox", "JustVugg/colibri", "alibaba/page-agent", "hasaneyldrm/exercises-dataset", "openai/codex-plugin-cc", "HKUDS/Vibe-Trading", "erincatto/box3d", "facebook/astryx", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "Zackriya-Solutions/meetily", "stablyai/orca", "herdrdev/herdr", "diegosouzapw/OmniRoute", "langchain-ai/openwiki", "usestrix/strix"], "data": [80, 81, 81, 88, 92, 92, 104, 110, 122, 122, 127, 130, 130, 143, 147, 147, 149, 155, 191, 261]}
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
| 1 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +10 | 13653 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +9 | 33775 |
| 3 | [block/buzz](https://github.com/block/buzz) | +4 | 18309 |
| 4 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +4 | 14168 |
| 5 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +4 | 4482 |
| 6 | [pascalorg/editor](https://github.com/pascalorg/editor) | +4 | 20053 |
| 7 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +4 | 6777 |
| 8 | [usestrix/strix](https://github.com/usestrix/strix) | +4 | 45859 |
| 9 | [different-ai/openwork](https://github.com/different-ai/openwork) | +3 | 18631 |
| 10 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +3 | 948 |
| 11 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +2 | 8063 |
| 12 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +2 | 2609 |
| 13 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +2 | 334 |
| 14 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +2 | 5729 |
| 15 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 36630 |
| 16 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +2 | 13677 |
| 17 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +2 | 2853 |
| 18 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +2 | 35250 |
| 19 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +2 | 9798 |
| 20 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +2 | 16539 |
| 21 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 21213 |
| 22 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +2 | 8287 |
| 23 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 12904 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2 | 22947 |
| 25 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +1 | 30944 |
| 26 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +1 | 8526 |
| 27 | [Norman-bury/research-writing-skill](https://github.com/Norman-bury/research-writing-skill) | +1 | 2939 |
| 28 | [guokaigdg/animal-island-ui](https://github.com/guokaigdg/animal-island-ui) | +1 | 4070 |
| 29 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +1 | 2684 |
| 30 | [QuackbackIO/quackback](https://github.com/QuackbackIO/quackback) | +1 | 203 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +45 | 18310 |
| 2 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +38 | 10963 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +30 | 35044 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +29 | 33775 |
| 5 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +25 | 8526 |
| 6 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +22 | 6463 |
| 7 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +21 | 30944 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +19 | 13653 |
| 9 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +17 | 6777 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +16 | 22733 |
| 11 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +16 | 16539 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +16 | 12904 |
| 13 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +14 | 14168 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | +14 | 45859 |
| 15 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2499 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +13 | 38805 |
| 17 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +13 | 2874 |
| 18 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +12 | 5902 |
| 19 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 21213 |
| 20 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +11 | 20779 |
| 21 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +10 | 36630 |
| 22 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +10 | 44147 |
| 23 | [pascalorg/editor](https://github.com/pascalorg/editor) | +9 | 20053 |
| 24 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +9 | 4482 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 42011 |
| 26 | [oblien/openship](https://github.com/oblien/openship) | +9 | 9907 |
| 27 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +9 | 23550 |
| 28 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 18058 |
| 29 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +9 | 3567 |
| 30 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +8 | 948 |
| 31 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +8 | 4430 |
| 32 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +8 | 2757 |
| 33 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 18098 |
| 34 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 32207 |
| 35 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +8 | 2206 |
| 36 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +8 | 31255 |
| 37 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +8 | 28759 |
| 38 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +7 | 22947 |
| 39 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 42434 |
| 40 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +7 | 3658 |
| 41 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 45128 |
| 42 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 15864 |
| 43 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +6 | 35250 |
| 44 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +6 | 2506 |
| 45 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 9627 |
| 46 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 6775 |
| 47 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +5 | 334 |
| 48 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 5222 |
| 49 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 12055 |
| 50 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 5494 |
| 51 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +5 | 6014 |
| 52 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +5 | 8063 |
| 53 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 20739 |
| 54 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +5 | 14754 |
| 55 | [multica-ai/multica](https://github.com/multica-ai/multica) | +5 | 42683 |
| 56 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +5 | 27753 |
| 57 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 40213 |
| 58 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 648 |
| 59 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +4 | 59614 |
| 60 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +4 | 9580 |
| 61 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | +4 | 1100 |
| 62 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +4 | 2513 |
| 63 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +4 | 5494 |
| 64 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 30634 |
| 65 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +4 | 8142 |
| 66 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 3928 |
| 67 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 12780 |
| 68 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +4 | 13104 |
| 69 | [nyblnet/bento](https://github.com/nyblnet/bento) | +4 | 3146 |
| 70 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +4 | 6549 |
| 71 | [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook) | +4 | 665 |
| 72 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +4 | 1390 |
| 73 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +4 | 15364 |
| 74 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +4 | 2430 |
| 75 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +4 | 8777 |
| 76 | [evolution-foundation/evolution-go](https://github.com/evolution-foundation/evolution-go) | +4 | 569 |
| 77 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +4 | 7107 |
| 78 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +3 | 1303 |
| 79 | [different-ai/openwork](https://github.com/different-ai/openwork) | +3 | 18632 |
| 80 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 8287 |
| 81 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +3 | 2609 |
| 82 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3122 |
| 83 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 13677 |
| 84 | [m5stack/StackChan](https://github.com/m5stack/StackChan) | +3 | 1085 |
| 85 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +3 | 2684 |
| 86 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2435 |
| 87 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9031 |
| 88 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +3 | 9798 |
| 89 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 32299 |
| 90 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +3 | 11233 |
| 91 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 43102 |
| 92 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +3 | 604 |
| 93 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +3 | 1660 |
| 94 | [worldwonderer/novel-to-game](https://github.com/worldwonderer/novel-to-game) | +3 | 441 |
| 95 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 921 |
| 96 | [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | +3 | 1607 |
| 97 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +3 | 19159 |
| 98 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +3 | 2853 |
| 99 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11688 |
| 100 | [tamnd/kage](https://github.com/tamnd/kage) | +3 | 3044 |
| 101 | [yanhua1010/self-media-content-workflow](https://github.com/yanhua1010/self-media-content-workflow) | +3 | 317 |
| 102 | [anbeime/skill](https://github.com/anbeime/skill) | +3 | 4472 |
| 103 | [microsoft/mlvc](https://github.com/microsoft/mlvc) | +3 | 207 |
| 104 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +3 | 968 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 12839 |
| 106 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +3 | 719 |
| 107 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 5001 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3 | 46350 |
| 109 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29276 |
| 110 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +2 | 15932 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 23501 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 18793 |
| 113 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +2 | 5729 |
| 114 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +2 | 9599 |
| 115 | [sunny-glow/Auto-BenchMax](https://github.com/sunny-glow/Auto-BenchMax) | +2 | 422 |
| 116 | [ryfineZ/codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) | +2 | 2438 |
| 117 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29419 |
| 118 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +2 | 2424 |
| 119 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +2 | 903 |
| 120 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +2 | 11039 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +261 | 45859 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +191 | 13677 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 35044 |
| 4 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +149 | 22733 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +147 | 33775 |
| 6 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +147 | 27519 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +143 | 44147 |
| 8 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +130 | 36630 |
| 9 | [facebook/astryx](https://github.com/facebook/astryx) | +130 | 11154 |
| 10 | [erincatto/box3d](https://github.com/erincatto/box3d) | +127 | 5682 |
| 11 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +122 | 28759 |
| 12 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +122 | 30522 |
| 13 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +110 | 18098 |
| 14 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +104 | 28237 |
| 15 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +92 | 21213 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +92 | 47501 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +88 | 13333 |
| 18 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +81 | 22947 |
| 19 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6858 |
| 20 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +80 | 59614 |
| 21 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +76 | 12904 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +74 | 14754 |
| 23 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +71 | 23550 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +70 | 42011 |
| 25 | [browser-use/video-use](https://github.com/browser-use/video-use) | +67 | 18163 |
| 26 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 12780 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +64 | 30634 |
| 28 | [block/buzz](https://github.com/block/buzz) | +58 | 18310 |
| 29 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +57 | 20779 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +55 | 8165 |
| 31 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +54 | 6775 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +53 | 38805 |
| 33 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +52 | 32299 |
| 34 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5311 |
| 35 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +50 | 6901 |
| 36 | [oblien/openship](https://github.com/oblien/openship) | +47 | 9907 |
| 37 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +47 | 30945 |
| 38 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +47 | 13654 |
| 39 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +47 | 15932 |
| 40 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +46 | 42434 |
| 41 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +46 | 9632 |
| 42 | [baairon/torlink](https://github.com/baairon/torlink) | +46 | 3926 |
| 43 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +45 | 43102 |
| 44 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +45 | 26713 |
| 45 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +44 | 6777 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +44 | 40213 |
| 47 | [google-research/tabfm](https://github.com/google-research/tabfm) | +44 | 2246 |
| 48 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9770 |
| 49 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +43 | 7107 |
| 50 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +43 | 45128 |
| 51 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +43 | 9150 |
| 52 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +42 | 27147 |
| 53 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +42 | 48001 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 20739 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +39 | 35250 |
| 56 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +39 | 9384 |
| 57 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +38 | 10963 |
| 58 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +38 | 8142 |
| 59 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +38 | 26981 |
| 60 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10779 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +37 | 42683 |
| 62 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5639 |
| 63 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 3264 |
| 64 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +36 | 15364 |
| 65 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +36 | 23671 |
| 66 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 8526 |
| 67 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +33 | 19358 |
| 68 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +33 | 2424 |
| 69 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +31 | 14168 |
| 70 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +31 | 23501 |
| 71 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +31 | 17349 |
| 72 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2691 |
| 73 | [floci-io/floci](https://github.com/floci-io/floci) | +30 | 18058 |
| 74 | [decolua/9router](https://github.com/decolua/9router) | +30 | 24125 |
| 75 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +30 | 27631 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +29 | 32207 |
| 77 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +29 | 1517 |
| 78 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2921 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 27753 |
| 80 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +28 | 28059 |
| 81 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +28 | 11233 |
| 82 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +27 | 6014 |
| 83 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +27 | 7247 |
| 84 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +27 | 13978 |
| 85 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +26 | 31255 |
| 86 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +26 | 16539 |
| 87 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +26 | 7960 |
| 88 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15256 |
| 89 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 6464 |
| 90 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +24 | 8063 |
| 91 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +24 | 2441 |
| 92 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +24 | 2513 |
| 93 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 3492 |
| 94 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +24 | 7921 |
| 95 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +24 | 10860 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +24 | 32195 |
| 97 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1904 |
| 98 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +24 | 2028 |
| 99 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +23 | 5902 |
| 100 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +23 | 18554 |
| 101 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6751 |
| 102 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1491 |
| 103 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +21 | 26276 |
| 104 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +21 | 25858 |
| 105 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +20 | 5494 |
| 106 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 12839 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +20 | 34595 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +20 | 46350 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +20 | 11688 |
| 110 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1157 |
| 111 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +20 | 6416 |
| 112 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4434 |
| 113 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 3928 |
| 114 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 6923 |
| 115 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +19 | 29241 |
| 116 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 4395 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +19 | 10128 |
| 118 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +19 | 4142 |
| 119 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +19 | 12055 |
| 120 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +19 | 26634 |
| 121 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1973 |
| 122 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +19 | 0 |
| 123 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +18 | 3658 |
| 124 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7946 |
| 125 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +17 | 44187 |
| 126 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2060 |
| 127 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +17 | 4968 |
| 128 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8504 |
| 129 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11039 |
| 130 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +16 | 29419 |
| 131 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 18793 |
| 132 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +16 | 7441 |
| 133 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3321 |
| 134 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +16 | 2351 |
| 135 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +16 | 6819 |
| 136 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 137 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4962 |
| 138 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +16 | 7455 |
| 139 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 5001 |
| 140 | [anbeime/skill](https://github.com/anbeime/skill) | +15 | 4472 |
| 141 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 18352 |
| 142 | [openai/plugins](https://github.com/openai/plugins) | +15 | 4827 |
| 143 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 408 |
| 144 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2499 |
| 145 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +14 | 9318 |
| 146 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1023 |
| 147 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +13 | 5497 |
| 148 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +13 | 40698 |
| 149 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +13 | 8542 |
| 150 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +13 | 5797 |
| 151 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +13 | 3122 |
| 152 | [openai/skills](https://github.com/openai/skills) | +13 | 24353 |
| 153 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +13 | 5570 |
| 154 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 846 |
| 155 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1045 |
| 156 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3567 |
| 157 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 1869 |
| 158 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27661 |
| 159 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 5494 |
| 160 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +12 | 14043 |
| 161 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1782 |
| 162 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 660 |
| 163 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +12 | 3862 |
| 164 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4884 |
| 165 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9545 |
| 166 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2578 |
| 167 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1812 |
| 168 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +11 | 2177 |
| 169 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +11 | 27461 |
| 170 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +11 | 2383 |
| 171 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 730 |
| 172 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 117 |
| 173 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9580 |
| 174 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 968 |
| 175 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +10 | 32873 |
| 176 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +10 | 16361 |
| 177 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +10 | 8287 |
| 178 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 633 |
| 179 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +10 | 2083 |
| 180 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +10 | 5147 |
| 181 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 899 |
| 182 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +10 | 2921 |
| 183 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 433 |
| 184 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1325 |
| 185 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 16738 |
| 186 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1875 |
| 187 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 4925 |
| 188 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +9 | 5729 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +9 | 9031 |
| 190 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1653 |
| 191 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1660 |
| 192 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5360 |
| 193 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +9 | 8199 |
| 194 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 2055 |
| 195 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1747 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +8 | 29633 |
| 197 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3162 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +8 | 18628 |
| 199 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +8 | 28025 |
| 200 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +7 | 7358 |
| 201 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 26964 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5729 |
| 203 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 204 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 656 |
| 205 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 8960 |
| 206 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1009 |
| 207 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2702 |
| 208 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +6 | 3076 |
| 209 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +6 | 646 |
| 210 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1136 |
| 211 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5954 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3053 |
| 213 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 901 |
| 214 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 648 |
| 215 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4814 |
| 216 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12115 |
| 217 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +5 | 349 |
| 218 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1071 |
| 219 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 332 |
| 220 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 559 |
| 221 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +5 | 6291 |
| 222 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 466 |
| 223 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +5 | 710 |
| 224 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +5 | 1459 |
| 225 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14459 |
| 226 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 478 |
| 227 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +4 | 1140 |
| 228 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 6572 |
| 229 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3119 |
| 230 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 699 |
| 231 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 538 |
| 232 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1049 |
| 233 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 630 |
| 234 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5081 |
| 235 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 387 |
| 236 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 170 |
| 237 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 2944 |
| 238 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 2712 |
| 239 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 655 |
| 240 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 857 |
| 241 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5909 |
| 242 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 461 |
| 243 | [beefiker/superloopy](https://github.com/beefiker/superloopy) | +4 | 102 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +4 | 4811 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +4 | 3384 |
| 246 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 743 |
| 247 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10057 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2977 |
| 249 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +3 | 10989 |
| 250 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 365 |
| 251 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 252 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 139 |
| 253 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9248 |
| 254 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 365 |
| 255 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 143 |
| 256 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 71 |
| 257 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 401 |
| 258 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 237 |
| 259 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +3 | 143 |
| 260 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 96 |
| 261 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9328 |
| 262 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2893 |
| 263 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 157 |
| 264 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +2 | 459 |
| 265 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6093 |
| 266 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 468 |
| 267 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +2 | 1019 |
| 268 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 349 |
| 269 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1038 |
| 270 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +2 | 3828 |
| 271 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 272 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 579 |
| 273 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 102 |
| 274 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 428 |
| 275 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 804 |
| 276 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 116 |
| 277 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 284 |
| 278 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 96 |
| 279 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 677 |
| 280 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 667 |
| 281 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +1 | 464 |
| 282 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 68 |
| 283 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 834 |
| 284 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 256 |
| 285 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 173 |
| 286 | [opanel-mc/opanel](https://github.com/opanel-mc/opanel) | +1 | 275 |
| 287 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2836 |
| 288 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 160 |
| 289 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 290 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 315 |
| 291 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 89 |
| 292 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 85 |
| 293 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 294 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 29 |
| 295 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1917 |
| 296 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 161 |
| 297 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 298 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 180 |
| 299 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 43 |
| 300 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +1 | 269 |
