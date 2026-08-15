---
title: "2026-08-15 GitHub增长趋势报告"
description: "1.deepseek-harness-desktop+10 2.watermarks-remover+7 3.diagram-design+7 4.DeepTutor+5 5.prime-agent+4"
date: 2026-08-15T20:23:32+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-15 20:23:32

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
        'daily': {"categories": ["deepseek-ai/awesome-deepseek-agent", "123panNextGen/123pan", "OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL", "opengeos/GeoLibre", "bojieli/ai-agent-book", "MrGeDiao/shuorenhua", "spinabot/brigade", "opensandbox-group/OpenSandbox", "lightningpixel/modly", "cactus-compute/needle", "zeronsh/comet", "macro-inc/macro", "titanwings/colleague-skill", "tt-a1i/archify", "herdrdev/herdr", "PrimeIntellect-ai/prime-agent", "HKUDS/DeepTutor", "cathrynlavery/diagram-design", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop"], "data": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 7, 7, 10]},
        'weekly': {"categories": ["SMNETSTUDIO/WeChat-AI", "every-app/open-seo", "Zeejay0/gathered-scenes-zine-skill", "block/buzz", "ayghri/i-have-adhd", "emilkowalski/skills", "TencentCloud/TencentDB-Agent-Memory", "anywhere-labs/deepseek-harness-desktop", "HKUDS/DeepTutor", "corsairdev/corsair", "herdrdev/herdr", "hugohe3/ppt-master", "MiniMax-AI/MiniMax-H3", "firecrawl/anydoc", "spinabot/brigade", "stablyai/orca", "zhaoxuya520/reverse-skill", "PrimeIntellect-ai/prime-agent", "guillaumemeyer/watermarks-remover", "cathrynlavery/diagram-design"], "data": [12, 13, 13, 13, 14, 14, 16, 16, 17, 18, 18, 20, 21, 21, 22, 27, 29, 40, 45, 69]},
        'monthly': {"categories": ["cloudflare/cloudflare-os", "MadsLorentzen/ai-job-search", "TencentCloud/TencentDB-Agent-Memory", "brightdata/cli", "k1tbyte/Wand-Enhancer", "Fei-Away/Codex-Dream-Skin", "floci-io/floci", "cathrynlavery/diagram-design", "andrewyng/openworker", "zhaoxuya520/reverse-skill", "ayghri/i-have-adhd", "emilkowalski/skills", "virgiliojr94/book-to-skill", "herdrdev/herdr", "stablyai/orca", "block/buzz", "bojieli/ai-agent-book", "firecrawl/anydoc", "diegosouzapw/OmniRoute", "PrimeIntellect-ai/prime-agent"], "data": [60, 61, 62, 63, 64, 66, 74, 76, 81, 85, 87, 89, 92, 93, 128, 133, 145, 154, 155, 249]}
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
| 1 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +10 | 5703 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +7 | 9588 |
| 3 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +7 | 18468 |
| 4 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 35775 |
| 5 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +4 | 16243 |
| 6 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +3 | 29463 |
| 7 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3 | 12945 |
| 8 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +3 | 22459 |
| 9 | [macro-inc/macro](https://github.com/macro-inc/macro) | +2 | 3249 |
| 10 | [zeronsh/comet](https://github.com/zeronsh/comet) | +2 | 699 |
| 11 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +2 | 6008 |
| 12 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +2 | 6115 |
| 13 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +2 | 13384 |
| 14 | [spinabot/brigade](https://github.com/spinabot/brigade) | +2 | 2698 |
| 15 | [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua) | +1 | 1081 |
| 16 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +1 | 37596 |
| 17 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +1 | 6123 |
| 18 | [OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL](https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL) | +1 | 631 |
| 19 | [123panNextGen/123pan](https://github.com/123panNextGen/123pan) | +1 | 351 |
| 20 | [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | +1 | 5866 |
| 21 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +1 | 3823 |
| 22 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +1 | 4427 |
| 23 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +1 | 7426 |
| 24 | [PVE-Tools/PVE-Tools-9](https://github.com/PVE-Tools/PVE-Tools-9) | +1 | 2070 |
| 25 | [imbue-ai/vet](https://github.com/imbue-ai/vet) | +1 | 578 |
| 26 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +1 | 4738 |
| 27 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +1 | 244 |
| 28 | [songloft-org/songloft](https://github.com/songloft-org/songloft) | +1 | 1464 |
| 29 | [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) | +1 | 1626 |
| 30 | [huanhq99/FlixPilot](https://github.com/huanhq99/FlixPilot) | +1 | 153 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +69 | 18468 |
| 2 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +45 | 9588 |
| 3 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +40 | 16243 |
| 4 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +29 | 25463 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 46052 |
| 6 | [spinabot/brigade](https://github.com/spinabot/brigade) | +22 | 2698 |
| 7 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +21 | 16257 |
| 8 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +21 | 6061 |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +20 | 47061 |
| 10 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +18 | 29463 |
| 11 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +18 | 10116 |
| 12 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +17 | 35775 |
| 13 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +16 | 5703 |
| 14 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +16 | 21942 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +14 | 29547 |
| 16 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 20817 |
| 17 | [block/buzz](https://github.com/block/buzz) | +13 | 27561 |
| 18 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +13 | 3638 |
| 19 | [every-app/open-seo](https://github.com/every-app/open-seo) | +13 | 12041 |
| 20 | [SMNETSTUDIO/WeChat-AI](https://github.com/SMNETSTUDIO/WeChat-AI) | +12 | 1730 |
| 21 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +12 | 6008 |
| 22 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +12 | 37596 |
| 23 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +12 | 3823 |
| 24 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +11 | 28417 |
| 25 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +11 | 48527 |
| 26 | [yc-software/qm](https://github.com/yc-software/qm) | +10 | 13617 |
| 27 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +10 | 22459 |
| 28 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +10 | 2432 |
| 29 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +10 | 20543 |
| 30 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +10 | 1774 |
| 31 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +10 | 23824 |
| 32 | [macro-inc/macro](https://github.com/macro-inc/macro) | +9 | 3249 |
| 33 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +9 | 4124 |
| 34 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +9 | 21804 |
| 35 | [brightdata/cli](https://github.com/brightdata/cli) | +9 | 5461 |
| 36 | [google/skills](https://github.com/google/skills) | +9 | 18309 |
| 37 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +9 | 8652 |
| 38 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +8 | 11839 |
| 39 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 46103 |
| 40 | [lightningpixel/modly](https://github.com/lightningpixel/modly) | +8 | 6115 |
| 41 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +8 | 12945 |
| 42 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +8 | 35336 |
| 43 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1060 |
| 44 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +8 | 5355 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +7 | 62959 |
| 46 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +7 | 7657 |
| 47 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +7 | 18855 |
| 48 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +7 | 24994 |
| 49 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +7 | 4776 |
| 50 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +7 | 48203 |
| 51 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +7 | 10186 |
| 52 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +7 | 15657 |
| 53 | [floci-io/floci](https://github.com/floci-io/floci) | +7 | 20128 |
| 54 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +7 | 5908 |
| 55 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +7 | 557 |
| 56 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +7 | 8799 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 35811 |
| 58 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +7 | 6177 |
| 59 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +7 | 15133 |
| 60 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +7 | 24110 |
| 61 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +6 | 7600 |
| 62 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +6 | 2051 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 44398 |
| 64 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 32027 |
| 65 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 11527 |
| 66 | [AgentWrapper/agent-orchestrator](https://github.com/AgentWrapper/agent-orchestrator) | +6 | 9538 |
| 67 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 47283 |
| 68 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +5 | 30253 |
| 69 | [trycompai/crm](https://github.com/trycompai/crm) | +5 | 8481 |
| 70 | [Jwuthri/Tracely](https://github.com/Jwuthri/Tracely) | +5 | 642 |
| 71 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 7982 |
| 72 | [t8y2/dbx](https://github.com/t8y2/dbx) | +5 | 14963 |
| 73 | [ZJU-REAL/HugAgentOS](https://github.com/ZJU-REAL/HugAgentOS) | +5 | 359 |
| 74 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +5 | 1457 |
| 75 | [Kylin010/tcpfit](https://github.com/Kylin010/tcpfit) | +5 | 443 |
| 76 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +5 | 244 |
| 77 | [AntigmaLabs/ante](https://github.com/AntigmaLabs/ante) | +5 | 1799 |
| 78 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 34616 |
| 79 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +5 | 15499 |
| 80 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +5 | 2206 |
| 81 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +5 | 28959 |
| 82 | [aipoch/open-science](https://github.com/aipoch/open-science) | +5 | 2477 |
| 83 | [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) | +5 | 538 |
| 84 | [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | +5 | 1809 |
| 85 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +4 | 1668 |
| 86 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 3582 |
| 87 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +4 | 8315 |
| 88 | [tanishqkancharla/calldiff](https://github.com/tanishqkancharla/calldiff) | +4 | 408 |
| 89 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 30920 |
| 90 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +4 | 2552 |
| 91 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4 | 31814 |
| 92 | [gloom-sh/gloomberb](https://github.com/gloom-sh/gloomberb) | +4 | 1685 |
| 93 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +4 | 41077 |
| 94 | [pacifio/atlas](https://github.com/pacifio/atlas) | +4 | 1037 |
| 95 | [NVIDIA-NeMo/Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) | +4 | 1564 |
| 96 | [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | +4 | 1081 |
| 97 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +4 | 27253 |
| 98 | [AML-memory/agent-memory-leaderboard](https://github.com/AML-memory/agent-memory-leaderboard) | +4 | 716 |
| 99 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +4 | 2370 |
| 100 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +4 | 3603 |
| 101 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +4 | 30679 |
| 102 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +4 | 1017 |
| 103 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 14221 |
| 104 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +3 | 40666 |
| 105 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +3 | 4580 |
| 106 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +3 | 13384 |
| 107 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +3 | 30114 |
| 108 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3 | 19992 |
| 109 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +3 | 24306 |
| 110 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 5662 |
| 111 | [waiterve/wai-play](https://github.com/waiterve/wai-play) | +3 | 178 |
| 112 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +3 | 33550 |
| 113 | [IAmIronMan42/MiniMax-H3-FineTuning](https://github.com/IAmIronMan42/MiniMax-H3-FineTuning) | +3 | 303 |
| 114 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 4820 |
| 115 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +3 | 1349 |
| 116 | [beenuar/AiSOC](https://github.com/beenuar/AiSOC) | +3 | 2435 |
| 117 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +3 | 1298 |
| 118 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +3 | 1215 |
| 119 | [pzqpzq/Principia](https://github.com/pzqpzq/Principia) | +3 | 587 |
| 120 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | +3 | 417 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +249 | 16243 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 48527 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +154 | 16257 |
| 4 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +145 | 37596 |
| 5 | [block/buzz](https://github.com/block/buzz) | +133 | 27561 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +128 | 46052 |
| 7 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +93 | 29463 |
| 8 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +92 | 21804 |
| 9 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +89 | 29547 |
| 10 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +87 | 20817 |
| 11 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +85 | 25463 |
| 12 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +81 | 14548 |
| 13 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +76 | 18468 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | +74 | 20128 |
| 15 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +66 | 13755 |
| 16 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +64 | 17575 |
| 17 | [brightdata/cli](https://github.com/brightdata/cli) | +63 | 5461 |
| 18 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +62 | 21942 |
| 19 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +61 | 31814 |
| 20 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +60 | 8315 |
| 21 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +59 | 28417 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +57 | 47061 |
| 23 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +56 | 24994 |
| 24 | [oblien/openship](https://github.com/oblien/openship) | +56 | 10775 |
| 25 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +55 | 15657 |
| 26 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +55 | 30920 |
| 27 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +53 | 8652 |
| 28 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +53 | 35775 |
| 29 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +53 | 23824 |
| 30 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +52 | 21446 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +51 | 12945 |
| 32 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +49 | 10186 |
| 33 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +47 | 15499 |
| 34 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +46 | 30253 |
| 35 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +46 | 33766 |
| 36 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +45 | 9588 |
| 37 | [yc-software/qm](https://github.com/yc-software/qm) | +44 | 13617 |
| 38 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +44 | 6061 |
| 39 | [google/skills](https://github.com/google/skills) | +44 | 18309 |
| 40 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +44 | 34616 |
| 41 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +44 | 46815 |
| 42 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +44 | 11839 |
| 43 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +43 | 1485 |
| 44 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +42 | 62959 |
| 45 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +42 | 25014 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +41 | 20543 |
| 47 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +40 | 48203 |
| 48 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +40 | 7886 |
| 49 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +39 | 8461 |
| 50 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +38 | 17634 |
| 51 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +37 | 5131 |
| 52 | [trycompai/crm](https://github.com/trycompai/crm) | +35 | 8481 |
| 53 | [every-app/open-seo](https://github.com/every-app/open-seo) | +35 | 12041 |
| 54 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +35 | 15133 |
| 55 | [blader/humanizer](https://github.com/blader/humanizer) | +35 | 35811 |
| 56 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +35 | 39027 |
| 57 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +34 | 35336 |
| 58 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +34 | 41077 |
| 59 | [openai/codex-security](https://github.com/openai/codex-security) | +33 | 9858 |
| 60 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +33 | 10116 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 46103 |
| 62 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +33 | 44398 |
| 63 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +33 | 10862 |
| 64 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +32 | 3638 |
| 65 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +31 | 6177 |
| 66 | [malisper/pgrust](https://github.com/malisper/pgrust) | +28 | 4434 |
| 67 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +28 | 19691 |
| 68 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +27 | 18855 |
| 69 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +27 | 7993 |
| 70 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +27 | 11527 |
| 71 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +26 | 4776 |
| 72 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +26 | 24464 |
| 73 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +26 | 21421 |
| 74 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +26 | 8382 |
| 75 | [different-ai/openwork](https://github.com/different-ai/openwork) | +25 | 22310 |
| 76 | [get-bb/bb](https://github.com/get-bb/bb) | +25 | 1985 |
| 77 | [emiliaprotocol/emilia-protocol](https://github.com/emiliaprotocol/emilia-protocol) | +25 | 841 |
| 78 | [openchamber/openchamber](https://github.com/openchamber/openchamber) | +25 | 8799 |
| 79 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +25 | 32027 |
| 80 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +25 | 8206 |
| 81 | [spinabot/brigade](https://github.com/spinabot/brigade) | +24 | 2698 |
| 82 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +24 | 3147 |
| 83 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +24 | 45552 |
| 84 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +24 | 5662 |
| 85 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +24 | 28978 |
| 86 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +23 | 4013 |
| 87 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +23 | 9966 |
| 88 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +22 | 0 |
| 89 | [browser-use/video-use](https://github.com/browser-use/video-use) | +22 | 20732 |
| 90 | [t8y2/dbx](https://github.com/t8y2/dbx) | +22 | 14963 |
| 91 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +21 | 3823 |
| 92 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +21 | 14221 |
| 93 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +20 | 9025 |
| 94 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +20 | 6054 |
| 95 | [agentplugins/agent-plugins-spec](https://github.com/agentplugins/agent-plugins-spec) | +20 | 1027 |
| 96 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +20 | 8536 |
| 97 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +19 | 5355 |
| 98 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +19 | 5079 |
| 99 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +18 | 7982 |
| 100 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 13465 |
| 101 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5823 |
| 102 | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | +17 | 4124 |
| 103 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +17 | 42590 |
| 104 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11186 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +16 | 47283 |
| 106 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +15 | 8877 |
| 107 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +15 | 16497 |
| 108 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +15 | 31913 |
| 109 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +14 | 6146 |
| 110 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +14 | 3091 |
| 111 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +14 | 708 |
| 112 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 30114 |
| 113 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +14 | 16042 |
| 114 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +14 | 2206 |
| 115 | [penecho/penecho](https://github.com/penecho/penecho) | +14 | 2077 |
| 116 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +13 | 4580 |
| 117 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +13 | 4001 |
| 118 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +13 | 19992 |
| 119 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +13 | 9969 |
| 120 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +13 | 5908 |
| 121 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +13 | 8612 |
| 122 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +13 | 2233 |
| 123 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 124 | [decolua/9router](https://github.com/decolua/9router) | +13 | 25500 |
| 125 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +13 | 5147 |
| 126 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +12 | 824 |
| 127 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +12 | 6008 |
| 128 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +12 | 1774 |
| 129 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1349 |
| 130 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +12 | 2531 |
| 131 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +12 | 2905 |
| 132 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +12 | 30680 |
| 133 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +12 | 15575 |
| 134 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +12 | 2051 |
| 135 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +11 | 1457 |
| 136 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +11 | 22459 |
| 137 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +11 | 1861 |
| 138 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +11 | 5941 |
| 139 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +11 | 4913 |
| 140 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +10 | 2432 |
| 141 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +10 | 2739 |
| 142 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +10 | 2370 |
| 143 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 10553 |
| 144 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +10 | 2219 |
| 145 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +10 | 10301 |
| 146 | [petergyang/human-review](https://github.com/petergyang/human-review) | +10 | 999 |
| 147 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +10 | 27575 |
| 148 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +10 | 1862 |
| 149 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +10 | 3657 |
| 150 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +10 | 3356 |
| 151 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1889 |
| 152 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +9 | 0 |
| 153 | [open-city-ai/haidian](https://github.com/open-city-ai/haidian) | +9 | 376 |
| 154 | [Gabson0x/bountyforge](https://github.com/Gabson0x/bountyforge) | +9 | 353 |
| 155 | [crawfordxx/xiaoma-durex-copywriter](https://github.com/crawfordxx/xiaoma-durex-copywriter) | +9 | 557 |
| 156 | [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) | +9 | 981 |
| 157 | [Fenng/Tech-Doc-Style-Chinese](https://github.com/Fenng/Tech-Doc-Style-Chinese) | +9 | 964 |
| 158 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +9 | 44991 |
| 159 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +9 | 14653 |
| 160 | [Jia-Ethan/codex-keysmith](https://github.com/Jia-Ethan/codex-keysmith) | +9 | 3562 |
| 161 | [TencentCloud/Octop](https://github.com/TencentCloud/Octop) | +9 | 1017 |
| 162 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +9 | 28488 |
| 163 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +9 | 8656 |
| 164 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +9 | 33586 |
| 165 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +9 | 5594 |
| 166 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +9 | 1312 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +9 | 1715 |
| 168 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +8 | 24306 |
| 169 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +8 | 1060 |
| 170 | [securo-finance/securo](https://github.com/securo-finance/securo) | +8 | 1558 |
| 171 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +8 | 47037 |
| 172 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +8 | 10921 |
| 173 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +8 | 9926 |
| 174 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +8 | 4820 |
| 175 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +8 | 2862 |
| 176 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +8 | 6503 |
| 177 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +8 | 2305 |
| 178 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +8 | 28214 |
| 179 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +8 | 8285 |
| 180 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +8 | 1150 |
| 181 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +8 | 9957 |
| 182 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +7 | 10628 |
| 183 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +7 | 6721 |
| 184 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +7 | 41042 |
| 185 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +7 | 13384 |
| 186 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +7 | 2552 |
| 187 | [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit) | +7 | 1298 |
| 188 | [uber/ADR](https://github.com/uber/ADR) | +7 | 1427 |
| 189 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +7 | 6128 |
| 190 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +7 | 1382 |
| 191 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 26 |
| 192 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 27407 |
| 193 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +7 | 10395 |
| 194 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +7 | 8612 |
| 195 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 30066 |
| 196 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +7 | 3262 |
| 197 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 198 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 272 |
| 199 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 276 |
| 200 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 444 |
| 201 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3026 |
| 202 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14629 |
| 203 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +6 | 528 |
| 204 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 2172 |
| 205 | [KubeezMedia/kubeez-scroll-world-video](https://github.com/KubeezMedia/kubeez-scroll-world-video) | +6 | 531 |
| 206 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5804 |
| 207 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +5 | 1668 |
| 208 | [vibevoice-community/VibeVoice](https://github.com/vibevoice-community/VibeVoice) | +5 | 1500 |
| 209 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 5602 |
| 210 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +5 | 427 |
| 211 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 523 |
| 212 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 7195 |
| 213 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 780 |
| 214 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5697 |
| 215 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 3015 |
| 216 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1334 |
| 217 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 694 |
| 218 | [2951461586/GPT-Register-Tool](https://github.com/2951461586/GPT-Register-Tool) | +4 | 310 |
| 219 | [harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) | +4 | 1215 |
| 220 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +4 | 11367 |
| 221 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 407 |
| 222 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 4919 |
| 223 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +4 | 5190 |
| 224 | [openai/plugins](https://github.com/openai/plugins) | +4 | 5104 |
| 225 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +4 | 1298 |
| 226 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +4 | 3368 |
| 227 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +4 | 9591 |
| 228 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 413 |
| 229 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +4 | 3479 |
| 230 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3320 |
| 231 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 105 |
| 232 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 961 |
| 233 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3245 |
| 234 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +4 | 28416 |
| 235 | [crimera/piko](https://github.com/crimera/piko) | +4 | 4697 |
| 236 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 173 |
| 237 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +3 | 998 |
| 238 | [AIsouler/MyClash](https://github.com/AIsouler/MyClash) | +3 | 523 |
| 239 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +3 | 9512 |
| 240 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +3 | 514 |
| 241 | [PlatformRelay/Kubernetes-Workshop](https://github.com/PlatformRelay/Kubernetes-Workshop) | +3 | 190 |
| 242 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +3 | 1322 |
| 243 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12310 |
| 244 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +3 | 1158 |
| 245 | [u7079256/paperjury](https://github.com/u7079256/paperjury) | +3 | 940 |
| 246 | [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | +3 | 345 |
| 247 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 547 |
| 248 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18949 |
| 249 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +3 | 3436 |
| 250 | [everett7623/airport-recommendations-2026](https://github.com/everett7623/airport-recommendations-2026) | +3 | 770 |
| 251 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +3 | 2816 |
| 252 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +3 | 452 |
| 253 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 0 |
| 254 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +3 | 1392 |
| 255 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 418 |
| 256 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +3 | 5535 |
| 257 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 904 |
| 258 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 600 |
| 259 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +3 | 299 |
| 260 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1188 |
| 261 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 2042 |
| 262 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 5076 |
| 263 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9199 |
| 264 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 836 |
| 265 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10497 |
| 266 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +2 | 714 |
| 267 | [xikhar/persona](https://github.com/xikhar/persona) | +2 | 891 |
| 268 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +2 | 326 |
| 269 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +2 | 1280 |
| 270 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3991 |
| 271 | [huangjia2019/claude-code-engineering](https://github.com/huangjia2019/claude-code-engineering) | +2 | 1068 |
| 272 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | +2 | 683 |
| 273 | [thangnq111203/oss-steward](https://github.com/thangnq111203/oss-steward) | +2 | 91 |
| 274 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +2 | 585 |
| 275 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +2 | 1593 |
| 276 | [SamurAIGPT/seedance-2-generator](https://github.com/SamurAIGPT/seedance-2-generator) | +2 | 76 |
| 277 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +2 | 1242 |
| 278 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 102 |
| 279 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 423 |
| 280 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 106 |
| 281 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +2 | 878 |
| 282 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +2 | 120 |
| 283 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 206 |
| 284 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +2 | 338 |
| 285 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +2 | 2900 |
| 286 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +2 | 266 |
| 287 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3160 |
| 288 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +2 | 10411 |
| 289 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1195 |
| 290 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1389 |
| 291 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 511 |
| 292 | [xoureldeen/Vectras-VM-Android](https://github.com/xoureldeen/Vectras-VM-Android) | +2 | 2550 |
| 293 | [Nekogram/Nekogram](https://github.com/Nekogram/Nekogram) | +2 | 3807 |
| 294 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +2 | 31476 |
| 295 | [anonfaded/FadCam](https://github.com/anonfaded/FadCam) | +2 | 2706 |
| 296 | [ankitbaghel01/wellfound_autoApply](https://github.com/ankitbaghel01/wellfound_autoApply) | +1 | 108 |
| 297 | [Matchameleon/gpt-codex-plugin](https://github.com/Matchameleon/gpt-codex-plugin) | +1 | 139 |
| 298 | [evan-steinhilb/md2hd](https://github.com/evan-steinhilb/md2hd) | +1 | 91 |
| 299 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1299 |
| 300 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +1 | 917 |
