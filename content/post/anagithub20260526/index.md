---
title: "2026-05-26 GitHub增长趋势报告"
description: "1.Understand-Anything+300 2.codegraph+224 3.ai-engineering-from-scratch+151 4.knowledge-work-plugins+108 5.taste-skill+81"
date: 2026-05-26T21:46:58+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-26 21:46:58

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
        'daily': {"categories": ["fathah/hermes-desktop", "CloakHQ/CloakBrowser", "rtk-ai/rtk", "shiyu-coder/Kronos", "Alishahryar1/free-claude-code", "tashfeenahmed/freellmapi", "greensock/gsap-skills", "Hmbown/CodeWhale", "tinyhumansai/openhuman", "safishamsi/graphify", "Yuan1z0825/nature-skills", "Axorax/awesome-free-apps", "Imbad0202/academic-research-skills", "mukul975/Anthropic-Cybersecurity-Skills", "NangoHQ/nango", "Leonxlnx/taste-skill", "anthropics/knowledge-work-plugins", "rohitg00/ai-engineering-from-scratch", "colbymchenry/codegraph", "Lum1104/Understand-Anything"], "data": [25, 25, 25, 25, 26, 26, 28, 28, 36, 39, 43, 50, 50, 52, 53, 81, 108, 151, 224, 300]},
        'weekly': {"categories": ["Fincept-Corporation/FinceptTerminal", "Yuan1z0825/nature-skills", "Hmbown/CodeWhale", "manaflow-ai/cmux", "rtk-ai/rtk", "multica-ai/multica", "tashfeenahmed/freellmapi", "mukul975/Anthropic-Cybersecurity-Skills", "Alishahryar1/free-claude-code", "anthropics/knowledge-work-plugins", "rohitg00/agentmemory", "safishamsi/graphify", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman", "anthropics/claude-plugins-official", "rohitg00/ai-engineering-from-scratch", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "Lum1104/Understand-Anything"], "data": [245, 249, 250, 257, 263, 302, 306, 319, 321, 358, 377, 393, 459, 628, 657, 797, 1102, 1696, 1883, 1883]},
        'monthly': {"categories": ["msitarzewski/agency-agents", "anthropics/financial-services", "garrytan/gstack", "VoltAgent/awesome-design-md", "Alishahryar1/free-claude-code", "safishamsi/graphify", "tinyhumansai/openhuman", "colbymchenry/codegraph", "addyosmani/agent-skills", "Lum1104/Understand-Anything", "ruvnet/ruflo", "affaan-m/ECC", "farion1231/cc-switch", "warpdotdev/warp", "TauricResearch/TradingAgents", "Hmbown/CodeWhale", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1918, 1971, 1988, 2013, 2066, 2070, 2172, 2339, 2344, 2621, 2660, 2896, 2975, 3216, 3234, 3401, 3825, 5231, 7287, 8423]}
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
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +300 | 35492 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +224 | 27567 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +151 | 20591 |
| 4 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +108 | 16599 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +81 | 21358 |
| 6 | [NangoHQ/nango](https://github.com/NangoHQ/nango) | +53 | 8919 |
| 7 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +52 | 10022 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +50 | 22127 |
| 9 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +50 | 5190 |
| 10 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +43 | 12553 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +39 | 54292 |
| 12 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +36 | 28277 |
| 13 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +28 | 35043 |
| 14 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +28 | 4791 |
| 15 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +26 | 5562 |
| 16 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +26 | 30006 |
| 17 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +25 | 26459 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +25 | 54606 |
| 19 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +25 | 21398 |
| 20 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +25 | 7635 |
| 21 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +25 | 27960 |
| 22 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +24 | 18186 |
| 23 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +22 | 3639 |
| 24 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +22 | 19795 |
| 25 | [yuanzhongqiao/deep-printfilm](https://github.com/yuanzhongqiao/deep-printfilm) | +21 | 1269 |
| 26 | [multica-ai/multica](https://github.com/multica-ai/multica) | +21 | 33324 |
| 27 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +20 | 19959 |
| 28 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +20 | 40595 |
| 29 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +19 | 21722 |
| 30 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +19 | 1058 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1883 | 35492 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1883 | 27567 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1696 | 156957 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1102 | 20591 |
| 5 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +797 | 27960 |
| 6 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +657 | 28277 |
| 7 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +628 | 22127 |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +459 | 21398 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +393 | 54292 |
| 10 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +377 | 18186 |
| 11 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +358 | 16599 |
| 12 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +321 | 30006 |
| 13 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +319 | 10022 |
| 14 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +306 | 5562 |
| 15 | [multica-ai/multica](https://github.com/multica-ai/multica) | +302 | 33324 |
| 16 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +263 | 54606 |
| 17 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +257 | 19795 |
| 18 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +250 | 35043 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +249 | 12553 |
| 20 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +245 | 24167 |
| 21 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +229 | 3230 |
| 22 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +226 | 7511 |
| 23 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +218 | 40595 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +217 | 21360 |
| 25 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +216 | 7618 |
| 26 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +199 | 4756 |
| 27 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +194 | 2510 |
| 28 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +193 | 21358 |
| 29 | [decolua/9router](https://github.com/decolua/9router) | +192 | 14534 |
| 30 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +189 | 2341 |
| 31 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +184 | 10626 |
| 32 | [presenton/presenton](https://github.com/presenton/presenton) | +184 | 7066 |
| 33 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +182 | 41851 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +181 | 53719 |
| 35 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +170 | 3435 |
| 36 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +169 | 6496 |
| 37 | [withcoral/coral](https://github.com/withcoral/coral) | +168 | 4908 |
| 38 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +167 | 46039 |
| 39 | [88lin/video_vip](https://github.com/88lin/video_vip) | +165 | 3207 |
| 40 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +163 | 27774 |
| 41 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +154 | 28550 |
| 42 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +145 | 14801 |
| 43 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +135 | 19959 |
| 44 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +134 | 23676 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +132 | 19157 |
| 46 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +131 | 11869 |
| 47 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +131 | 21378 |
| 48 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +131 | 6659 |
| 49 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +128 | 12282 |
| 50 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +128 | 3019 |
| 51 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +127 | 1632 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +126 | 30436 |
| 53 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +125 | 40370 |
| 54 | [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | +125 | 30432 |
| 55 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +124 | 62801 |
| 56 | [dotnet/skills](https://github.com/dotnet/skills) | +124 | 3106 |
| 57 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +123 | 4897 |
| 58 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +120 | 7635 |
| 59 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +120 | 15211 |
| 60 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +118 | 26068 |
| 61 | [santifer/career-ops](https://github.com/santifer/career-ops) | +118 | 47357 |
| 62 | [Achilng/floral-notepaper](https://github.com/Achilng/floral-notepaper) | +116 | 2560 |
| 63 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +116 | 35551 |
| 64 | [MinishLab/semble](https://github.com/MinishLab/semble) | +111 | 4369 |
| 65 | [antirez/ds4](https://github.com/antirez/ds4) | +107 | 11998 |
| 66 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +107 | 21390 |
| 67 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +107 | 4561 |
| 68 | [blader/humanizer](https://github.com/blader/humanizer) | +105 | 21050 |
| 69 | [google/ax](https://github.com/google/ax) | +100 | 1076 |
| 70 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +99 | 5086 |
| 71 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +98 | 920 |
| 72 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +97 | 6562 |
| 73 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +97 | 4791 |
| 74 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +96 | 55007 |
| 75 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +96 | 9417 |
| 76 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +92 | 1117 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +92 | 30630 |
| 78 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +92 | 2040 |
| 79 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +91 | 34916 |
| 80 | [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | +90 | 2263 |
| 81 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +90 | 33156 |
| 82 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +90 | 25521 |
| 83 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +89 | 1037 |
| 84 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +89 | 5150 |
| 85 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +88 | 26459 |
| 86 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +88 | 13012 |
| 87 | [soxoj/maigret](https://github.com/soxoj/maigret) | +87 | 30525 |
| 88 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +85 | 1058 |
| 89 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +84 | 5191 |
| 90 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +81 | 38970 |
| 91 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +81 | 8800 |
| 92 | [openai/skills](https://github.com/openai/skills) | +80 | 20391 |
| 93 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +79 | 2516 |
| 94 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +79 | 4778 |
| 95 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +76 | 8762 |
| 96 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +76 | 4571 |
| 97 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +76 | 1940 |
| 98 | [virattt/dexter](https://github.com/virattt/dexter) | +75 | 26527 |
| 99 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +73 | 2479 |
| 100 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +73 | 14683 |
| 101 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +70 | 26694 |
| 102 | [XiaoLuoLYG/GOD](https://github.com/XiaoLuoLYG/GOD) | +69 | 516 |
| 103 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +68 | 38811 |
| 104 | [tate233/todolist](https://github.com/tate233/todolist) | +67 | 778 |
| 105 | [lynote-ai/humanize-text](https://github.com/lynote-ai/humanize-text) | +67 | 802 |
| 106 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +64 | 8859 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +61 | 16264 |
| 108 | [jundot/omlx](https://github.com/jundot/omlx) | +61 | 15238 |
| 109 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +61 | 11838 |
| 110 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +60 | 2477 |
| 111 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +60 | 7705 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +60 | 44877 |
| 113 | [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | +59 | 1044 |
| 114 | [viticci/shortcuts-playground-plugin](https://github.com/viticci/shortcuts-playground-plugin) | +59 | 680 |
| 115 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +58 | 1813 |
| 116 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +57 | 34271 |
| 117 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +57 | 4232 |
| 118 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +57 | 5695 |
| 119 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +57 | 8841 |
| 120 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +54 | 1862 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8423 | 106803 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +7287 | 156957 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5231 | 168579 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3825 | 60312 |
| 5 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3401 | 35043 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3234 | 30590 |
| 7 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3216 | 60076 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2975 | 81709 |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2896 | 51199 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2660 | 55427 |
| 11 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2621 | 35493 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2344 | 46039 |
| 13 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2339 | 27567 |
| 14 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2172 | 28277 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2070 | 54292 |
| 16 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2066 | 30006 |
| 17 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2013 | 84460 |
| 18 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1988 | 103195 |
| 19 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1971 | 27774 |
| 20 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1918 | 105288 |
| 21 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1801 | 21398 |
| 22 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1786 | 54342 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1731 | 54606 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1688 | 109881 |
| 25 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1687 | 65137 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +1640 | 74774 |
| 27 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1526 | 22127 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1508 | 55517 |
| 29 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1492 | 55070 |
| 30 | [github/spec-kit](https://github.com/github/spec-kit) | +1490 | 71722 |
| 31 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1476 | 20591 |
| 32 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1448 | 19959 |
| 33 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1423 | 18186 |
| 34 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1400 | 30525 |
| 35 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1395 | 66283 |
| 36 | [antirez/ds4](https://github.com/antirez/ds4) | +1336 | 11998 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1336 | 53719 |
| 38 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1316 | 85286 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1272 | 21360 |
| 40 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1262 | 15560 |
| 41 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1249 | 40370 |
| 42 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1221 | 34148 |
| 43 | [decolua/9router](https://github.com/decolua/9router) | +1178 | 14534 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1172 | 33324 |
| 45 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1151 | 30678 |
| 46 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1086 | 24167 |
| 47 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1084 | 12553 |
| 48 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1030 | 11869 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1026 | 21378 |
| 50 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1002 | 27960 |
| 51 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +947 | 17020 |
| 52 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +917 | 67782 |
| 53 | [openai/symphony](https://github.com/openai/symphony) | +916 | 24664 |
| 54 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +893 | 14801 |
| 55 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +874 | 15200 |
| 56 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +844 | 23676 |
| 57 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +823 | 11522 |
| 58 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +807 | 30436 |
| 59 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +800 | 12282 |
| 60 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +777 | 21358 |
| 61 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +771 | 13824 |
| 62 | [santifer/career-ops](https://github.com/santifer/career-ops) | +768 | 47357 |
| 63 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +764 | 19157 |
| 64 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +759 | 50948 |
| 65 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +752 | 6568 |
| 66 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +751 | 55008 |
| 67 | [floci-io/floci](https://github.com/floci-io/floci) | +746 | 13091 |
| 68 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +720 | 6563 |
| 69 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +711 | 10626 |
| 70 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +704 | 8762 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +699 | 38970 |
| 72 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +694 | 35551 |
| 73 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +684 | 16625 |
| 74 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +673 | 63699 |
| 75 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +665 | 7701 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +659 | 33156 |
| 77 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +652 | 35353 |
| 78 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +648 | 47451 |
| 79 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +646 | 40595 |
| 80 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +645 | 21390 |
| 81 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +633 | 7635 |
| 82 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +626 | 26068 |
| 83 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +614 | 62801 |
| 84 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +604 | 62636 |
| 85 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +602 | 22702 |
| 86 | [virattt/dexter](https://github.com/virattt/dexter) | +600 | 26527 |
| 87 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +594 | 11838 |
| 88 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +592 | 51085 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +590 | 30630 |
| 90 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +589 | 5150 |
| 91 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +588 | 34916 |
| 92 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +562 | 12156 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +556 | 9417 |
| 94 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +551 | 4272 |
| 95 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +548 | 6659 |
| 96 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +544 | 6205 |
| 97 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +525 | 28550 |
| 98 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +523 | 34271 |
| 99 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +516 | 18781 |
| 100 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +507 | 41851 |
| 101 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +506 | 26459 |
| 102 | [withcoral/coral](https://github.com/withcoral/coral) | +492 | 4908 |
| 103 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +457 | 17449 |
| 104 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +453 | 16599 |
| 105 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +453 | 19907 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +446 | 8800 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +445 | 32179 |
| 108 | [jundot/omlx](https://github.com/jundot/omlx) | +421 | 15238 |
| 109 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +418 | 7618 |
| 110 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +393 | 4897 |
| 111 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +391 | 10022 |
| 112 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +390 | 6585 |
| 113 | [browser-use/video-use](https://github.com/browser-use/video-use) | +389 | 8446 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +387 | 14683 |
| 115 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +383 | 7992 |
| 116 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +380 | 44877 |
| 117 | [browserbase/skills](https://github.com/browserbase/skills) | +376 | 3438 |
| 118 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +366 | 19712 |
| 119 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +361 | 38811 |
| 120 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +360 | 10064 |
| 121 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +347 | 4756 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +345 | 15211 |
| 123 | [MinishLab/semble](https://github.com/MinishLab/semble) | +342 | 4369 |
| 124 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +339 | 16264 |
| 125 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +326 | 5841 |
| 126 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +324 | 13396 |
| 127 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +323 | 4778 |
| 128 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +322 | 4572 |
| 129 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +322 | 24321 |
| 130 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +317 | 3964 |
| 131 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +317 | 21618 |
| 132 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +316 | 4649 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +311 | 36799 |
| 134 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +310 | 9933 |
| 135 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +298 | 23776 |
| 136 | [openai/skills](https://github.com/openai/skills) | +292 | 20391 |
| 137 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +292 | 22337 |
| 138 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +290 | 8841 |
| 139 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +289 | 26585 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +286 | 22135 |
| 141 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +286 | 4925 |
| 142 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +285 | 2362 |
| 143 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +284 | 33168 |
| 144 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +275 | 2479 |
| 145 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +273 | 10738 |
| 146 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +273 | 3749 |
| 147 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +268 | 33055 |
| 148 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +266 | 27376 |
| 149 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +265 | 5259 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +264 | 33875 |
| 151 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +264 | 4232 |
| 152 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +262 | 5932 |
| 153 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +261 | 2567 |
| 154 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +260 | 2477 |
| 155 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +258 | 7111 |
| 156 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +250 | 4024 |
| 157 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +248 | 7705 |
| 158 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +248 | 2628 |
| 159 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +247 | 27586 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +242 | 26017 |
| 161 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +239 | 26130 |
| 162 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 1971 |
| 163 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +233 | 6810 |
| 164 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +233 | 4281 |
| 165 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +231 | 43199 |
| 166 | [z-lab/dflash](https://github.com/z-lab/dflash) | +228 | 4716 |
| 167 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +227 | 3126 |
| 168 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +222 | 5585 |
| 169 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +222 | 28374 |
| 170 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +221 | 20334 |
| 171 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +218 | 6602 |
| 172 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +215 | 3237 |
| 173 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +205 | 4500 |
| 174 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +205 | 37564 |
| 175 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +201 | 1862 |
| 176 | [88lin/video_vip](https://github.com/88lin/video_vip) | +200 | 3207 |
| 177 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +198 | 13142 |
| 178 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +196 | 2510 |
| 179 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +195 | 1590 |
| 180 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +191 | 7291 |
| 181 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +188 | 2286 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +184 | 14576 |
| 183 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +182 | 1941 |
| 184 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +177 | 2480 |
| 185 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +171 | 3435 |
| 186 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +171 | 4888 |
| 187 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +162 | 6252 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +157 | 27144 |
| 189 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +153 | 5208 |
| 190 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +146 | 3797 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +142 | 36103 |
| 192 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +139 | 2198 |
| 193 | [tiagozip/cap](https://github.com/tiagozip/cap) | +137 | 6622 |
| 194 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +136 | 4779 |
| 195 | [playcanvas/engine](https://github.com/playcanvas/engine) | +134 | 15885 |
| 196 | [sandeco/reversa](https://github.com/sandeco/reversa) | +130 | 1086 |
| 197 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +127 | 17213 |
| 198 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +121 | 15369 |
| 199 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +119 | 10061 |
| 200 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +117 | 10520 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +116 | 8516 |
| 202 | [usebruno/bruno](https://github.com/usebruno/bruno) | +115 | 41086 |
| 203 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +114 | 2976 |
| 204 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +113 | 1685 |
| 205 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +113 | 23255 |
| 206 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +111 | 1702 |
| 207 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +108 | 1352 |
| 208 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +108 | 2074 |
| 209 | [eze-is/web-access](https://github.com/eze-is/web-access) | +107 | 6846 |
| 210 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +107 | 856 |
| 211 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +104 | 39596 |
| 212 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +99 | 11869 |
| 213 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +97 | 5191 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +95 | 2077 |
| 215 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +94 | 3174 |
| 216 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 757 |
| 217 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +92 | 944 |
| 218 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +89 | 40265 |
| 219 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +84 | 3173 |
| 220 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +82 | 3639 |
| 221 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +81 | 10042 |
| 222 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +80 | 14926 |
| 223 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +80 | 7566 |
| 224 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +78 | 1689 |
| 225 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +76 | 10474 |
| 226 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +73 | 35473 |
| 227 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +72 | 4576 |
| 228 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +71 | 1045 |
| 229 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +71 | 4524 |
| 230 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +69 | 8037 |
| 231 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +67 | 573 |
| 232 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2452 |
| 233 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +65 | 11899 |
| 234 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +65 | 37313 |
| 235 | [qist/tvbox](https://github.com/qist/tvbox) | +62 | 9483 |
| 236 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 237 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +59 | 8488 |
| 238 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +59 | 30229 |
| 239 | [halo-dev/halo](https://github.com/halo-dev/halo) | +59 | 37991 |
| 240 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +58 | 3997 |
| 241 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +57 | 45263 |
| 242 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2614 |
| 243 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +55 | 3261 |
| 244 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +54 | 525 |
| 245 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +53 | 4677 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +52 | 13449 |
| 247 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +52 | 33000 |
| 248 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 249 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 306 |
| 250 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +50 | 350 |
| 251 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 486 |
| 252 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +48 | 601 |
| 253 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +47 | 2369 |
| 254 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +46 | 3294 |
| 255 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +45 | 1006 |
| 256 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 338 |
| 257 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +44 | 2244 |
| 258 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 339 |
| 259 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +42 | 1830 |
| 260 | [Gracker/SmartPerfetto](https://github.com/Gracker/SmartPerfetto) | +42 | 452 |
| 261 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +41 | 1116 |
| 262 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +41 | 659 |
| 263 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +41 | 2290 |
| 264 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +40 | 4231 |
| 265 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +40 | 491 |
| 266 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +39 | 1521 |
| 267 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +39 | 463 |
| 268 | [openmemind/memind](https://github.com/openmemind/memind) | +38 | 850 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +37 | 2236 |
| 270 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +37 | 514 |
| 271 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +37 | 2541 |
| 272 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +36 | 358 |
| 273 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +36 | 1391 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +36 | 9760 |
| 275 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +35 | 5183 |
| 276 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +35 | 1995 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +34 | 1458 |
| 278 | [FongMi/TV](https://github.com/FongMi/TV) | +34 | 8085 |
| 279 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +33 | 864 |
| 280 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +33 | 275 |
| 281 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 281 |
| 282 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 752 |
| 283 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +29 | 743 |
| 284 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +27 | 311 |
| 285 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +27 | 771 |
| 286 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2227 |
| 287 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +25 | 1551 |
| 288 | [is-a-dev/register](https://github.com/is-a-dev/register) | +22 | 10358 |
| 289 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +21 | 2432 |
| 290 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 291 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +21 | 2639 |
| 292 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +20 | 190 |
| 293 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +18 | 509 |
| 294 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +17 | 5167 |
| 295 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +17 | 2955 |
| 296 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +17 | 334 |
| 297 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +16 | 1973 |
| 298 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +16 | 245 |
| 299 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +16 | 229 |
| 300 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +15 | 311 |
