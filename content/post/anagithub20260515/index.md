---
title: "2026-05-15 GitHub增长趋势报告"
description: "1.openhuman+124 2.CloakBrowser+103 3.DeepSeek-TUI+89 4.ds4+69 5.OmniVoice-Studio+62"
date: 2026-05-15T21:03:37+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-15 21:03:37

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
        'daily': {"categories": ["shiyu-coder/Kronos", "dograh-hq/dograh", "addyosmani/agent-skills", "datawhalechina/hello-agents", "decolua/9router", "rtk-ai/rtk", "ruvnet/ruflo", "hugohe3/ppt-master", "badlogic/pi-mono", "Raiper34/spooty", "K-Dense-AI/scientific-agent-skills", "larksuite/cli", "AIDC-AI/Pixelle-Video", "Yuan1z0825/nature-skills", "rohitg00/agentmemory", "debpalash/OmniVoice-Studio", "antirez/ds4", "Hmbown/DeepSeek-TUI", "CloakHQ/CloakBrowser", "tinyhumansai/openhuman"], "data": [35, 36, 36, 37, 37, 41, 41, 42, 46, 48, 48, 52, 54, 58, 62, 62, 69, 89, 103, 124]},
        'weekly': {"categories": ["AIDC-AI/Pixelle-Video", "datawhalechina/easy-vibe", "yikart/AiToEarn", "bytedance/UI-TARS-desktop", "vercel-labs/zero-native", "floci-io/floci", "ruvnet/ruflo", "decolua/9router", "tinyhumansai/openhuman", "rohitg00/agentmemory", "datawhalechina/hello-agents", "CloakHQ/CloakBrowser", "farion1231/cc-switch", "addyosmani/agent-skills", "Hmbown/DeepSeek-TUI", "antirez/ds4", "forrestchang/andrej-karpathy-skills", "anthropics/financial-services", "NousResearch/hermes-agent", "mattpocock/skills"], "data": [401, 408, 411, 451, 497, 501, 507, 580, 598, 621, 672, 868, 892, 923, 933, 1010, 1150, 1193, 1355, 1625]},
        'monthly': {"categories": ["ruvnet/ruflo", "rtk-ai/rtk", "heygen-com/hyperframes", "thedotmack/claude-mem", "Fincept-Corporation/FinceptTerminal", "safishamsi/graphify", "Hmbown/DeepSeek-TUI", "addyosmani/agent-skills", "farion1231/cc-switch", "warpdotdev/warp", "Alishahryar1/free-claude-code", "garrytan/gstack", "TauricResearch/TradingAgents", "affaan-m/everything-claude-code", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "obra/superpowers", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2525, 2616, 2737, 2750, 2813, 2866, 2899, 3051, 3063, 3070, 3172, 3207, 3310, 3407, 3414, 3553, 4767, 7705, 8437, 12629]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +124 | 8909 |
| 2 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +103 | 11780 |
| 3 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +89 | 29811 |
| 4 | [antirez/ds4](https://github.com/antirez/ds4) | +69 | 9686 |
| 5 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +62 | 1820 |
| 6 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +62 | 9567 |
| 7 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +58 | 6631 |
| 8 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +54 | 17049 |
| 9 | [larksuite/cli](https://github.com/larksuite/cli) | +52 | 10669 |
| 10 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +48 | 22372 |
| 11 | [Raiper34/spooty](https://github.com/Raiper34/spooty) | +48 | 2063 |
| 12 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +46 | 49881 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +42 | 16811 |
| 14 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +41 | 51494 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +41 | 48502 |
| 16 | [decolua/9router](https://github.com/decolua/9router) | +37 | 10625 |
| 17 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +37 | 49789 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +36 | 42017 |
| 19 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +36 | 1019 |
| 20 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +35 | 25061 |
| 21 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +35 | 16340 |
| 22 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +32 | 2631 |
| 23 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) | +32 | 1774 |
| 24 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +31 | 23222 |
| 25 | [can4hou6joeng4/boss-agent-cli](https://github.com/can4hou6joeng4/boss-agent-cli) | +29 | 531 |
| 26 | [InterceptSuite/ProxyBridge](https://github.com/InterceptSuite/ProxyBridge) | +28 | 4239 |
| 27 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +28 | 34810 |
| 28 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +27 | 7430 |
| 29 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +27 | 48339 |
| 30 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +27 | 8967 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1625 | 84764 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1355 | 151883 |
| 3 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1193 | 23222 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1150 | 130853 |
| 5 | [antirez/ds4](https://github.com/antirez/ds4) | +1010 | 9686 |
| 6 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +933 | 29811 |
| 7 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +923 | 42017 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +892 | 71783 |
| 9 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +868 | 11780 |
| 10 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +672 | 49789 |
| 11 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +621 | 9567 |
| 12 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +598 | 8909 |
| 13 | [decolua/9router](https://github.com/decolua/9router) | +580 | 10625 |
| 14 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +507 | 51494 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +501 | 11083 |
| 16 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +497 | 3615 |
| 17 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +451 | 34073 |
| 18 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +411 | 14037 |
| 19 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +408 | 11087 |
| 20 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +401 | 17049 |
| 21 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +374 | 49882 |
| 22 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +373 | 48339 |
| 23 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +371 | 2895 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +362 | 16811 |
| 25 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +356 | 5162 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +354 | 6631 |
| 27 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +351 | 48502 |
| 28 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +337 | 17370 |
| 29 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +314 | 8052 |
| 30 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +310 | 9669 |
| 31 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +301 | 3351 |
| 32 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +292 | 4872 |
| 33 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +271 | 8967 |
| 34 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +269 | 42334 |
| 35 | [soxoj/maigret](https://github.com/soxoj/maigret) | +268 | 28802 |
| 36 | [multica-ai/multica](https://github.com/multica-ai/multica) | +262 | 28713 |
| 37 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +246 | 7430 |
| 38 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +234 | 24802 |
| 39 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +232 | 11515 |
| 40 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +231 | 21106 |
| 41 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +231 | 18391 |
| 42 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +222 | 15861 |
| 43 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +219 | 58579 |
| 44 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +217 | 49905 |
| 45 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +215 | 2215 |
| 46 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +214 | 10757 |
| 47 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +206 | 33575 |
| 48 | [jundot/omlx](https://github.com/jundot/omlx) | +200 | 14220 |
| 49 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +193 | 48326 |
| 50 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +188 | 7385 |
| 51 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +177 | 27994 |
| 52 | [openai/symphony](https://github.com/openai/symphony) | +172 | 23877 |
| 53 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +171 | 13905 |
| 54 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +167 | 2393 |
| 55 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +166 | 4463 |
| 56 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +165 | 38508 |
| 57 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +165 | 7706 |
| 58 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +163 | 60667 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +163 | 31453 |
| 60 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +161 | 36029 |
| 61 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +159 | 39705 |
| 62 | [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | +157 | 1843 |
| 63 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +157 | 2785 |
| 64 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +155 | 9361 |
| 65 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +154 | 17496 |
| 66 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +154 | 6164 |
| 67 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +152 | 9842 |
| 68 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +152 | 20697 |
| 69 | [oracle-devrel/oracle-ai-developer-hub](https://github.com/oracle-devrel/oracle-ai-developer-hub) | +152 | 2093 |
| 70 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +151 | 14767 |
| 71 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +149 | 5281 |
| 72 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +149 | 4018 |
| 73 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +147 | 32820 |
| 74 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +145 | 53165 |
| 75 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +144 | 4334 |
| 76 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +139 | 19350 |
| 77 | [santifer/career-ops](https://github.com/santifer/career-ops) | +139 | 44880 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +138 | 28775 |
| 79 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +135 | 7653 |
| 80 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +133 | 3500 |
| 81 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +132 | 25061 |
| 82 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +127 | 18807 |
| 83 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +127 | 2330 |
| 84 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +127 | 21208 |
| 85 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +126 | 33018 |
| 86 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +124 | 1363 |
| 87 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +123 | 22372 |
| 88 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +122 | 36243 |
| 89 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +120 | 7570 |
| 90 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +117 | 4927 |
| 91 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +116 | 1413 |
| 92 | [z-lab/dflash](https://github.com/z-lab/dflash) | +116 | 4587 |
| 93 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +116 | 31408 |
| 94 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +115 | 18396 |
| 95 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +114 | 25238 |
| 96 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +114 | 7332 |
| 97 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +113 | 13856 |
| 98 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +112 | 1281 |
| 99 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +111 | 3206 |
| 100 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +108 | 12795 |
| 101 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +105 | 13746 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +105 | 18888 |
| 103 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +105 | 1783 |
| 104 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +103 | 46013 |
| 105 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +103 | 11138 |
| 106 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +101 | 11021 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +94 | 43852 |
| 108 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +93 | 9776 |
| 109 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +91 | 44232 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +90 | 9432 |
| 111 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +89 | 36799 |
| 112 | [larksuite/cli](https://github.com/larksuite/cli) | +88 | 10669 |
| 113 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +87 | 6720 |
| 114 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +86 | 1820 |
| 115 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +85 | 34811 |
| 116 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +84 | 37623 |
| 117 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +78 | 14936 |
| 118 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +78 | 21351 |
| 119 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +78 | 907 |
| 120 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +78 | 1238 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +12629 | 130854 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +8437 | 151883 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7705 | 84764 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4767 | 60312 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3553 | 79299 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +3414 | 60705 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3407 | 51199 |
| 8 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3310 | 30590 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3207 | 97521 |
| 10 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3172 | 24802 |
| 11 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3070 | 58579 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3063 | 71784 |
| 13 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3051 | 42017 |
| 14 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +2899 | 29811 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2866 | 48339 |
| 16 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2813 | 21208 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2750 | 30678 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2737 | 18391 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2616 | 48502 |
| 20 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2525 | 51494 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2391 | 97862 |
| 22 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2278 | 55070 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2184 | 109881 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2051 | 28713 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +2031 | 74774 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1853 | 12795 |
| 27 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +1795 | 20216 |
| 28 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1748 | 49882 |
| 29 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1704 | 12969 |
| 30 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1639 | 34148 |
| 31 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1619 | 23222 |
| 32 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1606 | 49905 |
| 33 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1587 | 10734 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1580 | 49789 |
| 35 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1579 | 13856 |
| 36 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1560 | 26132 |
| 37 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1550 | 17049 |
| 38 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1518 | 44880 |
| 39 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1496 | 65680 |
| 40 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1459 | 38508 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1426 | 16811 |
| 42 | [github/spec-kit](https://github.com/github/spec-kit) | +1423 | 71722 |
| 43 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1374 | 11515 |
| 44 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1356 | 85286 |
| 45 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1337 | 18807 |
| 46 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1262 | 28802 |
| 47 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1252 | 69674 |
| 48 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1238 | 17496 |
| 49 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1193 | 13905 |
| 50 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1162 | 25839 |
| 51 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1154 | 53165 |
| 52 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1152 | 62447 |
| 53 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1150 | 81251 |
| 54 | [antirez/ds4](https://github.com/antirez/ds4) | +1125 | 9686 |
| 55 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1105 | 57364 |
| 56 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1084 | 8967 |
| 57 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1070 | 19350 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1046 | 21106 |
| 59 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1005 | 27994 |
| 60 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +1002 | 6354 |
| 61 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +986 | 9842 |
| 62 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +983 | 15861 |
| 63 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +981 | 14282 |
| 64 | [openai/codex](https://github.com/openai/codex) | +971 | 61744 |
| 65 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +966 | 11780 |
| 66 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +957 | 14812 |
| 67 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +957 | 23985 |
| 68 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +952 | 47144 |
| 69 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +927 | 26338 |
| 70 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +918 | 28775 |
| 71 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +908 | 25061 |
| 72 | [openai/symphony](https://github.com/openai/symphony) | +907 | 23877 |
| 73 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +897 | 48326 |
| 74 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +897 | 7429 |
| 75 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +895 | 31453 |
| 76 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +883 | 36243 |
| 77 | [decolua/9router](https://github.com/decolua/9router) | +869 | 10625 |
| 78 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +869 | 60667 |
| 79 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +860 | 52263 |
| 80 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +853 | 16573 |
| 81 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +848 | 32820 |
| 82 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +836 | 33878 |
| 83 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +831 | 33575 |
| 84 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +808 | 14767 |
| 85 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +807 | 37330 |
| 86 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +805 | 47122 |
| 87 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +802 | 18888 |
| 88 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +793 | 60808 |
| 89 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +785 | 33018 |
| 90 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +781 | 67897 |
| 91 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +767 | 36029 |
| 92 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +767 | 5870 |
| 93 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +759 | 10757 |
| 94 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +754 | 5945 |
| 95 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +749 | 7385 |
| 96 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +735 | 7570 |
| 97 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +734 | 9567 |
| 98 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +730 | 11087 |
| 99 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +716 | 6164 |
| 100 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +685 | 7706 |
| 101 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +652 | 6631 |
| 102 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +648 | 7332 |
| 103 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +631 | 8909 |
| 104 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +614 | 45886 |
| 105 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +610 | 37623 |
| 106 | [floci-io/floci](https://github.com/floci-io/floci) | +601 | 11083 |
| 107 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +601 | 20697 |
| 108 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +600 | 43852 |
| 109 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +594 | 21290 |
| 110 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +558 | 5154 |
| 111 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +553 | 18764 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +548 | 14220 |
| 113 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +544 | 34811 |
| 114 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +540 | 25894 |
| 115 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +537 | 20230 |
| 116 | [google/magika](https://github.com/google/magika) | +536 | 17007 |
| 117 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +519 | 7430 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +506 | 13398 |
| 119 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +504 | 17978 |
| 120 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +495 | 6720 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +492 | 14936 |
| 122 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +486 | 31408 |
| 123 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +483 | 5033 |
| 124 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +445 | 5281 |
| 125 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +444 | 22872 |
| 126 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +443 | 36907 |
| 127 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +433 | 17370 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +429 | 36799 |
| 129 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2623 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +405 | 39841 |
| 131 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +402 | 3205 |
| 132 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +393 | 12579 |
| 133 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +385 | 33073 |
| 134 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +384 | 3355 |
| 135 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +376 | 27303 |
| 136 | [z-lab/dflash](https://github.com/z-lab/dflash) | +370 | 4587 |
| 137 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +370 | 9091 |
| 138 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +368 | 13302 |
| 139 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +366 | 42537 |
| 140 | [browserbase/skills](https://github.com/browserbase/skills) | +366 | 3255 |
| 141 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +365 | 22372 |
| 142 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +365 | 4963 |
| 143 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +360 | 7653 |
| 144 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +359 | 9776 |
| 145 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +359 | 4906 |
| 146 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +347 | 21351 |
| 147 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +347 | 4249 |
| 148 | [PostHog/posthog](https://github.com/PostHog/posthog) | +342 | 31767 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +338 | 32127 |
| 150 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +337 | 2393 |
| 151 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +337 | 2849 |
| 152 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +323 | 3874 |
| 153 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +318 | 13397 |
| 154 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +316 | 21584 |
| 155 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +314 | 26751 |
| 156 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +313 | 1627 |
| 157 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +311 | 19444 |
| 158 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +309 | 2542 |
| 159 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +308 | 3798 |
| 160 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +307 | 18675 |
| 161 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +302 | 37564 |
| 162 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +301 | 32299 |
| 163 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +298 | 4320 |
| 164 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +296 | 3606 |
| 165 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +295 | 9432 |
| 166 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +293 | 25352 |
| 167 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +291 | 22827 |
| 168 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +289 | 2153 |
| 169 | [openai/skills](https://github.com/openai/skills) | +287 | 19179 |
| 170 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +284 | 2116 |
| 171 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +282 | 2111 |
| 172 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +281 | 19599 |
| 173 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +281 | 4978 |
| 174 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +280 | 5984 |
| 175 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +275 | 1967 |
| 176 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +268 | 1692 |
| 177 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | +262 | 27850 |
| 178 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +259 | 4055 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +252 | 27646 |
| 180 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +235 | 2330 |
| 181 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +234 | 3604 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +232 | 6933 |
| 183 | [88lin/video_vip](https://github.com/88lin/video_vip) | +232 | 1806 |
| 184 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +229 | 1867 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +225 | 13901 |
| 186 | [tiagozip/cap](https://github.com/tiagozip/cap) | +218 | 6370 |
| 187 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +212 | 4350 |
| 188 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +205 | 36103 |
| 189 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +200 | 3162 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +199 | 26618 |
| 191 | [eze-is/web-access](https://github.com/eze-is/web-access) | +185 | 6463 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +184 | 3477 |
| 193 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +169 | 2498 |
| 194 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +167 | 10221 |
| 195 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +151 | 5864 |
| 196 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +146 | 16639 |
| 197 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +142 | 7841 |
| 198 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +142 | 8766 |
| 199 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +141 | 2856 |
| 200 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +139 | 9830 |
| 201 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +139 | 39596 |
| 202 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +139 | 3348 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +137 | 15074 |
| 204 | [playcanvas/engine](https://github.com/playcanvas/engine) | +134 | 15785 |
| 205 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +133 | 1208 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +130 | 22892 |
| 207 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +123 | 873 |
| 208 | [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | +116 | 772 |
| 209 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +115 | 7753 |
| 210 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +111 | 1285 |
| 211 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +109 | 681 |
| 212 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +109 | 723 |
| 213 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +106 | 40265 |
| 214 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +105 | 1314 |
| 215 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +103 | 10267 |
| 216 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +102 | 783 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +99 | 35473 |
| 218 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +97 | 3766 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +96 | 1391 |
| 220 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 1813 |
| 221 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +95 | 883 |
| 222 | [sandeco/reversa](https://github.com/sandeco/reversa) | +94 | 816 |
| 223 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +93 | 11732 |
| 224 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +91 | 3127 |
| 225 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +90 | 736 |
| 226 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +90 | 23971 |
| 227 | [usebruno/bruno](https://github.com/usebruno/bruno) | +83 | 41086 |
| 228 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +80 | 30084 |
| 229 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +76 | 2101 |
| 230 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +74 | 3745 |
| 231 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +74 | 8292 |
| 232 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 445 |
| 233 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +69 | 478 |
| 234 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +68 | 2097 |
| 235 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +68 | 2545 |
| 236 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2413 |
| 237 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +67 | 45263 |
| 238 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +67 | 37313 |
| 239 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +66 | 13282 |
| 240 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +63 | 48784 |
| 241 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +62 | 4253 |
| 242 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +61 | 1780 |
| 243 | [halo-dev/halo](https://github.com/halo-dev/halo) | +61 | 37991 |
| 244 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +60 | 33000 |
| 245 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +59 | 651 |
| 246 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +58 | 2718 |
| 247 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +57 | 788 |
| 248 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +57 | 869 |
| 249 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +57 | 4168 |
| 250 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2444 |
| 251 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +56 | 3081 |
| 252 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +56 | 11167 |
| 253 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +54 | 4070 |
| 254 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +54 | 1417 |
| 255 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +54 | 27558 |
| 256 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +53 | 1767 |
| 257 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +53 | 3055 |
| 258 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 464 |
| 259 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +52 | 914 |
| 260 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +52 | 2078 |
| 261 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 310 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +52 | 746 |
| 263 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +51 | 362 |
| 264 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 505 |
| 265 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +49 | 293 |
| 266 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +49 | 872 |
| 267 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 432 |
| 268 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +48 | 4166 |
| 269 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +48 | 1679 |
| 270 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +47 | 464 |
| 271 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +46 | 1659 |
| 272 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +46 | 12002 |
| 273 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +45 | 3645 |
| 274 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +43 | 313 |
| 275 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +41 | 1873 |
| 276 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +41 | 2127 |
| 277 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +40 | 9621 |
| 278 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +37 | 5099 |
| 279 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +37 | 435 |
| 280 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +37 | 315 |
| 281 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +36 | 237 |
| 282 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +36 | 5346 |
| 283 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +35 | 2364 |
| 284 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +35 | 1390 |
| 285 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +33 | 195 |
| 286 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +33 | 2209 |
| 287 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +32 | 286 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +32 | 1534 |
| 289 | [intave/intave](https://github.com/intave/intave) | +30 | 251 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +29 | 1913 |
| 291 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +28 | 751 |
| 292 | [is-a-dev/register](https://github.com/is-a-dev/register) | +27 | 10291 |
| 293 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +26 | 190 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +26 | 2185 |
| 295 | [acoder-ai-infra/AGenUI](https://github.com/acoder-ai-infra/AGenUI) | +23 | 344 |
| 296 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +23 | 2625 |
| 297 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +23 | 434 |
| 298 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +22 | 848 |
| 299 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +21 | 2933 |
| 300 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +21 | 206 |
