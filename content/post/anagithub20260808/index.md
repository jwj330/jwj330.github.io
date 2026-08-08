---
title: "2026-08-08 GitHub增长趋势报告"
description: "1.prime-agent+195 2.OmniRoute+61 3.floci+55 4.book-to-skill+52 5.cli+50"
date: 2026-08-08T20:31:25+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-08 20:31:25

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
        'daily': {"categories": ["h4ckf0r0day/obscura", "ZhuLinsen/daily_stock_analysis", "stablyai/orca", "emiliaprotocol/emilia-protocol", "herdrdev/herdr", "k1tbyte/Wand-Enhancer", "zhaoxuya520/reverse-skill", "TencentCloud/TencentDB-Agent-Memory", "ifixai-ai/iFixAi", "emilkowalski/skills", "andrewyng/openworker", "google/skills", "talivia-group/talivia", "pranshuparmar/witr", "block/buzz", "brightdata/cli", "virgiliojr94/book-to-skill", "floci-io/floci", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [21, 23, 23, 24, 24, 26, 28, 29, 29, 30, 31, 33, 40, 42, 46, 50, 52, 55, 61, 195]},
        'weekly': {"categories": ["esengine/DeepSeek-Reasonix", "trycompai/crm", "stablyai/orca", "herdrdev/herdr", "k1tbyte/Wand-Enhancer", "google/skills", "andrewyng/openworker", "ifixai-ai/iFixAi", "emilkowalski/skills", "talivia-group/talivia", "TencentCloud/TencentDB-Agent-Memory", "firecrawl/pdf-inspector", "pranshuparmar/witr", "zhaoxuya520/reverse-skill", "brightdata/cli", "block/buzz", "floci-io/floci", "virgiliojr94/book-to-skill", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [29, 30, 31, 31, 34, 35, 38, 39, 39, 41, 44, 45, 46, 52, 55, 55, 56, 61, 75, 209]},
        'monthly': {"categories": ["brightdata/cli", "zhaoxuya520/reverse-skill", "bradautomates/claude-video", "Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "floci-io/floci", "usestrix/strix", "ayghri/i-have-adhd", "iOfficeAI/OfficeCLI", "k1tbyte/Wand-Enhancer", "andrewyng/openworker", "virgiliojr94/book-to-skill", "herdrdev/herdr", "MadsLorentzen/ai-job-search", "emilkowalski/skills", "JustVugg/colibri", "stablyai/orca", "block/buzz", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [55, 57, 59, 65, 68, 68, 69, 72, 73, 76, 79, 88, 89, 89, 92, 107, 115, 120, 150, 209]}
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
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +195 | 8577 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +61 | 43359 |
| 3 | [floci-io/floci](https://github.com/floci-io/floci) | +55 | 18999 |
| 4 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +52 | 18838 |
| 5 | [brightdata/cli](https://github.com/brightdata/cli) | +50 | 2487 |
| 6 | [block/buzz](https://github.com/block/buzz) | +46 | 25285 |
| 7 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +42 | 20101 |
| 8 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +40 | 1333 |
| 9 | [google/skills](https://github.com/google/skills) | +33 | 16647 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +31 | 13790 |
| 11 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +30 | 27221 |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +29 | 7363 |
| 13 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +29 | 18159 |
| 14 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +28 | 21118 |
| 15 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +26 | 15776 |
| 16 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +24 | 25922 |
| 17 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +24 | 726 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +23 | 40156 |
| 19 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +23 | 60743 |
| 20 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +21 | 20747 |
| 21 | [malisper/pgrust](https://github.com/malisper/pgrust) | +20 | 4216 |
| 22 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 676 |
| 23 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +19 | 4192 |
| 24 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +19 | 10575 |
| 25 | [ymichael/bb](https://github.com/ymichael/bb) | +19 | 1468 |
| 26 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +18 | 13447 |
| 27 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +18 | 18481 |
| 28 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +18 | 24128 |
| 29 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +18 | 33124 |
| 30 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +17 | 22994 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +209 | 8577 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +75 | 43359 |
| 3 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +61 | 18838 |
| 4 | [floci-io/floci](https://github.com/floci-io/floci) | +56 | 18999 |
| 5 | [block/buzz](https://github.com/block/buzz) | +55 | 25285 |
| 6 | [brightdata/cli](https://github.com/brightdata/cli) | +55 | 2487 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +52 | 21118 |
| 8 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +46 | 20101 |
| 9 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +45 | 13447 |
| 10 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +44 | 18159 |
| 11 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +41 | 1333 |
| 12 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +39 | 27221 |
| 13 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +39 | 7363 |
| 14 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +38 | 13790 |
| 15 | [google/skills](https://github.com/google/skills) | +35 | 16647 |
| 16 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +34 | 15776 |
| 17 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +31 | 25922 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +31 | 40156 |
| 19 | [trycompai/crm](https://github.com/trycompai/crm) | +30 | 7735 |
| 20 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +29 | 33124 |
| 21 | [yc-software/qm](https://github.com/yc-software/qm) | +29 | 12513 |
| 22 | [usestrix/strix](https://github.com/usestrix/strix) | +27 | 49947 |
| 23 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +25 | 60743 |
| 24 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +24 | 18481 |
| 25 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +24 | 726 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +24 | 10575 |
| 27 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +23 | 22995 |
| 28 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1468 |
| 29 | [malisper/pgrust](https://github.com/malisper/pgrust) | +22 | 4216 |
| 30 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +22 | 20747 |
| 31 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +20 | 24128 |
| 32 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 676 |
| 33 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +20 | 8569 |
| 34 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 30809 |
| 35 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +19 | 4192 |
| 36 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +19 | 3573 |
| 37 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +19 | 26793 |
| 38 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +17 | 29449 |
| 39 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +16 | 14702 |
| 40 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +16 | 7804 |
| 41 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +16 | 4712 |
| 42 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2025 |
| 43 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +16 | 43941 |
| 44 | [blader/humanizer](https://github.com/blader/humanizer) | +16 | 34349 |
| 45 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +16 | 5318 |
| 46 | [different-ai/openwork](https://github.com/different-ai/openwork) | +15 | 21579 |
| 47 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +15 | 14581 |
| 48 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +15 | 30361 |
| 49 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +15 | 23330 |
| 50 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +15 | 34094 |
| 51 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +14 | 46304 |
| 52 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +14 | 19702 |
| 53 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +13 | 38185 |
| 54 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +13 | 34247 |
| 55 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +13 | 22550 |
| 56 | [xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer](https://github.com/xdash/FDE-the-Guidance-Book-of-Forward-Deployed-Engineer) | +13 | 3601 |
| 57 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +12 | 5849 |
| 58 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +12 | 17383 |
| 59 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +12 | 7241 |
| 60 | [browser-use/video-use](https://github.com/browser-use/video-use) | +12 | 20267 |
| 61 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +11 | 4038 |
| 62 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +11 | 476 |
| 63 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +11 | 44926 |
| 64 | [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) | +11 | 1011 |
| 65 | [Hidashimora/free-vpn-anti-rkn](https://github.com/Hidashimora/free-vpn-anti-rkn) | +11 | 351 |
| 66 | [HakanSeven12/OpenCADStudio](https://github.com/HakanSeven12/OpenCADStudio) | +11 | 566 |
| 67 | [multica-ai/multica](https://github.com/multica-ai/multica) | +11 | 44805 |
| 68 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +11 | 9438 |
| 69 | [every-app/open-seo](https://github.com/every-app/open-seo) | +10 | 10952 |
| 70 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +10 | 40076 |
| 71 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +10 | 769 |
| 72 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +10 | 46102 |
| 73 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +10 | 2556 |
| 74 | [unclebob/swarm-forge](https://github.com/unclebob/swarm-forge) | +10 | 1969 |
| 75 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +10 | 8400 |
| 76 | [sopaco/deepwiki-rs](https://github.com/sopaco/deepwiki-rs) | +10 | 1545 |
| 77 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +10 | 28309 |
| 78 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +10 | 8275 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +10 | 43551 |
| 80 | [ben-z/findphone](https://github.com/ben-z/findphone) | +10 | 1033 |
| 81 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +10 | 40202 |
| 82 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +9 | 2021 |
| 83 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +9 | 4320 |
| 84 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +9 | 1708 |
| 85 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9 | 33163 |
| 86 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +9 | 1259 |
| 87 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +9 | 905 |
| 88 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 839 |
| 89 | [petergyang/human-review](https://github.com/petergyang/human-review) | +9 | 618 |
| 90 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +9 | 5012 |
| 91 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +9 | 3799 |
| 92 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +8 | 2433 |
| 93 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +8 | 2233 |
| 94 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 330 |
| 95 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1433 |
| 96 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +8 | 7214 |
| 97 | [openai/codex-security](https://github.com/openai/codex-security) | +8 | 9333 |
| 98 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 1982 |
| 99 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +7 | 2386 |
| 100 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +7 | 8181 |
| 101 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +7 | 9751 |
| 102 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +7 | 19314 |
| 103 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 961 |
| 104 | [CopilotKit/OpenTag](https://github.com/CopilotKit/OpenTag) | +6 | 1018 |
| 105 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +6 | 4547 |
| 106 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 13713 |
| 107 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +6 | 5796 |
| 108 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +6 | 29764 |
| 109 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +6 | 838 |
| 110 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +6 | 41391 |
| 111 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +6 | 3075 |
| 112 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +6 | 3884 |
| 113 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +6 | 5230 |
| 114 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1349 |
| 115 | [thecmdguy/Ducky](https://github.com/thecmdguy/Ducky) | +5 | 848 |
| 116 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +5 | 44652 |
| 117 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +5 | 1889 |
| 118 | [uber/ADR](https://github.com/uber/ADR) | +5 | 1297 |
| 119 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +4 | 6075 |
| 120 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +4 | 1664 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +209 | 8577 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +150 | 43359 |
| 3 | [block/buzz](https://github.com/block/buzz) | +120 | 25285 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +115 | 40156 |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +107 | 23330 |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +92 | 27221 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +89 | 30809 |
| 8 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +89 | 25922 |
| 9 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +88 | 18838 |
| 10 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +79 | 13790 |
| 11 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +76 | 15776 |
| 12 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +73 | 26793 |
| 13 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +72 | 18481 |
| 14 | [usestrix/strix](https://github.com/usestrix/strix) | +69 | 49947 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +68 | 19000 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +68 | 30361 |
| 17 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +65 | 13429 |
| 18 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +59 | 14581 |
| 19 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +57 | 21118 |
| 20 | [brightdata/cli](https://github.com/brightdata/cli) | +55 | 2487 |
| 21 | [oblien/openship](https://github.com/oblien/openship) | +55 | 10460 |
| 22 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +50 | 18159 |
| 23 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +49 | 34247 |
| 24 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +48 | 13447 |
| 25 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +48 | 10575 |
| 26 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +47 | 20101 |
| 27 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +47 | 7363 |
| 28 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +47 | 22550 |
| 29 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +47 | 46102 |
| 30 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +45 | 49807 |
| 31 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46304 |
| 32 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +44 | 43941 |
| 33 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +44 | 38185 |
| 34 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +43 | 33124 |
| 35 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +43 | 8569 |
| 36 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +42 | 60743 |
| 37 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +42 | 1333 |
| 38 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +41 | 22995 |
| 39 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +41 | 29449 |
| 40 | [google/skills](https://github.com/google/skills) | +39 | 16647 |
| 41 | [goauthentik/authentik](https://github.com/goauthentik/authentik) | +39 | 23930 |
| 42 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +38 | 8246 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +38 | 40076 |
| 44 | [malisper/pgrust](https://github.com/malisper/pgrust) | +38 | 4216 |
| 45 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +37 | 8181 |
| 46 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +37 | 14702 |
| 47 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +37 | 33163 |
| 48 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +36 | 10242 |
| 49 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +36 | 19189 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +35 | 16459 |
| 51 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +35 | 7800 |
| 52 | [yc-software/qm](https://github.com/yc-software/qm) | +34 | 12513 |
| 53 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9333 |
| 54 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +33 | 4192 |
| 55 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +32 | 19702 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 43551 |
| 57 | [multica-ai/multica](https://github.com/multica-ai/multica) | +32 | 44805 |
| 58 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +31 | 44926 |
| 59 | [blader/humanizer](https://github.com/blader/humanizer) | +31 | 34349 |
| 60 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +31 | 34094 |
| 61 | [trycompai/crm](https://github.com/trycompai/crm) | +30 | 7735 |
| 62 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +30 | 9318 |
| 63 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +29 | 31243 |
| 64 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +29 | 9807 |
| 65 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +28 | 5012 |
| 66 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +28 | 7241 |
| 67 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +27 | 20747 |
| 68 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +27 | 36321 |
| 69 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8575 |
| 70 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +26 | 7739 |
| 71 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +25 | 24128 |
| 72 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +25 | 28309 |
| 73 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +25 | 4424 |
| 74 | [different-ai/openwork](https://github.com/different-ai/openwork) | +24 | 21579 |
| 75 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +24 | 726 |
| 76 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +24 | 4712 |
| 77 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +24 | 9438 |
| 78 | [ymichael/bb](https://github.com/ymichael/bb) | +23 | 1468 |
| 79 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +23 | 8547 |
| 80 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 3799 |
| 81 | [marcelroed/gigatoken](https://github.com/marcelroed/gigatoken) | +23 | 3943 |
| 82 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +23 | 7076 |
| 83 | [every-app/open-seo](https://github.com/every-app/open-seo) | +22 | 10952 |
| 84 | [t8y2/dbx](https://github.com/t8y2/dbx) | +22 | 13728 |
| 85 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +21 | 17383 |
| 86 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +21 | 8275 |
| 87 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 13713 |
| 88 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +21 | 4884 |
| 89 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +20 | 2556 |
| 90 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 5318 |
| 91 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 676 |
| 92 | [browser-use/video-use](https://github.com/browser-use/video-use) | +20 | 20267 |
| 93 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +20 | 41391 |
| 94 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +20 | 5477 |
| 95 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +19 | 3573 |
| 96 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +19 | 7804 |
| 97 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +19 | 15779 |
| 98 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +18 | 4547 |
| 99 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +18 | 5674 |
| 100 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +18 | 15244 |
| 101 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13093 |
| 102 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +18 | 31544 |
| 103 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11138 |
| 104 | [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy) | +16 | 2025 |
| 105 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +16 | 8400 |
| 106 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +16 | 6662 |
| 107 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +16 | 35102 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16336 |
| 109 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +14 | 9751 |
| 110 | [decolua/9router](https://github.com/decolua/9router) | +14 | 24989 |
| 111 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +13 | 2433 |
| 112 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +13 | 29764 |
| 113 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +13 | 32990 |
| 114 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +13 | 3517 |
| 115 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +13 | 27127 |
| 116 | [penecho/penecho](https://github.com/penecho/penecho) | +13 | 1966 |
| 117 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +12 | 5849 |
| 118 | [vectorize-io/self-driving-agents](https://github.com/vectorize-io/self-driving-agents) | +12 | 2021 |
| 119 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 4038 |
| 120 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +12 | 19314 |
| 121 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +12 | 46768 |
| 122 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +12 | 2141 |
| 123 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +11 | 44652 |
| 124 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +11 | 14383 |
| 125 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +11 | 46787 |
| 126 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +11 | 3504 |
| 127 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +10 | 4320 |
| 128 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +10 | 476 |
| 129 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +10 | 2233 |
| 130 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +10 | 5796 |
| 131 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10219 |
| 132 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +10 | 5230 |
| 133 | [anbeime/skill](https://github.com/anbeime/skill) | +10 | 4960 |
| 134 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 30043 |
| 135 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +10 | 2678 |
| 136 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1531 |
| 137 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +10 | 2368 |
| 138 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 1048 |
| 139 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +10 | 7916 |
| 140 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +10 | 9989 |
| 141 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1835 |
| 142 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +10 | 4854 |
| 143 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 2386 |
| 144 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +9 | 905 |
| 145 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +9 | 1664 |
| 146 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 839 |
| 147 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28096 |
| 148 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +9 | 10561 |
| 149 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +9 | 6278 |
| 150 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +9 | 11884 |
| 151 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +9 | 1259 |
| 152 | [petergyang/human-review](https://github.com/petergyang/human-review) | +9 | 618 |
| 153 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +9 | 1761 |
| 154 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +9 | 9783 |
| 155 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 2127 |
| 156 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +8 | 330 |
| 157 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1433 |
| 158 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +8 | 3075 |
| 159 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +8 | 1982 |
| 160 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6682 |
| 161 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +8 | 713 |
| 162 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8450 |
| 163 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +8 | 1182 |
| 164 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9783 |
| 165 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +8 | 19381 |
| 166 | [openai/skills](https://github.com/openai/skills) | +8 | 24639 |
| 167 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 4060 |
| 168 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +8 | 5046 |
| 169 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +8 | 9903 |
| 170 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +8 | 1598 |
| 171 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1057 |
| 172 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +8 | 0 |
| 173 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +8 | 1993 |
| 174 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +7 | 6075 |
| 175 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +7 | 24029 |
| 176 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 5966 |
| 177 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +7 | 1915 |
| 178 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10483 |
| 179 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +7 | 14411 |
| 180 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +7 | 6581 |
| 181 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +7 | 8094 |
| 182 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +7 | 1804 |
| 183 | [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | +7 | 1619 |
| 184 | [openai/plugins](https://github.com/openai/plugins) | +7 | 4994 |
| 185 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +7 | 2931 |
| 186 | [open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1) | +6 | 1086 |
| 187 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +6 | 838 |
| 188 | [atilaahmettaner/tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | +6 | 3884 |
| 189 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +6 | 17111 |
| 190 | [visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness) | +6 | 2502 |
| 191 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +6 | 1889 |
| 192 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 961 |
| 193 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 381 |
| 194 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +6 | 27226 |
| 195 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +6 | 9332 |
| 196 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +6 | 5552 |
| 197 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14557 |
| 198 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +6 | 27920 |
| 199 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 517 |
| 200 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +6 | 29867 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5848 |
| 202 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1349 |
| 203 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +5 | 248 |
| 204 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +5 | 1009 |
| 205 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2863 |
| 206 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +5 | 1179 |
| 207 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7045 |
| 208 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1291 |
| 209 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +5 | 8433 |
| 210 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +5 | 3238 |
| 211 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 684 |
| 212 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +5 | 2640 |
| 213 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +5 | 748 |
| 214 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1225 |
| 215 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5416 |
| 216 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 846 |
| 217 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5249 |
| 218 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +4 | 314 |
| 219 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11192 |
| 220 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +4 | 364 |
| 221 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5139 |
| 222 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9453 |
| 223 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3317 |
| 224 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 401 |
| 225 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +4 | 5876 |
| 226 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 396 |
| 227 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 83 |
| 228 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3156 |
| 229 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 781 |
| 230 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28273 |
| 231 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4607 |
| 232 | [SulgX/SulgX-Panel](https://github.com/SulgX/SulgX-Panel) | +3 | 404 |
| 233 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +3 | 4942 |
| 234 | [darkzOGx/youtube-automation-agent](https://github.com/darkzOGx/youtube-automation-agent) | +3 | 1776 |
| 235 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 432 |
| 236 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 688 |
| 237 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 437 |
| 238 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 599 |
| 239 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 398 |
| 240 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 145 |
| 241 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18814 |
| 242 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1235 |
| 243 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +3 | 336 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4958 |
| 245 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1973 |
| 246 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +3 | 3080 |
| 247 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9238 |
| 248 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10446 |
| 249 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 884 |
| 250 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 307 |
| 251 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +2 | 484 |
| 252 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +2 | 664 |
| 253 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1243 |
| 254 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +2 | 180 |
| 255 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +2 | 12220 |
| 256 | [ljb1020/video-batch-download](https://github.com/ljb1020/video-batch-download) | +2 | 36 |
| 257 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2 | 2783 |
| 258 | [timethrough/xiaohei-Chrome](https://github.com/timethrough/xiaohei-Chrome) | +2 | 145 |
| 259 | [future-agi/future-agi](https://github.com/future-agi/future-agi) | +2 | 1627 |
| 260 | [hwttop5/tabbit2api](https://github.com/hwttop5/tabbit2api) | +2 | 84 |
| 261 | [ghanning/PolyLayout](https://github.com/ghanning/PolyLayout) | +2 | 71 |
| 262 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6192 |
| 263 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +2 | 5226 |
| 264 | [Joanium/Joanium](https://github.com/Joanium/Joanium) | +2 | 204 |
| 265 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 446 |
| 266 | [twalichiewicz/Backchannel](https://github.com/twalichiewicz/Backchannel) | +2 | 241 |
| 267 | [maxedapps/agent-skills](https://github.com/maxedapps/agent-skills) | +2 | 53 |
| 268 | [AashishH15/Lexicon](https://github.com/AashishH15/Lexicon) | +2 | 140 |
| 269 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 105 |
| 270 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +2 | 776 |
| 271 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1262 |
| 272 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2847 |
| 273 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 204 |
| 274 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 849 |
| 275 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 254 |
| 276 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10360 |
| 277 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1378 |
| 278 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 496 |
| 279 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 98 |
| 280 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2481 |
| 281 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 282 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2690 |
| 283 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 431 |
| 284 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +1 | 506 |
| 285 | [koosoli/ESPHomeDesigner](https://github.com/koosoli/ESPHomeDesigner) | +1 | 1033 |
| 286 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +1 | 5971 |
| 287 | [mruniquehacker/KnightBot-Mini](https://github.com/mruniquehacker/KnightBot-Mini) | +1 | 1036 |
| 288 | [FFF686868/proxypin-wloc-spoofer](https://github.com/FFF686868/proxypin-wloc-spoofer) | +1 | 362 |
| 289 | [tetherto/pearpass-app-mobile](https://github.com/tetherto/pearpass-app-mobile) | +1 | 265 |
| 290 | [appariciojunior/PrismSystem](https://github.com/appariciojunior/PrismSystem) | +1 | 54 |
| 291 | [The412Banner/bannerhub-revanced](https://github.com/The412Banner/bannerhub-revanced) | +1 | 149 |
| 292 | [java-up-up/nexus-agent](https://github.com/java-up-up/nexus-agent) | +1 | 289 |
| 293 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +1 | 556 |
| 294 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +1 | 185 |
| 295 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +1 | 401 |
| 296 | [kokodio/metallum](https://github.com/kokodio/metallum) | +1 | 44 |
| 297 | [jasonwu1994/Gboard-patches](https://github.com/jasonwu1994/Gboard-patches) | +1 | 201 |
| 298 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +1 | 2445 |
| 299 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +1 | 436 |
| 300 | [MrBZBZ/LeavesHack](https://github.com/MrBZBZ/LeavesHack) | +1 | 76 |
