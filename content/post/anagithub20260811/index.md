---
title: "2026-08-11 GitHub增长趋势报告"
description: "1.diagram-design+9 2.MiniMax-H3+9 3.prime-agent+8 4.DeepTutor+5 5.LifeOS+4"
date: 2026-08-11T20:45:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-11 20:45:48

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
        'daily': {"categories": ["jnMetaCode/agency-agents-zh", "Yuan1z0825/nature-skills", "block/buzz", "Conway-Research/automaton", "ayghri/i-have-adhd", "amap-cvlab/ABot-World", "pingdotgg/t3code", "baidu/Unlimited-OCR", "firecrawl/anydoc", "melgarafael/DeskcommCRM", "luongnv89/claude-howto", "hugohe3/ppt-master", "img2threejs/img2threejs", "bojieli/ai-agent-book", "elementalsouls/Claude-BugHunter", "danielmiessler/LifeOS", "HKUDS/DeepTutor", "PrimeIntellect-ai/prime-agent", "MiniMax-AI/MiniMax-H3", "cathrynlavery/diagram-design"], "data": [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 8, 9, 9]},
        'weekly': {"categories": ["ayghri/i-have-adhd", "MiniMax-AI/MiniMax-H3", "andrewyng/openworker", "herdrdev/herdr", "stablyai/orca", "talivia-group/talivia", "google/skills", "emilkowalski/skills", "ifixai-ai/iFixAi", "TencentCloud/TencentDB-Agent-Memory", "pranshuparmar/witr", "block/buzz", "brightdata/cli", "cloudflare/cloudflare-os", "zhaoxuya520/reverse-skill", "floci-io/floci", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute", "firecrawl/anydoc", "PrimeIntellect-ai/prime-agent"], "data": [30, 34, 35, 35, 38, 41, 41, 41, 42, 45, 50, 53, 57, 57, 58, 60, 60, 75, 141, 232]},
        'monthly': {"categories": ["cloudflare/cloudflare-os", "iOfficeAI/OfficeCLI", "Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "MadsLorentzen/ai-job-search", "floci-io/floci", "k1tbyte/Wand-Enhancer", "zhaoxuya520/reverse-skill", "andrewyng/openworker", "ayghri/i-have-adhd", "herdrdev/herdr", "emilkowalski/skills", "virgiliojr94/book-to-skill", "JustVugg/colibri", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [57, 63, 65, 69, 70, 71, 71, 78, 80, 81, 86, 90, 91, 98, 117, 124, 138, 141, 153, 232]}
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
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +9 | 6564 |
| 2 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +9 | 5190 |
| 3 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +8 | 13983 |
| 4 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 34628 |
| 5 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +4 | 18290 |
| 6 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +4 | 3480 |
| 7 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +3 | 36152 |
| 8 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +3 | 10940 |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 44852 |
| 10 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3 | 40990 |
| 11 | [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | +3 | 475 |
| 12 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +3 | 14338 |
| 13 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 23499 |
| 14 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +3 | 18252 |
| 15 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +3 | 2211 |
| 16 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +2 | 19658 |
| 17 | [Conway-Research/automaton](https://github.com/Conway-Research/automaton) | +2 | 5626 |
| 18 | [block/buzz](https://github.com/block/buzz) | +2 | 26316 |
| 19 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +2 | 34647 |
| 20 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +2 | 19265 |
| 21 | [karanb192/itr-wala](https://github.com/karanb192/itr-wala) | +2 | 612 |
| 22 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 3705 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2 | 45412 |
| 24 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +2 | 894 |
| 25 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2 | 31718 |
| 26 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +2 | 2504 |
| 27 | [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) | +2 | 963 |
| 28 | [floci-io/floci](https://github.com/floci-io/floci) | +2 | 19515 |
| 29 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +2 | 28670 |
| 30 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +2 | 19840 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +232 | 13983 |
| 2 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +141 | 14338 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +75 | 45841 |
| 4 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +60 | 20460 |
| 5 | [floci-io/floci](https://github.com/floci-io/floci) | +60 | 19515 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +58 | 23918 |
| 7 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +57 | 7680 |
| 8 | [brightdata/cli](https://github.com/brightdata/cli) | +57 | 4135 |
| 9 | [block/buzz](https://github.com/block/buzz) | +53 | 26316 |
| 10 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +50 | 21276 |
| 11 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +45 | 19840 |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +42 | 8339 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +41 | 28400 |
| 14 | [google/skills](https://github.com/google/skills) | +41 | 17756 |
| 15 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1528 |
| 16 | [stablyai/orca](https://github.com/stablyai/orca) | +38 | 42632 |
| 17 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +35 | 27601 |
| 18 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +35 | 14196 |
| 19 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +34 | 5190 |
| 20 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +30 | 19658 |
| 21 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +30 | 14660 |
| 22 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +29 | 16628 |
| 23 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +29 | 36152 |
| 24 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +26 | 33948 |
| 25 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 850 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +25 | 62067 |
| 27 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +24 | 21244 |
| 28 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +24 | 11402 |
| 29 | [trycompai/crm](https://github.com/trycompai/crm) | +23 | 8206 |
| 30 | [get-bb/bb](https://github.com/get-bb/bb) | +23 | 1635 |
| 31 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +22 | 23890 |
| 32 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +21 | 14894 |
| 33 | [malisper/pgrust](https://github.com/malisper/pgrust) | +21 | 4323 |
| 34 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +20 | 4647 |
| 35 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 909 |
| 36 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +20 | 2549 |
| 37 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +19 | 24288 |
| 38 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +19 | 4144 |
| 39 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +19 | 5530 |
| 40 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +19 | 9309 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +18 | 44852 |
| 42 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +17 | 31253 |
| 43 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +17 | 6565 |
| 44 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +17 | 27693 |
| 45 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +17 | 8345 |
| 46 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 35013 |
| 47 | [different-ai/openwork](https://github.com/different-ai/openwork) | +16 | 21856 |
| 48 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +16 | 20108 |
| 49 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +16 | 23499 |
| 50 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +16 | 15022 |
| 51 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +15 | 18253 |
| 52 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +15 | 34628 |
| 53 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 30623 |
| 54 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +15 | 34647 |
| 55 | [every-app/open-seo](https://github.com/every-app/open-seo) | +14 | 11340 |
| 56 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +14 | 8869 |
| 57 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +14 | 29807 |
| 58 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 6009 |
| 59 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +13 | 2504 |
| 60 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +13 | 24047 |
| 61 | [yc-software/qm](https://github.com/yc-software/qm) | +13 | 13088 |
| 62 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 63 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 38566 |
| 64 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 616 |
| 65 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 46540 |
| 66 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 732 |
| 67 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 40570 |
| 68 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +12 | 922 |
| 69 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +12 | 5036 |
| 70 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +12 | 1043 |
| 71 | [browser-use/video-use](https://github.com/browser-use/video-use) | +12 | 20519 |
| 72 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2688 |
| 73 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +12 | 7758 |
| 74 | [ben-z/findphone](https://github.com/ben-z/findphone) | +12 | 1233 |
| 75 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +12 | 33762 |
| 76 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +11 | 4022 |
| 77 | [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | +11 | 18290 |
| 78 | [multica-ai/multica](https://github.com/multica-ai/multica) | +11 | 45412 |
| 79 | [Hidashimora/free-vpn-anti-rkn](https://github.com/Hidashimora/free-vpn-anti-rkn) | +11 | 390 |
| 80 | [HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio) | +11 | 782 |
| 81 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 2908 |
| 82 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +10 | 28600 |
| 83 | [perplexityai/numbat](https://github.com/perplexityai/numbat) | +10 | 894 |
| 84 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1031 |
| 85 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +10 | 18308 |
| 86 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +10 | 8572 |
| 87 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +10 | 8455 |
| 88 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 343 |
| 89 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +9 | 2176 |
| 90 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +9 | 4457 |
| 91 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +9 | 847 |
| 92 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +9 | 47237 |
| 93 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +9 | 2752 |
| 94 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +9 | 45243 |
| 95 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2363 |
| 96 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +9 | 2162 |
| 97 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +9 | 1705 |
| 98 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +9 | 9844 |
| 99 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 920 |
| 100 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +9 | 2404 |
| 101 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +8 | 8802 |
| 102 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +8 | 13955 |
| 103 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +8 | 1098 |
| 104 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 334 |
| 105 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1473 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +8 | 19671 |
| 107 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +8 | 5319 |
| 108 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +7 | 0 |
| 109 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 4796 |
| 110 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +7 | 30328 |
| 111 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +7 | 3941 |
| 112 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +6 | 0 |
| 113 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +6 | 2211 |
| 114 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +6 | 5878 |
| 115 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +6 | 1086 |
| 116 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 466 |
| 117 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +5 | 0 |
| 118 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1445 |
| 119 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +5 | 10940 |
| 120 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +5 | 1762 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +232 | 13983 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +153 | 45841 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +141 | 14338 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +138 | 36152 |
| 5 | [block/buzz](https://github.com/block/buzz) | +124 | 26316 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +117 | 42633 |
| 7 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +98 | 24047 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +91 | 20460 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +90 | 28400 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +86 | 27601 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +81 | 19658 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +80 | 14196 |
| 13 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +78 | 23918 |
| 14 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +71 | 16628 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +71 | 19515 |
| 16 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +70 | 31253 |
| 17 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +69 | 30623 |
| 18 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +65 | 13572 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +63 | 27693 |
| 20 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +57 | 7680 |
| 21 | [brightdata/cli](https://github.com/brightdata/cli) | +57 | 4135 |
| 22 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10558 |
| 23 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +54 | 23499 |
| 24 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +53 | 19840 |
| 25 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21276 |
| 26 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +52 | 8339 |
| 27 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +50 | 14660 |
| 28 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +50 | 15022 |
| 29 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +50 | 33762 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +49 | 11402 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +47 | 44852 |
| 32 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +45 | 9309 |
| 33 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46540 |
| 34 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +44 | 34628 |
| 35 | [google/skills](https://github.com/google/skills) | +43 | 17756 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +43 | 23890 |
| 37 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +43 | 38566 |
| 38 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1528 |
| 39 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 33948 |
| 40 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +42 | 29807 |
| 41 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +41 | 47237 |
| 42 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +41 | 50082 |
| 43 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +40 | 10940 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 62068 |
| 45 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8357 |
| 46 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +38 | 14894 |
| 47 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +38 | 40570 |
| 48 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +36 | 20108 |
| 49 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +36 | 19436 |
| 50 | [yc-software/qm](https://github.com/yc-software/qm) | +35 | 13088 |
| 51 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +35 | 17174 |
| 52 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +34 | 5190 |
| 53 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +34 | 4647 |
| 54 | [malisper/pgrust](https://github.com/malisper/pgrust) | +34 | 4323 |
| 55 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +34 | 7992 |
| 56 | [trycompai/crm](https://github.com/trycompai/crm) | +33 | 8206 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +32 | 9621 |
| 58 | [blader/humanizer](https://github.com/blader/humanizer) | +31 | 35013 |
| 59 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 34647 |
| 60 | [multica-ai/multica](https://github.com/multica-ai/multica) | +31 | 45412 |
| 61 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +31 | 9595 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 43940 |
| 63 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +30 | 10834 |
| 64 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +29 | 21244 |
| 65 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +29 | 45243 |
| 66 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +28 | 0 |
| 67 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +28 | 5530 |
| 68 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +28 | 7758 |
| 69 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5319 |
| 70 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7864 |
| 71 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +27 | 28600 |
| 72 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8575 |
| 73 | [different-ai/openwork](https://github.com/different-ai/openwork) | +26 | 21856 |
| 74 | [every-app/open-seo](https://github.com/every-app/open-seo) | +26 | 11340 |
| 75 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +26 | 4497 |
| 76 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24288 |
| 77 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 850 |
| 78 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +25 | 4788 |
| 79 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +24 | 18253 |
| 80 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31718 |
| 81 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9678 |
| 82 | [get-bb/bb](https://github.com/get-bb/bb) | +23 | 1635 |
| 83 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20519 |
| 84 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3941 |
| 85 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36670 |
| 86 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +22 | 4144 |
| 87 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +22 | 2908 |
| 88 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +22 | 8869 |
| 89 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +21 | 8802 |
| 90 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 13955 |
| 91 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 909 |
| 92 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +20 | 2549 |
| 93 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +20 | 8345 |
| 94 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8455 |
| 95 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +19 | 5792 |
| 96 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 4796 |
| 97 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 41935 |
| 98 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +19 | 5607 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13271 |
| 100 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11163 |
| 101 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2225 |
| 102 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8572 |
| 103 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 7236 |
| 104 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +15 | 2752 |
| 105 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15 | 9844 |
| 106 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +15 | 15908 |
| 107 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16421 |
| 108 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +15 | 31708 |
| 109 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +14 | 15417 |
| 110 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +14 | 5020 |
| 111 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 6010 |
| 112 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +13 | 616 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 19671 |
| 114 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29894 |
| 115 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +13 | 35223 |
| 116 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 117 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25233 |
| 118 | [penecho/penecho](https://github.com/penecho/penecho) | +13 | 2023 |
| 119 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4022 |
| 120 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 732 |
| 121 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2363 |
| 122 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2688 |
| 123 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46858 |
| 124 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 2178 |
| 125 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 27316 |
| 126 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +11 | 30328 |
| 127 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +11 | 44782 |
| 128 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46905 |
| 129 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +11 | 1705 |
| 130 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4884 |
| 131 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +10 | 4457 |
| 132 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1031 |
| 133 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +10 | 1762 |
| 134 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5878 |
| 135 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10380 |
| 136 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +10 | 5386 |
| 137 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +10 | 33236 |
| 138 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1575 |
| 139 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +10 | 10116 |
| 140 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 3606 |
| 141 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 10215 |
| 142 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1861 |
| 143 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 144 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 343 |
| 145 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +9 | 1098 |
| 146 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 920 |
| 147 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +9 | 2404 |
| 148 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +9 | 2211 |
| 149 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8533 |
| 150 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1086 |
| 151 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +9 | 2016 |
| 152 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1255 |
| 153 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28224 |
| 154 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +9 | 5130 |
| 155 | [anbeime/skill](https://github.com/anbeime/skill) | +9 | 5117 |
| 156 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +9 | 5074 |
| 157 | [petergyang/human-review](https://github.com/petergyang/human-review) | +9 | 714 |
| 158 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1667 |
| 159 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +9 | 1801 |
| 160 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8072 |
| 161 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +9 | 9850 |
| 162 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2143 |
| 163 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 334 |
| 164 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1473 |
| 165 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +8 | 849 |
| 166 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 14516 |
| 167 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +8 | 3270 |
| 168 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 10749 |
| 169 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9834 |
| 170 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19545 |
| 171 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 4107 |
| 172 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +8 | 2732 |
| 173 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1095 |
| 174 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6255 |
| 175 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6709 |
| 176 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 40990 |
| 177 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24134 |
| 178 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +7 | 2528 |
| 179 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6039 |
| 180 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1664 |
| 181 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +7 | 1944 |
| 182 | [openai/skills](https://github.com/openai/skills) | +7 | 24818 |
| 183 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 3090 |
| 184 | [openai/plugins](https://github.com/openai/plugins) | +7 | 5052 |
| 185 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29950 |
| 186 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +6 | 10549 |
| 187 | [open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) | +6 | 1137 |
| 188 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 466 |
| 189 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1355 |
| 190 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +6 | 12139 |
| 191 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 192 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1245 |
| 193 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 263 |
| 194 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 237 |
| 195 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +6 | 1827 |
| 196 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 428 |
| 197 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27303 |
| 198 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5634 |
| 199 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14591 |
| 200 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 28074 |
| 201 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 2982 |
| 202 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 522 |
| 203 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +6 | 0 |
| 204 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 557 |
| 205 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5810 |
| 206 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1445 |
| 207 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 443 |
| 208 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7090 |
| 209 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +5 | 9412 |
| 210 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +5 | 5162 |
| 211 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2930 |
| 212 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1226 |
| 213 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1309 |
| 214 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8514 |
| 215 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 688 |
| 216 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +5 | 2719 |
| 217 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1219 |
| 218 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +4 | 383 |
| 219 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5413 |
| 220 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +4 | 369 |
| 221 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11272 |
| 222 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4879 |
| 223 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3297 |
| 224 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9505 |
| 225 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1294 |
| 226 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 408 |
| 227 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 763 |
| 228 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +4 | 5481 |
| 229 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 99 |
| 230 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 858 |
| 231 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3193 |
| 232 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28346 |
| 233 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 818 |
| 234 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4643 |
| 235 | [SulgX/SulgX-Panel](https://github.com/SulgX/SulgX-Panel) | +3 | 285 |
| 236 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1791 |
| 237 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 897 |
| 238 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 476 |
| 239 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18861 |
| 240 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3386 |
| 241 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 726 |
| 242 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 446 |
| 243 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 244 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +3 | 684 |
| 245 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 407 |
| 246 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +3 | 5895 |
| 247 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 147 |
| 248 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 857 |
| 249 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 282 |
| 250 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1160 |
| 251 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1996 |
| 252 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 5011 |
| 253 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9204 |
| 254 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 888 |
| 255 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 320 |
| 256 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 498 |
| 257 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6250 |
| 258 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +2 | 676 |
| 259 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1276 |
| 260 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12251 |
| 261 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +2 | 8959 |
| 262 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +2 | 1122 |
| 263 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 37 |
| 264 | [rubenmarcus/csbrasil](https://github.com/rubenmarcus/csbrasil) | +2 | 174 |
| 265 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2841 |
| 266 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +2 | 26 |
| 267 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +2 | 66 |
| 268 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +2 | 184 |
| 269 | [future-agi/future-agi](https://github.com/future-agi/future-agi) | +2 | 1649 |
| 270 | [hwttop5/tabbit2api](https://github.com/hwttop5/tabbit2api) | +2 | 85 |
| 271 | [Leon-PanPan/dragonclaw](https://github.com/Leon-PanPan/dragonclaw) | +2 | 480 |
| 272 | [ghanning/PolyLayout](https://github.com/ghanning/PolyLayout) | +2 | 129 |
| 273 | [timethrough/xiaohei-Chrome](https://github.com/timethrough/xiaohei-Chrome) | +2 | 148 |
| 274 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 275 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 859 |
| 276 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1278 |
| 277 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 323 |
| 278 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2871 |
| 279 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 233 |
| 280 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3117 |
| 281 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 262 |
| 282 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10366 |
| 283 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1189 |
| 284 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1379 |
| 285 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 504 |
| 286 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 102 |
| 287 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2517 |
| 288 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 289 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2693 |
| 290 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10475 |
| 291 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 292 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 66 |
| 293 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +1 | 509 |
| 294 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 885 |
| 295 | [The412Banner/bannerhub-revanced](https://github.com/The412Banner/bannerhub-revanced) | +1 | 149 |
| 296 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +1 | 925 |
| 297 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +1 | 313 |
| 298 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +1 | 3534 |
| 299 | [java-up-up/nexus-agent](https://github.com/java-up-up/nexus-agent) | +1 | 292 |
| 300 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +1 | 562 |
