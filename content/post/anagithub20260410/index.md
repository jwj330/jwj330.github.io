---
title: "2026-04-10 GitHub增长趋势报告"
description: "1.hermes-agent+1347 2.graphify+742 3.awesome-design-md+615 4.claude-code-best-practice+304 5.caveman+300"
date: 2026-04-10T20:40:22+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-10 20:40:22

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
        'daily': {"categories": ["siddharthvaddem/openscreen", "farion1231/cc-switch", "luongnv89/claude-howto", "farzaa/clicky", "jurplel/InstantSpaceSwitcher", "aloshdenny/reverse-SynthID", "rtk-ai/rtk", "webadderall/Recordly", "Yeachan-Heo/oh-my-codex", "OpenBMB/VoxCPM", "addyosmani/agent-skills", "opendataloader-project/opendataloader-pdf", "multica-ai/multica", "HKUDS/DeepTutor", "forrestchang/andrej-karpathy-skills", "JuliusBrussee/caveman", "shanraisshan/claude-code-best-practice", "VoltAgent/awesome-design-md", "safishamsi/graphify", "NousResearch/hermes-agent"], "data": [114, 122, 124, 132, 132, 140, 143, 144, 159, 171, 191, 229, 245, 245, 267, 300, 304, 615, 742, 1347]},
        'weekly': {"categories": ["Yeachan-Heo/oh-my-claudecode", "rtk-ai/rtk", "onyx-dot-app/onyx", "karpathy/autoresearch", "paperclipai/paperclip", "garrytan/gstack", "block/goose", "chenglou/pretext", "luongnv89/claude-howto", "msitarzewski/agency-agents", "Yeachan-Heo/oh-my-codex", "JuliusBrussee/caveman", "addyosmani/agent-skills", "obra/superpowers", "siddharthvaddem/openscreen", "safishamsi/graphify", "affaan-m/everything-claude-code", "NousResearch/hermes-agent", "ultraworkers/claw-code", "VoltAgent/awesome-design-md"], "data": [972, 986, 993, 1073, 1151, 1184, 1363, 1452, 1468, 1678, 1684, 1773, 2249, 2271, 2292, 3067, 3107, 4520, 5543, 7415]},
        'monthly': {"categories": ["siddharthvaddem/openscreen", "anomalyco/opencode", "gsd-build/get-shit-done", "anthropics/skills", "shareAI-lab/learn-claude-code", "bytedance/deer-flow", "HKUDS/CLI-Anything", "anthropics/claude-code", "paperclipai/paperclip", "chenglou/pretext", "666ghj/MiroFish", "NousResearch/hermes-agent", "VoltAgent/awesome-design-md", "karpathy/autoresearch", "msitarzewski/agency-agents", "openclaw/openclaw", "obra/superpowers", "garrytan/gstack", "affaan-m/everything-claude-code", "ultraworkers/claw-code"], "data": [3730, 3823, 3843, 4356, 4443, 4972, 5256, 5339, 6082, 6413, 7256, 7487, 8061, 8921, 10205, 11230, 11512, 11891, 13067, 23765]}
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
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1347 | 51468 |
| 2 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +742 | 20040 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +615 | 41373 |
| 4 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +304 | 35582 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +300 | 12224 |
| 6 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +267 | 11572 |
| 7 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +245 | 15862 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +245 | 5830 |
| 9 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +229 | 14692 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +191 | 11813 |
| 11 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +171 | 8632 |
| 12 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +159 | 20543 |
| 13 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +144 | 7392 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +143 | 22670 |
| 15 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +140 | 1715 |
| 16 | [jurplel/InstantSpaceSwitcher](https://github.com/jurplel/InstantSpaceSwitcher) | +132 | 1053 |
| 17 | [farzaa/clicky](https://github.com/farzaa/clicky) | +132 | 3538 |
| 18 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +124 | 24646 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +122 | 42412 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +114 | 27530 |
| 21 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +113 | 51331 |
| 22 | [coleam00/Archon](https://github.com/coleam00/Archon) | +111 | 15439 |
| 23 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +107 | 7208 |
| 24 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +100 | 27345 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +88 | 18188 |
| 26 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +88 | 11659 |
| 27 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +86 | 2440 |
| 28 | [chenglou/pretext](https://github.com/chenglou/pretext) | +84 | 42703 |
| 29 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +84 | 20388 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +81 | 30678 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +7415 | 41374 |
| 2 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +5543 | 180683 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4520 | 51468 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3107 | 51199 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3067 | 20040 |
| 6 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +2292 | 27530 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +2271 | 60312 |
| 8 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2249 | 11813 |
| 9 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1773 | 12225 |
| 10 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +1684 | 20543 |
| 11 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1678 | 77746 |
| 12 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1468 | 24646 |
| 13 | [chenglou/pretext](https://github.com/chenglou/pretext) | +1452 | 42703 |
| 14 | [block/goose](https://github.com/block/goose) | +1363 | 31098 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1184 | 69183 |
| 16 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1151 | 51223 |
| 17 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1073 | 70013 |
| 18 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +993 | 26391 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +986 | 22670 |
| 20 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +972 | 27345 |
| 21 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +960 | 26234 |
| 22 | [anthropics/skills](https://github.com/anthropics/skills) | +954 | 74774 |
| 23 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +912 | 53152 |
| 24 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +907 | 34148 |
| 25 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +892 | 20168 |
| 26 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +809 | 15862 |
| 27 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +800 | 4356 |
| 28 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +797 | 42412 |
| 29 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +760 | 51331 |
| 30 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +719 | 5590 |
| 31 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +710 | 35582 |
| 32 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +705 | 7705 |
| 33 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +675 | 6654 |
| 34 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +637 | 60218 |
| 35 | [jackwener/opencli](https://github.com/jackwener/opencli) | +632 | 14946 |
| 36 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +629 | 34158 |
| 37 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +629 | 22327 |
| 38 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +596 | 33878 |
| 39 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +595 | 8900 |
| 40 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +593 | 30590 |
| 41 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +586 | 50298 |
| 42 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +573 | 11573 |
| 43 | [multica-ai/multica](https://github.com/multica-ai/multica) | +569 | 5830 |
| 44 | [google-research/timesfm](https://github.com/google-research/timesfm) | +568 | 16246 |
| 45 | [tobi/qmd](https://github.com/tobi/qmd) | +565 | 20610 |
| 46 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +558 | 3953 |
| 47 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +549 | 37913 |
| 48 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +549 | 38303 |
| 49 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +524 | 14693 |
| 50 | [farzaa/clicky](https://github.com/farzaa/clicky) | +524 | 3538 |
| 51 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +513 | 20388 |
| 52 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +511 | 13396 |
| 53 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +485 | 4184 |
| 54 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +480 | 29926 |
| 55 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +479 | 10993 |
| 56 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +468 | 30678 |
| 57 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +460 | 24760 |
| 58 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +458 | 28531 |
| 59 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +440 | 2849 |
| 60 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +425 | 3301 |
| 61 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +416 | 9547 |
| 62 | [mattpocock/skills](https://github.com/mattpocock/skills) | +411 | 13807 |
| 63 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +403 | 2440 |
| 64 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +403 | 18188 |
| 65 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +402 | 16893 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +381 | 38965 |
| 67 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +376 | 32058 |
| 68 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +372 | 37330 |
| 69 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +371 | 7392 |
| 70 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +366 | 1670 |
| 71 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +365 | 8632 |
| 72 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +365 | 5614 |
| 73 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +365 | 47701 |
| 74 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +362 | 37902 |
| 75 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +361 | 4128 |
| 76 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) | +360 | 1698 |
| 77 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +343 | 31087 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +330 | 20143 |
| 79 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +328 | 16712 |
| 80 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +324 | 1951 |
| 81 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +322 | 1917 |
| 82 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +315 | 35165 |
| 83 | [maaslalani/sheets](https://github.com/maaslalani/sheets) | +313 | 1806 |
| 84 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +311 | 18203 |
| 85 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +306 | 4258 |
| 86 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +297 | 1328 |
| 87 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +293 | 5759 |
| 88 | [rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat) | +286 | 11659 |
| 89 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +284 | 45422 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +279 | 11556 |
| 91 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +271 | 20249 |
| 92 | [tw93/Waza](https://github.com/tw93/Waza) | +261 | 2201 |
| 93 | [hotcoffeeshake/tong-jincheng-skill](https://github.com/hotcoffeeshake/tong-jincheng-skill) | +257 | 1513 |
| 94 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +254 | 8837 |
| 95 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +252 | 10364 |
| 96 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +248 | 2215 |
| 97 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +247 | 2641 |
| 98 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +243 | 4919 |
| 99 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +241 | 14986 |
| 100 | [jundot/omlx](https://github.com/jundot/omlx) | +234 | 9394 |
| 101 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +231 | 29161 |
| 102 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +231 | 21965 |
| 103 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +231 | 32862 |
| 104 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +224 | 38954 |
| 105 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +221 | 24900 |
| 106 | [YishenTu/claudian](https://github.com/YishenTu/claudian) | +220 | 7208 |
| 107 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +220 | 1619 |
| 108 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +218 | 45886 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +208 | 9914 |
| 110 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +207 | 35778 |
| 111 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | +206 | 9285 |
| 112 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +206 | 1732 |
| 113 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +203 | 29084 |
| 114 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +200 | 10061 |
| 115 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +199 | 1960 |
| 116 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +193 | 1715 |
| 117 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +186 | 38073 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +184 | 39841 |
| 119 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +182 | 29254 |
| 120 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +176 | 2298 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +23765 | 180684 |
| 2 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13067 | 51199 |
| 3 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11891 | 69183 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +11512 | 60312 |
| 5 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +11230 | 224760 |
| 6 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +10205 | 77747 |
| 7 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +8921 | 70013 |
| 8 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +8061 | 41375 |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +7487 | 51468 |
| 10 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +7256 | 53152 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6413 | 42703 |
| 12 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +6082 | 51223 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5339 | 69674 |
| 14 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5256 | 29926 |
| 15 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +4972 | 60218 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4443 | 51331 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +4356 | 74774 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +3843 | 50300 |
| 19 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3823 | 109881 |
| 20 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3730 | 27530 |
| 21 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3697 | 34148 |
| 22 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3604 | 22687 |
| 23 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3542 | 35583 |
| 24 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3501 | 24646 |
| 25 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +3292 | 20543 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3082 | 21965 |
| 27 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +3067 | 20040 |
| 28 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2964 | 30590 |
| 29 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2937 | 28249 |
| 30 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2833 | 27345 |
| 31 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2830 | 18908 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2772 | 42412 |
| 33 | [tanweai/pua](https://github.com/tanweai/pua) | +2717 | 15792 |
| 34 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2711 | 85286 |
| 35 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +2670 | 16712 |
| 36 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2633 | 26234 |
| 37 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2571 | 22670 |
| 38 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2528 | 14946 |
| 39 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2510 | 14986 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2488 | 18188 |
| 41 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2363 | 29084 |
| 42 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2298 | 20388 |
| 43 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2298 | 18203 |
| 44 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2267 | 11813 |
| 45 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2243 | 47701 |
| 46 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2164 | 38303 |
| 47 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2159 | 30678 |
| 48 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2107 | 34158 |
| 49 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2103 | 46291 |
| 50 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +2071 | 14693 |
| 51 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2057 | 33878 |
| 52 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +2053 | 45422 |
| 53 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2032 | 13396 |
| 54 | [github/spec-kit](https://github.com/github/spec-kit) | +1940 | 71722 |
| 55 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1915 | 13807 |
| 56 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +1882 | 29161 |
| 57 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1816 | 20249 |
| 58 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1776 | 12228 |
| 59 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1719 | 37330 |
| 60 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1714 | 29572 |
| 61 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1709 | 24760 |
| 62 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1703 | 37902 |
| 63 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1685 | 10890 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1674 | 38965 |
| 65 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1667 | 31087 |
| 66 | [block/goose](https://github.com/block/goose) | +1657 | 31098 |
| 67 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1654 | 38073 |
| 68 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1647 | 26391 |
| 69 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +1635 | 12784 |
| 70 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1622 | 60117 |
| 71 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1581 | 32058 |
| 72 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1579 | 22327 |
| 73 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1507 | 16893 |
| 74 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1501 | 9890 |
| 75 | [openai/codex](https://github.com/openai/codex) | +1490 | 61744 |
| 76 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1483 | 79656 |
| 77 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1478 | 18986 |
| 78 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1473 | 13324 |
| 79 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1458 | 9547 |
| 80 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1437 | 13524 |
| 81 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1431 | 28531 |
| 82 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1426 | 9817 |
| 83 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1418 | 22361 |
| 84 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1386 | 11549 |
| 85 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1381 | 35165 |
| 86 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1380 | 8089 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1375 | 98536 |
| 88 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1340 | 38954 |
| 89 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1331 | 16581 |
| 90 | [cft0808/edict](https://github.com/cft0808/edict) | +1329 | 14856 |
| 91 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1325 | 8667 |
| 92 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1312 | 73135 |
| 93 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1307 | 6654 |
| 94 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1299 | 35778 |
| 95 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1288 | 7705 |
| 96 | [jundot/omlx](https://github.com/jundot/omlx) | +1281 | 9394 |
| 97 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1277 | 20143 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1255 | 11556 |
| 99 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1252 | 78902 |
| 100 | [webadderall/Recordly](https://github.com/webadderall/Recordly) | +1246 | 7392 |
| 101 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1242 | 8556 |
| 102 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1198 | 52700 |
| 103 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1110 | 5590 |
| 104 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1101 | 43973 |
| 105 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1097 | 16246 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1079 | 10364 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1060 | 6108 |
| 108 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1037 | 27053 |
| 109 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +1031 | 8837 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +976 | 9914 |
| 111 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +974 | 20168 |
| 112 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +908 | 8748 |
| 113 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +904 | 14993 |
| 114 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +895 | 5759 |
| 115 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +893 | 23800 |
| 116 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +882 | 9577 |
| 117 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +880 | 15863 |
| 118 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +863 | 49621 |
| 119 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +862 | 39841 |
| 120 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +815 | 6062 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +785 | 23359 |
| 122 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +768 | 10061 |
| 123 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +767 | 4665 |
| 124 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +765 | 4920 |
| 125 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +764 | 29254 |
| 126 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +755 | 29219 |
| 127 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +731 | 4233 |
| 128 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +727 | 4184 |
| 129 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +724 | 37564 |
| 130 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +715 | 4802 |
| 131 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +712 | 45886 |
| 132 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +707 | 5409 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +684 | 36799 |
| 134 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +677 | 32862 |
| 135 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +666 | 9413 |
| 136 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +649 | 24900 |
| 137 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +641 | 18038 |
| 138 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +640 | 8900 |
| 139 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +634 | 4705 |
| 140 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +630 | 3782 |
| 141 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +617 | 3358 |
| 142 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +604 | 47936 |
| 143 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +594 | 5783 |
| 144 | [eze-is/web-access](https://github.com/eze-is/web-access) | +584 | 4556 |
| 145 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +575 | 2851 |
| 146 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +570 | 18412 |
| 147 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +570 | 5043 |
| 148 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +568 | 2918 |
| 149 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +553 | 2849 |
| 150 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +536 | 15697 |
| 151 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +526 | 35735 |
| 152 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +518 | 47122 |
| 153 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +511 | 28905 |
| 154 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +503 | 2719 |
| 155 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +501 | 2263 |
| 156 | [floci-io/floci](https://github.com/floci-io/floci) | +501 | 3079 |
| 157 | [openai/skills](https://github.com/openai/skills) | +498 | 16542 |
| 158 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +496 | 7322 |
| 159 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +490 | 44545 |
| 160 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +485 | 8500 |
| 161 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +482 | 10993 |
| 162 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +468 | 2641 |
| 163 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +465 | 44232 |
| 164 | [htdt/godogen](https://github.com/htdt/godogen) | +463 | 2726 |
| 165 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +455 | 2807 |
| 166 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +452 | 18470 |
| 167 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +451 | 3712 |
| 168 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +445 | 4258 |
| 169 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +440 | 3093 |
| 170 | [wshobson/agents](https://github.com/wshobson/agents) | +439 | 33353 |
| 171 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +433 | 8576 |
| 172 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +429 | 2777 |
| 173 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +410 | 4304 |
| 174 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +388 | 24846 |
| 175 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +384 | 1670 |
| 176 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +383 | 11617 |
| 177 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +378 | 8632 |
| 178 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +378 | 2298 |
| 179 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +377 | 2740 |
| 180 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +375 | 2318 |
| 181 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +348 | 2539 |
| 182 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +326 | 1732 |
| 183 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +319 | 1575 |
| 184 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +317 | 5006 |
| 185 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +313 | 2993 |
| 186 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +306 | 1619 |
| 187 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +302 | 2294 |
| 188 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +301 | 1705 |
| 189 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +289 | 6775 |
| 190 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +286 | 2717 |
| 191 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +286 | 22926 |
| 192 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +283 | 10904 |
| 193 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +281 | 9643 |
| 194 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +262 | 1063 |
| 195 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +260 | 6185 |
| 196 | [Anil-matcha/Open-Higgsfield-AI](https://github.com/Anil-matcha/Open-Higgsfield-AI) | +257 | 4121 |
| 197 | [decolua/9router](https://github.com/decolua/9router) | +257 | 2224 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +241 | 5249 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +238 | 25493 |
| 200 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +232 | 23547 |
| 201 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +225 | 6233 |
| 202 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +218 | 13942 |
| 203 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +217 | 33712 |
| 204 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +214 | 15315 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +207 | 41086 |
| 206 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +206 | 36103 |
| 207 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +203 | 918 |
| 208 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +202 | 2155 |
| 209 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +191 | 2663 |
| 210 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +179 | 3686 |
| 211 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +177 | 1285 |
| 212 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +173 | 902 |
| 213 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +172 | 1779 |
| 214 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +171 | 1398 |
| 215 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +169 | 2863 |
| 216 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +157 | 940 |
| 217 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +153 | 21964 |
| 218 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +144 | 721 |
| 219 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +142 | 3749 |
| 220 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +140 | 1268 |
| 221 | [dashersw/gea](https://github.com/dashersw/gea) | +135 | 943 |
| 222 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +135 | 35473 |
| 223 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +134 | 29445 |
| 224 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +133 | 1232 |
| 225 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +132 | 2537 |
| 226 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +127 | 1081 |
| 227 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +126 | 804 |
| 228 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +126 | 538 |
| 229 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +124 | 10639 |
| 230 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +121 | 815 |
| 231 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +120 | 29458 |
| 232 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +120 | 40265 |
| 233 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +118 | 12646 |
| 234 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +118 | 23233 |
| 235 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +117 | 774 |
| 236 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +117 | 745 |
| 237 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +117 | 600 |
| 238 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +116 | 33000 |
| 239 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +109 | 1176 |
| 240 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +107 | 1060 |
| 241 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +107 | 0 |
| 242 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +107 | 491 |
| 243 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +106 | 26485 |
| 244 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +105 | 1432 |
| 245 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +104 | 840 |
| 246 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +104 | 48784 |
| 247 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 555 |
| 248 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +99 | 2104 |
| 249 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +98 | 1645 |
| 250 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +98 | 1658 |
| 251 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 373 |
| 252 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +95 | 1118 |
| 253 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +93 | 486 |
| 254 | [apify/agent-skills](https://github.com/apify/agent-skills) | +93 | 1882 |
| 255 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +93 | 1894 |
| 256 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +92 | 3861 |
| 257 | [idinging/freemail](https://github.com/idinging/freemail) | +89 | 1333 |
| 258 | [microg/GmsCore](https://github.com/microg/GmsCore) | +87 | 12883 |
| 259 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +86 | 1806 |
| 260 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +86 | 1522 |
| 261 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +86 | 3489 |
| 262 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +85 | 1003 |
| 263 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +82 | 474 |
| 264 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +82 | 915 |
| 265 | [AnnaSuSu/TechSpar](https://github.com/AnnaSuSu/TechSpar) | +82 | 522 |
| 266 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +81 | 1840 |
| 267 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3601 |
| 268 | [meodai/heerich](https://github.com/meodai/heerich) | +79 | 461 |
| 269 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +78 | 9169 |
| 270 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +77 | 515 |
| 271 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +76 | 728 |
| 272 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +75 | 2666 |
| 273 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +74 | 11544 |
| 274 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +74 | 27171 |
| 275 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +73 | 499 |
| 276 | [clawplays/ospec](https://github.com/clawplays/ospec) | +70 | 369 |
| 277 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +70 | 8475 |
| 278 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +68 | 45263 |
| 279 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +67 | 704 |
| 280 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +67 | 408 |
| 281 | [crimera/piko](https://github.com/crimera/piko) | +66 | 3106 |
| 282 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +65 | 531 |
| 283 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +64 | 294 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +63 | 7220 |
| 285 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +62 | 391 |
| 286 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +61 | 402 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1529 |
| 288 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +57 | 31476 |
| 289 | [CodePhiliaX/Chat2DB](https://github.com/CodePhiliaX/Chat2DB) | +56 | 25384 |
| 290 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +56 | 4650 |
| 291 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +55 | 282 |
| 292 | [jd-opensource/joyagent-jdgenie](https://github.com/jd-opensource/joyagent-jdgenie) | +55 | 11621 |
| 293 | [openmemind/memind](https://github.com/openmemind/memind) | +54 | 323 |
| 294 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +53 | 1652 |
| 295 | [apache/kafka](https://github.com/apache/kafka) | +53 | 32043 |
| 296 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +52 | 0 |
| 297 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +51 | 26683 |
| 298 | [risin42/NagramX](https://github.com/risin42/NagramX) | +47 | 1657 |
| 299 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +47 | 1699 |
| 300 | [xlrpa/FlowBot](https://github.com/xlrpa/FlowBot) | +46 | 1178 |
