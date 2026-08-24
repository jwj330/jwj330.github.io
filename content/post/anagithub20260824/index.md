---
title: "2026-08-24 GitHub增长趋势报告"
description: "1.vorssaint-utils+6 2.book-to-skill+3 3.FreeToken+3 4.unlazy+3 5.OpenLogi+2"
date: 2026-08-24T20:31:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-24 20:31:45

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
        'daily': {"categories": ["ArcReel/ArcReel", "AgIzT/NovelAI-Tag", "jd-opensource/JoyAI-Video-Edit", "AstrBotDevs/AstrBot-desktop", "anywhere-labs/deepseek-harness-desktop", "tjboudreaux/cc-thinking-skills", "guillaumemeyer/watermarks-remover", "dnshe/DNSHE-FreeDomains", "cactus-compute/needle", "tinyhumansai/openhuman", "cathrynlavery/diagram-design", "Alishahryar1/free-claude-code", "mukul975/Anthropic-Cybersecurity-Skills", "petergyang/no-ai-slop", "stablyai/orca", "AprilNEA/OpenLogi", "Leonxlnx/unlazy", "FlashML-org/FreeToken", "virgiliojr94/book-to-skill", "vorssaint/vorssaint-utils"], "data": [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 6]},
        'weekly': {"categories": ["ifixai-ai/iFixAi", "tt-a1i/archify", "FlashML-org/FreeToken", "zhu1090093659/dsh-web-ui", "zhaoxuya520/reverse-skill", "pathwaycom/arc-task-gen", "holaboss-ai/holaOS", "mukul975/Anthropic-Cybersecurity-Skills", "walkinglabs/learn-harness-engineering", "Tiger3807861189/J-Space-Cognition-Suite-V3.7", "akitaonrails/ai-memory", "General-Legal/legal-templates", "virgiliojr94/book-to-skill", "AprilNEA/OpenLogi", "stablyai/orca", "volcengine/OpenViking", "awesome-dsh-plugin/awesome-dsh-plugin", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 19, 19, 19, 28, 29, 30, 32, 35, 41, 53]},
        'monthly': {"categories": ["firecrawl/pdf-inspector", "k1tbyte/Wand-Enhancer", "TencentCloud/TencentDB-Agent-Memory", "ifixai-ai/iFixAi", "brightdata/cli", "emilkowalski/skills", "andrewyng/openworker", "herdrdev/herdr", "floci-io/floci", "ayghri/i-have-adhd", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "bojieli/ai-agent-book", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz", "cathrynlavery/diagram-design", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [61, 64, 65, 65, 66, 71, 73, 76, 78, 78, 82, 84, 89, 100, 112, 119, 122, 124, 163, 259]}
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
| 1 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +6 | 10601 |
| 2 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 25175 |
| 3 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +3 | 5028 |
| 4 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +3 | 2203 |
| 5 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +2 | 15757 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +2 | 52759 |
| 7 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +2 | 5909 |
| 8 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +2 | 30973 |
| 9 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2 | 48834 |
| 10 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2 | 26294 |
| 11 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2 | 37186 |
| 12 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 8931 |
| 13 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 12833 |
| 14 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +2 | 17864 |
| 15 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +2 | 1185 |
| 16 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +2 | 19648 |
| 17 | [AstrBotDevs/AstrBot-desktop](https://github.com/AstrBotDevs/AstrBot-desktop) | +1 | 761 |
| 18 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +1 | 1647 |
| 19 | [AgIzT/NovelAI-Tag](https://github.com/AgIzT/NovelAI-Tag) | +1 | 41 |
| 20 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +1 | 4153 |
| 21 | [RealDeco/SendspinZero](https://github.com/RealDeco/SendspinZero) | +1 | 572 |
| 22 | [shiaho777/web-to-app](https://github.com/shiaho777/web-to-app) | +1 | 5820 |
| 23 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1 | 13219 |
| 24 | [anbeime/skill](https://github.com/anbeime/skill) | +1 | 5722 |
| 25 | [byJoey/cfnew](https://github.com/byJoey/cfnew) | +1 | 15079 |
| 26 | [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) | +1 | 854 |
| 27 | [shawnla90/gtm-coding-agent](https://github.com/shawnla90/gtm-coding-agent) | +1 | 135 |
| 28 | [St0ff3l/fileterm](https://github.com/St0ff3l/fileterm) | +1 | 267 |
| 29 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +1 | 23787 |
| 30 | [ra1nyxin/tentacle-monster-roleplay-esp32](https://github.com/ra1nyxin/tentacle-monster-roleplay-esp32) | +1 | 522 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +53 | 19648 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +41 | 26294 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +35 | 17864 |
| 4 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +32 | 12245 |
| 5 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +30 | 32933 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +29 | 52759 |
| 7 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +28 | 15757 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +19 | 25175 |
| 9 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1746 |
| 10 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +19 | 4380 |
| 11 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +18 | 3011 |
| 12 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +17 | 14013 |
| 13 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +17 | 30973 |
| 14 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +17 | 10750 |
| 15 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +16 | 5481 |
| 16 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +16 | 28664 |
| 17 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +16 | 5909 |
| 18 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +15 | 5028 |
| 19 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +15 | 15324 |
| 20 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +15 | 11258 |
| 21 | [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | +15 | 6760 |
| 22 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +14 | 3578 |
| 23 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +14 | 10601 |
| 24 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +14 | 13219 |
| 25 | [block/buzz](https://github.com/block/buzz) | +14 | 30451 |
| 26 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +14 | 48834 |
| 27 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 23787 |
| 28 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +14 | 41738 |
| 29 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +13 | 39194 |
| 30 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +13 | 4077 |
| 31 | [blader/humanizer](https://github.com/blader/humanizer) | +13 | 37615 |
| 32 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +13 | 20336 |
| 33 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +12 | 15384 |
| 34 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +12 | 1594 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +12 | 27127 |
| 36 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 50064 |
| 37 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +12 | 2791 |
| 38 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +11 | 33845 |
| 39 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 49032 |
| 40 | [yetone/cumora](https://github.com/yetone/cumora) | +11 | 3030 |
| 41 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +11 | 4757 |
| 42 | [cursor/plugins](https://github.com/cursor/plugins) | +10 | 4951 |
| 43 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +10 | 32047 |
| 44 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +10 | 13372 |
| 45 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +10 | 7221 |
| 46 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +10 | 32118 |
| 47 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +10 | 45467 |
| 48 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +10 | 24799 |
| 49 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +9 | 2203 |
| 50 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +9 | 20332 |
| 51 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +9 | 18253 |
| 52 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +9 | 8931 |
| 53 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1755 |
| 54 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 12833 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 36862 |
| 56 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +8 | 5909 |
| 57 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 12000 |
| 58 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +7 | 1532 |
| 59 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +7 | 1491 |
| 60 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +7 | 601 |
| 61 | [jundot/omlx](https://github.com/jundot/omlx) | +7 | 20534 |
| 62 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +7 | 40361 |
| 63 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +7 | 37388 |
| 64 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +7 | 3661 |
| 65 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +7 | 2133 |
| 66 | [titanwings/distilly](https://github.com/titanwings/distilly) | +7 | 23912 |
| 67 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +7 | 18133 |
| 68 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +7 | 4416 |
| 69 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +6 | 21036 |
| 70 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +6 | 33911 |
| 71 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +6 | 1414 |
| 72 | [floci-io/floci](https://github.com/floci-io/floci) | +6 | 21905 |
| 73 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +6 | 1546 |
| 74 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +6 | 683 |
| 75 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +6 | 16620 |
| 76 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +6 | 11562 |
| 77 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +6 | 4529 |
| 78 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +6 | 941 |
| 79 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +6 | 7570 |
| 80 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 42452 |
| 81 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 9203 |
| 82 | [macro-inc/macro](https://github.com/macro-inc/macro) | +6 | 4017 |
| 83 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 16140 |
| 84 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +6 | 1901 |
| 85 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +6 | 6329 |
| 86 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47502 |
| 87 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 13305 |
| 88 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +6 | 433 |
| 89 | [iAmCorey/Wake](https://github.com/iAmCorey/Wake) | +6 | 585 |
| 90 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +6 | 16345 |
| 91 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +5 | 6044 |
| 92 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +5 | 3101 |
| 93 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +5 | 901 |
| 94 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +5 | 41254 |
| 95 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +5 | 1958 |
| 96 | [nuyoah-ai-works/nuyoah-xiezhen-prompt](https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt) | +5 | 420 |
| 97 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +5 | 6115 |
| 98 | [dob323/session-kit](https://github.com/dob323/session-kit) | +5 | 661 |
| 99 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +5 | 6579 |
| 100 | [securo-finance/securo](https://github.com/securo-finance/securo) | +5 | 2202 |
| 101 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +5 | 9184 |
| 102 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +4 | 659 |
| 103 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +4 | 593 |
| 104 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 4664 |
| 105 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +4 | 5528 |
| 106 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 484 |
| 107 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +4 | 575 |
| 108 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +4 | 1675 |
| 109 | [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | +4 | 4042 |
| 110 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +4 | 815 |
| 111 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 31292 |
| 112 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +4 | 14658 |
| 113 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10836 |
| 114 | [powerycy/BossHunter](https://github.com/powerycy/BossHunter) | +3 | 466 |
| 115 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +3 | 45341 |
| 116 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +3 | 526 |
| 117 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 12394 |
| 118 | [Leutenegger/vanity-eth](https://github.com/Leutenegger/vanity-eth) | +3 | 0 |
| 119 | [Audio8-AI/Audio8_TTS](https://github.com/Audio8-AI/Audio8_TTS) | +3 | 865 |
| 120 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +3 | 411 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +259 | 18133 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +163 | 18253 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +124 | 26294 |
| 4 | [block/buzz](https://github.com/block/buzz) | +122 | 30451 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +119 | 52759 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +112 | 25175 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +100 | 28664 |
| 8 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +89 | 41738 |
| 9 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +84 | 19648 |
| 10 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +82 | 17864 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +78 | 23787 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +78 | 21905 |
| 13 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +76 | 32047 |
| 14 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +73 | 14999 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +71 | 32118 |
| 16 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6416 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +65 | 11258 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +65 | 24236 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +64 | 20336 |
| 20 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +61 | 16620 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +61 | 49032 |
| 22 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 9104 |
| 23 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +57 | 10649 |
| 24 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21679 |
| 25 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +53 | 12245 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +52 | 15324 |
| 27 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +48 | 12000 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14154 |
| 29 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 6943 |
| 30 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +45 | 27127 |
| 31 | [blader/humanizer](https://github.com/blader/humanizer) | +44 | 37615 |
| 32 | [google/skills](https://github.com/google/skills) | +44 | 18657 |
| 33 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +44 | 21327 |
| 34 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +43 | 33912 |
| 35 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +43 | 37388 |
| 36 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +43 | 13372 |
| 37 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1457 |
| 38 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +43 | 16140 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 63776 |
| 40 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +39 | 13219 |
| 41 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +39 | 35117 |
| 42 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8609 |
| 43 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +38 | 32933 |
| 44 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +38 | 29157 |
| 45 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +37 | 26070 |
| 46 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +37 | 34404 |
| 47 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +36 | 20332 |
| 48 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +36 | 50064 |
| 49 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 13305 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8883 |
| 51 | [openai/codex-security](https://github.com/openai/codex-security) | +36 | 10142 |
| 52 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 4329 |
| 53 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +35 | 6236 |
| 54 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +35 | 24476 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 36862 |
| 56 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +34 | 42452 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 45467 |
| 58 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +32 | 15757 |
| 59 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +32 | 40361 |
| 60 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +31 | 10602 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +31 | 47502 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 10454 |
| 63 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +31 | 31647 |
| 64 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +30 | 5481 |
| 65 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +30 | 18438 |
| 66 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +30 | 6587 |
| 67 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +29 | 5909 |
| 68 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 15560 |
| 69 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 22233 |
| 70 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +28 | 48834 |
| 71 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +28 | 8931 |
| 72 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4707 |
| 73 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2607 |
| 74 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +28 | 3350 |
| 75 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 30778 |
| 76 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +27 | 4416 |
| 77 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3099 |
| 78 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +26 | 39194 |
| 79 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5073 |
| 80 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 23000 |
| 81 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +26 | 12833 |
| 82 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +25 | 10750 |
| 83 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 787 |
| 84 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +24 | 48208 |
| 85 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24906 |
| 86 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9176 |
| 87 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 88 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4154 |
| 89 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +23 | 15384 |
| 90 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +23 | 4381 |
| 91 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +23 | 14013 |
| 92 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +23 | 5909 |
| 93 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +22 | 9203 |
| 94 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +22 | 33014 |
| 95 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +21 | 2688 |
| 96 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3578 |
| 97 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 98 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +19 | 3011 |
| 99 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +19 | 30974 |
| 100 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1746 |
| 101 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +19 | 7221 |
| 102 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +18 | 21036 |
| 103 | [titanwings/distilly](https://github.com/titanwings/distilly) | +18 | 23912 |
| 104 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +17 | 5028 |
| 105 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +17 | 11562 |
| 106 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 6467 |
| 107 | [browser-use/video-use](https://github.com/browser-use/video-use) | +17 | 21320 |
| 108 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +16 | 6975 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +16 | 14982 |
| 110 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1219 |
| 111 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3744 |
| 112 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +16 | 8550 |
| 113 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 803 |
| 114 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +15 | 43563 |
| 115 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +15 | 13847 |
| 116 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5342 |
| 117 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3350 |
| 118 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +14 | 48061 |
| 119 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30757 |
| 120 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 2018 |
| 121 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9234 |
| 122 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +14 | 4077 |
| 123 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2513 |
| 124 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +13 | 2791 |
| 125 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +13 | 7570 |
| 126 | [securo-finance/securo](https://github.com/securo-finance/securo) | +13 | 2202 |
| 127 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3218 |
| 128 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9582 |
| 129 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +13 | 6116 |
| 130 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +13 | 32256 |
| 131 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 132 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2213 |
| 133 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +13 | 10477 |
| 134 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3984 |
| 135 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3661 |
| 136 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 889 |
| 137 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +12 | 8838 |
| 138 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 31292 |
| 139 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1812 |
| 140 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1452 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +12 | 3029 |
| 142 | [decolua/9router](https://github.com/decolua/9router) | +12 | 26221 |
| 143 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28064 |
| 144 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 0 |
| 145 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +11 | 14658 |
| 146 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1539 |
| 147 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6211 |
| 148 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 6105 |
| 149 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 8904 |
| 150 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2748 |
| 151 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47350 |
| 152 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +11 | 2203 |
| 153 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +11 | 2852 |
| 154 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 495 |
| 155 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6329 |
| 156 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4664 |
| 157 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 3020 |
| 158 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 34277 |
| 159 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2468 |
| 160 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +10 | 1971 |
| 161 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1146 |
| 162 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +10 | 8659 |
| 163 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1958 |
| 164 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1755 |
| 165 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +9 | 5528 |
| 166 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45341 |
| 167 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1111 |
| 168 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1127 |
| 169 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 11781 |
| 170 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10813 |
| 171 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1647 |
| 172 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 396 |
| 173 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 576 |
| 174 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +9 | 1675 |
| 175 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1065 |
| 176 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +9 | 1532 |
| 177 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1987 |
| 178 | [jundot/omlx](https://github.com/jundot/omlx) | +8 | 20534 |
| 179 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1840 |
| 180 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9184 |
| 181 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24660 |
| 182 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +8 | 6579 |
| 183 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +8 | 6207 |
| 184 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3468 |
| 185 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3704 |
| 186 | [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit) | +7 | 1098 |
| 187 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27609 |
| 188 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 189 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1533 |
| 190 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 6946 |
| 191 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 192 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +6 | 1185 |
| 193 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1533 |
| 194 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 279 |
| 195 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 341 |
| 196 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 501 |
| 197 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +6 | 14083 |
| 198 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3897 |
| 199 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +6 | 28028 |
| 200 | [aklivity/zilla](https://github.com/aklivity/zilla) | +6 | 1712 |
| 201 | [dob323/session-kit](https://github.com/dob323/session-kit) | +5 | 661 |
| 202 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3128 |
| 203 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1576 |
| 204 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 882 |
| 205 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +5 | 1289 |
| 206 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +5 | 9878 |
| 207 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 653 |
| 208 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 10218 |
| 209 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 210 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 842 |
| 211 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3449 |
| 212 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 1123 |
| 213 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +5 | 26344 |
| 214 | [FongMi/TV](https://github.com/FongMi/TV) | +5 | 9204 |
| 215 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 668 |
| 216 | [QwenAudio/qwen-audio-agent](https://github.com/QwenAudio/qwen-audio-agent) | +4 | 2231 |
| 217 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1411 |
| 218 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +4 | 631 |
| 219 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5822 |
| 220 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 784 |
| 221 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3043 |
| 222 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1244 |
| 223 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +4 | 6975 |
| 224 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +4 | 3224 |
| 225 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 249 |
| 226 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10638 |
| 227 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7299 |
| 228 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 544 |
| 229 | [penecho/penecho](https://github.com/penecho/penecho) | +4 | 2126 |
| 230 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5004 |
| 231 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5262 |
| 232 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8845 |
| 233 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 657 |
| 234 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3560 |
| 235 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5198 |
| 236 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1209 |
| 237 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +4 | 321 |
| 238 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 118 |
| 239 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 961 |
| 240 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4856 |
| 241 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 286 |
| 242 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 203 |
| 243 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3543 |
| 244 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6023 |
| 245 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 6025 |
| 246 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +3 | 309 |
| 247 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 865 |
| 248 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +3 | 1231 |
| 249 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +3 | 5621 |
| 250 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 266 |
| 251 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 338 |
| 252 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 168 |
| 253 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 610 |
| 254 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 646 |
| 255 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1759 |
| 256 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +3 | 1409 |
| 257 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8996 |
| 258 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 880 |
| 259 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 208 |
| 260 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 3056 |
| 261 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1650 |
| 262 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 193 |
| 263 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 405 |
| 264 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 246 |
| 265 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9698 |
| 266 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9725 |
| 267 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4905 |
| 268 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 973 |
| 269 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 222 |
| 270 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 583 |
| 271 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 336 |
| 272 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1252 |
| 273 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2124 |
| 274 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28719 |
| 275 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2583 |
| 276 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 402 |
| 277 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +2 | 138 |
| 278 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 746 |
| 279 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 280 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 512 |
| 281 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 122 |
| 282 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3756 |
| 283 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1039 |
| 284 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 264 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 371 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2911 |
| 287 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5248 |
| 288 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 220 |
| 289 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1242 |
| 290 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1412 |
| 291 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 520 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 293 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 264 |
| 294 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 138 |
| 295 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 908 |
| 296 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1344 |
| 297 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 172 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 962 |
| 299 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +1 | 3085 |
| 300 | [TensorHub-ORG/Coomi-Android](https://github.com/TensorHub-ORG/Coomi-Android) | +1 | 100 |
