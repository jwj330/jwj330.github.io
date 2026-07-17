---
title: "2026-07-17 GitHub增长趋势报告"
description: "1.Codex-Dream-Skin+30 2.orca+11 3.nitrostack+10 4.skills+10 5.herdr+9"
date: 2026-07-17T20:57:28+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-17 20:57:28

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
        'daily': {"categories": ["steipete/CodexBar", "multica-ai/multica", "contatomegasign/finance-account-tool", "x4gKing/X4G", "PrismML-Eng/Bonsai-demo", "hasaneyldrm/exercises-dataset", "team-reflect/reflect-open", "diegosouzapw/OmniRoute", "microsoft/flint-chart", "FB208/OpenBidKit_Yibiao", "usestrix/strix", "tt-a1i/archify", "HKUDS/DeepTutor", "oso95/scroll-world", "HKUDS/Vibe-Trading", "ogulcancelik/herdr", "emilkowalski/skills", "nitrocloudofficial/nitrostack", "stablyai/orca", "Fei-Away/Codex-Dream-Skin"], "data": [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 9, 10, 10, 11, 30]},
        'weekly': {"categories": ["hugohe3/ppt-master", "MDX-Tom/gpt-5.6-instruct", "PrismML-Eng/Bonsai-demo", "Alishahryar1/free-claude-code", "jamiepine/voicebox", "sharpemu/sharpemu", "calesthio/OpenMontage", "tt-a1i/archify", "hasaneyldrm/exercises-dataset", "ogulcancelik/herdr", "x4gKing/X4G", "iOfficeAI/OfficeCLI", "Dicklesworthstone/destructive_command_guard", "oso95/scroll-world", "k1tbyte/Wand-Enhancer", "MadsLorentzen/ai-job-search", "stablyai/orca", "emilkowalski/skills", "HKUDS/Vibe-Trading", "Fei-Away/Codex-Dream-Skin"], "data": [12, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 18, 19, 20, 20, 24, 31, 33, 40]},
        'monthly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "ogulcancelik/herdr", "XxHuberrr/Mineradio", "langchain-ai/openwiki", "topoteretes/cognee", "apple/container", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "hugohe3/ppt-master", "xbtlin/ai-berkshire", "jamiepine/voicebox", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "ZhuLinsen/daily_stock_analysis", "palmier-io/palmier-pro", "DeusData/codebase-memory-mcp", "headroomlabs-ai/headroom", "calesthio/OpenMontage", "DietrichGebert/ponytail"], "data": [177, 177, 180, 182, 184, 187, 188, 191, 193, 199, 203, 227, 232, 247, 286, 295, 526, 621, 621, 1037]}
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
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +30 | 8631 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca) | +11 | 21084 |
| 3 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1172 |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +10 | 16185 |
| 5 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +9 | 17583 |
| 6 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +7 | 24594 |
| 7 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +7 | 3199 |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +6 | 27294 |
| 9 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +6 | 5647 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | +6 | 42236 |
| 11 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +5 | 1744 |
| 12 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +5 | 1854 |
| 13 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4 | 18353 |
| 14 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +4 | 1269 |
| 15 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 15403 |
| 16 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +4 | 1695 |
| 17 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 5810 |
| 18 | [contatomegasign/finance-account-tool](https://github.com/contatomegasign/finance-account-tool) | +3 | 131 |
| 19 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3 | 40916 |
| 20 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +3 | 18543 |
| 21 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 12125 |
| 22 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 39491 |
| 23 | [apache/ossie](https://github.com/apache/ossie) | +3 | 1149 |
| 24 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 8951 |
| 25 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3 | 42062 |
| 26 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +3 | 5504 |
| 27 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +3 | 3491 |
| 28 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +3 | 23147 |
| 29 | [malisper/pgrust](https://github.com/malisper/pgrust) | +3 | 3368 |
| 30 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +3 | 6898 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +40 | 8631 |
| 2 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 24594 |
| 3 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +31 | 16185 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +24 | 21084 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +20 | 23509 |
| 6 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +20 | 8817 |
| 7 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +19 | 3199 |
| 8 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +18 | 5078 |
| 9 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +17 | 18781 |
| 10 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +16 | 5810 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +16 | 17583 |
| 12 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +15 | 15403 |
| 13 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +15 | 5647 |
| 14 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +14 | 39491 |
| 15 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +14 | 3261 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +13 | 42062 |
| 17 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +13 | 40644 |
| 18 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +12 | 1695 |
| 19 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +12 | 1870 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 39679 |
| 21 | [malisper/pgrust](https://github.com/malisper/pgrust) | +12 | 3368 |
| 22 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +12 | 6238 |
| 23 | [usestrix/strix](https://github.com/usestrix/strix) | +11 | 42236 |
| 24 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +11 | 8951 |
| 25 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +11 | 32400 |
| 26 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 27294 |
| 27 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1172 |
| 28 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +10 | 18354 |
| 29 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +10 | 32729 |
| 30 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +10 | 12125 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 35937 |
| 32 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 23147 |
| 33 | [multica-ai/multica](https://github.com/multica-ai/multica) | +9 | 40916 |
| 34 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +8 | 1269 |
| 35 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +8 | 6559 |
| 36 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +8 | 1854 |
| 37 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +8 | 4573 |
| 38 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +8 | 2633 |
| 39 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +8 | 18543 |
| 40 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +8 | 7467 |
| 41 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +8 | 14800 |
| 42 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +7 | 1744 |
| 43 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 5388 |
| 44 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +7 | 47600 |
| 45 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 2847 |
| 46 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +7 | 33544 |
| 47 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +7 | 2239 |
| 48 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +7 | 26902 |
| 49 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 7160 |
| 50 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 57647 |
| 51 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 40386 |
| 52 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +6 | 8287 |
| 53 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +6 | 13284 |
| 54 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +6 | 750 |
| 55 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +6 | 3491 |
| 56 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +6 | 883 |
| 57 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +6 | 1508 |
| 58 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 28561 |
| 59 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +6 | 10386 |
| 60 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +6 | 367 |
| 61 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +6 | 6204 |
| 62 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +6 | 1046 |
| 63 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 2334 |
| 64 | [nasa/spacewasm](https://github.com/nasa/spacewasm) | +6 | 1298 |
| 65 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +5 | 11421 |
| 66 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +5 | 5504 |
| 67 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +5 | 6898 |
| 68 | [threerocks/hand-drawn-styles](https://github.com/threerocks/hand-drawn-styles) | +5 | 416 |
| 69 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +5 | 4623 |
| 70 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 18219 |
| 71 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4413 |
| 72 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 25583 |
| 73 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +5 | 25668 |
| 74 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +5 | 28293 |
| 75 | [littledivy/mimic](https://github.com/littledivy/mimic) | +5 | 1142 |
| 76 | [decolua/9router](https://github.com/decolua/9router) | +5 | 22470 |
| 77 | [shadcn/improve](https://github.com/shadcn/improve) | +5 | 8422 |
| 78 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 31081 |
| 79 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +5 | 8729 |
| 80 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 10745 |
| 81 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +5 | 25825 |
| 82 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +5 | 5996 |
| 83 | [x4gKing/Marzban-Node](https://github.com/x4gKing/Marzban-Node) | +4 | 770 |
| 84 | [x4gKing/Marzban-Panel](https://github.com/x4gKing/Marzban-Panel) | +4 | 908 |
| 85 | [hicccc77/WeFlow](https://github.com/hicccc77/WeFlow) | +4 | 12965 |
| 86 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 38767 |
| 87 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +4 | 29381 |
| 88 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +4 | 8498 |
| 89 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +4 | 13255 |
| 90 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +4 | 30325 |
| 91 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +4 | 9529 |
| 92 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4 | 16295 |
| 93 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +4 | 4618 |
| 94 | [injaneity/pi-computer-use](https://github.com/injaneity/pi-computer-use) | +4 | 1433 |
| 95 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +4 | 4889 |
| 96 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +4 | 29077 |
| 97 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +4 | 3067 |
| 98 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +4 | 13932 |
| 99 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +4 | 12041 |
| 100 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +4 | 14882 |
| 101 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +4 | 38242 |
| 102 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +4 | 1381 |
| 103 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +4 | 1299 |
| 104 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1307 |
| 105 | [apache/ossie](https://github.com/apache/ossie) | +3 | 1149 |
| 106 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +3 | 6393 |
| 107 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +3 | 8563 |
| 108 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 43493 |
| 109 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 28531 |
| 110 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +3 | 25699 |
| 111 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +3 | 7706 |
| 112 | [RICHQAQ/PasteMD](https://github.com/RICHQAQ/PasteMD) | +3 | 5148 |
| 113 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +3 | 7421 |
| 114 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11194 |
| 115 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +3 | 236 |
| 116 | [bytedance/Bernini](https://github.com/bytedance/Bernini) | +3 | 1128 |
| 117 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 11664 |
| 118 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +3 | 17211 |
| 119 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +3 | 1202 |
| 120 | [HiDream-ai/HiDream-O1-Image](https://github.com/HiDream-ai/HiDream-O1-Image) | +3 | 1479 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1037 | 85187 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +621 | 39491 |
| 3 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +621 | 59674 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +526 | 32400 |
| 5 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +295 | 10745 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +286 | 57647 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | +247 | 42236 |
| 8 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +232 | 26009 |
| 9 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 14392 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +203 | 42062 |
| 11 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +199 | 13284 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +193 | 39679 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +191 | 21084 |
| 14 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +188 | 28561 |
| 15 | [apple/container](https://github.com/apple/container) | +187 | 47951 |
| 16 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +184 | 27983 |
| 17 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +182 | 12125 |
| 18 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +180 | 8498 |
| 19 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +177 | 17583 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +177 | 25699 |
| 21 | [EpicGames/lore](https://github.com/EpicGames/lore) | +166 | 8068 |
| 22 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +152 | 6721 |
| 23 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +146 | 18665 |
| 24 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +144 | 24594 |
| 25 | [facebook/astryx](https://github.com/facebook/astryx) | +142 | 9102 |
| 26 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +142 | 26902 |
| 27 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +141 | 8287 |
| 28 | [google-research/timesfm](https://github.com/google-research/timesfm) | +138 | 26932 |
| 29 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +135 | 23509 |
| 30 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +135 | 25268 |
| 31 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +133 | 29077 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +130 | 29381 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +127 | 16295 |
| 34 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5304 |
| 35 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +123 | 35937 |
| 36 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +115 | 18354 |
| 37 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +115 | 13350 |
| 38 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +114 | 15403 |
| 39 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 40 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3957 |
| 41 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +107 | 26332 |
| 42 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +105 | 8368 |
| 43 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +104 | 47600 |
| 44 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +104 | 38242 |
| 45 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +104 | 4760 |
| 46 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +102 | 6393 |
| 47 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +99 | 40644 |
| 48 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +98 | 45699 |
| 49 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +94 | 25583 |
| 50 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +86 | 40386 |
| 51 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +86 | 10366 |
| 52 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +85 | 18219 |
| 53 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +84 | 16185 |
| 54 | [browser-use/video-use](https://github.com/browser-use/video-use) | +83 | 17052 |
| 55 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4386 |
| 56 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6686 |
| 57 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6409 |
| 58 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +77 | 38767 |
| 59 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +77 | 10662 |
| 60 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +75 | 11194 |
| 61 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +74 | 8818 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +74 | 29674 |
| 63 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +74 | 23852 |
| 64 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +73 | 5388 |
| 65 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +73 | 5996 |
| 66 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +73 | 7421 |
| 67 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +72 | 18781 |
| 68 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +72 | 13015 |
| 69 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +72 | 23918 |
| 70 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +69 | 12041 |
| 71 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +68 | 47100 |
| 72 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +68 | 3743 |
| 73 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8214 |
| 74 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +67 | 7353 |
| 75 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +65 | 25825 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +65 | 28172 |
| 77 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +64 | 8951 |
| 78 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +64 | 23147 |
| 79 | [multica-ai/multica](https://github.com/multica-ai/multica) | +63 | 40916 |
| 80 | [antirez/ds4](https://github.com/antirez/ds4) | +63 | 18736 |
| 81 | [alibaba/zvec](https://github.com/alibaba/zvec) | +63 | 15045 |
| 82 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +62 | 26467 |
| 83 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +62 | 8729 |
| 84 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2888 |
| 85 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +59 | 6238 |
| 86 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +58 | 26427 |
| 87 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +58 | 21605 |
| 88 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2744 |
| 89 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +57 | 3454 |
| 90 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +57 | 31081 |
| 91 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +56 | 5647 |
| 92 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +55 | 32729 |
| 93 | [decolua/9router](https://github.com/decolua/9router) | +55 | 22470 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +55 | 39929 |
| 95 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27413 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +54 | 9529 |
| 97 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +54 | 23140 |
| 98 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +51 | 22691 |
| 99 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +51 | 3675 |
| 100 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 4889 |
| 101 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +50 | 18543 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +50 | 33544 |
| 103 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +46 | 4623 |
| 104 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +45 | 25668 |
| 105 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +43 | 8255 |
| 106 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +41 | 28531 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +41 | 6157 |
| 108 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +41 | 32256 |
| 109 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +40 | 8631 |
| 110 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1822 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +40 | 45500 |
| 112 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +39 | 13684 |
| 113 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2025 |
| 114 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +39 | 27418 |
| 115 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1381 |
| 116 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +37 | 9718 |
| 117 | [anbeime/skill](https://github.com/anbeime/skill) | +37 | 3834 |
| 118 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +37 | 36103 |
| 119 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +36 | 43493 |
| 120 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +36 | 11664 |
| 121 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +36 | 33564 |
| 122 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +36 | 22823 |
| 123 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +35 | 5890 |
| 124 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +35 | 25456 |
| 125 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +35 | 17211 |
| 126 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +34 | 5810 |
| 127 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +34 | 2104 |
| 128 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +34 | 26833 |
| 129 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +32 | 6775 |
| 130 | [openai/plugins](https://github.com/openai/plugins) | +32 | 4583 |
| 131 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +32 | 12492 |
| 132 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2111 |
| 133 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +31 | 1305 |
| 134 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +31 | 3100 |
| 135 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +30 | 1293 |
| 136 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +30 | 6494 |
| 137 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +29 | 4596 |
| 138 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +29 | 2010 |
| 139 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1133 |
| 140 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +29 | 2430 |
| 141 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +28 | 3806 |
| 142 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15163 |
| 143 | [openai/skills](https://github.com/openai/skills) | +27 | 23879 |
| 144 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2558 |
| 145 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +27 | 1318 |
| 146 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +26 | 1130 |
| 147 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +26 | 4617 |
| 148 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +26 | 8249 |
| 149 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +25 | 1655 |
| 150 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +25 | 18516 |
| 151 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +25 | 5536 |
| 152 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +24 | 8563 |
| 153 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +24 | 5504 |
| 154 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +24 | 17888 |
| 155 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1662 |
| 156 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +24 | 3336 |
| 157 | [floci-io/floci](https://github.com/floci-io/floci) | +24 | 16846 |
| 158 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 450 |
| 159 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1710 |
| 160 | [jundot/omlx](https://github.com/jundot/omlx) | +23 | 17910 |
| 161 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +23 | 16045 |
| 162 | [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | +23 | 8298 |
| 163 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +23 | 1744 |
| 164 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 1952 |
| 165 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +22 | 16186 |
| 166 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1333 |
| 167 | [browser-act/skills](https://github.com/browser-act/skills) | +21 | 4487 |
| 168 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +21 | 26377 |
| 169 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +21 | 26887 |
| 170 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +21 | 5678 |
| 171 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 1508 |
| 172 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +21 | 6898 |
| 173 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +20 | 8648 |
| 174 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 175 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +20 | 856 |
| 176 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +19 | 3697 |
| 177 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +19 | 1815 |
| 178 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +19 | 1693 |
| 179 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +19 | 3199 |
| 180 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +19 | 26527 |
| 181 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7706 |
| 182 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +18 | 27294 |
| 183 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +18 | 1936 |
| 184 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +18 | 667 |
| 185 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1922 |
| 186 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +17 | 3112 |
| 187 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +17 | 6990 |
| 188 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 661 |
| 189 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +17 | 2748 |
| 190 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +16 | 8373 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +16 | 29167 |
| 192 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +16 | 4231 |
| 193 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +16 | 18281 |
| 194 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 395 |
| 195 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +15 | 6352 |
| 196 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +14 | 7776 |
| 197 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +14 | 8489 |
| 198 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +14 | 5827 |
| 199 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 533 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +13 | 5440 |
| 201 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 202 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 498 |
| 203 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +12 | 1870 |
| 204 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +12 | 4434 |
| 205 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +12 | 2869 |
| 206 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 679 |
| 207 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 2698 |
| 208 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 696 |
| 209 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 817 |
| 210 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 352 |
| 211 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 843 |
| 212 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1041 |
| 213 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +10 | 11875 |
| 214 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 361 |
| 215 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 430 |
| 216 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 629 |
| 217 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 458 |
| 218 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 204 |
| 219 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +10 | 1454 |
| 220 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +10 | 688 |
| 221 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +9 | 2427 |
| 222 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 8977 |
| 223 | [rpamis/comet](https://github.com/rpamis/comet) | +9 | 2346 |
| 224 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +9 | 4540 |
| 225 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +9 | 2889 |
| 226 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5766 |
| 227 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +8 | 607 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 818 |
| 229 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 803 |
| 230 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 384 |
| 231 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4850 |
| 232 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +8 | 5018 |
| 233 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 207 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +8 | 3203 |
| 235 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 3981 |
| 236 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +8 | 486 |
| 237 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 604 |
| 238 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +7 | 5892 |
| 239 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6138 |
| 240 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1965 |
| 241 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1031 |
| 242 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 243 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 164 |
| 244 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +7 | 1888 |
| 245 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 353 |
| 246 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1761 |
| 247 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 457 |
| 248 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 419 |
| 249 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1597 |
| 250 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 545 |
| 251 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 633 |
| 252 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +6 | 370 |
| 253 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +6 | 2844 |
| 254 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 185 |
| 255 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2782 |
| 256 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +5 | 1350 |
| 257 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 305 |
| 258 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 2223 |
| 259 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 580 |
| 260 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 550 |
| 261 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 288 |
| 262 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 9774 |
| 263 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3722 |
| 264 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +5 | 906 |
| 265 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 95 |
| 266 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +4 | 424 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 603 |
| 268 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2733 |
| 269 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 331 |
| 270 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 1825 |
| 271 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 162 |
| 272 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 143 |
| 273 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2575 |
| 274 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 2850 |
| 275 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 557 |
| 276 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 123 |
| 277 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 25 |
| 278 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 279 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 687 |
| 280 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 281 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +3 | 3157 |
| 282 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +3 | 255 |
| 283 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 733 |
| 284 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 89 |
| 285 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2380 |
| 286 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 159 |
| 287 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 402 |
| 288 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 776 |
| 289 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 147 |
| 290 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 187 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 256 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 836 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1691 |
| 294 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 679 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3391 |
| 296 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 297 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 96 |
| 298 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 453 |
| 299 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +2 | 849 |
| 300 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 855 |
