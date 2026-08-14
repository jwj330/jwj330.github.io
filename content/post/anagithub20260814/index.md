---
title: "2026-08-14 GitHub增长趋势报告"
description: "1.diagram-design+18 2.watermarks-remover+15 3.colleague-skill+7 4.TencentDB-Agent-Memory+6 5.deepsec+6"
date: 2026-08-14T20:32:12+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-14 20:32:12

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
        'daily': {"categories": ["every-app/open-seo", "Zeejay0/gathered-scenes-zine-skill", "yc-software/qm", "firecrawl/pdf-inspector", "HKUDS/CLI-Anything", "gloom-sh/gloomberb", "holaboss-ai/holaOS", "whiteguo233/OpenBiliClaw", "PrimeIntellect-ai/prime-agent", "Devin-AXIS/iPolloWork", "block/buzz", "arvin341az-glitch/RVG", "cactus-compute/needle", "iOfficeAI/OfficeCLI", "lightningpixel/modly", "vercel-labs/deepsec", "TencentCloud/TencentDB-Agent-Memory", "titanwings/colleague-skill", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 15, 18]},
        'weekly': {"categories": ["guillaumemeyer/watermarks-remover", "herdrdev/herdr", "semantica-agi/semantica", "talivia-group/talivia", "google/skills", "MiniMax-AI/MiniMax-H3", "emilkowalski/skills", "TencentCloud/TencentDB-Agent-Memory", "cloudflare/cloudflare-os", "pranshuparmar/witr", "stablyai/orca", "zhaoxuya520/reverse-skill", "brightdata/cli", "block/buzz", "floci-io/floci", "virgiliojr94/book-to-skill", "cathrynlavery/diagram-design", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [38, 39, 40, 41, 41, 42, 43, 44, 46, 47, 51, 53, 58, 58, 61, 61, 69, 73, 136, 231]},
        'monthly': {"categories": ["brightdata/cli", "iOfficeAI/OfficeCLI", "Fei-Away/Codex-Dream-Skin", "k1tbyte/Wand-Enhancer", "MadsLorentzen/ai-job-search", "cathrynlavery/diagram-design", "JustVugg/colibri", "floci-io/floci", "andrewyng/openworker", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "emilkowalski/skills", "herdrdev/herdr", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [63, 64, 66, 67, 68, 69, 71, 73, 81, 82, 87, 92, 93, 95, 131, 132, 144, 153, 157, 245]}
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
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +18 | 17051 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +15 | 7826 |
| 3 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +7 | 22015 |
| 4 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +6 | 21669 |
| 5 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +6 | 7573 |
| 6 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +6 | 5874 |
| 7 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +5 | 28317 |
| 8 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +5 | 5529 |
| 9 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +4 | 1075 |
| 10 | [block/buzz](https://github.com/block/buzz) | +4 | 27377 |
| 11 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +4 | 3974 |
| 12 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +4 | 15887 |
| 13 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +4 | 2363 |
| 14 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +4 | 7210 |
| 15 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +4 | 1403 |
| 16 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +4 | 47085 |
| 17 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +4 | 15527 |
| 18 | [yc-software/qm](https://github.com/yc-software/qm) | +3 | 13545 |
| 19 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +3 | 3536 |
| 20 | [every-app/open-seo](https://github.com/every-app/open-seo) | +3 | 11906 |
| 21 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 11401 |
| 22 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 21518 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 46829 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3 | 46000 |
| 25 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 48097 |
| 26 | [macro-inc/macro](https://github.com/macro-inc/macro) | +3 | 2979 |
| 27 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +2 | 3039 |
| 28 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 30052 |
| 29 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1067 |
| 30 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +2 | 1311 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +231 | 15887 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +136 | 16069 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +73 | 47923 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +69 | 17051 |
| 5 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +61 | 21518 |
| 6 | [floci-io/floci](https://github.com/floci-io/floci) | +61 | 20058 |
| 7 | [block/buzz](https://github.com/block/buzz) | +58 | 27377 |
| 8 | [brightdata/cli](https://github.com/brightdata/cli) | +58 | 5238 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +53 | 25210 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +51 | 45598 |
| 11 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +47 | 21419 |
| 12 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +46 | 8229 |
| 13 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +44 | 21669 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +43 | 29274 |
| 15 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +42 | 5894 |
| 16 | [google/skills](https://github.com/google/skills) | +41 | 18174 |
| 17 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1465 |
| 18 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +40 | 7466 |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +39 | 29081 |
| 20 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +38 | 7826 |
| 21 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +36 | 8576 |
| 22 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +33 | 20509 |
| 23 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +33 | 14501 |
| 24 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +30 | 3536 |
| 25 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +30 | 62876 |
| 26 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +30 | 17285 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +28 | 46829 |
| 28 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +28 | 37332 |
| 29 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +25 | 9938 |
| 30 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +25 | 15527 |
| 31 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 32 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +24 | 12493 |
| 33 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +23 | 28317 |
| 34 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 8756 |
| 35 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +23 | 34585 |
| 36 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +23 | 5017 |
| 37 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +23 | 21391 |
| 38 | [every-app/open-seo](https://github.com/every-app/open-seo) | +22 | 11906 |
| 39 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +22 | 15081 |
| 40 | [spinabot/brigade](https://github.com/spinabot/brigade) | +21 | 2680 |
| 41 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +21 | 35620 |
| 42 | [trycompai/crm](https://github.com/trycompai/crm) | +21 | 8437 |
| 43 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +21 | 4702 |
| 44 | [get-bb/bb](https://github.com/get-bb/bb) | +21 | 1947 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +20 | 24808 |
| 46 | [malisper/pgrust](https://github.com/malisper/pgrust) | +20 | 4424 |
| 47 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 1008 |
| 48 | [yc-software/qm](https://github.com/yc-software/qm) | +19 | 13545 |
| 49 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +19 | 20485 |
| 50 | [blader/humanizer](https://github.com/blader/humanizer) | +19 | 35685 |
| 51 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +19 | 6074 |
| 52 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +19 | 24427 |
| 53 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +18 | 3706 |
| 54 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +18 | 15409 |
| 55 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +17 | 9963 |
| 56 | [different-ai/openwork](https://github.com/different-ai/openwork) | +17 | 22199 |
| 57 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +16 | 18728 |
| 58 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +16 | 24718 |
| 59 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +16 | 23777 |
| 60 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +16 | 30853 |
| 61 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +15 | 35204 |
| 62 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +15 | 48097 |
| 63 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +15 | 31679 |
| 64 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 692 |
| 65 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +13 | 3974 |
| 66 | [multica-ai/multica](https://github.com/multica-ai/multica) | +13 | 46000 |
| 67 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 38944 |
| 68 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +12 | 1709 |
| 69 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +12 | 11401 |
| 70 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +12 | 30118 |
| 71 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4006 |
| 72 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +12 | 5300 |
| 73 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 40969 |
| 74 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 46728 |
| 75 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +11 | 4578 |
| 76 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +11 | 6143 |
| 77 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +11 | 44290 |
| 78 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +11 | 1720 |
| 79 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +11 | 2425 |
| 80 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +11 | 31970 |
| 81 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +11 | 1311 |
| 82 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +11 | 18500 |
| 83 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +11 | 814 |
| 84 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +11 | 40631 |
| 85 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +10 | 5529 |
| 86 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +10 | 2261 |
| 87 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +10 | 1378 |
| 88 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +10 | 45488 |
| 89 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +10 | 19955 |
| 90 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +10 | 8533 |
| 91 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 373 |
| 92 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +9 | 11725 |
| 93 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +9 | 5835 |
| 94 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +9 | 5591 |
| 95 | [browser-use/video-use](https://github.com/browser-use/video-use) | +9 | 20682 |
| 96 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2510 |
| 97 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +9 | 9936 |
| 98 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +9 | 2879 |
| 99 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 937 |
| 100 | [macro-inc/macro](https://github.com/macro-inc/macro) | +8 | 2979 |
| 101 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +8 | 8982 |
| 102 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +8 | 5874 |
| 103 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1031 |
| 104 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +8 | 3039 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +8 | 14183 |
| 106 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 341 |
| 107 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +7 | 7210 |
| 108 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +7 | 22015 |
| 109 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 47085 |
| 110 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 42483 |
| 111 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +7 | 2351 |
| 112 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +7 | 1179 |
| 113 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +7 | 926 |
| 114 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +7 | 2704 |
| 115 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +7 | 5926 |
| 116 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 5033 |
| 117 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +7 | 8841 |
| 118 | [securo-finance/securo](https://github.com/securo-finance/securo) | +7 | 1528 |
| 119 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +6 | 24275 |
| 120 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +6 | 30052 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +245 | 15887 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +157 | 47923 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +153 | 16069 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +144 | 37332 |
| 5 | [block/buzz](https://github.com/block/buzz) | +132 | 27377 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +131 | 45598 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +95 | 21518 |
| 8 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +93 | 29081 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +92 | 29274 |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +87 | 20509 |
| 11 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +82 | 25210 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14501 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 20058 |
| 14 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +71 | 24718 |
| 15 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +69 | 17052 |
| 16 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +68 | 31679 |
| 17 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +67 | 17285 |
| 18 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +66 | 13715 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +64 | 28317 |
| 20 | [brightdata/cli](https://github.com/brightdata/cli) | +63 | 5238 |
| 21 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +63 | 30853 |
| 22 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +62 | 21669 |
| 23 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +59 | 8229 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +59 | 46829 |
| 25 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +55 | 15527 |
| 26 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10703 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +54 | 23777 |
| 28 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +53 | 8576 |
| 29 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21419 |
| 30 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +51 | 15409 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +50 | 12493 |
| 32 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +49 | 35620 |
| 33 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 33754 |
| 34 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +48 | 9963 |
| 35 | [google/skills](https://github.com/google/skills) | +45 | 18174 |
| 36 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +45 | 46728 |
| 37 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +45 | 34585 |
| 38 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +45 | 30118 |
| 39 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +44 | 5894 |
| 40 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +44 | 11725 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +43 | 62876 |
| 42 | [yc-software/qm](https://github.com/yc-software/qm) | +43 | 13545 |
| 43 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1465 |
| 44 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 24808 |
| 45 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +42 | 48097 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +41 | 20485 |
| 47 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +41 | 7466 |
| 48 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8442 |
| 49 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +38 | 7826 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +38 | 17546 |
| 51 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5017 |
| 52 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +37 | 15081 |
| 53 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +37 | 40969 |
| 54 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +37 | 38944 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +36 | 35204 |
| 56 | [trycompai/crm](https://github.com/trycompai/crm) | +35 | 8437 |
| 57 | [every-app/open-seo](https://github.com/every-app/open-seo) | +35 | 11906 |
| 58 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 35685 |
| 59 | [multica-ai/multica](https://github.com/multica-ai/multica) | +34 | 46000 |
| 60 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9824 |
| 61 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +33 | 19642 |
| 62 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +32 | 3536 |
| 63 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +32 | 9938 |
| 64 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 44290 |
| 65 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +32 | 10301 |
| 66 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +31 | 6074 |
| 67 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +30 | 8176 |
| 68 | [malisper/pgrust](https://github.com/malisper/pgrust) | +29 | 4424 |
| 69 | [different-ai/openwork](https://github.com/different-ai/openwork) | +28 | 22199 |
| 70 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5591 |
| 71 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +28 | 11401 |
| 72 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +28 | 8260 |
| 73 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +27 | 21391 |
| 74 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7971 |
| 75 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +27 | 28923 |
| 76 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +26 | 18728 |
| 77 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4702 |
| 78 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +26 | 8756 |
| 79 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +26 | 45488 |
| 80 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24427 |
| 81 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 1947 |
| 82 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 83 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31970 |
| 84 | [t8y2/dbx](https://github.com/t8y2/dbx) | +24 | 14747 |
| 85 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9902 |
| 86 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +23 | 0 |
| 87 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +23 | 3109 |
| 88 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20682 |
| 89 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3989 |
| 90 | [spinabot/brigade](https://github.com/spinabot/brigade) | +22 | 2680 |
| 91 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +21 | 8982 |
| 92 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 14183 |
| 93 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +20 | 3706 |
| 94 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6022 |
| 95 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 1008 |
| 96 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +20 | 5300 |
| 97 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8520 |
| 98 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 5033 |
| 99 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 42483 |
| 100 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +18 | 3974 |
| 101 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +18 | 7847 |
| 102 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13426 |
| 103 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11178 |
| 104 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +16 | 3039 |
| 105 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8841 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47085 |
| 107 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 5775 |
| 108 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +15 | 19955 |
| 109 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15 | 9936 |
| 110 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16485 |
| 111 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +15 | 31878 |
| 112 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6143 |
| 113 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 692 |
| 114 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30052 |
| 115 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +14 | 5835 |
| 116 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +14 | 8533 |
| 117 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16025 |
| 118 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2164 |
| 119 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 5118 |
| 120 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2068 |
| 121 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +13 | 4578 |
| 122 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 4006 |
| 123 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2223 |
| 124 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +13 | 15536 |
| 125 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 126 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25442 |
| 127 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 814 |
| 128 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1311 |
| 129 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2510 |
| 130 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2879 |
| 131 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 30604 |
| 132 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +11 | 1720 |
| 133 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +11 | 1378 |
| 134 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5926 |
| 135 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +11 | 1842 |
| 136 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +11 | 10516 |
| 137 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +11 | 2013 |
| 138 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +11 | 10230 |
| 139 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +11 | 27527 |
| 140 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3653 |
| 141 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4909 |
| 142 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +10 | 5529 |
| 143 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +10 | 24275 |
| 144 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +10 | 2704 |
| 145 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2351 |
| 146 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2188 |
| 147 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +10 | 28445 |
| 148 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +10 | 46999 |
| 149 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 33515 |
| 150 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 974 |
| 151 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1853 |
| 152 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 3323 |
| 153 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 10372 |
| 154 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +10 | 9935 |
| 155 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1886 |
| 156 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 157 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 373 |
| 158 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 958 |
| 159 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 937 |
| 160 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 44948 |
| 161 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3506 |
| 162 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 926 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8621 |
| 164 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 10886 |
| 165 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5557 |
| 166 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 9919 |
| 167 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1297 |
| 168 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 2845 |
| 169 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +9 | 19682 |
| 170 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4221 |
| 171 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1704 |
| 172 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8247 |
| 173 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 6436 |
| 174 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1031 |
| 175 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 341 |
| 176 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1528 |
| 177 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14625 |
| 178 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +8 | 6616 |
| 179 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 4786 |
| 180 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2220 |
| 181 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28184 |
| 182 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1142 |
| 183 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +8 | 2169 |
| 184 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10609 |
| 185 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6720 |
| 186 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41034 |
| 187 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +7 | 2363 |
| 188 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +7 | 1179 |
| 189 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6113 |
| 190 | [uber/ADR](https://github.com/uber/ADR) | +7 | 1418 |
| 191 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1737 |
| 192 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1371 |
| 193 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 23 |
| 194 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27393 |
| 195 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +7 | 8589 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 30033 |
| 197 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +7 | 3259 |
| 198 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 199 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 271 |
| 200 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 271 |
| 201 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 442 |
| 202 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3007 |
| 203 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5686 |
| 204 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14618 |
| 205 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 526 |
| 206 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 530 |
| 207 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5805 |
| 208 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 1075 |
| 209 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1494 |
| 210 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5568 |
| 211 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 415 |
| 212 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 512 |
| 213 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7182 |
| 214 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 774 |
| 215 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3006 |
| 216 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1285 |
| 217 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1328 |
| 218 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 694 |
| 219 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1218 |
| 220 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +5 | 3307 |
| 221 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 299 |
| 222 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1211 |
| 223 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +4 | 1993 |
| 224 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11327 |
| 225 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 369 |
| 226 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4915 |
| 227 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5185 |
| 228 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +4 | 9489 |
| 229 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5092 |
| 230 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3347 |
| 231 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9573 |
| 232 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1377 |
| 233 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +4 | 5526 |
| 234 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 411 |
| 235 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3411 |
| 236 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 105 |
| 237 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 934 |
| 238 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3229 |
| 239 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28406 |
| 240 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4671 |
| 241 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 164 |
| 242 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 971 |
| 243 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 514 |
| 244 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +3 | 1305 |
| 245 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 189 |
| 246 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12306 |
| 247 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1152 |
| 248 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 925 |
| 249 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 340 |
| 250 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 539 |
| 251 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18933 |
| 252 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3424 |
| 253 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 760 |
| 254 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2801 |
| 255 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 448 |
| 256 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 257 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 416 |
| 258 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +3 | 5937 |
| 259 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 894 |
| 260 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 599 |
| 261 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 296 |
| 262 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1187 |
| 263 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2029 |
| 264 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 5069 |
| 265 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9199 |
| 266 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 832 |
| 267 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 891 |
| 268 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 707 |
| 269 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 325 |
| 270 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3983 |
| 271 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6294 |
| 272 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1067 |
| 273 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 678 |
| 274 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +2 | 497 |
| 275 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +2 | 1587 |
| 276 | [SamurAIGPT/seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) | +2 | 75 |
| 277 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +2 | 1243 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 279 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1295 |
| 280 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 422 |
| 281 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 106 |
| 282 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 869 |
| 283 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 111 |
| 284 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 205 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 335 |
| 286 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2890 |
| 287 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 254 |
| 288 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3149 |
| 289 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 270 |
| 290 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10407 |
| 291 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1193 |
| 292 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1386 |
| 293 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 511 |
| 294 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2541 |
| 295 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3808 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 297 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2704 |
| 298 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10495 |
| 299 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 93 |
| 300 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 89 |
