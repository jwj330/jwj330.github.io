---
title: "2026-07-15 GitHub增长趋势报告"
description: "1.Vibe-Trading+9 2.ai-job-search+8 3.destructive_command_guard+7 4.Bonsai-demo+6 5.scroll-world+6"
date: 2026-07-15T21:01:57+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-15 21:01:57

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
        'daily': {"categories": ["FareedKhan-dev/all-agentic-architectures", "bradautomates/claude-video", "agentscope-ai/QwenPaw", "braedonsaunders/codeflow", "cobusgreyling/loop-engineering", "nashsu/llm_wiki", "heygen-com/hyperframes", "emilkowalski/skills", "MengTo/Skills", "Wei-Shaw/sub2api", "VoltAgent/awesome-agent-skills", "jamiepine/voicebox", "iOfficeAI/OfficeCLI", "HenryNdubuaku/maths-cs-ai-compendium", "hasaneyldrm/exercises-dataset", "oso95/scroll-world", "PrismML-Eng/Bonsai-demo", "Dicklesworthstone/destructive_command_guard", "MadsLorentzen/ai-job-search", "HKUDS/Vibe-Trading"], "data": [3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 9]},
        'weekly': {"categories": ["usestrix/strix", "malisper/pgrust", "nashsu/llm_wiki", "hasaneyldrm/exercises-dataset", "DeusData/codebase-memory-mcp", "jamiepine/voicebox", "JCodesMore/ai-website-cloner-template", "Wei-Shaw/sub2api", "oso95/scroll-world", "ogulcancelik/herdr", "stablyai/orca", "calesthio/OpenMontage", "Dicklesworthstone/destructive_command_guard", "x4gKing/X4G", "emilkowalski/skills", "k1tbyte/Wand-Enhancer", "bradautomates/claude-video", "HKUDS/Vibe-Trading", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search"], "data": [9, 10, 10, 10, 11, 11, 11, 11, 12, 14, 14, 14, 15, 15, 16, 17, 17, 17, 25, 32]},
        'monthly': {"categories": ["ogulcancelik/herdr", "XxHuberrr/Mineradio", "stablyai/orca", "langchain-ai/openwiki", "mukul975/Anthropic-Cybersecurity-Skills", "topoteretes/cognee", "JCodesMore/ai-website-cloner-template", "xbtlin/ai-berkshire", "jamiepine/voicebox", "apple/container", "hugohe3/ppt-master", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [173, 178, 179, 179, 180, 184, 188, 196, 201, 205, 210, 227, 232, 241, 296, 299, 534, 620, 660, 1372]}
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
| 1 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +9 | 23600 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +8 | 22916 |
| 3 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +7 | 4718 |
| 4 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +6 | 1291 |
| 5 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +6 | 2498 |
| 6 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +5 | 14274 |
| 7 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +5 | 5832 |
| 8 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +5 | 17656 |
| 9 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +5 | 41556 |
| 10 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +4 | 28156 |
| 11 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +4 | 32317 |
| 12 | [MengTo/Skills](https://github.com/MengTo/Skills) | +4 | 2250 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 13327 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +3 | 35422 |
| 15 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +3 | 14648 |
| 16 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +3 | 7976 |
| 17 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +3 | 4525 |
| 18 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +3 | 22686 |
| 19 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 8633 |
| 20 | [FareedKhan-dev/all-agentic-architectures](https://github.com/FareedKhan-dev/all-agentic-architectures) | +3 | 3877 |
| 21 | [weifuwan/seatunnel-web](https://github.com/weifuwan/seatunnel-web) | +3 | 1382 |
| 22 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 8655 |
| 23 | [accomplish-ai/coworker](https://github.com/accomplish-ai/coworker) | +3 | 10896 |
| 24 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +3 | 25279 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 39222 |
| 26 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +3 | 1726 |
| 27 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +3 | 552 |
| 28 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3 | 47018 |
| 29 | [different-ai/openwork](https://github.com/different-ai/openwork) | +3 | 16889 |
| 30 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 16787 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +32 | 22916 |
| 2 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +25 | 17656 |
| 3 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +17 | 23600 |
| 4 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +17 | 8633 |
| 5 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +17 | 8075 |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +16 | 13327 |
| 7 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +15 | 5458 |
| 8 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +15 | 4718 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +14 | 38915 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +14 | 19790 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +14 | 16787 |
| 12 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +12 | 2498 |
| 13 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +11 | 32317 |
| 14 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +11 | 28465 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +11 | 41556 |
| 16 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +11 | 31823 |
| 17 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +10 | 14274 |
| 18 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +10 | 14648 |
| 19 | [malisper/pgrust](https://github.com/malisper/pgrust) | +10 | 2996 |
| 20 | [usestrix/strix](https://github.com/usestrix/strix) | +9 | 41828 |
| 21 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +9 | 11564 |
| 22 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 5933 |
| 23 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +9 | 1726 |
| 24 | [vercel-labs/native](https://github.com/vercel-labs/native) | +9 | 6325 |
| 25 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +8 | 35422 |
| 26 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +8 | 33412 |
| 27 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +8 | 40281 |
| 28 | [MengTo/Skills](https://github.com/MengTo/Skills) | +8 | 2250 |
| 29 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +7 | 4525 |
| 30 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +7 | 47018 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +7 | 39222 |
| 32 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 40633 |
| 33 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +7 | 7227 |
| 34 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +7 | 26737 |
| 35 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +7 | 10374 |
| 36 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 13234 |
| 37 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +7 | 17701 |
| 38 | [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | +7 | 2464 |
| 39 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +7 | 18365 |
| 40 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +7 | 25566 |
| 41 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +7 | 1178 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +7 | 57368 |
| 43 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +6 | 5832 |
| 44 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +6 | 1291 |
| 45 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +6 | 2499 |
| 46 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +6 | 6972 |
| 47 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +6 | 30973 |
| 48 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +6 | 1419 |
| 49 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +6 | 908 |
| 50 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +6 | 726 |
| 51 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +6 | 10283 |
| 52 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +6 | 7575 |
| 53 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +6 | 1911 |
| 54 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +5 | 7976 |
| 55 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +5 | 28156 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 39665 |
| 57 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +5 | 4801 |
| 58 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +5 | 8655 |
| 59 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4370 |
| 60 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +5 | 10671 |
| 61 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +5 | 5042 |
| 62 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +5 | 26228 |
| 63 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 1986 |
| 64 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +5 | 1376 |
| 65 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +5 | 5919 |
| 66 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 37969 |
| 67 | [nasa/spacewasm](https://github.com/nasa/spacewasm) | +5 | 1272 |
| 68 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +5 | 12827 |
| 69 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 28909 |
| 70 | [chattocorp/chatto](https://github.com/chattocorp/chatto) | +5 | 1879 |
| 71 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +5 | 1727 |
| 72 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +4 | 6296 |
| 73 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +4 | 25279 |
| 74 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 22686 |
| 75 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +4 | 30129 |
| 76 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +4 | 6033 |
| 77 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +4 | 781 |
| 78 | [facebook/astryx](https://github.com/facebook/astryx) | +4 | 9091 |
| 79 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +4 | 1209 |
| 80 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +4 | 23030 |
| 81 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +4 | 9444 |
| 82 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +4 | 25667 |
| 83 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +4 | 14285 |
| 84 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +4 | 47019 |
| 85 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +4 | 4445 |
| 86 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +4 | 2200 |
| 87 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1273 |
| 88 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +4 | 28804 |
| 89 | [decolua/9router](https://github.com/decolua/9router) | +4 | 22294 |
| 90 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +4 | 5819 |
| 91 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 11479 |
| 92 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +3 | 8477 |
| 93 | [RICHQAQ/PasteMD](https://github.com/RICHQAQ/PasteMD) | +3 | 5139 |
| 94 | [FareedKhan-dev/all-agentic-architectures](https://github.com/FareedKhan-dev/all-agentic-architectures) | +3 | 3877 |
| 95 | [weifuwan/seatunnel-web](https://github.com/weifuwan/seatunnel-web) | +3 | 1382 |
| 96 | [accomplish-ai/coworker](https://github.com/accomplish-ai/coworker) | +3 | 10896 |
| 97 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +3 | 552 |
| 98 | [different-ai/openwork](https://github.com/different-ai/openwork) | +3 | 16889 |
| 99 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +3 | 4422 |
| 100 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +3 | 143 |
| 101 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +3 | 14817 |
| 102 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +3 | 1799 |
| 103 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +3 | 15014 |
| 104 | [littledivy/mimic](https://github.com/littledivy/mimic) | +3 | 993 |
| 105 | [Git-creat7/grokRegister-cpa](https://github.com/Git-creat7/grokRegister-cpa) | +3 | 294 |
| 106 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +3 | 6081 |
| 107 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +3 | 5102 |
| 108 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +3 | 3093 |
| 109 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +3 | 1213 |
| 110 | [HiDream-ai/HiDream-O1-Image](https://github.com/HiDream-ai/HiDream-O1-Image) | +3 | 1508 |
| 111 | [turnstonelabs/turnstone](https://github.com/turnstonelabs/turnstone) | +3 | 890 |
| 112 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 26809 |
| 113 | [google/skills](https://github.com/google/skills) | +3 | 14846 |
| 114 | [mira-wm/mira](https://github.com/mira-wm/mira) | +3 | 400 |
| 115 | [Robbyant/lingbot-vla-v2](https://github.com/Robbyant/lingbot-vla-v2) | +3 | 548 |
| 116 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +3 | 3925 |
| 117 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +3 | 13241 |
| 118 | [Robbyant/lingbot-video](https://github.com/Robbyant/lingbot-video) | +3 | 801 |
| 119 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 1061 |
| 120 | [SulgX/SulgX-Panel](https://github.com/SulgX/SulgX-Panel) | +2 | 271 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1372 | 83957 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +660 | 59346 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +620 | 38915 |
| 4 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +534 | 31823 |
| 5 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +299 | 57368 |
| 6 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +296 | 10671 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | +241 | 41828 |
| 8 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +232 | 25951 |
| 9 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 14285 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +210 | 39222 |
| 11 | [apple/container](https://github.com/apple/container) | +205 | 47927 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +201 | 41557 |
| 13 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +196 | 13234 |
| 14 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +188 | 28465 |
| 15 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +184 | 27948 |
| 16 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +180 | 25633 |
| 17 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +179 | 11564 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +179 | 19790 |
| 19 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +178 | 8381 |
| 20 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +173 | 16787 |
| 21 | [EpicGames/lore](https://github.com/EpicGames/lore) | +166 | 8017 |
| 22 | [google-research/timesfm](https://github.com/google-research/timesfm) | +154 | 26886 |
| 23 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +153 | 6669 |
| 24 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +149 | 45585 |
| 25 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +145 | 7976 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +144 | 28909 |
| 27 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18674 |
| 28 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +142 | 26737 |
| 29 | [facebook/astryx](https://github.com/facebook/astryx) | +140 | 9091 |
| 30 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +136 | 24948 |
| 31 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +132 | 28804 |
| 32 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +131 | 22916 |
| 33 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +131 | 23600 |
| 34 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +130 | 35422 |
| 35 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +129 | 13241 |
| 36 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +128 | 16136 |
| 37 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5267 |
| 38 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +121 | 37969 |
| 39 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +116 | 47018 |
| 40 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +115 | 25279 |
| 41 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 42 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +113 | 17701 |
| 43 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +109 | 40281 |
| 44 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +109 | 7332 |
| 45 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +108 | 14274 |
| 46 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3925 |
| 47 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +106 | 8271 |
| 48 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +106 | 26245 |
| 49 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +105 | 7122 |
| 50 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +104 | 6296 |
| 51 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +103 | 4651 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +99 | 38396 |
| 53 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +99 | 62663 |
| 54 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +94 | 12827 |
| 55 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +94 | 23711 |
| 56 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +91 | 17936 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +89 | 39665 |
| 58 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10374 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +86 | 29346 |
| 60 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +85 | 10574 |
| 61 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 16971 |
| 62 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4326 |
| 63 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6657 |
| 64 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +81 | 23632 |
| 65 | [alibaba/zvec](https://github.com/alibaba/zvec) | +79 | 14932 |
| 66 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6241 |
| 67 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +77 | 11062 |
| 68 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +75 | 25667 |
| 69 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +72 | 5919 |
| 70 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +71 | 27957 |
| 71 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +70 | 13327 |
| 72 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +70 | 26309 |
| 73 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +69 | 4801 |
| 74 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +69 | 47019 |
| 75 | [antirez/ds4](https://github.com/antirez/ds4) | +69 | 18617 |
| 76 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +69 | 3701 |
| 77 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +68 | 17656 |
| 78 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +67 | 8075 |
| 79 | [multica-ai/multica](https://github.com/multica-ai/multica) | +67 | 40633 |
| 80 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +67 | 33412 |
| 81 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +67 | 22686 |
| 82 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +66 | 8655 |
| 83 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 8035 |
| 84 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +63 | 10711 |
| 85 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +62 | 32317 |
| 86 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +62 | 30973 |
| 87 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +62 | 21485 |
| 88 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +61 | 8633 |
| 89 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +61 | 2863 |
| 90 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +58 | 26228 |
| 91 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2711 |
| 92 | [decolua/9router](https://github.com/decolua/9router) | +57 | 22294 |
| 93 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +57 | 3401 |
| 94 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +57 | 5933 |
| 95 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +57 | 39878 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +56 | 9444 |
| 97 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +55 | 22651 |
| 98 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +55 | 23109 |
| 99 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27473 |
| 100 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +55 | 3656 |
| 101 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +54 | 4445 |
| 102 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +48 | 25566 |
| 103 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +48 | 5042 |
| 104 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +47 | 4776 |
| 105 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +47 | 28376 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +46 | 32174 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +45 | 6081 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +44 | 45366 |
| 109 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +43 | 8198 |
| 110 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +41 | 17112 |
| 111 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +41 | 36103 |
| 112 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1791 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +40 | 43335 |
| 114 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +40 | 33509 |
| 115 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +40 | 22750 |
| 116 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +40 | 6666 |
| 117 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +39 | 13631 |
| 118 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +39 | 5819 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +39 | 25389 |
| 120 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +39 | 9647 |
| 121 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +39 | 3070 |
| 122 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +39 | 27278 |
| 123 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1378 |
| 124 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1963 |
| 125 | [anbeime/skill](https://github.com/anbeime/skill) | +37 | 3723 |
| 126 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +37 | 19905 |
| 127 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +36 | 26707 |
| 128 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +35 | 11479 |
| 129 | [openai/plugins](https://github.com/openai/plugins) | +34 | 4604 |
| 130 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2091 |
| 131 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +33 | 12440 |
| 132 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +33 | 8160 |
| 133 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +32 | 6326 |
| 134 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1991 |
| 135 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2093 |
| 136 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +31 | 3697 |
| 137 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +30 | 1265 |
| 138 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +30 | 4545 |
| 139 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1296 |
| 140 | [openai/skills](https://github.com/openai/skills) | +29 | 23771 |
| 141 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1128 |
| 142 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +29 | 4529 |
| 143 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +28 | 17822 |
| 144 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 2099 |
| 145 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1306 |
| 146 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +27 | 5458 |
| 147 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15138 |
| 148 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +27 | 18437 |
| 149 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +27 | 1649 |
| 150 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2527 |
| 151 | [jundot/omlx](https://github.com/jundot/omlx) | +26 | 17853 |
| 152 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +26 | 5445 |
| 153 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +25 | 15996 |
| 154 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +25 | 5630 |
| 155 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 16734 |
| 156 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 1074 |
| 157 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +24 | 8477 |
| 158 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +24 | 16098 |
| 159 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +24 | 3302 |
| 160 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1600 |
| 161 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 445 |
| 162 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1636 |
| 163 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +23 | 26280 |
| 164 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +23 | 26809 |
| 165 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +23 | 2609 |
| 166 | [browser-act/skills](https://github.com/browser-act/skills) | +22 | 4415 |
| 167 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +22 | 3643 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +22 | 8504 |
| 169 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +22 | 5401 |
| 170 | [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | +22 | 8266 |
| 171 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +22 | 1905 |
| 172 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +21 | 1677 |
| 173 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +21 | 1608 |
| 174 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +21 | 26338 |
| 175 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +21 | 18213 |
| 176 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +21 | 651 |
| 177 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +21 | 26434 |
| 178 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +20 | 1799 |
| 179 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 180 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +20 | 15014 |
| 181 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +20 | 6922 |
| 182 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +19 | 1286 |
| 183 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +19 | 1294 |
| 184 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +19 | 4138 |
| 185 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +18 | 1376 |
| 186 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +18 | 8214 |
| 187 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 6575 |
| 188 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +18 | 658 |
| 189 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +17 | 7575 |
| 190 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1888 |
| 191 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1911 |
| 192 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +17 | 29100 |
| 193 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +17 | 1353 |
| 194 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +17 | 5769 |
| 195 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +17 | 6215 |
| 196 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +16 | 8427 |
| 197 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 391 |
| 198 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +15 | 2645 |
| 199 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 530 |
| 200 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +13 | 4401 |
| 201 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +13 | 845 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +13 | 5382 |
| 203 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +13 | 7713 |
| 204 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 205 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +13 | 1444 |
| 206 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 478 |
| 207 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +12 | 11838 |
| 208 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +12 | 2845 |
| 209 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +12 | 484 |
| 210 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +11 | 2498 |
| 211 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 2596 |
| 212 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 690 |
| 213 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 806 |
| 214 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 351 |
| 215 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 819 |
| 216 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1011 |
| 217 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 632 |
| 218 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 354 |
| 219 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 428 |
| 220 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 611 |
| 221 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 455 |
| 222 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 203 |
| 223 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +10 | 685 |
| 224 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +10 | 2863 |
| 225 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +9 | 5858 |
| 226 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 8919 |
| 227 | [rpamis/comet](https://github.com/rpamis/comet) | +9 | 2307 |
| 228 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +9 | 3161 |
| 229 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +8 | 6085 |
| 230 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +8 | 1955 |
| 231 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5752 |
| 232 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 789 |
| 233 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 378 |
| 234 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +8 | 1876 |
| 235 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4821 |
| 236 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +8 | 4997 |
| 237 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 205 |
| 238 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +8 | 919 |
| 239 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +8 | 4490 |
| 240 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +8 | 2821 |
| 241 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 4023 |
| 242 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 576 |
| 243 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 244 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +7 | 519 |
| 245 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +7 | 2378 |
| 246 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 163 |
| 247 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 347 |
| 248 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +7 | 767 |
| 249 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1745 |
| 250 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +7 | 249 |
| 251 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 456 |
| 252 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +6 | 1339 |
| 253 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1578 |
| 254 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 543 |
| 255 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 632 |
| 256 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 1011 |
| 257 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +6 | 364 |
| 258 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 849 |
| 259 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 183 |
| 260 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +6 | 891 |
| 261 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +6 | 2765 |
| 262 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 1986 |
| 263 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 373 |
| 264 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 551 |
| 265 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3704 |
| 266 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 92 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 578 |
| 268 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2720 |
| 269 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +4 | 2571 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2830 |
| 271 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 9509 |
| 272 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2374 |
| 273 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +4 | 326 |
| 274 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +4 | 180 |
| 275 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 1816 |
| 276 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 164 |
| 277 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 550 |
| 278 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 87 |
| 279 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 123 |
| 280 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 230 |
| 281 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 671 |
| 282 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 283 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +3 | 3139 |
| 284 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +3 | 109 |
| 285 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 159 |
| 286 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 725 |
| 287 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 401 |
| 288 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 768 |
| 289 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +2 | 140 |
| 290 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 97 |
| 291 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 247 |
| 292 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 827 |
| 293 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1689 |
| 294 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 671 |
| 295 | [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | +2 | 218 |
| 296 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3381 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 95 |
| 299 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 430 |
| 300 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +2 | 846 |
