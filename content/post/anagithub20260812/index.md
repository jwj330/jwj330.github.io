---
title: "2026-08-12 GitHub增长趋势报告"
description: "1.brigade+21 2.diagram-design+19 3.orca+9 4.corsair+8 5.gathered-scenes-zine-skill+7"
date: 2026-08-12T20:46:54+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-12 20:46:54

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
        'daily': {"categories": ["Nasiko-Labs/nasiko", "ayghri/i-have-adhd", "zhaoxuya520/reverse-skill", "brightdata/cli", "openchamber/openchamber", "aipoch/open-science", "ZzzLc0405/photo-abstract-editorial", "HKUDS/DeepTutor", "lidge-jun/opencodex", "herdrdev/herdr", "hugohe3/ppt-master", "PrimeIntellect-ai/prime-agent", "ZhuLinsen/daily_stock_analysis", "firecrawl/anydoc", "MiniMax-AI/MiniMax-H3", "Zeejay0/gathered-scenes-zine-skill", "corsairdev/corsair", "stablyai/orca", "cathrynlavery/diagram-design", "spinabot/brigade"], "data": [3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 9, 19, 21]},
        'weekly': {"categories": ["andrewyng/openworker", "cathrynlavery/diagram-design", "ifixai-ai/iFixAi", "herdrdev/herdr", "talivia-group/talivia", "google/skills", "emilkowalski/skills", "MiniMax-AI/MiniMax-H3", "TencentCloud/TencentDB-Agent-Memory", "stablyai/orca", "pranshuparmar/witr", "zhaoxuya520/reverse-skill", "block/buzz", "cloudflare/cloudflare-os", "virgiliojr94/book-to-skill", "brightdata/cli", "floci-io/floci", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [34, 36, 38, 40, 41, 41, 41, 41, 43, 46, 50, 54, 54, 59, 59, 60, 62, 75, 146, 237]},
        'monthly': {"categories": ["brightdata/cli", "iOfficeAI/OfficeCLI", "Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "k1tbyte/Wand-Enhancer", "MadsLorentzen/ai-job-search", "floci-io/floci", "andrewyng/openworker", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "herdrdev/herdr", "JustVugg/colibri", "emilkowalski/skills", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [61, 64, 66, 69, 69, 70, 73, 80, 81, 85, 90, 91, 92, 92, 125, 126, 140, 147, 156, 237]}
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
| 1 | [spinabot/brigade](https://github.com/spinabot/brigade) | +21 | 2546 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +19 | 9860 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +9 | 43735 |
| 4 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +8 | 9675 |
| 5 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +7 | 3079 |
| 6 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +7 | 5425 |
| 7 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +6 | 15033 |
| 8 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +6 | 62566 |
| 9 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +5 | 14844 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 45491 |
| 11 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +5 | 28203 |
| 12 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +4 | 9584 |
| 13 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +4 | 35156 |
| 14 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +4 | 3006 |
| 15 | [aipoch/open-science](https://github.com/aipoch/open-science) | +4 | 2059 |
| 16 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +4 | 8570 |
| 17 | [brightdata/cli](https://github.com/brightdata/cli) | +4 | 4610 |
| 18 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +4 | 24418 |
| 19 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +4 | 19967 |
| 20 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +3 | 4530 |
| 21 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 36586 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 34856 |
| 23 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +3 | 44049 |
| 24 | [superdesigndev/tools-registry](https://github.com/superdesigndev/tools-registry) | +3 | 312 |
| 25 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +3 | 42196 |
| 26 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 47761 |
| 27 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +3 | 20484 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +3 | 13225 |
| 29 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +3 | 11374 |
| 30 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +3 | 1519 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +237 | 14844 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +146 | 15033 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +75 | 46535 |
| 4 | [floci-io/floci](https://github.com/floci-io/floci) | +62 | 19721 |
| 5 | [brightdata/cli](https://github.com/brightdata/cli) | +60 | 4610 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +59 | 20815 |
| 7 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +59 | 7900 |
| 8 | [block/buzz](https://github.com/block/buzz) | +54 | 26662 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +54 | 24418 |
| 10 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +50 | 21330 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +46 | 43735 |
| 12 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +43 | 20484 |
| 13 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +41 | 5425 |
| 14 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +41 | 28646 |
| 15 | [google/skills](https://github.com/google/skills) | +41 | 17888 |
| 16 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1480 |
| 17 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +40 | 28203 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +38 | 8347 |
| 19 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +36 | 9861 |
| 20 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +34 | 14309 |
| 21 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +33 | 19968 |
| 22 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +31 | 62566 |
| 23 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +30 | 36586 |
| 24 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +30 | 5614 |
| 25 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +29 | 16838 |
| 26 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +26 | 3079 |
| 27 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +25 | 14995 |
| 28 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +25 | 11678 |
| 29 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 846 |
| 30 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +24 | 21294 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +23 | 45491 |
| 32 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 24197 |
| 33 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +23 | 34181 |
| 34 | [get-bb/bb](https://github.com/get-bb/bb) | +23 | 1763 |
| 35 | [spinabot/brigade](https://github.com/spinabot/brigade) | +22 | 2546 |
| 36 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +22 | 9675 |
| 37 | [trycompai/crm](https://github.com/trycompai/crm) | +22 | 8313 |
| 38 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +22 | 9584 |
| 39 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +21 | 14944 |
| 40 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +21 | 8570 |
| 41 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +21 | 4817 |
| 42 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +20 | 4379 |
| 43 | [malisper/pgrust](https://github.com/malisper/pgrust) | +20 | 4357 |
| 44 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 943 |
| 45 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +19 | 5741 |
| 46 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +18 | 35156 |
| 47 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +18 | 31372 |
| 48 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 27927 |
| 49 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +18 | 23596 |
| 50 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +18 | 24348 |
| 51 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +17 | 3007 |
| 52 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +17 | 20275 |
| 53 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 35275 |
| 54 | [different-ai/openwork](https://github.com/different-ai/openwork) | +16 | 21941 |
| 55 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +16 | 34856 |
| 56 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +16 | 15134 |
| 57 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +16 | 30707 |
| 58 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +15 | 18401 |
| 59 | [yc-software/qm](https://github.com/yc-software/qm) | +15 | 13225 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +15 | 29910 |
| 61 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +14 | 5161 |
| 62 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +14 | 24304 |
| 63 | [every-app/open-seo](https://github.com/every-app/open-seo) | +14 | 11457 |
| 64 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 6096 |
| 65 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +13 | 40724 |
| 66 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 67 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 38696 |
| 68 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 640 |
| 69 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +12 | 4530 |
| 70 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 47761 |
| 71 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 760 |
| 72 | [multica-ai/multica](https://github.com/multica-ai/multica) | +12 | 45617 |
| 73 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +12 | 44049 |
| 74 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +12 | 925 |
| 75 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +12 | 1045 |
| 76 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2765 |
| 77 | [ben-z/findphone](https://github.com/ben-z/findphone) | +12 | 1249 |
| 78 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +11 | 4020 |
| 79 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +11 | 46605 |
| 80 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +11 | 18403 |
| 81 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +11 | 7920 |
| 82 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +11 | 33752 |
| 83 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +10 | 1519 |
| 84 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +10 | 2256 |
| 85 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +10 | 1854 |
| 86 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +10 | 2254 |
| 87 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 3005 |
| 88 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +10 | 31805 |
| 89 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +10 | 18396 |
| 90 | [browser-use/video-use](https://github.com/browser-use/video-use) | +10 | 20574 |
| 91 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1087 |
| 92 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 361 |
| 93 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +9 | 865 |
| 94 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +9 | 45329 |
| 95 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +9 | 14015 |
| 96 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +9 | 19820 |
| 97 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +9 | 2856 |
| 98 | [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | +9 | 2665 |
| 99 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +9 | 2277 |
| 100 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2432 |
| 101 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +9 | 1201 |
| 102 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +9 | 8712 |
| 103 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +9 | 9884 |
| 104 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 924 |
| 105 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +9 | 2544 |
| 106 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +8 | 11374 |
| 107 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +8 | 30426 |
| 108 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 337 |
| 109 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1485 |
| 110 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +8 | 5405 |
| 111 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +8 | 8485 |
| 112 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +7 | 0 |
| 113 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 4900 |
| 114 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 42196 |
| 115 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +7 | 3961 |
| 116 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +6 | 8874 |
| 117 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +6 | 2213 |
| 118 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +6 | 1118 |
| 119 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +6 | 5894 |
| 120 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1387 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +237 | 14844 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +156 | 46535 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +147 | 15033 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +140 | 36586 |
| 5 | [block/buzz](https://github.com/block/buzz) | +126 | 26662 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +125 | 43736 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +92 | 20815 |
| 8 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +92 | 28646 |
| 9 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +91 | 24304 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +90 | 28203 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +85 | 19968 |
| 12 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +81 | 24418 |
| 13 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +80 | 14309 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +73 | 19722 |
| 15 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +70 | 31372 |
| 16 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +69 | 16838 |
| 17 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +69 | 30707 |
| 18 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +66 | 13615 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +64 | 27927 |
| 20 | [brightdata/cli](https://github.com/brightdata/cli) | +61 | 4610 |
| 21 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +59 | 7900 |
| 22 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +56 | 20484 |
| 23 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +55 | 23596 |
| 24 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10580 |
| 25 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +53 | 8347 |
| 26 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21330 |
| 27 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +51 | 14995 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +51 | 45491 |
| 29 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +50 | 33752 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +49 | 11678 |
| 31 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +49 | 15134 |
| 32 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +48 | 9584 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +47 | 35156 |
| 34 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +45 | 62566 |
| 35 | [google/skills](https://github.com/google/skills) | +44 | 17888 |
| 36 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46605 |
| 37 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +44 | 24197 |
| 38 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +44 | 29910 |
| 39 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +44 | 47761 |
| 40 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +43 | 11374 |
| 41 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1480 |
| 42 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 34181 |
| 43 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +41 | 5425 |
| 44 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +41 | 38696 |
| 45 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +39 | 17332 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +39 | 40724 |
| 47 | [yc-software/qm](https://github.com/yc-software/qm) | +38 | 13225 |
| 48 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +38 | 9862 |
| 49 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +38 | 20275 |
| 50 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8390 |
| 51 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +37 | 14944 |
| 52 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +36 | 19503 |
| 53 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +35 | 4817 |
| 54 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 34856 |
| 55 | [trycompai/crm](https://github.com/trycompai/crm) | +33 | 8313 |
| 56 | [blader/humanizer](https://github.com/blader/humanizer) | +33 | 35275 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 44049 |
| 58 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +33 | 8061 |
| 59 | [openai/codex-security](https://github.com/openai/codex-security) | +32 | 9701 |
| 60 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 45617 |
| 61 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +31 | 9759 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +30 | 9675 |
| 63 | [malisper/pgrust](https://github.com/malisper/pgrust) | +30 | 4357 |
| 64 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +30 | 5614 |
| 65 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +29 | 5741 |
| 66 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +29 | 5405 |
| 67 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +29 | 11066 |
| 68 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +28 | 21294 |
| 69 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +28 | 7920 |
| 70 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +27 | 3079 |
| 71 | [different-ai/openwork](https://github.com/different-ai/openwork) | +27 | 21941 |
| 72 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7908 |
| 73 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +27 | 28719 |
| 74 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +26 | 0 |
| 75 | [every-app/open-seo](https://github.com/every-app/open-seo) | +26 | 11457 |
| 76 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +26 | 45329 |
| 77 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24348 |
| 78 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 846 |
| 79 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +24 | 18401 |
| 80 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +24 | 8570 |
| 81 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31805 |
| 82 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9765 |
| 83 | [spinabot/brigade](https://github.com/spinabot/brigade) | +23 | 2546 |
| 84 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +23 | 4379 |
| 85 | [get-bb/bb](https://github.com/get-bb/bb) | +23 | 1763 |
| 86 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20574 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36808 |
| 88 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3961 |
| 89 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +22 | 3005 |
| 90 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +22 | 14015 |
| 91 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +21 | 8874 |
| 92 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +21 | 5161 |
| 93 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 943 |
| 94 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8485 |
| 95 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +20 | 42196 |
| 96 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +19 | 5876 |
| 97 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 4900 |
| 98 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +19 | 5657 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13325 |
| 100 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +17 | 2277 |
| 101 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +17 | 3007 |
| 102 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +17 | 8712 |
| 103 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11167 |
| 104 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 7444 |
| 105 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +15 | 2856 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +15 | 19820 |
| 107 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15 | 9884 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16452 |
| 109 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +15 | 31769 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6096 |
| 111 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 15942 |
| 112 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 5063 |
| 113 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +13 | 4530 |
| 114 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 4020 |
| 115 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 640 |
| 116 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29946 |
| 117 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +13 | 15472 |
| 118 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +13 | 35273 |
| 119 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +13 | 1854 |
| 120 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 121 | [penecho/penecho](https://github.com/penecho/penecho) | +13 | 2039 |
| 122 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 760 |
| 123 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2432 |
| 124 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2765 |
| 125 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 30426 |
| 126 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46899 |
| 127 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 2188 |
| 128 | [decolua/9router](https://github.com/decolua/9router) | +12 | 25294 |
| 129 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27391 |
| 130 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46936 |
| 131 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 33327 |
| 132 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +11 | 10168 |
| 133 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3647 |
| 134 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +11 | 10282 |
| 135 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4889 |
| 136 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1087 |
| 137 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +10 | 1201 |
| 138 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +10 | 1784 |
| 139 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5894 |
| 140 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +10 | 44842 |
| 141 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2102 |
| 142 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10427 |
| 143 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +10 | 9855 |
| 144 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +10 | 5447 |
| 145 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1586 |
| 146 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 875 |
| 147 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1814 |
| 148 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +10 | 9883 |
| 149 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1869 |
| 150 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 151 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 361 |
| 152 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 924 |
| 153 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +9 | 2544 |
| 154 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +9 | 2213 |
| 155 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8562 |
| 156 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1118 |
| 157 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1273 |
| 158 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28281 |
| 159 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +9 | 5347 |
| 160 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +9 | 5085 |
| 161 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1682 |
| 162 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8126 |
| 163 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +9 | 3232 |
| 164 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2151 |
| 165 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 337 |
| 166 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1485 |
| 167 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +8 | 894 |
| 168 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14556 |
| 169 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +8 | 3347 |
| 170 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 10799 |
| 171 | [anbeime/skill](https://github.com/anbeime/skill) | +8 | 5173 |
| 172 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19585 |
| 173 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +8 | 5337 |
| 174 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +8 | 6575 |
| 175 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2000 |
| 176 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1111 |
| 177 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +8 | 29976 |
| 178 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6309 |
| 179 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6713 |
| 180 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 40995 |
| 181 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10571 |
| 182 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24191 |
| 183 | [uber/ADR](https://github.com/uber/ADR) | +7 | 1387 |
| 184 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1681 |
| 185 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +7 | 2533 |
| 186 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6069 |
| 187 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +7 | 1953 |
| 188 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27335 |
| 189 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +7 | 3253 |
| 190 | [open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) | +6 | 1138 |
| 191 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 485 |
| 192 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 193 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1309 |
| 194 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 267 |
| 195 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 246 |
| 196 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 438 |
| 197 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 2995 |
| 198 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5649 |
| 199 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14598 |
| 200 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 28122 |
| 201 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 525 |
| 202 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 544 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5803 |
| 204 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1469 |
| 205 | [LiPu-jpg/Openwrite](https://github.com/LiPu-jpg/Openwrite) | +5 | 560 |
| 206 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 465 |
| 207 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7142 |
| 208 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +5 | 9442 |
| 209 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2958 |
| 210 | [openai/plugins](https://github.com/openai/plugins) | +5 | 5067 |
| 211 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1241 |
| 212 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1319 |
| 213 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8538 |
| 214 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 690 |
| 215 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1218 |
| 216 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +5 | 0 |
| 217 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 271 |
| 218 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1174 |
| 219 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +4 | 405 |
| 220 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5463 |
| 221 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +4 | 377 |
| 222 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11302 |
| 223 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4904 |
| 224 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5170 |
| 225 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3319 |
| 226 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9526 |
| 227 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +4 | 2741 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1323 |
| 229 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 409 |
| 230 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 768 |
| 231 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +4 | 5501 |
| 232 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 100 |
| 233 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 883 |
| 234 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3205 |
| 235 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28366 |
| 236 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4649 |
| 237 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +3 | 1281 |
| 238 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12267 |
| 239 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 117 |
| 240 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1798 |
| 241 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 922 |
| 242 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 907 |
| 243 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 494 |
| 244 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18886 |
| 245 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3402 |
| 246 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 735 |
| 247 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 448 |
| 248 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 249 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 407 |
| 250 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +3 | 5906 |
| 251 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 147 |
| 252 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 867 |
| 253 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 286 |
| 254 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1168 |
| 255 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2004 |
| 256 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 5033 |
| 257 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9197 |
| 258 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 824 |
| 259 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 890 |
| 260 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 320 |
| 261 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 501 |
| 262 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6273 |
| 263 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +2 | 419 |
| 264 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +2 | 186 |
| 265 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +2 | 8961 |
| 266 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 694 |
| 267 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +2 | 1131 |
| 268 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 40 |
| 269 | [rubenmarcus/csbrasil](https://github.com/rubenmarcus/csbrasil) | +2 | 182 |
| 270 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2856 |
| 271 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +2 | 29 |
| 272 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +2 | 184 |
| 273 | [future-agi/future-agi](https://github.com/future-agi/future-agi) | +2 | 1656 |
| 274 | [hwttop5/tabbit2api](https://github.com/hwttop5/tabbit2api) | +2 | 87 |
| 275 | [Leon-PanPan/dragonclaw](https://github.com/Leon-PanPan/dragonclaw) | +2 | 480 |
| 276 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 277 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 862 |
| 278 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 71 |
| 279 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1282 |
| 280 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 326 |
| 281 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2876 |
| 282 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 238 |
| 283 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +2 | 2900 |
| 284 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3124 |
| 285 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 263 |
| 286 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10375 |
| 287 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1191 |
| 288 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1380 |
| 289 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 507 |
| 290 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 103 |
| 291 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2521 |
| 292 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3805 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 294 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2698 |
| 295 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10482 |
| 296 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 297 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 70 |
| 298 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +1 | 413 |
| 299 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 889 |
| 300 | [The412Banner/bannerhub-revanced](https://github.com/The412Banner/bannerhub-revanced) | +1 | 149 |
