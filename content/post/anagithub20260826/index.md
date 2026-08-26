---
title: "2026-08-26 GitHub增长趋势报告"
description: "1.awesome-gpt-image-2+14 2.gods-eye-view+13 3.FreeToken+11 4.ai-job-search+7 5.archify+6"
date: 2026-08-26T22:50:03+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-26 22:50:03

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
        'daily': {"categories": ["volcengine/OpenViking", "img2threejs/img2threejs", "anthropics/claude-plugins-community", "max-sixty/worktrunk", "ayghri/i-have-adhd", "emdash-cms/emdash", "awesome-dsh-plugin/awesome-dsh-plugin", "am-will/gooey-pi", "asz798838958/freeAgentIdentity", "anthropics/claude-plugins-official", "guillaumemeyer/watermarks-remover", "rohitg00/ai-engineering-from-scratch", "andrewyng/openworker", "cathrynlavery/diagram-design", "Gaoshu705/QzoneArchive", "tt-a1i/archify", "MadsLorentzen/ai-job-search", "FlashML-org/FreeToken", "bilawalsidhu/gods-eye-view", "freestylefly/awesome-gpt-image-2"], "data": [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 6, 7, 11, 13, 14]},
        'weekly': {"categories": ["blader/humanizer", "Alishahryar1/free-claude-code", "pathwaycom/arc-task-gen", "awesome-dsh-plugin/awesome-dsh-plugin", "tt-a1i/archify", "virgiliojr94/book-to-skill", "General-Legal/legal-templates", "MadsLorentzen/ai-job-search", "bilawalsidhu/gods-eye-view", "akitaonrails/ai-memory", "vorssaint/vorssaint-utils", "CopilotKit/OpenBot", "volcengine/OpenViking", "stablyai/orca", "guillaumemeyer/watermarks-remover", "freestylefly/awesome-gpt-image-2", "cathrynlavery/diagram-design", "AprilNEA/OpenLogi", "anywhere-labs/deepseek-harness-desktop", "FlashML-org/FreeToken"], "data": [14, 15, 16, 16, 16, 17, 19, 19, 19, 22, 22, 24, 24, 27, 28, 29, 32, 34, 35, 35]},
        'monthly': {"categories": ["k1tbyte/Wand-Enhancer", "cloudflare/cloudflare-os", "firecrawl/pdf-inspector", "ifixai-ai/iFixAi", "brightdata/cli", "TencentCloud/TencentDB-Agent-Memory", "emilkowalski/skills", "floci-io/floci", "herdrdev/herdr", "ayghri/i-have-adhd", "guillaumemeyer/watermarks-remover", "bojieli/ai-agent-book", "anywhere-labs/deepseek-harness-desktop", "zhaoxuya520/reverse-skill", "block/buzz", "virgiliojr94/book-to-skill", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [59, 60, 62, 63, 66, 66, 73, 73, 74, 77, 85, 87, 87, 102, 104, 113, 118, 128, 163, 259]}
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
| 1 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +14 | 21217 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +13 | 5552 |
| 3 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +11 | 8351 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +7 | 36417 |
| 5 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +6 | 17782 |
| 6 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +4 | 1020 |
| 7 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +3 | 27328 |
| 8 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +3 | 16227 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 49562 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +3 | 18531 |
| 11 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 34344 |
| 12 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +3 | 1439 |
| 13 | [am-will/gooey-pi](https://github.com/am-will/gooey-pi) | +3 | 804 |
| 14 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +3 | 12939 |
| 15 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +2 | 11960 |
| 16 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +2 | 24644 |
| 17 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | +2 | 6663 |
| 18 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +2 | 2168 |
| 19 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +2 | 14014 |
| 20 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +2 | 33559 |
| 21 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +2 | 6771 |
| 22 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +2 | 15144 |
| 23 | [jeffhajewski/latticedb](https://github.com/jeffhajewski/latticedb) | +2 | 486 |
| 24 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +2 | 6617 |
| 25 | [yashmulgaonkar/FlightScnr_Pi](https://github.com/yashmulgaonkar/FlightScnr_Pi) | +2 | 452 |
| 26 | [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | +2 | 4703 |
| 27 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +2 | 16843 |
| 28 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +2 | 1720 |
| 29 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +2 | 767 |
| 30 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +2 | 1269 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +35 | 8351 |
| 2 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +35 | 20709 |
| 3 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +34 | 16843 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +32 | 27328 |
| 5 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +29 | 21217 |
| 6 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +28 | 18531 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 54269 |
| 8 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +24 | 33559 |
| 9 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +24 | 3019 |
| 10 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +22 | 11900 |
| 11 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +22 | 4841 |
| 12 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +19 | 5552 |
| 13 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 36418 |
| 14 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1849 |
| 15 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +17 | 25867 |
| 16 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +16 | 17782 |
| 17 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +16 | 12939 |
| 18 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +16 | 6663 |
| 19 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +15 | 50342 |
| 20 | [blader/humanizer](https://github.com/blader/humanizer) | +14 | 38091 |
| 21 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +14 | 14222 |
| 22 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +13 | 14014 |
| 23 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +13 | 29581 |
| 24 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +12 | 3703 |
| 25 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +12 | 24644 |
| 26 | [cursor/plugins](https://github.com/cursor/plugins) | +12 | 5404 |
| 27 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 51217 |
| 28 | [block/buzz](https://github.com/block/buzz) | +11 | 30893 |
| 29 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +11 | 39524 |
| 30 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +11 | 2551 |
| 31 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +11 | 4822 |
| 32 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +11 | 32788 |
| 33 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +11 | 1875 |
| 34 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +10 | 42507 |
| 35 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +10 | 13762 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +10 | 27684 |
| 37 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +10 | 10923 |
| 38 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +9 | 34225 |
| 39 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +9 | 9308 |
| 40 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +9 | 31252 |
| 41 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1579 |
| 42 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +8 | 18559 |
| 43 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +8 | 767 |
| 44 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +8 | 6120 |
| 45 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 13103 |
| 46 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +8 | 11734 |
| 47 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 49602 |
| 48 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +8 | 894 |
| 49 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +8 | 2286 |
| 50 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +8 | 2221 |
| 51 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +8 | 3018 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +7 | 49562 |
| 53 | [floci-io/floci](https://github.com/floci-io/floci) | +7 | 22383 |
| 54 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +7 | 21227 |
| 55 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +7 | 3261 |
| 56 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +7 | 32623 |
| 57 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +7 | 15144 |
| 58 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +7 | 738 |
| 59 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 37282 |
| 60 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +7 | 1679 |
| 61 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +7 | 4613 |
| 62 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47841 |
| 63 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 20612 |
| 64 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +6 | 38178 |
| 65 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +6 | 1262 |
| 66 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +6 | 1508 |
| 67 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +6 | 48303 |
| 68 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +6 | 2129 |
| 69 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +6 | 7665 |
| 70 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +6 | 6182 |
| 71 | [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | +6 | 3590 |
| 72 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +6 | 7274 |
| 73 | [securo-finance/securo](https://github.com/securo-finance/securo) | +6 | 2304 |
| 74 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +6 | 1008 |
| 75 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +6 | 1414 |
| 76 | [tobi/walgit](https://github.com/tobi/walgit) | +5 | 1978 |
| 77 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +5 | 13389 |
| 78 | [missuo/kumone](https://github.com/missuo/kumone) | +5 | 759 |
| 79 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 16702 |
| 80 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 24667 |
| 81 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +5 | 16227 |
| 82 | [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | +5 | 1423 |
| 83 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +5 | 6376 |
| 84 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5 | 11173 |
| 85 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +5 | 2901 |
| 86 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +5 | 15707 |
| 87 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 37569 |
| 88 | [snflkd/fluent-korean](https://github.com/snflkd/fluent-korean) | +5 | 910 |
| 89 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +5 | 16751 |
| 90 | [jundot/omlx](https://github.com/jundot/omlx) | +5 | 20755 |
| 91 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +5 | 3817 |
| 92 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +5 | 6232 |
| 93 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +5 | 4900 |
| 94 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +5 | 551 |
| 95 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +5 | 999 |
| 96 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +5 | 9521 |
| 97 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 16255 |
| 98 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +5 | 6416 |
| 99 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +4 | 1020 |
| 100 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +4 | 2377 |
| 101 | [ombharatiya/ai-system-design-guide](https://github.com/ombharatiya/ai-system-design-guide) | +4 | 2885 |
| 102 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 6617 |
| 103 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +4 | 1269 |
| 104 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +4 | 2168 |
| 105 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +4 | 6620 |
| 106 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +4 | 5008 |
| 107 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +4 | 759 |
| 108 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +4 | 608 |
| 109 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 489 |
| 110 | [titanwings/distilly](https://github.com/titanwings/distilly) | +4 | 24015 |
| 111 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +3 | 11960 |
| 112 | [cdxiaodong/cain-agent](https://github.com/cdxiaodong/cain-agent) | +3 | 403 |
| 113 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 31784 |
| 114 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 34344 |
| 115 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +3 | 1439 |
| 116 | [powerycy/BossHunter](https://github.com/powerycy/BossHunter) | +3 | 493 |
| 117 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 12451 |
| 118 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | +3 | 3110 |
| 119 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 9043 |
| 120 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +3 | 614 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +259 | 18636 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +163 | 18559 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +128 | 27328 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +118 | 54269 |
| 5 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +113 | 25867 |
| 6 | [block/buzz](https://github.com/block/buzz) | +104 | 30893 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +102 | 29581 |
| 8 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +87 | 20709 |
| 9 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +87 | 42507 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +85 | 18531 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +77 | 24644 |
| 12 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +74 | 32623 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 22383 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +73 | 32788 |
| 15 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +66 | 24667 |
| 16 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6406 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +63 | 11173 |
| 18 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +62 | 16751 |
| 19 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9260 |
| 20 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +59 | 20868 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +59 | 49602 |
| 22 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +58 | 16227 |
| 23 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +58 | 10919 |
| 24 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +56 | 12939 |
| 25 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +56 | 17782 |
| 26 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21700 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +49 | 36420 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14236 |
| 29 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 38091 |
| 30 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +46 | 12220 |
| 31 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 7159 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +44 | 27684 |
| 33 | [google/skills](https://github.com/google/skills) | +44 | 18715 |
| 34 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +43 | 14014 |
| 35 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1417 |
| 36 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +41 | 21217 |
| 37 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +40 | 16843 |
| 38 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +40 | 11900 |
| 39 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +40 | 37569 |
| 40 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +40 | 21466 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 64005 |
| 42 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +39 | 33559 |
| 43 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +39 | 35191 |
| 44 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +39 | 16255 |
| 45 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8632 |
| 46 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8962 |
| 47 | [openai/codex-security](https://github.com/openai/codex-security) | +36 | 10202 |
| 48 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +35 | 8351 |
| 49 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +35 | 20612 |
| 50 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +35 | 51217 |
| 51 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 4440 |
| 52 | [every-app/open-seo](https://github.com/every-app/open-seo) | +34 | 13597 |
| 53 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +34 | 29329 |
| 54 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +33 | 26247 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +32 | 37282 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 45757 |
| 57 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +32 | 6412 |
| 58 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +31 | 6663 |
| 59 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +31 | 13762 |
| 60 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +31 | 15707 |
| 61 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +31 | 24568 |
| 62 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +31 | 34503 |
| 63 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +30 | 50342 |
| 64 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 47841 |
| 65 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +30 | 10554 |
| 66 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +29 | 6182 |
| 67 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +29 | 9308 |
| 68 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +29 | 42738 |
| 69 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 22330 |
| 70 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +28 | 4841 |
| 71 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +28 | 4601 |
| 72 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4867 |
| 73 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +28 | 31784 |
| 74 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +28 | 40767 |
| 75 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2666 |
| 76 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +28 | 6668 |
| 77 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +27 | 49562 |
| 78 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3119 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 30889 |
| 80 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +27 | 3402 |
| 81 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5202 |
| 82 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 23090 |
| 83 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +25 | 39524 |
| 84 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +25 | 10923 |
| 85 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +25 | 13103 |
| 86 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +25 | 18631 |
| 87 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +24 | 3019 |
| 88 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +24 | 14222 |
| 89 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9269 |
| 90 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 25031 |
| 92 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +22 | 33178 |
| 93 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2689 |
| 94 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +21 | 41386 |
| 95 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3703 |
| 96 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +20 | 31252 |
| 97 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 98 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +20 | 6120 |
| 99 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +19 | 5552 |
| 100 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +19 | 3018 |
| 101 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1849 |
| 102 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +18 | 21227 |
| 103 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +18 | 11734 |
| 104 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 24015 |
| 105 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 6617 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 48303 |
| 107 | [browser-use/video-use](https://github.com/browser-use/video-use) | +17 | 21393 |
| 108 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +17 | 4175 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +16 | 7090 |
| 110 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +16 | 9521 |
| 111 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +16 | 15353 |
| 112 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1224 |
| 113 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +16 | 4822 |
| 114 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3775 |
| 115 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 823 |
| 116 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +15 | 8632 |
| 117 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5330 |
| 118 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +14 | 2901 |
| 119 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 905 |
| 120 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3846 |
| 121 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +14 | 7665 |
| 122 | [securo-finance/securo](https://github.com/securo-finance/securo) | +14 | 2304 |
| 123 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30849 |
| 124 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 2041 |
| 125 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9311 |
| 126 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +14 | 3279 |
| 127 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +14 | 13926 |
| 128 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 6376 |
| 129 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2652 |
| 130 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10629 |
| 131 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +13 | 3817 |
| 132 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31439 |
| 133 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +13 | 1861 |
| 134 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +13 | 43837 |
| 135 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +13 | 3093 |
| 136 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +13 | 2551 |
| 137 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9690 |
| 138 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26413 |
| 139 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 28183 |
| 140 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +13 | 32420 |
| 141 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 142 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2229 |
| 143 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3980 |
| 144 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +12 | 13389 |
| 145 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +12 | 9014 |
| 146 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +12 | 9131 |
| 147 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2798 |
| 148 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1445 |
| 149 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +12 | 2953 |
| 150 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +12 | 2145 |
| 151 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +11 | 14737 |
| 152 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1585 |
| 153 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6240 |
| 154 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 6128 |
| 155 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47427 |
| 156 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 519 |
| 157 | [petergyang/human-review](https://github.com/petergyang/human-review) | +11 | 1170 |
| 158 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +10 | 5667 |
| 159 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4716 |
| 160 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3048 |
| 161 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 34705 |
| 162 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +10 | 1070 |
| 163 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2462 |
| 164 | [sowarma/wp2shell-PoC](https://github.com/sowarma/wp2shell-PoC) | +10 | 914 |
| 165 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1579 |
| 166 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +10 | 6334 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +10 | 2012 |
| 168 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1976 |
| 169 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +9 | 0 |
| 170 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 2221 |
| 171 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6416 |
| 172 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45477 |
| 173 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1167 |
| 174 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1209 |
| 175 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 9043 |
| 176 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10866 |
| 177 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1672 |
| 178 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 400 |
| 179 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 579 |
| 180 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8756 |
| 181 | [jundot/omlx](https://github.com/jundot/omlx) | +8 | 20755 |
| 182 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6620 |
| 183 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1883 |
| 184 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9337 |
| 185 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +8 | 894 |
| 186 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3551 |
| 187 | [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit) | +7 | 1108 |
| 188 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1262 |
| 189 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27657 |
| 190 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 191 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 7056 |
| 192 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 193 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1609 |
| 194 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1340 |
| 195 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +6 | 9927 |
| 196 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 10268 |
| 197 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 283 |
| 198 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +6 | 3719 |
| 199 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 356 |
| 200 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 508 |
| 201 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3912 |
| 202 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3146 |
| 203 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1587 |
| 204 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 962 |
| 205 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +5 | 1742 |
| 206 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3329 |
| 207 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 687 |
| 208 | [openai/plugins](https://github.com/openai/plugins) | +5 | 5230 |
| 209 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 210 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 850 |
| 211 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +5 | 1424 |
| 212 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +5 | 341 |
| 213 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3509 |
| 214 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +5 | 26403 |
| 215 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +5 | 28038 |
| 216 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 503 |
| 217 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1429 |
| 218 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 724 |
| 219 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2264 |
| 220 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 632 |
| 221 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5857 |
| 222 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +4 | 177 |
| 223 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 804 |
| 224 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3077 |
| 225 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1267 |
| 226 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +4 | 7059 |
| 227 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 14128 |
| 228 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 257 |
| 229 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10687 |
| 230 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 558 |
| 231 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7335 |
| 232 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5073 |
| 233 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5286 |
| 234 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +4 | 1264 |
| 235 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1179 |
| 236 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 163 |
| 237 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 984 |
| 238 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4893 |
| 239 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 294 |
| 240 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 205 |
| 241 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3609 |
| 242 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6022 |
| 243 | [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | +3 | 997 |
| 244 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +3 | 357 |
| 245 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 889 |
| 246 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1248 |
| 247 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 287 |
| 248 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +3 | 5669 |
| 249 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 440 |
| 250 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6112 |
| 251 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 623 |
| 252 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 650 |
| 253 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1776 |
| 254 | [visualbruno/3DGenStudio](https://github.com/visualbruno/3DGenStudio) | +3 | 550 |
| 255 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 9007 |
| 256 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 904 |
| 257 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 218 |
| 258 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 3121 |
| 259 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +3 | 8894 |
| 260 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +3 | 532 |
| 261 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 194 |
| 262 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +3 | 3600 |
| 263 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 677 |
| 264 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 413 |
| 265 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 251 |
| 266 | [penecho/penecho](https://github.com/penecho/penecho) | +3 | 2137 |
| 267 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4890 |
| 268 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 983 |
| 269 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 241 |
| 270 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 584 |
| 271 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 344 |
| 272 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2143 |
| 273 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28816 |
| 274 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 275 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2585 |
| 276 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 513 |
| 277 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 748 |
| 278 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 141 |
| 279 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 280 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 86 |
| 281 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 543 |
| 282 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 124 |
| 283 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 203 |
| 284 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2550 |
| 285 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3779 |
| 286 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1049 |
| 287 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 625 |
| 288 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 290 |
| 289 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 376 |
| 290 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2922 |
| 291 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 228 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1249 |
| 293 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1415 |
| 294 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 525 |
| 295 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 268 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 914 |
| 297 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1354 |
| 298 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 175 |
| 299 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 970 |
| 300 | [diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness) | +1 | 284 |
