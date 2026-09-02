---
title: "2026-08-31 GitHub增长趋势报告"
description: "1.OpenMAIC+31 2.archify+29 3.scientific-agent-skills+11 4.HeliosGen+9 5.awesome-gpt-image-2+9"
date: 2026-08-31T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-09-02 22:25:51

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
        'daily': {"categories": ["calesthio/OpenMontage", "MetaMask-AI/metamask-desktop", "zackb/tether", "p-e-w/heretic", "Lakr233/vphone-cli", "can1357/oh-my-pi", "MobAI-App/simslim", "handsomestWei/patent-disclosure-skill", "zhaoxuya520/reverse-skill", "bilawalsidhu/gods-eye-view", "every-app/open-seo", "laoma2053/awesome-zhuiju-free", "sapientinc/PRAXIST", "stablyai/orca", "arcboxlabs/arcbox", "freestylefly/awesome-gpt-image-2", "SegFault42/HeliosGen", "K-Dense-AI/scientific-agent-skills", "tt-a1i/archify", "THU-MAIC/OpenMAIC"], "data": [5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 11, 29, 31]},
        'weekly': {"categories": ["zhaoxuya520/reverse-skill", "pathwaycom/arc-task-gen", "Gaoshu705/QzoneArchive", "anywhere-labs/deepseek-harness-desktop", "tashfeenahmed/freellmapi", "FlashML-org/FreeToken", "vorssaintapp/vorssaint-utils", "calesthio/OpenMontage", "k1tbyte/Wand-Enhancer", "openJiuwen-ai/jiuwenswarm", "MadsLorentzen/ai-job-search", "sapientinc/PRAXIST", "tailscale/tailcat", "K-Dense-AI/scientific-agent-skills", "stablyai/orca", "basecamp/omarchy", "THU-MAIC/OpenMAIC", "freestylefly/awesome-gpt-image-2", "bilawalsidhu/gods-eye-view", "tt-a1i/archify"], "data": [19, 20, 20, 22, 23, 26, 27, 27, 30, 33, 35, 35, 36, 37, 39, 50, 51, 66, 84, 166]},
        'monthly': {"categories": ["TencentCloud/TencentDB-Agent-Memory", "herdrdev/herdr", "basecamp/omarchy", "bojieli/ai-agent-book", "emilkowalski/skills", "floci-io/floci", "k1tbyte/Wand-Enhancer", "bilawalsidhu/gods-eye-view", "freestylefly/awesome-gpt-image-2", "cloudflare/computer", "block/buzz", "guillaumemeyer/watermarks-remover", "anywhere-labs/deepseek-harness-desktop", "virgiliojr94/book-to-skill", "zhaoxuya520/reverse-skill", "stablyai/orca", "cathrynlavery/diagram-design", "firecrawl/anydoc", "tt-a1i/archify", "PrimeIntellect-ai/prime-agent"], "data": [69, 72, 75, 76, 78, 79, 83, 84, 85, 86, 89, 96, 106, 110, 114, 128, 137, 170, 215, 267]}
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
| 1 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +31 | 26915 |
| 2 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +29 | 38568 |
| 3 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +11 | 40692 |
| 4 | [SegFault42/HeliosGen](https://github.com/SegFault42/HeliosGen) | +9 | 1667 |
| 5 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +9 | 26343 |
| 6 | [arcboxlabs/arcbox](https://github.com/arcboxlabs/arcbox) | +9 | 1500 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +8 | 58383 |
| 8 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +8 | 5447 |
| 9 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +7 | 7513 |
| 10 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 15734 |
| 11 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +7 | 14585 |
| 12 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +6 | 33085 |
| 13 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +6 | 6192 |
| 14 | [MobAI-App/simslim](https://github.com/MobAI-App/simslim) | +6 | 1087 |
| 15 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +6 | 28719 |
| 16 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +5 | 10084 |
| 17 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +5 | 29635 |
| 18 | [zackb/tether](https://github.com/zackb/tether) | +5 | 1069 |
| 19 | [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | +5 | 1228 |
| 20 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +5 | 55019 |
| 21 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +4 | 43906 |
| 22 | [diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness) | +4 | 892 |
| 23 | [qusong0627/QuantMind](https://github.com/qusong0627/QuantMind) | +4 | 1225 |
| 24 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +4 | 14212 |
| 25 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +4 | 6316 |
| 26 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +3 | 2561 |
| 27 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +3 | 13890 |
| 28 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +3 | 2431 |
| 29 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +3 | 41516 |
| 30 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 27571 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +166 | 38568 |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +84 | 14585 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +66 | 26343 |
| 4 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +51 | 26916 |
| 5 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +50 | 36175 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +39 | 58383 |
| 7 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +37 | 40692 |
| 8 | [tailscale/tailcat](https://github.com/tailscale/tailcat) | +36 | 4846 |
| 9 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +35 | 5447 |
| 10 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +35 | 39078 |
| 11 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +33 | 6316 |
| 12 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +30 | 23358 |
| 13 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +27 | 55019 |
| 14 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +27 | 14212 |
| 15 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +26 | 10596 |
| 16 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +23 | 23319 |
| 17 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +22 | 22448 |
| 18 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +20 | 2561 |
| 19 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +20 | 9398 |
| 20 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +19 | 33085 |
| 21 | [workweave/router](https://github.com/workweave/router) | +19 | 3327 |
| 22 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +19 | 34698 |
| 23 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +19 | 2431 |
| 24 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +19 | 27571 |
| 25 | [every-app/open-seo](https://github.com/every-app/open-seo) | +18 | 15734 |
| 26 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +18 | 10084 |
| 27 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +17 | 3324 |
| 28 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +17 | 43906 |
| 29 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +15 | 35734 |
| 30 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +15 | 14485 |
| 31 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +15 | 18166 |
| 32 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +14 | 19672 |
| 33 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +13 | 13890 |
| 34 | [MetaMask-AI/metamask-desktop](https://github.com/MetaMask-AI/metamask-desktop) | +13 | 1228 |
| 35 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +13 | 29057 |
| 36 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | +13 | 3018 |
| 37 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +13 | 34131 |
| 38 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +12 | 29635 |
| 39 | [hieunc229/mailflare](https://github.com/hieunc229/mailflare) | +12 | 2141 |
| 40 | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | +12 | 2211 |
| 41 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +12 | 28719 |
| 42 | [cursor/plugins](https://github.com/cursor/plugins) | +12 | 6381 |
| 43 | [Webeoidentify/Honeypot-Detector](https://github.com/Webeoidentify/Honeypot-Detector) | +12 | 2235 |
| 44 | [tobi/walgit](https://github.com/tobi/walgit) | +12 | 2362 |
| 45 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 7513 |
| 46 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +11 | 34047 |
| 47 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +11 | 1000 |
| 48 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +11 | 26063 |
| 49 | [blader/humanizer](https://github.com/blader/humanizer) | +11 | 39263 |
| 50 | [SegFault42/HeliosGen](https://github.com/SegFault42/HeliosGen) | +10 | 1667 |
| 51 | [zackb/tether](https://github.com/zackb/tether) | +10 | 1069 |
| 52 | [agentconnect-md/agentconnect](https://github.com/agentconnect-md/agentconnect) | +10 | 1048 |
| 53 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +10 | 3005 |
| 54 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +10 | 33479 |
| 55 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +10 | 10923 |
| 56 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +10 | 13693 |
| 57 | [floci-io/floci](https://github.com/floci-io/floci) | +10 | 22895 |
| 58 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +10 | 39198 |
| 59 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +9 | 3519 |
| 60 | [arcboxlabs/arcbox](https://github.com/arcboxlabs/arcbox) | +9 | 1500 |
| 61 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +9 | 17124 |
| 62 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +9 | 38146 |
| 63 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +9 | 14730 |
| 64 | [34306/vphone-aio](https://github.com/34306/vphone-aio) | +9 | 6739 |
| 65 | [t8y2/dbx](https://github.com/t8y2/dbx) | +9 | 17575 |
| 66 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +9 | 3610 |
| 67 | [daimon3332/address](https://github.com/daimon3332/address) | +8 | 1912 |
| 68 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +8 | 19400 |
| 69 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +8 | 41516 |
| 70 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +8 | 7090 |
| 71 | [Waishnav/devspace](https://github.com/Waishnav/devspace) | +8 | 4353 |
| 72 | [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | +8 | 4210 |
| 73 | [deeplethe/utopia](https://github.com/deeplethe/utopia) | +8 | 761 |
| 74 | [multica-ai/multica](https://github.com/multica-ai/multica) | +8 | 48414 |
| 75 | [bookorbit/bookorbit](https://github.com/bookorbit/bookorbit) | +8 | 3687 |
| 76 | [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) | +8 | 2980 |
| 77 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 50697 |
| 78 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +7 | 19667 |
| 79 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +7 | 6192 |
| 80 | [MobAI-App/simslim](https://github.com/MobAI-App/simslim) | +7 | 1087 |
| 81 | [diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness) | +7 | 892 |
| 82 | [Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | +7 | 10774 |
| 83 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +7 | 6591 |
| 84 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +7 | 31838 |
| 85 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +7 | 5866 |
| 86 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +7 | 1071 |
| 87 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +7 | 22017 |
| 88 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +7 | 15952 |
| 89 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +7 | 7609 |
| 90 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +6 | 2979 |
| 91 | [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) | +6 | 3126 |
| 92 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +6 | 9882 |
| 93 | [BytePioneer-AI/codex-host](https://github.com/BytePioneer-AI/codex-host) | +6 | 1457 |
| 94 | [cbrock84/headcount](https://github.com/cbrock84/headcount) | +6 | 845 |
| 95 | [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | +6 | 8307 |
| 96 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +6 | 29975 |
| 97 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 15654 |
| 98 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +6 | 3896 |
| 99 | [warpdotdev/common-skills](https://github.com/warpdotdev/common-skills) | +6 | 492 |
| 100 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +6 | 3043 |
| 101 | [block/buzz](https://github.com/block/buzz) | +5 | 31669 |
| 102 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +5 | 21200 |
| 103 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +5 | 9962 |
| 104 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 46331 |
| 105 | [qusong0627/QuantMind](https://github.com/qusong0627/QuantMind) | +5 | 1225 |
| 106 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +5 | 64396 |
| 107 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +5 | 32182 |
| 108 | [User0332/rewards-farmer](https://github.com/User0332/rewards-farmer) | +5 | 697 |
| 109 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +5 | 12689 |
| 110 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +5 | 8876 |
| 111 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +5 | 6556 |
| 112 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5 | 38079 |
| 113 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +5 | 34741 |
| 114 | [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) | +5 | 1332 |
| 115 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 48750 |
| 116 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +4 | 5465 |
| 117 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +4 | 4343 |
| 118 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 7176 |
| 119 | [SuanmoSuanyangTechnology/MemoryBear](https://github.com/SuanmoSuanyangTechnology/MemoryBear) | +4 | 5367 |
| 120 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +4 | 962 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | +267 | 19400 |
| 2 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +215 | 38570 |
| 3 | [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | +170 | 19667 |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +137 | 29057 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +128 | 58383 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +114 | 33085 |
| 7 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +110 | 27571 |
| 8 | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | +106 | 22448 |
| 9 | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | +96 | 19672 |
| 10 | [block/buzz](https://github.com/block/buzz) | +89 | 31669 |
| 11 | [cloudflare/computer](https://github.com/cloudflare/computer) | +86 | 8850 |
| 12 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +85 | 26343 |
| 13 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +84 | 14586 |
| 14 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +83 | 23358 |
| 15 | [floci-io/floci](https://github.com/floci-io/floci) | +79 | 22895 |
| 16 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +78 | 34131 |
| 17 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +76 | 43906 |
| 18 | [basecamp/omarchy](https://github.com/basecamp/omarchy) | +75 | 36175 |
| 19 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +72 | 34047 |
| 20 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +69 | 25415 |
| 21 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +66 | 13890 |
| 22 | [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | +66 | 6909 |
| 23 | [brightdata/cli](https://github.com/brightdata/cli) | +66 | 6391 |
| 24 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +65 | 39078 |
| 25 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +65 | 12110 |
| 26 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +64 | 26063 |
| 27 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +64 | 17340 |
| 28 | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | +64 | 11504 |
| 29 | [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | +61 | 9440 |
| 30 | [vorssaintapp/vorssaint-utils](https://github.com/vorssaintapp/vorssaint-utils) | +58 | 14212 |
| 31 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +57 | 55019 |
| 32 | [pranshuparmar/witr](https://github.com/pranshuparmar/witr) | +57 | 21963 |
| 33 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +56 | 50697 |
| 34 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +53 | 34698 |
| 35 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +52 | 26917 |
| 36 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +52 | 28719 |
| 37 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +51 | 17124 |
| 38 | [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | +50 | 9398 |
| 39 | [yc-software/qm](https://github.com/yc-software/qm) | +49 | 14394 |
| 40 | [every-app/open-seo](https://github.com/every-app/open-seo) | +48 | 15734 |
| 41 | [blader/humanizer](https://github.com/blader/humanizer) | +48 | 39263 |
| 42 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +47 | 40692 |
| 43 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +47 | 6316 |
| 44 | [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | +47 | 7605 |
| 45 | [talivia-group/talivia](https://github.com/talivia-group/talivia) | +46 | 2032 |
| 46 | [AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) | +45 | 18166 |
| 47 | [google/skills](https://github.com/google/skills) | +44 | 19056 |
| 48 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | +41 | 10596 |
| 49 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +40 | 38146 |
| 50 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +40 | 38079 |
| 51 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +39 | 23319 |
| 52 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +39 | 64396 |
| 53 | [Zeejay0/gathered-scenes-zine-skill](https://github.com/Zeejay0/gathered-scenes-zine-skill) | +39 | 4650 |
| 54 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +38 | 12733 |
| 55 | [trycompai/crm](https://github.com/trycompai/crm) | +37 | 9166 |
| 56 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +37 | 35297 |
| 57 | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | +36 | 6591 |
| 58 | [sapientinc/PRAXIST](https://github.com/sapientinc/PRAXIST) | +35 | 5447 |
| 59 | [cactus-compute/needle](https://github.com/cactus-compute/needle) | +34 | 9882 |
| 60 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +33 | 21200 |
| 61 | [multica-ai/multica](https://github.com/multica-ai/multica) | +33 | 48414 |
| 62 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +33 | 11109 |
| 63 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +32 | 46331 |
| 64 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +32 | 13693 |
| 65 | [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | +32 | 22782 |
| 66 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +32 | 29594 |
| 67 | [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web) | +31 | 3326 |
| 68 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +31 | 5350 |
| 69 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +31 | 41516 |
| 70 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +31 | 26545 |
| 71 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +31 | 21723 |
| 72 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +31 | 15912 |
| 73 | [get-bb/bb](https://github.com/get-bb/bb) | +31 | 2821 |
| 74 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +30 | 14730 |
| 75 | [LaoFeng-mouse/flyingmouse-format](https://github.com/LaoFeng-mouse/flyingmouse-format) | +30 | 5106 |
| 76 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | +30 | 5168 |
| 77 | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | +29 | 3610 |
| 78 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +29 | 14492 |
| 79 | [openTrinity/mycontext](https://github.com/openTrinity/mycontext) | +29 | 3005 |
| 80 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +29 | 6909 |
| 81 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +29 | 5356 |
| 82 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +28 | 32182 |
| 83 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +28 | 16560 |
| 84 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +28 | 24933 |
| 85 | [holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS) | +27 | 11095 |
| 86 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +27 | 10923 |
| 87 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +26 | 31838 |
| 88 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +26 | 31046 |
| 89 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +25 | 7609 |
| 90 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +25 | 14586 |
| 91 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +24 | 14485 |
| 92 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | +24 | 32460 |
| 93 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +24 | 43387 |
| 94 | [jacubes/CVE-2026-24061](https://github.com/jacubes/CVE-2026-24061) | +24 | 824 |
| 95 | [cursor/plugins](https://github.com/cursor/plugins) | +23 | 6381 |
| 96 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +23 | 39994 |
| 97 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +23 | 22017 |
| 98 | [browser-use/video-use](https://github.com/browser-use/video-use) | +23 | 22364 |
| 99 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +23 | 33504 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +22 | 25315 |
| 101 | [arvin341az-glitch/RVG](https://github.com/arvin341az-glitch/RVG) | +21 | 3893 |
| 102 | [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin) | +21 | 5866 |
| 103 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +21 | 6556 |
| 104 | [Gaoshu705/QzoneArchive](https://github.com/Gaoshu705/QzoneArchive) | +20 | 2561 |
| 105 | [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox) | +20 | 2431 |
| 106 | [Tiger3807861189/J-Space-Cognition-Suite-V3.7](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.7) | +20 | 3010 |
| 107 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +20 | 12689 |
| 108 | [Dropnation/contract-fuzzer](https://github.com/Dropnation/contract-fuzzer) | +20 | 1413 |
| 109 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 15952 |
| 110 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +20 | 34741 |
| 111 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 7090 |
| 112 | [workweave/router](https://github.com/workweave/router) | +19 | 3327 |
| 113 | [Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli) | +19 | 10084 |
| 114 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +19 | 35734 |
| 115 | [General-Legal/legal-templates](https://github.com/General-Legal/legal-templates) | +19 | 1889 |
| 116 | [titanwings/distilly](https://github.com/titanwings/distilly) | +19 | 24208 |
| 117 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +19 | 9984 |
| 118 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +18 | 7176 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +18 | 48750 |
| 120 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 7513 |
| 121 | [securo-finance/securo](https://github.com/securo-finance/securo) | +16 | 2838 |
| 122 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +16 | 31793 |
| 123 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) | +16 | 2128 |
| 124 | [OStudi/short-video-generator-AI](https://github.com/OStudi/short-video-generator-AI) | +16 | 1228 |
| 125 | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | +16 | 688 |
| 126 | [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) | +16 | 2478 |
| 127 | [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | +16 | 3812 |
| 128 | [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) | +15 | 2980 |
| 129 | [llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier) | +15 | 3042 |
| 130 | [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) | +15 | 3490 |
| 131 | [tsingyuai/growth-lab](https://github.com/tsingyuai/growth-lab) | +15 | 1986 |
| 132 | [T8mars/comfyui-minimax-h3-audio-T8](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | +15 | 894 |
| 133 | [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | +15 | 2896 |
| 134 | [chuspeeism/dashi-taskboard](https://github.com/chuspeeism/dashi-taskboard) | +15 | 2828 |
| 135 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +14 | 44424 |
| 136 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +14 | 31022 |
| 137 | [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD) | +14 | 916 |
| 138 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 9559 |
| 139 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +14 | 9276 |
| 140 | [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | +14 | 3328 |
| 141 | [cinderline/northcinder](https://github.com/cinderline/northcinder) | +14 | 1218 |
| 142 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +14 | 10919 |
| 143 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +13 | 29635 |
| 144 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) | +13 | 1071 |
| 145 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +13 | 4035 |
| 146 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +13 | 5874 |
| 147 | [mnemosyne-oss/mnemosyne](https://github.com/mnemosyne-oss/mnemosyne) | +13 | 2938 |
| 148 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +13 | 9856 |
| 149 | [decolua/9router](https://github.com/decolua/9router) | +13 | 26805 |
| 150 | [duolahypercho/codex-router](https://github.com/duolahypercho/codex-router) | +13 | 2993 |
| 151 | [asuojun/claude-vision-skill](https://github.com/asuojun/claude-vision-skill) | +13 | 2247 |
| 152 | [0xwilliamortiz/claude-red](https://github.com/0xwilliamortiz/claude-red) | +13 | 0 |
| 153 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +12 | 5465 |
| 154 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +12 | 3977 |
| 155 | [MatrAIx-ai/MatrAIx-Persona-8B](https://github.com/MatrAIx-ai/MatrAIx-Persona-8B) | +12 | 1723 |
| 156 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +12 | 6279 |
| 157 | [Paritok-official/paritok-4b-v1](https://github.com/Paritok-official/paritok-4b-v1) | +12 | 1449 |
| 158 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +12 | 3753 |
| 159 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 28457 |
| 160 | [petergyang/human-review](https://github.com/petergyang/human-review) | +12 | 1201 |
| 161 | [Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) | +11 | 1000 |
| 162 | [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) | +11 | 6192 |
| 163 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +11 | 9274 |
| 164 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +11 | 14080 |
| 165 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +11 | 2697 |
| 166 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +11 | 8848 |
| 167 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +11 | 2036 |
| 168 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +10 | 45758 |
| 169 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | +10 | 14866 |
| 170 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +10 | 4844 |
| 171 | [ZimengXiong/tinyTouch](https://github.com/ZimengXiong/tinyTouch) | +10 | 1522 |
| 172 | [agentrhq/webcmd](https://github.com/agentrhq/webcmd) | +10 | 1554 |
| 173 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +10 | 32604 |
| 174 | [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner) | +9 | 4210 |
| 175 | [jundot/omlx](https://github.com/jundot/omlx) | +9 | 21160 |
| 176 | [henryqin1997/statem](https://github.com/henryqin1997/statem) | +9 | 796 |
| 177 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 11012 |
| 178 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +9 | 17938 |
| 179 | [anbeime/skill](https://github.com/anbeime/skill) | +9 | 5996 |
| 180 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +9 | 6565 |
| 181 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +9 | 9661 |
| 182 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +9 | 7295 |
| 183 | [stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck) | +9 | 3519 |
| 184 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +9 | 3887 |
| 185 | [memorax-ai/memorax-code](https://github.com/memorax-ai/memorax-code) | +9 | 1164 |
| 186 | [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) | +9 | 949 |
| 187 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 8958 |
| 188 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +8 | 2043 |
| 189 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 27748 |
| 190 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +7 | 0 |
| 191 | [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) | +7 | 3126 |
| 192 | [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) | +7 | 3043 |
| 193 | [syv-ai/qwen38-27b-rtx3090](https://github.com/syv-ai/qwen38-27b-rtx3090) | +7 | 962 |
| 194 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +7 | 17283 |
| 195 | [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | +7 | 1197 |
| 196 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +7 | 10004 |
| 197 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | +7 | 1279 |
| 198 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +7 | 1850 |
| 199 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +7 | 10395 |
| 200 | [ruudkoeyvoets/polymarket-trading-bot-twap](https://github.com/ruudkoeyvoets/polymarket-trading-bot-twap) | +7 | 0 |
| 201 | [diudiu-tech/delivery-harness](https://github.com/diudiu-tech/delivery-harness) | +7 | 892 |
| 202 | [x4gKing/3x-ui-multi](https://github.com/x4gKing/3x-ui-multi) | +6 | 0 |
| 203 | [zarazhangrui/youtube-digest](https://github.com/zarazhangrui/youtube-digest) | +6 | 1021 |
| 204 | [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | +6 | 971 |
| 205 | [amElnagdy/delegate-skills](https://github.com/amElnagdy/delegate-skills) | +6 | 1560 |
| 206 | [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | +6 | 1741 |
| 207 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +6 | 784 |
| 208 | [openai/plugins](https://github.com/openai/plugins) | +6 | 5307 |
| 209 | [StarKnightt/jungle-trail](https://github.com/StarKnightt/jungle-trail) | +6 | 287 |
| 210 | [pingmike2/freebuff2api-wokers](https://github.com/pingmike2/freebuff2api-wokers) | +6 | 364 |
| 211 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +6 | 2080 |
| 212 | [mindmuxai/brain.md](https://github.com/mindmuxai/brain.md) | +6 | 518 |
| 213 | [ZSvirt/zsvirt](https://github.com/ZSvirt/zsvirt) | +6 | 1516 |
| 214 | [yuanzhongqiao/printfilm](https://github.com/yuanzhongqiao/printfilm) | +6 | 3939 |
| 215 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +6 | 369 |
| 216 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +5 | 6288 |
| 217 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +5 | 1477 |
| 218 | [lklynet/aurral](https://github.com/lklynet/aurral) | +5 | 1604 |
| 219 | [zanwei/design-dna](https://github.com/zanwei/design-dna) | +5 | 1630 |
| 220 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +5 | 3177 |
| 221 | [achrefelouafi/LinearAbiltyCastingThreeJS](https://github.com/achrefelouafi/LinearAbiltyCastingThreeJS) | +5 | 819 |
| 222 | [agent-earth/deepseek-harness-desktop](https://github.com/agent-earth/deepseek-harness-desktop) | +5 | 188 |
| 223 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +5 | 7247 |
| 224 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +5 | 3742 |
| 225 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +5 | 0 |
| 226 | [mokshablr/gander](https://github.com/mokshablr/gander) | +5 | 873 |
| 227 | [x4gpanell/X4G](https://github.com/x4gpanell/X4G) | +4 | 641 |
| 228 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 1286 |
| 229 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +4 | 5935 |
| 230 | [boyang-hu/website-rebuild-skill](https://github.com/boyang-hu/website-rebuild-skill) | +4 | 546 |
| 231 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +4 | 3657 |
| 232 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +4 | 6438 |
| 233 | [davatron5000/microlighter](https://github.com/davatron5000/microlighter) | +4 | 702 |
| 234 | [deusyu/harness-engineering](https://github.com/deusyu/harness-engineering) | +4 | 5743 |
| 235 | [vlln/whale-girl](https://github.com/vlln/whale-girl) | +4 | 301 |
| 236 | [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) | +4 | 635 |
| 237 | [lyu0805/OpenBrowser](https://github.com/lyu0805/OpenBrowser) | +4 | 646 |
| 238 | [adrianpunk/Punk-Skill](https://github.com/adrianpunk/Punk-Skill) | +4 | 852 |
| 239 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +4 | 3252 |
| 240 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4 | 3186 |
| 241 | [Nystik-gh/ignis](https://github.com/Nystik-gh/ignis) | +4 | 1296 |
| 242 | [seesee75-commits/ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | +4 | 278 |
| 243 | [nkxx188/ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | +4 | 589 |
| 244 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +4 | 5227 |
| 245 | [zhukunpenglinyutong/jetbrains-cc-gui](https://github.com/zhukunpenglinyutong/jetbrains-cc-gui) | +4 | 5663 |
| 246 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 1308 |
| 247 | [albertoZurini/echo-dot-2-playground](https://github.com/albertoZurini/echo-dot-2-playground) | +4 | 171 |
| 248 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 3630 |
| 249 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +4 | 2201 |
| 250 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +4 | 1026 |
| 251 | [aozorae/Edgechat](https://github.com/aozorae/Edgechat) | +3 | 464 |
| 252 | [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) | +3 | 640 |
| 253 | [canivibecodeit/canivibecodeit](https://github.com/canivibecodeit/canivibecodeit) | +3 | 305 |
| 254 | [sam70361/emotion-ball](https://github.com/sam70361/emotion-ball) | +3 | 317 |
| 255 | [fxyadela/write-then-publish](https://github.com/fxyadela/write-then-publish) | +3 | 508 |
| 256 | [HaD0Yun/CozyClay](https://github.com/HaD0Yun/CozyClay) | +3 | 515 |
| 257 | [czm15053/linuxdo-idea-ui](https://github.com/czm15053/linuxdo-idea-ui) | +3 | 287 |
| 258 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +3 | 1471 |
| 259 | [akudamatata/iOS-Location-Spoofer-Web](https://github.com/akudamatata/iOS-Location-Spoofer-Web) | +3 | 146 |
| 260 | [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | +3 | 163 |
| 261 | [howmp/dsh-pentest](https://github.com/howmp/dsh-pentest) | +3 | 335 |
| 262 | [laogou717/md-wechat](https://github.com/laogou717/md-wechat) | +3 | 211 |
| 263 | [GamePhanesStudio/GamePhanes](https://github.com/GamePhanesStudio/GamePhanes) | +3 | 540 |
| 264 | [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) | +3 | 396 |
| 265 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +3 | 6035 |
| 266 | [p2r3/ha.mr](https://github.com/p2r3/ha.mr) | +3 | 920 |
| 267 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1306 |
| 268 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +3 | 3827 |
| 269 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +3 | 4928 |
| 270 | [lllucccian/Deekseep](https://github.com/lllucccian/Deekseep) | +3 | 264 |
| 271 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 1023 |
| 272 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +3 | 629 |
| 273 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +3 | 28874 |
| 274 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +3 | 31476 |
| 275 | [yan-labs/yan-skills](https://github.com/yan-labs/yan-skills) | +2 | 155 |
| 276 | [MartinDelophy/ai-video-editor](https://github.com/MartinDelophy/ai-video-editor) | +2 | 666 |
| 277 | [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) | +2 | 1811 |
| 278 | [silentchainai/SILENTCHAIN](https://github.com/silentchainai/SILENTCHAIN) | +2 | 450 |
| 279 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +2 | 5369 |
| 280 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 980 |
| 281 | [zerionproject/Zerion](https://github.com/zerionproject/Zerion) | +2 | 88 |
| 282 | [chitralabs/sheetz](https://github.com/chitralabs/sheetz) | +2 | 100 |
| 283 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 559 |
| 284 | [YesSteveModel/YesSteveModel](https://github.com/YesSteveModel/YesSteveModel) | +2 | 32 |
| 285 | [w1lli4m666-droid/TVFileBox](https://github.com/w1lli4m666-droid/TVFileBox) | +2 | 128 |
| 286 | [Xaaaa-bip/GodzillaSuper](https://github.com/Xaaaa-bip/GodzillaSuper) | +2 | 219 |
| 287 | [ModinMobileSTS/Sts2MobileLauncher](https://github.com/ModinMobileSTS/Sts2MobileLauncher) | +2 | 330 |
| 288 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +2 | 2584 |
| 289 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 1063 |
| 290 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +2 | 682 |
| 291 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +2 | 314 |
| 292 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +2 | 350 |
| 293 | [lxien/orbien](https://github.com/lxien/orbien) | +2 | 229 |
| 294 | [eddyizm/tempus](https://github.com/eddyizm/tempus) | +2 | 1256 |
| 295 | [ReSo7200/InstaEclipse](https://github.com/ReSo7200/InstaEclipse) | +2 | 1416 |
| 296 | [microsoft/Generative-AI-for-beginners-java](https://github.com/microsoft/Generative-AI-for-beginners-java) | +2 | 530 |
| 297 | [youdidking/stanngv2](https://github.com/youdidking/stanngv2) | +1 | 398 |
| 298 | [xingguangqwq/traceguard-vscode](https://github.com/xingguangqwq/traceguard-vscode) | +1 | 86 |
| 299 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 928 |
| 300 | [linzhi-524/linjian-peek-public](https://github.com/linzhi-524/linjian-peek-public) | +1 | 194 |
