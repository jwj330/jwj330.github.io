---
title: "2026-04-23 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+457 2.CL4R1T4S+266 3.free-claude-code+218 4.FinceptTerminal+149 5.claude-context+125"
date: 2026-04-23T20:55:33+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-23 20:55:33

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
        'daily': {"categories": ["HKUDS/RAG-Anything", "open-metadata/OpenMetadata", "YouMind-OpenLab/awesome-gpt-image-2", "vercel-labs/skills", "farion1231/cc-switch", "multica-ai/multica", "KeygraphHQ/shannon", "safishamsi/graphify", "VoltAgent/awesome-design-md", "TencentCloud/CubeSandbox", "addyosmani/agent-skills", "rtk-ai/rtk", "koala73/worldmonitor", "JuliusBrussee/caveman", "AIDC-AI/Pixelle-Video", "zilliztech/claude-context", "Fincept-Corporation/FinceptTerminal", "Alishahryar1/free-claude-code", "elder-plinius/CL4R1T4S", "forrestchang/andrej-karpathy-skills"], "data": [62, 68, 69, 70, 73, 85, 87, 88, 88, 89, 102, 105, 112, 116, 118, 125, 149, 218, 266, 457]},
        'weekly': {"categories": ["thunderbird/thunderbolt", "BasedHardware/omi", "santifer/career-ops", "EvoMap/evolver", "jamiepine/voicebox", "openai/openai-agents-python", "addyosmani/agent-skills", "Donchitos/Claude-Code-Game-Studios", "rtk-ai/rtk", "multica-ai/multica", "safishamsi/graphify", "garrytan/gstack", "thedotmack/claude-mem", "NawfalMotii79/PLFM_RADAR", "VoltAgent/awesome-design-md", "elder-plinius/CL4R1T4S", "JuliusBrussee/caveman", "Fincept-Corporation/FinceptTerminal", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [610, 631, 649, 659, 665, 673, 738, 771, 790, 887, 909, 1195, 1288, 1303, 1382, 1434, 1448, 1748, 3225, 4848]},
        'monthly': {"categories": ["paperclipai/paperclip", "shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "anthropics/claude-code", "openclaw/openclaw", "safishamsi/graphify", "garrytan/gstack", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "affaan-m/everything-claude-code", "forrestchang/andrej-karpathy-skills", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4160, 4174, 4219, 4287, 4450, 4593, 5205, 5570, 5658, 6118, 6860, 6974, 7369, 7780, 9048, 10003, 10488, 11947, 17468, 25218]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +457 | 80119 |
| 2 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +266 | 25289 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +218 | 5311 |
| 4 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +149 | 13867 |
| 5 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +125 | 8335 |
| 6 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +118 | 6301 |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +116 | 44675 |
| 8 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +112 | 52234 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +105 | 33399 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +102 | 21851 |
| 11 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +89 | 3237 |
| 12 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +88 | 64072 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +88 | 33710 |
| 14 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +87 | 40027 |
| 15 | [multica-ai/multica](https://github.com/multica-ai/multica) | +85 | 20123 |
| 16 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +73 | 49824 |
| 17 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +70 | 15819 |
| 18 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +69 | 941 |
| 19 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +68 | 12887 |
| 20 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +62 | 18082 |
| 21 | [langfuse/langfuse](https://github.com/langfuse/langfuse) | +62 | 25923 |
| 22 | [google/osv-scanner](https://github.com/google/osv-scanner) | +57 | 9133 |
| 23 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +52 | 39117 |
| 24 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +52 | 10771 |
| 25 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +51 | 3801 |
| 26 | [iamzhihuix/skills-manage](https://github.com/iamzhihuix/skills-manage) | +51 | 869 |
| 27 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +51 | 23974 |
| 28 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +49 | 20822 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +47 | 40064 |
| 30 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +43 | 49761 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4848 | 80119 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3225 | 112971 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1748 | 13867 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1448 | 44675 |
| 5 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1434 | 25289 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1382 | 64072 |
| 7 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1303 | 17789 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1288 | 30678 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1195 | 81397 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +909 | 33710 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +887 | 20123 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +790 | 33399 |
| 13 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +771 | 15745 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +738 | 21851 |
| 15 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +673 | 24841 |
| 16 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +665 | 22763 |
| 17 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +659 | 6670 |
| 18 | [santifer/career-ops](https://github.com/santifer/career-ops) | +649 | 38877 |
| 19 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +631 | 12087 |
| 20 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +610 | 3864 |
| 21 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +586 | 6304 |
| 22 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +556 | 12215 |
| 23 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +545 | 49824 |
| 24 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +522 | 52234 |
| 25 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +461 | 21184 |
| 26 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +444 | 10347 |
| 27 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +443 | 4727 |
| 28 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +423 | 49761 |
| 29 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +419 | 2531 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +418 | 39117 |
| 31 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +402 | 14233 |
| 32 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +377 | 8277 |
| 33 | [google/magika](https://github.com/google/magika) | +371 | 16536 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +364 | 40064 |
| 35 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +355 | 47640 |
| 36 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +352 | 12757 |
| 37 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +345 | 49240 |
| 38 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +337 | 15717 |
| 39 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +328 | 20822 |
| 40 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +327 | 7471 |
| 41 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +318 | 10771 |
| 42 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +316 | 32388 |
| 43 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +307 | 25321 |
| 44 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +306 | 36907 |
| 45 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +305 | 2340 |
| 46 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +303 | 23974 |
| 47 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +302 | 3237 |
| 48 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +297 | 55967 |
| 49 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +286 | 4855 |
| 50 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +282 | 16393 |
| 51 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +277 | 28198 |
| 52 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +274 | 42515 |
| 53 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +274 | 26114 |
| 54 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +270 | 9354 |
| 55 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +267 | 6301 |
| 56 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +263 | 1914 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +254 | 14824 |
| 58 | [PerryTS/perry](https://github.com/PerryTS/perry) | +254 | 1643 |
| 59 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +253 | 8335 |
| 60 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +250 | 23732 |
| 61 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +250 | 16161 |
| 62 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +249 | 21539 |
| 63 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | +246 | 1565 |
| 64 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +244 | 32359 |
| 65 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +243 | 18082 |
| 66 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +241 | 5311 |
| 67 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +241 | 37330 |
| 68 | [android/skills](https://github.com/android/skills) | +241 | 4211 |
| 69 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +240 | 32836 |
| 70 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +238 | 2640 |
| 71 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +238 | 36912 |
| 72 | [mnfst/manifest](https://github.com/mnfst/manifest) | +237 | 5586 |
| 73 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +236 | 17947 |
| 74 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +234 | 1587 |
| 75 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +228 | 2346 |
| 76 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +226 | 10372 |
| 77 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +225 | 30948 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +222 | 23661 |
| 79 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +222 | 19136 |
| 80 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +220 | 3801 |
| 81 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +219 | 3657 |
| 82 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +219 | 34777 |
| 83 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +217 | 3470 |
| 84 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +215 | 28436 |
| 85 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +214 | 40027 |
| 86 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +214 | 19331 |
| 87 | [mattpocock/skills](https://github.com/mattpocock/skills) | +214 | 17254 |
| 88 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +212 | 4262 |
| 89 | [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | +207 | 1387 |
| 90 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +207 | 28531 |
| 91 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +206 | 40582 |
| 92 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +206 | 5943 |
| 93 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +201 | 6796 |
| 94 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +200 | 39841 |
| 95 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +199 | 11811 |
| 96 | [88lin/video_vip](https://github.com/88lin/video_vip) | +193 | 1480 |
| 97 | [coleam00/Archon](https://github.com/coleam00/Archon) | +193 | 19474 |
| 98 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +193 | 38537 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +190 | 12478 |
| 100 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +187 | 3036 |
| 101 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +185 | 1572 |
| 102 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 16689 |
| 103 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +183 | 1485 |
| 104 | [pascalorg/editor](https://github.com/pascalorg/editor) | +177 | 14241 |
| 105 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +173 | 8016 |
| 106 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +172 | 15819 |
| 107 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +172 | 2796 |
| 108 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +170 | 2104 |
| 109 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +170 | 40829 |
| 110 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +163 | 5628 |
| 111 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +160 | 28244 |
| 112 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +147 | 31091 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +145 | 11249 |
| 114 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +143 | 34146 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +133 | 10415 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +133 | 36799 |
| 117 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +132 | 30993 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +131 | 11627 |
| 119 | [Lazarus-AI/clearwing](https://github.com/Lazarus-AI/clearwing) | +130 | 899 |
| 120 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +122 | 40666 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25218 | 187828 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17468 | 112971 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11947 | 64072 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +10488 | 80119 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +10003 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +9048 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7780 | 49240 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7369 | 44675 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6974 | 38877 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6860 | 45173 |
| 11 | [garrytan/gstack](https://github.com/garrytan/gstack) | +6118 | 81397 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5658 | 33710 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5570 | 224760 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5205 | 69674 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4593 | 23974 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4450 | 32388 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4287 | 30678 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4219 | 85905 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4174 | 47640 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4160 | 58131 |
| 21 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4155 | 28436 |
| 22 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4040 | 25321 |
| 23 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3957 | 21851 |
| 24 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3851 | 75994 |
| 25 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +3825 | 63559 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3528 | 74774 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3418 | 20123 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3259 | 33399 |
| 29 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3248 | 109881 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3238 | 34148 |
| 31 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3005 | 30948 |
| 32 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2921 | 55967 |
| 33 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2750 | 16764 |
| 34 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2744 | 23732 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2734 | 49824 |
| 36 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2678 | 16393 |
| 37 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2639 | 57012 |
| 38 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2609 | 56655 |
| 39 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2589 | 40829 |
| 40 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2447 | 14233 |
| 41 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2419 | 85286 |
| 42 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2415 | 15767 |
| 43 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2222 | 30590 |
| 44 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2048 | 10771 |
| 45 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2030 | 17789 |
| 46 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2025 | 12355 |
| 47 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1980 | 17028 |
| 48 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1966 | 28244 |
| 49 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1921 | 21184 |
| 50 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1906 | 31098 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1888 | 33878 |
| 52 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1880 | 39117 |
| 53 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1856 | 30198 |
| 54 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1832 | 79656 |
| 55 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1811 | 9975 |
| 56 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1786 | 15717 |
| 57 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1767 | 19136 |
| 58 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1764 | 13867 |
| 59 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1763 | 24805 |
| 60 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1753 | 15745 |
| 61 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1739 | 28568 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1725 | 26114 |
| 63 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1721 | 20822 |
| 64 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1720 | 32359 |
| 65 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1701 | 12757 |
| 66 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1619 | 14039 |
| 67 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1524 | 14241 |
| 68 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1497 | 25289 |
| 69 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1486 | 40582 |
| 70 | [openai/codex](https://github.com/openai/codex) | +1480 | 61744 |
| 71 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1476 | 28198 |
| 72 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1470 | 40064 |
| 73 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1462 | 52234 |
| 74 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1461 | 32936 |
| 75 | [github/spec-kit](https://github.com/github/spec-kit) | +1447 | 71722 |
| 76 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1432 | 49761 |
| 77 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1417 | 11717 |
| 78 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1408 | 18394 |
| 79 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1391 | 6473 |
| 80 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1389 | 73135 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1367 | 42515 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1349 | 37330 |
| 83 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1338 | 8277 |
| 84 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1338 | 21539 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1332 | 98536 |
| 86 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1325 | 20462 |
| 87 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1321 | 6692 |
| 88 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1315 | 45886 |
| 89 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1310 | 22763 |
| 90 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1291 | 21890 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1273 | 34777 |
| 92 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1273 | 18091 |
| 93 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1268 | 78902 |
| 94 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1239 | 10347 |
| 95 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1235 | 17254 |
| 96 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1208 | 95754 |
| 97 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1164 | 23661 |
| 98 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1156 | 5854 |
| 99 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1112 | 12215 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1110 | 14824 |
| 101 | [coleam00/Archon](https://github.com/coleam00/Archon) | +1052 | 19474 |
| 102 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1038 | 38537 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +980 | 12478 |
| 104 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +975 | 39841 |
| 105 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +970 | 31091 |
| 106 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +955 | 9000 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +948 | 5943 |
| 108 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +901 | 6492 |
| 109 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +886 | 11811 |
| 110 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +886 | 5664 |
| 111 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +885 | 52700 |
| 112 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +882 | 49621 |
| 113 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +868 | 21652 |
| 114 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +817 | 24284 |
| 115 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +816 | 4742 |
| 116 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +815 | 7471 |
| 117 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +815 | 40666 |
| 118 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +811 | 6670 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +806 | 11627 |
| 120 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +789 | 22944 |
| 121 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +787 | 4262 |
| 122 | [google/magika](https://github.com/google/magika) | +780 | 16536 |
| 123 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +776 | 4198 |
| 124 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +775 | 6304 |
| 125 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +763 | 24553 |
| 126 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +760 | 24841 |
| 127 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +752 | 34146 |
| 128 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +746 | 5597 |
| 129 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +735 | 9555 |
| 130 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +731 | 4855 |
| 131 | [jundot/omlx](https://github.com/jundot/omlx) | +728 | 11249 |
| 132 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +727 | 4015 |
| 133 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +725 | 3994 |
| 134 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +720 | 10415 |
| 135 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +709 | 47122 |
| 136 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +675 | 54903 |
| 137 | [eze-is/web-access](https://github.com/eze-is/web-access) | +670 | 5585 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +668 | 36799 |
| 139 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +664 | 30993 |
| 140 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +653 | 11579 |
| 141 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +644 | 30528 |
| 142 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +640 | 7343 |
| 143 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +614 | 6796 |
| 144 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +585 | 11518 |
| 145 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +581 | 17668 |
| 146 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +575 | 3801 |
| 147 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +573 | 19278 |
| 148 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +571 | 55070 |
| 149 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +570 | 37564 |
| 150 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +545 | 47936 |
| 151 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +522 | 3371 |
| 152 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +521 | 2511 |
| 153 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +521 | 25696 |
| 154 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +517 | 3036 |
| 155 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +515 | 16977 |
| 156 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +515 | 3657 |
| 157 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +510 | 3137 |
| 158 | [cft0808/edict](https://github.com/cft0808/edict) | +504 | 15406 |
| 159 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +504 | 2838 |
| 160 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +495 | 2327 |
| 161 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +484 | 2576 |
| 162 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +481 | 19771 |
| 163 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +474 | 30176 |
| 164 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +463 | 6671 |
| 165 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +460 | 44545 |
| 166 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +456 | 15862 |
| 167 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +448 | 18082 |
| 168 | [usestrix/strix](https://github.com/usestrix/strix) | +448 | 24484 |
| 169 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +441 | 2283 |
| 170 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +436 | 20452 |
| 171 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +428 | 11328 |
| 172 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +422 | 19439 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +417 | 9400 |
| 174 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +415 | 2416 |
| 175 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +399 | 3384 |
| 176 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +397 | 2813 |
| 177 | [floci-io/floci](https://github.com/floci-io/floci) | +395 | 4135 |
| 178 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +391 | 36907 |
| 179 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +388 | 2110 |
| 180 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +378 | 1947 |
| 181 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +374 | 9054 |
| 182 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +365 | 2949 |
| 183 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +359 | 23873 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +353 | 12394 |
| 185 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +339 | 2640 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +337 | 25604 |
| 187 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +333 | 2104 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +318 | 3186 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +296 | 5649 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +289 | 6205 |
| 191 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +277 | 3081 |
| 192 | [decolua/9router](https://github.com/decolua/9router) | +275 | 2974 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +272 | 36103 |
| 194 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +252 | 7122 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +244 | 1736 |
| 196 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +225 | 2745 |
| 197 | [88lin/video_vip](https://github.com/88lin/video_vip) | +220 | 1480 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +216 | 26104 |
| 199 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +214 | 11278 |
| 200 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +212 | 13025 |
| 201 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +204 | 7263 |
| 202 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +201 | 3066 |
| 203 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +200 | 15769 |
| 204 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +199 | 4220 |
| 205 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +199 | 8743 |
| 206 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +195 | 7902 |
| 207 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +194 | 5507 |
| 208 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +190 | 33712 |
| 209 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +181 | 23760 |
| 210 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +173 | 2559 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +173 | 529 |
| 212 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +172 | 2499 |
| 213 | [usebruno/bruno](https://github.com/usebruno/bruno) | +170 | 41086 |
| 214 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 799 |
| 215 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +152 | 3916 |
| 216 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +152 | 1630 |
| 217 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +150 | 945 |
| 218 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 219 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +147 | 22330 |
| 220 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +146 | 1477 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +145 | 35473 |
| 222 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +143 | 760 |
| 223 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +121 | 1725 |
| 224 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +119 | 3060 |
| 225 | [clawplays/ospec](https://github.com/clawplays/ospec) | +118 | 589 |
| 226 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +118 | 659 |
| 227 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +118 | 29705 |
| 228 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29699 |
| 229 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +115 | 1837 |
| 230 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +115 | 5413 |
| 231 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +113 | 23480 |
| 232 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +111 | 14233 |
| 233 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +111 | 10849 |
| 234 | [dashersw/gea](https://github.com/dashersw/gea) | +109 | 966 |
| 235 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +108 | 7287 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +107 | 33000 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +103 | 26788 |
| 238 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +102 | 6759 |
| 239 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +101 | 1901 |
| 240 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +99 | 1366 |
| 241 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +97 | 39596 |
| 242 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +96 | 736 |
| 243 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +96 | 2001 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +96 | 12856 |
| 245 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +96 | 1028 |
| 246 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 247 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1398 |
| 248 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +93 | 632 |
| 249 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +92 | 944 |
| 250 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 1779 |
| 251 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +89 | 507 |
| 252 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +87 | 604 |
| 253 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +87 | 804 |
| 254 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +86 | 456 |
| 255 | [crimera/piko](https://github.com/crimera/piko) | +85 | 3310 |
| 256 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +84 | 4039 |
| 257 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +84 | 1127 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +84 | 48784 |
| 259 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +83 | 620 |
| 260 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +83 | 2713 |
| 261 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +81 | 645 |
| 262 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +81 | 2757 |
| 263 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +80 | 461 |
| 264 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +80 | 491 |
| 265 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +80 | 2312 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +79 | 3822 |
| 267 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +79 | 1165 |
| 268 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +78 | 664 |
| 269 | [robinebers/openusage](https://github.com/robinebers/openusage) | +77 | 2015 |
| 270 | [openmemind/memind](https://github.com/openmemind/memind) | +77 | 509 |
| 271 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 272 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +77 | 3657 |
| 273 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +76 | 937 |
| 274 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +76 | 1705 |
| 275 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +75 | 762 |
| 276 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +72 | 643 |
| 277 | [microg/GmsCore](https://github.com/microg/GmsCore) | +71 | 13019 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +69 | 9367 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +66 | 27348 |
| 280 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +64 | 1445 |
| 281 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +63 | 375 |
| 282 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +63 | 4061 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +62 | 11739 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +61 | 7312 |
| 285 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +58 | 313 |
| 286 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +56 | 1676 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +55 | 37313 |
| 288 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +54 | 541 |
| 289 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 28969 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +52 | 1778 |
| 291 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +51 | 575 |
| 292 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +51 | 25431 |
| 293 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +50 | 1853 |
| 294 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +49 | 31476 |
| 295 | [idinging/freemail](https://github.com/idinging/freemail) | +48 | 1395 |
| 296 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +48 | 11682 |
| 297 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +44 | 964 |
| 298 | [risin42/NagramX](https://github.com/risin42/NagramX) | +43 | 1710 |
| 299 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +42 | 8568 |
| 300 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +41 | 394 |
