---
title: "2026-08-29 GitHub增长趋势报告"
description: "1.archify+33 2.gods-eye-view+28 3.awesome-gpt-image-2+12 4.jiuwenswarm+12 5.orca+11"
date: 2026-08-29T02:45:04+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-29 02:45:04

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
        'daily': {"categories": ["Lakr233/vphone-cli", "t8y2/dbx", "K-Dense-AI/scientific-agent-skills", "experientiallabs/experiential", "anywhere-labs/deepseek-harness-desktop", "firecrawl/anydoc", "cathrynlavery/diagram-design", "rohitg00/ai-engineering-from-scratch", "tashfeenahmed/freellmapi", "Tencent/WeMM-Embedding", "AgriciDaniel/claude-obsidian", "workweave/router", "calesthio/OpenMontage", "MadsLorentzen/ai-job-search", "pathwaycom/arc-task-gen", "stablyai/orca", "openJiuwen-ai/jiuwenswarm", "freestylefly/awesome-gpt-image-2", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 8, 11, 12, 12, 28, 33]},
        'weekly': {"categories": ["CopilotKit/OpenBot", "blader/humanizer", "AgriciDaniel/claude-obsidian", "virgiliojr94/book-to-skill", "rohitg00/ai-engineering-from-scratch", "calesthio/OpenMontage", "openJiuwen-ai/jiuwenswarm", "volcengine/OpenViking", "cathrynlavery/diagram-design", "guillaumemeyer/watermarks-remover", "AprilNEA/OpenLogi", "pathwaycom/arc-task-gen", "vorssaintapp/vorssaint-utils", "MadsLorentzen/ai-job-search", "anywhere-labs/deepseek-harness-desktop", "stablyai/orca", "FlashML-org/FreeToken", "freestylefly/awesome-gpt-image-2", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [15, 15, 16, 17, 17, 17, 17, 20, 21, 23, 24, 24, 25, 28, 29, 35, 37, 56, 60, 72]},
        'monthly': {"categories": ["firecrawl/pdf-inspector", "ifixai-ai/iFixAi", "brightdata/cli", "TencentCloud/TencentDB-Agent-Memory", "freestylefly/awesome-gpt-image-2", "herdrdev/herdr", "ayghri/i-have-adhd", "floci-io/floci", "emilkowalski/skills", "bojieli/ai-agent-book", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "block/buzz", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "tt-a1i/archify", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [63, 64, 66, 67, 67, 71, 71, 77, 78, 82, 89, 95, 96, 103, 115, 116, 127, 133, 167, 264]}
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
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +33 | 27735 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +28 | 11175 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +12 | 24323 |
| 4 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +12 | 4834 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +11 | 56248 |
| 6 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +8 | 8546 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +6 | 37761 |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +5 | 53371 |
| 9 | [workweave/router](https://github.com/workweave/router) | +5 | 2446 |
| 10 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +5 | 14305 |
| 11 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +5 | 826 |
| 12 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +5 | 21657 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +5 | 50643 |
| 14 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +5 | 28335 |
| 15 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +4 | 19083 |
| 16 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +4 | 21578 |
| 17 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | +4 | 709 |
| 18 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 36709 |
| 19 | [t8y2/dbx](https://github.com/t8y2/dbx) | +4 | 17292 |
| 20 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +4 | 8677 |
| 21 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +4 | 962 |
| 22 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +4 | 2773 |
| 23 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +3 | 10328 |
| 24 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 26725 |
| 25 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +3 | 28160 |
| 26 | [harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science) | +3 | 362 |
| 27 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +3 | 13130 |
| 28 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +3 | 2621 |
| 29 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +3 | 33218 |
| 30 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 34161 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +72 | 27735 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +60 | 11175 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +56 | 24323 |
| 4 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +37 | 9373 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +35 | 56248 |
| 6 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +29 | 21578 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +28 | 37761 |
| 8 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +25 | 13130 |
| 9 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +24 | 8546 |
| 10 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +24 | 17423 |
| 11 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +23 | 19076 |
| 12 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +21 | 28335 |
| 13 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +20 | 34161 |
| 14 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +17 | 4834 |
| 15 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +17 | 53371 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +17 | 50643 |
| 17 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +17 | 26725 |
| 18 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +16 | 14305 |
| 19 | [blader/humanizer](https://github.com/blader/humanizer) | +15 | 38623 |
| 20 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +15 | 3311 |
| 21 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 25363 |
| 22 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +14 | 5085 |
| 23 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +13 | 21657 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +13 | 33272 |
| 25 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +13 | 13406 |
| 26 | [cursor/plugins](https://github.com/cursor/plugins) | +13 | 5978 |
| 27 | [Webeoidentify/Honeypot-Detector](https://github.com/Webeoidentify/Honeypot-Detector) | +12 | 2236 |
| 28 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +12 | 1712 |
| 29 | [tobi/walgit](https://github.com/tobi/walgit) | +12 | 2297 |
| 30 | [floci-io/floci](https://github.com/floci-io/floci) | +12 | 22583 |
| 31 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +12 | 30144 |
| 32 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +12 | 14195 |
| 33 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +11 | 2773 |
| 34 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +11 | 38737 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +11 | 28160 |
| 36 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +11 | 39756 |
| 37 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +11 | 14354 |
| 38 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +11 | 14463 |
| 39 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +10 | 2738 |
| 40 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +10 | 37657 |
| 41 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +10 | 33218 |
| 42 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +10 | 34461 |
| 43 | [multica-ai/multica](https://github.com/multica-ai/multica) | +9 | 48149 |
| 44 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +9 | 1680 |
| 45 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +9 | 962 |
| 46 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +9 | 43023 |
| 47 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +9 | 50047 |
| 48 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +9 | 1975 |
| 49 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +8 | 826 |
| 50 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +8 | 19083 |
| 51 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +8 | 36709 |
| 52 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +8 | 2621 |
| 53 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +8 | 35061 |
| 54 | [t8y2/dbx](https://github.com/t8y2/dbx) | +8 | 17292 |
| 55 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +8 | 13367 |
| 56 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +8 | 5230 |
| 57 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +8 | 33076 |
| 58 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +8 | 6483 |
| 59 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1590 |
| 60 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +8 | 6368 |
| 61 | [workweave/router](https://github.com/workweave/router) | +7 | 2446 |
| 62 | [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | +7 | 4974 |
| 63 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +7 | 2678 |
| 64 | [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | +7 | 980 |
| 65 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +7 | 3525 |
| 66 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +7 | 26368 |
| 67 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +7 | 9584 |
| 68 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +7 | 2245 |
| 69 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +7 | 1184 |
| 70 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +6 | 16824 |
| 71 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 31982 |
| 72 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +6 | 23662 |
| 73 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +6 | 21608 |
| 74 | [missuo/kumone](https://github.com/missuo/kumone) | +6 | 838 |
| 75 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 11329 |
| 76 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +6 | 22396 |
| 77 | [harry0703/MangoDisk](https://github.com/harry0703/MangoDisk) | +6 | 1636 |
| 78 | [MacPaw/cleanmymac-cli](https://github.com/MacPaw/cleanmymac-cli) | +6 | 684 |
| 79 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +6 | 1270 |
| 80 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +6 | 2996 |
| 81 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 9753 |
| 82 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +5 | 10328 |
| 83 | [yetone/cumora](https://github.com/yetone/cumora) | +5 | 3223 |
| 84 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +5 | 15356 |
| 85 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 10348 |
| 86 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +5 | 2378 |
| 87 | [PoltergeistGunsmith/Portfolio-Rebalancer](https://github.com/PoltergeistGunsmith/Portfolio-Rebalancer) | +5 | 717 |
| 88 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +5 | 7352 |
| 89 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 45998 |
| 90 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +5 | 15712 |
| 91 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +5 | 2599 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 48528 |
| 93 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +5 | 41510 |
| 94 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +5 | 45609 |
| 95 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +5 | 5774 |
| 96 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 37795 |
| 97 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +5 | 31521 |
| 98 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +5 | 1044 |
| 99 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 16411 |
| 100 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +4 | 3789 |
| 101 | [block/buzz](https://github.com/block/buzz) | +4 | 31315 |
| 102 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +4 | 64219 |
| 103 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | +4 | 709 |
| 104 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +4 | 8677 |
| 105 | [noctalia-dev/umbriel](https://github.com/noctalia-dev/umbriel) | +4 | 340 |
| 106 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +4 | 2552 |
| 107 | [KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess) | +4 | 1075 |
| 108 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 6724 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +4 | 12521 |
| 110 | [Audio8-AI/Audio8_TTS](https://github.com/Audio8-AI/Audio8_TTS) | +4 | 1030 |
| 111 | [shengjidaguai-china/BossHunter](https://github.com/shengjidaguai-china/BossHunter) | +4 | 529 |
| 112 | [anbeime/skill](https://github.com/anbeime/skill) | +4 | 5895 |
| 113 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +4 | 855 |
| 114 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +4 | 4247 |
| 115 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +4 | 3909 |
| 116 | [jundot/omlx](https://github.com/jundot/omlx) | +4 | 20905 |
| 117 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +4 | 2576 |
| 118 | [harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science) | +3 | 362 |
| 119 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +3 | 10969 |
| 120 | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | +3 | 717 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +264 | 18966 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +167 | 19083 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +133 | 28335 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +127 | 56248 |
| 5 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +116 | 27735 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +115 | 26725 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +103 | 30144 |
| 8 | [block/buzz](https://github.com/block/buzz) | +96 | 31315 |
| 9 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +95 | 21578 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +89 | 19076 |
| 11 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +82 | 43023 |
| 12 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +78 | 33272 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +77 | 22583 |
| 14 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +71 | 25363 |
| 15 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +71 | 33218 |
| 16 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +67 | 24323 |
| 17 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +67 | 25050 |
| 18 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6396 |
| 19 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11329 |
| 20 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +63 | 16840 |
| 21 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +62 | 11176 |
| 22 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +61 | 21752 |
| 23 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9345 |
| 24 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +60 | 11142 |
| 25 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +59 | 13406 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +58 | 50047 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +56 | 37762 |
| 28 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21743 |
| 29 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +52 | 16824 |
| 30 | [yc-software/qm](https://github.com/yc-software/qm) | +49 | 14312 |
| 31 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +47 | 28160 |
| 32 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 38623 |
| 33 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 7336 |
| 34 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +45 | 13130 |
| 35 | [google/skills](https://github.com/google/skills) | +44 | 18929 |
| 36 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +43 | 53371 |
| 37 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +43 | 34161 |
| 38 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1403 |
| 39 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +42 | 8546 |
| 40 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +40 | 17423 |
| 41 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +40 | 12458 |
| 42 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +40 | 33615 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 64219 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +38 | 37795 |
| 45 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +38 | 35238 |
| 46 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +37 | 9373 |
| 47 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +37 | 37657 |
| 48 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +37 | 4535 |
| 49 | [openai/codex-security](https://github.com/openai/codex-security) | +37 | 10247 |
| 50 | [multica-ai/multica](https://github.com/multica-ai/multica) | +36 | 48149 |
| 51 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 9066 |
| 52 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +35 | 50643 |
| 53 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +35 | 16411 |
| 54 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +34 | 21578 |
| 55 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +34 | 29458 |
| 56 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +33 | 20897 |
| 57 | [every-app/open-seo](https://github.com/every-app/open-seo) | +32 | 14212 |
| 58 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +32 | 26368 |
| 59 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +32 | 22396 |
| 60 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +31 | 6389 |
| 61 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +31 | 45998 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 10623 |
| 63 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +30 | 4834 |
| 64 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +30 | 5085 |
| 65 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +30 | 9584 |
| 66 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +30 | 15795 |
| 67 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +29 | 14354 |
| 68 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +29 | 31982 |
| 69 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +29 | 5020 |
| 70 | [get-bb/bb](https://github.com/get-bb/bb) | +29 | 2742 |
| 71 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +29 | 24717 |
| 72 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +28 | 4852 |
| 73 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +28 | 13367 |
| 74 | [spinabot/brigade](https://github.com/spinabot/brigade) | +28 | 3151 |
| 75 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +28 | 6609 |
| 76 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +27 | 14195 |
| 77 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +27 | 6728 |
| 78 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +26 | 11005 |
| 79 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +26 | 14463 |
| 80 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +26 | 21657 |
| 81 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +26 | 42996 |
| 82 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5261 |
| 83 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +26 | 30970 |
| 84 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 23161 |
| 85 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +25 | 3311 |
| 86 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +25 | 41017 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +24 | 39757 |
| 88 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | +24 | 32395 |
| 89 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 825 |
| 90 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +23 | 14305 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 25166 |
| 92 | [t8y2/dbx](https://github.com/t8y2/dbx) | +22 | 17292 |
| 93 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 34620 |
| 94 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2691 |
| 95 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +21 | 41510 |
| 96 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +21 | 33310 |
| 97 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3789 |
| 98 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +20 | 7352 |
| 99 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +20 | 3015 |
| 100 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +20 | 31521 |
| 101 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 102 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +19 | 34461 |
| 103 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +19 | 21608 |
| 104 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1873 |
| 105 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 6368 |
| 106 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +18 | 11925 |
| 107 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 24100 |
| 108 | [browser-use/video-use](https://github.com/browser-use/video-use) | +18 | 21547 |
| 109 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +17 | 5230 |
| 110 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +17 | 36709 |
| 111 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 48528 |
| 112 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 15712 |
| 113 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 6724 |
| 114 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +17 | 9753 |
| 115 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1224 |
| 116 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3790 |
| 117 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +15 | 2996 |
| 118 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +15 | 2091 |
| 119 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 857 |
| 120 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +15 | 6744 |
| 121 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +15 | 2378 |
| 122 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +15 | 10778 |
| 123 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 911 |
| 124 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30930 |
| 125 | [securo-finance/securo](https://github.com/securo-finance/securo) | +14 | 2552 |
| 126 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +14 | 31604 |
| 127 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +14 | 3249 |
| 128 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +14 | 3359 |
| 129 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +14 | 2739 |
| 130 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2736 |
| 131 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 9446 |
| 132 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +13 | 44096 |
| 133 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +13 | 9192 |
| 134 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +13 | 1974 |
| 135 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +13 | 13995 |
| 136 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +13 | 4195 |
| 137 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9754 |
| 138 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +13 | 8761 |
| 139 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +13 | 2969 |
| 140 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 141 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2237 |
| 142 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +12 | 35061 |
| 143 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3979 |
| 144 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3909 |
| 145 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +12 | 5774 |
| 146 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1445 |
| 147 | [decolua/9router](https://github.com/decolua/9router) | +12 | 26579 |
| 148 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +12 | 555 |
| 149 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28319 |
| 150 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +11 | 962 |
| 151 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1626 |
| 152 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2868 |
| 153 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6262 |
| 154 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 6410 |
| 155 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +11 | 2025 |
| 156 | [petergyang/human-review](https://github.com/petergyang/human-review) | +11 | 1183 |
| 157 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +10 | 45609 |
| 158 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +10 | 9137 |
| 159 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4798 |
| 160 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14802 |
| 161 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 6143 |
| 162 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3087 |
| 163 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2618 |
| 164 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +10 | 1075 |
| 165 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +10 | 47505 |
| 166 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2462 |
| 167 | [sowarma/wp2shell-PoC](https://github.com/sowarma/wp2shell-PoC) | +10 | 914 |
| 168 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1590 |
| 169 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +10 | 32505 |
| 170 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +9 | 0 |
| 171 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 10969 |
| 172 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 2576 |
| 173 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6476 |
| 174 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +9 | 24831 |
| 175 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +9 | 6632 |
| 176 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 9146 |
| 177 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10907 |
| 178 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +9 | 2030 |
| 179 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +8 | 826 |
| 180 | [jundot/omlx](https://github.com/jundot/omlx) | +8 | 20905 |
| 181 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6666 |
| 182 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +8 | 17215 |
| 183 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1945 |
| 184 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9476 |
| 185 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +8 | 925 |
| 186 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8861 |
| 187 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3708 |
| 188 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 7160 |
| 189 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1270 |
| 190 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +7 | 9963 |
| 191 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27712 |
| 192 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +7 | 10323 |
| 193 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 194 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 195 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1710 |
| 196 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +6 | 1789 |
| 197 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1385 |
| 198 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +6 | 709 |
| 199 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 286 |
| 200 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +6 | 3727 |
| 201 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 362 |
| 202 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 515 |
| 203 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3927 |
| 204 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +6 | 28049 |
| 205 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +5 | 1449 |
| 206 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3160 |
| 207 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1599 |
| 208 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 1069 |
| 209 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3604 |
| 210 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +5 | 7172 |
| 211 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +5 | 10722 |
| 212 | [openai/plugins](https://github.com/openai/plugins) | +5 | 5260 |
| 213 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 214 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 863 |
| 215 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +5 | 1495 |
| 216 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +5 | 358 |
| 217 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 578 |
| 218 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 3631 |
| 219 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +4 | 459 |
| 220 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 780 |
| 221 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +4 | 5706 |
| 222 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 633 |
| 223 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2284 |
| 224 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +4 | 184 |
| 225 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5896 |
| 226 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 826 |
| 227 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +4 | 3184 |
| 228 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3150 |
| 229 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1276 |
| 230 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +4 | 9808 |
| 231 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 14182 |
| 232 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 263 |
| 233 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 572 |
| 234 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5145 |
| 235 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7361 |
| 236 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5302 |
| 237 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3590 |
| 238 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1233 |
| 239 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 168 |
| 240 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 2172 |
| 241 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 996 |
| 242 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4948 |
| 243 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +4 | 26451 |
| 244 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 305 |
| 245 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 209 |
| 246 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +3 | 6417 |
| 247 | [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | +3 | 160 |
| 248 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6028 |
| 249 | [GamePhanes/GamePhanes](https://github.com/GamePhanes/GamePhanes) | +3 | 539 |
| 250 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 907 |
| 251 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 303 |
| 252 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 607 |
| 253 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1264 |
| 254 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6187 |
| 255 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 654 |
| 256 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1789 |
| 257 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 639 |
| 258 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 625 |
| 259 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 9015 |
| 260 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 916 |
| 261 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 221 |
| 262 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +3 | 8946 |
| 263 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1282 |
| 264 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4912 |
| 265 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 250 |
| 266 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 1002 |
| 267 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 600 |
| 268 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 345 |
| 269 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28851 |
| 270 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 271 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2591 |
| 272 | [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills) | +2 | 146 |
| 273 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 606 |
| 274 | [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) | +2 | 1798 |
| 275 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 751 |
| 276 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 144 |
| 277 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 278 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 88 |
| 279 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 550 |
| 280 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 125 |
| 281 | [YesSteveModel/YesSteveModel](https://github.com/YesSteveModel/YesSteveModel) | +2 | 32 |
| 282 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 212 |
| 283 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2579 |
| 284 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3799 |
| 285 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1058 |
| 286 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 660 |
| 287 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 298 |
| 288 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 228 |
| 289 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1251 |
| 290 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1413 |
| 291 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 527 |
| 292 | [MartinDelophy/ai-video-editor](https://github.com/MartinDelophy/ai-video-editor) | +1 | 615 |
| 293 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 376 |
| 294 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 920 |
| 295 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1372 |
| 296 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 182 |
| 297 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +1 | 5339 |
| 298 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +1 | 147 |
| 299 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 973 |
| 300 | [cxOrz/AnyWhere](https://github.com/cxOrz/AnyWhere) | +1 | 10 |
