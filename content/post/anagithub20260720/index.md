---
title: "2026-07-20 GitHub增长趋势报告"
description: "1.ai-engineering-from-scratch+5 2.kimi-cli+5 3.herdr+4 4.astron-rpa+4 5.awesome-zhuiju-free+4"
date: 2026-07-20T21:13:18+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-20 21:13:18

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
        'daily': {"categories": ["MatheuZSecurity/Furtex", "1jehuang/jcode", "dramaclaw/dramaclaw", "langchain-ai/openwiki", "coreyhaines31/marketingskills", "microsoft/Ontology-Playground", "ibelick/ui-skills", "stupside/castor", "usestrix/strix", "hoainho/img2threejs", "HKUDS/DeepTutor", "MadsLorentzen/ai-job-search", "HKUDS/Vibe-Trading", "emilkowalski/skills", "diegosouzapw/OmniRoute", "laoma2053/awesome-zhuiju-free", "iflytek/astron-rpa", "ogulcancelik/herdr", "MoonshotAI/kimi-cli", "rohitg00/ai-engineering-from-scratch"], "data": [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5]},
        'weekly': {"categories": ["ibelick/ui-skills", "MoonshotAI/kimi-cli", "PrismML-Eng/Bonsai-demo", "HenryNdubuaku/maths-cs-ai-compendium", "HKUDS/DeepTutor", "tt-a1i/archify", "jamiepine/voicebox", "usestrix/strix", "k1tbyte/Wand-Enhancer", "oso95/scroll-world", "hasaneyldrm/exercises-dataset", "diegosouzapw/OmniRoute", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search", "ogulcancelik/herdr", "stablyai/orca", "HKUDS/Vibe-Trading", "emilkowalski/skills", "JustVugg/colibri", "Fei-Away/Codex-Dream-Skin"], "data": [13, 13, 14, 14, 14, 15, 15, 15, 15, 17, 18, 18, 22, 22, 25, 26, 34, 34, 41, 56]},
        'monthly': {"categories": ["StarTrail-org/PixelRAG", "mukul975/Anthropic-Cybersecurity-Skills", "hugohe3/ppt-master", "apple/container", "XxHuberrr/Mineradio", "ogulcancelik/herdr", "topoteretes/cognee", "JCodesMore/ai-website-cloner-template", "langchain-ai/openwiki", "stablyai/orca", "jamiepine/voicebox", "xbtlin/ai-berkshire", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "DietrichGebert/ponytail"], "data": [149, 167, 175, 178, 182, 183, 185, 187, 188, 191, 200, 201, 227, 229, 252, 255, 280, 440, 603, 830]}
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
| 1 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +5 | 40451 |
| 2 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +5 | 10198 |
| 3 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +4 | 18741 |
| 4 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +4 | 6018 |
| 5 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +4 | 3979 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 21568 |
| 7 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 18814 |
| 8 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 25658 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 24370 |
| 10 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 28344 |
| 11 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +3 | 934 |
| 12 | [usestrix/strix](https://github.com/usestrix/strix) | +3 | 42886 |
| 13 | [stupside/castor](https://github.com/stupside/castor) | +3 | 1602 |
| 14 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +3 | 5632 |
| 15 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +3 | 1683 |
| 16 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 40890 |
| 17 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +2 | 12615 |
| 18 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +2 | 1750 |
| 19 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 9550 |
| 20 | [MatheuZSecurity/Furtex](https://github.com/MatheuZSecurity/Furtex) | +2 | 101 |
| 21 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +2 | 912 |
| 22 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +2 | 1607 |
| 23 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +2 | 7439 |
| 24 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +2 | 9650 |
| 25 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +2 | 4818 |
| 26 | [Qualcomm-AI-research/MobileWan](https://github.com/Qualcomm-AI-research/MobileWan) | +2 | 59 |
| 27 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2 | 33885 |
| 28 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +2 | 7718 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +2 | 18658 |
| 30 | [xianyu110/gpt-codex](https://github.com/xianyu110/gpt-codex) | +2 | 1018 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +56 | 11051 |
| 2 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +41 | 16895 |
| 3 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +34 | 18814 |
| 4 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +34 | 25658 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +26 | 23404 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 18741 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +22 | 24370 |
| 8 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +22 | 20121 |
| 9 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +18 | 21568 |
| 10 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +18 | 16241 |
| 11 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +17 | 4362 |
| 12 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +15 | 10181 |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | +15 | 42886 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +15 | 44086 |
| 15 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +15 | 6191 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +14 | 28344 |
| 17 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +14 | 7007 |
| 18 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +14 | 1894 |
| 19 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +13 | 10198 |
| 20 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +13 | 5632 |
| 21 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +13 | 2296 |
| 22 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 40479 |
| 23 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +12 | 12615 |
| 24 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +12 | 9382 |
| 25 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 5986 |
| 26 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 40450 |
| 27 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +11 | 22954 |
| 28 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +11 | 14143 |
| 29 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 3979 |
| 30 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +11 | 7718 |
| 31 | [deer-flow/llm-space](https://github.com/deer-flow/llm-space) | +11 | 1116 |
| 32 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +11 | 5190 |
| 33 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 40140 |
| 34 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1168 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +10 | 48307 |
| 36 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +10 | 36419 |
| 37 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +10 | 33225 |
| 38 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +10 | 41210 |
| 39 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +10 | 23637 |
| 40 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +9 | 40890 |
| 41 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +9 | 2001 |
| 42 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1209 |
| 43 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +9 | 3662 |
| 44 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +9 | 1314 |
| 45 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +9 | 1101 |
| 46 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +9 | 1952 |
| 47 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +9 | 25950 |
| 48 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 4818 |
| 49 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +8 | 654 |
| 50 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +8 | 7408 |
| 51 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +8 | 887 |
| 52 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 41211 |
| 53 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +8 | 33111 |
| 54 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 6564 |
| 55 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +7 | 1411 |
| 56 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 5838 |
| 57 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +7 | 1683 |
| 58 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +7 | 9549 |
| 59 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +7 | 13643 |
| 60 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 30010 |
| 61 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +7 | 27281 |
| 62 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 7439 |
| 63 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +7 | 18658 |
| 64 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 13491 |
| 65 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 3015 |
| 66 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +7 | 28519 |
| 67 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +7 | 4633 |
| 68 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 58018 |
| 69 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +6 | 1607 |
| 70 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6018 |
| 71 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 10926 |
| 72 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +6 | 27410 |
| 73 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +6 | 8804 |
| 74 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 11886 |
| 75 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +6 | 702 |
| 76 | [malisper/pgrust](https://github.com/malisper/pgrust) | +6 | 3623 |
| 77 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 8647 |
| 78 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +6 | 18727 |
| 79 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +6 | 33885 |
| 80 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +6 | 2745 |
| 81 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 736 |
| 82 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +5 | 9096 |
| 83 | [stupside/castor](https://github.com/stupside/castor) | +5 | 1602 |
| 84 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +5 | 26192 |
| 85 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +5 | 411 |
| 86 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +5 | 6045 |
| 87 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +5 | 4170 |
| 88 | [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | +5 | 13912 |
| 89 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +5 | 4884 |
| 90 | [yorgai/ORG2](https://github.com/yorgai/ORG2) | +5 | 2245 |
| 91 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +5 | 969 |
| 92 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +5 | 30520 |
| 93 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +5 | 2897 |
| 94 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 4075 |
| 95 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +5 | 6388 |
| 96 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +5 | 540 |
| 97 | [littledivy/mimic](https://github.com/littledivy/mimic) | +5 | 1358 |
| 98 | [x4gKing/Marzban-Panel](https://github.com/x4gKing/Marzban-Panel) | +4 | 981 |
| 99 | [x4gKing/Marzban-Node](https://github.com/x4gKing/Marzban-Node) | +4 | 849 |
| 100 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +4 | 23248 |
| 101 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 29076 |
| 102 | [hicccc77/WeFlow](https://github.com/hicccc77/WeFlow) | +4 | 13101 |
| 103 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +4 | 934 |
| 104 | [tw93/Waza](https://github.com/tw93/Waza) | +4 | 6566 |
| 105 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 4938 |
| 106 | [apache/ossie](https://github.com/apache/ossie) | +4 | 1426 |
| 107 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 254 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +4 | 28763 |
| 109 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +4 | 7547 |
| 110 | [Cjbuilds/Codex-Orchestration](https://github.com/Cjbuilds/Codex-Orchestration) | +4 | 488 |
| 111 | [lynote-ai/ai-image-detector](https://github.com/lynote-ai/ai-image-detector) | +4 | 302 |
| 112 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +4 | 6255 |
| 113 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +4 | 15161 |
| 114 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +4 | 8786 |
| 115 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 17364 |
| 116 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +4 | 7799 |
| 117 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +4 | 1142 |
| 118 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 8910 |
| 119 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +3 | 2372 |
| 120 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2405 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +830 | 86578 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +603 | 40479 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +440 | 33225 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +280 | 58018 |
| 5 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +255 | 10867 |
| 6 | [usestrix/strix](https://github.com/usestrix/strix) | +252 | 42886 |
| 7 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +229 | 26148 |
| 8 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 15280 |
| 9 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +201 | 13491 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +200 | 44086 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +191 | 23405 |
| 12 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 12615 |
| 13 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +187 | 29076 |
| 14 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 28730 |
| 15 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +183 | 18741 |
| 16 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8647 |
| 17 | [apple/container](https://github.com/apple/container) | +178 | 48064 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +175 | 40140 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +167 | 26192 |
| 20 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +149 | 6969 |
| 21 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +146 | 18804 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +145 | 27281 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +144 | 25658 |
| 24 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +142 | 24370 |
| 25 | [facebook/astryx](https://github.com/facebook/astryx) | +142 | 9531 |
| 26 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +142 | 25784 |
| 27 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +140 | 8804 |
| 28 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +133 | 29430 |
| 29 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5389 |
| 30 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +122 | 21568 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +120 | 30010 |
| 32 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +119 | 16241 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +114 | 16520 |
| 34 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 35 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +112 | 36419 |
| 36 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3974 |
| 37 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +104 | 4852 |
| 38 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +102 | 6708 |
| 39 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +97 | 48307 |
| 40 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +97 | 8534 |
| 41 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +95 | 13470 |
| 42 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +94 | 38606 |
| 43 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +93 | 18814 |
| 44 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +87 | 4938 |
| 45 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10467 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +85 | 41210 |
| 47 | [google-research/timesfm](https://github.com/google-research/timesfm) | +84 | 26999 |
| 48 | [browser-use/video-use](https://github.com/browser-use/video-use) | +82 | 17364 |
| 49 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6709 |
| 50 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +81 | 25950 |
| 51 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +77 | 10181 |
| 52 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6539 |
| 53 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +77 | 40890 |
| 54 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +75 | 16895 |
| 55 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +75 | 5838 |
| 56 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +75 | 6255 |
| 57 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +74 | 20121 |
| 58 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +74 | 27410 |
| 59 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +73 | 18658 |
| 60 | [EpicGames/lore](https://github.com/EpicGames/lore) | +73 | 8124 |
| 61 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 14143 |
| 62 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +70 | 11377 |
| 63 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +70 | 24125 |
| 64 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8404 |
| 65 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +66 | 9382 |
| 66 | [blader/humanizer](https://github.com/blader/humanizer) | +66 | 30041 |
| 67 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +66 | 10736 |
| 68 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +63 | 40450 |
| 69 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +62 | 13280 |
| 70 | [multica-ai/multica](https://github.com/multica-ai/multica) | +61 | 41211 |
| 71 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +61 | 47261 |
| 72 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +60 | 25992 |
| 73 | [antirez/ds4](https://github.com/antirez/ds4) | +60 | 18933 |
| 74 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2919 |
| 75 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +59 | 3553 |
| 76 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +57 | 6192 |
| 77 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +57 | 24097 |
| 78 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +56 | 11051 |
| 79 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +56 | 7547 |
| 80 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +55 | 28380 |
| 81 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27509 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +54 | 33111 |
| 83 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +54 | 6564 |
| 84 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +54 | 26681 |
| 85 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +53 | 3809 |
| 86 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +52 | 22877 |
| 87 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +52 | 23249 |
| 88 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +52 | 40064 |
| 89 | [decolua/9router](https://github.com/decolua/9router) | +51 | 22843 |
| 90 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +51 | 38850 |
| 91 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +51 | 31300 |
| 92 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5042 |
| 93 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +50 | 9697 |
| 94 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +50 | 35135 |
| 95 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +50 | 2809 |
| 96 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +49 | 8910 |
| 97 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +48 | 18727 |
| 98 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3717 |
| 99 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +47 | 26696 |
| 100 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +45 | 23637 |
| 101 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +44 | 4884 |
| 102 | [google-research/tabfm](https://github.com/google-research/tabfm) | +42 | 1948 |
| 103 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +41 | 33885 |
| 104 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +40 | 8313 |
| 105 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +39 | 25784 |
| 106 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2025 |
| 107 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +38 | 32390 |
| 108 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1416 |
| 109 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +37 | 5986 |
| 110 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +37 | 36103 |
| 111 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +36 | 43642 |
| 112 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +36 | 6211 |
| 113 | [anbeime/skill](https://github.com/anbeime/skill) | +36 | 3943 |
| 114 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +35 | 11886 |
| 115 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +35 | 25574 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +35 | 45659 |
| 117 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +34 | 9825 |
| 118 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +33 | 28763 |
| 119 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +32 | 6164 |
| 120 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2145 |
| 121 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +31 | 1312 |
| 122 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +31 | 22899 |
| 123 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2542 |
| 124 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +31 | 26998 |
| 125 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +30 | 17530 |
| 126 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +30 | 6897 |
| 127 | [openai/plugins](https://github.com/openai/plugins) | +30 | 4631 |
| 128 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1118 |
| 129 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +29 | 2034 |
| 130 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1150 |
| 131 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +28 | 6680 |
| 132 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +28 | 12581 |
| 133 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +27 | 1230 |
| 134 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15195 |
| 135 | [openai/skills](https://github.com/openai/skills) | +27 | 23981 |
| 136 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +27 | 3717 |
| 137 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2597 |
| 138 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +25 | 22954 |
| 139 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 16939 |
| 140 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +24 | 18003 |
| 141 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +24 | 3904 |
| 142 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +24 | 5606 |
| 143 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +24 | 2001 |
| 144 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 7408 |
| 145 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +23 | 4833 |
| 146 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +23 | 8786 |
| 147 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1775 |
| 148 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +23 | 1732 |
| 149 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +23 | 3498 |
| 150 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 2041 |
| 151 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +22 | 451 |
| 152 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +22 | 28344 |
| 153 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1667 |
| 154 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +22 | 33651 |
| 155 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +22 | 2008 |
| 156 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 4362 |
| 157 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +22 | 8604 |
| 158 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1359 |
| 159 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +21 | 4668 |
| 160 | [jundot/omlx](https://github.com/jundot/omlx) | +21 | 17984 |
| 161 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 673 |
| 162 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +21 | 5777 |
| 163 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +21 | 18615 |
| 164 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 165 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 3823 |
| 166 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +20 | 27016 |
| 167 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +20 | 16136 |
| 168 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 169 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +19 | 15161 |
| 170 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +19 | 8807 |
| 171 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +19 | 26578 |
| 172 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +19 | 3926 |
| 173 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1947 |
| 174 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7799 |
| 175 | [browser-act/skills](https://github.com/browser-act/skills) | +18 | 4553 |
| 176 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1965 |
| 177 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +17 | 16308 |
| 178 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +17 | 1837 |
| 179 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +17 | 8493 |
| 180 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 666 |
| 181 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +17 | 1335 |
| 182 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 428 |
| 183 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3167 |
| 184 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +16 | 7064 |
| 185 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +16 | 26632 |
| 186 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +15 | 10198 |
| 187 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +15 | 9096 |
| 188 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +15 | 3979 |
| 189 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 399 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +15 | 18374 |
| 191 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +15 | 4818 |
| 192 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +14 | 2296 |
| 193 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +14 | 4075 |
| 194 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +14 | 7867 |
| 195 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +14 | 677 |
| 196 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1013 |
| 197 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +13 | 29252 |
| 198 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +13 | 4377 |
| 199 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +13 | 2827 |
| 200 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +13 | 6393 |
| 201 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 202 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 540 |
| 203 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +12 | 2799 |
| 204 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +12 | 8538 |
| 205 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +12 | 5508 |
| 206 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +11 | 4517 |
| 207 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 695 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +11 | 11923 |
| 209 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +11 | 2916 |
| 210 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 702 |
| 211 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 212 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2921 |
| 213 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 861 |
| 214 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1077 |
| 215 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 430 |
| 216 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 367 |
| 217 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 658 |
| 218 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 462 |
| 219 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 147 |
| 220 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1209 |
| 221 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 9036 |
| 222 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2495 |
| 223 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 401 |
| 224 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +8 | 837 |
| 225 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 208 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +8 | 3242 |
| 227 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +8 | 4590 |
| 228 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 627 |
| 229 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 912 |
| 230 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6201 |
| 231 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1975 |
| 232 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1047 |
| 233 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 234 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +7 | 878 |
| 235 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +7 | 815 |
| 236 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 165 |
| 237 | [rpamis/comet](https://github.com/rpamis/comet) | +7 | 2379 |
| 238 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 365 |
| 239 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1792 |
| 240 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +7 | 1460 |
| 241 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 458 |
| 242 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 736 |
| 243 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 420 |
| 244 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1617 |
| 245 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 551 |
| 246 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +6 | 1898 |
| 247 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +6 | 4890 |
| 248 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +6 | 5024 |
| 249 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6018 |
| 250 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10029 |
| 251 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +6 | 2873 |
| 252 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 189 |
| 253 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5924 |
| 254 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 315 |
| 255 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 817 |
| 256 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 595 |
| 257 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 575 |
| 258 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 296 |
| 259 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +5 | 373 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2759 |
| 261 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3746 |
| 262 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 96 |
| 263 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +5 | 933 |
| 264 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +5 | 2786 |
| 265 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +4 | 1368 |
| 266 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 653 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2884 |
| 268 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 633 |
| 269 | [databufflabs/databuff](https://github.com/databufflabs/databuff) | +4 | 350 |
| 270 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 271 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9446 |
| 272 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 150 |
| 273 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2583 |
| 274 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1845 |
| 275 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 561 |
| 276 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 264 |
| 277 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 122 |
| 278 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 279 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 280 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 717 |
| 281 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +3 | 335 |
| 282 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +3 | 489 |
| 283 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 88 |
| 284 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 92 |
| 285 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 751 |
| 286 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 169 |
| 287 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 419 |
| 288 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 770 |
| 289 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2409 |
| 290 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 153 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 265 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 843 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1698 |
| 294 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 694 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3393 |
| 296 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 297 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 99 |
| 298 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +2 | 0 |
| 299 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 484 |
| 300 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +2 | 3166 |
