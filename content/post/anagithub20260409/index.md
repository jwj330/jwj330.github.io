---
title: "2026-04-09 GitHub增长趋势报告"
description: "1.hermes-agent+1011 2.graphify+848 3.awesome-design-md+609 4.multica+240 5.DeepTutor+220"
date: 2026-04-09T20:54:28+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-09 20:54:28

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
        'daily': {"categories": ["shareAI-lab/learn-claude-code", "block/goose", "luongnv89/claude-howto", "farion1231/cc-switch", "Yeachan-Heo/oh-my-codex", "webadderall/Recordly", "opendataloader-project/opendataloader-pdf", "siddharthvaddem/openscreen", "farzaa/clicky", "addyosmani/agent-skills", "rowboatlabs/rowboat", "HughYau/qiushi-skill", "rtk-ai/rtk", "forrestchang/andrej-karpathy-skills", "JuliusBrussee/caveman", "HKUDS/DeepTutor", "multica-ai/multica", "VoltAgent/awesome-design-md", "safishamsi/graphify", "NousResearch/hermes-agent"], "data": [119, 129, 134, 137, 142, 148, 150, 151, 154, 155, 162, 173, 174, 207, 220, 220, 240, 609, 848, 1011]},
        'weekly': {"categories": ["karpathy/autoresearch", "paperclipai/paperclip", "garrytan/gstack", "onyx-dot-app/onyx", "ultraworkers/claw-code-parity", "block/goose", "JuliusBrussee/caveman", "luongnv89/claude-howto", "anthropics/claude-code", "msitarzewski/agency-agents", "addyosmani/agent-skills", "Yeachan-Heo/oh-my-codex", "chenglou/pretext", "obra/superpowers", "safishamsi/graphify", "siddharthvaddem/openscreen", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md", "ultraworkers/claw-code"], "data": [1102, 1259, 1285, 1292, 1298, 1373, 1478, 1516, 1537, 1652, 2064, 2119, 2168, 2261, 2374, 2722, 3289, 3468, 7258, 9292]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "anomalyco/opencode", "gsd-build/get-shit-done", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "anthropics/claude-code", "HKUDS/CLI-Anything", "paperclipai/paperclip", "NousResearch/hermes-agent", "chenglou/pretext", "VoltAgent/awesome-design-md", "666ghj/MiroFish", "karpathy/autoresearch", "msitarzewski/agency-agents", "obra/superpowers", "garrytan/gstack", "openclaw/openclaw", "affaan-m/everything-claude-code", "ultraworkers/claw-code"], "data": [3690, 3826, 3847, 4367, 4431, 5145, 5320, 5381, 6313, 6333, 6337, 7482, 7872, 9933, 11009, 11339, 11721, 12720, 13008, 23557]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1011 | 43802 |
| 2 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +848 | 17147 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +609 | 38091 |
| 4 | [multica-ai/multica](https://github.com/multica-ai/multica) | +240 | 4180 |
| 5 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +220 | 14665 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +220 | 8628 |
| 7 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +207 | 10272 |
| 8 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +174 | 21754 |
| 9 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +173 | 2126 |
| 10 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +162 | 11166 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +155 | 10352 |
| 12 | [farzaa/clicky](https://github.com/farzaa/clicky) | +154 | 3039 |
| 13 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +151 | 26864 |
| 14 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +150 | 13611 |
| 15 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +148 | 6760 |
| 16 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +142 | 19866 |
| 17 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +137 | 41810 |
| 18 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +134 | 23941 |
| 19 | [block/goose](https://github.com/block/goose) | +129 | 31098 |
| 20 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +119 | 50827 |
| 21 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +118 | 25817 |
| 22 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +110 | 3855 |
| 23 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +108 | 19884 |
| 24 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +107 | 7245 |
| 25 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +102 | 7566 |
| 26 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +99 | 26891 |
| 27 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +98 | 2435 |
| 28 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +88 | 49897 |
| 29 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +82 | 8724 |
| 30 | [chenglou/pretext](https://github.com/chenglou/pretext) | +80 | 42272 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +9292 | 179610 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +7258 | 38092 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +3468 | 43802 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3289 | 51199 |
| 5 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2722 | 26864 |
| 6 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2374 | 17148 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2261 | 60312 |
| 8 | [chenglou/pretext](https://github.com/chenglou/pretext) | +2168 | 42272 |
| 9 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2119 | 19866 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2064 | 10352 |
| 11 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1652 | 76803 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1537 | 69674 |
| 13 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1516 | 23941 |
| 14 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1478 | 8628 |
| 15 | [block/goose](https://github.com/block/goose) | +1373 | 31098 |
| 16 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1298 | 6648 |
| 17 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1292 | 26200 |
| 18 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1285 | 68283 |
| 19 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1259 | 50614 |
| 20 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1102 | 69396 |
| 21 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1092 | 26891 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +979 | 74774 |
| 23 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +927 | 52659 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +922 | 34148 |
| 25 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +914 | 25817 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +912 | 21754 |
| 27 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +888 | 73135 |
| 28 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +877 | 19885 |
| 29 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +824 | 4216 |
| 30 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +819 | 41810 |
| 31 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +792 | 5542 |
| 32 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +782 | 50827 |
| 33 | [jackwener/opencli](https://github.com/jackwener/opencli) | +782 | 14684 |
| 34 | [google-research/timesfm](https://github.com/google-research/timesfm) | +721 | 15941 |
| 35 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +710 | 13163 |
| 36 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +707 | 59901 |
| 37 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +684 | 33878 |
| 38 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +637 | 30590 |
| 39 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +633 | 7246 |
| 40 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +632 | 33722 |
| 41 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +625 | 22027 |
| 42 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +625 | 38008 |
| 43 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +598 | 49897 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +576 | 14665 |
| 45 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +569 | 29689 |
| 46 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +567 | 8724 |
| 47 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +565 | 4002 |
| 48 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +539 | 3846 |
| 49 | [tobi/qmd](https://github.com/tobi/qmd) | +538 | 20329 |
| 50 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +529 | 37805 |
| 51 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +522 | 20017 |
| 52 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +516 | 2681 |
| 53 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +508 | 34059 |
| 54 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +485 | 32872 |
| 55 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +476 | 28360 |
| 56 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +456 | 24437 |
| 57 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +451 | 30678 |
| 58 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +431 | 10839 |
| 59 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +428 | 9284 |
| 60 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +424 | 3178 |
| 61 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +421 | 5663 |
| 62 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +417 | 16679 |
| 63 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +404 | 37330 |
| 64 | [farzaa/clicky](https://github.com/farzaa/clicky) | +399 | 3039 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +388 | 4180 |
| 66 | [mattpocock/skills](https://github.com/mattpocock/skills) | +385 | 13456 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +385 | 38669 |
| 68 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +384 | 31843 |
| 69 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +384 | 4234 |
| 70 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +373 | 37699 |
| 71 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +366 | 1537 |
| 72 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +364 | 17765 |
| 73 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +355 | 47552 |
| 74 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +350 | 30917 |
| 75 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +347 | 17978 |
| 76 | [maaslalani/sheets](https://github.com/maaslalani/sheets) | +341 | 1745 |
| 77 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +336 | 5368 |
| 78 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) | +334 | 1554 |
| 79 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +328 | 34896 |
| 80 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +327 | 2126 |
| 81 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +322 | 10272 |
| 82 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +320 | 13611 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +320 | 19936 |
| 84 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +317 | 16577 |
| 85 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +316 | 2122 |
| 86 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +313 | 1866 |
| 87 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +309 | 3855 |
| 88 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +307 | 6760 |
| 89 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +303 | 45266 |
| 90 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +289 | 1292 |
| 91 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +289 | 4836 |
| 92 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +289 | 5361 |
| 93 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +280 | 1746 |
| 94 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +278 | 22558 |
| 95 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +278 | 1557 |
| 96 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +277 | 20078 |
| 97 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +272 | 32772 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +270 | 11292 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +269 | 10195 |
| 100 | [memvid/memvid](https://github.com/memvid/memvid) | +267 | 14771 |
| 101 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +258 | 8706 |
| 102 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +257 | 1932 |
| 103 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +256 | 1703 |
| 104 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +251 | 21837 |
| 105 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +238 | 2435 |
| 106 | [jundot/omlx](https://github.com/jundot/omlx) | +237 | 9278 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +232 | 24795 |
| 108 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +222 | 28900 |
| 109 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +222 | 6010 |
| 110 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +215 | 23750 |
| 111 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +211 | 38761 |
| 112 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | +210 | 9221 |
| 113 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +210 | 9864 |
| 114 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +203 | 45886 |
| 115 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +202 | 7566 |
| 116 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +202 | 9686 |
| 117 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +199 | 2773 |
| 118 | [Pika-Labs/Pika-Skills](https://github.com/Pika-Labs/Pika-Skills) | +197 | 952 |
| 119 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +195 | 28996 |
| 120 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +190 | 29116 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +23557 | 179610 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13008 | 51199 |
| 3 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +12720 | 224760 |
| 4 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11721 | 68284 |
| 5 | [obra/superpowers](https://github.com/obra/superpowers) | +11339 | 60312 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +11009 | 76803 |
| 7 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +9933 | 69396 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7872 | 52659 |
| 9 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +7482 | 38093 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6337 | 42272 |
| 11 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +6333 | 43802 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6313 | 50615 |
| 13 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5381 | 29689 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5320 | 69674 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5145 | 59901 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4431 | 50827 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +4367 | 74774 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3847 | 49897 |
| 19 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3826 | 109881 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3690 | 34148 |
| 21 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3629 | 26864 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3580 | 22558 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3387 | 23941 |
| 24 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3272 | 34059 |
| 25 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3150 | 19866 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3099 | 21837 |
| 27 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2935 | 30590 |
| 28 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2912 | 27999 |
| 29 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2814 | 18837 |
| 30 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2772 | 26891 |
| 31 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2760 | 16577 |
| 32 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2750 | 85286 |
| 33 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2744 | 41810 |
| 34 | [tanweai/pua](https://github.com/tanweai/pua) | +2720 | 15677 |
| 35 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2601 | 25817 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2571 | 17765 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2519 | 21754 |
| 38 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2478 | 14684 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2477 | 14768 |
| 40 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2377 | 46172 |
| 41 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2375 | 17148 |
| 42 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2341 | 28996 |
| 43 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2341 | 47552 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2277 | 17978 |
| 45 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +2228 | 45266 |
| 46 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2227 | 20017 |
| 47 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2131 | 30678 |
| 48 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2114 | 38008 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2105 | 33722 |
| 50 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2079 | 10352 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2056 | 33878 |
| 52 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1982 | 13163 |
| 53 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1963 | 12763 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1941 | 71722 |
| 55 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1896 | 28900 |
| 56 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1861 | 13456 |
| 57 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1851 | 13611 |
| 58 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1798 | 20078 |
| 59 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1755 | 29462 |
| 60 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1738 | 37330 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1710 | 24437 |
| 62 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1707 | 37699 |
| 63 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1667 | 31843 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1663 | 38669 |
| 65 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1661 | 10850 |
| 66 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1659 | 30917 |
| 67 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1639 | 60117 |
| 68 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1639 | 38030 |
| 69 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1628 | 26199 |
| 70 | [block/goose](https://github.com/block/goose) | +1603 | 31098 |
| 71 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1559 | 22027 |
| 72 | [jundot/omlx](https://github.com/jundot/omlx) | +1538 | 9278 |
| 73 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1535 | 16679 |
| 74 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1503 | 22173 |
| 75 | [cft0808/edict](https://github.com/cft0808/edict) | +1498 | 14792 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1491 | 61744 |
| 77 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1487 | 18922 |
| 78 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1485 | 9764 |
| 79 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1480 | 8628 |
| 80 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1473 | 79656 |
| 81 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1462 | 28360 |
| 82 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1457 | 13241 |
| 83 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1432 | 13358 |
| 84 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1431 | 9284 |
| 85 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1413 | 9771 |
| 86 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1412 | 38761 |
| 87 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1394 | 34896 |
| 88 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1388 | 35260 |
| 89 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1382 | 11525 |
| 90 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1370 | 8040 |
| 91 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1356 | 98536 |
| 92 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1330 | 16467 |
| 93 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1321 | 8635 |
| 94 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1315 | 73135 |
| 95 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1304 | 6648 |
| 96 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1292 | 19936 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1289 | 11292 |
| 98 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1243 | 78902 |
| 99 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1235 | 8496 |
| 100 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1222 | 43973 |
| 101 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1212 | 7246 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1189 | 10195 |
| 103 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1158 | 52700 |
| 104 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1110 | 26982 |
| 105 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1095 | 5542 |
| 106 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1095 | 9558 |
| 107 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1051 | 15941 |
| 108 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1051 | 5986 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1039 | 9686 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +1009 | 8706 |
| 111 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +957 | 14923 |
| 112 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +899 | 8701 |
| 113 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +892 | 23750 |
| 114 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +889 | 5663 |
| 115 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +850 | 49621 |
| 116 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +838 | 39841 |
| 117 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +796 | 6010 |
| 118 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +784 | 23248 |
| 119 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +760 | 29116 |
| 120 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +756 | 4632 |
| 121 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +756 | 29187 |
| 122 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +753 | 4836 |
| 123 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +752 | 9864 |
| 124 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +740 | 37564 |
| 125 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +732 | 45886 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +726 | 4189 |
| 127 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +719 | 4776 |
| 128 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +700 | 5361 |
| 129 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +695 | 4002 |
| 130 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +686 | 36799 |
| 131 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +677 | 3764 |
| 132 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +675 | 32772 |
| 133 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +668 | 35735 |
| 134 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +662 | 17822 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +656 | 9361 |
| 136 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +656 | 4945 |
| 137 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +651 | 24795 |
| 138 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +640 | 14665 |
| 139 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +640 | 3463 |
| 140 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +624 | 8724 |
| 141 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +623 | 4608 |
| 142 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +593 | 47936 |
| 143 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +593 | 18322 |
| 144 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +588 | 5757 |
| 145 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +574 | 2836 |
| 146 | [eze-is/web-access](https://github.com/eze-is/web-access) | +566 | 4466 |
| 147 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +551 | 2855 |
| 148 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +543 | 15586 |
| 149 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +523 | 2681 |
| 150 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +515 | 47122 |
| 151 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +513 | 28814 |
| 152 | [openai/skills](https://github.com/openai/skills) | +504 | 16474 |
| 153 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +499 | 7271 |
| 154 | [floci-io/floci](https://github.com/floci-io/floci) | +498 | 3041 |
| 155 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +492 | 44545 |
| 156 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +491 | 2874 |
| 157 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +479 | 8469 |
| 158 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +478 | 2344 |
| 159 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +472 | 44232 |
| 160 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +458 | 18397 |
| 161 | [htdt/godogen](https://github.com/htdt/godogen) | +458 | 2699 |
| 162 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +451 | 2773 |
| 163 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +448 | 3696 |
| 164 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +442 | 8032 |
| 165 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +441 | 4234 |
| 166 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +439 | 3066 |
| 167 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +438 | 10839 |
| 168 | [wshobson/agents](https://github.com/wshobson/agents) | +438 | 33267 |
| 169 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +435 | 8530 |
| 170 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +426 | 2400 |
| 171 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +425 | 2738 |
| 172 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +420 | 2435 |
| 173 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +400 | 4195 |
| 174 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +399 | 24788 |
| 175 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +378 | 11556 |
| 176 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +374 | 2736 |
| 177 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +372 | 2300 |
| 178 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +368 | 1537 |
| 179 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +346 | 2093 |
| 180 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +342 | 2511 |
| 181 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +324 | 1703 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +317 | 4956 |
| 183 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +311 | 2279 |
| 184 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +309 | 2981 |
| 185 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +306 | 1688 |
| 186 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +305 | 1501 |
| 187 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +290 | 2613 |
| 188 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +289 | 6753 |
| 189 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +284 | 10859 |
| 190 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +281 | 10347 |
| 191 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +273 | 22817 |
| 192 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +267 | 1282 |
| 193 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +256 | 6816 |
| 194 | [decolua/9router](https://github.com/decolua/9router) | +246 | 2148 |
| 195 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +242 | 5220 |
| 196 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +241 | 25461 |
| 197 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +235 | 6207 |
| 198 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +233 | 23524 |
| 199 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +222 | 33712 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +219 | 13915 |
| 201 | [usebruno/bruno](https://github.com/usebruno/bruno) | +217 | 41086 |
| 202 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +215 | 3676 |
| 203 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +213 | 15241 |
| 204 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +211 | 3917 |
| 205 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +208 | 2125 |
| 206 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +205 | 36103 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +204 | 914 |
| 208 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +190 | 2659 |
| 209 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +171 | 896 |
| 210 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +170 | 1378 |
| 211 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +162 | 2834 |
| 212 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +155 | 21945 |
| 213 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +150 | 915 |
| 214 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +144 | 3732 |
| 215 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +138 | 1063 |
| 216 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +136 | 1248 |
| 217 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +135 | 704 |
| 218 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +135 | 1209 |
| 219 | [dashersw/gea](https://github.com/dashersw/gea) | +134 | 933 |
| 220 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +133 | 29401 |
| 221 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +132 | 2519 |
| 222 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +132 | 35473 |
| 223 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +126 | 800 |
| 224 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +126 | 533 |
| 225 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +123 | 10626 |
| 226 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +119 | 40265 |
| 227 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +118 | 23218 |
| 228 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +117 | 600 |
| 229 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +116 | 769 |
| 230 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +116 | 2499 |
| 231 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +114 | 790 |
| 232 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +114 | 5557 |
| 233 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +114 | 1394 |
| 234 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +113 | 733 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +112 | 12630 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +112 | 33000 |
| 237 | [apify/agent-skills](https://github.com/apify/agent-skills) | +108 | 1878 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +108 | 26459 |
| 239 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +107 | 1056 |
| 240 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 241 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +107 | 488 |
| 242 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +106 | 48784 |
| 243 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +104 | 1385 |
| 244 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +102 | 827 |
| 245 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +101 | 1156 |
| 246 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 553 |
| 247 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +99 | 2095 |
| 248 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 443 |
| 249 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +96 | 1118 |
| 250 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +95 | 1888 |
| 251 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +94 | 903 |
| 252 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +93 | 3853 |
| 253 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +93 | 486 |
| 254 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +92 | 1628 |
| 255 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +92 | 1642 |
| 256 | [idinging/freemail](https://github.com/idinging/freemail) | +89 | 1329 |
| 257 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +88 | 1795 |
| 258 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +88 | 1507 |
| 259 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +88 | 3477 |
| 260 | [microg/GmsCore](https://github.com/microg/GmsCore) | +86 | 12873 |
| 261 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +85 | 987 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +82 | 3585 |
| 263 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +82 | 520 |
| 264 | [meodai/heerich](https://github.com/meodai/heerich) | +79 | 456 |
| 265 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +79 | 427 |
| 266 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +78 | 458 |
| 267 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +77 | 509 |
| 268 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +76 | 727 |
| 269 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +75 | 1816 |
| 270 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +75 | 9152 |
| 271 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +75 | 11530 |
| 272 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +74 | 27171 |
| 273 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +73 | 2657 |
| 274 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +70 | 499 |
| 275 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +69 | 8466 |
| 276 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +68 | 531 |
| 277 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +67 | 405 |
| 278 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +65 | 699 |
| 279 | [clawplays/ospec](https://github.com/clawplays/ospec) | +64 | 343 |
| 280 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +64 | 45263 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +63 | 7211 |
| 282 | [crimera/piko](https://github.com/crimera/piko) | +63 | 3091 |
| 283 | [apache/kafka](https://github.com/apache/kafka) | +63 | 32043 |
| 284 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +62 | 280 |
| 285 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +61 | 388 |
| 286 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +60 | 396 |
| 287 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +60 | 37313 |
| 288 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +59 | 4648 |
| 289 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +57 | 1516 |
| 290 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +57 | 0 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +56 | 31476 |
| 292 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +55 | 273 |
| 293 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11623 |
| 294 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +52 | 1643 |
| 295 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +52 | 353 |
| 296 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +52 | 436 |
| 297 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +51 | 26675 |
| 298 | [openmemind/memind](https://github.com/openmemind/memind) | +50 | 298 |
| 299 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +49 | 25392 |
| 300 | [risin42/NagramX](https://github.com/risin42/NagramX) | +47 | 1653 |
