---
title: "2026-05-05 GitHub增长趋势报告"
description: "1.ruflo+291 2.skills+206 3.maigret+114 4.Understand-Anything+103 5.agent-skills+96"
date: 2026-05-05T21:05:01+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-05 21:05:01

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
        'daily': {"categories": ["abhigyanpatwari/GitNexus", "hugohe3/ppt-master", "czlonkowski/n8n-mcp", "fspecii/ace-step-ui", "cocoindex-io/cocoindex", "1jehuang/jcode", "virattt/dexter", "Alishahryar1/free-claude-code", "warpdotdev/warp", "raullenchai/Rapid-MLX", "rtk-ai/rtk", "D4Vinci/Scrapling", "AIDC-AI/Pixelle-Video", "docusealco/docuseal", "safishamsi/graphify", "addyosmani/agent-skills", "Lum1104/Understand-Anything", "soxoj/maigret", "mattpocock/skills", "ruvnet/ruflo"], "data": [44, 45, 46, 47, 50, 54, 55, 56, 66, 66, 80, 84, 86, 90, 91, 96, 103, 114, 206, 291]},
        'weekly': {"categories": ["Fincept-Corporation/FinceptTerminal", "withastro/flue", "Lum1104/Understand-Anything", "1jehuang/jcode", "openai/symphony", "abhigyanpatwari/GitNexus", "rtk-ai/rtk", "AIDC-AI/Pixelle-Video", "JuliusBrussee/caveman", "Alishahryar1/free-claude-code", "farion1231/cc-switch", "safishamsi/graphify", "soxoj/maigret", "D4Vinci/Scrapling", "ruvnet/ruflo", "NousResearch/hermes-agent", "TauricResearch/TradingAgents", "forrestchang/andrej-karpathy-skills", "warpdotdev/warp", "mattpocock/skills"], "data": [403, 408, 411, 459, 472, 488, 530, 543, 554, 576, 680, 828, 841, 849, 1427, 1446, 2076, 2260, 2689, 2950]},
        'monthly': {"categories": ["TauricResearch/TradingAgents", "shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "rtk-ai/rtk", "multica-ai/multica", "openclaw/openclaw", "garrytan/gstack", "addyosmani/agent-skills", "thedotmack/claude-mem", "ultraworkers/claw-code", "affaan-m/everything-claude-code", "mattpocock/skills", "obra/superpowers", "safishamsi/graphify", "santifer/career-ops", "MemPalace/mempalace", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [3254, 3270, 3629, 3656, 3845, 3989, 4018, 4307, 4332, 4333, 5944, 6234, 6733, 7018, 7538, 8113, 8509, 10886, 15578, 18255]}
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
| 1 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +291 | 43387 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +206 | 60733 |
| 3 | [soxoj/maigret](https://github.com/soxoj/maigret) | +114 | 25452 |
| 4 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +103 | 12405 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +96 | 28682 |
| 6 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +91 | 43233 |
| 7 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +90 | 13910 |
| 8 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +86 | 11572 |
| 9 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +84 | 45067 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +80 | 42122 |
| 11 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +66 | 1461 |
| 12 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +66 | 54873 |
| 13 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +56 | 21548 |
| 14 | [virattt/dexter](https://github.com/virattt/dexter) | +55 | 23697 |
| 15 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +54 | 4182 |
| 16 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +50 | 8338 |
| 17 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +47 | 3093 |
| 18 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +46 | 20087 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +45 | 11647 |
| 20 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +44 | 35896 |
| 21 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +41 | 1865 |
| 22 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +39 | 6829 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +37 | 14677 |
| 24 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +37 | 10604 |
| 25 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +37 | 3111 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +35 | 44949 |
| 27 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +35 | 7800 |
| 28 | [ronitsingh10/FineTune](https://github.com/ronitsingh10/FineTune) | +34 | 6533 |
| 29 | [openai/symphony](https://github.com/openai/symphony) | +32 | 21611 |
| 30 | [steipete/RepoBar](https://github.com/steipete/RepoBar) | +32 | 1814 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2950 | 60733 |
| 2 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2689 | 54873 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2260 | 113637 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2076 | 30590 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1446 | 134016 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1427 | 43387 |
| 7 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +849 | 45067 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | +841 | 25452 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +828 | 43233 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +680 | 59786 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +576 | 21548 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +554 | 54446 |
| 13 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +543 | 11572 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +530 | 42122 |
| 15 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +488 | 35896 |
| 16 | [openai/symphony](https://github.com/openai/symphony) | +472 | 21611 |
| 17 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +459 | 4182 |
| 18 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +411 | 12405 |
| 19 | [withastro/flue](https://github.com/withastro/flue) | +408 | 2527 |
| 20 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +403 | 19905 |
| 21 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +397 | 6829 |
| 22 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +384 | 28683 |
| 23 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +379 | 10604 |
| 24 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +317 | 44949 |
| 25 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +315 | 7800 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +315 | 11647 |
| 27 | [virattt/dexter](https://github.com/virattt/dexter) | +299 | 23697 |
| 28 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +294 | 12847 |
| 29 | [multica-ai/multica](https://github.com/multica-ai/multica) | +288 | 24772 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +286 | 51146 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +286 | 25186 |
| 32 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +276 | 9755 |
| 33 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +264 | 13910 |
| 34 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +263 | 46583 |
| 35 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +258 | 3897 |
| 36 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +257 | 14677 |
| 37 | [santifer/career-ops](https://github.com/santifer/career-ops) | +256 | 42783 |
| 38 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +246 | 11521 |
| 39 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +243 | 3589 |
| 40 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +242 | 12955 |
| 41 | [browserbase/skills](https://github.com/browserbase/skills) | +241 | 2338 |
| 42 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +241 | 4757 |
| 43 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +241 | 15535 |
| 44 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +236 | 3707 |
| 45 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +233 | 28999 |
| 46 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +227 | 5101 |
| 47 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +227 | 15425 |
| 48 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +224 | 34850 |
| 49 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +219 | 17404 |
| 50 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +214 | 20087 |
| 51 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +208 | 4808 |
| 52 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +205 | 8041 |
| 53 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +202 | 34081 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +195 | 45378 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +192 | 17864 |
| 56 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +176 | 3093 |
| 57 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +173 | 35707 |
| 58 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +167 | 26756 |
| 59 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +167 | 9188 |
| 60 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +161 | 8338 |
| 61 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +160 | 30746 |
| 62 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +157 | 17398 |
| 63 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +152 | 3510 |
| 64 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +150 | 2956 |
| 65 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +149 | 2350 |
| 66 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +149 | 31235 |
| 67 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +148 | 22962 |
| 68 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +147 | 5859 |
| 69 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +145 | 23357 |
| 70 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +144 | 42651 |
| 71 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +143 | 8473 |
| 72 | [WeritoP/FL-STUDIO-PATCHER](https://github.com/WeritoP/FL-STUDIO-PATCHER) | +141 | 461 |
| 73 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +140 | 21478 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +139 | 5047 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +138 | 30736 |
| 76 | [sentrux/sentrux](https://github.com/sentrux/sentrux) | +138 | 2166 |
| 77 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +136 | 23799 |
| 78 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +134 | 25920 |
| 79 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +133 | 1411 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +133 | 17300 |
| 81 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +132 | 20325 |
| 82 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +131 | 13250 |
| 83 | [therealaleph/MasterHttpRelayVPN-RUST](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | +129 | 1788 |
| 84 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +129 | 12257 |
| 85 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +125 | 9815 |
| 86 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +121 | 3367 |
| 87 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +119 | 5760 |
| 88 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +119 | 5477 |
| 89 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +118 | 17576 |
| 90 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +117 | 2506 |
| 91 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +117 | 31793 |
| 92 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +115 | 17311 |
| 93 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +114 | 1943 |
| 94 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +114 | 11872 |
| 95 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +111 | 14985 |
| 96 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +111 | 36443 |
| 97 | [midudev/autoskills](https://github.com/midudev/autoskills) | +109 | 5086 |
| 98 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +109 | 3388 |
| 99 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +106 | 1461 |
| 100 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +105 | 25666 |
| 101 | [MAC-AutoML/MindPipe](https://github.com/MAC-AutoML/MindPipe) | +105 | 746 |
| 102 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +102 | 2433 |
| 103 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +102 | 12950 |
| 104 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +98 | 4517 |
| 105 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +98 | 733 |
| 106 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +98 | 5784 |
| 107 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +97 | 11182 |
| 108 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +94 | 945 |
| 109 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +94 | 3613 |
| 110 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +93 | 4509 |
| 111 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +93 | 42620 |
| 112 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +91 | 13822 |
| 113 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +90 | 1441 |
| 114 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +89 | 26760 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +88 | 4254 |
| 116 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +88 | 1293 |
| 117 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +87 | 20420 |
| 118 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +87 | 1686 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +86 | 33563 |
| 120 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +85 | 6401 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18255 | 134016 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +15578 | 113637 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +10886 | 71448 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8509 | 54446 |
| 5 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8113 | 51229 |
| 6 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7538 | 42783 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +7018 | 43233 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +6733 | 60312 |
| 9 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6234 | 60734 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5944 | 51199 |
| 11 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +4333 | 190189 |
| 12 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4332 | 30678 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4307 | 28683 |
| 14 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4018 | 89738 |
| 15 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3989 | 224760 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3845 | 24773 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3656 | 42122 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3629 | 93520 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3270 | 51146 |
| 20 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3254 | 30590 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2993 | 59786 |
| 22 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2916 | 21548 |
| 23 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2831 | 17398 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2818 | 109881 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2806 | 74774 |
| 26 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2733 | 54873 |
| 27 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2658 | 19905 |
| 28 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2554 | 34850 |
| 29 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2484 | 62670 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2428 | 34148 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2410 | 14677 |
| 32 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2388 | 13251 |
| 33 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2320 | 35896 |
| 34 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2203 | 19299 |
| 35 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2201 | 23357 |
| 36 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2194 | 79067 |
| 37 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2141 | 43387 |
| 38 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2103 | 55070 |
| 39 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2060 | 27576 |
| 40 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2057 | 17404 |
| 41 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2031 | 22962 |
| 42 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2029 | 44949 |
| 43 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1977 | 69674 |
| 44 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1956 | 31235 |
| 45 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +1955 | 25920 |
| 46 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1910 | 60196 |
| 47 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1889 | 85286 |
| 48 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1778 | 15425 |
| 49 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1756 | 17312 |
| 50 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1746 | 59239 |
| 51 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1654 | 10604 |
| 52 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1636 | 58210 |
| 53 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1628 | 45068 |
| 54 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1617 | 11872 |
| 55 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +1579 | 11956 |
| 56 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1569 | 25945 |
| 57 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1557 | 28999 |
| 58 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1548 | 46583 |
| 59 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1515 | 24570 |
| 60 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1507 | 20324 |
| 61 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1496 | 9755 |
| 62 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1482 | 31098 |
| 63 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1445 | 6871 |
| 64 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1419 | 32593 |
| 65 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1393 | 17311 |
| 66 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1376 | 45886 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1355 | 25186 |
| 68 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1347 | 11522 |
| 69 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1333 | 33878 |
| 70 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1323 | 98536 |
| 71 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1320 | 42651 |
| 72 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1311 | 15535 |
| 73 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1301 | 12847 |
| 74 | [chenglou/pretext](https://github.com/chenglou/pretext) | +1256 | 46262 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1251 | 30736 |
| 76 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1229 | 65125 |
| 77 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1223 | 9188 |
| 78 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1223 | 8041 |
| 79 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1202 | 11647 |
| 80 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1199 | 26756 |
| 81 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1194 | 17864 |
| 82 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1172 | 95754 |
| 83 | [github/spec-kit](https://github.com/github/spec-kit) | +1172 | 71722 |
| 84 | [openai/codex](https://github.com/openai/codex) | +1141 | 61744 |
| 85 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1110 | 45378 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1100 | 37330 |
| 87 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1099 | 24819 |
| 88 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1054 | 11572 |
| 89 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1053 | 53541 |
| 90 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +978 | 18777 |
| 91 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +973 | 78902 |
| 92 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +966 | 5494 |
| 93 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +959 | 5784 |
| 94 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +956 | 36443 |
| 95 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +949 | 17576 |
| 96 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +932 | 51769 |
| 97 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +928 | 34081 |
| 98 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +921 | 25911 |
| 99 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +917 | 30746 |
| 100 | [soxoj/maigret](https://github.com/soxoj/maigret) | +916 | 25452 |
| 101 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +916 | 12955 |
| 102 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +910 | 5101 |
| 103 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +907 | 42620 |
| 104 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +897 | 33563 |
| 105 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +887 | 7240 |
| 106 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +869 | 47122 |
| 107 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +859 | 5760 |
| 108 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +853 | 28986 |
| 109 | [google/magika](https://github.com/google/magika) | +839 | 16904 |
| 110 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +792 | 21757 |
| 111 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +781 | 6829 |
| 112 | [google-research/timesfm](https://github.com/google-research/timesfm) | +764 | 19400 |
| 113 | [openai/symphony](https://github.com/openai/symphony) | +755 | 21611 |
| 114 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +746 | 4153 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +738 | 13822 |
| 116 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +723 | 6401 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +688 | 12257 |
| 118 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +681 | 52700 |
| 119 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +638 | 18802 |
| 120 | [jundot/omlx](https://github.com/jundot/omlx) | +628 | 12345 |
| 121 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +621 | 4254 |
| 122 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +597 | 11562 |
| 123 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +596 | 12597 |
| 124 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +591 | 19673 |
| 125 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +578 | 41695 |
| 126 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +574 | 3698 |
| 127 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +566 | 4509 |
| 128 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +564 | 4483 |
| 129 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +560 | 12950 |
| 130 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +552 | 22293 |
| 131 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +540 | 9758 |
| 132 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +539 | 3449 |
| 133 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +534 | 4680 |
| 134 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +533 | 39841 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +524 | 32173 |
| 136 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +513 | 36799 |
| 137 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +508 | 11958 |
| 138 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +508 | 4113 |
| 139 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +508 | 3014 |
| 140 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +496 | 2948 |
| 141 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +481 | 17933 |
| 142 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +461 | 4288 |
| 143 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +448 | 20152 |
| 144 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +439 | 31248 |
| 145 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +432 | 34773 |
| 146 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +424 | 36907 |
| 147 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +421 | 37564 |
| 148 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +418 | 18599 |
| 149 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +414 | 7590 |
| 150 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +408 | 26760 |
| 151 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +406 | 31388 |
| 152 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +402 | 4120 |
| 153 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +398 | 8067 |
| 154 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +398 | 3367 |
| 155 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +390 | 23479 |
| 156 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +385 | 4517 |
| 157 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +384 | 20420 |
| 158 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +378 | 24669 |
| 159 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +372 | 2461 |
| 160 | [PostHog/posthog](https://github.com/PostHog/posthog) | +365 | 31767 |
| 161 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +363 | 8655 |
| 162 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +359 | 2790 |
| 163 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +357 | 7022 |
| 164 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +349 | 2612 |
| 165 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +345 | 25666 |
| 166 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +344 | 3479 |
| 167 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +337 | 2096 |
| 168 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +336 | 6066 |
| 169 | [openai/skills](https://github.com/openai/skills) | +334 | 18321 |
| 170 | [decolua/9router](https://github.com/decolua/9router) | +325 | 3868 |
| 171 | [eze-is/web-access](https://github.com/eze-is/web-access) | +322 | 6013 |
| 172 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +310 | 1560 |
| 173 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +301 | 3111 |
| 174 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +296 | 3613 |
| 175 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +295 | 26145 |
| 176 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +288 | 2433 |
| 177 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +277 | 1690 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +272 | 26983 |
| 179 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +265 | 1943 |
| 180 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +263 | 13099 |
| 181 | [floci-io/floci](https://github.com/floci-io/floci) | +261 | 4359 |
| 182 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +258 | 1973 |
| 183 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +257 | 2617 |
| 184 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +251 | 1716 |
| 185 | [browserbase/skills](https://github.com/browserbase/skills) | +247 | 2338 |
| 186 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +246 | 3018 |
| 187 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +246 | 3093 |
| 188 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +246 | 9931 |
| 189 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +244 | 36103 |
| 190 | [88lin/video_vip](https://github.com/88lin/video_vip) | +237 | 1681 |
| 191 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +226 | 6172 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +225 | 3726 |
| 193 | [tiagozip/cap](https://github.com/tiagozip/cap) | +212 | 6261 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +208 | 2103 |
| 195 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +198 | 16241 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +195 | 3101 |
| 197 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +180 | 33712 |
| 198 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +178 | 7481 |
| 199 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +176 | 3443 |
| 200 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +173 | 1166 |
| 201 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +171 | 9477 |
| 202 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +160 | 1053 |
| 203 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +155 | 2989 |
| 204 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +147 | 8110 |
| 205 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +146 | 22642 |
| 207 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +141 | 11496 |
| 208 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +139 | 14744 |
| 209 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +138 | 731 |
| 210 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +138 | 4265 |
| 211 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +134 | 35473 |
| 212 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +129 | 1700 |
| 213 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +128 | 7508 |
| 214 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +127 | 844 |
| 215 | [zmeyer44/Locker](https://github.com/zmeyer44/Locker) | +126 | 745 |
| 216 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +124 | 39596 |
| 217 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +121 | 1865 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +118 | 1064 |
| 219 | [usebruno/bruno](https://github.com/usebruno/bruno) | +118 | 41086 |
| 220 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +117 | 5642 |
| 221 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +115 | 29953 |
| 222 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +114 | 780 |
| 223 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +111 | 23777 |
| 224 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +110 | 29908 |
| 225 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +106 | 1162 |
| 226 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +106 | 1887 |
| 227 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +105 | 804 |
| 228 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +104 | 2644 |
| 229 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +101 | 5374 |
| 230 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +100 | 583 |
| 231 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +99 | 8304 |
| 232 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +98 | 13166 |
| 233 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +98 | 530 |
| 234 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +98 | 555 |
| 235 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +97 | 660 |
| 236 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +92 | 2055 |
| 237 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +91 | 475 |
| 238 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +90 | 2514 |
| 239 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +90 | 1951 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +89 | 27000 |
| 241 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +88 | 518 |
| 242 | [clawplays/ospec](https://github.com/clawplays/ospec) | +87 | 609 |
| 243 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +87 | 442 |
| 244 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +87 | 11028 |
| 245 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +86 | 1550 |
| 246 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +84 | 767 |
| 247 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +84 | 48784 |
| 248 | [sandeco/reversa](https://github.com/sandeco/reversa) | +82 | 606 |
| 249 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +82 | 3531 |
| 250 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +82 | 586 |
| 251 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +81 | 4073 |
| 252 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +80 | 865 |
| 253 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +80 | 33000 |
| 254 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +79 | 13083 |
| 255 | [openmemind/memind](https://github.com/openmemind/memind) | +79 | 643 |
| 256 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1916 |
| 257 | [robinebers/openusage](https://github.com/robinebers/openusage) | +78 | 2257 |
| 258 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +78 | 1732 |
| 259 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +75 | 2003 |
| 260 | [crimera/piko](https://github.com/crimera/piko) | +75 | 3449 |
| 261 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +71 | 1616 |
| 262 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +69 | 1256 |
| 263 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +67 | 767 |
| 264 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +67 | 27462 |
| 265 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 266 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +66 | 696 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +66 | 3973 |
| 268 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +64 | 390 |
| 269 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +61 | 396 |
| 270 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +61 | 29037 |
| 271 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 374 |
| 272 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +59 | 2835 |
| 273 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +58 | 1489 |
| 274 | [microg/GmsCore](https://github.com/microg/GmsCore) | +58 | 13159 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +57 | 1766 |
| 276 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +57 | 37313 |
| 277 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 466 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +52 | 9468 |
| 279 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 277 |
| 280 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +51 | 3858 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +51 | 11859 |
| 282 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +47 | 5012 |
| 283 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +47 | 1937 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +47 | 31476 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +46 | 7384 |
| 286 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +45 | 265 |
| 287 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +42 | 268 |
| 288 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +42 | 5217 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +41 | 1846 |
| 290 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +40 | 1333 |
| 291 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +39 | 629 |
| 292 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +38 | 2290 |
| 293 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +36 | 670 |
| 294 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +35 | 4029 |
| 295 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 162 |
| 296 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +31 | 812 |
| 297 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +31 | 222 |
| 298 | [is-a-dev/register](https://github.com/is-a-dev/register) | +30 | 10222 |
| 299 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +30 | 181 |
| 300 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +30 | 2175 |
