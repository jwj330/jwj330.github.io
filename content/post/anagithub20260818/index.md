---
title: "2026-08-18 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+12 2.iFixAi+6 3.watermarks-remover+5 4.internet-court-skill+5 5.mycontext+4"
date: 2026-08-18T20:25:08+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-18 20:25:08

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
        'daily': {"categories": ["coreyhaines31/marketingskills", "didilili/ai-agents-from-zero", "ZhuLinsen/daily_stock_analysis", "dnshe/DNSHE-FreeDomains", "blader/humanizer", "akitaonrails/ai-memory", "hugohe3/ppt-master", "pingdotgg/t3code", "cathrynlavery/diagram-design", "bojieli/ai-agent-book", "holaboss-ai/holaOS", "lightningpixel/modly", "tt-a1i/archify", "stablyai/orca", "zhaoxuya520/reverse-skill", "openTrinity/mycontext", "internet-court/internet-court-skill", "guillaumemeyer/watermarks-remover", "ifixai-ai/iFixAi", "anywhere-labs/deepseek-harness-desktop"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 12]},
        'weekly': {"categories": ["MiniMax-AI/MiniMax-H3", "TencentCloud/TencentDB-Agent-Memory", "zhaoxuya520/reverse-skill", "corsairdev/corsair", "HKUDS/DeepTutor", "firecrawl/anydoc", "Zeejay0/gathered-scenes-zine-skill", "pathwaycom/arc-task-gen", "titanwings/colleague-skill", "bojieli/ai-agent-book", "herdrdev/herdr", "cactus-compute/needle", "hugohe3/ppt-master", "PrimeIntellect-ai/prime-agent", "LaoFeng-mouse/flyingmouse-format", "stablyai/orca", "spinabot/brigade", "anywhere-labs/deepseek-harness-desktop", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [11, 11, 11, 12, 12, 13, 13, 14, 14, 14, 15, 17, 20, 21, 22, 22, 23, 43, 52, 69]},
        'monthly': {"categories": ["MadsLorentzen/ai-job-search", "k1tbyte/Wand-Enhancer", "ifixai-ai/iFixAi", "cloudflare/cloudflare-os", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "emilkowalski/skills", "floci-io/floci", "andrewyng/openworker", "herdrdev/herdr", "cathrynlavery/diagram-design", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "virgiliojr94/book-to-skill", "stablyai/orca", "bojieli/ai-agent-book", "block/buzz", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [56, 59, 60, 60, 61, 63, 70, 73, 81, 81, 86, 88, 89, 94, 116, 133, 134, 150, 154, 253]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +12 | 13539 |
| 2 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 10618 |
| 3 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +5 | 14392 |
| 4 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +5 | 3953 |
| 5 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +4 | 1496 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +4 | 26304 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 48182 |
| 8 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3 | 14197 |
| 9 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +3 | 6646 |
| 10 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +3 | 9805 |
| 11 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 39046 |
| 12 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +3 | 21624 |
| 13 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2 | 19327 |
| 14 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +2 | 47754 |
| 15 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +2 | 2647 |
| 16 | [blader/humanizer](https://github.com/blader/humanizer) | +2 | 36368 |
| 17 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 11980 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 63290 |
| 19 | [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | +2 | 3871 |
| 20 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 44771 |
| 21 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +2 | 12010 |
| 22 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2 | 23383 |
| 23 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +2 | 3729 |
| 24 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 258 |
| 25 | [JesseCHale/HaleHound-CYD](https://github.com/JesseCHale/HaleHound-CYD) | +1 | 1577 |
| 26 | [Qwejay/QPyPack](https://github.com/Qwejay/QPyPack) | +1 | 98 |
| 27 | [shitagaki-lab/see-through](https://github.com/shitagaki-lab/see-through) | +1 | 3571 |
| 28 | [guocong-bincai/ai-interview-guide](https://github.com/guocong-bincai/ai-interview-guide) | +1 | 455 |
| 29 | [XIAZY/wcctl](https://github.com/XIAZY/wcctl) | +1 | 100 |
| 30 | [ServiceNow/ServiceNowDocs](https://github.com/ServiceNow/ServiceNowDocs) | +1 | 447 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +69 | 21624 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +52 | 14392 |
| 3 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +43 | 13539 |
| 4 | [spinabot/brigade](https://github.com/spinabot/brigade) | +23 | 2885 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +22 | 48182 |
| 6 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +22 | 3729 |
| 7 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +21 | 17163 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +20 | 47754 |
| 9 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +17 | 7456 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +15 | 30320 |
| 11 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +14 | 39046 |
| 12 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +14 | 23383 |
| 13 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +14 | 3481 |
| 14 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +13 | 3996 |
| 15 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +13 | 16961 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +12 | 36297 |
| 17 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +12 | 10228 |
| 18 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +11 | 26304 |
| 19 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +11 | 22949 |
| 20 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +11 | 6274 |
| 21 | [block/buzz](https://github.com/block/buzz) | +10 | 28356 |
| 22 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +10 | 6646 |
| 23 | [yc-software/qm](https://github.com/yc-software/qm) | +10 | 13878 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +10 | 30247 |
| 25 | [every-app/open-seo](https://github.com/every-app/open-seo) | +10 | 12532 |
| 26 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +10 | 4168 |
| 27 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +9 | 10618 |
| 28 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +9 | 3953 |
| 29 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +9 | 9805 |
| 30 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +9 | 11003 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +9 | 14197 |
| 32 | [macro-inc/macro](https://github.com/macro-inc/macro) | +9 | 3645 |
| 33 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +9 | 50402 |
| 34 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | +9 | 1965 |
| 35 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +8 | 63290 |
| 36 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +8 | 21919 |
| 37 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +8 | 48761 |
| 38 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 44771 |
| 39 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +8 | 4165 |
| 40 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 36368 |
| 41 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +8 | 28735 |
| 42 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47772 |
| 43 | [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) | +7 | 567 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +7 | 46688 |
| 45 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +7 | 22824 |
| 46 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7728 |
| 47 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +6 | 19327 |
| 48 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 11980 |
| 49 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +6 | 12152 |
| 50 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +6 | 20733 |
| 51 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +6 | 2136 |
| 52 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +6 | 1213 |
| 53 | [brightdata/cli](https://github.com/brightdata/cli) | +6 | 6209 |
| 54 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +6 | 8926 |
| 55 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 2554 |
| 56 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +5 | 1496 |
| 57 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 11274 |
| 58 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +5 | 14267 |
| 59 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +5 | 12010 |
| 60 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 30354 |
| 61 | [xr843/insect-world](https://github.com/xr843/insect-world) | +5 | 397 |
| 62 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 8244 |
| 63 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +5 | 32400 |
| 64 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +5 | 2896 |
| 65 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +5 | 1883 |
| 66 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +5 | 25429 |
| 67 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +5 | 355 |
| 68 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 35867 |
| 69 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +5 | 1860 |
| 70 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 757 |
| 71 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +5 | 16122 |
| 72 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 15634 |
| 73 | [ZJU-REAL/HugAgentOS](https://github.com/ZJU-REAL/HugAgentOS) | +5 | 440 |
| 74 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +5 | 5997 |
| 75 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +5 | 571 |
| 76 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +5 | 1784 |
| 77 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +4 | 1226 |
| 78 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 3715 |
| 79 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +4 | 4914 |
| 80 | [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | +4 | 3430 |
| 81 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 32243 |
| 82 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 31219 |
| 83 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4 | 33829 |
| 84 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +4 | 4900 |
| 85 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +4 | 7482 |
| 86 | [vercel-labs/eve-software-factory-template](https://github.com/vercel-labs/eve-software-factory-template) | +4 | 907 |
| 87 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +4 | 17932 |
| 88 | [datawhalechina/deepagents-in-action](https://github.com/datawhalechina/deepagents-in-action) | +4 | 1698 |
| 89 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +4 | 15745 |
| 90 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +4 | 8571 |
| 91 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 22616 |
| 92 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +4 | 6364 |
| 93 | [OpenLabs-so/openanalytics](https://github.com/OpenLabs-so/openanalytics) | +4 | 237 |
| 94 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 30519 |
| 95 | [tanishqkancharla/calldiff](https://github.com/tanishqkancharla/calldiff) | +4 | 417 |
| 96 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | +4 | 473 |
| 97 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 45898 |
| 98 | [rukamori/ArchiveTune](https://github.com/rukamori/ArchiveTune) | +3 | 4734 |
| 99 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +3 | 41551 |
| 100 | [trycompai/crm](https://github.com/trycompai/crm) | +3 | 8601 |
| 101 | [AML-memory/agent-memory-leaderboard](https://github.com/AML-memory/agent-memory-leaderboard) | +3 | 738 |
| 102 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +3 | 1409 |
| 103 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +3 | 1546 |
| 104 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +3 | 1892 |
| 105 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +3 | 24427 |
| 106 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 5886 |
| 107 | [waiterve/wai-play](https://github.com/waiterve/wai-play) | +3 | 27 |
| 108 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 33670 |
| 109 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +3 | 2494 |
| 110 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | +3 | 637 |
| 111 | [agegr/pi-web](https://github.com/agegr/pi-web) | +2 | 4733 |
| 112 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +2 | 6742 |
| 113 | [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | +2 | 3871 |
| 114 | [yuwen-cool/yuwen-publish-precheck](https://github.com/yuwen-cool/yuwen-publish-precheck) | +2 | 578 |
| 115 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +2 | 29070 |
| 116 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +2 | 3116 |
| 117 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +2 | 16764 |
| 118 | [xinxinshuhao-create/grok-register](https://github.com/xinxinshuhao-create/grok-register) | +2 | 455 |
| 119 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 17451 |
| 120 | [akfamily/akquant](https://github.com/akfamily/akquant) | +2 | 2046 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +253 | 17163 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +154 | 16961 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +150 | 50402 |
| 4 | [block/buzz](https://github.com/block/buzz) | +134 | 28356 |
| 5 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +133 | 39046 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +116 | 48182 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +94 | 22824 |
| 8 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +89 | 21919 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +88 | 26304 |
| 10 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +86 | 21624 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +81 | 30320 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14782 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 20473 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +70 | 30247 |
| 15 | [brightdata/cli](https://github.com/brightdata/cli) | +63 | 6209 |
| 16 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +61 | 22949 |
| 17 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8560 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +60 | 10618 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +59 | 18561 |
| 20 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +56 | 32243 |
| 21 | [oblien/openship](https://github.com/oblien/openship) | +56 | 11002 |
| 22 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +55 | 16122 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +55 | 47755 |
| 24 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +53 | 11003 |
| 25 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +53 | 24073 |
| 26 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +52 | 14392 |
| 27 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21538 |
| 28 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +50 | 28735 |
| 29 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +46 | 12152 |
| 30 | [yc-software/qm](https://github.com/yc-software/qm) | +45 | 13878 |
| 31 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +45 | 6274 |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +45 | 36297 |
| 33 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +45 | 30519 |
| 34 | [google/skills](https://github.com/google/skills) | +44 | 18471 |
| 35 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +44 | 14197 |
| 36 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +44 | 15745 |
| 37 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +44 | 8959 |
| 38 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +43 | 13539 |
| 39 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1458 |
| 40 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +43 | 25429 |
| 41 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +42 | 20733 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +41 | 63290 |
| 43 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +41 | 34775 |
| 44 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 25650 |
| 45 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +40 | 31219 |
| 46 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +39 | 47104 |
| 47 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8510 |
| 48 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +39 | 33988 |
| 49 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5415 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +37 | 17932 |
| 51 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8601 |
| 52 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +36 | 48761 |
| 53 | [blader/humanizer](https://github.com/blader/humanizer) | +36 | 36368 |
| 54 | [every-app/open-seo](https://github.com/every-app/open-seo) | +35 | 12532 |
| 55 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +34 | 11841 |
| 56 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +33 | 3996 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9953 |
| 58 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +33 | 39404 |
| 59 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10228 |
| 60 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +32 | 41551 |
| 61 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +32 | 6364 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 44771 |
| 63 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +31 | 15295 |
| 64 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 35867 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 46688 |
| 66 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +29 | 19327 |
| 67 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4900 |
| 68 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 22616 |
| 69 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 21626 |
| 70 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +25 | 2685 |
| 71 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24623 |
| 72 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 2318 |
| 73 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 840 |
| 74 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 32400 |
| 75 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +25 | 8906 |
| 76 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +25 | 8082 |
| 77 | [spinabot/brigade](https://github.com/spinabot/brigade) | +24 | 2885 |
| 78 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +24 | 3216 |
| 79 | [malisper/pgrust](https://github.com/malisper/pgrust) | +24 | 4564 |
| 80 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +24 | 11980 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4070 |
| 82 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +23 | 4168 |
| 83 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 8926 |
| 84 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +22 | 3729 |
| 85 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +22 | 13903 |
| 86 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +21 | 1077 |
| 87 | [browser-use/video-use](https://github.com/browser-use/video-use) | +21 | 21044 |
| 88 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +21 | 5322 |
| 89 | [t8y2/dbx](https://github.com/t8y2/dbx) | +21 | 15634 |
| 90 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6143 |
| 91 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8611 |
| 92 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +19 | 45898 |
| 93 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +19 | 7456 |
| 94 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 5886 |
| 95 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +19 | 14475 |
| 96 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +18 | 5505 |
| 97 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13603 |
| 98 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 10150 |
| 99 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +17 | 9254 |
| 100 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +17 | 4165 |
| 101 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +17 | 5935 |
| 102 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 8244 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47772 |
| 104 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +16 | 42934 |
| 105 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11214 |
| 106 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +15 | 0 |
| 107 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +15 | 8296 |
| 108 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6479 |
| 109 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 4914 |
| 110 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +14 | 23383 |
| 111 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +14 | 3481 |
| 112 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30354 |
| 113 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 742 |
| 114 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16122 |
| 115 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2333 |
| 116 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2095 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3997 |
| 118 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +13 | 3081 |
| 119 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +13 | 1892 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 20184 |
| 121 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 5997 |
| 122 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2281 |
| 123 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +13 | 11274 |
| 124 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 125 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2136 |
| 126 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 845 |
| 127 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1440 |
| 128 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2604 |
| 129 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +12 | 9020 |
| 130 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 3010 |
| 131 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12 | 10072 |
| 132 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +12 | 16549 |
| 133 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 32030 |
| 134 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4895 |
| 135 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +11 | 1700 |
| 136 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +11 | 2849 |
| 137 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +11 | 2441 |
| 138 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5982 |
| 139 | [decolua/9router](https://github.com/decolua/9router) | +11 | 25742 |
| 140 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 8709 |
| 141 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 33829 |
| 142 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 30888 |
| 143 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2299 |
| 144 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +10 | 355 |
| 145 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +10 | 27757 |
| 146 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1052 |
| 147 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1907 |
| 148 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 3674 |
| 149 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 382 |
| 150 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 151 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1684 |
| 152 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +9 | 14267 |
| 153 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 376 |
| 154 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 571 |
| 155 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1024 |
| 156 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +9 | 47146 |
| 157 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1009 |
| 158 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3717 |
| 159 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +9 | 10645 |
| 160 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 29270 |
| 161 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5694 |
| 162 | [openai/skills](https://github.com/openai/skills) | +9 | 25019 |
| 163 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1366 |
| 164 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +9 | 1687 |
| 165 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1931 |
| 166 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24427 |
| 167 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1213 |
| 168 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1608 |
| 169 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +8 | 2896 |
| 170 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +8 | 1546 |
| 171 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +8 | 1025 |
| 172 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8760 |
| 173 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 10160 |
| 174 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2502 |
| 175 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28317 |
| 176 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8420 |
| 177 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10683 |
| 178 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +7 | 14748 |
| 179 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6751 |
| 180 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6153 |
| 181 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41094 |
| 182 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +7 | 45099 |
| 183 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +7 | 3116 |
| 184 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +7 | 1406 |
| 185 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6647 |
| 186 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1435 |
| 187 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 188 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 3401 |
| 189 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +6 | 2554 |
| 190 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1514 |
| 191 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 192 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 276 |
| 193 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27475 |
| 194 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 307 |
| 195 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 487 |
| 196 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5736 |
| 197 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14651 |
| 198 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30169 |
| 199 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +6 | 3274 |
| 200 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5582 |
| 201 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +5 | 542 |
| 202 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 559 |
| 203 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5765 |
| 204 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +5 | 11471 |
| 205 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 556 |
| 206 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 806 |
| 207 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8677 |
| 208 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +5 | 10042 |
| 209 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 532 |
| 210 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1353 |
| 211 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 696 |
| 212 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 350 |
| 213 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1221 |
| 214 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +4 | 1163 |
| 215 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3070 |
| 216 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7220 |
| 217 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 221 |
| 218 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10458 |
| 219 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 458 |
| 220 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4881 |
| 221 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1172 |
| 222 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5219 |
| 223 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5110 |
| 224 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +4 | 1340 |
| 225 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3441 |
| 226 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9639 |
| 227 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +4 | 2184 |
| 228 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 422 |
| 229 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +4 | 1905 |
| 230 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3662 |
| 231 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3343 |
| 232 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 108 |
| 233 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 995 |
| 234 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4757 |
| 235 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 247 |
| 236 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 185 |
| 237 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +3 | 573 |
| 238 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +3 | 548 |
| 239 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 549 |
| 240 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 614 |
| 241 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9594 |
| 242 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 191 |
| 243 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 381 |
| 244 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1196 |
| 245 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12364 |
| 246 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3107 |
| 247 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 949 |
| 248 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 347 |
| 249 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 587 |
| 250 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18992 |
| 251 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 807 |
| 252 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 455 |
| 253 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 254 | [Saganaki22/AgebypassX](https://github.com/Saganaki22/AgebypassX) | +3 | 340 |
| 255 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 423 |
| 256 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 928 |
| 257 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 579 |
| 258 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +3 | 283 |
| 259 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 314 |
| 260 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1214 |
| 261 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 8962 |
| 262 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28548 |
| 263 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 860 |
| 264 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2069 |
| 265 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 728 |
| 266 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 900 |
| 267 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 158 |
| 268 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 412 |
| 269 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1360 |
| 270 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 4011 |
| 271 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1074 |
| 272 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 689 |
| 273 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +2 | 154 |
| 274 | [thangnq111203/oss-steward](https://github.com/thangnq111203/oss-steward) | +2 | 90 |
| 275 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +2 | 600 |
| 276 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 893 |
| 277 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 101 |
| 278 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 437 |
| 279 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 114 |
| 280 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 148 |
| 281 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 217 |
| 282 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 352 |
| 283 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2905 |
| 284 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5125 |
| 285 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3190 |
| 286 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +2 | 3276 |
| 287 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1211 |
| 288 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1403 |
| 289 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 513 |
| 290 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2563 |
| 291 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3810 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 293 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2714 |
| 294 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 124 |
| 295 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 100 |
| 296 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +1 | 258 |
| 297 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1311 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 921 |
| 299 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3633 |
| 300 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 94 |
