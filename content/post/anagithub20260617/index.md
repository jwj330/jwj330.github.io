---
title: "2026-06-17 GitHub增长趋势报告"
description: "1.ponytail+161 2.Agent-Reach+41 3.codegraph+22 4.headroom+22 5.taste-skill+17"
date: 2026-06-17T22:02:03+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-17 22:02:03

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
        'daily': {"categories": ["Emily2040/seedance-2.0", "zai-org/GLM-5", "yifanfeng97/Hyper-Extract", "agentscope-ai/QwenPaw", "shanraisshan/claude-code-best-practice", "OpenBMB/VoxCPM", "rohitg00/ai-engineering-from-scratch", "rtk-ai/rtk", "ZhuLinsen/daily_stock_analysis", "alibaba/zvec", "mvanhorn/last30days-skill", "VitoHowe/glm-coding", "GoogleCloudPlatform/knowledge-catalog", "hugohe3/ppt-master", "omnigent-ai/omnigent", "Leonxlnx/taste-skill", "chopratejas/headroom", "colbymchenry/codegraph", "Panniantong/Agent-Reach", "DietrichGebert/ponytail"], "data": [6, 6, 6, 7, 7, 7, 9, 9, 9, 10, 11, 11, 13, 14, 15, 17, 22, 22, 41, 161]},
        'weekly': {"categories": ["OpenBMB/VoxCPM", "rtk-ai/rtk", "pbakaus/impeccable", "chatwoot/chatwoot", "Imbad0202/academic-research-skills", "refactoringhq/tolaria", "rohitg00/ai-engineering-from-scratch", "hugohe3/ppt-master", "lfnovo/open-notebook", "omnigent-ai/omnigent", "GoogleCloudPlatform/knowledge-catalog", "colbymchenry/codegraph", "shadcn/improve", "Leonxlnx/taste-skill", "NVIDIA/SkillSpector", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "chopratejas/headroom", "apple/container", "DietrichGebert/ponytail"], "data": [66, 70, 73, 78, 82, 84, 88, 89, 100, 108, 113, 169, 179, 189, 190, 195, 277, 299, 313, 706]},
        'monthly': {"categories": ["rohitg00/agentmemory", "addyosmani/agent-skills", "CloakHQ/CloakBrowser", "mvanhorn/last30days-skill", "ruvnet/RuView", "anthropics/claude-plugins-official", "safishamsi/graphify", "harry0703/MoneyPrinterTurbo", "chopratejas/headroom", "Imbad0202/academic-research-skills", "Leonxlnx/taste-skill", "tinyhumansai/openhuman", "farion1231/cc-switch", "rohitg00/ai-engineering-from-scratch", "NousResearch/hermes-agent", "mattpocock/skills", "pewdiepie-archdaemon/odysseus", "forrestchang/andrej-karpathy-skills", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph"], "data": [747, 779, 796, 837, 864, 896, 981, 1032, 1070, 1211, 1259, 1294, 1335, 1646, 2074, 2137, 2488, 2723, 2961, 2967]}
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
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +161 | 31249 |
| 2 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +41 | 33079 |
| 3 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +22 | 51001 |
| 4 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +22 | 31410 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +17 | 45923 |
| 6 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +15 | 3464 |
| 7 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +14 | 28809 |
| 8 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +13 | 3567 |
| 9 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +11 | 393 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +11 | 43945 |
| 11 | [alibaba/zvec](https://github.com/alibaba/zvec) | +10 | 10800 |
| 12 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +9 | 42954 |
| 13 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +9 | 63314 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +9 | 34066 |
| 15 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +7 | 30432 |
| 16 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +7 | 58130 |
| 17 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +7 | 18890 |
| 18 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +6 | 1568 |
| 19 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +6 | 3767 |
| 20 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +6 | 1184 |
| 21 | [zts212653/clowder-ai](https://github.com/zts212653/clowder-ai) | +6 | 1498 |
| 22 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +6 | 15141 |
| 23 | [l0ng-ai/papr](https://github.com/l0ng-ai/papr) | +6 | 423 |
| 24 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +6 | 9315 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 39193 |
| 26 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +6 | 5095 |
| 27 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +5 | 35138 |
| 28 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 28239 |
| 29 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +5 | 1524 |
| 30 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5 | 28413 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +706 | 31249 |
| 2 | [apple/container](https://github.com/apple/container) | +313 | 38196 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +299 | 31412 |
| 4 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +277 | 33079 |
| 5 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +195 | 43945 |
| 6 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +190 | 7432 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +189 | 45923 |
| 8 | [shadcn/improve](https://github.com/shadcn/improve) | +179 | 5188 |
| 9 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +169 | 51001 |
| 10 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +113 | 3567 |
| 11 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +108 | 3464 |
| 12 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +100 | 31338 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +89 | 28809 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +88 | 34066 |
| 15 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +84 | 16627 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +82 | 32448 |
| 17 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | +78 | 32336 |
| 18 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +73 | 39193 |
| 19 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +70 | 63314 |
| 20 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +66 | 30432 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +64 | 28413 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +63 | 20826 |
| 23 | [tamnd/kage](https://github.com/tamnd/kage) | +60 | 1852 |
| 24 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +58 | 2792 |
| 25 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +56 | 32872 |
| 26 | [SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI) | +55 | 1370 |
| 27 | [tw93/Kami](https://github.com/tw93/Kami) | +54 | 8834 |
| 28 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +52 | 13141 |
| 29 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +52 | 10673 |
| 30 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +50 | 42954 |
| 31 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +50 | 3583 |
| 32 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +49 | 30601 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +47 | 7739 |
| 34 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +45 | 35138 |
| 35 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +45 | 12389 |
| 36 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +45 | 32540 |
| 37 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +45 | 6612 |
| 38 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +44 | 28239 |
| 39 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +44 | 4411 |
| 40 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +44 | 3831 |
| 41 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 22935 |
| 42 | [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing) | +43 | 769 |
| 43 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +43 | 6339 |
| 44 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +42 | 4116 |
| 45 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +42 | 950 |
| 46 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +40 | 6647 |
| 47 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +40 | 23218 |
| 48 | [DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop) | +40 | 500 |
| 49 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +39 | 17841 |
| 50 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +39 | 37455 |
| 51 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +38 | 23260 |
| 52 | [blader/humanizer](https://github.com/blader/humanizer) | +37 | 24721 |
| 53 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +36 | 5017 |
| 54 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +36 | 1022 |
| 55 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +36 | 26426 |
| 56 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +36 | 21030 |
| 57 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +33 | 11864 |
| 58 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +33 | 1011 |
| 59 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 33804 |
| 60 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +32 | 15141 |
| 61 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +31 | 24725 |
| 62 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +30 | 25068 |
| 63 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +30 | 12461 |
| 64 | [getkimchi/kimchi](https://github.com/getkimchi/kimchi) | +29 | 1514 |
| 65 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +29 | 15415 |
| 66 | [extend-hq/ui](https://github.com/extend-hq/ui) | +29 | 1119 |
| 67 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +28 | 4796 |
| 68 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +28 | 22044 |
| 69 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +28 | 58130 |
| 70 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +28 | 1149 |
| 71 | [telemt/telemt](https://github.com/telemt/telemt) | +28 | 5255 |
| 72 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +28 | 21642 |
| 73 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +28 | 3183 |
| 74 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +27 | 3362 |
| 75 | [multica-ai/multica](https://github.com/multica-ai/multica) | +27 | 37046 |
| 76 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +27 | 19092 |
| 77 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +27 | 31086 |
| 78 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +26 | 9315 |
| 79 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +26 | 40986 |
| 80 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +26 | 2518 |
| 81 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +26 | 2563 |
| 82 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +26 | 3247 |
| 83 | [alibaba/zvec](https://github.com/alibaba/zvec) | +25 | 10800 |
| 84 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +25 | 29053 |
| 85 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +25 | 16144 |
| 86 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +25 | 38578 |
| 87 | [coder/boo](https://github.com/coder/boo) | +25 | 649 |
| 88 | [google/skills](https://github.com/google/skills) | +25 | 13848 |
| 89 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +24 | 5095 |
| 90 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +24 | 17663 |
| 91 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +23 | 31510 |
| 92 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +23 | 12359 |
| 93 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +22 | 8756 |
| 94 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +21 | 18890 |
| 95 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +21 | 6124 |
| 96 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +21 | 14953 |
| 97 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +21 | 2896 |
| 98 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +21 | 43332 |
| 99 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +21 | 3833 |
| 100 | [stablyai/orca](https://github.com/stablyai/orca) | +20 | 5205 |
| 101 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +20 | 37771 |
| 102 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +20 | 8098 |
| 103 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +19 | 5870 |
| 104 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +19 | 2230 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +18 | 18357 |
| 106 | [LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem) | +18 | 530 |
| 107 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +18 | 28526 |
| 108 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +18 | 30341 |
| 109 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +17 | 4560 |
| 110 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +16 | 16573 |
| 111 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +16 | 4292 |
| 112 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +16 | 14627 |
| 113 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +16 | 7033 |
| 114 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +16 | 3374 |
| 115 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +16 | 2888 |
| 116 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +16 | 44392 |
| 117 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +15 | 23534 |
| 118 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +15 | 7682 |
| 119 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +15 | 9142 |
| 120 | [liaohch3/claude-tap](https://github.com/liaohch3/claude-tap) | +15 | 1824 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2967 | 51001 |
| 2 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2961 | 62717 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2723 | 177593 |
| 4 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2488 | 73030 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2137 | 133403 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2074 | 196140 |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1646 | 34066 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1335 | 103427 |
| 9 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1294 | 32540 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1259 | 45923 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1211 | 32448 |
| 12 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1070 | 31413 |
| 13 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1032 | 49621 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +981 | 68676 |
| 15 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +896 | 30341 |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +864 | 74383 |
| 17 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +837 | 43945 |
| 18 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +796 | 26426 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +779 | 62200 |
| 20 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +747 | 23260 |
| 21 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +706 | 31249 |
| 22 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +682 | 34148 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +647 | 64606 |
| 24 | [earendil-works/pi](https://github.com/earendil-works/pi) | +640 | 63583 |
| 25 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +608 | 74050 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +591 | 63314 |
| 27 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +585 | 33079 |
| 28 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +572 | 20826 |
| 29 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +559 | 11864 |
| 30 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +528 | 21030 |
| 31 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +527 | 35138 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +523 | 10673 |
| 33 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +517 | 28809 |
| 34 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +514 | 16144 |
| 35 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +497 | 60037 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +475 | 13141 |
| 37 | [multica-ai/multica](https://github.com/multica-ai/multica) | +469 | 37046 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +467 | 28413 |
| 39 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +461 | 38578 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +446 | 43332 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +438 | 39193 |
| 42 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +436 | 9315 |
| 43 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +415 | 31510 |
| 44 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +407 | 30432 |
| 45 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9237 |
| 46 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +396 | 27009 |
| 47 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +383 | 4485 |
| 48 | [decolua/9router](https://github.com/decolua/9router) | +382 | 17832 |
| 49 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +379 | 7739 |
| 50 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +377 | 31338 |
| 51 | [apple/container](https://github.com/apple/container) | +369 | 38196 |
| 52 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +365 | 23218 |
| 53 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +365 | 10331 |
| 54 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +359 | 22302 |
| 55 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +357 | 12389 |
| 56 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +356 | 8357 |
| 57 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8256 |
| 58 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +345 | 21376 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +344 | 28239 |
| 60 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +334 | 5706 |
| 61 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +323 | 14627 |
| 62 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +317 | 12359 |
| 63 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +305 | 17064 |
| 64 | [roboflow/supervision](https://github.com/roboflow/supervision) | +303 | 36553 |
| 65 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +303 | 17841 |
| 66 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +299 | 42954 |
| 67 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +296 | 22935 |
| 68 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +296 | 28526 |
| 69 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +296 | 5252 |
| 70 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +288 | 19853 |
| 71 | [MinishLab/semble](https://github.com/MinishLab/semble) | +281 | 5230 |
| 72 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +276 | 30229 |
| 73 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +270 | 16627 |
| 74 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +268 | 5278 |
| 75 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +266 | 4411 |
| 76 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +266 | 43868 |
| 77 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +264 | 9345 |
| 78 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +264 | 39219 |
| 79 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +262 | 8319 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +257 | 24721 |
| 81 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +249 | 6124 |
| 82 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +247 | 19092 |
| 83 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +247 | 13838 |
| 84 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 3044 |
| 85 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +238 | 7432 |
| 86 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +238 | 30601 |
| 87 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +238 | 58130 |
| 88 | [soxoj/maigret](https://github.com/soxoj/maigret) | +237 | 33205 |
| 89 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +235 | 24725 |
| 90 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +235 | 4913 |
| 91 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +232 | 3899 |
| 92 | [google/skills](https://github.com/google/skills) | +230 | 13848 |
| 93 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +229 | 12461 |
| 94 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +228 | 33804 |
| 95 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +226 | 42381 |
| 96 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3434 |
| 97 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +223 | 35252 |
| 98 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +222 | 7133 |
| 99 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +220 | 37455 |
| 100 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +218 | 3839 |
| 101 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +218 | 4438 |
| 102 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +216 | 37771 |
| 103 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 104 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9271 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +213 | 16573 |
| 106 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +207 | 22044 |
| 107 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +205 | 4292 |
| 108 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +202 | 31086 |
| 109 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4067 |
| 110 | [88lin/video_vip](https://github.com/88lin/video_vip) | +196 | 4125 |
| 111 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +195 | 15415 |
| 112 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +193 | 6585 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +192 | 16520 |
| 114 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +191 | 31098 |
| 115 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +188 | 6647 |
| 116 | [openai/skills](https://github.com/openai/skills) | +187 | 22414 |
| 117 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +185 | 2518 |
| 118 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +182 | 5481 |
| 119 | [shadcn/improve](https://github.com/shadcn/improve) | +179 | 5188 |
| 120 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +179 | 4560 |
| 121 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +179 | 4156 |
| 122 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +176 | 21642 |
| 123 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +175 | 11555 |
| 124 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +173 | 40986 |
| 125 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +171 | 4652 |
| 126 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +171 | 18357 |
| 127 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +170 | 25068 |
| 128 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6612 |
| 129 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +169 | 19813 |
| 130 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +167 | 3374 |
| 131 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +167 | 46726 |
| 132 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +164 | 7666 |
| 133 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +164 | 25242 |
| 134 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +163 | 5017 |
| 135 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +161 | 36799 |
| 136 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +160 | 35054 |
| 137 | [mattzh72/articraft](https://github.com/mattzh72/articraft) | +158 | 1306 |
| 138 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +157 | 16765 |
| 139 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +156 | 12267 |
| 140 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +153 | 2453 |
| 141 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3432 |
| 142 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +151 | 8174 |
| 143 | [floci-io/floci](https://github.com/floci-io/floci) | +149 | 14220 |
| 144 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +147 | 3256 |
| 145 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +147 | 24647 |
| 146 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +146 | 23592 |
| 147 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2523 |
| 148 | [jundot/omlx](https://github.com/jundot/omlx) | +142 | 16767 |
| 149 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +136 | 49443 |
| 150 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +135 | 27298 |
| 151 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +127 | 15016 |
| 152 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1986 |
| 153 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2093 |
| 154 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +125 | 7682 |
| 155 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +125 | 4385 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +125 | 35194 |
| 157 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +124 | 32872 |
| 158 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 2951 |
| 159 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +118 | 23534 |
| 160 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +118 | 3222 |
| 161 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6821 |
| 162 | [browser-use/video-use](https://github.com/browser-use/video-use) | +113 | 9805 |
| 163 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +113 | 18630 |
| 164 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +113 | 25373 |
| 165 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +111 | 7116 |
| 166 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +110 | 9142 |
| 167 | [openai/plugins](https://github.com/openai/plugins) | +108 | 3145 |
| 168 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +107 | 25770 |
| 169 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +105 | 21194 |
| 170 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +104 | 6881 |
| 171 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +103 | 24782 |
| 172 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +102 | 4946 |
| 173 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +99 | 11305 |
| 174 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +99 | 7551 |
| 175 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +98 | 44392 |
| 176 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +97 | 12142 |
| 177 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +91 | 7033 |
| 178 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +87 | 5001 |
| 179 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +87 | 27279 |
| 180 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1104 |
| 181 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +84 | 28613 |
| 182 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +84 | 15972 |
| 183 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +81 | 3833 |
| 184 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +81 | 29524 |
| 185 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3583 |
| 186 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +78 | 5753 |
| 187 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +78 | 18438 |
| 188 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +74 | 3567 |
| 189 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +74 | 37564 |
| 190 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +72 | 4440 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +72 | 36103 |
| 192 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +70 | 3464 |
| 193 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +68 | 4887 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +66 | 28040 |
| 195 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +64 | 3051 |
| 196 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +63 | 1278 |
| 197 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +62 | 2686 |
| 198 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +61 | 8699 |
| 199 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +58 | 1687 |
| 200 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +56 | 16633 |
| 201 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +54 | 5140 |
| 202 | [eze-is/web-access](https://github.com/eze-is/web-access) | +51 | 7686 |
| 203 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +50 | 1110 |
| 204 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +49 | 1677 |
| 205 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +45 | 8092 |
| 206 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +45 | 511 |
| 207 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +44 | 5711 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +43 | 11178 |
| 209 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +43 | 5265 |
| 210 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +42 | 1643 |
| 211 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +41 | 1524 |
| 212 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +39 | 2351 |
| 213 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +39 | 1256 |
| 214 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +37 | 2834 |
| 215 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +36 | 598 |
| 216 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +36 | 855 |
| 217 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +35 | 2774 |
| 218 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +34 | 3701 |
| 219 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4281 |
| 220 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +34 | 3897 |
| 221 | [Nieobie/Game-Icon-Pack](https://github.com/Nieobie/Game-Icon-Pack) | +33 | 498 |
| 222 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +33 | 9414 |
| 223 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +32 | 748 |
| 224 | [sandeco/reversa](https://github.com/sandeco/reversa) | +32 | 1234 |
| 225 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +31 | 804 |
| 226 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +30 | 2824 |
| 227 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +29 | 2244 |
| 228 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 910 |
| 229 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +26 | 1913 |
| 230 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +26 | 8249 |
| 231 | [robinebers/openusage](https://github.com/robinebers/openusage) | +25 | 2903 |
| 232 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +25 | 5072 |
| 233 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +25 | 13714 |
| 234 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +25 | 702 |
| 235 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 735 |
| 236 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +24 | 10261 |
| 237 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 204 |
| 238 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +23 | 1884 |
| 239 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 26 |
| 240 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +23 | 2174 |
| 241 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +22 | 1961 |
| 242 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +21 | 12121 |
| 243 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +21 | 4472 |
| 244 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +21 | 371 |
| 245 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +21 | 2493 |
| 246 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +21 | 2565 |
| 247 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 523 |
| 248 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +20 | 4454 |
| 249 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +20 | 292 |
| 250 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +19 | 431 |
| 251 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +19 | 585 |
| 252 | [browserbase/skills](https://github.com/browserbase/skills) | +19 | 3565 |
| 253 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +18 | 2094 |
| 254 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +18 | 695 |
| 255 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +17 | 1352 |
| 256 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +17 | 2011 |
| 257 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +17 | 13608 |
| 258 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +16 | 673 |
| 259 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +16 | 2672 |
| 260 | [openmemind/memind](https://github.com/openmemind/memind) | +16 | 901 |
| 261 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 361 |
| 262 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +15 | 728 |
| 263 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +15 | 555 |
| 264 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +15 | 408 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +15 | 2545 |
| 266 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +15 | 3451 |
| 267 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +15 | 314 |
| 268 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +14 | 335 |
| 269 | [royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram) | +14 | 449 |
| 270 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +12 | 1160 |
| 271 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 263 |
| 272 | [buynao/aipath](https://github.com/buynao/aipath) | +12 | 303 |
| 273 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +12 | 516 |
| 274 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +12 | 624 |
| 275 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +12 | 2481 |
| 276 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 270 |
| 277 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1639 |
| 278 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 112 |
| 279 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +10 | 119 |
| 280 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 110 |
| 281 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +10 | 2582 |
| 282 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +10 | 3001 |
| 283 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +10 | 227 |
| 284 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +9 | 1619 |
| 285 | [emollick/concord](https://github.com/emollick/concord) | +8 | 190 |
| 286 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +8 | 891 |
| 287 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 63 |
| 288 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +7 | 425 |
| 289 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +7 | 240 |
| 290 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +7 | 8568 |
| 291 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +7 | 1014 |
| 292 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +7 | 461 |
| 293 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 3501 |
| 294 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 162 |
| 295 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 92 |
| 296 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +6 | 2128 |
| 297 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +6 | 494 |
| 298 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 160 |
| 299 | [spring-ai-alibaba/Lynxe](https://github.com/spring-ai-alibaba/Lynxe) | +6 | 1047 |
| 300 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +6 | 258 |
