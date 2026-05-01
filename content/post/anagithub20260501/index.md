---
title: "2026-05-01 GitHub增长趋势报告"
description: "1.skills+344 2.warp+333 3.sandcastle+66 4.graphify+63 5.omniget+55"
date: 2026-05-01T20:55:40+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-01 20:55:40

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
        'daily': {"categories": ["browserbase/skills", "tirth8205/code-review-graph", "1jehuang/jcode", "addyosmani/agent-skills", "rtk-ai/rtk", "santifer/career-ops", "hugohe3/ppt-master", "openai/symphony", "kepano/obsidian-skills", "badlogic/pi-mono", "Alishahryar1/free-claude-code", "Fincept-Corporation/FinceptTerminal", "soxoj/maigret", "freestylefly/awesome-gpt-image-2", "iamgio/quarkdown", "tonhowtf/omniget", "safishamsi/graphify", "mattpocock/sandcastle", "warpdotdev/warp", "mattpocock/skills"], "data": [35, 35, 36, 37, 39, 41, 42, 43, 45, 46, 46, 51, 52, 53, 54, 55, 63, 66, 333, 344]},
        'weekly': {"categories": ["op7418/guizang-ppt-skill", "Anil-matcha/Open-Generative-AI", "ComposioHQ/awesome-codex-skills", "badlogic/pi-mono", "addyosmani/agent-skills", "Fincept-Corporation/FinceptTerminal", "TauricResearch/TradingAgents", "microsoft/VibeVoice", "safishamsi/graphify", "abhigyanpatwari/GitNexus", "rtk-ai/rtk", "JuliusBrussee/caveman", "farion1231/cc-switch", "refactoringhq/tolaria", "Z4nzu/hackingtool", "NousResearch/hermes-agent", "Alishahryar1/free-claude-code", "warpdotdev/warp", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [478, 479, 486, 567, 592, 599, 610, 622, 669, 682, 714, 720, 773, 1034, 1214, 1736, 2012, 2052, 3183, 3892]},
        'monthly': {"categories": ["multica-ai/multica", "msitarzewski/agency-agents", "anthropics/claude-code", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "garrytan/gstack", "openclaw/openclaw", "addyosmani/agent-skills", "Gitlawb/openclaude", "mattpocock/skills", "safishamsi/graphify", "obra/superpowers", "santifer/career-ops", "affaan-m/everything-claude-code", "MemPalace/mempalace", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "ultraworkers/claw-code", "NousResearch/hermes-agent"], "data": [3845, 3869, 3956, 4301, 4319, 4519, 4660, 4670, 4730, 4963, 6386, 7330, 7365, 7421, 8007, 8191, 12647, 14072, 17159, 18217]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +344 | 52256 |
| 2 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +333 | 51293 |
| 3 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +66 | 2674 |
| 4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +63 | 39574 |
| 5 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +55 | 2831 |
| 6 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +54 | 13375 |
| 7 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +53 | 2941 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | +52 | 21512 |
| 9 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +51 | 18648 |
| 10 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +46 | 19654 |
| 11 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +46 | 43564 |
| 12 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +45 | 28101 |
| 13 | [openai/symphony](https://github.com/openai/symphony) | +43 | 20371 |
| 14 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +42 | 10387 |
| 15 | [santifer/career-ops](https://github.com/santifer/career-ops) | +41 | 41585 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +39 | 39429 |
| 17 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +37 | 26962 |
| 18 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +36 | 2296 |
| 19 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +35 | 14609 |
| 20 | [browserbase/skills](https://github.com/browserbase/skills) | +35 | 1124 |
| 21 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +32 | 24060 |
| 22 | [multica-ai/multica](https://github.com/multica-ai/multica) | +29 | 23439 |
| 23 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +28 | 8655 |
| 24 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +28 | 19799 |
| 25 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +28 | 5376 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +26 | 9145 |
| 27 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +26 | 13646 |
| 28 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +25 | 34033 |
| 29 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +25 | 7669 |
| 30 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +24 | 11710 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3892 | 52256 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3183 | 104542 |
| 3 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2052 | 51293 |
| 4 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2012 | 19654 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1736 | 128100 |
| 6 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1214 | 55070 |
| 7 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1034 | 8719 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +773 | 57145 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +720 | 51949 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +714 | 39429 |
| 11 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +682 | 34033 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +669 | 39574 |
| 13 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +622 | 46193 |
| 14 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +610 | 30590 |
| 15 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +599 | 18648 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +592 | 26962 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +567 | 43564 |
| 18 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +486 | 5376 |
| 19 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +479 | 10622 |
| 20 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +478 | 4500 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +465 | 13646 |
| 22 | [openai/symphony](https://github.com/openai/symphony) | +416 | 20371 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +378 | 23439 |
| 24 | [santifer/career-ops](https://github.com/santifer/career-ops) | +354 | 41585 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +351 | 9145 |
| 26 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +348 | 4088 |
| 27 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +335 | 2941 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +329 | 10387 |
| 29 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +297 | 5353 |
| 30 | [PostHog/posthog](https://github.com/PostHog/posthog) | +275 | 31767 |
| 31 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +274 | 50108 |
| 32 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +273 | 17073 |
| 33 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +270 | 16696 |
| 34 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +269 | 33557 |
| 35 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +264 | 10528 |
| 36 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +258 | 30659 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +256 | 42113 |
| 38 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +256 | 11710 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +256 | 22819 |
| 40 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +254 | 8623 |
| 41 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +247 | 3936 |
| 42 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +246 | 13375 |
| 43 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +243 | 24060 |
| 44 | [gastownhall/beads](https://github.com/gastownhall/beads) | +238 | 22939 |
| 45 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +235 | 4160 |
| 46 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +235 | 25973 |
| 47 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +229 | 28101 |
| 48 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +226 | 27140 |
| 49 | [trycua/cua](https://github.com/trycua/cua) | +223 | 15473 |
| 50 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +221 | 14361 |
| 51 | [victorchen96/deepseek_v4_rolepaly_instruct](https://github.com/victorchen96/deepseek_v4_rolepaly_instruct) | +215 | 1589 |
| 52 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +214 | 26539 |
| 53 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +212 | 8655 |
| 54 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +211 | 57725 |
| 55 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +209 | 32836 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +208 | 30188 |
| 57 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +206 | 3063 |
| 58 | [penpot/penpot](https://github.com/penpot/penpot) | +202 | 44370 |
| 59 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +198 | 1458 |
| 60 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +197 | 30111 |
| 61 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +194 | 12627 |
| 62 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +189 | 19799 |
| 63 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +189 | 7409 |
| 64 | [blader/humanizer](https://github.com/blader/humanizer) | +188 | 16758 |
| 65 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +186 | 34036 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +185 | 44624 |
| 67 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +184 | 22367 |
| 68 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +184 | 4172 |
| 69 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +183 | 34933 |
| 70 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +181 | 14609 |
| 71 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +180 | 8432 |
| 72 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +180 | 4817 |
| 73 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +179 | 7669 |
| 74 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +178 | 2384 |
| 75 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +177 | 1560 |
| 76 | [akinloluwami/avnac](https://github.com/akinloluwami/avnac) | +175 | 973 |
| 77 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +173 | 20767 |
| 78 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +172 | 5249 |
| 79 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +168 | 24234 |
| 80 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +168 | 42139 |
| 81 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +165 | 18410 |
| 82 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +165 | 25351 |
| 83 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +164 | 3994 |
| 84 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +161 | 12737 |
| 85 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +160 | 32195 |
| 86 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +160 | 1035 |
| 87 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +159 | 35954 |
| 88 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +158 | 4870 |
| 89 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +155 | 5499 |
| 90 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +151 | 9349 |
| 91 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +148 | 6072 |
| 92 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +148 | 6952 |
| 93 | [thClaws/thClaws](https://github.com/thClaws/thClaws) | +146 | 687 |
| 94 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +145 | 1755 |
| 95 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +144 | 1968 |
| 96 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +138 | 25697 |
| 97 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | +137 | 5665 |
| 98 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +137 | 2223 |
| 99 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +137 | 16851 |
| 100 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +136 | 1399 |
| 101 | [soxoj/maigret](https://github.com/soxoj/maigret) | +135 | 21512 |
| 102 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +135 | 39791 |
| 103 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +133 | 18883 |
| 104 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +132 | 2296 |
| 105 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +131 | 2674 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +131 | 11677 |
| 107 | [wxyhgk/retain-pdf](https://github.com/wxyhgk/retain-pdf) | +130 | 1300 |
| 108 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +129 | 2824 |
| 109 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +128 | 1142 |
| 110 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +127 | 13597 |
| 111 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +127 | 19499 |
| 112 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | +123 | 2050 |
| 113 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +123 | 30998 |
| 114 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +115 | 692 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +112 | 13394 |
| 116 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +111 | 5162 |
| 117 | [google-research/timesfm](https://github.com/google-research/timesfm) | +107 | 19200 |
| 118 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +102 | 36799 |
| 119 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +101 | 24508 |
| 120 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +100 | 31910 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18217 | 128100 |
| 2 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +17159 | 189535 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +14072 | 104542 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12647 | 69201 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8191 | 51949 |
| 6 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8007 | 50655 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7421 | 51199 |
| 8 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7365 | 41585 |
| 9 | [obra/superpowers](https://github.com/obra/superpowers) | +7330 | 60312 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6386 | 39574 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4963 | 52256 |
| 12 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4730 | 25351 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4670 | 26962 |
| 14 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4660 | 224760 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4519 | 87741 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4319 | 34036 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4301 | 30678 |
| 18 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3956 | 69674 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3869 | 90065 |
| 20 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3845 | 23439 |
| 21 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3799 | 27140 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3613 | 39429 |
| 23 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3470 | 50108 |
| 24 | [chenglou/pretext](https://github.com/chenglou/pretext) | +3145 | 45966 |
| 25 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3104 | 61365 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3089 | 74774 |
| 27 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3086 | 109881 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3016 | 57145 |
| 29 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2822 | 30659 |
| 30 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2757 | 16696 |
| 31 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2691 | 78321 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2666 | 34148 |
| 33 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2613 | 19654 |
| 34 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2419 | 18648 |
| 35 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2379 | 11701 |
| 36 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2337 | 17103 |
| 37 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2298 | 12627 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2248 | 13646 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2173 | 22819 |
| 40 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2173 | 32195 |
| 41 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2161 | 18883 |
| 42 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2160 | 34033 |
| 43 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2158 | 43564 |
| 44 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2102 | 17365 |
| 45 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2098 | 51293 |
| 46 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2073 | 59232 |
| 47 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2072 | 58648 |
| 48 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1996 | 57725 |
| 49 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1986 | 85286 |
| 50 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1946 | 22368 |
| 51 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1935 | 46193 |
| 52 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1932 | 31098 |
| 53 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1927 | 30590 |
| 54 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1869 | 16377 |
| 55 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1844 | 10206 |
| 56 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1836 | 55070 |
| 57 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1819 | 14609 |
| 58 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1763 | 28838 |
| 59 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1738 | 33878 |
| 60 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1705 | 16986 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1633 | 28101 |
| 62 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1619 | 64446 |
| 63 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1564 | 25868 |
| 64 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +1527 | 18410 |
| 65 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1502 | 19844 |
| 66 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1493 | 24234 |
| 67 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1430 | 6771 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1418 | 30188 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1412 | 42113 |
| 70 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1384 | 19200 |
| 71 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1381 | 98536 |
| 72 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1376 | 16851 |
| 73 | [openai/codex](https://github.com/openai/codex) | +1372 | 61744 |
| 74 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1365 | 9145 |
| 75 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1358 | 24508 |
| 76 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1349 | 45886 |
| 77 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1345 | 22406 |
| 78 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1324 | 6688 |
| 79 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1313 | 8719 |
| 80 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1312 | 73135 |
| 81 | [github/spec-kit](https://github.com/github/spec-kit) | +1293 | 71722 |
| 82 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1293 | 24060 |
| 83 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1274 | 95754 |
| 84 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1271 | 33160 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1234 | 25973 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1221 | 37330 |
| 87 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1220 | 9273 |
| 88 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1213 | 14361 |
| 89 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1210 | 53171 |
| 90 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1205 | 10990 |
| 91 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1201 | 44624 |
| 92 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1199 | 17073 |
| 93 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1190 | 10622 |
| 94 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1186 | 13597 |
| 95 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1155 | 7669 |
| 96 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1118 | 8623 |
| 97 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1098 | 35954 |
| 98 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1077 | 42139 |
| 99 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1055 | 10387 |
| 100 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1023 | 79656 |
| 101 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +997 | 78902 |
| 102 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +966 | 51253 |
| 103 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +947 | 33557 |
| 104 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +935 | 21388 |
| 105 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +915 | 5162 |
| 106 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +910 | 25697 |
| 107 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +909 | 5499 |
| 108 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +899 | 39791 |
| 109 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +876 | 7155 |
| 110 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +842 | 4572 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +838 | 13394 |
| 112 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +837 | 47122 |
| 113 | [google/magika](https://github.com/google/magika) | +833 | 16848 |
| 114 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +819 | 52700 |
| 115 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +810 | 5249 |
| 116 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +786 | 18589 |
| 117 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +782 | 4954 |
| 118 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +771 | 6072 |
| 119 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +742 | 4108 |
| 120 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +732 | 4160 |
| 121 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +730 | 9722 |
| 122 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +720 | 11677 |
| 123 | [jundot/omlx](https://github.com/jundot/omlx) | +680 | 12069 |
| 124 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +661 | 22097 |
| 125 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +659 | 19499 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +655 | 12273 |
| 127 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +646 | 11959 |
| 128 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +641 | 41464 |
| 129 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +624 | 54903 |
| 130 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +619 | 8655 |
| 131 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +606 | 4311 |
| 132 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +595 | 11550 |
| 133 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +591 | 39841 |
| 134 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +584 | 31910 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +576 | 34648 |
| 136 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +564 | 3617 |
| 137 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +558 | 5376 |
| 138 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +558 | 5645 |
| 139 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +557 | 36799 |
| 140 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +553 | 4172 |
| 141 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +543 | 3315 |
| 142 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +541 | 2668 |
| 143 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +532 | 12737 |
| 144 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +508 | 17689 |
| 145 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +503 | 2972 |
| 146 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +498 | 30343 |
| 147 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +494 | 19860 |
| 148 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +489 | 23325 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +486 | 30998 |
| 150 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +485 | 5969 |
| 151 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +478 | 37564 |
| 152 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +471 | 26033 |
| 153 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +464 | 18365 |
| 154 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +462 | 2761 |
| 155 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +460 | 2510 |
| 156 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +458 | 5011 |
| 157 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +453 | 25233 |
| 158 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +453 | 7873 |
| 159 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +440 | 3734 |
| 160 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +429 | 3994 |
| 161 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +424 | 31122 |
| 162 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +417 | 7409 |
| 163 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +416 | 26539 |
| 164 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +414 | 36907 |
| 165 | [eze-is/web-access](https://github.com/eze-is/web-access) | +410 | 5904 |
| 166 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +404 | 2663 |
| 167 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +400 | 4032 |
| 168 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +399 | 2722 |
| 169 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +389 | 24403 |
| 170 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +388 | 20077 |
| 171 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +380 | 6946 |
| 172 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +378 | 8432 |
| 173 | [PostHog/posthog](https://github.com/PostHog/posthog) | +369 | 31767 |
| 174 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +366 | 2382 |
| 175 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +365 | 20324 |
| 176 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +332 | 2346 |
| 177 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +329 | 3321 |
| 178 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +320 | 26021 |
| 179 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +319 | 3393 |
| 180 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +315 | 5918 |
| 181 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +298 | 9809 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +291 | 6007 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +288 | 12888 |
| 184 | [decolua/9router](https://github.com/decolua/9router) | +284 | 3493 |
| 185 | [floci-io/floci](https://github.com/floci-io/floci) | +283 | 4298 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +267 | 3602 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +254 | 26755 |
| 188 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +254 | 36103 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +242 | 2003 |
| 190 | [88lin/video_vip](https://github.com/88lin/video_vip) | +237 | 1605 |
| 191 | [tiagozip/cap](https://github.com/tiagozip/cap) | +209 | 6205 |
| 192 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +200 | 7436 |
| 193 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +196 | 16047 |
| 194 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +192 | 2912 |
| 195 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +186 | 9181 |
| 196 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +181 | 33712 |
| 197 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +174 | 11445 |
| 198 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +174 | 2903 |
| 199 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +169 | 4254 |
| 200 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +166 | 1257 |
| 201 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +163 | 1104 |
| 202 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +163 | 4043 |
| 203 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 827 |
| 204 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +161 | 8048 |
| 205 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +159 | 582 |
| 206 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +159 | 8833 |
| 207 | [usebruno/bruno](https://github.com/usebruno/bruno) | +155 | 41086 |
| 208 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +152 | 3205 |
| 209 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +151 | 1633 |
| 210 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +150 | 5854 |
| 211 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +147 | 2223 |
| 212 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +143 | 22542 |
| 213 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +142 | 35473 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +141 | 40265 |
| 215 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +137 | 940 |
| 216 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +132 | 2610 |
| 217 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +131 | 14618 |
| 218 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +128 | 29836 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +126 | 23692 |
| 220 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +125 | 732 |
| 221 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +124 | 5590 |
| 222 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +122 | 13137 |
| 223 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +119 | 7456 |
| 224 | [clawplays/ospec](https://github.com/clawplays/ospec) | +118 | 611 |
| 225 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +117 | 39596 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29891 |
| 227 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +116 | 727 |
| 228 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +115 | 1848 |
| 229 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +112 | 19288 |
| 230 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +109 | 1718 |
| 231 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 511 |
| 232 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +104 | 695 |
| 233 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +103 | 1128 |
| 234 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +102 | 788 |
| 235 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +100 | 2037 |
| 236 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +97 | 10982 |
| 237 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +96 | 26957 |
| 238 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +95 | 525 |
| 239 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +93 | 33000 |
| 240 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +92 | 3407 |
| 241 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +92 | 618 |
| 242 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 1917 |
| 243 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +91 | 1151 |
| 244 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +89 | 1508 |
| 245 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +89 | 469 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +88 | 13018 |
| 247 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +87 | 813 |
| 248 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +87 | 1231 |
| 249 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +87 | 48784 |
| 250 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +84 | 436 |
| 251 | [openmemind/memind](https://github.com/openmemind/memind) | +84 | 601 |
| 252 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +83 | 494 |
| 253 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +83 | 2437 |
| 254 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +82 | 743 |
| 255 | [cv-cat/DouYin_Spider](https://github.com/cv-cat/DouYin_Spider) | +82 | 1680 |
| 256 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +81 | 1589 |
| 257 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +81 | 1969 |
| 258 | [crimera/piko](https://github.com/crimera/piko) | +80 | 3408 |
| 259 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +79 | 1892 |
| 260 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +78 | 1854 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +75 | 3940 |
| 262 | [robinebers/openusage](https://github.com/robinebers/openusage) | +75 | 2186 |
| 263 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +75 | 3131 |
| 264 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +74 | 45263 |
| 265 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +72 | 1025 |
| 266 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +71 | 526 |
| 267 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +69 | 1440 |
| 268 | [microg/GmsCore](https://github.com/microg/GmsCore) | +69 | 13118 |
| 269 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +68 | 664 |
| 270 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +68 | 2812 |
| 271 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +67 | 4124 |
| 272 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | +67 | 1312 |
| 273 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +66 | 653 |
| 274 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +63 | 27423 |
| 275 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +60 | 9446 |
| 276 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +59 | 369 |
| 277 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +57 | 7357 |
| 278 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +57 | 358 |
| 279 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +57 | 1734 |
| 280 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +57 | 28988 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +54 | 11829 |
| 282 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +54 | 3738 |
| 283 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 284 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +53 | 360 |
| 285 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +52 | 4965 |
| 286 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +51 | 1921 |
| 287 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +48 | 258 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +48 | 1830 |
| 289 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +46 | 31476 |
| 290 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1754 |
| 291 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +44 | 263 |
| 292 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +41 | 613 |
| 293 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +41 | 5210 |
| 294 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +37 | 8622 |
| 295 | [is-a-dev/register](https://github.com/is-a-dev/register) | +35 | 10206 |
| 296 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +34 | 790 |
| 297 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 159 |
| 298 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +34 | 243 |
| 299 | [sandeco/reversa](https://github.com/sandeco/reversa) | +33 | 382 |
| 300 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +33 | 3161 |
