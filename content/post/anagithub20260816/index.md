---
title: "2026-08-16 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+7 2.diagram-design+5 3.opencodex+4 4.skills+3 5.awesome-free-models+2"
date: 2026-08-16T20:23:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-16 20:23:19

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
        'daily': {"categories": ["KKKKhazix/khazix-skills", "openchamber/openchamber", "Yu9191/wloc", "docling-project/docling-graph", "titanwings/colleague-skill", "pathwaycom/arc-task-gen", "xingkongliang/skills-manager", "cactus-compute/needle", "PrimeIntellect-ai/prime-agent", "herdrdev/herdr", "internet-court/internet-court-skill", "guillaumemeyer/watermarks-remover", "different-ai/openwork", "ChartGPU/ChartGPU", "HKUDS/CLI-Anything", "12britz/awesome-free-models", "emilkowalski/skills", "lidge-jun/opencodex", "cathrynlavery/diagram-design", "anywhere-labs/deepseek-harness-desktop"], "data": [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 7]},
        'weekly': {"categories": ["titanwings/colleague-skill", "Zeejay0/gathered-scenes-zine-skill", "block/buzz", "TencentCloud/TencentDB-Agent-Memory", "every-app/open-seo", "emilkowalski/skills", "cactus-compute/needle", "HKUDS/DeepTutor", "corsairdev/corsair", "hugohe3/ppt-master", "herdrdev/herdr", "zhaoxuya520/reverse-skill", "firecrawl/anydoc", "MiniMax-AI/MiniMax-H3", "spinabot/brigade", "anywhere-labs/deepseek-harness-desktop", "stablyai/orca", "PrimeIntellect-ai/prime-agent", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [12, 13, 13, 14, 14, 14, 14, 16, 17, 19, 19, 20, 20, 21, 22, 23, 25, 35, 47, 73]},
        'monthly': {"categories": ["iOfficeAI/OfficeCLI", "MadsLorentzen/ai-job-search", "cloudflare/cloudflare-os", "TencentCloud/TencentDB-Agent-Memory", "k1tbyte/Wand-Enhancer", "brightdata/cli", "floci-io/floci", "andrewyng/openworker", "cathrynlavery/diagram-design", "zhaoxuya520/reverse-skill", "emilkowalski/skills", "ayghri/i-have-adhd", "virgiliojr94/book-to-skill", "herdrdev/herdr", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [56, 58, 60, 62, 62, 63, 73, 81, 81, 84, 85, 87, 93, 94, 125, 133, 141, 154, 155, 251]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +7 | 8796 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +5 | 19448 |
| 3 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 10449 |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 29806 |
| 5 | [12britz/awesome-free-models](https://github.com/12britz/awesome-free-models) | +2 | 1704 |
| 6 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 47611 |
| 7 | [ChartGPU/ChartGPU](https://github.com/ChartGPU/ChartGPU) | +2 | 3205 |
| 8 | [different-ai/openwork](https://github.com/different-ai/openwork) | +2 | 22431 |
| 9 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +2 | 11087 |
| 10 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +2 | 2761 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +2 | 29725 |
| 12 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +2 | 16529 |
| 13 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 6483 |
| 14 | [xingkongliang/skills-manager](https://github.com/xingkongliang/skills-manager) | +2 | 3783 |
| 15 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +2 | 3177 |
| 16 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2 | 22796 |
| 17 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +1 | 448 |
| 18 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +1 | 9082 |
| 19 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +1 | 8846 |
| 20 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1 | 19738 |
| 21 | [umputun/agterm](https://github.com/umputun/agterm) | +1 | 473 |
| 22 | [CelestoAI/SmolVM](https://github.com/CelestoAI/SmolVM) | +1 | 770 |
| 23 | [off-grid-ai/OGAM](https://github.com/off-grid-ai/OGAM) | +1 | 2931 |
| 24 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +1 | 48352 |
| 25 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +1 | 7418 |
| 26 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +1 | 1359 |
| 27 | [duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer](https://github.com/duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer) | +1 | 84 |
| 28 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +1 | 17393 |
| 29 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1 | 47065 |
| 30 | [zhiyingzzhou/renewlet](https://github.com/zhiyingzzhou/renewlet) | +1 | 180 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +73 | 19448 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +47 | 11087 |
| 3 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +35 | 16529 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +25 | 46521 |
| 5 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +23 | 8796 |
| 6 | [spinabot/brigade](https://github.com/spinabot/brigade) | +22 | 2732 |
| 7 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +21 | 6048 |
| 8 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +20 | 16434 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +20 | 25664 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +19 | 29725 |
| 11 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +19 | 47252 |
| 12 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +17 | 10271 |
| 13 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +16 | 35937 |
| 14 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +14 | 6483 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +14 | 29806 |
| 16 | [every-app/open-seo](https://github.com/every-app/open-seo) | +14 | 12185 |
| 17 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +14 | 22209 |
| 18 | [block/buzz](https://github.com/block/buzz) | +13 | 27738 |
| 19 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +13 | 3747 |
| 20 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +12 | 22796 |
| 21 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +12 | 37850 |
| 22 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +12 | 3177 |
| 23 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +12 | 1765 |
| 24 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +11 | 21093 |
| 25 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +11 | 28513 |
| 26 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +11 | 3915 |
| 27 | [yc-software/qm](https://github.com/yc-software/qm) | +10 | 13689 |
| 28 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +10 | 10449 |
| 29 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +10 | 49097 |
| 30 | [macro-inc/macro](https://github.com/macro-inc/macro) | +9 | 3387 |
| 31 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +9 | 4041 |
| 32 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +9 | 22164 |
| 33 | [brightdata/cli](https://github.com/brightdata/cli) | +9 | 5802 |
| 34 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +8 | 11936 |
| 35 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 46188 |
| 36 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +8 | 48352 |
| 37 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +8 | 8846 |
| 38 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1122 |
| 39 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +7 | 63036 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47611 |
| 41 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +7 | 6168 |
| 42 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7678 |
| 43 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +7 | 18953 |
| 44 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +7 | 20594 |
| 45 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 35955 |
| 46 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +7 | 15839 |
| 47 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +7 | 565 |
| 48 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +7 | 23911 |
| 49 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 35469 |
| 50 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +6 | 8291 |
| 51 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +6 | 13305 |
| 52 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 25197 |
| 53 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +6 | 8086 |
| 54 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +6 | 301 |
| 55 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +6 | 5935 |
| 56 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +6 | 2079 |
| 57 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 32165 |
| 58 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +5 | 4810 |
| 59 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +5 | 1807 |
| 60 | [floci-io/floci](https://github.com/floci-io/floci) | +5 | 20184 |
| 61 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +5 | 1666 |
| 62 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 643 |
| 63 | [different-ai/openwork](https://github.com/different-ai/openwork) | +5 | 22431 |
| 64 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 15087 |
| 65 | [ZJU-REAL/HugAgentOS](https://github.com/ZJU-REAL/HugAgentOS) | +5 | 380 |
| 66 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 44500 |
| 67 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +5 | 11665 |
| 68 | [Kylin010/tcpfit](https://github.com/Kylin010/tcpfit) | +5 | 463 |
| 69 | [AntigmaLabs/ante](https://github.com/AntigmaLabs/ante) | +5 | 1784 |
| 70 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 34641 |
| 71 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +5 | 5415 |
| 72 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +5 | 2393 |
| 73 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +5 | 6230 |
| 74 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +5 | 1833 |
| 75 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 2241 |
| 76 | [aipoch/open-science](https://github.com/aipoch/open-science) | +5 | 2562 |
| 77 | [google/skills](https://github.com/google/skills) | +5 | 18397 |
| 78 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +4 | 2048 |
| 79 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 3622 |
| 80 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 30342 |
| 81 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 31930 |
| 82 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +4 | 30214 |
| 83 | [xr843/insect-world](https://github.com/xr843/insect-world) | +4 | 286 |
| 84 | [AML-memory/agent-memory-leaderboard](https://github.com/AML-memory/agent-memory-leaderboard) | +4 | 664 |
| 85 | [tanishqkancharla/calldiff](https://github.com/tanishqkancharla/calldiff) | +4 | 410 |
| 86 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +4 | 2730 |
| 87 | [gastownhall/beads](https://github.com/gastownhall/beads) | +4 | 26364 |
| 88 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +4 | 41209 |
| 89 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +4 | 1522 |
| 90 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +4 | 25216 |
| 91 | [pacifio/atlas](https://github.com/pacifio/atlas) | +4 | 1200 |
| 92 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +4 | 8404 |
| 93 | [CYQawa/YunX](https://github.com/CYQawa/YunX) | +4 | 448 |
| 94 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 8794 |
| 95 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | +4 | 426 |
| 96 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +4 | 3622 |
| 97 | [trycompai/crm](https://github.com/trycompai/crm) | +3 | 8512 |
| 98 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 40718 |
| 99 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +3 | 4817 |
| 100 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +3 | 9082 |
| 101 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +3 | 5135 |
| 102 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 31028 |
| 103 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +3 | 1359 |
| 104 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +3 | 13871 |
| 105 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +3 | 24340 |
| 106 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 5721 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 20037 |
| 108 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +3 | 15573 |
| 109 | [waiterve/wai-play](https://github.com/waiterve/wai-play) | +3 | 61 |
| 110 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 33585 |
| 111 | [IAmIronMan42/MiniMax-H3-FineTuning](https://github.com/IAmIronMan42/MiniMax-H3-FineTuning) | +3 | 85 |
| 112 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 4857 |
| 113 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +3 | 2462 |
| 114 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | +3 | 612 |
| 115 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 5337 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +3 | 10946 |
| 117 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3 | 41058 |
| 118 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +3 | 30730 |
| 119 | [ubuntu2310fake/Unikey-Wayland](https://github.com/ubuntu2310fake/Unikey-Wayland) | +2 | 105 |
| 120 | [browser-use/video-use](https://github.com/browser-use/video-use) | +2 | 20794 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +251 | 16529 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 49097 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +154 | 16434 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +141 | 37850 |
| 5 | [block/buzz](https://github.com/block/buzz) | +133 | 27738 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +125 | 46521 |
| 7 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +94 | 29725 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +93 | 22164 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +87 | 21093 |
| 10 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +85 | 29806 |
| 11 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +84 | 25664 |
| 12 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +81 | 19448 |
| 13 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14636 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 20184 |
| 15 | [brightdata/cli](https://github.com/brightdata/cli) | +63 | 5802 |
| 16 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +62 | 18002 |
| 17 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +62 | 22209 |
| 18 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8404 |
| 19 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +58 | 31930 |
| 20 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +56 | 28513 |
| 21 | [oblien/openship](https://github.com/oblien/openship) | +56 | 10820 |
| 22 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +56 | 13789 |
| 23 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +55 | 15839 |
| 24 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +54 | 8794 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +53 | 47252 |
| 26 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +53 | 10449 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +53 | 23911 |
| 28 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21485 |
| 29 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +50 | 35937 |
| 30 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +48 | 25196 |
| 31 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +47 | 11087 |
| 32 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +47 | 13305 |
| 33 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +46 | 15573 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +46 | 30342 |
| 35 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +46 | 31028 |
| 36 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +45 | 11936 |
| 37 | [yc-software/qm](https://github.com/yc-software/qm) | +44 | 13689 |
| 38 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +44 | 6048 |
| 39 | [google/skills](https://github.com/google/skills) | +44 | 18397 |
| 40 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +44 | 33783 |
| 41 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1486 |
| 42 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +43 | 34641 |
| 43 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +43 | 46927 |
| 44 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 25216 |
| 45 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +42 | 8154 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +41 | 20594 |
| 47 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 63036 |
| 48 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8474 |
| 49 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +38 | 48352 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +38 | 17743 |
| 51 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5227 |
| 52 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8512 |
| 53 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 12185 |
| 54 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +36 | 35469 |
| 55 | [blader/humanizer](https://github.com/blader/humanizer) | +36 | 35955 |
| 56 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +35 | 15178 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9883 |
| 58 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +33 | 41209 |
| 59 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +33 | 11294 |
| 60 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +32 | 3747 |
| 61 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 10271 |
| 62 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 46188 |
| 63 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +32 | 39118 |
| 64 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +31 | 6230 |
| 65 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 44500 |
| 66 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +27 | 18953 |
| 67 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +27 | 21459 |
| 68 | [malisper/pgrust](https://github.com/malisper/pgrust) | +27 | 4447 |
| 69 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 8011 |
| 70 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4810 |
| 71 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 22431 |
| 72 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +26 | 8846 |
| 73 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24523 |
| 74 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 2011 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 76 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 32165 |
| 77 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +25 | 11665 |
| 78 | [spinabot/brigade](https://github.com/spinabot/brigade) | +24 | 2732 |
| 79 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +24 | 3170 |
| 80 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +24 | 8524 |
| 81 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +23 | 8796 |
| 82 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +23 | 29033 |
| 83 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 4023 |
| 84 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +23 | 8233 |
| 85 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +22 | 45613 |
| 86 | [browser-use/video-use](https://github.com/browser-use/video-use) | +22 | 20794 |
| 87 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +22 | 10035 |
| 88 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +21 | 3915 |
| 89 | [t8y2/dbx](https://github.com/t8y2/dbx) | +21 | 15087 |
| 90 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6083 |
| 91 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 1041 |
| 92 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +20 | 5721 |
| 93 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +20 | 5155 |
| 94 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 14274 |
| 95 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8553 |
| 96 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +19 | 9082 |
| 97 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +19 | 5415 |
| 98 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +18 | 0 |
| 99 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +18 | 8086 |
| 100 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +18 | 47611 |
| 101 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13501 |
| 102 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5870 |
| 103 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +17 | 4041 |
| 104 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +17 | 2463 |
| 105 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 42697 |
| 106 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 11191 |
| 107 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +15 | 30214 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16512 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6382 |
| 110 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +14 | 6483 |
| 111 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 720 |
| 112 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 8921 |
| 113 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16056 |
| 114 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2241 |
| 115 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +14 | 31940 |
| 116 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2081 |
| 117 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +13 | 4817 |
| 118 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3998 |
| 119 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +13 | 3068 |
| 120 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +13 | 22796 |
| 121 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 20037 |
| 122 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 5935 |
| 123 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2247 |
| 124 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 125 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25579 |
| 126 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 830 |
| 127 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +12 | 3177 |
| 128 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +12 | 1833 |
| 129 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1407 |
| 130 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2546 |
| 131 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2933 |
| 132 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12 | 9988 |
| 133 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +12 | 8641 |
| 134 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +12 | 2079 |
| 135 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +11 | 1522 |
| 136 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +11 | 2393 |
| 137 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5956 |
| 138 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +11 | 15610 |
| 139 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4868 |
| 140 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +10 | 1657 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +10 | 2769 |
| 142 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 30730 |
| 143 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10581 |
| 144 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2262 |
| 145 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +10 | 301 |
| 146 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +10 | 10652 |
| 147 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1022 |
| 148 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +10 | 27616 |
| 149 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1866 |
| 150 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 3667 |
| 151 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 3373 |
| 152 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1891 |
| 153 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 154 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 378 |
| 155 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 354 |
| 156 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 565 |
| 157 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 974 |
| 158 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 993 |
| 159 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +9 | 14677 |
| 160 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 45017 |
| 161 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3592 |
| 162 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 904 |
| 163 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28655 |
| 164 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8682 |
| 165 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5618 |
| 166 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1322 |
| 167 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4256 |
| 168 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +9 | 1574 |
| 169 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1766 |
| 170 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24340 |
| 171 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1122 |
| 172 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1572 |
| 173 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +8 | 47065 |
| 174 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +8 | 33652 |
| 175 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9933 |
| 176 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 4857 |
| 177 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2368 |
| 178 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28238 |
| 179 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8328 |
| 180 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1157 |
| 181 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +8 | 9986 |
| 182 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10652 |
| 183 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6734 |
| 184 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41058 |
| 185 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +7 | 13871 |
| 186 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +7 | 2730 |
| 187 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +7 | 1477 |
| 188 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +7 | 1390 |
| 189 | [uber/ADR](https://github.com/uber/ADR) | +7 | 1436 |
| 190 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6110 |
| 191 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6559 |
| 192 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1391 |
| 193 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 31 |
| 194 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +7 | 10417 |
| 195 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +7 | 8634 |
| 196 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 197 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 273 |
| 198 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27426 |
| 199 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 284 |
| 200 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 450 |
| 201 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14633 |
| 202 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30097 |
| 203 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +6 | 3263 |
| 204 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 529 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5578 |
| 206 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 2048 |
| 207 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1505 |
| 208 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 446 |
| 209 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5655 |
| 210 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3047 |
| 211 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 533 |
| 212 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7202 |
| 213 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 785 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5708 |
| 215 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1339 |
| 216 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 694 |
| 217 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +5 | 2175 |
| 218 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 321 |
| 219 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1216 |
| 220 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11429 |
| 221 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 425 |
| 222 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4874 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5202 |
| 224 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5110 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +4 | 3041 |
| 226 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +4 | 1306 |
| 227 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3394 |
| 228 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9603 |
| 229 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 417 |
| 230 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3529 |
| 231 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3324 |
| 232 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 106 |
| 233 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 946 |
| 234 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3250 |
| 235 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28438 |
| 236 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4707 |
| 237 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 176 |
| 238 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +3 | 531 |
| 239 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 1065 |
| 240 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 527 |
| 241 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 573 |
| 242 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9532 |
| 243 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 190 |
| 244 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 363 |
| 245 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12317 |
| 246 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1170 |
| 247 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 928 |
| 248 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 347 |
| 249 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 555 |
| 250 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18964 |
| 251 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3443 |
| 252 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 788 |
| 253 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2831 |
| 254 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 453 |
| 255 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 256 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 419 |
| 257 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +3 | 5543 |
| 258 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 913 |
| 259 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 576 |
| 260 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 303 |
| 261 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1196 |
| 262 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2050 |
| 263 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 8956 |
| 264 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 842 |
| 265 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10504 |
| 266 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 719 |
| 267 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 893 |
| 268 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 330 |
| 269 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1333 |
| 270 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3995 |
| 271 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1071 |
| 272 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 687 |
| 273 | [thangnq111203/oss-steward](https://github.com/thangnq111203/oss-steward) | +2 | 91 |
| 274 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +2 | 591 |
| 275 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +2 | 1606 |
| 276 | [SamurAIGPT/seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) | +2 | 76 |
| 277 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +2 | 1247 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 101 |
| 279 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 883 |
| 280 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 423 |
| 281 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 108 |
| 282 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 132 |
| 283 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 207 |
| 284 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5084 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 343 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2900 |
| 287 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 270 |
| 288 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3174 |
| 289 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10414 |
| 290 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1199 |
| 291 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1397 |
| 292 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 512 |
| 293 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2554 |
| 294 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3806 |
| 295 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 296 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2710 |
| 297 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 109 |
| 298 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 93 |
| 299 | [Matchameleon/gpt-codex-plugin](https://github.com/Matchameleon/gpt-codex-plugin) | +1 | 139 |
| 300 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1303 |
