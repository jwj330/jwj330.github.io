---
title: "2026-05-25 GitHub增长趋势报告"
description: "1.Understand-Anything+606 2.ai-engineering-from-scratch+328 3.codegraph+327 4.knowledge-work-plugins+142 5.academic-research-skills+102"
date: 2026-05-25T21:10:46+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-25 21:10:46

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
        'daily': {"categories": ["K-Dense-AI/scientific-agent-skills", "withcoral/coral", "rtk-ai/rtk", "hugohe3/ppt-master", "st-tech/ppf-contact-solver", "Hmbown/CodeWhale", "multica-ai/multica", "Alishahryar1/free-claude-code", "rohitg00/agentmemory", "safishamsi/graphify", "manaflow-ai/cmux", "anthropics/claude-plugins-official", "CloakHQ/CloakBrowser", "mukul975/Anthropic-Cybersecurity-Skills", "tinyhumansai/openhuman", "Imbad0202/academic-research-skills", "anthropics/knowledge-work-plugins", "colbymchenry/codegraph", "rohitg00/ai-engineering-from-scratch", "Lum1104/Understand-Anything"], "data": [38, 40, 41, 49, 50, 51, 60, 63, 65, 67, 73, 82, 87, 91, 101, 102, 142, 327, 328, 606]},
        'weekly': {"categories": ["manaflow-ai/cmux", "truelockmc/streambert", "Hmbown/CodeWhale", "HKUDS/CLI-Anything", "anthropics/knowledge-work-plugins", "rtk-ai/rtk", "mukul975/Anthropic-Cybersecurity-Skills", "tashfeenahmed/freellmapi", "multica-ai/multica", "Alishahryar1/free-claude-code", "safishamsi/graphify", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "Imbad0202/academic-research-skills", "anthropics/claude-plugins-official", "tinyhumansai/openhuman", "rohitg00/ai-engineering-from-scratch", "Lum1104/Understand-Anything", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph"], "data": [242, 244, 244, 250, 254, 268, 272, 296, 301, 313, 367, 434, 500, 713, 781, 790, 960, 1616, 1631, 1734]},
        'monthly': {"categories": ["anthropics/financial-services", "msitarzewski/agency-agents", "garrytan/gstack", "colbymchenry/codegraph", "tinyhumansai/openhuman", "VoltAgent/awesome-design-md", "safishamsi/graphify", "Lum1104/Understand-Anything", "addyosmani/agent-skills", "Alishahryar1/free-claude-code", "ruvnet/ruflo", "affaan-m/ECC", "farion1231/cc-switch", "warpdotdev/warp", "TauricResearch/TradingAgents", "Hmbown/CodeWhale", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1959, 1994, 2104, 2126, 2144, 2151, 2158, 2394, 2397, 2569, 2698, 2953, 3063, 3206, 3305, 3381, 3952, 5534, 8092, 8926]}
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
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +606 | 30677 |
| 2 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +328 | 18309 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +327 | 24731 |
| 4 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +142 | 15242 |
| 5 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +102 | 21412 |
| 6 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +101 | 27748 |
| 7 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +91 | 9123 |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +87 | 20929 |
| 9 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +82 | 27736 |
| 10 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +73 | 19442 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +67 | 53648 |
| 12 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +65 | 17795 |
| 13 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +63 | 29627 |
| 14 | [multica-ai/multica](https://github.com/multica-ai/multica) | +60 | 33014 |
| 15 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +51 | 34666 |
| 16 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +50 | 3152 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +49 | 20974 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +41 | 53985 |
| 19 | [withcoral/coral](https://github.com/withcoral/coral) | +40 | 4811 |
| 20 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +38 | 25860 |
| 21 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +37 | 10433 |
| 22 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +37 | 5218 |
| 23 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +36 | 11947 |
| 24 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +35 | 977 |
| 25 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +35 | 7278 |
| 26 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +34 | 30214 |
| 27 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +34 | 40339 |
| 28 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +34 | 28367 |
| 29 | [decolua/9router](https://github.com/decolua/9router) | +33 | 14227 |
| 30 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +33 | 53378 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1734 | 24731 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1631 | 154698 |
| 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1616 | 30677 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +960 | 18309 |
| 5 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +790 | 27748 |
| 6 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +781 | 27736 |
| 7 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +713 | 21413 |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +500 | 20929 |
| 9 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +434 | 17795 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +367 | 53648 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +313 | 29627 |
| 12 | [multica-ai/multica](https://github.com/multica-ai/multica) | +301 | 33014 |
| 13 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +296 | 5218 |
| 14 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +272 | 9123 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +268 | 53985 |
| 16 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +254 | 15242 |
| 17 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +250 | 40339 |
| 18 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +244 | 34666 |
| 19 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +244 | 4712 |
| 20 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +242 | 19442 |
| 21 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +241 | 6284 |
| 22 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +240 | 7278 |
| 23 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +234 | 7509 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +232 | 11947 |
| 25 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +231 | 3091 |
| 26 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +229 | 23827 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +220 | 20974 |
| 28 | [decolua/9router](https://github.com/decolua/9router) | +205 | 14227 |
| 29 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +192 | 2416 |
| 30 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +191 | 10433 |
| 31 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +183 | 53378 |
| 32 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +183 | 27524 |
| 33 | [withcoral/coral](https://github.com/withcoral/coral) | +175 | 4812 |
| 34 | [presenton/presenton](https://github.com/presenton/presenton) | +175 | 6859 |
| 35 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +174 | 45628 |
| 36 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +173 | 41710 |
| 37 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +173 | 2137 |
| 38 | [88lin/video_vip](https://github.com/88lin/video_vip) | +162 | 3143 |
| 39 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +161 | 3152 |
| 40 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +156 | 28367 |
| 41 | [santifer/career-ops](https://github.com/santifer/career-ops) | +144 | 47209 |
| 42 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +143 | 14684 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +142 | 18930 |
| 44 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +137 | 6435 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +135 | 21103 |
| 46 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +134 | 23433 |
| 47 | [MinishLab/semble](https://github.com/MinishLab/semble) | +134 | 4259 |
| 48 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +131 | 25860 |
| 49 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +128 | 15106 |
| 50 | [Achilng/floral-notepaper](https://github.com/Achilng/floral-notepaper) | +128 | 2454 |
| 51 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +127 | 19752 |
| 52 | [dotnet/skills](https://github.com/dotnet/skills) | +125 | 3060 |
| 53 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +123 | 12004 |
| 54 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +123 | 2798 |
| 55 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +122 | 11639 |
| 56 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +122 | 40220 |
| 57 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +121 | 19578 |
| 58 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +120 | 38839 |
| 59 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +119 | 30214 |
| 60 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +119 | 62575 |
| 61 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +117 | 35357 |
| 62 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +115 | 4750 |
| 63 | [blader/humanizer](https://github.com/blader/humanizer) | +113 | 20902 |
| 64 | [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | +113 | 30432 |
| 65 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +112 | 1491 |
| 66 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +112 | 4944 |
| 67 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +111 | 4505 |
| 68 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +107 | 21228 |
| 69 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +106 | 2152 |
| 70 | [antirez/ds4](https://github.com/antirez/ds4) | +105 | 11831 |
| 71 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +103 | 7066 |
| 72 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +103 | 9259 |
| 73 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +102 | 54822 |
| 74 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +97 | 6480 |
| 75 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +96 | 33006 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +96 | 25357 |
| 77 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +90 | 850 |
| 78 | [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | +89 | 2227 |
| 79 | [google/ax](https://github.com/google/ax) | +89 | 958 |
| 80 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +89 | 12918 |
| 81 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +87 | 1000 |
| 82 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +87 | 30473 |
| 83 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +87 | 1993 |
| 84 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +86 | 5007 |
| 85 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +84 | 34743 |
| 86 | [soxoj/maigret](https://github.com/soxoj/maigret) | +84 | 30358 |
| 87 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +80 | 4332 |
| 88 | [openai/skills](https://github.com/openai/skills) | +80 | 20273 |
| 89 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +80 | 7614 |
| 90 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +79 | 977 |
| 91 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +79 | 2412 |
| 92 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +79 | 18918 |
| 93 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +77 | 26547 |
| 94 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +76 | 1814 |
| 95 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +76 | 20033 |
| 96 | [virattt/dexter](https://github.com/virattt/dexter) | +75 | 26480 |
| 97 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +75 | 8662 |
| 98 | [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | +74 | 9211 |
| 99 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +73 | 8663 |
| 100 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +73 | 8809 |
| 101 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +72 | 4715 |
| 102 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +71 | 2177 |
| 103 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +69 | 38676 |
| 104 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +66 | 652 |
| 105 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +66 | 1765 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +65 | 16174 |
| 107 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +63 | 26000 |
| 108 | [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | +63 | 1026 |
| 109 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +63 | 11738 |
| 110 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +62 | 4185 |
| 111 | [jundot/omlx](https://github.com/jundot/omlx) | +60 | 15146 |
| 112 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +60 | 44792 |
| 113 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +59 | 34180 |
| 114 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +59 | 14556 |
| 115 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +58 | 1663 |
| 116 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +57 | 2385 |
| 117 | [viticci/shortcuts-playground-plugin](https://github.com/viticci/shortcuts-playground-plugin) | +56 | 638 |
| 118 | [tate233/todolist](https://github.com/tate233/todolist) | +55 | 499 |
| 119 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +55 | 2360 |
| 120 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +55 | 5667 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8926 | 105109 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8092 | 154698 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5534 | 167113 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3952 | 60312 |
| 5 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3381 | 34666 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3305 | 30590 |
| 7 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3206 | 59930 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3063 | 80678 |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2953 | 51199 |
| 10 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2698 | 55039 |
| 11 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2569 | 29628 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2397 | 45628 |
| 13 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2394 | 30677 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2158 | 53648 |
| 15 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2151 | 84008 |
| 16 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2144 | 27748 |
| 17 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2126 | 24731 |
| 18 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2104 | 102363 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1994 | 105025 |
| 20 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1959 | 27524 |
| 21 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1915 | 53985 |
| 22 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1886 | 55070 |
| 23 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1840 | 64666 |
| 24 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1802 | 54139 |
| 25 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1783 | 20929 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1769 | 109881 |
| 27 | [anthropics/skills](https://github.com/anthropics/skills) | +1702 | 74774 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1581 | 54601 |
| 29 | [github/spec-kit](https://github.com/github/spec-kit) | +1501 | 71722 |
| 30 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1487 | 21413 |
| 31 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1464 | 19752 |
| 32 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1416 | 15498 |
| 33 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1410 | 17795 |
| 34 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1405 | 40220 |
| 35 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1399 | 65877 |
| 36 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1391 | 30358 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1369 | 53378 |
| 38 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1365 | 18309 |
| 39 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1345 | 85286 |
| 40 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1342 | 20974 |
| 41 | [antirez/ds4](https://github.com/antirez/ds4) | +1325 | 11831 |
| 42 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1285 | 34148 |
| 43 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1274 | 30678 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1249 | 33014 |
| 45 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1225 | 11487 |
| 46 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1224 | 23827 |
| 47 | [decolua/9router](https://github.com/decolua/9router) | +1173 | 14227 |
| 48 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1156 | 21103 |
| 49 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1126 | 11639 |
| 50 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1107 | 16915 |
| 51 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1043 | 11947 |
| 52 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1003 | 15036 |
| 53 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1002 | 27736 |
| 54 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +961 | 67612 |
| 55 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +948 | 14684 |
| 56 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +931 | 12004 |
| 57 | [openai/symphony](https://github.com/openai/symphony) | +917 | 24604 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +878 | 23433 |
| 59 | [santifer/career-ops](https://github.com/santifer/career-ops) | +864 | 47209 |
| 60 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +864 | 13735 |
| 61 | [openai/codex](https://github.com/openai/codex) | +860 | 61744 |
| 62 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +838 | 30214 |
| 63 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +792 | 18930 |
| 64 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +789 | 54822 |
| 65 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +779 | 83312 |
| 66 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +768 | 47421 |
| 67 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +764 | 50684 |
| 68 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +763 | 8663 |
| 69 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +762 | 6480 |
| 70 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +751 | 19578 |
| 71 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +749 | 6537 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +746 | 38839 |
| 73 | [floci-io/floci](https://github.com/floci-io/floci) | +744 | 13024 |
| 74 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +727 | 63703 |
| 75 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +719 | 35357 |
| 76 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +696 | 10433 |
| 77 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +692 | 33006 |
| 78 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +676 | 16481 |
| 79 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +671 | 21228 |
| 80 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +662 | 7647 |
| 81 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +653 | 62501 |
| 82 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +652 | 62575 |
| 83 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +651 | 35233 |
| 84 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +646 | 40339 |
| 85 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +641 | 51085 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +636 | 30473 |
| 87 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +631 | 37330 |
| 88 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +624 | 22606 |
| 89 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +623 | 25860 |
| 90 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +616 | 7067 |
| 91 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +615 | 12085 |
| 92 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +611 | 34743 |
| 93 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +607 | 9259 |
| 94 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +605 | 11738 |
| 95 | [virattt/dexter](https://github.com/virattt/dexter) | +603 | 26480 |
| 96 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +589 | 34180 |
| 97 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +588 | 6035 |
| 98 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +584 | 5007 |
| 99 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +574 | 6435 |
| 100 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +561 | 28367 |
| 101 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +546 | 4232 |
| 102 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +526 | 26000 |
| 103 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +519 | 18727 |
| 104 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +491 | 17383 |
| 105 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +482 | 8662 |
| 106 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +472 | 19801 |
| 107 | [browser-use/video-use](https://github.com/browser-use/video-use) | +452 | 8397 |
| 108 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +450 | 32123 |
| 109 | [jundot/omlx](https://github.com/jundot/omlx) | +434 | 15146 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +426 | 44792 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +421 | 6503 |
| 112 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +414 | 7509 |
| 113 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +414 | 4750 |
| 114 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +412 | 24302 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +408 | 14556 |
| 116 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +402 | 38676 |
| 117 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +401 | 19612 |
| 118 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +398 | 13384 |
| 119 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +383 | 7961 |
| 120 | [browserbase/skills](https://github.com/browserbase/skills) | +377 | 3426 |
| 121 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +367 | 15106 |
| 122 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +367 | 16174 |
| 123 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +361 | 10048 |
| 124 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +357 | 5804 |
| 125 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +350 | 15242 |
| 126 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +348 | 9123 |
| 127 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +344 | 4712 |
| 128 | [MinishLab/semble](https://github.com/MinishLab/semble) | +336 | 4259 |
| 129 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +332 | 36799 |
| 130 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +326 | 21575 |
| 131 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +324 | 5226 |
| 132 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +322 | 1682 |
| 133 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +321 | 27562 |
| 134 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +319 | 2765 |
| 135 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +318 | 4332 |
| 136 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +318 | 3726 |
| 137 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +317 | 4609 |
| 138 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +317 | 4715 |
| 139 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +317 | 3957 |
| 140 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +316 | 5854 |
| 141 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +309 | 26540 |
| 142 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +308 | 9725 |
| 143 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +307 | 23677 |
| 144 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +305 | 7087 |
| 145 | [openai/skills](https://github.com/openai/skills) | +302 | 20273 |
| 146 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +299 | 22268 |
| 147 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +297 | 33092 |
| 148 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +295 | 22057 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +293 | 32925 |
| 150 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +290 | 4873 |
| 151 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +289 | 4185 |
| 152 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +288 | 8809 |
| 153 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +287 | 27316 |
| 154 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +287 | 2339 |
| 155 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +276 | 10623 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +275 | 33801 |
| 157 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +273 | 2615 |
| 158 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +271 | 6770 |
| 159 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +266 | 25960 |
| 160 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +261 | 2538 |
| 161 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +256 | 2360 |
| 162 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +255 | 2385 |
| 163 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +255 | 2655 |
| 164 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +253 | 43123 |
| 165 | [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) | +250 | 2398 |
| 166 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +250 | 3906 |
| 167 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +248 | 3074 |
| 168 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +246 | 5496 |
| 169 | [z-lab/dflash](https://github.com/z-lab/dflash) | +244 | 4707 |
| 170 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +244 | 1891 |
| 171 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +242 | 7614 |
| 172 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +241 | 28309 |
| 173 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +237 | 26037 |
| 174 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 1962 |
| 175 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +234 | 4264 |
| 176 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +233 | 20264 |
| 177 | [tiagozip/cap](https://github.com/tiagozip/cap) | +229 | 6596 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +222 | 6552 |
| 179 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +222 | 37564 |
| 180 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +210 | 4433 |
| 181 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +200 | 2895 |
| 182 | [88lin/video_vip](https://github.com/88lin/video_vip) | +200 | 3143 |
| 183 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +199 | 1765 |
| 184 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +199 | 7259 |
| 185 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +196 | 2416 |
| 186 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +188 | 14479 |
| 187 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +173 | 1815 |
| 188 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +172 | 3766 |
| 189 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +170 | 27087 |
| 190 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +164 | 6220 |
| 191 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +161 | 5182 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +151 | 4758 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +144 | 36103 |
| 194 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +139 | 2152 |
| 195 | [playcanvas/engine](https://github.com/playcanvas/engine) | +137 | 15882 |
| 196 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +135 | 17114 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +134 | 15340 |
| 198 | [sandeco/reversa](https://github.com/sandeco/reversa) | +127 | 1058 |
| 199 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +125 | 10488 |
| 200 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +123 | 1667 |
| 201 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +122 | 10049 |
| 202 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +121 | 2062 |
| 203 | [usebruno/bruno](https://github.com/usebruno/bruno) | +117 | 41086 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +117 | 23226 |
| 205 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +117 | 0 |
| 206 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +113 | 2916 |
| 207 | [eze-is/web-access](https://github.com/eze-is/web-access) | +113 | 6810 |
| 208 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +111 | 39596 |
| 209 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +106 | 1342 |
| 210 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 842 |
| 211 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +101 | 11850 |
| 212 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +99 | 2056 |
| 213 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +98 | 3150 |
| 214 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +94 | 7559 |
| 215 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 756 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +93 | 40265 |
| 217 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +91 | 0 |
| 218 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +90 | 915 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +84 | 1659 |
| 220 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +82 | 4552 |
| 221 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +82 | 10025 |
| 222 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +81 | 14885 |
| 223 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +80 | 24201 |
| 224 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +78 | 10456 |
| 225 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +78 | 35473 |
| 226 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +76 | 8026 |
| 227 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +69 | 11888 |
| 228 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +69 | 4482 |
| 229 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +67 | 3972 |
| 230 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2449 |
| 231 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +66 | 1008 |
| 232 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +66 | 37313 |
| 233 | [qist/tvbox](https://github.com/qist/tvbox) | +64 | 9469 |
| 234 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +64 | 30224 |
| 235 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +63 | 48784 |
| 236 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +62 | 4659 |
| 237 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +62 | 3252 |
| 238 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +61 | 8472 |
| 239 | [halo-dev/halo](https://github.com/halo-dev/halo) | +61 | 37991 |
| 240 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +57 | 13415 |
| 241 | [robinebers/openusage](https://github.com/robinebers/openusage) | +56 | 2596 |
| 242 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +56 | 33000 |
| 243 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +56 | 45263 |
| 244 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +53 | 999 |
| 245 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +52 | 520 |
| 246 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 247 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +51 | 459 |
| 248 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 304 |
| 249 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +50 | 2240 |
| 250 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +49 | 3261 |
| 251 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +49 | 347 |
| 252 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 479 |
| 253 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +48 | 599 |
| 254 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +48 | 2344 |
| 255 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +46 | 2543 |
| 256 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 334 |
| 257 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +44 | 995 |
| 258 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +43 | 1489 |
| 259 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +43 | 4218 |
| 260 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +43 | 735 |
| 261 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 337 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +42 | 2278 |
| 263 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +41 | 1819 |
| 264 | [openmemind/memind](https://github.com/openmemind/memind) | +41 | 839 |
| 265 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +40 | 1078 |
| 266 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +40 | 479 |
| 267 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +39 | 855 |
| 268 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +39 | 655 |
| 269 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +39 | 2214 |
| 270 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +37 | 5175 |
| 271 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +37 | 429 |
| 272 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +37 | 507 |
| 273 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +36 | 1385 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +35 | 9733 |
| 275 | [FongMi/TV](https://github.com/FongMi/TV) | +35 | 8077 |
| 276 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +34 | 344 |
| 277 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +34 | 1980 |
| 278 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +34 | 1447 |
| 279 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 281 |
| 280 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +32 | 272 |
| 281 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 753 |
| 282 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +29 | 766 |
| 283 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2225 |
| 284 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +26 | 2427 |
| 285 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 308 |
| 286 | [is-a-dev/register](https://github.com/is-a-dev/register) | +25 | 10347 |
| 287 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +25 | 231 |
| 288 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +25 | 503 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +25 | 1551 |
| 290 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +23 | 1018 |
| 291 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +22 | 2633 |
| 292 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 293 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2950 |
| 294 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +19 | 333 |
| 295 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +18 | 183 |
| 296 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +18 | 0 |
| 297 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +17 | 3232 |
| 298 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +16 | 245 |
| 299 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +16 | 228 |
| 300 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +16 | 863 |
