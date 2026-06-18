---
title: "2026-06-18 GitHub增长趋势报告"
description: "1.ponytail+98 2.codebase-memory-mcp+47 3.headroom+34 4.Agent-Reach+26 5.taste-skill+21"
date: 2026-06-18T22:10:51+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-18 22:10:51

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
        'daily': {"categories": ["router-for-me/CLIProxyAPI", "alibaba/zvec", "GoogleCloudPlatform/knowledge-catalog", "calesthio/OpenMontage", "alibaba/open-code-review", "NVIDIA/SkillSpector", "Imbad0202/academic-research-skills", "heygen-com/hyperframes", "rtk-ai/rtk", "dzcmemory-web/bazi-ziwei-skill", "can1357/oh-my-pi", "agentscope-ai/QwenPaw", "omnigent-ai/omnigent", "anthropics/financial-services", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "Panniantong/Agent-Reach", "chopratejas/headroom", "DeusData/codebase-memory-mcp", "DietrichGebert/ponytail"], "data": [6, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10, 11, 12, 13, 13, 21, 26, 34, 47, 98]},
        'weekly': {"categories": ["pbakaus/impeccable", "rtk-ai/rtk", "DeusData/codebase-memory-mcp", "Imbad0202/academic-research-skills", "chatwoot/chatwoot", "hugohe3/ppt-master", "rohitg00/ai-engineering-from-scratch", "lfnovo/open-notebook", "GoogleCloudPlatform/knowledge-catalog", "omnigent-ai/omnigent", "colbymchenry/codegraph", "shadcn/improve", "mvanhorn/last30days-skill", "Leonxlnx/taste-skill", "NVIDIA/SkillSpector", "XiaomiMiMo/MiMo-Code", "apple/container", "Panniantong/Agent-Reach", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [65, 69, 71, 78, 82, 82, 84, 97, 120, 120, 159, 162, 171, 177, 190, 247, 262, 287, 301, 800]},
        'monthly': {"categories": ["CloakHQ/CloakBrowser", "addyosmani/agent-skills", "ruvnet/RuView", "DietrichGebert/ponytail", "mvanhorn/last30days-skill", "anthropics/claude-plugins-official", "safishamsi/graphify", "tinyhumansai/openhuman", "harry0703/MoneyPrinterTurbo", "Imbad0202/academic-research-skills", "chopratejas/headroom", "Leonxlnx/taste-skill", "farion1231/cc-switch", "rohitg00/ai-engineering-from-scratch", "NousResearch/hermes-agent", "mattpocock/skills", "pewdiepie-archdaemon/odysseus", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph", "Egonex-AI/Understand-Anything"], "data": [686, 747, 796, 800, 826, 880, 958, 989, 1041, 1101, 1102, 1255, 1265, 1644, 1917, 1948, 2500, 2566, 2879, 2965]}
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
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +98 | 36396 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +47 | 6932 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +34 | 34211 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +26 | 34321 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +21 | 46556 |
| 6 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +13 | 51608 |
| 7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +13 | 31864 |
| 8 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +12 | 3786 |
| 9 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +11 | 19266 |
| 10 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +10 | 13368 |
| 11 | [dzcmemory-web/bazi-ziwei-skill](https://github.com/dzcmemory-web/bazi-ziwei-skill) | +9 | 379 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +9 | 63667 |
| 13 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 28699 |
| 14 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +9 | 32726 |
| 15 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 7910 |
| 16 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +8 | 7929 |
| 17 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +7 | 5833 |
| 18 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +7 | 3918 |
| 19 | [alibaba/zvec](https://github.com/alibaba/zvec) | +7 | 11190 |
| 20 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +6 | 37847 |
| 21 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +6 | 495 |
| 22 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +6 | 1014 |
| 23 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 34388 |
| 24 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 33958 |
| 25 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +5 | 23369 |
| 26 | [Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM) | +5 | 4457 |
| 27 | [microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach) | +5 | 2552 |
| 28 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 28681 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +5 | 35395 |
| 30 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +5 | 22837 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +800 | 36396 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +301 | 34211 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +287 | 34321 |
| 4 | [apple/container](https://github.com/apple/container) | +262 | 38561 |
| 5 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +247 | 9772 |
| 6 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +190 | 7910 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +177 | 46556 |
| 8 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +171 | 44381 |
| 9 | [shadcn/improve](https://github.com/shadcn/improve) | +162 | 5462 |
| 10 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +159 | 51608 |
| 11 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +120 | 3786 |
| 12 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +120 | 3918 |
| 13 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +97 | 31575 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +84 | 34388 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +82 | 29154 |
| 16 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | +82 | 32567 |
| 17 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +78 | 32726 |
| 18 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +71 | 6932 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +69 | 63667 |
| 20 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +65 | 39465 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +64 | 30651 |
| 22 | [tamnd/kage](https://github.com/tamnd/kage) | +62 | 1999 |
| 23 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +62 | 28699 |
| 24 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +59 | 16704 |
| 25 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +58 | 2854 |
| 26 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +56 | 21094 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +55 | 13368 |
| 28 | [SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI) | +54 | 1404 |
| 29 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +54 | 32872 |
| 30 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +52 | 7929 |
| 31 | [tw93/Kami](https://github.com/tw93/Kami) | +52 | 8900 |
| 32 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +50 | 30683 |
| 33 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +47 | 35395 |
| 34 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +46 | 4044 |
| 35 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +45 | 10787 |
| 36 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +45 | 12409 |
| 37 | [google-research/timesfm](https://github.com/google-research/timesfm) | +45 | 23039 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +43 | 43114 |
| 39 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 23027 |
| 40 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +43 | 4467 |
| 41 | [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing) | +43 | 809 |
| 42 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 0 |
| 43 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +40 | 32611 |
| 44 | [DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop) | +40 | 511 |
| 45 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +39 | 28380 |
| 46 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +39 | 4164 |
| 47 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +39 | 6684 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +37 | 23369 |
| 49 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +37 | 3607 |
| 50 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +36 | 5200 |
| 51 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +36 | 33958 |
| 52 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +36 | 1049 |
| 53 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 24901 |
| 54 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +34 | 31864 |
| 55 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +34 | 23353 |
| 56 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +33 | 1018 |
| 57 | [alibaba/zvec](https://github.com/alibaba/zvec) | +32 | 11190 |
| 58 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +32 | 19266 |
| 59 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +32 | 17992 |
| 60 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +32 | 26517 |
| 61 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +32 | 6356 |
| 62 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +31 | 15480 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +31 | 21166 |
| 64 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +30 | 25138 |
| 65 | [getkimchi/kimchi](https://github.com/getkimchi/kimchi) | +30 | 1604 |
| 66 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +30 | 22184 |
| 67 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +29 | 4861 |
| 68 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +28 | 9458 |
| 69 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +28 | 1163 |
| 70 | [telemt/telemt](https://github.com/telemt/telemt) | +28 | 5276 |
| 71 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +28 | 3201 |
| 72 | [loc567/loc567](https://github.com/loc567/loc567) | +27 | 1139 |
| 73 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +27 | 24875 |
| 74 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +27 | 2556 |
| 75 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +27 | 12575 |
| 76 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +27 | 15208 |
| 77 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +26 | 37847 |
| 78 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +26 | 19180 |
| 79 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +26 | 31187 |
| 80 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +26 | 58270 |
| 81 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +26 | 43419 |
| 82 | [coder/boo](https://github.com/coder/boo) | +26 | 661 |
| 83 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +25 | 6237 |
| 84 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +25 | 3391 |
| 85 | [TestSprite/testsprite-cli](https://github.com/TestSprite/testsprite-cli) | +25 | 478 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +24 | 37166 |
| 87 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +24 | 41058 |
| 88 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +24 | 38660 |
| 89 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +24 | 11923 |
| 90 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +24 | 3339 |
| 91 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +24 | 21727 |
| 92 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +23 | 37539 |
| 93 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +22 | 29151 |
| 94 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +21 | 16443 |
| 95 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +21 | 21948 |
| 96 | [stablyai/orca](https://github.com/stablyai/orca) | +21 | 5333 |
| 97 | [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | +21 | 12676 |
| 98 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +21 | 2943 |
| 99 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +20 | 2272 |
| 100 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +19 | 28681 |
| 101 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +18 | 4348 |
| 102 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +18 | 7097 |
| 103 | [LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem) | +18 | 588 |
| 104 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +17 | 495 |
| 105 | [alchaincyf/loop-engineering-orange-book](https://github.com/alchaincyf/loop-engineering-orange-book) | +17 | 668 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +17 | 30392 |
| 107 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +16 | 5833 |
| 108 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +16 | 18472 |
| 109 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +16 | 14678 |
| 110 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +16 | 7790 |
| 111 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +15 | 1723 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 16615 |
| 113 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +15 | 23584 |
| 114 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +15 | 3421 |
| 115 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +15 | 44438 |
| 116 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +15 | 9212 |
| 117 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +15 | 1851 |
| 118 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +14 | 2928 |
| 119 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +14 | 8220 |
| 120 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +14 | 4965 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2965 | 63480 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2879 | 51608 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2566 | 178311 |
| 4 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2500 | 73601 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1948 | 135300 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1917 | 196955 |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1644 | 34388 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1265 | 104169 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1255 | 46556 |
| 10 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1102 | 34211 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1101 | 32726 |
| 12 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1041 | 49621 |
| 13 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +989 | 32611 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +958 | 69117 |
| 15 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +880 | 30392 |
| 16 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +826 | 44381 |
| 17 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +800 | 36397 |
| 18 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +796 | 74561 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +747 | 62869 |
| 20 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +686 | 26517 |
| 21 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +682 | 34148 |
| 22 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +638 | 23353 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +618 | 64811 |
| 24 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +608 | 74521 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +600 | 34322 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +553 | 63667 |
| 27 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +547 | 11923 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +530 | 21094 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +525 | 10787 |
| 30 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +524 | 21166 |
| 31 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +514 | 16443 |
| 32 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +507 | 35395 |
| 33 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +497 | 60220 |
| 34 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +489 | 29154 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +482 | 13368 |
| 36 | [multica-ai/multica](https://github.com/multica-ai/multica) | +447 | 37166 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +432 | 28699 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +428 | 39465 |
| 39 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +406 | 30651 |
| 40 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9276 |
| 41 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +390 | 38660 |
| 42 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +387 | 7929 |
| 43 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +386 | 27093 |
| 44 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +383 | 4517 |
| 45 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +382 | 31575 |
| 46 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +382 | 43419 |
| 47 | [apple/container](https://github.com/apple/container) | +371 | 38561 |
| 48 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +358 | 31864 |
| 49 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +356 | 8375 |
| 50 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +352 | 22390 |
| 51 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8256 |
| 52 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +339 | 9772 |
| 53 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +332 | 10406 |
| 54 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +331 | 9458 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +328 | 28380 |
| 56 | [decolua/9router](https://github.com/decolua/9router) | +325 | 17911 |
| 57 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +318 | 23369 |
| 58 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +317 | 5760 |
| 59 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +312 | 14678 |
| 60 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +300 | 12395 |
| 61 | [roboflow/supervision](https://github.com/roboflow/supervision) | +298 | 36553 |
| 62 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +291 | 21421 |
| 63 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +284 | 12409 |
| 64 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +281 | 43114 |
| 65 | [MinishLab/semble](https://github.com/MinishLab/semble) | +280 | 5274 |
| 66 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +278 | 17992 |
| 67 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +269 | 4467 |
| 68 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +269 | 5261 |
| 69 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +268 | 5293 |
| 70 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +266 | 16704 |
| 71 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +263 | 23027 |
| 72 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +262 | 8330 |
| 73 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +259 | 9404 |
| 74 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +257 | 43947 |
| 75 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +248 | 39319 |
| 76 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +248 | 17096 |
| 77 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +246 | 7910 |
| 78 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +245 | 28682 |
| 79 | [blader/humanizer](https://github.com/blader/humanizer) | +243 | 24901 |
| 80 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 3071 |
| 81 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +239 | 19180 |
| 82 | [soxoj/maigret](https://github.com/soxoj/maigret) | +237 | 33257 |
| 83 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +235 | 4965 |
| 84 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +234 | 30521 |
| 85 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +232 | 3905 |
| 86 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +231 | 30683 |
| 87 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +229 | 24875 |
| 88 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +228 | 13895 |
| 89 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +227 | 12575 |
| 90 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3454 |
| 91 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +224 | 58270 |
| 92 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +221 | 35293 |
| 93 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +220 | 37539 |
| 94 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +218 | 4464 |
| 95 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +216 | 33958 |
| 96 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 97 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +215 | 3877 |
| 98 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9292 |
| 99 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +213 | 16615 |
| 100 | [google/skills](https://github.com/google/skills) | +210 | 13903 |
| 101 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +209 | 37847 |
| 102 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +209 | 19964 |
| 103 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +206 | 42427 |
| 104 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +205 | 4348 |
| 105 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +204 | 6237 |
| 106 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +201 | 31187 |
| 107 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4071 |
| 108 | [88lin/video_vip](https://github.com/88lin/video_vip) | +198 | 4148 |
| 109 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +197 | 22184 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +192 | 16616 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +190 | 15480 |
| 112 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +188 | 7214 |
| 113 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +188 | 6684 |
| 114 | [shadcn/improve](https://github.com/shadcn/improve) | +187 | 5462 |
| 115 | [openai/skills](https://github.com/openai/skills) | +187 | 22487 |
| 116 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +186 | 4164 |
| 117 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +186 | 6631 |
| 118 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +185 | 2556 |
| 119 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +184 | 31098 |
| 120 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +182 | 5497 |
| 121 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +179 | 4577 |
| 122 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +179 | 4218 |
| 123 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +175 | 11602 |
| 124 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +173 | 21727 |
| 125 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +173 | 41058 |
| 126 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +171 | 4690 |
| 127 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +171 | 18472 |
| 128 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +170 | 25138 |
| 129 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +169 | 19852 |
| 130 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +169 | 6624 |
| 131 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +167 | 5200 |
| 132 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +167 | 3421 |
| 133 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +167 | 46792 |
| 134 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +163 | 25306 |
| 135 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +161 | 36799 |
| 136 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +160 | 35153 |
| 137 | [mattzh72/articraft](https://github.com/mattzh72/articraft) | +158 | 1307 |
| 138 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +157 | 16799 |
| 139 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +156 | 12316 |
| 140 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +155 | 7699 |
| 141 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3451 |
| 142 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +151 | 8220 |
| 143 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +147 | 3297 |
| 144 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +146 | 23628 |
| 145 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2555 |
| 146 | [jundot/omlx](https://github.com/jundot/omlx) | +142 | 16811 |
| 147 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +136 | 49470 |
| 148 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +135 | 27330 |
| 149 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +127 | 15073 |
| 150 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +127 | 32872 |
| 151 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1985 |
| 152 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2096 |
| 153 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +125 | 7790 |
| 154 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +125 | 4402 |
| 155 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +125 | 35259 |
| 156 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +125 | 24741 |
| 157 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 2951 |
| 158 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +119 | 2455 |
| 159 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +118 | 23584 |
| 160 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +118 | 3255 |
| 161 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6869 |
| 162 | [browser-use/video-use](https://github.com/browser-use/video-use) | +113 | 9875 |
| 163 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +113 | 18669 |
| 164 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +111 | 7164 |
| 165 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +110 | 9212 |
| 166 | [floci-io/floci](https://github.com/floci-io/floci) | +110 | 14253 |
| 167 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +108 | 25425 |
| 168 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +107 | 25794 |
| 169 | [openai/plugins](https://github.com/openai/plugins) | +106 | 3180 |
| 170 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +103 | 24822 |
| 171 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +101 | 6930 |
| 172 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +99 | 7578 |
| 173 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +98 | 44438 |
| 174 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +98 | 12146 |
| 175 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +97 | 11363 |
| 176 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +97 | 4983 |
| 177 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +94 | 21260 |
| 178 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +91 | 7097 |
| 179 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +88 | 5030 |
| 180 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1104 |
| 181 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +84 | 28666 |
| 182 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +82 | 27328 |
| 183 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +81 | 3934 |
| 184 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3607 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +76 | 16020 |
| 186 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +76 | 29556 |
| 187 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +75 | 18482 |
| 188 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +74 | 3918 |
| 189 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +72 | 5766 |
| 190 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +70 | 3786 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +66 | 36103 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +65 | 4491 |
| 193 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +65 | 37564 |
| 194 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +64 | 4895 |
| 195 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +63 | 28095 |
| 196 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +63 | 1282 |
| 197 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +61 | 3121 |
| 198 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +59 | 8707 |
| 199 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +57 | 2717 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +55 | 16726 |
| 201 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +52 | 5166 |
| 202 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +50 | 1687 |
| 203 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +49 | 1115 |
| 204 | [eze-is/web-access](https://github.com/eze-is/web-access) | +49 | 7717 |
| 205 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +46 | 8130 |
| 206 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +45 | 515 |
| 207 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +43 | 5721 |
| 208 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +43 | 1569 |
| 209 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +43 | 11206 |
| 210 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +41 | 1668 |
| 211 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +40 | 5291 |
| 212 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +37 | 1263 |
| 213 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +36 | 607 |
| 214 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +35 | 2357 |
| 215 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4284 |
| 216 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +33 | 776 |
| 217 | [Nieobie/Game-Icon-Pack](https://github.com/Nieobie/Game-Icon-Pack) | +33 | 500 |
| 218 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +33 | 3935 |
| 219 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +33 | 855 |
| 220 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9416 |
| 221 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +31 | 2799 |
| 222 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +29 | 3726 |
| 223 | [sandeco/reversa](https://github.com/sandeco/reversa) | +28 | 1237 |
| 224 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +27 | 3279 |
| 225 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 923 |
| 226 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +26 | 1921 |
| 227 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +26 | 2827 |
| 228 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +25 | 5084 |
| 229 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +25 | 2255 |
| 230 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 737 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +24 | 13734 |
| 232 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 204 |
| 233 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +23 | 1893 |
| 234 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +23 | 8253 |
| 235 | [robinebers/openusage](https://github.com/robinebers/openusage) | +23 | 2908 |
| 236 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +23 | 755 |
| 237 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 26 |
| 238 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +22 | 4497 |
| 239 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +22 | 1694 |
| 240 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +22 | 10262 |
| 241 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +21 | 4471 |
| 242 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +21 | 2188 |
| 243 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 523 |
| 244 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +20 | 1969 |
| 245 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +20 | 12131 |
| 246 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +19 | 444 |
| 247 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +19 | 2581 |
| 248 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +18 | 704 |
| 249 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +18 | 376 |
| 250 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +18 | 587 |
| 251 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +18 | 2512 |
| 252 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +17 | 2103 |
| 253 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +17 | 1362 |
| 254 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +17 | 2844 |
| 255 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +17 | 2024 |
| 256 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +16 | 679 |
| 257 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +16 | 2677 |
| 258 | [royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram) | +15 | 466 |
| 259 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 362 |
| 260 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +15 | 413 |
| 261 | [openmemind/memind](https://github.com/openmemind/memind) | +15 | 901 |
| 262 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 341 |
| 263 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +14 | 167 |
| 264 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +14 | 732 |
| 265 | [Shiyao-Huang/awesome-agent-evolution](https://github.com/Shiyao-Huang/awesome-agent-evolution) | +14 | 170 |
| 266 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 558 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +14 | 2560 |
| 268 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +14 | 314 |
| 269 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +12 | 1165 |
| 270 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 270 |
| 271 | [buynao/aipath](https://github.com/buynao/aipath) | +12 | 319 |
| 272 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +12 | 525 |
| 273 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +12 | 644 |
| 274 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 270 |
| 275 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +12 | 294 |
| 276 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3457 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1650 |
| 278 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 114 |
| 279 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +10 | 120 |
| 280 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +10 | 2588 |
| 281 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3009 |
| 282 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +9 | 110 |
| 283 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +9 | 2488 |
| 284 | [emollick/concord](https://github.com/emollick/concord) | +8 | 191 |
| 285 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +8 | 893 |
| 286 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +8 | 1619 |
| 287 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +8 | 229 |
| 288 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 64 |
| 289 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +7 | 242 |
| 290 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +7 | 8573 |
| 291 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +7 | 461 |
| 292 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 162 |
| 293 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 95 |
| 294 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +6 | 284 |
| 295 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +6 | 132 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +6 | 2128 |
| 297 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +6 | 497 |
| 298 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 161 |
| 299 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +6 | 1015 |
| 300 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +6 | 264 |
