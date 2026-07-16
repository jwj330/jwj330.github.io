---
title: "2026-07-16 GitHub增长趋势报告"
description: "1.Vibe-Trading+9 2.marketingskills+4 3.orca+4 4.gpt-5.6-instruct+4 5.archify+4"
date: 2026-07-16T21:00:53+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-16 21:00:53

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
        'daily': {"categories": ["PrismML-Eng/Bonsai-demo", "rmyndharis/OpenWA", "openai/codex-plugin-cc", "ZhuLinsen/daily_stock_analysis", "shanraisshan/claude-code-best-practice", "EverMind-AI/EverOS", "iOfficeAI/OfficeCLI", "HKUDS/DeepTutor", "shadcn/improve", "DeusData/codebase-memory-mcp", "Dicklesworthstone/destructive_command_guard", "Alishahryar1/free-claude-code", "x4gKing/X4G", "MadsLorentzen/ai-job-search", "hugohe3/ppt-master", "tt-a1i/archify", "MDX-Tom/gpt-5.6-instruct", "stablyai/orca", "coreyhaines31/marketingskills", "HKUDS/Vibe-Trading"], "data": [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 9]},
        'weekly': {"categories": ["heygen-com/hyperframes", "Alishahryar1/free-claude-code", "hugohe3/ppt-master", "malisper/pgrust", "dnshe/DNSHE-FreeDomains", "jamiepine/voicebox", "calesthio/OpenMontage", "hasaneyldrm/exercises-dataset", "MDX-Tom/gpt-5.6-instruct", "bradautomates/claude-video", "DeusData/codebase-memory-mcp", "oso95/scroll-world", "x4gKing/X4G", "stablyai/orca", "Dicklesworthstone/destructive_command_guard", "k1tbyte/Wand-Enhancer", "iOfficeAI/OfficeCLI", "emilkowalski/skills", "HKUDS/Vibe-Trading", "MadsLorentzen/ai-job-search"], "data": [9, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 13, 14, 15, 18, 19, 20, 25, 26, 28]},
        'monthly': {"categories": ["ogulcancelik/herdr", "mukul975/Anthropic-Cybersecurity-Skills", "XxHuberrr/Mineradio", "langchain-ai/openwiki", "stablyai/orca", "topoteretes/cognee", "JCodesMore/ai-website-cloner-template", "apple/container", "xbtlin/ai-berkshire", "jamiepine/voicebox", "hugohe3/ppt-master", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "ZhuLinsen/daily_stock_analysis", "palmier-io/palmier-pro", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [169, 177, 178, 179, 182, 184, 187, 194, 197, 202, 205, 227, 234, 241, 295, 296, 532, 618, 642, 1189]}
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
| 1 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +9 | 24238 |
| 2 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +4 | 40172 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 20473 |
| 4 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 1658 |
| 5 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4 | 5414 |
| 6 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4 | 39471 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 23153 |
| 8 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 5638 |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 40502 |
| 10 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +3 | 5015 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +3 | 32099 |
| 12 | [shadcn/improve](https://github.com/shadcn/improve) | +3 | 8372 |
| 13 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 26808 |
| 14 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +3 | 18313 |
| 15 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11139 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3 | 62892 |
| 17 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 57529 |
| 18 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2 | 28918 |
| 19 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +2 | 11371 |
| 20 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +2 | 1477 |
| 21 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +2 | 2444 |
| 22 | [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | +2 | 830 |
| 23 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +2 | 2034 |
| 24 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +2 | 6129 |
| 25 | [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding) | +2 | 2813 |
| 26 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +2 | 25952 |
| 27 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +2 | 6223 |
| 28 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +2 | 12994 |
| 29 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +2 | 5578 |
| 30 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +2 | 1988 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +28 | 23153 |
| 2 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +26 | 24238 |
| 3 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +25 | 14371 |
| 4 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +20 | 18313 |
| 5 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +19 | 8458 |
| 6 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +18 | 5015 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +15 | 20474 |
| 8 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +14 | 5638 |
| 9 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +13 | 2867 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +12 | 32099 |
| 11 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +12 | 8787 |
| 12 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +11 | 1658 |
| 13 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +11 | 14958 |
| 14 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 39187 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +11 | 41844 |
| 16 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +11 | 6104 |
| 17 | [malisper/pgrust](https://github.com/malisper/pgrust) | +11 | 3191 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 39471 |
| 19 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +10 | 40502 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 35659 |
| 21 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +9 | 5414 |
| 22 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +9 | 14734 |
| 23 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +9 | 17118 |
| 24 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +9 | 11819 |
| 25 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +8 | 1477 |
| 26 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +8 | 32526 |
| 27 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +8 | 4562 |
| 28 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +8 | 2570 |
| 29 | [usestrix/strix](https://github.com/usestrix/strix) | +8 | 42001 |
| 30 | [MengTo/Skills](https://github.com/MengTo/Skills) | +8 | 2307 |
| 31 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +8 | 26800 |
| 32 | [vercel-labs/native](https://github.com/vercel-labs/native) | +8 | 6367 |
| 33 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 40172 |
| 34 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +7 | 2034 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +7 | 33467 |
| 36 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +7 | 7317 |
| 37 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +7 | 25615 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 57529 |
| 39 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +6 | 6223 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +6 | 5185 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 47280 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 40788 |
| 43 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 28459 |
| 44 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +6 | 6129 |
| 45 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +6 | 981 |
| 46 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +6 | 17985 |
| 47 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +6 | 13214 |
| 48 | [nasa/spacewasm](https://github.com/nasa/spacewasm) | +6 | 1288 |
| 49 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +6 | 10335 |
| 50 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +6 | 7063 |
| 51 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 1774 |
| 52 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +6 | 22913 |
| 53 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +5 | 8124 |
| 54 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +5 | 1437 |
| 55 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4393 |
| 56 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 25426 |
| 57 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +5 | 28227 |
| 58 | [shadcn/improve](https://github.com/shadcn/improve) | +5 | 8372 |
| 59 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 31025 |
| 60 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +5 | 8694 |
| 61 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 10717 |
| 62 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +5 | 26330 |
| 63 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +5 | 18461 |
| 64 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +5 | 4841 |
| 65 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +5 | 7673 |
| 66 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 2091 |
| 67 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +5 | 991 |
| 68 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 1493 |
| 69 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +5 | 1220 |
| 70 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +4 | 11371 |
| 71 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +4 | 915 |
| 72 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +4 | 26808 |
| 73 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +4 | 30232 |
| 74 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 16922 |
| 75 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +4 | 331 |
| 76 | [threerocks/hand-drawn-styles](https://github.com/threerocks/hand-drawn-styles) | +4 | 364 |
| 77 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +4 | 18077 |
| 78 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +4 | 28918 |
| 79 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +4 | 2734 |
| 80 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +4 | 4525 |
| 81 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +4 | 25952 |
| 82 | [facebook/astryx](https://github.com/facebook/astryx) | +4 | 9045 |
| 83 | [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | +4 | 2511 |
| 84 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +4 | 10321 |
| 85 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +4 | 19758 |
| 86 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4 | 62892 |
| 87 | [littledivy/mimic](https://github.com/littledivy/mimic) | +4 | 1098 |
| 88 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +4 | 29158 |
| 89 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 3277 |
| 90 | [nagisanzenin/engram](https://github.com/nagisanzenin/engram) | +4 | 830 |
| 91 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +4 | 38112 |
| 92 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +4 | 5950 |
| 93 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +4 | 1296 |
| 94 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +4 | 1268 |
| 95 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +4 | 752 |
| 96 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 28079 |
| 97 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +4 | 14341 |
| 98 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1296 |
| 99 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +3 | 6331 |
| 100 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +3 | 8519 |
| 101 | [hicccc77/WeFlow](https://github.com/hicccc77/WeFlow) | +3 | 12939 |
| 102 | [AIEraDev/Clypra](https://github.com/AIEraDev/Clypra) | +3 | 2853 |
| 103 | [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) | +3 | 4877 |
| 104 | [RICHQAQ/PasteMD](https://github.com/RICHQAQ/PasteMD) | +3 | 5146 |
| 105 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +3 | 9493 |
| 106 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 11139 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +3 | 17170 |
| 108 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +3 | 1199 |
| 109 | [QuantumByteOSS/quantumbyte](https://github.com/QuantumByteOSS/quantumbyte) | +3 | 315 |
| 110 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +3 | 4469 |
| 111 | [PhyAgentOS/PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS) | +3 | 657 |
| 112 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +3 | 4101 |
| 113 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +3 | 14854 |
| 114 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +3 | 1806 |
| 115 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +3 | 15039 |
| 116 | [Git-creat7/grokRegister-cpa](https://github.com/Git-creat7/grokRegister-cpa) | +3 | 330 |
| 117 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +3 | 6120 |
| 118 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +3 | 5126 |
| 119 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +3 | 5863 |
| 120 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 11564 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1189 | 84624 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +642 | 59515 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +618 | 39187 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +532 | 32099 |
| 5 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +296 | 10717 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +295 | 57529 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | +241 | 42001 |
| 8 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +234 | 25952 |
| 9 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 14341 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +205 | 39471 |
| 11 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +202 | 41844 |
| 12 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +197 | 13214 |
| 13 | [apple/container](https://github.com/apple/container) | +194 | 47907 |
| 14 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +187 | 28459 |
| 15 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +184 | 27923 |
| 16 | [stablyai/orca](https://github.com/stablyai/orca) | +182 | 20474 |
| 17 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +179 | 11819 |
| 18 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +178 | 8439 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +177 | 25637 |
| 20 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +169 | 17118 |
| 21 | [EpicGames/lore](https://github.com/EpicGames/lore) | +166 | 8046 |
| 22 | [google-research/timesfm](https://github.com/google-research/timesfm) | +153 | 26914 |
| 23 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +152 | 6695 |
| 24 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +145 | 18622 |
| 25 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +142 | 26800 |
| 26 | [facebook/astryx](https://github.com/facebook/astryx) | +141 | 9045 |
| 27 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +139 | 8124 |
| 28 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +138 | 24238 |
| 29 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +135 | 25083 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +134 | 29158 |
| 31 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +133 | 23153 |
| 32 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +133 | 28918 |
| 33 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +127 | 16223 |
| 34 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +127 | 35659 |
| 35 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5288 |
| 36 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +125 | 45650 |
| 37 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +117 | 13304 |
| 38 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 39 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +113 | 17985 |
| 40 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +110 | 14958 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +109 | 47280 |
| 42 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3942 |
| 43 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +108 | 38112 |
| 44 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +107 | 8313 |
| 45 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +106 | 26307 |
| 46 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +103 | 4701 |
| 47 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +102 | 6331 |
| 48 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +102 | 25426 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +101 | 40502 |
| 50 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +98 | 62892 |
| 51 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +90 | 40172 |
| 52 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10335 |
| 53 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +87 | 18077 |
| 54 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +87 | 7380 |
| 55 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +84 | 38542 |
| 56 | [browser-use/video-use](https://github.com/browser-use/video-use) | +83 | 16970 |
| 57 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4361 |
| 58 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6675 |
| 59 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +80 | 23837 |
| 60 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +80 | 10617 |
| 61 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +79 | 7222 |
| 62 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +78 | 12938 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +78 | 29510 |
| 64 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6345 |
| 65 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +77 | 11139 |
| 66 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +76 | 14371 |
| 67 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +76 | 23730 |
| 68 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +72 | 5950 |
| 69 | [alibaba/zvec](https://github.com/alibaba/zvec) | +72 | 14976 |
| 70 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +71 | 5185 |
| 71 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +70 | 18313 |
| 72 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +70 | 28079 |
| 73 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +70 | 22913 |
| 74 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +69 | 8458 |
| 75 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +69 | 3724 |
| 76 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +68 | 47038 |
| 77 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +67 | 25749 |
| 78 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +66 | 8123 |
| 79 | [multica-ai/multica](https://github.com/multica-ai/multica) | +65 | 40788 |
| 80 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +65 | 26392 |
| 81 | [antirez/ds4](https://github.com/antirez/ds4) | +65 | 18668 |
| 82 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +64 | 8694 |
| 83 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +63 | 10691 |
| 84 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +62 | 8787 |
| 85 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +61 | 31025 |
| 86 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2881 |
| 87 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +59 | 6104 |
| 88 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +58 | 32526 |
| 89 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +58 | 26330 |
| 90 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2731 |
| 91 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +57 | 3432 |
| 92 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +57 | 39916 |
| 93 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +56 | 33467 |
| 94 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +55 | 23098 |
| 95 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +55 | 3663 |
| 96 | [decolua/9router](https://github.com/decolua/9router) | +54 | 22365 |
| 97 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +54 | 22629 |
| 98 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +54 | 9493 |
| 99 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +54 | 27399 |
| 100 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +51 | 4525 |
| 101 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +50 | 5414 |
| 102 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +49 | 4841 |
| 103 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +47 | 25615 |
| 104 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +44 | 8230 |
| 105 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +43 | 32216 |
| 106 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +42 | 28442 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +42 | 6120 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +41 | 45413 |
| 109 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1811 |
| 110 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +39 | 43414 |
| 111 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +39 | 5863 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +39 | 17170 |
| 113 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +39 | 13659 |
| 114 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +39 | 27374 |
| 115 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +38 | 25425 |
| 116 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +38 | 9689 |
| 117 | [anbeime/skill](https://github.com/anbeime/skill) | +38 | 3786 |
| 118 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1379 |
| 119 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 2001 |
| 120 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +38 | 6715 |
| 121 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +37 | 33538 |
| 122 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +37 | 3086 |
| 123 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +36 | 11564 |
| 124 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +36 | 22783 |
| 125 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +36 | 36103 |
| 126 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +35 | 19940 |
| 127 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +34 | 26766 |
| 128 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2099 |
| 129 | [openai/plugins](https://github.com/openai/plugins) | +33 | 4561 |
| 130 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +32 | 12471 |
| 131 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2101 |
| 132 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +31 | 6408 |
| 133 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +31 | 1998 |
| 134 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +30 | 5638 |
| 135 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +30 | 1283 |
| 136 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +30 | 4572 |
| 137 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1304 |
| 138 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +30 | 3768 |
| 139 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +29 | 4569 |
| 140 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1131 |
| 141 | [openai/skills](https://github.com/openai/skills) | +28 | 23827 |
| 142 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 2233 |
| 143 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1315 |
| 144 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15146 |
| 145 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +27 | 8199 |
| 146 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2541 |
| 147 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +26 | 1651 |
| 148 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +26 | 18482 |
| 149 | [jundot/omlx](https://github.com/jundot/omlx) | +26 | 17880 |
| 150 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +25 | 1107 |
| 151 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +25 | 8519 |
| 152 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +25 | 17858 |
| 153 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +25 | 5497 |
| 154 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +24 | 3315 |
| 155 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1632 |
| 156 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +24 | 16016 |
| 157 | [floci-io/floci](https://github.com/floci-io/floci) | +24 | 16790 |
| 158 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 447 |
| 159 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1679 |
| 160 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +23 | 16158 |
| 161 | [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | +23 | 8287 |
| 162 | [browser-act/skills](https://github.com/browser-act/skills) | +22 | 4464 |
| 163 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +22 | 3667 |
| 164 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +22 | 26856 |
| 165 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +22 | 5652 |
| 166 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +22 | 1928 |
| 167 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +22 | 26474 |
| 168 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1316 |
| 169 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +21 | 5461 |
| 170 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +21 | 26325 |
| 171 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +21 | 8583 |
| 172 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 1905 |
| 173 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +21 | 2629 |
| 174 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 175 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +20 | 1646 |
| 176 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +20 | 1437 |
| 177 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +20 | 18253 |
| 178 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +20 | 662 |
| 179 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +19 | 1806 |
| 180 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +19 | 1691 |
| 181 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +19 | 6741 |
| 182 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7673 |
| 183 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +18 | 8302 |
| 184 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +18 | 1370 |
| 185 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +18 | 4182 |
| 186 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +18 | 660 |
| 187 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1908 |
| 188 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +17 | 3101 |
| 189 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1925 |
| 190 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +17 | 6960 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +17 | 29141 |
| 192 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +16 | 2468 |
| 193 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +16 | 2703 |
| 194 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +16 | 6253 |
| 195 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 393 |
| 196 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +15 | 8461 |
| 197 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +15 | 5800 |
| 198 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 533 |
| 199 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +13 | 2867 |
| 200 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +13 | 851 |
| 201 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +13 | 5416 |
| 202 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 203 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 484 |
| 204 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +12 | 4424 |
| 205 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +12 | 7749 |
| 206 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +12 | 2860 |
| 207 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +11 | 11853 |
| 208 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 2642 |
| 209 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 693 |
| 210 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 812 |
| 211 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 352 |
| 212 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 833 |
| 213 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1025 |
| 214 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 674 |
| 215 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 358 |
| 216 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 430 |
| 217 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 620 |
| 218 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 456 |
| 219 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 204 |
| 220 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +10 | 1448 |
| 221 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +10 | 686 |
| 222 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +9 | 5874 |
| 223 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 8947 |
| 224 | [rpamis/comet](https://github.com/rpamis/comet) | +9 | 2329 |
| 225 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +9 | 4517 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +9 | 3177 |
| 227 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +9 | 484 |
| 228 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2405 |
| 229 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5761 |
| 230 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 798 |
| 231 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +8 | 799 |
| 232 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 380 |
| 233 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +8 | 1881 |
| 234 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4834 |
| 235 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +8 | 5009 |
| 236 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 207 |
| 237 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 3964 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +8 | 2877 |
| 239 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 587 |
| 240 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6104 |
| 241 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1958 |
| 242 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1018 |
| 243 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 244 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +7 | 572 |
| 245 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 163 |
| 246 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 352 |
| 247 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1754 |
| 248 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 457 |
| 249 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +6 | 1346 |
| 250 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1585 |
| 251 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 545 |
| 252 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 633 |
| 253 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +6 | 367 |
| 254 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 858 |
| 255 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +6 | 2830 |
| 256 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 183 |
| 257 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2774 |
| 258 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +6 | 251 |
| 259 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 2091 |
| 260 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 403 |
| 261 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 572 |
| 262 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 536 |
| 263 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3714 |
| 264 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +5 | 898 |
| 265 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 93 |
| 266 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 590 |
| 267 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2725 |
| 268 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 9620 |
| 269 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2377 |
| 270 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 328 |
| 271 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 1820 |
| 272 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 164 |
| 273 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 142 |
| 274 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2572 |
| 275 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 2841 |
| 276 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 553 |
| 277 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 88 |
| 278 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 123 |
| 279 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +3 | 183 |
| 280 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 246 |
| 281 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 681 |
| 282 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 283 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +3 | 3152 |
| 284 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 729 |
| 285 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 403 |
| 286 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 773 |
| 287 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 99 |
| 288 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 252 |
| 289 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 833 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1690 |
| 291 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 677 |
| 292 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3389 |
| 293 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 294 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 95 |
| 295 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 441 |
| 296 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +2 | 849 |
| 297 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 854 |
| 298 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
| 299 | [tamboui/tamboui](https://github.com/tamboui/tamboui) | +2 | 590 |
| 300 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +2 | 126 |
