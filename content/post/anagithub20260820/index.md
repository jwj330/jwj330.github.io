---
title: "2026-08-20 GitHub增长趋势报告"
description: "1.diagram-design+12 2.OpenLogi+10 3.watermarks-remover+8 4.OpenViking+7 5.orca+7"
date: 2026-08-20T20:29:50+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-20 20:29:50

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
        'daily': {"categories": ["getpaseo/paseo", "chaitanyagiri/munder-difflin", "wang2122/sprix-sage-router", "firecrawl/anydoc", "lidge-jun/opencodex", "WenyuChiou/awesome-agentic-ai-zh", "maka-agent/maka-agent", "virgiliojr94/book-to-skill", "block/buzz", "akitaonrails/ai-memory", "Tiger3807861189/J-Space-Cognition-Suite-V3.6", "calesthio/OpenMontage", "arvin341az-glitch/RVG", "walkinglabs/learn-harness-engineering", "anywhere-labs/deepseek-harness-desktop", "stablyai/orca", "volcengine/OpenViking", "guillaumemeyer/watermarks-remover", "AprilNEA/OpenLogi", "cathrynlavery/diagram-design"], "data": [3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8, 10, 12]},
        'weekly': {"categories": ["internet-court/internet-court-skill", "walkinglabs/learn-harness-engineering", "ifixai-ai/iFixAi", "block/buzz", "AprilNEA/OpenLogi", "arvin341az-glitch/RVG", "mukul975/Anthropic-Cybersecurity-Skills", "virgiliojr94/book-to-skill", "bojieli/ai-agent-book", "xiaobright/dsh-anchored-standard", "PrimeIntellect-ai/prime-agent", "volcengine/OpenViking", "titanwings/colleague-skill", "Tiger3807861189/J-Space-Cognition-Suite-V3.6", "cactus-compute/needle", "holaboss-ai/holaOS", "stablyai/orca", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [12, 12, 12, 12, 12, 12, 13, 14, 14, 15, 15, 15, 16, 16, 17, 18, 23, 42, 57, 59]},
        'monthly': {"categories": ["anywhere-labs/deepseek-harness-desktop", "cloudflare/cloudflare-os", "TencentCloud/TencentDB-Agent-Memory", "k1tbyte/Wand-Enhancer", "ifixai-ai/iFixAi", "brightdata/cli", "guillaumemeyer/watermarks-remover", "emilkowalski/skills", "floci-io/floci", "herdrdev/herdr", "andrewyng/openworker", "ayghri/i-have-adhd", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "cathrynlavery/diagram-design", "bojieli/ai-agent-book", "stablyai/orca", "block/buzz", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [59, 60, 61, 61, 64, 65, 65, 69, 74, 78, 82, 83, 91, 103, 108, 122, 122, 140, 159, 256]}
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
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +12 | 24209 |
| 2 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +10 | 11674 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +8 | 15977 |
| 4 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +7 | 30942 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +7 | 49944 |
| 6 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +7 | 16416 |
| 7 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +6 | 13171 |
| 8 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 3093 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +5 | 49105 |
| 10 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +5 | 2994 |
| 11 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +5 | 3523 |
| 12 | [block/buzz](https://github.com/block/buzz) | +4 | 28883 |
| 13 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 23391 |
| 14 | [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | +4 | 1872 |
| 15 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +4 | 6110 |
| 16 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 11500 |
| 17 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +4 | 17495 |
| 18 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +3 | 678 |
| 19 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +3 | 3082 |
| 20 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +3 | 14446 |
| 21 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +3 | 30319 |
| 22 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +3 | 10704 |
| 23 | [securo-finance/securo](https://github.com/securo-finance/securo) | +3 | 1951 |
| 24 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +3 | 24629 |
| 25 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3 | 47065 |
| 26 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +3 | 10811 |
| 27 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 31136 |
| 28 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +2 | 494 |
| 29 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +2 | 9633 |
| 30 | [onecli/onecli](https://github.com/onecli/onecli) | +2 | 3296 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +59 | 16416 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +57 | 24209 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +42 | 15977 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +23 | 49944 |
| 5 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +18 | 10426 |
| 6 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +17 | 8099 |
| 7 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +16 | 2994 |
| 8 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +16 | 23637 |
| 9 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +15 | 30942 |
| 10 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +15 | 17508 |
| 11 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +15 | 3679 |
| 12 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +14 | 40232 |
| 13 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +14 | 23392 |
| 14 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +13 | 30319 |
| 15 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +12 | 3093 |
| 16 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +12 | 11674 |
| 17 | [block/buzz](https://github.com/block/buzz) | +12 | 28883 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +12 | 11038 |
| 19 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +12 | 13171 |
| 20 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +12 | 4272 |
| 21 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +12 | 14703 |
| 22 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 31136 |
| 23 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +12 | 31006 |
| 24 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +12 | 3975 |
| 25 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +12 | 7021 |
| 26 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +11 | 11500 |
| 27 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 49105 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 48227 |
| 29 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +11 | 3792 |
| 30 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +10 | 26995 |
| 31 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | +10 | 2182 |
| 32 | [yetone/cumora](https://github.com/yetone/cumora) | +9 | 2771 |
| 33 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +9 | 45064 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9 | 36642 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +9 | 47065 |
| 36 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +8 | 24629 |
| 37 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +8 | 3082 |
| 38 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +8 | 17495 |
| 39 | [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) | +8 | 631 |
| 40 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +8 | 23461 |
| 41 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +7 | 3523 |
| 42 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +7 | 33248 |
| 43 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +7 | 4482 |
| 44 | [yc-software/qm](https://github.com/yc-software/qm) | +7 | 14001 |
| 45 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +7 | 2957 |
| 46 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47879 |
| 47 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7765 |
| 48 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +6 | 22609 |
| 49 | [blader/humanizer](https://github.com/blader/humanizer) | +6 | 36835 |
| 50 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 26078 |
| 51 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 12279 |
| 52 | [spinabot/brigade](https://github.com/spinabot/brigade) | +6 | 3009 |
| 53 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +6 | 14467 |
| 54 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 12842 |
| 55 | [macro-inc/macro](https://github.com/macro-inc/macro) | +6 | 3860 |
| 56 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +6 | 16356 |
| 57 | [Leutenegger/book-to-skill](https://github.com/Leutenegger/book-to-skill) | +6 | 1214 |
| 58 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +5 | 19751 |
| 59 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +5 | 6110 |
| 60 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +5 | 12227 |
| 61 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +5 | 39694 |
| 62 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +5 | 1613 |
| 63 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +5 | 24498 |
| 64 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +5 | 1806 |
| 65 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +5 | 13011 |
| 66 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +5 | 4336 |
| 67 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +5 | 12383 |
| 68 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +5 | 14446 |
| 69 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 34000 |
| 70 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +5 | 46292 |
| 71 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 30451 |
| 72 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +5 | 32532 |
| 73 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +5 | 4155 |
| 74 | [xr843/insect-world](https://github.com/xr843/insect-world) | +5 | 515 |
| 75 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 755 |
| 76 | [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | +4 | 1872 |
| 77 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +4 | 678 |
| 78 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10704 |
| 79 | [csyqlz/VOZEB-PRO](https://github.com/csyqlz/VOZEB-PRO) | +4 | 676 |
| 80 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3773 |
| 81 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +4 | 41828 |
| 82 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4 | 47228 |
| 83 | [xuboyuebobb/investorskills](https://github.com/xuboyuebobb/investorskills) | +4 | 1449 |
| 84 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1136 |
| 85 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +4 | 1511 |
| 86 | [momenbasel/PureMac](https://github.com/momenbasel/PureMac) | +4 | 5970 |
| 87 | [floci-io/floci](https://github.com/floci-io/floci) | +4 | 20677 |
| 88 | [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil) | +4 | 5472 |
| 89 | [Kylin010/tcpfit](https://github.com/Kylin010/tcpfit) | +4 | 537 |
| 90 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +4 | 3261 |
| 91 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 4587 |
| 92 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +4 | 1607 |
| 93 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +4 | 6511 |
| 94 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 8479 |
| 95 | [agegr/pi-web](https://github.com/agegr/pi-web) | +3 | 4929 |
| 96 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +3 | 3290 |
| 97 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 5096 |
| 98 | [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | +3 | 2079 |
| 99 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +3 | 20462 |
| 100 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +3 | 20965 |
| 101 | [securo-finance/securo](https://github.com/securo-finance/securo) | +3 | 1951 |
| 102 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 41025 |
| 103 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +3 | 10811 |
| 104 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +3 | 667 |
| 105 | [jundot/omlx](https://github.com/jundot/omlx) | +3 | 20085 |
| 106 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +3 | 31030 |
| 107 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +3 | 8957 |
| 108 | [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | +3 | 3941 |
| 109 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 36242 |
| 110 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 15899 |
| 111 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +3 | 17556 |
| 112 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +3 | 6438 |
| 113 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 24236 |
| 114 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +3 | 6199 |
| 115 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 31350 |
| 116 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +3 | 30621 |
| 117 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 63495 |
| 118 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +2 | 279 |
| 119 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +2 | 494 |
| 120 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +2 | 9633 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +256 | 17508 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +159 | 17495 |
| 3 | [block/buzz](https://github.com/block/buzz) | +140 | 28883 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +122 | 49944 |
| 5 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +122 | 40232 |
| 6 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +108 | 24210 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +103 | 23392 |
| 8 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +91 | 26995 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +83 | 22609 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +82 | 14882 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +78 | 31006 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +74 | 20677 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +69 | 31136 |
| 14 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +65 | 15977 |
| 15 | [brightdata/cli](https://github.com/brightdata/cli) | +65 | 6334 |
| 16 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11038 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +61 | 19132 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +61 | 23461 |
| 19 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8672 |
| 20 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +59 | 16416 |
| 21 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +58 | 11500 |
| 22 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +57 | 16356 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +57 | 48227 |
| 24 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +55 | 24236 |
| 25 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21590 |
| 26 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +51 | 9797 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +50 | 32551 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14001 |
| 29 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +47 | 28932 |
| 30 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 6511 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +46 | 14703 |
| 32 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +45 | 12384 |
| 33 | [google/skills](https://github.com/google/skills) | +44 | 18561 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +43 | 36642 |
| 35 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1451 |
| 36 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +43 | 20965 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 26078 |
| 38 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +42 | 15899 |
| 39 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +41 | 34946 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 63495 |
| 41 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +40 | 49105 |
| 42 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +40 | 25600 |
| 43 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8547 |
| 44 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +39 | 34218 |
| 45 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +38 | 30621 |
| 46 | [blader/humanizer](https://github.com/blader/humanizer) | +37 | 36835 |
| 47 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5646 |
| 48 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +37 | 12227 |
| 49 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8719 |
| 50 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 12842 |
| 51 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +36 | 47352 |
| 52 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +34 | 4155 |
| 53 | [oblien/openship](https://github.com/oblien/openship) | +34 | 11138 |
| 54 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 47065 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 45064 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +33 | 39694 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 10009 |
| 58 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +32 | 41828 |
| 59 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +32 | 6484 |
| 60 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +32 | 31350 |
| 61 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +32 | 18092 |
| 62 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +31 | 19751 |
| 63 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 36242 |
| 64 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +30 | 10305 |
| 65 | [different-ai/openwork](https://github.com/different-ai/openwork) | +27 | 22798 |
| 66 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +26 | 4482 |
| 67 | [spinabot/brigade](https://github.com/spinabot/brigade) | +26 | 3009 |
| 68 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4979 |
| 69 | [get-bb/bb](https://github.com/get-bb/bb) | +26 | 2454 |
| 70 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +26 | 15418 |
| 71 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +26 | 3261 |
| 72 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 21815 |
| 73 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +26 | 9188 |
| 74 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +25 | 2686 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 812 |
| 76 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +25 | 12279 |
| 77 | [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) | +25 | 6221 |
| 78 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +24 | 3975 |
| 79 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24721 |
| 80 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 32532 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4118 |
| 82 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 9027 |
| 83 | [malisper/pgrust](https://github.com/malisper/pgrust) | +23 | 4598 |
| 84 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +22 | 8099 |
| 85 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +22 | 30942 |
| 86 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +22 | 1102 |
| 87 | [xai-org/grok-build](https://github.com/xai-org/grok-build) | +22 | 25780 |
| 88 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +21 | 10426 |
| 89 | [browser-use/video-use](https://github.com/browser-use/video-use) | +21 | 21186 |
| 90 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +21 | 5489 |
| 91 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +20 | 46292 |
| 92 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +19 | 5680 |
| 93 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +19 | 1613 |
| 94 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13715 |
| 95 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +17 | 3792 |
| 96 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +17 | 8479 |
| 97 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 6124 |
| 98 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 14665 |
| 99 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +17 | 8644 |
| 100 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 43161 |
| 101 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +16 | 2994 |
| 102 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +16 | 4336 |
| 103 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +16 | 9415 |
| 104 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +16 | 23637 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47879 |
| 106 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +16 | 10259 |
| 107 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 764 |
| 108 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +15 | 3679 |
| 109 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +15 | 8381 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6883 |
| 111 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5270 |
| 112 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +14 | 30319 |
| 113 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3188 |
| 114 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +14 | 10812 |
| 115 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2408 |
| 116 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +13 | 3093 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3992 |
| 118 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 30451 |
| 119 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +13 | 1948 |
| 120 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 9095 |
| 121 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3113 |
| 122 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31030 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 20692 |
| 124 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 6115 |
| 125 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +13 | 16203 |
| 126 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +13 | 11446 |
| 127 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 128 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2168 |
| 129 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +12 | 0 |
| 130 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 854 |
| 131 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1813 |
| 132 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 6064 |
| 133 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1444 |
| 134 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 34000 |
| 135 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27867 |
| 136 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +12 | 5810 |
| 137 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 32106 |
| 138 | [securo-finance/securo](https://github.com/securo-finance/securo) | +11 | 1951 |
| 139 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2662 |
| 140 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47228 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +11 | 2905 |
| 142 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +11 | 2459 |
| 143 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 389 |
| 144 | [decolua/9router](https://github.com/decolua/9router) | +11 | 25925 |
| 145 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 2106 |
| 146 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6110 |
| 147 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14467 |
| 148 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 2957 |
| 149 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 8772 |
| 150 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2336 |
| 151 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1067 |
| 152 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1933 |
| 153 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +10 | 13992 |
| 154 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 386 |
| 155 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 156 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1712 |
| 157 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 3290 |
| 158 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4587 |
| 159 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10726 |
| 160 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1048 |
| 161 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 383 |
| 162 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1607 |
| 163 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 573 |
| 164 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3853 |
| 165 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1052 |
| 166 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +9 | 10722 |
| 167 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +9 | 1819 |
| 168 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +9 | 28392 |
| 169 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1948 |
| 170 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 5096 |
| 171 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 10704 |
| 172 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1346 |
| 173 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6840 |
| 174 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 8957 |
| 175 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +8 | 6199 |
| 176 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +8 | 1082 |
| 177 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +8 | 15721 |
| 178 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2546 |
| 179 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +8 | 6026 |
| 180 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3683 |
| 181 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8505 |
| 182 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24528 |
| 183 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +7 | 755 |
| 184 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +7 | 9633 |
| 185 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +7 | 14818 |
| 186 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +7 | 11077 |
| 187 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +7 | 17556 |
| 188 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1471 |
| 189 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27519 |
| 190 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 191 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 3439 |
| 192 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1525 |
| 193 | [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | +6 | 2079 |
| 194 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 6750 |
| 195 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 196 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3098 |
| 197 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 277 |
| 198 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 322 |
| 199 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 491 |
| 200 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30271 |
| 201 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5756 |
| 202 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 593 |
| 203 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5854 |
| 204 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 205 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 819 |
| 206 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +5 | 14688 |
| 207 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 699 |
| 208 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +5 | 3773 |
| 209 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3386 |
| 210 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 364 |
| 211 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 623 |
| 212 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +4 | 1203 |
| 213 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +4 | 616 |
| 214 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7258 |
| 215 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 230 |
| 216 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10509 |
| 217 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 494 |
| 218 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4899 |
| 219 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5239 |
| 220 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1188 |
| 221 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8745 |
| 222 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 611 |
| 223 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +4 | 10102 |
| 224 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5133 |
| 225 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9790 |
| 226 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5989 |
| 227 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +4 | 3331 |
| 228 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 429 |
| 229 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1136 |
| 230 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +4 | 4892 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 108 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1049 |
| 233 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4785 |
| 234 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +4 | 27995 |
| 235 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 265 |
| 236 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 197 |
| 237 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +3 | 607 |
| 238 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 572 |
| 239 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 156 |
| 240 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 635 |
| 241 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +3 | 651 |
| 242 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +3 | 1366 |
| 243 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8984 |
| 244 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2912 |
| 245 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9636 |
| 246 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 191 |
| 247 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 389 |
| 248 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1215 |
| 249 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3151 |
| 250 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9621 |
| 251 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +3 | 6468 |
| 252 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 964 |
| 253 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +3 | 537 |
| 254 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +3 | 3476 |
| 255 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +3 | 1355 |
| 256 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 460 |
| 257 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 258 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 944 |
| 259 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 581 |
| 260 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +3 | 295 |
| 261 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 322 |
| 262 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1224 |
| 263 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2081 |
| 264 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28609 |
| 265 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 870 |
| 266 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +3 | 7376 |
| 267 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 737 |
| 268 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 169 |
| 269 | [Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) | +2 | 2817 |
| 270 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 905 |
| 271 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 419 |
| 272 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1381 |
| 273 | [panel-zeus/Z-E-U-S](https://github.com/panel-zeus/Z-E-U-S) | +2 | 662 |
| 274 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12396 |
| 275 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 4046 |
| 276 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1077 |
| 277 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 693 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 101 |
| 279 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 445 |
| 280 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 118 |
| 281 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3690 |
| 282 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 176 |
| 283 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 220 |
| 284 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 358 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2905 |
| 286 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5192 |
| 287 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1224 |
| 288 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1409 |
| 289 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 516 |
| 290 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2567 |
| 291 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 129 |
| 292 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 118 |
| 293 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 902 |
| 294 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1326 |
| 295 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 935 |
| 296 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 94 |
| 297 | [taovietducofficial/OOP-Junior](https://github.com/taovietducofficial/OOP-Junior) | +1 | 37 |
| 298 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +1 | 256 |
| 299 | [linzhi-524/cineisle](https://github.com/linzhi-524/cineisle) | +1 | 35 |
| 300 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +1 | 375 |
