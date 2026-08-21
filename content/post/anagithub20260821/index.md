---
title: "2026-08-21 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+7 2.ai-memory+5 3.terminal-browser+5 4.diagram-design+4 5.getcontact-cli+4"
date: 2026-08-21T20:27:10+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-21 20:27:10

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
        'daily': {"categories": ["Wei-Shaw/sub2api", "t8y2/dbx", "arvin341az-glitch/RVG", "Tiger3807861189/J-Space-Cognition-Suite-V3.6", "helloianneo/ian-xiaohei-illustrations", "volcengine/OpenViking", "zenbu-labs/terminal-code", "blader/humanizer", "xai-org/grok-build", "block/buzz", "holaboss-ai/holaOS", "tt-a1i/archify", "hugohe3/ppt-master", "vectorize-io/hindsight", "bojieli/ai-agent-book", "xdreizein666/getcontact-cli", "cathrynlavery/diagram-design", "zenbu-labs/terminal-browser", "akitaonrails/ai-memory", "anywhere-labs/deepseek-harness-desktop"], "data": [2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 7]},
        'weekly': {"categories": ["ifixai-ai/iFixAi", "block/buzz", "arvin341az-glitch/RVG", "internet-court/internet-court-skill", "virgiliojr94/book-to-skill", "walkinglabs/learn-harness-engineering", "akitaonrails/ai-memory", "cactus-compute/needle", "tt-a1i/archify", "mukul975/Anthropic-Cybersecurity-Skills", "AprilNEA/OpenLogi", "xiaobright/dsh-anchored-standard", "holaboss-ai/holaOS", "bojieli/ai-agent-book", "volcengine/OpenViking", "stablyai/orca", "Tiger3807861189/J-Space-Cognition-Suite-V3.6", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 15, 15, 16, 17, 19, 19, 28, 43, 60]},
        'monthly': {"categories": ["cloudflare/cloudflare-os", "k1tbyte/Wand-Enhancer", "TencentCloud/TencentDB-Agent-Memory", "ifixai-ai/iFixAi", "brightdata/cli", "anywhere-labs/deepseek-harness-desktop", "guillaumemeyer/watermarks-remover", "emilkowalski/skills", "floci-io/floci", "herdrdev/herdr", "andrewyng/openworker", "ayghri/i-have-adhd", "zhaoxuya520/reverse-skill", "virgiliojr94/book-to-skill", "bojieli/ai-agent-book", "cathrynlavery/diagram-design", "stablyai/orca", "block/buzz", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [60, 61, 62, 64, 65, 66, 66, 69, 74, 77, 82, 82, 92, 104, 111, 112, 122, 143, 159, 256]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +7 | 17522 |
| 2 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +5 | 3919 |
| 3 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +5 | 1882 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +4 | 24926 |
| 5 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 358 |
| 6 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +4 | 40673 |
| 7 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 20842 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 48468 |
| 9 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3 | 14939 |
| 10 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +3 | 10580 |
| 11 | [block/buzz](https://github.com/block/buzz) | +3 | 29158 |
| 12 | [xai-org/grok-build](https://github.com/xai-org/grok-build) | +3 | 25846 |
| 13 | [blader/humanizer](https://github.com/blader/humanizer) | +3 | 37042 |
| 14 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +3 | 1192 |
| 15 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3 | 31602 |
| 16 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +3 | 10008 |
| 17 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +3 | 3002 |
| 18 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +2 | 3302 |
| 19 | [t8y2/dbx](https://github.com/t8y2/dbx) | +2 | 16189 |
| 20 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +2 | 38521 |
| 21 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +2 | 16569 |
| 22 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +2 | 4110 |
| 23 | [rukamori/ArchiveTune](https://github.com/rukamori/ArchiveTune) | +2 | 4905 |
| 24 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +2 | 1479 |
| 25 | [pgrundev/pgbot](https://github.com/pgrundev/pgbot) | +2 | 547 |
| 26 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +2 | 9811 |
| 27 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +2 | 274 |
| 28 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2 | 11085 |
| 29 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +2 | 5876 |
| 30 | [stablyai/orca](https://github.com/stablyai/orca) | +2 | 50645 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +60 | 17522 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +43 | 24926 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +28 | 16569 |
| 4 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +19 | 3002 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +19 | 50645 |
| 6 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +17 | 31602 |
| 7 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +16 | 40673 |
| 8 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +15 | 10580 |
| 9 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +15 | 3696 |
| 10 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +14 | 12756 |
| 11 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +13 | 30512 |
| 12 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +13 | 14939 |
| 13 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +13 | 8304 |
| 14 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +12 | 3919 |
| 15 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +12 | 13566 |
| 16 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +12 | 23640 |
| 17 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +12 | 4347 |
| 18 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +11 | 3302 |
| 19 | [block/buzz](https://github.com/block/buzz) | +11 | 29158 |
| 20 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +11 | 11168 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +11 | 48468 |
| 22 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +11 | 17644 |
| 23 | [yetone/cumora](https://github.com/yetone/cumora) | +10 | 2857 |
| 24 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +10 | 27203 |
| 25 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 11661 |
| 26 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +10 | 31357 |
| 27 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +10 | 31339 |
| 28 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +9 | 3370 |
| 29 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +9 | 4118 |
| 30 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +9 | 45176 |
| 31 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +9 | 7119 |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9 | 36912 |
| 33 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +9 | 23741 |
| 34 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 37042 |
| 35 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +8 | 49249 |
| 36 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +8 | 24694 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +8 | 26281 |
| 38 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +8 | 4110 |
| 39 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +7 | 22950 |
| 40 | [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) | +7 | 1882 |
| 41 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +7 | 33431 |
| 42 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +7 | 4550 |
| 43 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +7 | 14540 |
| 44 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 19938 |
| 45 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +6 | 17744 |
| 46 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 12422 |
| 47 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +6 | 39796 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +6 | 46453 |
| 49 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +6 | 12572 |
| 50 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 47208 |
| 51 | [spinabot/brigade](https://github.com/spinabot/brigade) | +6 | 3023 |
| 52 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +5 | 38521 |
| 53 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +5 | 6195 |
| 54 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +5 | 12499 |
| 55 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +5 | 11085 |
| 56 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +5 | 1009 |
| 57 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +5 | 1479 |
| 58 | [xai-org/grok-build](https://github.com/xai-org/grok-build) | +5 | 25846 |
| 59 | [every-app/open-seo](https://github.com/every-app/open-seo) | +5 | 13002 |
| 60 | [rukamori/ArchiveTune](https://github.com/rukamori/ArchiveTune) | +5 | 4905 |
| 61 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +5 | 1639 |
| 62 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +5 | 1847 |
| 63 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +5 | 32621 |
| 64 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +5 | 34070 |
| 65 | [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) | +4 | 1192 |
| 66 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +4 | 5876 |
| 67 | [agegr/pi-web](https://github.com/agegr/pi-web) | +4 | 4998 |
| 68 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 4619 |
| 69 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +4 | 3378 |
| 70 | [xdreizein666/getcontact-cli](https://github.com/xdreizein666/getcontact-cli) | +4 | 358 |
| 71 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +4 | 1612 |
| 72 | [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | +4 | 1988 |
| 73 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +4 | 41956 |
| 74 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +4 | 274 |
| 75 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +4 | 16187 |
| 76 | [iAmCorey/Wake](https://github.com/iAmCorey/Wake) | +4 | 400 |
| 77 | [tw93/Kami](https://github.com/tw93/Kami) | +4 | 10835 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 31107 |
| 79 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +4 | 10008 |
| 80 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 10749 |
| 81 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +4 | 734 |
| 82 | [BetterWright/betterwright](https://github.com/BetterWright/betterwright) | +4 | 205 |
| 83 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +4 | 5757 |
| 84 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +4 | 13044 |
| 85 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +4 | 24584 |
| 86 | [csyqlz/VOZEB-PRO](https://github.com/csyqlz/VOZEB-PRO) | +4 | 708 |
| 87 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +4 | 14553 |
| 88 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +4 | 3274 |
| 89 | [macro-inc/macro](https://github.com/macro-inc/macro) | +4 | 3932 |
| 90 | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | +4 | 1128 |
| 91 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +4 | 47261 |
| 92 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4 | 47926 |
| 93 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 20842 |
| 94 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +3 | 2671 |
| 95 | [jundot/omlx](https://github.com/jundot/omlx) | +3 | 20210 |
| 96 | [t8y2/dbx](https://github.com/t8y2/dbx) | +3 | 16189 |
| 97 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 32768 |
| 98 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +3 | 21067 |
| 99 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 41093 |
| 100 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +3 | 5819 |
| 101 | [securo-finance/securo](https://github.com/securo-finance/securo) | +3 | 2017 |
| 102 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 36399 |
| 103 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +3 | 9017 |
| 104 | [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | +3 | 3969 |
| 105 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +3 | 2975 |
| 106 | [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) | +3 | 363 |
| 107 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +3 | 5633 |
| 108 | [openai/skills](https://github.com/openai/skills) | +3 | 25097 |
| 109 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +3 | 1960 |
| 110 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +3 | 17587 |
| 111 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 24310 |
| 112 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +2 | 325 |
| 113 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 63581 |
| 114 | [ARahim3/mlx-dspark](https://github.com/ARahim3/mlx-dspark) | +2 | 515 |
| 115 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +2 | 9648 |
| 116 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +2 | 5290 |
| 117 | [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | +2 | 2096 |
| 118 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +2 | 1430 |
| 119 | [yuwen-cool/yuwen-publish-precheck](https://github.com/yuwen-cool/yuwen-publish-precheck) | +2 | 614 |
| 120 | [rosemarycox5334-debug/PA_Agent](https://github.com/rosemarycox5334-debug/PA_Agent) | +2 | 1879 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +256 | 17644 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +159 | 17744 |
| 3 | [block/buzz](https://github.com/block/buzz) | +143 | 29158 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +122 | 50645 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +112 | 24926 |
| 6 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +111 | 40673 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +104 | 23640 |
| 8 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +92 | 27203 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +82 | 22950 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +82 | 14922 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +77 | 31340 |
| 12 | [floci-io/floci](https://github.com/floci-io/floci) | +74 | 20771 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +69 | 31357 |
| 14 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +66 | 16570 |
| 15 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +66 | 17522 |
| 16 | [brightdata/cli](https://github.com/brightdata/cli) | +65 | 6368 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 11168 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +62 | 23654 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +61 | 19430 |
| 20 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8717 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +60 | 48468 |
| 22 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +58 | 16435 |
| 23 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +55 | 11661 |
| 24 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +54 | 10043 |
| 25 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +53 | 21622 |
| 26 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +52 | 24310 |
| 27 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +49 | 14939 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +49 | 32768 |
| 29 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 14040 |
| 30 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +46 | 6628 |
| 31 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +46 | 29000 |
| 32 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +46 | 12572 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +44 | 36912 |
| 34 | [google/skills](https://github.com/google/skills) | +44 | 18585 |
| 35 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +44 | 21067 |
| 36 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1447 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 26281 |
| 38 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 35004 |
| 39 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +41 | 15964 |
| 40 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 63581 |
| 41 | [blader/humanizer](https://github.com/blader/humanizer) | +40 | 37042 |
| 42 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +39 | 49249 |
| 43 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8562 |
| 44 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +39 | 34297 |
| 45 | [every-app/open-seo](https://github.com/every-app/open-seo) | +38 | 13002 |
| 46 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +38 | 25681 |
| 47 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5952 |
| 48 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +37 | 30669 |
| 49 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +37 | 12499 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8771 |
| 51 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +34 | 4197 |
| 52 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +33 | 19938 |
| 53 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 47208 |
| 54 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 45176 |
| 55 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 41956 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +33 | 39796 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 10046 |
| 58 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +32 | 47531 |
| 59 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +32 | 36399 |
| 60 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +32 | 6514 |
| 61 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +32 | 31412 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +30 | 10346 |
| 63 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +30 | 18169 |
| 64 | [oblien/openship](https://github.com/oblien/openship) | +30 | 11163 |
| 65 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +27 | 4550 |
| 66 | [spinabot/brigade](https://github.com/spinabot/brigade) | +27 | 3023 |
| 67 | [different-ai/openwork](https://github.com/different-ai/openwork) | +27 | 22881 |
| 68 | [get-bb/bb](https://github.com/get-bb/bb) | +27 | 2519 |
| 69 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +27 | 3274 |
| 70 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +26 | 4110 |
| 71 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 5001 |
| 72 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +26 | 15456 |
| 73 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 22000 |
| 74 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +26 | 9305 |
| 75 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +25 | 31602 |
| 76 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 789 |
| 77 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 32621 |
| 78 | [drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare) | +25 | 6253 |
| 79 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +24 | 2688 |
| 80 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24766 |
| 81 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 9063 |
| 82 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +24 | 12422 |
| 83 | [xai-org/grok-build](https://github.com/xai-org/grok-build) | +24 | 25846 |
| 84 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4127 |
| 85 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +23 | 8304 |
| 86 | [t8y2/dbx](https://github.com/t8y2/dbx) | +23 | 16189 |
| 87 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +22 | 10580 |
| 88 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +22 | 46453 |
| 89 | [malisper/pgrust](https://github.com/malisper/pgrust) | +22 | 4615 |
| 90 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +22 | 1111 |
| 91 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +22 | 5633 |
| 92 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +21 | 5757 |
| 93 | [browser-use/video-use](https://github.com/browser-use/video-use) | +21 | 21225 |
| 94 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +20 | 38521 |
| 95 | [Tiger3807861189/J-Space-Cognition-Suite-V3.6](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6) | +19 | 3002 |
| 96 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +18 | 4118 |
| 97 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +18 | 12756 |
| 98 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 6228 |
| 99 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 14741 |
| 100 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +17 | 47926 |
| 101 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +17 | 8813 |
| 102 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 43238 |
| 103 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +17 | 13752 |
| 104 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +16 | 3302 |
| 105 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +16 | 4415 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +16 | 20842 |
| 107 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +16 | 23741 |
| 108 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +16 | 11085 |
| 109 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +16 | 10326 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +15 | 6957 |
| 111 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +15 | 30512 |
| 112 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +15 | 3225 |
| 113 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +15 | 8557 |
| 114 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 775 |
| 115 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +15 | 3696 |
| 116 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +15 | 8427 |
| 117 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 5331 |
| 118 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +14 | 1960 |
| 119 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +14 | 9464 |
| 120 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2440 |
| 121 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3992 |
| 122 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 30494 |
| 123 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +13 | 31107 |
| 124 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 9142 |
| 125 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3152 |
| 126 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 6136 |
| 127 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +13 | 5876 |
| 128 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +13 | 11579 |
| 129 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 130 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2192 |
| 131 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +13 | 32153 |
| 132 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 855 |
| 133 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +12 | 14540 |
| 134 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1811 |
| 135 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 6078 |
| 136 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1448 |
| 137 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 34070 |
| 138 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +12 | 16231 |
| 139 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27924 |
| 140 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 0 |
| 141 | [securo-finance/securo](https://github.com/securo-finance/securo) | +11 | 2017 |
| 142 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2681 |
| 143 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +11 | 47261 |
| 144 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +11 | 2945 |
| 145 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 456 |
| 146 | [decolua/9router](https://github.com/decolua/9router) | +11 | 26011 |
| 147 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 2112 |
| 148 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +10 | 6195 |
| 149 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +10 | 1430 |
| 150 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +10 | 2975 |
| 151 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 8849 |
| 152 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2461 |
| 153 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +10 | 1860 |
| 154 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1075 |
| 155 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1942 |
| 156 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 388 |
| 157 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 3378 |
| 158 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1729 |
| 159 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1062 |
| 160 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4619 |
| 161 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10742 |
| 162 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 387 |
| 163 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1618 |
| 164 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 574 |
| 165 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1096 |
| 166 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1056 |
| 167 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3897 |
| 168 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +9 | 2317 |
| 169 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +9 | 10758 |
| 170 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +9 | 2354 |
| 171 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1954 |
| 172 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +9 | 14017 |
| 173 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 5290 |
| 174 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 10749 |
| 175 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 7203 |
| 176 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +8 | 9017 |
| 177 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +8 | 6223 |
| 178 | [uber/ADR](https://github.com/uber/ADR) | +8 | 1475 |
| 179 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +8 | 5819 |
| 180 | [openai/skills](https://github.com/openai/skills) | +8 | 25097 |
| 181 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2583 |
| 182 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +8 | 6072 |
| 183 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 27540 |
| 184 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28431 |
| 185 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3689 |
| 186 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8556 |
| 187 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24555 |
| 188 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +7 | 45234 |
| 189 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +7 | 829 |
| 190 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +7 | 9648 |
| 191 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1494 |
| 192 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 193 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 3449 |
| 194 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1526 |
| 195 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +6 | 6797 |
| 196 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 197 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3106 |
| 198 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 277 |
| 199 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +6 | 9811 |
| 200 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 326 |
| 201 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 494 |
| 202 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30300 |
| 203 | [aklivity/zilla](https://github.com/aklivity/zilla) | +6 | 1702 |
| 204 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +5 | 1215 |
| 205 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5769 |
| 206 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 609 |
| 207 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5896 |
| 208 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 10136 |
| 209 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 210 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 825 |
| 211 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 701 |
| 212 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +5 | 3812 |
| 213 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3404 |
| 214 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 364 |
| 215 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +4 | 631 |
| 216 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +4 | 708 |
| 217 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7268 |
| 218 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 237 |
| 219 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10528 |
| 220 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 508 |
| 221 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4919 |
| 222 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5244 |
| 223 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8762 |
| 224 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1200 |
| 225 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +4 | 621 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3497 |
| 227 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5158 |
| 228 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14701 |
| 229 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +4 | 3332 |
| 230 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1176 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 111 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1072 |
| 233 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4802 |
| 234 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 271 |
| 235 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 199 |
| 236 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +3 | 1398 |
| 237 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 222 |
| 238 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +3 | 615 |
| 239 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 588 |
| 240 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 158 |
| 241 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 642 |
| 242 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +3 | 733 |
| 243 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +3 | 1376 |
| 244 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3527 |
| 245 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8985 |
| 246 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 843 |
| 247 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 204 |
| 248 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2931 |
| 249 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1584 |
| 250 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 192 |
| 251 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 397 |
| 252 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9660 |
| 253 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1220 |
| 254 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3176 |
| 255 | [AnInsomniacy/motrix-next](https://github.com/AnInsomniacy/motrix-next) | +3 | 9653 |
| 256 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +3 | 5999 |
| 257 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 973 |
| 258 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +3 | 538 |
| 259 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +3 | 1359 |
| 260 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4888 |
| 261 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 955 |
| 262 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 581 |
| 263 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +3 | 300 |
| 264 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 328 |
| 265 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1233 |
| 266 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2095 |
| 267 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 874 |
| 268 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28641 |
| 269 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +3 | 7399 |
| 270 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +2 | 6019 |
| 271 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 738 |
| 272 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 171 |
| 273 | [Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) | +2 | 2825 |
| 274 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 634 |
| 275 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 906 |
| 276 | [panel-zeus/Z-E-U-S](https://github.com/panel-zeus/Z-E-U-S) | +2 | 675 |
| 277 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12409 |
| 278 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +2 | 215 |
| 279 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 280 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 453 |
| 281 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 119 |
| 282 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3706 |
| 283 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3219 |
| 284 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 202 |
| 285 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 224 |
| 286 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 360 |
| 287 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2905 |
| 288 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5211 |
| 289 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1229 |
| 290 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1412 |
| 291 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 518 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 293 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2576 |
| 294 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 133 |
| 295 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 121 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 902 |
| 297 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1329 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 946 |
| 299 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 94 |
| 300 | [Swayingleaves/novanova-studio](https://github.com/Swayingleaves/novanova-studio) | +1 | 138 |
