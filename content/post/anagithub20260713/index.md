---
title: "2026-07-13 GitHub增长趋势报告"
description: "1.Vibe-Trading+6 2.destructive_command_guard+5 3.OpenMontage+3 4.orca+3 5.OmniRoute+3"
date: 2026-07-13T20:57:55+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-13 20:57:55

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
        'daily': {"categories": ["basketikun/chatgpt2api", "AIDC-AI/Pixelle-Video", "dramaclaw/dramaclaw", "HBAI-Ltd/Toonflow-app", "microsoft/ResearchStudio", "THU-MAIC/OpenMAIC", "JuneYaooo/nihaisha-nishi-tcm", "OpenBMB/VoxCPM", "Mesh-LLM/mesh-llm", "emilkowalski/skills", "x4gKing/X4G", "oso95/scroll-world", "dnshe/DNSHE-FreeDomains", "ogulcancelik/herdr", "DeusData/codebase-memory-mcp", "diegosouzapw/OmniRoute", "stablyai/orca", "calesthio/OpenMontage", "Dicklesworthstone/destructive_command_guard", "HKUDS/Vibe-Trading"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6]},
        'weekly': {"categories": ["mvanhorn/last30days-skill", "alibaba/page-agent", "kyutai-labs/pocket-tts", "HKUDS/Vibe-Trading", "JCodesMore/ai-website-cloner-template", "generative-computing/mellea", "emilkowalski/skills", "DeusData/codebase-memory-mcp", "k1tbyte/Wand-Enhancer", "calesthio/OpenMontage", "stablyai/orca", "Shpigford/knockoff", "diegosouzapw/OmniRoute", "usestrix/strix", "bradautomates/claude-video", "ogulcancelik/herdr", "x4gKing/X4G", "langchain-ai/openwiki", "iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search"], "data": [10, 11, 11, 11, 11, 12, 12, 13, 15, 15, 15, 17, 21, 22, 22, 25, 25, 26, 32, 69]},
        'monthly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "topoteretes/cognee", "stablyai/orca", "JCodesMore/ai-website-cloner-template", "xbtlin/ai-berkshire", "jamiepine/voicebox", "baidu/Unlimited-OCR", "NVIDIA/SkillSpector", "hugohe3/ppt-master", "mvanhorn/last30days-skill", "usestrix/strix", "apple/container", "palmier-io/palmier-pro", "ZhuLinsen/daily_stock_analysis", "elder-plinius/CL4R1T4S", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "Panniantong/Agent-Reach", "headroomlabs-ai/headroom", "DietrichGebert/ponytail"], "data": [184, 185, 188, 191, 194, 203, 225, 228, 229, 237, 241, 276, 292, 315, 480, 539, 617, 652, 784, 1690]}
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
| 1 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 21628 |
| 2 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +5 | 3802 |
| 3 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 37978 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 18118 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 16790 |
| 6 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +3 | 31066 |
| 7 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 16090 |
| 8 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 5596 |
| 9 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +3 | 1565 |
| 10 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 5036 |
| 11 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 12325 |
| 12 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +3 | 2055 |
| 13 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2 | 33278 |
| 14 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +2 | 1287 |
| 15 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2 | 19650 |
| 16 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +2 | 795 |
| 17 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +2 | 11440 |
| 18 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +2 | 1263 |
| 19 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +2 | 25358 |
| 20 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +2 | 5053 |
| 21 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +2 | 12525 |
| 22 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +2 | 1678 |
| 23 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +2 | 6771 |
| 24 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 3024 |
| 25 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 15993 |
| 26 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +2 | 41031 |
| 27 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +2 | 4437 |
| 28 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +2 | 4233 |
| 29 | [iisu-network/iiSU](https://github.com/iisu-network/iiSU) | +2 | 2429 |
| 30 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +2 | 2102 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +69 | 21858 |
| 2 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +32 | 16044 |
| 3 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +26 | 10906 |
| 4 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +25 | 5036 |
| 5 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 16090 |
| 6 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +22 | 8091 |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | +22 | 41173 |
| 8 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +21 | 16790 |
| 9 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1866 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +15 | 18118 |
| 11 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +15 | 37978 |
| 12 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +15 | 7329 |
| 13 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 31066 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 12325 |
| 15 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1723 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +11 | 28089 |
| 17 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +11 | 21628 |
| 18 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 7497 |
| 19 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +11 | 26416 |
| 20 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +10 | 51937 |
| 21 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +10 | 12529 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +10 | 13011 |
| 23 | [malisper/pgrust](https://github.com/malisper/pgrust) | +9 | 2793 |
| 24 | [vercel-labs/native](https://github.com/vercel-labs/native) | +9 | 6138 |
| 25 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +9 | 41031 |
| 26 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +9 | 18123 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 28315 |
| 28 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +8 | 3802 |
| 29 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 5596 |
| 30 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +8 | 57053 |
| 31 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +8 | 28362 |
| 32 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +8 | 5881 |
| 33 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +8 | 37672 |
| 34 | [tutti-os/tutti](https://github.com/tutti-os/tutti) | +8 | 2102 |
| 35 | [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) | +8 | 2066 |
| 36 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +8 | 9971 |
| 37 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +8 | 4184 |
| 38 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +7 | 31875 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +7 | 39965 |
| 40 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +7 | 10290 |
| 41 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +7 | 6771 |
| 42 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +7 | 8756 |
| 43 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +7 | 9317 |
| 44 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 1952 |
| 45 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +7 | 22236 |
| 46 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +6 | 33278 |
| 47 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +6 | 1263 |
| 48 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +6 | 5737 |
| 49 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 46313 |
| 50 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +6 | 12525 |
| 51 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +6 | 25358 |
| 52 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +6 | 2733 |
| 53 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +6 | 29973 |
| 54 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +6 | 4624 |
| 55 | [shadcn/improve](https://github.com/shadcn/improve) | +6 | 8172 |
| 56 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 34758 |
| 57 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 1486 |
| 58 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 40194 |
| 59 | [MengTo/Skills](https://github.com/MengTo/Skills) | +6 | 2020 |
| 60 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +6 | 6375 |
| 61 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 38445 |
| 62 | [wouterdebie/davit](https://github.com/wouterdebie/davit) | +6 | 907 |
| 63 | [alibaba/zvec](https://github.com/alibaba/zvec) | +6 | 14854 |
| 64 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +5 | 1565 |
| 65 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +5 | 4233 |
| 66 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +5 | 14472 |
| 67 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 38756 |
| 68 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 8642 |
| 69 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +5 | 7798 |
| 70 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 30828 |
| 71 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +5 | 1021 |
| 72 | [decolua/9router](https://github.com/decolua/9router) | +5 | 22052 |
| 73 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +5 | 1923 |
| 74 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +4 | 1678 |
| 75 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +4 | 1198 |
| 76 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +4 | 4437 |
| 77 | [Hao0321/video-autopilot-kit](https://github.com/Hao0321/video-autopilot-kit) | +4 | 1216 |
| 78 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 7294 |
| 79 | [microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio) | +4 | 795 |
| 80 | [nasa/spacewasm](https://github.com/nasa/spacewasm) | +4 | 1145 |
| 81 | [turnstonelabs/turnstone](https://github.com/turnstonelabs/turnstone) | +4 | 860 |
| 82 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +4 | 652 |
| 83 | [baairon/torlink](https://github.com/baairon/torlink) | +4 | 3546 |
| 84 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4 | 4176 |
| 85 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +4 | 26024 |
| 86 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +4 | 1501 |
| 87 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +4 | 13101 |
| 88 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +4 | 3759 |
| 89 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +4 | 26687 |
| 90 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 27736 |
| 91 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 11266 |
| 92 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 5216 |
| 93 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 4193 |
| 94 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 43086 |
| 95 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +3 | 22505 |
| 96 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +3 | 15993 |
| 97 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +3 | 46849 |
| 98 | [Mesh-LLM/mesh-llm](https://github.com/Mesh-LLM/mesh-llm) | +3 | 2055 |
| 99 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +3 | 19650 |
| 100 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +3 | 5053 |
| 101 | [openai/plugins](https://github.com/openai/plugins) | +3 | 4542 |
| 102 | [erincatto/box3d](https://github.com/erincatto/box3d) | +3 | 5153 |
| 103 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +3 | 1070 |
| 104 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 14177 |
| 105 | [tiantianGPU/reg-factory](https://github.com/tiantianGPU/reg-factory) | +3 | 1434 |
| 106 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +3 | 725 |
| 107 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +3 | 4542 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 28167 |
| 109 | [Robbyant/lingbot-vla-v2](https://github.com/Robbyant/lingbot-vla-v2) | +3 | 513 |
| 110 | [mira-wm/mira](https://github.com/mira-wm/mira) | +3 | 380 |
| 111 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 38182 |
| 112 | [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd) | +3 | 1388 |
| 113 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 6607 |
| 114 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 16821 |
| 115 | [kuskhan/jetendard](https://github.com/kuskhan/jetendard) | +3 | 303 |
| 116 | [x4gKing/3x-ui-Upgrade](https://github.com/x4gKing/3x-ui-Upgrade) | +2 | 943 |
| 117 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +2 | 7675 |
| 118 | [h1papc11/healthcare-ai-agent-vault](https://github.com/h1papc11/healthcare-ai-agent-vault) | +2 | 152 |
| 119 | [x4gKing/PasarGuard-Node](https://github.com/x4gKing/PasarGuard-Node) | +2 | 532 |
| 120 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +2 | 1287 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1690 | 82219 |
| 2 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +784 | 58950 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +652 | 55736 |
| 4 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +617 | 37978 |
| 5 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +539 | 31066 |
| 6 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +480 | 45361 |
| 7 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +315 | 57053 |
| 8 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +292 | 10418 |
| 9 | [apple/container](https://github.com/apple/container) | +276 | 47694 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | +241 | 41173 |
| 11 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +237 | 51937 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +229 | 38756 |
| 13 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +228 | 13101 |
| 14 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +225 | 14177 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +203 | 41031 |
| 16 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +194 | 13011 |
| 17 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +191 | 28089 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +188 | 18118 |
| 19 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 27765 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +184 | 25486 |
| 21 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +180 | 16090 |
| 22 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +177 | 7209 |
| 23 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +176 | 10906 |
| 24 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +176 | 8282 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +169 | 28315 |
| 26 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +168 | 6867 |
| 27 | [EpicGames/lore](https://github.com/EpicGames/lore) | +165 | 7867 |
| 28 | [google-research/timesfm](https://github.com/google-research/timesfm) | +158 | 26846 |
| 29 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +157 | 6607 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +154 | 34758 |
| 31 | [shadcn/improve](https://github.com/shadcn/improve) | +153 | 8172 |
| 32 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +150 | 37672 |
| 33 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +149 | 7294 |
| 34 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +146 | 16006 |
| 35 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +144 | 23624 |
| 36 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18569 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +142 | 46313 |
| 38 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +140 | 26416 |
| 39 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +140 | 24988 |
| 40 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +140 | 35594 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +139 | 28362 |
| 42 | [facebook/astryx](https://github.com/facebook/astryx) | +138 | 8642 |
| 43 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +135 | 21628 |
| 44 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +134 | 38182 |
| 45 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +134 | 12529 |
| 46 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +133 | 24094 |
| 47 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +129 | 11930 |
| 48 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5153 |
| 49 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +123 | 39965 |
| 50 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +122 | 21858 |
| 51 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +115 | 16790 |
| 52 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +115 | 8195 |
| 53 | [clent267/FUNCAPTCHAV3](https://github.com/clent267/FUNCAPTCHAV3) | +113 | 1 |
| 54 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +113 | 10481 |
| 55 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +112 | 17579 |
| 56 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +108 | 23344 |
| 57 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +107 | 3901 |
| 58 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +107 | 26136 |
| 59 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +106 | 62530 |
| 60 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +105 | 6100 |
| 61 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +101 | 12525 |
| 62 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +101 | 4498 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +98 | 29040 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +97 | 38446 |
| 65 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +94 | 33278 |
| 66 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10290 |
| 67 | [alibaba/zvec](https://github.com/alibaba/zvec) | +87 | 14854 |
| 68 | [browser-use/video-use](https://github.com/browser-use/video-use) | +86 | 16821 |
| 69 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +83 | 4193 |
| 70 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +82 | 25488 |
| 71 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +82 | 10927 |
| 72 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +80 | 6614 |
| 73 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +80 | 26113 |
| 74 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +79 | 8571 |
| 75 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +79 | 27096 |
| 76 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 5882 |
| 77 | [antirez/ds4](https://github.com/antirez/ds4) | +77 | 18437 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +76 | 27736 |
| 79 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +75 | 46849 |
| 80 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +75 | 25358 |
| 81 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +74 | 21366 |
| 82 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +72 | 22236 |
| 83 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +71 | 5737 |
| 84 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +71 | 34785 |
| 85 | [multica-ai/multica](https://github.com/multica-ai/multica) | +70 | 40194 |
| 86 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +70 | 4176 |
| 87 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +68 | 4437 |
| 88 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +68 | 31875 |
| 89 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +68 | 16044 |
| 90 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +68 | 8137 |
| 91 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +66 | 7798 |
| 92 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +66 | 12325 |
| 93 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +66 | 32123 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +65 | 39793 |
| 95 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +65 | 9317 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +65 | 30828 |
| 97 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +64 | 7329 |
| 98 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +64 | 10623 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +63 | 22505 |
| 100 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +62 | 26984 |
| 101 | [decolua/9router](https://github.com/decolua/9router) | +61 | 22052 |
| 102 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +61 | 2811 |
| 103 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +61 | 28167 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +60 | 49940 |
| 105 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +58 | 8091 |
| 106 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +58 | 22994 |
| 107 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +58 | 5717 |
| 108 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +58 | 2669 |
| 109 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +57 | 3298 |
| 110 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +56 | 22578 |
| 111 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +56 | 27441 |
| 112 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +56 | 3625 |
| 113 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +55 | 16968 |
| 114 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +54 | 43086 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +53 | 32077 |
| 116 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +52 | 4184 |
| 117 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +52 | 45261 |
| 118 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +49 | 33456 |
| 119 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +48 | 5954 |
| 120 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +47 | 25277 |
| 121 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +46 | 4624 |
| 122 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +45 | 9575 |
| 123 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +44 | 6510 |
| 124 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +43 | 3047 |
| 125 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +43 | 36103 |
| 126 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +43 | 19814 |
| 127 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +42 | 11266 |
| 128 | [anbeime/skill](https://github.com/anbeime/skill) | +42 | 3570 |
| 129 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +42 | 26596 |
| 130 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | +41 | 13575 |
| 131 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +41 | 2561 |
| 132 | [google-research/tabfm](https://github.com/google-research/tabfm) | +40 | 1726 |
| 133 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +40 | 8086 |
| 134 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +39 | 1642 |
| 135 | [openai/plugins](https://github.com/openai/plugins) | +39 | 4542 |
| 136 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +38 | 26225 |
| 137 | [lvy010/X-Plore](https://github.com/lvy010/X-Plore) | +38 | 1362 |
| 138 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +38 | 1893 |
| 139 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +37 | 17711 |
| 140 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +37 | 12272 |
| 141 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +36 | 4414 |
| 142 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +36 | 6151 |
| 143 | [openai/skills](https://github.com/openai/skills) | +35 | 23644 |
| 144 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +34 | 2844 |
| 145 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +33 | 4456 |
| 146 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +33 | 18302 |
| 147 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +33 | 3556 |
| 148 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +33 | 2073 |
| 149 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +32 | 2053 |
| 150 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +32 | 1948 |
| 151 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +31 | 15993 |
| 152 | [jundot/omlx](https://github.com/jundot/omlx) | +31 | 17806 |
| 153 | [lyra81604/zhengxi-views](https://github.com/lyra81604/zhengxi-views) | +30 | 1261 |
| 154 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +30 | 5379 |
| 155 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +29 | 1232 |
| 156 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +29 | 1113 |
| 157 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +29 | 3271 |
| 158 | [kairos-agi/kairos](https://github.com/kairos-agi/kairos) | +29 | 1519 |
| 159 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +29 | 26380 |
| 160 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +29 | 8369 |
| 161 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +28 | 1970 |
| 162 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +28 | 1296 |
| 163 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +27 | 8349 |
| 164 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +27 | 1638 |
| 165 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +27 | 5782 |
| 166 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +27 | 2473 |
| 167 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +27 | 634 |
| 168 | [floci-io/floci](https://github.com/floci-io/floci) | +27 | 16590 |
| 169 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +26 | 5036 |
| 170 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +26 | 26195 |
| 171 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +26 | 26687 |
| 172 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +26 | 15941 |
| 173 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15113 |
| 174 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +25 | 3562 |
| 175 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +25 | 18138 |
| 176 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +24 | 1001 |
| 177 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +24 | 1501 |
| 178 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +24 | 5221 |
| 179 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +24 | 4057 |
| 180 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +23 | 442 |
| 181 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1578 |
| 182 | [browser-act/skills](https://github.com/browser-act/skills) | +23 | 4358 |
| 183 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +23 | 8387 |
| 184 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +23 | 1859 |
| 185 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +23 | 5719 |
| 186 | [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) | +23 | 919 |
| 187 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +22 | 6830 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +21 | 6316 |
| 189 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +21 | 2345 |
| 190 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +20 | 8079 |
| 191 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +19 | 1211 |
| 192 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +19 | 7644 |
| 193 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7497 |
| 194 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +18 | 651 |
| 195 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +17 | 1198 |
| 196 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +17 | 1866 |
| 197 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +17 | 786 |
| 198 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +17 | 29025 |
| 199 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +17 | 1320 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +16 | 5334 |
| 201 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +16 | 2515 |
| 202 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +16 | 2484 |
| 203 | [kadevin/ilab-gpt-conjure](https://github.com/kadevin/ilab-gpt-conjure) | +16 | 625 |
| 204 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 387 |
| 205 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +15 | 2813 |
| 206 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +15 | 1437 |
| 207 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +14 | 4355 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +14 | 11804 |
| 209 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +14 | 518 |
| 210 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +14 | 8874 |
| 211 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 212 | [rpamis/comet](https://github.com/rpamis/comet) | +13 | 2239 |
| 213 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +13 | 329 |
| 214 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +13 | 449 |
| 215 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +13 | 486 |
| 216 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +12 | 681 |
| 217 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +12 | 14036 |
| 218 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +11 | 6065 |
| 219 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 686 |
| 220 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +11 | 793 |
| 221 | [buynao/aipath](https://github.com/buynao/aipath) | +11 | 480 |
| 222 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +11 | 8896 |
| 223 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 354 |
| 224 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +11 | 2839 |
| 225 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 947 |
| 226 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +10 | 608 |
| 227 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 350 |
| 228 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 426 |
| 229 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +10 | 5811 |
| 230 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 584 |
| 231 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +10 | 448 |
| 232 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 202 |
| 233 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +10 | 4441 |
| 234 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +10 | 2800 |
| 235 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +9 | 778 |
| 236 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +9 | 1946 |
| 237 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +9 | 2330 |
| 238 | [WhiteNightShadow/firefox-reverse](https://github.com/WhiteNightShadow/firefox-reverse) | +9 | 396 |
| 239 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +9 | 3124 |
| 240 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 0 |
| 241 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +8 | 781 |
| 242 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 373 |
| 243 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +8 | 4803 |
| 244 | [igoruehara/spec-driven](https://github.com/igoruehara/spec-driven) | +8 | 204 |
| 245 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +8 | 4994 |
| 246 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +8 | 4001 |
| 247 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 555 |
| 248 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 294 |
| 249 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 162 |
| 250 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 979 |
| 251 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +7 | 356 |
| 252 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 334 |
| 253 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +7 | 1729 |
| 254 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +7 | 872 |
| 255 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +7 | 245 |
| 256 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 454 |
| 257 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +6 | 1326 |
| 258 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +6 | 1544 |
| 259 | [akiralereal/iptv](https://github.com/akiralereal/iptv) | +6 | 337 |
| 260 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 538 |
| 261 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +6 | 3686 |
| 262 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 182 |
| 263 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +6 | 2812 |
| 264 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 353 |
| 265 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +5 | 1678 |
| 266 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 554 |
| 267 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +5 | 2567 |
| 268 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +5 | 90 |
| 269 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +5 | 319 |
| 270 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +5 | 1803 |
| 271 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +5 | 119 |
| 272 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2698 |
| 273 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 9503 |
| 274 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +4 | 2356 |
| 275 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 164 |
| 276 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +3 | 82 |
| 277 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +3 | 759 |
| 278 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 120 |
| 279 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 196 |
| 280 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +3 | 656 |
| 281 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +3 | 0 |
| 282 | [DuanYan007/markitdown](https://github.com/DuanYan007/markitdown) | +3 | 846 |
| 283 | [OrtonY/smart-resume](https://github.com/OrtonY/smart-resume) | +3 | 104 |
| 284 | [rrezartprebreza/spring-boot-skills](https://github.com/rrezartprebreza/spring-boot-skills) | +2 | 152 |
| 285 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 705 |
| 286 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 400 |
| 287 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +2 | 138 |
| 288 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 84 |
| 289 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 824 |
| 290 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1686 |
| 291 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 659 |
| 292 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +2 | 223 |
| 293 | [DitriXNew/EDT-MCP](https://github.com/DitriXNew/EDT-MCP) | +2 | 217 |
| 294 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 547 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +2 | 3364 |
| 296 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 297 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 93 |
| 298 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 419 |
| 299 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +2 | 852 |
| 300 | [LQF-dev/Zero-code](https://github.com/LQF-dev/Zero-code) | +2 | 64 |
