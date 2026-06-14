---
title: "2026-06-14 GitHub增长趋势报告"
description: "1.Agent-Reach+102 2.headroom+89 3.container+62 4.last30days-skill+51 5.Understand-Anything+45"
date: 2026-06-14T21:14:51+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-14 21:14:51

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
        'daily': {"categories": ["Yuan1z0825/nature-skills", "tt-a1i/archify", "Imbad0202/academic-research-skills", "sleep3r/mtproto.zig", "Thysrael/Horizon", "heygen-com/hyperframes", "rohitg00/ai-engineering-from-scratch", "telemt/telemt", "kenn-io/agentsview", "supertone-inc/supertonic", "tw93/Kami", "lfnovo/open-notebook", "colbymchenry/codegraph", "GoogleCloudPlatform/knowledge-catalog", "Leonxlnx/taste-skill", "Egonex-AI/Understand-Anything", "mvanhorn/last30days-skill", "apple/container", "chopratejas/headroom", "Panniantong/Agent-Reach"], "data": [19, 20, 21, 22, 22, 23, 23, 24, 24, 29, 31, 34, 37, 37, 42, 45, 51, 62, 89, 102]},
        'weekly': {"categories": ["aaif-goose/goose", "yikart/AiToEarn", "heygen-com/hyperframes", "KunAgent/Kun", "Imbad0202/academic-research-skills", "rohitg00/ai-engineering-from-scratch", "pbakaus/impeccable", "santifer/career-ops", "alibaba/open-code-review", "refactoringhq/tolaria", "roboflow/supervision", "lfnovo/open-notebook", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph", "RyanCodrai/turbovec", "Panniantong/Agent-Reach", "apple/container", "Leonxlnx/taste-skill", "chopratejas/headroom", "mvanhorn/last30days-skill"], "data": [92, 96, 97, 98, 106, 109, 112, 122, 125, 147, 164, 165, 197, 224, 225, 256, 328, 333, 401, 523]},
        'monthly': {"categories": ["anthropics/claude-plugins-official", "rohitg00/agentmemory", "chopratejas/headroom", "msitarzewski/agency-agents", "harry0703/MoneyPrinterTurbo", "safishamsi/graphify", "CloakHQ/CloakBrowser", "ruvnet/RuView", "Leonxlnx/taste-skill", "Imbad0202/academic-research-skills", "farion1231/cc-switch", "rohitg00/ai-engineering-from-scratch", "tinyhumansai/openhuman", "affaan-m/ECC", "pewdiepie-archdaemon/odysseus", "NousResearch/hermes-agent", "mattpocock/skills", "Egonex-AI/Understand-Anything", "colbymchenry/codegraph", "forrestchang/andrej-karpathy-skills"], "data": [910, 986, 995, 1001, 1010, 1026, 1116, 1229, 1239, 1458, 1567, 1646, 1840, 1937, 2437, 2556, 2765, 2892, 3127, 3186]}
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
| 1 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +102 | 28645 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +89 | 27449 |
| 3 | [apple/container](https://github.com/apple/container) | +62 | 36921 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +51 | 41930 |
| 5 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +45 | 59144 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +42 | 43623 |
| 7 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +37 | 1266 |
| 8 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +37 | 48959 |
| 9 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +34 | 30481 |
| 10 | [tw93/Kami](https://github.com/tw93/Kami) | +31 | 8411 |
| 11 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +29 | 12143 |
| 12 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +24 | 2566 |
| 13 | [telemt/telemt](https://github.com/telemt/telemt) | +24 | 5032 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +23 | 32388 |
| 15 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +23 | 27605 |
| 16 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +22 | 6449 |
| 17 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +22 | 985 |
| 18 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +21 | 31366 |
| 19 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +20 | 925 |
| 20 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +19 | 19859 |
| 21 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +18 | 4152 |
| 22 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +17 | 42524 |
| 23 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +17 | 22489 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +17 | 38323 |
| 25 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +17 | 6922 |
| 26 | [santifer/career-ops](https://github.com/santifer/career-ops) | +17 | 53710 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +17 | 12404 |
| 28 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +16 | 3322 |
| 29 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +15 | 2067 |
| 30 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +15 | 709 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +523 | 41930 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +401 | 27449 |
| 3 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +333 | 43623 |
| 4 | [apple/container](https://github.com/apple/container) | +328 | 36921 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +256 | 28646 |
| 6 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +225 | 11488 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +224 | 48959 |
| 8 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +197 | 59144 |
| 9 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +165 | 30481 |
| 10 | [roboflow/supervision](https://github.com/roboflow/supervision) | +164 | 36553 |
| 11 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +147 | 16199 |
| 12 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +125 | 6922 |
| 13 | [santifer/career-ops](https://github.com/santifer/career-ops) | +122 | 53710 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +112 | 38323 |
| 15 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +109 | 32388 |
| 16 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +106 | 31366 |
| 17 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +98 | 4152 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +97 | 27605 |
| 19 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +96 | 21104 |
| 20 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +92 | 31098 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +90 | 10294 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +89 | 27504 |
| 23 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +84 | 18670 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +81 | 62279 |
| 25 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +76 | 30797 |
| 26 | [google/skills](https://github.com/google/skills) | +76 | 13671 |
| 27 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +73 | 19859 |
| 28 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +67 | 59122 |
| 29 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +67 | 37151 |
| 30 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +63 | 3467 |
| 31 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +62 | 12404 |
| 32 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +62 | 42334 |
| 33 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +61 | 27696 |
| 34 | [devenjarvis/lathe](https://github.com/devenjarvis/lathe) | +59 | 1449 |
| 35 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +58 | 2566 |
| 36 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +58 | 29140 |
| 37 | [NoopApp/noop](https://github.com/NoopApp/noop) | +56 | 1646 |
| 38 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +56 | 22744 |
| 39 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +55 | 22798 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +54 | 42524 |
| 41 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +53 | 34444 |
| 42 | [soxoj/maigret](https://github.com/soxoj/maigret) | +50 | 33049 |
| 43 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +50 | 11317 |
| 44 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +49 | 17188 |
| 45 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +48 | 20650 |
| 46 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +47 | 1266 |
| 47 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +47 | 3322 |
| 48 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +47 | 33300 |
| 49 | [openai/plugins](https://github.com/openai/plugins) | +47 | 3024 |
| 50 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +46 | 6252 |
| 51 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 24168 |
| 52 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +45 | 21275 |
| 53 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +44 | 26067 |
| 54 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +44 | 709 |
| 55 | [tw93/Kami](https://github.com/tw93/Kami) | +43 | 8411 |
| 56 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +43 | 4463 |
| 57 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +43 | 37499 |
| 58 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +43 | 8496 |
| 59 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +42 | 32096 |
| 60 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +40 | 22489 |
| 61 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +40 | 6449 |
| 62 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +40 | 12168 |
| 63 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +40 | 57697 |
| 64 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +39 | 2118 |
| 65 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +39 | 3638 |
| 66 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +39 | 2633 |
| 67 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +39 | 3382 |
| 68 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +39 | 4745 |
| 69 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +39 | 2759 |
| 70 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +38 | 29871 |
| 71 | [DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop) | +37 | 376 |
| 72 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +37 | 12152 |
| 73 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | +37 | 9043 |
| 74 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +36 | 12143 |
| 75 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +36 | 24291 |
| 76 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +36 | 5451 |
| 77 | [revfactory/harness](https://github.com/revfactory/harness) | +36 | 6966 |
| 78 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +35 | 31088 |
| 79 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +34 | 15686 |
| 80 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +33 | 21624 |
| 81 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +33 | 9176 |
| 82 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +33 | 7067 |
| 83 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +33 | 2921 |
| 84 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +33 | 43034 |
| 85 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 36554 |
| 86 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +32 | 38307 |
| 87 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +32 | 4840 |
| 88 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +32 | 3360 |
| 89 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 2067 |
| 90 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +30 | 2873 |
| 91 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +30 | 2379 |
| 92 | [run-llama/liteparse](https://github.com/run-llama/liteparse) | +30 | 10041 |
| 93 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +30 | 14413 |
| 94 | [francescopace/espectre](https://github.com/francescopace/espectre) | +30 | 8588 |
| 95 | [extend-hq/ui](https://github.com/extend-hq/ui) | +29 | 1057 |
| 96 | [telemt/telemt](https://github.com/telemt/telemt) | +28 | 5032 |
| 97 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +28 | 14866 |
| 98 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +27 | 985 |
| 99 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +27 | 40713 |
| 100 | [agent0ai/dox](https://github.com/agent0ai/dox) | +27 | 793 |
| 101 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +27 | 14755 |
| 102 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +27 | 4454 |
| 103 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +27 | 13655 |
| 104 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +26 | 24619 |
| 105 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +26 | 28195 |
| 106 | [openai/skills](https://github.com/openai/skills) | +26 | 22162 |
| 107 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +25 | 2394 |
| 108 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +24 | 2736 |
| 109 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +23 | 25635 |
| 110 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +22 | 3098 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +22 | 16421 |
| 112 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +22 | 8881 |
| 113 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +22 | 8021 |
| 114 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +21 | 3068 |
| 115 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +21 | 925 |
| 116 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +21 | 3083 |
| 117 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +21 | 3194 |
| 118 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +21 | 49340 |
| 119 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +20 | 44197 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +20 | 30122 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3186 | 175299 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3127 | 48959 |
| 3 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2892 | 59144 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2765 | 128695 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2556 | 193457 |
| 6 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2437 | 70902 |
| 7 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +1937 | 51199 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1840 | 32096 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1646 | 32388 |
| 10 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1567 | 100606 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1458 | 31367 |
| 12 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1239 | 43623 |
| 13 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1229 | 73825 |
| 14 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1116 | 26067 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1026 | 67102 |
| 16 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1010 | 49621 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1001 | 113134 |
| 18 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +995 | 27449 |
| 19 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +986 | 22798 |
| 20 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +910 | 30122 |
| 21 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +872 | 59396 |
| 22 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +807 | 41930 |
| 23 | [earendil-works/pi](https://github.com/earendil-works/pi) | +767 | 62584 |
| 24 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +750 | 63644 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +724 | 19859 |
| 26 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +713 | 38307 |
| 27 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +705 | 34148 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +702 | 62279 |
| 29 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +632 | 72463 |
| 30 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +632 | 12143 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +617 | 27504 |
| 32 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +600 | 11488 |
| 33 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +584 | 59461 |
| 34 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +577 | 34444 |
| 35 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +577 | 31088 |
| 36 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +543 | 28195 |
| 37 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +542 | 8275 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +534 | 27605 |
| 39 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +533 | 20650 |
| 40 | [decolua/9router](https://github.com/decolua/9router) | +533 | 17493 |
| 41 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +532 | 43034 |
| 42 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +526 | 15686 |
| 43 | [multica-ai/multica](https://github.com/multica-ai/multica) | +526 | 36554 |
| 44 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +520 | 59122 |
| 45 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +517 | 10294 |
| 46 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +486 | 38323 |
| 47 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +484 | 28647 |
| 48 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +483 | 12404 |
| 49 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +473 | 16907 |
| 50 | [santifer/career-ops](https://github.com/santifer/career-ops) | +469 | 53710 |
| 51 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +466 | 6745 |
| 52 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +461 | 21104 |
| 53 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +459 | 5677 |
| 54 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +452 | 8534 |
| 55 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +451 | 22744 |
| 56 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +435 | 19363 |
| 57 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +420 | 26692 |
| 58 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +416 | 22489 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +408 | 29140 |
| 60 | [google/skills](https://github.com/google/skills) | +407 | 13671 |
| 61 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +406 | 5047 |
| 62 | [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | +396 | 4578 |
| 63 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +395 | 27696 |
| 64 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +395 | 10024 |
| 65 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +393 | 8935 |
| 66 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +392 | 6972 |
| 67 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +385 | 12152 |
| 68 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +381 | 4445 |
| 69 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +377 | 22027 |
| 70 | [withcoral/coral](https://github.com/withcoral/coral) | +377 | 5135 |
| 71 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +372 | 17188 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +368 | 42524 |
| 73 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +368 | 5223 |
| 74 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +361 | 5451 |
| 75 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +360 | 6922 |
| 76 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +359 | 30481 |
| 77 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +358 | 14413 |
| 78 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8257 |
| 79 | [apple/container](https://github.com/apple/container) | +345 | 36921 |
| 80 | [antirez/ds4](https://github.com/antirez/ds4) | +340 | 13755 |
| 81 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +330 | 29974 |
| 82 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +324 | 38744 |
| 83 | [roboflow/supervision](https://github.com/roboflow/supervision) | +318 | 36553 |
| 84 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +315 | 13655 |
| 85 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +301 | 5151 |
| 86 | [crynta/terax-ai](https://github.com/crynta/terax-ai) | +293 | 7090 |
| 87 | [blader/humanizer](https://github.com/blader/humanizer) | +292 | 24169 |
| 88 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +289 | 16199 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +287 | 33300 |
| 90 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +285 | 43589 |
| 91 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +284 | 24346 |
| 92 | [floci-io/floci](https://github.com/floci-io/floci) | +282 | 14086 |
| 93 | [MinishLab/semble](https://github.com/MinishLab/semble) | +280 | 5150 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +272 | 37499 |
| 95 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +269 | 18670 |
| 96 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +269 | 9176 |
| 97 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +268 | 29871 |
| 98 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +267 | 5634 |
| 99 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +265 | 24291 |
| 100 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +265 | 8242 |
| 101 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +260 | 57697 |
| 102 | [soxoj/maigret](https://github.com/soxoj/maigret) | +254 | 33049 |
| 103 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +253 | 4395 |
| 104 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +252 | 4152 |
| 105 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +248 | 12168 |
| 106 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 2967 |
| 107 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +234 | 4745 |
| 108 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +233 | 21624 |
| 109 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +230 | 3873 |
| 110 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +226 | 4126 |
| 111 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +225 | 37151 |
| 112 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3354 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +216 | 16421 |
| 114 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +215 | 9229 |
| 115 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +209 | 30797 |
| 116 | [88lin/video_vip](https://github.com/88lin/video_vip) | +202 | 3949 |
| 117 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4045 |
| 118 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +201 | 6358 |
| 119 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +200 | 14755 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +196 | 16383 |
| 121 | [openai/skills](https://github.com/openai/skills) | +193 | 22162 |
| 122 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +190 | 6449 |
| 123 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +190 | 4454 |
| 124 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +184 | 7369 |
| 125 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +182 | 5422 |
| 126 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +179 | 3874 |
| 127 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +179 | 19712 |
| 128 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +179 | 46445 |
| 129 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +176 | 11317 |
| 130 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +173 | 18063 |
| 131 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +172 | 3194 |
| 132 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +171 | 6563 |
| 133 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +169 | 40713 |
| 134 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +165 | 36799 |
| 135 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +164 | 16649 |
| 136 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +162 | 34725 |
| 137 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +160 | 24619 |
| 138 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +160 | 12058 |
| 139 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +154 | 8021 |
| 140 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +154 | 24924 |
| 141 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +153 | 23500 |
| 142 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +152 | 34649 |
| 143 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +151 | 2439 |
| 144 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +147 | 3083 |
| 145 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2394 |
| 146 | [jundot/omlx](https://github.com/jundot/omlx) | +145 | 16601 |
| 147 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +143 | 27200 |
| 148 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +140 | 49340 |
| 149 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +137 | 14822 |
| 150 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +137 | 35002 |
| 151 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +134 | 25155 |
| 152 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +129 | 20962 |
| 153 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +126 | 7431 |
| 154 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1987 |
| 155 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2066 |
| 156 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +125 | 3174 |
| 157 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +124 | 4293 |
| 158 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +124 | 6746 |
| 159 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3009 |
| 160 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +120 | 18487 |
| 161 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +120 | 32872 |
| 162 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +119 | 23295 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6694 |
| 164 | [browser-use/video-use](https://github.com/browser-use/video-use) | +116 | 9645 |
| 165 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +116 | 27056 |
| 166 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +113 | 11161 |
| 167 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +113 | 6943 |
| 168 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +112 | 8881 |
| 169 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +109 | 4840 |
| 170 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +109 | 1653 |
| 171 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +108 | 25635 |
| 172 | [openai/plugins](https://github.com/openai/plugins) | +107 | 3024 |
| 173 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +105 | 24612 |
| 174 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +104 | 44197 |
| 175 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +103 | 7425 |
| 176 | [NVlabs/LongLive](https://github.com/NVlabs/LongLive) | +103 | 2334 |
| 177 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +99 | 37564 |
| 178 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +98 | 5690 |
| 179 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +98 | 15773 |
| 180 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +98 | 29370 |
| 181 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +97 | 12101 |
| 182 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +94 | 803 |
| 183 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +94 | 36103 |
| 184 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +91 | 4866 |
| 185 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +90 | 18142 |
| 186 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +89 | 6771 |
| 187 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +88 | 28447 |
| 188 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +85 | 4288 |
| 189 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1160 |
| 190 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +81 | 27919 |
| 191 | [usebruno/bruno](https://github.com/usebruno/bruno) | +81 | 41086 |
| 192 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +80 | 3638 |
| 193 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +77 | 3467 |
| 194 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +75 | 2801 |
| 195 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +74 | 2461 |
| 196 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +73 | 1268 |
| 197 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +72 | 2860 |
| 198 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +67 | 1233 |
| 199 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +65 | 8670 |
| 200 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +61 | 7972 |
| 201 | [eze-is/web-access](https://github.com/eze-is/web-access) | +59 | 7577 |
| 202 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +55 | 5181 |
| 203 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +54 | 3627 |
| 204 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +53 | 5050 |
| 205 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +51 | 5183 |
| 206 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +50 | 1069 |
| 207 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +49 | 5584 |
| 208 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +49 | 11055 |
| 209 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +48 | 1645 |
| 210 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +45 | 2326 |
| 211 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +45 | 495 |
| 212 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +45 | 3797 |
| 213 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +45 | 855 |
| 214 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +44 | 2813 |
| 215 | [sandeco/reversa](https://github.com/sandeco/reversa) | +41 | 1216 |
| 216 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +40 | 2716 |
| 217 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1351 |
| 218 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +36 | 9402 |
| 219 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +35 | 2172 |
| 220 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +35 | 552 |
| 221 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4272 |
| 222 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +34 | 294 |
| 223 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +32 | 360 |
| 224 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +31 | 8224 |
| 225 | [robinebers/openusage](https://github.com/robinebers/openusage) | +31 | 2871 |
| 226 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +31 | 4404 |
| 227 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +30 | 1879 |
| 228 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +29 | 627 |
| 229 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +29 | 10239 |
| 230 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +29 | 12087 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +28 | 13677 |
| 232 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +28 | 578 |
| 233 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +27 | 4419 |
| 234 | [browserbase/skills](https://github.com/browserbase/skills) | +27 | 3557 |
| 235 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 844 |
| 236 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +26 | 286 |
| 237 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +25 | 2145 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +25 | 2535 |
| 239 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 725 |
| 240 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +24 | 1891 |
| 241 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 203 |
| 242 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +23 | 2455 |
| 243 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +23 | 5033 |
| 244 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +22 | 1074 |
| 245 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +22 | 99 |
| 246 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +21 | 2053 |
| 247 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 518 |
| 248 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +20 | 392 |
| 249 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +20 | 1966 |
| 250 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 580 |
| 251 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +20 | 2430 |
| 252 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +19 | 2636 |
| 253 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13588 |
| 254 | [kookoo1sabzy/BaleVPN](https://github.com/kookoo1sabzy/BaleVPN) | +19 | 398 |
| 255 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +19 | 3430 |
| 256 | [openmemind/memind](https://github.com/openmemind/memind) | +19 | 900 |
| 257 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +18 | 1552 |
| 258 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +18 | 310 |
| 259 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +17 | 662 |
| 260 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +17 | 3458 |
| 261 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +17 | 2508 |
| 262 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +17 | 387 |
| 263 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +16 | 318 |
| 264 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +16 | 354 |
| 265 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +16 | 1334 |
| 266 | [is-a-dev/register](https://github.com/is-a-dev/register) | +15 | 10486 |
| 267 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +15 | 703 |
| 268 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +15 | 652 |
| 269 | [Kappaemme-git/codex-startup-pressure-test-skill](https://github.com/Kappaemme-git/codex-startup-pressure-test-skill) | +15 | 950 |
| 270 | [WJZ-P/sona](https://github.com/WJZ-P/sona) | +15 | 651 |
| 271 | [ihmily/doubao-nomark](https://github.com/ihmily/doubao-nomark) | +15 | 610 |
| 272 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +15 | 2452 |
| 273 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +15 | 2996 |
| 274 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +14 | 439 |
| 275 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +14 | 611 |
| 276 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 539 |
| 277 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +14 | 460 |
| 278 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +13 | 1144 |
| 279 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +13 | 359 |
| 280 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +12 | 2562 |
| 281 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 256 |
| 282 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +12 | 8559 |
| 283 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 223 |
| 284 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1617 |
| 285 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 110 |
| 286 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 109 |
| 287 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +9 | 872 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +9 | 1616 |
| 289 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 484 |
| 290 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +8 | 1004 |
| 291 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 235 |
| 292 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +8 | 3256 |
| 293 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +7 | 2098 |
| 294 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +7 | 2286 |
| 295 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +7 | 5177 |
| 296 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 66 |
| 297 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +7 | 130 |
| 298 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +7 | 245 |
| 299 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +7 | 389 |
| 300 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +6 | 737 |
