---
title: "2026-04-20 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+953 2.FinceptTerminal+638 3.PLFM_RADAR+317 4.caveman+301 5.Claude-Code-Game-Studios+266"
date: 2026-04-20T20:51:25+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-20 20:51:25

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
        'daily': {"categories": ["byoungd/English-level-up-tips", "paperless-ngx/paperless-ngx", "titanwings/colleague-skill", "mnfst/awesome-free-llm-apis", "NanmiCoder/cc-haha", "jamiepine/voicebox", "thunderbird/thunderbolt", "safishamsi/graphify", "webadderall/Recordly", "multica-ai/multica", "elder-plinius/CL4R1T4S", "BasedHardware/omi", "openai/openai-agents-python", "rtk-ai/rtk", "VoltAgent/awesome-design-md", "Donchitos/Claude-Code-Game-Studios", "JuliusBrussee/caveman", "NawfalMotii79/PLFM_RADAR", "Fincept-Corporation/FinceptTerminal", "forrestchang/andrej-karpathy-skills"], "data": [135, 136, 136, 141, 141, 150, 161, 161, 165, 167, 181, 183, 206, 218, 234, 266, 301, 317, 638, 953]},
        'weekly': {"categories": ["lsdefine/GenericAgent", "BasedHardware/omi", "santifer/career-ops", "EvoMap/evolver", "google/magika", "rtk-ai/rtk", "jamiepine/voicebox", "Donchitos/Claude-Code-Game-Studios", "shanraisshan/claude-code-best-practice", "safishamsi/graphify", "multica-ai/multica", "Fincept-Corporation/FinceptTerminal", "garrytan/gstack", "obra/superpowers", "NawfalMotii79/PLFM_RADAR", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [622, 657, 672, 702, 747, 817, 857, 858, 903, 1022, 1077, 1099, 1215, 1772, 1798, 1838, 1977, 1998, 4626, 6274]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "shanraisshan/claude-code-best-practice", "Gitlawb/openclaude", "bytedance/deer-flow", "msitarzewski/agency-agents", "karpathy/autoresearch", "anthropics/claude-code", "safishamsi/graphify", "openclaw/openclaw", "santifer/career-ops", "chenglou/pretext", "JuliusBrussee/caveman", "MemPalace/mempalace", "garrytan/gstack", "forrestchang/andrej-karpathy-skills", "obra/superpowers", "VoltAgent/awesome-design-md", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4400, 4441, 4478, 4770, 4967, 5200, 5327, 5344, 6536, 6729, 6823, 6887, 7691, 7899, 8796, 9991, 11611, 11903, 16767, 25062]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +953 | 65953 |
| 2 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +638 | 9266 |
| 3 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +317 | 16973 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +301 | 40498 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +266 | 14346 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +234 | 61393 |
| 7 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +218 | 30809 |
| 8 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +206 | 23874 |
| 9 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +183 | 11600 |
| 10 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +181 | 18547 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +167 | 17530 |
| 12 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +165 | 9961 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +161 | 31325 |
| 14 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +161 | 2751 |
| 15 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +150 | 21673 |
| 16 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +141 | 7443 |
| 17 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +141 | 3213 |
| 18 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +136 | 15780 |
| 19 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +136 | 36907 |
| 20 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +135 | 41523 |
| 21 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +123 | 48113 |
| 22 | [santifer/career-ops](https://github.com/santifer/career-ops) | +117 | 36967 |
| 23 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +115 | 5980 |
| 24 | [mnfst/manifest](https://github.com/mnfst/manifest) | +111 | 5325 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +110 | 47811 |
| 26 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +108 | 3969 |
| 27 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +106 | 20444 |
| 28 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +104 | 11883 |
| 29 | [88lin/video_vip](https://github.com/88lin/video_vip) | +98 | 1314 |
| 30 | [PerryTS/perry](https://github.com/PerryTS/perry) | +97 | 806 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6274 | 65953 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4626 | 105121 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1998 | 40498 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1977 | 61393 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1838 | 30678 |
| 6 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1798 | 16973 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +1772 | 60312 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1215 | 78546 |
| 9 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1099 | 9266 |
| 10 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1077 | 17530 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1022 | 31325 |
| 12 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +903 | 46886 |
| 13 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +858 | 14346 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +857 | 21673 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +817 | 30809 |
| 16 | [google/magika](https://github.com/google/magika) | +747 | 16299 |
| 17 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +702 | 5980 |
| 18 | [santifer/career-ops](https://github.com/santifer/career-ops) | +672 | 36967 |
| 19 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +657 | 11600 |
| 20 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +622 | 4989 |
| 21 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +607 | 45886 |
| 22 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +602 | 56786 |
| 23 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +597 | 18220 |
| 24 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +574 | 48459 |
| 25 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +555 | 23874 |
| 26 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +554 | 47811 |
| 27 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +544 | 3897 |
| 28 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +529 | 18548 |
| 29 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +527 | 13143 |
| 30 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +506 | 20444 |
| 31 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +495 | 15115 |
| 32 | [android/skills](https://github.com/android/skills) | +478 | 3813 |
| 33 | [pascalorg/editor](https://github.com/pascalorg/editor) | +473 | 13793 |
| 34 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +466 | 19819 |
| 35 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +459 | 2751 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +422 | 38908 |
| 37 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +418 | 2237 |
| 38 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +414 | 9961 |
| 39 | [AgentSeal/codeburn](https://github.com/AgentSeal/codeburn) | +412 | 3024 |
| 40 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +411 | 10441 |
| 41 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +404 | 24562 |
| 42 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +402 | 3969 |
| 43 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +400 | 37861 |
| 44 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +391 | 2201 |
| 45 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +381 | 11883 |
| 46 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +380 | 9678 |
| 47 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +374 | 55126 |
| 48 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +370 | 5551 |
| 49 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +363 | 31583 |
| 50 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +362 | 5967 |
| 51 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +339 | 15780 |
| 52 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +326 | 25541 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +314 | 27489 |
| 54 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +313 | 6806 |
| 55 | [momenbasel/PureMac](https://github.com/momenbasel/PureMac) | +312 | 2941 |
| 56 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +301 | 30280 |
| 57 | [mattpocock/skills](https://github.com/mattpocock/skills) | +300 | 16644 |
| 58 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +296 | 33311 |
| 59 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +294 | 3884 |
| 60 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +292 | 22886 |
| 61 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +292 | 20878 |
| 62 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +289 | 18572 |
| 63 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +285 | 27839 |
| 64 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +285 | 2122 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +283 | 13898 |
| 66 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +278 | 7443 |
| 67 | [tw93/Mole](https://github.com/tw93/Mole) | +275 | 36870 |
| 68 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +272 | 41522 |
| 69 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +262 | 4443 |
| 70 | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | +262 | 1641 |
| 71 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +261 | 37330 |
| 72 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +260 | 49919 |
| 73 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +259 | 4195 |
| 74 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +257 | 36391 |
| 75 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +256 | 34164 |
| 76 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +245 | 31857 |
| 77 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +243 | 5177 |
| 78 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +240 | 22978 |
| 79 | [coleam00/Archon](https://github.com/coleam00/Archon) | +238 | 19063 |
| 80 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +235 | 48113 |
| 81 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +234 | 36907 |
| 82 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +233 | 27866 |
| 83 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +228 | 1910 |
| 84 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +227 | 22467 |
| 85 | [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | +226 | 1415 |
| 86 | [chenglou/pretext](https://github.com/chenglou/pretext) | +224 | 44818 |
| 87 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +223 | 12063 |
| 88 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +220 | 15577 |
| 89 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +216 | 8377 |
| 90 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +214 | 18672 |
| 91 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +214 | 39908 |
| 92 | [mnfst/manifest](https://github.com/mnfst/manifest) | +213 | 5325 |
| 93 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +210 | 1968 |
| 94 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +208 | 10140 |
| 95 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +204 | 38064 |
| 96 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +198 | 11651 |
| 97 | [tractorjuice/arc-kit](https://github.com/tractorjuice/arc-kit) | +196 | 1292 |
| 98 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +196 | 40454 |
| 99 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +191 | 16547 |
| 100 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +188 | 2961 |
| 101 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +188 | 39841 |
| 102 | [patterniha/SNI-Spoofing](https://github.com/patterniha/SNI-Spoofing) | +184 | 1118 |
| 103 | [google-research/timesfm](https://github.com/google-research/timesfm) | +184 | 18220 |
| 104 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +181 | 2800 |
| 105 | [88lin/video_vip](https://github.com/88lin/video_vip) | +180 | 1314 |
| 106 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +169 | 30659 |
| 107 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +165 | 2390 |
| 108 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +163 | 3214 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +163 | 10858 |
| 110 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +162 | 27774 |
| 111 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +148 | 33912 |
| 112 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +140 | 6551 |
| 113 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +137 | 20142 |
| 114 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +134 | 1677 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +134 | 9875 |
| 116 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +133 | 40218 |
| 117 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +133 | 30572 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +133 | 36799 |
| 119 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +132 | 30164 |
| 120 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +125 | 1043 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25062 | 186693 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +16767 | 105121 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +11903 | 51199 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11611 | 61393 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +9991 | 60312 |
| 6 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8796 | 65953 |
| 7 | [garrytan/gstack](https://github.com/garrytan/gstack) | +7899 | 78546 |
| 8 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7691 | 48459 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +6887 | 40498 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6823 | 44818 |
| 11 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6729 | 36967 |
| 12 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +6536 | 224760 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5344 | 31325 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5327 | 69674 |
| 15 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +5200 | 74919 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4967 | 84050 |
| 17 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4770 | 62969 |
| 18 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4478 | 22886 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4441 | 46886 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4400 | 31583 |
| 21 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4358 | 56786 |
| 22 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4220 | 30678 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4107 | 27839 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3965 | 24562 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +3802 | 74774 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3636 | 109881 |
| 27 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3599 | 18220 |
| 28 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3487 | 34148 |
| 29 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3483 | 24601 |
| 30 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3404 | 56473 |
| 31 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3310 | 55126 |
| 32 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3211 | 30590 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3194 | 30809 |
| 34 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3116 | 17530 |
| 35 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3106 | 55355 |
| 36 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3045 | 30280 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2776 | 47811 |
| 38 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2723 | 16482 |
| 39 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2681 | 22979 |
| 40 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2628 | 85286 |
| 41 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2599 | 15780 |
| 42 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2573 | 40454 |
| 43 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2364 | 16568 |
| 44 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2357 | 15298 |
| 45 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2337 | 30164 |
| 46 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2304 | 13143 |
| 47 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2172 | 18572 |
| 48 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +2155 | 14346 |
| 49 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2112 | 31857 |
| 50 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2004 | 12048 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1999 | 33878 |
| 52 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1979 | 37861 |
| 53 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1927 | 9678 |
| 54 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1925 | 27774 |
| 55 | [block/goose](https://github.com/block/goose) | +1920 | 31098 |
| 56 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1907 | 20122 |
| 57 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1906 | 16973 |
| 58 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1898 | 13793 |
| 59 | [github/spec-kit](https://github.com/github/spec-kit) | +1868 | 71722 |
| 60 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1861 | 28190 |
| 61 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1847 | 20444 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1847 | 25541 |
| 63 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1819 | 11883 |
| 64 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1788 | 9845 |
| 65 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1760 | 79656 |
| 66 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1717 | 15115 |
| 67 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1702 | 39908 |
| 68 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1686 | 10963 |
| 69 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1623 | 19819 |
| 70 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1612 | 16644 |
| 71 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1608 | 32537 |
| 72 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1606 | 13939 |
| 73 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1593 | 20878 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1543 | 27489 |
| 75 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1502 | 49919 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1501 | 61744 |
| 77 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1501 | 48113 |
| 78 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1478 | 38908 |
| 79 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1450 | 37330 |
| 80 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1422 | 41522 |
| 81 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1416 | 11694 |
| 82 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1398 | 98536 |
| 83 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1393 | 18220 |
| 84 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1389 | 73135 |
| 85 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1375 | 34164 |
| 86 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1375 | 78902 |
| 87 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1367 | 6250 |
| 88 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1319 | 6701 |
| 89 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1298 | 17903 |
| 90 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1271 | 21657 |
| 91 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1266 | 45886 |
| 92 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1250 | 21674 |
| 93 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1241 | 22467 |
| 94 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1233 | 9961 |
| 95 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1213 | 7443 |
| 96 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1191 | 95754 |
| 97 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1155 | 30659 |
| 98 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1148 | 5779 |
| 99 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1131 | 13898 |
| 100 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1119 | 9266 |
| 101 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1074 | 38064 |
| 102 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1013 | 22647 |
| 103 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1008 | 21358 |
| 104 | [coleam00/Archon](https://github.com/coleam00/Archon) | +1007 | 19063 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +998 | 12063 |
| 106 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +965 | 39841 |
| 107 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +951 | 8954 |
| 108 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +945 | 52700 |
| 109 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +922 | 5551 |
| 110 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +918 | 49621 |
| 111 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +888 | 6401 |
| 112 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +887 | 24357 |
| 113 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +883 | 11651 |
| 114 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +882 | 40218 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +879 | 11291 |
| 116 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +878 | 5542 |
| 117 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +820 | 24126 |
| 118 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +808 | 4657 |
| 119 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +798 | 6806 |
| 120 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +789 | 33912 |
| 121 | [jundot/omlx](https://github.com/jundot/omlx) | +785 | 10858 |
| 122 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +766 | 9875 |
| 123 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +754 | 11430 |
| 124 | [google/magika](https://github.com/google/magika) | +753 | 16299 |
| 125 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +753 | 3901 |
| 126 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +745 | 5576 |
| 127 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +741 | 3884 |
| 128 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +738 | 9492 |
| 129 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +738 | 5980 |
| 130 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +722 | 17413 |
| 131 | [eze-is/web-access](https://github.com/eze-is/web-access) | +718 | 5380 |
| 132 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +717 | 3944 |
| 133 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +711 | 30333 |
| 134 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +702 | 4443 |
| 135 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +700 | 7101 |
| 136 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +699 | 3840 |
| 137 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +692 | 30572 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +676 | 36799 |
| 139 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +672 | 54903 |
| 140 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +666 | 23874 |
| 141 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +654 | 4989 |
| 142 | [floci-io/floci](https://github.com/floci-io/floci) | +644 | 4000 |
| 143 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +614 | 37564 |
| 144 | [cft0808/edict](https://github.com/cft0808/edict) | +593 | 15318 |
| 145 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +585 | 18987 |
| 146 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +583 | 11500 |
| 147 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +569 | 8921 |
| 148 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +568 | 47122 |
| 149 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +566 | 47936 |
| 150 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +537 | 25548 |
| 151 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +530 | 2961 |
| 152 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +529 | 19642 |
| 153 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +523 | 4882 |
| 154 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +519 | 16702 |
| 155 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +517 | 2464 |
| 156 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +509 | 3247 |
| 157 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +509 | 6551 |
| 158 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +507 | 3095 |
| 159 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +505 | 2678 |
| 160 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +498 | 2793 |
| 161 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +497 | 5417 |
| 162 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +495 | 29762 |
| 163 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +494 | 2800 |
| 164 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +493 | 4393 |
| 165 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +484 | 3214 |
| 166 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +472 | 15681 |
| 167 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +471 | 44545 |
| 168 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +471 | 4432 |
| 169 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +466 | 3232 |
| 170 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +458 | 11228 |
| 171 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +456 | 19136 |
| 172 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +443 | 19175 |
| 173 | [usestrix/strix](https://github.com/usestrix/strix) | +440 | 24286 |
| 174 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +430 | 20142 |
| 175 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +430 | 2149 |
| 176 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +426 | 3195 |
| 177 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +423 | 9173 |
| 178 | [wshobson/agents](https://github.com/wshobson/agents) | +410 | 33961 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +393 | 2797 |
| 180 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +391 | 2114 |
| 181 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +391 | 12985 |
| 182 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +379 | 2035 |
| 183 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +375 | 1932 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +375 | 12209 |
| 185 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +357 | 2839 |
| 186 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +356 | 23670 |
| 187 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +355 | 25410 |
| 188 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +318 | 3095 |
| 189 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +306 | 5448 |
| 190 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +306 | 2684 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +282 | 36103 |
| 192 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +279 | 3062 |
| 193 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +278 | 3014 |
| 194 | [decolua/9router](https://github.com/decolua/9router) | +276 | 2755 |
| 195 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +274 | 5942 |
| 196 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +248 | 7843 |
| 197 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +244 | 1469 |
| 198 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +239 | 4198 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +226 | 25947 |
| 200 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +222 | 11204 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +221 | 9335 |
| 202 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +215 | 6080 |
| 203 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +212 | 15675 |
| 204 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +210 | 7103 |
| 205 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +209 | 6464 |
| 206 | [88lin/video_vip](https://github.com/88lin/video_vip) | +203 | 1314 |
| 207 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +200 | 2447 |
| 208 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +199 | 951 |
| 209 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +191 | 3020 |
| 210 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +190 | 33712 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +183 | 560 |
| 212 | [usebruno/bruno](https://github.com/usebruno/bruno) | +181 | 41086 |
| 213 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +180 | 2465 |
| 214 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +179 | 23713 |
| 215 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +177 | 1513 |
| 216 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +177 | 1011 |
| 217 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +160 | 793 |
| 218 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +154 | 3887 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +153 | 40265 |
| 220 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +151 | 2720 |
| 221 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +150 | 22249 |
| 222 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +142 | 880 |
| 223 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +141 | 1429 |
| 224 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +141 | 35473 |
| 225 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +138 | 1805 |
| 226 | [dashersw/gea](https://github.com/dashersw/gea) | +134 | 964 |
| 227 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +128 | 29673 |
| 228 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +127 | 1650 |
| 229 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +122 | 29666 |
| 230 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +118 | 5338 |
| 231 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +117 | 10810 |
| 232 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +115 | 1087 |
| 233 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +115 | 839 |
| 234 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +113 | 23424 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +110 | 12787 |
| 236 | [clawplays/ospec](https://github.com/clawplays/ospec) | +109 | 576 |
| 237 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +108 | 5774 |
| 238 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +107 | 601 |
| 239 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +106 | 1736 |
| 240 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +106 | 1348 |
| 241 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +105 | 1851 |
| 242 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +102 | 1976 |
| 243 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +102 | 994 |
| 244 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +99 | 6693 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +99 | 33000 |
| 246 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +98 | 1357 |
| 247 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +98 | 959 |
| 248 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 361 |
| 249 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +93 | 7129 |
| 250 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +92 | 1195 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +92 | 48784 |
| 252 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +91 | 695 |
| 253 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +89 | 598 |
| 254 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +88 | 854 |
| 255 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +88 | 3997 |
| 256 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +88 | 1147 |
| 257 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +88 | 620 |
| 258 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +88 | 562 |
| 259 | [crimera/piko](https://github.com/crimera/piko) | +88 | 3270 |
| 260 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +87 | 1072 |
| 261 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +87 | 606 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +84 | 471 |
| 263 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +83 | 2267 |
| 264 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +83 | 2670 |
| 265 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +82 | 445 |
| 266 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +81 | 3619 |
| 267 | [robinebers/openusage](https://github.com/robinebers/openusage) | +80 | 1980 |
| 268 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3765 |
| 269 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +80 | 1662 |
| 270 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +78 | 900 |
| 271 | [microg/GmsCore](https://github.com/microg/GmsCore) | +78 | 12986 |
| 272 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 273 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +76 | 434 |
| 274 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +76 | 363 |
| 275 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +74 | 820 |
| 276 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +73 | 748 |
| 277 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +71 | 484 |
| 278 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +70 | 27308 |
| 279 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +68 | 605 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +68 | 9322 |
| 281 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +67 | 476 |
| 282 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +67 | 1421 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +62 | 11682 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +61 | 7287 |
| 285 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +61 | 37313 |
| 286 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +60 | 312 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1643 |
| 288 | [idinging/freemail](https://github.com/idinging/freemail) | +56 | 1381 |
| 289 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +55 | 1824 |
| 290 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +55 | 25427 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +54 | 31476 |
| 292 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +53 | 28961 |
| 293 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +51 | 263 |
| 294 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +51 | 1737 |
| 295 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +46 | 11659 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +43 | 8538 |
| 297 | [risin42/NagramX](https://github.com/risin42/NagramX) | +42 | 1694 |
| 298 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 123 |
| 299 | [is-a-dev/register](https://github.com/is-a-dev/register) | +36 | 10147 |
| 300 | [hoo-dles/morphe-patches](https://github.com/hoo-dles/morphe-patches) | +36 | 393 |
