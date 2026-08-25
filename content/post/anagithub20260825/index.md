---
title: "2026-08-25 GitHub增长趋势报告"
description: "1.vorssaint-utils+8 2.awesome-gpt-image-2+7 3.OpenLogi+7 4.orca+6 5.ai-job-search+6"
date: 2026-08-25T20:30:13+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-25 20:30:13

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
        'daily': {"categories": ["weicj/vLLM-2080Ti-Definitive", "HKUDS/CLI-Anything", "NiluK/worldmodels101", "t8y2/dbx", "plannotator/effective-html", "bojieli/ai-agent-book", "CopilotKit/OpenBot", "virgiliojr94/book-to-skill", "emilkowalski/skills", "AgriciDaniel/claude-obsidian", "zhaoxuya520/reverse-skill", "rohitg00/ai-engineering-from-scratch", "akitaonrails/ai-memory", "blader/humanizer", "bilawalsidhu/gods-eye-view", "MadsLorentzen/ai-job-search", "stablyai/orca", "AprilNEA/OpenLogi", "freestylefly/awesome-gpt-image-2", "vorssaint/vorssaint-utils"], "data": [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8]},
        'weekly': {"categories": ["zhaoxuya520/reverse-skill", "blader/humanizer", "freestylefly/awesome-gpt-image-2", "walkinglabs/learn-harness-engineering", "Tiger3807861189/J-Space-Cognition-Suite-V3.7", "pathwaycom/arc-task-gen", "mukul975/Anthropic-Cybersecurity-Skills", "General-Legal/legal-templates", "akitaonrails/ai-memory", "virgiliojr94/book-to-skill", "vorssaint/vorssaint-utils", "CopilotKit/OpenBot", "awesome-dsh-plugin/awesome-dsh-plugin", "FlashML-org/FreeToken", "volcengine/OpenViking", "guillaumemeyer/watermarks-remover", "stablyai/orca", "AprilNEA/OpenLogi", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [15, 15, 15, 16, 17, 17, 18, 19, 21, 22, 22, 23, 25, 28, 29, 30, 32, 34, 38, 43]},
        'monthly': {"categories": ["firecrawl/pdf-inspector", "k1tbyte/Wand-Enhancer", "andrewyng/openworker", "ifixai-ai/iFixAi", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "emilkowalski/skills", "herdrdev/herdr", "ayghri/i-have-adhd", "floci-io/floci", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "bojieli/ai-agent-book", "zhaoxuya520/reverse-skill", "block/buzz", "virgiliojr94/book-to-skill", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [62, 62, 63, 63, 65, 66, 74, 76, 77, 78, 82, 86, 91, 103, 113, 115, 121, 124, 163, 259]}
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
| 1 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +8 | 11399 |
| 2 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +7 | 17471 |
| 3 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +7 | 16372 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +6 | 53548 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +6 | 35155 |
| 6 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +5 | 3563 |
| 7 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 37857 |
| 8 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +4 | 4607 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 48867 |
| 10 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +3 | 29185 |
| 11 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +3 | 12603 |
| 12 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 32460 |
| 13 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 25504 |
| 14 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +3 | 2870 |
| 15 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 42167 |
| 16 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +2 | 2298 |
| 17 | [t8y2/dbx](https://github.com/t8y2/dbx) | +2 | 16577 |
| 18 | [NiluK/worldmodels101](https://github.com/NiluK/worldmodels101) | +2 | 67 |
| 19 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 48208 |
| 20 | [weicj/vLLM-2080Ti-Definitive](https://github.com/weicj/vLLM-2080Ti-Definitive) | +2 | 666 |
| 21 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +2 | 3178 |
| 22 | [floci-io/floci](https://github.com/floci-io/floci) | +2 | 22186 |
| 23 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +2 | 31108 |
| 24 | [mixelpixx/Konnect](https://github.com/mixelpixx/Konnect) | +2 | 331 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +2 | 17135 |
| 26 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2 | 20477 |
| 27 | [nfzerox/VirtualMacOniPad](https://github.com/nfzerox/VirtualMacOniPad) | +2 | 1222 |
| 28 | [snflkd/fluent-korean](https://github.com/snflkd/fluent-korean) | +2 | 843 |
| 29 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2 | 49689 |
| 30 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | +2 | 2544 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +43 | 20175 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +38 | 26773 |
| 3 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +34 | 16372 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +32 | 53548 |
| 5 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +30 | 18246 |
| 6 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +29 | 33254 |
| 7 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +28 | 7368 |
| 8 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +25 | 12639 |
| 9 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +23 | 2870 |
| 10 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +22 | 11399 |
| 11 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +22 | 25504 |
| 12 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +21 | 4607 |
| 13 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1768 |
| 14 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +18 | 31108 |
| 15 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +17 | 6041 |
| 16 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +17 | 3015 |
| 17 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +16 | 14141 |
| 18 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +15 | 17471 |
| 19 | [blader/humanizer](https://github.com/blader/humanizer) | +15 | 37857 |
| 20 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +15 | 29185 |
| 21 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +15 | 49689 |
| 22 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +14 | 3652 |
| 23 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +14 | 42167 |
| 24 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +14 | 10842 |
| 25 | [block/buzz](https://github.com/block/buzz) | +13 | 30668 |
| 26 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +13 | 24225 |
| 27 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +13 | 32460 |
| 28 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +13 | 4396 |
| 29 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +13 | 16184 |
| 30 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +12 | 35155 |
| 31 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +12 | 39359 |
| 32 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +12 | 34032 |
| 33 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +12 | 13471 |
| 34 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +12 | 13727 |
| 35 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 50263 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +12 | 27421 |
| 37 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +11 | 2393 |
| 38 | [cursor/plugins](https://github.com/cursor/plugins) | +11 | 5161 |
| 39 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +11 | 32310 |
| 40 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +11 | 1774 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 49310 |
| 42 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +11 | 2850 |
| 43 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +11 | 20586 |
| 44 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +10 | 6049 |
| 45 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +9 | 20477 |
| 46 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +9 | 18436 |
| 47 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +9 | 11179 |
| 48 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +9 | 9153 |
| 49 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 2090 |
| 50 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +9 | 24821 |
| 51 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1547 |
| 52 | [floci-io/floci](https://github.com/floci-io/floci) | +8 | 22186 |
| 53 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +8 | 5997 |
| 54 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +8 | 11632 |
| 55 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 12969 |
| 56 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 37085 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 45611 |
| 58 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 12105 |
| 59 | [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | +8 | 6811 |
| 60 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +7 | 1506 |
| 61 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +7 | 4578 |
| 62 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +7 | 16684 |
| 63 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +7 | 708 |
| 64 | [jundot/omlx](https://github.com/jundot/omlx) | +7 | 20630 |
| 65 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 7648 |
| 66 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +7 | 4868 |
| 67 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +7 | 7249 |
| 68 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +7 | 497 |
| 69 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +7 | 2224 |
| 70 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +6 | 21111 |
| 71 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +6 | 3178 |
| 72 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +6 | 12603 |
| 73 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47664 |
| 74 | [snflkd/fluent-korean](https://github.com/snflkd/fluent-korean) | +6 | 843 |
| 75 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +6 | 1414 |
| 76 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +6 | 6301 |
| 77 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +6 | 40597 |
| 78 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +6 | 650 |
| 79 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +6 | 1613 |
| 80 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +6 | 986 |
| 81 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +6 | 37481 |
| 82 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 42580 |
| 83 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +6 | 3759 |
| 84 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 9375 |
| 85 | [macro-inc/macro](https://github.com/macro-inc/macro) | +6 | 4039 |
| 86 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +6 | 1915 |
| 87 | [yetone/cumora](https://github.com/yetone/cumora) | +6 | 3113 |
| 88 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +6 | 6391 |
| 89 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +5 | 3564 |
| 90 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +5 | 48867 |
| 91 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 16577 |
| 92 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +5 | 37701 |
| 93 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 24425 |
| 94 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +5 | 6123 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 48208 |
| 96 | [harry0703/MangoDisk](https://github.com/harry0703/MangoDisk) | +5 | 1399 |
| 97 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +5 | 959 |
| 98 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +5 | 5603 |
| 99 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 16198 |
| 100 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +5 | 31362 |
| 101 | [dob323/session-kit](https://github.com/dob323/session-kit) | +5 | 649 |
| 102 | [securo-finance/securo](https://github.com/securo-finance/securo) | +5 | 2260 |
| 103 | [missuo/kumone](https://github.com/missuo/kumone) | +4 | 707 |
| 104 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +4 | 2881 |
| 105 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +4 | 12420 |
| 106 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 437 |
| 107 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +4 | 703 |
| 108 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +4 | 601 |
| 109 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +4 | 6602 |
| 110 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 15096 |
| 111 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 4680 |
| 112 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +4 | 9265 |
| 113 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 486 |
| 114 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +4 | 593 |
| 115 | [titanwings/distilly](https://github.com/titanwings/distilly) | +4 | 23969 |
| 116 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +4 | 828 |
| 117 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10880 |
| 118 | [powerycy/BossHunter](https://github.com/powerycy/BossHunter) | +3 | 478 |
| 119 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 45381 |
| 120 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +3 | 17135 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +259 | 18377 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +163 | 18436 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +124 | 26773 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +121 | 53548 |
| 5 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +115 | 25504 |
| 6 | [block/buzz](https://github.com/block/buzz) | +113 | 30668 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +103 | 29185 |
| 8 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +91 | 42167 |
| 9 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +86 | 20175 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +82 | 18246 |
| 11 | [floci-io/floci](https://github.com/floci-io/floci) | +78 | 22186 |
| 12 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +77 | 24225 |
| 13 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +76 | 32310 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +74 | 32460 |
| 15 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6415 |
| 16 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +65 | 24425 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +63 | 11179 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +63 | 15262 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +62 | 20586 |
| 20 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +62 | 16684 |
| 21 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9186 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +60 | 49310 |
| 23 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +58 | 10788 |
| 24 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21686 |
| 25 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +53 | 12639 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +50 | 16184 |
| 27 | [blader/humanizer](https://github.com/blader/humanizer) | +47 | 37857 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14191 |
| 29 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +47 | 12105 |
| 30 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 7068 |
| 31 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +45 | 35155 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +45 | 27421 |
| 33 | [google/skills](https://github.com/google/skills) | +44 | 18697 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +43 | 37481 |
| 35 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +43 | 13727 |
| 36 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1417 |
| 37 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +41 | 21403 |
| 38 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +41 | 16198 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 63839 |
| 40 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +39 | 11399 |
| 41 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +39 | 35158 |
| 42 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8625 |
| 43 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +38 | 16372 |
| 44 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +38 | 29235 |
| 45 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +37 | 20477 |
| 46 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +37 | 33254 |
| 47 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8919 |
| 48 | [openai/codex-security](https://github.com/openai/codex-security) | +36 | 10163 |
| 49 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +36 | 34457 |
| 50 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +35 | 50263 |
| 51 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 4377 |
| 52 | [every-app/open-seo](https://github.com/every-app/open-seo) | +34 | 13459 |
| 53 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 37085 |
| 54 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +34 | 26163 |
| 55 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +34 | 13471 |
| 56 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 42581 |
| 57 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +33 | 24521 |
| 58 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 45611 |
| 59 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10514 |
| 60 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +32 | 6338 |
| 61 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +31 | 6042 |
| 62 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +30 | 49689 |
| 63 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 47664 |
| 64 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +30 | 40597 |
| 65 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +29 | 6049 |
| 66 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 15622 |
| 67 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +29 | 31697 |
| 68 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 22277 |
| 69 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +29 | 18556 |
| 70 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +29 | 6620 |
| 71 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +28 | 7368 |
| 72 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +28 | 9153 |
| 73 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4780 |
| 74 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2642 |
| 75 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 30828 |
| 76 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +27 | 17471 |
| 77 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +27 | 4607 |
| 78 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +27 | 4533 |
| 79 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3112 |
| 80 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +27 | 3376 |
| 81 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +26 | 39359 |
| 82 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +26 | 12969 |
| 83 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5148 |
| 84 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 23032 |
| 85 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +25 | 10842 |
| 86 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +25 | 48867 |
| 87 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 706 |
| 88 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +24 | 14141 |
| 89 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9217 |
| 90 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 91 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +23 | 2870 |
| 92 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +23 | 5997 |
| 93 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 24959 |
| 94 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +22 | 33104 |
| 95 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2688 |
| 96 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +21 | 31108 |
| 97 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3652 |
| 98 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 99 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +19 | 3015 |
| 100 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1768 |
| 101 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +19 | 4166 |
| 102 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +18 | 11632 |
| 103 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 23969 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +17 | 21111 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 15096 |
| 106 | [browser-use/video-use](https://github.com/browser-use/video-use) | +17 | 21347 |
| 107 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +16 | 6978 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 48208 |
| 109 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +16 | 9375 |
| 110 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +16 | 6546 |
| 111 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1220 |
| 112 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3753 |
| 113 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +16 | 8584 |
| 114 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +15 | 43678 |
| 115 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 816 |
| 116 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +15 | 13890 |
| 117 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5337 |
| 118 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +14 | 2850 |
| 119 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3353 |
| 120 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +14 | 7648 |
| 121 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30800 |
| 122 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 2030 |
| 123 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9274 |
| 124 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +14 | 4397 |
| 125 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 6301 |
| 126 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2569 |
| 127 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +13 | 898 |
| 128 | [securo-finance/securo](https://github.com/securo-finance/securo) | +13 | 2260 |
| 129 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31362 |
| 130 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +13 | 1840 |
| 131 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +13 | 3059 |
| 132 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3250 |
| 133 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +13 | 2393 |
| 134 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9628 |
| 135 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +13 | 32354 |
| 136 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 137 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2227 |
| 138 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +13 | 10552 |
| 139 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3983 |
| 140 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3759 |
| 141 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 12603 |
| 142 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +12 | 8932 |
| 143 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +12 | 8994 |
| 144 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1449 |
| 145 | [decolua/9router](https://github.com/decolua/9router) | +12 | 26313 |
| 146 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +12 | 2881 |
| 147 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28119 |
| 148 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +11 | 14697 |
| 149 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1563 |
| 150 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6216 |
| 151 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 6116 |
| 152 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2773 |
| 153 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47389 |
| 154 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +11 | 2019 |
| 155 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 502 |
| 156 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +10 | 5603 |
| 157 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6391 |
| 158 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4680 |
| 159 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3039 |
| 160 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 34445 |
| 161 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2465 |
| 162 | [sowarma/wp2shell-PoC](https://github.com/sowarma/wp2shell-PoC) | +10 | 914 |
| 163 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1547 |
| 164 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +10 | 2005 |
| 165 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1155 |
| 166 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1970 |
| 167 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +9 | 0 |
| 168 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 2090 |
| 169 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45381 |
| 170 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1143 |
| 171 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1174 |
| 172 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10838 |
| 173 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1660 |
| 174 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 399 |
| 175 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 577 |
| 176 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +9 | 6274 |
| 177 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8708 |
| 178 | [jundot/omlx](https://github.com/jundot/omlx) | +8 | 20630 |
| 179 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1860 |
| 180 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9265 |
| 181 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6602 |
| 182 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24701 |
| 183 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3499 |
| 184 | [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit) | +7 | 1106 |
| 185 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +7 | 497 |
| 186 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27634 |
| 187 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 188 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1538 |
| 189 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 7009 |
| 190 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 191 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1552 |
| 192 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +6 | 9897 |
| 193 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 10237 |
| 194 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 280 |
| 195 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +6 | 3710 |
| 196 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 348 |
| 197 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 505 |
| 198 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +6 | 14102 |
| 199 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3911 |
| 200 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +6 | 28035 |
| 201 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3137 |
| 202 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +5 | 1255 |
| 203 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1581 |
| 204 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 932 |
| 205 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +5 | 1320 |
| 206 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3243 |
| 207 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 668 |
| 208 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 209 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 848 |
| 210 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +5 | 330 |
| 211 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3464 |
| 212 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +5 | 26375 |
| 213 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1418 |
| 214 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 689 |
| 215 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2248 |
| 216 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 632 |
| 217 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5838 |
| 218 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +4 | 174 |
| 219 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 798 |
| 220 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3050 |
| 221 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1705 |
| 222 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1256 |
| 223 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +4 | 7017 |
| 224 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 251 |
| 225 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10656 |
| 226 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 552 |
| 227 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7317 |
| 228 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5033 |
| 229 | [penecho/penecho](https://github.com/penecho/penecho) | +4 | 2132 |
| 230 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5275 |
| 231 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 668 |
| 232 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5215 |
| 233 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1244 |
| 234 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1149 |
| 235 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 155 |
| 236 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 971 |
| 237 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4864 |
| 238 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 290 |
| 239 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 204 |
| 240 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3586 |
| 241 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6024 |
| 242 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +3 | 339 |
| 243 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6063 |
| 244 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 877 |
| 245 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1239 |
| 246 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +3 | 5649 |
| 247 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 275 |
| 248 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 392 |
| 249 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 619 |
| 250 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 650 |
| 251 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1768 |
| 252 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 9000 |
| 253 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 896 |
| 254 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 218 |
| 255 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 3084 |
| 256 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +3 | 8859 |
| 257 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 193 |
| 258 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +3 | 3580 |
| 259 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 409 |
| 260 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 250 |
| 261 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9739 |
| 262 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4878 |
| 263 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 977 |
| 264 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 230 |
| 265 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 583 |
| 266 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 339 |
| 267 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1261 |
| 268 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2132 |
| 269 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28787 |
| 270 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 271 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2583 |
| 272 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 452 |
| 273 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 746 |
| 274 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 140 |
| 275 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +2 | 5718 |
| 276 | [cosmicstack-labs/mercury-agent-skills](https://github.com/cosmicstack-labs/mercury-agent-skills) | +2 | 461 |
| 277 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 278 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 528 |
| 279 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 123 |
| 280 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 202 |
| 281 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3772 |
| 282 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1044 |
| 283 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 613 |
| 284 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 278 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 375 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2918 |
| 287 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 226 |
| 288 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1245 |
| 289 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1412 |
| 290 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 524 |
| 291 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 264 |
| 292 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 141 |
| 293 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 912 |
| 294 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1346 |
| 295 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 172 |
| 296 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 966 |
| 297 | [sbancuz/PlanNH](https://github.com/sbancuz/PlanNH) | +1 | 15 |
| 298 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +1 | 3098 |
| 299 | [TensorHub-ORG/Coomi-Android](https://github.com/TensorHub-ORG/Coomi-Android) | +1 | 102 |
| 300 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 95 |
