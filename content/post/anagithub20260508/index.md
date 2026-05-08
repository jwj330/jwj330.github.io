---
title: "2026-05-08 GitHub增长趋势报告"
description: "1.financial-services-plugins+252 2.agent-skills+136 3.skills+123 4.rtk+89 5.9router+85"
date: 2026-05-08T21:03:20+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-08 21:03:20

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
        'daily': {"categories": ["CloakHQ/CloakBrowser", "heygen-com/hyperframes", "LearningCircuit/local-deep-research", "InsForge/InsForge", "KKKKhazix/khazix-skills", "badlogic/pi-mono", "datawhalechina/hello-agents", "Augani/openreel-video", "bytedance/UI-TARS-desktop", "hugohe3/ppt-master", "docusealco/docuseal", "VectifyAI/PageIndex", "D4Vinci/Scrapling", "ruvnet/ruflo", "modem-dev/hunk", "decolua/9router", "rtk-ai/rtk", "mattpocock/skills", "addyosmani/agent-skills", "anthropics/financial-services-plugins"], "data": [44, 45, 46, 46, 46, 49, 50, 51, 52, 55, 56, 56, 60, 62, 75, 85, 89, 123, 136, 252]},
        'weekly': {"categories": ["virattt/dexter", "browser-use/browser-harness", "withastro/flue", "abhigyanpatwari/GitNexus", "docusealco/docuseal", "1jehuang/jcode", "Alishahryar1/free-claude-code", "Lum1104/Understand-Anything", "rtk-ai/rtk", "addyosmani/agent-skills", "AIDC-AI/Pixelle-Video", "farion1231/cc-switch", "safishamsi/graphify", "warpdotdev/warp", "soxoj/maigret", "D4Vinci/Scrapling", "ruvnet/ruflo", "mattpocock/skills", "TauricResearch/TradingAgents", "forrestchang/andrej-karpathy-skills"], "data": [383, 386, 424, 430, 433, 435, 453, 483, 594, 614, 626, 730, 746, 843, 847, 1034, 1674, 1909, 1915, 2107]},
        'monthly': {"categories": ["farion1231/cc-switch", "Alishahryar1/free-claude-code", "msitarzewski/agency-agents", "shanraisshan/claude-code-best-practice", "TauricResearch/TradingAgents", "addyosmani/agent-skills", "rtk-ai/rtk", "santifer/career-ops", "garrytan/gstack", "multica-ai/multica", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "MemPalace/mempalace", "safishamsi/graphify", "obra/superpowers", "VoltAgent/awesome-design-md", "mattpocock/skills", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [2941, 2958, 2968, 3137, 3186, 3368, 3419, 3579, 3647, 3896, 4219, 4619, 4926, 5596, 6049, 6275, 6470, 7427, 16048, 16927]}
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
| 1 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +252 | 14744 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +136 | 35100 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +123 | 66467 |
| 4 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +89 | 44731 |
| 5 | [decolua/9router](https://github.com/decolua/9router) | +85 | 5482 |
| 6 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +75 | 2855 |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +62 | 46791 |
| 8 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +60 | 47817 |
| 9 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +56 | 30088 |
| 10 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +56 | 15902 |
| 11 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +55 | 13440 |
| 12 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +52 | 30819 |
| 13 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +51 | 2089 |
| 14 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +50 | 44504 |
| 15 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +49 | 46567 |
| 16 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +46 | 9007 |
| 17 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +46 | 9093 |
| 18 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +46 | 6683 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +45 | 16174 |
| 20 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +44 | 2836 |
| 21 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +40 | 1482 |
| 22 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +39 | 44986 |
| 23 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +38 | 3501 |
| 24 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +36 | 6044 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +34 | 26232 |
| 26 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +34 | 13741 |
| 27 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +33 | 5235 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +31 | 59125 |
| 29 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +31 | 5083 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +31 | 22761 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2107 | 120498 |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1915 | 30590 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1909 | 66467 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1674 | 46791 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1034 | 47817 |
| 6 | [soxoj/maigret](https://github.com/soxoj/maigret) | +847 | 26570 |
| 7 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +843 | 56762 |
| 8 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +746 | 44986 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +730 | 63624 |
| 10 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +626 | 13741 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +614 | 35100 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +594 | 44731 |
| 13 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +483 | 13409 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +453 | 22761 |
| 15 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +435 | 5083 |
| 16 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +433 | 15902 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +430 | 37027 |
| 18 | [withastro/flue](https://github.com/withastro/flue) | +424 | 2854 |
| 19 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +386 | 11655 |
| 20 | [virattt/dexter](https://github.com/virattt/dexter) | +383 | 24863 |
| 21 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +372 | 14744 |
| 22 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +372 | 13798 |
| 23 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +366 | 8366 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +349 | 13440 |
| 25 | [multica-ai/multica](https://github.com/multica-ai/multica) | +317 | 26213 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +313 | 46567 |
| 27 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +313 | 7637 |
| 28 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +284 | 20327 |
| 29 | [openai/symphony](https://github.com/openai/symphony) | +276 | 22648 |
| 30 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +269 | 5337 |
| 31 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +265 | 16174 |
| 32 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +262 | 6044 |
| 33 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +261 | 51803 |
| 34 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +260 | 30088 |
| 35 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +260 | 14022 |
| 36 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +259 | 3193 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +252 | 26233 |
| 38 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +237 | 16233 |
| 39 | [browserbase/skills](https://github.com/browserbase/skills) | +236 | 2714 |
| 40 | [santifer/career-ops](https://github.com/santifer/career-ops) | +232 | 43579 |
| 41 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +225 | 20369 |
| 42 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +224 | 17814 |
| 43 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +223 | 4595 |
| 44 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +221 | 9156 |
| 45 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +220 | 18948 |
| 46 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +218 | 6683 |
| 47 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +217 | 10177 |
| 48 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +217 | 12149 |
| 49 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +215 | 2855 |
| 50 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +203 | 1638 |
| 51 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +197 | 15834 |
| 52 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +195 | 35396 |
| 53 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +195 | 3800 |
| 54 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +194 | 44504 |
| 55 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +192 | 46292 |
| 56 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +186 | 12018 |
| 57 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +182 | 5284 |
| 58 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +181 | 29787 |
| 59 | [decolua/9router](https://github.com/decolua/9router) | +173 | 5482 |
| 60 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +171 | 31733 |
| 61 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +171 | 3961 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +167 | 27362 |
| 63 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +166 | 22331 |
| 64 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +160 | 8852 |
| 65 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +152 | 34650 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +152 | 31430 |
| 67 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +151 | 23659 |
| 68 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +146 | 18051 |
| 69 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +146 | 3699 |
| 70 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +144 | 5878 |
| 71 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +142 | 13844 |
| 72 | [WeritoP/FL-STUDIO-PATCHER](https://github.com/WeritoP/FL-STUDIO-PATCHER) | +142 | 465 |
| 73 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +142 | 2442 |
| 74 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +139 | 59125 |
| 75 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +139 | 9786 |
| 76 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +138 | 23705 |
| 77 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +137 | 9007 |
| 78 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +134 | 1482 |
| 79 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +134 | 10224 |
| 80 | [appergb/openless](https://github.com/appergb/openless) | +134 | 1091 |
| 81 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +132 | 3151 |
| 82 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +132 | 1985 |
| 83 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +131 | 21048 |
| 84 | [blader/humanizer](https://github.com/blader/humanizer) | +130 | 17857 |
| 85 | [RivoLink/leaf](https://github.com/RivoLink/leaf) | +130 | 979 |
| 86 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +129 | 5208 |
| 87 | [therealaleph/MasterHttpRelayVPN-RUST](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | +128 | 2113 |
| 88 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +123 | 12679 |
| 89 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +121 | 20843 |
| 90 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +120 | 3370 |
| 91 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +119 | 17758 |
| 92 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +118 | 5058 |
| 93 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +118 | 2216 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +117 | 31837 |
| 95 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +110 | 6415 |
| 96 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +109 | 5235 |
| 97 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +109 | 6218 |
| 98 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +104 | 12276 |
| 99 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +101 | 1046 |
| 100 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +98 | 2596 |
| 101 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +96 | 9093 |
| 102 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +93 | 25960 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +93 | 33971 |
| 104 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +92 | 46830 |
| 105 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +92 | 42999 |
| 106 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +91 | 2716 |
| 107 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +90 | 36843 |
| 108 | [olaxbt/ai-market-maker](https://github.com/olaxbt/ai-market-maker) | +89 | 1266 |
| 109 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +89 | 3630 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +86 | 12865 |
| 111 | [MAC-AutoML/MindPipe](https://github.com/MAC-AutoML/MindPipe) | +86 | 970 |
| 112 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +85 | 1631 |
| 113 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +85 | 1690 |
| 114 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +85 | 20686 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +84 | 4543 |
| 116 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +83 | 935 |
| 117 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +82 | 2089 |
| 118 | [z-lab/dflash](https://github.com/z-lab/dflash) | +82 | 3802 |
| 119 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +82 | 14154 |
| 120 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +80 | 3953 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +16927 | 139095 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +16048 | 120498 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7427 | 56642 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6470 | 66467 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +6275 | 73527 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +6049 | 60312 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5596 | 44986 |
| 8 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +4926 | 51610 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4619 | 51199 |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4219 | 30678 |
| 11 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3896 | 26213 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3647 | 91613 |
| 13 | [santifer/career-ops](https://github.com/santifer/career-ops) | +3579 | 43579 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3419 | 44731 |
| 15 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3368 | 35101 |
| 16 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3186 | 30590 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3137 | 51803 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2968 | 95050 |
| 19 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2958 | 22761 |
| 20 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2941 | 63624 |
| 21 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2866 | 56762 |
| 22 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2694 | 20327 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +2533 | 74774 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2518 | 109881 |
| 25 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2513 | 16174 |
| 26 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2435 | 190722 |
| 27 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2430 | 13844 |
| 28 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2301 | 18051 |
| 29 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2251 | 46791 |
| 30 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2230 | 19777 |
| 31 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2154 | 55070 |
| 32 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2076 | 63579 |
| 33 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2060 | 23659 |
| 34 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2032 | 34148 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1989 | 17814 |
| 36 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1955 | 23705 |
| 37 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1847 | 46567 |
| 38 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1775 | 37027 |
| 39 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1753 | 79773 |
| 40 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1748 | 11655 |
| 41 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1747 | 47817 |
| 42 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1707 | 60959 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1692 | 85286 |
| 44 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1646 | 12276 |
| 45 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1635 | 69674 |
| 46 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1570 | 26001 |
| 47 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1568 | 35396 |
| 48 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1543 | 27958 |
| 49 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1529 | 10177 |
| 50 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1505 | 24840 |
| 51 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1480 | 15834 |
| 52 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1430 | 6965 |
| 53 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1397 | 20590 |
| 54 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1386 | 17758 |
| 55 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1366 | 59125 |
| 56 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1350 | 59673 |
| 57 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1337 | 13798 |
| 58 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1321 | 46830 |
| 59 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1306 | 31837 |
| 60 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1295 | 12149 |
| 61 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1291 | 45886 |
| 62 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1289 | 44504 |
| 63 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1273 | 13440 |
| 64 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1271 | 16233 |
| 65 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1242 | 9786 |
| 66 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1231 | 13741 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1228 | 26233 |
| 68 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1224 | 29787 |
| 69 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1204 | 98536 |
| 70 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1164 | 17531 |
| 71 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1163 | 18948 |
| 72 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1137 | 33878 |
| 73 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1111 | 31430 |
| 74 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1106 | 27362 |
| 75 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1097 | 9007 |
| 76 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +1084 | 26188 |
| 77 | [openai/codex](https://github.com/openai/codex) | +1070 | 61744 |
| 78 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1068 | 33079 |
| 79 | [github/spec-kit](https://github.com/github/spec-kit) | +1053 | 71722 |
| 80 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1027 | 66090 |
| 81 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1020 | 46292 |
| 82 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1015 | 26570 |
| 83 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +983 | 6044 |
| 84 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +983 | 5729 |
| 85 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +982 | 37330 |
| 86 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +968 | 5961 |
| 87 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +948 | 14022 |
| 88 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +941 | 53773 |
| 89 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +934 | 78902 |
| 90 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +924 | 26077 |
| 91 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +895 | 25174 |
| 92 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +893 | 7315 |
| 93 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +879 | 52154 |
| 94 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +874 | 31733 |
| 95 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +873 | 34650 |
| 96 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +866 | 6415 |
| 97 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +864 | 22331 |
| 98 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +847 | 7637 |
| 99 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +839 | 20843 |
| 100 | [google/magika](https://github.com/google/magika) | +839 | 16939 |
| 101 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +834 | 47122 |
| 102 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +819 | 36843 |
| 103 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +814 | 5878 |
| 104 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +804 | 12191 |
| 105 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +803 | 6218 |
| 106 | [openai/symphony](https://github.com/openai/symphony) | +795 | 22648 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +782 | 42999 |
| 108 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +766 | 19339 |
| 109 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +738 | 17925 |
| 110 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +727 | 4182 |
| 111 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +724 | 13409 |
| 112 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +723 | 33971 |
| 113 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +664 | 22127 |
| 114 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +662 | 6498 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +637 | 14154 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +633 | 12679 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +626 | 4543 |
| 118 | [google-research/timesfm](https://github.com/google-research/timesfm) | +595 | 19541 |
| 119 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +580 | 19954 |
| 120 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +570 | 4705 |
| 121 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +549 | 13062 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +537 | 12865 |
| 123 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +534 | 29190 |
| 124 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +532 | 3737 |
| 125 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +515 | 3185 |
| 126 | [jundot/omlx](https://github.com/jundot/omlx) | +512 | 12588 |
| 127 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +504 | 30088 |
| 128 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +503 | 4278 |
| 129 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +495 | 39841 |
| 130 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +493 | 42013 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +490 | 36799 |
| 132 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +486 | 4553 |
| 133 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +463 | 14744 |
| 134 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +456 | 4465 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +454 | 32477 |
| 136 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +449 | 3543 |
| 137 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +447 | 11955 |
| 138 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +425 | 7978 |
| 139 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +423 | 22485 |
| 140 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +420 | 36907 |
| 141 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +418 | 18206 |
| 142 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +418 | 19032 |
| 143 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +414 | 5462 |
| 144 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +400 | 20403 |
| 145 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +400 | 31539 |
| 146 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +395 | 27025 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +393 | 3625 |
| 148 | [decolua/9router](https://github.com/decolua/9router) | +387 | 5482 |
| 149 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +374 | 2499 |
| 150 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +370 | 21048 |
| 151 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +365 | 18890 |
| 152 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +364 | 5058 |
| 153 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +363 | 2866 |
| 154 | [PostHog/posthog](https://github.com/PostHog/posthog) | +359 | 31767 |
| 155 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +359 | 3039 |
| 156 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +358 | 37564 |
| 157 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +357 | 20686 |
| 158 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +354 | 8775 |
| 159 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +344 | 8479 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +339 | 24879 |
| 161 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +338 | 2147 |
| 162 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +330 | 4189 |
| 163 | [z-lab/dflash](https://github.com/z-lab/dflash) | +327 | 3802 |
| 164 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +322 | 3567 |
| 165 | [openai/skills](https://github.com/openai/skills) | +321 | 18618 |
| 166 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +317 | 25960 |
| 167 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +310 | 1586 |
| 168 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +308 | 2716 |
| 169 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +306 | 12018 |
| 170 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +300 | 3953 |
| 171 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +299 | 3193 |
| 172 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +293 | 3630 |
| 173 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +289 | 1826 |
| 174 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +284 | 2216 |
| 175 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +281 | 9156 |
| 176 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +277 | 2144 |
| 177 | [browserbase/skills](https://github.com/browserbase/skills) | +277 | 2714 |
| 178 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +263 | 3370 |
| 179 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +263 | 1857 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +261 | 27209 |
| 181 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +260 | 1879 |
| 182 | [eze-is/web-access](https://github.com/eze-is/web-access) | +257 | 6141 |
| 183 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +253 | 26288 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +247 | 13365 |
| 185 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +240 | 3234 |
| 186 | [88lin/video_vip](https://github.com/88lin/video_vip) | +239 | 1725 |
| 187 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +234 | 1420 |
| 188 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +216 | 10049 |
| 189 | [tiagozip/cap](https://github.com/tiagozip/cap) | +213 | 6293 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +210 | 36103 |
| 191 | [floci-io/floci](https://github.com/floci-io/floci) | +206 | 4428 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +204 | 3878 |
| 193 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +203 | 1639 |
| 194 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +193 | 2692 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +191 | 2243 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +191 | 6290 |
| 197 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +186 | 3210 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +177 | 16346 |
| 199 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +174 | 2596 |
| 200 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +173 | 1197 |
| 201 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +171 | 1236 |
| 202 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +165 | 7569 |
| 203 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +160 | 33712 |
| 204 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +159 | 9619 |
| 205 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +149 | 40265 |
| 206 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +144 | 3496 |
| 207 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +143 | 789 |
| 208 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +143 | 22718 |
| 209 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +135 | 14848 |
| 210 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +134 | 8158 |
| 211 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +131 | 4369 |
| 212 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +130 | 3034 |
| 213 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +129 | 7532 |
| 214 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +125 | 35473 |
| 215 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +124 | 945 |
| 216 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +124 | 39596 |
| 217 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +117 | 831 |
| 218 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +115 | 11568 |
| 219 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +112 | 5707 |
| 220 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +110 | 5387 |
| 221 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +106 | 818 |
| 222 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +105 | 1202 |
| 223 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +105 | 29991 |
| 224 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +104 | 23833 |
| 225 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +102 | 612 |
| 226 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +102 | 681 |
| 227 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +101 | 1173 |
| 228 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +100 | 29969 |
| 229 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +100 | 605 |
| 230 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +95 | 1956 |
| 231 | [usebruno/bruno](https://github.com/usebruno/bruno) | +92 | 41086 |
| 232 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 2011 |
| 233 | [sandeco/reversa](https://github.com/sandeco/reversa) | +88 | 712 |
| 234 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +87 | 1728 |
| 235 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +84 | 670 |
| 236 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +83 | 2547 |
| 237 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +82 | 13212 |
| 238 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +81 | 1966 |
| 239 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +77 | 1515 |
| 240 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +77 | 2670 |
| 241 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +76 | 8295 |
| 242 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +75 | 13141 |
| 243 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +75 | 849 |
| 244 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +74 | 3611 |
| 245 | [robinebers/openusage](https://github.com/robinebers/openusage) | +74 | 2313 |
| 246 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +74 | 533 |
| 247 | [openmemind/memind](https://github.com/openmemind/memind) | +72 | 678 |
| 248 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +72 | 5353 |
| 249 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +71 | 48784 |
| 250 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +70 | 1747 |
| 251 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +70 | 11064 |
| 252 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +68 | 1577 |
| 253 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +68 | 2043 |
| 254 | [crimera/piko](https://github.com/crimera/piko) | +68 | 3475 |
| 255 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +67 | 811 |
| 256 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +67 | 27485 |
| 257 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 258 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +67 | 33000 |
| 259 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +66 | 1632 |
| 260 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +64 | 4103 |
| 261 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +64 | 407 |
| 262 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +61 | 720 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +61 | 1302 |
| 264 | [iamzifei/show-me-the-money](https://github.com/iamzifei/show-me-the-money) | +61 | 387 |
| 265 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 399 |
| 266 | [halo-dev/halo](https://github.com/halo-dev/halo) | +58 | 37991 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +57 | 3998 |
| 268 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +56 | 9513 |
| 269 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +55 | 2060 |
| 270 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +55 | 423 |
| 271 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +54 | 2874 |
| 272 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 466 |
| 273 | [jimmysu0309/shinkansen](https://github.com/jimmysu0309/shinkansen) | +51 | 297 |
| 274 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 291 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +51 | 1802 |
| 276 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +50 | 29127 |
| 277 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +49 | 837 |
| 278 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +49 | 3907 |
| 279 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 303 |
| 280 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +47 | 5040 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +47 | 11900 |
| 282 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +45 | 468 |
| 283 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +45 | 1971 |
| 284 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +44 | 1507 |
| 285 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +42 | 278 |
| 286 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +40 | 1352 |
| 287 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +38 | 1872 |
| 288 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +36 | 2314 |
| 289 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +34 | 210 |
| 290 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 646 |
| 291 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 170 |
| 292 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +32 | 4045 |
| 293 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +31 | 234 |
| 294 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +30 | 384 |
| 295 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +30 | 2185 |
| 296 | [intave/intave](https://github.com/intave/intave) | +29 | 238 |
| 297 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 747 |
| 298 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 155 |
| 299 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +26 | 827 |
| 300 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2161 |
