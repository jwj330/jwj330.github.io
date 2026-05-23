---
title: "2026-05-23 GitHub增长趋势报告"
description: "1.codegraph+334 2.Understand-Anything+271 3.claude-plugins-official+263 4.ai-engineering-from-scratch+215 5.graphify+102"
date: 2026-05-23T20:55:16+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-23 20:55:16

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
        'daily': {"categories": ["jamiepine/voicebox", "OpenSenseNova/SenseNova-U1", "rohitg00/agentmemory", "ChromeDevTools/chrome-devtools-mcp", "multica-ai/multica", "thananon/9arm-skills", "walkinglabs/learn-harness-engineering", "Hmbown/DeepSeek-TUI", "can1357/oh-my-pi", "tashfeenahmed/freellmapi", "simplifaisoul/osiris", "Alishahryar1/free-claude-code", "Fincept-Corporation/FinceptTerminal", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman", "safishamsi/graphify", "rohitg00/ai-engineering-from-scratch", "anthropics/claude-plugins-official", "Lum1104/Understand-Anything", "colbymchenry/codegraph"], "data": [43, 43, 47, 48, 49, 50, 50, 52, 55, 57, 61, 68, 73, 76, 83, 102, 215, 263, 271, 334]},
        'weekly': {"categories": ["decolua/9router", "vercel-labs/zero", "anthropics/financial-services", "Anil-matcha/Open-Generative-AI", "Yuan1z0825/nature-skills", "HKUDS/CLI-Anything", "truelockmc/streambert", "supertone-inc/supertonic", "Hmbown/DeepSeek-TUI", "rmyndharis/OpenWA", "rohitg00/ai-engineering-from-scratch", "Lum1104/Understand-Anything", "rohitg00/agentmemory", "anthropics/claude-plugins-official", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman", "mattpocock/skills", "colbymchenry/codegraph", "forrestchang/andrej-karpathy-skills"], "data": [266, 278, 281, 287, 289, 292, 309, 322, 326, 336, 411, 454, 516, 518, 550, 795, 1145, 1162, 1221, 1373]},
        'monthly': {"categories": ["tinyhumansai/openhuman", "JuliusBrussee/caveman", "msitarzewski/agency-agents", "rtk-ai/rtk", "safishamsi/graphify", "VoltAgent/awesome-design-md", "Z4nzu/hackingtool", "garrytan/gstack", "addyosmani/agent-skills", "ruvnet/ruflo", "affaan-m/ECC", "farion1231/cc-switch", "warpdotdev/warp", "Alishahryar1/free-claude-code", "TauricResearch/TradingAgents", "Hmbown/DeepSeek-TUI", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1923, 1983, 2039, 2050, 2128, 2185, 2214, 2236, 2528, 2639, 2828, 3066, 3167, 3196, 3247, 3276, 3950, 5688, 8358, 8786]}
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
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +334 | 19152 |
| 2 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +271 | 21125 |
| 3 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +263 | 26313 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +215 | 13568 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +102 | 52420 |
| 6 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +83 | 26266 |
| 7 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +76 | 19624 |
| 8 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +73 | 23073 |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +68 | 28537 |
| 10 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +61 | 2487 |
| 11 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +57 | 4479 |
| 12 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +55 | 6717 |
| 13 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +52 | 33840 |
| 14 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +50 | 6188 |
| 15 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +50 | 1847 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +49 | 31850 |
| 17 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +48 | 41290 |
| 18 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +47 | 16783 |
| 19 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +43 | 2279 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +43 | 27889 |
| 21 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +43 | 797 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +42 | 10912 |
| 23 | [withcoral/coral](https://github.com/withcoral/coral) | +41 | 4278 |
| 24 | [decolua/9router](https://github.com/decolua/9router) | +37 | 13770 |
| 25 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +36 | 9751 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +36 | 53186 |
| 27 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +35 | 2040 |
| 28 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +34 | 45129 |
| 29 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +33 | 472 |
| 30 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +32 | 27008 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1373 | 149398 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1221 | 19153 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1162 | 102249 |
| 4 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1145 | 26266 |
| 5 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +795 | 19624 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +550 | 19464 |
| 7 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +518 | 26313 |
| 8 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +516 | 16783 |
| 9 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +454 | 21125 |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +411 | 13568 |
| 11 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +336 | 5893 |
| 12 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +326 | 33840 |
| 13 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +322 | 9751 |
| 14 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +309 | 4544 |
| 15 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +292 | 39799 |
| 16 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +289 | 10912 |
| 17 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +287 | 16714 |
| 18 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +281 | 27008 |
| 19 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +278 | 4400 |
| 20 | [decolua/9router](https://github.com/decolua/9router) | +266 | 13770 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +265 | 53186 |
| 22 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +260 | 52421 |
| 23 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +253 | 25339 |
| 24 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +237 | 14215 |
| 25 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +232 | 28537 |
| 26 | [withcoral/coral](https://github.com/withcoral/coral) | +232 | 4278 |
| 27 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +221 | 45129 |
| 28 | [multica-ai/multica](https://github.com/multica-ai/multica) | +208 | 31850 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +207 | 4479 |
| 30 | [MinishLab/semble](https://github.com/MinishLab/semble) | +205 | 3911 |
| 31 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +203 | 7530 |
| 32 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +190 | 18460 |
| 33 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +189 | 6943 |
| 34 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +188 | 3892 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +187 | 20140 |
| 36 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +180 | 8717 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +178 | 52633 |
| 38 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +177 | 7384 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +176 | 38589 |
| 40 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +174 | 16139 |
| 41 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +173 | 19343 |
| 42 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +169 | 2487 |
| 43 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +167 | 4526 |
| 44 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +165 | 20686 |
| 45 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +163 | 27889 |
| 46 | [compozy/compozy](https://github.com/compozy/compozy) | +161 | 2145 |
| 47 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +155 | 6717 |
| 48 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +152 | 4028 |
| 49 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +152 | 40326 |
| 50 | [santifer/career-ops](https://github.com/santifer/career-ops) | +146 | 46863 |
| 51 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +144 | 50247 |
| 52 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +144 | 1630 |
| 53 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +142 | 1847 |
| 54 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +140 | 23073 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +139 | 23013 |
| 56 | [floci-io/floci](https://github.com/floci-io/floci) | +138 | 12900 |
| 57 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +138 | 4016 |
| 58 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +137 | 11528 |
| 59 | [antirez/ds4](https://github.com/antirez/ds4) | +136 | 11548 |
| 60 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +134 | 2040 |
| 61 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +134 | 2608 |
| 62 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +134 | 10724 |
| 63 | [Achilng/floral-notepaper](https://github.com/Achilng/floral-notepaper) | +128 | 2147 |
| 64 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +124 | 4681 |
| 65 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +122 | 6188 |
| 66 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +121 | 22408 |
| 67 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +118 | 1813 |
| 68 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +116 | 41290 |
| 69 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +115 | 2582 |
| 70 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +115 | 2204 |
| 71 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +113 | 43570 |
| 72 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +113 | 4398 |
| 73 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +112 | 39887 |
| 74 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +112 | 912 |
| 75 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +111 | 62185 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +111 | 25032 |
| 77 | [larksuite/cli](https://github.com/larksuite/cli) | +111 | 12448 |
| 78 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +109 | 35054 |
| 79 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +106 | 54557 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +105 | 20617 |
| 81 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +104 | 18778 |
| 82 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +104 | 29735 |
| 83 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +103 | 14792 |
| 84 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +103 | 12702 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +100 | 34404 |
| 86 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +99 | 4442 |
| 87 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +99 | 20920 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +98 | 30187 |
| 89 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +98 | 11239 |
| 90 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +95 | 6594 |
| 91 | [soxoj/maigret](https://github.com/soxoj/maigret) | +93 | 30039 |
| 92 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +89 | 18545 |
| 93 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +87 | 18659 |
| 94 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +84 | 8971 |
| 95 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +84 | 1649 |
| 96 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +80 | 1971 |
| 97 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +79 | 8395 |
| 98 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +78 | 4561 |
| 99 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | +74 | 5863 |
| 100 | [openai/skills](https://github.com/openai/skills) | +73 | 20059 |
| 101 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +73 | 16003 |
| 102 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +72 | 8408 |
| 103 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +71 | 10453 |
| 104 | [dotnet/skills](https://github.com/dotnet/skills) | +70 | 2721 |
| 105 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +68 | 2279 |
| 106 | [88lin/video_vip](https://github.com/88lin/video_vip) | +67 | 2651 |
| 107 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +67 | 2217 |
| 108 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +67 | 44614 |
| 109 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +66 | 15400 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +65 | 14310 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +64 | 6323 |
| 112 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +59 | 1565 |
| 113 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +58 | 19651 |
| 114 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +58 | 11559 |
| 115 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +58 | 33946 |
| 116 | [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | +56 | 921 |
| 117 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +55 | 4057 |
| 118 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +52 | 25629 |
| 119 | [jundot/omlx](https://github.com/jundot/omlx) | +52 | 14985 |
| 120 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +51 | 1407 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8786 | 102249 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8358 | 149400 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5688 | 164301 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3950 | 60312 |
| 5 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3276 | 33840 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3247 | 30590 |
| 7 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3196 | 28537 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3167 | 59721 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3066 | 78944 |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2828 | 51199 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2639 | 54434 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2528 | 45129 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2236 | 101222 |
| 14 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2214 | 55070 |
| 15 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2185 | 83036 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2128 | 52421 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2050 | 53186 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2039 | 104493 |
| 19 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1983 | 64013 |
| 20 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1923 | 26266 |
| 21 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1902 | 27008 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1830 | 109881 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1757 | 53645 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +1724 | 74774 |
| 25 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1597 | 15400 |
| 26 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1582 | 11363 |
| 27 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1573 | 19464 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1571 | 53354 |
| 29 | [github/spec-kit](https://github.com/github/spec-kit) | +1501 | 71722 |
| 30 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1481 | 19343 |
| 31 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1421 | 39887 |
| 32 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1368 | 19153 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1367 | 52633 |
| 34 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1363 | 30678 |
| 35 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1357 | 30039 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1305 | 34148 |
| 37 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1299 | 64651 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1297 | 20140 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1295 | 85286 |
| 40 | [antirez/ds4](https://github.com/antirez/ds4) | +1287 | 11548 |
| 41 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1277 | 16714 |
| 42 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1268 | 16783 |
| 43 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1267 | 19624 |
| 44 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1248 | 11528 |
| 45 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1220 | 21125 |
| 46 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1220 | 31850 |
| 47 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1217 | 23073 |
| 48 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1205 | 20686 |
| 49 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1171 | 14754 |
| 50 | [decolua/9router](https://github.com/decolua/9router) | +1120 | 13770 |
| 51 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1093 | 11239 |
| 52 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1025 | 67286 |
| 53 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +974 | 13564 |
| 54 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +965 | 10912 |
| 55 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +960 | 14215 |
| 56 | [santifer/career-ops](https://github.com/santifer/career-ops) | +924 | 46863 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +910 | 23013 |
| 58 | [openai/symphony](https://github.com/openai/symphony) | +910 | 24478 |
| 59 | [openai/codex](https://github.com/openai/codex) | +858 | 61744 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +826 | 18460 |
| 61 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +823 | 13569 |
| 62 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +819 | 54557 |
| 63 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +819 | 29735 |
| 64 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +808 | 63639 |
| 65 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +803 | 82920 |
| 66 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +793 | 47382 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +788 | 30187 |
| 68 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +784 | 38589 |
| 69 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +770 | 18778 |
| 70 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +762 | 8408 |
| 71 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +761 | 50247 |
| 72 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +744 | 6484 |
| 73 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +734 | 26313 |
| 74 | [floci-io/floci](https://github.com/floci-io/floci) | +733 | 12900 |
| 75 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +724 | 12011 |
| 76 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +721 | 35054 |
| 77 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +720 | 15482 |
| 78 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +706 | 51085 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +701 | 20920 |
| 80 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +693 | 6053 |
| 81 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +687 | 32626 |
| 82 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +663 | 62185 |
| 83 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +656 | 8971 |
| 84 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +653 | 37330 |
| 85 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +649 | 7530 |
| 86 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +646 | 34404 |
| 87 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +638 | 16139 |
| 88 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +638 | 33878 |
| 89 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +630 | 35045 |
| 90 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +629 | 22408 |
| 91 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +625 | 5749 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +616 | 39799 |
| 93 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +616 | 61759 |
| 94 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +603 | 33946 |
| 95 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +602 | 9751 |
| 96 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +601 | 11559 |
| 97 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +580 | 25629 |
| 98 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +568 | 25339 |
| 99 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +561 | 6594 |
| 100 | [browser-use/video-use](https://github.com/browser-use/video-use) | +551 | 8280 |
| 101 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +544 | 4681 |
| 102 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +537 | 4161 |
| 103 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +525 | 17252 |
| 104 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +502 | 18545 |
| 105 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +499 | 8395 |
| 106 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +487 | 13330 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +483 | 19651 |
| 108 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +477 | 24234 |
| 109 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +459 | 44614 |
| 110 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +458 | 32032 |
| 111 | [jundot/omlx](https://github.com/jundot/omlx) | +453 | 14985 |
| 112 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +435 | 6323 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +425 | 14310 |
| 114 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +421 | 19472 |
| 115 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +420 | 4442 |
| 116 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +407 | 38474 |
| 117 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +379 | 7925 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +378 | 16004 |
| 119 | [browserbase/skills](https://github.com/browserbase/skills) | +376 | 3409 |
| 120 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +375 | 2753 |
| 121 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +360 | 9996 |
| 122 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +354 | 3671 |
| 123 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +350 | 5725 |
| 124 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +350 | 5657 |
| 125 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +346 | 36799 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +342 | 14792 |
| 127 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +334 | 27505 |
| 128 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +332 | 21515 |
| 129 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +328 | 23519 |
| 130 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +327 | 26396 |
| 131 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +323 | 5167 |
| 132 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +321 | 1676 |
| 133 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +313 | 4526 |
| 134 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +312 | 4544 |
| 135 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +312 | 3928 |
| 136 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +310 | 6943 |
| 137 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +308 | 9617 |
| 138 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +307 | 20554 |
| 139 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +305 | 7032 |
| 140 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +305 | 2620 |
| 141 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +302 | 21934 |
| 142 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +301 | 32771 |
| 143 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +300 | 4561 |
| 144 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +300 | 2297 |
| 145 | [MinishLab/semble](https://github.com/MinishLab/semble) | +295 | 3911 |
| 146 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +295 | 2356 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +295 | 4745 |
| 148 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +294 | 4028 |
| 149 | [openai/skills](https://github.com/openai/skills) | +294 | 20059 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +293 | 33697 |
| 151 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +290 | 10453 |
| 152 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +287 | 22102 |
| 153 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +285 | 32925 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +284 | 27202 |
| 155 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +284 | 4057 |
| 156 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +284 | 6673 |
| 157 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +284 | 1854 |
| 158 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +284 | 2311 |
| 159 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +275 | 2578 |
| 160 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +271 | 13604 |
| 161 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +268 | 43043 |
| 162 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +264 | 25851 |
| 163 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +263 | 2962 |
| 164 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +260 | 5400 |
| 165 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +251 | 2279 |
| 166 | [z-lab/dflash](https://github.com/z-lab/dflash) | +251 | 4697 |
| 167 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +248 | 2485 |
| 168 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +244 | 39841 |
| 169 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +242 | 4247 |
| 170 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +238 | 28173 |
| 171 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +234 | 37564 |
| 172 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +232 | 2217 |
| 173 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +232 | 20139 |
| 174 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +232 | 1946 |
| 175 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +230 | 18393 |
| 176 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +230 | 3723 |
| 177 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +222 | 12979 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +217 | 6456 |
| 179 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +213 | 7384 |
| 180 | [tiagozip/cap](https://github.com/tiagozip/cap) | +213 | 6438 |
| 181 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +212 | 4322 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +205 | 7197 |
| 183 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +194 | 2582 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +193 | 14390 |
| 185 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +186 | 1630 |
| 186 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +167 | 3693 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +166 | 5164 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +165 | 27008 |
| 189 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +160 | 6150 |
| 190 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +155 | 4699 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +142 | 36103 |
| 192 | [playcanvas/engine](https://github.com/playcanvas/engine) | +138 | 15874 |
| 193 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +135 | 2039 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +131 | 16999 |
| 195 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +126 | 2863 |
| 196 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +126 | 10447 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +125 | 15273 |
| 198 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +125 | 0 |
| 199 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +123 | 7542 |
| 200 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +120 | 1565 |
| 201 | [usebruno/bruno](https://github.com/usebruno/bruno) | +118 | 41086 |
| 202 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +116 | 9984 |
| 203 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +115 | 39596 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +114 | 23155 |
| 205 | [sandeco/reversa](https://github.com/sandeco/reversa) | +112 | 959 |
| 206 | [eze-is/web-access](https://github.com/eze-is/web-access) | +109 | 6748 |
| 207 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 837 |
| 208 | [88lin/video_vip](https://github.com/88lin/video_vip) | +103 | 2651 |
| 209 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +102 | 1327 |
| 210 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +97 | 3109 |
| 211 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +97 | 2017 |
| 212 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +96 | 0 |
| 213 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +90 | 24177 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +89 | 40265 |
| 215 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +88 | 731 |
| 216 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +88 | 4502 |
| 217 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +84 | 10406 |
| 218 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +83 | 1615 |
| 219 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +82 | 14840 |
| 220 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +81 | 8000 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +80 | 35473 |
| 222 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +79 | 11732 |
| 223 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +77 | 9991 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +68 | 11863 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +68 | 3936 |
| 226 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2445 |
| 227 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +63 | 3231 |
| 228 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +62 | 37313 |
| 229 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 230 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +60 | 949 |
| 231 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +60 | 30184 |
| 232 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +59 | 13392 |
| 233 | [halo-dev/halo](https://github.com/halo-dev/halo) | +59 | 37991 |
| 234 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +58 | 8436 |
| 235 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +56 | 45263 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +55 | 33000 |
| 237 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +54 | 441 |
| 238 | [robinebers/openusage](https://github.com/robinebers/openusage) | +52 | 2557 |
| 239 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +52 | 988 |
| 240 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 303 |
| 241 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +51 | 519 |
| 242 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 304 |
| 243 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +50 | 2543 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +49 | 3239 |
| 245 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +49 | 344 |
| 246 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +49 | 11250 |
| 247 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 477 |
| 248 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +48 | 983 |
| 249 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +48 | 2303 |
| 250 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +48 | 2204 |
| 251 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +47 | 844 |
| 252 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +46 | 591 |
| 253 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +45 | 1831 |
| 254 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +44 | 4176 |
| 255 | [cursor/plugins](https://github.com/cursor/plugins) | +43 | 665 |
| 256 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 332 |
| 257 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +42 | 1503 |
| 258 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 331 |
| 259 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +42 | 2190 |
| 260 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +41 | 1791 |
| 261 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +41 | 723 |
| 262 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +40 | 1410 |
| 263 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +40 | 924 |
| 264 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +40 | 498 |
| 265 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +39 | 2247 |
| 266 | [openmemind/memind](https://github.com/openmemind/memind) | +39 | 816 |
| 267 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +38 | 1366 |
| 268 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +37 | 5158 |
| 269 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +37 | 639 |
| 270 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +37 | 431 |
| 271 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +37 | 1958 |
| 272 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +35 | 890 |
| 273 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1435 |
| 274 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +34 | 322 |
| 275 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +34 | 9710 |
| 276 | [intave/intave](https://github.com/intave/intave) | +32 | 259 |
| 277 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +31 | 754 |
| 278 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +30 | 365 |
| 279 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +30 | 500 |
| 280 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +27 | 2409 |
| 282 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +27 | 246 |
| 283 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2218 |
| 284 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +26 | 226 |
| 285 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 293 |
| 286 | [is-a-dev/register](https://github.com/is-a-dev/register) | +24 | 10331 |
| 287 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +24 | 0 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +24 | 1548 |
| 289 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +23 | 2634 |
| 290 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +23 | 228 |
| 291 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +22 | 2949 |
| 292 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 293 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +21 | 329 |
| 294 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +20 | 343 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +18 | 3233 |
| 296 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +18 | 243 |
| 297 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +18 | 450 |
| 298 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +18 | 862 |
| 299 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +15 | 159 |
| 300 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +15 | 1949 |
