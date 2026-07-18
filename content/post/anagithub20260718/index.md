---
title: "2026-07-18 GitHub增长趋势报告"
description: "1.Codex-Dream-Skin+6 2.skills+5 3.herdr+4 4.maths-cs-ai-compendium+4 5.OfficeCLI+3"
date: 2026-07-18T20:50:55+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-18 20:50:55

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
        'daily': {"categories": ["jnMetaCode/agency-agents-zh", "mekos2772/ios-location-spoofer", "BigPizzaV3/CodexPlusPlus", "OpenSenseNova/SenseNova-U1", "PrismML-Eng/Bonsai-demo", "MadsLorentzen/ai-job-search", "CoreBunch/Instatic", "RyanCodrai/turbovec", "dnshe/DNSHE-FreeDomains", "rohitg00/ai-engineering-from-scratch", "1jehuang/jcode", "JustVugg/colibri", "stablyai/orca", "diegosouzapw/OmniRoute", "anthropics/cwc-workshops", "iOfficeAI/OfficeCLI", "HenryNdubuaku/maths-cs-ai-compendium", "ogulcancelik/herdr", "emilkowalski/skills", "Fei-Away/Codex-Dream-Skin"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6]},
        'weekly': {"categories": ["HenryNdubuaku/maths-cs-ai-compendium", "sharpemu/sharpemu", "Alishahryar1/free-claude-code", "calesthio/OpenMontage", "x4gKing/X4G", "jamiepine/voicebox", "tt-a1i/archify", "PrismML-Eng/Bonsai-demo", "Dicklesworthstone/destructive_command_guard", "hasaneyldrm/exercises-dataset", "MadsLorentzen/ai-job-search", "iOfficeAI/OfficeCLI", "ogulcancelik/herdr", "k1tbyte/Wand-Enhancer", "oso95/scroll-world", "stablyai/orca", "emilkowalski/skills", "HKUDS/Vibe-Trading", "Fei-Away/Codex-Dream-Skin", "JustVugg/colibri"], "data": [12, 13, 13, 13, 13, 14, 14, 14, 15, 16, 19, 20, 20, 20, 22, 23, 30, 33, 44, 61]},
        'monthly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "ogulcancelik/herdr", "XxHuberrr/Mineradio", "hugohe3/ppt-master", "langchain-ai/openwiki", "topoteretes/cognee", "apple/container", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "xbtlin/ai-berkshire", "jamiepine/voicebox", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "ZhuLinsen/daily_stock_analysis", "palmier-io/palmier-pro", "DeusData/codebase-memory-mcp", "headroomlabs-ai/headroom", "calesthio/OpenMontage", "DietrichGebert/ponytail"], "data": [173, 176, 181, 183, 183, 184, 184, 188, 191, 200, 201, 227, 231, 247, 283, 287, 482, 587, 615, 943]}
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
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +6 | 9716 |
| 2 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +5 | 17438 |
| 3 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +4 | 17958 |
| 4 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +4 | 6872 |
| 5 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +3 | 19253 |
| 6 | [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) | +3 | 1694 |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 18728 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 21738 |
| 9 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 16063 |
| 10 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 8521 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2 | 39048 |
| 12 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 6280 |
| 13 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +2 | 13488 |
| 14 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +2 | 3487 |
| 15 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2 | 23682 |
| 16 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +2 | 1796 |
| 17 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +2 | 3976 |
| 18 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +2 | 25692 |
| 19 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +2 | 2477 |
| 20 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +2 | 17609 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1 | 42694 |
| 22 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +1 | 1033 |
| 23 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +1 | 4780 |
| 24 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1 | 57770 |
| 25 | [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding) | +1 | 2915 |
| 26 | [Tencent-Hunyuan/HunyuanOCR](https://github.com/Tencent-Hunyuan/HunyuanOCR) | +1 | 1848 |
| 27 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +1 | 2548 |
| 28 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +1 | 710 |
| 29 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | +1 | 7653 |
| 30 | [browser-use/video-use](https://github.com/browser-use/video-use) | +1 | 17108 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +61 | 16063 |
| 2 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +44 | 9716 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 24946 |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +30 | 17438 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +23 | 21738 |
| 6 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 3570 |
| 7 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +20 | 9326 |
| 8 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +20 | 17958 |
| 9 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +20 | 19253 |
| 10 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 23682 |
| 11 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +16 | 15772 |
| 12 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +15 | 5109 |
| 13 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +14 | 1796 |
| 14 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +14 | 5820 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +14 | 42694 |
| 16 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +13 | 5742 |
| 17 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +13 | 39784 |
| 18 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +13 | 40752 |
| 19 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +13 | 3412 |
| 20 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +12 | 6872 |
| 21 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +12 | 18729 |
| 22 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +12 | 2029 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 39806 |
| 24 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +12 | 6280 |
| 25 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +12 | 32679 |
| 26 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +11 | 23330 |
| 27 | [usestrix/strix](https://github.com/usestrix/strix) | +10 | 42430 |
| 28 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 27634 |
| 29 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1172 |
| 30 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +10 | 9103 |
| 31 | [malisper/pgrust](https://github.com/malisper/pgrust) | +10 | 3479 |
| 32 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 36101 |
| 33 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +9 | 32843 |
| 34 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +9 | 18610 |
| 35 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +8 | 1287 |
| 36 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +8 | 1905 |
| 37 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 40981 |
| 38 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +8 | 25692 |
| 39 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +8 | 47886 |
| 40 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +8 | 12280 |
| 41 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +8 | 7538 |
| 42 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +8 | 4596 |
| 43 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +8 | 2660 |
| 44 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +8 | 14848 |
| 45 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +7 | 1860 |
| 46 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +7 | 8459 |
| 47 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 5554 |
| 48 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 13331 |
| 49 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +7 | 957 |
| 50 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 2919 |
| 51 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 7249 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 57770 |
| 53 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 40574 |
| 54 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 39048 |
| 55 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +6 | 1033 |
| 56 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +6 | 13488 |
| 57 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +6 | 7126 |
| 58 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +6 | 4693 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +6 | 33665 |
| 60 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +6 | 1543 |
| 61 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +6 | 10437 |
| 62 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +6 | 2434 |
| 63 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +6 | 6265 |
| 64 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +6 | 1082 |
| 65 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 29560 |
| 66 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +5 | 496 |
| 67 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +5 | 11471 |
| 68 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +5 | 5514 |
| 69 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 3652 |
| 70 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 8556 |
| 71 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +5 | 524 |
| 72 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +5 | 807 |
| 73 | [threerocks/hand-drawn-styles](https://github.com/threerocks/hand-drawn-styles) | +5 | 437 |
| 74 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 18343 |
| 75 | [MengTo/Skills](https://github.com/MengTo/Skills) | +5 | 2380 |
| 76 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +5 | 25702 |
| 77 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +5 | 28373 |
| 78 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4424 |
| 79 | [littledivy/mimic](https://github.com/littledivy/mimic) | +5 | 1165 |
| 80 | [decolua/9router](https://github.com/decolua/9router) | +5 | 22588 |
| 81 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +5 | 27027 |
| 82 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 38354 |
| 83 | [x4gKing/Marzban-Panel](https://github.com/x4gKing/Marzban-Panel) | +4 | 863 |
| 84 | [x4gKing/Marzban-Node](https://github.com/x4gKing/Marzban-Node) | +4 | 743 |
| 85 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +4 | 12805 |
| 86 | [hicccc77/WeFlow](https://github.com/hicccc77/WeFlow) | +4 | 13033 |
| 87 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +4 | 7462 |
| 88 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +4 | 27257 |
| 89 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +4 | 43541 |
| 90 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +4 | 28584 |
| 91 | [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) | +4 | 1694 |
| 92 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +4 | 28650 |
| 93 | [Chunyu33/light-c](https://github.com/Chunyu33/light-c) | +4 | 913 |
| 94 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +4 | 7723 |
| 95 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4 | 16350 |
| 96 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +4 | 4930 |
| 97 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +4 | 26537 |
| 98 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +4 | 6088 |
| 99 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 31141 |
| 100 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 8758 |
| 101 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +4 | 14898 |
| 102 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +4 | 1430 |
| 103 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +4 | 1323 |
| 104 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1314 |
| 105 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +3 | 5046 |
| 106 | [apache/ossie](https://github.com/apache/ossie) | +3 | 1248 |
| 107 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +3 | 8612 |
| 108 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +3 | 9583 |
| 109 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +3 | 269 |
| 110 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +3 | 710 |
| 111 | [simonlin1212/TradingAgents-astock](https://github.com/simonlin1212/TradingAgents-astock) | +3 | 2477 |
| 112 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 17108 |
| 113 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +3 | 26435 |
| 114 | [RICHQAQ/PasteMD](https://github.com/RICHQAQ/PasteMD) | +3 | 5148 |
| 115 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +3 | 1603 |
| 116 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11257 |
| 117 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4668 |
| 118 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +3 | 244 |
| 119 | [bytedance/Bernini](https://github.com/bytedance/Bernini) | +3 | 1135 |
| 120 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 11728 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +943 | 85551 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +615 | 39784 |
| 3 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +587 | 59827 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +482 | 32679 |
| 5 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +287 | 10765 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +283 | 57770 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | +247 | 42430 |
| 8 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +231 | 26050 |
| 9 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 14419 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +201 | 42694 |
| 11 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +200 | 13331 |
| 12 | [stablyai/orca](https://github.com/stablyai/orca) | +191 | 21738 |
| 13 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +188 | 28650 |
| 14 | [apple/container](https://github.com/apple/container) | +184 | 47987 |
| 15 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +184 | 28160 |
| 16 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +183 | 12280 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +183 | 39806 |
| 18 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +181 | 8556 |
| 19 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +176 | 17958 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +173 | 25818 |
| 21 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +152 | 6760 |
| 22 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +146 | 18728 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +143 | 24946 |
| 24 | [facebook/astryx](https://github.com/facebook/astryx) | +142 | 9136 |
| 25 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +142 | 27027 |
| 26 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +141 | 8459 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +137 | 23682 |
| 28 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +136 | 25432 |
| 29 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +133 | 29225 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +127 | 29560 |
| 31 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5332 |
| 32 | [EpicGames/lore](https://github.com/EpicGames/lore) | +125 | 8079 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +123 | 16350 |
| 34 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +117 | 18729 |
| 35 | [google-research/timesfm](https://github.com/google-research/timesfm) | +116 | 26954 |
| 36 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +115 | 15772 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +115 | 36101 |
| 38 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 39 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3964 |
| 40 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +107 | 13389 |
| 41 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +104 | 4791 |
| 42 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +102 | 6498 |
| 43 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +100 | 47887 |
| 44 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +100 | 8397 |
| 45 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +95 | 40752 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +95 | 38354 |
| 47 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +89 | 17438 |
| 48 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +89 | 25692 |
| 49 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +86 | 10387 |
| 50 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +86 | 45724 |
| 51 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 17108 |
| 52 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4430 |
| 53 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6689 |
| 54 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +80 | 40574 |
| 55 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6460 |
| 56 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +77 | 27257 |
| 57 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +75 | 9326 |
| 58 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +75 | 18343 |
| 59 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +74 | 19253 |
| 60 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +74 | 6088 |
| 61 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +74 | 11257 |
| 62 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +73 | 5554 |
| 63 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +73 | 39048 |
| 64 | [blader/humanizer](https://github.com/blader/humanizer) | +73 | 29783 |
| 65 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +72 | 16063 |
| 66 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +69 | 23970 |
| 67 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +69 | 10685 |
| 68 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +69 | 23945 |
| 69 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8284 |
| 70 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +67 | 13080 |
| 71 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +66 | 12806 |
| 72 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +66 | 3785 |
| 73 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +65 | 47147 |
| 74 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +64 | 9103 |
| 75 | [multica-ai/multica](https://github.com/multica-ai/multica) | +63 | 40981 |
| 76 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +63 | 7462 |
| 77 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +63 | 25872 |
| 78 | [antirez/ds4](https://github.com/antirez/ds4) | +62 | 18790 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +61 | 28232 |
| 80 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +61 | 6280 |
| 81 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2900 |
| 82 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +60 | 7391 |
| 83 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +59 | 3487 |
| 84 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +59 | 26545 |
| 85 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +59 | 8758 |
| 86 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2758 |
| 87 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +56 | 5820 |
| 88 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +56 | 23330 |
| 89 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27448 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +54 | 32843 |
| 91 | [decolua/9router](https://github.com/decolua/9router) | +54 | 22588 |
| 92 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +54 | 39964 |
| 93 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +53 | 26537 |
| 94 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +53 | 23184 |
| 95 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +52 | 9583 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +52 | 31141 |
| 97 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +51 | 22759 |
| 98 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 4938 |
| 99 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +50 | 18610 |
| 100 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3676 |
| 101 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +46 | 4693 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +45 | 33665 |
| 103 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +45 | 3685 |
| 104 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +44 | 9716 |
| 105 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 25702 |
| 106 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +42 | 28584 |
| 107 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +42 | 8265 |
| 108 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1832 |
| 109 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +40 | 32298 |
| 110 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2026 |
| 111 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +38 | 6182 |
| 112 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1387 |
| 113 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +38 | 13696 |
| 114 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +37 | 43541 |
| 115 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +37 | 45556 |
| 116 | [anbeime/skill](https://github.com/anbeime/skill) | +37 | 3873 |
| 117 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +37 | 36103 |
| 118 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +37 | 27451 |
| 119 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +36 | 9743 |
| 120 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +35 | 11728 |
| 121 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +35 | 25466 |
| 122 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +35 | 22844 |
| 123 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +34 | 5742 |
| 124 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +33 | 5968 |
| 125 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2106 |
| 126 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +32 | 17261 |
| 127 | [openai/plugins](https://github.com/openai/plugins) | +32 | 4597 |
| 128 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +32 | 26905 |
| 129 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2118 |
| 130 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +31 | 1308 |
| 131 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2477 |
| 132 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +31 | 6807 |
| 133 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +30 | 12521 |
| 134 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1274 |
| 135 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +29 | 6557 |
| 136 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +29 | 2020 |
| 137 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1141 |
| 138 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +28 | 3107 |
| 139 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15172 |
| 140 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +27 | 3833 |
| 141 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2572 |
| 142 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +26 | 1155 |
| 143 | [openai/skills](https://github.com/openai/skills) | +26 | 23921 |
| 144 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +26 | 4676 |
| 145 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +25 | 4619 |
| 146 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +25 | 5558 |
| 147 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +24 | 5514 |
| 148 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +24 | 17931 |
| 149 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +24 | 18542 |
| 150 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1692 |
| 151 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +24 | 8273 |
| 152 | [floci-io/floci](https://github.com/floci-io/floci) | +24 | 16882 |
| 153 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 450 |
| 154 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +23 | 8612 |
| 155 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1730 |
| 156 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +23 | 33595 |
| 157 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +23 | 1657 |
| 158 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +23 | 3359 |
| 159 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +23 | 1860 |
| 160 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 1981 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +22 | 17935 |
| 162 | [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | +22 | 8309 |
| 163 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +22 | 7126 |
| 164 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1340 |
| 165 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +21 | 26435 |
| 166 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +21 | 8696 |
| 167 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +21 | 26922 |
| 168 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +21 | 16080 |
| 169 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 1960 |
| 170 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 1543 |
| 171 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +20 | 16229 |
| 172 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 173 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +20 | 857 |
| 174 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +20 | 5706 |
| 175 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +20 | 3570 |
| 176 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +20 | 1323 |
| 177 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +19 | 7723 |
| 178 | [browser-act/skills](https://github.com/browser-act/skills) | +19 | 4506 |
| 179 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 3727 |
| 180 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +18 | 27634 |
| 181 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +18 | 1824 |
| 182 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +18 | 1938 |
| 183 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1944 |
| 184 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +17 | 7011 |
| 185 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 662 |
| 186 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +17 | 2776 |
| 187 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +17 | 26563 |
| 188 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3124 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +16 | 8410 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +16 | 29194 |
| 191 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 398 |
| 192 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +15 | 4280 |
| 193 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +15 | 18307 |
| 194 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 670 |
| 195 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +14 | 7799 |
| 196 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +14 | 6368 |
| 197 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +14 | 5852 |
| 198 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 534 |
| 199 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1011 |
| 200 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +13 | 8499 |
| 201 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +13 | 5463 |
| 202 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 203 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 516 |
| 204 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +12 | 2029 |
| 205 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +12 | 2882 |
| 206 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +11 | 4455 |
| 207 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 685 |
| 208 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 698 |
| 209 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 822 |
| 210 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 352 |
| 211 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 852 |
| 212 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1051 |
| 213 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +10 | 11893 |
| 214 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 430 |
| 215 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 362 |
| 216 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 2726 |
| 217 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 640 |
| 218 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 459 |
| 219 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 205 |
| 220 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +10 | 1459 |
| 221 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +10 | 2902 |
| 222 | [rpamis/comet](https://github.com/rpamis/comet) | +9 | 2353 |
| 223 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +9 | 689 |
| 224 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +9 | 4549 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2447 |
| 226 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5775 |
| 227 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +8 | 8998 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 841 |
| 229 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 810 |
| 230 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 391 |
| 231 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 207 |
| 232 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +8 | 3215 |
| 233 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 4353 |
| 234 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 616 |
| 235 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +7 | 5901 |
| 236 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6161 |
| 237 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1968 |
| 238 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1037 |
| 239 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 240 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 165 |
| 241 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +7 | 1890 |
| 242 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 360 |
| 243 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +7 | 4857 |
| 244 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1771 |
| 245 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +7 | 5019 |
| 246 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +7 | 487 |
| 247 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 458 |
| 248 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +6 | 1033 |
| 249 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +6 | 3102 |
| 250 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 406 |
| 251 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1605 |
| 252 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 545 |
| 253 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 635 |
| 254 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +6 | 370 |
| 255 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 9874 |
| 256 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +6 | 2857 |
| 257 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 186 |
| 258 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2786 |
| 259 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +5 | 1355 |
| 260 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 308 |
| 261 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +5 | 524 |
| 262 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 585 |
| 263 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 555 |
| 264 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3731 |
| 265 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +5 | 911 |
| 266 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 96 |
| 267 | [databufflabs/databuff](https://github.com/databufflabs/databuff) | +5 | 327 |
| 268 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 615 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2740 |
| 270 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 332 |
| 271 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 162 |
| 272 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 145 |
| 273 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2578 |
| 274 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 2862 |
| 275 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 558 |
| 276 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 123 |
| 277 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 25 |
| 278 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 279 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 699 |
| 280 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1830 |
| 281 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 282 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +3 | 3162 |
| 283 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +3 | 254 |
| 284 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 741 |
| 285 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 89 |
| 286 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 165 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2388 |
| 288 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 417 |
| 289 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 780 |
| 290 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 149 |
| 291 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 192 |
| 292 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 259 |
| 293 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 838 |
| 294 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1693 |
| 295 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 683 |
| 296 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3393 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 98 |
| 299 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 462 |
| 300 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +2 | 849 |
