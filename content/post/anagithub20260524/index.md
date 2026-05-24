---
title: "2026-05-24 GitHub增长趋势报告"
description: "1.Understand-Anything+652 2.codegraph+516 3.ai-engineering-from-scratch+279 4.claude-plugins-official+250 5.academic-research-skills+156"
date: 2026-05-24T20:58:18+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-05-24 20:58:18

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
        'daily': {"categories": ["janestreet/magic-trace", "hugohe3/ppt-master", "st-tech/ppf-contact-solver", "anthropics/knowledge-work-plugins", "rohitg00/agentmemory", "Alishahryar1/free-claude-code", "multica-ai/multica", "simplifaisoul/osiris", "Fincept-Corporation/FinceptTerminal", "presenton/presenton", "safishamsi/graphify", "CloakHQ/CloakBrowser", "tinyhumansai/openhuman", "manaflow-ai/cmux", "mukul975/Anthropic-Cybersecurity-Skills", "Imbad0202/academic-research-skills", "anthropics/claude-plugins-official", "rohitg00/ai-engineering-from-scratch", "colbymchenry/codegraph", "Lum1104/Understand-Anything"], "data": [76, 87, 88, 88, 92, 92, 93, 93, 99, 103, 115, 148, 149, 150, 150, 156, 250, 279, 516, 652]},
        'weekly': {"categories": ["Yuan1z0825/nature-skills", "truelockmc/streambert", "Hmbown/DeepSeek-TUI", "tashfeenahmed/freellmapi", "multica-ai/multica", "Alishahryar1/free-claude-code", "rtk-ai/rtk", "HKUDS/CLI-Anything", "safishamsi/graphify", "rmyndharis/OpenWA", "rohitg00/agentmemory", "CloakHQ/CloakBrowser", "rohitg00/ai-engineering-from-scratch", "anthropics/claude-plugins-official", "Imbad0202/academic-research-skills", "tinyhumansai/openhuman", "mattpocock/skills", "Lum1104/Understand-Anything", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph"], "data": [252, 261, 265, 265, 267, 281, 283, 288, 336, 337, 490, 530, 647, 727, 742, 1003, 1053, 1079, 1498, 1548]},
        'monthly': {"categories": ["anthropics/financial-services", "msitarzewski/agency-agents", "rtk-ai/rtk", "tinyhumansai/openhuman", "Z4nzu/hackingtool", "garrytan/gstack", "safishamsi/graphify", "VoltAgent/awesome-design-md", "addyosmani/agent-skills", "ruvnet/ruflo", "affaan-m/ECC", "Alishahryar1/free-claude-code", "farion1231/cc-switch", "warpdotdev/warp", "TauricResearch/TradingAgents", "Hmbown/DeepSeek-TUI", "obra/superpowers", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [1940, 2017, 2026, 2059, 2065, 2150, 2166, 2182, 2436, 2674, 2873, 3029, 3070, 3193, 3291, 3332, 3957, 5620, 8304, 8928]}
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
| 1 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +652 | 25320 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +516 | 21737 |
| 3 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +279 | 15632 |
| 4 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +250 | 27184 |
| 5 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +156 | 20512 |
| 6 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +150 | 8200 |
| 7 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +150 | 18948 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +149 | 27046 |
| 9 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +148 | 20228 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +115 | 52972 |
| 11 | [presenton/presenton](https://github.com/presenton/presenton) | +103 | 6711 |
| 12 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +99 | 23441 |
| 13 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +93 | 2882 |
| 14 | [multica-ai/multica](https://github.com/multica-ai/multica) | +93 | 32411 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +92 | 29087 |
| 16 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +92 | 17271 |
| 17 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +88 | 13890 |
| 18 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +88 | 2807 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +87 | 20576 |
| 20 | [janestreet/magic-trace](https://github.com/janestreet/magic-trace) | +76 | 6023 |
| 21 | [88lin/video_vip](https://github.com/88lin/video_vip) | +74 | 2983 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +73 | 53592 |
| 23 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +73 | 10115 |
| 24 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +73 | 7288 |
| 25 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +72 | 7013 |
| 26 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +67 | 41516 |
| 27 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +66 | 4847 |
| 28 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +65 | 34190 |
| 29 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +62 | 11325 |
| 30 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +61 | 53004 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1548 | 21737 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1498 | 151831 |
| 3 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1079 | 25320 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1053 | 103450 |
| 5 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1003 | 27046 |
| 6 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +742 | 20512 |
| 7 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +727 | 27184 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +647 | 15632 |
| 9 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +530 | 20228 |
| 10 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +490 | 17271 |
| 11 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +337 | 6081 |
| 12 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +336 | 52972 |
| 13 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +288 | 40031 |
| 14 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +283 | 53592 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +281 | 29087 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +267 | 32411 |
| 17 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +265 | 4847 |
| 18 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +265 | 34191 |
| 19 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +261 | 4632 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +252 | 11325 |
| 21 | [MinishLab/semble](https://github.com/MinishLab/semble) | +241 | 4113 |
| 22 | [decolua/9router](https://github.com/decolua/9router) | +240 | 14000 |
| 23 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +238 | 10115 |
| 24 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +238 | 7288 |
| 25 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +232 | 27293 |
| 26 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +223 | 2882 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +223 | 20576 |
| 28 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +217 | 23441 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +210 | 7013 |
| 30 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +194 | 45376 |
| 31 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +193 | 18948 |
| 32 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +192 | 8200 |
| 33 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +190 | 14476 |
| 34 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +187 | 53004 |
| 35 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +181 | 2277 |
| 36 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +176 | 16816 |
| 37 | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | +173 | 1984 |
| 38 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +173 | 18686 |
| 39 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +171 | 28149 |
| 40 | [presenton/presenton](https://github.com/presenton/presenton) | +168 | 6711 |
| 41 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +168 | 4449 |
| 42 | [Achilng/floral-notepaper](https://github.com/Achilng/floral-notepaper) | +166 | 2343 |
| 43 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +165 | 41516 |
| 44 | [withcoral/coral](https://github.com/withcoral/coral) | +163 | 4594 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +158 | 20893 |
| 46 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +152 | 25602 |
| 47 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +146 | 19534 |
| 48 | [santifer/career-ops](https://github.com/santifer/career-ops) | +146 | 47037 |
| 49 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +140 | 16284 |
| 50 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +138 | 8762 |
| 51 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +136 | 50413 |
| 52 | [88lin/video_vip](https://github.com/88lin/video_vip) | +135 | 2983 |
| 53 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +133 | 2097 |
| 54 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +132 | 38715 |
| 55 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +132 | 6302 |
| 56 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +132 | 2677 |
| 57 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +132 | 11739 |
| 58 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +130 | 4787 |
| 59 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +129 | 14992 |
| 60 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +128 | 23186 |
| 61 | [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | +122 | 4014 |
| 62 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +120 | 62337 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +119 | 13891 |
| 64 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +119 | 2807 |
| 65 | [antirez/ds4](https://github.com/antirez/ds4) | +118 | 11682 |
| 66 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +118 | 40013 |
| 67 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +117 | 18959 |
| 68 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +114 | 2308 |
| 69 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +112 | 4556 |
| 70 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +111 | 11462 |
| 71 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +111 | 21066 |
| 72 | [blader/humanizer](https://github.com/blader/humanizer) | +111 | 20758 |
| 73 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +110 | 35164 |
| 74 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +109 | 7496 |
| 75 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +108 | 1686 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +107 | 25172 |
| 77 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +104 | 29945 |
| 78 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +101 | 54647 |
| 79 | [dotnet/skills](https://github.com/dotnet/skills) | +100 | 2929 |
| 80 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +99 | 4194 |
| 81 | [floci-io/floci](https://github.com/floci-io/floci) | +99 | 12963 |
| 82 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +97 | 43625 |
| 83 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +94 | 4866 |
| 84 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +93 | 12784 |
| 85 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +92 | 9114 |
| 86 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +91 | 32834 |
| 87 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +88 | 6787 |
| 88 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +87 | 6349 |
| 89 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +87 | 34569 |
| 90 | [larksuite/cli](https://github.com/larksuite/cli) | +87 | 12529 |
| 91 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +86 | 30326 |
| 92 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +85 | 1958 |
| 93 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +84 | 2621 |
| 94 | [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | +82 | 2173 |
| 95 | [google/ax](https://github.com/google/ax) | +82 | 886 |
| 96 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +81 | 934 |
| 97 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +81 | 4571 |
| 98 | [soxoj/maigret](https://github.com/soxoj/maigret) | +80 | 30197 |
| 99 | [chengzuopeng/stock-sdk](https://github.com/chengzuopeng/stock-sdk) | +78 | 750 |
| 100 | [openai/skills](https://github.com/openai/skills) | +77 | 20165 |
| 101 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +75 | 2076 |
| 102 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +74 | 1505 |
| 103 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +72 | 8514 |
| 104 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +72 | 1698 |
| 105 | [Light-Heart-Labs/DreamServer](https://github.com/Light-Heart-Labs/DreamServer) | +71 | 1685 |
| 106 | [virattt/dexter](https://github.com/virattt/dexter) | +69 | 26405 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +69 | 16079 |
| 108 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +68 | 18632 |
| 109 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +67 | 8514 |
| 110 | [feder-cr/invisible_playwright](https://github.com/feder-cr/invisible_playwright) | +67 | 996 |
| 111 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +67 | 2308 |
| 112 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +67 | 4620 |
| 113 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +66 | 7587 |
| 114 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +64 | 44697 |
| 115 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +63 | 6416 |
| 116 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +63 | 2305 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +62 | 38563 |
| 118 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +61 | 11638 |
| 119 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +60 | 4173 |
| 120 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +57 | 34057 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8928 | 103450 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +8304 | 151831 |
| 3 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +5620 | 165543 |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | +3957 | 60312 |
| 5 | [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | +3332 | 34191 |
| 6 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3291 | 30590 |
| 7 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +3193 | 59825 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3070 | 79656 |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3029 | 29087 |
| 10 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +2873 | 51199 |
| 11 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2674 | 54759 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2436 | 45377 |
| 13 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +2182 | 83518 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +2166 | 52972 |
| 15 | [garrytan/gstack](https://github.com/garrytan/gstack) | +2150 | 101616 |
| 16 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +2065 | 55070 |
| 17 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2059 | 27046 |
| 18 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2026 | 53592 |
| 19 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2017 | 104728 |
| 20 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +1940 | 27293 |
| 21 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1900 | 64296 |
| 22 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1856 | 25320 |
| 23 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +1840 | 21737 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1815 | 109881 |
| 25 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1789 | 53908 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +1718 | 74774 |
| 27 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1704 | 20228 |
| 28 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1600 | 53855 |
| 29 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +1507 | 15441 |
| 30 | [github/spec-kit](https://github.com/github/spec-kit) | +1499 | 71722 |
| 31 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +1463 | 19534 |
| 32 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1423 | 40013 |
| 33 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1405 | 20512 |
| 34 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1387 | 11446 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1381 | 53004 |
| 36 | [soxoj/maigret](https://github.com/soxoj/maigret) | +1370 | 30197 |
| 37 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1365 | 65321 |
| 38 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +1356 | 17271 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1349 | 20576 |
| 40 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +1323 | 85286 |
| 41 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1323 | 30678 |
| 42 | [antirez/ds4](https://github.com/antirez/ds4) | +1312 | 11682 |
| 43 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +1302 | 34148 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +1248 | 32411 |
| 45 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1243 | 23441 |
| 46 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1189 | 16816 |
| 47 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1175 | 20893 |
| 48 | [decolua/9router](https://github.com/decolua/9router) | +1159 | 14000 |
| 49 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +1116 | 11462 |
| 50 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +1074 | 11739 |
| 51 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1061 | 14846 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1051 | 15633 |
| 53 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1019 | 11325 |
| 54 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +998 | 14476 |
| 55 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +994 | 67445 |
| 56 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +945 | 27184 |
| 57 | [openai/symphony](https://github.com/openai/symphony) | +915 | 24543 |
| 58 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +915 | 13635 |
| 59 | [santifer/career-ops](https://github.com/santifer/career-ops) | +912 | 47037 |
| 60 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +891 | 23186 |
| 61 | [openai/codex](https://github.com/openai/codex) | +870 | 61744 |
| 62 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +832 | 29945 |
| 63 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +809 | 18686 |
| 64 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +800 | 54647 |
| 65 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +792 | 83092 |
| 66 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +783 | 47402 |
| 67 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +775 | 38715 |
| 68 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +771 | 63680 |
| 69 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +768 | 8514 |
| 70 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +759 | 50413 |
| 71 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +758 | 18959 |
| 72 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +747 | 6506 |
| 73 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +742 | 6349 |
| 74 | [floci-io/floci](https://github.com/floci-io/floci) | +740 | 12963 |
| 75 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +719 | 35164 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +691 | 32834 |
| 77 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +686 | 21066 |
| 78 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +677 | 30326 |
| 79 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +671 | 10115 |
| 80 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +662 | 12037 |
| 81 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +658 | 16284 |
| 82 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +657 | 7587 |
| 83 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +657 | 62337 |
| 84 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | +652 | 51085 |
| 85 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +650 | 37330 |
| 86 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +650 | 9114 |
| 87 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | +641 | 35138 |
| 88 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +632 | 34569 |
| 89 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +629 | 62085 |
| 90 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +629 | 33878 |
| 91 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +624 | 40031 |
| 92 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +618 | 22486 |
| 93 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +609 | 5881 |
| 94 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +604 | 11638 |
| 95 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +602 | 34057 |
| 96 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +599 | 25602 |
| 97 | [virattt/dexter](https://github.com/virattt/dexter) | +597 | 26405 |
| 98 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +587 | 6787 |
| 99 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +568 | 4866 |
| 100 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +557 | 28149 |
| 101 | [TwilitRealm/dusklight](https://github.com/TwilitRealm/dusklight) | +541 | 4188 |
| 102 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +536 | 25762 |
| 103 | [browser-use/video-use](https://github.com/browser-use/video-use) | +513 | 8332 |
| 104 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +509 | 18632 |
| 105 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +504 | 17319 |
| 106 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +495 | 8514 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +478 | 19708 |
| 108 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +457 | 24266 |
| 109 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +456 | 32071 |
| 110 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +449 | 44697 |
| 111 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +443 | 6416 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +439 | 15067 |
| 113 | [kyegomez/OpenMythos](https://github.com/kyegomez/OpenMythos) | +434 | 13354 |
| 114 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +418 | 4556 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +417 | 14415 |
| 116 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +416 | 19533 |
| 117 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +408 | 38563 |
| 118 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +383 | 7288 |
| 119 | [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research) | +382 | 7940 |
| 120 | [browserbase/skills](https://github.com/browserbase/skills) | +378 | 3416 |
| 121 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +377 | 16079 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +368 | 14992 |
| 123 | [cocoindex-io/cocoindex](https://github.com/cocoindex-io/cocoindex) | +357 | 10026 |
| 124 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +350 | 5709 |
| 125 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +345 | 5788 |
| 126 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +335 | 4632 |
| 127 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +332 | 36799 |
| 128 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +332 | 21551 |
| 129 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +331 | 3703 |
| 130 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +329 | 27535 |
| 131 | [Einsia/OpenChronicle](https://github.com/Einsia/OpenChronicle) | +327 | 2757 |
| 132 | [MinishLab/semble](https://github.com/MinishLab/semble) | +325 | 4113 |
| 133 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +325 | 5187 |
| 134 | [openclaw/clawsweeper](https://github.com/openclaw/clawsweeper) | +322 | 1679 |
| 135 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +318 | 4571 |
| 136 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +317 | 26476 |
| 137 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +317 | 23581 |
| 138 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +316 | 3945 |
| 139 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +309 | 9672 |
| 140 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +305 | 4194 |
| 141 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +305 | 4620 |
| 142 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +303 | 2628 |
| 143 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +302 | 7054 |
| 144 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +299 | 33003 |
| 145 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +298 | 21988 |
| 146 | [openai/skills](https://github.com/openai/skills) | +297 | 20165 |
| 147 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +296 | 22194 |
| 148 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +295 | 4806 |
| 149 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +294 | 32836 |
| 150 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +293 | 27260 |
| 151 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +293 | 2325 |
| 152 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +292 | 4173 |
| 153 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +290 | 1886 |
| 154 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +285 | 2324 |
| 155 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +283 | 10517 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +282 | 33727 |
| 157 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +278 | 6732 |
| 158 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +276 | 2372 |
| 159 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +274 | 8200 |
| 160 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +272 | 2595 |
| 161 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +267 | 13624 |
| 162 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +266 | 25911 |
| 163 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +262 | 43074 |
| 164 | [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | +255 | 2516 |
| 165 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +255 | 2308 |
| 166 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +254 | 3013 |
| 167 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +250 | 5448 |
| 168 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +248 | 2305 |
| 169 | [z-lab/dflash](https://github.com/z-lab/dflash) | +248 | 4697 |
| 170 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +247 | 3802 |
| 171 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +240 | 28232 |
| 172 | [Q00/ouroboros](https://github.com/Q00/ouroboros) | +236 | 4250 |
| 173 | [aattaran/deepclaude](https://github.com/aattaran/deepclaude) | +234 | 1957 |
| 174 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +232 | 20192 |
| 175 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +230 | 7496 |
| 176 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +230 | 25967 |
| 177 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +229 | 37564 |
| 178 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +220 | 6492 |
| 179 | [tiagozip/cap](https://github.com/tiagozip/cap) | +216 | 6455 |
| 180 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +215 | 13891 |
| 181 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +210 | 4365 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +202 | 7230 |
| 183 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +199 | 2621 |
| 184 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +195 | 1686 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +190 | 14423 |
| 186 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +182 | 2277 |
| 187 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +171 | 3740 |
| 188 | [88lin/video_vip](https://github.com/88lin/video_vip) | +169 | 2983 |
| 189 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +163 | 5172 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +163 | 27044 |
| 191 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +161 | 6177 |
| 192 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +154 | 4727 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +145 | 36103 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +137 | 17067 |
| 195 | [playcanvas/engine](https://github.com/playcanvas/engine) | +137 | 15877 |
| 196 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +133 | 15310 |
| 197 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +132 | 2097 |
| 198 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +130 | 10468 |
| 199 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +125 | 1623 |
| 200 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +122 | 2886 |
| 201 | [bergside/design-md-chrome](https://github.com/bergside/design-md-chrome) | +122 | 2050 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +122 | 0 |
| 203 | [sandeco/reversa](https://github.com/sandeco/reversa) | +121 | 1022 |
| 204 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +121 | 23198 |
| 205 | [usebruno/bruno](https://github.com/usebruno/bruno) | +119 | 41086 |
| 206 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +118 | 10014 |
| 207 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +114 | 39596 |
| 208 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +112 | 7548 |
| 209 | [eze-is/web-access](https://github.com/eze-is/web-access) | +107 | 6768 |
| 210 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +106 | 839 |
| 211 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +105 | 1331 |
| 212 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +97 | 3129 |
| 213 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +97 | 2038 |
| 214 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +94 | 0 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +93 | 40265 |
| 216 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +91 | 751 |
| 217 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +89 | 11795 |
| 218 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +88 | 4525 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +88 | 24188 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +82 | 1639 |
| 221 | [yonggekkk/Cloudflare-vless-trojan](https://github.com/yonggekkk/Cloudflare-vless-trojan) | +82 | 14862 |
| 222 | [fishjar/kiss-translator](https://github.com/fishjar/kiss-translator) | +80 | 10435 |
| 223 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +80 | 35473 |
| 224 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +79 | 8009 |
| 225 | [viarotel-org/escrcpy](https://github.com/viarotel-org/escrcpy) | +78 | 10007 |
| 226 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +71 | 11878 |
| 227 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +68 | 3954 |
| 228 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +68 | 37313 |
| 229 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +67 | 2445 |
| 230 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +66 | 4635 |
| 231 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +65 | 30206 |
| 232 | [qist/tvbox](https://github.com/qist/tvbox) | +63 | 9460 |
| 233 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +63 | 3242 |
| 234 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +63 | 48784 |
| 235 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +62 | 962 |
| 236 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +62 | 8458 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +58 | 13401 |
| 238 | [halo-dev/halo](https://github.com/halo-dev/halo) | +58 | 37991 |
| 239 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +56 | 33000 |
| 240 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +55 | 45263 |
| 241 | [robinebers/openusage](https://github.com/robinebers/openusage) | +54 | 2578 |
| 242 | [b-nnett/codex-plusplus-ios-simulator](https://github.com/b-nnett/codex-plusplus-ios-simulator) | +52 | 519 |
| 243 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +52 | 2317 |
| 244 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +51 | 303 |
| 245 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +51 | 992 |
| 246 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +51 | 2219 |
| 247 | [hankmt/Artemis-Timeline](https://github.com/hankmt/Artemis-Timeline) | +50 | 304 |
| 248 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +50 | 11266 |
| 249 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +49 | 3243 |
| 250 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +49 | 345 |
| 251 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +49 | 2543 |
| 252 | [manojmallick/sigmap](https://github.com/manojmallick/sigmap) | +48 | 478 |
| 253 | [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | +47 | 592 |
| 254 | [qualisero/awesome-pi-agent](https://github.com/qualisero/awesome-pi-agent) | +47 | 992 |
| 255 | [kunchenguid/autopreso](https://github.com/kunchenguid/autopreso) | +44 | 332 |
| 256 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +44 | 850 |
| 257 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +44 | 4199 |
| 258 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +43 | 1453 |
| 259 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +42 | 335 |
| 260 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +41 | 1799 |
| 261 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +41 | 1517 |
| 262 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +41 | 2202 |
| 263 | [openmemind/memind](https://github.com/openmemind/memind) | +41 | 833 |
| 264 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +41 | 726 |
| 265 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +40 | 499 |
| 266 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +39 | 648 |
| 267 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +39 | 2268 |
| 268 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +38 | 447 |
| 269 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +37 | 1377 |
| 270 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +37 | 928 |
| 271 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +36 | 1971 |
| 272 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +35 | 5165 |
| 273 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +35 | 395 |
| 274 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +35 | 9715 |
| 275 | [FongMi/TV](https://github.com/FongMi/TV) | +35 | 8068 |
| 276 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +34 | 330 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +34 | 1439 |
| 278 | [killervillsy/SessionToJson](https://github.com/killervillsy/SessionToJson) | +30 | 280 |
| 279 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +30 | 258 |
| 280 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +29 | 753 |
| 281 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +29 | 759 |
| 282 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +27 | 2420 |
| 283 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +27 | 2218 |
| 284 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +26 | 299 |
| 285 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +26 | 500 |
| 286 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +25 | 229 |
| 287 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +25 | 1015 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +25 | 1550 |
| 289 | [is-a-dev/register](https://github.com/is-a-dev/register) | +24 | 10339 |
| 290 | [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | +24 | 228 |
| 291 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +22 | 0 |
| 292 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +22 | 2634 |
| 293 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +22 | 2951 |
| 294 | [cchenax/streamforge-ai](https://github.com/cchenax/streamforge-ai) | +21 | 309 |
| 295 | [Droid-VM/DroidVM](https://github.com/Droid-VM/DroidVM) | +21 | 333 |
| 296 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +18 | 346 |
| 297 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +18 | 863 |
| 298 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +17 | 3233 |
| 299 | [zhikunqingtao/zhikuncode](https://github.com/zhikunqingtao/zhikuncode) | +16 | 243 |
| 300 | [spring-ai-community/spring-ai-agent-utils](https://github.com/spring-ai-community/spring-ai-agent-utils) | +16 | 453 |
