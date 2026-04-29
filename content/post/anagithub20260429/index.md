---
title: "2026-04-29 GitHub增长趋势报告"
description: "1.warp+1153 2.skills+608 3.symphony+143 4.VibeVoice+119 5.free-claude-code+105"
date: 2026-04-29T21:08:30+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-29 21:08:30

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
        'daily': {"categories": ["davila7/claude-code-templates", "badlogic/pi-mono", "refactoringhq/tolaria", "everywall/ladder", "fluffypony/dothething", "rtk-ai/rtk", "safishamsi/graphify", "fspecii/ace-step-ui", "KKKKhazix/khazix-skills", "abhigyanpatwari/GitNexus", "addyosmani/agent-skills", "Fincept-Corporation/FinceptTerminal", "JuliusBrussee/caveman", "ComposioHQ/awesome-codex-skills", "iamgio/quarkdown", "Alishahryar1/free-claude-code", "microsoft/VibeVoice", "openai/symphony", "mattpocock/skills", "warpdotdev/warp"], "data": [45, 46, 48, 50, 52, 59, 63, 65, 71, 72, 73, 76, 76, 84, 95, 105, 119, 143, 608, 1153]},
        'weekly': {"categories": ["Anil-matcha/Open-Generative-AI", "badlogic/pi-mono", "microsoft/VibeVoice", "op7418/guizang-ppt-skill", "abhigyanpatwari/GitNexus", "safishamsi/graphify", "VoltAgent/awesome-design-md", "Fincept-Corporation/FinceptTerminal", "addyosmani/agent-skills", "farion1231/cc-switch", "JuliusBrussee/caveman", "rtk-ai/rtk", "garrytan/gstack", "warpdotdev/warp", "refactoringhq/tolaria", "Z4nzu/hackingtool", "NousResearch/hermes-agent", "Alishahryar1/free-claude-code", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [569, 577, 577, 637, 641, 683, 688, 724, 738, 790, 796, 844, 855, 1168, 1266, 1429, 1966, 2357, 3058, 3524]},
        'monthly': {"categories": ["mattpocock/skills", "Yeachan-Heo/oh-my-codex", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "addyosmani/agent-skills", "Gitlawb/openclaude", "openclaw/openclaw", "garrytan/gstack", "anthropics/claude-code", "chenglou/pretext", "safishamsi/graphify", "santifer/career-ops", "MemPalace/mempalace", "obra/superpowers", "JuliusBrussee/caveman", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4102, 4210, 4494, 4593, 4594, 4762, 5051, 5066, 5144, 5936, 6253, 7308, 7977, 8027, 8048, 8792, 12547, 13545, 18515, 25494]}
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
| 1 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1153 | 43007 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +608 | 43642 |
| 3 | [openai/symphony](https://github.com/openai/symphony) | +143 | 19027 |
| 4 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +119 | 45597 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +105 | 18482 |
| 6 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +95 | 12599 |
| 7 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +84 | 4714 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +76 | 50341 |
| 9 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +76 | 17759 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +73 | 26056 |
| 11 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +72 | 33276 |
| 12 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +71 | 7082 |
| 13 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +65 | 2104 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +63 | 38171 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +59 | 38377 |
| 16 | [fluffypony/dothething](https://github.com/fluffypony/dothething) | +52 | 751 |
| 17 | [everywall/ladder](https://github.com/everywall/ladder) | +50 | 7257 |
| 18 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +48 | 8254 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +46 | 42715 |
| 20 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +45 | 26403 |
| 21 | [caamer20/Telegram-Drive](https://github.com/caamer20/Telegram-Drive) | +43 | 1655 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +42 | 49456 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +41 | 23354 |
| 24 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | +40 | 5297 |
| 25 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +38 | 2674 |
| 26 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +38 | 27460 |
| 27 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +37 | 4949 |
| 28 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +36 | 12964 |
| 29 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +36 | 8426 |
| 30 | [agno-agi/scout](https://github.com/agno-agi/scout) | +34 | 400 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3524 | 99363 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3058 | 43643 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2357 | 18482 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1966 | 124851 |
| 5 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1429 | 55070 |
| 6 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1266 | 8254 |
| 7 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1168 | 43007 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +855 | 86732 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +844 | 38377 |
| 10 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +796 | 50341 |
| 11 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +790 | 55555 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +738 | 26056 |
| 13 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +724 | 17759 |
| 14 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +688 | 68090 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +683 | 38171 |
| 16 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +641 | 33276 |
| 17 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +637 | 4156 |
| 18 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +577 | 45597 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +577 | 42715 |
| 20 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +569 | 10118 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +532 | 12964 |
| 22 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +521 | 3777 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +465 | 22839 |
| 24 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +453 | 8426 |
| 25 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +442 | 10258 |
| 26 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +440 | 4714 |
| 27 | [santifer/career-ops](https://github.com/santifer/career-ops) | +372 | 40955 |
| 28 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +362 | 4745 |
| 29 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +355 | 25616 |
| 30 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +343 | 25800 |
| 31 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +317 | 8210 |
| 32 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +310 | 4949 |
| 33 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +309 | 16726 |
| 34 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +309 | 16277 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +308 | 9499 |
| 36 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +300 | 41764 |
| 37 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +294 | 11183 |
| 38 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +293 | 7770 |
| 39 | [openai/symphony](https://github.com/openai/symphony) | +289 | 19027 |
| 40 | [PostHog/posthog](https://github.com/PostHog/posthog) | +288 | 31767 |
| 41 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +280 | 19393 |
| 42 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +278 | 49456 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +278 | 12298 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +277 | 22563 |
| 45 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +269 | 30294 |
| 46 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +264 | 13981 |
| 47 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +257 | 2103 |
| 48 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +257 | 13717 |
| 49 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +250 | 21988 |
| 50 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +250 | 19382 |
| 51 | [victorchen96/deepseek_v4_rolepaly_instruct](https://github.com/victorchen96/deepseek_v4_rolepaly_instruct) | +248 | 1520 |
| 52 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +245 | 26842 |
| 53 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +236 | 32836 |
| 54 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +235 | 57425 |
| 55 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +233 | 24036 |
| 56 | [trycua/cua](https://github.com/trycua/cua) | +232 | 15218 |
| 57 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +230 | 32666 |
| 58 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +227 | 29779 |
| 59 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +226 | 50357 |
| 60 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +220 | 25039 |
| 61 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +219 | 26403 |
| 62 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +219 | 4963 |
| 63 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +218 | 23354 |
| 64 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +218 | 53027 |
| 65 | [gastownhall/beads](https://github.com/gastownhall/beads) | +216 | 22632 |
| 66 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +214 | 3685 |
| 67 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +211 | 29789 |
| 68 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +206 | 27460 |
| 69 | [tw93/Kami](https://github.com/tw93/Kami) | +205 | 3803 |
| 70 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +204 | 33637 |
| 71 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +203 | 3947 |
| 72 | [penpot/penpot](https://github.com/penpot/penpot) | +202 | 44370 |
| 73 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +198 | 40796 |
| 74 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +196 | 41851 |
| 75 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +195 | 7269 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +194 | 44007 |
| 77 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +192 | 9102 |
| 78 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +187 | 16646 |
| 79 | [tiagozip/cap](https://github.com/tiagozip/cap) | +187 | 6158 |
| 80 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +185 | 14056 |
| 81 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +183 | 1447 |
| 82 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +183 | 12599 |
| 83 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +183 | 20343 |
| 84 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +181 | 8293 |
| 85 | [blader/humanizer](https://github.com/blader/humanizer) | +180 | 16468 |
| 86 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +179 | 4607 |
| 87 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +178 | 2674 |
| 88 | [jackwener/opencli](https://github.com/jackwener/opencli) | +177 | 18204 |
| 89 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +176 | 18712 |
| 90 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +175 | 1210 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +171 | 35713 |
| 92 | [leigest519/OpenGame](https://github.com/leigest519/OpenGame) | +170 | 1611 |
| 93 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +169 | 31941 |
| 94 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +168 | 25562 |
| 95 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +165 | 1723 |
| 96 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +163 | 34011 |
| 97 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +161 | 1596 |
| 98 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +159 | 5187 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +158 | 1170 |
| 100 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +157 | 3757 |
| 101 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +153 | 11383 |
| 102 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +150 | 39288 |
| 103 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +147 | 1025 |
| 104 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +144 | 891 |
| 105 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +141 | 7082 |
| 106 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +141 | 5753 |
| 107 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +135 | 30812 |
| 108 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +132 | 2656 |
| 109 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +132 | 24328 |
| 110 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +131 | 1344 |
| 111 | [deepseek-ai/TileKernels](https://github.com/deepseek-ai/TileKernels) | +130 | 1347 |
| 112 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +126 | 36799 |
| 113 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +125 | 12265 |
| 114 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +125 | 13184 |
| 115 | [wxyhgk/retain-pdf](https://github.com/wxyhgk/retain-pdf) | +123 | 1201 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +116 | 33017 |
| 117 | [jundot/omlx](https://github.com/jundot/omlx) | +116 | 11847 |
| 118 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +115 | 41295 |
| 119 | [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image) | +115 | 922 |
| 120 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | +115 | 1932 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25494 | 189228 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18515 | 124851 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +13545 | 99363 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12547 | 68090 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8792 | 51199 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8048 | 50341 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +8027 | 60312 |
| 8 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7977 | 50357 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7308 | 40955 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6253 | 38171 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +5936 | 45745 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5144 | 69674 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5066 | 86732 |
| 14 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5051 | 224760 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4762 | 25039 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4594 | 26056 |
| 17 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4593 | 33637 |
| 18 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4494 | 30678 |
| 19 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4210 | 26842 |
| 20 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4102 | 43644 |
| 21 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4031 | 49456 |
| 22 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4030 | 88826 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3964 | 30294 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3797 | 22839 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3718 | 38377 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3658 | 60610 |
| 27 | [anthropics/skills](https://github.com/anthropics/skills) | +3348 | 74774 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3246 | 109881 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3067 | 55555 |
| 30 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3012 | 77857 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2924 | 34148 |
| 32 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2912 | 45597 |
| 33 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2829 | 17253 |
| 34 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2770 | 16971 |
| 35 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2715 | 16277 |
| 36 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2679 | 31941 |
| 37 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2545 | 16731 |
| 38 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2522 | 18482 |
| 39 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2421 | 57425 |
| 40 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2374 | 11578 |
| 41 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2336 | 17759 |
| 42 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2304 | 58272 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2275 | 12298 |
| 44 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2270 | 58733 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2195 | 42715 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2190 | 12964 |
| 47 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2173 | 85286 |
| 48 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2162 | 33276 |
| 49 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2155 | 22564 |
| 50 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2153 | 18712 |
| 51 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2066 | 64251 |
| 52 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1941 | 31098 |
| 53 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1908 | 21988 |
| 54 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1899 | 55070 |
| 55 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1854 | 16217 |
| 56 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1851 | 33878 |
| 57 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1843 | 10152 |
| 58 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1815 | 28732 |
| 59 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1797 | 30590 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1788 | 14056 |
| 61 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1679 | 24328 |
| 62 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1657 | 18204 |
| 63 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1639 | 27460 |
| 64 | [openai/codex](https://github.com/openai/codex) | +1572 | 61744 |
| 65 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1562 | 25800 |
| 66 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1562 | 19724 |
| 67 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1509 | 13239 |
| 68 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1485 | 18843 |
| 69 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1484 | 73135 |
| 70 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1478 | 24036 |
| 71 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1468 | 29779 |
| 72 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1467 | 41764 |
| 73 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1445 | 9090 |
| 74 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1430 | 16646 |
| 75 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1426 | 11762 |
| 76 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1425 | 6724 |
| 77 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1420 | 98536 |
| 78 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1410 | 33017 |
| 79 | [github/spec-kit](https://github.com/github/spec-kit) | +1385 | 71722 |
| 80 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1355 | 45886 |
| 81 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1339 | 22279 |
| 82 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1334 | 79656 |
| 83 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1333 | 37330 |
| 84 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1324 | 6688 |
| 85 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1313 | 23355 |
| 86 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1311 | 8426 |
| 87 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1308 | 95754 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1303 | 25616 |
| 89 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1290 | 53027 |
| 90 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1275 | 10846 |
| 91 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1272 | 44007 |
| 92 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1268 | 8254 |
| 93 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1242 | 41851 |
| 94 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1238 | 35713 |
| 95 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1237 | 16726 |
| 96 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1223 | 43008 |
| 97 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1223 | 13981 |
| 98 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1139 | 10118 |
| 99 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1089 | 7082 |
| 100 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1079 | 8210 |
| 101 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1043 | 21204 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1034 | 78902 |
| 103 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1024 | 18497 |
| 104 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1006 | 9499 |
| 105 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +952 | 32666 |
| 106 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +935 | 39288 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +903 | 13184 |
| 108 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +902 | 25562 |
| 109 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +899 | 4855 |
| 110 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +876 | 5187 |
| 111 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +876 | 7100 |
| 112 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +868 | 47122 |
| 113 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +848 | 6629 |
| 114 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +846 | 4906 |
| 115 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +838 | 52700 |
| 116 | [google/magika](https://github.com/google/magika) | +834 | 16829 |
| 117 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +834 | 4470 |
| 118 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +792 | 4963 |
| 119 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +773 | 5753 |
| 120 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +762 | 11961 |
| 121 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +750 | 5636 |
| 122 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +739 | 4083 |
| 123 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +735 | 9707 |
| 124 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +734 | 11383 |
| 125 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +710 | 3685 |
| 126 | [jundot/omlx](https://github.com/jundot/omlx) | +710 | 11847 |
| 127 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +708 | 22006 |
| 128 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +704 | 41295 |
| 129 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +693 | 12137 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +678 | 39841 |
| 131 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +671 | 4259 |
| 132 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +666 | 19382 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +657 | 54903 |
| 134 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +623 | 31657 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +621 | 34560 |
| 136 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +609 | 5919 |
| 137 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +596 | 11546 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +595 | 36799 |
| 139 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +578 | 30279 |
| 140 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +563 | 3585 |
| 141 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +558 | 23255 |
| 142 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +554 | 3270 |
| 143 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +548 | 7770 |
| 144 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +539 | 2646 |
| 145 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +536 | 3947 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +529 | 19738 |
| 147 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +528 | 17544 |
| 148 | [eze-is/web-access](https://github.com/eze-is/web-access) | +521 | 5852 |
| 149 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +519 | 37564 |
| 150 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +516 | 18213 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +507 | 30812 |
| 152 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +503 | 25124 |
| 153 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +502 | 12265 |
| 154 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +500 | 25976 |
| 155 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +497 | 2903 |
| 156 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +494 | 7785 |
| 157 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +486 | 4714 |
| 158 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +476 | 30983 |
| 159 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +473 | 4976 |
| 160 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +460 | 2445 |
| 161 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +457 | 2692 |
| 162 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +451 | 3466 |
| 163 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +451 | 2700 |
| 164 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +436 | 3757 |
| 165 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +423 | 26403 |
| 166 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +423 | 11816 |
| 167 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +421 | 7269 |
| 168 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +416 | 3981 |
| 169 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +413 | 36907 |
| 170 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +402 | 6904 |
| 171 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +399 | 3021 |
| 172 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +398 | 2569 |
| 173 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +395 | 24318 |
| 174 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +394 | 19915 |
| 175 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +392 | 8293 |
| 176 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +391 | 16110 |
| 177 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +389 | 9701 |
| 178 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +367 | 2351 |
| 179 | [PostHog/posthog](https://github.com/PostHog/posthog) | +365 | 31767 |
| 180 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +336 | 25928 |
| 181 | [floci-io/floci](https://github.com/floci-io/floci) | +324 | 4273 |
| 182 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +320 | 3365 |
| 183 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +311 | 5923 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +310 | 12742 |
| 185 | [decolua/9router](https://github.com/decolua/9router) | +301 | 3364 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +297 | 3576 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +272 | 36103 |
| 188 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +264 | 9141 |
| 189 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +261 | 26631 |
| 190 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +250 | 1967 |
| 191 | [88lin/video_vip](https://github.com/88lin/video_vip) | +231 | 1572 |
| 192 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +209 | 7413 |
| 193 | [tiagozip/cap](https://github.com/tiagozip/cap) | +207 | 6158 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +200 | 15951 |
| 195 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +196 | 11405 |
| 196 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +194 | 2834 |
| 197 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +193 | 2838 |
| 198 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +191 | 33712 |
| 199 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +179 | 4248 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +176 | 5580 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +170 | 8817 |
| 202 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +169 | 8022 |
| 203 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +168 | 3180 |
| 204 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +165 | 4023 |
| 205 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +163 | 576 |
| 206 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 823 |
| 207 | [usebruno/bruno](https://github.com/usebruno/bruno) | +162 | 41086 |
| 208 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +161 | 1074 |
| 209 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +160 | 2597 |
| 210 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +159 | 1170 |
| 211 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +153 | 13108 |
| 212 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +150 | 22491 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +148 | 40265 |
| 214 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +147 | 1569 |
| 215 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +145 | 35473 |
| 216 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +141 | 3327 |
| 217 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +135 | 23661 |
| 218 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +133 | 897 |
| 219 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +132 | 2104 |
| 220 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +130 | 14535 |
| 221 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +129 | 29815 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +128 | 1827 |
| 223 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +124 | 1698 |
| 224 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +124 | 721 |
| 225 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +121 | 5548 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +121 | 29841 |
| 227 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 611 |
| 228 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +118 | 7420 |
| 229 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +118 | 39596 |
| 230 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +116 | 663 |
| 231 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +115 | 2846 |
| 232 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +114 | 19266 |
| 233 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +109 | 6819 |
| 234 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 501 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +105 | 26934 |
| 236 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +105 | 761 |
| 237 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +104 | 1088 |
| 238 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +103 | 682 |
| 239 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +103 | 10949 |
| 240 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +102 | 2030 |
| 241 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +101 | 773 |
| 242 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +101 | 33000 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +100 | 12995 |
| 244 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +98 | 648 |
| 245 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +94 | 1486 |
| 246 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +94 | 1897 |
| 247 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +93 | 513 |
| 248 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +92 | 1136 |
| 249 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +90 | 1878 |
| 250 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +90 | 597 |
| 251 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +90 | 48784 |
| 252 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +89 | 1218 |
| 253 | [crimera/piko](https://github.com/crimera/piko) | +89 | 3386 |
| 254 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 466 |
| 255 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +88 | 2408 |
| 256 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +87 | 1949 |
| 257 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +86 | 3131 |
| 258 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | +86 | 1295 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +86 | 579 |
| 260 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +85 | 782 |
| 261 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +83 | 432 |
| 262 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +83 | 1817 |
| 263 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +82 | 481 |
| 264 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +82 | 3923 |
| 265 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +81 | 1571 |
| 266 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +80 | 720 |
| 267 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +80 | 648 |
| 268 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +80 | 1423 |
| 269 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +79 | 648 |
| 270 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +77 | 2796 |
| 271 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 272 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +74 | 636 |
| 273 | [robinebers/openusage](https://github.com/robinebers/openusage) | +74 | 2090 |
| 274 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +74 | 3720 |
| 275 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +73 | 4105 |
| 276 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +72 | 1001 |
| 277 | [microg/GmsCore](https://github.com/microg/GmsCore) | +72 | 13094 |
| 278 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +69 | 27408 |
| 279 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +65 | 382 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +64 | 9435 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +60 | 7343 |
| 282 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1719 |
| 283 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +57 | 28985 |
| 284 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +56 | 341 |
| 285 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +56 | 11812 |
| 286 | [halo-dev/halo](https://github.com/halo-dev/halo) | +56 | 37991 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 288 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +55 | 4949 |
| 289 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 290 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +53 | 1905 |
| 291 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +51 | 333 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1817 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +49 | 31476 |
| 294 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +48 | 247 |
| 295 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1742 |
| 296 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +42 | 601 |
| 297 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +41 | 5202 |
| 298 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +40 | 8610 |
| 299 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +34 | 10196 |
