---
title: "2026-05-06 GitHub增长趋势报告"
description: "1.ruflo+185 2.skills+184 3.Pixelle-Video+117 4.PageIndex+117 5.awesome-ai-apps+72"
date: 2026-05-06T21:13:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-06 21:13:05

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
        'daily': {"categories": ["LearningCircuit/local-deep-research", "PDFCraftTool/pdfcraft", "badlogic/pi-mono", "virattt/dexter", "Lum1104/Understand-Anything", "hugohe3/ppt-master", "ScrapeGraphAI/Scrapegraph-ai", "rtk-ai/rtk", "mksglu/context-mode", "vercel-labs/open-agents", "docusealco/docuseal", "soxoj/maigret", "warpdotdev/warp", "D4Vinci/Scrapling", "webadderallorg/Recordly", "Arindam200/awesome-ai-apps", "VectifyAI/PageIndex", "AIDC-AI/Pixelle-Video", "mattpocock/skills", "ruvnet/ruflo"], "data": [45, 45, 48, 50, 51, 55, 56, 57, 59, 59, 60, 64, 65, 68, 70, 72, 117, 117, 184, 185]},
        'weekly': {"categories": ["webadderallorg/Recordly", "openai/symphony", "browser-use/browser-harness", "withastro/flue", "Lum1104/Understand-Anything", "abhigyanpatwari/GitNexus", "1jehuang/jcode", "Alishahryar1/free-claude-code", "rtk-ai/rtk", "AIDC-AI/Pixelle-Video", "farion1231/cc-switch", "safishamsi/graphify", "soxoj/maigret", "D4Vinci/Scrapling", "NousResearch/hermes-agent", "ruvnet/ruflo", "warpdotdev/warp", "TauricResearch/TradingAgents", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [360, 365, 379, 417, 450, 458, 459, 505, 530, 632, 672, 808, 899, 909, 1403, 1596, 1655, 2140, 2329, 2558]},
        'monthly': {"categories": ["shanraisshan/claude-code-best-practice", "TauricResearch/TradingAgents", "ultraworkers/claw-code", "msitarzewski/agency-agents", "rtk-ai/rtk", "openclaw/openclaw", "addyosmani/agent-skills", "multica-ai/multica", "garrytan/gstack", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "santifer/career-ops", "mattpocock/skills", "obra/superpowers", "safishamsi/graphify", "JuliusBrussee/caveman", "MemPalace/mempalace", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [3222, 3233, 3377, 3436, 3531, 3736, 3839, 3868, 3898, 4255, 5272, 6035, 6337, 6557, 6959, 8033, 8119, 8834, 15847, 17974]}
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
| 1 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +185 | 45108 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +184 | 62843 |
| 3 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +117 | 12704 |
| 4 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +117 | 28671 |
| 5 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +72 | 11792 |
| 6 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +70 | 13494 |
| 7 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +68 | 46145 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +65 | 55674 |
| 9 | [soxoj/maigret](https://github.com/soxoj/maigret) | +64 | 25897 |
| 10 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +60 | 14761 |
| 11 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +59 | 4827 |
| 12 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +59 | 13583 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +57 | 42962 |
| 14 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +56 | 24392 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +55 | 12211 |
| 16 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +51 | 12829 |
| 17 | [virattt/dexter](https://github.com/virattt/dexter) | +50 | 24294 |
| 18 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +48 | 45505 |
| 19 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +45 | 5075 |
| 20 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +45 | 5575 |
| 21 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +42 | 43844 |
| 22 | [pierrecomputer/pierre](https://github.com/pierrecomputer/pierre) | +41 | 3721 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +40 | 25313 |
| 24 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +38 | 36374 |
| 25 | [openai/symphony](https://github.com/openai/symphony) | +36 | 22084 |
| 26 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +36 | 2394 |
| 27 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +33 | 11013 |
| 28 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +32 | 8178 |
| 29 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +31 | 15181 |
| 30 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +31 | 6649 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2558 | 62843 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2329 | 116320 |
| 3 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2140 | 30590 |
| 4 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1655 | 55674 |
| 5 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1596 | 45108 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1403 | 135770 |
| 7 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +909 | 46145 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | +899 | 25897 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +808 | 43844 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +672 | 61111 |
| 11 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +632 | 12705 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +530 | 42962 |
| 13 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +505 | 21995 |
| 14 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +459 | 4479 |
| 15 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +458 | 36375 |
| 16 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +450 | 12829 |
| 17 | [withastro/flue](https://github.com/withastro/flue) | +417 | 2622 |
| 18 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +379 | 11013 |
| 19 | [openai/symphony](https://github.com/openai/symphony) | +365 | 22084 |
| 20 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +360 | 13494 |
| 21 | [cursor/cookbook](https://github.com/cursor/cookbook) | +355 | 3643 |
| 22 | [virattt/dexter](https://github.com/virattt/dexter) | +347 | 24294 |
| 23 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +346 | 8178 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +346 | 30210 |
| 25 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +346 | 20132 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +343 | 12211 |
| 27 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +341 | 7120 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +320 | 45505 |
| 29 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +320 | 14761 |
| 30 | [multica-ai/multica](https://github.com/multica-ai/multica) | +303 | 25313 |
| 31 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +282 | 13583 |
| 32 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +269 | 51372 |
| 33 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +267 | 25492 |
| 34 | [browserbase/skills](https://github.com/browserbase/skills) | +262 | 2545 |
| 35 | [santifer/career-ops](https://github.com/santifer/career-ops) | +259 | 43084 |
| 36 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +252 | 4150 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +249 | 15181 |
| 38 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +247 | 3739 |
| 39 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +246 | 4864 |
| 40 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +244 | 9956 |
| 41 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +243 | 3751 |
| 42 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +237 | 11757 |
| 43 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +236 | 15781 |
| 44 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +226 | 5284 |
| 45 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +224 | 29314 |
| 46 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +223 | 17494 |
| 47 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +219 | 15572 |
| 48 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +218 | 20178 |
| 49 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +211 | 4998 |
| 50 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +210 | 34940 |
| 51 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +198 | 34257 |
| 52 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +194 | 45669 |
| 53 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +190 | 8628 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +186 | 18209 |
| 55 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +178 | 35707 |
| 56 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +169 | 11792 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +164 | 26967 |
| 58 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +163 | 9338 |
| 59 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +160 | 8593 |
| 60 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +158 | 46684 |
| 61 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +155 | 21865 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +151 | 30956 |
| 63 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +150 | 17618 |
| 64 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +148 | 28671 |
| 65 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +148 | 2402 |
| 66 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +148 | 8188 |
| 67 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +147 | 23487 |
| 68 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +146 | 23170 |
| 69 | [WeritoP/FL-STUDIO-PATCHER](https://github.com/WeritoP/FL-STUDIO-PATCHER) | +141 | 461 |
| 70 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +140 | 31064 |
| 71 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +139 | 23891 |
| 72 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +138 | 20474 |
| 73 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +137 | 42969 |
| 74 | [blader/humanizer](https://github.com/blader/humanizer) | +135 | 17556 |
| 75 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +135 | 5225 |
| 76 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +134 | 26014 |
| 77 | [appergb/openless](https://github.com/appergb/openless) | +133 | 906 |
| 78 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +133 | 1425 |
| 79 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +132 | 13442 |
| 80 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +131 | 31434 |
| 81 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +130 | 3711 |
| 82 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +128 | 12421 |
| 83 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +126 | 9966 |
| 84 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +126 | 5575 |
| 85 | [sentrux/sentrux](https://github.com/sentrux/sentrux) | +125 | 2202 |
| 86 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +125 | 17720 |
| 87 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +124 | 3514 |
| 88 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +123 | 3140 |
| 89 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +122 | 3457 |
| 90 | [therealaleph/MasterHttpRelayVPN-RUST](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | +122 | 1881 |
| 91 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +119 | 15031 |
| 92 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +117 | 12100 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +116 | 6068 |
| 94 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +115 | 58508 |
| 95 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +114 | 2536 |
| 96 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +113 | 1687 |
| 97 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +110 | 2042 |
| 98 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +110 | 5917 |
| 99 | [midudev/autoskills](https://github.com/midudev/autoskills) | +107 | 5139 |
| 100 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +103 | 2525 |
| 101 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +101 | 819 |
| 102 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +101 | 36586 |
| 103 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +99 | 4710 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +99 | 42748 |
| 105 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +97 | 1002 |
| 106 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +97 | 12990 |
| 107 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +92 | 3618 |
| 108 | [MAC-AutoML/MindPipe](https://github.com/MAC-AutoML/MindPipe) | +91 | 789 |
| 109 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +90 | 25772 |
| 110 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +90 | 4400 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +89 | 33738 |
| 112 | [olaxbt/ai-market-maker](https://github.com/olaxbt/ai-market-maker) | +89 | 1286 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +88 | 13916 |
| 114 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +87 | 5855 |
| 115 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +86 | 12708 |
| 116 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +85 | 20504 |
| 117 | [microsoft/qlib](https://github.com/microsoft/qlib) | +84 | 37792 |
| 118 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +83 | 6426 |
| 119 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +83 | 4582 |
| 120 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +81 | 2394 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17974 | 135770 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +15847 | 116320 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +8834 | 72054 |
| 4 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8119 | 51349 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8033 | 55258 |
| 6 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6959 | 43844 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +6557 | 60312 |
| 8 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6337 | 62843 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +6035 | 43084 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +5272 | 51199 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4255 | 30678 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3898 | 90420 |
| 13 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3868 | 25314 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3839 | 30211 |
| 15 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3736 | 224760 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3531 | 42963 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3436 | 94329 |
| 18 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +3377 | 190378 |
| 19 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3233 | 30590 |
| 20 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3222 | 51372 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2987 | 61111 |
| 22 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2919 | 21995 |
| 23 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2795 | 55674 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2718 | 109881 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2698 | 74774 |
| 26 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2673 | 20132 |
| 27 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2656 | 17618 |
| 28 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2437 | 15181 |
| 29 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2405 | 13442 |
| 30 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2292 | 63024 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2254 | 34148 |
| 32 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2236 | 45108 |
| 33 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2206 | 19417 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2151 | 23487 |
| 35 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2132 | 36375 |
| 36 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2122 | 55070 |
| 37 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2062 | 17494 |
| 38 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2042 | 23170 |
| 39 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2018 | 79293 |
| 40 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1997 | 34940 |
| 41 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1935 | 45505 |
| 42 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1845 | 60464 |
| 43 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1841 | 69674 |
| 44 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1840 | 27711 |
| 45 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1791 | 85286 |
| 46 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1690 | 11013 |
| 47 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1689 | 15572 |
| 48 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1662 | 46146 |
| 49 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1652 | 31434 |
| 50 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1632 | 12100 |
| 51 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1580 | 17375 |
| 52 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1570 | 25967 |
| 53 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1540 | 59381 |
| 54 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1540 | 58508 |
| 55 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1512 | 9956 |
| 56 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1510 | 24675 |
| 57 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +1499 | 26014 |
| 58 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1498 | 20480 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1475 | 29314 |
| 60 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1452 | 46684 |
| 61 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1449 | 6904 |
| 62 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1390 | 17438 |
| 63 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1366 | 11757 |
| 64 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1342 | 13495 |
| 65 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1333 | 45886 |
| 66 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1314 | 25492 |
| 67 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1295 | 15781 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1289 | 42969 |
| 69 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1289 | 98536 |
| 70 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1274 | 32742 |
| 71 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1250 | 33878 |
| 72 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1233 | 9338 |
| 73 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1232 | 8188 |
| 74 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1231 | 12211 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1192 | 30956 |
| 76 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1175 | 18209 |
| 77 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1169 | 12705 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1166 | 26967 |
| 79 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1151 | 95754 |
| 80 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1148 | 65486 |
| 81 | [github/spec-kit](https://github.com/github/spec-kit) | +1131 | 71722 |
| 82 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +1123 | 12032 |
| 83 | [openai/codex](https://github.com/openai/codex) | +1116 | 61744 |
| 84 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1075 | 45669 |
| 85 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1054 | 37330 |
| 86 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1034 | 14086 |
| 87 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1008 | 53643 |
| 88 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1003 | 24915 |
| 89 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +974 | 5593 |
| 90 | [soxoj/maigret](https://github.com/soxoj/maigret) | +972 | 25897 |
| 91 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +963 | 5855 |
| 92 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +957 | 78902 |
| 93 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +952 | 13583 |
| 94 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +927 | 5284 |
| 95 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +915 | 25945 |
| 96 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +901 | 18983 |
| 97 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +898 | 31064 |
| 98 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +897 | 51879 |
| 99 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +896 | 36586 |
| 100 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +895 | 34257 |
| 101 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +889 | 7257 |
| 102 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +875 | 17720 |
| 103 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +859 | 47122 |
| 104 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +856 | 42748 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +838 | 33738 |
| 106 | [google/magika](https://github.com/google/magika) | +838 | 16916 |
| 107 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +834 | 5917 |
| 108 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +807 | 7120 |
| 109 | [openai/symphony](https://github.com/openai/symphony) | +778 | 22084 |
| 110 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +770 | 5225 |
| 111 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +747 | 4164 |
| 112 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +736 | 21880 |
| 113 | [google-research/timesfm](https://github.com/google-research/timesfm) | +691 | 19458 |
| 114 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +683 | 6426 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +683 | 13916 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +671 | 12421 |
| 117 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +654 | 52700 |
| 118 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +648 | 29074 |
| 119 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +631 | 4400 |
| 120 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +576 | 19762 |
| 121 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +575 | 18870 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +574 | 12708 |
| 123 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +574 | 3707 |
| 124 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +564 | 4582 |
| 125 | [jundot/omlx](https://github.com/jundot/omlx) | +561 | 12430 |
| 126 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +553 | 12990 |
| 127 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +550 | 41808 |
| 128 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +534 | 4509 |
| 129 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +519 | 39841 |
| 130 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +510 | 3024 |
| 131 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +509 | 22352 |
| 132 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +505 | 3023 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +503 | 36799 |
| 134 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +503 | 3487 |
| 135 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +500 | 4159 |
| 136 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +482 | 32286 |
| 137 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +482 | 5098 |
| 138 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +482 | 11957 |
| 139 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +462 | 18031 |
| 140 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +461 | 9771 |
| 141 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +459 | 4332 |
| 142 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +434 | 20245 |
| 143 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +430 | 31340 |
| 144 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +424 | 36907 |
| 145 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +423 | 28671 |
| 146 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +410 | 7648 |
| 147 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +403 | 4143 |
| 148 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +396 | 26887 |
| 149 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +395 | 18690 |
| 150 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +394 | 37564 |
| 151 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +393 | 3457 |
| 152 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +381 | 34815 |
| 153 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +380 | 31475 |
| 154 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +376 | 8158 |
| 155 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +375 | 4710 |
| 156 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +373 | 2476 |
| 157 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +369 | 20504 |
| 158 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +362 | 8694 |
| 159 | [PostHog/posthog](https://github.com/PostHog/posthog) | +361 | 31767 |
| 160 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +359 | 2754 |
| 161 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +359 | 24739 |
| 162 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +355 | 2829 |
| 163 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +350 | 7044 |
| 164 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +343 | 23551 |
| 165 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +337 | 2102 |
| 166 | [openai/skills](https://github.com/openai/skills) | +331 | 18433 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +329 | 25772 |
| 168 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +324 | 3504 |
| 169 | [decolua/9router](https://github.com/decolua/9router) | +321 | 3992 |
| 170 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +310 | 1568 |
| 171 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +297 | 2525 |
| 172 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +296 | 3618 |
| 173 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +292 | 3209 |
| 174 | [eze-is/web-access](https://github.com/eze-is/web-access) | +291 | 6059 |
| 175 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +280 | 1718 |
| 176 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +279 | 26204 |
| 177 | [browserbase/skills](https://github.com/browserbase/skills) | +270 | 2545 |
| 178 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +268 | 2042 |
| 179 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +267 | 2023 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +265 | 27071 |
| 181 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +255 | 3140 |
| 182 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +255 | 1780 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +254 | 13203 |
| 184 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +252 | 1718 |
| 185 | [floci-io/floci](https://github.com/floci-io/floci) | +252 | 4371 |
| 186 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +251 | 3284 |
| 187 | [88lin/video_vip](https://github.com/88lin/video_vip) | +239 | 1698 |
| 188 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +237 | 9977 |
| 189 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +237 | 36103 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +222 | 3784 |
| 191 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +221 | 2654 |
| 192 | [tiagozip/cap](https://github.com/tiagozip/cap) | +212 | 6268 |
| 193 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +209 | 6214 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +201 | 2150 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +191 | 3134 |
| 196 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +187 | 16286 |
| 197 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +174 | 1181 |
| 198 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +171 | 33712 |
| 199 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +170 | 7510 |
| 200 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +165 | 9543 |
| 201 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +163 | 3458 |
| 202 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +162 | 1091 |
| 203 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +149 | 2205 |
| 204 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 205 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +144 | 3006 |
| 206 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +142 | 8126 |
| 207 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +141 | 22663 |
| 208 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +140 | 757 |
| 209 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +137 | 35473 |
| 210 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +136 | 14774 |
| 211 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +132 | 11519 |
| 212 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +132 | 4270 |
| 213 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +128 | 7517 |
| 214 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +124 | 874 |
| 215 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +123 | 39596 |
| 216 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +114 | 801 |
| 217 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +111 | 1101 |
| 218 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +111 | 5657 |
| 219 | [usebruno/bruno](https://github.com/usebruno/bruno) | +109 | 41086 |
| 220 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +108 | 29964 |
| 221 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +107 | 23803 |
| 222 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +106 | 29932 |
| 223 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +105 | 1177 |
| 224 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +105 | 808 |
| 225 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +102 | 1704 |
| 226 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +101 | 602 |
| 227 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +100 | 589 |
| 228 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +99 | 1903 |
| 229 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +98 | 668 |
| 230 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +97 | 2654 |
| 231 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +93 | 8311 |
| 232 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 5075 |
| 233 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +91 | 2055 |
| 234 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +89 | 13179 |
| 235 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +89 | 5376 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +88 | 2535 |
| 237 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +87 | 1966 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +86 | 27018 |
| 239 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +84 | 597 |
| 240 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +84 | 535 |
| 241 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +84 | 48784 |
| 242 | [sandeco/reversa](https://github.com/sandeco/reversa) | +83 | 644 |
| 243 | [cv-cat/DouYin_Spider](https://github.com/cv-cat/DouYin_Spider) | +83 | 1724 |
| 244 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +80 | 1937 |
| 245 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +80 | 11043 |
| 246 | [openmemind/memind](https://github.com/openmemind/memind) | +79 | 661 |
| 247 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +78 | 784 |
| 248 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +77 | 1558 |
| 249 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +76 | 13108 |
| 250 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +76 | 865 |
| 251 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +75 | 33000 |
| 252 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +74 | 3559 |
| 253 | [clawplays/ospec](https://github.com/clawplays/ospec) | +74 | 610 |
| 254 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +74 | 444 |
| 255 | [robinebers/openusage](https://github.com/robinebers/openusage) | +73 | 2268 |
| 256 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +73 | 2020 |
| 257 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +72 | 1736 |
| 258 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +70 | 1621 |
| 259 | [crimera/piko](https://github.com/crimera/piko) | +70 | 3459 |
| 260 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +68 | 4085 |
| 261 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +66 | 706 |
| 262 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +65 | 1274 |
| 264 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +64 | 396 |
| 265 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +63 | 3980 |
| 266 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +63 | 27471 |
| 267 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +62 | 772 |
| 268 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 379 |
| 269 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +59 | 410 |
| 270 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +59 | 2848 |
| 271 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1780 |
| 272 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +56 | 1306 |
| 273 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +56 | 29088 |
| 274 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 275 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +55 | 1497 |
| 276 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +55 | 9488 |
| 277 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 466 |
| 278 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 280 |
| 279 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +51 | 11870 |
| 280 | [jimmysu0309/shinkansen](https://github.com/jimmysu0309/shinkansen) | +50 | 294 |
| 281 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +49 | 3877 |
| 282 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +48 | 5020 |
| 283 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +48 | 292 |
| 284 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +47 | 1948 |
| 285 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +44 | 31476 |
| 286 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +42 | 271 |
| 287 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +39 | 2301 |
| 288 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +39 | 1340 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +39 | 1854 |
| 290 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +34 | 198 |
| 291 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 637 |
| 292 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 164 |
| 293 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +34 | 4039 |
| 294 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +31 | 226 |
| 295 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +30 | 2178 |
| 296 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +29 | 816 |
| 297 | [intave/intave](https://github.com/intave/intave) | +29 | 231 |
| 298 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +29 | 373 |
| 299 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +29 | 2156 |
| 300 | [Horace-Maxwell/Horosa-Web-App-comprehensively-improved-MacOS](https://github.com/Horace-Maxwell/Horosa-Web-App-comprehensively-improved-MacOS) | +29 | 215 |
