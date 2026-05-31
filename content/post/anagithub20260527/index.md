---
title: "2026-05-27 GitHub增长趋势报告"
description: "1.Understand-Anything+231 2.taste-skill+174 3.codegraph+112 4.ai-engineering-from-scratch+109 5.English-level-up-tips+66"
date: 2026-05-27T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-31 21:08:31

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
        'daily': {"categories": ["Video-Reason/VBVR-EvalKit", "shiyu-coder/Kronos", "rohitg00/agentmemory", "hugohe3/ppt-master", "Open-Dev-Society/OpenStock", "addyosmani/agent-skills", "safishamsi/graphify", "fathah/hermes-desktop", "mukul975/Anthropic-Cybersecurity-Skills", "microsoft/agent-governance-toolkit", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman", "anthropics/knowledge-work-plugins", "russellromney/honker", "Axorax/awesome-free-apps", "byoungd/English-level-up-tips", "rohitg00/ai-engineering-from-scratch", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "Lum1104/Understand-Anything"], "data": [23, 23, 23, 24, 25, 25, 26, 26, 27, 28, 32, 34, 36, 40, 49, 66, 109, 112, 174, 231]},
        'weekly': {"categories": ["Hmbown/CodeWhale", "Yuan1z0825/nature-skills", "Fincept-Corporation/FinceptTerminal", "manaflow-ai/cmux", "tashfeenahmed/freellmapi", "multica-ai/multica", "Alishahryar1/free-claude-code", "mukul975/Anthropic-Cybersecurity-Skills", "rohitg00/agentmemory", "Leonxlnx/taste-skill", "anthropics/knowledge-work-plugins", "safishamsi/graphify", "CloakHQ/CloakBrowser", "tinyhumansai/openhuman", "Imbad0202/academic-research-skills", "anthropics/claude-plugins-official", "rohitg00/ai-engineering-from-scratch", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "Lum1104/Understand-Anything"], "data": [242, 247, 253, 264, 278, 306, 324, 343, 345, 355, 391, 397, 426, 533, 598, 771, 1175, 1672, 1917, 2087]},
        'monthly': {"categories": ["garrytan/gstack", "CloakHQ/CloakBrowser", "msitarzewski/agency-agents", "VoltAgent/awesome-design-md", "safishamsi/graphify", "anthropics/financial-services", "addyosmani/agent-skills", "tinyhumansai/openhuman", "colbymchenry/codegraph", "ruvnet/ruflo", "Lum1104/Understand-Anything", "affaan-m/ECC", "farion1231/cc-switch", "TauricResearch/TradingAgents", "warpdotdev/warp", "Hmbown/CodeWhale", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1784, 1818, 1822, 1880, 1893, 1981, 2141, 2203, 2438, 2643, 2806, 2849, 2853, 3214, 3222, 3415, 3647, 4851, 6704, 7398]}
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
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +231 | 39531 |
| 2 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +174 | 24060 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +112 | 29685 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +109 | 22393 |
| 5 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +66 | 41523 |
| 6 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +49 | 5826 |
| 7 | [russellromney/honker](https://github.com/russellromney/honker) | +40 | 2281 |
| 8 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +36 | 17208 |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +34 | 28812 |
| 10 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +32 | 22730 |
| 11 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +28 | 2960 |
| 12 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +27 | 10891 |
| 13 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +26 | 8084 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +26 | 54951 |
| 15 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +25 | 46456 |
| 16 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +25 | 12450 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +24 | 21752 |
| 18 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +23 | 18620 |
| 19 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +23 | 26854 |
| 20 | [Video-Reason/VBVR-EvalKit](https://github.com/Video-Reason/VBVR-EvalKit) | +23 | 297 |
| 21 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +23 | 30312 |
| 22 | [multica-ai/multica](https://github.com/multica-ai/multica) | +22 | 33638 |
| 23 | [JJLibra/CC-Pan](https://github.com/JJLibra/CC-Pan) | +22 | 230 |
| 24 | [Zafer-Liu/Data-Analysis-Agent](https://github.com/Zafer-Liu/Data-Analysis-Agent) | +21 | 1224 |
| 25 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +20 | 3816 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +19 | 13011 |
| 27 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +19 | 5256 |
| 28 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +19 | 4874 |
| 29 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +19 | 21754 |
| 30 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +19 | 35312 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2087 | 39531 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1917 | 29685 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1672 | 158870 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1175 | 22393 |
| 5 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +771 | 28230 |
| 6 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +598 | 22730 |
| 7 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +533 | 28812 |
| 8 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +426 | 21754 |
| 9 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +397 | 54951 |
| 10 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +391 | 17208 |
| 11 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +355 | 24060 |
| 12 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +345 | 18620 |
| 13 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +343 | 10891 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +324 | 30312 |
| 15 | [multica-ai/multica](https://github.com/multica-ai/multica) | +306 | 33638 |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +278 | 5814 |
| 17 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +264 | 19996 |
| 18 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +253 | 24271 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +247 | 13011 |
| 20 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +242 | 35312 |
| 21 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +236 | 7833 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +233 | 55131 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +227 | 21752 |
| 24 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +226 | 3304 |
| 25 | [presenton/presenton](https://github.com/presenton/presenton) | +191 | 7195 |
| 26 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +190 | 41987 |
| 27 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +188 | 4816 |
| 28 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +187 | 3674 |
| 29 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +187 | 7786 |
| 30 | [decolua/9router](https://github.com/decolua/9router) | +182 | 14714 |
| 31 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +181 | 40864 |
| 32 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +180 | 10789 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +178 | 54052 |
| 34 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +171 | 46456 |
| 35 | [88lin/video_vip](https://github.com/88lin/video_vip) | +166 | 3236 |
| 36 | [withcoral/coral](https://github.com/withcoral/coral) | +163 | 4963 |
| 37 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +160 | 2567 |
| 38 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +155 | 28176 |
| 39 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +147 | 28658 |
| 40 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +146 | 2429 |
| 41 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +140 | 8084 |
| 42 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +140 | 20141 |
| 43 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +140 | 6820 |
| 44 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +139 | 3270 |
| 45 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +138 | 6682 |
| 46 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +133 | 12111 |
| 47 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +133 | 1767 |
| 48 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +132 | 14913 |
| 49 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +131 | 19404 |
| 50 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +131 | 5826 |
| 51 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +131 | 21653 |
| 52 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +130 | 30779 |
| 53 | [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | +129 | 30432 |
| 54 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +127 | 23891 |
| 55 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +126 | 63057 |
| 56 | [dotnet/skills](https://github.com/dotnet/skills) | +126 | 3150 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +125 | 12558 |
| 58 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +123 | 26221 |
| 59 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +119 | 4989 |
| 60 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +113 | 40495 |
| 61 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +113 | 15318 |
| 62 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +113 | 35754 |
| 63 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +112 | 5256 |
| 64 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +109 | 21563 |
| 65 | [blader/humanizer](https://github.com/blader/humanizer) | +108 | 21210 |
| 66 | [santifer/career-ops](https://github.com/santifer/career-ops) | +106 | 47486 |
| 67 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +105 | 26854 |
| 68 | [google/ax](https://github.com/google/ax) | +104 | 1160 |
| 69 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +103 | 6617 |
| 70 | [Achilng/floral-notepaper](https://github.com/Achilng/floral-notepaper) | +102 | 2693 |
| 71 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +101 | 1497 |
| 72 | [antirez/ds4](https://github.com/antirez/ds4) | +100 | 12132 |
| 73 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +97 | 950 |
| 74 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +97 | 41523 |
| 75 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +95 | 1273 |
| 76 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +94 | 35079 |
| 77 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +94 | 5288 |
| 78 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +93 | 33290 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +91 | 30768 |
| 80 | [MinishLab/semble](https://github.com/MinishLab/semble) | +91 | 4432 |
| 81 | [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | +90 | 2291 |
| 82 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +90 | 1084 |
| 83 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +89 | 55181 |
| 84 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +89 | 2083 |
| 85 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +86 | 9555 |
| 86 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +85 | 19295 |
| 87 | [soxoj/maigret](https://github.com/soxoj/maigret) | +85 | 30656 |
| 88 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +83 | 4874 |
| 89 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +83 | 6439 |
| 90 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +83 | 8961 |
| 91 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +82 | 2061 |
| 92 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +81 | 8848 |
| 93 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +80 | 2960 |
| 94 | [tate233/todolist](https://github.com/tate233/todolist) | +80 | 1059 |
| 95 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +80 | 13127 |
| 96 | [openai/skills](https://github.com/openai/skills) | +80 | 20551 |
| 97 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +78 | 2601 |
| 98 | [virattt/dexter](https://github.com/virattt/dexter) | +77 | 26577 |
| 99 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +77 | 14859 |
| 100 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +76 | 4819 |
| 101 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +75 | 39136 |
| 102 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +74 | 8965 |
| 103 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +73 | 37565 |
| 104 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +73 | 38915 |
| 105 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +73 | 2529 |
| 106 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +71 | 26874 |
| 107 | [XiaoLuoLYG/GOD](https://github.com/XiaoLuoLYG/GOD) | +69 | 521 |
| 108 | [lynote-ai/humanize-text](https://github.com/lynote-ai/humanize-text) | +68 | 829 |
| 109 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +65 | 1947 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +62 | 15333 |
| 111 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +61 | 2573 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +60 | 11933 |
| 113 | [viticci/shortcuts-playground-plugin](https://github.com/viticci/shortcuts-playground-plugin) | +60 | 699 |
| 114 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +59 | 34357 |
| 115 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +57 | 16336 |
| 116 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +56 | 7762 |
| 117 | [xzf-thu/Mega-ASR](https://github.com/xzf-thu/Mega-ASR) | +55 | 680 |
| 118 | [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | +54 | 1054 |
| 119 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +53 | 6775 |
| 120 | [0xSero/codex-shim](https://github.com/0xSero/codex-shim) | +53 | 655 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7398 | 108416 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +6704 | 158871 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4851 | 170161 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3647 | 60312 |
| 5 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +3415 | 35312 |
| 6 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3222 | 60210 |
| 7 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3214 | 30590 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2853 | 82706 |
| 9 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2849 | 51199 |
| 10 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +2806 | 39531 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2643 | 55772 |
| 12 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2438 | 29685 |
| 13 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2203 | 28812 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2141 | 46456 |
| 15 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1981 | 28176 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1893 | 54951 |
| 17 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1880 | 84894 |
| 18 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1822 | 105559 |
| 19 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1818 | 21754 |
| 20 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1784 | 103624 |
| 21 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1723 | 54526 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +1578 | 55131 |
| 23 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1573 | 109881 |
| 24 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1556 | 65589 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +1552 | 74774 |
| 26 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1541 | 22730 |
| 27 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1523 | 22393 |
| 28 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1504 | 30312 |
| 29 | [github/spec-kit](https://github.com/github/spec-kit) | +1464 | 71722 |
| 30 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1433 | 18621 |
| 31 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1418 | 20141 |
| 32 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1392 | 66693 |
| 33 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1387 | 30656 |
| 34 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1378 | 56311 |
| 35 | [antirez/ds4](https://github.com/antirez/ds4) | +1339 | 12132 |
| 36 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1291 | 85286 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1279 | 54052 |
| 38 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1237 | 21752 |
| 39 | [decolua/9router](https://github.com/decolua/9router) | +1176 | 14714 |
| 40 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1137 | 34148 |
| 41 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1103 | 55070 |
| 42 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1102 | 13011 |
| 43 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1090 | 33638 |
| 44 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1078 | 30678 |
| 45 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1042 | 40495 |
| 46 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +989 | 28230 |
| 47 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +938 | 24272 |
| 48 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +920 | 12111 |
| 49 | [openai/symphony](https://github.com/openai/symphony) | +916 | 24716 |
| 50 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +913 | 21653 |
| 51 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +895 | 24060 |
| 52 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +891 | 15616 |
| 53 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +861 | 14913 |
| 54 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +849 | 67955 |
| 55 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +831 | 17102 |
| 56 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +775 | 30779 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +753 | 23891 |
| 58 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +752 | 6604 |
| 59 | [floci-io/floci](https://github.com/floci-io/floci) | +743 | 13168 |
| 60 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +727 | 19404 |
| 61 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +722 | 12558 |
| 62 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +719 | 10789 |
| 63 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +716 | 51169 |
| 64 | [santifer/career-ops](https://github.com/santifer/career-ops) | +704 | 47486 |
| 65 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +700 | 13887 |
| 66 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +685 | 16768 |
| 67 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +681 | 55181 |
| 68 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +678 | 15370 |
| 69 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +667 | 7744 |
| 70 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +657 | 35503 |
| 71 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +654 | 8084 |
| 72 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +652 | 35754 |
| 73 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +643 | 39136 |
| 74 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +631 | 33290 |
| 75 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +628 | 40864 |
| 76 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +624 | 26221 |
| 77 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +615 | 8848 |
| 78 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +598 | 5288 |
| 79 | [virattt/dexter](https://github.com/virattt/dexter) | +598 | 26577 |
| 80 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +586 | 11933 |
| 81 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +584 | 6617 |
| 82 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +565 | 22803 |
| 83 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +564 | 63057 |
| 84 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +555 | 4299 |
| 85 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +543 | 62830 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +541 | 30768 |
| 87 | [vercel-labs/zero-native](https://github.com/vercel-labs/zero-native) | +540 | 4013 |
| 88 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +537 | 21563 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +529 | 35079 |
| 90 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +518 | 6439 |
| 91 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +514 | 18834 |
| 92 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +506 | 12190 |
| 93 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +505 | 6820 |
| 94 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +504 | 41987 |
| 95 | [withcoral/coral](https://github.com/withcoral/coral) | +492 | 4963 |
| 96 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +483 | 28658 |
| 97 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +482 | 17208 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +480 | 26854 |
| 99 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +473 | 47468 |
| 100 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +467 | 34357 |
| 101 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +451 | 19996 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +442 | 19965 |
| 103 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +441 | 32238 |
| 104 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +432 | 17530 |
| 105 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +422 | 7786 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +413 | 8961 |
| 107 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +408 | 10891 |
| 108 | [jundot/omlx](https://github.com/jundot/omlx) | +400 | 15333 |
| 109 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +399 | 6682 |
| 110 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +387 | 8044 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +377 | 6775 |
| 112 | [browserbase/skills](https://github.com/browserbase/skills) | +377 | 3444 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +367 | 14859 |
| 114 | [browser-use/video-use](https://github.com/browser-use/video-use) | +355 | 8496 |
| 115 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +351 | 4816 |
| 116 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +350 | 10080 |
| 117 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +343 | 19794 |
| 118 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +342 | 4989 |
| 119 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +341 | 4874 |
| 120 | [MinishLab/semble](https://github.com/MinishLab/semble) | +341 | 4432 |
| 121 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +334 | 44968 |
| 122 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +330 | 38915 |
| 123 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +326 | 15318 |
| 124 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +324 | 4819 |
| 125 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +316 | 4674 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +315 | 16336 |
| 127 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +302 | 5887 |
| 128 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +294 | 36799 |
| 129 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +289 | 8864 |
| 130 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +289 | 22407 |
| 131 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +285 | 2372 |
| 132 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +284 | 23874 |
| 133 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +281 | 13418 |
| 134 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +280 | 21651 |
| 135 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +274 | 2529 |
| 136 | [openai/skills](https://github.com/openai/skills) | +271 | 20551 |
| 137 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +271 | 26661 |
| 138 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +270 | 3974 |
| 139 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +269 | 4965 |
| 140 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +267 | 22206 |
| 141 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +266 | 24344 |
| 142 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +266 | 33250 |
| 143 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +265 | 10839 |
| 144 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +264 | 2593 |
| 145 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +262 | 2573 |
| 146 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +258 | 27436 |
| 147 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +256 | 4288 |
| 148 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +254 | 7762 |
| 149 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +243 | 33941 |
| 150 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +243 | 26252 |
| 151 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +243 | 4095 |
| 152 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +239 | 2640 |
| 153 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +236 | 33141 |
| 154 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +236 | 1982 |
| 155 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +233 | 4294 |
| 156 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +231 | 3767 |
| 157 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +228 | 3404 |
| 158 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +226 | 7153 |
| 159 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +220 | 6006 |
| 160 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +220 | 26078 |
| 161 | [z-lab/dflash](https://github.com/z-lab/dflash) | +219 | 4729 |
| 162 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +216 | 3190 |
| 163 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +210 | 10003 |
| 164 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +207 | 5635 |
| 165 | [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX) | +206 | 2453 |
| 166 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +205 | 1948 |
| 167 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +205 | 43265 |
| 168 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +203 | 6646 |
| 169 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +203 | 5290 |
| 170 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +202 | 6838 |
| 171 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +201 | 37564 |
| 172 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +200 | 20403 |
| 173 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +199 | 2567 |
| 174 | [88lin/video_vip](https://github.com/88lin/video_vip) | +199 | 3236 |
| 175 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +199 | 28453 |
| 176 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +196 | 4546 |
| 177 | [jingyaogong/minimind-o](https://github.com/jingyaogong/minimind-o) | +195 | 1608 |
| 178 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +190 | 3674 |
| 179 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +188 | 2061 |
| 180 | [yaojingang/yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | +188 | 2307 |
| 181 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +180 | 2504 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +180 | 7327 |
| 183 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +179 | 13199 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +177 | 14657 |
| 185 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +164 | 4925 |
| 186 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +162 | 6272 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +148 | 5231 |
| 188 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +144 | 27197 |
| 189 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +143 | 5826 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +141 | 36103 |
| 191 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +141 | 2237 |
| 192 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +136 | 3840 |
| 193 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +134 | 17338 |
| 194 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +131 | 4805 |
| 195 | [sandeco/reversa](https://github.com/sandeco/reversa) | +130 | 1106 |
| 196 | [playcanvas/engine](https://github.com/playcanvas/engine) | +130 | 15896 |
| 197 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +116 | 8522 |
| 198 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +113 | 10094 |
| 199 | [usebruno/bruno](https://github.com/usebruno/bruno) | +110 | 41086 |
| 200 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1362 |
| 201 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +109 | 867 |
| 202 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +108 | 39596 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +108 | 15397 |
| 204 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +107 | 10559 |
| 205 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +106 | 3069 |
| 206 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +106 | 23279 |
| 207 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +105 | 1753 |
| 208 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +102 | 2087 |
| 209 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +101 | 3816 |
| 210 | [eze-is/web-access](https://github.com/eze-is/web-access) | +100 | 6880 |
| 211 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +97 | 11880 |
| 212 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +93 | 955 |
| 213 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +93 | 759 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +92 | 2098 |
| 215 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +89 | 3202 |
| 216 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +85 | 40265 |
| 217 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +81 | 3199 |
| 218 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +80 | 10048 |
| 219 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +78 | 14954 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +75 | 1718 |
| 221 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +72 | 1065 |
| 222 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +71 | 4602 |
| 223 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +70 | 4557 |
| 224 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +67 | 578 |
| 225 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2453 |
| 226 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +66 | 8047 |
| 227 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +66 | 35473 |
| 228 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +65 | 7575 |
| 229 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +65 | 37313 |
| 230 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +61 | 48784 |
| 231 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +60 | 1689 |
| 232 | [qist/tvbox](https://github.com/qist/tvbox) | +59 | 9494 |
| 233 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +59 | 45263 |
| 234 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +58 | 11907 |
| 235 | [robinebers/openusage](https://github.com/robinebers/openusage) | +58 | 2624 |
| 236 | [halo-dev/halo](https://github.com/halo-dev/halo) | +58 | 37991 |
| 237 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +56 | 8509 |
| 238 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +54 | 13471 |
| 239 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +54 | 526 |
| 240 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 294 |
| 241 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +51 | 4015 |
| 242 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +51 | 3273 |
| 243 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +51 | 30242 |
| 244 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 306 |
| 245 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +50 | 353 |
| 246 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 489 |
| 247 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +48 | 604 |
| 248 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +48 | 33000 |
| 249 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +47 | 4701 |
| 250 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +45 | 3310 |
| 251 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 347 |
| 252 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +44 | 2386 |
| 253 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +43 | 339 |
| 254 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +41 | 4237 |
| 255 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +41 | 665 |
| 256 | [Gracker/SmartPerfetto](https://github.com/Gracker/SmartPerfetto) | +41 | 454 |
| 257 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +41 | 488 |
| 258 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +40 | 1129 |
| 259 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +40 | 1015 |
| 260 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +40 | 508 |
| 261 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +40 | 2305 |
| 262 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +40 | 2256 |
| 263 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +38 | 1536 |
| 264 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +38 | 375 |
| 265 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +38 | 1848 |
| 266 | [openmemind/memind](https://github.com/openmemind/memind) | +37 | 862 |
| 267 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +35 | 1575 |
| 268 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +35 | 2254 |
| 269 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +35 | 9775 |
| 270 | [FongMi/TV](https://github.com/FongMi/TV) | +35 | 8096 |
| 271 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +34 | 1396 |
| 272 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 277 |
| 273 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +34 | 2004 |
| 274 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +34 | 1467 |
| 275 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +34 | 2541 |
| 276 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +33 | 518 |
| 277 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +32 | 279 |
| 278 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +30 | 5191 |
| 279 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +29 | 3999 |
| 280 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +28 | 753 |
| 281 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +28 | 868 |
| 282 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +28 | 317 |
| 283 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2233 |
| 284 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +27 | 753 |
| 285 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +25 | 775 |
| 286 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +21 | 236 |
| 287 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +21 | 205 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +21 | 1551 |
| 289 | [is-a-dev/register](https://github.com/is-a-dev/register) | +20 | 10366 |
| 290 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +20 | 2441 |
| 291 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +19 | 2959 |
| 292 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +19 | 309 |
| 293 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +19 | 2643 |
| 294 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +18 | 335 |
| 295 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +16 | 324 |
| 296 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +15 | 5171 |
| 297 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +15 | 3239 |
| 298 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +15 | 511 |
| 299 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +15 | 245 |
| 300 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +14 | 136 |
