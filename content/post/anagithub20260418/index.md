---
title: "2026-04-18 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+595 2.evolver+235 3.PLFM_RADAR+223 4.smolvm+202 5.claude-mem+201"
date: 2026-04-18T20:39:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-18 20:39:49

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
        'daily': {"categories": ["Tracer-Cloud/opensre", "addyosmani/agent-skills", "google/magika", "BasedHardware/omi", "HKUDS/DeepTutor", "davebcn87/pi-autoresearch", "Donchitos/Claude-Code-Game-Studios", "Fincept-Corporation/FinceptTerminal", "Leonxlnx/taste-skill", "safishamsi/graphify", "jamiepine/voicebox", "multica-ai/multica", "lsdefine/GenericAgent", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "thedotmack/claude-mem", "smol-machines/smolvm", "NawfalMotii79/PLFM_RADAR", "EvoMap/evolver", "forrestchang/andrej-karpathy-skills"], "data": [87, 100, 108, 112, 113, 115, 118, 123, 126, 127, 133, 138, 159, 188, 191, 201, 202, 223, 235, 595]},
        'weekly': {"categories": ["virattt/ai-hedge-fund", "anthropics/skills", "rtk-ai/rtk", "addyosmani/agent-skills", "alchaincyf/nuwa-skill", "OpenBMB/VoxCPM", "garrytan/gstack", "garrytan/gbrain", "NawfalMotii79/PLFM_RADAR", "MemPalace/mempalace", "safishamsi/graphify", "affaan-m/everything-claude-code", "multica-ai/multica", "shanraisshan/claude-code-best-practice", "obra/superpowers", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [841, 865, 912, 917, 941, 996, 1002, 1168, 1236, 1310, 1579, 1644, 1694, 1729, 1898, 2230, 2589, 3533, 6204, 7841]},
        'monthly': {"categories": ["luongnv89/claude-howto", "siddharthvaddem/openscreen", "paperclipai/paperclip", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "safishamsi/graphify", "msitarzewski/agency-agents", "anthropics/claude-code", "karpathy/autoresearch", "JuliusBrussee/caveman", "chenglou/pretext", "openclaw/openclaw", "forrestchang/andrej-karpathy-skills", "MemPalace/mempalace", "garrytan/gstack", "obra/superpowers", "VoltAgent/awesome-design-md", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4024, 4282, 4396, 4425, 4717, 4984, 5026, 5315, 5521, 6334, 6748, 6969, 7025, 7540, 8564, 10274, 11069, 12287, 15480, 24864]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +595 | 57606 |
| 2 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +235 | 4936 |
| 3 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +223 | 14474 |
| 4 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +202 | 1684 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +201 | 30678 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +191 | 59270 |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +188 | 37735 |
| 8 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +159 | 4215 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | +138 | 16114 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +133 | 20473 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +127 | 29803 |
| 12 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +126 | 9880 |
| 13 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +123 | 4455 |
| 14 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +118 | 12565 |
| 15 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +115 | 5794 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +113 | 19656 |
| 17 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +112 | 10345 |
| 18 | [google/magika](https://github.com/google/magika) | +108 | 15847 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +100 | 17474 |
| 20 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +87 | 1674 |
| 21 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +83 | 36070 |
| 22 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +80 | 22245 |
| 23 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +78 | 46850 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +73 | 6210 |
| 25 | [JOYCEQL/magic-resume](https://github.com/JOYCEQL/magic-resume) | +72 | 6357 |
| 26 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +70 | 14519 |
| 27 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +69 | 1472 |
| 28 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +65 | 3072 |
| 29 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +65 | 29100 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +63 | 46205 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7841 | 99190 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6204 | 57606 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +3533 | 37735 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2589 | 59270 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2230 | 30678 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +1898 | 60312 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1729 | 46205 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1694 | 16114 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1644 | 51199 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1579 | 29803 |
| 11 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +1310 | 47827 |
| 12 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1236 | 14474 |
| 13 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1168 | 9141 |
| 14 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1002 | 76206 |
| 15 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +996 | 14519 |
| 16 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +941 | 12494 |
| 17 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +917 | 17474 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +912 | 29100 |
| 19 | [anthropics/skills](https://github.com/anthropics/skills) | +865 | 74774 |
| 20 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +841 | 45886 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +777 | 20473 |
| 22 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +756 | 6155 |
| 23 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +741 | 34148 |
| 24 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +698 | 55739 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +646 | 46850 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +642 | 54655 |
| 27 | [google/magika](https://github.com/google/magika) | +633 | 15847 |
| 28 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +610 | 19656 |
| 29 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +586 | 5204 |
| 30 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +566 | 18159 |
| 31 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +566 | 3651 |
| 32 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +561 | 31054 |
| 33 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +559 | 23993 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +539 | 11037 |
| 35 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +506 | 54626 |
| 36 | [coleam00/Archon](https://github.com/coleam00/Archon) | +491 | 18726 |
| 37 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +486 | 3706 |
| 38 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +485 | 33311 |
| 39 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +465 | 12565 |
| 40 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +463 | 3989 |
| 41 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +457 | 4936 |
| 42 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +457 | 4215 |
| 43 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +439 | 25078 |
| 44 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +430 | 27483 |
| 45 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +423 | 4787 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +419 | 37102 |
| 47 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +411 | 38236 |
| 48 | [pascalorg/editor](https://github.com/pascalorg/editor) | +399 | 13318 |
| 49 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +399 | 11902 |
| 50 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +388 | 29816 |
| 51 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +383 | 27085 |
| 52 | [snarktank/ralph](https://github.com/snarktank/ralph) | +383 | 17227 |
| 53 | [markdown-viewer/skills](https://github.com/markdown-viewer/skills) | +382 | 1857 |
| 54 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +379 | 14906 |
| 55 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +365 | 36070 |
| 56 | [mattpocock/skills](https://github.com/mattpocock/skills) | +357 | 16234 |
| 57 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +355 | 20467 |
| 58 | [tw93/Mole](https://github.com/tw93/Mole) | +349 | 36870 |
| 59 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +336 | 22582 |
| 60 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +331 | 5794 |
| 61 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +322 | 10345 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +322 | 13499 |
| 63 | [AgentSeal/codeburn](https://github.com/AgentSeal/codeburn) | +318 | 2699 |
| 64 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +297 | 40172 |
| 65 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +291 | 33825 |
| 66 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +289 | 37330 |
| 67 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +289 | 11170 |
| 68 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +283 | 27956 |
| 69 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +280 | 19888 |
| 70 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +280 | 24296 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +278 | 41047 |
| 72 | [chenglou/pretext](https://github.com/chenglou/pretext) | +276 | 44553 |
| 73 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +275 | 9881 |
| 74 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +274 | 37798 |
| 75 | [block/goose](https://github.com/block/goose) | +274 | 31098 |
| 76 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +266 | 2645 |
| 77 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +260 | 6210 |
| 78 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +258 | 1919 |
| 79 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +251 | 2679 |
| 80 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +249 | 39568 |
| 81 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +248 | 1991 |
| 82 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +247 | 1984 |
| 83 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +247 | 20031 |
| 84 | [tobi/qmd](https://github.com/tobi/qmd) | +246 | 22272 |
| 85 | [google-research/timesfm](https://github.com/google-research/timesfm) | +246 | 18080 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +245 | 21931 |
| 87 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +243 | 5482 |
| 88 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +238 | 15030 |
| 89 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +237 | 27526 |
| 90 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +232 | 1684 |
| 91 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +224 | 18236 |
| 92 | [jackwener/opencli](https://github.com/jackwener/opencli) | +223 | 16334 |
| 93 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +221 | 31413 |
| 94 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +217 | 4228 |
| 95 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +211 | 11755 |
| 96 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +210 | 30385 |
| 97 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +209 | 1904 |
| 98 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +197 | 48935 |
| 99 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +193 | 11296 |
| 100 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +192 | 22245 |
| 101 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +191 | 3738 |
| 102 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +188 | 3073 |
| 103 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +186 | 1446 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +184 | 11068 |
| 105 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +181 | 27515 |
| 106 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +180 | 16358 |
| 107 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +172 | 4455 |
| 108 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +172 | 3163 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +168 | 10631 |
| 110 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +163 | 21190 |
| 111 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +160 | 6274 |
| 112 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +159 | 1674 |
| 113 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +158 | 2208 |
| 114 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +155 | 1134 |
| 115 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +143 | 30335 |
| 116 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +143 | 3761 |
| 117 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +140 | 40001 |
| 118 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +138 | 33764 |
| 119 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +137 | 17790 |
| 120 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +131 | 39841 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24864 | 185987 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +15480 | 99190 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12287 | 51199 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11069 | 59270 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10274 | 60312 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +8564 | 76206 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7540 | 47827 |
| 8 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +7025 | 57606 |
| 9 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +6969 | 224760 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6748 | 44553 |
| 11 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +6334 | 37735 |
| 12 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +5521 | 74125 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5315 | 69674 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5026 | 82545 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4984 | 29804 |
| 16 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4717 | 62542 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4425 | 46205 |
| 18 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4396 | 55739 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4282 | 31054 |
| 20 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4024 | 27483 |
| 21 | [anthropics/skills](https://github.com/anthropics/skills) | +3850 | 74774 |
| 22 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3849 | 30678 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3844 | 23993 |
| 24 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3721 | 56080 |
| 25 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3632 | 109881 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3597 | 34148 |
| 27 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3583 | 54626 |
| 28 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3529 | 24296 |
| 29 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3392 | 54655 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3383 | 17474 |
| 31 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3182 | 30590 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3019 | 29816 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2955 | 29100 |
| 34 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2798 | 16114 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2797 | 46850 |
| 36 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2667 | 16226 |
| 37 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2665 | 85286 |
| 38 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2600 | 22582 |
| 39 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2584 | 18159 |
| 40 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2502 | 40172 |
| 41 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2489 | 16334 |
| 42 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2439 | 14906 |
| 43 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2396 | 29979 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2314 | 19888 |
| 45 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2296 | 15030 |
| 46 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2222 | 31413 |
| 47 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2159 | 12494 |
| 48 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2141 | 19425 |
| 49 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2134 | 16234 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2028 | 33878 |
| 51 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1963 | 27956 |
| 52 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1960 | 11902 |
| 53 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1932 | 37102 |
| 54 | [block/goose](https://github.com/block/goose) | +1874 | 31098 |
| 55 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1853 | 27515 |
| 56 | [github/spec-kit](https://github.com/github/spec-kit) | +1849 | 71722 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1819 | 9141 |
| 58 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1811 | 13318 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1781 | 25078 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1767 | 11037 |
| 61 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1763 | 9745 |
| 62 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1720 | 12565 |
| 63 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1711 | 79656 |
| 64 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1676 | 10825 |
| 65 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1669 | 39568 |
| 66 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1643 | 32310 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1633 | 20467 |
| 68 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1622 | 19656 |
| 69 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1589 | 13860 |
| 70 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1588 | 15922 |
| 71 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1585 | 27085 |
| 72 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1569 | 14519 |
| 73 | [openai/codex](https://github.com/openai/codex) | +1495 | 61744 |
| 74 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1491 | 48935 |
| 75 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1464 | 37330 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1458 | 41047 |
| 77 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1448 | 38236 |
| 78 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1410 | 47071 |
| 79 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1409 | 11675 |
| 80 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1364 | 18080 |
| 81 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1361 | 33825 |
| 82 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1358 | 98536 |
| 83 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1355 | 73135 |
| 84 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1343 | 6155 |
| 85 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1318 | 6693 |
| 86 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1315 | 46498 |
| 87 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1314 | 14474 |
| 88 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1308 | 17790 |
| 89 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1302 | 78902 |
| 90 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1264 | 30385 |
| 91 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1236 | 21468 |
| 92 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1197 | 21931 |
| 93 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1182 | 52700 |
| 94 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1175 | 45886 |
| 95 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1150 | 21190 |
| 96 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1147 | 22518 |
| 97 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1139 | 5751 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1137 | 13499 |
| 99 | [tobi/qmd](https://github.com/tobi/qmd) | +1083 | 22272 |
| 100 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1075 | 37798 |
| 101 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1072 | 95754 |
| 102 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +991 | 20473 |
| 103 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +984 | 6214 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +959 | 11755 |
| 105 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +943 | 8926 |
| 106 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +937 | 11340 |
| 107 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +919 | 40001 |
| 108 | [coleam00/Archon](https://github.com/coleam00/Archon) | +914 | 18726 |
| 109 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +905 | 49621 |
| 110 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +883 | 39841 |
| 111 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +882 | 24243 |
| 112 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +874 | 6345 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +859 | 11068 |
| 114 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +849 | 5426 |
| 115 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +839 | 11296 |
| 116 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +837 | 5204 |
| 117 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +817 | 17258 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +812 | 9597 |
| 119 | [jundot/omlx](https://github.com/jundot/omlx) | +809 | 10631 |
| 120 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +801 | 4611 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +795 | 23994 |
| 122 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +795 | 8878 |
| 123 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +758 | 33764 |
| 124 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +757 | 6975 |
| 125 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +741 | 5559 |
| 126 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +731 | 9439 |
| 127 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +720 | 3761 |
| 128 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +717 | 30195 |
| 129 | [cft0808/edict](https://github.com/cft0808/edict) | +704 | 15276 |
| 130 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +701 | 30335 |
| 131 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +693 | 3651 |
| 132 | [eze-is/web-access](https://github.com/eze-is/web-access) | +693 | 5240 |
| 133 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +688 | 4841 |
| 134 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +670 | 6210 |
| 135 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +664 | 3692 |
| 136 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +655 | 36799 |
| 137 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +650 | 54903 |
| 138 | [google/magika](https://github.com/google/magika) | +644 | 15847 |
| 139 | [floci-io/floci](https://github.com/floci-io/floci) | +636 | 3948 |
| 140 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +615 | 37564 |
| 141 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +612 | 3171 |
| 142 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +606 | 9585 |
| 143 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +597 | 3738 |
| 144 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +574 | 11476 |
| 145 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +568 | 25466 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +567 | 18790 |
| 147 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +560 | 47936 |
| 148 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +550 | 19553 |
| 149 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +515 | 38403 |
| 150 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +515 | 12960 |
| 151 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +514 | 16542 |
| 152 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +504 | 2424 |
| 153 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +499 | 2665 |
| 154 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +498 | 3065 |
| 155 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +496 | 15585 |
| 156 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +493 | 29592 |
| 157 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +492 | 11170 |
| 158 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +491 | 6274 |
| 159 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +488 | 3163 |
| 160 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +487 | 4215 |
| 161 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +470 | 4937 |
| 162 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +469 | 2679 |
| 163 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +464 | 4414 |
| 164 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +462 | 3198 |
| 165 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +460 | 4228 |
| 166 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +458 | 5147 |
| 167 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +456 | 19035 |
| 168 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +454 | 2645 |
| 169 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +454 | 44545 |
| 170 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +450 | 5995 |
| 171 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +449 | 5220 |
| 172 | [usestrix/strix](https://github.com/usestrix/strix) | +435 | 24183 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +424 | 9089 |
| 174 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +422 | 18973 |
| 175 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +412 | 20031 |
| 176 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +407 | 2940 |
| 177 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +390 | 2791 |
| 178 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +379 | 4182 |
| 179 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +378 | 2022 |
| 180 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +378 | 7791 |
| 181 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +374 | 1919 |
| 182 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +371 | 25323 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +358 | 12083 |
| 184 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +354 | 1951 |
| 185 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +348 | 1984 |
| 186 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +345 | 2957 |
| 187 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +342 | 2225 |
| 188 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +337 | 2757 |
| 189 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +331 | 23550 |
| 190 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +331 | 2642 |
| 191 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +317 | 3037 |
| 192 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +304 | 5374 |
| 193 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +277 | 3044 |
| 194 | [decolua/9router](https://github.com/decolua/9router) | +268 | 2651 |
| 195 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +263 | 7038 |
| 196 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +261 | 36103 |
| 197 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +260 | 5874 |
| 198 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +236 | 11150 |
| 199 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +227 | 9439 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +223 | 6180 |
| 201 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +218 | 25870 |
| 202 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +215 | 1374 |
| 203 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +215 | 2432 |
| 204 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +210 | 6376 |
| 205 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +201 | 943 |
| 206 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +201 | 2713 |
| 207 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +200 | 1492 |
| 208 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +199 | 15614 |
| 209 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +197 | 3587 |
| 210 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +194 | 1067 |
| 211 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +187 | 3003 |
| 212 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +187 | 33712 |
| 213 | [usebruno/bruno](https://github.com/usebruno/bruno) | +186 | 41086 |
| 214 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +185 | 582 |
| 215 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +178 | 23686 |
| 216 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +171 | 2387 |
| 217 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 786 |
| 218 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +159 | 1789 |
| 219 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +152 | 3868 |
| 220 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +142 | 35473 |
| 222 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +141 | 22178 |
| 223 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +137 | 1410 |
| 224 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 961 |
| 225 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +133 | 1601 |
| 226 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +128 | 840 |
| 227 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +123 | 947 |
| 228 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 828 |
| 229 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +117 | 805 |
| 230 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +117 | 972 |
| 231 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +117 | 5288 |
| 232 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +117 | 10775 |
| 233 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29625 |
| 234 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +115 | 1084 |
| 235 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +113 | 29626 |
| 236 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +111 | 23392 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +108 | 26589 |
| 238 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +108 | 1704 |
| 239 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +106 | 12760 |
| 240 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +105 | 1321 |
| 241 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +104 | 1828 |
| 242 | [clawplays/ospec](https://github.com/clawplays/ospec) | +102 | 554 |
| 243 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +102 | 578 |
| 244 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +99 | 783 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +98 | 33000 |
| 246 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 247 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +96 | 48784 |
| 248 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +94 | 593 |
| 249 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +93 | 3718 |
| 250 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +92 | 1327 |
| 251 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +92 | 0 |
| 252 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +91 | 1177 |
| 253 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +89 | 3973 |
| 254 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +88 | 1922 |
| 255 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +88 | 594 |
| 256 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +88 | 2639 |
| 257 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +88 | 554 |
| 258 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +87 | 1124 |
| 259 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +86 | 2226 |
| 260 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3241 |
| 261 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +85 | 588 |
| 262 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +83 | 789 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +81 | 1037 |
| 264 | [openmemind/memind](https://github.com/openmemind/memind) | +80 | 448 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1629 |
| 266 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +79 | 3599 |
| 267 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +78 | 6624 |
| 268 | [microg/GmsCore](https://github.com/microg/GmsCore) | +78 | 12972 |
| 269 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 1966 |
| 270 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +75 | 7053 |
| 271 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +74 | 631 |
| 272 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +73 | 359 |
| 273 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +73 | 3730 |
| 274 | [88lin/video_vip](https://github.com/88lin/video_vip) | +72 | 717 |
| 275 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +72 | 45263 |
| 276 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +70 | 731 |
| 277 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +70 | 4047 |
| 278 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +69 | 389 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9296 |
| 280 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +65 | 464 |
| 281 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +65 | 1396 |
| 282 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +65 | 27286 |
| 283 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +64 | 570 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +63 | 7274 |
| 285 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +63 | 785 |
| 286 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +63 | 11659 |
| 287 | [idinging/freemail](https://github.com/idinging/freemail) | +61 | 1367 |
| 288 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +61 | 381 |
| 289 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +59 | 308 |
| 290 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1617 |
| 291 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +57 | 37313 |
| 292 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +56 | 25427 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +54 | 31476 |
| 294 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +51 | 1802 |
| 295 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +51 | 28954 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1721 |
| 297 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +48 | 11651 |
| 298 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +44 | 8521 |
| 299 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1688 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +37 | 122 |
