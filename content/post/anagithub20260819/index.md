---
title: "2026-08-19 GitHub增长趋势报告"
description: "1.diagram-design+10 2.deepseek-harness-desktop+9 3.Anthropic-Cybersecurity-Skills+8 4.OpenViking+7 5.orca+6"
date: 2026-08-19T20:29:06+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-19 20:29:06

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
        'daily': {"categories": ["magnitudedev/magnitude", "BetterWright/betterwright", "hugohe3/ppt-master", "ayghri/i-have-adhd", "vibeinging/deepseek-harness-desktop-app", "herdrdev/herdr", "NawfalMotii79/PLFM_RADAR", "holaboss-ai/holaOS", "AlexsJones/llmfit", "ifixai-ai/iFixAi", "diegosouzapw/OmniRoute", "chaitanyagiri/munder-difflin", "bojieli/ai-agent-book", "AprilNEA/OpenLogi", "virgiliojr94/book-to-skill", "stablyai/orca", "volcengine/OpenViking", "mukul975/Anthropic-Cybersecurity-Skills", "anywhere-labs/deepseek-harness-desktop", "cathrynlavery/diagram-design"], "data": [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]},
        'weekly': {"categories": ["every-app/open-seo", "emilkowalski/skills", "lightningpixel/modly", "virgiliojr94/book-to-skill", "tt-a1i/archify", "internet-court/internet-court-skill", "holaboss-ai/holaOS", "ifixai-ai/iFixAi", "titanwings/colleague-skill", "herdrdev/herdr", "xiaobright/dsh-anchored-standard", "bojieli/ai-agent-book", "hugohe3/ppt-master", "PrimeIntellect-ai/prime-agent", "stablyai/orca", "cactus-compute/needle", "LaoFeng-mouse/flyingmouse-format", "anywhere-labs/deepseek-harness-desktop", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [11, 11, 11, 11, 11, 11, 12, 12, 14, 14, 14, 15, 17, 19, 19, 20, 23, 52, 60, 60]},
        'monthly': {"categories": ["cloudflare/cloudflare-os", "guillaumemeyer/watermarks-remover", "k1tbyte/Wand-Enhancer", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "ifixai-ai/iFixAi", "emilkowalski/skills", "floci-io/floci", "andrewyng/openworker", "herdrdev/herdr", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "cathrynlavery/diagram-design", "virgiliojr94/book-to-skill", "stablyai/orca", "bojieli/ai-agent-book", "block/buzz", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [60, 60, 61, 62, 64, 64, 68, 75, 81, 81, 90, 92, 96, 99, 116, 128, 136, 148, 155, 256]}
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
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +10 | 23196 |
| 2 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +9 | 15089 |
| 3 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +8 | 29747 |
| 4 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +7 | 30080 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +6 | 49018 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +5 | 23090 |
| 7 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +4 | 10310 |
| 8 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +4 | 39488 |
| 9 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +4 | 2620 |
| 10 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +4 | 51141 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 10940 |
| 12 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4 | 32990 |
| 13 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +4 | 10148 |
| 14 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +4 | 24557 |
| 15 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +4 | 30634 |
| 16 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +3 | 491 |
| 17 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +3 | 22285 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 48007 |
| 19 | [BetterWright/betterwright](https://github.com/BetterWright/betterwright) | +3 | 151 |
| 20 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +3 | 1363 |
| 21 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +3 | 17368 |
| 22 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3 | 14468 |
| 23 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +3 | 44908 |
| 24 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +2 | 2794 |
| 25 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +2 | 12031 |
| 26 | [block/buzz](https://github.com/block/buzz) | +2 | 28628 |
| 27 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +2 | 3733 |
| 28 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +2 | 221 |
| 29 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2 | 19548 |
| 30 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +2 | 5588 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +60 | 23196 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +60 | 15207 |
| 3 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +52 | 15089 |
| 4 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +23 | 3858 |
| 5 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +20 | 7774 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +19 | 49018 |
| 7 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +19 | 17368 |
| 8 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +17 | 48007 |
| 9 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +15 | 39488 |
| 10 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +14 | 3637 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +14 | 30634 |
| 12 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +14 | 23534 |
| 13 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +12 | 10940 |
| 14 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +12 | 10148 |
| 15 | [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) | +11 | 4190 |
| 16 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +11 | 14468 |
| 17 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +11 | 23090 |
| 18 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +11 | 6878 |
| 19 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +11 | 30699 |
| 20 | [every-app/open-seo](https://github.com/every-app/open-seo) | +11 | 12654 |
| 21 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +10 | 29747 |
| 22 | [block/buzz](https://github.com/block/buzz) | +10 | 28628 |
| 23 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +10 | 51141 |
| 24 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +10 | 26703 |
| 25 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 36486 |
| 26 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +10 | 3694 |
| 27 | [macro-inc/macro](https://github.com/macro-inc/macro) | +10 | 3766 |
| 28 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | +10 | 2077 |
| 29 | [yc-software/qm](https://github.com/yc-software/qm) | +9 | 13941 |
| 30 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +9 | 23205 |
| 31 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +8 | 30080 |
| 32 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 44908 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +8 | 11254 |
| 34 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 36589 |
| 35 | [MiniMax-AI/MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) | +8 | 608 |
| 36 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +8 | 17219 |
| 37 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +8 | 4073 |
| 38 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +7 | 2794 |
| 39 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +7 | 19548 |
| 40 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +7 | 22285 |
| 41 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +7 | 48956 |
| 42 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +7 | 4376 |
| 43 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +7 | 4270 |
| 44 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47821 |
| 45 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7754 |
| 46 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +6 | 24557 |
| 47 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +6 | 12584 |
| 48 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +6 | 14321 |
| 49 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +6 | 16253 |
| 50 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +6 | 2932 |
| 51 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 46856 |
| 52 | [spinabot/brigade](https://github.com/spinabot/brigade) | +6 | 2976 |
| 53 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +6 | 28843 |
| 54 | [Leutenegger/book-to-skill](https://github.com/Leutenegger/book-to-skill) | +6 | 1202 |
| 55 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +5 | 12031 |
| 56 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +5 | 2620 |
| 57 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +5 | 32990 |
| 58 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 30400 |
| 59 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +5 | 25506 |
| 60 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +5 | 1579 |
| 61 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 34868 |
| 62 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +5 | 12113 |
| 63 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +5 | 376 |
| 64 | [xr843/insect-world](https://github.com/xr843/insect-world) | +5 | 495 |
| 65 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 8351 |
| 66 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 778 |
| 67 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +5 | 1929 |
| 68 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +5 | 2156 |
| 69 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +5 | 6087 |
| 70 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +4 | 3197 |
| 71 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3733 |
| 72 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +4 | 10310 |
| 73 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1055 |
| 74 | [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | +4 | 1361 |
| 75 | [floci-io/floci](https://github.com/floci-io/floci) | +4 | 20558 |
| 76 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +4 | 20853 |
| 77 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +4 | 12243 |
| 78 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +4 | 25862 |
| 79 | [rukamori/ArchiveTune](https://github.com/rukamori/ArchiveTune) | +4 | 4803 |
| 80 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +4 | 11367 |
| 81 | [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | +4 | 3499 |
| 82 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 46101 |
| 83 | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | +4 | 607 |
| 84 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +4 | 7503 |
| 85 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +4 | 4994 |
| 86 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +4 | 6433 |
| 87 | [different-ai/openwork](https://github.com/different-ai/openwork) | +4 | 22686 |
| 88 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +4 | 8614 |
| 89 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 9063 |
| 90 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +4 | 1593 |
| 91 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +4 | 9358 |
| 92 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +4 | 15840 |
| 93 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +4 | 6383 |
| 94 | [agegr/pi-web](https://github.com/agegr/pi-web) | +3 | 4829 |
| 95 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 40952 |
| 96 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +3 | 20273 |
| 97 | [docling-project/docling-graph](https://github.com/docling-project/docling-graph) | +3 | 589 |
| 98 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +3 | 491 |
| 99 | [BetterWright/betterwright](https://github.com/BetterWright/betterwright) | +3 | 151 |
| 100 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +3 | 1363 |
| 101 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +3 | 41697 |
| 102 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +3 | 17495 |
| 103 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 24132 |
| 104 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +3 | 47181 |
| 105 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +3 | 6176 |
| 106 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +3 | 31282 |
| 107 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 36063 |
| 108 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +3 | 4456 |
| 109 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +3 | 4954 |
| 110 | [ZJU-REAL/HugAgentOS](https://github.com/ZJU-REAL/HugAgentOS) | +3 | 441 |
| 111 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +3 | 24478 |
| 112 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +3 | 1255 |
| 113 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 63387 |
| 114 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +2 | 221 |
| 115 | [yuwen-cool/yuwen-publish-precheck](https://github.com/yuwen-cool/yuwen-publish-precheck) | +2 | 593 |
| 116 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +2 | 6044 |
| 117 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +2 | 10707 |
| 118 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +2 | 3093 |
| 119 | [jundot/omlx](https://github.com/jundot/omlx) | +2 | 19785 |
| 120 | [krusemediallc/arcads-claude-code](https://github.com/krusemediallc/arcads-claude-code) | +2 | 1346 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +256 | 17368 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +155 | 17219 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +148 | 51141 |
| 4 | [block/buzz](https://github.com/block/buzz) | +136 | 28628 |
| 5 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +128 | 39488 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +116 | 49018 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +99 | 23090 |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +96 | 23196 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +92 | 22285 |
| 10 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +90 | 26703 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +81 | 30634 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14827 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +75 | 20558 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +68 | 30699 |
| 15 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +64 | 10940 |
| 16 | [brightdata/cli](https://github.com/brightdata/cli) | +64 | 6277 |
| 17 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +62 | 23205 |
| 18 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +61 | 18855 |
| 19 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +60 | 15207 |
| 20 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8609 |
| 21 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +57 | 16253 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +56 | 48007 |
| 23 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +55 | 11254 |
| 24 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +55 | 24132 |
| 25 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +53 | 32390 |
| 26 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +52 | 15089 |
| 27 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21575 |
| 28 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +49 | 9472 |
| 29 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +48 | 28843 |
| 30 | [yc-software/qm](https://github.com/yc-software/qm) | +47 | 13941 |
| 31 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +46 | 12243 |
| 32 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +45 | 6383 |
| 33 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +45 | 14468 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +45 | 36486 |
| 35 | [google/skills](https://github.com/google/skills) | +44 | 18511 |
| 36 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1466 |
| 37 | [oblien/openship](https://github.com/oblien/openship) | +43 | 11118 |
| 38 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +42 | 20853 |
| 39 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 34868 |
| 40 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 25862 |
| 41 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +42 | 15840 |
| 42 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +41 | 63387 |
| 43 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +41 | 25506 |
| 44 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +41 | 30574 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +39 | 47210 |
| 46 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8531 |
| 47 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +39 | 34094 |
| 48 | [blader/humanizer](https://github.com/blader/humanizer) | +37 | 36589 |
| 49 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5500 |
| 50 | [trycompai/crm](https://github.com/trycompai/crm) | +36 | 8666 |
| 51 | [every-app/open-seo](https://github.com/every-app/open-seo) | +36 | 12654 |
| 52 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +36 | 12031 |
| 53 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +35 | 48956 |
| 54 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +35 | 31282 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +34 | 44908 |
| 56 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +34 | 18009 |
| 57 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +33 | 4073 |
| 58 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9978 |
| 59 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +32 | 6433 |
| 60 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +32 | 39572 |
| 61 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +31 | 19548 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 10257 |
| 63 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +31 | 41697 |
| 64 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 36063 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 46856 |
| 66 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +28 | 15352 |
| 67 | [different-ai/openwork](https://github.com/different-ai/openwork) | +27 | 22686 |
| 68 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4954 |
| 69 | [get-bb/bb](https://github.com/get-bb/bb) | +26 | 2372 |
| 70 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 21684 |
| 71 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +26 | 9063 |
| 72 | [MIgHTy-alIeN/ai-trader-bot](https://github.com/MIgHTy-alIeN/ai-trader-bot) | +25 | 2686 |
| 73 | [spinabot/brigade](https://github.com/spinabot/brigade) | +25 | 2976 |
| 74 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +25 | 3242 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 840 |
| 76 | [xai-org/grok-build](https://github.com/xai-org/grok-build) | +25 | 25698 |
| 77 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +25 | 8119 |
| 78 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +24 | 4377 |
| 79 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 24670 |
| 80 | [malisper/pgrust](https://github.com/malisper/pgrust) | +24 | 4582 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +24 | 4094 |
| 82 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +23 | 3858 |
| 83 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 8976 |
| 84 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 32464 |
| 85 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +23 | 12113 |
| 86 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +22 | 7774 |
| 87 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +22 | 1089 |
| 88 | [browser-use/video-use](https://github.com/browser-use/video-use) | +21 | 21124 |
| 89 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +21 | 5381 |
| 90 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6169 |
| 91 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +19 | 46101 |
| 92 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +19 | 5552 |
| 93 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +19 | 8624 |
| 94 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 5992 |
| 95 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13666 |
| 96 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +17 | 14594 |
| 97 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 43035 |
| 98 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 10194 |
| 99 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +16 | 9358 |
| 100 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +16 | 4270 |
| 101 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +16 | 30080 |
| 102 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47821 |
| 103 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +16 | 13957 |
| 104 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +15 | 10148 |
| 105 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +15 | 3694 |
| 106 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +15 | 8351 |
| 107 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 748 |
| 108 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +15 | 8341 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6520 |
| 110 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +14 | 4958 |
| 111 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +14 | 23534 |
| 112 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +14 | 33917 |
| 113 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16168 |
| 114 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +14 | 3637 |
| 115 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2360 |
| 116 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +13 | 0 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 3996 |
| 118 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +13 | 29747 |
| 119 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 30401 |
| 120 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +13 | 3105 |
| 121 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +13 | 1923 |
| 122 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +13 | 3052 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 20278 |
| 124 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +13 | 11367 |
| 125 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 126 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2156 |
| 127 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 851 |
| 128 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +12 | 1789 |
| 129 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +12 | 6044 |
| 130 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1441 |
| 131 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +12 | 9059 |
| 132 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 30954 |
| 133 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12 | 10344 |
| 134 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +12 | 6087 |
| 135 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +12 | 32063 |
| 136 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +12 | 5962 |
| 137 | [penecho/penecho](https://github.com/penecho/penecho) | +12 | 2104 |
| 138 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2642 |
| 139 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +11 | 2876 |
| 140 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +11 | 2461 |
| 141 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +11 | 376 |
| 142 | [decolua/9router](https://github.com/decolua/9router) | +11 | 25828 |
| 143 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +11 | 27821 |
| 144 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +11 | 5588 |
| 145 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14321 |
| 146 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 8742 |
| 147 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +10 | 47181 |
| 148 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +10 | 3790 |
| 149 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2318 |
| 150 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 1058 |
| 151 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1923 |
| 152 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 385 |
| 153 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 154 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 3197 |
| 155 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +9 | 10707 |
| 156 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1696 |
| 157 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +9 | 2932 |
| 158 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 1016 |
| 159 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 380 |
| 160 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +9 | 1593 |
| 161 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 572 |
| 162 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 1039 |
| 163 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +9 | 10682 |
| 164 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5731 |
| 165 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1393 |
| 166 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +9 | 1738 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1944 |
| 168 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +8 | 2794 |
| 169 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24478 |
| 170 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1255 |
| 171 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6760 |
| 172 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1761 |
| 173 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +8 | 6176 |
| 174 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 4994 |
| 175 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +8 | 1059 |
| 176 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +8 | 15705 |
| 177 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2538 |
| 178 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3675 |
| 179 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28353 |
| 180 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8464 |
| 181 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +7 | 778 |
| 182 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +7 | 14783 |
| 183 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +7 | 17495 |
| 184 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +7 | 11042 |
| 185 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +7 | 45142 |
| 186 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41107 |
| 187 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +7 | 8883 |
| 188 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +7 | 1412 |
| 189 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6692 |
| 190 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1455 |
| 191 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 192 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 3431 |
| 193 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +6 | 1522 |
| 194 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 195 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 277 |
| 196 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27495 |
| 197 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 318 |
| 198 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 490 |
| 199 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 30216 |
| 200 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3733 |
| 201 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +6 | 4905 |
| 202 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5745 |
| 203 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3085 |
| 204 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 575 |
| 205 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5806 |
| 206 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +5 | 11485 |
| 207 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 208 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 813 |
| 209 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1355 |
| 210 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +5 | 14672 |
| 211 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +5 | 3324 |
| 212 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 698 |
| 213 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 359 |
| 214 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1224 |
| 215 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +4 | 1181 |
| 216 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +4 | 578 |
| 217 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +4 | 7233 |
| 218 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 225 |
| 219 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +4 | 10480 |
| 220 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 478 |
| 221 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4886 |
| 222 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5228 |
| 223 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1180 |
| 224 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +4 | 8708 |
| 225 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +4 | 10078 |
| 226 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5110 |
| 227 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +4 | 1352 |
| 228 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 423 |
| 229 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +4 | 1055 |
| 230 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3369 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 108 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1023 |
| 233 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +4 | 5586 |
| 234 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 259 |
| 235 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 187 |
| 236 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +3 | 602 |
| 237 | [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | +3 | 491 |
| 238 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 560 |
| 239 | [steven-kid/deepseek-harness-desktop](https://github.com/steven-kid/deepseek-harness-desktop) | +3 | 155 |
| 240 | [NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode) | +3 | 630 |
| 241 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +3 | 602 |
| 242 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +3 | 8984 |
| 243 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9613 |
| 244 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 191 |
| 245 | [quickdrawjs/quickdraw](https://github.com/quickdrawjs/quickdraw) | +3 | 383 |
| 246 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1200 |
| 247 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +3 | 3132 |
| 248 | [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) | +3 | 957 |
| 249 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 351 |
| 250 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +3 | 534 |
| 251 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 598 |
| 252 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +3 | 3455 |
| 253 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 19004 |
| 254 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 819 |
| 255 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 457 |
| 256 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 257 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9732 |
| 258 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 937 |
| 259 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 580 |
| 260 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +3 | 290 |
| 261 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 318 |
| 262 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1221 |
| 263 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28576 |
| 264 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 864 |
| 265 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2073 |
| 266 | [crimera/piko](https://github.com/crimera/piko) | +3 | 4776 |
| 267 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 734 |
| 268 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 905 |
| 269 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +2 | 158 |
| 270 | [Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) | +2 | 2794 |
| 271 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 413 |
| 272 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +2 | 1417 |
| 273 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1367 |
| 274 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12382 |
| 275 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 4033 |
| 276 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1075 |
| 277 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 691 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 101 |
| 279 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 441 |
| 280 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 114 |
| 281 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +2 | 3665 |
| 282 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 154 |
| 283 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 218 |
| 284 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 355 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2905 |
| 286 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5155 |
| 287 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1217 |
| 288 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1407 |
| 289 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 514 |
| 290 | [langgraph4j/langgraph4j](https://github.com/langgraph4j/langgraph4j) | +2 | 1934 |
| 291 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2565 |
| 292 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 293 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2714 |
| 294 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 128 |
| 295 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 106 |
| 296 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 898 |
| 297 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1318 |
| 298 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 929 |
| 299 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 94 |
| 300 | [linzhi-524/cineisle](https://github.com/linzhi-524/cineisle) | +1 | 35 |
