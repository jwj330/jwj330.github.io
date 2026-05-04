---
title: "2026-05-04 GitHub增长趋势报告"
description: "1.ruflo+544 2.skills+376 3.vscode-dark-islands+285 4.Scrapling+273 5.Pixelle-Video+241"
date: 2026-05-04T21:10:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-04 21:10:48

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
        'daily': {"categories": ["virattt/dexter", "browser-use/browser-harness", "earthtojake/text-to-cad", "webadderallorg/Recordly", "abhigyanpatwari/GitNexus", "Alishahryar1/free-claude-code", "Lum1104/Understand-Anything", "czlonkowski/n8n-mcp", "docusealco/docuseal", "1jehuang/jcode", "rtk-ai/rtk", "holaboss-ai/holaOS", "warpdotdev/warp", "safishamsi/graphify", "soxoj/maigret", "AIDC-AI/Pixelle-Video", "D4Vinci/Scrapling", "bwya77/vscode-dark-islands", "mattpocock/skills", "ruvnet/ruflo"], "data": [83, 85, 85, 97, 99, 100, 101, 107, 120, 120, 128, 129, 162, 182, 220, 241, 273, 285, 376, 544]},
        'weekly': {"categories": ["1jehuang/jcode", "ComposioHQ/awesome-codex-skills", "Fincept-Corporation/FinceptTerminal", "AIDC-AI/Pixelle-Video", "rtk-ai/rtk", "Z4nzu/hackingtool", "abhigyanpatwari/GitNexus", "openai/symphony", "JuliusBrussee/caveman", "Alishahryar1/free-claude-code", "farion1231/cc-switch", "soxoj/maigret", "D4Vinci/Scrapling", "safishamsi/graphify", "ruvnet/ruflo", "NousResearch/hermes-agent", "TauricResearch/TradingAgents", "forrestchang/andrej-karpathy-skills", "warpdotdev/warp", "mattpocock/skills"], "data": [441, 448, 461, 493, 537, 564, 564, 571, 583, 693, 736, 742, 792, 831, 1163, 1486, 1928, 2305, 2644, 3301]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "shanraisshan/claude-code-best-practice", "msitarzewski/agency-agents", "rtk-ai/rtk", "multica-ai/multica", "garrytan/gstack", "openclaw/openclaw", "thedotmack/claude-mem", "addyosmani/agent-skills", "ultraworkers/claw-code", "mattpocock/skills", "affaan-m/everything-claude-code", "obra/superpowers", "safishamsi/graphify", "santifer/career-ops", "MemPalace/mempalace", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [3186, 3334, 3751, 3775, 3849, 4151, 4191, 4361, 4771, 5524, 6095, 6446, 6934, 6943, 7523, 8102, 8473, 11995, 15340, 18470]}
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
| 1 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +544 | 41130 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +376 | 58836 |
| 3 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +285 | 7477 |
| 4 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +273 | 44127 |
| 5 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +241 | 10813 |
| 6 | [soxoj/maigret](https://github.com/soxoj/maigret) | +220 | 24727 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +182 | 42603 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +162 | 54223 |
| 9 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +129 | 4744 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +128 | 41365 |
| 11 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +120 | 3864 |
| 12 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +120 | 13153 |
| 13 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +107 | 19863 |
| 14 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +101 | 11575 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +100 | 21170 |
| 16 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +99 | 35570 |
| 17 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +97 | 12580 |
| 18 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +85 | 1850 |
| 19 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +85 | 10293 |
| 20 | [virattt/dexter](https://github.com/virattt/dexter) | +83 | 23115 |
| 21 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +78 | 15306 |
| 22 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +76 | 9514 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +72 | 24383 |
| 24 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +71 | 2259 |
| 25 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +71 | 34732 |
| 26 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +69 | 6465 |
| 27 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +69 | 8323 |
| 28 | [browserbase/skills](https://github.com/browserbase/skills) | +68 | 2080 |
| 29 | [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | +68 | 10763 |
| 30 | [withastro/flue](https://github.com/withastro/flue) | +67 | 2350 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3301 | 58836 |
| 2 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2644 | 54223 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2305 | 111345 |
| 4 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1928 | 30590 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1486 | 132570 |
| 6 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1163 | 41130 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +831 | 42603 |
| 8 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +792 | 44127 |
| 9 | [soxoj/maigret](https://github.com/soxoj/maigret) | +742 | 24727 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +736 | 59016 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +693 | 21170 |
| 12 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +583 | 53734 |
| 13 | [openai/symphony](https://github.com/openai/symphony) | +571 | 21259 |
| 14 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +564 | 35570 |
| 15 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +564 | 55070 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +537 | 41365 |
| 17 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +493 | 10813 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +461 | 19702 |
| 19 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +448 | 6465 |
| 20 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +441 | 3864 |
| 21 | [withastro/flue](https://github.com/withastro/flue) | +391 | 2350 |
| 22 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +369 | 10293 |
| 23 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +367 | 27752 |
| 24 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +364 | 46501 |
| 25 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +348 | 44525 |
| 26 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +322 | 11575 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +319 | 24383 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +312 | 11242 |
| 29 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +304 | 9514 |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +297 | 50942 |
| 31 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +296 | 12580 |
| 32 | [bwya77/vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands) | +287 | 7477 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +286 | 14361 |
| 34 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +283 | 24893 |
| 35 | [santifer/career-ops](https://github.com/santifer/career-ops) | +276 | 42444 |
| 36 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +262 | 3604 |
| 37 | [virattt/dexter](https://github.com/virattt/dexter) | +253 | 23116 |
| 38 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +240 | 15306 |
| 39 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +239 | 12549 |
| 40 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +239 | 11289 |
| 41 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +238 | 4744 |
| 42 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +238 | 15271 |
| 43 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +235 | 3418 |
| 44 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +233 | 4942 |
| 45 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +229 | 34732 |
| 46 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +229 | 28645 |
| 47 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +221 | 3600 |
| 48 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +221 | 13554 |
| 49 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +214 | 17327 |
| 50 | [browserbase/skills](https://github.com/browserbase/skills) | +213 | 2080 |
| 51 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +210 | 33962 |
| 52 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +207 | 4630 |
| 53 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +207 | 7965 |
| 54 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +200 | 45182 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +194 | 17635 |
| 56 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +188 | 5746 |
| 57 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +184 | 17208 |
| 58 | [docusealco/docuseal](https://github.com/docusealco/docuseal) | +183 | 13153 |
| 59 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +181 | 9080 |
| 60 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +181 | 31090 |
| 61 | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | +176 | 19863 |
| 62 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +173 | 3370 |
| 63 | [ShareX/ShareX](https://github.com/ShareX/ShareX) | +169 | 35707 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +160 | 26535 |
| 65 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +159 | 30555 |
| 66 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +158 | 42497 |
| 67 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +154 | 23230 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +153 | 17157 |
| 69 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +152 | 2834 |
| 70 | [giancarloerra/SocratiCode](https://github.com/giancarloerra/SocratiCode) | +151 | 2259 |
| 71 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +148 | 4896 |
| 72 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +145 | 2770 |
| 73 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +144 | 21217 |
| 74 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +143 | 18684 |
| 75 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +142 | 13093 |
| 76 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +141 | 22732 |
| 77 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +138 | 20201 |
| 78 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +136 | 8323 |
| 79 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +136 | 25803 |
| 80 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +135 | 30567 |
| 81 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +133 | 58059 |
| 82 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +133 | 27435 |
| 83 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +132 | 23707 |
| 84 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +130 | 5314 |
| 85 | [caamer20/Telegram-Drive](https://github.com/caamer20/Telegram-Drive) | +130 | 2201 |
| 86 | [evoiz/Agentic-Design-Patterns](https://github.com/evoiz/Agentic-Design-Patterns) | +129 | 1400 |
| 87 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +129 | 12100 |
| 88 | [sentrux/sentrux](https://github.com/sentrux/sentrux) | +126 | 2101 |
| 89 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +125 | 9716 |
| 90 | [therealaleph/MasterHttpRelayVPN-RUST](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | +122 | 1674 |
| 91 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +122 | 11668 |
| 92 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +120 | 26707 |
| 93 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +118 | 31683 |
| 94 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +117 | 5634 |
| 95 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +115 | 4053 |
| 96 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +114 | 36313 |
| 97 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +114 | 1912 |
| 98 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +113 | 3217 |
| 99 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +113 | 17179 |
| 100 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +112 | 7950 |
| 101 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +111 | 1850 |
| 102 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +111 | 5729 |
| 103 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +107 | 25531 |
| 104 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +107 | 3604 |
| 105 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +105 | 2461 |
| 106 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +103 | 12913 |
| 107 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +101 | 3254 |
| 108 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +100 | 42488 |
| 109 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +99 | 6345 |
| 110 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +99 | 1658 |
| 111 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +96 | 2320 |
| 112 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +95 | 4169 |
| 113 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +95 | 20349 |
| 114 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +94 | 4429 |
| 115 | [MAC-AutoML/MindPipe](https://github.com/MAC-AutoML/MindPipe) | +94 | 679 |
| 116 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +92 | 1338 |
| 117 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +89 | 1259 |
| 118 | [siddsachar/Thoth](https://github.com/siddsachar/Thoth) | +87 | 890 |
| 119 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +87 | 639 |
| 120 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +87 | 2506 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18470 | 132572 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +15340 | 111347 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +11995 | 70913 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8473 | 53734 |
| 5 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +8102 | 51105 |
| 6 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7523 | 42445 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6943 | 42603 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +6934 | 60312 |
| 9 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +6446 | 51199 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6095 | 58836 |
| 11 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +5524 | 190015 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4771 | 27752 |
| 13 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4361 | 30678 |
| 14 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4191 | 224760 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4151 | 89118 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3849 | 24383 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3775 | 41365 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3751 | 92498 |
| 19 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3334 | 50942 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3186 | 34732 |
| 21 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3130 | 30590 |
| 22 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3027 | 59016 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2917 | 109881 |
| 24 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2891 | 21171 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2875 | 74774 |
| 26 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2837 | 17208 |
| 27 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2706 | 62307 |
| 28 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +2688 | 54224 |
| 29 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2646 | 19702 |
| 30 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +2559 | 25803 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2532 | 34148 |
| 32 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2412 | 27435 |
| 33 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2406 | 35570 |
| 34 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2384 | 78873 |
| 35 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2374 | 14361 |
| 36 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2372 | 13093 |
| 37 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2287 | 31090 |
| 38 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2265 | 23230 |
| 39 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2194 | 19163 |
| 40 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2117 | 69674 |
| 41 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2088 | 44525 |
| 42 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2067 | 55070 |
| 43 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +2053 | 17327 |
| 44 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2012 | 22732 |
| 45 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1959 | 85286 |
| 46 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1955 | 59912 |
| 47 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +1948 | 11870 |
| 48 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1927 | 17256 |
| 49 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1926 | 41130 |
| 50 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1867 | 15271 |
| 51 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1854 | 59115 |
| 52 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +1728 | 58059 |
| 53 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1686 | 31098 |
| 54 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +1645 | 46501 |
| 55 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1619 | 32505 |
| 56 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1618 | 10293 |
| 57 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1601 | 11668 |
| 58 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1595 | 28645 |
| 59 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1584 | 44127 |
| 60 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1571 | 25930 |
| 61 | [chenglou/pretext](https://github.com/chenglou/pretext) | +1539 | 46175 |
| 62 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1513 | 20153 |
| 63 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1505 | 24486 |
| 64 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1471 | 9514 |
| 65 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1444 | 6846 |
| 66 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1409 | 33878 |
| 67 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1392 | 17179 |
| 68 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1368 | 45886 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1354 | 42497 |
| 70 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1354 | 24893 |
| 71 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1345 | 98536 |
| 72 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1338 | 64833 |
| 73 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1326 | 11289 |
| 74 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1312 | 30567 |
| 75 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1308 | 12580 |
| 76 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1305 | 15306 |
| 77 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1281 | 22596 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1225 | 26535 |
| 79 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1225 | 95754 |
| 80 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1216 | 7965 |
| 81 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1210 | 17635 |
| 82 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1205 | 9080 |
| 83 | [github/spec-kit](https://github.com/github/spec-kit) | +1201 | 71722 |
| 84 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1184 | 24716 |
| 85 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1179 | 11242 |
| 86 | [openai/codex](https://github.com/openai/codex) | +1175 | 61744 |
| 87 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1137 | 53428 |
| 88 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1137 | 37330 |
| 89 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1136 | 45182 |
| 90 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1131 | 28923 |
| 91 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1130 | 13899 |
| 92 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +1065 | 18684 |
| 93 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1008 | 17366 |
| 94 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1003 | 36313 |
| 95 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +989 | 10813 |
| 96 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +989 | 78902 |
| 97 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +974 | 33421 |
| 98 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +972 | 42488 |
| 99 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +964 | 5419 |
| 100 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +960 | 51662 |
| 101 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +951 | 5729 |
| 102 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +951 | 20201 |
| 103 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +941 | 33962 |
| 104 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +929 | 25863 |
| 105 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +920 | 30555 |
| 106 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +905 | 12549 |
| 107 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +903 | 4942 |
| 108 | [google-research/timesfm](https://github.com/google-research/timesfm) | +889 | 19367 |
| 109 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +883 | 7213 |
| 110 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +870 | 47122 |
| 111 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +860 | 5634 |
| 112 | [google/magika](https://github.com/google/magika) | +838 | 16899 |
| 113 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +826 | 21672 |
| 114 | [soxoj/maigret](https://github.com/soxoj/maigret) | +812 | 24727 |
| 115 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +763 | 6345 |
| 116 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +761 | 13705 |
| 117 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +749 | 6465 |
| 118 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +743 | 4133 |
| 119 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +734 | 9749 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +721 | 12100 |
| 121 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +717 | 52700 |
| 122 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +672 | 18738 |
| 123 | [jundot/omlx](https://github.com/jundot/omlx) | +647 | 12286 |
| 124 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +633 | 4643 |
| 125 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +625 | 12497 |
| 126 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +618 | 4169 |
| 127 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +611 | 19615 |
| 128 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +609 | 41626 |
| 129 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +597 | 11558 |
| 130 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +596 | 22236 |
| 131 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +574 | 4429 |
| 132 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +574 | 3681 |
| 133 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +562 | 4447 |
| 134 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +560 | 39841 |
| 135 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +558 | 12913 |
| 136 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +545 | 32098 |
| 137 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +542 | 11958 |
| 138 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +541 | 3416 |
| 139 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +537 | 2715 |
| 140 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +527 | 36799 |
| 141 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +509 | 3001 |
| 142 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +508 | 4053 |
| 143 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +501 | 4996 |
| 144 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +490 | 17860 |
| 145 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +490 | 2881 |
| 146 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +475 | 34735 |
| 147 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +469 | 20079 |
| 148 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +461 | 31183 |
| 149 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +459 | 4235 |
| 150 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +436 | 37564 |
| 151 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +430 | 5067 |
| 152 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +429 | 36907 |
| 153 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +426 | 18536 |
| 154 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +425 | 23427 |
| 155 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +409 | 8024 |
| 156 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +409 | 7543 |
| 157 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +408 | 26707 |
| 158 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +405 | 20349 |
| 159 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +403 | 31315 |
| 160 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +402 | 3217 |
| 161 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +401 | 4106 |
| 162 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +389 | 24605 |
| 163 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +374 | 2449 |
| 164 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +371 | 4413 |
| 165 | [PostHog/posthog](https://github.com/PostHog/posthog) | +370 | 31767 |
| 166 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +366 | 8600 |
| 167 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +362 | 25531 |
| 168 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +358 | 6997 |
| 169 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +357 | 2506 |
| 170 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +351 | 3443 |
| 171 | [eze-is/web-access](https://github.com/eze-is/web-access) | +348 | 5984 |
| 172 | [openai/skills](https://github.com/openai/skills) | +338 | 18231 |
| 173 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +334 | 2087 |
| 174 | [decolua/9router](https://github.com/decolua/9router) | +321 | 3733 |
| 175 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +308 | 1537 |
| 176 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +308 | 26103 |
| 177 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +303 | 2598 |
| 178 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +296 | 3604 |
| 179 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +283 | 3055 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +280 | 26923 |
| 181 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +277 | 1656 |
| 182 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +275 | 2320 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +275 | 13036 |
| 184 | [floci-io/floci](https://github.com/floci-io/floci) | +267 | 4344 |
| 185 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +264 | 9895 |
| 186 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +256 | 1912 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +252 | 36103 |
| 188 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +247 | 1850 |
| 189 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +243 | 1682 |
| 190 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +238 | 6128 |
| 191 | [88lin/video_vip](https://github.com/88lin/video_vip) | +236 | 1636 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +233 | 3680 |
| 193 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +228 | 2084 |
| 194 | [browserbase/skills](https://github.com/browserbase/skills) | +220 | 2080 |
| 195 | [tiagozip/cap](https://github.com/tiagozip/cap) | +212 | 6251 |
| 196 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +202 | 16199 |
| 197 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +201 | 2770 |
| 198 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +197 | 3055 |
| 199 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +191 | 3430 |
| 200 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +190 | 33712 |
| 201 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +189 | 7471 |
| 202 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +173 | 1156 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +173 | 9359 |
| 204 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +168 | 2973 |
| 205 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +154 | 1017 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +153 | 22619 |
| 207 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +151 | 8094 |
| 208 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +150 | 1685 |
| 209 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +148 | 11491 |
| 210 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +148 | 40265 |
| 211 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +142 | 4262 |
| 212 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +141 | 14711 |
| 213 | [usebruno/bruno](https://github.com/usebruno/bruno) | +141 | 41086 |
| 214 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +138 | 35473 |
| 215 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +136 | 724 |
| 216 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +126 | 813 |
| 217 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +126 | 7496 |
| 218 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +125 | 39596 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +123 | 1040 |
| 220 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +117 | 5628 |
| 221 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +117 | 29895 |
| 222 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +117 | 5878 |
| 223 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +117 | 23747 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29942 |
| 225 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +115 | 2632 |
| 226 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +115 | 583 |
| 227 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +115 | 8858 |
| 228 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +108 | 13157 |
| 229 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +108 | 1877 |
| 230 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +107 | 719 |
| 231 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +106 | 1152 |
| 232 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +105 | 797 |
| 233 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 517 |
| 234 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +100 | 4066 |
| 235 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +99 | 573 |
| 236 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +98 | 545 |
| 237 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +97 | 2048 |
| 238 | [clawplays/ospec](https://github.com/clawplays/ospec) | +95 | 612 |
| 239 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +95 | 652 |
| 240 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +93 | 26985 |
| 241 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +92 | 2493 |
| 242 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +91 | 475 |
| 243 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +90 | 1539 |
| 244 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +90 | 1940 |
| 245 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +89 | 11016 |
| 246 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +87 | 441 |
| 247 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +87 | 48784 |
| 248 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +86 | 3508 |
| 249 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +86 | 33000 |
| 250 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +85 | 13066 |
| 251 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +84 | 763 |
| 252 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +84 | 1253 |
| 253 | [robinebers/openusage](https://github.com/robinebers/openusage) | +82 | 2240 |
| 254 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +81 | 1607 |
| 255 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +81 | 570 |
| 256 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +81 | 1898 |
| 257 | [openmemind/memind](https://github.com/openmemind/memind) | +81 | 632 |
| 258 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +80 | 859 |
| 259 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +80 | 1250 |
| 260 | [crimera/piko](https://github.com/crimera/piko) | +78 | 3439 |
| 261 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +77 | 1730 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +76 | 1990 |
| 263 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +75 | 764 |
| 264 | [sandeco/reversa](https://github.com/sandeco/reversa) | +74 | 565 |
| 265 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +72 | 1064 |
| 266 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +71 | 3964 |
| 267 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +70 | 45263 |
| 268 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +68 | 688 |
| 269 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +64 | 27456 |
| 270 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +63 | 29034 |
| 271 | [microg/GmsCore](https://github.com/microg/GmsCore) | +63 | 13144 |
| 272 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +62 | 380 |
| 273 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +62 | 2829 |
| 274 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +61 | 393 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +61 | 1758 |
| 276 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +61 | 1479 |
| 277 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +60 | 370 |
| 278 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +54 | 3838 |
| 279 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +53 | 9461 |
| 281 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +51 | 272 |
| 282 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +51 | 11853 |
| 283 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +50 | 7380 |
| 284 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +49 | 4999 |
| 285 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +48 | 1933 |
| 286 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +47 | 31476 |
| 287 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +45 | 265 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +42 | 1842 |
| 289 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +42 | 664 |
| 290 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +42 | 5215 |
| 291 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +41 | 265 |
| 292 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +40 | 1330 |
| 293 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +40 | 627 |
| 294 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +37 | 2281 |
| 295 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +34 | 162 |
| 296 | [NotHarshhaa/DevOps-Projects](https://github.com/NotHarshhaa/DevOps-Projects) | +34 | 4023 |
| 297 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +32 | 811 |
| 298 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +32 | 2148 |
| 299 | [is-a-dev/register](https://github.com/is-a-dev/register) | +31 | 10217 |
| 300 | [wechatpay-apiv3/wechatpay-skills](https://github.com/wechatpay-apiv3/wechatpay-skills) | +31 | 222 |
