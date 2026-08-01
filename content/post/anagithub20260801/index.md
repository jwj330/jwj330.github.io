---
title: "2026-08-01 GitHub增长趋势报告"
description: "1.qm+5 2.pdf-inspector+4 3.aos-ce+3 4.buzz+2 5.NeriPlayer+2"
date: 2026-08-01T20:54:32+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-01 20:54:32

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
        'daily': {"categories": ["RunMaestro/Maestro", "hahhforest/pi-textbook", "Steel-Foundation/SteelMC", "b3nito404/Loyd", "sii-research/tau-0-vla", "tandpfun/wardrobe", "workopia/US-New-Grad-Internship-Jobs", "shy3130/tickflow-stock-panel", "BigBodyCobain/Shadowbroker", "K-Dense-AI/scientific-agent-skills", "bryanthaboi/gen1recomp", "stablyai/orca", "ArvinLovegood/go-stock", "mekos2772/ios-location-spoofer", "HKUDS/DeepTutor", "cwuom/NeriPlayer", "block/buzz", "unicity-aos/aos-ce", "firecrawl/pdf-inspector", "yc-software/qm"], "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5]},
        'weekly': {"categories": ["citrolabs/ego-lite", "HKUDS/DeepTutor", "hugohe3/ppt-master", "opengeos/GeoLibre", "usestrix/strix", "pascalorg/editor", "heygen-com/hyperframes", "alibaba/open-code-review", "herdrdev/herdr", "1jehuang/jcode", "CoreBunch/Instatic", "bradautomates/claude-video", "diegosouzapw/OmniRoute", "img2threejs/img2threejs", "andrewyng/openworker", "virgiliojr94/book-to-skill", "agentscope-ai/QwenPaw", "ayghri/i-have-adhd", "stablyai/orca", "block/buzz"], "data": [10, 10, 10, 11, 11, 11, 12, 12, 14, 14, 15, 15, 17, 20, 21, 21, 22, 23, 27, 31]},
        'monthly': {"categories": ["ZhuLinsen/daily_stock_analysis", "emilkowalski/skills", "teamchong/pxpipe", "k1tbyte/Wand-Enhancer", "hasaneyldrm/exercises-dataset", "JustVugg/colibri", "jamiepine/voicebox", "alibaba/page-agent", "HKUDS/Vibe-Trading", "openai/codex-plugin-cc", "DeusData/codebase-memory-mcp", "facebook/astryx", "erincatto/box3d", "calesthio/OpenMontage", "Zackriya-Solutions/meetily", "herdrdev/herdr", "stablyai/orca", "diegosouzapw/OmniRoute", "langchain-ai/openwiki", "usestrix/strix"], "data": [79, 80, 81, 89, 92, 92, 94, 104, 117, 122, 124, 125, 127, 134, 145, 147, 150, 151, 191, 257]}
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
| 1 | [yc-software/qm](https://github.com/yc-software/qm) | +5 | 4698 |
| 2 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +4 | 3049 |
| 3 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +3 | 8577 |
| 4 | [block/buzz](https://github.com/block/buzz) | +2 | 20319 |
| 5 | [cwuom/NeriPlayer](https://github.com/cwuom/NeriPlayer) | +2 | 2654 |
| 6 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2 | 31790 |
| 7 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +2 | 2787 |
| 8 | [ArvinLovegood/go-stock](https://github.com/ArvinLovegood/go-stock) | +2 | 7094 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +1 | 35135 |
| 10 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +1 | 1443 |
| 11 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1 | 32327 |
| 12 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +1 | 10442 |
| 13 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +1 | 2461 |
| 14 | [workopia/US-New-Grad-Internship-Jobs](https://github.com/workopia/US-New-Grad-Internship-Jobs) | +1 | 130 |
| 15 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +1 | 1725 |
| 16 | [sii-research/tau-0-vla](https://github.com/sii-research/tau-0-vla) | +1 | 250 |
| 17 | [b3nito404/Loyd](https://github.com/b3nito404/Loyd) | +1 | 118 |
| 18 | [Steel-Foundation/SteelMC](https://github.com/Steel-Foundation/SteelMC) | +1 | 237 |
| 19 | [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook) | +1 | 703 |
| 20 | [RunMaestro/Maestro](https://github.com/RunMaestro/Maestro) | +1 | 3192 |
| 21 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +1 | 31840 |
| 22 | [SHITIANYU-hue/amai_ocl](https://github.com/SHITIANYU-hue/amai_ocl) | +1 | 201 |
| 23 | [wondelai/skills](https://github.com/wondelai/skills) | +1 | 1813 |
| 24 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1 | 32945 |
| 25 | [nethical6/conversation-steganography](https://github.com/nethical6/conversation-steganography) | +1 | 1181 |
| 26 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +1 | 2849 |
| 27 | [AMD-DEV-CONTEST/Radeon-hackathon-2026-07](https://github.com/AMD-DEV-CONTEST/Radeon-hackathon-2026-07) | +1 | 59 |
| 28 | [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) | +1 | 3792 |
| 29 | [jundot/omlx](https://github.com/jundot/omlx) | +1 | 18372 |
| 30 | [SourByte05/Vulnerability-Wiki-PoC](https://github.com/SourByte05/Vulnerability-Wiki-PoC) | +1 | 1032 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +31 | 20319 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 35135 |
| 3 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +23 | 15191 |
| 4 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 31840 |
| 5 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +21 | 14778 |
| 6 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +21 | 11563 |
| 7 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +20 | 8922 |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +17 | 36962 |
| 9 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +15 | 13272 |
| 10 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +15 | 7113 |
| 11 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +14 | 14921 |
| 12 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +14 | 23337 |
| 13 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +12 | 17453 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 39076 |
| 15 | [pascalorg/editor](https://github.com/pascalorg/editor) | +11 | 20596 |
| 16 | [usestrix/strix](https://github.com/usestrix/strix) | +11 | 46418 |
| 17 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +11 | 4829 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 42383 |
| 19 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 31790 |
| 20 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +10 | 7342 |
| 21 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +9 | 6443 |
| 22 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +8 | 1443 |
| 23 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +8 | 21865 |
| 24 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +8 | 18446 |
| 25 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +8 | 21360 |
| 26 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +8 | 2926 |
| 27 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +8 | 2694 |
| 28 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +7 | 16215 |
| 29 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +7 | 8577 |
| 30 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +7 | 2675 |
| 31 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +7 | 36961 |
| 32 | [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner) | +7 | 4579 |
| 33 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +7 | 24050 |
| 34 | [floci-io/floci](https://github.com/floci-io/floci) | +7 | 18096 |
| 35 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 29141 |
| 36 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 23623 |
| 37 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +6 | 2344 |
| 38 | [oblien/openship](https://github.com/oblien/openship) | +6 | 10100 |
| 39 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +6 | 35511 |
| 40 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 12374 |
| 41 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +6 | 3140 |
| 42 | [blader/humanizer](https://github.com/blader/humanizer) | +6 | 32538 |
| 43 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 3732 |
| 44 | [yc-software/qm](https://github.com/yc-software/qm) | +5 | 4698 |
| 45 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +5 | 11770 |
| 46 | [NodePassProject/Nowhere](https://github.com/NodePassProject/Nowhere) | +5 | 338 |
| 47 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +5 | 2849 |
| 48 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 42629 |
| 49 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 21051 |
| 50 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 5689 |
| 51 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 45426 |
| 52 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 19910 |
| 53 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +4 | 3049 |
| 54 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +4 | 47885 |
| 55 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 6302 |
| 56 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 57 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +4 | 2837 |
| 58 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | +4 | 1180 |
| 59 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +4 | 9877 |
| 60 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +4 | 59779 |
| 61 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +4 | 14854 |
| 62 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 27964 |
| 63 | [multica-ai/multica](https://github.com/multica-ai/multica) | +4 | 43142 |
| 64 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +4 | 418 |
| 65 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +4 | 12964 |
| 66 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 30776 |
| 67 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | +4 | 1122 |
| 68 | [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook) | +4 | 703 |
| 69 | [every-app/open-seo](https://github.com/every-app/open-seo) | +4 | 9945 |
| 70 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +4 | 44506 |
| 71 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 5896 |
| 72 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +3 | 1360 |
| 73 | [Mangi-11/Eta](https://github.com/Mangi-11/Eta) | +3 | 705 |
| 74 | [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem) | +3 | 1058 |
| 75 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 32640 |
| 76 | [kunchenguid/dotfiles](https://github.com/kunchenguid/dotfiles) | +3 | 371 |
| 77 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +3 | 2461 |
| 78 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +3 | 2387 |
| 79 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 8773 |
| 80 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3122 |
| 81 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 13843 |
| 82 | [m5stack/StackChan](https://github.com/m5stack/StackChan) | +3 | 1098 |
| 83 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +3 | 5556 |
| 84 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +3 | 28347 |
| 85 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +3 | 9715 |
| 86 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +3 | 2596 |
| 87 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +3 | 909 |
| 88 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +3 | 11343 |
| 89 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +3 | 675 |
| 90 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +3 | 1669 |
| 91 | [worldwonderer/novel-to-game](https://github.com/worldwonderer/novel-to-game) | +3 | 487 |
| 92 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +3 | 40447 |
| 93 | [MoonshotAI/MoonEP](https://github.com/MoonshotAI/MoonEP) | +3 | 980 |
| 94 | [hello245m/free-stockdb](https://github.com/hello245m/free-stockdb) | +3 | 1671 |
| 95 | [yanhua1010/self-media-content-workflow](https://github.com/yanhua1010/self-media-content-workflow) | +3 | 325 |
| 96 | [anbeime/skill](https://github.com/anbeime/skill) | +3 | 4563 |
| 97 | [microsoft/mlvc](https://github.com/microsoft/mlvc) | +3 | 233 |
| 98 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 13030 |
| 99 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +2 | 7252 |
| 100 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 1285 |
| 101 | [agavra/tuicr](https://github.com/agavra/tuicr) | +2 | 2254 |
| 102 | [Steel-Foundation/SteelMC](https://github.com/Steel-Foundation/SteelMC) | +2 | 237 |
| 103 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29389 |
| 104 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +2 | 1418 |
| 105 | [gavamedia/deltafin](https://github.com/gavamedia/deltafin) | +2 | 588 |
| 106 | [hardness1020/awesome-agent-architecture](https://github.com/hardness1020/awesome-agent-architecture) | +2 | 459 |
| 107 | [sii-research/tau-0-vla](https://github.com/sii-research/tau-0-vla) | +2 | 250 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +2 | 16027 |
| 109 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +2 | 10442 |
| 110 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +2 | 1928 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 18883 |
| 112 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +2 | 11751 |
| 113 | [reflex-dev/xy](https://github.com/reflex-dev/xy) | +2 | 1204 |
| 114 | [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | +2 | 3774 |
| 115 | [ZeroPointSix/outlookEmailPlus](https://github.com/ZeroPointSix/outlookEmailPlus) | +2 | 1826 |
| 116 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +2 | 3840 |
| 117 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +2 | 5007 |
| 118 | [Optim-Agent/optim-agent](https://github.com/Optim-Agent/optim-agent) | +2 | 681 |
| 119 | [ryfineZ/codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) | +2 | 2445 |
| 120 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29490 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +257 | 46418 |
| 2 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +191 | 13843 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +151 | 36962 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +150 | 35135 |
| 5 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +147 | 23338 |
| 6 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +145 | 27833 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +134 | 44506 |
| 8 | [erincatto/box3d](https://github.com/erincatto/box3d) | +127 | 5752 |
| 9 | [facebook/astryx](https://github.com/facebook/astryx) | +125 | 11226 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +124 | 36961 |
| 11 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +122 | 30842 |
| 12 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +117 | 29141 |
| 13 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +104 | 28347 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +94 | 47885 |
| 15 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +92 | 21865 |
| 16 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +92 | 18446 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +89 | 13892 |
| 18 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +81 | 6894 |
| 19 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +80 | 23623 |
| 20 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +79 | 59779 |
| 21 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +79 | 13273 |
| 22 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +72 | 24050 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +69 | 42383 |
| 24 | [block/buzz](https://github.com/block/buzz) | +65 | 20319 |
| 25 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 12943 |
| 26 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +64 | 14854 |
| 27 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +63 | 30776 |
| 28 | [browser-use/video-use](https://github.com/browser-use/video-use) | +62 | 18252 |
| 29 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +56 | 8378 |
| 30 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +55 | 21360 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +53 | 39076 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +51 | 32640 |
| 33 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +51 | 6901 |
| 34 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +50 | 31840 |
| 35 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5343 |
| 36 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +49 | 15191 |
| 37 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +49 | 14778 |
| 38 | [oblien/openship](https://github.com/oblien/openship) | +48 | 10100 |
| 39 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +46 | 42629 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +46 | 7388 |
| 41 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +45 | 9738 |
| 42 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +44 | 43305 |
| 43 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +44 | 16027 |
| 44 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +43 | 7113 |
| 45 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +43 | 27407 |
| 46 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +43 | 26842 |
| 47 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +42 | 7252 |
| 48 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +42 | 45426 |
| 49 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +42 | 40447 |
| 50 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +42 | 48332 |
| 51 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +41 | 11563 |
| 52 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 21052 |
| 53 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +41 | 9769 |
| 54 | [baairon/torlink](https://github.com/baairon/torlink) | +40 | 3949 |
| 55 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +39 | 9228 |
| 56 | [google-research/tabfm](https://github.com/google-research/tabfm) | +39 | 2290 |
| 57 | [multica-ai/multica](https://github.com/multica-ai/multica) | +38 | 43142 |
| 58 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +38 | 8479 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +37 | 35511 |
| 60 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5774 |
| 61 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 3460 |
| 62 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +36 | 23728 |
| 63 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +36 | 27101 |
| 64 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 8922 |
| 65 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +35 | 10813 |
| 66 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +34 | 15463 |
| 67 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +33 | 14921 |
| 68 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +33 | 19450 |
| 69 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +33 | 9528 |
| 70 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +31 | 23616 |
| 71 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +31 | 2461 |
| 72 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +30 | 6757 |
| 73 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +30 | 27770 |
| 74 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +29 | 27964 |
| 75 | [floci-io/floci](https://github.com/floci-io/floci) | +29 | 18096 |
| 76 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +29 | 2946 |
| 77 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +29 | 17489 |
| 78 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +28 | 31790 |
| 79 | [blader/humanizer](https://github.com/blader/humanizer) | +28 | 32538 |
| 80 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +28 | 28519 |
| 81 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1518 |
| 82 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +28 | 11343 |
| 83 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8577 |
| 84 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +27 | 2787 |
| 85 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +26 | 17453 |
| 86 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +26 | 7315 |
| 87 | [decolua/9router](https://github.com/decolua/9router) | +26 | 24322 |
| 88 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +26 | 8000 |
| 89 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +26 | 14029 |
| 90 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +25 | 2596 |
| 91 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +25 | 2849 |
| 92 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +25 | 32327 |
| 93 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +24 | 6443 |
| 94 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 7342 |
| 95 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 4011 |
| 96 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1913 |
| 97 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +23 | 12964 |
| 98 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +23 | 8004 |
| 99 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +23 | 2028 |
| 100 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +22 | 6816 |
| 101 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1499 |
| 102 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +21 | 2837 |
| 103 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +20 | 34713 |
| 104 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +20 | 46474 |
| 105 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +20 | 11751 |
| 106 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +20 | 26330 |
| 107 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1161 |
| 108 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 12374 |
| 109 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4488 |
| 110 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 4177 |
| 111 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 5896 |
| 112 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +19 | 13030 |
| 113 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +19 | 7013 |
| 114 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 4563 |
| 115 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +19 | 6447 |
| 116 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1978 |
| 117 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +19 | 0 |
| 118 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +18 | 3874 |
| 119 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7976 |
| 120 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +18 | 10229 |
| 121 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +18 | 25905 |
| 122 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +18 | 5007 |
| 123 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +18 | 4154 |
| 124 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +18 | 26728 |
| 125 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +17 | 29423 |
| 126 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +17 | 5105 |
| 127 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8821 |
| 128 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11067 |
| 129 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +16 | 44271 |
| 130 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +16 | 18883 |
| 131 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +16 | 7575 |
| 132 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3343 |
| 133 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +16 | 2406 |
| 134 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 135 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 29490 |
| 136 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 5070 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 18401 |
| 138 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +15 | 7551 |
| 139 | [openai/plugins](https://github.com/openai/plugins) | +15 | 4864 |
| 140 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 2694 |
| 141 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +14 | 9393 |
| 142 | [anbeime/skill](https://github.com/anbeime/skill) | +14 | 4563 |
| 143 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +14 | 2076 |
| 144 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1035 |
| 145 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 409 |
| 146 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +13 | 5636 |
| 147 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 1928 |
| 148 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +13 | 40754 |
| 149 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +13 | 8586 |
| 150 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +13 | 5812 |
| 151 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +13 | 3122 |
| 152 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +13 | 5637 |
| 153 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +13 | 6842 |
| 154 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +13 | 15264 |
| 155 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3732 |
| 156 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27722 |
| 157 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 5556 |
| 158 | [openai/skills](https://github.com/openai/skills) | +12 | 24407 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +12 | 14106 |
| 160 | [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit) | +12 | 662 |
| 161 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +12 | 1048 |
| 162 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4834 |
| 163 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9586 |
| 164 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +11 | 6302 |
| 165 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +11 | 32945 |
| 166 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1840 |
| 167 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +11 | 2198 |
| 168 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +11 | 27563 |
| 169 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +11 | 2449 |
| 170 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 734 |
| 171 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +11 | 3883 |
| 172 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 119 |
| 173 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9715 |
| 174 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1418 |
| 175 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 980 |
| 176 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 3840 |
| 177 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +10 | 2597 |
| 178 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +10 | 15522 |
| 179 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +10 | 16415 |
| 180 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +10 | 8773 |
| 181 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1725 |
| 182 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 433 |
| 183 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1330 |
| 184 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 16811 |
| 185 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1966 |
| 186 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +9 | 5030 |
| 187 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1669 |
| 188 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5401 |
| 189 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +9 | 8239 |
| 190 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 2055 |
| 191 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +9 | 5199 |
| 192 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +9 | 909 |
| 193 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +9 | 2945 |
| 194 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1822 |
| 195 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +8 | 9072 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +8 | 29672 |
| 197 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +8 | 18689 |
| 198 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +8 | 28062 |
| 199 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3230 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5757 |
| 201 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27012 |
| 202 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 679 |
| 203 | [crimera/piko](https://github.com/crimera/piko) | +7 | 4521 |
| 204 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 9014 |
| 205 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1024 |
| 206 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2739 |
| 207 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +6 | 3102 |
| 208 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +6 | 655 |
| 209 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1155 |
| 210 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5895 |
| 211 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3072 |
| 212 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 931 |
| 213 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 662 |
| 214 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 4886 |
| 215 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12133 |
| 216 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +5 | 361 |
| 217 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1117 |
| 218 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +5 | 7397 |
| 219 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 330 |
| 220 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 581 |
| 221 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +5 | 6306 |
| 222 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 473 |
| 223 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +5 | 708 |
| 224 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +5 | 0 |
| 225 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +5 | 1473 |
| 226 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14481 |
| 227 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9291 |
| 228 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 483 |
| 229 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 6716 |
| 230 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3175 |
| 231 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 716 |
| 232 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 538 |
| 233 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1088 |
| 234 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 638 |
| 235 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5088 |
| 236 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 389 |
| 237 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 170 |
| 238 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 658 |
| 239 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 863 |
| 240 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +4 | 5924 |
| 241 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 461 |
| 242 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +4 | 4837 |
| 243 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +4 | 3399 |
| 244 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 764 |
| 245 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10261 |
| 246 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 3002 |
| 247 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 371 |
| 248 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +3 | 1149 |
| 249 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 139 |
| 250 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 251 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 374 |
| 252 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 143 |
| 253 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 71 |
| 254 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 412 |
| 255 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 240 |
| 256 | [wengzige/html-deck-editor](https://github.com/wengzige/html-deck-editor) | +3 | 145 |
| 257 | [vibe-motion/create-vibe-motion](https://github.com/vibe-motion/create-vibe-motion) | +3 | 97 |
| 258 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9278 |
| 259 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2907 |
| 260 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 160 |
| 261 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10369 |
| 262 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11049 |
| 263 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6113 |
| 264 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +2 | 473 |
| 265 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1213 |
| 266 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +2 | 576 |
| 267 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 470 |
| 268 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +2 | 1021 |
| 269 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 361 |
| 270 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1054 |
| 271 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 91 |
| 272 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 583 |
| 273 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 104 |
| 274 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 429 |
| 275 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 810 |
| 276 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +2 | 119 |
| 277 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 96 |
| 278 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 682 |
| 279 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 761 |
| 280 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +1 | 464 |
| 281 | [TechyCSR/OpenCluely](https://github.com/TechyCSR/OpenCluely) | +1 | 701 |
| 282 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 68 |
| 283 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 836 |
| 284 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 260 |
| 285 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 286 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 201 |
| 287 | [opanel-mc/opanel](https://github.com/opanel-mc/opanel) | +1 | 276 |
| 288 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2833 |
| 289 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 192 |
| 290 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 7 |
| 291 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 315 |
| 292 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 293 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3843 |
| 294 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 86 |
| 295 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 296 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 30 |
| 297 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1926 |
| 298 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 162 |
| 299 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 300 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 183 |
