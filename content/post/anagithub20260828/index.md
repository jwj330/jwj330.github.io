---
title: "2026-08-28 GitHub增长趋势报告"
description: "1.archify+29 2.awesome-gpt-image-2+15 3.gods-eye-view+11 4.openhuman+6 5.OpenMontage+6"
date: 2026-08-28T04:05:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-28 04:05:48

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
        'daily': {"categories": ["awesome-dsh-plugin/awesome-dsh-plugin", "tashfeenahmed/freellmapi", "emilkowalski/skills", "multica-ai/multica", "openJiuwen-ai/jiuwenswarm", "LilMGenius/paperthin", "MadsLorentzen/ai-job-search", "floci-io/floci", "anywhere-labs/deepseek-harness-desktop", "VoltAgent/awesome-agent-skills", "rocketride-org/rocketride-server", "stablyai/orca", "rohitg00/ai-engineering-from-scratch", "AgriciDaniel/claude-obsidian", "tobi/walgit", "calesthio/OpenMontage", "tinyhumansai/openhuman", "bilawalsidhu/gods-eye-view", "freestylefly/awesome-gpt-image-2", "tt-a1i/archify"], "data": [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 11, 15, 29]},
        'weekly': {"categories": ["calesthio/OpenMontage", "ayghri/i-have-adhd", "awesome-dsh-plugin/awesome-dsh-plugin", "virgiliojr94/book-to-skill", "blader/humanizer", "pathwaycom/arc-task-gen", "akitaonrails/ai-memory", "CopilotKit/OpenBot", "volcengine/OpenViking", "cathrynlavery/diagram-design", "guillaumemeyer/watermarks-remover", "MadsLorentzen/ai-job-search", "vorssaintapp/vorssaint-utils", "AprilNEA/OpenLogi", "stablyai/orca", "bilawalsidhu/gods-eye-view", "anywhere-labs/deepseek-harness-desktop", "FlashML-org/FreeToken", "tt-a1i/archify", "freestylefly/awesome-gpt-image-2"], "data": [13, 14, 14, 15, 16, 17, 19, 20, 20, 22, 23, 23, 24, 25, 26, 30, 31, 36, 44, 44]},
        'monthly': {"categories": ["k1tbyte/Wand-Enhancer", "firecrawl/pdf-inspector", "ifixai-ai/iFixAi", "brightdata/cli", "TencentCloud/TencentDB-Agent-Memory", "herdrdev/herdr", "ayghri/i-have-adhd", "emilkowalski/skills", "floci-io/floci", "tt-a1i/archify", "bojieli/ai-agent-book", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "block/buzz", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [60, 62, 64, 66, 67, 73, 74, 77, 77, 85, 86, 87, 91, 101, 102, 114, 119, 130, 163, 261]}
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
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +29 | 24034 |
| 2 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +15 | 23323 |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +11 | 8588 |
| 4 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +6 | 38575 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +6 | 52541 |
| 6 | [tobi/walgit](https://github.com/tobi/walgit) | +6 | 2252 |
| 7 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +6 | 14094 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +6 | 50256 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +5 | 55441 |
| 10 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +4 | 7335 |
| 11 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +4 | 32938 |
| 12 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +4 | 21256 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +4 | 22512 |
| 14 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 37309 |
| 15 | [LilMGenius/paperthin](https://github.com/LilMGenius/paperthin) | +4 | 865 |
| 16 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +4 | 4628 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +4 | 48039 |
| 18 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +4 | 33096 |
| 19 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4 | 21135 |
| 20 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +3 | 13250 |
| 21 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 37521 |
| 22 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +3 | 11383 |
| 23 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 33949 |
| 24 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3 | 15585 |
| 25 | [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | +3 | 934 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 49887 |
| 27 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +3 | 1416 |
| 28 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 13264 |
| 29 | [KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess) | +3 | 996 |
| 30 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +3 | 26319 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +44 | 23323 |
| 2 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +44 | 24034 |
| 3 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +36 | 9019 |
| 4 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +31 | 21256 |
| 5 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +30 | 8589 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +26 | 55441 |
| 7 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +25 | 17187 |
| 8 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +24 | 12491 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +23 | 37309 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +23 | 18846 |
| 11 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +22 | 28049 |
| 12 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +20 | 33949 |
| 13 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +20 | 3206 |
| 14 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +19 | 5018 |
| 15 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +17 | 7769 |
| 16 | [blader/humanizer](https://github.com/blader/humanizer) | +16 | 38385 |
| 17 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +15 | 26321 |
| 18 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +14 | 13250 |
| 19 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 25062 |
| 20 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +13 | 52541 |
| 21 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +13 | 1864 |
| 22 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 50256 |
| 23 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +12 | 2661 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 33096 |
| 25 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +12 | 14228 |
| 26 | [cursor/plugins](https://github.com/cursor/plugins) | +12 | 5745 |
| 27 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +12 | 29914 |
| 28 | [tobi/walgit](https://github.com/tobi/walgit) | +11 | 2252 |
| 29 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +11 | 14094 |
| 30 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +11 | 38575 |
| 31 | [floci-io/floci](https://github.com/floci-io/floci) | +11 | 22512 |
| 32 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +11 | 39678 |
| 33 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +11 | 42851 |
| 34 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +10 | 49887 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +10 | 27968 |
| 36 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +10 | 1943 |
| 37 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +9 | 5077 |
| 38 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +9 | 34385 |
| 39 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +9 | 21545 |
| 40 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 13264 |
| 41 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 37521 |
| 42 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +9 | 6209 |
| 43 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +9 | 14411 |
| 44 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +9 | 14028 |
| 45 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1586 |
| 46 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +8 | 32938 |
| 47 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +8 | 21135 |
| 48 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +8 | 2190 |
| 49 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +8 | 791 |
| 50 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +7 | 1416 |
| 51 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 48039 |
| 52 | [block/buzz](https://github.com/block/buzz) | +7 | 31164 |
| 53 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +7 | 1500 |
| 54 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +7 | 3404 |
| 55 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +7 | 2975 |
| 56 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +7 | 32995 |
| 57 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +7 | 6308 |
| 58 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +7 | 9466 |
| 59 | [nuyoah-ai-works/nuyoah-xiezhen-prompt](https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt) | +7 | 627 |
| 60 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +7 | 10963 |
| 61 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +6 | 3746 |
| 62 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +6 | 2572 |
| 63 | [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | +6 | 934 |
| 64 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +6 | 7335 |
| 65 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +6 | 4631 |
| 66 | [missuo/kumone](https://github.com/missuo/kumone) | +6 | 808 |
| 67 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 26319 |
| 68 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 15585 |
| 69 | [harry0703/MangoDisk](https://github.com/harry0703/MangoDisk) | +6 | 1557 |
| 70 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +6 | 24908 |
| 71 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +6 | 41453 |
| 72 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +6 | 6404 |
| 73 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +6 | 1265 |
| 74 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 42899 |
| 75 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 11262 |
| 76 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +6 | 37737 |
| 77 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 20785 |
| 78 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +6 | 1028 |
| 79 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +6 | 31413 |
| 80 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 9660 |
| 81 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +5 | 16601 |
| 82 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +5 | 2221 |
| 83 | [yetone/cumora](https://github.com/yetone/cumora) | +5 | 3182 |
| 84 | [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | +5 | 4844 |
| 85 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +5 | 34736 |
| 86 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +5 | 2441 |
| 87 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +5 | 2313 |
| 88 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +5 | 11870 |
| 89 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +5 | 888 |
| 90 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 45900 |
| 91 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +5 | 5734 |
| 92 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 17086 |
| 93 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +5 | 18844 |
| 94 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 48400 |
| 95 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 16345 |
| 96 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +5 | 3879 |
| 97 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +5 | 610 |
| 98 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +5 | 2405 |
| 99 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +5 | 1414 |
| 100 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +4 | 2524 |
| 101 | [LilMGenius/paperthin](https://github.com/LilMGenius/paperthin) | +4 | 865 |
| 102 | [KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess) | +4 | 996 |
| 103 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 31911 |
| 104 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +4 | 18806 |
| 105 | [am-will/gooey-pi](https://github.com/am-will/gooey-pi) | +4 | 812 |
| 106 | [NoizAI/HelixWorld](https://github.com/NoizAI/HelixWorld) | +4 | 294 |
| 107 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +4 | 12493 |
| 108 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +4 | 17195 |
| 109 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 6677 |
| 110 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +4 | 45556 |
| 111 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +4 | 4230 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +4 | 20843 |
| 113 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +4 | 5049 |
| 114 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +4 | 3017 |
| 115 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 497 |
| 116 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 64148 |
| 117 | [zeenie-ai/OpenCompany](https://github.com/zeenie-ai/OpenCompany) | +3 | 750 |
| 118 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +3 | 1959 |
| 119 | [asz798838958/aBaiFreeGPT](https://github.com/asz798838958/aBaiFreeGPT) | +3 | 1444 |
| 120 | [lxf746/outlook-auto-register](https://github.com/lxf746/outlook-auto-register) | +3 | 375 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +261 | 18844 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +163 | 18806 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +130 | 28049 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +119 | 55441 |
| 5 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +114 | 26321 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +102 | 29914 |
| 7 | [block/buzz](https://github.com/block/buzz) | +101 | 31164 |
| 8 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +91 | 21256 |
| 9 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +87 | 18846 |
| 10 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +86 | 42851 |
| 11 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +85 | 24034 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +77 | 22512 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +77 | 33096 |
| 14 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +74 | 25062 |
| 15 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +73 | 32995 |
| 16 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +67 | 24908 |
| 17 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6398 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11262 |
| 19 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +62 | 16806 |
| 20 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +60 | 21240 |
| 21 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9311 |
| 22 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +60 | 11068 |
| 23 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +59 | 13250 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +59 | 49887 |
| 25 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +56 | 23323 |
| 26 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21724 |
| 27 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +55 | 16602 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +52 | 37309 |
| 29 | [yc-software/qm](https://github.com/yc-software/qm) | +48 | 14274 |
| 30 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 38385 |
| 31 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 7276 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +45 | 27968 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +44 | 12359 |
| 34 | [google/skills](https://github.com/google/skills) | +44 | 18839 |
| 35 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1402 |
| 36 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +42 | 12491 |
| 37 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +42 | 33949 |
| 38 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +40 | 17187 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 64148 |
| 40 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +40 | 52541 |
| 41 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +40 | 37737 |
| 42 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +40 | 8648 |
| 43 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +39 | 35231 |
| 44 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +39 | 16345 |
| 45 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +37 | 21539 |
| 46 | [openai/codex-security](https://github.com/openai/codex-security) | +37 | 10230 |
| 47 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +36 | 9019 |
| 48 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +36 | 4493 |
| 49 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 9018 |
| 50 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +35 | 20785 |
| 51 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 14228 |
| 52 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +35 | 37521 |
| 53 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +35 | 26319 |
| 54 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +34 | 7769 |
| 55 | [multica-ai/multica](https://github.com/multica-ai/multica) | +34 | 48039 |
| 56 | [every-app/open-seo](https://github.com/every-app/open-seo) | +34 | 13798 |
| 57 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +34 | 29411 |
| 58 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +33 | 50256 |
| 59 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 45900 |
| 60 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +31 | 6308 |
| 61 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +31 | 15770 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 10579 |
| 63 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +31 | 22371 |
| 64 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +31 | 6527 |
| 65 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +31 | 24659 |
| 66 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +30 | 8589 |
| 67 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +30 | 5018 |
| 68 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +29 | 9466 |
| 69 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +29 | 42899 |
| 70 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +28 | 4729 |
| 71 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4966 |
| 72 | [spinabot/brigade](https://github.com/spinabot/brigade) | +28 | 3148 |
| 73 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +28 | 31911 |
| 74 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2717 |
| 75 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +28 | 6708 |
| 76 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +27 | 13264 |
| 77 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 30936 |
| 78 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +27 | 3413 |
| 79 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +26 | 10963 |
| 80 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +26 | 40914 |
| 81 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5237 |
| 82 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 23124 |
| 83 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +26 | 34577 |
| 84 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +25 | 39678 |
| 85 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +25 | 14411 |
| 86 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +25 | 14028 |
| 87 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +25 | 18713 |
| 88 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +24 | 3206 |
| 89 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9305 |
| 90 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 25106 |
| 92 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +22 | 41453 |
| 93 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +22 | 33262 |
| 94 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2689 |
| 95 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +21 | 6209 |
| 96 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3746 |
| 97 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +20 | 7335 |
| 98 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +20 | 21545 |
| 99 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +20 | 3017 |
| 100 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +20 | 31413 |
| 101 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 102 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1864 |
| 103 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +18 | 34385 |
| 104 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +18 | 14094 |
| 105 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +18 | 11870 |
| 106 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +18 | 4638 |
| 107 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 24057 |
| 108 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 15585 |
| 109 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 6677 |
| 110 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +17 | 5077 |
| 111 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +17 | 9660 |
| 112 | [browser-use/video-use](https://github.com/browser-use/video-use) | +17 | 21476 |
| 113 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +16 | 35426 |
| 114 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 48400 |
| 115 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 43985 |
| 116 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1225 |
| 117 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3779 |
| 118 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +15 | 5565 |
| 119 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +15 | 2975 |
| 120 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 844 |
| 121 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 909 |
| 122 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30894 |
| 123 | [securo-finance/securo](https://github.com/securo-finance/securo) | +14 | 2432 |
| 124 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 2058 |
| 125 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +14 | 3211 |
| 126 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +14 | 3324 |
| 127 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +14 | 13969 |
| 128 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +14 | 4185 |
| 129 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +14 | 2662 |
| 130 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 6573 |
| 131 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +14 | 2313 |
| 132 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2712 |
| 133 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10699 |
| 134 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +13 | 9173 |
| 135 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31536 |
| 136 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +13 | 1923 |
| 137 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 9383 |
| 138 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9728 |
| 139 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26511 |
| 140 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +13 | 2966 |
| 141 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 28265 |
| 142 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 143 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2235 |
| 144 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3981 |
| 145 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3879 |
| 146 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +12 | 5734 |
| 147 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1445 |
| 148 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +12 | 539 |
| 149 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +12 | 8724 |
| 150 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +11 | 9090 |
| 151 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +11 | 14774 |
| 152 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1603 |
| 153 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2820 |
| 154 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6247 |
| 155 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 6137 |
| 156 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 6385 |
| 157 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +11 | 32473 |
| 158 | [petergyang/human-review](https://github.com/petergyang/human-review) | +11 | 1176 |
| 159 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4756 |
| 160 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3069 |
| 161 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +10 | 1074 |
| 162 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +10 | 47475 |
| 163 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2462 |
| 164 | [sowarma/wp2shell-PoC](https://github.com/sowarma/wp2shell-PoC) | +10 | 914 |
| 165 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1586 |
| 166 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +10 | 2018 |
| 167 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 2015 |
| 168 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +9 | 0 |
| 169 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +9 | 34736 |
| 170 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45556 |
| 171 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 2405 |
| 172 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 10960 |
| 173 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6446 |
| 174 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +9 | 24797 |
| 175 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1241 |
| 176 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1236 |
| 177 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 9087 |
| 178 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10897 |
| 179 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1682 |
| 180 | [jundot/omlx](https://github.com/jundot/omlx) | +8 | 20843 |
| 181 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6648 |
| 182 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1922 |
| 183 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +8 | 17195 |
| 184 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9427 |
| 185 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +8 | 912 |
| 186 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8818 |
| 187 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3578 |
| 188 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +7 | 888 |
| 189 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1265 |
| 190 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27685 |
| 191 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +7 | 10298 |
| 192 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 193 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 7109 |
| 194 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 195 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1698 |
| 196 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1364 |
| 197 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +6 | 9951 |
| 198 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 286 |
| 199 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +6 | 3727 |
| 200 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 359 |
| 201 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 513 |
| 202 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3917 |
| 203 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +6 | 352 |
| 204 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3153 |
| 205 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1595 |
| 206 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 1016 |
| 207 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +5 | 1772 |
| 208 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +5 | 7118 |
| 209 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3492 |
| 210 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +5 | 10710 |
| 211 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 703 |
| 212 | [openai/plugins](https://github.com/openai/plugins) | +5 | 5247 |
| 213 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 214 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 858 |
| 215 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +5 | 1465 |
| 216 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3579 |
| 217 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +5 | 26430 |
| 218 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +5 | 28045 |
| 219 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 543 |
| 220 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1443 |
| 221 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 3623 |
| 222 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +4 | 413 |
| 223 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 760 |
| 224 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +4 | 5695 |
| 225 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2277 |
| 226 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 632 |
| 227 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5890 |
| 228 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +4 | 181 |
| 229 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 816 |
| 230 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3130 |
| 231 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1274 |
| 232 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +4 | 9798 |
| 233 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 14156 |
| 234 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 261 |
| 235 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 567 |
| 236 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5113 |
| 237 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7346 |
| 238 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5298 |
| 239 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1216 |
| 240 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 166 |
| 241 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 990 |
| 242 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4926 |
| 243 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 304 |
| 244 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 208 |
| 245 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6026 |
| 246 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 900 |
| 247 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 295 |
| 248 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1254 |
| 249 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 523 |
| 250 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6166 |
| 251 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 651 |
| 252 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 629 |
| 253 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1784 |
| 254 | [visualbruno/3DGenStudio](https://github.com/visualbruno/3DGenStudio) | +3 | 552 |
| 255 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 9013 |
| 256 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 913 |
| 257 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 219 |
| 258 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 3161 |
| 259 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +3 | 8926 |
| 260 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +3 | 533 |
| 261 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 195 |
| 262 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +3 | 3626 |
| 263 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 698 |
| 264 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 416 |
| 265 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 255 |
| 266 | [penecho/penecho](https://github.com/penecho/penecho) | +3 | 2140 |
| 267 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1275 |
| 268 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4898 |
| 269 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 247 |
| 270 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 993 |
| 271 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 584 |
| 272 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 345 |
| 273 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2164 |
| 274 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28834 |
| 275 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 276 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2588 |
| 277 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 581 |
| 278 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 750 |
| 279 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 141 |
| 280 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 281 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 87 |
| 282 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 547 |
| 283 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 125 |
| 284 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 212 |
| 285 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2571 |
| 286 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3792 |
| 287 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1055 |
| 288 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 642 |
| 289 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 297 |
| 290 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2938 |
| 291 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 228 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1250 |
| 293 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1413 |
| 294 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 526 |
| 295 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 269 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 917 |
| 297 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1363 |
| 298 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 177 |
| 299 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +1 | 147 |
| 300 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 973 |
