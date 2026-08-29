---
title: "2026-08-29 GitHub增长趋势报告"
description: "1.archify+34 2.gods-eye-view+11 3.editor+8 4.jiuwenswarm+7 5.codex-chatgpt-web+6"
date: 2026-08-29T22:27:56+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-29 22:27:56

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
        'daily': {"categories": ["vorssaintapp/vorssaint-utils", "rohitg00/ai-engineering-from-scratch", "andrewyng/openworker", "tashfeenahmed/freellmapi", "THU-MAIC/OpenMAIC", "every-app/open-seo", "stablyai/orca", "Lakr233/vphone-cli", "sapientinc/PRAXIST", "Gaoshu705/QzoneArchive", "cursor/plugins", "openTrinity/mycontext", "calesthio/OpenMontage", "anywhere-labs/deepseek-harness-desktop", "freestylefly/awesome-gpt-image-2", "miuuyy/codex-chatgpt-web", "openJiuwen-ai/jiuwenswarm", "diffusionstudio/editor", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 8, 11, 34]},
        'weekly': {"categories": ["Tianyu199509/DeskBox", "AgriciDaniel/claude-obsidian", "Gaoshu705/QzoneArchive", "pathwaycom/arc-task-gen", "tashfeenahmed/freellmapi", "sapientinc/PRAXIST", "K-Dense-AI/scientific-agent-skills", "calesthio/OpenMontage", "virgiliojr94/book-to-skill", "anywhere-labs/deepseek-harness-desktop", "rohitg00/ai-engineering-from-scratch", "openJiuwen-ai/jiuwenswarm", "vorssaintapp/vorssaint-utils", "MadsLorentzen/ai-job-search", "stablyai/orca", "basecamp/omarchy", "FlashML-org/FreeToken", "freestylefly/awesome-gpt-image-2", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [13, 14, 14, 15, 15, 16, 17, 17, 18, 20, 20, 23, 26, 28, 28, 30, 34, 57, 69, 99]},
        'monthly': {"categories": ["brightdata/cli", "TencentCloud/TencentDB-Agent-Memory", "k1tbyte/Wand-Enhancer", "ayghri/i-have-adhd", "bilawalsidhu/gods-eye-view", "herdrdev/herdr", "freestylefly/awesome-gpt-image-2", "floci-io/floci", "emilkowalski/skills", "bojieli/ai-agent-book", "guillaumemeyer/watermarks-remover", "block/buzz", "anywhere-labs/deepseek-harness-desktop", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "stablyai/orca", "cathrynlavery/diagram-design", "tt-a1i/archify", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [66, 67, 67, 68, 69, 71, 72, 77, 78, 80, 91, 96, 101, 105, 115, 128, 133, 147, 168, 263]}
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
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +34 | 30863 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +11 | 12538 |
| 3 | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | +8 | 1564 |
| 4 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +7 | 4860 |
| 5 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +6 | 2299 |
| 6 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 25042 |
| 7 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +6 | 21839 |
| 8 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +6 | 54023 |
| 9 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +6 | 2869 |
| 10 | [cursor/plugins](https://github.com/cursor/plugins) | +5 | 6157 |
| 11 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +5 | 2074 |
| 12 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +5 | 2930 |
| 13 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +5 | 9226 |
| 14 | [stablyai/orca](https://github.com/stablyai/orca) | +5 | 56768 |
| 15 | [every-app/open-seo](https://github.com/every-app/open-seo) | +5 | 14610 |
| 16 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +5 | 22129 |
| 17 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4 | 22187 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +4 | 16951 |
| 19 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 50951 |
| 20 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +4 | 13480 |
| 21 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 38071 |
| 22 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 27019 |
| 23 | [agentconnect-md/agentconnect](https://github.com/agentconnect-md/agentconnect) | +4 | 743 |
| 24 | [daimon3332/address](https://github.com/daimon3332/address) | +4 | 1544 |
| 25 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +4 | 8818 |
| 26 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +3 | 28654 |
| 27 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +3 | 41098 |
| 28 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +3 | 2859 |
| 29 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +2 | 3770 |
| 30 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +2 | 903 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +99 | 30863 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +69 | 12538 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +57 | 25042 |
| 4 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +34 | 9590 |
| 5 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +30 | 34743 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +28 | 56768 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +28 | 38071 |
| 8 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +26 | 13480 |
| 9 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +23 | 4860 |
| 10 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +20 | 50951 |
| 11 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +20 | 21839 |
| 12 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +18 | 27019 |
| 13 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +17 | 54023 |
| 14 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +17 | 37891 |
| 15 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +16 | 2930 |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +15 | 22187 |
| 17 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +15 | 8818 |
| 18 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +14 | 2074 |
| 19 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +14 | 14347 |
| 20 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +13 | 1979 |
| 21 | [tobi/walgit](https://github.com/tobi/walgit) | +13 | 2322 |
| 22 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +13 | 34289 |
| 23 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +13 | 17632 |
| 24 | [Webeoidentify/Honeypot-Detector](https://github.com/Webeoidentify/Honeypot-Detector) | +12 | 2237 |
| 25 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +12 | 19238 |
| 26 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 33415 |
| 27 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +11 | 2859 |
| 28 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +11 | 43364 |
| 29 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +11 | 28569 |
| 30 | [cursor/plugins](https://github.com/cursor/plugins) | +10 | 6157 |
| 31 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +10 | 903 |
| 32 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +10 | 38851 |
| 33 | [blader/humanizer](https://github.com/blader/humanizer) | +10 | 38788 |
| 34 | [workweave/router](https://github.com/workweave/router) | +9 | 2673 |
| 35 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +9 | 16951 |
| 36 | [t8y2/dbx](https://github.com/t8y2/dbx) | +9 | 17406 |
| 37 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +9 | 35374 |
| 38 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 22697 |
| 39 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 13452 |
| 40 | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | +8 | 1564 |
| 41 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +8 | 9226 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 48234 |
| 43 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +8 | 33406 |
| 44 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +8 | 30400 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +8 | 28293 |
| 46 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +8 | 2825 |
| 47 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +8 | 25564 |
| 48 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +8 | 34495 |
| 49 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +8 | 13538 |
| 50 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +8 | 5126 |
| 51 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 14610 |
| 52 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +7 | 19195 |
| 53 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +7 | 2869 |
| 54 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +7 | 2299 |
| 55 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +7 | 999 |
| 56 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +7 | 10537 |
| 57 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +7 | 14456 |
| 58 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 37806 |
| 59 | [MudCosmetologist/Autocad-Software](https://github.com/MudCosmetologist/Autocad-Software) | +7 | 1197 |
| 60 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +7 | 33245 |
| 61 | [AgnesAI-Labs/AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | +7 | 5017 |
| 62 | [bryllim/workout-guide](https://github.com/bryllim/workout-guide) | +7 | 1003 |
| 63 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +7 | 2773 |
| 64 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +7 | 9663 |
| 65 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +6 | 22129 |
| 66 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 64267 |
| 67 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +6 | 32056 |
| 68 | [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) | +6 | 1066 |
| 69 | [plannotator/effective-html](https://github.com/plannotator/effective-html) | +6 | 2705 |
| 70 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +6 | 2408 |
| 71 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +6 | 3434 |
| 72 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +6 | 14490 |
| 73 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +6 | 50198 |
| 74 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 26415 |
| 75 | [missuo/kumone](https://github.com/missuo/kumone) | +6 | 857 |
| 76 | [yetone/cumora](https://github.com/yetone/cumora) | +5 | 3247 |
| 77 | [agentconnect-md/agentconnect](https://github.com/agentconnect-md/agentconnect) | +5 | 743 |
| 78 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +5 | 15448 |
| 79 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | +5 | 660 |
| 80 | [LilMGenius/paperthin](https://github.com/LilMGenius/paperthin) | +5 | 907 |
| 81 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +5 | 5473 |
| 82 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +5 | 22784 |
| 83 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 10475 |
| 84 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +5 | 6770 |
| 85 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +5 | 2714 |
| 86 | [PoltergeistGunsmith/Portfolio-Rebalancer](https://github.com/PoltergeistGunsmith/Portfolio-Rebalancer) | +5 | 717 |
| 87 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +5 | 6515 |
| 88 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +5 | 31618 |
| 89 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +5 | 6433 |
| 90 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +4 | 28654 |
| 91 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +4 | 19048 |
| 92 | [daimon3332/address](https://github.com/daimon3332/address) | +4 | 1544 |
| 93 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +4 | 3770 |
| 94 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | +4 | 8223 |
| 95 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +4 | 37846 |
| 96 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +4 | 34658 |
| 97 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +4 | 2329 |
| 98 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +4 | 7372 |
| 99 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +4 | 2643 |
| 100 | [zeenie-ai/OpenCompany](https://github.com/zeenie-ai/OpenCompany) | +4 | 786 |
| 101 | [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) | +4 | 8104 |
| 102 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 15784 |
| 103 | [KatrielMoses/MailAccess](https://github.com/KatrielMoses/MailAccess) | +4 | 1099 |
| 104 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4 | 48599 |
| 105 | [block/buzz](https://github.com/block/buzz) | +3 | 31429 |
| 106 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +3 | 17230 |
| 107 | [haoruilee/awesome-agent-native-services](https://github.com/haoruilee/awesome-agent-native-services) | +3 | 319 |
| 108 | [cdxiaodong/cain-agent](https://github.com/cdxiaodong/cain-agent) | +3 | 444 |
| 109 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | +3 | 722 |
| 110 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +3 | 3735 |
| 111 | [microsoft/AutoSaddler](https://github.com/microsoft/AutoSaddler) | +3 | 145 |
| 112 | [harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science) | +3 | 374 |
| 113 | [securo-finance/securo](https://github.com/securo-finance/securo) | +3 | 2603 |
| 114 | [framepipe-dev/media-inference-worker](https://github.com/framepipe-dev/media-inference-worker) | +3 | 227 |
| 115 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 24747 |
| 116 | [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) | +3 | 479 |
| 117 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +3 | 7019 |
| 118 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +3 | 10977 |
| 119 | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | +3 | 745 |
| 120 | [NoizAI/HelixWorld](https://github.com/NoizAI/HelixWorld) | +3 | 294 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +263 | 19048 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +168 | 19195 |
| 3 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +147 | 30863 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +133 | 28569 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +128 | 56769 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +115 | 27019 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +105 | 30400 |
| 8 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +101 | 21839 |
| 9 | [block/buzz](https://github.com/block/buzz) | +96 | 31429 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +91 | 19238 |
| 11 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +80 | 43364 |
| 12 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +78 | 33415 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +77 | 22697 |
| 14 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +72 | 25042 |
| 15 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +71 | 33406 |
| 16 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +69 | 12538 |
| 17 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +68 | 25564 |
| 18 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +67 | 22306 |
| 19 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +67 | 25157 |
| 20 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6395 |
| 21 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | +65 | 6718 |
| 22 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11400 |
| 23 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +63 | 16885 |
| 24 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9365 |
| 25 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +60 | 11246 |
| 26 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +59 | 13538 |
| 27 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +58 | 38071 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +58 | 50198 |
| 29 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21891 |
| 30 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +54 | 16951 |
| 31 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +52 | 34743 |
| 32 | [yc-software/qm](https://github.com/yc-software/qm) | +49 | 14331 |
| 33 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +48 | 13480 |
| 34 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +48 | 28293 |
| 35 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +47 | 54024 |
| 36 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +47 | 7400 |
| 37 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 38788 |
| 38 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +44 | 8818 |
| 39 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +44 | 34289 |
| 40 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +44 | 1407 |
| 41 | [google/skills](https://github.com/google/skills) | +44 | 18970 |
| 42 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +41 | 17632 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +41 | 64267 |
| 44 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +40 | 12533 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +39 | 50951 |
| 46 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +39 | 37846 |
| 47 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +38 | 9590 |
| 48 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +38 | 37806 |
| 49 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +38 | 4567 |
| 50 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +38 | 35240 |
| 51 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +37 | 4860 |
| 52 | [every-app/open-seo](https://github.com/every-app/open-seo) | +37 | 14610 |
| 53 | [trycompai/crm](https://github.com/trycompai/crm) | +37 | 9098 |
| 54 | [multica-ai/multica](https://github.com/multica-ai/multica) | +35 | 48234 |
| 55 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +33 | 20973 |
| 56 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +33 | 6453 |
| 57 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +33 | 21624 |
| 58 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +33 | 29498 |
| 59 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +32 | 26415 |
| 60 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +32 | 22411 |
| 61 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +32 | 16462 |
| 62 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +31 | 9663 |
| 63 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +31 | 15818 |
| 64 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 10722 |
| 65 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +30 | 22187 |
| 66 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +30 | 5126 |
| 67 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 46071 |
| 68 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +30 | 32056 |
| 69 | [get-bb/bb](https://github.com/get-bb/bb) | +30 | 2754 |
| 70 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +29 | 13452 |
| 71 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +29 | 5066 |
| 72 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +29 | 24747 |
| 73 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +28 | 14456 |
| 74 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +28 | 4966 |
| 75 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +28 | 41098 |
| 76 | [spinabot/brigade](https://github.com/spinabot/brigade) | +28 | 3152 |
| 77 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +27 | 37891 |
| 78 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +27 | 14314 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 30999 |
| 80 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +27 | 6670 |
| 81 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +27 | 6747 |
| 82 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +26 | 3434 |
| 83 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +26 | 11027 |
| 84 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +26 | 2869 |
| 85 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5284 |
| 86 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +25 | 14490 |
| 87 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | +24 | 32412 |
| 88 | [t8y2/dbx](https://github.com/t8y2/dbx) | +24 | 17406 |
| 89 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +24 | 43071 |
| 90 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 91 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 39813 |
| 92 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +23 | 25217 |
| 93 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +22 | 14347 |
| 94 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +22 | 31618 |
| 95 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +22 | 34658 |
| 96 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +22 | 33353 |
| 97 | [cursor/plugins](https://github.com/cursor/plugins) | +21 | 6158 |
| 98 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +21 | 34495 |
| 99 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2691 |
| 100 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3819 |
| 101 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +20 | 7372 |
| 102 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +20 | 3016 |
| 103 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +19 | 21659 |
| 105 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1877 |
| 106 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +18 | 5473 |
| 107 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +18 | 6433 |
| 108 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +18 | 11959 |
| 109 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 6770 |
| 110 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 24135 |
| 111 | [browser-use/video-use](https://github.com/browser-use/video-use) | +18 | 21571 |
| 112 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +17 | 5582 |
| 113 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 48599 |
| 114 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 15784 |
| 115 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +17 | 9811 |
| 116 | [yetone/cumora](https://github.com/yetone/cumora) | +16 | 3247 |
| 117 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +16 | 2930 |
| 118 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 44177 |
| 119 | [securo-finance/securo](https://github.com/securo-finance/securo) | +16 | 2603 |
| 120 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1225 |
| 121 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +16 | 6824 |
| 122 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +16 | 2408 |
| 123 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3797 |
| 124 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +15 | 3010 |
| 125 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +15 | 2107 |
| 126 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 866 |
| 127 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 913 |
| 128 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9482 |
| 129 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30947 |
| 130 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +14 | 31667 |
| 131 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +14 | 1983 |
| 132 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +14 | 3375 |
| 133 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +14 | 3273 |
| 134 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +14 | 2773 |
| 135 | [cinderline/northcinder](https://github.com/cinderline/northcinder) | +14 | 1218 |
| 136 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2756 |
| 137 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10816 |
| 138 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +13 | 35374 |
| 139 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +13 | 3949 |
| 140 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +13 | 9209 |
| 141 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9784 |
| 142 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +13 | 8781 |
| 143 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +13 | 2980 |
| 144 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2240 |
| 145 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 146 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +12 | 999 |
| 147 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3979 |
| 148 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +12 | 5809 |
| 149 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +12 | 1651 |
| 150 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2890 |
| 151 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1447 |
| 152 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +12 | 4200 |
| 153 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +12 | 4520 |
| 154 | [decolua/9router](https://github.com/decolua/9router) | +12 | 26631 |
| 155 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +12 | 593 |
| 156 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28356 |
| 157 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +11 | 2668 |
| 158 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +11 | 9173 |
| 159 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +11 | 2643 |
| 160 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6273 |
| 161 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +11 | 14016 |
| 162 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 6446 |
| 163 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +11 | 2027 |
| 164 | [petergyang/human-review](https://github.com/petergyang/human-review) | +11 | 1186 |
| 165 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +10 | 903 |
| 166 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +10 | 45648 |
| 167 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14818 |
| 168 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4875 |
| 169 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3097 |
| 170 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +10 | 1076 |
| 171 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2462 |
| 172 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1594 |
| 173 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +10 | 32535 |
| 174 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 3731 |
| 175 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +9 | 0 |
| 176 | [jundot/omlx](https://github.com/jundot/omlx) | +9 | 20956 |
| 177 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 10977 |
| 178 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1959 |
| 179 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6499 |
| 180 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +9 | 24857 |
| 181 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +9 | 6149 |
| 182 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +9 | 6642 |
| 183 | [memorax-ai/memorax-code](https://github.com/memorax-ai/memorax-code) | +9 | 1125 |
| 184 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8888 |
| 185 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +8 | 17230 |
| 186 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +8 | 701 |
| 187 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6677 |
| 188 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 7209 |
| 189 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +8 | 3770 |
| 190 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +8 | 933 |
| 191 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +8 | 2036 |
| 192 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +7 | 7019 |
| 193 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1273 |
| 194 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +7 | 9981 |
| 195 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27725 |
| 196 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 197 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 198 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1714 |
| 199 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +6 | 1119 |
| 200 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +6 | 1804 |
| 201 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1420 |
| 202 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 10339 |
| 203 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +6 | 7200 |
| 204 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +6 | 10730 |
| 205 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +6 | 733 |
| 206 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 286 |
| 207 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +6 | 3735 |
| 208 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 362 |
| 209 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 515 |
| 210 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +6 | 1504 |
| 211 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3929 |
| 212 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +6 | 28053 |
| 213 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +5 | 1456 |
| 214 | [zarazhangrui/youtube-digest](https://github.com/zarazhangrui/youtube-digest) | +5 | 964 |
| 215 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3166 |
| 216 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1599 |
| 217 | [openai/plugins](https://github.com/openai/plugins) | +5 | 5270 |
| 218 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 219 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 863 |
| 220 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +5 | 366 |
| 221 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 601 |
| 222 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 3639 |
| 223 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +4 | 476 |
| 224 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +4 | 690 |
| 225 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 790 |
| 226 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +4 | 5711 |
| 227 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 634 |
| 228 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2290 |
| 229 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +4 | 184 |
| 230 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5911 |
| 231 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +4 | 639 |
| 232 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 832 |
| 233 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +4 | 3201 |
| 234 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3161 |
| 235 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1280 |
| 236 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +4 | 14194 |
| 237 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 269 |
| 238 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 577 |
| 239 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5176 |
| 240 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5307 |
| 241 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3599 |
| 242 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1257 |
| 243 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 169 |
| 244 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 2188 |
| 245 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 1001 |
| 246 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +4 | 26471 |
| 247 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 305 |
| 248 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 305 |
| 249 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1276 |
| 250 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +3 | 128 |
| 251 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +3 | 6422 |
| 252 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 211 |
| 253 | [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | +3 | 163 |
| 254 | [GamePhanes/GamePhanes](https://github.com/GamePhanes/GamePhanes) | +3 | 540 |
| 255 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6031 |
| 256 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 913 |
| 257 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6208 |
| 258 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12504 |
| 259 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9824 |
| 260 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 658 |
| 261 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1797 |
| 262 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 1022 |
| 263 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 640 |
| 264 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1288 |
| 265 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4919 |
| 266 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 253 |
| 267 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 1009 |
| 268 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 615 |
| 269 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 347 |
| 270 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28857 |
| 271 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 272 | [crimera/piko](https://github.com/crimera/piko) | +3 | 4964 |
| 273 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2593 |
| 274 | [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills) | +2 | 150 |
| 275 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +2 | 446 |
| 276 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 608 |
| 277 | [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) | +2 | 1804 |
| 278 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 751 |
| 279 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 147 |
| 280 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 281 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 88 |
| 282 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 551 |
| 283 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 126 |
| 284 | [YesSteveModel/YesSteveModel](https://github.com/YesSteveModel/YesSteveModel) | +2 | 32 |
| 285 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 214 |
| 286 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2579 |
| 287 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3805 |
| 288 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1058 |
| 289 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 680 |
| 290 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 300 |
| 291 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 228 |
| 292 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1253 |
| 293 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1413 |
| 294 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 529 |
| 295 | [youdidking/stanngv2](https://github.com/youdidking/stanngv2) | +1 | 384 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 923 |
| 297 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 184 |
| 298 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1376 |
| 299 | [OpenVapeCN/VapeV4.21](https://github.com/OpenVapeCN/VapeV4.21) | +1 | 164 |
| 300 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +1 | 5345 |
