---
title: "2026-06-15 GitHub增长趋势报告"
description: "1.ponytail+261 2.headroom+43 3.Agent-Reach+35 4.last30days-skill+29 5.knowledge-catalog+28"
date: 2026-06-15T22:20:55+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-15 22:20:55

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
        'daily': {"categories": ["alibaba/open-code-review", "supertone-inc/supertonic", "datawhalechina/hello-agents", "simonlin1212/a-stock-data", "itsfatduck/optimizerDuck", "rtk-ai/rtk", "tw93/Kami", "AIDC-AI/Pixelle-Video", "pbakaus/impeccable", "voidful/hung-yi-lee-skill", "OpenBMB/VoxCPM", "omnigent-ai/omnigent", "rohitg00/ai-engineering-from-scratch", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "GoogleCloudPlatform/knowledge-catalog", "mvanhorn/last30days-skill", "Panniantong/Agent-Reach", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [12, 12, 12, 14, 14, 14, 14, 14, 15, 15, 16, 16, 17, 23, 24, 28, 29, 35, 43, 261]},
        'weekly': {"categories": ["maziyarpanahi/openmed", "tashfeenahmed/freellmapi", "omnigent-ai/omnigent", "rtk-ai/rtk", "heygen-com/hyperframes", "GoogleCloudPlatform/knowledge-catalog", "rohitg00/ai-engineering-from-scratch", "pbakaus/impeccable", "hugohe3/ppt-master", "Imbad0202/academic-research-skills", "RyanCodrai/turbovec", "lfnovo/open-notebook", "refactoringhq/tolaria", "colbymchenry/codegraph", "Leonxlnx/taste-skill", "Panniantong/Agent-Reach", "mvanhorn/last30days-skill", "apple/container", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [65, 65, 70, 71, 74, 75, 84, 87, 88, 92, 103, 112, 121, 179, 222, 239, 312, 339, 352, 367]},
        'monthly': {"categories": ["addyosmani/agent-skills", "anthropics/claude-plugins-official", "rohitg00/agentmemory", "msitarzewski/agency-agents", "harry0703/MoneyPrinterTurbo", "CloakHQ/CloakBrowser", "safishamsi/graphify", "chopratejas/headroom", "ruvnet/RuView", "Leonxlnx/taste-skill", "Imbad0202/academic-research-skills", "farion1231/cc-switch", "rohitg00/ai-engineering-from-scratch", "tinyhumansai/openhuman", "NousResearch/hermes-agent", "pewdiepie-archdaemon/odysseus", "mattpocock/skills", "Egonex-AI/Understand-Anything", "forrestchang/andrej-karpathy-skills", "colbymchenry/codegraph"], "data": [874, 908, 934, 967, 1020, 1022, 1022, 1034, 1110, 1254, 1443, 1545, 1655, 1729, 2452, 2466, 2574, 2915, 3089, 3124]}
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
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +261 | 15834 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +43 | 28766 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +35 | 30019 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +29 | 42814 |
| 5 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +28 | 2134 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +24 | 44468 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +23 | 49635 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +17 | 33022 |
| 9 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 1840 |
| 10 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +16 | 29715 |
| 11 | [voidful/hung-yi-lee-skill](https://github.com/voidful/hung-yi-lee-skill) | +15 | 515 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +15 | 38634 |
| 13 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +14 | 22722 |
| 14 | [tw93/Kami](https://github.com/tw93/Kami) | +14 | 8669 |
| 15 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +14 | 62586 |
| 16 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +14 | 3656 |
| 17 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +14 | 4589 |
| 18 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +12 | 59435 |
| 19 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +12 | 12311 |
| 20 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +12 | 7256 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +12 | 27840 |
| 22 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +12 | 24770 |
| 23 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +11 | 30243 |
| 24 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +11 | 31726 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +11 | 20204 |
| 26 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +10 | 28947 |
| 27 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +9 | 15099 |
| 28 | [steipete/oracle](https://github.com/steipete/oracle) | +9 | 2509 |
| 29 | [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing) | +9 | 667 |
| 30 | [learningCatHD/telos-sdk](https://github.com/learningCatHD/telos-sdk) | +9 | 437 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +367 | 15835 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +352 | 28766 |
| 3 | [apple/container](https://github.com/apple/container) | +339 | 37427 |
| 4 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +312 | 42814 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +239 | 30019 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +222 | 44468 |
| 7 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +179 | 49635 |
| 8 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +121 | 16386 |
| 9 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +112 | 30869 |
| 10 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +103 | 11638 |
| 11 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +92 | 31726 |
| 12 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +88 | 27840 |
| 13 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +87 | 38634 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +84 | 33022 |
| 15 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +75 | 2135 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +74 | 27893 |
| 17 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +71 | 62586 |
| 18 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +70 | 1841 |
| 19 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +65 | 10446 |
| 20 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +65 | 3522 |
| 21 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +62 | 59435 |
| 22 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +62 | 2670 |
| 23 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +62 | 7256 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +62 | 20204 |
| 25 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +61 | 29715 |
| 26 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | +61 | 31632 |
| 27 | [roboflow/supervision](https://github.com/roboflow/supervision) | +61 | 36553 |
| 28 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +59 | 37248 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +57 | 12628 |
| 30 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +55 | 4251 |
| 31 | [SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI) | +53 | 1281 |
| 32 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +53 | 31098 |
| 33 | [tw93/Kami](https://github.com/tw93/Kami) | +51 | 8669 |
| 34 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +51 | 27874 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +47 | 42643 |
| 36 | [masterking32/MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | +47 | 6298 |
| 37 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +47 | 25107 |
| 38 | [google/skills](https://github.com/google/skills) | +46 | 13715 |
| 39 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +45 | 22722 |
| 40 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +45 | 12311 |
| 41 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +45 | 22880 |
| 42 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +44 | 3510 |
| 43 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +43 | 22949 |
| 44 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +43 | 20778 |
| 45 | [LMCache/LMCache](https://github.com/LMCache/LMCache) | +42 | 9131 |
| 46 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +41 | 6535 |
| 47 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +41 | 32257 |
| 48 | [orange2ai/renwei-writing](https://github.com/orange2ai/renwei-writing) | +40 | 667 |
| 49 | [DanMcInerney/architect-loop](https://github.com/DanMcInerney/architect-loop) | +40 | 443 |
| 50 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +40 | 17420 |
| 51 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +40 | 18814 |
| 52 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +39 | 30243 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +38 | 34694 |
| 54 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +37 | 33443 |
| 55 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +36 | 26212 |
| 56 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +35 | 30886 |
| 57 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +35 | 21447 |
| 58 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +35 | 2976 |
| 59 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +34 | 4688 |
| 60 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +34 | 1003 |
| 61 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +34 | 24770 |
| 62 | [blader/humanizer](https://github.com/blader/humanizer) | +34 | 24331 |
| 63 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +34 | 0 |
| 64 | [andrewyng/aisuite](https://github.com/andrewyng/aisuite) | +34 | 14570 |
| 65 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 12268 |
| 66 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +33 | 3656 |
| 67 | [extend-hq/ui](https://github.com/extend-hq/ui) | +33 | 1090 |
| 68 | [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) | +33 | 8748 |
| 69 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +32 | 810 |
| 70 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +32 | 9253 |
| 71 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +32 | 57817 |
| 72 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +31 | 4805 |
| 73 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +30 | 12265 |
| 74 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +29 | 14967 |
| 75 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +29 | 37588 |
| 76 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +29 | 2977 |
| 77 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +29 | 24451 |
| 78 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +29 | 3698 |
| 79 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +28 | 2421 |
| 80 | [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | +28 | 3140 |
| 81 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +28 | 31156 |
| 82 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +28 | 21785 |
| 83 | [agent0ai/dox](https://github.com/agent0ai/dox) | +28 | 837 |
| 84 | [OpenHub-Store/GitHub-Store](https://github.com/OpenHub-Store/GitHub-Store) | +28 | 15361 |
| 85 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +27 | 8807 |
| 86 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +27 | 15099 |
| 87 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +27 | 38389 |
| 88 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +27 | 2691 |
| 89 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +26 | 1041 |
| 90 | [telemt/telemt](https://github.com/telemt/telemt) | +26 | 5171 |
| 91 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +25 | 3197 |
| 92 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +25 | 15825 |
| 93 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +25 | 40800 |
| 94 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +25 | 5570 |
| 95 | [deeplethe/forkd](https://github.com/deeplethe/forkd) | +25 | 2436 |
| 96 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +25 | 25431 |
| 97 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +25 | 43132 |
| 98 | [multica-ai/multica](https://github.com/multica-ai/multica) | +23 | 36736 |
| 99 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +23 | 4589 |
| 100 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +23 | 7136 |
| 101 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +21 | 28947 |
| 102 | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | +21 | 7974 |
| 103 | [stablyai/orca](https://github.com/stablyai/orca) | +21 | 4912 |
| 104 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +21 | 2787 |
| 105 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +21 | 44228 |
| 106 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +19 | 3241 |
| 107 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +18 | 28281 |
| 108 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +18 | 2445 |
| 109 | [francescopace/espectre](https://github.com/francescopace/espectre) | +18 | 8602 |
| 110 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +17 | 25670 |
| 111 | [huggingface/OpenEnv](https://github.com/huggingface/OpenEnv) | +17 | 2272 |
| 112 | [xiaohuailabs/xiaohu-video-translate](https://github.com/xiaohuailabs/xiaohu-video-translate) | +17 | 514 |
| 113 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +16 | 18176 |
| 114 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +16 | 8974 |
| 115 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +16 | 8067 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +16 | 6884 |
| 117 | [rednote-hilab/dots.tts](https://github.com/rednote-hilab/dots.tts) | +16 | 665 |
| 118 | [browser-act/skills](https://github.com/browser-act/skills) | +16 | 2532 |
| 119 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +16 | 4506 |
| 120 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +15 | 14488 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +3124 | 49635 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3089 | 176120 |
| 3 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2915 | 60442 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2574 | 130016 |
| 5 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2466 | 71732 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2452 | 194399 |
| 7 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +1729 | 32257 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1655 | 33022 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1545 | 101627 |
| 10 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1443 | 31726 |
| 11 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1254 | 44469 |
| 12 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1110 | 74021 |
| 13 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1034 | 28766 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +1022 | 67671 |
| 15 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +1022 | 26212 |
| 16 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1020 | 49621 |
| 17 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +967 | 113478 |
| 18 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +934 | 22949 |
| 19 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +908 | 30194 |
| 20 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +874 | 60265 |
| 21 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +829 | 42814 |
| 22 | [earendil-works/pi](https://github.com/earendil-works/pi) | +743 | 62945 |
| 23 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +732 | 63954 |
| 24 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +686 | 20204 |
| 25 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +684 | 34148 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +674 | 62586 |
| 27 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +644 | 38389 |
| 28 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +608 | 72989 |
| 29 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +601 | 11638 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +594 | 27840 |
| 31 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +593 | 12311 |
| 32 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +567 | 34694 |
| 33 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +554 | 31156 |
| 34 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +551 | 59621 |
| 35 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +533 | 20778 |
| 36 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +522 | 15825 |
| 37 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +520 | 27893 |
| 38 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +519 | 10446 |
| 39 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +512 | 43132 |
| 40 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +510 | 30019 |
| 41 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +508 | 28281 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +503 | 36736 |
| 43 | [decolua/9router](https://github.com/decolua/9router) | +499 | 17615 |
| 44 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +498 | 59435 |
| 45 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +485 | 38634 |
| 46 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +485 | 12628 |
| 47 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +460 | 8807 |
| 48 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +449 | 16957 |
| 49 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +439 | 22880 |
| 50 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +431 | 19589 |
| 51 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +425 | 21211 |
| 52 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +418 | 29715 |
| 53 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +418 | 26847 |
| 54 | [vercel-labs/zero](https://github.com/vercel-labs/zero) | +407 | 5072 |
| 55 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +392 | 9070 |
| 56 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +391 | 10131 |
| 57 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +382 | 4461 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +379 | 27874 |
| 59 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +377 | 22722 |
| 60 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +376 | 22130 |
| 61 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +374 | 30869 |
| 62 | [withcoral/coral](https://github.com/withcoral/coral) | +374 | 5133 |
| 63 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +371 | 7256 |
| 64 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +368 | 5233 |
| 65 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +367 | 15838 |
| 66 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +366 | 12265 |
| 67 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +365 | 5570 |
| 68 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +363 | 5786 |
| 69 | [google/skills](https://github.com/google/skills) | +359 | 13715 |
| 70 | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | +358 | 8310 |
| 71 | [apple/container](https://github.com/apple/container) | +356 | 37427 |
| 72 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +352 | 42643 |
| 73 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +352 | 14488 |
| 74 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +348 | 17420 |
| 75 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8256 |
| 76 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | +345 | 6810 |
| 77 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +334 | 7018 |
| 78 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +321 | 30006 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +302 | 38926 |
| 80 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +299 | 13712 |
| 81 | [roboflow/supervision](https://github.com/roboflow/supervision) | +298 | 36553 |
| 82 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +290 | 16386 |
| 83 | [blader/humanizer](https://github.com/blader/humanizer) | +284 | 24331 |
| 84 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +282 | 43682 |
| 85 | [MinishLab/semble](https://github.com/MinishLab/semble) | +280 | 5171 |
| 86 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +278 | 24446 |
| 87 | [antirez/ds4](https://github.com/antirez/ds4) | +277 | 14008 |
| 88 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +273 | 9253 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +272 | 33443 |
| 90 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +268 | 5222 |
| 91 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +264 | 5784 |
| 92 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +263 | 18814 |
| 93 | [NVlabs/Sana](https://github.com/NVlabs/Sana) | +262 | 8260 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +261 | 37588 |
| 95 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +260 | 4251 |
| 96 | [floci-io/floci](https://github.com/floci-io/floci) | +259 | 14144 |
| 97 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +255 | 24451 |
| 98 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +255 | 57817 |
| 99 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +248 | 12268 |
| 100 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +248 | 30243 |
| 101 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +241 | 2987 |
| 102 | [soxoj/maigret](https://github.com/soxoj/maigret) | +237 | 33120 |
| 103 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +235 | 4805 |
| 104 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +231 | 3882 |
| 105 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +230 | 35155 |
| 106 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +226 | 21786 |
| 107 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +225 | 3380 |
| 108 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +220 | 37248 |
| 109 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +218 | 4406 |
| 110 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +215 | 30886 |
| 111 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4348 |
| 112 | [BigBodyCobain/Shadowbroker](https://github.com/BigBodyCobain/Shadowbroker) | +214 | 9250 |
| 113 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +213 | 16475 |
| 114 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +212 | 31098 |
| 115 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +205 | 15099 |
| 116 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +205 | 4164 |
| 117 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +201 | 4055 |
| 118 | [88lin/video_vip](https://github.com/88lin/video_vip) | +201 | 3952 |
| 119 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +194 | 6442 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +192 | 16451 |
| 121 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +188 | 6535 |
| 122 | [openai/skills](https://github.com/openai/skills) | +187 | 22236 |
| 123 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +185 | 2421 |
| 124 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +182 | 5447 |
| 125 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +180 | 7535 |
| 126 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +179 | 4506 |
| 127 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +179 | 3975 |
| 128 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +175 | 11393 |
| 129 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +173 | 40800 |
| 130 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +171 | 18176 |
| 131 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +170 | 24770 |
| 132 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +170 | 6573 |
| 133 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +169 | 19764 |
| 134 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +169 | 25107 |
| 135 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +167 | 3241 |
| 136 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +167 | 46555 |
| 137 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +161 | 36799 |
| 138 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +160 | 34846 |
| 139 | [mattzh72/articraft](https://github.com/mattzh72/articraft) | +158 | 1290 |
| 140 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +157 | 16697 |
| 141 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +156 | 12144 |
| 142 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +152 | 2443 |
| 143 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +151 | 8067 |
| 144 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +147 | 3142 |
| 145 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +146 | 23533 |
| 146 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +145 | 2445 |
| 147 | [jundot/omlx](https://github.com/jundot/omlx) | +142 | 16656 |
| 148 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +136 | 49371 |
| 149 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | +135 | 27241 |
| 150 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +129 | 25230 |
| 151 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +127 | 14893 |
| 152 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1987 |
| 153 | [antoinezambelli/forge](https://github.com/antoinezambelli/forge) | +126 | 2068 |
| 154 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +125 | 7485 |
| 155 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +125 | 4337 |
| 156 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +125 | 35074 |
| 157 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +125 | 6789 |
| 158 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +123 | 3010 |
| 159 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +123 | 32872 |
| 160 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +118 | 23379 |
| 161 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +118 | 3182 |
| 162 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +117 | 6734 |
| 163 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +117 | 21038 |
| 164 | [browser-use/video-use](https://github.com/browser-use/video-use) | +113 | 9708 |
| 165 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +113 | 18531 |
| 166 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +112 | 11203 |
| 167 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +112 | 27144 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +111 | 7015 |
| 169 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +110 | 8974 |
| 170 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +110 | 1662 |
| 171 | [openai/plugins](https://github.com/openai/plugins) | +109 | 3082 |
| 172 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +108 | 4958 |
| 173 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +107 | 25670 |
| 174 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +107 | 4876 |
| 175 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +103 | 24671 |
| 176 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +99 | 7483 |
| 177 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +98 | 44228 |
| 178 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +98 | 12130 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +96 | 29430 |
| 180 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +95 | 5706 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +94 | 15837 |
| 182 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +93 | 18325 |
| 183 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +91 | 6884 |
| 184 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +90 | 4874 |
| 185 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +90 | 37564 |
| 186 | [boona13/mykonos-island-voxels](https://github.com/boona13/mykonos-island-voxels) | +88 | 803 |
| 187 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1162 |
| 188 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +84 | 28518 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +83 | 4334 |
| 190 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +81 | 3698 |
| 191 | [usebruno/bruno](https://github.com/usebruno/bruno) | +81 | 41086 |
| 192 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +79 | 3522 |
| 193 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +79 | 36103 |
| 194 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +75 | 27947 |
| 195 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +74 | 2135 |
| 196 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +74 | 2815 |
| 197 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +72 | 2932 |
| 198 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +70 | 1841 |
| 199 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +70 | 1269 |
| 200 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +69 | 2549 |
| 201 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +65 | 16514 |
| 202 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +64 | 8695 |
| 203 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +57 | 8010 |
| 204 | [eze-is/web-access](https://github.com/eze-is/web-access) | +57 | 7619 |
| 205 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +54 | 5082 |
| 206 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +52 | 3649 |
| 207 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +51 | 5209 |
| 208 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +51 | 1241 |
| 209 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +50 | 1090 |
| 210 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +50 | 5211 |
| 211 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +48 | 1650 |
| 212 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +48 | 1571 |
| 213 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +48 | 11093 |
| 214 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +47 | 5637 |
| 215 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +45 | 497 |
| 216 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +44 | 855 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +43 | 3839 |
| 218 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +42 | 2336 |
| 219 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +40 | 2816 |
| 220 | [sandeco/reversa](https://github.com/sandeco/reversa) | +40 | 1220 |
| 221 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +39 | 2735 |
| 222 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +35 | 1357 |
| 223 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +35 | 9404 |
| 224 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +35 | 568 |
| 225 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4275 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +32 | 2196 |
| 227 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +32 | 366 |
| 228 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +30 | 682 |
| 229 | [robinebers/openusage](https://github.com/robinebers/openusage) | +30 | 2885 |
| 230 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +30 | 293 |
| 231 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +28 | 8233 |
| 232 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +28 | 4424 |
| 233 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +27 | 1888 |
| 234 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +27 | 13698 |
| 235 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +27 | 10246 |
| 236 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +27 | 599 |
| 237 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +26 | 864 |
| 238 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +26 | 12101 |
| 239 | [havingautism/Codemini-CLI](https://github.com/havingautism/Codemini-CLI) | +26 | 286 |
| 240 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +26 | 2542 |
| 241 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +24 | 726 |
| 242 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +24 | 5053 |
| 243 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +24 | 4434 |
| 244 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 203 |
| 245 | [browserbase/skills](https://github.com/browserbase/skills) | +24 | 3562 |
| 246 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +23 | 1918 |
| 247 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 136 |
| 248 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +21 | 2065 |
| 249 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +21 | 2446 |
| 250 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +21 | 2157 |
| 251 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 520 |
| 252 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +20 | 408 |
| 253 | [Juwan-Hwang/Zephyr](https://github.com/Juwan-Hwang/Zephyr) | +20 | 583 |
| 254 | [Zen4-bit/Proxima](https://github.com/Zen4-bit/Proxima) | +20 | 1077 |
| 255 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +20 | 3435 |
| 256 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +19 | 1988 |
| 257 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +19 | 13593 |
| 258 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +18 | 2651 |
| 259 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +18 | 2525 |
| 260 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +18 | 311 |
| 261 | [mimusic-org/mimusic](https://github.com/mimusic-org/mimusic) | +17 | 673 |
| 262 | [openmemind/memind](https://github.com/openmemind/memind) | +17 | 900 |
| 263 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +16 | 325 |
| 264 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +16 | 1344 |
| 265 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +16 | 659 |
| 266 | [huangserva/3DCellForge](https://github.com/huangserva/3DCellForge) | +16 | 2458 |
| 267 | [is-a-dev/register](https://github.com/is-a-dev/register) | +15 | 10498 |
| 268 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +15 | 473 |
| 269 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +15 | 713 |
| 270 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 356 |
| 271 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +14 | 632 |
| 272 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 541 |
| 273 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +14 | 2997 |
| 274 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +14 | 404 |
| 275 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +13 | 1150 |
| 276 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +13 | 2462 |
| 277 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +13 | 460 |
| 278 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +12 | 2564 |
| 279 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 3472 |
| 280 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +12 | 263 |
| 281 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +12 | 224 |
| 282 | [OpenYSM/OpenYSM](https://github.com/OpenYSM/OpenYSM) | +12 | 359 |
| 283 | [royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram) | +11 | 350 |
| 284 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +11 | 1626 |
| 285 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 111 |
| 286 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +10 | 109 |
| 287 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +9 | 879 |
| 288 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +9 | 1616 |
| 289 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +9 | 488 |
| 290 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +9 | 8560 |
| 291 | [emollick/concord](https://github.com/emollick/concord) | +8 | 185 |
| 292 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 238 |
| 293 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +8 | 1004 |
| 294 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +7 | 89 |
| 295 | [1Panel-dev/CordysCRM](https://github.com/1Panel-dev/CordysCRM) | +7 | 2287 |
| 296 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +7 | 5177 |
| 297 | [CosmonauticsTeam/Create-Cosmonautics](https://github.com/CosmonauticsTeam/Create-Cosmonautics) | +7 | 66 |
| 298 | [HappyNewYear1995/UBA-X](https://github.com/HappyNewYear1995/UBA-X) | +7 | 133 |
| 299 | [noellegazelle6/kail_location](https://github.com/noellegazelle6/kail_location) | +7 | 251 |
| 300 | [LSPosed/DirtySepolicy](https://github.com/LSPosed/DirtySepolicy) | +7 | 390 |
