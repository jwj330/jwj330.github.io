---
title: "2026-05-09 GitHub增长趋势报告"
description: "1.financial-services-plugins+396 2.agent-skills+327 3.skills+185 4.CloakBrowser+136 5.hello-agents+132"
date: 2026-05-09T20:47:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-09 20:47:05

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
        'daily': {"categories": ["jundot/omlx", "KKKKhazix/khazix-skills", "D4Vinci/Scrapling", "Zafer-Liu/VizPilot_AI", "AIDC-AI/Pixelle-Video", "rtk-ai/rtk", "hugohe3/ppt-master", "millionco/react-doctor", "masterking32/MasterDnsVPN", "ruvnet/ruflo", "lsdefine/GenericAgent", "dwgx/WindsurfAPI", "HKUDS/AI-Trader", "decolua/9router", "bannedbook/fanqiang", "datawhalechina/hello-agents", "CloakHQ/CloakBrowser", "mattpocock/skills", "addyosmani/agent-skills", "anthropics/financial-services-plugins"], "data": [56, 56, 61, 61, 62, 66, 66, 69, 76, 77, 86, 98, 99, 118, 125, 132, 136, 185, 327, 396]},
        'weekly': {"categories": ["virattt/dexter", "bwya77/vscode-dark-islands", "1jehuang/jcode", "Lum1104/Understand-Anything", "abhigyanpatwari/GitNexus", "Alishahryar1/free-claude-code", "docusealco/docuseal", "rtk-ai/rtk", "safishamsi/graphify", "warpdotdev/warp", "AIDC-AI/Pixelle-Video", "soxoj/maigret", "anthropics/financial-services-plugins", "farion1231/cc-switch", "addyosmani/agent-skills", "D4Vinci/Scrapling", "ruvnet/ruflo", "mattpocock/skills", "TauricResearch/TradingAgents", "forrestchang/andrej-karpathy-skills"], "data": [358, 367, 393, 395, 401, 421, 447, 559, 600, 626, 637, 737, 752, 773, 894, 910, 1553, 1632, 1697, 2049]},
        'monthly': {"categories": ["santifer/career-ops", "warpdotdev/warp", "farion1231/cc-switch", "Alishahryar1/free-claude-code", "shanraisshan/claude-code-best-practice", "TauricResearch/TradingAgents", "rtk-ai/rtk", "addyosmani/agent-skills", "garrytan/gstack", "MemPalace/mempalace", "multica-ai/multica", "thedotmack/claude-mem", "affaan-m/everything-claude-code", "safishamsi/graphify", "VoltAgent/awesome-design-md", "obra/superpowers", "mattpocock/skills", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [2850, 2919, 2975, 3009, 3116, 3214, 3312, 3547, 3581, 3612, 3708, 4221, 4395, 4845, 5777, 5858, 6617, 7258, 16096, 16183]}
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
| 1 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +396 | 17203 |
| 2 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +327 | 37270 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +185 | 67929 |
| 4 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +136 | 3900 |
| 5 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +132 | 45625 |
| 6 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +125 | 42334 |
| 7 | [decolua/9router](https://github.com/decolua/9router) | +118 | 6408 |
| 8 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +99 | 15077 |
| 9 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +98 | 2001 |
| 10 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +86 | 10289 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +77 | 47712 |
| 12 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +76 | 2427 |
| 13 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +69 | 7272 |
| 14 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +66 | 13940 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +66 | 45241 |
| 16 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +62 | 14151 |
| 17 | [Zafer-Liu/VizPilot_AI](https://github.com/Zafer-Liu/VizPilot_AI) | +61 | 1 |
| 18 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +61 | 48245 |
| 19 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +56 | 9466 |
| 20 | [jundot/omlx](https://github.com/jundot/omlx) | +56 | 12983 |
| 21 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +56 | 31317 |
| 22 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +55 | 23219 |
| 23 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +54 | 45552 |
| 24 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +53 | 57075 |
| 25 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +52 | 6497 |
| 26 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +48 | 6963 |
| 27 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +47 | 26537 |
| 28 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +47 | 6199 |
| 29 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +46 | 47114 |
| 30 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +45 | 3667 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2049 | 122172 |
| 2 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1697 | 30590 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1632 | 67929 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1553 | 47712 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +910 | 48245 |
| 6 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +894 | 37270 |
| 7 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +773 | 64925 |
| 8 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +752 | 17203 |
| 9 | [soxoj/maigret](https://github.com/soxoj/maigret) | +737 | 27021 |
| 10 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +637 | 14151 |
| 11 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +626 | 57075 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +600 | 45552 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +559 | 45241 |
| 14 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +447 | 16065 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +421 | 23219 |
| 16 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +401 | 37261 |
| 17 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +395 | 13701 |
| 18 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +393 | 5305 |
| 19 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +367 | 8380 |
| 20 | [virattt/dexter](https://github.com/virattt/dexter) | +358 | 25015 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +340 | 13940 |
| 22 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +325 | 11826 |
| 23 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +312 | 45625 |
| 24 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +310 | 13884 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +309 | 47114 |
| 26 | [multica-ai/multica](https://github.com/multica-ai/multica) | +304 | 26589 |
| 27 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +281 | 30267 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +279 | 3667 |
| 29 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +274 | 7798 |
| 30 | [decolua/9router](https://github.com/decolua/9router) | +273 | 6408 |
| 31 | [openai/symphony](https://github.com/openai/symphony) | +271 | 22930 |
| 32 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +265 | 26537 |
| 33 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +261 | 6963 |
| 34 | [withastro/flue](https://github.com/withastro/flue) | +256 | 2970 |
| 35 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +251 | 6497 |
| 36 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +245 | 16509 |
| 37 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +240 | 14154 |
| 38 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +240 | 5408 |
| 39 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +238 | 16428 |
| 40 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +236 | 51999 |
| 41 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +233 | 19284 |
| 42 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +232 | 3003 |
| 43 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +230 | 20440 |
| 44 | [santifer/career-ops](https://github.com/santifer/career-ops) | +220 | 43765 |
| 45 | [browserbase/skills](https://github.com/browserbase/skills) | +216 | 2945 |
| 46 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +216 | 20461 |
| 47 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +211 | 9310 |
| 48 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +209 | 1670 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +202 | 46562 |
| 50 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +201 | 3900 |
| 51 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +195 | 12359 |
| 52 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +194 | 10289 |
| 53 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +189 | 10240 |
| 54 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +187 | 12053 |
| 55 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +183 | 32007 |
| 56 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +177 | 4781 |
| 57 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +177 | 35551 |
| 58 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +173 | 5372 |
| 59 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +172 | 12849 |
| 60 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +170 | 27551 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +168 | 30051 |
| 62 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +164 | 9467 |
| 63 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +164 | 22470 |
| 64 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +164 | 18044 |
| 65 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +163 | 59379 |
| 66 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +163 | 15960 |
| 67 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +163 | 8963 |
| 68 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +154 | 34861 |
| 69 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +152 | 18258 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +151 | 31661 |
| 71 | [walkinglabs/hands-on-modern-rl](https://github.com/walkinglabs/hands-on-modern-rl) | +150 | 1575 |
| 72 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +148 | 14083 |
| 73 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +148 | 6070 |
| 74 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +142 | 2427 |
| 75 | [WeritoP/FL-STUDIO-PATCHER](https://github.com/WeritoP/FL-STUDIO-PATCHER) | +142 | 467 |
| 76 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +141 | 21119 |
| 77 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +140 | 5314 |
| 78 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +140 | 23781 |
| 79 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +140 | 42334 |
| 80 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +140 | 2982 |
| 81 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +137 | 1733 |
| 82 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +137 | 3241 |
| 83 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +136 | 2036 |
| 84 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +134 | 10362 |
| 85 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +129 | 8210 |
| 86 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +128 | 2001 |
| 87 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +128 | 32022 |
| 88 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +126 | 15077 |
| 89 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +122 | 6575 |
| 90 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +119 | 31317 |
| 91 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +118 | 5230 |
| 92 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +116 | 23730 |
| 93 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +115 | 6372 |
| 94 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +114 | 5283 |
| 95 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +114 | 3815 |
| 96 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +113 | 12779 |
| 97 | [jundot/omlx](https://github.com/jundot/omlx) | +112 | 12983 |
| 98 | [z-lab/dflash](https://github.com/z-lab/dflash) | +111 | 4034 |
| 99 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +111 | 2716 |
| 100 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +102 | 4221 |
| 101 | [InsForge/InsForge](https://github.com/InsForge/InsForge) | +101 | 9222 |
| 102 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +100 | 1060 |
| 103 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +99 | 2305 |
| 104 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +97 | 26078 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +96 | 36960 |
| 106 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +94 | 12314 |
| 107 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +94 | 34064 |
| 108 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +94 | 2867 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +90 | 43139 |
| 110 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +86 | 24797 |
| 111 | [nikzad-avasam/downloader](https://github.com/nikzad-avasam/downloader) | +85 | 771 |
| 112 | [MrsEWE44/musicDownload](https://github.com/MrsEWE44/musicDownload) | +84 | 1659 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +79 | 12921 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +78 | 14241 |
| 115 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +77 | 25285 |
| 116 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +77 | 1774 |
| 117 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +76 | 46889 |
| 118 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +76 | 4618 |
| 119 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +74 | 3592 |
| 120 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +72 | 970 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +16183 | 140824 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +16096 | 122172 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7258 | 57056 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6617 | 67929 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +5858 | 60312 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5777 | 74097 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4845 | 45552 |
| 8 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +4395 | 51199 |
| 9 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4221 | 30678 |
| 10 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3708 | 26589 |
| 11 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +3612 | 51765 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3581 | 92300 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3547 | 37270 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3312 | 45241 |
| 15 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3214 | 30590 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3116 | 51999 |
| 17 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3009 | 23219 |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2975 | 64925 |
| 19 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2919 | 57075 |
| 20 | [santifer/career-ops](https://github.com/santifer/career-ops) | +2850 | 43765 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2821 | 95335 |
| 22 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2708 | 20461 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2535 | 16509 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2470 | 74774 |
| 25 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2469 | 109881 |
| 26 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2434 | 14083 |
| 27 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2298 | 47712 |
| 28 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2246 | 19901 |
| 29 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2187 | 190855 |
| 30 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2173 | 55070 |
| 31 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2080 | 18258 |
| 32 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2041 | 23781 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2030 | 34148 |
| 34 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2010 | 63764 |
| 35 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1925 | 18044 |
| 36 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1830 | 47114 |
| 37 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1795 | 48245 |
| 38 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1758 | 11826 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1753 | 23730 |
| 40 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1686 | 37262 |
| 41 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1681 | 85286 |
| 42 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1673 | 80003 |
| 43 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1649 | 12314 |
| 44 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1642 | 61127 |
| 45 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1599 | 69674 |
| 46 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1566 | 26019 |
| 47 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1536 | 10240 |
| 48 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1516 | 24922 |
| 49 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1484 | 12849 |
| 50 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1451 | 35551 |
| 51 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1417 | 28055 |
| 52 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1393 | 17870 |
| 53 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1387 | 15960 |
| 54 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1377 | 45625 |
| 55 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1327 | 10289 |
| 56 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1316 | 13940 |
| 57 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1297 | 59379 |
| 58 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1286 | 14151 |
| 59 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1268 | 46889 |
| 60 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1268 | 20752 |
| 61 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1250 | 16428 |
| 62 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1249 | 12359 |
| 63 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1238 | 6998 |
| 64 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1236 | 59770 |
| 65 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1229 | 45886 |
| 66 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1210 | 13884 |
| 67 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1208 | 26537 |
| 68 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1206 | 32022 |
| 69 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1204 | 30051 |
| 70 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1177 | 98536 |
| 71 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1159 | 19284 |
| 72 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1129 | 9467 |
| 73 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1095 | 33878 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1090 | 31661 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1082 | 61744 |
| 76 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1068 | 27551 |
| 77 | [github/spec-kit](https://github.com/github/spec-kit) | +1057 | 71722 |
| 78 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1054 | 27021 |
| 79 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1029 | 17610 |
| 80 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1015 | 46562 |
| 81 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +995 | 26246 |
| 82 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +991 | 5780 |
| 83 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +989 | 33194 |
| 84 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +985 | 6497 |
| 85 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +980 | 66249 |
| 86 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +978 | 6016 |
| 87 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +965 | 37330 |
| 88 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +953 | 14154 |
| 89 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +932 | 78902 |
| 90 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +925 | 26109 |
| 91 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +917 | 53844 |
| 92 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +893 | 7334 |
| 93 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +878 | 52263 |
| 94 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +872 | 34861 |
| 95 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +872 | 25285 |
| 96 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +870 | 32007 |
| 97 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +867 | 7798 |
| 98 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +851 | 6575 |
| 99 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +850 | 17203 |
| 100 | [google/magika](https://github.com/google/magika) | +840 | 16945 |
| 101 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +836 | 6070 |
| 102 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +832 | 47122 |
| 103 | [openai/symphony](https://github.com/openai/symphony) | +815 | 22930 |
| 104 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +792 | 6372 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +786 | 36960 |
| 106 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +771 | 43139 |
| 107 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +746 | 13701 |
| 108 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +728 | 19472 |
| 109 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +717 | 12252 |
| 110 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +717 | 18038 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +693 | 34064 |
| 112 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +662 | 6564 |
| 113 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +633 | 22200 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +621 | 14241 |
| 115 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +618 | 4618 |
| 116 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +580 | 4194 |
| 117 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +578 | 19996 |
| 118 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +576 | 4746 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +574 | 12779 |
| 120 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +550 | 13089 |
| 121 | [google-research/timesfm](https://github.com/google-research/timesfm) | +544 | 19577 |
| 122 | [jundot/omlx](https://github.com/jundot/omlx) | +543 | 12983 |
| 123 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +528 | 3766 |
| 124 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +527 | 12921 |
| 125 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +515 | 3250 |
| 126 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +506 | 4367 |
| 127 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +502 | 29231 |
| 128 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +498 | 30267 |
| 129 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +485 | 39841 |
| 130 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +484 | 42087 |
| 131 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +480 | 36799 |
| 132 | [decolua/9router](https://github.com/decolua/9router) | +469 | 6408 |
| 133 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +463 | 4571 |
| 134 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +448 | 32545 |
| 135 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +445 | 8457 |
| 136 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +431 | 3591 |
| 137 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +421 | 11955 |
| 138 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +418 | 36907 |
| 139 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +409 | 22544 |
| 140 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +404 | 4596 |
| 141 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +401 | 19076 |
| 142 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +400 | 18257 |
| 143 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +397 | 5581 |
| 144 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +397 | 31617 |
| 145 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +394 | 20497 |
| 146 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +390 | 27074 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +388 | 3707 |
| 148 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +375 | 2515 |
| 149 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +373 | 2930 |
| 150 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +366 | 21119 |
| 151 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +363 | 18970 |
| 152 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +359 | 20761 |
| 153 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +357 | 8838 |
| 154 | [PostHog/posthog](https://github.com/PostHog/posthog) | +356 | 31767 |
| 155 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +354 | 5230 |
| 156 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +348 | 37564 |
| 157 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +346 | 2207 |
| 158 | [z-lab/dflash](https://github.com/z-lab/dflash) | +345 | 4034 |
| 159 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +342 | 3667 |
| 160 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +340 | 8573 |
| 161 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +334 | 24952 |
| 162 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +330 | 4221 |
| 163 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +324 | 15077 |
| 164 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +322 | 2867 |
| 165 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +321 | 3584 |
| 166 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +318 | 4209 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +316 | 26078 |
| 168 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +311 | 1593 |
| 169 | [openai/skills](https://github.com/openai/skills) | +310 | 18693 |
| 170 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +308 | 3853 |
| 171 | [browserbase/skills](https://github.com/browserbase/skills) | +306 | 2945 |
| 172 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +297 | 9310 |
| 173 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +296 | 2302 |
| 174 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +291 | 1881 |
| 175 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +281 | 2206 |
| 176 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +278 | 6963 |
| 177 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +275 | 3505 |
| 178 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +265 | 1878 |
| 179 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +260 | 3900 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +260 | 27289 |
| 181 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +254 | 2002 |
| 182 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +244 | 26329 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +244 | 13432 |
| 184 | [eze-is/web-access](https://github.com/eze-is/web-access) | +243 | 6186 |
| 185 | [88lin/video_vip](https://github.com/88lin/video_vip) | +238 | 1742 |
| 186 | [tiagozip/cap](https://github.com/tiagozip/cap) | +215 | 6307 |
| 187 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +208 | 1670 |
| 188 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +208 | 10068 |
| 189 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +208 | 36103 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +203 | 3916 |
| 191 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +200 | 3047 |
| 192 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +200 | 3246 |
| 193 | [floci-io/floci](https://github.com/floci-io/floci) | +200 | 4721 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +193 | 2289 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +192 | 3249 |
| 196 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +185 | 2715 |
| 197 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +182 | 6325 |
| 198 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +177 | 2716 |
| 199 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +174 | 1209 |
| 200 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +173 | 16380 |
| 201 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +159 | 7632 |
| 202 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +154 | 9653 |
| 203 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +144 | 40265 |
| 204 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +143 | 801 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +139 | 22745 |
| 206 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +138 | 3513 |
| 207 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +134 | 14886 |
| 208 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +131 | 4379 |
| 209 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +130 | 8178 |
| 210 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +129 | 7537 |
| 211 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +128 | 3045 |
| 212 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +124 | 35473 |
| 213 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +122 | 978 |
| 214 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +122 | 39596 |
| 215 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +119 | 837 |
| 216 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +116 | 5491 |
| 217 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +113 | 11596 |
| 218 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +113 | 5739 |
| 219 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +109 | 30007 |
| 220 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +106 | 1213 |
| 221 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +106 | 824 |
| 222 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +104 | 620 |
| 223 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +103 | 629 |
| 224 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +103 | 686 |
| 225 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +102 | 1203 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +102 | 23854 |
| 227 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +98 | 29981 |
| 228 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +94 | 743 |
| 229 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +90 | 1972 |
| 230 | [sandeco/reversa](https://github.com/sandeco/reversa) | +89 | 722 |
| 231 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +88 | 1595 |
| 232 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +88 | 2030 |
| 233 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +87 | 695 |
| 234 | [usebruno/bruno](https://github.com/usebruno/bruno) | +87 | 41086 |
| 235 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +83 | 1983 |
| 236 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +82 | 1737 |
| 237 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +82 | 2567 |
| 238 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +75 | 13221 |
| 239 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +74 | 13160 |
| 240 | [robinebers/openusage](https://github.com/robinebers/openusage) | +73 | 2330 |
| 241 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +73 | 849 |
| 242 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +72 | 2679 |
| 243 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +71 | 3639 |
| 244 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +71 | 8302 |
| 245 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +71 | 11075 |
| 246 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 247 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +70 | 14435 |
| 248 | [openmemind/memind](https://github.com/openmemind/memind) | +69 | 693 |
| 249 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +69 | 5354 |
| 250 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +68 | 1592 |
| 251 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +68 | 2056 |
| 252 | [crimera/piko](https://github.com/crimera/piko) | +67 | 3482 |
| 253 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +66 | 1642 |
| 254 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +66 | 1749 |
| 255 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +65 | 27482 |
| 256 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +65 | 48784 |
| 257 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +64 | 416 |
| 258 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +63 | 33000 |
| 259 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +61 | 730 |
| 260 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +61 | 4112 |
| 261 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +60 | 817 |
| 262 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 401 |
| 263 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +60 | 434 |
| 264 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +57 | 1317 |
| 265 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +57 | 9524 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +55 | 4003 |
| 267 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +55 | 2891 |
| 268 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +55 | 37313 |
| 269 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 270 | [jimmysu0309/shinkansen](https://github.com/jimmysu0309/shinkansen) | +51 | 299 |
| 271 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 296 |
| 272 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +50 | 847 |
| 273 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +50 | 1805 |
| 274 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +50 | 29139 |
| 275 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +49 | 323 |
| 276 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +46 | 477 |
| 277 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +46 | 3930 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +45 | 11916 |
| 279 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +45 | 1980 |
| 280 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +44 | 5050 |
| 281 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +42 | 282 |
| 282 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +41 | 31476 |
| 283 | [Arvincreator/project-golem](https://github.com/Arvincreator/project-golem) | +40 | 590 |
| 284 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +40 | 1358 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +40 | 1512 |
| 286 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +37 | 2324 |
| 287 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +34 | 212 |
| 288 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +34 | 646 |
| 289 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 175 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +34 | 1879 |
| 291 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +33 | 396 |
| 292 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +31 | 4050 |
| 293 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +30 | 2185 |
| 294 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +30 | 235 |
| 295 | [intave/intave](https://github.com/intave/intave) | +29 | 240 |
| 296 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +27 | 747 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +27 | 829 |
| 298 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 162 |
| 299 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2166 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +26 | 10249 |
