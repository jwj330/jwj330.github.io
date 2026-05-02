---
title: "2026-05-02 GitHub增长趋势报告"
description: "1.skills+503 2.warp+283 3.graphify+226 4.ruflo+222 5.Scrapling+202"
date: 2026-05-02T20:43:26+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-02 20:43:26

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
        'daily': {"categories": ["ComposioHQ/awesome-codex-skills", "browser-use/browser-harness", "hugohe3/ppt-master", "freestylefly/awesome-gpt-image-2", "1jehuang/jcode", "webadderallorg/Recordly", "tonhowtf/omniget", "Fincept-Corporation/FinceptTerminal", "evoiz/Agentic-Design-Patterns", "Alishahryar1/free-claude-code", "OpenBMB/VoxCPM", "rtk-ai/rtk", "Lum1104/Understand-Anything", "soxoj/maigret", "withastro/flue", "D4Vinci/Scrapling", "ruvnet/ruflo", "safishamsi/graphify", "warpdotdev/warp", "mattpocock/skills"], "data": [67, 75, 78, 78, 83, 83, 86, 89, 92, 92, 100, 109, 128, 158, 193, 202, 222, 226, 283, 503]},
        'weekly': {"categories": ["openai/symphony", "heygen-com/hyperframes", "ComposioHQ/awesome-codex-skills", "badlogic/pi-mono", "addyosmani/agent-skills", "microsoft/VibeVoice", "Fincept-Corporation/FinceptTerminal", "rtk-ai/rtk", "JuliusBrussee/caveman", "abhigyanpatwari/GitNexus", "farion1231/cc-switch", "safishamsi/graphify", "refactoringhq/tolaria", "TauricResearch/TradingAgents", "Z4nzu/hackingtool", "Alishahryar1/free-claude-code", "NousResearch/hermes-agent", "warpdotdev/warp", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [444, 472, 532, 538, 574, 623, 639, 673, 691, 698, 816, 822, 905, 906, 1132, 1584, 1724, 2277, 2979, 4198]},
        'monthly': {"categories": ["rtk-ai/rtk", "multica-ai/multica", "msitarzewski/agency-agents", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "thedotmack/claude-mem", "garrytan/gstack", "openclaw/openclaw", "addyosmani/agent-skills", "mattpocock/skills", "safishamsi/graphify", "affaan-m/everything-claude-code", "obra/superpowers", "santifer/career-ops", "MemPalace/mempalace", "JuliusBrussee/caveman", "ultraworkers/claw-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [3675, 3780, 3847, 3990, 4172, 4314, 4409, 4508, 4715, 5416, 6608, 7120, 7244, 7408, 8033, 8260, 11288, 12497, 14375, 18312]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +503 | 54801 |
| 2 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +283 | 52636 |
| 3 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +226 | 40640 |
| 4 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +222 | 36581 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +202 | 41519 |
| 6 | [withastro/flue](https://github.com/withastro/flue) | +193 | 1587 |
| 7 | [soxoj/maigret](https://github.com/soxoj/maigret) | +158 | 22512 |
| 8 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +128 | 10515 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +109 | 39977 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +100 | 16881 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +92 | 20166 |
| 12 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +92 | 1328 |
| 13 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +89 | 19096 |
| 14 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +86 | 3179 |
| 15 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +83 | 11634 |
| 16 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +83 | 2755 |
| 17 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +78 | 3247 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +78 | 10729 |
| 19 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +75 | 9540 |
| 20 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +67 | 5800 |
| 21 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +63 | 4489 |
| 22 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +62 | 34583 |
| 23 | [virattt/dexter](https://github.com/virattt/dexter) | +61 | 22188 |
| 24 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +60 | 2971 |
| 25 | [amir1376/ab-download-manager](https://github.com/amir1376/ab-download-manager) | +59 | 15124 |
| 26 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +58 | 9131 |
| 27 | [simstudioai/sim](https://github.com/simstudioai/sim) | +54 | 28296 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +53 | 43845 |
| 29 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +53 | 3552 |
| 30 | [browserbase/skills](https://github.com/browserbase/skills) | +53 | 1456 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4198 | 54801 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2979 | 106356 |
| 3 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2277 | 52636 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1724 | 129588 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1584 | 20166 |
| 6 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1132 | 55070 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +906 | 30590 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +905 | 8895 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +822 | 40640 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +816 | 57822 |
| 11 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +698 | 34583 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +691 | 52435 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +673 | 39977 |
| 14 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +639 | 19096 |
| 15 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +623 | 46265 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +574 | 27161 |
| 17 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +538 | 43845 |
| 18 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +532 | 5800 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +472 | 13876 |
| 20 | [openai/symphony](https://github.com/openai/symphony) | +444 | 20679 |
| 21 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +427 | 10818 |
| 22 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +408 | 3247 |
| 23 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +383 | 36582 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +372 | 23752 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +362 | 10730 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +360 | 9540 |
| 27 | [santifer/career-ops](https://github.com/santifer/career-ops) | +334 | 41809 |
| 28 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +334 | 4633 |
| 29 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +323 | 41519 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +291 | 50442 |
| 31 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +288 | 1415 |
| 32 | [soxoj/maigret](https://github.com/soxoj/maigret) | +286 | 22512 |
| 33 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +280 | 4489 |
| 34 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +279 | 4190 |
| 35 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +268 | 16865 |
| 36 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +264 | 17247 |
| 37 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +261 | 11961 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +258 | 24284 |
| 39 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +254 | 5483 |
| 40 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +251 | 9131 |
| 41 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +251 | 30775 |
| 42 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +250 | 28298 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +246 | 33679 |
| 44 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +245 | 13468 |
| 45 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +243 | 4112 |
| 46 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +243 | 22953 |
| 47 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +239 | 8794 |
| 48 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +234 | 10515 |
| 49 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +234 | 42225 |
| 50 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +220 | 3161 |
| 51 | [gastownhall/beads](https://github.com/gastownhall/beads) | +219 | 22998 |
| 52 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +216 | 2015 |
| 53 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +211 | 2755 |
| 54 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +211 | 14537 |
| 55 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +211 | 26599 |
| 56 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +208 | 34258 |
| 57 | [trycua/cua](https://github.com/trycua/cua) | +208 | 15504 |
| 58 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +207 | 27220 |
| 59 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +206 | 14841 |
| 60 | [PostHog/posthog](https://github.com/PostHog/posthog) | +205 | 31767 |
| 61 | [withastro/flue](https://github.com/withastro/flue) | +204 | 1587 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +202 | 16903 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +199 | 44798 |
| 64 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +199 | 57825 |
| 65 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +198 | 7787 |
| 66 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +195 | 26123 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +193 | 30322 |
| 68 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +193 | 10583 |
| 69 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +187 | 30270 |
| 70 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +183 | 4930 |
| 71 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +179 | 8487 |
| 72 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +179 | 2446 |
| 73 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +177 | 22490 |
| 74 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +173 | 20906 |
| 75 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +173 | 12815 |
| 76 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +172 | 2971 |
| 77 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +172 | 12754 |
| 78 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +171 | 19931 |
| 79 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +171 | 4081 |
| 80 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +169 | 25504 |
| 81 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +169 | 18500 |
| 82 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +164 | 1525 |
| 83 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +162 | 5367 |
| 84 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +162 | 4249 |
| 85 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +160 | 16881 |
| 86 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +158 | 11634 |
| 87 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +157 | 24307 |
| 88 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +156 | 42251 |
| 89 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +155 | 7006 |
| 90 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +154 | 32281 |
| 91 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +152 | 5574 |
| 92 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +151 | 3179 |
| 93 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +148 | 9463 |
| 94 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +146 | 2254 |
| 95 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | +145 | 2134 |
| 96 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +144 | 36062 |
| 97 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +143 | 6147 |
| 98 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +142 | 11831 |
| 99 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +142 | 2089 |
| 100 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +139 | 3552 |
| 101 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +139 | 1136 |
| 102 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +138 | 1816 |
| 103 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +138 | 13710 |
| 104 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | +137 | 5696 |
| 105 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +136 | 1590 |
| 106 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +134 | 1412 |
| 107 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +134 | 25771 |
| 108 | [wxyhgk/retain-pdf](https://github.com/wxyhgk/retain-pdf) | +132 | 1332 |
| 109 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +119 | 31047 |
| 110 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +117 | 19528 |
| 111 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +116 | 5246 |
| 112 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +113 | 1184 |
| 113 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +105 | 2863 |
| 114 | [google-research/timesfm](https://github.com/google-research/timesfm) | +105 | 19271 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +104 | 13468 |
| 116 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +101 | 1328 |
| 117 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +101 | 36799 |
| 118 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +99 | 31966 |
| 119 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +98 | 3971 |
| 120 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +96 | 2421 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18312 | 129588 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +14375 | 106356 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12497 | 69714 |
| 4 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +11288 | 189668 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8260 | 52435 |
| 6 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8033 | 50772 |
| 7 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7408 | 41809 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +7244 | 60312 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +7120 | 51199 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6608 | 40640 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5416 | 54801 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4715 | 27161 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4508 | 224760 |
| 14 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4409 | 88141 |
| 15 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4314 | 30678 |
| 16 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4172 | 25504 |
| 17 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3990 | 34258 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3847 | 90526 |
| 19 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3780 | 23752 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3675 | 39977 |
| 21 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3428 | 27220 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3396 | 50442 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +3044 | 74774 |
| 24 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3034 | 57822 |
| 25 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3020 | 61723 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3006 | 109881 |
| 27 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2894 | 69674 |
| 28 | [chenglou/pretext](https://github.com/chenglou/pretext) | +2785 | 46031 |
| 29 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2775 | 16865 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2691 | 20166 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2630 | 34148 |
| 32 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2600 | 78490 |
| 33 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2592 | 30775 |
| 34 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2501 | 19096 |
| 35 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2359 | 11743 |
| 36 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2322 | 52636 |
| 37 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2314 | 12754 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2294 | 13876 |
| 39 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2247 | 17144 |
| 40 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2208 | 22953 |
| 41 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2204 | 34583 |
| 42 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2186 | 30590 |
| 43 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2168 | 18982 |
| 44 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2154 | 43845 |
| 45 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2042 | 59441 |
| 46 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2029 | 58814 |
| 47 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1987 | 32281 |
| 48 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1985 | 85286 |
| 49 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1968 | 16881 |
| 50 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1965 | 22490 |
| 51 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1932 | 31098 |
| 52 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1906 | 57825 |
| 53 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1902 | 55070 |
| 54 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1859 | 14841 |
| 55 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1816 | 46265 |
| 56 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1759 | 28868 |
| 57 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1662 | 28298 |
| 58 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +1637 | 17411 |
| 59 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1624 | 33878 |
| 60 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1564 | 25886 |
| 61 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1529 | 64523 |
| 62 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1504 | 24307 |
| 63 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1500 | 19906 |
| 64 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1470 | 10221 |
| 65 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1437 | 9540 |
| 66 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1433 | 6808 |
| 67 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +1403 | 18500 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1395 | 30322 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1387 | 42225 |
| 70 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1387 | 98536 |
| 71 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1369 | 16940 |
| 72 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1358 | 22476 |
| 73 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1351 | 45886 |
| 74 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1348 | 8895 |
| 75 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1319 | 6688 |
| 76 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1313 | 24578 |
| 77 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1313 | 17086 |
| 78 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1305 | 24284 |
| 79 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1292 | 95754 |
| 80 | [github/spec-kit](https://github.com/github/spec-kit) | +1265 | 71722 |
| 81 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1228 | 10818 |
| 82 | [openai/codex](https://github.com/openai/codex) | +1228 | 61744 |
| 83 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1227 | 19271 |
| 84 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1221 | 14537 |
| 85 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1218 | 26123 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1209 | 37330 |
| 87 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1209 | 73135 |
| 88 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1207 | 11634 |
| 89 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1201 | 44798 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1200 | 17247 |
| 91 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1192 | 53245 |
| 92 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1182 | 7787 |
| 93 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1175 | 13710 |
| 94 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1164 | 33220 |
| 95 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1150 | 8794 |
| 96 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1121 | 10730 |
| 97 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1121 | 36582 |
| 98 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1080 | 41519 |
| 99 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1070 | 36062 |
| 100 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1053 | 42251 |
| 101 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +999 | 9340 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +997 | 78902 |
| 103 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +985 | 79656 |
| 104 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +978 | 51410 |
| 105 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +932 | 33679 |
| 106 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +924 | 5246 |
| 107 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +919 | 5574 |
| 108 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +917 | 25771 |
| 109 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +901 | 21500 |
| 110 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +878 | 7174 |
| 111 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +843 | 4599 |
| 112 | [google/magika](https://github.com/google/magika) | +835 | 16861 |
| 113 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +831 | 47122 |
| 114 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +826 | 5367 |
| 115 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +815 | 52700 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +812 | 13468 |
| 117 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +793 | 4489 |
| 118 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +763 | 6147 |
| 119 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +763 | 18636 |
| 120 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +742 | 4117 |
| 121 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +729 | 9735 |
| 122 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +722 | 4969 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +721 | 11831 |
| 124 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +673 | 9131 |
| 125 | [jundot/omlx](https://github.com/jundot/omlx) | +670 | 12126 |
| 126 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +658 | 19528 |
| 127 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +650 | 12334 |
| 128 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +645 | 22133 |
| 129 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +640 | 41521 |
| 130 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +630 | 11959 |
| 131 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +625 | 54903 |
| 132 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +624 | 5800 |
| 133 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +596 | 11551 |
| 134 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +583 | 4332 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +582 | 31966 |
| 136 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +580 | 39841 |
| 137 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +573 | 3971 |
| 138 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +570 | 34676 |
| 139 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +565 | 4249 |
| 140 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +565 | 3622 |
| 141 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +557 | 36799 |
| 142 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +544 | 2693 |
| 143 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +540 | 12815 |
| 144 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +540 | 3330 |
| 145 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +504 | 17739 |
| 146 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +504 | 2980 |
| 147 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +486 | 19918 |
| 148 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +479 | 23359 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +478 | 31047 |
| 150 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +475 | 3879 |
| 151 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +473 | 2804 |
| 152 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +468 | 37564 |
| 153 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +462 | 5981 |
| 154 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +461 | 18415 |
| 155 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +454 | 26058 |
| 156 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +453 | 2539 |
| 157 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +450 | 5026 |
| 158 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +442 | 7914 |
| 159 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +437 | 4082 |
| 160 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +433 | 25277 |
| 161 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +421 | 31187 |
| 162 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +420 | 7458 |
| 163 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +419 | 36907 |
| 164 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +413 | 26599 |
| 165 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +406 | 2685 |
| 166 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +403 | 20187 |
| 167 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +403 | 4058 |
| 168 | [eze-is/web-access](https://github.com/eze-is/web-access) | +389 | 5929 |
| 169 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +384 | 24466 |
| 170 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +376 | 6966 |
| 171 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +372 | 8487 |
| 172 | [PostHog/posthog](https://github.com/PostHog/posthog) | +370 | 31767 |
| 173 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +366 | 2395 |
| 174 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +354 | 2730 |
| 175 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +348 | 2421 |
| 176 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +339 | 3351 |
| 177 | [soxoj/maigret](https://github.com/soxoj/maigret) | +336 | 22512 |
| 178 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +319 | 26048 |
| 179 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +314 | 2015 |
| 180 | [decolua/9router](https://github.com/decolua/9router) | +299 | 3581 |
| 181 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +295 | 3409 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +289 | 6051 |
| 183 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +288 | 1415 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +283 | 12938 |
| 185 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +275 | 9841 |
| 186 | [floci-io/floci](https://github.com/floci-io/floci) | +274 | 4315 |
| 187 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +261 | 26797 |
| 188 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +256 | 3625 |
| 189 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +255 | 36103 |
| 190 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +241 | 1816 |
| 191 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +239 | 2026 |
| 192 | [88lin/video_vip](https://github.com/88lin/video_vip) | +237 | 1620 |
| 193 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +216 | 1570 |
| 194 | [tiagozip/cap](https://github.com/tiagozip/cap) | +210 | 6230 |
| 195 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +198 | 7447 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +197 | 2966 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +197 | 16093 |
| 198 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +185 | 33712 |
| 199 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +178 | 2930 |
| 200 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +175 | 9209 |
| 201 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +167 | 11462 |
| 202 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +166 | 1277 |
| 203 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +164 | 1118 |
| 204 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 827 |
| 205 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +160 | 4256 |
| 206 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +157 | 8062 |
| 207 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +156 | 2254 |
| 208 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +154 | 1651 |
| 209 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +153 | 4053 |
| 210 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +153 | 582 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +153 | 41086 |
| 212 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +148 | 8839 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +146 | 40265 |
| 214 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +145 | 3214 |
| 215 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +144 | 22562 |
| 216 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +141 | 35473 |
| 217 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +140 | 5878 |
| 218 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +139 | 973 |
| 219 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +134 | 14648 |
| 220 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +129 | 29856 |
| 221 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +125 | 2615 |
| 222 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +123 | 7475 |
| 223 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +122 | 39596 |
| 224 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +122 | 5606 |
| 225 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +121 | 23714 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +120 | 29908 |
| 227 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +118 | 13143 |
| 228 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +118 | 735 |
| 229 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +117 | 763 |
| 230 | [clawplays/ospec](https://github.com/clawplays/ospec) | +116 | 611 |
| 231 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +112 | 1859 |
| 232 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +106 | 713 |
| 233 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 512 |
| 234 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +104 | 1140 |
| 235 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +103 | 790 |
| 236 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +99 | 1722 |
| 237 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +99 | 10994 |
| 238 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +98 | 2040 |
| 239 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +98 | 532 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +94 | 26963 |
| 241 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +94 | 33000 |
| 242 | [browserbase/skills](https://github.com/browserbase/skills) | +93 | 1457 |
| 243 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +93 | 628 |
| 244 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +93 | 1925 |
| 245 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +91 | 48784 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +90 | 13041 |
| 247 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +90 | 470 |
| 248 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +88 | 1516 |
| 249 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +88 | 3456 |
| 250 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +86 | 1168 |
| 251 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +85 | 436 |
| 252 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +85 | 2460 |
| 253 | [openmemind/memind](https://github.com/openmemind/memind) | +85 | 610 |
| 254 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +84 | 499 |
| 255 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +84 | 1234 |
| 256 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +83 | 828 |
| 257 | [cv-cat/DouYin_Spider](https://github.com/cv-cat/DouYin_Spider) | +83 | 1690 |
| 258 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +82 | 749 |
| 259 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +82 | 1599 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +80 | 1977 |
| 261 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1870 |
| 262 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +79 | 45263 |
| 263 | [crimera/piko](https://github.com/crimera/piko) | +79 | 3420 |
| 264 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +77 | 545 |
| 265 | [robinebers/openusage](https://github.com/robinebers/openusage) | +77 | 2210 |
| 266 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +77 | 3135 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +73 | 3954 |
| 268 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +72 | 1037 |
| 269 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +68 | 672 |
| 270 | [microg/GmsCore](https://github.com/microg/GmsCore) | +67 | 13126 |
| 271 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +66 | 2817 |
| 272 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +66 | 1443 |
| 273 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +65 | 658 |
| 274 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +62 | 370 |
| 275 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +62 | 27431 |
| 276 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1741 |
| 277 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +59 | 369 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +59 | 9448 |
| 279 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +58 | 361 |
| 280 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +58 | 28993 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +56 | 7362 |
| 282 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +53 | 11835 |
| 284 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +51 | 4973 |
| 285 | [sandeco/reversa](https://github.com/sandeco/reversa) | +50 | 448 |
| 286 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +50 | 262 |
| 287 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +48 | 1924 |
| 288 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +47 | 31476 |
| 289 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +46 | 1833 |
| 290 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +45 | 265 |
| 291 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1756 |
| 292 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +44 | 5213 |
| 293 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +40 | 619 |
| 294 | [is-a-dev/register](https://github.com/is-a-dev/register) | +36 | 10208 |
| 295 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +36 | 250 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +36 | 8622 |
| 297 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 161 |
| 298 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +34 | 1303 |
| 299 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +33 | 798 |
| 300 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +33 | 2147 |
