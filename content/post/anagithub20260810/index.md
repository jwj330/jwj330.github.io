---
title: "2026-08-10 GitHub增长趋势报告"
description: "1.prime-agent+8 2.reverse-skill+6 3.orca+4 4.corsair+3 5.witr+3"
date: 2026-08-10T20:43:22+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-10 20:43:22

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
        'daily': {"categories": ["google/skills", "baidu/Unlimited-OCR", "herdrdev/herdr", "heygen-com/hyperframes", "diegosouzapw/OmniRoute", "VoltAgent/awesome-agent-skills", "block/buzz", "MiniMax-AI/MiniMax-H3", "yynxxxxx/Codex-X", "sozercan/kaset", "ayghri/i-have-adhd", "brightdata/cli", "pctrade/end4-pC", "MengTo/kage", "op7418/guizang-ppt-skill", "pranshuparmar/witr", "corsairdev/corsair", "stablyai/orca", "zhaoxuya520/reverse-skill", "PrimeIntellect-ai/prime-agent"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 6, 8]},
        'weekly': {"categories": ["ayghri/i-have-adhd", "k1tbyte/Wand-Enhancer", "firecrawl/pdf-inspector", "herdrdev/herdr", "andrewyng/openworker", "stablyai/orca", "google/skills", "emilkowalski/skills", "talivia-group/talivia", "ifixai-ai/iFixAi", "TencentCloud/TencentDB-Agent-Memory", "pranshuparmar/witr", "block/buzz", "cloudflare/cloudflare-os", "brightdata/cli", "zhaoxuya520/reverse-skill", "floci-io/floci", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [29, 29, 32, 34, 35, 36, 40, 40, 41, 44, 44, 51, 51, 56, 57, 57, 58, 61, 76, 224]},
        'monthly': {"categories": ["cloudflare/cloudflare-os", "brightdata/cli", "iOfficeAI/OfficeCLI", "Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "floci-io/floci", "zhaoxuya520/reverse-skill", "k1tbyte/Wand-Enhancer", "MadsLorentzen/ai-job-search", "ayghri/i-have-adhd", "andrewyng/openworker", "herdrdev/herdr", "virgiliojr94/book-to-skill", "emilkowalski/skills", "JustVugg/colibri", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [56, 57, 61, 66, 69, 70, 70, 72, 73, 79, 80, 84, 90, 94, 102, 116, 122, 135, 153, 224]}
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
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +8 | 12900 |
| 2 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +6 | 23278 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 41666 |
| 4 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +3 | 8206 |
| 5 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +3 | 21197 |
| 6 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +3 | 23676 |
| 7 | [MengTo/kage](https://github.com/MengTo/kage) | +3 | 762 |
| 8 | [pctrade/end4-pC](https://github.com/pctrade/end4-pC) | +3 | 1235 |
| 9 | [brightdata/cli](https://github.com/brightdata/cli) | +3 | 3700 |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +3 | 19092 |
| 11 | [sozercan/kaset](https://github.com/sozercan/kaset) | +3 | 1904 |
| 12 | [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) | +2 | 2341 |
| 13 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +2 | 4111 |
| 14 | [block/buzz](https://github.com/block/buzz) | +2 | 26043 |
| 15 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +2 | 29947 |
| 16 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2 | 45084 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 40405 |
| 18 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +2 | 26972 |
| 19 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +2 | 23334 |
| 20 | [google/skills](https://github.com/google/skills) | +2 | 17577 |
| 21 | [valqore/valqore](https://github.com/valqore/valqore) | +2 | 1511 |
| 22 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +2 | 10704 |
| 23 | [every-app/open-seo](https://github.com/every-app/open-seo) | +2 | 11224 |
| 24 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2 | 28032 |
| 25 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2 | 9817 |
| 26 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +1 | 357 |
| 27 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +1 | 27424 |
| 28 | [zachlatta/freeflow](https://github.com/zachlatta/freeflow) | +1 | 2447 |
| 29 | [free-nodes/shadowrocket](https://github.com/free-nodes/shadowrocket) | +1 | 175 |
| 30 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +1 | 13512 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +224 | 12900 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +76 | 45084 |
| 3 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +61 | 19945 |
| 4 | [floci-io/floci](https://github.com/floci-io/floci) | +58 | 19426 |
| 5 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +57 | 23278 |
| 6 | [brightdata/cli](https://github.com/brightdata/cli) | +57 | 3700 |
| 7 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +56 | 7415 |
| 8 | [block/buzz](https://github.com/block/buzz) | +51 | 26043 |
| 9 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +51 | 21197 |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +44 | 19350 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +44 | 8277 |
| 12 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1529 |
| 13 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +40 | 28032 |
| 14 | [google/skills](https://github.com/google/skills) | +40 | 17577 |
| 15 | [stablyai/orca](https://github.com/stablyai/orca) | +36 | 41666 |
| 16 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +35 | 14076 |
| 17 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +34 | 26972 |
| 18 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +32 | 14332 |
| 19 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +29 | 16402 |
| 20 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +29 | 19092 |
| 21 | [trycompai/crm](https://github.com/trycompai/crm) | +27 | 8096 |
| 22 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +27 | 35667 |
| 23 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +27 | 33693 |
| 24 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +26 | 11165 |
| 25 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +25 | 61723 |
| 26 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +25 | 4111 |
| 27 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 845 |
| 28 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1581 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +22 | 23583 |
| 30 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +22 | 21143 |
| 31 | [malisper/pgrust](https://github.com/malisper/pgrust) | +22 | 4302 |
| 32 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +20 | 14836 |
| 33 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +20 | 3929 |
| 34 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 852 |
| 35 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 31101 |
| 36 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +19 | 24240 |
| 37 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +19 | 4493 |
| 38 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +19 | 5304 |
| 39 | [yc-software/qm](https://github.com/yc-software/qm) | +18 | 12943 |
| 40 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +18 | 8918 |
| 41 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +17 | 27424 |
| 42 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +17 | 14912 |
| 43 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +17 | 19926 |
| 44 | [blader/humanizer](https://github.com/blader/humanizer) | +17 | 34706 |
| 45 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +16 | 8135 |
| 46 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +16 | 44407 |
| 47 | [different-ai/openwork](https://github.com/different-ai/openwork) | +15 | 21783 |
| 48 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 30536 |
| 49 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +15 | 23334 |
| 50 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +15 | 29694 |
| 51 | [browser-use/video-use](https://github.com/browser-use/video-use) | +15 | 20472 |
| 52 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +14 | 38405 |
| 53 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +14 | 34439 |
| 54 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 5890 |
| 55 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 56 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +13 | 2155 |
| 57 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +13 | 7587 |
| 58 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +13 | 33997 |
| 59 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +12 | 46467 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +12 | 17978 |
| 61 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +12 | 40405 |
| 62 | [every-app/open-seo](https://github.com/every-app/open-seo) | +12 | 11224 |
| 63 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +12 | 23678 |
| 64 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +12 | 8206 |
| 65 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +12 | 28487 |
| 66 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +12 | 1037 |
| 67 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +12 | 584 |
| 68 | [ben-z/findphone](https://github.com/ben-z/findphone) | +12 | 1204 |
| 69 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +12 | 5704 |
| 70 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +11 | 4026 |
| 71 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +11 | 683 |
| 72 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +11 | 45159 |
| 73 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +11 | 2238 |
| 74 | [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) | +11 | 889 |
| 75 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +11 | 4968 |
| 76 | [Hidashimora/free-vpn-anti-rkn](https://github.com/Hidashimora/free-vpn-anti-rkn) | +11 | 383 |
| 77 | [HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio) | +11 | 737 |
| 78 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +11 | 2609 |
| 79 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 2826 |
| 80 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +10 | 2634 |
| 81 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 33831 |
| 82 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1015 |
| 83 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +10 | 43800 |
| 84 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +10 | 8490 |
| 85 | [sopaco/deepwiki-rs](https://github.com/sopaco/deepwiki-rs) | +10 | 1658 |
| 86 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +10 | 8404 |
| 87 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +9 | 2071 |
| 88 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +9 | 4363 |
| 89 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +9 | 8723 |
| 90 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +9 | 822 |
| 91 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +9 | 46690 |
| 92 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +9 | 13885 |
| 93 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +9 | 2317 |
| 94 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +9 | 9817 |
| 95 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +9 | 2103 |
| 96 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 910 |
| 97 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +8 | 308 |
| 98 | [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | +8 | 2467 |
| 99 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 334 |
| 100 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1461 |
| 101 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +8 | 5221 |
| 102 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +8 | 1001 |
| 103 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 2264 |
| 104 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +8 | 3903 |
| 105 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +7 | 0 |
| 106 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +7 | 4716 |
| 107 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +7 | 19486 |
| 108 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +6 | 0 |
| 109 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +6 | 5858 |
| 110 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +6 | 1055 |
| 111 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 453 |
| 112 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1337 |
| 113 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +5 | 0 |
| 114 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1417 |
| 115 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +5 | 1729 |
| 116 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +5 | 10704 |
| 117 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +5 | 29852 |
| 118 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +5 | 703 |
| 119 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +5 | 41720 |
| 120 | [thecmdguy/Ducky](https://github.com/thecmdguy/Ducky) | +5 | 887 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +224 | 12900 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +153 | 45084 |
| 3 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +135 | 35667 |
| 4 | [block/buzz](https://github.com/block/buzz) | +122 | 26044 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +116 | 41666 |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +102 | 23678 |
| 7 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +94 | 28032 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +90 | 19945 |
| 9 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +84 | 26972 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +80 | 14076 |
| 11 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +79 | 19093 |
| 12 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +73 | 31101 |
| 13 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +72 | 16402 |
| 14 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +70 | 23278 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +70 | 19426 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +69 | 30536 |
| 17 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +66 | 13512 |
| 18 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +61 | 27424 |
| 19 | [brightdata/cli](https://github.com/brightdata/cli) | +57 | 3700 |
| 20 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +56 | 7415 |
| 21 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10522 |
| 22 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +53 | 21197 |
| 23 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +52 | 8277 |
| 24 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +51 | 19350 |
| 25 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +51 | 14912 |
| 26 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +51 | 23334 |
| 27 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +50 | 11165 |
| 28 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 33997 |
| 29 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +48 | 14332 |
| 30 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46467 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +44 | 44407 |
| 32 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +43 | 8918 |
| 33 | [google/skills](https://github.com/google/skills) | +42 | 17577 |
| 34 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1529 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 23583 |
| 36 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 33693 |
| 37 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +42 | 29694 |
| 38 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +42 | 38405 |
| 39 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +41 | 46690 |
| 40 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +41 | 49989 |
| 41 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +40 | 61723 |
| 42 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +40 | 14836 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +39 | 40405 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +39 | 33831 |
| 45 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8329 |
| 46 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +37 | 10538 |
| 47 | [malisper/pgrust](https://github.com/malisper/pgrust) | +36 | 4302 |
| 48 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +36 | 19350 |
| 49 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +35 | 19926 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +35 | 16816 |
| 51 | [yc-software/qm](https://github.com/yc-software/qm) | +34 | 12943 |
| 52 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +34 | 7902 |
| 53 | [trycompai/crm](https://github.com/trycompai/crm) | +33 | 8096 |
| 54 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +33 | 4493 |
| 55 | [openai/codex-security](https://github.com/openai/codex-security) | +32 | 9508 |
| 56 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +31 | 0 |
| 57 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +31 | 10407 |
| 58 | [blader/humanizer](https://github.com/blader/humanizer) | +30 | 34706 |
| 59 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 43800 |
| 60 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +30 | 45159 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 45123 |
| 62 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +30 | 9517 |
| 63 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +29 | 34439 |
| 64 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +29 | 7587 |
| 65 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +28 | 28487 |
| 66 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5221 |
| 67 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +27 | 5304 |
| 68 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +27 | 21143 |
| 69 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7796 |
| 70 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8575 |
| 71 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +26 | 4474 |
| 72 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24240 |
| 73 | [different-ai/openwork](https://github.com/different-ai/openwork) | +25 | 21783 |
| 74 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +25 | 4111 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 845 |
| 76 | [every-app/open-seo](https://github.com/every-app/open-seo) | +24 | 11224 |
| 77 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +24 | 31606 |
| 78 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9605 |
| 79 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1581 |
| 80 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 20472 |
| 81 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3903 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 36531 |
| 83 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +22 | 3929 |
| 84 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +22 | 2826 |
| 85 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +21 | 17978 |
| 86 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +21 | 8723 |
| 87 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 13885 |
| 88 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +21 | 8206 |
| 89 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 852 |
| 90 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8404 |
| 91 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +20 | 5551 |
| 92 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +19 | 5704 |
| 93 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 4716 |
| 94 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +19 | 8135 |
| 95 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +19 | 41720 |
| 96 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13224 |
| 97 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11153 |
| 98 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2155 |
| 99 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8490 |
| 100 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 6976 |
| 101 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +16 | 15855 |
| 102 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +15 | 2634 |
| 103 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15 | 9817 |
| 104 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16376 |
| 105 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +15 | 31652 |
| 106 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +15 | 4958 |
| 107 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +14 | 15358 |
| 108 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +14 | 35190 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +13 | 5890 |
| 110 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29852 |
| 111 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 112 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25131 |
| 113 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 27248 |
| 114 | [penecho/penecho](https://github.com/penecho/penecho) | +13 | 1997 |
| 115 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4026 |
| 116 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +12 | 2071 |
| 117 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +12 | 584 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +12 | 19486 |
| 119 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46827 |
| 120 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 2161 |
| 121 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +11 | 683 |
| 122 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +11 | 2317 |
| 123 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +11 | 2609 |
| 124 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +11 | 44733 |
| 125 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46859 |
| 126 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 33145 |
| 127 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3575 |
| 128 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4871 |
| 129 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +10 | 4363 |
| 130 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +10 | 1015 |
| 131 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +10 | 1729 |
| 132 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5858 |
| 133 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10339 |
| 134 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +10 | 5332 |
| 135 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +10 | 28167 |
| 136 | [anbeime/skill](https://github.com/anbeime/skill) | +10 | 5048 |
| 137 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1559 |
| 138 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 10126 |
| 139 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1851 |
| 140 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 141 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 910 |
| 142 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +9 | 14473 |
| 143 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1055 |
| 144 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1233 |
| 145 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 10704 |
| 146 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +9 | 30226 |
| 147 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +9 | 5086 |
| 148 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +9 | 5064 |
| 149 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +9 | 1471 |
| 150 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +9 | 10031 |
| 151 | [petergyang/human-review](https://github.com/petergyang/human-review) | +9 | 694 |
| 152 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1656 |
| 153 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +9 | 1790 |
| 154 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8011 |
| 155 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +9 | 9824 |
| 156 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2139 |
| 157 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +8 | 308 |
| 158 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 334 |
| 159 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1461 |
| 160 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +8 | 828 |
| 161 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +8 | 1001 |
| 162 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 2264 |
| 163 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +8 | 3173 |
| 164 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8505 |
| 165 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +8 | 1892 |
| 166 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9811 |
| 167 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19479 |
| 168 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 4092 |
| 169 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +8 | 2724 |
| 170 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +8 | 15753 |
| 171 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +8 | 5934 |
| 172 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1086 |
| 173 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6208 |
| 174 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6695 |
| 175 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24094 |
| 176 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6017 |
| 177 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1647 |
| 178 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +7 | 1936 |
| 179 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +7 | 6533 |
| 180 | [openai/skills](https://github.com/openai/skills) | +7 | 24741 |
| 181 | [openai/plugins](https://github.com/openai/plugins) | +7 | 5032 |
| 182 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29928 |
| 183 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +6 | 10525 |
| 184 | [open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) | +6 | 1137 |
| 185 | [xmarre/ComfyUI-Spectrum-MiniMax-H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | +6 | 453 |
| 186 | [uber/ADR](https://github.com/uber/ADR) | +6 | 1337 |
| 187 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +6 | 2516 |
| 188 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +6 | 8247 |
| 189 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 190 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 260 |
| 191 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +6 | 1242 |
| 192 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 422 |
| 193 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27271 |
| 194 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5595 |
| 195 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14583 |
| 196 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 28025 |
| 197 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 520 |
| 198 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +6 | 2956 |
| 199 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +6 | 0 |
| 200 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 563 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5809 |
| 202 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1417 |
| 203 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +5 | 9381 |
| 204 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2903 |
| 205 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1204 |
| 206 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7067 |
| 207 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1311 |
| 208 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 2977 |
| 209 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8484 |
| 210 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 686 |
| 211 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +5 | 2692 |
| 212 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +5 | 760 |
| 213 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1220 |
| 214 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +4 | 357 |
| 215 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5349 |
| 216 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +4 | 348 |
| 217 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11242 |
| 218 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +4 | 425 |
| 219 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5155 |
| 220 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3269 |
| 221 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9493 |
| 222 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1271 |
| 223 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 407 |
| 224 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5895 |
| 225 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +4 | 5458 |
| 226 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 93 |
| 227 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 840 |
| 228 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3184 |
| 229 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 811 |
| 230 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4640 |
| 231 | [SulgX/SulgX-Panel](https://github.com/SulgX/SulgX-Panel) | +3 | 276 |
| 232 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +3 | 4874 |
| 233 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1786 |
| 234 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 892 |
| 235 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 462 |
| 236 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18849 |
| 237 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3363 |
| 238 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 717 |
| 239 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 442 |
| 240 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 241 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +3 | 681 |
| 242 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 404 |
| 243 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 144 |
| 244 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 338 |
| 245 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 842 |
| 246 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 278 |
| 247 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1137 |
| 248 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1984 |
| 249 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4985 |
| 250 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9203 |
| 251 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28323 |
| 252 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 887 |
| 253 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 320 |
| 254 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 493 |
| 255 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +2 | 673 |
| 256 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1263 |
| 257 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12247 |
| 258 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +2 | 1112 |
| 259 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 36 |
| 260 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2822 |
| 261 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +2 | 184 |
| 262 | [future-agi/future-agi](https://github.com/future-agi/future-agi) | +2 | 1639 |
| 263 | [hwttop5/tabbit2api](https://github.com/hwttop5/tabbit2api) | +2 | 84 |
| 264 | [ghanning/PolyLayout](https://github.com/ghanning/PolyLayout) | +2 | 115 |
| 265 | [timethrough/xiaohei-Chrome](https://github.com/timethrough/xiaohei-Chrome) | +2 | 145 |
| 266 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +2 | 207 |
| 267 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 461 |
| 268 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +2 | 783 |
| 269 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +2 | 5245 |
| 270 | [twalichiewicz/Backchannel](https://github.com/twalichiewicz/Backchannel) | +2 | 247 |
| 271 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 272 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 857 |
| 273 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1275 |
| 274 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2861 |
| 275 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 225 |
| 276 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3102 |
| 277 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 259 |
| 278 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10368 |
| 279 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1187 |
| 280 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1379 |
| 281 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 501 |
| 282 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 100 |
| 283 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2497 |
| 284 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 285 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2691 |
| 286 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +2 | 10469 |
| 287 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 288 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 59 |
| 289 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +1 | 509 |
| 290 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1038 |
| 291 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +1 | 5978 |
| 292 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +1 | 1041 |
| 293 | [The412Banner/bannerhub-revanced](https://github.com/The412Banner/bannerhub-revanced) | +1 | 149 |
| 294 | [oxylabs/google-ai-mode-scraper](https://github.com/oxylabs/google-ai-mode-scraper) | +1 | 3534 |
| 295 | [java-up-up/nexus-agent](https://github.com/java-up-up/nexus-agent) | +1 | 290 |
| 296 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +1 | 551 |
| 297 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +1 | 191 |
| 298 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +1 | 409 |
| 299 | [kokodio/metallum](https://github.com/kokodio/metallum) | +1 | 47 |
| 300 | [jasonwu1994/Gboard-patches](https://github.com/jasonwu1994/Gboard-patches) | +1 | 241 |
