---
title: "2026-07-19 GitHub增长趋势报告"
description: "1.lingbot-map+7 2.kimi-cli+7 3.nullhub+6 4.ui-skills+6 5.orca+6"
date: 2026-07-19T20:51:57+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-19 20:51:57

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
        'daily': {"categories": ["MadsLorentzen/ai-job-search", "sectionpoemchant/Meccha-Chameleon-Phantom", "ogulcancelik/herdr", "tirth8205/code-review-graph", "Open-Dev-Society/OpenStock", "microsoft/Ontology-Playground", "jamiepine/voicebox", "hasaneyldrm/exercises-dataset", "emilkowalski/skills", "yizhiyanhua-ai/fireworks-tech-graph", "HKUDS/Vibe-Trading", "laoma2053/awesome-zhuiju-free", "getpaseo/paseo", "iflytek/skillhub", "diegosouzapw/OmniRoute", "stablyai/orca", "ibelick/ui-skills", "nullclaw/nullhub", "MoonshotAI/kimi-cli", "Robbyant/lingbot-map"], "data": [3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7]},
        'weekly': {"categories": ["MDX-Tom/gpt-5.6-instruct", "x4gKing/X4G", "PrismML-Eng/Bonsai-demo", "HenryNdubuaku/maths-cs-ai-compendium", "calesthio/OpenMontage", "tt-a1i/archify", "Dicklesworthstone/destructive_command_guard", "jamiepine/voicebox", "diegosouzapw/OmniRoute", "k1tbyte/Wand-Enhancer", "oso95/scroll-world", "hasaneyldrm/exercises-dataset", "MadsLorentzen/ai-job-search", "iOfficeAI/OfficeCLI", "ogulcancelik/herdr", "stablyai/orca", "emilkowalski/skills", "HKUDS/Vibe-Trading", "Fei-Away/Codex-Dream-Skin", "JustVugg/colibri"], "data": [13, 13, 14, 14, 15, 15, 16, 17, 18, 19, 20, 20, 20, 22, 23, 28, 34, 37, 50, 55]},
        'monthly': {"categories": ["StarTrail-org/PixelRAG", "mukul975/Anthropic-Cybersecurity-Skills", "ogulcancelik/herdr", "hugohe3/ppt-master", "XxHuberrr/Mineradio", "apple/container", "topoteretes/cognee", "langchain-ai/openwiki", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "xbtlin/ai-berkshire", "jamiepine/voicebox", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "DietrichGebert/ponytail"], "data": [151, 169, 179, 182, 182, 184, 186, 186, 189, 194, 201, 203, 227, 230, 249, 278, 283, 466, 614, 880]}
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
| 1 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +7 | 13569 |
| 2 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +7 | 9839 |
| 3 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +6 | 1241 |
| 4 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +6 | 5400 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +6 | 22246 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +6 | 20138 |
| 7 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 4736 |
| 8 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +5 | 10864 |
| 9 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 3687 |
| 10 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +5 | 25247 |
| 11 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 8962 |
| 12 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +4 | 18146 |
| 13 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 16015 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +4 | 43250 |
| 15 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +4 | 1316 |
| 16 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +4 | 13919 |
| 17 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 21033 |
| 18 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +4 | 18336 |
| 19 | [sectionpoemchant/Meccha-Chameleon-Phantom](https://github.com/sectionpoemchant/Meccha-Chameleon-Phantom) | +3 | 92 |
| 20 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 24052 |
| 21 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +3 | 5870 |
| 22 | [Orkas-AI/Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) | +3 | 328 |
| 23 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 11805 |
| 24 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +3 | 567 |
| 25 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +3 | 8832 |
| 26 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2393 |
| 27 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +3 | 16459 |
| 28 | [cloudflare/skills](https://github.com/cloudflare/skills) | +3 | 2395 |
| 29 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +3 | 324 |
| 30 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +3 | 1146 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +55 | 16459 |
| 2 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +50 | 10266 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +37 | 25247 |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +34 | 18146 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +28 | 22246 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +23 | 18336 |
| 7 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +22 | 19610 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +20 | 24052 |
| 9 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +20 | 16015 |
| 10 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +20 | 3801 |
| 11 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +19 | 9819 |
| 12 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +18 | 20138 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +17 | 43250 |
| 14 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +16 | 5154 |
| 15 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +15 | 5942 |
| 16 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +15 | 40099 |
| 17 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +14 | 6946 |
| 18 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +14 | 1852 |
| 19 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +13 | 5855 |
| 20 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +13 | 2154 |
| 21 | [usestrix/strix](https://github.com/usestrix/strix) | +12 | 42629 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 39941 |
| 23 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +12 | 32945 |
| 24 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +11 | 13569 |
| 25 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +11 | 27896 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +11 | 36261 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +11 | 48099 |
| 28 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +11 | 9227 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +11 | 40900 |
| 30 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +11 | 23459 |
| 31 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +11 | 3505 |
| 32 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +11 | 6411 |
| 33 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +10 | 5400 |
| 34 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1166 |
| 35 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +10 | 12423 |
| 36 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1146 |
| 37 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +9 | 5738 |
| 38 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +9 | 1299 |
| 39 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +9 | 3687 |
| 40 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +9 | 7610 |
| 41 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +9 | 2701 |
| 42 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +8 | 1925 |
| 43 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +8 | 9839 |
| 44 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +8 | 567 |
| 45 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 41070 |
| 46 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +8 | 1010 |
| 47 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +8 | 32958 |
| 48 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +8 | 1921 |
| 49 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +8 | 25809 |
| 50 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 40735 |
| 51 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +7 | 13590 |
| 52 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +7 | 8632 |
| 53 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 13380 |
| 54 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +7 | 3813 |
| 55 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +7 | 27150 |
| 56 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +7 | 7230 |
| 57 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +7 | 856 |
| 58 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 2995 |
| 59 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +7 | 28440 |
| 60 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +7 | 18664 |
| 61 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 7330 |
| 62 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +7 | 4619 |
| 63 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +7 | 14899 |
| 64 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +6 | 1241 |
| 65 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 57901 |
| 66 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +6 | 8962 |
| 67 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 39588 |
| 68 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 4736 |
| 69 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 10864 |
| 70 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 29750 |
| 71 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 11805 |
| 72 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 8608 |
| 73 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 615 |
| 74 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +6 | 3868 |
| 75 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 18471 |
| 76 | [malisper/pgrust](https://github.com/malisper/pgrust) | +6 | 3530 |
| 77 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 2409 |
| 78 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +6 | 10483 |
| 79 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +6 | 33784 |
| 80 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +6 | 2580 |
| 81 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +6 | 1113 |
| 82 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +5 | 28793 |
| 83 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +5 | 21034 |
| 84 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +5 | 8832 |
| 85 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 27322 |
| 86 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 28627 |
| 87 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +5 | 6316 |
| 88 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +5 | 1625 |
| 89 | [Chunyu33/light-c](https://github.com/Chunyu33/light-c) | +5 | 958 |
| 90 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +5 | 11561 |
| 91 | [Cjbuilds/Codex-Orchestration](https://github.com/Cjbuilds/Codex-Orchestration) | +5 | 473 |
| 92 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +5 | 4781 |
| 93 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +5 | 6176 |
| 94 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +5 | 5529 |
| 95 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +5 | 25739 |
| 96 | [littledivy/mimic](https://github.com/littledivy/mimic) | +5 | 1204 |
| 97 | [x4gKing/Marzban-Panel](https://github.com/x4gKing/Marzban-Panel) | +4 | 937 |
| 98 | [x4gKing/Marzban-Node](https://github.com/x4gKing/Marzban-Node) | +4 | 814 |
| 99 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 1540 |
| 100 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +4 | 26069 |
| 101 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +4 | 1316 |
| 102 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +4 | 13919 |
| 103 | [apache/ossie](https://github.com/apache/ossie) | +4 | 1376 |
| 104 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +4 | 324 |
| 105 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 29908 |
| 106 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 251 |
| 107 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +4 | 7504 |
| 108 | [lynote-ai/ai-image-detector](https://github.com/lynote-ai/ai-image-detector) | +4 | 258 |
| 109 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 17262 |
| 110 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +4 | 7768 |
| 111 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +4 | 531 |
| 112 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +4 | 38483 |
| 113 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 31214 |
| 114 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 8784 |
| 115 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +4 | 14920 |
| 116 | [x4gKing/PasarGuard-Node](https://github.com/x4gKing/PasarGuard-Node) | +3 | 657 |
| 117 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2393 |
| 118 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 43588 |
| 119 | [ufy2024/AuC](https://github.com/ufy2024/AuC) | +3 | 645 |
| 120 | [valqore/valqore](https://github.com/valqore/valqore) | +3 | 1525 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +880 | 86061 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +614 | 40099 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +466 | 32945 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +283 | 57901 |
| 5 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +278 | 10813 |
| 6 | [usestrix/strix](https://github.com/usestrix/strix) | +249 | 42629 |
| 7 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +230 | 26094 |
| 8 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 14550 |
| 9 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +203 | 43251 |
| 10 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +201 | 13380 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +194 | 22246 |
| 12 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +189 | 28793 |
| 13 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +186 | 12423 |
| 14 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +186 | 28471 |
| 15 | [apple/container](https://github.com/apple/container) | +184 | 48025 |
| 16 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8608 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +182 | 39941 |
| 18 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +179 | 18336 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +169 | 26069 |
| 20 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +151 | 6864 |
| 21 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +146 | 18767 |
| 22 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +145 | 25247 |
| 23 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +144 | 27150 |
| 24 | [facebook/astryx](https://github.com/facebook/astryx) | +142 | 9191 |
| 25 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +141 | 25602 |
| 26 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +140 | 8632 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +139 | 24052 |
| 28 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +133 | 29329 |
| 29 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5353 |
| 30 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +122 | 20138 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +122 | 29750 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +121 | 16413 |
| 33 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +119 | 16015 |
| 34 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +116 | 36261 |
| 35 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 36 | [EpicGames/lore](https://github.com/EpicGames/lore) | +109 | 8103 |
| 37 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3969 |
| 38 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +104 | 4805 |
| 39 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +103 | 13424 |
| 40 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +102 | 6619 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +101 | 48099 |
| 42 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +97 | 8431 |
| 43 | [google-research/timesfm](https://github.com/google-research/timesfm) | +97 | 26974 |
| 44 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +96 | 38483 |
| 45 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +91 | 18146 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +90 | 40900 |
| 47 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10433 |
| 48 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +87 | 25809 |
| 49 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +85 | 4881 |
| 50 | [browser-use/video-use](https://github.com/browser-use/video-use) | +83 | 17262 |
| 51 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6696 |
| 52 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +79 | 40735 |
| 53 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +78 | 9819 |
| 54 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6498 |
| 55 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +76 | 19610 |
| 56 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +76 | 27322 |
| 57 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +75 | 5738 |
| 58 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +75 | 6176 |
| 59 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +75 | 18471 |
| 60 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +74 | 16459 |
| 61 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +73 | 11318 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +73 | 29908 |
| 63 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 13569 |
| 64 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +69 | 24024 |
| 65 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +68 | 8340 |
| 66 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +68 | 24006 |
| 67 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +67 | 13166 |
| 68 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +67 | 10699 |
| 69 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +66 | 9227 |
| 70 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +64 | 39588 |
| 71 | [multica-ai/multica](https://github.com/multica-ai/multica) | +64 | 41070 |
| 72 | [antirez/ds4](https://github.com/antirez/ds4) | +63 | 18849 |
| 73 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +62 | 47190 |
| 74 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +62 | 7504 |
| 75 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +62 | 3793 |
| 76 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +61 | 25932 |
| 77 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +60 | 6411 |
| 78 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2906 |
| 79 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +59 | 3518 |
| 80 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +58 | 26613 |
| 81 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2802 |
| 82 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +57 | 5942 |
| 83 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +57 | 28296 |
| 84 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +56 | 8784 |
| 85 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +55 | 21678 |
| 86 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27481 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +54 | 32958 |
| 88 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +54 | 39990 |
| 89 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +53 | 38759 |
| 90 | [decolua/9router](https://github.com/decolua/9router) | +52 | 22694 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +52 | 22814 |
| 92 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +52 | 7437 |
| 93 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +51 | 26618 |
| 94 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +51 | 23218 |
| 95 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +51 | 31214 |
| 96 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +50 | 10266 |
| 97 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 4997 |
| 98 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +50 | 23459 |
| 99 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +50 | 9626 |
| 100 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +49 | 18664 |
| 101 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3698 |
| 102 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +45 | 4781 |
| 103 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +44 | 3703 |
| 104 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +43 | 33784 |
| 105 | [google-research/tabfm](https://github.com/google-research/tabfm) | +41 | 1872 |
| 106 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +41 | 25739 |
| 107 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +41 | 8282 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +40 | 28627 |
| 109 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2026 |
| 110 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +38 | 32341 |
| 111 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1403 |
| 112 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +37 | 36103 |
| 113 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +37 | 27484 |
| 114 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +36 | 5855 |
| 115 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +36 | 43588 |
| 116 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +36 | 11805 |
| 117 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +36 | 6200 |
| 118 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +36 | 9783 |
| 119 | [anbeime/skill](https://github.com/anbeime/skill) | +36 | 3897 |
| 120 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +35 | 25518 |
| 121 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +35 | 45592 |
| 122 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +33 | 22876 |
| 123 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +32 | 6057 |
| 124 | [openai/plugins](https://github.com/openai/plugins) | +32 | 4614 |
| 125 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +32 | 26948 |
| 126 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2133 |
| 127 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +31 | 17290 |
| 128 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +31 | 1311 |
| 129 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2517 |
| 130 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +31 | 12546 |
| 131 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +30 | 6838 |
| 132 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1277 |
| 133 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +29 | 2023 |
| 134 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1144 |
| 135 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +28 | 6608 |
| 136 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +28 | 3855 |
| 137 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +28 | 2108 |
| 138 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15181 |
| 139 | [openai/skills](https://github.com/openai/skills) | +27 | 23952 |
| 140 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2579 |
| 141 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +26 | 1193 |
| 142 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +25 | 5582 |
| 143 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +24 | 4760 |
| 144 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +24 | 5529 |
| 145 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +24 | 17963 |
| 146 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1711 |
| 147 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +24 | 3112 |
| 148 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +24 | 8308 |
| 149 | [floci-io/floci](https://github.com/floci-io/floci) | +24 | 16907 |
| 150 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 451 |
| 151 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +23 | 8722 |
| 152 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1746 |
| 153 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +23 | 33626 |
| 154 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +23 | 4635 |
| 155 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +23 | 3403 |
| 156 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +23 | 18579 |
| 157 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +23 | 1925 |
| 158 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +23 | 7230 |
| 159 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 2014 |
| 160 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1662 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +22 | 17961 |
| 162 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +22 | 1977 |
| 163 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 3801 |
| 164 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +21 | 21034 |
| 165 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1348 |
| 166 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +21 | 8750 |
| 167 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 858 |
| 168 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +21 | 5744 |
| 169 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +21 | 16111 |
| 170 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 171 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 3784 |
| 172 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +20 | 26515 |
| 173 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 174 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +20 | 1330 |
| 175 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +19 | 7768 |
| 176 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +19 | 27896 |
| 177 | [browser-act/skills](https://github.com/browser-act/skills) | +19 | 4526 |
| 178 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +19 | 26959 |
| 179 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +19 | 3868 |
| 180 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1945 |
| 181 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +18 | 16267 |
| 182 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +18 | 1829 |
| 183 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1951 |
| 184 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +17 | 2522 |
| 185 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 663 |
| 186 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +17 | 26583 |
| 187 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +16 | 7030 |
| 188 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +16 | 8453 |
| 189 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +15 | 8962 |
| 190 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 398 |
| 191 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +15 | 18330 |
| 192 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +14 | 3813 |
| 193 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +14 | 29218 |
| 194 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +14 | 7836 |
| 195 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +14 | 4325 |
| 196 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +14 | 2803 |
| 197 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +14 | 6376 |
| 198 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +14 | 670 |
| 199 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +13 | 2154 |
| 200 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1013 |
| 201 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +13 | 2903 |
| 202 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +13 | 5871 |
| 203 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 204 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +13 | 4736 |
| 205 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 522 |
| 206 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +12 | 2755 |
| 207 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +12 | 8525 |
| 208 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +12 | 5482 |
| 209 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 3687 |
| 210 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +11 | 4481 |
| 211 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 691 |
| 212 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +11 | 11907 |
| 213 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 700 |
| 214 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 828 |
| 215 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 352 |
| 216 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2917 |
| 217 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 856 |
| 218 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1069 |
| 219 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 429 |
| 220 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 366 |
| 221 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 651 |
| 222 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 461 |
| 223 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 205 |
| 224 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1146 |
| 225 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 9015 |
| 226 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +9 | 1460 |
| 227 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +9 | 4557 |
| 228 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2462 |
| 229 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5782 |
| 230 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 859 |
| 231 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 813 |
| 232 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 398 |
| 233 | [rpamis/comet](https://github.com/rpamis/comet) | +8 | 2363 |
| 234 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 207 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +8 | 3223 |
| 236 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 620 |
| 237 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6180 |
| 238 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1972 |
| 239 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1041 |
| 240 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 241 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 165 |
| 242 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +7 | 1892 |
| 243 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 363 |
| 244 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +7 | 4878 |
| 245 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1777 |
| 246 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +7 | 693 |
| 247 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 459 |
| 248 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +6 | 5919 |
| 249 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 615 |
| 250 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 412 |
| 251 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1610 |
| 252 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 549 |
| 253 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 635 |
| 254 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +6 | 373 |
| 255 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 9936 |
| 256 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +6 | 2861 |
| 257 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 187 |
| 258 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2786 |
| 259 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +6 | 488 |
| 260 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +5 | 1359 |
| 261 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 311 |
| 262 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 660 |
| 263 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 590 |
| 264 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 559 |
| 265 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2744 |
| 266 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3739 |
| 267 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +5 | 917 |
| 268 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 96 |
| 269 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2872 |
| 270 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 623 |
| 271 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 334 |
| 272 | [databufflabs/databuff](https://github.com/databufflabs/databuff) | +4 | 328 |
| 273 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 274 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +3 | 5921 |
| 275 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 148 |
| 276 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2583 |
| 277 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 559 |
| 278 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 122 |
| 279 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 25 |
| 280 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 281 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 706 |
| 282 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1838 |
| 283 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +3 | 3166 |
| 284 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +3 | 256 |
| 285 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +2 | 9361 |
| 286 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 86 |
| 287 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 747 |
| 288 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 91 |
| 289 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 167 |
| 290 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 419 |
| 291 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 786 |
| 292 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2398 |
| 293 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 151 |
| 294 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 196 |
| 295 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 264 |
| 296 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 842 |
| 297 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1694 |
| 298 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 690 |
| 299 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3393 |
| 300 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
