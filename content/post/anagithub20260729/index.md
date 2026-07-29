---
title: "2026-07-29 GitHub增长趋势报告"
description: "1.OmniRoute+5 2.book-to-skill+4 3.strix+4 4.buzz+4 5.claude-video+3"
date: 2026-07-29T20:57:38+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-29 20:57:38

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
        'daily': {"categories": ["tuya/TuyaOpenClaw", "pingdotgg/t3code", "bryanthaboi/gen1recomp", "1jehuang/jcode", "andrewyng/openworker", "Neoexm/Shittim-Server", "heygen-com/hyperframes-launches", "img2threejs/img2threejs", "OpenNSWM-Lab/FAROS", "mauriceboe/TREK", "heygen-com/hyperframes", "m5stack/StackChan", "earthtojake/text-to-cad", "emilkowalski/skills", "pascalorg/editor", "bradautomates/claude-video", "block/buzz", "usestrix/strix", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute"], "data": [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5]},
        'weekly': {"categories": ["rohitg00/ai-engineering-from-scratch", "petergyang/no-ai-slop", "Vincentwei1021/video-shotcraft", "slvDev/esp32-ai", "heygen-com/hyperframes", "iOfficeAI/OfficeCLI", "CoreBunch/Instatic", "bradautomates/claude-video", "alibaba/open-code-review", "lidge-jun/opencodex", "ogulcancelik/herdr", "oblien/openship", "agentscope-ai/QwenPaw", "citrolabs/ego-lite", "baidu/Unlimited-OCR", "stablyai/orca", "img2threejs/img2threejs", "andrewyng/openworker", "diegosouzapw/OmniRoute", "block/buzz"], "data": [11, 12, 12, 13, 13, 14, 14, 14, 14, 15, 16, 18, 21, 22, 25, 27, 27, 38, 42, 47]},
        'monthly': {"categories": ["emilkowalski/skills", "ZhuLinsen/daily_stock_analysis", "teamchong/pxpipe", "k1tbyte/Wand-Enhancer", "JustVugg/colibri", "jamiepine/voicebox", "alibaba/page-agent", "hasaneyldrm/exercises-dataset", "HKUDS/Vibe-Trading", "openai/codex-plugin-cc", "erincatto/box3d", "DeusData/codebase-memory-mcp", "facebook/astryx", "stablyai/orca", "calesthio/OpenMontage", "Zackriya-Solutions/meetily", "ogulcancelik/herdr", "diegosouzapw/OmniRoute", "langchain-ai/openwiki", "usestrix/strix"], "data": [79, 80, 81, 86, 90, 92, 104, 109, 121, 122, 127, 128, 130, 138, 142, 146, 147, 154, 189, 257]}
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
| 1 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +5 | 34024 |
| 2 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 12578 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +4 | 45579 |
| 4 | [block/buzz](https://github.com/block/buzz) | +4 | 16862 |
| 5 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 12630 |
| 6 | [pascalorg/editor](https://github.com/pascalorg/editor) | +3 | 19494 |
| 7 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2 | 22500 |
| 8 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +2 | 11831 |
| 9 | [m5stack/StackChan](https://github.com/m5stack/StackChan) | +2 | 1082 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 38612 |
| 11 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +2 | 11149 |
| 12 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +2 | 2898 |
| 13 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +2 | 8101 |
| 14 | [heygen-com/hyperframes-launches](https://github.com/heygen-com/hyperframes-launches) | +2 | 346 |
| 15 | [Neoexm/Shittim-Server](https://github.com/Neoexm/Shittim-Server) | +2 | 437 |
| 16 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +2 | 10574 |
| 17 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 13378 |
| 18 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +2 | 587 |
| 19 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1 | 15587 |
| 20 | [tuya/TuyaOpenClaw](https://github.com/tuya/TuyaOpenClaw) | +1 | 195 |
| 21 | [sndsh404/summer-2027-internships](https://github.com/sndsh404/summer-2027-internships) | +1 | 839 |
| 22 | [ZJUI-AI4H/Hulu-Med](https://github.com/ZJUI-AI4H/Hulu-Med) | +1 | 1026 |
| 23 | [riba2534/feishu-cli](https://github.com/riba2534/feishu-cli) | +1 | 1317 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1 | 32080 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1 | 16336 |
| 26 | [chen2he/orange-cloud](https://github.com/chen2he/orange-cloud) | +1 | 407 |
| 27 | [moss-apps/Flick](https://github.com/moss-apps/Flick) | +1 | 148 |
| 28 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +1 | 364 |
| 29 | [Open-Less/openless](https://github.com/Open-Less/openless) | +1 | 2898 |
| 30 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +1 | 5451 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +47 | 16862 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +42 | 34024 |
| 3 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +38 | 10574 |
| 4 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +27 | 8101 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 32664 |
| 6 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +25 | 20424 |
| 7 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +22 | 5960 |
| 8 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +21 | 30350 |
| 9 | [oblien/openship](https://github.com/oblien/openship) | +18 | 9710 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +16 | 22360 |
| 11 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +15 | 5725 |
| 12 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +14 | 15922 |
| 13 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +14 | 12630 |
| 14 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +14 | 6591 |
| 15 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +14 | 23161 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +13 | 38612 |
| 17 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +13 | 2288 |
| 18 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +12 | 2698 |
| 19 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3433 |
| 20 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 44879 |
| 21 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 20956 |
| 22 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 13378 |
| 23 | [usestrix/strix](https://github.com/usestrix/strix) | +11 | 45579 |
| 24 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +11 | 31124 |
| 25 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +10 | 12578 |
| 26 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 18018 |
| 27 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +9 | 36434 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 41815 |
| 29 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +9 | 43846 |
| 30 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +9 | 28539 |
| 31 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +9 | 7794 |
| 32 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 31999 |
| 33 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 17864 |
| 34 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +8 | 2005 |
| 35 | [every-app/open-seo](https://github.com/every-app/open-seo) | +8 | 9311 |
| 36 | [nyblnet/bento](https://github.com/nyblnet/bento) | +8 | 3009 |
| 37 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +8 | 27561 |
| 38 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +7 | 4358 |
| 39 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +7 | 2678 |
| 40 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +7 | 30553 |
| 41 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 40079 |
| 42 | [agegr/pi-web](https://github.com/agegr/pi-web) | +7 | 3222 |
| 43 | [penecho/penecho](https://github.com/penecho/penecho) | +7 | 1788 |
| 44 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 15587 |
| 45 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 22500 |
| 46 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +6 | 2303 |
| 47 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +6 | 587 |
| 48 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 42297 |
| 49 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 11831 |
| 50 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +6 | 35053 |
| 51 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42509 |
| 52 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +6 | 4979 |
| 53 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 6707 |
| 54 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +6 | 1288 |
| 55 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 20583 |
| 56 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 3545 |
| 57 | [pascalorg/editor](https://github.com/pascalorg/editor) | +5 | 19494 |
| 58 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 59504 |
| 59 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +5 | 3969 |
| 60 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 5211 |
| 61 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +5 | 47368 |
| 62 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +5 | 15307 |
| 63 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +5 | 13040 |
| 64 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 32080 |
| 65 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +5 | 8726 |
| 66 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 12744 |
| 67 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +5 | 240 |
| 68 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 639 |
| 69 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 8096 |
| 70 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +5 | 12685 |
| 71 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +5 | 19946 |
| 72 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 27053 |
| 73 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 46290 |
| 74 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +4 | 9506 |
| 75 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +4 | 14701 |
| 76 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 42894 |
| 77 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 3735 |
| 78 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +4 | 5730 |
| 79 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +4 | 5656 |
| 80 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +4 | 30364 |
| 81 | [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook) | +4 | 643 |
| 82 | [facebook/astryx](https://github.com/facebook/astryx) | +4 | 11089 |
| 83 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 12755 |
| 84 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +4 | 956 |
| 85 | [evolution-foundation/evolution-go](https://github.com/evolution-foundation/evolution-go) | +4 | 566 |
| 86 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +4 | 10824 |
| 87 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +3 | 1278 |
| 88 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2164 |
| 89 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +3 | 11149 |
| 90 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +3 | 18704 |
| 91 | [worldwonderer/novel-to-game](https://github.com/worldwonderer/novel-to-game) | +3 | 409 |
| 92 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +3 | 27554 |
| 93 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 858 |
| 94 | [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | +3 | 1568 |
| 95 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +3 | 19128 |
| 96 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +3 | 177 |
| 97 | [tamnd/kage](https://github.com/tamnd/kage) | +3 | 3007 |
| 98 | [yanhua1010/self-media-content-workflow](https://github.com/yanhua1010/self-media-content-workflow) | +3 | 309 |
| 99 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 364 |
| 100 | [anbeime/skill](https://github.com/anbeime/skill) | +3 | 4416 |
| 101 | [microsoft/mlvc](https://github.com/microsoft/mlvc) | +3 | 196 |
| 102 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +3 | 5451 |
| 103 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +3 | 900 |
| 104 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 4947 |
| 105 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +3 | 13938 |
| 106 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +3 | 6863 |
| 107 | [dondai1234/master-fetch](https://github.com/dondai1234/master-fetch) | +3 | 735 |
| 108 | [AMAP-ML/DreamX-World](https://github.com/AMAP-ML/DreamX-World) | +3 | 735 |
| 109 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 18896 |
| 110 | [Rimagination/scansci-pdf](https://github.com/Rimagination/scansci-pdf) | +3 | 662 |
| 111 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +3 | 2397 |
| 112 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4895 |
| 113 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +3 | 8524 |
| 114 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +2 | 7027 |
| 115 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +2 | 15851 |
| 116 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +2 | 2898 |
| 117 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +2 | 11022 |
| 118 | [ryfineZ/codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) | +2 | 2433 |
| 119 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +2 | 2049 |
| 120 | [inclusionAI/AReno](https://github.com/inclusionAI/AReno) | +2 | 254 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +257 | 45579 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +189 | 13559 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +154 | 34024 |
| 4 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +147 | 22360 |
| 5 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +146 | 27367 |
| 6 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +142 | 43847 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +138 | 32664 |
| 8 | [facebook/astryx](https://github.com/facebook/astryx) | +130 | 11089 |
| 9 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +128 | 36434 |
| 10 | [erincatto/box3d](https://github.com/erincatto/box3d) | +127 | 5658 |
| 11 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +122 | 30364 |
| 12 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +121 | 28539 |
| 13 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +109 | 17864 |
| 14 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +104 | 28126 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +92 | 47368 |
| 16 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +90 | 20956 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +86 | 13077 |
| 18 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6838 |
| 19 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +80 | 59504 |
| 20 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +79 | 22500 |
| 21 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +74 | 12630 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +73 | 14701 |
| 23 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +70 | 23161 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +69 | 41815 |
| 25 | [browser-use/video-use](https://github.com/browser-use/video-use) | +67 | 18098 |
| 26 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +64 | 30553 |
| 27 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +63 | 12685 |
| 28 | [block/buzz](https://github.com/block/buzz) | +55 | 16862 |
| 29 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +55 | 20424 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +55 | 7995 |
| 31 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +54 | 6707 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +53 | 32080 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +52 | 38612 |
| 34 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5293 |
| 35 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +50 | 6765 |
| 36 | [oblien/openship](https://github.com/oblien/openship) | +47 | 9710 |
| 37 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +47 | 15851 |
| 38 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +46 | 30350 |
| 39 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +46 | 9588 |
| 40 | [baairon/torlink](https://github.com/baairon/torlink) | +46 | 3914 |
| 41 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +45 | 42297 |
| 42 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +45 | 42894 |
| 43 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +45 | 26583 |
| 44 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +44 | 40079 |
| 45 | [google-research/tabfm](https://github.com/google-research/tabfm) | +44 | 2223 |
| 46 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9769 |
| 47 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +43 | 9102 |
| 48 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +42 | 44879 |
| 49 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +42 | 27053 |
| 50 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +42 | 47836 |
| 51 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +40 | 7027 |
| 52 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +40 | 6591 |
| 53 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +40 | 20583 |
| 54 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +39 | 9290 |
| 55 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +38 | 10574 |
| 56 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +38 | 26885 |
| 57 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10761 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +37 | 35053 |
| 59 | [multica-ai/multica](https://github.com/multica-ai/multica) | +37 | 42509 |
| 60 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +37 | 12578 |
| 61 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +37 | 7977 |
| 62 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5577 |
| 63 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 3210 |
| 64 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +36 | 15307 |
| 65 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +36 | 23637 |
| 66 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +34 | 8101 |
| 67 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +33 | 19303 |
| 68 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +32 | 2407 |
| 69 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +31 | 17288 |
| 70 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2666 |
| 71 | [floci-io/floci](https://github.com/floci-io/floci) | +30 | 18018 |
| 72 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +30 | 23440 |
| 73 | [decolua/9router](https://github.com/decolua/9router) | +30 | 24025 |
| 74 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +30 | 27554 |
| 75 | [blader/humanizer](https://github.com/blader/humanizer) | +29 | 31999 |
| 76 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2902 |
| 77 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +28 | 11149 |
| 78 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1494 |
| 79 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +27 | 13378 |
| 80 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 27562 |
| 81 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +27 | 7205 |
| 82 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +27 | 28006 |
| 83 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +27 | 13938 |
| 84 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +26 | 31124 |
| 85 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +26 | 5730 |
| 86 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +26 | 7921 |
| 87 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15250 |
| 88 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 5960 |
| 89 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +24 | 15922 |
| 90 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +24 | 2259 |
| 91 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 3455 |
| 92 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +24 | 7889 |
| 93 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +24 | 10824 |
| 94 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +24 | 32115 |
| 95 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1898 |
| 96 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +24 | 2028 |
| 97 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +23 | 2471 |
| 98 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +23 | 18511 |
| 99 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +22 | 5725 |
| 100 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7794 |
| 101 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6700 |
| 102 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1483 |
| 103 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +21 | 26235 |
| 104 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +21 | 25837 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 12755 |
| 106 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +20 | 34510 |
| 107 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +20 | 46290 |
| 108 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1147 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +20 | 6400 |
| 110 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4390 |
| 111 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 3735 |
| 112 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 5211 |
| 113 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 6863 |
| 114 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +19 | 29132 |
| 115 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 4285 |
| 116 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +19 | 11648 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +19 | 10091 |
| 118 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +19 | 4135 |
| 119 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +19 | 11831 |
| 120 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +19 | 26585 |
| 121 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +19 | 0 |
| 122 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1971 |
| 123 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7929 |
| 124 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +17 | 44134 |
| 125 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 3545 |
| 126 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2052 |
| 127 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +17 | 4955 |
| 128 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8363 |
| 129 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11022 |
| 130 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 18704 |
| 131 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +16 | 7354 |
| 132 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3308 |
| 133 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +16 | 6809 |
| 134 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 135 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4866 |
| 136 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +16 | 7401 |
| 137 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 29358 |
| 138 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 4947 |
| 139 | [anbeime/skill](https://github.com/anbeime/skill) | +15 | 4416 |
| 140 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 18327 |
| 141 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +15 | 2324 |
| 142 | [openai/plugins](https://github.com/openai/plugins) | +15 | 4807 |
| 143 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 407 |
| 144 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2288 |
| 145 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +14 | 9263 |
| 146 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1014 |
| 147 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +13 | 5434 |
| 148 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +13 | 40654 |
| 149 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +13 | 8524 |
| 150 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +13 | 5787 |
| 151 | [openai/skills](https://github.com/openai/skills) | +13 | 24315 |
| 152 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +13 | 5537 |
| 153 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 890 |
| 154 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1039 |
| 155 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3433 |
| 156 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27621 |
| 157 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +12 | 2898 |
| 158 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1781 |
| 159 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 660 |
| 160 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +12 | 3849 |
| 161 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4936 |
| 162 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9518 |
| 163 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +11 | 1842 |
| 164 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2566 |
| 165 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5451 |
| 166 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 14006 |
| 167 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1788 |
| 168 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +11 | 2171 |
| 169 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +11 | 2333 |
| 170 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 726 |
| 171 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 116 |
| 172 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9506 |
| 173 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 956 |
| 174 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +10 | 32830 |
| 175 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 625 |
| 176 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +10 | 2049 |
| 177 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +10 | 4504 |
| 178 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +10 | 15097 |
| 179 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +10 | 15419 |
| 180 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +10 | 5115 |
| 181 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +10 | 27389 |
| 182 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 895 |
| 183 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +10 | 2915 |
| 184 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 434 |
| 185 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1323 |
| 186 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 16691 |
| 187 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1854 |
| 188 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 4894 |
| 189 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1624 |
| 190 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5334 |
| 191 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +9 | 8176 |
| 192 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 2054 |
| 193 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1740 |
| 194 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +8 | 8995 |
| 195 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +8 | 29608 |
| 196 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +8 | 1573 |
| 197 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +8 | 18601 |
| 198 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +8 | 27996 |
| 199 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3127 |
| 200 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +7 | 7328 |
| 201 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 26939 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5710 |
| 203 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 204 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 639 |
| 205 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 8892 |
| 206 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1001 |
| 207 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2681 |
| 208 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +6 | 3058 |
| 209 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +6 | 634 |
| 210 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1124 |
| 211 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6019 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3043 |
| 213 | [crimera/piko](https://github.com/crimera/piko) | +6 | 4484 |
| 214 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 887 |
| 215 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 639 |
| 216 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4767 |
| 217 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12092 |
| 218 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +5 | 337 |
| 219 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1053 |
| 220 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 331 |
| 221 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 545 |
| 222 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +5 | 6280 |
| 223 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 466 |
| 224 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +5 | 709 |
| 225 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +5 | 1456 |
| 226 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14441 |
| 227 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +4 | 1131 |
| 228 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 468 |
| 229 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3101 |
| 230 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 689 |
| 231 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 538 |
| 232 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1027 |
| 233 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 626 |
| 234 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5079 |
| 235 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 387 |
| 236 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 168 |
| 237 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 2882 |
| 238 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 2693 |
| 239 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 654 |
| 240 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 854 |
| 241 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5897 |
| 242 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 461 |
| 243 | [beefiker/superloopy](https://github.com/beefiker/superloopy) | +4 | 102 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +4 | 4791 |
| 245 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +4 | 3362 |
| 246 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 735 |
| 247 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10051 |
| 248 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2969 |
| 249 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +3 | 10962 |
| 250 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 364 |
| 251 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 252 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 139 |
| 253 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9218 |
| 254 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 255 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 362 |
| 256 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 71 |
| 257 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 398 |
| 258 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6532 |
| 259 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 237 |
| 260 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +3 | 143 |
| 261 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 94 |
| 262 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9389 |
| 263 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2878 |
| 264 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 157 |
| 265 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10340 |
| 266 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6068 |
| 267 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +2 | 450 |
| 268 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 467 |
| 269 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +2 | 1017 |
| 270 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 347 |
| 271 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1025 |
| 272 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +2 | 3821 |
| 273 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 274 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 577 |
| 275 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 98 |
| 276 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 428 |
| 277 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 801 |
| 278 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 114 |
| 279 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 282 |
| 280 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 671 |
| 281 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +1 | 464 |
| 282 | [angieruiz17/claude-fintech-skills](https://github.com/angieruiz17/claude-fintech-skills) | +1 | 133 |
| 283 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 832 |
| 284 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 67 |
| 285 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 255 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2829 |
| 287 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 153 |
| 288 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 289 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 310 |
| 290 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 88 |
| 291 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 85 |
| 292 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 293 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 28 |
| 294 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1912 |
| 295 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 158 |
| 296 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 297 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 177 |
| 298 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 43 |
| 299 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +1 | 269 |
| 300 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +1 | 197 |
