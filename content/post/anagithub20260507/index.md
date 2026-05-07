---
title: "2026-05-07 GitHub增长趋势报告"
description: "1.agent-skills+222 2.skills+151 3.hunk+149 4.Scrapling+85 5.financial-services-plugins+84"
date: 2026-05-07T21:06:03+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-07 21:06:03

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
        'daily': {"categories": ["Wei-Shaw/sub2api", "hugohe3/ppt-master", "vasu-devs/JustHireMe", "MrsEWE44/musicDownload", "multica-ai/multica", "z-lab/dflash", "warpdotdev/warp", "AIDC-AI/Pixelle-Video", "LearningCircuit/local-deep-research", "rtk-ai/rtk", "datawhalechina/hello-agents", "cheahjs/free-llm-api-resources", "docusealco/docuseal", "VectifyAI/PageIndex", "ruvnet/ruflo", "anthropics/financial-services-plugins", "D4Vinci/Scrapling", "modem-dev/hunk", "mattpocock/skills", "addyosmani/agent-skills"], "data": [36, 38, 42, 45, 45, 46, 47, 47, 50, 50, 54, 57, 64, 69, 81, 84, 85, 149, 151, 222]},
        'weekly': {"categories": ["docusealco/docuseal", "browser-use/browser-harness", "withastro/flue", "1jehuang/jcode", "abhigyanpatwari/GitNexus", "Lum1104/Understand-Anything", "Alishahryar1/free-claude-code", "addyosmani/agent-skills", "rtk-ai/rtk", "AIDC-AI/Pixelle-Video", "farion1231/cc-switch", "safishamsi/graphify", "soxoj/maigret", "D4Vinci/Scrapling", "warpdotdev/warp", "NousResearch/hermes-agent", "ruvnet/ruflo", "TauricResearch/TradingAgents", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [379, 383, 428, 435, 436, 463, 464, 516, 540, 617, 686, 763, 872, 984, 1090, 1364, 1655, 2040, 2097, 2200]},
        'monthly': {"categories": ["Alishahryar1/free-claude-code", "farion1231/cc-switch", "shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "TauricResearch/TradingAgents", "rtk-ai/rtk", "addyosmani/agent-skills", "garrytan/gstack", "multica-ai/multica", "thedotmack/claude-mem", "santifer/career-ops", "affaan-m/everything-claude-code", "obra/superpowers", "safishamsi/graphify", "mattpocock/skills", "VoltAgent/awesome-design-md", "MemPalace/mempalace", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [2931, 2942, 3167, 3198, 3213, 3442, 3452, 3746, 3885, 4235, 4728, 4872, 6284, 6357, 6394, 7281, 7610, 7640, 15990, 17690]}
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
| 1 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +222 | 32765 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +151 | 64691 |
| 3 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +149 | 2309 |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +85 | 47171 |
| 5 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +84 | 11316 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +81 | 46056 |
| 7 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +69 | 29467 |
| 8 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +64 | 15533 |
| 9 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +57 | 20920 |
| 10 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +54 | 43794 |
| 11 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +50 | 43852 |
| 12 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +50 | 6173 |
| 13 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +47 | 13287 |
| 14 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +47 | 56296 |
| 15 | [z-lab/dflash](https://github.com/z-lab/dflash) | +46 | 3436 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +45 | 25800 |
| 17 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +45 | 1558 |
| 18 | [vasu-devs/JustHireMe](https://github.com/vasu-devs/JustHireMe) | +42 | 939 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +38 | 12747 |
| 20 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +36 | 18615 |
| 21 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +36 | 2884 |
| 22 | [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) | +36 | 678 |
| 23 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +36 | 11384 |
| 24 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +36 | 31098 |
| 25 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +35 | 4417 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +34 | 36746 |
| 27 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +33 | 44397 |
| 28 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +33 | 7823 |
| 29 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 15751 |
| 30 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +31 | 3650 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2200 | 118512 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2097 | 64691 |
| 3 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2040 | 30590 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1655 | 46056 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1364 | 137414 |
| 6 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1090 | 56296 |
| 7 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +984 | 47171 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | +872 | 26200 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +763 | 44397 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +686 | 62389 |
| 11 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +617 | 13287 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +540 | 43852 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +516 | 32765 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +464 | 22348 |
| 15 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +463 | 13130 |
| 16 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +436 | 36746 |
| 17 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +435 | 4829 |
| 18 | [withastro/flue](https://github.com/withastro/flue) | +428 | 2754 |
| 19 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +383 | 11384 |
| 20 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +379 | 15533 |
| 21 | [virattt/dexter](https://github.com/virattt/dexter) | +372 | 24679 |
| 22 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +365 | 13656 |
| 23 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +363 | 8333 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +338 | 12747 |
| 25 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +326 | 7420 |
| 26 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +321 | 20238 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +316 | 25800 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +308 | 45999 |
| 29 | [openai/symphony](https://github.com/openai/symphony) | +301 | 22357 |
| 30 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +275 | 13815 |
| 31 | [browserbase/skills](https://github.com/browserbase/skills) | +265 | 2592 |
| 32 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +260 | 4417 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +256 | 51594 |
| 34 | [santifer/career-ops](https://github.com/santifer/career-ops) | +255 | 43338 |
| 35 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +255 | 5184 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +250 | 25804 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +245 | 15751 |
| 38 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +243 | 3777 |
| 39 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +241 | 5565 |
| 40 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +236 | 16009 |
| 41 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +235 | 10102 |
| 42 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +224 | 20321 |
| 43 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +223 | 11960 |
| 44 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +221 | 17575 |
| 45 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +216 | 3867 |
| 46 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +213 | 15710 |
| 47 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +210 | 29537 |
| 48 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +208 | 29467 |
| 49 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +203 | 18615 |
| 50 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +200 | 35057 |
| 51 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +198 | 8806 |
| 52 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +196 | 1576 |
| 53 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +192 | 45984 |
| 54 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +186 | 5174 |
| 55 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +186 | 35707 |
| 56 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +178 | 11948 |
| 57 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +173 | 6173 |
| 58 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +165 | 43794 |
| 59 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +163 | 8731 |
| 60 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +161 | 31427 |
| 61 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +159 | 27183 |
| 62 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +157 | 22137 |
| 63 | [cursor/cookbook](https://github.com/cursor/cookbook) | +155 | 3671 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +153 | 31200 |
| 65 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +150 | 2310 |
| 66 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +150 | 17865 |
| 67 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +150 | 9458 |
| 68 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +145 | 34460 |
| 69 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +145 | 2428 |
| 70 | [WeritoP/FL-STUDIO-PATCHER](https://github.com/WeritoP/FL-STUDIO-PATCHER) | +142 | 466 |
| 71 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +142 | 23607 |
| 72 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +139 | 23410 |
| 73 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +138 | 13606 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +138 | 5570 |
| 75 | [blader/humanizer](https://github.com/blader/humanizer) | +135 | 17723 |
| 76 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +135 | 10107 |
| 77 | [appergb/openless](https://github.com/appergb/openless) | +133 | 964 |
| 78 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +133 | 20677 |
| 79 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +132 | 3619 |
| 80 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +126 | 23978 |
| 81 | [therealaleph/MasterHttpRelayVPN-RUST](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | +125 | 1992 |
| 82 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +124 | 20920 |
| 83 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +123 | 11317 |
| 84 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +123 | 58810 |
| 85 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +123 | 12538 |
| 86 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +122 | 7823 |
| 87 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +122 | 5019 |
| 88 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +122 | 26106 |
| 89 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +121 | 1877 |
| 90 | [RivoLink/leaf](https://github.com/RivoLink/leaf) | +121 | 909 |
| 91 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +117 | 2126 |
| 92 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +115 | 3806 |
| 93 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +114 | 2884 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +114 | 31629 |
| 95 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +113 | 17610 |
| 96 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +113 | 3525 |
| 97 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +112 | 3213 |
| 98 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +112 | 8316 |
| 99 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +111 | 6260 |
| 100 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +110 | 12210 |
| 101 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +105 | 4905 |
| 102 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +103 | 2605 |
| 103 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +102 | 36724 |
| 104 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +101 | 6038 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +99 | 33882 |
| 106 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +97 | 1024 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +97 | 42855 |
| 108 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +96 | 25860 |
| 109 | [MAC-AutoML/MindPipe](https://github.com/MAC-AutoML/MindPipe) | +96 | 914 |
| 110 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +94 | 892 |
| 111 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +94 | 46766 |
| 112 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +92 | 3629 |
| 113 | [olaxbt/ai-market-maker](https://github.com/olaxbt/ai-market-maker) | +89 | 1274 |
| 114 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +85 | 12804 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +85 | 14017 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +85 | 4482 |
| 117 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +83 | 4659 |
| 118 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +81 | 25057 |
| 119 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +80 | 20591 |
| 120 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +77 | 5913 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17690 | 137414 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +15990 | 118513 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7640 | 56032 |
| 4 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7610 | 51457 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +7281 | 72722 |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6394 | 64691 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6357 | 44397 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +6284 | 60312 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4872 | 51199 |
| 10 | [santifer/career-ops](https://github.com/santifer/career-ops) | +4728 | 43338 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4235 | 30678 |
| 12 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3885 | 25800 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3746 | 91031 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3452 | 32765 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3442 | 43852 |
| 16 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3213 | 30590 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3198 | 94737 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3167 | 51594 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2942 | 62389 |
| 20 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2931 | 22348 |
| 21 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2835 | 56296 |
| 22 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2765 | 190564 |
| 23 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2687 | 20238 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2622 | 109881 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2607 | 74774 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2467 | 15751 |
| 27 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2464 | 17865 |
| 28 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2421 | 13606 |
| 29 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2242 | 46056 |
| 30 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2216 | 19626 |
| 31 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2153 | 63333 |
| 32 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2135 | 55070 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2132 | 23607 |
| 34 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2121 | 34148 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2061 | 17575 |
| 36 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2049 | 23410 |
| 37 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1923 | 36746 |
| 38 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1867 | 79534 |
| 39 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1866 | 45999 |
| 40 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1771 | 60723 |
| 41 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1750 | 85286 |
| 42 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1722 | 11384 |
| 43 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1713 | 69674 |
| 44 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1711 | 47171 |
| 45 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1686 | 35057 |
| 46 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1668 | 27837 |
| 47 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1638 | 12210 |
| 48 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1625 | 15710 |
| 49 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1571 | 25983 |
| 50 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1525 | 10102 |
| 51 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1505 | 24771 |
| 52 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1494 | 20545 |
| 53 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1449 | 58810 |
| 54 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1445 | 6931 |
| 55 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1437 | 31629 |
| 56 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1424 | 59528 |
| 57 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1383 | 17610 |
| 58 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1377 | 11960 |
| 59 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1358 | 46766 |
| 60 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1339 | 13656 |
| 61 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1325 | 17454 |
| 62 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1303 | 45886 |
| 63 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1294 | 43794 |
| 64 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1294 | 29537 |
| 65 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1293 | 16009 |
| 66 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1285 | 25804 |
| 67 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1237 | 12747 |
| 68 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1237 | 98536 |
| 69 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1235 | 9458 |
| 70 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +1204 | 26106 |
| 71 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1200 | 13287 |
| 72 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1175 | 33878 |
| 73 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1171 | 18615 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1157 | 31200 |
| 75 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1133 | 32901 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1126 | 27183 |
| 77 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1105 | 8316 |
| 78 | [github/spec-kit](https://github.com/github/spec-kit) | +1090 | 71722 |
| 79 | [openai/codex](https://github.com/openai/codex) | +1087 | 61744 |
| 80 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1086 | 65897 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1044 | 45984 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1009 | 37330 |
| 83 | [soxoj/maigret](https://github.com/soxoj/maigret) | +998 | 26200 |
| 84 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +980 | 5667 |
| 85 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +974 | 53719 |
| 86 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +966 | 5913 |
| 87 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +955 | 13815 |
| 88 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +949 | 5565 |
| 89 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +943 | 78902 |
| 90 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +925 | 25057 |
| 91 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +920 | 12119 |
| 92 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +914 | 26012 |
| 93 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +891 | 31427 |
| 94 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +891 | 7281 |
| 95 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +887 | 34460 |
| 96 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +885 | 51993 |
| 97 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +862 | 20677 |
| 98 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +861 | 47122 |
| 99 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +856 | 36724 |
| 100 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +854 | 6260 |
| 101 | [google/magika](https://github.com/google/magika) | +839 | 16930 |
| 102 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +838 | 7420 |
| 103 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +831 | 19160 |
| 104 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +825 | 6038 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +823 | 42855 |
| 106 | [openai/symphony](https://github.com/openai/symphony) | +797 | 22357 |
| 107 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +793 | 5570 |
| 108 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +786 | 17818 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +778 | 33882 |
| 110 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +743 | 4175 |
| 111 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +707 | 13130 |
| 112 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +699 | 22008 |
| 113 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +666 | 6456 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +651 | 14018 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +644 | 12538 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +633 | 4482 |
| 117 | [google-research/timesfm](https://github.com/google-research/timesfm) | +632 | 19508 |
| 118 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +579 | 19881 |
| 119 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +575 | 29150 |
| 120 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +574 | 3724 |
| 121 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +567 | 4659 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +551 | 12804 |
| 123 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +551 | 13025 |
| 124 | [jundot/omlx](https://github.com/jundot/omlx) | +539 | 12508 |
| 125 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +516 | 41918 |
| 126 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +511 | 3114 |
| 127 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +507 | 3030 |
| 128 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +503 | 39841 |
| 129 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +503 | 4193 |
| 130 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +502 | 4532 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +495 | 36799 |
| 132 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +484 | 3514 |
| 133 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +465 | 32388 |
| 134 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +465 | 22420 |
| 135 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +462 | 11957 |
| 136 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +461 | 4386 |
| 137 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +459 | 18963 |
| 138 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +457 | 29467 |
| 139 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +440 | 5320 |
| 140 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +435 | 18129 |
| 141 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +417 | 36907 |
| 142 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +416 | 7745 |
| 143 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +415 | 20329 |
| 144 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +410 | 31438 |
| 145 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +400 | 4162 |
| 146 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +396 | 26965 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +391 | 3525 |
| 148 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +376 | 18790 |
| 149 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +374 | 37564 |
| 150 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +373 | 2486 |
| 151 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +371 | 20920 |
| 152 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +365 | 4905 |
| 153 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +364 | 31565 |
| 154 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +359 | 2813 |
| 155 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +359 | 20591 |
| 156 | [PostHog/posthog](https://github.com/PostHog/posthog) | +359 | 31767 |
| 157 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +357 | 8731 |
| 158 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +355 | 2886 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +351 | 8342 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +349 | 24803 |
| 161 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +347 | 7060 |
| 162 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +337 | 2108 |
| 163 | [openai/skills](https://github.com/openai/skills) | +328 | 18532 |
| 164 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +322 | 3534 |
| 165 | [decolua/9router](https://github.com/decolua/9router) | +321 | 4434 |
| 166 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +320 | 25860 |
| 167 | [z-lab/dflash](https://github.com/z-lab/dflash) | +312 | 3437 |
| 168 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +310 | 1580 |
| 169 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +305 | 2605 |
| 170 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +297 | 11948 |
| 171 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +295 | 3629 |
| 172 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +285 | 1774 |
| 173 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +279 | 3650 |
| 174 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +278 | 2126 |
| 175 | [browserbase/skills](https://github.com/browserbase/skills) | +275 | 2592 |
| 176 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +272 | 3220 |
| 177 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +270 | 2072 |
| 178 | [eze-is/web-access](https://github.com/eze-is/web-access) | +267 | 6097 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +264 | 27143 |
| 180 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +259 | 1824 |
| 181 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +259 | 26252 |
| 182 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +255 | 3213 |
| 183 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +254 | 1747 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +253 | 13292 |
| 185 | [88lin/video_vip](https://github.com/88lin/video_vip) | +237 | 1715 |
| 186 | [floci-io/floci](https://github.com/floci-io/floci) | +229 | 4389 |
| 187 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +227 | 1386 |
| 188 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +222 | 10005 |
| 189 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +218 | 3844 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +216 | 36103 |
| 191 | [tiagozip/cap](https://github.com/tiagozip/cap) | +213 | 6284 |
| 192 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +203 | 2672 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +197 | 6255 |
| 194 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +196 | 1576 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +195 | 2188 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +192 | 3171 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +181 | 16314 |
| 198 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +173 | 1184 |
| 199 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +168 | 7528 |
| 200 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +167 | 33712 |
| 201 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +166 | 1121 |
| 202 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +164 | 2462 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +160 | 9594 |
| 204 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +149 | 40265 |
| 205 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +148 | 3482 |
| 206 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +142 | 778 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +141 | 22695 |
| 208 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +137 | 8145 |
| 209 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +135 | 14802 |
| 210 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +135 | 3020 |
| 211 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +134 | 35473 |
| 212 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +129 | 7526 |
| 213 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +129 | 4332 |
| 214 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +124 | 912 |
| 215 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +122 | 39596 |
| 216 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +119 | 11541 |
| 217 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +116 | 818 |
| 218 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +111 | 5682 |
| 219 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +107 | 5276 |
| 220 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +107 | 23817 |
| 221 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +107 | 29973 |
| 222 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +105 | 812 |
| 223 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +105 | 1136 |
| 224 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +104 | 1188 |
| 225 | [usebruno/bruno](https://github.com/usebruno/bruno) | +103 | 41086 |
| 226 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +102 | 606 |
| 227 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +100 | 29952 |
| 228 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +100 | 597 |
| 229 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +100 | 677 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +97 | 1927 |
| 231 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +91 | 2058 |
| 232 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +89 | 1713 |
| 233 | [sandeco/reversa](https://github.com/sandeco/reversa) | +87 | 690 |
| 234 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +87 | 1991 |
| 235 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +86 | 2665 |
| 236 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +86 | 13197 |
| 237 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +86 | 2540 |
| 238 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +85 | 8307 |
| 239 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +84 | 604 |
| 240 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +84 | 5375 |
| 241 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +83 | 27029 |
| 242 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +80 | 1946 |
| 243 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +78 | 536 |
| 244 | [openmemind/memind](https://github.com/openmemind/memind) | +78 | 667 |
| 245 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +77 | 48784 |
| 246 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 2301 |
| 247 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +75 | 3586 |
| 248 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +75 | 797 |
| 249 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +75 | 856 |
| 250 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +74 | 13130 |
| 251 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +74 | 11055 |
| 252 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +73 | 1741 |
| 253 | [clawplays/ospec](https://github.com/clawplays/ospec) | +72 | 613 |
| 254 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +71 | 1566 |
| 255 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +70 | 33000 |
| 256 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +69 | 1624 |
| 257 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +69 | 2026 |
| 258 | [crimera/piko](https://github.com/crimera/piko) | +69 | 3467 |
| 259 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 260 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +66 | 4095 |
| 261 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +65 | 716 |
| 262 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +65 | 27480 |
| 263 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +64 | 401 |
| 264 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +61 | 1287 |
| 265 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 392 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +59 | 3991 |
| 267 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +58 | 9498 |
| 268 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +57 | 1323 |
| 269 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +56 | 2856 |
| 270 | [halo-dev/halo](https://github.com/halo-dev/halo) | +56 | 37991 |
| 271 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +55 | 1791 |
| 272 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +55 | 37313 |
| 273 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +54 | 413 |
| 274 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +54 | 29118 |
| 275 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 466 |
| 276 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 290 |
| 277 | [jimmysu0309/shinkansen](https://github.com/jimmysu0309/shinkansen) | +50 | 294 |
| 278 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 293 |
| 279 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +47 | 5031 |
| 280 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +47 | 1961 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +46 | 3891 |
| 282 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +46 | 11881 |
| 283 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +44 | 1500 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +44 | 31476 |
| 285 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +42 | 273 |
| 286 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +40 | 440 |
| 287 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +39 | 1344 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +38 | 1861 |
| 289 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +37 | 2306 |
| 290 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +34 | 206 |
| 291 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 165 |
| 292 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 639 |
| 293 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +33 | 4044 |
| 294 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +31 | 230 |
| 295 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +30 | 2182 |
| 296 | [intave/intave](https://github.com/intave/intave) | +29 | 235 |
| 297 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +29 | 379 |
| 298 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 746 |
| 299 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 148 |
| 300 | [Horace-Maxwell/Horosa-Web-App-comprehensively-improved-MacOS](https://github.com/Horace-Maxwell/Horosa-Web-App-comprehensively-improved-MacOS) | +27 | 218 |
