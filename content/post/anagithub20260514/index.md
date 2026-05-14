---
title: "2026-05-14 GitHub增长趋势报告"
description: "1.openhuman+233 2.agentmemory+128 3.CloakBrowser+107 4.AiToEarn+95 5.floci+78"
date: 2026-05-14T21:12:13+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-14 21:12:13

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
        'daily': {"categories": ["fathah/hermes-desktop", "op7418/guizang-ppt-skill", "Fission-AI/OpenSpec", "rtk-ai/rtk", "decolua/9router", "AIDC-AI/Pixelle-Video", "danielmiessler/Personal_AI_Infrastructure", "Yuan1z0825/nature-skills", "K-Dense-AI/scientific-agent-skills", "datawhalechina/hello-agents", "addyosmani/agent-skills", "millionco/react-doctor", "anthropics/financial-services-plugins", "ruvnet/ruflo", "hugohe3/ppt-master", "floci-io/floci", "yikart/AiToEarn", "CloakHQ/CloakBrowser", "rohitg00/agentmemory", "tinyhumansai/openhuman"], "data": [31, 32, 32, 34, 34, 36, 37, 40, 41, 42, 43, 43, 43, 43, 45, 78, 95, 107, 128, 233]},
        'weekly': {"categories": ["safishamsi/graphify", "rtk-ai/rtk", "datawhalechina/easy-vibe", "floci-io/floci", "vercel-labs/zero-native", "bytedance/UI-TARS-desktop", "tinyhumansai/openhuman", "ruvnet/ruflo", "TauricResearch/TradingAgents", "rohitg00/agentmemory", "decolua/9router", "VoltAgent/awesome-design-md", "datawhalechina/hello-agents", "CloakHQ/CloakBrowser", "farion1231/cc-switch", "addyosmani/agent-skills", "antirez/ds4", "forrestchang/andrej-karpathy-skills", "anthropics/financial-services-plugins", "mattpocock/skills"], "data": [384, 397, 398, 479, 482, 493, 494, 527, 530, 576, 628, 668, 684, 814, 919, 1022, 1058, 1187, 1403, 1513]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "ruvnet/ruflo", "rtk-ai/rtk", "heygen-com/hyperframes", "Fincept-Corporation/FinceptTerminal", "safishamsi/graphify", "thedotmack/claude-mem", "warpdotdev/warp", "farion1231/cc-switch", "addyosmani/agent-skills", "Alishahryar1/free-claude-code", "garrytan/gstack", "TauricResearch/TradingAgents", "affaan-m/everything-claude-code", "JuliusBrussee/caveman", "VoltAgent/awesome-design-md", "obra/superpowers", "mattpocock/skills", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [2422, 2508, 2682, 2720, 2803, 2998, 3024, 3056, 3083, 3093, 3159, 3237, 3310, 3536, 3778, 3853, 4917, 7510, 9030, 13709]}
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
| 1 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +233 | 7647 |
| 2 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +128 | 8898 |
| 3 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +107 | 10742 |
| 4 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +95 | 13740 |
| 5 | [floci-io/floci](https://github.com/floci-io/floci) | +78 | 10471 |
| 6 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +45 | 16410 |
| 7 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +43 | 50979 |
| 8 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +43 | 22745 |
| 9 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +43 | 9586 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +43 | 41537 |
| 11 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +42 | 49426 |
| 12 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +41 | 21727 |
| 13 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +40 | 6049 |
| 14 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +37 | 13660 |
| 15 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +36 | 16653 |
| 16 | [decolua/9router](https://github.com/decolua/9router) | +34 | 10256 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +34 | 47932 |
| 18 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +32 | 48043 |
| 19 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +32 | 8658 |
| 20 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +31 | 4948 |
| 21 | [multica-ai/multica](https://github.com/multica-ai/multica) | +27 | 28412 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +27 | 18175 |
| 23 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +27 | 47960 |
| 24 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +27 | 9569 |
| 25 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +26 | 7177 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +26 | 49395 |
| 27 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +26 | 3078 |
| 28 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +23 | 17199 |
| 29 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +22 | 2179 |
| 30 | [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) | +22 | 1547 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1513 | 81996 |
| 2 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1403 | 22745 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1187 | 129566 |
| 4 | [antirez/ds4](https://github.com/antirez/ds4) | +1058 | 8741 |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1022 | 41537 |
| 6 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +919 | 70773 |
| 7 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +814 | 10742 |
| 8 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +684 | 49426 |
| 9 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +668 | 78709 |
| 10 | [decolua/9router](https://github.com/decolua/9router) | +628 | 10256 |
| 11 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +576 | 8898 |
| 12 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +530 | 30590 |
| 13 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +527 | 50979 |
| 14 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +494 | 7647 |
| 15 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +493 | 33909 |
| 16 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +482 | 3478 |
| 17 | [floci-io/floci](https://github.com/floci-io/floci) | +479 | 10471 |
| 18 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +398 | 10834 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +397 | 47932 |
| 20 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +384 | 47960 |
| 21 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +381 | 13741 |
| 22 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +381 | 16653 |
| 23 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +378 | 49395 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +371 | 16410 |
| 25 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +359 | 2771 |
| 26 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +336 | 4948 |
| 27 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +333 | 17199 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +330 | 6049 |
| 29 | [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | +328 | 7949 |
| 30 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +305 | 3335 |
| 31 | [millionco/react-doctor](https://github.com/millionco/react-doctor) | +303 | 9586 |
| 32 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +285 | 4769 |
| 33 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +268 | 42334 |
| 34 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +267 | 8658 |
| 35 | [soxoj/maigret](https://github.com/soxoj/maigret) | +264 | 28606 |
| 36 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +257 | 49519 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +253 | 18175 |
| 38 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +253 | 10648 |
| 39 | [multica-ai/multica](https://github.com/multica-ai/multica) | +252 | 28412 |
| 40 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +247 | 24574 |
| 41 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +239 | 20884 |
| 42 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +237 | 7177 |
| 43 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +233 | 58416 |
| 44 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +228 | 11381 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +222 | 15632 |
| 46 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +222 | 3982 |
| 47 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +218 | 7322 |
| 48 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +209 | 33339 |
| 49 | [jundot/omlx](https://github.com/jundot/omlx) | +203 | 14114 |
| 50 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +199 | 48043 |
| 51 | [jackwener/wx-cli](https://github.com/jackwener/wx-cli) | +195 | 2034 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +195 | 27724 |
| 53 | [openai/symphony](https://github.com/openai/symphony) | +181 | 23777 |
| 54 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +180 | 6101 |
| 55 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +179 | 60473 |
| 56 | [NVlabs/cuda-oxide](https://github.com/NVlabs/cuda-oxide) | +175 | 1794 |
| 57 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +172 | 4414 |
| 58 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +172 | 7589 |
| 59 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +171 | 14653 |
| 60 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +170 | 13550 |
| 61 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +169 | 31295 |
| 62 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +168 | 38341 |
| 63 | [angelos-p/llm-from-scratch](https://github.com/angelos-p/llm-from-scratch) | +168 | 2757 |
| 64 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +167 | 7634 |
| 65 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +167 | 2361 |
| 66 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +166 | 5154 |
| 67 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +166 | 17322 |
| 68 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +162 | 53017 |
| 69 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +161 | 39602 |
| 70 | [oracle-devrel/oracle-ai-developer-hub](https://github.com/oracle-devrel/oracle-ai-developer-hub) | +161 | 2052 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +155 | 35919 |
| 72 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +155 | 31292 |
| 73 | [strukto-ai/mirage](https://github.com/strukto-ai/mirage) | +155 | 2237 |
| 74 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +152 | 9569 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +151 | 32676 |
| 76 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +150 | 20579 |
| 77 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +145 | 4260 |
| 78 | [santifer/career-ops](https://github.com/santifer/career-ops) | +144 | 44714 |
| 79 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +143 | 9198 |
| 80 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +143 | 2310 |
| 81 | [Augani/openreel-video](https://github.com/Augani/openreel-video) | +143 | 2914 |
| 82 | [z-lab/dflash](https://github.com/z-lab/dflash) | +143 | 4561 |
| 83 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +139 | 19160 |
| 84 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +138 | 28530 |
| 85 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +131 | 32834 |
| 86 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +131 | 1351 |
| 87 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +130 | 3443 |
| 88 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +129 | 36169 |
| 89 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +128 | 18717 |
| 90 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +125 | 21136 |
| 91 | [HongyuanLuke/frequencylaw](https://github.com/HongyuanLuke/frequencylaw) | +124 | 1347 |
| 92 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +123 | 7421 |
| 93 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +121 | 24767 |
| 94 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +121 | 9747 |
| 95 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +120 | 1218 |
| 96 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +119 | 12637 |
| 97 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +118 | 7202 |
| 98 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +118 | 13705 |
| 99 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +115 | 25156 |
| 100 | [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | +111 | 4804 |
| 101 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +109 | 18779 |
| 102 | [romainsimon/paperasse](https://github.com/romainsimon/paperasse) | +102 | 1753 |
| 103 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +101 | 863 |
| 104 | [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | +100 | 13660 |
| 105 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +99 | 46013 |
| 106 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +94 | 44232 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +93 | 9347 |
| 108 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +89 | 36799 |
| 109 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +87 | 37529 |
| 110 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +86 | 6674 |
| 111 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +86 | 3897 |
| 112 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +83 | 21253 |
| 113 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +83 | 43722 |
| 114 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +81 | 21727 |
| 115 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +81 | 16467 |
| 116 | [elementalsouls/Claude-OSINT](https://github.com/elementalsouls/Claude-OSINT) | +79 | 1227 |
| 117 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +79 | 25821 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +78 | 14810 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +78 | 13322 |
| 120 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +76 | 3317 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +13709 | 129566 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +9030 | 150221 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7510 | 81996 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +4917 | 60312 |
| 5 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +3853 | 78709 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +3778 | 60193 |
| 7 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3536 | 51199 |
| 8 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3310 | 30590 |
| 9 | [garrytan/gstack](https://github.com/garrytan/gstack) | +3237 | 96641 |
| 10 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3159 | 24574 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3093 | 41537 |
| 12 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3083 | 70773 |
| 13 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3056 | 58416 |
| 14 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3024 | 30678 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2998 | 47960 |
| 16 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2803 | 21136 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2720 | 18175 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2682 | 47932 |
| 19 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2508 | 50979 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2422 | 97314 |
| 21 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2267 | 55070 |
| 22 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2213 | 109881 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2164 | 28412 |
| 24 | [anthropics/skills](https://github.com/anthropics/skills) | +2087 | 74774 |
| 25 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2053 | 20183 |
| 26 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1842 | 12637 |
| 27 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1738 | 49395 |
| 28 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +1687 | 12861 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1677 | 34148 |
| 30 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1631 | 49426 |
| 31 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1612 | 49520 |
| 32 | [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | +1594 | 22745 |
| 33 | [santifer/career-ops](https://github.com/santifer/career-ops) | +1584 | 44714 |
| 34 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1582 | 10668 |
| 35 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1568 | 13705 |
| 36 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1561 | 26113 |
| 37 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1546 | 65427 |
| 38 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1514 | 16653 |
| 39 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1463 | 38341 |
| 40 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1423 | 11381 |
| 41 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1416 | 85286 |
| 42 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1401 | 16410 |
| 43 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1393 | 18717 |
| 44 | [github/spec-kit](https://github.com/github/spec-kit) | +1392 | 71722 |
| 45 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +1379 | 53017 |
| 46 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1294 | 69674 |
| 47 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1274 | 25717 |
| 48 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1242 | 17322 |
| 49 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1241 | 28606 |
| 50 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +1217 | 62223 |
| 51 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1212 | 81083 |
| 52 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1183 | 13550 |
| 53 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +1139 | 19160 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1071 | 20884 |
| 55 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1060 | 8658 |
| 56 | [antirez/ds4](https://github.com/antirez/ds4) | +1058 | 8741 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +1009 | 15632 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1009 | 27724 |
| 59 | [openai/codex](https://github.com/openai/codex) | +997 | 61744 |
| 60 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +996 | 55717 |
| 61 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +996 | 6317 |
| 62 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +995 | 23940 |
| 63 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +993 | 14192 |
| 64 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +978 | 47118 |
| 65 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +969 | 9569 |
| 66 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +967 | 52198 |
| 67 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +957 | 14707 |
| 68 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +949 | 24767 |
| 69 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +931 | 48043 |
| 70 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +930 | 36169 |
| 71 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +929 | 26311 |
| 72 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +924 | 28530 |
| 73 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +923 | 31292 |
| 74 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +916 | 60473 |
| 75 | [openai/symphony](https://github.com/openai/symphony) | +907 | 23777 |
| 76 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +901 | 16467 |
| 77 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +896 | 7415 |
| 78 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +879 | 18779 |
| 79 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +875 | 32676 |
| 80 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +873 | 28660 |
| 81 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +870 | 10743 |
| 82 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +858 | 33878 |
| 83 | [decolua/9router](https://github.com/decolua/9router) | +841 | 10256 |
| 84 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +832 | 10648 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +831 | 33339 |
| 86 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +824 | 60679 |
| 87 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +814 | 47122 |
| 88 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +811 | 14653 |
| 89 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +811 | 37330 |
| 90 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +804 | 67707 |
| 91 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +801 | 32834 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +771 | 35919 |
| 93 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +761 | 5755 |
| 94 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +758 | 45886 |
| 95 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +749 | 7322 |
| 96 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +749 | 5895 |
| 97 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +737 | 7421 |
| 98 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +716 | 10834 |
| 99 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +713 | 6101 |
| 100 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +696 | 7634 |
| 101 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +688 | 8898 |
| 102 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +660 | 7202 |
| 103 | [google/magika](https://github.com/google/magika) | +646 | 17000 |
| 104 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +639 | 37529 |
| 105 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +632 | 21254 |
| 106 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +619 | 20579 |
| 107 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +608 | 43722 |
| 108 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +599 | 6049 |
| 109 | [floci-io/floci](https://github.com/floci-io/floci) | +596 | 10471 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +580 | 14114 |
| 111 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +575 | 5064 |
| 112 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +566 | 6674 |
| 113 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +564 | 25821 |
| 114 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +563 | 18632 |
| 115 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +547 | 20186 |
| 116 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +547 | 17915 |
| 117 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +537 | 34453 |
| 118 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +520 | 14810 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +515 | 13322 |
| 120 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +504 | 5007 |
| 121 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +501 | 7177 |
| 122 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +495 | 31295 |
| 123 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +482 | 22767 |
| 124 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +447 | 36799 |
| 125 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +440 | 36907 |
| 126 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +439 | 5154 |
| 127 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +433 | 12531 |
| 128 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +431 | 17199 |
| 129 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +424 | 4920 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +415 | 39841 |
| 131 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +406 | 2622 |
| 132 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +402 | 3191 |
| 133 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +393 | 32984 |
| 134 | [z-lab/dflash](https://github.com/z-lab/dflash) | +391 | 4561 |
| 135 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +381 | 3317 |
| 136 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +378 | 13239 |
| 137 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +377 | 27274 |
| 138 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +376 | 42463 |
| 139 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +370 | 9064 |
| 140 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +362 | 4869 |
| 141 | [browserbase/skills](https://github.com/browserbase/skills) | +361 | 3235 |
| 142 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +359 | 9747 |
| 143 | [google-research/timesfm](https://github.com/google-research/timesfm) | +358 | 19783 |
| 144 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +357 | 4176 |
| 145 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +353 | 7589 |
| 146 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +351 | 21253 |
| 147 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +346 | 32055 |
| 148 | [PostHog/posthog](https://github.com/PostHog/posthog) | +345 | 31767 |
| 149 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +343 | 21727 |
| 150 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +336 | 13348 |
| 151 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +333 | 2361 |
| 152 | [OpenMOSS/MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | +331 | 2971 |
| 153 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +328 | 2721 |
| 154 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +323 | 19372 |
| 155 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +323 | 3873 |
| 156 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +317 | 21484 |
| 157 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +317 | 18602 |
| 158 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +315 | 3555 |
| 159 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +313 | 1624 |
| 160 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +312 | 26688 |
| 161 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +310 | 37564 |
| 162 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +308 | 3782 |
| 163 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +307 | 2497 |
| 164 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +306 | 22795 |
| 165 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +304 | 9347 |
| 166 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +297 | 25279 |
| 167 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +294 | 4306 |
| 168 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +292 | 19510 |
| 169 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +290 | 5924 |
| 170 | [openai/skills](https://github.com/openai/skills) | +289 | 19108 |
| 171 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +289 | 4938 |
| 172 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +286 | 2133 |
| 173 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +281 | 2092 |
| 174 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +281 | 2095 |
| 175 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +274 | 1948 |
| 176 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +266 | 1645 |
| 177 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +258 | 4037 |
| 178 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +255 | 27589 |
| 179 | [88lin/video_vip](https://github.com/88lin/video_vip) | +236 | 1800 |
| 180 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +232 | 2310 |
| 181 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +232 | 6886 |
| 182 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +229 | 3570 |
| 183 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +228 | 1849 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +226 | 13829 |
| 185 | [tiagozip/cap](https://github.com/tiagozip/cap) | +217 | 6360 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +215 | 4284 |
| 187 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +209 | 26575 |
| 188 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +200 | 3095 |
| 189 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +198 | 10193 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +195 | 36103 |
| 191 | [eze-is/web-access](https://github.com/eze-is/web-access) | +192 | 6407 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +184 | 2471 |
| 193 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +183 | 3447 |
| 194 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +150 | 5819 |
| 195 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +150 | 16599 |
| 196 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +149 | 7818 |
| 197 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +146 | 2834 |
| 198 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +146 | 7747 |
| 199 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +142 | 9810 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +142 | 8750 |
| 201 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +138 | 1267 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +138 | 39596 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +137 | 15042 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +137 | 22873 |
| 205 | [playcanvas/engine](https://github.com/playcanvas/engine) | +135 | 15769 |
| 206 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +134 | 1170 |
| 207 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +134 | 3332 |
| 208 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +123 | 866 |
| 209 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +110 | 1302 |
| 210 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +109 | 40265 |
| 211 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +109 | 678 |
| 212 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +109 | 722 |
| 213 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +105 | 35473 |
| 214 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +102 | 779 |
| 215 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +101 | 3740 |
| 216 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +101 | 1369 |
| 217 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +101 | 3118 |
| 218 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +100 | 852 |
| 219 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +99 | 10224 |
| 220 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +97 | 11713 |
| 221 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 1783 |
| 222 | [sandeco/reversa](https://github.com/sandeco/reversa) | +93 | 790 |
| 223 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +92 | 23923 |
| 224 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +90 | 731 |
| 225 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +87 | 866 |
| 226 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +84 | 30069 |
| 227 | [usebruno/bruno](https://github.com/usebruno/bruno) | +83 | 41086 |
| 228 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +80 | 8271 |
| 229 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +77 | 2091 |
| 230 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +75 | 3732 |
| 231 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +73 | 2071 |
| 232 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +71 | 4243 |
| 233 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +70 | 470 |
| 234 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +70 | 2544 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +69 | 13268 |
| 236 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +69 | 437 |
| 237 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +69 | 37313 |
| 238 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2387 |
| 239 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 240 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +65 | 48784 |
| 241 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +63 | 645 |
| 242 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +63 | 1773 |
| 243 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +62 | 1765 |
| 244 | [halo-dev/halo](https://github.com/halo-dev/halo) | +62 | 37991 |
| 245 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +59 | 2712 |
| 246 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +58 | 778 |
| 247 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +58 | 3078 |
| 248 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +58 | 11152 |
| 249 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +58 | 33000 |
| 250 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +57 | 2065 |
| 251 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2420 |
| 252 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +56 | 4137 |
| 253 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +56 | 27551 |
| 254 | [openmemind/memind](https://github.com/openmemind/memind) | +54 | 737 |
| 255 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +53 | 867 |
| 256 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +53 | 1402 |
| 257 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +53 | 4058 |
| 258 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 465 |
| 259 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +52 | 2974 |
| 260 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +52 | 311 |
| 261 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +51 | 1661 |
| 262 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +50 | 902 |
| 263 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +50 | 459 |
| 264 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +50 | 352 |
| 265 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +49 | 505 |
| 266 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 427 |
| 267 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +48 | 291 |
| 268 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +48 | 1653 |
| 269 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +47 | 4161 |
| 270 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +47 | 11996 |
| 271 | [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | +46 | 3646 |
| 272 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +45 | 311 |
| 273 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +44 | 9605 |
| 274 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +43 | 2120 |
| 275 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +41 | 308 |
| 276 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +38 | 5097 |
| 277 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +37 | 2359 |
| 278 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +37 | 1860 |
| 279 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +37 | 5330 |
| 280 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +36 | 234 |
| 281 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +36 | 1383 |
| 282 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +36 | 430 |
| 283 | [WsttXm/RiskEngine](https://github.com/WsttXm/RiskEngine) | +36 | 193 |
| 284 | [dedicatedcode/reitti](https://github.com/dedicatedcode/reitti) | +34 | 2208 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +33 | 1533 |
| 286 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +31 | 271 |
| 287 | [intave/intave](https://github.com/intave/intave) | +30 | 250 |
| 288 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +28 | 749 |
| 289 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +28 | 184 |
| 290 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +28 | 1907 |
| 291 | [is-a-dev/register](https://github.com/is-a-dev/register) | +27 | 10287 |
| 292 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2181 |
| 293 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +23 | 846 |
| 294 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +23 | 430 |
| 295 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +22 | 206 |
| 296 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +21 | 2617 |
| 297 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +21 | 2923 |
| 298 | [supermalparit/Towns](https://github.com/supermalparit/Towns) | +21 | 144 |
| 299 | [vincentchen2026/claude-code-java](https://github.com/vincentchen2026/claude-code-java) | +21 | 116 |
| 300 | [acoder-ai-infra/AGenUI](https://github.com/acoder-ai-infra/AGenUI) | +20 | 283 |
