---
title: "2026-06-16 GitHub增长趋势报告"
description: "1.ponytail+191 2.Agent-Reach+49 3.knowledge-catalog+27 4.omnigent+23 5.taste-skill+22"
date: 2026-06-16T22:13:44+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-16 22:13:44

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
        'daily': {"categories": ["zarazhangrui/frontend-slides", "datawhalechina/hello-agents", "blader/humanizer", "QuantFunc/ComfyUI-QuantFunc", "itsfatduck/optimizerDuck", "hugohe3/ppt-master", "Alishahryar1/free-claude-code", "OpenBMB/VoxCPM", "Yuan1z0825/nature-skills", "Imbad0202/academic-research-skills", "colbymchenry/codegraph", "rohitg00/ai-engineering-from-scratch", "shiyu-coder/Kronos", "chopratejas/headroom", "mvanhorn/last30days-skill", "Leonxlnx/taste-skill", "omnigent-ai/omnigent", "GoogleCloudPlatform/knowledge-catalog", "Panniantong/Agent-Reach", "DietrichGebert/ponytail"], "data": [8, 8, 8, 8, 8, 9, 10, 11, 11, 12, 16, 17, 17, 19, 19, 22, 23, 27, 49, 191]},
        'weekly': {"categories": ["datawhalechina/hello-agents", "heygen-com/hyperframes", "Yuan1z0825/nature-skills", "rtk-ai/rtk", "chatwoot/chatwoot", "Imbad0202/academic-research-skills", "pbakaus/impeccable", "hugohe3/ppt-master", "rohitg00/ai-engineering-from-scratch", "omnigent-ai/omnigent", "GoogleCloudPlatform/knowledge-catalog", "refactoringhq/tolaria", "lfnovo/open-notebook", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "chopratejas/headroom", "apple/container", "DietrichGebert/ponytail"], "data": [63, 67, 67, 72, 73, 83, 84, 85, 88, 93, 100, 104, 106, 170, 199, 254, 255, 317, 348, 547]},
        'monthly': {"categories": ["mvanhorn/last30days-skill", "rohitg00/agentmemory", "anthropics/claude-plugins-official", "msitarzewski/agency-agents", "CloakHQ/CloakBrowser", "safishamsi/graphify", "ruvnet/RuView", "harry0703/MoneyPrinterTurbo", "chopratejas/headroom", "Leonxlnx/taste-skill", "Imbad0202/academic-research-skills", "farion1231/cc-switch", "tinyhumansai/openhuman", "rohitg00/ai-engineering-from-scratch", "NousResearch/hermes-agent", "mattpocock/skills", "pewdiepie-archdaemon/odysseus", "Egonex-AI/Understand-Anything", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph"], "data": [841, 861, 905, 905, 947, 1003, 1018, 1023, 1049, 1263, 1406, 1469, 1571, 1655, 2313, 2414, 2477, 2935, 2968, 3091]}
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
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +191 | 24252 |
| 2 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +49 | 31960 |
| 3 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +27 | 2996 |
| 4 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +23 | 2710 |
| 5 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +22 | 45204 |
| 6 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +19 | 43443 |
| 7 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +19 | 29970 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +17 | 30530 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +17 | 33668 |
| 10 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +16 | 50287 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +12 | 32096 |
| 12 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +11 | 20529 |
| 13 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +11 | 30100 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +10 | 34940 |
| 15 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 28352 |
| 16 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +8 | 4010 |
| 17 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +8 | 910 |
| 18 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 24519 |
| 19 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +8 | 59724 |
| 20 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +8 | 21935 |
| 21 | [yuanzhongqiao/ai-interview-platform](https://github.com/yuanzhongqiao/ai-interview-platform) | +8 | 587 |
| 22 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +7 | 28066 |
| 23 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +7 | 62962 |
| 24 | [alibaba/zvec](https://github.com/alibaba/zvec) | +7 | 10412 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +7 | 38887 |
| 26 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +7 | 4724 |
| 27 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +6 | 4867 |
| 28 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +6 | 1655 |
| 29 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 6529 |
| 30 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 12845 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +547 | 24253 |
| 2 | [apple/container](https://github.com/apple/container) | +348 | 37840 |
| 3 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +317 | 29970 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +255 | 43443 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +254 | 31960 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +199 | 45204 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +170 | 50287 |
| 8 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +106 | 31098 |
| 9 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +104 | 16535 |
| 10 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +100 | 2996 |
| 11 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +93 | 2710 |
| 12 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +88 | 33668 |
| 13 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +85 | 28352 |
| 14 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +84 | 38887 |
| 15 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +83 | 32096 |
| 16 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | +73 | 32033 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +72 | 62962 |
| 18 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +67 | 20529 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +67 | 28103 |
| 20 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +63 | 59724 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +63 | 30100 |
| 22 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +63 | 2740 |
| 23 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +62 | 3565 |
| 24 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +59 | 11767 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +56 | 10553 |
| 26 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +56 | 12845 |
| 27 | [tw93/Kami](https://github.com/tw93/Kami) | +54 | 8775 |
| 28 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +54 | 7386 |
| 29 | [SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI) | +54 | 1334 |
| 30 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +53 | 30530 |
| 31 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +47 | 28066 |
| 32 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +47 | 6318 |
| 33 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +47 | 32872 |
| 34 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +46 | 12358 |
| 35 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +46 | 25174 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +45 | 42783 |
| 37 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +44 | 34940 |
| 38 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +44 | 4337 |
| 39 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +43 | 22815 |
| 40 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +42 | 32432 |
| 41 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +42 | 3652 |
| 42 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +42 | 23030 |
| 43 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | +42 | 9182 |
| 44 | [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing) | +41 | 716 |
| 45 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +41 | 17658 |
| 46 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +41 | 37351 |
| 47 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +40 | 910 |
| 48 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +40 | 6608 |
| 49 | [DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop) | +40 | 482 |
| 50 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +40 | 26345 |
| 51 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +40 | 20921 |
| 52 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +38 | 4867 |
| 53 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +38 | 4010 |
| 54 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +38 | 23132 |
| 55 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 24519 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +34 | 33643 |
| 57 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +34 | 1003 |
| 58 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +34 | 21555 |
| 59 | [extend-hq/ui](https://github.com/extend-hq/ui) | +34 | 1107 |
| 60 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +33 | 18959 |
| 61 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +32 | 24844 |
| 62 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +32 | 12353 |
| 63 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +32 | 30991 |
| 64 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +31 | 21935 |
| 65 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +29 | 15289 |
| 66 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +29 | 24573 |
| 67 | [google/skills](https://github.com/google/skills) | +29 | 13795 |
| 68 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +28 | 3317 |
| 69 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +28 | 4724 |
| 70 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +28 | 1107 |
| 71 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +28 | 3160 |
| 72 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +28 | 15055 |
| 73 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +28 | 57960 |
| 74 | [telemt/telemt](https://github.com/telemt/telemt) | +27 | 5225 |
| 75 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +27 | 2510 |
| 76 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +27 | 9306 |
| 77 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +26 | 2466 |
| 78 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +26 | 12302 |
| 79 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +26 | 8856 |
| 80 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +25 | 15957 |
| 81 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +25 | 31225 |
| 82 | [multica-ai/multica](https://github.com/multica-ai/multica) | +25 | 36898 |
| 83 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +25 | 3133 |
| 84 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +24 | 40900 |
| 85 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +24 | 38487 |
| 86 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +24 | 17586 |
| 87 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +24 | 3763 |
| 88 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +23 | 37685 |
| 89 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +23 | 8041 |
| 90 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +23 | 29004 |
| 91 | [coder/boo](https://github.com/coder/boo) | +23 | 634 |
| 92 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +23 | 0 |
| 93 | [ZenNotes/zennotes](https://github.com/ZenNotes/zennotes) | +23 | 1333 |
| 94 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +23 | 43241 |
| 95 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +22 | 9041 |
| 96 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +22 | 7202 |
| 97 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +22 | 3787 |
| 98 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +20 | 3995 |
| 99 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +20 | 5992 |
| 100 | [ziguishian/xhs-visual-director-skill](https://github.com/ziguishian/xhs-visual-director-skill) | +20 | 469 |
| 101 | [stablyai/orca](https://github.com/stablyai/orca) | +20 | 5024 |
| 102 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +19 | 5651 |
| 103 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +19 | 2797 |
| 104 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +19 | 4853 |
| 105 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +18 | 2203 |
| 106 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +18 | 3020 |
| 107 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +18 | 30260 |
| 108 | [francescopace/espectre](https://github.com/francescopace/espectre) | +18 | 8613 |
| 109 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +17 | 18266 |
| 110 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +17 | 2486 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +16 | 16531 |
| 112 | [LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem) | +16 | 474 |
| 113 | [openai/skills](https://github.com/openai/skills) | +16 | 22329 |
| 114 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +16 | 2836 |
| 115 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +16 | 28403 |
| 116 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +16 | 25717 |
| 117 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +16 | 4538 |
| 118 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +15 | 14563 |
| 119 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +15 | 4228 |
| 120 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 9757 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3091 | 50287 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2968 | 176854 |
| 3 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2935 | 61511 |
| 4 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2477 | 72451 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2414 | 131814 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2313 | 195298 |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1655 | 33668 |
| 8 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1571 | 32432 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1469 | 102611 |
| 10 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1406 | 32096 |
| 11 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1263 | 45204 |
| 12 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1049 | 29970 |
| 13 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1023 | 49621 |
| 14 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1018 | 74204 |
| 15 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1003 | 68173 |
| 16 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +947 | 26345 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +905 | 113847 |
| 18 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +905 | 30260 |
| 19 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +861 | 23132 |
| 20 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +841 | 43443 |
| 21 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +829 | 61170 |
| 22 | [earendil-works/pi](https://github.com/earendil-works/pi) | +704 | 63268 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +677 | 64308 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +659 | 20529 |
| 25 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +654 | 34148 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +635 | 62962 |
| 27 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +580 | 38487 |
| 28 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +579 | 11767 |
| 29 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +578 | 73566 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +556 | 34940 |
| 31 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +554 | 31960 |
| 32 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +550 | 28352 |
| 33 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +549 | 24255 |
| 34 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +533 | 20922 |
| 35 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +522 | 10553 |
| 36 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +521 | 15957 |
| 37 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +511 | 12358 |
| 38 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +501 | 28103 |
| 39 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +501 | 31225 |
| 40 | [multica-ai/multica](https://github.com/multica-ai/multica) | +495 | 36898 |
| 41 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +483 | 12845 |
| 42 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +475 | 43241 |
| 43 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +473 | 59724 |
| 44 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +467 | 38887 |
| 45 | [decolua/9router](https://github.com/decolua/9router) | +455 | 17722 |
| 46 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +455 | 9041 |
| 47 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +431 | 28403 |
| 48 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +421 | 23030 |
| 49 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +420 | 30100 |
| 50 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +416 | 19742 |
| 51 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +409 | 26925 |
| 52 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9165 |
| 53 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +396 | 21301 |
| 54 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +395 | 17003 |
| 55 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +383 | 4478 |
| 56 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +379 | 10238 |
| 57 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +377 | 31098 |
| 58 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +376 | 7386 |
| 59 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +372 | 28066 |
| 60 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +372 | 22214 |
| 61 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +365 | 5240 |
| 62 | [apple/container](https://github.com/apple/container) | +364 | 37840 |
| 63 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +364 | 5651 |
| 64 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +356 | 8333 |
| 65 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +351 | 12302 |
| 66 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +348 | 42783 |
| 67 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +348 | 22815 |
| 68 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8256 |
| 69 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +345 | 14563 |
| 70 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +324 | 17658 |
| 71 | [withcoral/coral](https://github.com/withcoral/coral) | +317 | 5131 |
| 72 | [vercel-labs/zerolang](https://github.com/vercel-labs/zerolang) | +315 | 5089 |
| 73 | [roboflow/supervision](https://github.com/roboflow/supervision) | +302 | 36553 |
| 74 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +297 | 30054 |
| 75 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +297 | 5834 |
| 76 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +291 | 39065 |
| 77 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +289 | 7059 |
| 78 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +284 | 16535 |
| 79 | [google/skills](https://github.com/google/skills) | +282 | 13795 |
| 80 | [MinishLab/semble](https://github.com/MinishLab/semble) | +280 | 5205 |
| 81 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +278 | 13780 |
| 82 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +277 | 43776 |
| 83 | [blader/humanizer](https://github.com/blader/humanizer) | +274 | 24519 |
| 84 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +272 | 9306 |
| 85 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +272 | 6880 |
| 86 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +268 | 5257 |
| 87 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +267 | 5992 |
| 88 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +263 | 4337 |
| 89 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +262 | 8294 |
| 90 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +257 | 18959 |
| 91 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +254 | 37685 |
| 92 | [antirez/ds4](https://github.com/antirez/ds4) | +253 | 14191 |
| 93 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +252 | 33643 |
| 94 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +251 | 30530 |
| 95 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +250 | 57960 |
| 96 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +244 | 24573 |
| 97 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +244 | 28649 |
| 98 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +242 | 12353 |
| 99 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 3018 |
| 100 | [soxoj/maigret](https://github.com/soxoj/maigret) | +237 | 33165 |
| 101 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +235 | 4853 |
| 102 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +232 | 3891 |
| 103 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +227 | 35209 |
| 104 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +226 | 21935 |
| 105 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3406 |
| 106 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +220 | 37351 |
| 107 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +218 | 4423 |
| 108 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 109 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +214 | 30991 |
| 110 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9265 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +213 | 16531 |
| 112 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +205 | 15289 |
| 113 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +205 | 4228 |
| 114 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +204 | 31098 |
| 115 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +204 | 24557 |
| 116 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4059 |
| 117 | [88lin/video_vip](https://github.com/88lin/video_vip) | +200 | 3989 |
| 118 | [floci-io/floci](https://github.com/floci-io/floci) | +199 | 14184 |
| 119 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +195 | 6529 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +192 | 16487 |
| 121 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +188 | 6608 |
| 122 | [openai/skills](https://github.com/openai/skills) | +187 | 22329 |
| 123 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +185 | 2466 |
| 124 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +182 | 5465 |
| 125 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +179 | 4538 |
| 126 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +179 | 4052 |
| 127 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +176 | 7618 |
| 128 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +175 | 11486 |
| 129 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +173 | 40900 |
| 130 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +171 | 18266 |
| 131 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +171 | 6597 |
| 132 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +170 | 24844 |
| 133 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +169 | 19792 |
| 134 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +168 | 25174 |
| 135 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +167 | 3320 |
| 136 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +167 | 46641 |
| 137 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +161 | 36799 |
| 138 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +160 | 34948 |
| 139 | [mattzh72/articraft](https://github.com/mattzh72/articraft) | +158 | 1298 |
| 140 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +157 | 16729 |
| 141 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +156 | 12192 |
| 142 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +153 | 2449 |
| 143 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3410 |
| 144 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +151 | 8113 |
| 145 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +147 | 3197 |
| 146 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +146 | 23562 |
| 147 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2486 |
| 148 | [jundot/omlx](https://github.com/jundot/omlx) | +142 | 16717 |
| 149 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +136 | 49398 |
| 150 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +135 | 27264 |
| 151 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +127 | 14953 |
| 152 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1987 |
| 153 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2078 |
| 154 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +125 | 7565 |
| 155 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +125 | 4363 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +125 | 35135 |
| 157 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +125 | 6843 |
| 158 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3010 |
| 159 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +122 | 25289 |
| 160 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +119 | 32872 |
| 161 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +118 | 23434 |
| 162 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +118 | 3198 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6776 |
| 164 | [browser-use/video-use](https://github.com/browser-use/video-use) | +113 | 9757 |
| 165 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +113 | 18582 |
| 166 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +111 | 7063 |
| 167 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +110 | 9073 |
| 168 | [openai/plugins](https://github.com/openai/plugins) | +110 | 3125 |
| 169 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +110 | 21110 |
| 170 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +110 | 1675 |
| 171 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +107 | 11254 |
| 172 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +107 | 25717 |
| 173 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +105 | 4907 |
| 174 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +103 | 24731 |
| 175 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +103 | 27213 |
| 176 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +99 | 7517 |
| 177 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +98 | 44299 |
| 178 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +98 | 12139 |
| 179 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +96 | 4988 |
| 180 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +92 | 15899 |
| 181 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +92 | 29478 |
| 182 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +91 | 6961 |
| 183 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +89 | 5733 |
| 184 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +87 | 18389 |
| 185 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1163 |
| 186 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +84 | 28568 |
| 187 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +84 | 803 |
| 188 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +84 | 37564 |
| 189 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +81 | 3763 |
| 190 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +81 | 4876 |
| 191 | [usebruno/bruno](https://github.com/usebruno/bruno) | +81 | 41086 |
| 192 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +80 | 36103 |
| 193 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3565 |
| 194 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +78 | 4381 |
| 195 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +74 | 2996 |
| 196 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +74 | 2824 |
| 197 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +73 | 27986 |
| 198 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +70 | 2710 |
| 199 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +67 | 2988 |
| 200 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +67 | 1271 |
| 201 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +65 | 2624 |
| 202 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +64 | 8748 |
| 203 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +64 | 16568 |
| 204 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +55 | 5112 |
| 205 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +52 | 8052 |
| 206 | [eze-is/web-access](https://github.com/eze-is/web-access) | +52 | 7653 |
| 207 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +50 | 1099 |
| 208 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +49 | 1655 |
| 209 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +48 | 11143 |
| 210 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +48 | 5231 |
| 211 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +46 | 3681 |
| 212 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +46 | 5680 |
| 213 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +46 | 1606 |
| 214 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +46 | 5238 |
| 215 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +45 | 500 |
| 216 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +43 | 1250 |
| 217 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +42 | 2344 |
| 218 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +41 | 3872 |
| 219 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +40 | 855 |
| 220 | [sandeco/reversa](https://github.com/sandeco/reversa) | +39 | 1230 |
| 221 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +37 | 2757 |
| 222 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +36 | 1401 |
| 223 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +36 | 2819 |
| 224 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +36 | 576 |
| 225 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +35 | 9410 |
| 226 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4276 |
| 227 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +32 | 715 |
| 228 | [robinebers/openusage](https://github.com/robinebers/openusage) | +31 | 2898 |
| 229 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +31 | 2215 |
| 230 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +27 | 8240 |
| 231 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +27 | 13706 |
| 232 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +27 | 10248 |
| 233 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 884 |
| 234 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +26 | 1901 |
| 235 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +26 | 658 |
| 236 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +25 | 1863 |
| 237 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +25 | 368 |
| 238 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 731 |
| 239 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +24 | 5063 |
| 240 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 204 |
| 241 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +24 | 2555 |
| 242 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +24 | 292 |
| 243 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +23 | 1940 |
| 244 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +23 | 12116 |
| 245 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +23 | 4446 |
| 246 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +23 | 4440 |
| 247 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 130 |
| 248 | [browserbase/skills](https://github.com/browserbase/skills) | +22 | 3561 |
| 249 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +21 | 2475 |
| 250 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +21 | 2167 |
| 251 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 522 |
| 252 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +20 | 422 |
| 253 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +20 | 3444 |
| 254 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +19 | 2082 |
| 255 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +19 | 2003 |
| 256 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +19 | 584 |
| 257 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +18 | 684 |
| 258 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +18 | 2662 |
| 259 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +18 | 13599 |
| 260 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +18 | 312 |
| 261 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +16 | 333 |
| 262 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +16 | 1348 |
| 263 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +16 | 663 |
| 264 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +16 | 2536 |
| 265 | [openmemind/memind](https://github.com/openmemind/memind) | +16 | 901 |
| 266 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +15 | 720 |
| 267 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 357 |
| 268 | [is-a-dev/register](https://github.com/is-a-dev/register) | +15 | 10505 |
| 269 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +15 | 401 |
| 270 | [royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram) | +14 | 382 |
| 271 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +14 | 642 |
| 272 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 549 |
| 273 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +13 | 1158 |
| 274 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +13 | 491 |
| 275 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +12 | 2572 |
| 276 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 254 |
| 277 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +12 | 2471 |
| 278 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 267 |
| 279 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 225 |
| 280 | [buynao/aipath](https://github.com/buynao/aipath) | +11 | 280 |
| 281 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1636 |
| 282 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +11 | 2999 |
| 283 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 112 |
| 284 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +11 | 461 |
| 285 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 109 |
| 286 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +9 | 884 |
| 287 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +9 | 1617 |
| 288 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 489 |
| 289 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +9 | 414 |
| 290 | [emollick/concord](https://github.com/emollick/concord) | +8 | 187 |
| 291 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +8 | 8565 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +8 | 1009 |
| 293 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +8 | 357 |
| 294 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 61 |
| 295 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +7 | 2291 |
| 296 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 66 |
| 297 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +7 | 239 |
| 298 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +7 | 257 |
| 299 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 3490 |
| 300 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 160 |
