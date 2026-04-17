---
title: "2026-04-17 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+826 2.hermes-agent+468 3.PLFM_RADAR+353 4.claude-mem+335 5.awesome-design-md+321"
date: 2026-04-17T20:49:21+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-17 20:49:21

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
        'daily': {"categories": ["rtk-ai/rtk", "SimoneAvogadro/android-reverse-engineering-skill", "farion1231/cc-switch", "thunderbird/thunderbolt", "rohitg00/ai-engineering-from-scratch", "vercel-labs/open-agents", "openai/openai-agents-python", "EvoMap/evolver", "jamiepine/voicebox", "lsdefine/GenericAgent", "BasedHardware/omi", "safishamsi/graphify", "google/magika", "multica-ai/multica", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "thedotmack/claude-mem", "NawfalMotii79/PLFM_RADAR", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [73, 77, 77, 82, 82, 84, 85, 95, 100, 101, 111, 120, 122, 139, 237, 321, 335, 353, 468, 826]},
        'weekly': {"categories": ["alchaincyf/zhangxuefeng-skill", "anthropics/skills", "garrytan/gstack", "rtk-ai/rtk", "NawfalMotii79/PLFM_RADAR", "addyosmani/agent-skills", "alchaincyf/nuwa-skill", "OpenBMB/VoxCPM", "garrytan/gbrain", "MemPalace/mempalace", "affaan-m/everything-claude-code", "safishamsi/graphify", "multica-ai/multica", "shanraisshan/claude-code-best-practice", "obra/superpowers", "thedotmack/claude-mem", "VoltAgent/awesome-design-md", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent"], "data": [861, 890, 945, 1005, 1029, 1036, 1053, 1142, 1689, 1763, 1799, 1830, 1940, 1950, 2000, 2192, 2866, 4412, 5890, 8708]},
        'monthly': {"categories": ["luongnv89/claude-howto", "siddharthvaddem/openscreen", "shanraisshan/claude-code-best-practice", "paperclipai/paperclip", "bytedance/deer-flow", "safishamsi/graphify", "msitarzewski/agency-agents", "anthropics/claude-code", "karpathy/autoresearch", "JuliusBrussee/caveman", "forrestchang/andrej-karpathy-skills", "chenglou/pretext", "openclaw/openclaw", "MemPalace/mempalace", "garrytan/gstack", "obra/superpowers", "VoltAgent/awesome-design-md", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4000, 4244, 4426, 4474, 4713, 4870, 5306, 5331, 5706, 6157, 6488, 6735, 7335, 7488, 8946, 10661, 10886, 12508, 15144, 24804]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +826 | 54386 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +468 | 96578 |
| 3 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +353 | 13522 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +335 | 30678 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +321 | 58072 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +237 | 36774 |
| 7 | [multica-ai/multica](https://github.com/multica-ai/multica) | +139 | 15347 |
| 8 | [google/magika](https://github.com/google/magika) | +122 | 15370 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +120 | 29041 |
| 10 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +111 | 9740 |
| 11 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +101 | 3517 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +100 | 19738 |
| 13 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +95 | 4095 |
| 14 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +85 | 21748 |
| 15 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +84 | 3553 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +82 | 3632 |
| 17 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +82 | 956 |
| 18 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +77 | 46525 |
| 19 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +77 | 2698 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +73 | 28576 |
| 21 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +73 | 16190 |
| 22 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +67 | 12237 |
| 23 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +67 | 5420 |
| 24 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +63 | 16895 |
| 25 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +61 | 37962 |
| 26 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +58 | 45954 |
| 27 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +57 | 36792 |
| 28 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +55 | 54426 |
| 29 | [tw93/Mole](https://github.com/tw93/Mole) | +55 | 36870 |
| 30 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +54 | 27328 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +8708 | 96578 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +5890 | 54386 |
| 3 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +4412 | 36774 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2866 | 58072 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2192 | 30678 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +2000 | 60312 |
| 7 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1950 | 45954 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1940 | 15347 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1830 | 29042 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1799 | 51199 |
| 11 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +1763 | 47518 |
| 12 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1689 | 8924 |
| 13 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1142 | 14095 |
| 14 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1053 | 12237 |
| 15 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1036 | 16895 |
| 16 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1029 | 13522 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1005 | 28576 |
| 18 | [garrytan/gstack](https://github.com/garrytan/gstack) | +945 | 74843 |
| 19 | [anthropics/skills](https://github.com/anthropics/skills) | +890 | 74774 |
| 20 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +861 | 6103 |
| 21 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +816 | 45886 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +759 | 34148 |
| 23 | [coleam00/Archon](https://github.com/coleam00/Archon) | +734 | 18542 |
| 24 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +729 | 55328 |
| 25 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +678 | 3570 |
| 26 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +676 | 54401 |
| 27 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +674 | 17930 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +665 | 46525 |
| 29 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +663 | 19019 |
| 30 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +655 | 19738 |
| 31 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +643 | 30777 |
| 32 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +641 | 23798 |
| 33 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +587 | 5097 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +578 | 10793 |
| 35 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +554 | 3885 |
| 36 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +548 | 54426 |
| 37 | [QuipNetwork/quip-node-manager](https://github.com/QuipNetwork/quip-node-manager) | +542 | 4595 |
| 38 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +528 | 55909 |
| 39 | [google/magika](https://github.com/google/magika) | +526 | 15370 |
| 40 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +510 | 27328 |
| 41 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +492 | 11815 |
| 42 | [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | +486 | 33311 |
| 43 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +460 | 14799 |
| 44 | [vercel-labs/open-agents](https://github.com/vercel-labs/open-agents) | +456 | 3553 |
| 45 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +452 | 24792 |
| 46 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +440 | 36792 |
| 47 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +419 | 29636 |
| 48 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +408 | 37962 |
| 49 | [snarktank/ralph](https://github.com/snarktank/ralph) | +400 | 17119 |
| 50 | [markdown-viewer/skills](https://github.com/markdown-viewer/skills) | +396 | 1825 |
| 51 | [pascalorg/editor](https://github.com/pascalorg/editor) | +386 | 13236 |
| 52 | [mattpocock/skills](https://github.com/mattpocock/skills) | +381 | 16029 |
| 53 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +378 | 26878 |
| 54 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +361 | 22439 |
| 55 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +360 | 20285 |
| 56 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +359 | 11698 |
| 57 | [tw93/Mole](https://github.com/tw93/Mole) | +350 | 36870 |
| 58 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +341 | 40056 |
| 59 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +340 | 37674 |
| 60 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +339 | 27861 |
| 61 | [chenglou/pretext](https://github.com/chenglou/pretext) | +334 | 44421 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +331 | 13320 |
| 63 | [Keychron/Keychron-Keyboards-Hardware-Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design) | +312 | 3146 |
| 64 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +302 | 35784 |
| 65 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +301 | 3517 |
| 66 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | +301 | 8704 |
| 67 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +298 | 37330 |
| 68 | [block/goose](https://github.com/block/goose) | +298 | 31098 |
| 69 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +297 | 19811 |
| 70 | [rustfs/rustfs](https://github.com/rustfs/rustfs) | +292 | 26056 |
| 71 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +291 | 33659 |
| 72 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +290 | 23768 |
| 73 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +286 | 3082 |
| 74 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +284 | 24140 |
| 75 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +280 | 40920 |
| 76 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +280 | 11126 |
| 77 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +280 | 1899 |
| 78 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +280 | 19979 |
| 79 | [google-research/timesfm](https://github.com/google-research/timesfm) | +278 | 18020 |
| 80 | [alchaincyf/hermes-agent-orange-book](https://github.com/alchaincyf/hermes-agent-orange-book) | +274 | 2677 |
| 81 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +272 | 21788 |
| 82 | [tobi/qmd](https://github.com/tobi/qmd) | +271 | 22039 |
| 83 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +266 | 2545 |
| 84 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +258 | 39375 |
| 85 | [tw93/Waza](https://github.com/tw93/Waza) | +257 | 3321 |
| 86 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +256 | 5390 |
| 87 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +253 | 14910 |
| 88 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +253 | 2524 |
| 89 | [jackwener/opencli](https://github.com/jackwener/opencli) | +248 | 16234 |
| 90 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +242 | 27384 |
| 91 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +236 | 31237 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +231 | 30289 |
| 93 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +230 | 18100 |
| 94 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +227 | 4095 |
| 95 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +224 | 4229 |
| 96 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +223 | 11595 |
| 97 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +222 | 5776 |
| 98 | [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | +220 | 5420 |
| 99 | [KurtGokhan/tegaki](https://github.com/KurtGokhan/tegaki) | +216 | 1868 |
| 100 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +212 | 9740 |
| 101 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +207 | 10978 |
| 102 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +206 | 1858 |
| 103 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +198 | 3632 |
| 104 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +198 | 27406 |
| 105 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +192 | 6194 |
| 106 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +177 | 11129 |
| 107 | [jundot/omlx](https://github.com/jundot/omlx) | +175 | 10521 |
| 108 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +169 | 21101 |
| 109 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +160 | 3708 |
| 110 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +160 | 2639 |
| 111 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +157 | 39905 |
| 112 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +156 | 17724 |
| 113 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +155 | 4760 |
| 114 | [joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui) | +150 | 1006 |
| 115 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +149 | 16190 |
| 116 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +144 | 30236 |
| 117 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +139 | 2139 |
| 118 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +136 | 6930 |
| 119 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +136 | 18727 |
| 120 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +135 | 33645 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +24804 | 185685 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +15144 | 96578 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +12508 | 51199 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +10886 | 58072 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +10661 | 60312 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +8946 | 74843 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7488 | 47518 |
| 8 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +7335 | 224760 |
| 9 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6735 | 44421 |
| 10 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6488 | 54386 |
| 11 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +6157 | 36774 |
| 12 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +5706 | 73822 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5331 | 69674 |
| 14 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +5306 | 81646 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +4870 | 29043 |
| 16 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4713 | 62276 |
| 17 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4474 | 55329 |
| 18 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4426 | 45954 |
| 19 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4244 | 30777 |
| 20 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4000 | 27328 |
| 21 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +3963 | 55909 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +3897 | 74774 |
| 23 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +3849 | 54426 |
| 24 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3824 | 23798 |
| 25 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3766 | 54401 |
| 26 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3741 | 30678 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3724 | 34148 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3636 | 109881 |
| 29 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3540 | 24140 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3284 | 16895 |
| 31 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3165 | 30590 |
| 32 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3014 | 29636 |
| 33 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2979 | 28576 |
| 34 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2820 | 46525 |
| 35 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2718 | 17930 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2685 | 85286 |
| 37 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2671 | 15347 |
| 38 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2654 | 16154 |
| 39 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2581 | 22439 |
| 40 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2518 | 16234 |
| 41 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2516 | 19372 |
| 42 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2488 | 40056 |
| 43 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2462 | 29893 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2461 | 19811 |
| 45 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2425 | 14799 |
| 46 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2328 | 31237 |
| 47 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2278 | 14910 |
| 48 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2251 | 16029 |
| 49 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2114 | 12237 |
| 50 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2111 | 27861 |
| 51 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2076 | 15858 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2045 | 33878 |
| 53 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1949 | 11815 |
| 54 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1937 | 36792 |
| 55 | [block/goose](https://github.com/block/goose) | +1852 | 31098 |
| 56 | [github/spec-kit](https://github.com/github/spec-kit) | +1852 | 71722 |
| 57 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1826 | 27406 |
| 58 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1817 | 10793 |
| 59 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1792 | 13236 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1775 | 8924 |
| 61 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1769 | 24792 |
| 62 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1758 | 9681 |
| 63 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1698 | 20285 |
| 64 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1692 | 79656 |
| 65 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1667 | 39375 |
| 66 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1667 | 10774 |
| 67 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1655 | 32196 |
| 68 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1608 | 26878 |
| 69 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1599 | 11698 |
| 70 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1584 | 13823 |
| 71 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1526 | 48649 |
| 72 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1515 | 37330 |
| 73 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1511 | 19019 |
| 74 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1503 | 14095 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1494 | 61744 |
| 76 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1494 | 40920 |
| 77 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1450 | 37962 |
| 78 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1441 | 28870 |
| 79 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1434 | 11284 |
| 80 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1427 | 46931 |
| 81 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1409 | 11669 |
| 82 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1395 | 33659 |
| 83 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1360 | 30289 |
| 84 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +1358 | 46413 |
| 85 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1356 | 18020 |
| 86 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1356 | 73135 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1355 | 98536 |
| 88 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1339 | 6103 |
| 89 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1329 | 21101 |
| 90 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1328 | 17724 |
| 91 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1318 | 6696 |
| 92 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1310 | 52700 |
| 93 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1301 | 78902 |
| 94 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +1252 | 22477 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1235 | 21788 |
| 96 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1210 | 21390 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1170 | 13320 |
| 98 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1140 | 45886 |
| 99 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1139 | 5743 |
| 100 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1129 | 13522 |
| 101 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1104 | 37674 |
| 102 | [tobi/qmd](https://github.com/tobi/qmd) | +1075 | 22039 |
| 103 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +978 | 39905 |
| 104 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +974 | 6178 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +966 | 11595 |
| 106 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +957 | 8860 |
| 107 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +938 | 8904 |
| 108 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +900 | 49621 |
| 109 | [coleam00/Archon](https://github.com/coleam00/Archon) | +888 | 18542 |
| 110 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +881 | 24201 |
| 111 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +870 | 6324 |
| 112 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +867 | 39841 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +863 | 10978 |
| 114 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +844 | 5372 |
| 115 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +835 | 17192 |
| 116 | [jundot/omlx](https://github.com/jundot/omlx) | +829 | 10521 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +823 | 9512 |
| 118 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +821 | 11129 |
| 119 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +819 | 5097 |
| 120 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +807 | 6930 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +803 | 23955 |
| 122 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +800 | 4579 |
| 123 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +797 | 4821 |
| 124 | [cft0808/edict](https://github.com/cft0808/edict) | +763 | 15253 |
| 125 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +751 | 33645 |
| 126 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +747 | 30162 |
| 127 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +740 | 5556 |
| 128 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +728 | 9414 |
| 129 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +712 | 30236 |
| 130 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +710 | 3708 |
| 131 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +703 | 12955 |
| 132 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +690 | 9579 |
| 133 | [eze-is/web-access](https://github.com/eze-is/web-access) | +681 | 5193 |
| 134 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +676 | 3570 |
| 135 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +657 | 36799 |
| 136 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +649 | 3616 |
| 137 | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) | +647 | 59619 |
| 138 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +633 | 54903 |
| 139 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +632 | 37564 |
| 140 | [floci-io/floci](https://github.com/floci-io/floci) | +632 | 3919 |
| 141 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +609 | 3158 |
| 142 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +603 | 5776 |
| 143 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +597 | 19512 |
| 144 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +579 | 25429 |
| 145 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +576 | 3632 |
| 146 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +572 | 11459 |
| 147 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +568 | 18727 |
| 148 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +564 | 47936 |
| 149 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +557 | 38380 |
| 150 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +548 | 4143 |
| 151 | [google/magika](https://github.com/google/magika) | +543 | 15370 |
| 152 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +524 | 15551 |
| 153 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +524 | 5976 |
| 154 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +523 | 43973 |
| 155 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +516 | 11126 |
| 156 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +513 | 16469 |
| 157 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +510 | 29525 |
| 158 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +504 | 2627 |
| 159 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +500 | 2404 |
| 160 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +495 | 3054 |
| 161 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +494 | 6194 |
| 162 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +492 | 5180 |
| 163 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +470 | 3082 |
| 164 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +466 | 44545 |
| 165 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +465 | 4401 |
| 166 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +460 | 3196 |
| 167 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +460 | 4229 |
| 168 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +456 | 1942 |
| 169 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +443 | 5095 |
| 170 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +435 | 2545 |
| 171 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +433 | 2524 |
| 172 | [usestrix/strix](https://github.com/usestrix/strix) | +432 | 24158 |
| 173 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +431 | 9061 |
| 174 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +425 | 7760 |
| 175 | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | +408 | 19979 |
| 176 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +402 | 2909 |
| 177 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +388 | 2784 |
| 178 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +387 | 2622 |
| 179 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +376 | 25289 |
| 180 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +374 | 1941 |
| 181 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +368 | 1899 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +363 | 12039 |
| 183 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +359 | 2945 |
| 184 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +332 | 3517 |
| 185 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +328 | 23491 |
| 186 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +323 | 2701 |
| 187 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +315 | 3022 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +301 | 5327 |
| 189 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +277 | 3037 |
| 190 | [decolua/9router](https://github.com/decolua/9router) | +267 | 2614 |
| 191 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +267 | 6996 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +266 | 5853 |
| 193 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +263 | 4095 |
| 194 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +253 | 36103 |
| 195 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +244 | 11121 |
| 196 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +231 | 9411 |
| 197 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +227 | 6159 |
| 198 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +224 | 25824 |
| 199 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +218 | 2416 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +212 | 1320 |
| 201 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +210 | 6364 |
| 202 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +205 | 940 |
| 203 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +201 | 1067 |
| 204 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +199 | 1469 |
| 205 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +199 | 2710 |
| 206 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +195 | 15583 |
| 207 | [mswnlz/edu-knowlege](https://github.com/mswnlz/edu-knowlege) | +191 | 3562 |
| 208 | [usebruno/bruno](https://github.com/usebruno/bruno) | +190 | 41086 |
| 209 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +188 | 33712 |
| 210 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +187 | 2995 |
| 211 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +185 | 561 |
| 212 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +182 | 23670 |
| 213 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +176 | 2366 |
| 214 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +166 | 1780 |
| 215 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +159 | 784 |
| 216 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +153 | 3857 |
| 217 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +143 | 40265 |
| 218 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +142 | 1591 |
| 219 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +141 | 35473 |
| 220 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +140 | 1398 |
| 221 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +140 | 22151 |
| 222 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +138 | 943 |
| 223 | [dashersw/gea](https://github.com/dashersw/gea) | +137 | 961 |
| 224 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +129 | 960 |
| 225 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +127 | 837 |
| 226 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +122 | 817 |
| 227 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +116 | 5270 |
| 228 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +116 | 10770 |
| 229 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +115 | 1082 |
| 230 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +113 | 29597 |
| 231 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +110 | 23376 |
| 232 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +108 | 758 |
| 233 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +108 | 26583 |
| 234 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +107 | 1687 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +106 | 12749 |
| 236 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +105 | 779 |
| 237 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +105 | 1311 |
| 238 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +103 | 3715 |
| 239 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +103 | 1812 |
| 240 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +102 | 881 |
| 241 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +102 | 33000 |
| 242 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +101 | 570 |
| 243 | [clawplays/ospec](https://github.com/clawplays/ospec) | +99 | 536 |
| 244 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +98 | 48784 |
| 245 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 246 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +96 | 504 |
| 247 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1314 |
| 248 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +95 | 584 |
| 249 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +94 | 0 |
| 250 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +93 | 1153 |
| 251 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3961 |
| 252 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +91 | 2632 |
| 253 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +88 | 1912 |
| 254 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +88 | 551 |
| 255 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +87 | 588 |
| 256 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +87 | 2208 |
| 257 | [crimera/piko](https://github.com/crimera/piko) | +86 | 3230 |
| 258 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +85 | 583 |
| 259 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +84 | 3584 |
| 260 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +83 | 1104 |
| 261 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +83 | 784 |
| 262 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +82 | 1612 |
| 263 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +80 | 1026 |
| 264 | [meodai/heerich](https://github.com/meodai/heerich) | +80 | 485 |
| 265 | [microg/GmsCore](https://github.com/microg/GmsCore) | +80 | 12963 |
| 266 | [openmemind/memind](https://github.com/openmemind/memind) | +79 | 437 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +76 | 3720 |
| 268 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 1955 |
| 269 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +75 | 865 |
| 270 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +74 | 9291 |
| 271 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +74 | 45263 |
| 272 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +73 | 357 |
| 273 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +72 | 4043 |
| 274 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +71 | 600 |
| 275 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +71 | 7015 |
| 276 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +70 | 727 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +67 | 27272 |
| 278 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +66 | 461 |
| 279 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +65 | 1378 |
| 280 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +64 | 365 |
| 281 | [idinging/freemail](https://github.com/idinging/freemail) | +63 | 1365 |
| 282 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +63 | 11646 |
| 283 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +62 | 557 |
| 284 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +62 | 1699 |
| 285 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +61 | 7264 |
| 286 | [dgreenheck/webgpu-claude-skill](https://github.com/dgreenheck/webgpu-claude-skill) | +61 | 775 |
| 287 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +59 | 25422 |
| 288 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +58 | 305 |
| 289 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +57 | 31476 |
| 290 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +56 | 1603 |
| 291 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +55 | 37313 |
| 292 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +52 | 1798 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +48 | 1714 |
| 294 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +48 | 28947 |
| 295 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +47 | 11650 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +45 | 8517 |
| 297 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1682 |
| 298 | [is-a-dev/register](https://github.com/is-a-dev/register) | +37 | 10129 |
| 299 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +37 | 122 |
| 300 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +34 | 736 |
