---
title: "2026-04-22 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+564 2.CL4R1T4S+240 3.FinceptTerminal+234 4.CubeSandbox+222 5.agent-skills+214"
date: 2026-04-22T20:57:46+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-22 20:57:46

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
        'daily': {"categories": ["ruvnet/RuView", "Anil-matcha/Open-Generative-AI", "Donchitos/Claude-Code-Game-Studios", "thunderbird/thunderbolt", "farion1231/cc-switch", "zilliztech/claude-context", "HKUDS/RAG-Anything", "rtk-ai/rtk", "santifer/career-ops", "VoltAgent/awesome-agent-skills", "VoltAgent/awesome-design-md", "multica-ai/multica", "Leonxlnx/taste-skill", "safishamsi/graphify", "JuliusBrussee/caveman", "addyosmani/agent-skills", "TencentCloud/CubeSandbox", "Fincept-Corporation/FinceptTerminal", "elder-plinius/CL4R1T4S", "forrestchang/andrej-karpathy-skills"], "data": [67, 72, 73, 75, 81, 82, 85, 87, 93, 103, 124, 125, 151, 151, 158, 214, 222, 234, 240, 564]},
        'weekly': {"categories": ["BasedHardware/omi", "addyosmani/agent-skills", "santifer/career-ops", "jamiepine/voicebox", "EvoMap/evolver", "rtk-ai/rtk", "msitarzewski/agency-agents", "Donchitos/Claude-Code-Game-Studios", "safishamsi/graphify", "multica-ai/multica", "elder-plinius/CL4R1T4S", "garrytan/gstack", "thedotmack/claude-mem", "NawfalMotii79/PLFM_RADAR", "JuliusBrussee/caveman", "Fincept-Corporation/FinceptTerminal", "VoltAgent/awesome-design-md", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [663, 705, 725, 738, 774, 776, 856, 894, 950, 975, 1176, 1221, 1443, 1452, 1592, 1619, 1626, 1626, 3537, 5368]},
        'monthly': {"categories": ["thedotmack/claude-mem", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "siddharthvaddem/openscreen", "msitarzewski/agency-agents", "Gitlawb/openclaude", "anthropics/claude-code", "safishamsi/graphify", "openclaw/openclaw", "garrytan/gstack", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "forrestchang/andrej-karpathy-skills", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4301, 4304, 4409, 4427, 4432, 4549, 5250, 5575, 5918, 6805, 6847, 6938, 7258, 7753, 9396, 10058, 10741, 11866, 17315, 25181]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +564 | 75822 |
| 2 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +240 | 23905 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +234 | 12955 |
| 4 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +222 | 2299 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +214 | 21052 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +158 | 43515 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +151 | 33040 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +151 | 11908 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | +125 | 19351 |
| 10 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +124 | 63252 |
| 11 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +103 | 17440 |
| 12 | [santifer/career-ops](https://github.com/santifer/career-ops) | +93 | 38476 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +87 | 32480 |
| 14 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +85 | 17471 |
| 15 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +82 | 7409 |
| 16 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +81 | 49134 |
| 17 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +75 | 3722 |
| 18 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +73 | 15388 |
| 19 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +72 | 6347 |
| 20 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +67 | 49333 |
| 21 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +61 | 5901 |
| 22 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +57 | 2203 |
| 23 | [cloudflare/kumo](https://github.com/cloudflare/kumo) | +54 | 1610 |
| 24 | [432539/gpt2api](https://github.com/432539/gpt2api) | +52 | 786 |
| 25 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +50 | 23617 |
| 26 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +49 | 13943 |
| 27 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +48 | 42245 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +48 | 38724 |
| 29 | [PerryTS/perry](https://github.com/PerryTS/perry) | +46 | 1539 |
| 30 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +44 | 8083 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5368 | 75822 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3537 | 110502 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +1626 | 60312 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1626 | 63252 |
| 5 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1619 | 12955 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1592 | 43515 |
| 7 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1452 | 17557 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1443 | 30678 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1221 | 80392 |
| 10 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1176 | 23905 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +975 | 19351 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +950 | 33041 |
| 13 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +894 | 15388 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +856 | 85360 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +776 | 32480 |
| 16 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +774 | 6516 |
| 17 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +738 | 22440 |
| 18 | [santifer/career-ops](https://github.com/santifer/career-ops) | +725 | 38476 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +705 | 21052 |
| 20 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +663 | 11961 |
| 21 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +655 | 24605 |
| 22 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +649 | 5901 |
| 23 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +601 | 3722 |
| 24 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +554 | 11908 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +541 | 49134 |
| 26 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +482 | 4634 |
| 27 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +475 | 20994 |
| 28 | [google/magika](https://github.com/google/magika) | +462 | 16486 |
| 29 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +451 | 10266 |
| 30 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +444 | 13943 |
| 31 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +427 | 47391 |
| 32 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +426 | 51450 |
| 33 | [android/skills](https://github.com/android/skills) | +424 | 4137 |
| 34 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +418 | 2447 |
| 35 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +414 | 38724 |
| 36 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +398 | 49333 |
| 37 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +395 | 48999 |
| 38 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +373 | 39643 |
| 39 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +368 | 15540 |
| 40 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +367 | 8083 |
| 41 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +367 | 2317 |
| 42 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +365 | 6047 |
| 43 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +358 | 12511 |
| 44 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +348 | 20267 |
| 45 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +341 | 25105 |
| 46 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +337 | 32140 |
| 47 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +335 | 7253 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +319 | 10342 |
| 49 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +312 | 55702 |
| 50 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +298 | 21364 |
| 51 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +297 | 36907 |
| 52 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +296 | 16232 |
| 53 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +295 | 23617 |
| 54 | [pascalorg/editor](https://github.com/pascalorg/editor) | +295 | 14165 |
| 55 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +292 | 27956 |
| 56 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +288 | 4763 |
| 57 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +286 | 25927 |
| 58 | [AgentSeal/codeburn](https://github.com/AgentSeal/codeburn) | +286 | 3359 |
| 59 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +284 | 1836 |
| 60 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +281 | 42245 |
| 61 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +280 | 2203 |
| 62 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +280 | 4007 |
| 63 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +274 | 19008 |
| 64 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +265 | 8961 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +260 | 14452 |
| 66 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +254 | 36714 |
| 67 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +252 | 32836 |
| 68 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +248 | 30738 |
| 69 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +245 | 15995 |
| 70 | [mattpocock/skills](https://github.com/mattpocock/skills) | +245 | 16933 |
| 71 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | +244 | 1540 |
| 72 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +243 | 37330 |
| 73 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +243 | 28227 |
| 74 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +239 | 34598 |
| 75 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +238 | 23505 |
| 76 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +237 | 32219 |
| 77 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +237 | 2375 |
| 78 | [mnfst/manifest](https://github.com/mnfst/manifest) | +237 | 5533 |
| 79 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +234 | 1548 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +231 | 23087 |
| 81 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +230 | 2299 |
| 82 | [PerryTS/perry](https://github.com/PerryTS/perry) | +230 | 1539 |
| 83 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +228 | 10302 |
| 84 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +226 | 17440 |
| 85 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +221 | 2185 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +220 | 36870 |
| 87 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +219 | 28311 |
| 88 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +219 | 5383 |
| 89 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +212 | 4172 |
| 90 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +209 | 3531 |
| 91 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +207 | 5827 |
| 92 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +205 | 19136 |
| 93 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +202 | 39841 |
| 94 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +201 | 40328 |
| 95 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +199 | 11769 |
| 96 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +195 | 17471 |
| 97 | [88lin/video_vip](https://github.com/88lin/video_vip) | +193 | 1458 |
| 98 | [coleam00/Archon](https://github.com/coleam00/Archon) | +193 | 19342 |
| 99 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +193 | 38422 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +191 | 3378 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +190 | 12344 |
| 102 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +189 | 6347 |
| 103 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +187 | 2981 |
| 104 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +185 | 16637 |
| 105 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +181 | 1425 |
| 106 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +170 | 40704 |
| 107 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +168 | 1444 |
| 108 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +167 | 2027 |
| 109 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +164 | 5553 |
| 110 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +160 | 5472 |
| 111 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +160 | 28062 |
| 112 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +150 | 30948 |
| 113 | [jundot/omlx](https://github.com/jundot/omlx) | +145 | 11063 |
| 114 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +143 | 34063 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +133 | 10185 |
| 116 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +133 | 36799 |
| 117 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +132 | 30872 |
| 118 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +131 | 11515 |
| 119 | [Lazarus-AI/clearwing](https://github.com/Lazarus-AI/clearwing) | +130 | 872 |
| 120 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +122 | 40530 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25181 | 187507 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17315 | 110502 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11866 | 63252 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +10741 | 51199 |
| 5 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +10058 | 75822 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +9396 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7753 | 48999 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7258 | 43515 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6938 | 38476 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6847 | 45049 |
| 11 | [garrytan/gstack](https://github.com/garrytan/gstack) | +6805 | 80393 |
| 12 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5918 | 224760 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5575 | 33041 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5250 | 69674 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4549 | 23617 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4432 | 85360 |
| 17 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4427 | 32140 |
| 18 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4409 | 63431 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4304 | 47391 |
| 20 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4301 | 30678 |
| 21 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4215 | 57733 |
| 22 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +4210 | 75600 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4133 | 28227 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4030 | 25105 |
| 25 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3857 | 21052 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3656 | 74774 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3352 | 19351 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3344 | 34148 |
| 29 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3322 | 109881 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3215 | 32480 |
| 31 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3084 | 55702 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3024 | 30738 |
| 33 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2909 | 56863 |
| 34 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2798 | 56184 |
| 35 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2753 | 49134 |
| 36 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2741 | 16681 |
| 37 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2730 | 23505 |
| 38 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2664 | 16232 |
| 39 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2654 | 30590 |
| 40 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2588 | 40704 |
| 41 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +2566 | 24741 |
| 42 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2487 | 85286 |
| 43 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2411 | 13943 |
| 44 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2397 | 15616 |
| 45 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2110 | 16858 |
| 46 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2021 | 12258 |
| 47 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2000 | 17557 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1996 | 10342 |
| 49 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1988 | 15388 |
| 50 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1955 | 28062 |
| 51 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1941 | 14165 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1939 | 33878 |
| 53 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1914 | 38724 |
| 54 | [block/goose](https://github.com/block/goose) | +1911 | 31098 |
| 55 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1902 | 20994 |
| 56 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +1867 | 30192 |
| 57 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1854 | 32219 |
| 58 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1848 | 19008 |
| 59 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1806 | 9938 |
| 60 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1803 | 79656 |
| 61 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1789 | 12511 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1775 | 25927 |
| 63 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1769 | 28459 |
| 64 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1767 | 15540 |
| 65 | [github/spec-kit](https://github.com/github/spec-kit) | +1739 | 71722 |
| 66 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1677 | 20267 |
| 67 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1647 | 11093 |
| 68 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1635 | 12955 |
| 69 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1617 | 14012 |
| 70 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1584 | 49333 |
| 71 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1566 | 32820 |
| 72 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1555 | 40328 |
| 73 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1498 | 27956 |
| 74 | [openai/codex](https://github.com/openai/codex) | +1498 | 61744 |
| 75 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1490 | 20343 |
| 76 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1483 | 39643 |
| 77 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1460 | 51450 |
| 78 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1419 | 21364 |
| 79 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1416 | 11709 |
| 80 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1405 | 18340 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1395 | 42245 |
| 82 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1394 | 73135 |
| 83 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1383 | 6412 |
| 84 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1375 | 37330 |
| 85 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1365 | 98536 |
| 86 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1321 | 6693 |
| 87 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1317 | 8083 |
| 88 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1306 | 34598 |
| 89 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1299 | 45886 |
| 90 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1289 | 21831 |
| 91 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1286 | 22441 |
| 92 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1273 | 16933 |
| 93 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1273 | 18038 |
| 94 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1268 | 78902 |
| 95 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1249 | 10266 |
| 96 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1237 | 23905 |
| 97 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1206 | 95754 |
| 98 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1186 | 23088 |
| 99 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1141 | 11908 |
| 100 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1113 | 14452 |
| 101 | [coleam00/Archon](https://github.com/coleam00/Archon) | +1040 | 19342 |
| 102 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1038 | 38422 |
| 103 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1004 | 30948 |
| 104 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +980 | 12344 |
| 105 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +975 | 39841 |
| 106 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +955 | 8985 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +948 | 5827 |
| 108 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +901 | 6453 |
| 109 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +886 | 11769 |
| 110 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +886 | 5627 |
| 111 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +885 | 52700 |
| 112 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +882 | 49621 |
| 113 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +868 | 21551 |
| 114 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +817 | 24241 |
| 115 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +816 | 4715 |
| 116 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +815 | 7253 |
| 117 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +815 | 40530 |
| 118 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +808 | 6516 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +806 | 11515 |
| 120 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +789 | 22826 |
| 121 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +787 | 4172 |
| 122 | [google/magika](https://github.com/google/magika) | +780 | 16486 |
| 123 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +776 | 4134 |
| 124 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +775 | 5901 |
| 125 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +763 | 24506 |
| 126 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +760 | 24605 |
| 127 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +752 | 34063 |
| 128 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +746 | 5593 |
| 129 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +735 | 9537 |
| 130 | [eze-is/web-access](https://github.com/eze-is/web-access) | +732 | 5507 |
| 131 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +731 | 4763 |
| 132 | [jundot/omlx](https://github.com/jundot/omlx) | +728 | 11064 |
| 133 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +727 | 4004 |
| 134 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +720 | 10185 |
| 135 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +718 | 3943 |
| 136 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +709 | 47122 |
| 137 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +675 | 54903 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +668 | 36799 |
| 139 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +664 | 30872 |
| 140 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +653 | 11529 |
| 141 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +644 | 30476 |
| 142 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +640 | 7233 |
| 143 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +585 | 11510 |
| 144 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +583 | 37564 |
| 145 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +581 | 17592 |
| 146 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +580 | 6347 |
| 147 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +575 | 3378 |
| 148 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +573 | 19194 |
| 149 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +571 | 55070 |
| 150 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +545 | 47936 |
| 151 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +531 | 3531 |
| 152 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +522 | 3329 |
| 153 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +521 | 2494 |
| 154 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +521 | 25640 |
| 155 | [floci-io/floci](https://github.com/floci-io/floci) | +520 | 4113 |
| 156 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +517 | 2981 |
| 157 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +515 | 16894 |
| 158 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +510 | 3128 |
| 159 | [cft0808/edict](https://github.com/cft0808/edict) | +504 | 15367 |
| 160 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +504 | 2826 |
| 161 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +495 | 2302 |
| 162 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +494 | 2560 |
| 163 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +481 | 19727 |
| 164 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +474 | 30041 |
| 165 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +463 | 6641 |
| 166 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +460 | 44545 |
| 167 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +456 | 15799 |
| 168 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +448 | 17471 |
| 169 | [usestrix/strix](https://github.com/usestrix/strix) | +448 | 24390 |
| 170 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +436 | 20369 |
| 171 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +436 | 2242 |
| 172 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +428 | 11301 |
| 173 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +422 | 19358 |
| 174 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +418 | 8987 |
| 175 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +415 | 9314 |
| 176 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +411 | 3337 |
| 177 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +404 | 2296 |
| 178 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +397 | 2808 |
| 179 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +391 | 36907 |
| 180 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +388 | 2093 |
| 181 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +378 | 1942 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +366 | 12334 |
| 183 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +364 | 2918 |
| 184 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +357 | 23819 |
| 185 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +341 | 25537 |
| 186 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +339 | 2376 |
| 187 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +333 | 2027 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +323 | 3163 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +297 | 5575 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +283 | 6132 |
| 191 | [decolua/9router](https://github.com/decolua/9router) | +277 | 2912 |
| 192 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +276 | 3078 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +273 | 36103 |
| 194 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +261 | 13014 |
| 195 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +260 | 7081 |
| 196 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +252 | 2725 |
| 197 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +238 | 1574 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +226 | 26054 |
| 199 | [88lin/video_vip](https://github.com/88lin/video_vip) | +219 | 1458 |
| 200 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +219 | 3052 |
| 201 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +217 | 11256 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +211 | 8744 |
| 203 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +208 | 4217 |
| 204 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +205 | 7888 |
| 205 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +204 | 7216 |
| 206 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +203 | 5508 |
| 207 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +202 | 15738 |
| 208 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +189 | 33712 |
| 209 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +182 | 2480 |
| 210 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +180 | 23745 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +179 | 521 |
| 212 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +175 | 2526 |
| 213 | [usebruno/bruno](https://github.com/usebruno/bruno) | +171 | 41086 |
| 214 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 795 |
| 215 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +157 | 760 |
| 216 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +156 | 3051 |
| 217 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +153 | 3904 |
| 218 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +150 | 931 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +150 | 40265 |
| 220 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +148 | 22296 |
| 221 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +145 | 1457 |
| 222 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +145 | 1524 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +141 | 35473 |
| 224 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +124 | 1701 |
| 225 | [dashersw/gea](https://github.com/dashersw/gea) | +122 | 964 |
| 226 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +121 | 29686 |
| 227 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +120 | 1830 |
| 228 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +119 | 5400 |
| 229 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +117 | 652 |
| 230 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29688 |
| 231 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +115 | 10837 |
| 232 | [clawplays/ospec](https://github.com/clawplays/ospec) | +113 | 578 |
| 233 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +113 | 23458 |
| 234 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +106 | 1767 |
| 235 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +104 | 7257 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +104 | 33000 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +103 | 26724 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +102 | 1889 |
| 239 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +101 | 1993 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +100 | 12831 |
| 241 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +100 | 6738 |
| 242 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +100 | 1361 |
| 243 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +97 | 1017 |
| 244 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +96 | 725 |
| 245 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 246 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1381 |
| 247 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +94 | 39596 |
| 248 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +92 | 924 |
| 249 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +90 | 623 |
| 250 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +88 | 492 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +88 | 48784 |
| 252 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +87 | 804 |
| 253 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +87 | 2701 |
| 254 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3289 |
| 255 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +85 | 579 |
| 256 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +85 | 1115 |
| 257 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +84 | 4027 |
| 258 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +84 | 618 |
| 259 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +83 | 437 |
| 260 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +82 | 2747 |
| 261 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +81 | 1165 |
| 262 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +81 | 2297 |
| 263 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +81 | 45263 |
| 264 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +80 | 455 |
| 265 | [robinebers/openusage](https://github.com/robinebers/openusage) | +80 | 2002 |
| 266 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +80 | 648 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +79 | 3808 |
| 268 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +78 | 467 |
| 269 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +78 | 3646 |
| 270 | [openmemind/memind](https://github.com/openmemind/memind) | +77 | 497 |
| 271 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +76 | 836 |
| 272 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +76 | 916 |
| 273 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +76 | 1685 |
| 274 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +75 | 760 |
| 275 | [microg/GmsCore](https://github.com/microg/GmsCore) | +73 | 13012 |
| 276 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +70 | 627 |
| 277 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +70 | 9355 |
| 278 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +68 | 545 |
| 279 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +65 | 11718 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +65 | 27333 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7308 |
| 282 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +64 | 1435 |
| 283 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +63 | 372 |
| 284 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +61 | 491 |
| 285 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +58 | 313 |
| 286 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1666 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 288 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +57 | 574 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +55 | 1763 |
| 290 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +55 | 25433 |
| 291 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 28966 |
| 292 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +53 | 4877 |
| 293 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +53 | 1841 |
| 294 | [idinging/freemail](https://github.com/idinging/freemail) | +51 | 1392 |
| 295 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +51 | 959 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +50 | 31476 |
| 297 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +48 | 11676 |
| 298 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1708 |
| 299 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +44 | 8556 |
| 300 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +39 | 370 |
