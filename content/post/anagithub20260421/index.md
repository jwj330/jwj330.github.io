---
title: "2026-04-21 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+782 2.CL4R1T4S+444 3.FinceptTerminal+351 4.caveman+224 5.worldmonitor+168"
date: 2026-04-21T20:55:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-21 20:55:49

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
        'daily': {"categories": ["tirth8205/code-review-graph", "paperless-ngx/paperless-ngx", "AIDC-AI/Pixelle-Video", "NawfalMotii79/PLFM_RADAR", "Donchitos/Claude-Code-Game-Studios", "lsdefine/GenericAgent", "thunderbird/thunderbolt", "openai/openai-agents-python", "farion1231/cc-switch", "safishamsi/graphify", "rtk-ai/rtk", "santifer/career-ops", "ruvnet/RuView", "multica-ai/multica", "VoltAgent/awesome-design-md", "koala73/worldmonitor", "JuliusBrussee/caveman", "Fincept-Corporation/FinceptTerminal", "elder-plinius/CL4R1T4S", "forrestchang/andrej-karpathy-skills"], "data": [71, 73, 74, 75, 76, 77, 81, 82, 87, 92, 95, 122, 123, 133, 143, 168, 224, 351, 444, 782]},
        'weekly': {"categories": ["shanraisshan/claude-code-best-practice", "lsdefine/GenericAgent", "BasedHardware/omi", "santifer/career-ops", "EvoMap/evolver", "rtk-ai/rtk", "jamiepine/voicebox", "Donchitos/Claude-Code-Game-Studios", "elder-plinius/CL4R1T4S", "safishamsi/graphify", "multica-ai/multica", "garrytan/gstack", "Fincept-Corporation/FinceptTerminal", "thedotmack/claude-mem", "NawfalMotii79/PLFM_RADAR", "obra/superpowers", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [628, 657, 696, 711, 746, 793, 825, 887, 957, 959, 1008, 1233, 1410, 1655, 1675, 1754, 1840, 1846, 3966, 6014]},
        'monthly': {"categories": ["shanraisshan/claude-code-best-practice", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "karpathy/autoresearch", "msitarzewski/agency-agents", "bytedance/deer-flow", "anthropics/claude-code", "safishamsi/graphify", "openclaw/openclaw", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "garrytan/gstack", "MemPalace/mempalace", "forrestchang/andrej-karpathy-skills", "obra/superpowers", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4370, 4410, 4500, 4755, 4760, 4776, 5296, 5429, 6274, 6840, 6850, 7099, 7341, 7731, 9520, 9765, 11460, 11744, 17106, 25127]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +782 | 71667 |
| 2 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +444 | 21497 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +351 | 11410 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +224 | 42159 |
| 5 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +168 | 50829 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +143 | 62339 |
| 7 | [multica-ai/multica](https://github.com/multica-ai/multica) | +133 | 18408 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +123 | 48821 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +122 | 37861 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +95 | 31650 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +92 | 32002 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +87 | 48458 |
| 13 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +82 | 24345 |
| 14 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +81 | 3403 |
| 15 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +77 | 5472 |
| 16 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +76 | 14932 |
| 17 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +75 | 17327 |
| 18 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +74 | 4988 |
| 19 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +73 | 36907 |
| 20 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +71 | 12242 |
| 21 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +70 | 13590 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +68 | 22109 |
| 23 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +64 | 32836 |
| 24 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +63 | 4401 |
| 25 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +62 | 7792 |
| 26 | [PerryTS/perry](https://github.com/PerryTS/perry) | +57 | 1213 |
| 27 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +56 | 38288 |
| 28 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +56 | 24845 |
| 29 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +55 | 19521 |
| 30 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +52 | 39278 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6014 | 71667 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3966 | 107939 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1846 | 62339 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1840 | 42159 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +1754 | 60312 |
| 6 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1675 | 17327 |
| 7 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1655 | 30678 |
| 8 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1410 | 11410 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1233 | 79473 |
| 10 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1008 | 18408 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +959 | 32002 |
| 12 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +957 | 21498 |
| 13 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +887 | 14932 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +825 | 22109 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +793 | 31650 |
| 16 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +746 | 6289 |
| 17 | [santifer/career-ops](https://github.com/santifer/career-ops) | +711 | 37861 |
| 18 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +696 | 11808 |
| 19 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +657 | 5472 |
| 20 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +628 | 47147 |
| 21 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +624 | 24345 |
| 22 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +587 | 57266 |
| 23 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +575 | 19521 |
| 24 | [google/magika](https://github.com/google/magika) | +560 | 16419 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +553 | 48458 |
| 26 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +530 | 3404 |
| 27 | [android/skills](https://github.com/android/skills) | +501 | 3991 |
| 28 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +488 | 48761 |
| 29 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +483 | 20706 |
| 30 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +481 | 13590 |
| 31 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +457 | 4401 |
| 32 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +454 | 10158 |
| 33 | [pascalorg/editor](https://github.com/pascalorg/editor) | +442 | 14020 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +431 | 39278 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +424 | 15343 |
| 36 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +420 | 10999 |
| 37 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +416 | 2352 |
| 38 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +410 | 50829 |
| 39 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +404 | 38288 |
| 40 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +403 | 2259 |
| 41 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +402 | 3947 |
| 42 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +401 | 20039 |
| 43 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +401 | 24845 |
| 44 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +385 | 12242 |
| 45 | [AgentSeal/codeburn](https://github.com/AgentSeal/codeburn) | +382 | 3231 |
| 46 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +369 | 6020 |
| 47 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +352 | 48821 |
| 48 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +350 | 31878 |
| 49 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +335 | 55427 |
| 50 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +333 | 7792 |
| 51 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +330 | 9896 |
| 52 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +326 | 7059 |
| 53 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +321 | 16044 |
| 54 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +304 | 25738 |
| 55 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +298 | 27720 |
| 56 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +294 | 36907 |
| 57 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +291 | 21144 |
| 58 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +288 | 18820 |
| 59 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +287 | 4650 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +284 | 41870 |
| 61 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +282 | 23035 |
| 62 | [mattpocock/skills](https://github.com/mattpocock/skills) | +276 | 16814 |
| 63 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +275 | 1751 |
| 64 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +275 | 14180 |
| 65 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +275 | 30513 |
| 66 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +274 | 5696 |
| 67 | [tw93/Mole](https://github.com/tw93/Mole) | +270 | 36870 |
| 68 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +269 | 36583 |
| 69 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +268 | 4046 |
| 70 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +262 | 28050 |
| 71 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +250 | 37330 |
| 72 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +247 | 34384 |
| 73 | [momenbasel/PureMac](https://github.com/momenbasel/PureMac) | +245 | 3009 |
| 74 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +243 | 23275 |
| 75 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +241 | 2173 |
| 76 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +239 | 8613 |
| 77 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | +238 | 1500 |
| 78 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +238 | 5307 |
| 79 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +236 | 32051 |
| 80 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +236 | 32836 |
| 81 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +234 | 1505 |
| 82 | [mnfst/manifest](https://github.com/mnfst/manifest) | +233 | 5471 |
| 83 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +230 | 2123 |
| 84 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +227 | 1876 |
| 85 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +226 | 10238 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +226 | 22781 |
| 87 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +224 | 15747 |
| 88 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +220 | 28082 |
| 89 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +215 | 2008 |
| 90 | [coleam00/Archon](https://github.com/coleam00/Archon) | +213 | 19217 |
| 91 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +210 | 18919 |
| 92 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +208 | 11715 |
| 93 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +206 | 12205 |
| 94 | [chenglou/pretext](https://github.com/chenglou/pretext) | +206 | 44940 |
| 95 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +200 | 40108 |
| 96 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +199 | 3439 |
| 97 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +199 | 39841 |
| 98 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +197 | 16596 |
| 99 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +196 | 38254 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +191 | 3123 |
| 101 | [88lin/video_vip](https://github.com/88lin/video_vip) | +189 | 1413 |
| 102 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +189 | 40589 |
| 103 | [PerryTS/perry](https://github.com/PerryTS/perry) | +184 | 1213 |
| 104 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +174 | 2869 |
| 105 | [google-research/timesfm](https://github.com/google-research/timesfm) | +171 | 18295 |
| 106 | [jundot/omlx](https://github.com/jundot/omlx) | +170 | 10959 |
| 107 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +167 | 30823 |
| 108 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +162 | 2455 |
| 109 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +160 | 27902 |
| 110 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +159 | 5444 |
| 111 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +154 | 1218 |
| 112 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +153 | 4988 |
| 113 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +152 | 1868 |
| 114 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +148 | 1276 |
| 115 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +147 | 33992 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +142 | 36799 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +137 | 9986 |
| 118 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +136 | 30721 |
| 119 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +128 | 21460 |
| 120 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +128 | 11423 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25127 | 187123 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17106 | 107939 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11744 | 62339 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11460 | 51199 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +9765 | 60312 |
| 6 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +9520 | 71667 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7731 | 48761 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +7341 | 79473 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7099 | 42159 |
| 10 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6850 | 37861 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6840 | 44940 |
| 12 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +6274 | 224760 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5429 | 32002 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5296 | 69674 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4776 | 63232 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4760 | 84717 |
| 17 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +4755 | 75276 |
| 18 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4500 | 23035 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4410 | 31878 |
| 20 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4370 | 47147 |
| 21 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4308 | 30678 |
| 22 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4305 | 57266 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4128 | 28050 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4011 | 24845 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +3750 | 74774 |
| 26 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3651 | 19521 |
| 27 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3488 | 109881 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3445 | 34148 |
| 29 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3235 | 18408 |
| 30 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3203 | 56674 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3202 | 31650 |
| 32 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3201 | 55427 |
| 33 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3143 | 24682 |
| 34 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3042 | 30513 |
| 35 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2986 | 55769 |
| 36 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2954 | 30590 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2764 | 48458 |
| 38 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2732 | 16585 |
| 39 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2714 | 23275 |
| 40 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2643 | 16044 |
| 41 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2586 | 40589 |
| 42 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2567 | 85286 |
| 43 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2378 | 15442 |
| 44 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2365 | 13590 |
| 45 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2276 | 16708 |
| 46 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2266 | 30181 |
| 47 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +2123 | 14932 |
| 48 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2024 | 32051 |
| 49 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2013 | 12160 |
| 50 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1995 | 18820 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1983 | 33878 |
| 52 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1968 | 17327 |
| 53 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1964 | 9896 |
| 54 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1953 | 38288 |
| 55 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1948 | 27902 |
| 56 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1925 | 14020 |
| 57 | [block/goose](https://github.com/block/goose) | +1919 | 31098 |
| 58 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1870 | 20706 |
| 59 | [github/spec-kit](https://github.com/github/spec-kit) | +1856 | 71722 |
| 60 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1843 | 25738 |
| 61 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1832 | 12242 |
| 62 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1811 | 28338 |
| 63 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1797 | 9897 |
| 64 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1784 | 79656 |
| 65 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1742 | 15343 |
| 66 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1704 | 20243 |
| 67 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1695 | 11024 |
| 68 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1674 | 40108 |
| 69 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1661 | 20039 |
| 70 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1611 | 13978 |
| 71 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1586 | 32689 |
| 72 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1574 | 48821 |
| 73 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1562 | 50829 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1523 | 27720 |
| 75 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1522 | 21144 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1510 | 61744 |
| 77 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1493 | 39278 |
| 78 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1429 | 11410 |
| 79 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1416 | 11702 |
| 80 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1409 | 37330 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1407 | 41870 |
| 82 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1404 | 18295 |
| 83 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1393 | 73135 |
| 84 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1392 | 98536 |
| 85 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1378 | 6335 |
| 86 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1353 | 16814 |
| 87 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1342 | 78902 |
| 88 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1341 | 34384 |
| 89 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1320 | 6702 |
| 90 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1283 | 45886 |
| 91 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1283 | 21733 |
| 92 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1283 | 17977 |
| 93 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1280 | 22110 |
| 94 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1274 | 7792 |
| 95 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1256 | 10158 |
| 96 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1227 | 22781 |
| 97 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1208 | 95754 |
| 98 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1149 | 5794 |
| 99 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1126 | 14180 |
| 100 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1087 | 30823 |
| 101 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1050 | 38254 |
| 102 | [coleam00/Archon](https://github.com/coleam00/Archon) | +1032 | 19217 |
| 103 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1018 | 21498 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +992 | 12205 |
| 105 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +980 | 39841 |
| 106 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +954 | 8967 |
| 107 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +951 | 21460 |
| 108 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +937 | 5696 |
| 109 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +921 | 49621 |
| 110 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +919 | 52700 |
| 111 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +906 | 22710 |
| 112 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +901 | 11715 |
| 113 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +894 | 6418 |
| 114 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +881 | 5593 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +855 | 11423 |
| 116 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +845 | 40407 |
| 117 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +826 | 24445 |
| 118 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +824 | 24188 |
| 119 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +822 | 7059 |
| 120 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +811 | 4689 |
| 121 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +800 | 33992 |
| 122 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +783 | 6289 |
| 123 | [jundot/omlx](https://github.com/jundot/omlx) | +770 | 10959 |
| 124 | [google/magika](https://github.com/google/magika) | +769 | 16419 |
| 125 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +768 | 4046 |
| 126 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +763 | 4025 |
| 127 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +750 | 9986 |
| 128 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +746 | 5583 |
| 129 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +739 | 24345 |
| 130 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +737 | 9518 |
| 131 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +728 | 4650 |
| 132 | [eze-is/web-access](https://github.com/eze-is/web-access) | +727 | 5450 |
| 133 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +725 | 3981 |
| 134 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +718 | 5472 |
| 135 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +718 | 11512 |
| 136 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +715 | 3901 |
| 137 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +697 | 30421 |
| 138 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +679 | 7171 |
| 139 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +678 | 30721 |
| 140 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +673 | 36799 |
| 141 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +671 | 54903 |
| 142 | [floci-io/floci](https://github.com/floci-io/floci) | +657 | 4079 |
| 143 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +629 | 17499 |
| 144 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +620 | 47122 |
| 145 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +602 | 37564 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +587 | 19102 |
| 147 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +584 | 11506 |
| 148 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +563 | 47936 |
| 149 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +554 | 3123 |
| 150 | [cft0808/edict](https://github.com/cft0808/edict) | +550 | 15342 |
| 151 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +529 | 3439 |
| 152 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +527 | 25596 |
| 153 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +520 | 16798 |
| 154 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +519 | 2481 |
| 155 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +513 | 5784 |
| 156 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +511 | 3278 |
| 157 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +510 | 19688 |
| 158 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +509 | 3110 |
| 159 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +507 | 2733 |
| 160 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +501 | 2810 |
| 161 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +498 | 2869 |
| 162 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +485 | 29892 |
| 163 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +485 | 8936 |
| 164 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +480 | 4426 |
| 165 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +473 | 44545 |
| 166 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +471 | 4448 |
| 167 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +469 | 6599 |
| 168 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +466 | 3243 |
| 169 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +463 | 15731 |
| 170 | [usestrix/strix](https://github.com/usestrix/strix) | +448 | 24356 |
| 171 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +446 | 11270 |
| 172 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +444 | 19267 |
| 173 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +435 | 2193 |
| 174 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +423 | 20269 |
| 175 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +421 | 3280 |
| 176 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +419 | 9247 |
| 177 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +397 | 2805 |
| 178 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +395 | 2204 |
| 179 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +389 | 36907 |
| 180 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +382 | 2067 |
| 181 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +377 | 1938 |
| 182 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +374 | 16775 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +372 | 12276 |
| 184 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +362 | 2880 |
| 185 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +357 | 23747 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +354 | 25476 |
| 187 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +334 | 12999 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +321 | 3133 |
| 189 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +314 | 1868 |
| 190 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +304 | 5508 |
| 191 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +284 | 2704 |
| 192 | [decolua/9router](https://github.com/decolua/9router) | +278 | 2833 |
| 193 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +277 | 3074 |
| 194 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +276 | 36103 |
| 195 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +272 | 6024 |
| 196 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +261 | 3031 |
| 197 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +243 | 6904 |
| 198 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +238 | 1509 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +227 | 25999 |
| 200 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +223 | 4209 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +222 | 9361 |
| 202 | [88lin/video_vip](https://github.com/88lin/video_vip) | +219 | 1413 |
| 203 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +219 | 11229 |
| 204 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +215 | 7864 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +212 | 6095 |
| 206 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +211 | 15701 |
| 207 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +194 | 7168 |
| 208 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +194 | 2463 |
| 209 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +192 | 3030 |
| 210 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +190 | 33712 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +188 | 609 |
| 212 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +179 | 23730 |
| 213 | [usebruno/bruno](https://github.com/usebruno/bruno) | +179 | 41086 |
| 214 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +176 | 2491 |
| 215 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +172 | 1011 |
| 216 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 794 |
| 217 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +153 | 3896 |
| 218 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +152 | 1516 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +152 | 40265 |
| 220 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +151 | 22270 |
| 221 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +149 | 914 |
| 222 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +142 | 1440 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +139 | 35473 |
| 224 | [dashersw/gea](https://github.com/dashersw/gea) | +132 | 964 |
| 225 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +128 | 1817 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +125 | 1676 |
| 227 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +123 | 29684 |
| 228 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +120 | 29675 |
| 229 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +119 | 5375 |
| 230 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +118 | 10822 |
| 231 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +114 | 23442 |
| 232 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +111 | 1752 |
| 233 | [clawplays/ospec](https://github.com/clawplays/ospec) | +110 | 536 |
| 234 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +110 | 611 |
| 235 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +109 | 845 |
| 236 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +106 | 1875 |
| 237 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +105 | 5805 |
| 238 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +104 | 33000 |
| 239 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +103 | 1985 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +103 | 12801 |
| 241 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +102 | 1353 |
| 242 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +100 | 6724 |
| 243 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +99 | 1004 |
| 244 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +99 | 957 |
| 245 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +98 | 7199 |
| 246 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +97 | 1373 |
| 247 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 361 |
| 248 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +96 | 2742 |
| 249 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +95 | 711 |
| 250 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +92 | 48784 |
| 251 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +91 | 893 |
| 252 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +90 | 603 |
| 253 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +89 | 1198 |
| 254 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +88 | 963 |
| 255 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +87 | 1157 |
| 256 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +86 | 467 |
| 257 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +86 | 611 |
| 258 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +86 | 803 |
| 259 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +86 | 2684 |
| 260 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3279 |
| 261 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +85 | 1088 |
| 262 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +85 | 634 |
| 263 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +84 | 4015 |
| 264 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +82 | 552 |
| 265 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +82 | 2276 |
| 266 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +82 | 45263 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +81 | 3786 |
| 268 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +81 | 907 |
| 269 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +81 | 3632 |
| 270 | [robinebers/openusage](https://github.com/robinebers/openusage) | +80 | 1990 |
| 271 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +79 | 448 |
| 272 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1672 |
| 273 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +77 | 367 |
| 274 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +77 | 432 |
| 275 | [openmemind/memind](https://github.com/openmemind/memind) | +77 | 481 |
| 276 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +76 | 829 |
| 277 | [microg/GmsCore](https://github.com/microg/GmsCore) | +76 | 12997 |
| 278 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +75 | 759 |
| 279 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +71 | 618 |
| 280 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +69 | 568 |
| 281 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +67 | 1428 |
| 282 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9335 |
| 283 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +67 | 27323 |
| 284 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +65 | 485 |
| 285 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +64 | 11699 |
| 286 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +63 | 370 |
| 287 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7296 |
| 288 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +60 | 403 |
| 289 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +60 | 313 |
| 290 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1653 |
| 291 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +54 | 1750 |
| 293 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +54 | 1833 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 28965 |
| 295 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +54 | 25432 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +52 | 31476 |
| 297 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +47 | 11665 |
| 298 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +45 | 8544 |
| 299 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1706 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +38 | 10154 |
