---
title: "2026-08-22 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+15 2.watermarks-remover+14 3.OpenLogi+12 4.sub2api+11 5.arc-task-gen+11"
date: 2026-08-22T20:23:47+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-22 20:23:47

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
        'daily': {"categories": ["meituan-longcat/LongCat-Video", "ifixai-ai/iFixAi", "FailproofAI/failproofai", "gastongouron/ironpress", "akitaonrails/ai-memory", "zhaoxuya520/reverse-skill", "Alishahryar1/free-claude-code", "ayghri/i-have-adhd", "volcengine/OpenViking", "cursor/plugins", "agentrhq/webcmd", "HiThink-Tech/Financial-API", "stablyai/orca", "citrolabs/ego-lite", "cathrynlavery/diagram-design", "pathwaycom/arc-task-gen", "Wei-Shaw/sub2api", "AprilNEA/OpenLogi", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop"], "data": [5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9, 10, 11, 11, 12, 14, 15]},
        'weekly': {"categories": ["zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "Wei-Shaw/sub2api", "mukul975/Anthropic-Cybersecurity-Skills", "arvin341az-glitch/RVG", "walkinglabs/learn-harness-engineering", "ifixai-ai/iFixAi", "bojieli/ai-agent-book", "holaboss-ai/holaOS", "akitaonrails/ai-memory", "zhu1090093659/dsh-web-ui", "Tiger3807861189/J-Space-Cognition-Suite-V3.6", "pathwaycom/arc-task-gen", "General-Legal/legal-templates", "volcengine/OpenViking", "AprilNEA/OpenLogi", "stablyai/orca", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [14, 14, 14, 15, 15, 16, 16, 17, 18, 18, 19, 19, 19, 19, 25, 25, 27, 35, 46, 65]},
        'monthly': {"categories": ["hugohe3/ppt-master", "k1tbyte/Wand-Enhancer", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "ifixai-ai/iFixAi", "emilkowalski/skills", "floci-io/floci", "herdrdev/herdr", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "andrewyng/openworker", "ayghri/i-have-adhd", "zhaoxuya520/reverse-skill", "bojieli/ai-agent-book", "virgiliojr94/book-to-skill", "cathrynlavery/diagram-design", "stablyai/orca", "block/buzz", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [62, 64, 65, 66, 69, 72, 77, 80, 80, 81, 83, 89, 98, 100, 107, 122, 128, 138, 161, 259]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +15 | 18276 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +14 | 17004 |
| 3 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +12 | 13753 |
| 4 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +11 | 38761 |
| 5 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +11 | 4536 |
| 6 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +10 | 25418 |
| 7 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +9 | 12735 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +9 | 51188 |
| 9 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +9 | 959 |
| 10 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1317 |
| 11 | [cursor/plugins](https://github.com/cursor/plugins) | +8 | 4622 |
| 12 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +8 | 32005 |
| 13 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +7 | 23206 |
| 14 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +6 | 47018 |
| 15 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +6 | 27397 |
| 16 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +6 | 4069 |
| 17 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +6 | 680 |
| 18 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +5 | 1387 |
| 19 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5 | 11244 |
| 20 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +5 | 7410 |
| 21 | [blader/humanizer](https://github.com/blader/humanizer) | +5 | 37206 |
| 22 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +5 | 915 |
| 23 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +5 | 12840 |
| 24 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +5 | 8962 |
| 25 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +5 | 13701 |
| 26 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +4 | 3436 |
| 27 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +4 | 12197 |
| 28 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +4 | 3623 |
| 29 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 32896 |
| 30 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +4 | 1243 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +65 | 18276 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +46 | 25418 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +35 | 17004 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 51188 |
| 5 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +25 | 13753 |
| 6 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +25 | 32005 |
| 7 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1704 |
| 8 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +19 | 4536 |
| 9 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +19 | 3019 |
| 10 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +19 | 5591 |
| 11 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +18 | 4069 |
| 12 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +18 | 10648 |
| 13 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +17 | 40922 |
| 14 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +16 | 11244 |
| 15 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +16 | 13701 |
| 16 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +15 | 3436 |
| 17 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +15 | 30649 |
| 18 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +14 | 38761 |
| 19 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 23206 |
| 20 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +14 | 27397 |
| 21 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +14 | 15048 |
| 22 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +14 | 24099 |
| 23 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +14 | 4448 |
| 24 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +13 | 12735 |
| 25 | [block/buzz](https://github.com/block/buzz) | +13 | 29725 |
| 26 | [blader/humanizer](https://github.com/blader/humanizer) | +13 | 37206 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +13 | 48619 |
| 28 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +12 | 3623 |
| 29 | [HiThink-Tech/Financial-API](https://github.com/HiThink-Tech/Financial-API) | +12 | 959 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +12 | 47018 |
| 31 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 49449 |
| 32 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 31572 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +12 | 11795 |
| 34 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +12 | 8562 |
| 35 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +12 | 3713 |
| 36 | [yetone/cumora](https://github.com/yetone/cumora) | +11 | 2898 |
| 37 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +11 | 33551 |
| 38 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +11 | 2618 |
| 39 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +11 | 26502 |
| 40 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +11 | 31571 |
| 41 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +11 | 12840 |
| 42 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +11 | 45286 |
| 43 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +11 | 19774 |
| 44 | [cursor/plugins](https://github.com/cursor/plugins) | +10 | 4622 |
| 45 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +10 | 7155 |
| 46 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +10 | 24734 |
| 47 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +10 | 17847 |
| 48 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +9 | 20051 |
| 49 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1243 |
| 50 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1317 |
| 51 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +8 | 12197 |
| 52 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +8 | 39884 |
| 53 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +8 | 4203 |
| 54 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +8 | 23804 |
| 55 | [FailproofAI/failproofai](https://github.com/FailproofAI/failproofai) | +7 | 1387 |
| 56 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +7 | 574 |
| 57 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 36531 |
| 58 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +7 | 17909 |
| 59 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +7 | 37102 |
| 60 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +7 | 3455 |
| 61 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +7 | 1965 |
| 62 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 13092 |
| 63 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +7 | 4593 |
| 64 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +7 | 1868 |
| 65 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +6 | 20917 |
| 66 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +6 | 32896 |
| 67 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +6 | 1306 |
| 68 | [jundot/omlx](https://github.com/jundot/omlx) | +6 | 20331 |
| 69 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +6 | 16488 |
| 70 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +6 | 11217 |
| 71 | [gastongouron/ironpress](https://github.com/gastongouron/ironpress) | +6 | 680 |
| 72 | [MemTensor/memmy-agent](https://github.com/MemTensor/memmy-agent) | +6 | 915 |
| 73 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +6 | 7410 |
| 74 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 8962 |
| 75 | [macro-inc/macro](https://github.com/macro-inc/macro) | +6 | 3971 |
| 76 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +6 | 6221 |
| 77 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47287 |
| 78 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 16021 |
| 79 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +6 | 327 |
| 80 | [iAmCorey/Wake](https://github.com/iAmCorey/Wake) | +6 | 446 |
| 81 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +6 | 16227 |
| 82 | [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc) | +6 | 4361 |
| 83 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +6 | 5837 |
| 84 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 42106 |
| 85 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 5727 |
| 86 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +6 | 1828 |
| 87 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 12556 |
| 88 | [floci-io/floci](https://github.com/floci-io/floci) | +5 | 21174 |
| 89 | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | +5 | 1154 |
| 90 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +5 | 41143 |
| 91 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +5 | 5983 |
| 92 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +5 | 1722 |
| 93 | [nuyoah-ai-works/nuyoah-xiezhen-prompt](https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt) | +5 | 410 |
| 94 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +5 | 21131 |
| 95 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +5 | 23817 |
| 96 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +5 | 4643 |
| 97 | [securo-finance/securo](https://github.com/securo-finance/securo) | +5 | 2063 |
| 98 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +5 | 757 |
| 99 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +5 | 14577 |
| 100 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 47961 |
| 101 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 20611 |
| 102 | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | +4 | 5842 |
| 103 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +4 | 526 |
| 104 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +4 | 5358 |
| 105 | [sunchaokun/PPT-Design-Skill](https://github.com/sunchaokun/PPT-Design-Skill) | +4 | 546 |
| 106 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 445 |
| 107 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +4 | 1323 |
| 108 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +4 | 6493 |
| 109 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +4 | 9064 |
| 110 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 31156 |
| 111 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10768 |
| 112 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +4 | 376 |
| 113 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 34129 |
| 114 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4 | 47286 |
| 115 | [powerycy/BossHunter](https://github.com/powerycy/BossHunter) | +3 | 425 |
| 116 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +3 | 358 |
| 117 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +3 | 437 |
| 118 | [Leutenegger/vanity-eth](https://github.com/Leutenegger/vanity-eth) | +3 | 803 |
| 119 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +3 | 507 |
| 120 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +3 | 27173 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +259 | 17847 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +161 | 17909 |
| 3 | [block/buzz](https://github.com/block/buzz) | +138 | 29725 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +128 | 51188 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +122 | 25418 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +107 | 24099 |
| 7 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +100 | 40922 |
| 8 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +98 | 27397 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +89 | 23206 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +83 | 14941 |
| 11 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +81 | 18276 |
| 12 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +80 | 17004 |
| 13 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +80 | 31571 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +77 | 21174 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +72 | 31572 |
| 16 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +69 | 11244 |
| 17 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6400 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +65 | 23817 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +64 | 19774 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +62 | 48619 |
| 21 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +61 | 16488 |
| 22 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8783 |
| 23 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +57 | 10246 |
| 24 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +56 | 21644 |
| 25 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +55 | 11795 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +52 | 15048 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +52 | 24361 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +48 | 32896 |
| 29 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +48 | 12840 |
| 30 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14074 |
| 31 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +47 | 29052 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +46 | 26502 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +46 | 37102 |
| 34 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 6718 |
| 35 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +46 | 21131 |
| 36 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +46 | 12735 |
| 37 | [google/skills](https://github.com/google/skills) | +45 | 18608 |
| 38 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +45 | 16021 |
| 39 | [blader/humanizer](https://github.com/blader/humanizer) | +44 | 37206 |
| 40 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1448 |
| 41 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 35037 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 63631 |
| 43 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +39 | 49449 |
| 44 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8576 |
| 45 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +39 | 34328 |
| 46 | [every-app/open-seo](https://github.com/every-app/open-seo) | +38 | 13092 |
| 47 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +38 | 6051 |
| 48 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +37 | 25835 |
| 49 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +36 | 20051 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8800 |
| 51 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 4229 |
| 52 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +35 | 36531 |
| 53 | [openai/codex-security](https://github.com/openai/codex-security) | +35 | 10075 |
| 54 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +34 | 45286 |
| 55 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +34 | 42106 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +34 | 39884 |
| 57 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +34 | 30700 |
| 58 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +33 | 32005 |
| 59 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 47287 |
| 60 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +33 | 31469 |
| 61 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10378 |
| 62 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +32 | 18240 |
| 63 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +31 | 6542 |
| 64 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +30 | 47644 |
| 65 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +29 | 38761 |
| 66 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +29 | 4536 |
| 67 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +29 | 13754 |
| 68 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | +29 | 5591 |
| 69 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +29 | 15486 |
| 70 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 22096 |
| 71 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +28 | 47018 |
| 72 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +28 | 4593 |
| 73 | [get-bb/bb](https://github.com/get-bb/bb) | +28 | 2556 |
| 74 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +28 | 3297 |
| 75 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +27 | 4203 |
| 76 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3047 |
| 77 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5022 |
| 78 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 22952 |
| 79 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +25 | 10648 |
| 80 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 788 |
| 81 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 32795 |
| 82 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +25 | 5727 |
| 83 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +25 | 4137 |
| 84 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +24 | 2688 |
| 85 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +24 | 8562 |
| 86 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24809 |
| 87 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9095 |
| 88 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +24 | 12556 |
| 89 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +23 | 13701 |
| 90 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +23 | 5837 |
| 91 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +22 | 4069 |
| 92 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +22 | 8962 |
| 93 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +20 | 3436 |
| 94 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +20 | 41143 |
| 95 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +19 | 3019 |
| 96 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1704 |
| 97 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +19 | 20917 |
| 98 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +19 | 7155 |
| 99 | [browser-use/video-use](https://github.com/browser-use/video-use) | +19 | 21256 |
| 100 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +18 | 23804 |
| 101 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +18 | 47961 |
| 102 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +18 | 43335 |
| 103 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +17 | 30649 |
| 104 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +17 | 11217 |
| 105 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 6291 |
| 106 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 14806 |
| 107 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +17 | 12197 |
| 108 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +16 | 6968 |
| 109 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +16 | 3291 |
| 110 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +16 | 13773 |
| 111 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3713 |
| 112 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +16 | 8457 |
| 113 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 786 |
| 114 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +15 | 10360 |
| 115 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5352 |
| 116 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30589 |
| 117 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 1979 |
| 118 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9172 |
| 119 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +14 | 8650 |
| 120 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +14 | 9510 |
| 121 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 5983 |
| 122 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2460 |
| 123 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3988 |
| 124 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +13 | 7410 |
| 125 | [securo-finance/securo](https://github.com/securo-finance/securo) | +13 | 2063 |
| 126 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31156 |
| 127 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3168 |
| 128 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26070 |
| 129 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 130 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2196 |
| 131 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +13 | 32187 |
| 132 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +12 | 2618 |
| 133 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +12 | 3455 |
| 134 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 869 |
| 135 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +12 | 14577 |
| 136 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1813 |
| 137 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +12 | 6156 |
| 138 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 6085 |
| 139 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1450 |
| 140 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +12 | 2972 |
| 141 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 34129 |
| 142 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27968 |
| 143 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 0 |
| 144 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +11 | 1476 |
| 145 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 8873 |
| 146 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2702 |
| 147 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47286 |
| 148 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 477 |
| 149 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6221 |
| 150 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +10 | 5358 |
| 151 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +10 | 4643 |
| 152 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 2985 |
| 153 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2461 |
| 154 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +10 | 2763 |
| 155 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +10 | 1892 |
| 156 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1086 |
| 157 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +10 | 1961 |
| 158 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1946 |
| 159 | [penecho/penecho](https://github.com/penecho/penecho) | +10 | 2118 |
| 160 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 390 |
| 161 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +9 | 1243 |
| 162 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1763 |
| 163 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1082 |
| 164 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45270 |
| 165 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1103 |
| 166 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10756 |
| 167 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +9 | 9064 |
| 168 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1633 |
| 169 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 388 |
| 170 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 575 |
| 171 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +9 | 1323 |
| 172 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1059 |
| 173 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3924 |
| 174 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +9 | 15761 |
| 175 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24590 |
| 176 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 10768 |
| 177 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14876 |
| 178 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 11135 |
| 179 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +8 | 6247 |
| 180 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +8 | 1317 |
| 181 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 27561 |
| 182 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28454 |
| 183 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +8 | 6115 |
| 184 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 3452 |
| 185 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3695 |
| 186 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +8 | 14036 |
| 187 | [jundot/omlx](https://github.com/jundot/omlx) | +7 | 20331 |
| 188 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +7 | 6493 |
| 189 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1517 |
| 190 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 191 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +7 | 26300 |
| 192 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1527 |
| 193 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 6837 |
| 194 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 195 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3112 |
| 196 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +6 | 767 |
| 197 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 278 |
| 198 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 332 |
| 199 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 495 |
| 200 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30333 |
| 201 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3843 |
| 202 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1559 |
| 203 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +5 | 1230 |
| 204 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +5 | 9831 |
| 205 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 623 |
| 206 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 10161 |
| 207 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 208 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 829 |
| 209 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 703 |
| 210 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3419 |
| 211 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 1095 |
| 212 | [crimera/piko](https://github.com/crimera/piko) | +5 | 4819 |
| 213 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 369 |
| 214 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 640 |
| 215 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5782 |
| 216 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +4 | 1401 |
| 217 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +4 | 616 |
| 218 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 763 |
| 219 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3017 |
| 220 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1210 |
| 221 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +4 | 1022 |
| 222 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7276 |
| 223 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 241 |
| 224 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10540 |
| 225 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 519 |
| 226 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4937 |
| 227 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5251 |
| 228 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8781 |
| 229 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 632 |
| 230 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3516 |
| 231 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5170 |
| 232 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14709 |
| 233 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +4 | 3335 |
| 234 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1203 |
| 235 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +4 | 306 |
| 236 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 112 |
| 237 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 880 |
| 238 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +4 | 7440 |
| 239 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 274 |
| 240 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 199 |
| 241 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3529 |
| 242 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6021 |
| 243 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 5948 |
| 244 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 830 |
| 245 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 232 |
| 246 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +3 | 236 |
| 247 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 594 |
| 248 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 160 |
| 249 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 642 |
| 250 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +3 | 1726 |
| 251 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +3 | 1383 |
| 252 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8986 |
| 253 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 856 |
| 254 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 207 |
| 255 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2947 |
| 256 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1609 |
| 257 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 192 |
| 258 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 398 |
| 259 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +3 | 240 |
| 260 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1229 |
| 261 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9676 |
| 262 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3188 |
| 263 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9672 |
| 264 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4889 |
| 265 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 960 |
| 266 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 212 |
| 267 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 581 |
| 268 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 331 |
| 269 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1241 |
| 270 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2105 |
| 271 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28650 |
| 272 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +3 | 2577 |
| 273 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 743 |
| 274 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 172 |
| 275 | [Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) | +2 | 2834 |
| 276 | [howmp/dsh-pentest](https://github.com/howmp/dsh-pentest) | +2 | 199 |
| 277 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 278 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 472 |
| 279 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 120 |
| 280 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3717 |
| 281 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1029 |
| 282 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 234 |
| 283 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +2 | 95 |
| 284 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 367 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2906 |
| 286 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5218 |
| 287 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1233 |
| 288 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1412 |
| 289 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 519 |
| 290 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 291 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 264 |
| 292 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 136 |
| 293 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 123 |
| 294 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 904 |
| 295 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1332 |
| 296 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 948 |
| 297 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 94 |
| 298 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +1 | 3073 |
| 299 | [TensorHub-ORG/Coomi-Android](https://github.com/TensorHub-ORG/Coomi-Android) | +1 | 93 |
| 300 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +1 | 2651 |
