---
title: "2026-07-28 GitHub增长趋势报告"
description: "1.img2threejs+6 2.openworker+5 3.QwenPaw+5 4.herdr+5 5.buzz+5"
date: 2026-07-28T21:09:55+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-28 21:09:55

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
        'daily': {"categories": ["Vincentwei1021/video-shotcraft", "stablyai/orca", "pingdotgg/t3code", "zhishile/codex-auth-helper", "tamnd/kage", "heygen-com/hyperframes", "alibaba/open-code-review", "NodePassProject/Nowhere", "every-app/open-seo", "rohitg00/ai-engineering-from-scratch", "bradautomates/claude-video", "lidge-jun/opencodex", "builtbybel/FluentCleaner", "hasaneyldrm/exercises-dataset", "JustVugg/colibri", "block/buzz", "ogulcancelik/herdr", "agentscope-ai/QwenPaw", "andrewyng/openworker", "img2threejs/img2threejs"], "data": [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6]},
        'weekly': {"categories": ["heygen-com/hyperframes", "iOfficeAI/OfficeCLI", "JustVugg/colibri", "alibaba/open-code-review", "calesthio/OpenMontage", "CoreBunch/Instatic", "rohitg00/ai-engineering-from-scratch", "unicity-aos/aos-ce", "ogulcancelik/herdr", "lidge-jun/opencodex", "agentscope-ai/QwenPaw", "oblien/openship", "MadsLorentzen/ai-job-search", "citrolabs/ego-lite", "baidu/Unlimited-OCR", "img2threejs/img2threejs", "stablyai/orca", "andrewyng/openworker", "diegosouzapw/OmniRoute", "block/buzz"], "data": [12, 13, 13, 13, 14, 14, 14, 15, 16, 17, 20, 21, 21, 22, 25, 28, 30, 37, 40, 51]},
        'monthly': {"categories": ["teamchong/pxpipe", "k1tbyte/Wand-Enhancer", "ZhuLinsen/daily_stock_analysis", "JustVugg/colibri", "jamiepine/voicebox", "alibaba/page-agent", "hasaneyldrm/exercises-dataset", "HKUDS/Vibe-Trading", "openai/codex-plugin-cc", "erincatto/box3d", "facebook/astryx", "DeusData/codebase-memory-mcp", "stablyai/orca", "Zackriya-Solutions/meetily", "ogulcancelik/herdr", "diegosouzapw/OmniRoute", "calesthio/OpenMontage", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki", "usestrix/strix"], "data": [80, 85, 87, 90, 93, 105, 120, 121, 123, 127, 130, 137, 137, 145, 148, 150, 152, 162, 189, 254]}
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
| 1 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +6 | 7545 |
| 2 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +5 | 9955 |
| 3 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +5 | 29696 |
| 4 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +5 | 21935 |
| 5 | [block/buzz](https://github.com/block/buzz) | +5 | 15443 |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +4 | 20576 |
| 7 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 17599 |
| 8 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +4 | 4259 |
| 9 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 5540 |
| 10 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +4 | 11989 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 44580 |
| 12 | [every-app/open-seo](https://github.com/every-app/open-seo) | +3 | 8992 |
| 13 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +3 | 173 |
| 14 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +3 | 15443 |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +3 | 38369 |
| 16 | [tamnd/kage](https://github.com/tamnd/kage) | +3 | 2971 |
| 17 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +3 | 4717 |
| 18 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +3 | 15443 |
| 19 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 31700 |
| 20 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +3 | 2503 |
| 21 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 19868 |
| 22 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +3 | 6437 |
| 23 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 33045 |
| 24 | [blader/humanizer](https://github.com/blader/humanizer) | +2 | 31807 |
| 25 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +2 | 941 |
| 26 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 42137 |
| 27 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2 | 43220 |
| 28 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +2 | 771 |
| 29 | [inclusionAI/AReno](https://github.com/inclusionAI/AReno) | +2 | 247 |
| 30 | [facebook/astryx](https://github.com/facebook/astryx) | +2 | 11023 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +51 | 15443 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +40 | 33045 |
| 3 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +37 | 9955 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +30 | 31700 |
| 5 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +28 | 7545 |
| 6 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +25 | 19868 |
| 7 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +22 | 5689 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +21 | 28079 |
| 9 | [oblien/openship](https://github.com/oblien/openship) | +21 | 9343 |
| 10 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +20 | 29696 |
| 11 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +17 | 5540 |
| 12 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +16 | 21935 |
| 13 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +15 | 7703 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +14 | 44580 |
| 15 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +14 | 6438 |
| 16 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +14 | 43220 |
| 17 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +13 | 15443 |
| 18 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +13 | 20576 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +13 | 22879 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 38369 |
| 21 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +12 | 2026 |
| 22 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +12 | 27271 |
| 23 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 12732 |
| 24 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +11 | 2503 |
| 25 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +11 | 11989 |
| 26 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +11 | 3187 |
| 27 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +11 | 30872 |
| 28 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +10 | 36185 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 41622 |
| 30 | [every-app/open-seo](https://github.com/every-app/open-seo) | +10 | 8992 |
| 31 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +10 | 47235 |
| 32 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 17978 |
| 33 | [blader/humanizer](https://github.com/blader/humanizer) | +9 | 31807 |
| 34 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +9 | 28305 |
| 35 | [usestrix/strix](https://github.com/usestrix/strix) | +9 | 45282 |
| 36 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +9 | 15257 |
| 37 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 17599 |
| 38 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +8 | 30457 |
| 39 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +8 | 4717 |
| 40 | [nyblnet/bento](https://github.com/nyblnet/bento) | +8 | 2803 |
| 41 | [penecho/penecho](https://github.com/penecho/penecho) | +8 | 1765 |
| 42 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +7 | 2530 |
| 43 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +7 | 5035 |
| 44 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 42137 |
| 45 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 39922 |
| 46 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +7 | 1160 |
| 47 | [facebook/astryx](https://github.com/facebook/astryx) | +7 | 11023 |
| 48 | [agegr/pi-web](https://github.com/agegr/pi-web) | +7 | 3105 |
| 49 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +6 | 11194 |
| 50 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +6 | 4259 |
| 51 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 6659 |
| 52 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42367 |
| 53 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +6 | 12954 |
| 54 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +6 | 1677 |
| 55 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 20426 |
| 56 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 11464 |
| 57 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 12666 |
| 58 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +6 | 223 |
| 59 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 3345 |
| 60 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +6 | 12567 |
| 61 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +6 | 19904 |
| 62 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 59413 |
| 63 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +5 | 15443 |
| 64 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 34869 |
| 65 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +5 | 3493 |
| 66 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +5 | 5518 |
| 67 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +5 | 8690 |
| 68 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 12638 |
| 69 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 8033 |
| 70 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 631 |
| 71 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +5 | 7820 |
| 72 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 31796 |
| 73 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 26962 |
| 74 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +5 | 3427 |
| 75 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 46244 |
| 76 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +4 | 22041 |
| 77 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +4 | 18580 |
| 78 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 42764 |
| 79 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +4 | 7163 |
| 80 | [bryanthaboi/pokemon-gen1-recomp-project](https://github.com/bryanthaboi/pokemon-gen1-recomp-project) | +4 | 373 |
| 81 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +4 | 5601 |
| 82 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +4 | 3322 |
| 83 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +4 | 30238 |
| 84 | [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook) | +4 | 631 |
| 85 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +4 | 14594 |
| 86 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +4 | 941 |
| 87 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +4 | 7817 |
| 88 | [browser-act/skills](https://github.com/browser-act/skills) | +4 | 4895 |
| 89 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 18027 |
| 90 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +4 | 13966 |
| 91 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +4 | 1139 |
| 92 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +3 | 1251 |
| 93 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2164 |
| 94 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +3 | 9417 |
| 95 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +3 | 27458 |
| 96 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +3 | 173 |
| 97 | [tamnd/kage](https://github.com/tamnd/kage) | +3 | 2971 |
| 98 | [LanceZPF/agent-as-a-router](https://github.com/LanceZPF/agent-as-a-router) | +3 | 1012 |
| 99 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +3 | 3751 |
| 100 | [microsoft/mlvc](https://github.com/microsoft/mlvc) | +3 | 178 |
| 101 | [dondai1234/master-fetch](https://github.com/dondai1234/master-fetch) | +3 | 726 |
| 102 | [AMAP-ML/DreamX-World](https://github.com/AMAP-ML/DreamX-World) | +3 | 733 |
| 103 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 18866 |
| 104 | [Rimagination/scansci-pdf](https://github.com/Rimagination/scansci-pdf) | +3 | 657 |
| 105 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +3 | 10773 |
| 106 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +3 | 2353 |
| 107 | [orca-wm/Orca](https://github.com/orca-wm/Orca) | +3 | 615 |
| 108 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4871 |
| 109 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +3 | 8510 |
| 110 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +3 | 4265 |
| 111 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +2 | 6954 |
| 112 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +2 | 1780 |
| 113 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +2 | 10988 |
| 114 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +2 | 7847 |
| 115 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +2 | 771 |
| 116 | [inclusionAI/AReno](https://github.com/inclusionAI/AReno) | +2 | 247 |
| 117 | [worldwonderer/novel-to-game](https://github.com/worldwonderer/novel-to-game) | +2 | 309 |
| 118 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +2 | 397 |
| 119 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +2 | 426 |
| 120 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +2 | 1811 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +254 | 45282 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +189 | 13475 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +162 | 28079 |
| 4 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +152 | 43220 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +150 | 33045 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +148 | 21935 |
| 7 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +145 | 27198 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +137 | 31700 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +137 | 36185 |
| 10 | [facebook/astryx](https://github.com/facebook/astryx) | +130 | 11023 |
| 11 | [erincatto/box3d](https://github.com/erincatto/box3d) | +127 | 5636 |
| 12 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +123 | 30238 |
| 13 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +121 | 28305 |
| 14 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +120 | 17599 |
| 15 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +105 | 28064 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +93 | 47235 |
| 17 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +90 | 20576 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +87 | 59413 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +85 | 12846 |
| 20 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +80 | 6793 |
| 21 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +77 | 22041 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +74 | 14594 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +73 | 41622 |
| 24 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +71 | 11989 |
| 25 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +70 | 22879 |
| 26 | [browser-use/video-use](https://github.com/browser-use/video-use) | +69 | 18027 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +68 | 30457 |
| 28 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +63 | 12567 |
| 29 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +57 | 6659 |
| 30 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +56 | 19868 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +55 | 7820 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +54 | 31796 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +52 | 38369 |
| 34 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +52 | 6636 |
| 35 | [block/buzz](https://github.com/block/buzz) | +51 | 15443 |
| 36 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5273 |
| 37 | [oblien/openship](https://github.com/oblien/openship) | +48 | 9343 |
| 38 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +48 | 15767 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +47 | 42764 |
| 40 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +47 | 26532 |
| 41 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +47 | 9136 |
| 42 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +46 | 9547 |
| 43 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +46 | 9058 |
| 44 | [baairon/torlink](https://github.com/baairon/torlink) | +46 | 3896 |
| 45 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +45 | 29696 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +45 | 39922 |
| 47 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 44580 |
| 48 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +44 | 42137 |
| 49 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +44 | 6438 |
| 50 | [google-research/tabfm](https://github.com/google-research/tabfm) | +44 | 2198 |
| 51 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9789 |
| 52 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +42 | 26962 |
| 53 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +42 | 47747 |
| 54 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 20426 |
| 55 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +40 | 6954 |
| 56 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +39 | 26802 |
| 57 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10739 |
| 58 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +37 | 9955 |
| 59 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +37 | 15257 |
| 60 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +37 | 7817 |
| 61 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5517 |
| 62 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 3117 |
| 63 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +36 | 34869 |
| 64 | [multica-ai/multica](https://github.com/multica-ai/multica) | +36 | 42367 |
| 65 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +36 | 23593 |
| 66 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +34 | 6611 |
| 67 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +33 | 11194 |
| 68 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +33 | 19241 |
| 69 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +33 | 2391 |
| 70 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +32 | 7545 |
| 71 | [floci-io/floci](https://github.com/floci-io/floci) | +31 | 17978 |
| 72 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +31 | 27458 |
| 73 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +31 | 17233 |
| 74 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2649 |
| 75 | [blader/humanizer](https://github.com/blader/humanizer) | +30 | 31807 |
| 76 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +30 | 23371 |
| 77 | [decolua/9router](https://github.com/decolua/9router) | +30 | 23936 |
| 78 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2789 |
| 79 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +29 | 13895 |
| 80 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 27271 |
| 81 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +28 | 7163 |
| 82 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +28 | 27954 |
| 83 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1470 |
| 84 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +27 | 11016 |
| 85 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +26 | 30872 |
| 86 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +26 | 5601 |
| 87 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +26 | 7860 |
| 88 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +25 | 12732 |
| 89 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +25 | 7847 |
| 90 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15239 |
| 91 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +25 | 2027 |
| 92 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 5689 |
| 93 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +24 | 2154 |
| 94 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 3427 |
| 95 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +24 | 32011 |
| 96 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1882 |
| 97 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +23 | 15443 |
| 98 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +23 | 18461 |
| 99 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +23 | 4130 |
| 100 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +22 | 5540 |
| 101 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7703 |
| 102 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6654 |
| 103 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1475 |
| 104 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +21 | 46244 |
| 105 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +21 | 26182 |
| 106 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +21 | 25811 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +21 | 6385 |
| 108 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +20 | 5035 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 12666 |
| 110 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +20 | 34408 |
| 111 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +20 | 29023 |
| 112 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1139 |
| 113 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +20 | 6804 |
| 114 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4351 |
| 115 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 3493 |
| 116 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 4265 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +19 | 10048 |
| 118 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +19 | 26492 |
| 119 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +19 | 0 |
| 120 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1968 |
| 121 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7922 |
| 122 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +18 | 6779 |
| 123 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +18 | 11614 |
| 124 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +18 | 2279 |
| 125 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 11464 |
| 126 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +17 | 44088 |
| 127 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 3345 |
| 128 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2042 |
| 129 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +17 | 4927 |
| 130 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8284 |
| 131 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10988 |
| 132 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 18580 |
| 133 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +16 | 7278 |
| 134 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3289 |
| 135 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 136 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4775 |
| 137 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +16 | 7335 |
| 138 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 29306 |
| 139 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 4895 |
| 140 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 18290 |
| 141 | [openai/plugins](https://github.com/openai/plugins) | +15 | 4789 |
| 142 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 407 |
| 143 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +14 | 9198 |
| 144 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +14 | 40625 |
| 145 | [anbeime/skill](https://github.com/anbeime/skill) | +14 | 4355 |
| 146 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +13 | 5367 |
| 147 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +13 | 8510 |
| 148 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +13 | 5765 |
| 149 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +13 | 27572 |
| 150 | [openai/skills](https://github.com/openai/skills) | +13 | 24279 |
| 151 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +13 | 5504 |
| 152 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +13 | 1000 |
| 153 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 891 |
| 154 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1036 |
| 155 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +12 | 2026 |
| 156 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1783 |
| 157 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 660 |
| 158 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +12 | 3837 |
| 159 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +12 | 2904 |
| 160 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4928 |
| 161 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +11 | 3188 |
| 162 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9487 |
| 163 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2547 |
| 164 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +11 | 32787 |
| 165 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 13966 |
| 166 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +11 | 4257 |
| 167 | [HiDream-ai/HiDream-O1-Image](https://github.com/HiDream-ai/HiDream-O1-Image) | +11 | 1480 |
| 168 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1765 |
| 169 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +11 | 2156 |
| 170 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +11 | 27334 |
| 171 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +11 | 2279 |
| 172 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 727 |
| 173 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 117 |
| 174 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 941 |
| 175 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 612 |
| 176 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +10 | 4450 |
| 177 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +10 | 15080 |
| 178 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +10 | 15379 |
| 179 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +10 | 10079 |
| 180 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +10 | 5082 |
| 181 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 894 |
| 182 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 434 |
| 183 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1322 |
| 184 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +9 | 9417 |
| 185 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 16653 |
| 186 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 4866 |
| 187 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1833 |
| 188 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1577 |
| 189 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +9 | 29570 |
| 190 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5312 |
| 191 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +9 | 8149 |
| 192 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 2050 |
| 193 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +9 | 27958 |
| 194 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1717 |
| 195 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +8 | 8965 |
| 196 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +8 | 18582 |
| 197 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3088 |
| 198 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +7 | 1441 |
| 199 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +7 | 7298 |
| 200 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 26904 |
| 201 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +7 | 3025 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5681 |
| 203 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 204 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 629 |
| 205 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 8851 |
| 206 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 995 |
| 207 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2661 |
| 208 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +6 | 623 |
| 209 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1118 |
| 210 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +6 | 2678 |
| 211 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6019 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3026 |
| 213 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 869 |
| 214 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 631 |
| 215 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4717 |
| 216 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12074 |
| 217 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +5 | 328 |
| 218 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1021 |
| 219 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 330 |
| 220 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 529 |
| 221 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +5 | 6276 |
| 222 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 465 |
| 223 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +5 | 702 |
| 224 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +5 | 1439 |
| 225 | [crimera/piko](https://github.com/crimera/piko) | +5 | 4470 |
| 226 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14430 |
| 227 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +4 | 1127 |
| 228 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 463 |
| 229 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3083 |
| 230 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9200 |
| 231 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 683 |
| 232 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 538 |
| 233 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1018 |
| 234 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 621 |
| 235 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5073 |
| 236 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 387 |
| 237 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 167 |
| 238 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 2872 |
| 239 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 652 |
| 240 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 852 |
| 241 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5882 |
| 242 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 461 |
| 243 | [beefiker/superloopy](https://github.com/beefiker/superloopy) | +4 | 102 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +4 | 4765 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +4 | 3349 |
| 246 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 731 |
| 247 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10053 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2959 |
| 249 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +3 | 10887 |
| 250 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 251 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 252 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 359 |
| 253 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 68 |
| 254 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 395 |
| 255 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6513 |
| 256 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 235 |
| 257 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 94 |
| 258 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +3 | 968 |
| 259 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +3 | 2078 |
| 260 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +3 | 1663 |
| 261 | [kimsh-1/gongnyang-prompt-kit](https://github.com/kimsh-1/gongnyang-prompt-kit) | +3 | 291 |
| 262 | [cloud-hu2000/autoComment](https://github.com/cloud-hu2000/autoComment) | +3 | 85 |
| 263 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9388 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2860 |
| 265 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 157 |
| 266 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6007 |
| 267 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 467 |
| 268 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +2 | 358 |
| 269 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 340 |
| 270 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1017 |
| 271 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +2 | 3815 |
| 272 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 273 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 576 |
| 274 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 97 |
| 275 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 425 |
| 276 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 797 |
| 277 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 113 |
| 278 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 280 |
| 279 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 668 |
| 280 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +1 | 464 |
| 281 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 829 |
| 282 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 66 |
| 283 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 255 |
| 284 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2822 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 145 |
| 286 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 310 |
| 287 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 88 |
| 288 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 83 |
| 289 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 290 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 27 |
| 291 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1901 |
| 292 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 157 |
| 293 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 294 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 174 |
| 295 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 43 |
| 296 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +1 | 268 |
| 297 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +1 | 2595 |
| 298 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +1 | 194 |
| 299 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +1 | 183 |
| 300 | [Pumpkin-MC/PatchBukkit](https://github.com/Pumpkin-MC/PatchBukkit) | +1 | 165 |
