---
title: "2026-04-19 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+915 2.awesome-design-md+344 3.FinceptTerminal+335 4.PLFM_RADAR+328 5.CL4R1T4S+288"
date: 2026-04-19T20:40:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-19 20:40:49

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
        'daily': {"categories": ["addyosmani/agent-skills", "HKUDS/DeepTutor", "Leonxlnx/taste-skill", "EvoMap/evolver", "thunderbird/thunderbolt", "jamiepine/voicebox", "multica-ai/multica", "BasedHardware/omi", "smol-machines/smolvm", "webadderall/Recordly", "openai/openai-agents-python", "rtk-ai/rtk", "Donchitos/Claude-Code-Game-Studios", "safishamsi/graphify", "JuliusBrussee/caveman", "elder-plinius/CL4R1T4S", "NawfalMotii79/PLFM_RADAR", "Fincept-Corporation/FinceptTerminal", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills"], "data": [139, 146, 149, 167, 174, 175, 175, 176, 179, 185, 189, 191, 192, 217, 264, 288, 328, 335, 344, 915]},
        'weekly': {"categories": ["alchaincyf/nuwa-skill", "garrytan/gbrain", "virattt/ai-hedge-fund", "OpenBMB/VoxCPM", "shiyu-coder/Kronos", "rtk-ai/rtk", "addyosmani/agent-skills", "jamiepine/voicebox", "MemPalace/mempalace", "garrytan/gstack", "safishamsi/graphify", "multica-ai/multica", "shanraisshan/claude-code-best-practice", "NawfalMotii79/PLFM_RADAR", "obra/superpowers", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [705, 712, 713, 784, 792, 794, 830, 836, 923, 1186, 1282, 1314, 1386, 1546, 1857, 2312, 2366, 2545, 6451, 6470]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "paperclipai/paperclip", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "safishamsi/graphify", "msitarzewski/agency-agents", "anthropics/claude-code", "karpathy/autoresearch", "JuliusBrussee/caveman", "santifer/career-ops", "chenglou/pretext", "openclaw/openclaw", "forrestchang/andrej-karpathy-skills", "MemPalace/mempalace", "garrytan/gstack", "obra/superpowers", "VoltAgent/awesome-design-md", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4282, 4396, 4425, 4717, 4984, 5026, 5315, 5521, 6334, 6610, 6748, 6969, 7025, 7540, 8564, 10274, 11069, 12287, 15480, 24864]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +915 | 60963 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +344 | 60318 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +335 | 6219 |
| 4 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +328 | 15943 |
| 5 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +288 | 16085 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +264 | 38827 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +217 | 30545 |
| 8 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +192 | 13287 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +191 | 29935 |
| 10 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +189 | 23062 |
| 11 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +185 | 9374 |
| 12 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +179 | 2024 |
| 13 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +176 | 11054 |
| 14 | [multica-ai/multica](https://github.com/multica-ai/multica) | +175 | 16690 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +175 | 21090 |
| 16 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +174 | 2132 |
| 17 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +167 | 5453 |
| 18 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +149 | 10235 |
| 19 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +146 | 20085 |
| 20 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +139 | 17859 |
| 21 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +138 | 2029 |
| 22 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +118 | 3536 |
| 23 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +109 | 6948 |
| 24 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +108 | 15384 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +108 | 6458 |
| 26 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +99 | 14818 |
| 27 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +94 | 11377 |
| 28 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +91 | 4504 |
| 29 | [mnfst/manifest](https://github.com/mnfst/manifest) | +90 | 5021 |
| 30 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +89 | 36907 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6470 | 60963 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +6451 | 101836 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2545 | 38827 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2366 | 60318 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2312 | 30678 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +1857 | 60312 |
| 7 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1546 | 15943 |
| 8 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1386 | 46540 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1314 | 16690 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1282 | 30545 |
| 11 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1186 | 77361 |
| 12 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +923 | 48094 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +836 | 21090 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +830 | 17859 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +794 | 29935 |
| 16 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +792 | 19569 |
| 17 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +784 | 14818 |
| 18 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +713 | 45886 |
| 19 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +712 | 9371 |
| 20 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +705 | 12773 |
| 21 | [google/magika](https://github.com/google/magika) | +700 | 16060 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +663 | 34148 |
| 23 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +650 | 56268 |
| 24 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +623 | 13288 |
| 25 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +597 | 5360 |
| 26 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +596 | 5453 |
| 27 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +586 | 47198 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +555 | 54935 |
| 29 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +532 | 4504 |
| 30 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +516 | 3813 |
| 31 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +506 | 20085 |
| 32 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +489 | 11054 |
| 33 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +479 | 6219 |
| 34 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +477 | 24245 |
| 35 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +476 | 33311 |
| 36 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +467 | 54803 |
| 37 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +450 | 31315 |
| 38 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +442 | 11377 |
| 39 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +421 | 38487 |
| 40 | [pascalorg/editor](https://github.com/pascalorg/editor) | +411 | 13514 |
| 41 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +407 | 37421 |
| 42 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +407 | 25329 |
| 43 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +394 | 18274 |
| 44 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +394 | 3723 |
| 45 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +385 | 10235 |
| 46 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +379 | 2024 |
| 47 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +377 | 16085 |
| 48 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +369 | 23062 |
| 49 | [coleam00/Archon](https://github.com/coleam00/Archon) | +364 | 18919 |
| 50 | [AgentSeal/codeburn](https://github.com/AgentSeal/codeburn) | +362 | 2840 |
| 51 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +355 | 27647 |
| 52 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +351 | 5867 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +350 | 27261 |
| 54 | [mattpocock/skills](https://github.com/mattpocock/skills) | +344 | 16431 |
| 55 | [tw93/Mole](https://github.com/tw93/Mole) | +332 | 36870 |
| 56 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +330 | 30018 |
| 57 | [snarktank/ralph](https://github.com/snarktank/ralph) | +326 | 17355 |
| 58 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +324 | 2029 |
| 59 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +324 | 36187 |
| 60 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +323 | 4079 |
| 61 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +318 | 20661 |
| 62 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +317 | 15248 |
| 63 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +311 | 22677 |
| 64 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +311 | 13688 |
| 65 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +308 | 2132 |
| 66 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +308 | 6458 |
| 67 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +305 | 3536 |
| 68 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +299 | 22737 |
| 69 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +292 | 4987 |
| 70 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +291 | 11201 |
| 71 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +282 | 37330 |
| 72 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +281 | 9374 |
| 73 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +280 | 33978 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +271 | 41219 |
| 75 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +270 | 2064 |
| 76 | [block/goose](https://github.com/block/goose) | +253 | 31098 |
| 77 | [chenglou/pretext](https://github.com/chenglou/pretext) | +252 | 44673 |
| 78 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +250 | 19978 |
| 79 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +244 | 49288 |
| 80 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +242 | 40315 |
| 81 | [google-research/timesfm](https://github.com/google-research/timesfm) | +242 | 18152 |
| 82 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +241 | 39736 |
| 83 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +239 | 31636 |
| 84 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +235 | 11966 |
| 85 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +233 | 37921 |
| 86 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +230 | 11934 |
| 87 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +230 | 27657 |
| 88 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +226 | 15144 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +225 | 22162 |
| 90 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +224 | 2813 |
| 91 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +216 | 18404 |
| 92 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +213 | 2074 |
| 93 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +211 | 15384 |
| 94 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +203 | 2722 |
| 95 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +201 | 1393 |
| 96 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +198 | 20095 |
| 97 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +196 | 3886 |
| 98 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +196 | 1798 |
| 99 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +192 | 1257 |
| 100 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +189 | 1862 |
| 101 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +187 | 16461 |
| 102 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +184 | 30510 |
| 103 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +177 | 39841 |
| 104 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +176 | 11478 |
| 105 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +176 | 27649 |
| 106 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +171 | 6948 |
| 107 | [jundot/omlx](https://github.com/jundot/omlx) | +166 | 10741 |
| 108 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +163 | 1947 |
| 109 | [patterniha/SNI-Spoofing](https://github.com/patterniha/SNI-Spoofing) | +161 | 1097 |
| 110 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +159 | 2288 |
| 111 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +154 | 21269 |
| 112 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +154 | 1921 |
| 113 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +152 | 40093 |
| 114 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +149 | 6461 |
| 115 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +146 | 33831 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +144 | 9744 |
| 117 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +140 | 11164 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +133 | 36799 |
| 119 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +132 | 1443 |
| 120 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +132 | 30431 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24864 | 186291 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +15480 | 101836 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12287 | 51199 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11069 | 60318 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10274 | 60312 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +8564 | 77361 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7540 | 48094 |
| 8 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +7025 | 60963 |
| 9 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +6969 | 224760 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6748 | 44673 |
| 11 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6610 | 36448 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +6334 | 38827 |
| 13 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +5521 | 74494 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5315 | 69674 |
| 15 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5026 | 83292 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4984 | 30545 |
| 17 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4717 | 62714 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4425 | 46540 |
| 19 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4396 | 56268 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4282 | 31315 |
| 21 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4024 | 27647 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +3850 | 74774 |
| 23 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3849 | 30678 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3844 | 24245 |
| 25 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3721 | 56276 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3632 | 109881 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3597 | 34148 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3583 | 54803 |
| 29 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3529 | 24453 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3392 | 54935 |
| 31 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3383 | 17859 |
| 32 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3182 | 30590 |
| 33 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3019 | 30018 |
| 34 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2955 | 29935 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2798 | 16690 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2797 | 47198 |
| 37 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2667 | 16351 |
| 38 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2665 | 85286 |
| 39 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2600 | 22737 |
| 40 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2584 | 18274 |
| 41 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2502 | 40315 |
| 42 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2489 | 16437 |
| 43 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2439 | 15248 |
| 44 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2396 | 30091 |
| 45 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2314 | 19978 |
| 46 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2296 | 15144 |
| 47 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2222 | 31636 |
| 48 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2159 | 12773 |
| 49 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2141 | 19479 |
| 50 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2134 | 16431 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2028 | 33878 |
| 52 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1963 | 28030 |
| 53 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1960 | 11966 |
| 54 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1932 | 37421 |
| 55 | [block/goose](https://github.com/block/goose) | +1874 | 31098 |
| 56 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1853 | 27649 |
| 57 | [github/spec-kit](https://github.com/github/spec-kit) | +1849 | 71722 |
| 58 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1819 | 9371 |
| 59 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1811 | 13514 |
| 60 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1781 | 25329 |
| 61 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1767 | 11377 |
| 62 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1763 | 9795 |
| 63 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1720 | 13288 |
| 64 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1711 | 79656 |
| 65 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1676 | 10883 |
| 66 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1669 | 39736 |
| 67 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1643 | 32429 |
| 68 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1633 | 20661 |
| 69 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1622 | 20085 |
| 70 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1589 | 13900 |
| 71 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +1588 | 15985 |
| 72 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1585 | 27261 |
| 73 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1575 | 19569 |
| 74 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1569 | 14818 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1495 | 61744 |
| 76 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1491 | 49288 |
| 77 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1464 | 37330 |
| 78 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1458 | 41219 |
| 79 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1448 | 38487 |
| 80 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1410 | 47413 |
| 81 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1409 | 11684 |
| 82 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1364 | 18152 |
| 83 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1361 | 33978 |
| 84 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1358 | 98536 |
| 85 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1355 | 73135 |
| 86 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1343 | 6186 |
| 87 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1318 | 6694 |
| 88 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1315 | 46614 |
| 89 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1314 | 15943 |
| 90 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1308 | 17836 |
| 91 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1302 | 78902 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1264 | 30510 |
| 93 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1236 | 21567 |
| 94 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1197 | 22162 |
| 95 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1175 | 45886 |
| 96 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1139 | 5763 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1137 | 13688 |
| 98 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1095 | 22583 |
| 99 | [tobi/qmd](https://github.com/tobi/qmd) | +1083 | 22412 |
| 100 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1079 | 37921 |
| 101 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1072 | 95754 |
| 102 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1067 | 21269 |
| 103 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1029 | 52700 |
| 104 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +991 | 21091 |
| 105 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +984 | 6948 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +984 | 11934 |
| 107 | [coleam00/Archon](https://github.com/coleam00/Archon) | +965 | 18919 |
| 108 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +944 | 39841 |
| 109 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +943 | 8940 |
| 110 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +916 | 49621 |
| 111 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +898 | 40093 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +883 | 24298 |
| 113 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +880 | 5360 |
| 114 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +880 | 6362 |
| 115 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +871 | 5487 |
| 116 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +870 | 11164 |
| 117 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +853 | 11478 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +828 | 9744 |
| 119 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +818 | 11392 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +813 | 17316 |
| 121 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +806 | 4630 |
| 122 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +806 | 24043 |
| 123 | [jundot/omlx](https://github.com/jundot/omlx) | +796 | 10741 |
| 124 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +779 | 33831 |
| 125 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +753 | 6458 |
| 126 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +745 | 5565 |
| 127 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +740 | 3819 |
| 128 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +736 | 9466 |
| 129 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +719 | 7026 |
| 130 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +716 | 3925 |
| 131 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +715 | 3723 |
| 132 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +713 | 30266 |
| 133 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +706 | 30431 |
| 134 | [eze-is/web-access](https://github.com/eze-is/web-access) | +706 | 5303 |
| 135 | [google/magika](https://github.com/google/magika) | +704 | 16060 |
| 136 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +680 | 3767 |
| 137 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +676 | 54903 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +672 | 36799 |
| 139 | [floci-io/floci](https://github.com/floci-io/floci) | +640 | 3967 |
| 140 | [cft0808/edict](https://github.com/cft0808/edict) | +637 | 15294 |
| 141 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +634 | 8902 |
| 142 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +632 | 3886 |
| 143 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +623 | 5453 |
| 144 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +615 | 37564 |
| 145 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +590 | 4858 |
| 146 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +587 | 3189 |
| 147 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +579 | 11486 |
| 148 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +572 | 18886 |
| 149 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +569 | 4504 |
| 150 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +566 | 47936 |
| 151 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +558 | 25494 |
| 152 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +530 | 19597 |
| 153 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +525 | 6461 |
| 154 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +523 | 16606 |
| 155 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +509 | 2440 |
| 156 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +508 | 2813 |
| 157 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +502 | 6220 |
| 158 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +502 | 3090 |
| 159 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +501 | 3200 |
| 160 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +500 | 2680 |
| 161 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +494 | 2778 |
| 162 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +490 | 29658 |
| 163 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +489 | 15625 |
| 164 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +482 | 23062 |
| 165 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +480 | 11201 |
| 166 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +473 | 38414 |
| 167 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +472 | 2722 |
| 168 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +472 | 5270 |
| 169 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +467 | 4421 |
| 170 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +463 | 4252 |
| 171 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +461 | 44545 |
| 172 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +461 | 3222 |
| 173 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +451 | 19094 |
| 174 | [usestrix/strix](https://github.com/usestrix/strix) | +439 | 24222 |
| 175 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +439 | 19064 |
| 176 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +439 | 12972 |
| 177 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +426 | 20095 |
| 178 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +425 | 9127 |
| 179 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +415 | 3073 |
| 180 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +405 | 2094 |
| 181 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +392 | 2791 |
| 182 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +376 | 1992 |
| 183 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +375 | 2074 |
| 184 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +374 | 1921 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +369 | 12140 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +360 | 25359 |
| 187 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +355 | 2591 |
| 188 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +351 | 23614 |
| 189 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +349 | 2796 |
| 190 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +323 | 7814 |
| 191 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +319 | 3060 |
| 192 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +313 | 2666 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +307 | 5411 |
| 194 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +306 | 2994 |
| 195 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +283 | 4196 |
| 196 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +278 | 3052 |
| 197 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +275 | 36103 |
| 198 | [decolua/9router](https://github.com/decolua/9router) | +270 | 2691 |
| 199 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +269 | 5902 |
| 200 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +236 | 7073 |
| 201 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +235 | 1427 |
| 202 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +230 | 11170 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +227 | 6185 |
| 204 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +225 | 9450 |
| 205 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +223 | 25907 |
| 206 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +209 | 6389 |
| 207 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +207 | 1506 |
| 208 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +205 | 15641 |
| 209 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +204 | 2439 |
| 210 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +202 | 3602 |
| 211 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +199 | 946 |
| 212 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +191 | 33712 |
| 213 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +189 | 584 |
| 214 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +188 | 3011 |
| 215 | [usebruno/bruno](https://github.com/usebruno/bruno) | +185 | 41086 |
| 216 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +181 | 1067 |
| 217 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +178 | 23699 |
| 218 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +175 | 2424 |
| 219 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +172 | 2718 |
| 220 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 787 |
| 221 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +153 | 3879 |
| 222 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +150 | 40265 |
| 223 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +148 | 1794 |
| 224 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +146 | 22212 |
| 225 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +141 | 1421 |
| 226 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +140 | 35473 |
| 227 | [dashersw/gea](https://github.com/dashersw/gea) | +135 | 961 |
| 228 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +132 | 837 |
| 229 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +130 | 1617 |
| 230 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +123 | 29651 |
| 231 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 834 |
| 232 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +119 | 29639 |
| 233 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +117 | 5309 |
| 234 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +117 | 10794 |
| 235 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +115 | 1085 |
| 236 | [88lin/video_vip](https://github.com/88lin/video_vip) | +111 | 1095 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +109 | 12774 |
| 238 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +109 | 23405 |
| 239 | [clawplays/ospec](https://github.com/clawplays/ospec) | +108 | 569 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +108 | 26594 |
| 241 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +107 | 1329 |
| 242 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +106 | 984 |
| 243 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +106 | 1842 |
| 244 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +105 | 951 |
| 245 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +104 | 588 |
| 246 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +104 | 1720 |
| 247 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +98 | 1960 |
| 248 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +98 | 33000 |
| 249 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +97 | 6655 |
| 250 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 251 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +96 | 1182 |
| 252 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +94 | 1340 |
| 253 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +94 | 48784 |
| 254 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +93 | 608 |
| 255 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +90 | 1135 |
| 256 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +89 | 557 |
| 257 | [crimera/piko](https://github.com/crimera/piko) | +88 | 3256 |
| 258 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +86 | 7078 |
| 259 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +86 | 595 |
| 260 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +86 | 601 |
| 261 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +86 | 2648 |
| 262 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +85 | 3984 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +85 | 1052 |
| 264 | [openmemind/memind](https://github.com/openmemind/memind) | +85 | 459 |
| 265 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +84 | 791 |
| 266 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +84 | 2242 |
| 267 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +81 | 659 |
| 268 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +81 | 3606 |
| 269 | [robinebers/openusage](https://github.com/robinebers/openusage) | +79 | 1972 |
| 270 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1644 |
| 271 | [microg/GmsCore](https://github.com/microg/GmsCore) | +79 | 12978 |
| 272 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +78 | 890 |
| 273 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +76 | 45263 |
| 274 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +75 | 420 |
| 275 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +75 | 362 |
| 276 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +74 | 3748 |
| 277 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +72 | 801 |
| 278 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +71 | 413 |
| 279 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +71 | 803 |
| 280 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +67 | 471 |
| 281 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9310 |
| 282 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +67 | 27302 |
| 283 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +66 | 1405 |
| 284 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +65 | 584 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7278 |
| 286 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +62 | 1625 |
| 287 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +62 | 11667 |
| 288 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +61 | 311 |
| 289 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +61 | 37313 |
| 290 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +59 | 427 |
| 291 | [idinging/freemail](https://github.com/idinging/freemail) | +58 | 1375 |
| 292 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +57 | 25428 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +54 | 31476 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +52 | 28960 |
| 295 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +50 | 1730 |
| 296 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +49 | 1809 |
| 297 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +47 | 11654 |
| 298 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +44 | 8531 |
| 299 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1687 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +37 | 122 |
