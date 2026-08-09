---
title: "2026-08-09 GitHub增长趋势报告"
description: "1.prime-agent+8 2.reverse-skill+8 3.iFixAi+6 4.skills+4 5.openwiki+4"
date: 2026-08-09T20:33:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-09 20:33:49

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
        'daily': {"categories": ["TencentCloud/Octop", "GVCLab/PersonaLive", "diegosouzapw/OmniRoute", "wumingqi60/lingxi", "SangLuoCN/OneStep4", "bradautomates/claude-video", "ayghri/i-have-adhd", "vorssaint/vorssaint-utils", "pranshuparmar/witr", "alibaba/open-code-review", "emilkowalski/skills", "stablyai/orca", "AgentWrapper/agent-orchestrator", "baidu/Unlimited-OCR", "trycompai/crm", "langchain-ai/openwiki", "google/skills", "ifixai-ai/iFixAi", "zhaoxuya520/reverse-skill", "PrimeIntellect-ai/prime-agent"], "data": [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 6, 8, 8]},
        'weekly': {"categories": ["trycompai/crm", "herdrdev/herdr", "k1tbyte/Wand-Enhancer", "stablyai/orca", "firecrawl/pdf-inspector", "andrewyng/openworker", "google/skills", "emilkowalski/skills", "talivia-group/talivia", "ifixai-ai/iFixAi", "TencentCloud/TencentDB-Agent-Memory", "pranshuparmar/witr", "block/buzz", "brightdata/cli", "cloudflare/cloudflare-os", "zhaoxuya520/reverse-skill", "floci-io/floci", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [30, 32, 32, 33, 35, 37, 38, 38, 41, 43, 46, 48, 51, 54, 56, 57, 58, 61, 76, 216]},
        'monthly': {"categories": ["bradautomates/claude-video", "cloudflare/cloudflare-os", "zhaoxuya520/reverse-skill", "Fei-Away/Codex-Dream-Skin", "iOfficeAI/OfficeCLI", "usestrix/strix", "HKUDS/Vibe-Trading", "floci-io/floci", "ayghri/i-have-adhd", "k1tbyte/Wand-Enhancer", "andrewyng/openworker", "MadsLorentzen/ai-job-search", "herdrdev/herdr", "virgiliojr94/book-to-skill", "emilkowalski/skills", "JustVugg/colibri", "stablyai/orca", "block/buzz", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [55, 56, 64, 65, 65, 67, 69, 70, 76, 76, 80, 82, 84, 89, 94, 108, 115, 120, 151, 216]}
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
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +8 | 10786 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +8 | 22415 |
| 3 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 8034 |
| 4 | [google/skills](https://github.com/google/skills) | +4 | 17164 |
| 5 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +4 | 14782 |
| 6 | [trycompai/crm](https://github.com/trycompai/crm) | +3 | 7952 |
| 7 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +3 | 22980 |
| 8 | [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | +3 | 9081 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 40723 |
| 10 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3 | 27665 |
| 11 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +3 | 19799 |
| 12 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +3 | 20524 |
| 13 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +3 | 4893 |
| 14 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +3 | 18743 |
| 15 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +2 | 14739 |
| 16 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +2 | 271 |
| 17 | [wumingqi60/lingxi](https://github.com/wumingqi60/lingxi) | +2 | 697 |
| 18 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 44164 |
| 19 | [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) | +2 | 3503 |
| 20 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +2 | 998 |
| 21 | [yuhuangerdi/InduSecAgent](https://github.com/yuhuangerdi/InduSecAgent) | +2 | 645 |
| 22 | [rorkai/App-Store-Connect-CLI](https://github.com/rorkai/App-Store-Connect-CLI) | +2 | 5661 |
| 23 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +2 | 10877 |
| 24 | [browser-use/video-use](https://github.com/browser-use/video-use) | +2 | 20399 |
| 25 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +2 | 23590 |
| 26 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 13807 |
| 27 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +2 | 826 |
| 28 | [NO6KIKO/gorest-2d-animation-spritesheet-generator](https://github.com/NO6KIKO/gorest-2d-animation-spritesheet-generator) | +2 | 1337 |
| 29 | [floci-io/floci](https://github.com/floci-io/floci) | +2 | 19247 |
| 30 | [sqdshguy/wreq-js](https://github.com/sqdshguy/wreq-js) | +2 | 367 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +216 | 10787 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +76 | 44164 |
| 3 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +61 | 19373 |
| 4 | [floci-io/floci](https://github.com/floci-io/floci) | +58 | 19247 |
| 5 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +57 | 22415 |
| 6 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +56 | 7050 |
| 7 | [brightdata/cli](https://github.com/brightdata/cli) | +54 | 3310 |
| 8 | [block/buzz](https://github.com/block/buzz) | +51 | 25582 |
| 9 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +48 | 20525 |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +46 | 18703 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +43 | 8034 |
| 12 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1493 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +38 | 27665 |
| 14 | [google/skills](https://github.com/google/skills) | +38 | 17164 |
| 15 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +37 | 13942 |
| 16 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +35 | 13831 |
| 17 | [stablyai/orca](https://github.com/stablyai/orca) | +33 | 40723 |
| 18 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +32 | 16132 |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +32 | 26328 |
| 20 | [trycompai/crm](https://github.com/trycompai/crm) | +30 | 7952 |
| 21 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +27 | 33415 |
| 22 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +26 | 18743 |
| 23 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +26 | 10877 |
| 24 | [usestrix/strix](https://github.com/usestrix/strix) | +26 | 50282 |
| 25 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 798 |
| 26 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +24 | 61113 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +24 | 23273 |
| 28 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1528 |
| 29 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +23 | 2669 |
| 30 | [yc-software/qm](https://github.com/yc-software/qm) | +23 | 12746 |
| 31 | [malisper/pgrust](https://github.com/malisper/pgrust) | +22 | 4266 |
| 32 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +21 | 20904 |
| 33 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +21 | 3732 |
| 34 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +20 | 24176 |
| 35 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 768 |
| 36 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +19 | 14782 |
| 37 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +19 | 4312 |
| 38 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +18 | 30950 |
| 39 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +18 | 5016 |
| 40 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +18 | 8708 |
| 41 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +17 | 14739 |
| 42 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +17 | 27052 |
| 43 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 34490 |
| 44 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +17 | 29564 |
| 45 | [different-ai/openwork](https://github.com/different-ai/openwork) | +16 | 21700 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +16 | 19799 |
| 47 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +16 | 7883 |
| 48 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +16 | 44088 |
| 49 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2088 |
| 50 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +16 | 22980 |
| 51 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +16 | 34250 |
| 52 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 30450 |
| 53 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 20399 |
| 54 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +14 | 38282 |
| 55 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 5870 |
| 56 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +13 | 46380 |
| 57 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +13 | 7390 |
| 58 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +13 | 34250 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +12 | 17600 |
| 60 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +12 | 23477 |
| 61 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +12 | 540 |
| 62 | [ben-z/findphone](https://github.com/ben-z/findphone) | +12 | 1116 |
| 63 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +12 | 5551 |
| 64 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +11 | 4032 |
| 65 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +11 | 45040 |
| 66 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +11 | 826 |
| 67 | [sopaco/deepwiki-rs](https://github.com/sopaco/deepwiki-rs) | +11 | 1613 |
| 68 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +11 | 1030 |
| 69 | [Hidashimora/free-vpn-anti-rkn](https://github.com/Hidashimora/free-vpn-anti-rkn) | +11 | 373 |
| 70 | [HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio) | +11 | 654 |
| 71 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +11 | 2449 |
| 72 | [multica-ai/multica](https://github.com/multica-ai/multica) | +11 | 44913 |
| 73 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +10 | 612 |
| 74 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +10 | 40224 |
| 75 | [every-app/open-seo](https://github.com/every-app/open-seo) | +10 | 11087 |
| 76 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +10 | 46281 |
| 77 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +10 | 1944 |
| 78 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 33359 |
| 79 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +10 | 28395 |
| 80 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 913 |
| 81 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +10 | 43664 |
| 82 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +10 | 8431 |
| 83 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +10 | 4893 |
| 84 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +10 | 9524 |
| 85 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +10 | 8346 |
| 86 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +9 | 2046 |
| 87 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +9 | 4342 |
| 88 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +9 | 8611 |
| 89 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +9 | 796 |
| 90 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +9 | 2716 |
| 91 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +9 | 2571 |
| 92 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2283 |
| 93 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +9 | 2040 |
| 94 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 886 |
| 95 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +9 | 5099 |
| 96 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +9 | 3848 |
| 97 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +8 | 229 |
| 98 | [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | +8 | 2330 |
| 99 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +8 | 13807 |
| 100 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 333 |
| 101 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1441 |
| 102 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 2090 |
| 103 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +7 | 2428 |
| 104 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +7 | 8390 |
| 105 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +7 | 9780 |
| 106 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +7 | 19397 |
| 107 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +7 | 941 |
| 108 | [CopilotKit/OpenTag](https://github.com/CopilotKit/OpenTag) | +6 | 1021 |
| 109 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 4608 |
| 110 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +6 | 5836 |
| 111 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 430 |
| 112 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +6 | 41487 |
| 113 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +6 | 3114 |
| 114 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1317 |
| 115 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +6 | 5289 |
| 116 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +5 | 993 |
| 117 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1387 |
| 118 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 29791 |
| 119 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +5 | 998 |
| 120 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +5 | 589 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +216 | 10788 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +151 | 44164 |
| 3 | [block/buzz](https://github.com/block/buzz) | +120 | 25582 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +115 | 40723 |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +108 | 23477 |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +94 | 27665 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +89 | 19373 |
| 8 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +84 | 26328 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +82 | 30950 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +80 | 13942 |
| 11 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +76 | 16132 |
| 12 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +76 | 18743 |
| 13 | [floci-io/floci](https://github.com/floci-io/floci) | +70 | 19247 |
| 14 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +69 | 30450 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +67 | 50282 |
| 16 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +65 | 27052 |
| 17 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +65 | 13461 |
| 18 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +64 | 22415 |
| 19 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +56 | 7050 |
| 20 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +55 | 14739 |
| 21 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10486 |
| 22 | [brightdata/cli](https://github.com/brightdata/cli) | +54 | 3310 |
| 23 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +51 | 8034 |
| 24 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +50 | 20525 |
| 25 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +50 | 18704 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +50 | 10877 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +50 | 22980 |
| 28 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 34250 |
| 29 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +48 | 13831 |
| 30 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46380 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +44 | 44088 |
| 32 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +43 | 33415 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +43 | 8708 |
| 34 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +43 | 38282 |
| 35 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1493 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 23273 |
| 37 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +42 | 29564 |
| 38 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +42 | 46281 |
| 39 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +42 | 49882 |
| 40 | [google/skills](https://github.com/google/skills) | +41 | 17164 |
| 41 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +41 | 14782 |
| 42 | [goauthentik/authentik](https://github.com/goauthentik/authentik) | +40 | 24220 |
| 43 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 61113 |
| 44 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8283 |
| 45 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +38 | 40224 |
| 46 | [malisper/pgrust](https://github.com/malisper/pgrust) | +38 | 4266 |
| 47 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +38 | 33359 |
| 48 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +37 | 10335 |
| 49 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +35 | 16606 |
| 50 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +35 | 7851 |
| 51 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +35 | 19255 |
| 52 | [yc-software/qm](https://github.com/yc-software/qm) | +34 | 12746 |
| 53 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +34 | 19799 |
| 54 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +33 | 8390 |
| 55 | [trycompai/crm](https://github.com/trycompai/crm) | +33 | 7952 |
| 56 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +33 | 4312 |
| 57 | [openai/codex-security](https://github.com/openai/codex-security) | +32 | 9398 |
| 58 | [blader/humanizer](https://github.com/blader/humanizer) | +31 | 34490 |
| 59 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +31 | 43664 |
| 60 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +31 | 9979 |
| 61 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +30 | 45040 |
| 62 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 44913 |
| 63 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +30 | 34250 |
| 64 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +30 | 9411 |
| 65 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +29 | 7390 |
| 66 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5099 |
| 67 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7773 |
| 68 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8576 |
| 69 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +26 | 5016 |
| 70 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 20905 |
| 71 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +26 | 28395 |
| 72 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +26 | 4443 |
| 73 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24176 |
| 74 | [different-ai/openwork](https://github.com/different-ai/openwork) | +25 | 21700 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 798 |
| 76 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 31455 |
| 77 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9524 |
| 78 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1528 |
| 79 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +23 | 2669 |
| 80 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20399 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3848 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36395 |
| 83 | [marcelroed/gigatoken](https://github.com/marcelroed/gigatoken) | +23 | 3947 |
| 84 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +22 | 8611 |
| 85 | [every-app/open-seo](https://github.com/every-app/open-seo) | +22 | 11087 |
| 86 | [t8y2/dbx](https://github.com/t8y2/dbx) | +22 | 13773 |
| 87 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +21 | 17600 |
| 88 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +21 | 3732 |
| 89 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +21 | 2716 |
| 90 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 13807 |
| 91 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +21 | 5505 |
| 92 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 768 |
| 93 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8346 |
| 94 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +19 | 5551 |
| 95 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +19 | 7883 |
| 96 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 41487 |
| 97 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +18 | 4608 |
| 98 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13147 |
| 99 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +17 | 15805 |
| 100 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11145 |
| 101 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2088 |
| 102 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8431 |
| 103 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 6743 |
| 104 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +16 | 15300 |
| 105 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +16 | 31596 |
| 106 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +16 | 4910 |
| 107 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16354 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +15 | 35134 |
| 109 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 2571 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 5870 |
| 111 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +13 | 9780 |
| 112 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29791 |
| 113 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25060 |
| 114 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 27185 |
| 115 | [penecho/penecho](https://github.com/penecho/penecho) | +13 | 1984 |
| 116 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4032 |
| 117 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +12 | 2046 |
| 118 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +12 | 540 |
| 119 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +12 | 19397 |
| 120 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46795 |
| 121 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2283 |
| 122 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +11 | 2449 |
| 123 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +11 | 44694 |
| 124 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +11 | 2153 |
| 125 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +11 | 30122 |
| 126 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46812 |
| 127 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 33056 |
| 128 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3542 |
| 129 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4861 |
| 130 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +10 | 4342 |
| 131 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +10 | 612 |
| 132 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 913 |
| 133 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5836 |
| 134 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +10 | 14417 |
| 135 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10283 |
| 136 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +10 | 5289 |
| 137 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +10 | 28121 |
| 138 | [anbeime/skill](https://github.com/anbeime/skill) | +10 | 5001 |
| 139 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1544 |
| 140 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 10070 |
| 141 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1841 |
| 142 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 2428 |
| 143 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1698 |
| 144 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 886 |
| 145 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1214 |
| 146 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +9 | 2703 |
| 147 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +9 | 1290 |
| 148 | [petergyang/human-review](https://github.com/petergyang/human-review) | +9 | 646 |
| 149 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1625 |
| 150 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +9 | 1774 |
| 151 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 7962 |
| 152 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +9 | 9801 |
| 153 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2132 |
| 154 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +8 | 229 |
| 155 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 333 |
| 156 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1441 |
| 157 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6688 |
| 158 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 2090 |
| 159 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +8 | 3114 |
| 160 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +8 | 788 |
| 161 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8475 |
| 162 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +8 | 998 |
| 163 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +8 | 1842 |
| 164 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +8 | 1634 |
| 165 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9797 |
| 166 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19422 |
| 167 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +8 | 5051 |
| 168 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 4076 |
| 169 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +8 | 15729 |
| 170 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +8 | 5052 |
| 171 | [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide) | +8 | 2093 |
| 172 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +8 | 9937 |
| 173 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1073 |
| 174 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6135 |
| 175 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24062 |
| 176 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +7 | 941 |
| 177 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 5990 |
| 178 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +7 | 1923 |
| 179 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +7 | 6596 |
| 180 | [openai/skills](https://github.com/openai/skills) | +7 | 24668 |
| 181 | [openai/plugins](https://github.com/openai/plugins) | +7 | 5013 |
| 182 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29900 |
| 183 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +6 | 10496 |
| 184 | [open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) | +6 | 1116 |
| 185 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 430 |
| 186 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1317 |
| 187 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +6 | 2504 |
| 188 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +6 | 17154 |
| 189 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +6 | 8156 |
| 190 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 993 |
| 191 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 255 |
| 192 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +6 | 1136 |
| 193 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 401 |
| 194 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27246 |
| 195 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5576 |
| 196 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14571 |
| 197 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 27974 |
| 198 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 518 |
| 199 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +6 | 2943 |
| 200 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +6 | 0 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5848 |
| 202 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1387 |
| 203 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +5 | 9357 |
| 204 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2876 |
| 205 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1194 |
| 206 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7059 |
| 207 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1300 |
| 208 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3331 |
| 209 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8455 |
| 210 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +5 | 3252 |
| 211 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 685 |
| 212 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +5 | 2667 |
| 213 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +5 | 753 |
| 214 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1224 |
| 215 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +5 | 1994 |
| 216 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 862 |
| 217 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5290 |
| 218 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +4 | 325 |
| 219 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11201 |
| 220 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +4 | 398 |
| 221 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5140 |
| 222 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9471 |
| 223 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +4 | 18831 |
| 224 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1250 |
| 225 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 403 |
| 226 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5880 |
| 227 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +4 | 5439 |
| 228 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 396 |
| 229 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 91 |
| 230 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3167 |
| 231 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 802 |
| 232 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28301 |
| 233 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4624 |
| 234 | [SulgX/SulgX-Panel](https://github.com/SulgX/SulgX-Panel) | +3 | 405 |
| 235 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +3 | 4947 |
| 236 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1781 |
| 237 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 923 |
| 238 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 447 |
| 239 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3303 |
| 240 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 699 |
| 241 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 440 |
| 242 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 601 |
| 243 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +3 | 726 |
| 244 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 402 |
| 245 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 144 |
| 246 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 338 |
| 247 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 824 |
| 248 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 271 |
| 249 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1982 |
| 250 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4967 |
| 251 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 3087 |
| 252 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9241 |
| 253 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 886 |
| 254 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 315 |
| 255 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 488 |
| 256 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +2 | 667 |
| 257 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1255 |
| 258 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +2 | 182 |
| 259 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12235 |
| 260 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +2 | 1101 |
| 261 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 36 |
| 262 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2802 |
| 263 | [future-agi/future-agi](https://github.com/future-agi/future-agi) | +2 | 1634 |
| 264 | [hwttop5/tabbit2api](https://github.com/hwttop5/tabbit2api) | +2 | 84 |
| 265 | [ghanning/PolyLayout](https://github.com/ghanning/PolyLayout) | +2 | 81 |
| 266 | [timethrough/xiaohei-Chrome](https://github.com/timethrough/xiaohei-Chrome) | +2 | 145 |
| 267 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +2 | 206 |
| 268 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 454 |
| 269 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +2 | 5233 |
| 270 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +2 | 741 |
| 271 | [twalichiewicz/Backchannel](https://github.com/twalichiewicz/Backchannel) | +2 | 243 |
| 272 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 273 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 852 |
| 274 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1269 |
| 275 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2857 |
| 276 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +2 | 1132 |
| 277 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 216 |
| 278 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 255 |
| 279 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10365 |
| 280 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1376 |
| 281 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 497 |
| 282 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 98 |
| 283 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2486 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 285 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2690 |
| 286 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10456 |
| 287 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 288 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 50 |
| 289 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +1 | 509 |
| 290 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1037 |
| 291 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +1 | 5976 |
| 292 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +1 | 1039 |
| 293 | [The412Banner/bannerhub-revanced](https://github.com/The412Banner/bannerhub-revanced) | +1 | 149 |
| 294 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +1 | 3528 |
| 295 | [java-up-up/nexus-agent](https://github.com/java-up-up/nexus-agent) | +1 | 289 |
| 296 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +1 | 565 |
| 297 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +1 | 189 |
| 298 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +1 | 406 |
| 299 | [kokodio/metallum](https://github.com/kokodio/metallum) | +1 | 46 |
| 300 | [jasonwu1994/Gboard-patches](https://github.com/jasonwu1994/Gboard-patches) | +1 | 228 |
