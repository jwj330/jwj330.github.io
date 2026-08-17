---
title: "2026-08-17 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+9 2.needle+5 3.ai-agent-book+3 4.ppt-master+2 5.diagram-design+2"
date: 2026-08-17T20:28:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-17 20:28:19

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
        'daily': {"categories": ["yuanzhongqiao/printfilm", "whiteguo233/OpenBiliClaw", "xr843/insect-world", "CalvinXKY/InfraTech", "t8y2/dbx", "guillaumemeyer/watermarks-remover", "arvin341az-glitch/RVG", "larashero3-dotcom/lieflat-charts", "amirappleidfd-stack/spider--panel", "Gaurav-Gosain/tuios", "43PR/dotfiles", "pathwaycom/arc-task-gen", "hydra-db/hydradb", "freestylefly/awesome-gpt-image-2", "internet-court/internet-court-skill", "cathrynlavery/diagram-design", "hugohe3/ppt-master", "bojieli/ai-agent-book", "cactus-compute/needle", "anywhere-labs/deepseek-harness-desktop"], "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 5, 9]},
        'weekly': {"categories": ["emilkowalski/skills", "titanwings/colleague-skill", "corsairdev/corsair", "zhaoxuya520/reverse-skill", "pathwaycom/arc-task-gen", "bojieli/ai-agent-book", "HKUDS/DeepTutor", "TencentCloud/TencentDB-Agent-Memory", "firecrawl/anydoc", "herdrdev/herdr", "Zeejay0/gathered-scenes-zine-skill", "cactus-compute/needle", "MiniMax-AI/MiniMax-H3", "hugohe3/ppt-master", "stablyai/orca", "spinabot/brigade", "PrimeIntellect-ai/prime-agent", "anywhere-labs/deepseek-harness-desktop", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [12, 12, 14, 14, 14, 14, 15, 15, 16, 16, 16, 19, 20, 21, 21, 23, 28, 34, 47, 75]},
        'monthly': {"categories": ["oblien/openship", "MadsLorentzen/ai-job-search", "k1tbyte/Wand-Enhancer", "cloudflare/cloudflare-os", "brightdata/cli", "TencentCloud/TencentDB-Agent-Memory", "floci-io/floci", "emilkowalski/skills", "andrewyng/openworker", "cathrynlavery/diagram-design", "zhaoxuya520/reverse-skill", "herdrdev/herdr", "ayghri/i-have-adhd", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [56, 56, 58, 60, 63, 63, 73, 75, 81, 83, 84, 85, 88, 94, 116, 133, 138, 154, 154, 252]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +9 | 11573 |
| 2 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +5 | 7080 |
| 3 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 38475 |
| 4 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +2 | 47484 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2 | 20504 |
| 6 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +2 | 3435 |
| 7 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +2 | 11046 |
| 8 | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | +2 | 496 |
| 9 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +2 | 3313 |
| 10 | [43PR/dotfiles](https://github.com/43PR/dotfiles) | +2 | 534 |
| 11 | [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | +2 | 3323 |
| 12 | [amirappleidfd-stack/spider--panel](https://github.com/amirappleidfd-stack/spider--panel) | +1 | 971 |
| 13 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +1 | 1162 |
| 14 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +1 | 2292 |
| 15 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +1 | 13273 |
| 16 | [t8y2/dbx](https://github.com/t8y2/dbx) | +1 | 15320 |
| 17 | [CalvinXKY/InfraTech](https://github.com/CalvinXKY/InfraTech) | +1 | 3549 |
| 18 | [xr843/insect-world](https://github.com/xr843/insect-world) | +1 | 340 |
| 19 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +1 | 2837 |
| 20 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +1 | 3592 |
| 21 | [tornadus/frlg-ldn-trade](https://github.com/tornadus/frlg-ldn-trade) | +1 | 93 |
| 22 | [guocong-bincai/ai-interview-guide](https://github.com/guocong-bincai/ai-interview-guide) | +1 | 440 |
| 23 | [MGdaasLab/WHartTest](https://github.com/MGdaasLab/WHartTest) | +1 | 995 |
| 24 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +1 | 49757 |
| 25 | [MengTo/kage](https://github.com/MengTo/kage) | +1 | 1111 |
| 26 | [VexDB-THU/VexDB-Lite](https://github.com/VexDB-THU/VexDB-Lite) | +1 | 2046 |
| 27 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +1 | 28278 |
| 28 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +1 | 14154 |
| 29 | [Nagi-ovo/voyager](https://github.com/Nagi-ovo/voyager) | +1 | 19591 |
| 30 | [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) | +1 | 397 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +75 | 20504 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +47 | 13273 |
| 3 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +34 | 11573 |
| 4 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +28 | 16880 |
| 5 | [spinabot/brigade](https://github.com/spinabot/brigade) | +23 | 2809 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +21 | 47309 |
| 7 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +21 | 47484 |
| 8 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +20 | 6130 |
| 9 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +19 | 7080 |
| 10 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +16 | 3888 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +16 | 30018 |
| 12 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +16 | 16686 |
| 13 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +15 | 22587 |
| 14 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +15 | 36123 |
| 15 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +14 | 38475 |
| 16 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +14 | 3313 |
| 17 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +14 | 25994 |
| 18 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +14 | 10314 |
| 19 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +12 | 23130 |
| 20 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +12 | 30031 |
| 21 | [every-app/open-seo](https://github.com/every-app/open-seo) | +12 | 12361 |
| 22 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +12 | 1774 |
| 23 | [block/buzz](https://github.com/block/buzz) | +11 | 27930 |
| 24 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +11 | 4034 |
| 25 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 10681 |
| 26 | [yc-software/qm](https://github.com/yc-software/qm) | +10 | 13788 |
| 27 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +10 | 28618 |
| 28 | [macro-inc/macro](https://github.com/macro-inc/macro) | +9 | 3526 |
| 29 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +9 | 21383 |
| 30 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +9 | 4107 |
| 31 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | +9 | 1804 |
| 32 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +9 | 12047 |
| 33 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +9 | 49757 |
| 34 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +9 | 22512 |
| 35 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +8 | 48582 |
| 36 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 46471 |
| 37 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1173 |
| 38 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +7 | 9155 |
| 39 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47707 |
| 40 | [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) | +7 | 519 |
| 41 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +7 | 6280 |
| 42 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7703 |
| 43 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +7 | 19069 |
| 44 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 35667 |
| 45 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 36148 |
| 46 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +7 | 15974 |
| 47 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +7 | 568 |
| 48 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +7 | 8885 |
| 49 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 63157 |
| 50 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +6 | 13830 |
| 51 | [t8y2/dbx](https://github.com/t8y2/dbx) | +6 | 15320 |
| 52 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 25319 |
| 53 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 44622 |
| 54 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +6 | 2111 |
| 55 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +6 | 20660 |
| 56 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 32305 |
| 57 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +6 | 1867 |
| 58 | [brightdata/cli](https://github.com/brightdata/cli) | +6 | 6082 |
| 59 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 2292 |
| 60 | [xr843/insect-world](https://github.com/xr843/insect-world) | +5 | 340 |
| 61 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +5 | 2837 |
| 62 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 11046 |
| 63 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 8171 |
| 64 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +5 | 1858 |
| 65 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +5 | 327 |
| 66 | [floci-io/floci](https://github.com/floci-io/floci) | +5 | 20310 |
| 67 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +5 | 1791 |
| 68 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 643 |
| 69 | [different-ai/openwork](https://github.com/different-ai/openwork) | +5 | 22546 |
| 70 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +5 | 5460 |
| 71 | [ZJU-REAL/HugAgentOS](https://github.com/ZJU-REAL/HugAgentOS) | +5 | 411 |
| 72 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +5 | 5964 |
| 73 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +5 | 11806 |
| 74 | [Kylin010/tcpfit](https://github.com/Kylin010/tcpfit) | +5 | 477 |
| 75 | [AntigmaLabs/ante](https://github.com/AntigmaLabs/ante) | +5 | 1798 |
| 76 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 34676 |
| 77 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +5 | 2417 |
| 78 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +5 | 18574 |
| 79 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 2287 |
| 80 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +5 | 24001 |
| 81 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +4 | 4895 |
| 82 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +4 | 1162 |
| 83 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +4 | 3435 |
| 84 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 3665 |
| 85 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +4 | 4859 |
| 86 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +4 | 14154 |
| 87 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +4 | 30286 |
| 88 | [vercel-labs/eve-software-factory-template](https://github.com/vercel-labs/eve-software-factory-template) | +4 | 878 |
| 89 | [AML-memory/agent-memory-leaderboard](https://github.com/AML-memory/agent-memory-leaderboard) | +4 | 686 |
| 90 | [OpenLabs-so/openanalytics](https://github.com/OpenLabs-so/openanalytics) | +4 | 224 |
| 91 | [tanishqkancharla/calldiff](https://github.com/tanishqkancharla/calldiff) | +4 | 416 |
| 92 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +4 | 5458 |
| 93 | [VexDB-THU/VexDB-Lite](https://github.com/VexDB-THU/VexDB-Lite) | +4 | 2046 |
| 94 | [gastownhall/beads](https://github.com/gastownhall/beads) | +4 | 26394 |
| 95 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 30432 |
| 96 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 9748 |
| 97 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | +4 | 449 |
| 98 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +4 | 3636 |
| 99 | [trycompai/crm](https://github.com/trycompai/crm) | +3 | 8563 |
| 100 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +3 | 41377 |
| 101 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +3 | 3592 |
| 102 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 40788 |
| 103 | [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | +3 | 3323 |
| 104 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 32083 |
| 105 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 31095 |
| 106 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +3 | 1373 |
| 107 | [1537271403/paypal-agreement-protocol](https://github.com/1537271403/paypal-agreement-protocol) | +3 | 202 |
| 108 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +3 | 1509 |
| 109 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +3 | 33741 |
| 110 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +3 | 1619 |
| 111 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +3 | 24380 |
| 112 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 5796 |
| 113 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 15660 |
| 114 | [waiterve/wai-play](https://github.com/waiterve/wai-play) | +3 | 26 |
| 115 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 20100 |
| 116 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 33617 |
| 117 | [IAmIronMan42/MiniMax-H3-FineTuning](https://github.com/IAmIronMan42/MiniMax-H3-FineTuning) | +3 | 55 |
| 118 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 4894 |
| 119 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +3 | 2474 |
| 120 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | +3 | 631 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +252 | 16880 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +154 | 16686 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +154 | 49757 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +138 | 38475 |
| 5 | [block/buzz](https://github.com/block/buzz) | +133 | 27931 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +116 | 47309 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +94 | 22512 |
| 8 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +88 | 21383 |
| 9 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +85 | 30018 |
| 10 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +84 | 25994 |
| 11 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +83 | 20504 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14723 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +75 | 30031 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 20310 |
| 15 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +63 | 22587 |
| 16 | [brightdata/cli](https://github.com/brightdata/cli) | +63 | 6082 |
| 17 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8489 |
| 18 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +58 | 18279 |
| 19 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +56 | 32083 |
| 20 | [oblien/openship](https://github.com/oblien/openship) | +56 | 10925 |
| 21 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +55 | 15974 |
| 22 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +54 | 9748 |
| 23 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +54 | 28618 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +53 | 47484 |
| 25 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +53 | 10681 |
| 26 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +53 | 24001 |
| 27 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21510 |
| 28 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +48 | 30432 |
| 29 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +47 | 13273 |
| 30 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +46 | 12047 |
| 31 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +45 | 6130 |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +45 | 36123 |
| 33 | [yc-software/qm](https://github.com/yc-software/qm) | +44 | 13788 |
| 34 | [google/skills](https://github.com/google/skills) | +44 | 18432 |
| 35 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +44 | 25319 |
| 36 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1451 |
| 37 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +43 | 15660 |
| 38 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +43 | 8489 |
| 39 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +41 | 20660 |
| 40 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +41 | 13830 |
| 41 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +41 | 34676 |
| 42 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 25429 |
| 43 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +41 | 47027 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 63157 |
| 45 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +40 | 33860 |
| 46 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +39 | 31095 |
| 47 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8489 |
| 48 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +38 | 17842 |
| 49 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5320 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8563 |
| 51 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 12361 |
| 52 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +35 | 3888 |
| 53 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +35 | 48582 |
| 54 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 36148 |
| 55 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +34 | 11573 |
| 56 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9916 |
| 57 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 41377 |
| 58 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +33 | 39258 |
| 59 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +33 | 11464 |
| 60 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10314 |
| 61 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +32 | 15237 |
| 62 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +32 | 35667 |
| 63 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +31 | 6290 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 44622 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +29 | 46471 |
| 66 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +28 | 13845 |
| 67 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +27 | 19069 |
| 68 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 8041 |
| 69 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4859 |
| 70 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 22546 |
| 71 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 21533 |
| 72 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +25 | 2685 |
| 73 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24567 |
| 74 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 2250 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 840 |
| 76 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +25 | 8698 |
| 77 | [spinabot/brigade](https://github.com/spinabot/brigade) | +24 | 2809 |
| 78 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +24 | 3194 |
| 79 | [malisper/pgrust](https://github.com/malisper/pgrust) | +24 | 4541 |
| 80 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 32305 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4048 |
| 82 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +24 | 11806 |
| 83 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 8885 |
| 84 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +22 | 4034 |
| 85 | [browser-use/video-use](https://github.com/browser-use/video-use) | +22 | 20934 |
| 86 | [t8y2/dbx](https://github.com/t8y2/dbx) | +22 | 15320 |
| 87 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +22 | 29109 |
| 88 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +21 | 1060 |
| 89 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6122 |
| 90 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +20 | 5250 |
| 91 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8575 |
| 92 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +19 | 7080 |
| 93 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +19 | 45707 |
| 94 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +19 | 5796 |
| 95 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +19 | 14336 |
| 96 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +19 | 10074 |
| 97 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +18 | 5460 |
| 98 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +18 | 47707 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13552 |
| 100 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5905 |
| 101 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +17 | 9144 |
| 102 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +17 | 4107 |
| 103 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +17 | 2487 |
| 104 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 42807 |
| 105 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +17 | 8266 |
| 106 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11204 |
| 107 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +15 | 0 |
| 108 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +15 | 8171 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6458 |
| 110 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 4895 |
| 111 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +14 | 3313 |
| 112 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 728 |
| 113 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30286 |
| 114 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16086 |
| 115 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2287 |
| 116 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2088 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3999 |
| 118 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +13 | 3076 |
| 119 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +13 | 1867 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 20100 |
| 121 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +13 | 8983 |
| 122 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 5964 |
| 123 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2264 |
| 124 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 125 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2111 |
| 126 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 840 |
| 127 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +12 | 23130 |
| 128 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1436 |
| 129 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2584 |
| 130 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2962 |
| 131 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12 | 10029 |
| 132 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +12 | 11046 |
| 133 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 31983 |
| 134 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +11 | 1619 |
| 135 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +11 | 8671 |
| 136 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +11 | 2417 |
| 137 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5964 |
| 138 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +11 | 16531 |
| 139 | [decolua/9router](https://github.com/decolua/9router) | +11 | 25664 |
| 140 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4882 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +10 | 2813 |
| 142 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 30813 |
| 143 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10620 |
| 144 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2283 |
| 145 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +10 | 327 |
| 146 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1034 |
| 147 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1886 |
| 148 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 3670 |
| 149 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 150 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 381 |
| 151 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1671 |
| 152 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 358 |
| 153 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 568 |
| 154 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +9 | 47100 |
| 155 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 993 |
| 156 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1003 |
| 157 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +9 | 33741 |
| 158 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3634 |
| 159 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28883 |
| 160 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8715 |
| 161 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5651 |
| 162 | [openai/skills](https://github.com/openai/skills) | +9 | 25004 |
| 163 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1342 |
| 164 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +9 | 15645 |
| 165 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +9 | 1642 |
| 166 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +9 | 27685 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1897 |
| 168 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +9 | 3383 |
| 169 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24380 |
| 170 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1173 |
| 171 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +8 | 14154 |
| 172 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1592 |
| 173 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +8 | 2837 |
| 174 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +8 | 1509 |
| 175 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +8 | 6134 |
| 176 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +8 | 978 |
| 177 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +8 | 45062 |
| 178 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9958 |
| 179 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 4894 |
| 180 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2414 |
| 181 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28278 |
| 182 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8361 |
| 183 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10669 |
| 184 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +7 | 14709 |
| 185 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6747 |
| 186 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41081 |
| 187 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +7 | 1396 |
| 188 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6603 |
| 189 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1416 |
| 190 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 38 |
| 191 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +6 | 2292 |
| 192 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 193 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 275 |
| 194 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27446 |
| 195 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 299 |
| 196 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 479 |
| 197 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +6 | 10006 |
| 198 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14641 |
| 199 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30136 |
| 200 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +6 | 3267 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5578 |
| 202 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1509 |
| 203 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 490 |
| 204 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5716 |
| 205 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +5 | 11450 |
| 206 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 545 |
| 207 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 795 |
| 208 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +5 | 10440 |
| 209 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5719 |
| 210 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 1164 |
| 211 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8655 |
| 212 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 529 |
| 213 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1348 |
| 214 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 696 |
| 215 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +5 | 2180 |
| 216 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +5 | 1899 |
| 217 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 331 |
| 218 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1217 |
| 219 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3057 |
| 220 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7207 |
| 221 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 447 |
| 222 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4880 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5211 |
| 224 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5110 |
| 225 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +4 | 1324 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3421 |
| 227 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9624 |
| 228 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 419 |
| 229 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3592 |
| 230 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3335 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 107 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 969 |
| 233 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4736 |
| 234 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 182 |
| 235 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +3 | 559 |
| 236 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 1131 |
| 237 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +3 | 522 |
| 238 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 533 |
| 239 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 598 |
| 240 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9559 |
| 241 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 191 |
| 242 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 374 |
| 243 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1182 |
| 244 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12343 |
| 245 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3070 |
| 246 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 936 |
| 247 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 346 |
| 248 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 573 |
| 249 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18981 |
| 250 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3457 |
| 251 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 796 |
| 252 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 454 |
| 253 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 254 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 422 |
| 255 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 922 |
| 256 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 577 |
| 257 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +3 | 347 |
| 258 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +3 | 274 |
| 259 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 308 |
| 260 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1205 |
| 261 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2060 |
| 262 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +3 | 3259 |
| 263 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 8957 |
| 264 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28505 |
| 265 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 848 |
| 266 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 724 |
| 267 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 895 |
| 268 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 152 |
| 269 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 331 |
| 270 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1347 |
| 271 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 4000 |
| 272 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1072 |
| 273 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 688 |
| 274 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +2 | 153 |
| 275 | [thangnq111203/oss-steward](https://github.com/thangnq111203/oss-steward) | +2 | 91 |
| 276 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +2 | 594 |
| 277 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +2 | 1622 |
| 278 | [SamurAIGPT/seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) | +2 | 76 |
| 279 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 889 |
| 280 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 101 |
| 281 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 429 |
| 282 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 111 |
| 283 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 139 |
| 284 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 211 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2905 |
| 286 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5102 |
| 287 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3182 |
| 288 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1202 |
| 289 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1400 |
| 290 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 513 |
| 291 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2558 |
| 292 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3809 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 294 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2714 |
| 295 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 116 |
| 296 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 99 |
| 297 | [OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL](https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL) | +1 | 640 |
| 298 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | +1 | 109 |
| 299 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1304 |
| 300 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 907 |
