---
title: "2026-08-30 GitHub增长趋势报告"
description: "1.archify+41 2.gods-eye-view+13 3.PRAXIST+11 4.scientific-agent-skills+10 5.router+9"
date: 2026-08-30T22:28:28+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-30 22:28:28

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
        'daily': {"categories": ["RockxyApp/Rockxy", "freestylefly/awesome-gpt-image-2", "stemdeckapp/stemdeck", "kaifcodec/user-scanner", "pathwaycom/arc-task-gen", "tashfeenahmed/freellmapi", "volcengine/OpenViking", "vorssaintapp/vorssaint-utils", "openJiuwen-ai/jiuwenswarm", "miuuyy/codex-chatgpt-web", "calesthio/OpenMontage", "MadsLorentzen/ai-job-search", "stablyai/orca", "zhaoxuya520/reverse-skill", "hieunc229/mailflare", "workweave/router", "K-Dense-AI/scientific-agent-skills", "sapientinc/PRAXIST", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 11, 13, 41]},
        'weekly': {"categories": ["volcengine/OpenViking", "workweave/router", "virgiliojr94/book-to-skill", "pathwaycom/arc-task-gen", "tashfeenahmed/freellmapi", "anywhere-labs/deepseek-harness-desktop", "k1tbyte/Wand-Enhancer", "THU-MAIC/OpenMAIC", "calesthio/OpenMontage", "K-Dense-AI/scientific-agent-skills", "sapientinc/PRAXIST", "vorssaintapp/vorssaint-utils", "openJiuwen-ai/jiuwenswarm", "FlashML-org/FreeToken", "stablyai/orca", "MadsLorentzen/ai-job-search", "basecamp/omarchy", "freestylefly/awesome-gpt-image-2", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [18, 18, 19, 20, 20, 21, 21, 23, 24, 26, 27, 29, 29, 30, 34, 34, 41, 61, 80, 139]},
        'monthly': {"categories": ["ayghri/i-have-adhd", "TencentCloud/TencentDB-Agent-Memory", "herdrdev/herdr", "k1tbyte/Wand-Enhancer", "bojieli/ai-agent-book", "freestylefly/awesome-gpt-image-2", "emilkowalski/skills", "bilawalsidhu/gods-eye-view", "floci-io/floci", "cloudflare/computer", "block/buzz", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "virgiliojr94/book-to-skill", "zhaoxuya520/reverse-skill", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "tt-a1i/archify", "PrimeIntellect-ai/prime-agent"], "data": [66, 69, 71, 72, 76, 76, 78, 80, 81, 86, 92, 95, 103, 109, 111, 126, 135, 168, 187, 264]}
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
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +41 | 34314 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +13 | 13744 |
| 3 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +11 | 4522 |
| 4 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 39122 |
| 5 | [workweave/router](https://github.com/workweave/router) | +9 | 3079 |
| 6 | [hieunc229/mailflare](https://github.com/hieunc229/mailflare) | +9 | 1968 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +8 | 31957 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +8 | 57336 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +7 | 38484 |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +7 | 54612 |
| 11 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +7 | 2647 |
| 12 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +6 | 5885 |
| 13 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +6 | 13834 |
| 14 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +6 | 34484 |
| 15 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +6 | 22729 |
| 16 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +6 | 9054 |
| 17 | [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | +5 | 3885 |
| 18 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +5 | 3373 |
| 19 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 25615 |
| 20 | [RockxyApp/Rockxy](https://github.com/RockxyApp/Rockxy) | +5 | 1311 |
| 21 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +5 | 9570 |
| 22 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +4 | 2791 |
| 23 | [daimon3332/address](https://github.com/daimon3332/address) | +4 | 1892 |
| 24 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +4 | 29132 |
| 25 | [every-app/open-seo](https://github.com/every-app/open-seo) | +4 | 15105 |
| 26 | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | +4 | 1882 |
| 27 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +4 | 13706 |
| 28 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 27301 |
| 29 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +4 | 43635 |
| 30 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 10663 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +139 | 34314 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +80 | 13744 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +61 | 25615 |
| 4 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +41 | 35483 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +34 | 38484 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +34 | 57336 |
| 7 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +30 | 10091 |
| 8 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +29 | 5885 |
| 9 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +29 | 13834 |
| 10 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +27 | 4522 |
| 11 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +26 | 39122 |
| 12 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +24 | 54612 |
| 13 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +23 | 23840 |
| 14 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +21 | 22910 |
| 15 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +21 | 22077 |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +20 | 22729 |
| 17 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +20 | 9054 |
| 18 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +19 | 27301 |
| 19 | [workweave/router](https://github.com/workweave/router) | +18 | 3079 |
| 20 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +18 | 34484 |
| 21 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +17 | 2366 |
| 22 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +16 | 2230 |
| 23 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +15 | 31957 |
| 24 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +15 | 19467 |
| 25 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +15 | 14393 |
| 26 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +14 | 2647 |
| 27 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +14 | 17882 |
| 28 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +13 | 2966 |
| 29 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +13 | 43635 |
| 30 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +13 | 33683 |
| 31 | [floci-io/floci](https://github.com/floci-io/floci) | +13 | 22801 |
| 32 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +13 | 28781 |
| 33 | [tobi/walgit](https://github.com/tobi/walgit) | +13 | 2349 |
| 34 | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | +12 | 1882 |
| 35 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +12 | 9570 |
| 36 | [cursor/plugins](https://github.com/cursor/plugins) | +12 | 6265 |
| 37 | [Webeoidentify/Honeypot-Detector](https://github.com/Webeoidentify/Honeypot-Detector) | +12 | 2237 |
| 38 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +12 | 35605 |
| 39 | [every-app/open-seo](https://github.com/every-app/open-seo) | +11 | 15105 |
| 40 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +11 | 39002 |
| 41 | [blader/humanizer](https://github.com/blader/humanizer) | +11 | 39016 |
| 42 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +10 | 2966 |
| 43 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +10 | 13706 |
| 44 | [t8y2/dbx](https://github.com/t8y2/dbx) | +10 | 17477 |
| 45 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +10 | 930 |
| 46 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +10 | 25756 |
| 47 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +10 | 13562 |
| 48 | [hieunc229/mailflare](https://github.com/hieunc229/mailflare) | +9 | 1968 |
| 49 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +9 | 33661 |
| 50 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +9 | 10663 |
| 51 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +9 | 33382 |
| 52 | [daimon3332/address](https://github.com/daimon3332/address) | +8 | 1892 |
| 53 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +8 | 29132 |
| 54 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +8 | 17056 |
| 55 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 48289 |
| 56 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +8 | 2880 |
| 57 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +8 | 5225 |
| 58 | [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | +7 | 3885 |
| 59 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +7 | 15535 |
| 60 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +7 | 28486 |
| 61 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 37950 |
| 62 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +7 | 1034 |
| 63 | [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) | +7 | 1077 |
| 64 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +7 | 31704 |
| 65 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +7 | 34542 |
| 66 | [MudCosmetologist/Autocad-Software](https://github.com/MudCosmetologist/Autocad-Software) | +7 | 1197 |
| 67 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +7 | 3539 |
| 68 | [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | +7 | 5025 |
| 69 | [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | +7 | 1021 |
| 70 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +6 | 2791 |
| 71 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +6 | 3373 |
| 72 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +6 | 10681 |
| 73 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +6 | 3883 |
| 74 | [agentconnect-md/agentconnect](https://github.com/agentconnect-md/agentconnect) | +6 | 900 |
| 75 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +6 | 2865 |
| 76 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +6 | 9768 |
| 77 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +6 | 14570 |
| 78 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +6 | 6931 |
| 79 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 15866 |
| 80 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 32117 |
| 81 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +6 | 50377 |
| 82 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +6 | 2439 |
| 83 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +6 | 2738 |
| 84 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 6477 |
| 85 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +5 | 19395 |
| 86 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3831 |
| 87 | [RockxyApp/Rockxy](https://github.com/RockxyApp/Rockxy) | +5 | 1311 |
| 88 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +5 | 41293 |
| 89 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +5 | 19259 |
| 90 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | +5 | 11766 |
| 91 | [Waishnav/devspace](https://github.com/Waishnav/devspace) | +5 | 4293 |
| 92 | [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | +5 | 4179 |
| 93 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 64329 |
| 94 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +5 | 8703 |
| 95 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +5 | 6515 |
| 96 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +5 | 5643 |
| 97 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 37907 |
| 98 | [warpdotdev/common-skills](https://github.com/warpdotdev/common-skills) | +5 | 433 |
| 99 | [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | +5 | 1298 |
| 100 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +5 | 6823 |
| 101 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +4 | 46173 |
| 102 | [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) | +4 | 3033 |
| 103 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +4 | 913 |
| 104 | [cdxiaodong/cain-agent](https://github.com/cdxiaodong/cain-agent) | +4 | 463 |
| 105 | [harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science) | +4 | 381 |
| 106 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 31727 |
| 107 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 34696 |
| 108 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +4 | 7536 |
| 109 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +4 | 2676 |
| 110 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +4 | 21881 |
| 111 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +4 | 5835 |
| 112 | [zeenie-ai/OpenCompany](https://github.com/zeenie-ai/OpenCompany) | +4 | 799 |
| 113 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +4 | 8116 |
| 114 | [lxf746/outlook-auto-register](https://github.com/lxf746/outlook-auto-register) | +4 | 578 |
| 115 | [KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess) | +4 | 1125 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4 | 48675 |
| 117 | [block/buzz](https://github.com/block/buzz) | +3 | 31542 |
| 118 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +3 | 9809 |
| 119 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 21688 |
| 120 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +3 | 11828 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +264 | 19259 |
| 2 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +187 | 34315 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +168 | 19395 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +135 | 28781 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +126 | 57336 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +111 | 31957 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +109 | 27301 |
| 8 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +103 | 22077 |
| 9 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +95 | 19467 |
| 10 | [block/buzz](https://github.com/block/buzz) | +92 | 31542 |
| 11 | [cloudflare/computer](https://github.com/cloudflare/computer) | +86 | 8839 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +81 | 22801 |
| 13 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +80 | 13744 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +78 | 33683 |
| 15 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +76 | 25615 |
| 16 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +76 | 43635 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +72 | 22910 |
| 18 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +71 | 33661 |
| 19 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +69 | 25269 |
| 20 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +66 | 25756 |
| 21 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | +66 | 6809 |
| 22 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6392 |
| 23 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +64 | 38484 |
| 24 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11828 |
| 25 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +64 | 16985 |
| 26 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +63 | 13706 |
| 27 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +63 | 35483 |
| 28 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +61 | 11381 |
| 29 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9389 |
| 30 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +58 | 50377 |
| 31 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +58 | 21935 |
| 32 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +54 | 13834 |
| 33 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +53 | 54612 |
| 34 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +53 | 17056 |
| 35 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +50 | 9054 |
| 36 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +50 | 34484 |
| 37 | [yc-software/qm](https://github.com/yc-software/qm) | +49 | 14369 |
| 38 | [blader/humanizer](https://github.com/blader/humanizer) | +47 | 39016 |
| 39 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +47 | 28486 |
| 40 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +47 | 7494 |
| 41 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +46 | 1839 |
| 42 | [google/skills](https://github.com/google/skills) | +44 | 19008 |
| 43 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +43 | 5885 |
| 44 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +43 | 17882 |
| 45 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +42 | 10092 |
| 46 | [every-app/open-seo](https://github.com/every-app/open-seo) | +41 | 15105 |
| 47 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 64329 |
| 48 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +40 | 37907 |
| 49 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +39 | 37950 |
| 50 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +39 | 12609 |
| 51 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +38 | 4603 |
| 52 | [trycompai/crm](https://github.com/trycompai/crm) | +37 | 9134 |
| 53 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +37 | 35275 |
| 54 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +36 | 39122 |
| 55 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +36 | 22729 |
| 56 | [multica-ai/multica](https://github.com/multica-ai/multica) | +35 | 48289 |
| 57 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +34 | 21078 |
| 58 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +34 | 6515 |
| 59 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +33 | 29532 |
| 60 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +32 | 9768 |
| 61 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +32 | 22455 |
| 62 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +31 | 5225 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +31 | 46173 |
| 64 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +31 | 21664 |
| 65 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +30 | 13562 |
| 66 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +30 | 5022 |
| 67 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +30 | 26476 |
| 68 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +30 | 5106 |
| 69 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +30 | 10926 |
| 70 | [get-bb/bb](https://github.com/get-bb/bb) | +30 | 2764 |
| 71 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +30 | 16504 |
| 72 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +29 | 2966 |
| 73 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +29 | 32117 |
| 74 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +29 | 6777 |
| 75 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 15872 |
| 76 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +28 | 2647 |
| 77 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +28 | 41293 |
| 78 | [spinabot/brigade](https://github.com/spinabot/brigade) | +28 | 3190 |
| 79 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +28 | 5319 |
| 80 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +28 | 24783 |
| 81 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +27 | 4522 |
| 82 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +27 | 14570 |
| 83 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +27 | 3539 |
| 84 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +27 | 11064 |
| 85 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +27 | 14387 |
| 86 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 31016 |
| 87 | [t8y2/dbx](https://github.com/t8y2/dbx) | +26 | 17477 |
| 88 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +26 | 10663 |
| 89 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +25 | 14539 |
| 90 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +24 | 23840 |
| 91 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +24 | 31704 |
| 92 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | +24 | 32435 |
| 93 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +24 | 43177 |
| 94 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 95 | [cursor/plugins](https://github.com/cursor/plugins) | +23 | 6265 |
| 96 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +23 | 14393 |
| 97 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 33438 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +22 | 39901 |
| 99 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +22 | 25265 |
| 100 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 34696 |
| 101 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +21 | 3861 |
| 102 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +21 | 34542 |
| 103 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +20 | 7536 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +20 | 21881 |
| 105 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +20 | 3013 |
| 106 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +20 | 6477 |
| 107 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 108 | [browser-use/video-use](https://github.com/browser-use/video-use) | +20 | 21688 |
| 109 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +19 | 5643 |
| 110 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1884 |
| 111 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +19 | 12088 |
| 112 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +19 | 15866 |
| 113 | [titanwings/distilly](https://github.com/titanwings/distilly) | +19 | 24169 |
| 114 | [workweave/router](https://github.com/workweave/router) | +18 | 3079 |
| 115 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 6823 |
| 116 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +18 | 9882 |
| 117 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +18 | 6931 |
| 118 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 48675 |
| 119 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 44256 |
| 120 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +16 | 35605 |
| 121 | [securo-finance/securo](https://github.com/securo-finance/securo) | +16 | 2693 |
| 122 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +16 | 31727 |
| 123 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +16 | 2120 |
| 124 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1226 |
| 125 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +16 | 2439 |
| 126 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3805 |
| 127 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +15 | 2791 |
| 128 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +15 | 3022 |
| 129 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +15 | 1984 |
| 130 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 881 |
| 131 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +15 | 2796 |
| 132 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 914 |
| 133 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9516 |
| 134 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +14 | 9246 |
| 135 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +14 | 3435 |
| 136 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +14 | 3300 |
| 137 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +14 | 2824 |
| 138 | [cinderline/northcinder](https://github.com/cinderline/northcinder) | +14 | 1218 |
| 139 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +14 | 662 |
| 140 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10874 |
| 141 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +13 | 5835 |
| 142 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 30978 |
| 143 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 6270 |
| 144 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +13 | 2919 |
| 145 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9808 |
| 146 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26698 |
| 147 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +13 | 2987 |
| 148 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2242 |
| 149 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 150 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +12 | 1034 |
| 151 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3989 |
| 152 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3979 |
| 153 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +12 | 5157 |
| 154 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +12 | 1676 |
| 155 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1448 |
| 156 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +12 | 8815 |
| 157 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +12 | 6604 |
| 158 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +12 | 3737 |
| 159 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28406 |
| 160 | [petergyang/human-review](https://github.com/petergyang/human-review) | +12 | 1196 |
| 161 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +11 | 9220 |
| 162 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +11 | 2676 |
| 163 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +11 | 14048 |
| 164 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +11 | 4213 |
| 165 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +11 | 2030 |
| 166 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +10 | 930 |
| 167 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +10 | 45705 |
| 168 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14836 |
| 169 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +10 | 1516 |
| 170 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3109 |
| 171 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1548 |
| 172 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +10 | 32562 |
| 173 | [jundot/omlx](https://github.com/jundot/omlx) | +9 | 21048 |
| 174 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +9 | 747 |
| 175 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 10988 |
| 176 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6523 |
| 177 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +9 | 3831 |
| 178 | [memorax-ai/memorax-code](https://github.com/memorax-ai/memorax-code) | +9 | 1149 |
| 179 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +9 | 947 |
| 180 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8919 |
| 181 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +8 | 29132 |
| 182 | [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | +8 | 3885 |
| 183 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1998 |
| 184 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6693 |
| 185 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +8 | 17896 |
| 186 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 7249 |
| 187 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +8 | 9990 |
| 188 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 27734 |
| 189 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +7 | 0 |
| 190 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +7 | 2865 |
| 191 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +7 | 913 |
| 192 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +7 | 17252 |
| 193 | [cdxiaodong/cain-agent](https://github.com/cdxiaodong/cain-agent) | +7 | 463 |
| 194 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +7 | 8703 |
| 195 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +7 | 1161 |
| 196 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1277 |
| 197 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +7 | 758 |
| 198 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 199 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +7 | 2043 |
| 200 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 201 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +6 | 3373 |
| 202 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +6 | 811 |
| 203 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1484 |
| 204 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1725 |
| 205 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +6 | 1823 |
| 206 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 10369 |
| 207 | [openai/plugins](https://github.com/openai/plugins) | +6 | 5280 |
| 208 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 287 |
| 209 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 363 |
| 210 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 517 |
| 211 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +6 | 1511 |
| 212 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3935 |
| 213 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +6 | 371 |
| 214 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +5 | 1460 |
| 215 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1600 |
| 216 | [zarazhangrui/youtube-digest](https://github.com/zarazhangrui/youtube-digest) | +5 | 988 |
| 217 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3170 |
| 218 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +5 | 186 |
| 219 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +5 | 7224 |
| 220 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +5 | 3740 |
| 221 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 222 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 868 |
| 223 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 619 |
| 224 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1282 |
| 225 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5924 |
| 226 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +4 | 6432 |
| 227 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 3649 |
| 228 | [zanwei/design-dna](https://github.com/zanwei/design-dna) | +4 | 1598 |
| 229 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 804 |
| 230 | [davatron5000/microlighter](https://github.com/davatron5000/microlighter) | +4 | 633 |
| 231 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +4 | 5721 |
| 232 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 6245 |
| 233 | [vlln/whale-girl](https://github.com/vlln/whale-girl) | +4 | 300 |
| 234 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 635 |
| 235 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2296 |
| 236 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +4 | 645 |
| 237 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 844 |
| 238 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +4 | 3219 |
| 239 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3169 |
| 240 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1288 |
| 241 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 276 |
| 242 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 583 |
| 243 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5200 |
| 244 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5308 |
| 245 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1288 |
| 246 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 170 |
| 247 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3613 |
| 248 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 2195 |
| 249 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 1012 |
| 250 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +4 | 26492 |
| 251 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +3 | 460 |
| 252 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 305 |
| 253 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 311 |
| 254 | [fxyadela/write-then-publish](https://github.com/fxyadela/write-then-publish) | +3 | 499 |
| 255 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +3 | 490 |
| 256 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +3 | 135 |
| 257 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +3 | 1464 |
| 258 | [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | +3 | 163 |
| 259 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 212 |
| 260 | [GamePhanesStudio/GamePhanes](https://github.com/GamePhanesStudio/GamePhanes) | +3 | 540 |
| 261 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6035 |
| 262 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 915 |
| 263 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +3 | 30643 |
| 264 | [diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness) | +3 | 799 |
| 265 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1299 |
| 266 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4915 |
| 267 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 261 |
| 268 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 1017 |
| 269 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 619 |
| 270 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28866 |
| 271 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 272 | [crimera/piko](https://github.com/crimera/piko) | +3 | 4987 |
| 273 | [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills) | +2 | 153 |
| 274 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 612 |
| 275 | [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) | +2 | 1806 |
| 276 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 751 |
| 277 | [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer) | +2 | 1166 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 279 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 88 |
| 280 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 555 |
| 281 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 126 |
| 282 | [YesSteveModel/YesSteveModel](https://github.com/YesSteveModel/YesSteveModel) | +2 | 32 |
| 283 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 218 |
| 284 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2581 |
| 285 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3812 |
| 286 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1059 |
| 287 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 682 |
| 288 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 306 |
| 289 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +2 | 349 |
| 290 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 228 |
| 291 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1255 |
| 292 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1413 |
| 293 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 530 |
| 294 | [youdidking/stanngv2](https://github.com/youdidking/stanngv2) | +1 | 393 |
| 295 | [xingguangqwq/traceguard-vscode](https://github.com/xingguangqwq/traceguard-vscode) | +1 | 86 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 926 |
| 297 | [silentchainai/SILENTCHAIN](https://github.com/silentchainai/SILENTCHAIN) | +1 | 449 |
| 298 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 187 |
| 299 | [OpenVapeCN/VapeV4.21](https://github.com/OpenVapeCN/VapeV4.21) | +1 | 168 |
| 300 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +1 | 5353 |
