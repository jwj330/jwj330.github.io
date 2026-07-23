---
title: "2026-07-23 GitHub增长趋势报告"
description: "1.Unlimited-OCR+16 2.OmniRoute+13 3.orca+9 4.openship+9 5.ai-engineering-from-scratch+7"
date: 2026-07-23T21:05:59+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-23 21:05:59

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
        'daily': {"categories": ["ogulcancelik/herdr", "JustVugg/colibri", "agegr/pi-web", "vercel-labs/agent-skills", "JCodesMore/ai-website-cloner-template", "hoainho/img2threejs", "stackryze/FreeDomains", "can1357/oh-my-pi", "tonhowtf/omniget", "HKUDS/Vibe-Trading", "HKUDS/DeepTutor", "tirth8205/code-review-graph", "lidge-jun/opencodex", "block/buzz", "iOfficeAI/OfficeCLI", "rohitg00/ai-engineering-from-scratch", "oblien/openship", "stablyai/orca", "diegosouzapw/OmniRoute", "baidu/Unlimited-OCR"], "data": [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 7, 9, 9, 13, 16]},
        'weekly': {"categories": ["1jehuang/jcode", "MoonshotAI/kimi-cli", "block/buzz", "HKUDS/DeepTutor", "JustVugg/colibri", "usestrix/strix", "ibelick/ui-skills", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search", "HKUDS/Vibe-Trading", "jamiepine/voicebox", "tirth8205/code-review-graph", "baidu/Unlimited-OCR", "rohitg00/ai-engineering-from-scratch", "emilkowalski/skills", "ogulcancelik/herdr", "stablyai/orca", "diegosouzapw/OmniRoute", "oblien/openship", "Fei-Away/Codex-Dream-Skin"], "data": [12, 13, 13, 14, 15, 16, 16, 16, 17, 18, 18, 18, 19, 22, 23, 25, 32, 36, 38, 50]},
        'monthly': {"categories": ["Zackriya-Solutions/meetily", "simplex-chat/simplex-chat", "facebook/astryx", "hugohe3/ppt-master", "MadsLorentzen/ai-job-search", "apple/container", "jamiepine/voicebox", "topoteretes/cognee", "ogulcancelik/herdr", "JCodesMore/ai-website-cloner-template", "XxHuberrr/Mineradio", "langchain-ai/openwiki", "stablyai/orca", "ZhuLinsen/daily_stock_analysis", "xbtlin/ai-berkshire", "google-labs-code/design.md", "baidu/Unlimited-OCR", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [143, 144, 146, 149, 149, 157, 159, 160, 171, 179, 182, 188, 194, 198, 201, 229, 235, 254, 330, 474]}
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
| 1 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +16 | 18123 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +13 | 26975 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +9 | 27238 |
| 4 | [oblien/openship](https://github.com/oblien/openship) | +9 | 7833 |
| 5 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +7 | 42824 |
| 6 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +6 | 21557 |
| 7 | [block/buzz](https://github.com/block/buzz) | +5 | 6538 |
| 8 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 4097 |
| 9 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 25806 |
| 10 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 29351 |
| 11 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 26900 |
| 12 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +3 | 7575 |
| 13 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +3 | 19378 |
| 14 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +3 | 7811 |
| 15 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +3 | 2899 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +3 | 29876 |
| 17 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +3 | 29406 |
| 18 | [agegr/pi-web](https://github.com/agegr/pi-web) | +3 | 2324 |
| 19 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 18283 |
| 20 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +2 | 19940 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2 | 46249 |
| 22 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +2 | 6945 |
| 23 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +2 | 12043 |
| 24 | [every-app/open-seo](https://github.com/every-app/open-seo) | +2 | 7450 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +2 | 30718 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2 | 44565 |
| 27 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 45950 |
| 28 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +2 | 27654 |
| 29 | [nubjs/nub](https://github.com/nubjs/nub) | +2 | 3036 |
| 30 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +2 | 10650 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +50 | 12043 |
| 2 | [oblien/openship](https://github.com/oblien/openship) | +38 | 7833 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +36 | 26975 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +32 | 27238 |
| 5 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 19940 |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +23 | 20192 |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +22 | 42824 |
| 8 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +19 | 18123 |
| 9 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +18 | 25806 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +18 | 46249 |
| 11 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +18 | 26900 |
| 12 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +17 | 25771 |
| 13 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +16 | 21557 |
| 14 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +16 | 6147 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +16 | 43688 |
| 16 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +15 | 18283 |
| 17 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +14 | 29351 |
| 18 | [block/buzz](https://github.com/block/buzz) | +13 | 6538 |
| 19 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +13 | 10692 |
| 20 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +12 | 10977 |
| 21 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +12 | 15090 |
| 22 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 4097 |
| 23 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +10 | 41616 |
| 24 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +10 | 2899 |
| 25 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +10 | 7811 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +10 | 7113 |
| 27 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +10 | 4396 |
| 28 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +10 | 16715 |
| 29 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1518 |
| 30 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +10 | 11184 |
| 31 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +9 | 1534 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +9 | 19378 |
| 33 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +9 | 4772 |
| 34 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4843 |
| 35 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +9 | 13035 |
| 36 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1405 |
| 37 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +9 | 4972 |
| 38 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +8 | 29876 |
| 39 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 30718 |
| 40 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 7255 |
| 41 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +8 | 2163 |
| 42 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +8 | 2069 |
| 43 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +8 | 7101 |
| 44 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +7 | 6505 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 41399 |
| 46 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +7 | 14746 |
| 47 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +7 | 34551 |
| 48 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +7 | 12165 |
| 49 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +7 | 7841 |
| 50 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +7 | 9751 |
| 51 | [deer-flow/llm-space](https://github.com/deer-flow/llm-space) | +7 | 1210 |
| 52 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 7451 |
| 53 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 41733 |
| 54 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +6 | 1538 |
| 55 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +6 | 27654 |
| 56 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +6 | 6183 |
| 57 | [stupside/castor](https://github.com/stupside/castor) | +6 | 1863 |
| 58 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 37180 |
| 59 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6012 |
| 60 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 49088 |
| 61 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +6 | 3133 |
| 62 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +6 | 4507 |
| 63 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 11233 |
| 64 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +6 | 41852 |
| 65 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +6 | 24126 |
| 66 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 2076 |
| 67 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +6 | 1972 |
| 68 | [browser-use/video-use](https://github.com/browser-use/video-use) | +5 | 17666 |
| 69 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 9913 |
| 70 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 10505 |
| 71 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 45950 |
| 72 | [tw93/Waza](https://github.com/tw93/Waza) | +5 | 6598 |
| 73 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 33841 |
| 74 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 40771 |
| 75 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +5 | 13964 |
| 76 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 26348 |
| 77 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +5 | 501 |
| 78 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +5 | 7665 |
| 79 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +5 | 6202 |
| 80 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +5 | 18920 |
| 81 | [apache/ossie](https://github.com/apache/ossie) | +5 | 1544 |
| 82 | [malisper/pgrust](https://github.com/malisper/pgrust) | +5 | 3738 |
| 83 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +5 | 6475 |
| 84 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +5 | 13748 |
| 85 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +5 | 946 |
| 86 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 3436 |
| 87 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +4 | 4061 |
| 88 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 9295 |
| 89 | [agegr/pi-web](https://github.com/agegr/pi-web) | +4 | 2324 |
| 90 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +4 | 30726 |
| 91 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +4 | 4168 |
| 92 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 1751 |
| 93 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 2731 |
| 94 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +4 | 12177 |
| 95 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +4 | 35286 |
| 96 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +4 | 26424 |
| 97 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +4 | 1354 |
| 98 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 5438 |
| 99 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 141 |
| 100 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +4 | 785 |
| 101 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 58450 |
| 102 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3 | 44565 |
| 103 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +3 | 23341 |
| 104 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +3 | 27598 |
| 105 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +3 | 7575 |
| 106 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +3 | 29406 |
| 107 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +3 | 1332 |
| 108 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +3 | 39217 |
| 109 | [Qualcomm-AI-research/MobileWan](https://github.com/Qualcomm-AI-research/MobileWan) | +3 | 71 |
| 110 | [openai/skills](https://github.com/openai/skills) | +3 | 24109 |
| 111 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +3 | 4054 |
| 112 | [inssekt/CocoonFE](https://github.com/inssekt/CocoonFE) | +3 | 1092 |
| 113 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2482 |
| 114 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +3 | 7677 |
| 115 | [google-research/tabfm](https://github.com/google-research/tabfm) | +3 | 2058 |
| 116 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 7865 |
| 117 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 4298 |
| 118 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +3 | 5183 |
| 119 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +3 | 966 |
| 120 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +3 | 13586 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +474 | 41616 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +330 | 34551 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +254 | 43688 |
| 4 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +235 | 18123 |
| 5 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +229 | 26290 |
| 6 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +201 | 13748 |
| 7 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +198 | 58450 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +194 | 27238 |
| 9 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 13035 |
| 10 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8804 |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +179 | 29876 |
| 12 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +171 | 19940 |
| 13 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +160 | 29218 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +159 | 46249 |
| 15 | [apple/container](https://github.com/apple/container) | +157 | 48228 |
| 16 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +149 | 25771 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +149 | 40771 |
| 18 | [facebook/astryx](https://github.com/facebook/astryx) | +146 | 10505 |
| 19 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18937 |
| 20 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +143 | 26271 |
| 21 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +139 | 26975 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +138 | 27598 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +137 | 26900 |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +130 | 29781 |
| 25 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +130 | 9245 |
| 26 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5495 |
| 27 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +120 | 16715 |
| 28 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +116 | 26424 |
| 29 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 4051 |
| 30 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +96 | 6944 |
| 31 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +95 | 16796 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +94 | 30718 |
| 33 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +89 | 20192 |
| 34 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +87 | 5438 |
| 35 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10556 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +86 | 49089 |
| 37 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 17666 |
| 38 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +81 | 18283 |
| 39 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6749 |
| 40 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +79 | 11185 |
| 41 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +79 | 37180 |
| 42 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6641 |
| 43 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +77 | 6183 |
| 44 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +77 | 8825 |
| 45 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 15090 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +70 | 39217 |
| 47 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +68 | 21557 |
| 48 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8699 |
| 49 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +67 | 6475 |
| 50 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +67 | 13586 |
| 51 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +64 | 9751 |
| 52 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +62 | 41852 |
| 53 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +62 | 26348 |
| 54 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +60 | 12043 |
| 55 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +60 | 3913 |
| 56 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2978 |
| 57 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +59 | 7113 |
| 58 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +59 | 14746 |
| 59 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +58 | 42824 |
| 60 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +58 | 41399 |
| 61 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +58 | 24472 |
| 62 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +55 | 47477 |
| 63 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27556 |
| 64 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +54 | 27654 |
| 65 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +53 | 19378 |
| 66 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +53 | 11465 |
| 67 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +52 | 26237 |
| 68 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5125 |
| 69 | [multica-ai/multica](https://github.com/multica-ai/multica) | +50 | 41733 |
| 70 | [antirez/ds4](https://github.com/antirez/ds4) | +50 | 19130 |
| 71 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +48 | 33841 |
| 72 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +48 | 7255 |
| 73 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3792 |
| 74 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +48 | 11196 |
| 75 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +48 | 29939 |
| 76 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +47 | 23386 |
| 77 | [every-app/open-seo](https://github.com/every-app/open-seo) | +47 | 7451 |
| 78 | [EpicGames/lore](https://github.com/EpicGames/lore) | +47 | 8169 |
| 79 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +46 | 3840 |
| 80 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +46 | 3840 |
| 81 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +45 | 28625 |
| 82 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +45 | 35286 |
| 83 | [blader/humanizer](https://github.com/blader/humanizer) | +45 | 30618 |
| 84 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +45 | 40365 |
| 85 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9790 |
| 86 | [tigicion/dao-code](https://github.com/tigicion/dao-code) | +44 | 1376 |
| 87 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 2058 |
| 88 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +43 | 27056 |
| 89 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +43 | 9846 |
| 90 | [decolua/9router](https://github.com/decolua/9router) | +42 | 23290 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +42 | 23074 |
| 92 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +42 | 26928 |
| 93 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +42 | 24331 |
| 94 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +41 | 18920 |
| 95 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +41 | 7677 |
| 96 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +40 | 5183 |
| 97 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +39 | 10628 |
| 98 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2028 |
| 99 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +38 | 6505 |
| 100 | [oblien/openship](https://github.com/oblien/openship) | +38 | 7833 |
| 101 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +35 | 9433 |
| 102 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +35 | 8418 |
| 103 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +34 | 31558 |
| 104 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +34 | 7092 |
| 105 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +33 | 24126 |
| 106 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +33 | 4972 |
| 107 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +31 | 25806 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +31 | 34084 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +31 | 12165 |
| 110 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +31 | 45950 |
| 111 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +31 | 25676 |
| 112 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2184 |
| 113 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2591 |
| 114 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +30 | 29025 |
| 115 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +30 | 6294 |
| 116 | [anbeime/skill](https://github.com/anbeime/skill) | +30 | 4095 |
| 117 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +29 | 43770 |
| 118 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1332 |
| 119 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +28 | 32550 |
| 120 | [openai/plugins](https://github.com/openai/plugins) | +28 | 4703 |
| 121 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +27 | 25924 |
| 122 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15214 |
| 123 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +26 | 6446 |
| 124 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +26 | 1144 |
| 125 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +26 | 27127 |
| 126 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +25 | 29351 |
| 127 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +25 | 2089 |
| 128 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 17006 |
| 129 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +24 | 6945 |
| 130 | [openai/skills](https://github.com/openai/skills) | +24 | 24109 |
| 131 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 7811 |
| 132 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +24 | 7106 |
| 133 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1835 |
| 134 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +23 | 1162 |
| 135 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +22 | 5050 |
| 136 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +22 | 17798 |
| 137 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +22 | 9931 |
| 138 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +22 | 18111 |
| 139 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1676 |
| 140 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 4972 |
| 141 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1412 |
| 142 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 729 |
| 143 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 2090 |
| 144 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 145 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +21 | 2842 |
| 146 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +21 | 12734 |
| 147 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 4168 |
| 148 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +20 | 4795 |
| 149 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +20 | 1797 |
| 150 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 151 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 9913 |
| 152 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +19 | 8925 |
| 153 | [browser-act/skills](https://github.com/browser-act/skills) | +19 | 4706 |
| 154 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +19 | 4054 |
| 155 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +19 | 3583 |
| 156 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +19 | 4097 |
| 157 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1958 |
| 158 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +19 | 2117 |
| 159 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7857 |
| 160 | [jundot/omlx](https://github.com/jundot/omlx) | +18 | 18118 |
| 161 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1420 |
| 162 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2005 |
| 163 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +17 | 27144 |
| 164 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +17 | 1856 |
| 165 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1738 |
| 166 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +17 | 5702 |
| 167 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +17 | 3756 |
| 168 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 673 |
| 169 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +17 | 27757 |
| 170 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10692 |
| 171 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 4507 |
| 172 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 458 |
| 173 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +16 | 15247 |
| 174 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +16 | 33733 |
| 175 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +16 | 18738 |
| 176 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +16 | 22975 |
| 177 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +15 | 2731 |
| 178 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +15 | 3613 |
| 179 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +15 | 3218 |
| 180 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +15 | 3935 |
| 181 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +15 | 2592 |
| 182 | [ascending-llc/jarvis-registry](https://github.com/ascending-llc/jarvis-registry) | +15 | 2427 |
| 183 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +15 | 4396 |
| 184 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +15 | 2069 |
| 185 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +15 | 29406 |
| 186 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 401 |
| 187 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +14 | 16459 |
| 188 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +14 | 4511 |
| 189 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +14 | 7166 |
| 190 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +14 | 2629 |
| 191 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +14 | 4843 |
| 192 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +13 | 13774 |
| 193 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1020 |
| 194 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +13 | 8742 |
| 195 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +13 | 26742 |
| 196 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 197 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +12 | 7972 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +12 | 18462 |
| 199 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +12 | 687 |
| 200 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +11 | 9295 |
| 201 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 719 |
| 202 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 705 |
| 203 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 204 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +10 | 2899 |
| 205 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 878 |
| 206 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1096 |
| 207 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +10 | 11962 |
| 208 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 431 |
| 209 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +10 | 8647 |
| 210 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 370 |
| 211 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +10 | 6464 |
| 212 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +10 | 1363 |
| 213 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 691 |
| 214 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 147 |
| 215 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +10 | 569 |
| 216 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1405 |
| 217 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5118 |
| 218 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +9 | 5581 |
| 219 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 2909 |
| 220 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +8 | 6234 |
| 221 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +8 | 9096 |
| 222 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +8 | 2959 |
| 223 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +8 | 2948 |
| 224 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5808 |
| 225 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 412 |
| 226 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +8 | 2959 |
| 227 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +7 | 2571 |
| 228 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 641 |
| 229 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 959 |
| 230 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1995 |
| 231 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1073 |
| 232 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 233 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 166 |
| 234 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +7 | 4671 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +7 | 3293 |
| 236 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 459 |
| 237 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 964 |
| 238 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 456 |
| 239 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14325 |
| 240 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +6 | 460 |
| 241 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 559 |
| 242 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +6 | 462 |
| 243 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6012 |
| 244 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10041 |
| 245 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 192 |
| 246 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +5 | 453 |
| 247 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5960 |
| 248 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 325 |
| 249 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 599 |
| 250 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1637 |
| 251 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 606 |
| 252 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 309 |
| 253 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +5 | 1913 |
| 254 | [rpamis/comet](https://github.com/rpamis/comet) | +5 | 2475 |
| 255 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +5 | 561 |
| 256 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3774 |
| 257 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 752 |
| 258 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +4 | 911 |
| 259 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +4 | 915 |
| 260 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 536 |
| 261 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 920 |
| 262 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 570 |
| 263 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +4 | 234 |
| 264 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 378 |
| 265 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 644 |
| 266 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2796 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2911 |
| 268 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 2927 |
| 269 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 671 |
| 270 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +4 | 964 |
| 271 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +3 | 1386 |
| 272 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 273 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 274 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9387 |
| 275 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 154 |
| 276 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2590 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1867 |
| 278 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 564 |
| 279 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 264 |
| 280 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 104 |
| 281 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 129 |
| 282 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 283 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 284 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +3 | 2800 |
| 285 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 89 |
| 286 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 94 |
| 287 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 176 |
| 288 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 420 |
| 289 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 781 |
| 290 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 164 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 270 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 847 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1700 |
| 294 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 757 |
| 295 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 708 |
| 296 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2429 |
| 297 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 740 |
| 298 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 342 |
| 299 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 300 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 116 |
