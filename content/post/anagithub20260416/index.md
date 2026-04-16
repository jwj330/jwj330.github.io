---
title: "2026-04-16 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+1011 2.hermes-agent+636 3.awesome-design-md+346 4.caveman+274 5.claude-mem+240"
date: 2026-04-16T20:52:02+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-16 20:52:02

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
        'daily': {"categories": ["alchaincyf/nuwa-skill", "vercel-labs/open-agents", "google/magika", "rtk-ai/rtk", "shanraisshan/claude-code-best-practice", "lsdefine/GenericAgent", "KurtGokhan/tegaki", "jamiepine/voicebox", "EvoMap/evolver", "pascalorg/editor", "safishamsi/graphify", "multica-ai/multica", "davebcn87/pi-autoresearch", "Donchitos/Claude-Code-Game-Studios", "NawfalMotii79/PLFM_RADAR", "thedotmack/claude-mem", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [81, 93, 95, 96, 96, 104, 112, 112, 126, 130, 133, 155, 156, 175, 187, 240, 274, 346, 636, 1011]},
        'weekly': {"categories": ["opendataloader-project/opendataloader-pdf", "HKUDS/DeepTutor", "anthropics/skills", "garrytan/gstack", "rtk-ai/rtk", "alchaincyf/zhangxuefeng-skill", "addyosmani/agent-skills", "alchaincyf/nuwa-skill", "OpenBMB/VoxCPM", "garrytan/gbrain", "affaan-m/everything-claude-code", "thedotmack/claude-mem", "multica-ai/multica", "obra/superpowers", "shanraisshan/claude-code-best-practice", "safishamsi/graphify", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [851, 866, 924, 1015, 1077, 1108, 1158, 1203, 1252, 1709, 1914, 1935, 2037, 2174, 2185, 2433, 3144, 4467, 5379, 9535]},
        'monthly': {"categories": ["shareAI-lab/learn-claude-code", "siddharthvaddem/openscreen", "666ghj/MiroFish", "shanraisshan/claude-code-best-practice", "paperclipai/paperclip", "bytedance/deer-flow", "safishamsi/graphify", "anthropics/claude-code", "msitarzewski/agency-agents", "forrestchang/andrej-karpathy-skills", "karpathy/autoresearch", "JuliusBrussee/caveman", "chenglou/pretext", "openclaw/openclaw", "garrytan/gstack", "VoltAgent/awesome-design-md", "obra/superpowers", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [3986, 4214, 4381, 4427, 4637, 4710, 4759, 5338, 5589, 5725, 5911, 5941, 6702, 7666, 9322, 10588, 10889, 12755, 14767, 24746]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1011 | 49203 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +636 | 93362 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +346 | 56219 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +274 | 34852 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +240 | 30678 |
| 6 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +187 | 10982 |
| 7 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +175 | 11242 |
| 8 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +156 | 4828 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | +155 | 14532 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +133 | 28187 |
| 11 | [pascalorg/editor](https://github.com/pascalorg/editor) | +130 | 13114 |
| 12 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +126 | 3090 |
| 13 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +112 | 18981 |
| 14 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +112 | 1568 |
| 15 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +104 | 2686 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +96 | 45517 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +96 | 27993 |
| 18 | [google/magika](https://github.com/google/magika) | +95 | 14641 |
| 19 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +93 | 3130 |
| 20 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +81 | 11747 |
| 21 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +75 | 994 |
| 22 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +72 | 16440 |
| 23 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +68 | 2292 |
| 24 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +66 | 17701 |
| 25 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +66 | 45926 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +64 | 19930 |
| 27 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +63 | 3327 |
| 28 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +59 | 27076 |
| 29 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +59 | 23562 |
| 30 | [braedonsaunders/codeflow](https://github.com/braedonsaunders/codeflow) | +58 | 1210 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +9535 | 93362 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5379 | 49203 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4467 | 34852 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3144 | 56219 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2433 | 28187 |
| 6 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +2185 | 45517 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2174 | 60312 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2037 | 14532 |
| 9 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1935 | 30678 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1914 | 51199 |
| 11 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1709 | 8635 |
| 12 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1252 | 13760 |
| 13 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1203 | 11747 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1158 | 16440 |
| 15 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1108 | 6024 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1077 | 27993 |
| 17 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1015 | 73911 |
| 18 | [anthropics/skills](https://github.com/anthropics/skills) | +924 | 74774 |
| 19 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +866 | 18724 |
| 20 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +851 | 17701 |
| 21 | [coleam00/Archon](https://github.com/coleam00/Archon) | +828 | 18391 |
| 22 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +806 | 45886 |
| 23 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +781 | 54764 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +762 | 34148 |
| 25 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +751 | 23562 |
| 26 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +746 | 4348 |
| 27 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +741 | 73333 |
| 28 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +712 | 30452 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +699 | 45926 |
| 30 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +695 | 54032 |
| 31 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +680 | 10982 |
| 32 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +638 | 3327 |
| 33 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +623 | 10581 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +599 | 54086 |
| 35 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +596 | 55647 |
| 36 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +596 | 14623 |
| 37 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +582 | 27076 |
| 38 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +573 | 4913 |
| 39 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +562 | 18981 |
| 40 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +534 | 3745 |
| 41 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +502 | 11689 |
| 42 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +484 | 29376 |
| 43 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +470 | 24581 |
| 44 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +469 | 33311 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +457 | 36370 |
| 46 | [Keychron/Keychron-Keyboards-Hardware-Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design) | +449 | 3104 |
| 47 | [snarktank/ralph](https://github.com/snarktank/ralph) | +429 | 17042 |
| 48 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +417 | 22302 |
| 49 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +412 | 26578 |
| 50 | [google/magika](https://github.com/google/magika) | +407 | 14641 |
| 51 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +399 | 2949 |
| 52 | [mattpocock/skills](https://github.com/mattpocock/skills) | +397 | 15660 |
| 53 | [markdown-viewer/skills](https://github.com/markdown-viewer/skills) | +394 | 1811 |
| 54 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +394 | 19930 |
| 55 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +393 | 37543 |
| 56 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +391 | 27704 |
| 57 | [pascalorg/editor](https://github.com/pascalorg/editor) | +385 | 13114 |
| 58 | [chenglou/pretext](https://github.com/chenglou/pretext) | +374 | 44246 |
| 59 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +373 | 39910 |
| 60 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +372 | 3130 |
| 61 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +370 | 2627 |
| 62 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +369 | 37446 |
| 63 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +344 | 13075 |
| 64 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +343 | 11242 |
| 65 | [block/goose](https://github.com/block/goose) | +335 | 31098 |
| 66 | [farzaa/clicky](https://github.com/farzaa/clicky) | +319 | 4305 |
| 67 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +316 | 12528 |
| 68 | [tw93/Mole](https://github.com/tw93/Mole) | +315 | 36870 |
| 69 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +313 | 35465 |
| 70 | [google-research/timesfm](https://github.com/google-research/timesfm) | +313 | 17905 |
| 71 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +311 | 37330 |
| 72 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +310 | 40624 |
| 73 | [tobi/qmd](https://github.com/tobi/qmd) | +305 | 21899 |
| 74 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +303 | 21598 |
| 75 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +302 | 23686 |
| 76 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +301 | 19628 |
| 77 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +300 | 25997 |
| 78 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +297 | 21293 |
| 79 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +294 | 7935 |
| 80 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +293 | 5206 |
| 81 | [tw93/Waza](https://github.com/tw93/Waza) | +291 | 3297 |
| 82 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +290 | 33467 |
| 83 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +288 | 8212 |
| 84 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +286 | 23993 |
| 85 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | +285 | 8576 |
| 86 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +274 | 1826 |
| 87 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +272 | 14714 |
| 88 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +271 | 39137 |
| 89 | [jackwener/opencli](https://github.com/jackwener/opencli) | +270 | 16081 |
| 90 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +267 | 19908 |
| 91 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +265 | 10952 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +263 | 30177 |
| 93 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +259 | 2329 |
| 94 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +250 | 17915 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +249 | 31059 |
| 96 | [alejandrobalderas/claude-code-from-source](https://github.com/alejandrobalderas/claude-code-from-source) | +248 | 1569 |
| 97 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +237 | 2292 |
| 98 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +224 | 10828 |
| 99 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +224 | 4220 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +222 | 11414 |
| 101 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +218 | 5593 |
| 102 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +211 | 27295 |
| 103 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +202 | 2686 |
| 104 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +199 | 1812 |
| 105 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +195 | 6152 |
| 106 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +189 | 10940 |
| 107 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +188 | 39798 |
| 108 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +186 | 1568 |
| 109 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +186 | 4828 |
| 110 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +182 | 17631 |
| 111 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +180 | 3619 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +178 | 10381 |
| 113 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +174 | 20979 |
| 114 | [joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui) | +172 | 939 |
| 115 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +164 | 4668 |
| 116 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +161 | 2581 |
| 117 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +147 | 18648 |
| 118 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +147 | 3020 |
| 119 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +147 | 1009 |
| 120 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +145 | 39841 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24746 | 185282 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +14767 | 93362 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12755 | 51199 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +10889 | 60312 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +10588 | 56219 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +9322 | 73911 |
| 7 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +7666 | 224760 |
| 8 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6702 | 44246 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +5941 | 34852 |
| 10 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +5911 | 73333 |
| 11 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5725 | 49204 |
| 12 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5589 | 81017 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5338 | 69674 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4759 | 28187 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4710 | 62027 |
| 16 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4637 | 54764 |
| 17 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4427 | 45517 |
| 18 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +4381 | 55647 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4214 | 30452 |
| 20 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3986 | 54086 |
| 21 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3955 | 27076 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +3923 | 74774 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3793 | 23562 |
| 24 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3781 | 54032 |
| 25 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3739 | 34148 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3675 | 109881 |
| 27 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3621 | 23993 |
| 28 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3604 | 30678 |
| 29 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3227 | 16440 |
| 30 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3160 | 30590 |
| 31 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3053 | 27993 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3012 | 29376 |
| 33 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2917 | 19328 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2818 | 45926 |
| 35 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2701 | 85286 |
| 36 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2688 | 17701 |
| 37 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2637 | 16053 |
| 38 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2566 | 22302 |
| 39 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2556 | 16081 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2532 | 14532 |
| 41 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2517 | 19628 |
| 42 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2474 | 39910 |
| 43 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2465 | 31059 |
| 44 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2453 | 29779 |
| 45 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2432 | 15776 |
| 46 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2403 | 14623 |
| 47 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2253 | 14714 |
| 48 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2250 | 15660 |
| 49 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2234 | 27704 |
| 50 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2048 | 11747 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2046 | 33878 |
| 52 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1947 | 36370 |
| 53 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1934 | 11689 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1861 | 71722 |
| 55 | [block/goose](https://github.com/block/goose) | +1840 | 31098 |
| 56 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1816 | 27295 |
| 57 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1804 | 10581 |
| 58 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1796 | 13114 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1768 | 24581 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1735 | 8635 |
| 61 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1731 | 9532 |
| 62 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1721 | 19930 |
| 63 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1683 | 79656 |
| 64 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1679 | 39137 |
| 65 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1663 | 32087 |
| 66 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1658 | 10706 |
| 67 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1628 | 11260 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1627 | 26578 |
| 69 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1619 | 48500 |
| 70 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1581 | 28816 |
| 71 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1576 | 13772 |
| 72 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1575 | 11242 |
| 73 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1541 | 37330 |
| 74 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1531 | 40624 |
| 75 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1496 | 20979 |
| 76 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1488 | 46846 |
| 77 | [openai/codex](https://github.com/openai/codex) | +1487 | 61744 |
| 78 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1481 | 18724 |
| 79 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1463 | 22418 |
| 80 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1460 | 13760 |
| 81 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1437 | 37543 |
| 82 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1427 | 30177 |
| 83 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +1410 | 17109 |
| 84 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1407 | 11658 |
| 85 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1401 | 46297 |
| 86 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1391 | 33467 |
| 87 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1355 | 73135 |
| 88 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1349 | 17631 |
| 89 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1346 | 17905 |
| 90 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1340 | 98536 |
| 91 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1325 | 6024 |
| 92 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1318 | 6689 |
| 93 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1291 | 78902 |
| 94 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1289 | 52700 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1263 | 21598 |
| 96 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1200 | 21293 |
| 97 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1199 | 8838 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1195 | 13075 |
| 99 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1135 | 5725 |
| 100 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1129 | 37446 |
| 101 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1118 | 45886 |
| 102 | [tobi/qmd](https://github.com/tobi/qmd) | +1096 | 21899 |
| 103 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1001 | 39798 |
| 104 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +981 | 12944 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +964 | 11414 |
| 106 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +961 | 6104 |
| 107 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +936 | 8890 |
| 108 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +901 | 49621 |
| 109 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +885 | 24154 |
| 110 | [coleam00/Archon](https://github.com/coleam00/Archon) | +873 | 18391 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +872 | 10828 |
| 112 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +867 | 6301 |
| 113 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +865 | 39841 |
| 114 | [jundot/omlx](https://github.com/jundot/omlx) | +857 | 10381 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +857 | 9397 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +849 | 17114 |
| 117 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +846 | 6830 |
| 118 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +836 | 5310 |
| 119 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +835 | 10940 |
| 120 | [cft0808/edict](https://github.com/cft0808/edict) | +824 | 15211 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +803 | 23911 |
| 122 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +797 | 4553 |
| 123 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +797 | 30103 |
| 124 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +791 | 4913 |
| 125 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +791 | 4803 |
| 126 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +738 | 5544 |
| 127 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +726 | 9381 |
| 128 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +723 | 33504 |
| 129 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +721 | 30057 |
| 130 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +704 | 3619 |
| 131 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +691 | 9567 |
| 132 | [eze-is/web-access](https://github.com/eze-is/web-access) | +669 | 5073 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +666 | 36799 |
| 134 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +663 | 59619 |
| 135 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +659 | 19449 |
| 136 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +639 | 37564 |
| 137 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +635 | 3327 |
| 138 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +630 | 3481 |
| 139 | [floci-io/floci](https://github.com/floci-io/floci) | +623 | 3872 |
| 140 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +622 | 54903 |
| 141 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +606 | 3129 |
| 142 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +600 | 38361 |
| 143 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +593 | 25367 |
| 144 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +588 | 5593 |
| 145 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +573 | 18648 |
| 146 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +569 | 11445 |
| 147 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +569 | 47936 |
| 148 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +560 | 5956 |
| 149 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +556 | 15488 |
| 150 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +547 | 4079 |
| 151 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +532 | 43973 |
| 152 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +524 | 10952 |
| 153 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +524 | 29455 |
| 154 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +513 | 16372 |
| 155 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +507 | 2575 |
| 156 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +505 | 5109 |
| 157 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +498 | 2385 |
| 158 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +498 | 6152 |
| 159 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +493 | 3040 |
| 160 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +493 | 3020 |
| 161 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +481 | 18897 |
| 162 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +474 | 44545 |
| 163 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +470 | 4220 |
| 164 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +466 | 4377 |
| 165 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +459 | 3189 |
| 166 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +455 | 2949 |
| 167 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +455 | 1927 |
| 168 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +442 | 7741 |
| 169 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +439 | 18843 |
| 170 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +433 | 9020 |
| 171 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +428 | 4990 |
| 172 | [usestrix/strix](https://github.com/usestrix/strix) | +423 | 24093 |
| 173 | [google/magika](https://github.com/google/magika) | +418 | 14641 |
| 174 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +416 | 2584 |
| 175 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +407 | 2329 |
| 176 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +396 | 19908 |
| 177 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +396 | 2868 |
| 178 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +395 | 2292 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +388 | 2778 |
| 180 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +380 | 25225 |
| 181 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +380 | 2934 |
| 182 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +371 | 1882 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +363 | 11973 |
| 184 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +354 | 1826 |
| 185 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +327 | 23421 |
| 186 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +316 | 2635 |
| 187 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +310 | 2992 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +307 | 5280 |
| 189 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +279 | 3030 |
| 190 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +267 | 6961 |
| 191 | [decolua/9router](https://github.com/decolua/9router) | +266 | 2568 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +265 | 5829 |
| 193 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +248 | 11088 |
| 194 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +235 | 6134 |
| 195 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +234 | 9379 |
| 196 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +227 | 36103 |
| 197 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +224 | 2393 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +223 | 25778 |
| 199 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +212 | 6340 |
| 200 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +209 | 1066 |
| 201 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +205 | 938 |
| 202 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +204 | 15559 |
| 203 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +203 | 1271 |
| 204 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +198 | 1455 |
| 205 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +197 | 2702 |
| 206 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +194 | 33712 |
| 207 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +191 | 3547 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +191 | 41086 |
| 209 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +187 | 23660 |
| 210 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +186 | 2983 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +180 | 540 |
| 212 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +177 | 2337 |
| 213 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +177 | 1767 |
| 214 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +175 | 3091 |
| 215 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +158 | 779 |
| 216 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +155 | 940 |
| 217 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +152 | 3843 |
| 218 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +148 | 956 |
| 219 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +147 | 40265 |
| 220 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +144 | 1562 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +143 | 35473 |
| 222 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +142 | 1390 |
| 223 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +140 | 22122 |
| 224 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 959 |
| 225 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +127 | 820 |
| 226 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 816 |
| 227 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +117 | 29582 |
| 228 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +115 | 5253 |
| 229 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +115 | 10759 |
| 230 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +114 | 1080 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +112 | 12734 |
| 232 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +110 | 26574 |
| 233 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +110 | 873 |
| 234 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +108 | 1301 |
| 235 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +108 | 23351 |
| 236 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +107 | 771 |
| 237 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +104 | 3707 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +104 | 1791 |
| 239 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +102 | 1664 |
| 240 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +102 | 33000 |
| 241 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +99 | 2619 |
| 242 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +99 | 48784 |
| 243 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +97 | 681 |
| 244 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +96 | 551 |
| 245 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 246 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +96 | 0 |
| 247 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +96 | 502 |
| 248 | [clawplays/ospec](https://github.com/clawplays/ospec) | +95 | 517 |
| 249 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +95 | 1147 |
| 250 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +94 | 1296 |
| 251 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +94 | 3948 |
| 252 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +94 | 561 |
| 253 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +92 | 2189 |
| 254 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +88 | 545 |
| 255 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +86 | 1907 |
| 256 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +86 | 573 |
| 257 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3217 |
| 258 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +85 | 1591 |
| 259 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +85 | 3570 |
| 260 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +84 | 1090 |
| 261 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +83 | 571 |
| 262 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +82 | 778 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +80 | 1007 |
| 264 | [meodai/heerich](https://github.com/meodai/heerich) | +80 | 485 |
| 265 | [microg/GmsCore](https://github.com/microg/GmsCore) | +80 | 12948 |
| 266 | [robinebers/openusage](https://github.com/robinebers/openusage) | +77 | 1942 |
| 267 | [openmemind/memind](https://github.com/openmemind/memind) | +77 | 423 |
| 268 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +77 | 9271 |
| 269 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +76 | 3704 |
| 270 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +76 | 854 |
| 271 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +75 | 1902 |
| 272 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +73 | 352 |
| 273 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +73 | 45263 |
| 274 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +71 | 4036 |
| 275 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +70 | 727 |
| 276 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +68 | 6962 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +68 | 27258 |
| 278 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +67 | 1366 |
| 279 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +66 | 451 |
| 280 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +66 | 1693 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +65 | 11637 |
| 282 | [idinging/freemail](https://github.com/idinging/freemail) | +63 | 1362 |
| 283 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +63 | 543 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +62 | 7260 |
| 285 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +62 | 536 |
| 286 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +61 | 339 |
| 287 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +60 | 31476 |
| 288 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +59 | 25413 |
| 289 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +57 | 300 |
| 290 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +56 | 1591 |
| 291 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +55 | 37313 |
| 292 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +54 | 1787 |
| 293 | [apache/kafka](https://github.com/apache/kafka) | +53 | 32043 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +51 | 28939 |
| 295 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +49 | 11648 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +48 | 1703 |
| 297 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +47 | 8508 |
| 298 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1678 |
| 299 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +37 | 122 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +36 | 10126 |
