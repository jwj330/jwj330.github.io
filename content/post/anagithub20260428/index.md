---
title: "2026-04-28 GitHub增长趋势报告"
description: "1.skills+564 2.free-claude-code+181 3.symphony+134 4.GitNexus+130 5.VibeVoice+119"
date: 2026-04-28T21:09:05+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-28 21:09:05

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
        'daily': {"categories": ["PurpleAILAB/Decepticon", "luongnv89/claude-howto", "gastownhall/beads", "multica-ai/multica", "nashsu/llm_wiki", "refactoringhq/tolaria", "basketikun/chatgpt2api", "heygen-com/hyperframes", "badlogic/pi-mono", "rtk-ai/rtk", "addyosmani/agent-skills", "Fincept-Corporation/FinceptTerminal", "safishamsi/graphify", "JuliusBrussee/caveman", "ComposioHQ/awesome-codex-skills", "microsoft/VibeVoice", "abhigyanpatwari/GitNexus", "openai/symphony", "Alishahryar1/free-claude-code", "mattpocock/skills"], "data": [41, 42, 49, 49, 52, 58, 61, 62, 65, 76, 78, 80, 85, 87, 95, 119, 130, 134, 181, 564]},
        'weekly': {"categories": ["heygen-com/hyperframes", "elder-plinius/CL4R1T4S", "badlogic/pi-mono", "abhigyanpatwari/GitNexus", "Anil-matcha/Open-Generative-AI", "op7418/guizang-ppt-skill", "VoltAgent/awesome-design-md", "farion1231/cc-switch", "safishamsi/graphify", "Fincept-Corporation/FinceptTerminal", "rtk-ai/rtk", "JuliusBrussee/caveman", "addyosmani/agent-skills", "garrytan/gstack", "refactoringhq/tolaria", "Z4nzu/hackingtool", "NousResearch/hermes-agent", "Alishahryar1/free-claude-code", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [562, 573, 576, 598, 608, 614, 744, 766, 773, 871, 871, 879, 879, 907, 1221, 1444, 2091, 2264, 2477, 3869]},
        'monthly': {"categories": ["shanraisshan/claude-code-best-practice", "Yeachan-Heo/oh-my-codex", "thedotmack/claude-mem", "addyosmani/agent-skills", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "anthropics/claude-code", "openclaw/openclaw", "garrytan/gstack", "safishamsi/graphify", "chenglou/pretext", "santifer/career-ops", "MemPalace/mempalace", "JuliusBrussee/caveman", "obra/superpowers", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4150, 4198, 4507, 4522, 4577, 4757, 5179, 5191, 5319, 6197, 6866, 7280, 7963, 7978, 8325, 9098, 12486, 13352, 18499, 25480]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +564 | 36715 |
| 2 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +181 | 17376 |
| 3 | [openai/symphony](https://github.com/openai/symphony) | +134 | 17674 |
| 4 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +130 | 32561 |
| 5 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +119 | 44635 |
| 6 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +95 | 3908 |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +87 | 49194 |
| 8 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +85 | 37258 |
| 9 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +80 | 17103 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +78 | 25234 |
| 11 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +76 | 37697 |
| 12 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +65 | 42126 |
| 13 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +62 | 12475 |
| 14 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +61 | 1457 |
| 15 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +58 | 7818 |
| 16 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +52 | 4498 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +49 | 22408 |
| 18 | [gastownhall/beads](https://github.com/gastownhall/beads) | +49 | 22474 |
| 19 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +42 | 29962 |
| 20 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +41 | 3133 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +40 | 9076 |
| 22 | [vercel-labs/portless](https://github.com/vercel-labs/portless) | +40 | 8107 |
| 23 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +40 | 15978 |
| 24 | [blader/humanizer](https://github.com/blader/humanizer) | +40 | 16258 |
| 25 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +37 | 8170 |
| 26 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +34 | 16420 |
| 27 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +34 | 26103 |
| 28 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +34 | 1682 |
| 29 | [jackwener/opencli](https://github.com/jackwener/opencli) | +33 | 17993 |
| 30 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +33 | 2415 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3869 | 96684 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2477 | 36716 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2264 | 17376 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2091 | 122737 |
| 5 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1444 | 55070 |
| 6 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1221 | 7818 |
| 7 | [garrytan/gstack](https://github.com/garrytan/gstack) | +907 | 86063 |
| 8 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +879 | 25234 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +879 | 49194 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +871 | 37697 |
| 11 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +871 | 17103 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +773 | 37258 |
| 13 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +766 | 54358 |
| 14 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +744 | 67455 |
| 15 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +614 | 3783 |
| 16 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +608 | 9701 |
| 17 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +598 | 32561 |
| 18 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +576 | 42126 |
| 19 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +573 | 25744 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +562 | 12475 |
| 21 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +560 | 4574 |
| 22 | [multica-ai/multica](https://github.com/multica-ai/multica) | +548 | 22408 |
| 23 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +515 | 10078 |
| 24 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +513 | 3498 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +492 | 7873 |
| 26 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +475 | 44635 |
| 27 | [santifer/career-ops](https://github.com/santifer/career-ops) | +435 | 40627 |
| 28 | [tw93/Kami](https://github.com/tw93/Kami) | +402 | 3733 |
| 29 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +387 | 13763 |
| 30 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +367 | 3908 |
| 31 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +366 | 25389 |
| 32 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +365 | 19263 |
| 33 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +361 | 7986 |
| 34 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +331 | 15978 |
| 35 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +322 | 19230 |
| 36 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +317 | 16420 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +314 | 41479 |
| 38 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +312 | 10921 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +307 | 9076 |
| 40 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +304 | 4498 |
| 41 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +302 | 22412 |
| 42 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +294 | 12038 |
| 43 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +291 | 7302 |
| 44 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +289 | 13710 |
| 45 | [PostHog/posthog](https://github.com/PostHog/posthog) | +283 | 31767 |
| 46 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +274 | 49011 |
| 47 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +262 | 32836 |
| 48 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +258 | 24849 |
| 49 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +257 | 23877 |
| 50 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +255 | 21872 |
| 51 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +253 | 57199 |
| 52 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +251 | 52946 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +249 | 29487 |
| 54 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +247 | 29963 |
| 55 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +247 | 26622 |
| 56 | [victorchen96/deepseek_v4_rolepaly_instruct](https://github.com/victorchen96/deepseek_v4_rolepaly_instruct) | +238 | 1450 |
| 57 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +237 | 16484 |
| 58 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +235 | 50184 |
| 59 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +225 | 1682 |
| 60 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +220 | 33420 |
| 61 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +219 | 32188 |
| 62 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +219 | 40668 |
| 63 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +217 | 3785 |
| 64 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +217 | 4758 |
| 65 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +216 | 8934 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +216 | 43640 |
| 67 | [trycua/cua](https://github.com/trycua/cua) | +215 | 14849 |
| 68 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +215 | 41703 |
| 69 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +210 | 8170 |
| 70 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +207 | 22778 |
| 71 | [gastownhall/beads](https://github.com/gastownhall/beads) | +205 | 22474 |
| 72 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +203 | 3484 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +203 | 29532 |
| 74 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +202 | 7179 |
| 75 | [penpot/penpot](https://github.com/penpot/penpot) | +200 | 44370 |
| 76 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +198 | 25495 |
| 77 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +197 | 20172 |
| 78 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +195 | 27070 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +195 | 13771 |
| 80 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +193 | 18566 |
| 81 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +188 | 1383 |
| 82 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +187 | 26103 |
| 83 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +185 | 4485 |
| 84 | [tiagozip/cap](https://github.com/tiagozip/cap) | +185 | 6133 |
| 85 | [leigest519/OpenGame](https://github.com/leigest519/OpenGame) | +182 | 1504 |
| 86 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +181 | 31765 |
| 87 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +180 | 35539 |
| 88 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +179 | 5023 |
| 89 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +178 | 1457 |
| 90 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +177 | 1643 |
| 91 | [blader/humanizer](https://github.com/blader/humanizer) | +175 | 16258 |
| 92 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +166 | 33847 |
| 93 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +165 | 39204 |
| 94 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +162 | 1016 |
| 95 | [openai/symphony](https://github.com/openai/symphony) | +160 | 17674 |
| 96 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +158 | 8958 |
| 97 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +156 | 5508 |
| 98 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +155 | 3675 |
| 99 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +154 | 11198 |
| 100 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +153 | 24246 |
| 101 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +149 | 2434 |
| 102 | [zhom/donutbrowser](https://github.com/zhom/donutbrowser) | +145 | 2142 |
| 103 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +143 | 2281 |
| 104 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +140 | 940 |
| 105 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +137 | 820 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +134 | 13059 |
| 107 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +129 | 30693 |
| 108 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +128 | 4803 |
| 109 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +128 | 36799 |
| 110 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +126 | 1287 |
| 111 | [deepseek-ai/TileKernels](https://github.com/deepseek-ai/TileKernels) | +126 | 1314 |
| 112 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +123 | 41190 |
| 113 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +123 | 32913 |
| 114 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +120 | 11908 |
| 115 | [jundot/omlx](https://github.com/jundot/omlx) | +120 | 11748 |
| 116 | [wxyhgk/retain-pdf](https://github.com/wxyhgk/retain-pdf) | +119 | 1111 |
| 117 | [Russell-cell/PPT-Design-Prompt](https://github.com/Russell-cell/PPT-Design-Prompt) | +119 | 846 |
| 118 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +118 | 16879 |
| 119 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +116 | 16146 |
| 120 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +112 | 11488 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25480 | 189040 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18499 | 122737 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +13352 | 96684 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12486 | 67455 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9098 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +8325 | 60312 |
| 7 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7978 | 49194 |
| 8 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7963 | 50184 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7280 | 40627 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6866 | 45627 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6197 | 37258 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5319 | 86063 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5191 | 224760 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5179 | 69674 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4757 | 24849 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4577 | 33420 |
| 17 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4522 | 25234 |
| 18 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4507 | 30678 |
| 19 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4198 | 26622 |
| 20 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4150 | 49011 |
| 21 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4116 | 29963 |
| 22 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4089 | 88186 |
| 23 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3955 | 60177 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3775 | 22408 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3693 | 37697 |
| 26 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3535 | 36716 |
| 27 | [anthropics/skills](https://github.com/anthropics/skills) | +3412 | 74774 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3279 | 109881 |
| 29 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3183 | 77528 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3043 | 54358 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3025 | 34148 |
| 32 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2941 | 44635 |
| 33 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2823 | 31765 |
| 34 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2818 | 17159 |
| 35 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2760 | 16879 |
| 36 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2693 | 15978 |
| 37 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2564 | 57199 |
| 38 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2535 | 16553 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2430 | 17378 |
| 40 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2408 | 58025 |
| 41 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2369 | 58442 |
| 42 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2368 | 11488 |
| 43 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2281 | 64133 |
| 44 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2270 | 17103 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2257 | 12038 |
| 46 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2251 | 85286 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2194 | 42126 |
| 48 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2153 | 22412 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2151 | 12475 |
| 50 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2142 | 32561 |
| 51 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2140 | 18566 |
| 52 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1943 | 31098 |
| 53 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1934 | 55070 |
| 54 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1913 | 24246 |
| 55 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1904 | 28680 |
| 56 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1897 | 21872 |
| 57 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1890 | 30590 |
| 58 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1873 | 33878 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1851 | 16146 |
| 60 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1839 | 10112 |
| 61 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1826 | 13079 |
| 62 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1778 | 13772 |
| 63 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1687 | 17993 |
| 64 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1653 | 27070 |
| 65 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1647 | 19633 |
| 66 | [openai/codex](https://github.com/openai/codex) | +1579 | 61744 |
| 67 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1565 | 25744 |
| 68 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1538 | 79656 |
| 69 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1496 | 73135 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1491 | 29487 |
| 71 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1481 | 18789 |
| 72 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1480 | 32913 |
| 73 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1471 | 23877 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1471 | 41479 |
| 75 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1447 | 16484 |
| 76 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1431 | 8958 |
| 77 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1425 | 11756 |
| 78 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1421 | 6684 |
| 79 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1421 | 98536 |
| 80 | [github/spec-kit](https://github.com/github/spec-kit) | +1403 | 71722 |
| 81 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1365 | 45886 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1364 | 37330 |
| 83 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1334 | 22216 |
| 84 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1330 | 52946 |
| 85 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1324 | 6691 |
| 86 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1319 | 41703 |
| 87 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1317 | 95754 |
| 88 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1317 | 22778 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1313 | 25390 |
| 90 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1284 | 10794 |
| 91 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1282 | 43640 |
| 92 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1277 | 7874 |
| 93 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1263 | 35539 |
| 94 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1248 | 18435 |
| 95 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1240 | 13763 |
| 96 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1231 | 16420 |
| 97 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1223 | 7818 |
| 98 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1110 | 9701 |
| 99 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1087 | 21057 |
| 100 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1066 | 7986 |
| 101 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1029 | 78902 |
| 102 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1018 | 6264 |
| 103 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +994 | 9076 |
| 104 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +976 | 32188 |
| 105 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +965 | 9044 |
| 106 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +960 | 39204 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +941 | 13059 |
| 108 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +904 | 25495 |
| 109 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +896 | 4803 |
| 110 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +870 | 47122 |
| 111 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +870 | 7064 |
| 112 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +862 | 6610 |
| 113 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +861 | 5023 |
| 114 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +856 | 11961 |
| 115 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +842 | 4879 |
| 116 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +841 | 52700 |
| 117 | [google/magika](https://github.com/google/magika) | +830 | 16806 |
| 118 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +830 | 4410 |
| 119 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +801 | 5508 |
| 120 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +770 | 4758 |
| 121 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +750 | 5628 |
| 122 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +739 | 4075 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +735 | 11198 |
| 124 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +735 | 9686 |
| 125 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +728 | 41190 |
| 126 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +727 | 21950 |
| 127 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +723 | 12052 |
| 128 | [jundot/omlx](https://github.com/jundot/omlx) | +722 | 11748 |
| 129 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +719 | 5879 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +693 | 39841 |
| 131 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +690 | 3484 |
| 132 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +679 | 4216 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +666 | 54903 |
| 134 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +663 | 19230 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +642 | 34495 |
| 136 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +634 | 31513 |
| 137 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +620 | 30265 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +602 | 36799 |
| 139 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +596 | 11541 |
| 140 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +588 | 23204 |
| 141 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +560 | 3555 |
| 142 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +552 | 3232 |
| 143 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +550 | 19671 |
| 144 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +537 | 37564 |
| 145 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +535 | 2621 |
| 146 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +533 | 18111 |
| 147 | [eze-is/web-access](https://github.com/eze-is/web-access) | +532 | 5795 |
| 148 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +526 | 17450 |
| 149 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +523 | 7302 |
| 150 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +523 | 7717 |
| 151 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +522 | 3785 |
| 152 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +506 | 30693 |
| 153 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +506 | 30907 |
| 154 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +505 | 3208 |
| 155 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +501 | 11908 |
| 156 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +499 | 25916 |
| 157 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +496 | 24992 |
| 158 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +495 | 2878 |
| 159 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +486 | 4952 |
| 160 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +482 | 24440 |
| 161 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +466 | 2685 |
| 162 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +457 | 2408 |
| 163 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +453 | 11776 |
| 164 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +449 | 2644 |
| 165 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +448 | 3937 |
| 166 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +444 | 3386 |
| 167 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +442 | 3675 |
| 168 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +432 | 6863 |
| 169 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +428 | 7179 |
| 170 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +415 | 36907 |
| 171 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +407 | 24240 |
| 172 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +403 | 3908 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +403 | 9653 |
| 174 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +398 | 19840 |
| 175 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +391 | 2474 |
| 176 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +387 | 8170 |
| 177 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +385 | 26103 |
| 178 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +372 | 2336 |
| 179 | [PostHog/posthog](https://github.com/PostHog/posthog) | +362 | 31767 |
| 180 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +346 | 25870 |
| 181 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +328 | 3539 |
| 182 | [floci-io/floci](https://github.com/floci-io/floci) | +328 | 4249 |
| 183 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +322 | 5884 |
| 184 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +322 | 3346 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +317 | 12668 |
| 186 | [decolua/9router](https://github.com/decolua/9router) | +298 | 3289 |
| 187 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +296 | 9124 |
| 188 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +270 | 36103 |
| 189 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +266 | 2838 |
| 190 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +257 | 26552 |
| 191 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +252 | 1936 |
| 192 | [88lin/video_vip](https://github.com/88lin/video_vip) | +230 | 1558 |
| 193 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +227 | 3281 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +210 | 15906 |
| 195 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +208 | 7393 |
| 196 | [tiagozip/cap](https://github.com/tiagozip/cap) | +206 | 6133 |
| 197 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +204 | 2821 |
| 198 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +201 | 11389 |
| 199 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +199 | 2795 |
| 200 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +194 | 33712 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +183 | 5577 |
| 202 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +180 | 4245 |
| 203 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +179 | 8805 |
| 204 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +174 | 3153 |
| 205 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +171 | 8002 |
| 206 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +168 | 2585 |
| 207 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +167 | 4014 |
| 208 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +167 | 574 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +165 | 41086 |
| 210 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 820 |
| 211 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +160 | 1055 |
| 212 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +160 | 13093 |
| 213 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +157 | 1541 |
| 214 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +152 | 22461 |
| 215 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +151 | 1074 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +151 | 40265 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +145 | 35473 |
| 218 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +135 | 1692 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +135 | 23645 |
| 220 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +132 | 878 |
| 221 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +132 | 14490 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +131 | 1812 |
| 223 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +130 | 29799 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +124 | 29816 |
| 225 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +123 | 718 |
| 226 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 610 |
| 227 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +118 | 626 |
| 228 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +118 | 7399 |
| 229 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +118 | 5522 |
| 230 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +117 | 39596 |
| 231 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +116 | 760 |
| 232 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +115 | 19247 |
| 233 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +109 | 6809 |
| 234 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +109 | 10930 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +106 | 26920 |
| 236 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 498 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +105 | 33000 |
| 238 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +103 | 675 |
| 239 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +103 | 1060 |
| 240 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +103 | 2029 |
| 241 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +102 | 646 |
| 242 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +101 | 769 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +99 | 12974 |
| 244 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +97 | 644 |
| 245 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +96 | 1469 |
| 246 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 247 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +93 | 1124 |
| 248 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +93 | 1945 |
| 249 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | +92 | 1287 |
| 250 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +92 | 3123 |
| 251 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +92 | 1874 |
| 252 | [crimera/piko](https://github.com/crimera/piko) | +92 | 3370 |
| 253 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +91 | 1203 |
| 254 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +91 | 493 |
| 255 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +90 | 1867 |
| 256 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +90 | 2397 |
| 257 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +89 | 584 |
| 258 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +89 | 48784 |
| 259 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 465 |
| 260 | [openmemind/memind](https://github.com/openmemind/memind) | +88 | 569 |
| 261 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +87 | 765 |
| 262 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +87 | 1413 |
| 263 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +86 | 3892 |
| 264 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +83 | 429 |
| 265 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +82 | 478 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +82 | 1801 |
| 267 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +81 | 1563 |
| 268 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +81 | 644 |
| 269 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +81 | 45263 |
| 270 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +80 | 711 |
| 271 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +80 | 4093 |
| 272 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +77 | 2774 |
| 273 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +76 | 3706 |
| 274 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +75 | 1609 |
| 275 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +75 | 2782 |
| 276 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +74 | 629 |
| 277 | [robinebers/openusage](https://github.com/robinebers/openusage) | +74 | 2072 |
| 278 | [microg/GmsCore](https://github.com/microg/GmsCore) | +72 | 13086 |
| 279 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +71 | 27404 |
| 280 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +66 | 9420 |
| 281 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +65 | 380 |
| 282 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +61 | 7341 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1715 |
| 284 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +58 | 11796 |
| 285 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +56 | 327 |
| 286 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +56 | 28980 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 288 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +55 | 4926 |
| 289 | [halo-dev/halo](https://github.com/halo-dev/halo) | +55 | 37991 |
| 290 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 291 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +53 | 1900 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +50 | 31476 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1809 |
| 294 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +47 | 243 |
| 295 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +46 | 305 |
| 296 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1741 |
| 297 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +41 | 599 |
| 298 | [hoo-dles/morphe-patches](https://github.com/hoo-dles/morphe-patches) | +41 | 455 |
| 299 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +41 | 8603 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
