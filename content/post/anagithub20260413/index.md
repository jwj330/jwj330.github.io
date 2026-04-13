---
title: "2026-04-13 GitHub增长趋势报告"
description: "1.hermes-agent+2633 2.andrej-karpathy-skills+1152 3.caveman+898 4.claude-mem+701 5.awesome-design-md+630"
date: 2026-04-13T20:58:12+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-13 20:58:12

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
        'daily': {"categories": ["snarktank/ralph", "tirth8205/code-review-graph", "siddharthvaddem/openscreen", "virattt/ai-hedge-fund", "coleam00/Archon", "rtk-ai/rtk", "nikopueringer/CorridorKey", "anthropics/claude-cookbooks", "alchaincyf/nuwa-skill", "addyosmani/agent-skills", "OpenBMB/VoxCPM", "garrytan/gbrain", "multica-ai/multica", "safishamsi/graphify", "shanraisshan/claude-code-best-practice", "VoltAgent/awesome-design-md", "thedotmack/claude-mem", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [155, 157, 160, 165, 166, 184, 204, 213, 254, 334, 354, 400, 409, 417, 598, 630, 701, 898, 1152, 2633]},
        'weekly': {"categories": ["HKUDS/DeepTutor", "garrytan/gstack", "rtk-ai/rtk", "OpenBMB/VoxCPM", "thedotmack/claude-mem", "alchaincyf/zhangxuefeng-skill", "msitarzewski/agency-agents", "garrytan/gbrain", "alchaincyf/nuwa-skill", "shanraisshan/claude-code-best-practice", "multica-ai/multica", "addyosmani/agent-skills", "ultraworkers/claw-code", "affaan-m/everything-claude-code", "obra/superpowers", "forrestchang/andrej-karpathy-skills", "safishamsi/graphify", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent"], "data": [1170, 1172, 1187, 1209, 1244, 1249, 1284, 1558, 1574, 1742, 1818, 1918, 2177, 2413, 2440, 2528, 4233, 4400, 5451, 9454]},
        'monthly': {"categories": ["anthropics/skills", "siddharthvaddem/openscreen", "safishamsi/graphify", "shareAI-lab/learn-claude-code", "shanraisshan/claude-code-best-practice", "bytedance/deer-flow", "JuliusBrussee/caveman", "anthropics/claude-code", "paperclipai/paperclip", "666ghj/MiroFish", "chenglou/pretext", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw", "VoltAgent/awesome-design-md", "obra/superpowers", "garrytan/gstack", "NousResearch/hermes-agent", "affaan-m/everything-claude-code", "ultraworkers/claw-code"], "data": [4166, 4185, 4332, 4555, 4644, 4825, 4946, 5397, 5443, 6280, 6606, 7449, 7888, 9138, 9659, 11683, 11834, 12820, 13330, 24470]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2633 | 76437 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1152 | 24150 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +898 | 25730 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +701 | 30678 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +630 | 48072 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +598 | 41400 |
| 7 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +417 | 25007 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +409 | 10930 |
| 9 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +400 | 7347 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +354 | 12236 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +334 | 14751 |
| 12 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +254 | 9615 |
| 13 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +213 | 33311 |
| 14 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +204 | 10590 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +184 | 25497 |
| 16 | [coleam00/Archon](https://github.com/coleam00/Archon) | +166 | 17559 |
| 17 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +165 | 45886 |
| 18 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +160 | 29316 |
| 19 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +157 | 9478 |
| 20 | [snarktank/ralph](https://github.com/snarktank/ralph) | +155 | 16467 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +154 | 44066 |
| 22 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +151 | 3463 |
| 23 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +150 | 25578 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +146 | 22188 |
| 25 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +146 | 52002 |
| 26 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +144 | 52759 |
| 27 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +144 | 5519 |
| 28 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +137 | 23548 |
| 29 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +129 | 16487 |
| 30 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +126 | 16175 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +9454 | 76437 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5451 | 48072 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4400 | 25731 |
| 4 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4233 | 25007 |
| 5 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2528 | 24150 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2440 | 60312 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2413 | 51199 |
| 8 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +2177 | 183332 |
| 9 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1918 | 14751 |
| 10 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1818 | 10930 |
| 11 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1742 | 41400 |
| 12 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1574 | 9615 |
| 13 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1558 | 7347 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1284 | 79389 |
| 15 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1249 | 5519 |
| 16 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1244 | 30678 |
| 17 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1209 | 12236 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1187 | 25497 |
| 19 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1172 | 71456 |
| 20 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1170 | 17704 |
| 21 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +1166 | 29316 |
| 22 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +1030 | 13747 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +1016 | 74774 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1008 | 22188 |
| 25 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +959 | 16487 |
| 26 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +941 | 26040 |
| 27 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +922 | 71555 |
| 28 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +915 | 52971 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +897 | 34148 |
| 30 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +842 | 27124 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +835 | 44066 |
| 32 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +822 | 9478 |
| 33 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +812 | 54632 |
| 34 | [coleam00/Archon](https://github.com/coleam00/Archon) | +752 | 17559 |
| 35 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +750 | 52759 |
| 36 | [block/goose](https://github.com/block/goose) | +729 | 31098 |
| 37 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +716 | 52002 |
| 38 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +679 | 11156 |
| 39 | [farzaa/clicky](https://github.com/farzaa/clicky) | +676 | 4069 |
| 40 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +675 | 23548 |
| 41 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +669 | 20886 |
| 42 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +668 | 3629 |
| 43 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +660 | 28402 |
| 44 | [chenglou/pretext](https://github.com/chenglou/pretext) | +652 | 43509 |
| 45 | [tobi/qmd](https://github.com/tobi/qmd) | +571 | 21382 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +555 | 35207 |
| 47 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +524 | 4822 |
| 48 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +519 | 45886 |
| 49 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +517 | 61115 |
| 50 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +517 | 33878 |
| 51 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +498 | 39267 |
| 52 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +492 | 21527 |
| 53 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +490 | 18966 |
| 54 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +480 | 12292 |
| 55 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +479 | 30590 |
| 56 | [tw93/Waza](https://github.com/tw93/Waza) | +458 | 3005 |
| 57 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +455 | 2643 |
| 58 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +442 | 25692 |
| 59 | [mattpocock/skills](https://github.com/mattpocock/skills) | +437 | 14695 |
| 60 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +415 | 7741 |
| 61 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +407 | 6133 |
| 62 | [jackwener/opencli](https://github.com/jackwener/opencli) | +403 | 15468 |
| 63 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +400 | 2618 |
| 64 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +399 | 2497 |
| 65 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +396 | 2268 |
| 66 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +393 | 9192 |
| 67 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +391 | 38192 |
| 68 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +385 | 2123 |
| 69 | [snarktank/ralph](https://github.com/snarktank/ralph) | +382 | 16467 |
| 70 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +374 | 14031 |
| 71 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +374 | 2091 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +363 | 20850 |
| 73 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +362 | 4667 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +361 | 35882 |
| 75 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +357 | 37330 |
| 76 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +356 | 36703 |
| 77 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +353 | 30502 |
| 78 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +347 | 3653 |
| 79 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +345 | 12256 |
| 80 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +341 | 11122 |
| 81 | [google-research/timesfm](https://github.com/google-research/timesfm) | +339 | 16921 |
| 82 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +338 | 39592 |
| 83 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +333 | 17254 |
| 84 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +330 | 32735 |
| 85 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +322 | 34786 |
| 86 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +322 | 26925 |
| 87 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +320 | 23211 |
| 88 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +319 | 4706 |
| 89 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +314 | 38501 |
| 90 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +313 | 18855 |
| 91 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +310 | 7720 |
| 92 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +309 | 23448 |
| 93 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +302 | 33311 |
| 94 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +293 | 31589 |
| 95 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +287 | 2969 |
| 96 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +285 | 25578 |
| 97 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +284 | 45873 |
| 98 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +278 | 1740 |
| 99 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +275 | 29697 |
| 100 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +269 | 4411 |
| 101 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +253 | 16175 |
| 102 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +249 | 1585 |
| 103 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +247 | 3225 |
| 104 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +244 | 10453 |
| 105 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +244 | 20604 |
| 106 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +238 | 2275 |
| 107 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +233 | 1596 |
| 108 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +231 | 10590 |
| 109 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +229 | 9122 |
| 110 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +227 | 4156 |
| 111 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +225 | 10883 |
| 112 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +219 | 39370 |
| 113 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +211 | 10520 |
| 114 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +206 | 4933 |
| 115 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +205 | 1634 |
| 116 | [mattmireles/gemma-tuner-multimodal](https://github.com/mattmireles/gemma-tuner-multimodal) | +203 | 1251 |
| 117 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +197 | 19452 |
| 118 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +192 | 1792 |
| 119 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +187 | 13313 |
| 120 | [jundot/omlx](https://github.com/jundot/omlx) | +182 | 9735 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24470 | 183332 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13330 | 51199 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +12820 | 76437 |
| 4 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11834 | 71456 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +11683 | 60312 |
| 6 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +9659 | 48072 |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +9138 | 224760 |
| 8 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +7888 | 79389 |
| 9 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +7449 | 71555 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6606 | 43509 |
| 11 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +6280 | 54632 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +5443 | 52971 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5397 | 69674 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4946 | 25732 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4825 | 61115 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4644 | 41400 |
| 17 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4555 | 52759 |
| 18 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4332 | 25007 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4185 | 29316 |
| 20 | [anthropics/skills](https://github.com/anthropics/skills) | +4166 | 74774 |
| 21 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3920 | 52002 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3893 | 34148 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3886 | 109881 |
| 24 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3857 | 30502 |
| 25 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3827 | 26040 |
| 26 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3760 | 23448 |
| 27 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3650 | 22188 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3147 | 30590 |
| 29 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3082 | 30678 |
| 30 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3046 | 25497 |
| 31 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3020 | 14751 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2980 | 28402 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2893 | 19156 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2867 | 44066 |
| 35 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2829 | 85286 |
| 36 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2768 | 28620 |
| 37 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2746 | 22193 |
| 38 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2741 | 27124 |
| 39 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2664 | 15468 |
| 40 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2611 | 15401 |
| 41 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2600 | 24150 |
| 42 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2549 | 16487 |
| 43 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2514 | 21527 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2439 | 18855 |
| 45 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2410 | 29420 |
| 46 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2400 | 39267 |
| 47 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2264 | 13747 |
| 48 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2167 | 14031 |
| 49 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2166 | 18966 |
| 50 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2158 | 35207 |
| 51 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2132 | 14695 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2123 | 33878 |
| 53 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2052 | 10930 |
| 54 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2013 | 48126 |
| 55 | [github/spec-kit](https://github.com/github/spec-kit) | +1966 | 71722 |
| 56 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1958 | 16915 |
| 57 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1873 | 11156 |
| 58 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1826 | 20604 |
| 59 | [block/goose](https://github.com/block/goose) | +1805 | 31098 |
| 60 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1800 | 29697 |
| 61 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1795 | 46570 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1783 | 23548 |
| 63 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1782 | 9615 |
| 64 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1779 | 26925 |
| 65 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1767 | 38501 |
| 66 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1736 | 25692 |
| 67 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1735 | 11101 |
| 68 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1711 | 45873 |
| 69 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1704 | 31589 |
| 70 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1697 | 9187 |
| 71 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1691 | 9478 |
| 72 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1676 | 37330 |
| 73 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1629 | 39592 |
| 74 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1610 | 79656 |
| 75 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1607 | 10299 |
| 76 | [tanweai/pua](https://github.com/tanweai/pua) | +1604 | 15972 |
| 77 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1558 | 7347 |
| 78 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1541 | 13588 |
| 79 | [openai/codex](https://github.com/openai/codex) | +1518 | 61744 |
| 80 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1497 | 32735 |
| 81 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1448 | 10405 |
| 82 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1443 | 17254 |
| 83 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1433 | 98536 |
| 84 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1400 | 11607 |
| 85 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1392 | 35882 |
| 86 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1371 | 28993 |
| 87 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1370 | 17704 |
| 88 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1362 | 23211 |
| 89 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1353 | 8760 |
| 90 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1340 | 73135 |
| 91 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1323 | 20850 |
| 92 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1313 | 78902 |
| 93 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1311 | 6669 |
| 94 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1304 | 36703 |
| 95 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1285 | 12256 |
| 96 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1273 | 19253 |
| 97 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1272 | 52700 |
| 98 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1251 | 5519 |
| 99 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1236 | 12236 |
| 100 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1234 | 16846 |
| 101 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1222 | 16921 |
| 102 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1186 | 29867 |
| 103 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1171 | 39370 |
| 104 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1151 | 20886 |
| 105 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1134 | 12885 |
| 106 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1132 | 5690 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1085 | 6483 |
| 108 | [cft0808/edict](https://github.com/cft0808/edict) | +1063 | 15000 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +1040 | 9735 |
| 110 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1028 | 10883 |
| 111 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +986 | 9122 |
| 112 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +974 | 38217 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +962 | 10453 |
| 114 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +936 | 5920 |
| 115 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +927 | 8831 |
| 116 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +923 | 27209 |
| 117 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +908 | 23986 |
| 118 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +891 | 49621 |
| 119 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +879 | 39841 |
| 120 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +845 | 6195 |
| 121 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +837 | 10520 |
| 122 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +819 | 43973 |
| 123 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +818 | 45886 |
| 124 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +810 | 5136 |
| 125 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +805 | 15224 |
| 126 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +802 | 23543 |
| 127 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +784 | 4411 |
| 128 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +784 | 4736 |
| 129 | [coleam00/Archon](https://github.com/coleam00/Archon) | +779 | 17559 |
| 130 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +757 | 10591 |
| 131 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +755 | 4338 |
| 132 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +744 | 29551 |
| 133 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +730 | 5499 |
| 134 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +704 | 9192 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +700 | 33113 |
| 136 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +695 | 37564 |
| 137 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +687 | 9494 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +672 | 36799 |
| 139 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +665 | 25152 |
| 140 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +661 | 59619 |
| 141 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +654 | 4915 |
| 142 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +652 | 3225 |
| 143 | [eze-is/web-access](https://github.com/eze-is/web-access) | +637 | 4772 |
| 144 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +621 | 3047 |
| 145 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +620 | 18334 |
| 146 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +618 | 54903 |
| 147 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +613 | 47936 |
| 148 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +603 | 5861 |
| 149 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +601 | 3071 |
| 150 | [floci-io/floci](https://github.com/floci-io/floci) | +574 | 3388 |
| 151 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +559 | 2969 |
| 152 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +557 | 18661 |
| 153 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +544 | 2452 |
| 154 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +542 | 16029 |
| 155 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +540 | 4008 |
| 156 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +529 | 29157 |
| 157 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +522 | 44545 |
| 158 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +521 | 4933 |
| 159 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +519 | 11122 |
| 160 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +518 | 7594 |
| 161 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +512 | 2750 |
| 162 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +508 | 5749 |
| 163 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +495 | 8585 |
| 164 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +494 | 4156 |
| 165 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +481 | 2950 |
| 166 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +478 | 2275 |
| 167 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +459 | 4319 |
| 168 | [openai/skills](https://github.com/openai/skills) | +456 | 16743 |
| 169 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +454 | 3146 |
| 170 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +453 | 18655 |
| 171 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +452 | 2572 |
| 172 | [wshobson/agents](https://github.com/wshobson/agents) | +447 | 33535 |
| 173 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +439 | 1861 |
| 174 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +432 | 2869 |
| 175 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +425 | 8674 |
| 176 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +408 | 2497 |
| 177 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +403 | 4667 |
| 178 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +397 | 2389 |
| 179 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +395 | 25007 |
| 180 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +385 | 2758 |
| 181 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +378 | 2707 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +371 | 11776 |
| 183 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +351 | 1735 |
| 184 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +345 | 1740 |
| 185 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +341 | 1788 |
| 186 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +322 | 23175 |
| 187 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +321 | 5140 |
| 188 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +316 | 3012 |
| 189 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +309 | 2853 |
| 190 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +279 | 5585 |
| 191 | [decolua/9router](https://github.com/decolua/9router) | +278 | 2391 |
| 192 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +275 | 1729 |
| 193 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +268 | 6839 |
| 194 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +265 | 6262 |
| 195 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +263 | 9601 |
| 196 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +262 | 2324 |
| 197 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +259 | 10987 |
| 198 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +249 | 2097 |
| 199 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +239 | 1065 |
| 200 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +236 | 36103 |
| 201 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +234 | 25623 |
| 202 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +232 | 23599 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +227 | 14011 |
| 204 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +223 | 15448 |
| 205 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +221 | 6285 |
| 206 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +214 | 33712 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +205 | 929 |
| 208 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +201 | 2257 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +201 | 41086 |
| 210 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +199 | 2685 |
| 211 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +179 | 2912 |
| 212 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +178 | 666 |
| 213 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +178 | 1315 |
| 214 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +178 | 927 |
| 215 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +173 | 1478 |
| 216 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +166 | 1021 |
| 217 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +156 | 3463 |
| 218 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +155 | 22050 |
| 219 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +154 | 3812 |
| 220 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +153 | 757 |
| 221 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +152 | 40265 |
| 222 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +151 | 1332 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +143 | 35473 |
| 224 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +141 | 902 |
| 225 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +141 | 29527 |
| 226 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 948 |
| 227 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +137 | 3691 |
| 228 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +132 | 10699 |
| 229 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +128 | 29514 |
| 230 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +126 | 812 |
| 231 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +121 | 556 |
| 232 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +120 | 797 |
| 233 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +117 | 1230 |
| 234 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +117 | 23293 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +116 | 26522 |
| 236 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +114 | 12691 |
| 237 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +114 | 1263 |
| 238 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +111 | 1070 |
| 239 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +111 | 761 |
| 240 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +108 | 497 |
| 241 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 242 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +107 | 854 |
| 243 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +107 | 1527 |
| 244 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +106 | 5142 |
| 245 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +106 | 33000 |
| 246 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +105 | 2568 |
| 247 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +105 | 1735 |
| 248 | [RemotePinee/AudioVisual](https://github.com/RemotePinee/AudioVisual) | +102 | 2992 |
| 249 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +100 | 2144 |
| 250 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +98 | 1127 |
| 251 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 252 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +96 | 493 |
| 253 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +95 | 48784 |
| 254 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +93 | 1564 |
| 255 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3886 |
| 256 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +90 | 3525 |
| 257 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +89 | 495 |
| 258 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +89 | 510 |
| 259 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +88 | 1870 |
| 260 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +88 | 1672 |
| 261 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +88 | 1051 |
| 262 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +88 | 1865 |
| 263 | [microg/GmsCore](https://github.com/microg/GmsCore) | +88 | 12912 |
| 264 | [crimera/piko](https://github.com/crimera/piko) | +85 | 3167 |
| 265 | [clawplays/ospec](https://github.com/clawplays/ospec) | +84 | 428 |
| 266 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +83 | 537 |
| 267 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +81 | 548 |
| 268 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +81 | 823 |
| 269 | [robinebers/openusage](https://github.com/robinebers/openusage) | +80 | 1889 |
| 270 | [meodai/heerich](https://github.com/meodai/heerich) | +80 | 474 |
| 271 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +78 | 3640 |
| 272 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +77 | 9212 |
| 273 | [idinging/freemail](https://github.com/idinging/freemail) | +76 | 1343 |
| 274 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +74 | 4004 |
| 275 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +74 | 2687 |
| 276 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +72 | 334 |
| 277 | [openmemind/memind](https://github.com/openmemind/memind) | +71 | 385 |
| 278 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +71 | 11583 |
| 279 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +71 | 45263 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +71 | 27199 |
| 281 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +69 | 423 |
| 282 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +69 | 718 |
| 283 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +68 | 492 |
| 284 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +65 | 1566 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +64 | 7234 |
| 286 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +63 | 8489 |
| 287 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +62 | 390 |
| 288 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +61 | 31476 |
| 289 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +61 | 37313 |
| 290 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +59 | 25392 |
| 291 | [apache/kafka](https://github.com/apache/kafka) | +59 | 32043 |
| 292 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +56 | 286 |
| 293 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +56 | 292 |
| 294 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +56 | 489 |
| 295 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +56 | 1756 |
| 296 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11635 |
| 297 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +54 | 4669 |
| 298 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +52 | 531 |
| 299 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +51 | 28926 |
| 300 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1676 |
