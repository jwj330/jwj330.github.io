---
title: "2026-05-03 GitHub增长趋势报告"
description: "1.TradingAgents+726 2.skills+465 3.ruflo+373 4.Scrapling+323 5.maigret+273"
date: 2026-05-03T20:46:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-03 20:46:45

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
        'daily': {"categories": ["OpenBMB/VoxCPM", "AIDC-AI/Pixelle-Video", "Fincept-Corporation/FinceptTerminal", "shanraisshan/claude-code-best-practice", "browser-use/browser-harness", "webadderallorg/Recordly", "virattt/dexter", "ShareX/ShareX", "rtk-ai/rtk", "Alishahryar1/free-claude-code", "1jehuang/jcode", "withastro/flue", "abhigyanpatwari/GitNexus", "safishamsi/graphify", "warpdotdev/warp", "soxoj/maigret", "D4Vinci/Scrapling", "ruvnet/ruflo", "mattpocock/skills", "TauricResearch/TradingAgents"], "data": [85, 88, 93, 96, 100, 111, 115, 120, 126, 133, 138, 146, 152, 199, 230, 273, 323, 373, 465, 726]},
        'weekly': {"categories": ["openai/symphony", "microsoft/VibeVoice", "addyosmani/agent-skills", "refactoringhq/tolaria", "soxoj/maigret", "Fincept-Corporation/FinceptTerminal", "rtk-ai/rtk", "D4Vinci/Scrapling", "JuliusBrussee/caveman", "ruvnet/ruflo", "abhigyanpatwari/GitNexus", "farion1231/cc-switch", "Z4nzu/hackingtool", "safishamsi/graphify", "Alishahryar1/free-claude-code", "TauricResearch/TradingAgents", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "warpdotdev/warp", "mattpocock/skills"], "data": [517, 524, 531, 548, 550, 561, 580, 604, 619, 681, 684, 798, 856, 862, 1181, 1515, 1618, 2447, 2492, 4038]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "Gitlawb/openclaude", "rtk-ai/rtk", "multica-ai/multica", "msitarzewski/agency-agents", "garrytan/gstack", "thedotmack/claude-mem", "openclaw/openclaw", "addyosmani/agent-skills", "mattpocock/skills", "safishamsi/graphify", "affaan-m/everything-claude-code", "obra/superpowers", "ultraworkers/claw-code", "santifer/career-ops", "MemPalace/mempalace", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [3495, 3527, 3723, 3804, 3805, 4248, 4329, 4340, 4742, 5803, 6772, 6785, 7057, 7365, 7465, 8053, 8355, 12183, 14800, 18373]}
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
| 1 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +726 | 30590 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +465 | 56824 |
| 3 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +373 | 38660 |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +323 | 42878 |
| 5 | [soxoj/maigret](https://github.com/soxoj/maigret) | +273 | 23667 |
| 6 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +230 | 53481 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +199 | 41714 |
| 8 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +152 | 35160 |
| 9 | [withastro/flue](https://github.com/withastro/flue) | +146 | 2062 |
| 10 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +138 | 3363 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +133 | 20643 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +126 | 40595 |
| 13 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +120 | 35707 |
| 14 | [virattt/dexter](https://github.com/virattt/dexter) | +115 | 22584 |
| 15 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +111 | 12223 |
| 16 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +100 | 9946 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +96 | 50723 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +93 | 19481 |
| 19 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +88 | 9841 |
| 20 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +85 | 17209 |
| 21 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +83 | 6118 |
| 22 | [openai/symphony](https://github.com/openai/symphony) | +83 | 20970 |
| 23 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +78 | 10750 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +78 | 24052 |
| 25 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +76 | 14843 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +64 | 24619 |
| 27 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +64 | 4494 |
| 28 | [santifer/career-ops](https://github.com/santifer/career-ops) | +63 | 42129 |
| 29 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +63 | 2360 |
| 30 | [browserbase/skills](https://github.com/browserbase/skills) | +63 | 1777 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4038 | 56825 |
| 2 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2492 | 53481 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2447 | 108568 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1618 | 131041 |
| 5 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1515 | 30590 |
| 6 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1181 | 20643 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +862 | 41714 |
| 8 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +856 | 55070 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +798 | 58417 |
| 10 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +684 | 35160 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +681 | 38660 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +619 | 52992 |
| 13 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +604 | 42878 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +580 | 40595 |
| 15 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +561 | 19481 |
| 16 | [soxoj/maigret](https://github.com/soxoj/maigret) | +550 | 23667 |
| 17 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +548 | 9178 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +531 | 27395 |
| 19 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +524 | 46369 |
| 20 | [openai/symphony](https://github.com/openai/symphony) | +517 | 20970 |
| 21 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +500 | 6118 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +451 | 44146 |
| 23 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +394 | 3416 |
| 24 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +360 | 9946 |
| 25 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +360 | 14078 |
| 26 | [multica-ai/multica](https://github.com/multica-ai/multica) | +353 | 24052 |
| 27 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +337 | 3363 |
| 28 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +332 | 50723 |
| 29 | [withastro/flue](https://github.com/withastro/flue) | +328 | 2062 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +326 | 10932 |
| 31 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +319 | 11057 |
| 32 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +298 | 9841 |
| 33 | [santifer/career-ops](https://github.com/santifer/career-ops) | +292 | 42129 |
| 34 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +274 | 4741 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +272 | 24619 |
| 36 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +264 | 17032 |
| 37 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +258 | 10750 |
| 38 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +252 | 17393 |
| 39 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +247 | 12262 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +238 | 33848 |
| 41 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +237 | 28462 |
| 42 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +235 | 12223 |
| 43 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +235 | 4354 |
| 44 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +225 | 5625 |
| 45 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +225 | 13509 |
| 46 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +222 | 4759 |
| 47 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +219 | 14900 |
| 48 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +218 | 30943 |
| 49 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +216 | 15075 |
| 50 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +214 | 17209 |
| 51 | [gastownhall/beads](https://github.com/gastownhall/beads) | +214 | 23049 |
| 52 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +213 | 34475 |
| 53 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +210 | 8923 |
| 54 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +203 | 7875 |
| 55 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +199 | 42351 |
| 56 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +197 | 3199 |
| 57 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +197 | 44978 |
| 58 | [blader/humanizer](https://github.com/blader/humanizer) | +195 | 17026 |
| 59 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +186 | 3390 |
| 60 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +183 | 8542 |
| 61 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +182 | 23091 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +182 | 30450 |
| 63 | [virattt/dexter](https://github.com/virattt/dexter) | +181 | 22584 |
| 64 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +181 | 2614 |
| 65 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +181 | 4270 |
| 66 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +179 | 3245 |
| 67 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +177 | 30396 |
| 68 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +169 | 26310 |
| 69 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +169 | 57938 |
| 70 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +168 | 12928 |
| 71 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +164 | 22603 |
| 72 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +164 | 5133 |
| 73 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +163 | 1619 |
| 74 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +161 | 20059 |
| 75 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +160 | 27318 |
| 76 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +159 | 18583 |
| 77 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +159 | 2444 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +158 | 21049 |
| 79 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +153 | 11553 |
| 80 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +152 | 12862 |
| 81 | [genlayerlabs/genlayer-project-boilerplate](https://github.com/genlayerlabs/genlayer-project-boilerplate) | +151 | 12060 |
| 82 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +149 | 26657 |
| 83 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +148 | 25646 |
| 84 | [browserbase/skills](https://github.com/browserbase/skills) | +147 | 1777 |
| 85 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +143 | 6269 |
| 86 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +142 | 3598 |
| 87 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | +142 | 5717 |
| 88 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +141 | 13807 |
| 89 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +140 | 35707 |
| 90 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +138 | 5508 |
| 91 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +135 | 9595 |
| 92 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +134 | 42369 |
| 93 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +131 | 32400 |
| 94 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +129 | 2005 |
| 95 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +127 | 5651 |
| 96 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +126 | 1383 |
| 97 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +126 | 11953 |
| 98 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +126 | 36198 |
| 99 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +125 | 4348 |
| 100 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +123 | 2060 |
| 101 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +122 | 23559 |
| 102 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +122 | 1847 |
| 103 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +121 | 3982 |
| 104 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +121 | 4149 |
| 105 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +119 | 2206 |
| 106 | [caamer20/Telegram-Drive](https://github.com/caamer20/Telegram-Drive) | +116 | 2165 |
| 107 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +115 | 4494 |
| 108 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +105 | 7648 |
| 109 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +105 | 1310 |
| 110 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | +104 | 2187 |
| 111 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +100 | 20272 |
| 112 | [google-research/timesfm](https://github.com/google-research/timesfm) | +97 | 19338 |
| 113 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +97 | 31113 |
| 114 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +96 | 5341 |
| 115 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +94 | 19552 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +92 | 33323 |
| 117 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +92 | 2505 |
| 118 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +91 | 4087 |
| 119 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +91 | 32017 |
| 120 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +90 | 3175 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18373 | 131041 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +14800 | 108568 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12183 | 70260 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8355 | 52992 |
| 5 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8053 | 50947 |
| 6 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7465 | 42129 |
| 7 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +7365 | 189813 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +7057 | 60312 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6785 | 51199 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6772 | 41715 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5803 | 56825 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4742 | 27395 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4340 | 224760 |
| 14 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4329 | 30678 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4248 | 88632 |
| 16 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3805 | 91242 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3804 | 24053 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3723 | 40596 |
| 19 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +3527 | 25646 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3495 | 34475 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3381 | 50723 |
| 22 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3023 | 58417 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2940 | 109881 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2936 | 74774 |
| 25 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2856 | 27318 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2837 | 62004 |
| 27 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2805 | 17032 |
| 28 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2804 | 20643 |
| 29 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2788 | 30590 |
| 30 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2587 | 19482 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2578 | 34148 |
| 32 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2537 | 53481 |
| 33 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2485 | 78660 |
| 34 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2464 | 30943 |
| 35 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2353 | 69674 |
| 36 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2348 | 12928 |
| 37 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2325 | 35160 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2324 | 14078 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2236 | 23091 |
| 40 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2183 | 19087 |
| 41 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2138 | 11799 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2129 | 44146 |
| 43 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2071 | 17204 |
| 44 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2040 | 17209 |
| 45 | [chenglou/pretext](https://github.com/chenglou/pretext) | +1998 | 46081 |
| 46 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1994 | 59660 |
| 47 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1992 | 22603 |
| 48 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1986 | 55070 |
| 49 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1975 | 85286 |
| 50 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1930 | 58974 |
| 51 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1899 | 15075 |
| 52 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1870 | 31098 |
| 53 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1805 | 57938 |
| 54 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1789 | 32400 |
| 55 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1706 | 46369 |
| 56 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1640 | 28462 |
| 57 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1587 | 11553 |
| 58 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1567 | 25907 |
| 59 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1533 | 9946 |
| 60 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1506 | 24392 |
| 61 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1506 | 20018 |
| 62 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1504 | 33878 |
| 63 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1442 | 28897 |
| 64 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1439 | 6826 |
| 65 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1425 | 38660 |
| 66 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1417 | 64587 |
| 67 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1396 | 9179 |
| 68 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1386 | 17067 |
| 69 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1367 | 98536 |
| 70 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1364 | 45886 |
| 71 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1354 | 42351 |
| 72 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1348 | 30450 |
| 73 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1346 | 42879 |
| 74 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1334 | 22540 |
| 75 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1323 | 24619 |
| 76 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1287 | 11057 |
| 77 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1261 | 14900 |
| 78 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1256 | 95754 |
| 79 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1239 | 12223 |
| 80 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1239 | 24657 |
| 81 | [github/spec-kit](https://github.com/github/spec-kit) | +1223 | 71722 |
| 82 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +1219 | 18583 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1213 | 26310 |
| 84 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1201 | 17393 |
| 85 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1199 | 7875 |
| 86 | [openai/codex](https://github.com/openai/codex) | +1194 | 61744 |
| 87 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1189 | 53328 |
| 88 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1177 | 8923 |
| 89 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1156 | 37330 |
| 90 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1155 | 44978 |
| 91 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1154 | 10932 |
| 92 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1152 | 13807 |
| 93 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1084 | 17210 |
| 94 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1055 | 36198 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1051 | 33323 |
| 96 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1040 | 19338 |
| 97 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1028 | 42369 |
| 98 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +990 | 73135 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +989 | 78902 |
| 100 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +973 | 51546 |
| 101 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +965 | 20059 |
| 102 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +953 | 5341 |
| 103 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +942 | 79656 |
| 104 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +935 | 33848 |
| 105 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +934 | 30396 |
| 106 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +931 | 5651 |
| 107 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +928 | 25821 |
| 108 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +882 | 9408 |
| 109 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +878 | 7195 |
| 110 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +859 | 21591 |
| 111 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +850 | 4741 |
| 112 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +846 | 5508 |
| 113 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +842 | 47122 |
| 114 | [google/magika](https://github.com/google/magika) | +834 | 16878 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +780 | 13581 |
| 116 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +777 | 6269 |
| 117 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +761 | 52700 |
| 118 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +752 | 9841 |
| 119 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +742 | 4125 |
| 120 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +739 | 4619 |
| 121 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +733 | 9739 |
| 122 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +717 | 18686 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +711 | 11953 |
| 124 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +695 | 6118 |
| 125 | [jundot/omlx](https://github.com/jundot/omlx) | +666 | 12208 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +637 | 12413 |
| 127 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +632 | 19552 |
| 128 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +622 | 41571 |
| 129 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +617 | 54903 |
| 130 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +614 | 22191 |
| 131 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +604 | 4978 |
| 132 | [soxoj/maigret](https://github.com/soxoj/maigret) | +603 | 23667 |
| 133 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +596 | 11554 |
| 134 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +594 | 4087 |
| 135 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +587 | 11959 |
| 136 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +578 | 4348 |
| 137 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +573 | 3665 |
| 138 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +572 | 39841 |
| 139 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +563 | 32017 |
| 140 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +559 | 4388 |
| 141 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +553 | 12862 |
| 142 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +546 | 2704 |
| 143 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +540 | 36799 |
| 144 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +538 | 3372 |
| 145 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +525 | 34698 |
| 146 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +507 | 2992 |
| 147 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +497 | 3982 |
| 148 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +491 | 17796 |
| 149 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +484 | 2842 |
| 150 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +476 | 20002 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +468 | 31113 |
| 152 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +447 | 23395 |
| 153 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +445 | 4149 |
| 154 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +443 | 37564 |
| 155 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +439 | 18470 |
| 156 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +436 | 5050 |
| 157 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +429 | 36907 |
| 158 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +414 | 7978 |
| 159 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +410 | 7503 |
| 160 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +409 | 20272 |
| 161 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +408 | 26657 |
| 162 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +408 | 31240 |
| 163 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +406 | 4085 |
| 164 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +391 | 3076 |
| 165 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +385 | 24525 |
| 166 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +377 | 2717 |
| 167 | [PostHog/posthog](https://github.com/PostHog/posthog) | +372 | 31767 |
| 168 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +371 | 2505 |
| 169 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +368 | 2421 |
| 170 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +368 | 8542 |
| 171 | [eze-is/web-access](https://github.com/eze-is/web-access) | +368 | 5949 |
| 172 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +366 | 6981 |
| 173 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +363 | 25411 |
| 174 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +363 | 2575 |
| 175 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +344 | 3393 |
| 176 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +327 | 2060 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +313 | 26074 |
| 178 | [decolua/9router](https://github.com/decolua/9router) | +308 | 3646 |
| 179 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +305 | 2735 |
| 180 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +295 | 3598 |
| 181 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +292 | 1452 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +276 | 12978 |
| 183 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +272 | 6089 |
| 184 | [floci-io/floci](https://github.com/floci-io/floci) | +272 | 4327 |
| 185 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +270 | 9870 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +269 | 26870 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +252 | 36103 |
| 188 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +249 | 1847 |
| 189 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +241 | 3653 |
| 190 | [88lin/video_vip](https://github.com/88lin/video_vip) | +236 | 1629 |
| 191 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +232 | 2056 |
| 192 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +231 | 1628 |
| 193 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +217 | 3418 |
| 194 | [tiagozip/cap](https://github.com/tiagozip/cap) | +211 | 6240 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +200 | 3005 |
| 196 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +197 | 16152 |
| 197 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +192 | 7457 |
| 198 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +188 | 33712 |
| 199 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +177 | 9260 |
| 200 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +177 | 2957 |
| 201 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +167 | 1368 |
| 202 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +167 | 2444 |
| 203 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +167 | 1138 |
| 204 | [browserbase/skills](https://github.com/browserbase/skills) | +158 | 1777 |
| 205 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +156 | 11474 |
| 206 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +156 | 8077 |
| 207 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +153 | 827 |
| 208 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +150 | 987 |
| 209 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +150 | 1667 |
| 210 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +148 | 4260 |
| 211 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 212 | [usebruno/bruno](https://github.com/usebruno/bruno) | +147 | 41086 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +147 | 22588 |
| 214 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +144 | 583 |
| 215 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +140 | 14683 |
| 216 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +140 | 35473 |
| 217 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +134 | 4060 |
| 218 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +132 | 8850 |
| 219 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +130 | 5878 |
| 220 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +126 | 794 |
| 221 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +126 | 29868 |
| 222 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +124 | 7485 |
| 223 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +121 | 39596 |
| 224 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +120 | 2627 |
| 225 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +120 | 5615 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +120 | 23731 |
| 227 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +118 | 29921 |
| 228 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +117 | 13147 |
| 229 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +115 | 19326 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +111 | 1869 |
| 231 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +107 | 715 |
| 232 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +105 | 1147 |
| 233 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 516 |
| 234 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +104 | 794 |
| 235 | [clawplays/ospec](https://github.com/clawplays/ospec) | +101 | 611 |
| 236 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +98 | 539 |
| 237 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +97 | 2046 |
| 238 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +95 | 11003 |
| 239 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +93 | 26970 |
| 240 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +93 | 638 |
| 241 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +91 | 472 |
| 242 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +90 | 549 |
| 243 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +90 | 1530 |
| 244 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +90 | 1932 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +90 | 33000 |
| 246 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +89 | 3481 |
| 247 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +89 | 13050 |
| 248 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +87 | 2476 |
| 249 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +87 | 48784 |
| 250 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +86 | 438 |
| 251 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +85 | 1175 |
| 252 | [openmemind/memind](https://github.com/openmemind/memind) | +84 | 620 |
| 253 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +83 | 755 |
| 254 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +82 | 1602 |
| 255 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +82 | 1886 |
| 256 | [crimera/piko](https://github.com/crimera/piko) | +82 | 3431 |
| 257 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +81 | 837 |
| 258 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +80 | 1986 |
| 259 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +79 | 559 |
| 260 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +78 | 1727 |
| 261 | [robinebers/openusage](https://github.com/robinebers/openusage) | +78 | 2225 |
| 262 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +78 | 1240 |
| 263 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +77 | 754 |
| 264 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +74 | 1048 |
| 265 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +74 | 45263 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +70 | 3956 |
| 267 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +69 | 682 |
| 268 | [microg/GmsCore](https://github.com/microg/GmsCore) | +66 | 13130 |
| 269 | [sandeco/reversa](https://github.com/sandeco/reversa) | +64 | 482 |
| 270 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +64 | 2825 |
| 271 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +63 | 27441 |
| 272 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +62 | 378 |
| 273 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +62 | 29020 |
| 274 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +61 | 1446 |
| 275 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +60 | 384 |
| 276 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +59 | 366 |
| 277 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +59 | 1748 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +56 | 9454 |
| 279 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 280 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +55 | 7369 |
| 281 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 282 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +52 | 663 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +51 | 11843 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +51 | 31476 |
| 285 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +50 | 4985 |
| 286 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +50 | 267 |
| 287 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +48 | 1929 |
| 288 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +45 | 265 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +43 | 1839 |
| 290 | [risin42/NagramX](https://github.com/risin42/NagramX) | +43 | 1760 |
| 291 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +43 | 5214 |
| 292 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +41 | 260 |
| 293 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +40 | 622 |
| 294 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +37 | 2276 |
| 295 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +37 | 1321 |
| 296 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 161 |
| 297 | [is-a-dev/register](https://github.com/is-a-dev/register) | +33 | 10213 |
| 298 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +33 | 805 |
| 299 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +33 | 2147 |
| 300 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +33 | 4012 |
