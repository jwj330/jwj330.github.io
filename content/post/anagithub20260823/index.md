---
title: "2026-08-23 GitHub增长趋势报告"
description: "1.vorssaint-utils+3 2.book-to-skill+3 3.anydoc+2 4.colibri+2 5.bookorbit+2"
date: 2026-08-23T20:24:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-23 20:24:19

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
        'daily': {"categories": ["backnotprop/plannotator", "jlcodes99/cockpit-tools", "HarnessRouter/harnessrouter", "axoviq-ai/synthadoc", "AnmolSaini16/mapcn", "kaishi00/hermes-conduit", "HiThink-Tech/Financial-API", "MadsLorentzen/ai-job-search", "Steel-Foundation/SteelMC", "SHAdd0WTAka/Zen-Ai-Pentest", "lance0/ttl", "cosmicstack-labs/mercury-agent-skills", "awesome-dsh-plugin/awesome-dsh-plugin", "Untrivial-ai/agent-orchestrator", "cactus-compute/needle", "bookorbit/bookorbit", "JustVugg/colibri", "firecrawl/anydoc", "virgiliojr94/book-to-skill", "vorssaint/vorssaint-utils"], "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3]},
        'weekly': {"categories": ["mukul975/Anthropic-Cybersecurity-Skills", "zhaoxuya520/reverse-skill", "ifixai-ai/iFixAi", "arvin341az-glitch/RVG", "bojieli/ai-agent-book", "walkinglabs/learn-harness-engineering", "zhu1090093659/dsh-web-ui", "virgiliojr94/book-to-skill", "holaboss-ai/holaOS", "pathwaycom/arc-task-gen", "Tiger3807861189/J-Space-Cognition-Suite-V3.7", "akitaonrails/ai-memory", "General-Legal/legal-templates", "volcengine/OpenViking", "AprilNEA/OpenLogi", "stablyai/orca", "guillaumemeyer/watermarks-remover", "awesome-dsh-plugin/awesome-dsh-plugin", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [15, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 19, 26, 26, 27, 34, 36, 41, 58]},
        'monthly': {"categories": ["firecrawl/pdf-inspector", "k1tbyte/Wand-Enhancer", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "ifixai-ai/iFixAi", "emilkowalski/skills", "floci-io/floci", "herdrdev/herdr", "guillaumemeyer/watermarks-remover", "ayghri/i-have-adhd", "anywhere-labs/deepseek-harness-desktop", "andrewyng/openworker", "bojieli/ai-agent-book", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "stablyai/orca", "cathrynlavery/diagram-design", "block/buzz", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [61, 63, 65, 66, 69, 72, 77, 78, 80, 82, 82, 83, 94, 99, 109, 121, 122, 134, 163, 259]}
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
| 1 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +3 | 8451 |
| 2 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 24549 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +2 | 18056 |
| 4 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 25958 |
| 5 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +2 | 3032 |
| 6 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 8728 |
| 7 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +2 | 9897 |
| 8 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +2 | 11858 |
| 9 | [cosmicstack-labs/mercury-agent-skills](https://github.com/cosmicstack-labs/mercury-agent-skills) | +1 | 423 |
| 10 | [lance0/ttl](https://github.com/lance0/ttl) | +1 | 1441 |
| 11 | [SHAdd0WTAka/Zen-Ai-Pentest](https://github.com/SHAdd0WTAka/Zen-Ai-Pentest) | +1 | 440 |
| 12 | [Steel-Foundation/SteelMC](https://github.com/Steel-Foundation/SteelMC) | +1 | 543 |
| 13 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +1 | 33154 |
| 14 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +1 | 1368 |
| 15 | [kaishi00/hermes-conduit](https://github.com/kaishi00/hermes-conduit) | +1 | 72 |
| 16 | [AnmolSaini16/mapcn](https://github.com/AnmolSaini16/mapcn) | +1 | 11814 |
| 17 | [axoviq-ai/synthadoc](https://github.com/axoviq-ai/synthadoc) | +1 | 1116 |
| 18 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +1 | 528 |
| 19 | [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | +1 | 16379 |
| 20 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | +1 | 7971 |
| 21 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1 | 36678 |
| 22 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +1 | 14798 |
| 23 | [google-research/envharness](https://github.com/google-research/envharness) | +1 | 274 |
| 24 | [croffasia/itsaplan](https://github.com/croffasia/itsaplan) | +1 | 273 |
| 25 | [activeloopai/hivemind](https://github.com/activeloopai/hivemind) | +1 | 1580 |
| 26 | [Kodiqa-Solutions/VaultS3](https://github.com/Kodiqa-Solutions/VaultS3) | +1 | 1345 |
| 27 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1 | 12937 |
| 28 | [chirpz-ai/pandaprobe](https://github.com/chirpz-ai/pandaprobe) | +1 | 774 |
| 29 | [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) | +1 | 364 |
| 30 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +1 | 12364 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +58 | 18903 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +41 | 25803 |
| 3 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +36 | 11858 |
| 4 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +34 | 17391 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 51740 |
| 6 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +26 | 14798 |
| 7 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +26 | 32440 |
| 8 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1728 |
| 9 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +19 | 4216 |
| 10 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +19 | 3015 |
| 11 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +18 | 4951 |
| 12 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +18 | 10716 |
| 13 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +17 | 24551 |
| 14 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +17 | 5737 |
| 15 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +16 | 13873 |
| 16 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +16 | 41170 |
| 17 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +15 | 3503 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +15 | 11258 |
| 19 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +15 | 27782 |
| 20 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +15 | 30816 |
| 21 | [block/buzz](https://github.com/block/buzz) | +14 | 30036 |
| 22 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 23444 |
| 23 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +14 | 15144 |
| 24 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +13 | 38999 |
| 25 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +13 | 3853 |
| 26 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +13 | 12937 |
| 27 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +13 | 1368 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +13 | 48782 |
| 29 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +13 | 4564 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +12 | 47847 |
| 31 | [blader/humanizer](https://github.com/blader/humanizer) | +12 | 37381 |
| 32 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +12 | 2671 |
| 33 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +12 | 8729 |
| 34 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +11 | 33692 |
| 35 | [yetone/cumora](https://github.com/yetone/cumora) | +11 | 2941 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +11 | 26748 |
| 37 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 49759 |
| 38 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +11 | 12993 |
| 39 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +11 | 45362 |
| 40 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +11 | 20100 |
| 41 | [cursor/plugins](https://github.com/cursor/plugins) | +10 | 4804 |
| 42 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +10 | 7176 |
| 43 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +10 | 31825 |
| 44 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +10 | 24768 |
| 45 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +9 | 20166 |
| 46 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +9 | 18056 |
| 47 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +9 | 8451 |
| 48 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +9 | 31764 |
| 49 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1412 |
| 50 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 36678 |
| 51 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 11903 |
| 52 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +8 | 40138 |
| 53 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +8 | 18009 |
| 54 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +8 | 4291 |
| 55 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +7 | 1507 |
| 56 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +7 | 1403 |
| 57 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +7 | 33154 |
| 58 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +7 | 594 |
| 59 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +7 | 12631 |
| 60 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +7 | 37253 |
| 61 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +7 | 3534 |
| 62 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +7 | 2049 |
| 63 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +7 | 12697 |
| 64 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +7 | 4648 |
| 65 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +6 | 20973 |
| 66 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +6 | 1414 |
| 67 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +6 | 1462 |
| 68 | [jundot/omlx](https://github.com/jundot/omlx) | +6 | 20441 |
| 69 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +6 | 16537 |
| 70 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +6 | 11391 |
| 71 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +6 | 682 |
| 72 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +6 | 928 |
| 73 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +6 | 7515 |
| 74 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 9034 |
| 75 | [macro-inc/macro](https://github.com/macro-inc/macro) | +6 | 3994 |
| 76 | [Steel-Foundation/SteelMC](https://github.com/Steel-Foundation/SteelMC) | +6 | 543 |
| 77 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 5810 |
| 78 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +6 | 6267 |
| 79 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 16074 |
| 80 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47369 |
| 81 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 13177 |
| 82 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +6 | 384 |
| 83 | [iAmCorey/Wake](https://github.com/iAmCorey/Wake) | +6 | 534 |
| 84 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +6 | 16267 |
| 85 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 42285 |
| 86 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 32919 |
| 87 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +6 | 1905 |
| 88 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +6 | 23859 |
| 89 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +5 | 5904 |
| 90 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +5 | 3032 |
| 91 | [floci-io/floci](https://github.com/floci-io/floci) | +5 | 21385 |
| 92 | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | +5 | 1160 |
| 93 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +5 | 41196 |
| 94 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +5 | 6043 |
| 95 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +5 | 1832 |
| 96 | [nuyoah-ai-works/nuyoah-xiezhen-prompt](https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt) | +5 | 415 |
| 97 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +5 | 21232 |
| 98 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +5 | 4419 |
| 99 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 23995 |
| 100 | [securo-finance/securo](https://github.com/securo-finance/securo) | +5 | 2108 |
| 101 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +5 | 9124 |
| 102 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +5 | 528 |
| 103 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +5 | 14609 |
| 104 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +4 | 581 |
| 105 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 4648 |
| 106 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +4 | 5416 |
| 107 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +4 | 805 |
| 108 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 479 |
| 109 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +4 | 1567 |
| 110 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +4 | 6540 |
| 111 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +4 | 798 |
| 112 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 31208 |
| 113 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10791 |
| 114 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 34184 |
| 115 | [powerycy/BossHunter](https://github.com/powerycy/BossHunter) | +3 | 441 |
| 116 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +3 | 383 |
| 117 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +3 | 479 |
| 118 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +3 | 12364 |
| 119 | [Leutenegger/vanity-eth](https://github.com/Leutenegger/vanity-eth) | +3 | 0 |
| 120 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +3 | 566 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +259 | 18009 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +163 | 18056 |
| 3 | [block/buzz](https://github.com/block/buzz) | +134 | 30036 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +122 | 25803 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +121 | 51740 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +109 | 24551 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +99 | 27782 |
| 8 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +94 | 41170 |
| 9 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +83 | 14967 |
| 10 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +82 | 18903 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +82 | 23444 |
| 12 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +80 | 17391 |
| 13 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +78 | 31764 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +77 | 21385 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +72 | 31825 |
| 16 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +69 | 11258 |
| 17 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6424 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +65 | 23995 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +63 | 20100 |
| 20 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +61 | 16537 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +61 | 48782 |
| 22 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8970 |
| 23 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +57 | 10435 |
| 24 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21664 |
| 25 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +53 | 11858 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +51 | 15144 |
| 27 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +51 | 11903 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +48 | 33154 |
| 29 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14101 |
| 30 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 6807 |
| 31 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +46 | 12993 |
| 32 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +46 | 21232 |
| 33 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +46 | 12937 |
| 34 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +45 | 26748 |
| 35 | [google/skills](https://github.com/google/skills) | +45 | 18628 |
| 36 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +45 | 16074 |
| 37 | [blader/humanizer](https://github.com/blader/humanizer) | +44 | 37381 |
| 38 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +43 | 37253 |
| 39 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1448 |
| 40 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +41 | 29085 |
| 41 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +40 | 35076 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 63706 |
| 43 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +39 | 49759 |
| 44 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8588 |
| 45 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +38 | 6137 |
| 46 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +38 | 34358 |
| 47 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +37 | 25958 |
| 48 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +36 | 20166 |
| 49 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 13177 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8840 |
| 51 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +36 | 24410 |
| 52 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 4278 |
| 53 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +35 | 36678 |
| 54 | [openai/codex-security](https://github.com/openai/codex-security) | +35 | 10104 |
| 55 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +34 | 32440 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +34 | 45362 |
| 57 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 42285 |
| 58 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +33 | 40138 |
| 59 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 47369 |
| 60 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10423 |
| 61 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +31 | 18338 |
| 62 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +31 | 31549 |
| 63 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +30 | 4951 |
| 64 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +30 | 14798 |
| 65 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +30 | 30728 |
| 66 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +29 | 5737 |
| 67 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 15518 |
| 68 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 22172 |
| 69 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +29 | 6567 |
| 70 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +28 | 47848 |
| 71 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4648 |
| 72 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2574 |
| 73 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +28 | 3326 |
| 74 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +27 | 4291 |
| 75 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3088 |
| 76 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +26 | 38999 |
| 77 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +26 | 8729 |
| 78 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5044 |
| 79 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 22978 |
| 80 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +25 | 10716 |
| 81 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +25 | 8451 |
| 82 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 788 |
| 83 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +25 | 4143 |
| 84 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +24 | 47863 |
| 85 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24848 |
| 86 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9133 |
| 87 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +24 | 12697 |
| 88 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +23 | 4216 |
| 89 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 32919 |
| 90 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +23 | 5810 |
| 91 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +22 | 2689 |
| 92 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +22 | 13873 |
| 93 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +22 | 9034 |
| 94 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3503 |
| 95 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1414 |
| 96 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +20 | 41196 |
| 97 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +19 | 3015 |
| 98 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1728 |
| 99 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +19 | 7176 |
| 100 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +18 | 20973 |
| 101 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +18 | 23859 |
| 102 | [browser-use/video-use](https://github.com/browser-use/video-use) | +18 | 21287 |
| 103 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +17 | 30816 |
| 104 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +17 | 11391 |
| 105 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 6375 |
| 106 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +17 | 12631 |
| 107 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +16 | 6964 |
| 108 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47997 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +16 | 14865 |
| 110 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 43433 |
| 111 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3728 |
| 112 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +16 | 8495 |
| 113 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 793 |
| 114 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +15 | 13805 |
| 115 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5349 |
| 116 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3332 |
| 117 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30695 |
| 118 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 1994 |
| 119 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9197 |
| 120 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +14 | 3853 |
| 121 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +14 | 9544 |
| 122 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 6043 |
| 123 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2478 |
| 124 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10412 |
| 125 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +13 | 2671 |
| 126 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +13 | 7515 |
| 127 | [securo-finance/securo](https://github.com/securo-finance/securo) | +13 | 2108 |
| 128 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +13 | 8737 |
| 129 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3183 |
| 130 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26137 |
| 131 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 132 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2205 |
| 133 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3986 |
| 134 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3534 |
| 135 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 879 |
| 136 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +12 | 14609 |
| 137 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1813 |
| 138 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 31208 |
| 139 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 6093 |
| 140 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1452 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +12 | 3003 |
| 142 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28005 |
| 143 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 32223 |
| 144 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 0 |
| 145 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1509 |
| 146 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +11 | 6181 |
| 147 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 8891 |
| 148 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2731 |
| 149 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47309 |
| 150 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +11 | 2810 |
| 151 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 489 |
| 152 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6267 |
| 153 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4648 |
| 154 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 2998 |
| 155 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 34184 |
| 156 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2462 |
| 157 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +10 | 1918 |
| 158 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1133 |
| 159 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1953 |
| 160 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 392 |
| 161 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1412 |
| 162 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +9 | 5416 |
| 163 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1092 |
| 164 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45309 |
| 165 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1109 |
| 166 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10771 |
| 167 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1641 |
| 168 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 390 |
| 169 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 576 |
| 170 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +9 | 1567 |
| 171 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1061 |
| 172 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +9 | 15786 |
| 173 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +9 | 1507 |
| 174 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1963 |
| 175 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8626 |
| 176 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 1803 |
| 177 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9124 |
| 178 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24626 |
| 179 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 10791 |
| 180 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 11310 |
| 181 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8928 |
| 182 | [openai/skills](https://github.com/openai/skills) | +8 | 25140 |
| 183 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 27582 |
| 184 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28485 |
| 185 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +8 | 6151 |
| 186 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3456 |
| 187 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3702 |
| 188 | [jundot/omlx](https://github.com/jundot/omlx) | +7 | 20441 |
| 189 | [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit) | +7 | 1097 |
| 190 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +7 | 6540 |
| 191 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 192 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1531 |
| 193 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 6903 |
| 194 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 195 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3122 |
| 196 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1521 |
| 197 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 279 |
| 198 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 336 |
| 199 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 497 |
| 200 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +6 | 14053 |
| 201 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3876 |
| 202 | [OtterMind/Chat2DB](https://github.com/OtterMind/Chat2DB) | +6 | 28017 |
| 203 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1571 |
| 204 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +5 | 821 |
| 205 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +5 | 1252 |
| 206 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +5 | 9847 |
| 207 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 637 |
| 208 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 10192 |
| 209 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 210 | [penecho/penecho](https://github.com/penecho/penecho) | +5 | 2118 |
| 211 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 831 |
| 212 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 705 |
| 213 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3433 |
| 214 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 1110 |
| 215 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +5 | 26327 |
| 216 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 648 |
| 217 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5799 |
| 218 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1403 |
| 219 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +4 | 621 |
| 220 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 775 |
| 221 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3030 |
| 222 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1218 |
| 223 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +4 | 6946 |
| 224 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +4 | 3208 |
| 225 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +4 | 1117 |
| 226 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7287 |
| 227 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 243 |
| 228 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10600 |
| 229 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 533 |
| 230 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4969 |
| 231 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5252 |
| 232 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8815 |
| 233 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 645 |
| 234 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3539 |
| 235 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5185 |
| 236 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +4 | 3336 |
| 237 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1203 |
| 238 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +4 | 312 |
| 239 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 112 |
| 240 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 914 |
| 241 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4838 |
| 242 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 282 |
| 243 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 201 |
| 244 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3532 |
| 245 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6024 |
| 246 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 5980 |
| 247 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 855 |
| 248 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 242 |
| 249 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 275 |
| 250 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 601 |
| 251 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 162 |
| 252 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 642 |
| 253 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1746 |
| 254 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +3 | 1395 |
| 255 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8990 |
| 256 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 866 |
| 257 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 208 |
| 258 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 3021 |
| 259 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1622 |
| 260 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 192 |
| 261 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 399 |
| 262 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 243 |
| 263 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1234 |
| 264 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9683 |
| 265 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +3 | 14748 |
| 266 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9699 |
| 267 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4891 |
| 268 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 971 |
| 269 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 218 |
| 270 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 581 |
| 271 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 332 |
| 272 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1248 |
| 273 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2114 |
| 274 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28659 |
| 275 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2582 |
| 276 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +2 | 354 |
| 277 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 745 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 279 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 475 |
| 280 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 121 |
| 281 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3731 |
| 282 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1037 |
| 283 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 237 |
| 284 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +2 | 95 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 367 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2906 |
| 287 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5232 |
| 288 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1239 |
| 289 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1413 |
| 290 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 519 |
| 291 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 292 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 264 |
| 293 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 137 |
| 294 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 123 |
| 295 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 907 |
| 296 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1336 |
| 297 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 168 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 951 |
| 299 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +1 | 3078 |
| 300 | [TensorHub-ORG/Coomi-Android](https://github.com/TensorHub-ORG/Coomi-Android) | +1 | 97 |
