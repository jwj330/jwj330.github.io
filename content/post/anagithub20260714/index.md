---
title: "2026-07-14 GitHub增长趋势报告"
description: "1.OfficeCLI+4 2.codeflow+3 3.boop-agent+3 4.VoxCPM+3 5.skills+3"
date: 2026-07-14T21:01:47+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-14 21:01:47

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
        'daily': {"categories": ["nashsu/llm_wiki", "David-Crty/databasement", "Natively-AI-assistant/natively-cluely-ai-assistant", "multica-ai/multica", "coreyhaines31/marketingskills", "HKUDS/Vibe-Trading", "intercom/2x-skills", "eatmoreduck/boss-zhipin-scraper", "palmier-io/palmier-pro", "DeusData/codebase-memory-mcp", "hasaneyldrm/exercises-dataset", "Alpha-Dojo/DojoAgents", "MadsLorentzen/ai-job-search", "heygen-com/hyperframes", "bradautomates/claude-video", "emilkowalski/skills", "OpenBMB/VoxCPM", "raroque/boop-agent", "braedonsaunders/codeflow", "iOfficeAI/OfficeCLI"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4]},
        'weekly': {"categories": ["ZhuLinsen/daily_stock_analysis", "TencentCloud/CubeSandbox", "kyutai-labs/pocket-tts", "dnshe/DNSHE-FreeDomains", "JCodesMore/ai-website-cloner-template", "diegosouzapw/OmniRoute", "HKUDS/Vibe-Trading", "usestrix/strix", "langchain-ai/openwiki", "stablyai/orca", "DeusData/codebase-memory-mcp", "k1tbyte/Wand-Enhancer", "emilkowalski/skills", "calesthio/OpenMontage", "Shpigford/knockoff", "bradautomates/claude-video", "ogulcancelik/herdr", "x4gKing/X4G", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search"], "data": [9, 10, 10, 10, 10, 12, 12, 13, 14, 14, 14, 15, 15, 16, 17, 18, 19, 24, 31, 61]},
        'monthly': {"categories": ["langchain-ai/openwiki", "mukul975/Anthropic-Cybersecurity-Skills", "topoteretes/cognee", "stablyai/orca", "mvanhorn/last30days-skill", "JCodesMore/ai-website-cloner-template", "xbtlin/ai-berkshire", "jamiepine/voicebox", "hugohe3/ppt-master", "apple/container", "baidu/Unlimited-OCR", "usestrix/strix", "elder-plinius/CL4R1T4S", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "DeusData/codebase-memory-mcp", "Panniantong/Agent-Reach", "calesthio/OpenMontage", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [177, 182, 184, 184, 188, 189, 195, 196, 219, 223, 225, 242, 280, 294, 299, 537, 558, 619, 698, 1617]}
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
| 1 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +4 | 16668 |
| 2 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +3 | 4449 |
| 3 | [raroque/boop-agent](https://github.com/raroque/boop-agent) | +3 | 1027 |
| 4 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +3 | 33375 |
| 5 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 12781 |
| 6 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 8434 |
| 7 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 35116 |
| 8 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2 | 22434 |
| 9 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +2 | 823 |
| 10 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +2 | 13359 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 31487 |
| 12 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +2 | 10605 |
| 13 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +2 | 691 |
| 14 | [intercom/2x-skills](https://github.com/intercom/2x-skills) | +2 | 172 |
| 15 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +2 | 22751 |
| 16 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 39188 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2 | 40422 |
| 18 | [Natively-AI-assistant/natively-cluely-ai-assistant](https://github.com/Natively-AI-assistant/natively-cluely-ai-assistant) | +2 | 1863 |
| 19 | [David-Crty/databasement](https://github.com/David-Crty/databasement) | +2 | 1358 |
| 20 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +2 | 14552 |
| 21 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2 | 38481 |
| 22 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 5776 |
| 23 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +2 | 10830 |
| 24 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2 | 45572 |
| 25 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +2 | 10151 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2 | 46679 |
| 27 | [TableProApp/TablePro](https://github.com/TableProApp/TablePro) | +2 | 5141 |
| 28 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +2 | 6994 |
| 29 | [RICHQAQ/PasteMD](https://github.com/RICHQAQ/PasteMD) | +1 | 5129 |
| 30 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +1 | 1628 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +61 | 22434 |
| 2 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +31 | 16668 |
| 3 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +24 | 5258 |
| 4 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +19 | 16452 |
| 5 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +18 | 8434 |
| 6 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1900 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +16 | 38481 |
| 8 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +15 | 12781 |
| 9 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +15 | 7718 |
| 10 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +14 | 31487 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +14 | 19036 |
| 12 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +14 | 11180 |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | +13 | 41466 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +12 | 22751 |
| 15 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +12 | 17285 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +10 | 28268 |
| 17 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +10 | 5776 |
| 18 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 7536 |
| 19 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +10 | 10151 |
| 20 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +9 | 57203 |
| 21 | [malisper/pgrust](https://github.com/malisper/pgrust) | +9 | 2919 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +9 | 41275 |
| 23 | [vercel-labs/native](https://github.com/vercel-labs/native) | +9 | 6259 |
| 24 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +8 | 33375 |
| 25 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +8 | 4329 |
| 26 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +8 | 52186 |
| 27 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +8 | 37826 |
| 28 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +8 | 18244 |
| 29 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +7 | 32112 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +7 | 35116 |
| 31 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +7 | 13359 |
| 32 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +7 | 10334 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +7 | 46679 |
| 34 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +7 | 14552 |
| 35 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +7 | 40099 |
| 36 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 6856 |
| 37 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +7 | 26601 |
| 38 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 40422 |
| 39 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +7 | 12704 |
| 40 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +7 | 13146 |
| 41 | [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) | +7 | 2409 |
| 42 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +7 | 1723 |
| 43 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +6 | 2128 |
| 44 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +6 | 691 |
| 45 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 39188 |
| 46 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +6 | 28615 |
| 47 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +6 | 5835 |
| 48 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +6 | 25445 |
| 49 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +6 | 2153 |
| 50 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +6 | 2318 |
| 51 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 1635 |
| 52 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 2154 |
| 53 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +6 | 6391 |
| 54 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +6 | 9385 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 28615 |
| 56 | [wouterdebie/davit](https://github.com/wouterdebie/davit) | +6 | 923 |
| 57 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +6 | 2132 |
| 58 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 1856 |
| 59 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4337 |
| 60 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 1329 |
| 61 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +5 | 30043 |
| 62 | [nasa/spacewasm](https://github.com/nasa/spacewasm) | +5 | 1218 |
| 63 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +5 | 823 |
| 64 | [chattocorp/chatto](https://github.com/chattocorp/chatto) | +5 | 1824 |
| 65 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +5 | 7934 |
| 66 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +5 | 1101 |
| 67 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 8850 |
| 68 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +5 | 1978 |
| 69 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +4 | 4449 |
| 70 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4 | 38996 |
| 71 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +4 | 2337 |
| 72 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +4 | 1262 |
| 73 | [facebook/astryx](https://github.com/facebook/astryx) | +4 | 8949 |
| 74 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +4 | 4581 |
| 75 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1241 |
| 76 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +4 | 6994 |
| 77 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 7767 |
| 78 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +4 | 26133 |
| 79 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4 | 4516 |
| 80 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +4 | 25580 |
| 81 | [turnstonelabs/turnstone](https://github.com/turnstonelabs/turnstone) | +4 | 879 |
| 82 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 30906 |
| 83 | [MaximeRivest/riddle](https://github.com/MaximeRivest/riddle) | +4 | 1560 |
| 84 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 11376 |
| 85 | [decolua/9router](https://github.com/decolua/9router) | +4 | 22173 |
| 86 | [Robbyant/lingbot-vla-v2](https://github.com/Robbyant/lingbot-vla-v2) | +4 | 532 |
| 87 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 22467 |
| 88 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +4 | 26739 |
| 89 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +4 | 4307 |
| 90 | [raroque/boop-agent](https://github.com/raroque/boop-agent) | +3 | 1027 |
| 91 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +3 | 2905 |
| 92 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 43228 |
| 93 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +3 | 21330 |
| 94 | [hicccc77/WeFlow](https://github.com/hicccc77/WeFlow) | +3 | 12966 |
| 95 | [ggbond268/MacTools](https://github.com/ggbond268/MacTools) | +3 | 659 |
| 96 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +3 | 10605 |
| 97 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +3 | 1037 |
| 98 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +3 | 46929 |
| 99 | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | +3 | 23320 |
| 100 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +3 | 5826 |
| 101 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +3 | 5772 |
| 102 | [mira-wm/mira](https://github.com/mira-wm/mira) | +3 | 391 |
| 103 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +3 | 1130 |
| 104 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +3 | 3908 |
| 105 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 14237 |
| 106 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +3 | 13168 |
| 107 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +3 | 27846 |
| 108 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +3 | 5220 |
| 109 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +3 | 4289 |
| 110 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 38293 |
| 111 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 6650 |
| 112 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 1025 |
| 113 | [x4gKing/PasarGuard-Node](https://github.com/x4gKing/PasarGuard-Node) | +2 | 561 |
| 114 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +2 | 7701 |
| 115 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +2 | 1361 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 22571 |
| 117 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 16042 |
| 118 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +2 | 5072 |
| 119 | [OpenMOSS/MOSS-Transcribe-Diarize](https://github.com/OpenMOSS/MOSS-Transcribe-Diarize) | +2 | 402 |
| 120 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +2 | 45572 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1617 | 83043 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +698 | 59152 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +619 | 38481 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +558 | 56211 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +537 | 31487 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +299 | 57203 |
| 7 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +294 | 10605 |
| 8 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +280 | 45447 |
| 9 | [usestrix/strix](https://github.com/usestrix/strix) | +242 | 41466 |
| 10 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +225 | 14237 |
| 11 | [apple/container](https://github.com/apple/container) | +223 | 47848 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +219 | 38996 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +196 | 41275 |
| 14 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +195 | 13146 |
| 15 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +189 | 28268 |
| 16 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +188 | 52186 |
| 17 | [stablyai/orca](https://github.com/stablyai/orca) | +184 | 19036 |
| 18 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +184 | 27865 |
| 19 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +182 | 25568 |
| 20 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +177 | 11180 |
| 21 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 8325 |
| 22 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +173 | 13168 |
| 23 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +171 | 16452 |
| 24 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7963 |
| 25 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26866 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +153 | 28615 |
| 27 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +153 | 6650 |
| 28 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +148 | 7767 |
| 29 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18625 |
| 30 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +140 | 26601 |
| 31 | [facebook/astryx](https://github.com/facebook/astryx) | +139 | 8949 |
| 32 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +135 | 28615 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +135 | 35116 |
| 34 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +134 | 16077 |
| 35 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +132 | 24595 |
| 36 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +131 | 7009 |
| 37 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +130 | 37826 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +128 | 46679 |
| 39 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +127 | 25128 |
| 40 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +126 | 22751 |
| 41 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5224 |
| 42 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +124 | 22434 |
| 43 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +124 | 7263 |
| 44 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +120 | 12704 |
| 45 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +117 | 23678 |
| 46 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +115 | 38293 |
| 47 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 48 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +113 | 17285 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +113 | 40099 |
| 50 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +110 | 35654 |
| 51 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 3908 |
| 52 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +107 | 8233 |
| 53 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +106 | 26187 |
| 54 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +103 | 13359 |
| 55 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +103 | 6196 |
| 56 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +102 | 62602 |
| 57 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4585 |
| 58 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +97 | 10532 |
| 59 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +96 | 17760 |
| 60 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +93 | 39188 |
| 61 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +93 | 23477 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +90 | 29192 |
| 63 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10334 |
| 64 | [alibaba/zvec](https://github.com/alibaba/zvec) | +87 | 14892 |
| 65 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 16913 |
| 66 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4289 |
| 67 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +83 | 33375 |
| 68 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6642 |
| 69 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +79 | 10991 |
| 70 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +79 | 12067 |
| 71 | [shadcn/improve](https://github.com/shadcn/improve) | +78 | 8234 |
| 72 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6112 |
| 73 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +75 | 25580 |
| 74 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +74 | 46929 |
| 75 | [antirez/ds4](https://github.com/antirez/ds4) | +74 | 18546 |
| 76 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +73 | 26219 |
| 77 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +73 | 8609 |
| 78 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +71 | 5835 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +71 | 27846 |
| 80 | [multica-ai/multica](https://github.com/multica-ai/multica) | +70 | 40422 |
| 81 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +69 | 12781 |
| 82 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +69 | 3667 |
| 83 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +68 | 4581 |
| 84 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +67 | 21418 |
| 85 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +67 | 22467 |
| 86 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +65 | 7718 |
| 87 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +65 | 16669 |
| 88 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 7934 |
| 89 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +64 | 10677 |
| 90 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +62 | 39839 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +61 | 32112 |
| 92 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +61 | 30906 |
| 93 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +60 | 22571 |
| 94 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2835 |
| 95 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +60 | 25445 |
| 96 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +59 | 26133 |
| 97 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +59 | 9385 |
| 98 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +58 | 8434 |
| 99 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2685 |
| 100 | [decolua/9router](https://github.com/decolua/9router) | +57 | 22173 |
| 101 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +57 | 3357 |
| 102 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +56 | 27461 |
| 103 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +56 | 3642 |
| 104 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +55 | 23042 |
| 105 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +55 | 27143 |
| 106 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +53 | 4516 |
| 107 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +52 | 4307 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +52 | 28287 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +50 | 50021 |
| 110 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +49 | 14306 |
| 111 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +48 | 32133 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +48 | 17006 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +47 | 43228 |
| 114 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +47 | 45321 |
| 115 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4709 |
| 116 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +45 | 8169 |
| 117 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +45 | 25353 |
| 118 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +45 | 22661 |
| 119 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +44 | 5772 |
| 120 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +44 | 33496 |
| 121 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +44 | 6032 |
| 122 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +41 | 9604 |
| 123 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +41 | 3062 |
| 124 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +41 | 6602 |
| 125 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +41 | 36103 |
| 126 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +40 | 13609 |
| 127 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1761 |
| 128 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +40 | 19857 |
| 129 | [anbeime/skill](https://github.com/anbeime/skill) | +39 | 3646 |
| 130 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1370 |
| 131 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1936 |
| 132 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +38 | 26652 |
| 133 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +37 | 11376 |
| 134 | [openai/plugins](https://github.com/openai/plugins) | +36 | 4577 |
| 135 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +36 | 8124 |
| 136 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +34 | 12382 |
| 137 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +33 | 26300 |
| 138 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2084 |
| 139 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +32 | 6231 |
| 140 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1960 |
| 141 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2075 |
| 142 | [openai/skills](https://github.com/openai/skills) | +31 | 23705 |
| 143 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +31 | 3619 |
| 144 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +31 | 4473 |
| 145 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +30 | 1247 |
| 146 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +30 | 4505 |
| 147 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1289 |
| 148 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +29 | 17768 |
| 149 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1118 |
| 150 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +29 | 1664 |
| 151 | [jundot/omlx](https://github.com/jundot/omlx) | +28 | 17830 |
| 152 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 2016 |
| 153 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1302 |
| 154 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +27 | 16042 |
| 155 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +27 | 1643 |
| 156 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +27 | 5412 |
| 157 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2500 |
| 158 | [floci-io/floci](https://github.com/floci-io/floci) | +27 | 16686 |
| 159 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +26 | 5258 |
| 160 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +26 | 15130 |
| 161 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +26 | 18359 |
| 162 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +25 | 2578 |
| 163 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +25 | 26401 |
| 164 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 1040 |
| 165 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +24 | 26235 |
| 166 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +24 | 3285 |
| 167 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1546 |
| 168 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +24 | 1577 |
| 169 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +24 | 15965 |
| 170 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 444 |
| 171 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1613 |
| 172 | [browser-act/skills](https://github.com/browser-act/skills) | +23 | 4385 |
| 173 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +23 | 8419 |
| 174 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +23 | 26739 |
| 175 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 1882 |
| 176 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +23 | 643 |
| 177 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +22 | 8443 |
| 178 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +22 | 5273 |
| 179 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +22 | 18185 |
| 180 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +21 | 3609 |
| 181 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +21 | 6876 |
| 182 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +21 | 4101 |
| 183 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +21 | 8403 |
| 184 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +20 | 1780 |
| 185 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 186 | [wshobson/agents](https://github.com/wshobson/agents) | +20 | 37911 |
| 187 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +19 | 1257 |
| 188 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +19 | 5741 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +18 | 8158 |
| 190 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +18 | 655 |
| 191 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 6411 |
| 192 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +18 | 2370 |
| 193 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +17 | 7536 |
| 194 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +17 | 2425 |
| 195 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +17 | 1262 |
| 196 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1900 |
| 197 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +17 | 29061 |
| 198 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +17 | 6192 |
| 199 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +16 | 1340 |
| 200 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +16 | 2538 |
| 201 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +16 | 7672 |
| 202 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 388 |
| 203 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +14 | 5359 |
| 204 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 523 |
| 205 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +14 | 2538 |
| 206 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +13 | 830 |
| 207 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +13 | 4369 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +13 | 11827 |
| 209 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 210 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +13 | 1442 |
| 211 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 467 |
| 212 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 483 |
| 213 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +12 | 2827 |
| 214 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 691 |
| 215 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 798 |
| 216 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +11 | 329 |
| 217 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 353 |
| 218 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2852 |
| 219 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 975 |
| 220 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 614 |
| 221 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 352 |
| 222 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 427 |
| 223 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 597 |
| 224 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 453 |
| 225 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 202 |
| 226 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +10 | 683 |
| 227 | [rpamis/comet](https://github.com/rpamis/comet) | +10 | 2272 |
| 228 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +10 | 4463 |
| 229 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +9 | 803 |
| 230 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +9 | 6076 |
| 231 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 1950 |
| 232 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 8898 |
| 233 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +9 | 920 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +9 | 3145 |
| 235 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5748 |
| 236 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +8 | 5835 |
| 237 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 788 |
| 238 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 377 |
| 239 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 2356 |
| 240 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4811 |
| 241 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 242 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +8 | 4999 |
| 243 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +8 | 404 |
| 244 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 4012 |
| 245 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +8 | 2814 |
| 246 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 568 |
| 247 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 299 |
| 248 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 163 |
| 249 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +7 | 363 |
| 250 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 337 |
| 251 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1736 |
| 252 | [oalanicolas/claude-design-premium](https://github.com/oalanicolas/claude-design-premium) | +7 | 252 |
| 253 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +7 | 248 |
| 254 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 455 |
| 255 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +6 | 1856 |
| 256 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +6 | 1332 |
| 257 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +6 | 2128 |
| 258 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1557 |
| 259 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 542 |
| 260 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +6 | 631 |
| 261 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +6 | 990 |
| 262 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +6 | 3693 |
| 263 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +6 | 877 |
| 264 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 183 |
| 265 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 361 |
| 266 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 456 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 568 |
| 268 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2570 |
| 269 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 92 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +5 | 2822 |
| 271 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 323 |
| 272 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2708 |
| 273 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 9504 |
| 274 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2368 |
| 275 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 1810 |
| 276 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 164 |
| 277 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 84 |
| 278 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 121 |
| 279 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 215 |
| 280 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 663 |
| 281 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 282 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 847 |
| 283 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +3 | 108 |
| 284 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 156 |
| 285 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 715 |
| 286 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 400 |
| 287 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 765 |
| 288 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +2 | 139 |
| 289 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 89 |
| 290 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 243 |
| 291 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 825 |
| 292 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1689 |
| 293 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 664 |
| 294 | [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | +2 | 218 |
| 295 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 547 |
| 296 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3374 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 95 |
| 299 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 425 |
| 300 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 853 |
