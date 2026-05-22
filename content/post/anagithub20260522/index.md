---
title: "2026-05-22 GitHub增长趋势报告"
description: "1.codegraph+249 2.claude-plugins-official+153 3.Understand-Anything+104 4.openhuman+78 5.streambert+69"
date: 2026-05-22T21:13:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-22 21:13:00

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
        'daily': {"categories": ["Yuan1z0825/nature-skills", "ChromeDevTools/chrome-devtools-mcp", "chengzuopeng/stock-sdk", "tashfeenahmed/freellmapi", "HKUDS/CLI-Anything", "88lin/video_vip", "CloakHQ/CloakBrowser", "Alishahryar1/free-claude-code", "safishamsi/graphify", "wiltodelta/remove-ai-watermarks", "rohitg00/agentmemory", "RyanCodrai/turbovec", "multica-ai/multica", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "truelockmc/streambert", "tinyhumansai/openhuman", "Lum1104/Understand-Anything", "anthropics/claude-plugins-official", "colbymchenry/codegraph"], "data": [30, 31, 32, 32, 33, 39, 40, 40, 42, 42, 50, 52, 56, 59, 67, 69, 78, 104, 153, 249]},
        'weekly': {"categories": ["rtk-ai/rtk", "Yuan1z0825/nature-skills", "Anil-matcha/Open-Generative-AI", "truelockmc/streambert", "anthropics/financial-services", "HKUDS/CLI-Anything", "neilsonnn/image-blaster", "anthropics/claude-for-legal", "K-Dense-AI/scientific-agent-skills", "rmyndharis/OpenWA", "Hmbown/DeepSeek-TUI", "vercel-labs/zero", "supertone-inc/supertonic", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "colbymchenry/codegraph", "forrestchang/andrej-karpathy-skills", "mattpocock/skills", "tinyhumansai/openhuman"], "data": [276, 283, 288, 301, 306, 309, 310, 316, 327, 328, 341, 357, 370, 544, 550, 766, 946, 1110, 1221, 1224]},
        'monthly': {"categories": ["anthropics/financial-services", "JuliusBrussee/caveman", "msitarzewski/agency-agents", "safishamsi/graphify", "rtk-ai/rtk", "VoltAgent/awesome-design-md", "garrytan/gstack", "Z4nzu/hackingtool", "addyosmani/agent-skills", "ruvnet/ruflo", "affaan-m/everything-claude-code", "farion1231/cc-switch", "warpdotdev/warp", "Hmbown/DeepSeek-TUI", "TauricResearch/TradingAgents", "Alishahryar1/free-claude-code", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1873, 2049, 2051, 2106, 2119, 2228, 2270, 2325, 2590, 2629, 2905, 3030, 3152, 3224, 3231, 3327, 3944, 5813, 8383, 8657]}
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
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +249 | 16322 |
| 2 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +153 | 24673 |
| 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +104 | 18334 |
| 4 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +78 | 25651 |
| 5 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +69 | 4458 |
| 6 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +67 | 11749 |
| 7 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +59 | 19013 |
| 8 | [multica-ai/multica](https://github.com/multica-ai/multica) | +56 | 31377 |
| 9 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +52 | 2408 |
| 10 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +50 | 16379 |
| 11 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +42 | 1814 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +42 | 51714 |
| 13 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +40 | 27988 |
| 14 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +40 | 18695 |
| 15 | [88lin/video_vip](https://github.com/88lin/video_vip) | +39 | 2323 |
| 16 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +33 | 39542 |
| 17 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +32 | 3968 |
| 18 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +32 | 505 |
| 19 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +31 | 40926 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 10574 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +29 | 52887 |
| 22 | [decolua/9router](https://github.com/decolua/9router) | +28 | 13492 |
| 23 | [dotnet/skills](https://github.com/dotnet/skills) | +27 | 2495 |
| 24 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +27 | 6306 |
| 25 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +27 | 4265 |
| 26 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +26 | 8295 |
| 27 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +26 | 5720 |
| 28 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +25 | 14599 |
| 29 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +23 | 2048 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +23 | 19782 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1224 | 25651 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1221 | 100902 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1110 | 146309 |
| 4 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +946 | 16322 |
| 5 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +766 | 19013 |
| 6 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +550 | 18695 |
| 7 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +544 | 16379 |
| 8 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +370 | 9426 |
| 9 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +357 | 4305 |
| 10 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +341 | 33473 |
| 11 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +328 | 5720 |
| 12 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +327 | 25205 |
| 13 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +316 | 7466 |
| 14 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +310 | 3976 |
| 15 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +309 | 39542 |
| 16 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +306 | 26727 |
| 17 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +301 | 4458 |
| 18 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +288 | 16614 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +283 | 10574 |
| 20 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +276 | 52887 |
| 21 | [decolua/9router](https://github.com/decolua/9router) | +276 | 13492 |
| 22 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +263 | 24673 |
| 23 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +261 | 13994 |
| 24 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +251 | 3842 |
| 25 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +249 | 44877 |
| 26 | [withcoral/coral](https://github.com/withcoral/coral) | +248 | 3947 |
| 27 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +223 | 4445 |
| 28 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +218 | 11749 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +214 | 19782 |
| 30 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +199 | 7281 |
| 31 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +196 | 18334 |
| 32 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +190 | 16049 |
| 33 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +189 | 51715 |
| 34 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +189 | 18190 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +186 | 52458 |
| 36 | [MinishLab/semble](https://github.com/MinishLab/semble) | +185 | 3697 |
| 37 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +185 | 3918 |
| 38 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +185 | 22329 |
| 39 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +184 | 27988 |
| 40 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +182 | 8657 |
| 41 | [floci-io/floci](https://github.com/floci-io/floci) | +179 | 12801 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +175 | 31377 |
| 43 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +174 | 19172 |
| 44 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +174 | 1555 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +169 | 38489 |
| 46 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +168 | 6708 |
| 47 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +163 | 20493 |
| 48 | [compozy/compozy](https://github.com/compozy/compozy) | +161 | 2139 |
| 49 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +160 | 4525 |
| 50 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +152 | 43530 |
| 51 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +151 | 3968 |
| 52 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +148 | 2531 |
| 53 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +146 | 50066 |
| 54 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +143 | 27631 |
| 55 | [antirez/ds4](https://github.com/antirez/ds4) | +143 | 11365 |
| 56 | [santifer/career-ops](https://github.com/santifer/career-ops) | +138 | 46679 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +137 | 11306 |
| 58 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +136 | 2408 |
| 59 | [calcom/cal.diy](https://github.com/calcom/cal.diy) | +136 | 40326 |
| 60 | [larksuite/cli](https://github.com/larksuite/cli) | +135 | 12372 |
| 61 | [orailnoor/DroidDesk](https://github.com/orailnoor/DroidDesk) | +133 | 1773 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +130 | 22806 |
| 63 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +129 | 1632 |
| 64 | [wechat-article/wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter) | +128 | 10687 |
| 65 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +117 | 39766 |
| 66 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +115 | 29591 |
| 67 | [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) | +113 | 4380 |
| 68 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +112 | 34914 |
| 69 | [blader/humanizer](https://github.com/blader/humanizer) | +111 | 20447 |
| 70 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +109 | 2048 |
| 71 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +109 | 6306 |
| 72 | [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) | +109 | 890 |
| 73 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +106 | 24917 |
| 74 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +105 | 62037 |
| 75 | [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | +105 | 20380 |
| 76 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +104 | 2093 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +103 | 30054 |
| 78 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +102 | 54430 |
| 79 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +102 | 12599 |
| 80 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +101 | 18466 |
| 81 | [soxoj/maigret](https://github.com/soxoj/maigret) | +101 | 29931 |
| 82 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +99 | 1814 |
| 83 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +96 | 11029 |
| 84 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +95 | 20801 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +95 | 34225 |
| 86 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +93 | 8881 |
| 87 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +92 | 1479 |
| 88 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +92 | 6426 |
| 89 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +91 | 1311 |
| 90 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +88 | 14599 |
| 91 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +87 | 32509 |
| 92 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +87 | 18628 |
| 93 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +85 | 6557 |
| 94 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +82 | 5963 |
| 95 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +82 | 19680 |
| 96 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +81 | 1858 |
| 97 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +78 | 4266 |
| 98 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +78 | 40926 |
| 99 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +78 | 33848 |
| 100 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +77 | 4523 |
| 101 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +76 | 22571 |
| 102 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +73 | 15313 |
| 103 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +72 | 8289 |
| 104 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +71 | 2138 |
| 105 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +71 | 10394 |
| 106 | [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) | +69 | 5829 |
| 107 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +69 | 6234 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +69 | 15883 |
| 109 | [yichuan-w/LEANN](https://github.com/yichuan-w/LEANN) | +66 | 11662 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +66 | 44545 |
| 111 | [byrongamatos/slopsmith](https://github.com/byrongamatos/slopsmith) | +63 | 1033 |
| 112 | [shang-zhu/violin](https://github.com/shang-zhu/violin) | +62 | 779 |
| 113 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +61 | 8295 |
| 114 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +61 | 13498 |
| 115 | [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | +58 | 1357 |
| 116 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +58 | 14207 |
| 117 | [jundot/omlx](https://github.com/jundot/omlx) | +57 | 14903 |
| 118 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +57 | 2387 |
| 119 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +56 | 32707 |
| 120 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +55 | 1448 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8657 | 100902 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8383 | 146309 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5813 | 163037 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3944 | 60312 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3327 | 27988 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3231 | 30590 |
| 7 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3224 | 33473 |
| 8 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3152 | 59603 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3030 | 78155 |
| 10 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +2905 | 51199 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2629 | 54157 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2590 | 44877 |
| 13 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2325 | 55070 |
| 14 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2270 | 100854 |
| 15 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2228 | 82695 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2119 | 52887 |
| 17 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2106 | 51715 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2051 | 104205 |
| 19 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2049 | 63730 |
| 20 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1873 | 26727 |
| 21 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1851 | 109881 |
| 22 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1843 | 25651 |
| 23 | [anthropics/skills](https://github.com/anthropics/skills) | +1734 | 74774 |
| 24 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1685 | 53080 |
| 25 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1682 | 15313 |
| 26 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1632 | 11256 |
| 27 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1582 | 52935 |
| 28 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1562 | 19172 |
| 29 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1497 | 18695 |
| 30 | [github/spec-kit](https://github.com/github/spec-kit) | +1467 | 71722 |
| 31 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1425 | 30678 |
| 32 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1420 | 39766 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1385 | 52458 |
| 34 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1347 | 29931 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1314 | 34148 |
| 36 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1301 | 19782 |
| 37 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1294 | 16614 |
| 38 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1291 | 22571 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1277 | 85286 |
| 40 | [antirez/ds4](https://github.com/antirez/ds4) | +1265 | 11365 |
| 41 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1258 | 31377 |
| 42 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1250 | 14663 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1244 | 20492 |
| 44 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1237 | 63910 |
| 45 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1226 | 16379 |
| 46 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1221 | 11306 |
| 47 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1200 | 19013 |
| 48 | [decolua/9router](https://github.com/decolua/9router) | +1091 | 13492 |
| 49 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1075 | 11029 |
| 50 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1057 | 67142 |
| 51 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1057 | 13498 |
| 52 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1048 | 16322 |
| 53 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +956 | 18335 |
| 54 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +938 | 13994 |
| 55 | [santifer/career-ops](https://github.com/santifer/career-ops) | +933 | 46679 |
| 56 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +921 | 10574 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +915 | 22806 |
| 58 | [openai/symphony](https://github.com/openai/symphony) | +910 | 24443 |
| 59 | [openai/codex](https://github.com/openai/codex) | +856 | 61744 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +851 | 18190 |
| 61 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +839 | 63631 |
| 62 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +826 | 54430 |
| 63 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +824 | 82774 |
| 64 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +824 | 29591 |
| 65 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +802 | 6489 |
| 66 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +801 | 47362 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +790 | 30054 |
| 68 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +785 | 38489 |
| 69 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +776 | 18628 |
| 70 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +763 | 50066 |
| 71 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +759 | 11984 |
| 72 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +747 | 8295 |
| 73 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +740 | 6465 |
| 74 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +736 | 15423 |
| 75 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +726 | 34914 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +723 | 20801 |
| 77 | [floci-io/floci](https://github.com/floci-io/floci) | +714 | 12801 |
| 78 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +712 | 51085 |
| 79 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +701 | 32509 |
| 80 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +678 | 5858 |
| 81 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +664 | 62037 |
| 82 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +664 | 8881 |
| 83 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +660 | 37330 |
| 84 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +656 | 5660 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +653 | 34225 |
| 86 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +648 | 33878 |
| 87 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +642 | 7466 |
| 88 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +631 | 22329 |
| 89 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +626 | 16049 |
| 90 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +621 | 33848 |
| 91 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +620 | 34984 |
| 92 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +615 | 11749 |
| 93 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +615 | 39542 |
| 94 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +609 | 61570 |
| 95 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +609 | 25510 |
| 96 | [browser-use/video-use](https://github.com/browser-use/video-use) | +603 | 8235 |
| 97 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +598 | 11459 |
| 98 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +588 | 13297 |
| 99 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +574 | 25205 |
| 100 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +567 | 9426 |
| 101 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +542 | 6426 |
| 102 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +540 | 17182 |
| 103 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +532 | 4137 |
| 104 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +531 | 8289 |
| 105 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +529 | 4525 |
| 106 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +497 | 18466 |
| 107 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +497 | 24201 |
| 108 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +490 | 24673 |
| 109 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +485 | 19518 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +466 | 44545 |
| 111 | [jundot/omlx](https://github.com/jundot/omlx) | +460 | 14903 |
| 112 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +456 | 31983 |
| 113 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +444 | 6234 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +430 | 14207 |
| 115 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +429 | 19417 |
| 116 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +417 | 38387 |
| 117 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +416 | 2748 |
| 118 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +414 | 4266 |
| 119 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +376 | 7906 |
| 120 | [browserbase/skills](https://github.com/browserbase/skills) | +376 | 3404 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +371 | 15883 |
| 122 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +367 | 3631 |
| 123 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +365 | 9978 |
| 124 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +363 | 20519 |
| 125 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +360 | 5647 |
| 126 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +350 | 36799 |
| 127 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +349 | 26347 |
| 128 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +341 | 27493 |
| 129 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +341 | 5603 |
| 130 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +339 | 21488 |
| 131 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +328 | 23475 |
| 132 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +325 | 14599 |
| 133 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +322 | 5145 |
| 134 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +320 | 1672 |
| 135 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +311 | 32707 |
| 136 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +310 | 4445 |
| 137 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +310 | 7001 |
| 138 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +310 | 2605 |
| 139 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +310 | 3909 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +305 | 21883 |
| 141 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +305 | 4699 |
| 142 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +301 | 9560 |
| 143 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +300 | 2283 |
| 144 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +299 | 6577 |
| 145 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +299 | 4458 |
| 146 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +297 | 2334 |
| 147 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +295 | 4523 |
| 148 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +293 | 33637 |
| 149 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +289 | 3934 |
| 150 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +289 | 26583 |
| 151 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +286 | 10394 |
| 152 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +286 | 2567 |
| 153 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +285 | 6708 |
| 154 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +285 | 27146 |
| 155 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +284 | 2304 |
| 156 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +283 | 22019 |
| 157 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +282 | 2921 |
| 158 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +281 | 1816 |
| 159 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +280 | 32861 |
| 160 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +279 | 3918 |
| 161 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +278 | 43002 |
| 162 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +276 | 5358 |
| 163 | [MinishLab/semble](https://github.com/MinishLab/semble) | +275 | 3697 |
| 164 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +271 | 13582 |
| 165 | [openai/skills](https://github.com/openai/skills) | +267 | 19888 |
| 166 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +267 | 25794 |
| 167 | [z-lab/dflash](https://github.com/z-lab/dflash) | +266 | 4695 |
| 168 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +247 | 39841 |
| 169 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +246 | 2462 |
| 170 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +244 | 4236 |
| 171 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +240 | 18370 |
| 172 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +240 | 37564 |
| 173 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +236 | 12952 |
| 174 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +234 | 20097 |
| 175 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +231 | 1931 |
| 176 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +231 | 28097 |
| 177 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +228 | 3662 |
| 178 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +224 | 2138 |
| 179 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +220 | 4284 |
| 180 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +218 | 6399 |
| 181 | [tiagozip/cap](https://github.com/tiagozip/cap) | +213 | 6431 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +209 | 7166 |
| 183 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +206 | 7281 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +191 | 14346 |
| 185 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +190 | 2531 |
| 186 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +174 | 1555 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +172 | 5151 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +170 | 26972 |
| 189 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +163 | 3667 |
| 190 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +161 | 6130 |
| 191 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +153 | 4670 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +142 | 36103 |
| 193 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +139 | 2034 |
| 194 | [playcanvas/engine](https://github.com/playcanvas/engine) | +139 | 15868 |
| 195 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +136 | 10421 |
| 196 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +135 | 2831 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +132 | 15250 |
| 198 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +131 | 7537 |
| 199 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +129 | 16956 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +126 | 0 |
| 201 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +121 | 1511 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +121 | 39596 |
| 203 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +120 | 9953 |
| 204 | [eze-is/web-access](https://github.com/eze-is/web-access) | +120 | 6729 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +118 | 41086 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +112 | 23126 |
| 207 | [sandeco/reversa](https://github.com/sandeco/reversa) | +111 | 927 |
| 208 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 835 |
| 209 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +101 | 3088 |
| 210 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +99 | 1311 |
| 211 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +98 | 0 |
| 212 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +96 | 4478 |
| 213 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 1994 |
| 214 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +95 | 10388 |
| 215 | [88lin/video_vip](https://github.com/88lin/video_vip) | +90 | 2323 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +88 | 40265 |
| 217 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +86 | 24156 |
| 218 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +85 | 703 |
| 219 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +85 | 7978 |
| 220 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +84 | 14829 |
| 221 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +83 | 35473 |
| 222 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +80 | 1590 |
| 223 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +77 | 9976 |
| 224 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +69 | 11852 |
| 225 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +69 | 3922 |
| 226 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +68 | 2447 |
| 227 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +64 | 3217 |
| 228 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +61 | 8421 |
| 229 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +60 | 37313 |
| 230 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +60 | 48784 |
| 231 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +59 | 30173 |
| 232 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +57 | 13381 |
| 233 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +56 | 441 |
| 234 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +56 | 45263 |
| 235 | [halo-dev/halo](https://github.com/halo-dev/halo) | +56 | 37991 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +55 | 33000 |
| 237 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +54 | 983 |
| 238 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +54 | 718 |
| 239 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +52 | 910 |
| 240 | [robinebers/openusage](https://github.com/robinebers/openusage) | +52 | 2542 |
| 241 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 283 |
| 242 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +51 | 840 |
| 243 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +51 | 2291 |
| 244 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +50 | 517 |
| 245 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 304 |
| 246 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +50 | 977 |
| 247 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +50 | 3232 |
| 248 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +50 | 2542 |
| 249 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +49 | 341 |
| 250 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 471 |
| 251 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +48 | 1823 |
| 252 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +48 | 11238 |
| 253 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +47 | 2188 |
| 254 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +46 | 586 |
| 255 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +44 | 2184 |
| 256 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 330 |
| 257 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +42 | 1777 |
| 258 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +42 | 922 |
| 259 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +42 | 1492 |
| 260 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +42 | 4152 |
| 261 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +42 | 4186 |
| 262 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 330 |
| 263 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +41 | 3138 |
| 264 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +40 | 494 |
| 265 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +39 | 887 |
| 266 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +39 | 1405 |
| 267 | [openmemind/memind](https://github.com/openmemind/memind) | +39 | 807 |
| 268 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +37 | 1358 |
| 269 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +37 | 2232 |
| 270 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +37 | 1945 |
| 271 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +36 | 630 |
| 272 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1429 |
| 273 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +34 | 5146 |
| 274 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +33 | 751 |
| 275 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +33 | 498 |
| 276 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +33 | 9705 |
| 277 | [intave/intave](https://github.com/intave/intave) | +32 | 259 |
| 278 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +31 | 314 |
| 279 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 280 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +27 | 2402 |
| 281 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +27 | 223 |
| 282 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +26 | 340 |
| 283 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 291 |
| 284 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2214 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +25 | 1544 |
| 286 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +24 | 0 |
| 287 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +24 | 2634 |
| 288 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +23 | 2950 |
| 289 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +23 | 243 |
| 290 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +22 | 339 |
| 291 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +22 | 329 |
| 292 | [is-a-dev/register](https://github.com/is-a-dev/register) | +21 | 10325 |
| 293 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 294 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +21 | 210 |
| 295 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +19 | 3233 |
| 296 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +18 | 867 |
| 297 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +18 | 449 |
| 298 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +18 | 858 |
| 299 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +16 | 1947 |
| 300 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +14 | 150 |
