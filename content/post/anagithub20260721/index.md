---
title: "2026-07-21 GitHub增长趋势报告"
description: "1.OmniRoute+5 2.opencodex+3 3.Unlimited-OCR+3 4.ai-engineering-from-scratch+3 5.ui-skills+3"
date: 2026-07-21T21:11:31+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-21 21:11:31

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
        'daily': {"categories": ["amplitude/builder-skills", "ReconWorldLab/godot-gaussian-splatting", "x4gKing/X4G", "coreyhaines31/marketingskills", "1jehuang/jcode", "UditAkhourii/adhd", "MadsLorentzen/ai-job-search", "LanceZPF/agent-as-a-router", "JustVugg/colibri", "MoonshotAI/kimi-code", "Yu9191/wloc", "can1357/oh-my-pi", "Fei-Away/Codex-Dream-Skin", "HBAI-Ltd/Toonflow-app", "dnshe/DNSHE-FreeDomains", "ibelick/ui-skills", "rohitg00/ai-engineering-from-scratch", "baidu/Unlimited-OCR", "lidge-jun/opencodex", "diegosouzapw/OmniRoute"], "data": [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5]},
        'weekly': {"categories": ["rohitg00/ai-engineering-from-scratch", "PrismML-Eng/Bonsai-demo", "tt-a1i/archify", "HenryNdubuaku/maths-cs-ai-compendium", "MoonshotAI/kimi-cli", "k1tbyte/Wand-Enhancer", "usestrix/strix", "oso95/scroll-world", "hasaneyldrm/exercises-dataset", "ibelick/ui-skills", "iOfficeAI/OfficeCLI", "jamiepine/voicebox", "MadsLorentzen/ai-job-search", "diegosouzapw/OmniRoute", "ogulcancelik/herdr", "stablyai/orca", "emilkowalski/skills", "HKUDS/Vibe-Trading", "JustVugg/colibri", "Fei-Away/Codex-Dream-Skin"], "data": [13, 14, 14, 14, 14, 14, 15, 16, 16, 16, 18, 19, 22, 23, 25, 26, 32, 33, 34, 58]},
        'monthly': {"categories": ["simplex-chat/simplex-chat", "alibaba/page-agent", "mukul975/Anthropic-Cybersecurity-Skills", "palmier-io/palmier-pro", "hugohe3/ppt-master", "apple/container", "ogulcancelik/herdr", "topoteretes/cognee", "jamiepine/voicebox", "XxHuberrr/Mineradio", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "langchain-ai/openwiki", "xbtlin/ai-berkshire", "google-labs-code/design.md", "baidu/Unlimited-OCR", "ZhuLinsen/daily_stock_analysis", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [144, 145, 147, 159, 165, 166, 172, 175, 179, 182, 183, 187, 188, 201, 228, 230, 247, 252, 387, 565]}
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
| 1 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +5 | 23383 |
| 2 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +3 | 2221 |
| 3 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 16405 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 41421 |
| 5 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +3 | 5815 |
| 6 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 6850 |
| 7 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +2 | 11856 |
| 8 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +2 | 11494 |
| 9 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +2 | 18949 |
| 10 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +2 | 5940 |
| 11 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +2 | 4386 |
| 12 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 17494 |
| 13 | [LanceZPF/agent-as-a-router](https://github.com/LanceZPF/agent-as-a-router) | +2 | 817 |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2 | 24845 |
| 15 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +2 | 1575 |
| 16 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 10254 |
| 17 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1 | 41057 |
| 18 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +1 | 6203 |
| 19 | [ReconWorldLab/godot-gaussian-splatting](https://github.com/ReconWorldLab/godot-gaussian-splatting) | +1 | 248 |
| 20 | [amplitude/builder-skills](https://github.com/amplitude/builder-skills) | +1 | 132 |
| 21 | [cdredfox/workbuddy-skin-studio](https://github.com/cdredfox/workbuddy-skin-studio) | +1 | 56 |
| 22 | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | +1 | 1911 |
| 23 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +1 | 6749 |
| 24 | [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) | +1 | 1804 |
| 25 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +1 | 1837 |
| 26 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +1 | 1020 |
| 27 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +1 | 2173 |
| 28 | [openai/symphony](https://github.com/openai/symphony) | +1 | 26112 |
| 29 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +1 | 13948 |
| 30 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1 | 32168 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +58 | 11494 |
| 2 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +34 | 17494 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 26094 |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +32 | 19387 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +26 | 24808 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 19121 |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +23 | 23383 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +22 | 24845 |
| 9 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +19 | 45116 |
| 10 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 20590 |
| 11 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +16 | 5815 |
| 12 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +16 | 16426 |
| 13 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +16 | 4679 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | +15 | 43164 |
| 15 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +14 | 10490 |
| 16 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +14 | 10487 |
| 17 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +14 | 7050 |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +14 | 6668 |
| 19 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +14 | 1922 |
| 20 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +13 | 41421 |
| 21 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +13 | 28819 |
| 22 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +12 | 6203 |
| 23 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +12 | 14683 |
| 24 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 40837 |
| 25 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +11 | 9530 |
| 26 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +11 | 12764 |
| 27 | [deer-flow/llm-space](https://github.com/deer-flow/llm-space) | +11 | 1155 |
| 28 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +11 | 5270 |
| 29 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +10 | 24464 |
| 30 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +10 | 4185 |
| 31 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +10 | 2027 |
| 32 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +10 | 2422 |
| 33 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +10 | 33624 |
| 34 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1167 |
| 35 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +10 | 41560 |
| 36 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +10 | 23780 |
| 37 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 40343 |
| 38 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +9 | 10255 |
| 39 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4857 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +9 | 5940 |
| 41 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 6850 |
| 42 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1279 |
| 43 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +9 | 48518 |
| 44 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +9 | 3825 |
| 45 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +9 | 7773 |
| 46 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +9 | 1333 |
| 47 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +9 | 1172 |
| 48 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +9 | 1989 |
| 49 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +8 | 1526 |
| 50 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 41057 |
| 51 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +8 | 18949 |
| 52 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +8 | 7537 |
| 53 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +8 | 36614 |
| 54 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +8 | 906 |
| 55 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +8 | 26115 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +8 | 33342 |
| 57 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +7 | 4386 |
| 58 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +7 | 1978 |
| 59 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +7 | 13677 |
| 60 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 30253 |
| 61 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +7 | 734 |
| 62 | [malisper/pgrust](https://github.com/malisper/pgrust) | +7 | 3666 |
| 63 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 41407 |
| 64 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +6 | 27405 |
| 65 | [stupside/castor](https://github.com/stupside/castor) | +6 | 1695 |
| 66 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6043 |
| 67 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 10998 |
| 68 | [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | +6 | 13989 |
| 69 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +6 | 7531 |
| 70 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +6 | 27488 |
| 71 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +6 | 30592 |
| 72 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +6 | 13605 |
| 73 | [MatinSenPai/Aether-GUI](https://github.com/MatinSenPai/Aether-GUI) | +6 | 703 |
| 74 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +6 | 8946 |
| 75 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +6 | 760 |
| 76 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +6 | 3057 |
| 77 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 8695 |
| 78 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +6 | 18796 |
| 79 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +6 | 28607 |
| 80 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 58150 |
| 81 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +5 | 23288 |
| 82 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +5 | 9168 |
| 83 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +5 | 1658 |
| 84 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +5 | 26288 |
| 85 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +5 | 13948 |
| 86 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +5 | 456 |
| 87 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +5 | 6105 |
| 88 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +5 | 16405 |
| 89 | [yorgai/ORG2](https://github.com/yorgai/ORG2) | +5 | 2235 |
| 90 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +5 | 970 |
| 91 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +5 | 4967 |
| 92 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +5 | 11973 |
| 93 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 4235 |
| 94 | [NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt) | +5 | 548 |
| 95 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 29438 |
| 96 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 2221 |
| 97 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +4 | 1467 |
| 98 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +4 | 1414 |
| 99 | [Orkas-AI/Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) | +4 | 353 |
| 100 | [tw93/Waza](https://github.com/tw93/Waza) | +4 | 6576 |
| 101 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 4983 |
| 102 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 143 |
| 103 | [apache/ossie](https://github.com/apache/ossie) | +4 | 1453 |
| 104 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +4 | 28835 |
| 105 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +4 | 7580 |
| 106 | [Cjbuilds/Codex-Orchestration](https://github.com/Cjbuilds/Codex-Orchestration) | +4 | 505 |
| 107 | [lynote-ai/ai-image-detector](https://github.com/lynote-ai/ai-image-detector) | +4 | 302 |
| 108 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +4 | 6471 |
| 109 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +4 | 6336 |
| 110 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +4 | 11404 |
| 111 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +4 | 15196 |
| 112 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 17456 |
| 113 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +4 | 1186 |
| 114 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +4 | 8824 |
| 115 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +4 | 7828 |
| 116 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +3 | 4910 |
| 117 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2430 |
| 118 | [google-research/tabfm](https://github.com/google-research/tabfm) | +3 | 1992 |
| 119 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +3 | 1265 |
| 120 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +3 | 11740 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +565 | 40837 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +387 | 33624 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +252 | 43164 |
| 4 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +247 | 58150 |
| 5 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +230 | 16405 |
| 6 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +228 | 26199 |
| 7 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +201 | 13605 |
| 8 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 12764 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +187 | 24808 |
| 10 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +183 | 29438 |
| 11 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8695 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +179 | 45116 |
| 13 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +175 | 29009 |
| 14 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +172 | 19121 |
| 15 | [apple/container](https://github.com/apple/container) | +166 | 48107 |
| 16 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +165 | 40343 |
| 17 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +159 | 10890 |
| 18 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +147 | 26288 |
| 19 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +145 | 27405 |
| 20 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18855 |
| 21 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +143 | 24845 |
| 22 | [facebook/astryx](https://github.com/facebook/astryx) | +142 | 9994 |
| 23 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +142 | 25935 |
| 24 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +138 | 26094 |
| 25 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +134 | 8946 |
| 26 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +132 | 29548 |
| 27 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +125 | 23383 |
| 28 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5434 |
| 29 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +119 | 16426 |
| 30 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3985 |
| 31 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +105 | 30253 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +101 | 16589 |
| 33 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +100 | 6794 |
| 34 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +97 | 36614 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +91 | 48518 |
| 36 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +89 | 19387 |
| 37 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +89 | 8702 |
| 38 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +89 | 7014 |
| 39 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +87 | 4983 |
| 40 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10508 |
| 41 | [browser-use/video-use](https://github.com/browser-use/video-use) | +81 | 17456 |
| 42 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6723 |
| 43 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +78 | 38802 |
| 44 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +78 | 13507 |
| 45 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +77 | 10490 |
| 46 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +77 | 17494 |
| 47 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6582 |
| 48 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +77 | 5940 |
| 49 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +75 | 6336 |
| 50 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +74 | 26115 |
| 51 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 14683 |
| 52 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +69 | 41560 |
| 53 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +69 | 27488 |
| 54 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +68 | 20590 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +68 | 41057 |
| 56 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8490 |
| 57 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +65 | 9530 |
| 58 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +65 | 18949 |
| 59 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +64 | 24215 |
| 60 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +63 | 11404 |
| 61 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +63 | 4899 |
| 62 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +60 | 41421 |
| 63 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2923 |
| 64 | [EpicGames/lore](https://github.com/EpicGames/lore) | +60 | 8141 |
| 65 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +59 | 47326 |
| 66 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +59 | 3605 |
| 67 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +58 | 11494 |
| 68 | [multica-ai/multica](https://github.com/multica-ai/multica) | +58 | 41407 |
| 69 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +57 | 6668 |
| 70 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +57 | 13901 |
| 71 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +57 | 26084 |
| 72 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27529 |
| 73 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +54 | 10810 |
| 74 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +53 | 6850 |
| 75 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +53 | 28462 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +53 | 30197 |
| 77 | [antirez/ds4](https://github.com/antirez/ds4) | +51 | 19011 |
| 78 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5067 |
| 79 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +50 | 33342 |
| 80 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +49 | 23301 |
| 81 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +49 | 3817 |
| 82 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3737 |
| 83 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +48 | 7580 |
| 84 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +48 | 24161 |
| 85 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +48 | 26762 |
| 86 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +48 | 9752 |
| 87 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +47 | 22939 |
| 88 | [decolua/9router](https://github.com/decolua/9router) | +46 | 22965 |
| 89 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +46 | 21762 |
| 90 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +46 | 3834 |
| 91 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +45 | 40174 |
| 92 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +45 | 35173 |
| 93 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +44 | 18796 |
| 94 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +44 | 26836 |
| 95 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9791 |
| 96 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 1992 |
| 97 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +41 | 4967 |
| 98 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +41 | 9235 |
| 99 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +41 | 31386 |
| 100 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +39 | 10577 |
| 101 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2027 |
| 102 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +38 | 6203 |
| 103 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +38 | 33952 |
| 104 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +38 | 23780 |
| 105 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +37 | 8343 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +36 | 32433 |
| 107 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +36 | 2820 |
| 108 | [anbeime/skill](https://github.com/anbeime/skill) | +35 | 3983 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +34 | 6225 |
| 110 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +33 | 25830 |
| 111 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +33 | 11973 |
| 112 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +32 | 43679 |
| 113 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +32 | 28836 |
| 114 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +32 | 25600 |
| 115 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +32 | 2160 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +31 | 45699 |
| 117 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2559 |
| 118 | [openai/plugins](https://github.com/openai/plugins) | +29 | 4652 |
| 119 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +29 | 27037 |
| 120 | [openai/skills](https://github.com/openai/skills) | +28 | 24023 |
| 121 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +28 | 1125 |
| 122 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +27 | 1265 |
| 123 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15204 |
| 124 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +27 | 17661 |
| 125 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +27 | 6965 |
| 126 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +26 | 6254 |
| 127 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +26 | 6749 |
| 128 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +26 | 1321 |
| 129 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +26 | 1153 |
| 130 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +25 | 24464 |
| 131 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +25 | 2043 |
| 132 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 16962 |
| 133 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +24 | 9876 |
| 134 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +23 | 4910 |
| 135 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1806 |
| 136 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +23 | 1752 |
| 137 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +23 | 12628 |
| 138 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +22 | 28819 |
| 139 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +22 | 18044 |
| 140 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1668 |
| 141 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +22 | 22930 |
| 142 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +22 | 2033 |
| 143 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 4679 |
| 144 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +22 | 7537 |
| 145 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +22 | 2064 |
| 146 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +22 | 2608 |
| 147 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1380 |
| 148 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 673 |
| 149 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +21 | 3961 |
| 150 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +21 | 5631 |
| 151 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 152 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +21 | 9038 |
| 153 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +20 | 27052 |
| 154 | [jundot/omlx](https://github.com/jundot/omlx) | +20 | 18014 |
| 155 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +20 | 4715 |
| 156 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +20 | 3529 |
| 157 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 158 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +20 | 3727 |
| 159 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +19 | 8824 |
| 160 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 3848 |
| 161 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +19 | 33676 |
| 162 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +19 | 5805 |
| 163 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +19 | 18655 |
| 164 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +19 | 2027 |
| 165 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +19 | 3982 |
| 166 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1950 |
| 167 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7828 |
| 168 | [browser-act/skills](https://github.com/browser-act/skills) | +18 | 4593 |
| 169 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1413 |
| 170 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1977 |
| 171 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +17 | 1841 |
| 172 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +17 | 16157 |
| 173 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1725 |
| 174 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 669 |
| 175 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10487 |
| 176 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +16 | 16365 |
| 177 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 437 |
| 178 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +16 | 15196 |
| 179 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3182 |
| 180 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | +16 | 2620 |
| 181 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +16 | 4857 |
| 182 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +15 | 9168 |
| 183 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +15 | 2555 |
| 184 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +15 | 26621 |
| 185 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +15 | 4185 |
| 186 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +15 | 8562 |
| 187 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 399 |
| 188 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +14 | 2422 |
| 189 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +14 | 4235 |
| 190 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +14 | 7901 |
| 191 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +14 | 7100 |
| 192 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +14 | 680 |
| 193 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1016 |
| 194 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +13 | 18407 |
| 195 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +13 | 4424 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +13 | 26670 |
| 197 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +13 | 1349 |
| 198 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 199 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 553 |
| 200 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +12 | 29283 |
| 201 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +12 | 6422 |
| 202 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 708 |
| 203 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +11 | 11943 |
| 204 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +11 | 2858 |
| 205 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +11 | 8558 |
| 206 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 702 |
| 207 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 208 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +10 | 452 |
| 209 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 867 |
| 210 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1079 |
| 211 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +10 | 5540 |
| 212 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 431 |
| 213 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 368 |
| 214 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 669 |
| 215 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 147 |
| 216 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +10 | 2930 |
| 217 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1279 |
| 218 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 4793 |
| 219 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +9 | 2847 |
| 220 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 9055 |
| 221 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +9 | 2927 |
| 222 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2523 |
| 223 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +8 | 6213 |
| 224 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 403 |
| 225 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +8 | 462 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +8 | 3267 |
| 227 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 635 |
| 228 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 926 |
| 229 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1982 |
| 230 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1050 |
| 231 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 232 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +7 | 819 |
| 233 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 166 |
| 234 | [rpamis/comet](https://github.com/rpamis/comet) | +7 | 2395 |
| 235 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 366 |
| 236 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +7 | 4625 |
| 237 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 458 |
| 238 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 839 |
| 239 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 434 |
| 240 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +6 | 893 |
| 241 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 556 |
| 242 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +6 | 1902 |
| 243 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +6 | 5029 |
| 244 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +6 | 848 |
| 245 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +6 | 698 |
| 246 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6043 |
| 247 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10040 |
| 248 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 190 |
| 249 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5937 |
| 250 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 317 |
| 251 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 582 |
| 252 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 599 |
| 253 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1626 |
| 254 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 301 |
| 255 | [pshenok/server-survival](https://github.com/pshenok/server-survival) | +5 | 6219 |
| 256 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +5 | 2776 |
| 257 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 2883 |
| 258 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 700 |
| 259 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +4 | 855 |
| 260 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 509 |
| 261 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 640 |
| 262 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 376 |
| 263 | [kimsh-1/gongnyang-prompt-kit](https://github.com/kimsh-1/gongnyang-prompt-kit) | +4 | 282 |
| 264 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2889 |
| 265 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 648 |
| 266 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +4 | 3754 |
| 267 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +4 | 97 |
| 268 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +4 | 944 |
| 269 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +4 | 2793 |
| 270 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +3 | 1374 |
| 271 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 272 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 138 |
| 273 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9478 |
| 274 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 151 |
| 275 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2586 |
| 276 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1847 |
| 277 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 560 |
| 278 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 264 |
| 279 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 125 |
| 280 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 281 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 282 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +3 | 339 |
| 283 | [databufflabs/databuff](https://github.com/databufflabs/databuff) | +3 | 365 |
| 284 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 88 |
| 285 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 94 |
| 286 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 170 |
| 287 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 751 |
| 288 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 420 |
| 289 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 776 |
| 290 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 160 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 266 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 843 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1699 |
| 294 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 698 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2416 |
| 296 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 726 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 100 |
| 299 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +2 | 0 |
| 300 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 490 |
