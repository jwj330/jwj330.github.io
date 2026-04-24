---
title: "2026-04-24 GitHub增长趋势报告"
description: "1.free-claude-code+261 2.agent-skills+141 3.marketingskills+140 4.CubeSandbox+138 5.awesome-gpt-image-2+137"
date: 2026-04-24T20:52:25+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-24 20:52:25

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
        'daily': {"categories": ["multica-ai/multica", "garrytan/gbrain", "Fincept-Corporation/FinceptTerminal", "mksglu/context-mode", "mattpocock/skills", "safishamsi/graphify", "open-metadata/OpenMetadata", "lsdefine/GenericAgent", "HKUDS/RAG-Anything", "VoltAgent/awesome-design-md", "zilliztech/claude-context", "rtk-ai/rtk", "VoltAgent/awesome-agent-skills", "Anil-matcha/Open-Generative-AI", "JuliusBrussee/caveman", "YouMind-OpenLab/awesome-gpt-image-2", "TencentCloud/CubeSandbox", "coreyhaines31/marketingskills", "addyosmani/agent-skills", "Alishahryar1/free-claude-code"], "data": [63, 65, 66, 68, 68, 74, 75, 77, 88, 90, 97, 98, 108, 109, 127, 137, 138, 140, 141, 261]},
        'weekly': {"categories": ["Leonxlnx/taste-skill", "farion1231/cc-switch", "EvoMap/evolver", "santifer/career-ops", "openai/openai-agents-python", "jamiepine/voicebox", "Donchitos/Claude-Code-Game-Studios", "addyosmani/agent-skills", "rtk-ai/rtk", "multica-ai/multica", "safishamsi/graphify", "NawfalMotii79/PLFM_RADAR", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "garrytan/gstack", "JuliusBrussee/caveman", "elder-plinius/CL4R1T4S", "Fincept-Corporation/FinceptTerminal", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [566, 575, 579, 582, 607, 628, 756, 812, 815, 819, 868, 995, 1040, 1161, 1236, 1341, 1412, 1782, 3047, 4518]},
        'monthly': {"categories": ["shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "luongnv89/claude-howto", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "anthropics/claude-code", "openclaw/openclaw", "safishamsi/graphify", "garrytan/gstack", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "affaan-m/everything-claude-code", "forrestchang/andrej-karpathy-skills", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4150, 4170, 4174, 4303, 4462, 4628, 5184, 5303, 5725, 5778, 6873, 7014, 7486, 7810, 8848, 9741, 10925, 12035, 17572, 25259]}
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
| 1 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +261 | 8459 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +141 | 22663 |
| 3 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +140 | 24443 |
| 4 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +138 | 3906 |
| 5 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +137 | 1960 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +127 | 45756 |
| 7 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +109 | 7587 |
| 8 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +108 | 18592 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +98 | 34500 |
| 10 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +97 | 8944 |
| 11 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +90 | 64765 |
| 12 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +88 | 18543 |
| 13 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +77 | 6835 |
| 14 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +75 | 13301 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +74 | 34266 |
| 16 | [mattpocock/skills](https://github.com/mattpocock/skills) | +68 | 18015 |
| 17 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +68 | 9786 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +66 | 14304 |
| 19 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +65 | 11141 |
| 20 | [multica-ai/multica](https://github.com/multica-ai/multica) | +63 | 20629 |
| 21 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +61 | 21261 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +55 | 23098 |
| 23 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +52 | 6617 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +50 | 50101 |
| 25 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +47 | 14470 |
| 26 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +46 | 40400 |
| 27 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +46 | 12641 |
| 28 | [guokaigdg/animal-island-ui](https://github.com/guokaigdg/animal-island-ui) | +44 | 501 |
| 29 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +42 | 28534 |
| 30 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +42 | 15188 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4518 | 83382 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3047 | 115010 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1782 | 14304 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1412 | 25436 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1341 | 45756 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1236 | 82475 |
| 7 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1161 | 64765 |
| 8 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1040 | 30678 |
| 9 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +995 | 18053 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +868 | 34266 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +819 | 20629 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +815 | 34500 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +812 | 22663 |
| 14 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +756 | 15990 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +628 | 23098 |
| 16 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +607 | 24979 |
| 17 | [santifer/career-ops](https://github.com/santifer/career-ops) | +582 | 39193 |
| 18 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +579 | 6802 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +575 | 50640 |
| 20 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +566 | 12641 |
| 21 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +562 | 6835 |
| 22 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +552 | 3952 |
| 23 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +531 | 12147 |
| 24 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +530 | 52464 |
| 25 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +480 | 8459 |
| 26 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +466 | 50101 |
| 27 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +452 | 21354 |
| 28 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +435 | 3906 |
| 29 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +429 | 10433 |
| 30 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +425 | 2590 |
| 31 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +401 | 39577 |
| 32 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +388 | 14470 |
| 33 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +387 | 4837 |
| 34 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +385 | 8482 |
| 35 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +353 | 12949 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +350 | 40400 |
| 37 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +345 | 24443 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +345 | 7749 |
| 39 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +342 | 21261 |
| 40 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +340 | 8944 |
| 41 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +336 | 47867 |
| 42 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +334 | 11141 |
| 43 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +330 | 9786 |
| 44 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +325 | 49454 |
| 45 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +324 | 18592 |
| 46 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +311 | 18543 |
| 47 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +310 | 36907 |
| 48 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +305 | 15836 |
| 49 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +302 | 25576 |
| 50 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +301 | 6617 |
| 51 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +301 | 24215 |
| 52 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +294 | 7587 |
| 53 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +293 | 32578 |
| 54 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +276 | 28534 |
| 55 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +275 | 56253 |
| 56 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +274 | 16501 |
| 57 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +266 | 42755 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +265 | 15188 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +264 | 26268 |
| 60 | [PerryTS/perry](https://github.com/PerryTS/perry) | +262 | 1686 |
| 61 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +260 | 2373 |
| 62 | [google/magika](https://github.com/google/magika) | +255 | 16628 |
| 63 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +251 | 16290 |
| 64 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +248 | 32836 |
| 65 | [mattpocock/skills](https://github.com/mattpocock/skills) | +246 | 18015 |
| 66 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +244 | 23862 |
| 67 | [mnfst/manifest](https://github.com/mnfst/manifest) | +240 | 5627 |
| 68 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +237 | 2877 |
| 69 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +237 | 37089 |
| 70 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +235 | 37330 |
| 71 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +228 | 4943 |
| 72 | [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | +226 | 1506 |
| 73 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +226 | 3758 |
| 74 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +224 | 32492 |
| 75 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +220 | 40189 |
| 76 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +220 | 21765 |
| 77 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +219 | 1960 |
| 78 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +218 | 1980 |
| 79 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +215 | 31131 |
| 80 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +215 | 10417 |
| 81 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +214 | 19502 |
| 82 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +212 | 13301 |
| 83 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +211 | 3977 |
| 84 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | +210 | 1575 |
| 85 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +208 | 2442 |
| 86 | [android/skills](https://github.com/android/skills) | +205 | 4268 |
| 87 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +204 | 28750 |
| 88 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +202 | 34941 |
| 89 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +198 | 3102 |
| 90 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +197 | 40800 |
| 91 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +197 | 39841 |
| 92 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +194 | 19200 |
| 93 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +187 | 8226 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +185 | 28643 |
| 95 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +185 | 1680 |
| 96 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +178 | 12601 |
| 97 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +177 | 11839 |
| 98 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +174 | 5684 |
| 99 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +174 | 1545 |
| 100 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +172 | 15944 |
| 101 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +172 | 2152 |
| 102 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +171 | 28381 |
| 103 | [pascalorg/editor](https://github.com/pascalorg/editor) | +170 | 14296 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +162 | 10590 |
| 105 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +162 | 38612 |
| 106 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +161 | 40956 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +159 | 6032 |
| 108 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +149 | 31262 |
| 109 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +145 | 36799 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +135 | 11438 |
| 111 | [the-hidden-fish/advisor-ledger](https://github.com/the-hidden-fish/advisor-ledger) | +133 | 1053 |
| 112 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +131 | 4335 |
| 113 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +126 | 40779 |
| 114 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +123 | 1462 |
| 115 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +119 | 31136 |
| 116 | [OranAi-Ltd/oransim](https://github.com/OranAi-Ltd/oransim) | +117 | 930 |
| 117 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +116 | 1618 |
| 118 | [Lazarus-AI/clearwing](https://github.com/Lazarus-AI/clearwing) | +112 | 903 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +108 | 11698 |
| 120 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +108 | 2412 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25259 | 188113 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17572 | 115010 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12035 | 64765 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +10925 | 83382 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9741 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +8848 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7810 | 49454 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7486 | 45756 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7014 | 39193 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6873 | 45270 |
| 11 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5778 | 82475 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5725 | 34266 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5303 | 224760 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5184 | 69674 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4628 | 24215 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4462 | 32578 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4303 | 30678 |
| 18 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4174 | 28643 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4170 | 86407 |
| 20 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4150 | 47867 |
| 21 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4149 | 58501 |
| 22 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4092 | 22663 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4066 | 25576 |
| 24 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3658 | 76308 |
| 25 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3478 | 20630 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3449 | 74774 |
| 27 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +3320 | 63666 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3306 | 34500 |
| 29 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3201 | 109881 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3193 | 34148 |
| 31 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3007 | 31131 |
| 32 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2806 | 56253 |
| 33 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2763 | 16850 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2759 | 50640 |
| 35 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2743 | 23862 |
| 36 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2694 | 16501 |
| 37 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2607 | 40956 |
| 38 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2549 | 57188 |
| 39 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2522 | 57062 |
| 40 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2492 | 14470 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2429 | 15961 |
| 42 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2386 | 85286 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2109 | 11141 |
| 44 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2057 | 18053 |
| 45 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2031 | 12440 |
| 46 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2020 | 30590 |
| 47 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1981 | 28381 |
| 48 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1943 | 21354 |
| 49 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1904 | 31098 |
| 50 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1876 | 39577 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1875 | 33878 |
| 52 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1862 | 17163 |
| 53 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1845 | 79656 |
| 54 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1827 | 14304 |
| 55 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1811 | 10003 |
| 56 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1798 | 15836 |
| 57 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1776 | 21261 |
| 58 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1711 | 28798 |
| 59 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1708 | 19200 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1704 | 12949 |
| 61 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1689 | 15990 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1647 | 26268 |
| 63 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1644 | 32492 |
| 64 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1514 | 24857 |
| 65 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1513 | 25436 |
| 66 | [openai/codex](https://github.com/openai/codex) | +1496 | 61744 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1476 | 28534 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1454 | 40400 |
| 69 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1425 | 52464 |
| 70 | [github/spec-kit](https://github.com/github/spec-kit) | +1425 | 71722 |
| 71 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1418 | 11724 |
| 72 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1418 | 18480 |
| 73 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1399 | 6516 |
| 74 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1391 | 73135 |
| 75 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1389 | 40800 |
| 76 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1379 | 50101 |
| 77 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1375 | 14296 |
| 78 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1358 | 8482 |
| 79 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1356 | 23098 |
| 80 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1343 | 37330 |
| 81 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1330 | 98536 |
| 82 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1330 | 42755 |
| 83 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1327 | 33141 |
| 84 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1322 | 45886 |
| 85 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1321 | 6693 |
| 86 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1312 | 21765 |
| 87 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1293 | 21969 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1263 | 24443 |
| 89 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1256 | 18015 |
| 90 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1254 | 20601 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1251 | 34941 |
| 92 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1241 | 10433 |
| 93 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1236 | 18149 |
| 94 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1203 | 95754 |
| 95 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1162 | 5880 |
| 96 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1130 | 12641 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1105 | 15188 |
| 98 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +978 | 6032 |
| 99 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +971 | 38612 |
| 100 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +961 | 31262 |
| 101 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +956 | 9004 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +947 | 78902 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +944 | 12601 |
| 104 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +928 | 30213 |
| 105 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +905 | 6515 |
| 106 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +895 | 11839 |
| 107 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +894 | 5690 |
| 108 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +886 | 6835 |
| 109 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +884 | 55070 |
| 110 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +849 | 52700 |
| 111 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +827 | 7749 |
| 112 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +824 | 4775 |
| 113 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +821 | 6802 |
| 114 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +813 | 39841 |
| 115 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +804 | 4335 |
| 116 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +795 | 24979 |
| 117 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +793 | 4249 |
| 118 | [google/magika](https://github.com/google/magika) | +785 | 16628 |
| 119 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +784 | 47122 |
| 120 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +768 | 40779 |
| 121 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +760 | 21710 |
| 122 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +747 | 5604 |
| 123 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +736 | 24324 |
| 124 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +732 | 4062 |
| 125 | [jundot/omlx](https://github.com/jundot/omlx) | +731 | 11438 |
| 126 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +731 | 9562 |
| 127 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +729 | 4027 |
| 128 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +728 | 4943 |
| 129 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +727 | 11698 |
| 130 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +725 | 10590 |
| 131 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +724 | 7587 |
| 132 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +672 | 36799 |
| 133 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +656 | 34208 |
| 134 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +656 | 23006 |
| 135 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +655 | 54903 |
| 136 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +643 | 3977 |
| 137 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +637 | 31136 |
| 138 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +637 | 49621 |
| 139 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +631 | 8460 |
| 140 | [eze-is/web-access](https://github.com/eze-is/web-access) | +627 | 5626 |
| 141 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +589 | 11519 |
| 142 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +573 | 24589 |
| 143 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +572 | 7435 |
| 144 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +569 | 18543 |
| 145 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +562 | 30586 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +560 | 19352 |
| 147 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +551 | 37564 |
| 148 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +549 | 11599 |
| 149 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +540 | 17738 |
| 150 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +536 | 3430 |
| 151 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +530 | 3089 |
| 152 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +525 | 2558 |
| 153 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +514 | 3154 |
| 154 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +509 | 3758 |
| 155 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +506 | 25744 |
| 156 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +505 | 2846 |
| 157 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +504 | 17088 |
| 158 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +501 | 2398 |
| 159 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +479 | 2612 |
| 160 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +472 | 30275 |
| 161 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +461 | 19814 |
| 162 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +446 | 6694 |
| 163 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +443 | 44545 |
| 164 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +443 | 2309 |
| 165 | [cft0808/edict](https://github.com/cft0808/edict) | +439 | 15436 |
| 166 | [usestrix/strix](https://github.com/usestrix/strix) | +434 | 24550 |
| 167 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +432 | 15925 |
| 168 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +423 | 2474 |
| 169 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +418 | 6617 |
| 170 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +415 | 9452 |
| 171 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +412 | 11360 |
| 172 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +403 | 19536 |
| 173 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +400 | 36907 |
| 174 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +398 | 2814 |
| 175 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +396 | 3416 |
| 176 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +393 | 2149 |
| 177 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +380 | 1951 |
| 178 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +378 | 2877 |
| 179 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +372 | 2977 |
| 180 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +366 | 23944 |
| 181 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +362 | 2213 |
| 182 | [floci-io/floci](https://github.com/floci-io/floci) | +356 | 4166 |
| 183 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +355 | 9071 |
| 184 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +349 | 2152 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +346 | 12439 |
| 186 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +337 | 25660 |
| 187 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +310 | 3212 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +300 | 5713 |
| 189 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +294 | 6436 |
| 190 | [decolua/9router](https://github.com/decolua/9router) | +284 | 3029 |
| 191 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +278 | 3085 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +273 | 36103 |
| 193 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +250 | 7148 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +250 | 1783 |
| 195 | [88lin/video_vip](https://github.com/88lin/video_vip) | +221 | 1502 |
| 196 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +213 | 2760 |
| 197 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +212 | 26177 |
| 198 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +207 | 11300 |
| 199 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +204 | 7294 |
| 200 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +202 | 15805 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +197 | 8763 |
| 202 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +195 | 4227 |
| 203 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +194 | 33712 |
| 204 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +193 | 13031 |
| 205 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +192 | 7921 |
| 206 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +192 | 3077 |
| 207 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +189 | 5525 |
| 208 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +180 | 23768 |
| 209 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +175 | 2592 |
| 210 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +172 | 547 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +169 | 41086 |
| 212 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +168 | 2517 |
| 213 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +161 | 809 |
| 214 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +156 | 982 |
| 215 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +156 | 3947 |
| 216 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +156 | 1662 |
| 217 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +146 | 1494 |
| 218 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +146 | 40265 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +143 | 35473 |
| 220 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +142 | 22363 |
| 221 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +136 | 760 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +121 | 1749 |
| 223 | [clawplays/ospec](https://github.com/clawplays/ospec) | +119 | 605 |
| 224 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +118 | 671 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +118 | 29715 |
| 226 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +117 | 29725 |
| 227 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +116 | 1850 |
| 228 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +115 | 5431 |
| 229 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +114 | 23512 |
| 230 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +112 | 3072 |
| 231 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +111 | 14253 |
| 232 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +109 | 7326 |
| 233 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +109 | 10864 |
| 234 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +107 | 19177 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +105 | 26810 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +103 | 33000 |
| 237 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +102 | 6767 |
| 238 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +101 | 634 |
| 239 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +100 | 39596 |
| 240 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +99 | 749 |
| 241 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +99 | 1908 |
| 242 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +99 | 1375 |
| 243 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +97 | 2005 |
| 244 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +97 | 12883 |
| 245 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 246 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +94 | 966 |
| 247 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +94 | 633 |
| 248 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +93 | 619 |
| 249 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +93 | 1414 |
| 250 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +91 | 527 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 1796 |
| 252 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +89 | 1153 |
| 253 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +88 | 723 |
| 254 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 460 |
| 255 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +88 | 1037 |
| 256 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +87 | 805 |
| 257 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3323 |
| 258 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +83 | 623 |
| 259 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +82 | 4046 |
| 260 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +82 | 509 |
| 261 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +82 | 48784 |
| 262 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +81 | 466 |
| 263 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +81 | 3842 |
| 264 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +80 | 2322 |
| 265 | [openmemind/memind](https://github.com/openmemind/memind) | +80 | 519 |
| 266 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +80 | 45263 |
| 267 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +80 | 2765 |
| 268 | [robinebers/openusage](https://github.com/robinebers/openusage) | +78 | 2025 |
| 269 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +78 | 692 |
| 270 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +78 | 1166 |
| 271 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +76 | 764 |
| 272 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +76 | 1724 |
| 273 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +75 | 659 |
| 274 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +74 | 947 |
| 275 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +74 | 2726 |
| 276 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +74 | 3665 |
| 277 | [microg/GmsCore](https://github.com/microg/GmsCore) | +71 | 13024 |
| 278 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +70 | 397 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9378 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +66 | 27357 |
| 281 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +65 | 1454 |
| 282 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +63 | 377 |
| 283 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +63 | 4063 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7322 |
| 285 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +62 | 11750 |
| 286 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +58 | 564 |
| 287 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +58 | 313 |
| 288 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1684 |
| 289 | [iamzifei/show-me-the-money](https://github.com/iamzifei/show-me-the-money) | +57 | 333 |
| 290 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 291 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 28969 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +52 | 1789 |
| 293 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +51 | 1863 |
| 294 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +50 | 11684 |
| 295 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +50 | 25436 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +49 | 31476 |
| 297 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +43 | 421 |
| 298 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +43 | 582 |
| 299 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +43 | 8576 |
| 300 | [risin42/NagramX](https://github.com/risin42/NagramX) | +41 | 1716 |
