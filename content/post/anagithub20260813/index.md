---
title: "2026-08-13 GitHub增长趋势报告"
description: "1.watermarks-remover+23 2.diagram-design+16 3.ppt-master+8 4.open-seo+6 5.colibri+4"
date: 2026-08-13T20:44:08+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-13 20:44:08

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
        'daily': {"categories": ["alibaba/open-code-review", "block/buzz", "cactus-compute/needle", "tanishqkancharla/calldiff", "herdrdev/herdr", "stablyai/orca", "bojieli/ai-agent-book", "Devin-AXIS/iPolloWork", "huangruiteng/loopx", "emilkowalski/skills", "Zeejay0/gathered-scenes-zine-skill", "PrimeIntellect-ai/prime-agent", "firecrawl/anydoc", "repowise-dev/repowise", "macro-inc/macro", "JustVugg/colibri", "every-app/open-seo", "hugohe3/ppt-master", "cathrynlavery/diagram-design", "guillaumemeyer/watermarks-remover"], "data": [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 6, 8, 16, 23]},
        'weekly': {"categories": ["ayghri/i-have-adhd", "ifixai-ai/iFixAi", "TencentCloud/TencentDB-Agent-Memory", "talivia-group/talivia", "google/skills", "herdrdev/herdr", "MiniMax-AI/MiniMax-H3", "emilkowalski/skills", "stablyai/orca", "pranshuparmar/witr", "cloudflare/cloudflare-os", "zhaoxuya520/reverse-skill", "cathrynlavery/diagram-design", "block/buzz", "virgiliojr94/book-to-skill", "brightdata/cli", "floci-io/floci", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [33, 36, 39, 40, 41, 41, 41, 43, 47, 48, 49, 52, 53, 54, 58, 59, 61, 73, 143, 235]},
        'monthly': {"categories": ["brightdata/cli", "HKUDS/Vibe-Trading", "iOfficeAI/OfficeCLI", "Fei-Away/Codex-Dream-Skin", "k1tbyte/Wand-Enhancer", "MadsLorentzen/ai-job-search", "floci-io/floci", "JustVugg/colibri", "andrewyng/openworker", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "emilkowalski/skills", "herdrdev/herdr", "virgiliojr94/book-to-skill", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [61, 63, 64, 66, 68, 69, 72, 80, 80, 81, 86, 91, 91, 93, 125, 128, 143, 151, 155, 241]}
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
| 1 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +23 | 5048 |
| 2 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +16 | 14034 |
| 3 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 46479 |
| 4 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 11739 |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +4 | 24487 |
| 6 | [macro-inc/macro](https://github.com/macro-inc/macro) | +4 | 2544 |
| 7 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +4 | 5722 |
| 8 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +4 | 15643 |
| 9 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +4 | 15404 |
| 10 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +4 | 3370 |
| 11 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 28910 |
| 12 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +3 | 4595 |
| 13 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +3 | 3554 |
| 14 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 36978 |
| 15 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 44837 |
| 16 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +3 | 28639 |
| 17 | [tanishqkancharla/calldiff](https://github.com/tanishqkancharla/calldiff) | +3 | 385 |
| 18 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +3 | 4887 |
| 19 | [block/buzz](https://github.com/block/buzz) | +2 | 27145 |
| 20 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +2 | 20403 |
| 21 | [Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills) | +2 | 1616 |
| 22 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +2 | 11253 |
| 23 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2 | 35431 |
| 24 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +2 | 1682 |
| 25 | [zerx-lab/FluxDown](https://github.com/zerx-lab/FluxDown) | +2 | 2026 |
| 26 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +2 | 34447 |
| 27 | [AntigmaLabs/ante-preview](https://github.com/AntigmaLabs/ante-preview) | +2 | 1566 |
| 28 | [yc-software/qm](https://github.com/yc-software/qm) | +2 | 13437 |
| 29 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 15301 |
| 30 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +2 | 3452 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +235 | 15404 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +143 | 15643 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +73 | 47226 |
| 4 | [floci-io/floci](https://github.com/floci-io/floci) | +61 | 19921 |
| 5 | [brightdata/cli](https://github.com/brightdata/cli) | +59 | 4964 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +58 | 21172 |
| 7 | [block/buzz](https://github.com/block/buzz) | +54 | 27145 |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +53 | 14034 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +52 | 24894 |
| 10 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +49 | 8039 |
| 11 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +48 | 21381 |
| 12 | [stablyai/orca](https://github.com/stablyai/orca) | +47 | 44837 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +43 | 28910 |
| 14 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +41 | 5737 |
| 15 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +41 | 28639 |
| 16 | [google/skills](https://github.com/google/skills) | +41 | 18046 |
| 17 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +40 | 1446 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +39 | 21170 |
| 19 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +36 | 8519 |
| 20 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +33 | 20212 |
| 21 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +33 | 14400 |
| 22 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +33 | 6509 |
| 23 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +31 | 17053 |
| 24 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +30 | 62733 |
| 25 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +30 | 36978 |
| 26 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +29 | 46479 |
| 27 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +28 | 3370 |
| 28 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +25 | 34447 |
| 29 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 30 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +24 | 9755 |
| 31 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +24 | 15300 |
| 32 | [get-bb/bb](https://github.com/get-bb/bb) | +24 | 1846 |
| 33 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +24 | 21334 |
| 34 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +23 | 5049 |
| 35 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +23 | 4595 |
| 36 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +23 | 8684 |
| 37 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +23 | 4933 |
| 38 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 24537 |
| 39 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +23 | 12029 |
| 40 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +21 | 15008 |
| 41 | [spinabot/brigade](https://github.com/spinabot/brigade) | +20 | 2619 |
| 42 | [malisper/pgrust](https://github.com/malisper/pgrust) | +20 | 4392 |
| 43 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 984 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +19 | 35431 |
| 45 | [every-app/open-seo](https://github.com/every-app/open-seo) | +19 | 11739 |
| 46 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +19 | 3452 |
| 47 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +19 | 20403 |
| 48 | [trycompai/crm](https://github.com/trycompai/crm) | +19 | 8383 |
| 49 | [blader/humanizer](https://github.com/blader/humanizer) | +19 | 35500 |
| 50 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +19 | 5866 |
| 51 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +19 | 24388 |
| 52 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +18 | 28145 |
| 53 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +18 | 9810 |
| 54 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +17 | 24487 |
| 55 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +17 | 18579 |
| 56 | [yc-software/qm](https://github.com/yc-software/qm) | +17 | 13437 |
| 57 | [different-ai/openwork](https://github.com/different-ai/openwork) | +17 | 22055 |
| 58 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +17 | 15301 |
| 59 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +17 | 23673 |
| 60 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +16 | 31529 |
| 61 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +15 | 35044 |
| 62 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +15 | 30018 |
| 63 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 30781 |
| 64 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +13 | 40853 |
| 65 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 38828 |
| 66 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 671 |
| 67 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +12 | 1682 |
| 68 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +12 | 4569 |
| 69 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4015 |
| 70 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +12 | 5242 |
| 71 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 47958 |
| 72 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 46670 |
| 73 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 797 |
| 74 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +12 | 0 |
| 75 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +12 | 930 |
| 76 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +12 | 1047 |
| 77 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +11 | 6129 |
| 78 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +11 | 1682 |
| 79 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +11 | 919 |
| 80 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +11 | 18460 |
| 81 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +11 | 44154 |
| 82 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +11 | 2836 |
| 83 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +10 | 2266 |
| 84 | [multica-ai/multica](https://github.com/multica-ai/multica) | +10 | 45835 |
| 85 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +10 | 19898 |
| 86 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +10 | 11253 |
| 87 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +10 | 2373 |
| 88 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +10 | 28832 |
| 89 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +10 | 31896 |
| 90 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +10 | 18464 |
| 91 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 367 |
| 92 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +9 | 11580 |
| 93 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +9 | 3554 |
| 94 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +9 | 875 |
| 95 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +9 | 45399 |
| 96 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +9 | 2902 |
| 97 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2479 |
| 98 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +9 | 1291 |
| 99 | [browser-use/video-use](https://github.com/browser-use/video-use) | +9 | 20631 |
| 100 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +9 | 9907 |
| 101 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +9 | 1158 |
| 102 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 934 |
| 103 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +8 | 5722 |
| 104 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +8 | 2071 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +8 | 14097 |
| 106 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 2649 |
| 107 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +8 | 8803 |
| 108 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +8 | 5503 |
| 109 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 338 |
| 110 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1497 |
| 111 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +8 | 33743 |
| 112 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +7 | 8926 |
| 113 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +7 | 42364 |
| 114 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +7 | 2323 |
| 115 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +7 | 1130 |
| 116 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 4991 |
| 117 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +6 | 0 |
| 118 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +6 | 3495 |
| 119 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +6 | 4887 |
| 120 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +6 | 973 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +241 | 15404 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 47226 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +151 | 15643 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +143 | 36978 |
| 5 | [block/buzz](https://github.com/block/buzz) | +128 | 27145 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +125 | 44837 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +93 | 21172 |
| 8 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +91 | 28639 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +91 | 28910 |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +86 | 20212 |
| 11 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +81 | 24894 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +80 | 14400 |
| 13 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +80 | 24487 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +72 | 19921 |
| 15 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +69 | 31529 |
| 16 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +68 | 17053 |
| 17 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +66 | 13661 |
| 18 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +64 | 28145 |
| 19 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +63 | 30781 |
| 20 | [brightdata/cli](https://github.com/brightdata/cli) | +61 | 4964 |
| 21 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +59 | 8039 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +58 | 46479 |
| 23 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +56 | 21170 |
| 24 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10623 |
| 25 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +54 | 23673 |
| 26 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +53 | 14034 |
| 27 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21381 |
| 28 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +52 | 8519 |
| 29 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +51 | 15300 |
| 30 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +51 | 15301 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +49 | 12029 |
| 32 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 33743 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +48 | 9810 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +48 | 35431 |
| 35 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +45 | 46670 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +44 | 62733 |
| 37 | [google/skills](https://github.com/google/skills) | +44 | 18046 |
| 38 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +44 | 34447 |
| 39 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +44 | 24537 |
| 40 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +44 | 11580 |
| 41 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +44 | 30018 |
| 42 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +42 | 5737 |
| 43 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1446 |
| 44 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +41 | 47958 |
| 45 | [yc-software/qm](https://github.com/yc-software/qm) | +40 | 13437 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +40 | 20403 |
| 47 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +38 | 17452 |
| 48 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8417 |
| 49 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +38 | 40853 |
| 50 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +38 | 38828 |
| 51 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 4933 |
| 52 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +37 | 15008 |
| 53 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 35500 |
| 54 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +35 | 35044 |
| 55 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +34 | 19568 |
| 56 | [trycompai/crm](https://github.com/trycompai/crm) | +33 | 8383 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 44154 |
| 58 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +33 | 6510 |
| 59 | [every-app/open-seo](https://github.com/every-app/open-seo) | +32 | 11739 |
| 60 | [openai/codex-security](https://github.com/openai/codex-security) | +32 | 9764 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 45835 |
| 62 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +32 | 9975 |
| 63 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +31 | 9755 |
| 64 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +30 | 5866 |
| 65 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +30 | 8128 |
| 66 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +29 | 3370 |
| 67 | [malisper/pgrust](https://github.com/malisper/pgrust) | +29 | 4392 |
| 68 | [different-ai/openwork](https://github.com/different-ai/openwork) | +28 | 22055 |
| 69 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +28 | 21334 |
| 70 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +28 | 28832 |
| 71 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +28 | 8096 |
| 72 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5503 |
| 73 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +28 | 11253 |
| 74 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7938 |
| 75 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +26 | 18579 |
| 76 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4595 |
| 77 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +26 | 8684 |
| 78 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24388 |
| 79 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 1846 |
| 80 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 81 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +25 | 45399 |
| 82 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9834 |
| 83 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +23 | 0 |
| 84 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +23 | 5049 |
| 85 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20631 |
| 86 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 31896 |
| 87 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36935 |
| 88 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3978 |
| 89 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +22 | 3063 |
| 90 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +22 | 14097 |
| 91 | [spinabot/brigade](https://github.com/spinabot/brigade) | +21 | 2619 |
| 92 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +21 | 5242 |
| 93 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +20 | 8926 |
| 94 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 984 |
| 95 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8505 |
| 96 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +19 | 3452 |
| 97 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +19 | 5962 |
| 98 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 4991 |
| 99 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 42364 |
| 100 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13373 |
| 101 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +17 | 2339 |
| 102 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11175 |
| 103 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +17 | 5717 |
| 104 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8803 |
| 105 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 7673 |
| 106 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +15 | 2902 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +15 | 19898 |
| 108 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15 | 9907 |
| 109 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16471 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6129 |
| 111 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 15995 |
| 112 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +14 | 15501 |
| 113 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +14 | 31826 |
| 114 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 5092 |
| 115 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2053 |
| 116 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +13 | 4569 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 4015 |
| 118 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 671 |
| 119 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 5722 |
| 120 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +13 | 2071 |
| 121 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 122 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25367 |
| 123 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 797 |
| 124 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2479 |
| 125 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2836 |
| 126 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +12 | 30001 |
| 127 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 30528 |
| 128 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +12 | 46969 |
| 129 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46944 |
| 130 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 2203 |
| 131 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +12 | 35602 |
| 132 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27467 |
| 133 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +11 | 1682 |
| 134 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +11 | 10472 |
| 135 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +11 | 10210 |
| 136 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3648 |
| 137 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4899 |
| 138 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1158 |
| 139 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +10 | 1291 |
| 140 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +10 | 2649 |
| 141 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5903 |
| 142 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +10 | 1807 |
| 143 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2323 |
| 144 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +10 | 1130 |
| 145 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2149 |
| 146 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 33427 |
| 147 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 950 |
| 148 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1828 |
| 149 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 3277 |
| 150 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 10325 |
| 151 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +10 | 9906 |
| 152 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1879 |
| 153 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 154 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 367 |
| 155 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 921 |
| 156 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 934 |
| 157 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 44905 |
| 158 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3432 |
| 159 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8579 |
| 160 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 9882 |
| 161 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5511 |
| 162 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1288 |
| 163 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28382 |
| 164 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 2830 |
| 165 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +9 | 4199 |
| 166 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +9 | 5101 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1697 |
| 168 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8178 |
| 169 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2162 |
| 170 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 6373 |
| 171 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 338 |
| 172 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1497 |
| 173 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24236 |
| 174 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14596 |
| 175 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +8 | 6593 |
| 176 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 10843 |
| 177 | [browser-act/skills](https://github.com/browser-act/skills) | +8 | 5366 |
| 178 | [anbeime/skill](https://github.com/anbeime/skill) | +8 | 5233 |
| 179 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19646 |
| 180 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2107 |
| 181 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1129 |
| 182 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6718 |
| 183 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41014 |
| 184 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10592 |
| 185 | [uber/ADR](https://github.com/uber/ADR) | +7 | 1411 |
| 186 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1712 |
| 187 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +7 | 2536 |
| 188 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1357 |
| 189 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 20 |
| 190 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27363 |
| 191 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 30009 |
| 192 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +7 | 3256 |
| 193 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +6 | 4887 |
| 194 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +6 | 973 |
| 195 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 196 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 268 |
| 197 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 253 |
| 198 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 438 |
| 199 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 2999 |
| 200 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5666 |
| 201 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 28156 |
| 202 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14608 |
| 203 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +6 | 8565 |
| 204 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 526 |
| 205 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 529 |
| 206 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5803 |
| 207 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1481 |
| 208 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 389 |
| 209 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 488 |
| 210 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7167 |
| 211 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 756 |
| 212 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2987 |
| 213 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1268 |
| 214 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1322 |
| 215 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 693 |
| 216 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5517 |
| 217 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1218 |
| 218 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 277 |
| 219 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1200 |
| 220 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5518 |
| 221 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11320 |
| 222 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4911 |
| 223 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +4 | 9463 |
| 224 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5177 |
| 225 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5072 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3329 |
| 227 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9552 |
| 228 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1346 |
| 229 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 410 |
| 230 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +4 | 0 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 103 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 915 |
| 233 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3220 |
| 234 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28378 |
| 235 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4658 |
| 236 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 152 |
| 237 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 948 |
| 238 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +3 | 1295 |
| 239 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12289 |
| 240 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 188 |
| 241 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1142 |
| 242 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1825 |
| 243 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 917 |
| 244 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 524 |
| 245 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18913 |
| 246 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3411 |
| 247 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 746 |
| 248 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2776 |
| 249 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 448 |
| 250 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 251 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 410 |
| 252 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +3 | 5926 |
| 253 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 147 |
| 254 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 879 |
| 255 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 586 |
| 256 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 291 |
| 257 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1178 |
| 258 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2018 |
| 259 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 5051 |
| 260 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9196 |
| 261 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 827 |
| 262 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 891 |
| 263 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 702 |
| 264 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 323 |
| 265 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 503 |
| 266 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6283 |
| 267 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +2 | 466 |
| 268 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +2 | 1585 |
| 269 | [SamurAIGPT/seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) | +2 | 75 |
| 270 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +2 | 1238 |
| 271 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +2 | 8968 |
| 272 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 40 |
| 273 | [rubenmarcus/csbrasil](https://github.com/rubenmarcus/csbrasil) | +2 | 188 |
| 274 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2867 |
| 275 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +2 | 30 |
| 276 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 277 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 415 |
| 278 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 864 |
| 279 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 88 |
| 280 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1287 |
| 281 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 334 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2882 |
| 283 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 247 |
| 284 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +2 | 3306 |
| 285 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3139 |
| 286 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 265 |
| 287 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10391 |
| 288 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1192 |
| 289 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1384 |
| 290 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 509 |
| 291 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2531 |
| 292 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3810 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 294 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2701 |
| 295 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10487 |
| 296 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 297 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +1 | 747 |
| 298 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 76 |
| 299 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 900 |
| 300 | [zgcwkjOpenProject/XPoser_MiBackup](https://github.com/zgcwkjOpenProject/XPoser_MiBackup) | +1 | 89 |
