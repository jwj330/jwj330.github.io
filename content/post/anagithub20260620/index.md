---
title: "2026-06-20 GitHub增长趋势报告"
description: "1.headroom+102 2.ponytail+56 3.codebase-memory-mcp+29 4.worldmonitor+17 5.Agent-Reach+15"
date: 2026-06-20T21:19:45+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-06-20 21:19:45

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
        'daily': {"categories": ["dnshe/DNSHE-FreeDomains", "CloakHQ/CloakBrowser", "zubair-trabzada/geo-seo-claude", "nashsu/llm_wiki", "rohitg00/ai-engineering-from-scratch", "Alishahryar1/free-claude-code", "blader/humanizer", "NVIDIA/SkillSpector", "tashfeenahmed/freellmapi", "modem-dev/hunk", "mvanhorn/last30days-skill", "calesthio/OpenMontage", "xrpcommunity/XRP-community-wallet", "yaojingang/yao-meta-skill", "Leonxlnx/taste-skill", "Panniantong/Agent-Reach", "koala73/worldmonitor", "DeusData/codebase-memory-mcp", "DietrichGebert/ponytail", "chopratejas/headroom"], "data": [6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 11, 11, 12, 13, 15, 17, 29, 56, 102]},
        'weekly': {"categories": ["Imbad0202/academic-research-skills", "tamnd/kage", "hugohe3/ppt-master", "chatwoot/chatwoot", "lfnovo/open-notebook", "google-research/timesfm", "rohitg00/ai-engineering-from-scratch", "XiaomiMiMo/MiMo-Code", "apple/container", "DeusData/codebase-memory-mcp", "colbymchenry/codegraph", "shadcn/improve", "GoogleCloudPlatform/knowledge-catalog", "mvanhorn/last30days-skill", "omnigent-ai/omnigent", "NVIDIA/SkillSpector", "Leonxlnx/taste-skill", "Panniantong/Agent-Reach", "chopratejas/headroom", "DietrichGebert/ponytail"], "data": [59, 66, 66, 71, 75, 79, 80, 95, 103, 109, 119, 122, 122, 125, 125, 135, 145, 279, 352, 888]},
        'monthly': {"categories": ["CloakHQ/CloakBrowser", "D4Vinci/Scrapling", "Panniantong/Agent-Reach", "tinyhumansai/openhuman", "addyosmani/agent-skills", "mvanhorn/last30days-skill", "anthropics/claude-plugins-official", "Imbad0202/academic-research-skills", "DietrichGebert/ponytail", "safishamsi/graphify", "harry0703/MoneyPrinterTurbo", "farion1231/cc-switch", "chopratejas/headroom", "Leonxlnx/taste-skill", "rohitg00/ai-engineering-from-scratch", "mattpocock/skills", "forrestchang/andrej-karpathy-skills", "pewdiepie-archdaemon/odysseus", "colbymchenry/codegraph", "Egonex-AI/Understand-Anything"], "data": [581, 591, 622, 670, 730, 837, 839, 912, 920, 942, 1053, 1204, 1253, 1265, 1627, 1769, 2374, 2525, 2748, 2974]}
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
| 1 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +102 | 41605 |
| 2 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +56 | 42900 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +29 | 9224 |
| 4 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +17 | 57647 |
| 5 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +15 | 35792 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +13 | 47694 |
| 7 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +12 | 1407 |
| 8 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +11 | 670 |
| 9 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 6958 |
| 10 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +9 | 45048 |
| 11 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +9 | 5213 |
| 12 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +8 | 11101 |
| 13 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +8 | 8638 |
| 14 | [blader/humanizer](https://github.com/blader/humanizer) | +8 | 25196 |
| 15 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +8 | 35879 |
| 16 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +7 | 35058 |
| 17 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +7 | 12217 |
| 18 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +7 | 8464 |
| 19 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +7 | 26701 |
| 20 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 3048 |
| 21 | [vercel/eve](https://github.com/vercel/eve) | +6 | 1845 |
| 22 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +6 | 4184 |
| 23 | [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB) | +5 | 2500 |
| 24 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +5 | 34306 |
| 25 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 13646 |
| 26 | [LearnPrompt/humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | +5 | 301 |
| 27 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +5 | 5431 |
| 28 | [microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach) | +5 | 2802 |
| 29 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +4 | 28375 |
| 30 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +4 | 4482 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +888 | 42900 |
| 2 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +352 | 41604 |
| 3 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +279 | 35792 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +145 | 47694 |
| 5 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +135 | 8638 |
| 6 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +125 | 4184 |
| 7 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +125 | 45048 |
| 8 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +122 | 4482 |
| 9 | [shadcn/improve](https://github.com/shadcn/improve) | +122 | 5765 |
| 10 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +119 | 52286 |
| 11 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +109 | 9224 |
| 12 | [apple/container](https://github.com/apple/container) | +103 | 39070 |
| 13 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +95 | 10069 |
| 14 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +80 | 35058 |
| 15 | [google-research/timesfm](https://github.com/google-research/timesfm) | +79 | 24484 |
| 16 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +75 | 32015 |
| 17 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | +71 | 32931 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +66 | 29623 |
| 19 | [tamnd/kage](https://github.com/tamnd/kage) | +66 | 2160 |
| 20 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +59 | 33092 |
| 21 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +58 | 31075 |
| 22 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +56 | 21530 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +54 | 39855 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +52 | 29061 |
| 25 | [tw93/Kami](https://github.com/tw93/Kami) | +51 | 8976 |
| 26 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +50 | 35879 |
| 27 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +49 | 32872 |
| 28 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +47 | 64158 |
| 29 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +47 | 13646 |
| 30 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +47 | 8045 |
| 31 | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | +44 | 23297 |
| 32 | [alibaba/zvec](https://github.com/alibaba/zvec) | +42 | 11815 |
| 33 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +41 | 43501 |
| 34 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +41 | 30784 |
| 35 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +41 | 12485 |
| 36 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +39 | 23160 |
| 37 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +38 | 4604 |
| 38 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +37 | 11101 |
| 39 | [blader/humanizer](https://github.com/blader/humanizer) | +37 | 25196 |
| 40 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +36 | 19631 |
| 41 | [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | +35 | 3030 |
| 42 | [vercel/eve](https://github.com/vercel/eve) | +34 | 1845 |
| 43 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +33 | 5431 |
| 44 | [getkimchi/kimchi](https://github.com/getkimchi/kimchi) | +33 | 1817 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +32 | 23571 |
| 46 | [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | +32 | 5010 |
| 47 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +32 | 26701 |
| 48 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +32 | 4272 |
| 49 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +31 | 9624 |
| 50 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +30 | 57647 |
| 51 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +30 | 34306 |
| 52 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +30 | 0 |
| 53 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +30 | 6729 |
| 54 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +29 | 32055 |
| 55 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +29 | 15594 |
| 56 | [loc567/loc567](https://github.com/loc567/loc567) | +29 | 1240 |
| 57 | [sleep3r/mtproto.zig](https://github.com/sleep3r/mtproto.zig) | +29 | 1024 |
| 58 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +28 | 4252 |
| 59 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +28 | 1192 |
| 60 | [telemt/telemt](https://github.com/telemt/telemt) | +28 | 5302 |
| 61 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +27 | 16769 |
| 62 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +26 | 6958 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +26 | 21496 |
| 64 | [zai-org/GLM-5](https://github.com/zai-org/GLM-5) | +25 | 4798 |
| 65 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +25 | 12765 |
| 66 | [stablyai/orca](https://github.com/stablyai/orca) | +25 | 5654 |
| 67 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +25 | 23537 |
| 68 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +25 | 22345 |
| 69 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +24 | 25259 |
| 70 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +24 | 19298 |
| 71 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +24 | 58412 |
| 72 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +24 | 29215 |
| 73 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +24 | 32719 |
| 74 | [SkyBlue997/enableMacosAI](https://github.com/SkyBlue997/enableMacosAI) | +24 | 1456 |
| 75 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +23 | 25065 |
| 76 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +23 | 6496 |
| 77 | [levy-street/world-of-claudecraft](https://github.com/levy-street/world-of-claudecraft) | +23 | 1049 |
| 78 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +23 | 851 |
| 79 | [withastro/flue](https://github.com/withastro/flue) | +22 | 6060 |
| 80 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +22 | 17031 |
| 81 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +22 | 22068 |
| 82 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +22 | 28518 |
| 83 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +22 | 43518 |
| 84 | [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | +22 | 2327 |
| 85 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +21 | 12217 |
| 86 | [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | +21 | 2046 |
| 87 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +20 | 18172 |
| 88 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +20 | 21814 |
| 89 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +20 | 31380 |
| 90 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +20 | 5837 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +20 | 41230 |
| 92 | [xrpcommunity/XRP-community-wallet](https://github.com/xrpcommunity/XRP-community-wallet) | +19 | 670 |
| 93 | [VitoHowe/glm-coding](https://github.com/VitoHowe/glm-coding) | +19 | 524 |
| 94 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +19 | 37963 |
| 95 | [alchaincyf/loop-engineering-orange-book](https://github.com/alchaincyf/loop-engineering-orange-book) | +19 | 716 |
| 96 | [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) | +18 | 1407 |
| 97 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +18 | 30961 |
| 98 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +18 | 23022 |
| 99 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +18 | 2196 |
| 100 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +18 | 7193 |
| 101 | [shuvonsec/claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty) | +18 | 3452 |
| 102 | [multica-ai/multica](https://github.com/multica-ai/multica) | +17 | 37288 |
| 103 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +17 | 28856 |
| 104 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +17 | 2593 |
| 105 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +16 | 1225 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +16 | 30496 |
| 107 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +15 | 3241 |
| 108 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +15 | 4455 |
| 109 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +15 | 8127 |
| 110 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +15 | 37685 |
| 111 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +15 | 16666 |
| 112 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +15 | 3006 |
| 113 | [LycheeMem/LycheeMem](https://github.com/LycheeMem/LycheeMem) | +15 | 726 |
| 114 | [WeiboAI/VibeThinker](https://github.com/WeiboAI/VibeThinker) | +14 | 1152 |
| 115 | [kairos-agi/kairos-sensenova](https://github.com/kairos-agi/kairos-sensenova) | +14 | 817 |
| 116 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +14 | 7775 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +14 | 16725 |
| 118 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +14 | 14774 |
| 119 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +14 | 3632 |
| 120 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +13 | 1437 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +2974 | 64534 |
| 2 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | +2748 | 52286 |
| 3 | [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | +2525 | 74996 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +2374 | 179193 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1769 | 138088 |
| 6 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +1627 | 35058 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1265 | 47694 |
| 8 | [chopratejas/headroom](https://github.com/chopratejas/headroom) | +1253 | 41604 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +1204 | 105179 |
| 10 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +1053 | 49621 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +942 | 69876 |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +920 | 42901 |
| 13 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +912 | 33092 |
| 14 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +839 | 30496 |
| 15 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +837 | 45048 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +730 | 64095 |
| 17 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +670 | 32719 |
| 18 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +622 | 35792 |
| 19 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +591 | 65175 |
| 20 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +581 | 26701 |
| 21 | [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | +546 | 12010 |
| 22 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +524 | 21496 |
| 23 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +520 | 17031 |
| 24 | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | +513 | 23537 |
| 25 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +496 | 21530 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +490 | 64158 |
| 27 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +482 | 35879 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +478 | 11101 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +469 | 29623 |
| 30 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +459 | 13646 |
| 31 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +420 | 39855 |
| 32 | [multica-ai/multica](https://github.com/multica-ai/multica) | +420 | 37288 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +411 | 29061 |
| 34 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +406 | 31075 |
| 35 | [unicity-astrid/astrid](https://github.com/unicity-astrid/astrid) | +396 | 9351 |
| 36 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +390 | 8045 |
| 37 | [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | +388 | 32015 |
| 38 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | +386 | 4555 |
| 39 | [apple/container](https://github.com/apple/container) | +379 | 39070 |
| 40 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +376 | 27182 |
| 41 | [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) | +350 | 38748 |
| 42 | [unicity-astrid/sdk-js](https://github.com/unicity-astrid/sdk-js) | +346 | 8255 |
| 43 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +344 | 22525 |
| 44 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +343 | 10069 |
| 45 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +304 | 32055 |
| 46 | [simplifaisoul/osiris](https://github.com/simplifaisoul/osiris) | +304 | 5837 |
| 47 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +303 | 14774 |
| 48 | [roboflow/supervision](https://github.com/roboflow/supervision) | +302 | 36553 |
| 49 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +297 | 28518 |
| 50 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +293 | 23571 |
| 51 | [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | +288 | 12477 |
| 52 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +288 | 43518 |
| 53 | [decolua/9router](https://github.com/decolua/9router) | +278 | 18088 |
| 54 | [HKUDS/ViMax](https://github.com/HKUDS/ViMax) | +277 | 10470 |
| 55 | [KunAgent/Kun](https://github.com/KunAgent/Kun) | +272 | 4604 |
| 56 | [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | +269 | 21601 |
| 57 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +259 | 16769 |
| 58 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +259 | 18172 |
| 59 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +258 | 8638 |
| 60 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | +256 | 9609 |
| 61 | [supertone-inc/supertonic](https://github.com/supertone-inc/supertonic) | +251 | 12485 |
| 62 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +251 | 44068 |
| 63 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +249 | 23160 |
| 64 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +232 | 30784 |
| 65 | [blader/humanizer](https://github.com/blader/humanizer) | +231 | 25196 |
| 66 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +230 | 43501 |
| 67 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +230 | 39447 |
| 68 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +228 | 12765 |
| 69 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +228 | 19298 |
| 70 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +224 | 25065 |
| 71 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +223 | 13971 |
| 72 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +222 | 17146 |
| 73 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | +219 | 35336 |
| 74 | [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA) | +217 | 9624 |
| 75 | [unicity-astrid/sdk-rust](https://github.com/unicity-astrid/sdk-rust) | +215 | 4347 |
| 76 | [unicity-sphere/sphere-sdk](https://github.com/unicity-sphere/sphere-sdk) | +215 | 5447 |
| 77 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +214 | 30961 |
| 78 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +212 | 3958 |
| 79 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +210 | 34306 |
| 80 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +209 | 28856 |
| 81 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +204 | 5278 |
| 82 | [FoundZiGu/GuJumpgate](https://github.com/FoundZiGu/GuJumpgate) | +202 | 3918 |
| 83 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +201 | 37963 |
| 84 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +201 | 4600 |
| 85 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +200 | 31380 |
| 86 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +199 | 58412 |
| 87 | [st-tech/ppf-contact-solver](https://github.com/st-tech/ppf-contact-solver) | +198 | 4083 |
| 88 | [88lin/video_vip](https://github.com/88lin/video_vip) | +197 | 4165 |
| 89 | [google/skills](https://github.com/google/skills) | +194 | 13980 |
| 90 | [shadcn/improve](https://github.com/shadcn/improve) | +188 | 5765 |
| 91 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +188 | 6496 |
| 92 | [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck) | +187 | 4272 |
| 93 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +186 | 31098 |
| 94 | [wiltodelta/remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | +185 | 3480 |
| 95 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +185 | 20200 |
| 96 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | +184 | 2593 |
| 97 | [microsoft/Webwright](https://github.com/microsoft/Webwright) | +183 | 5522 |
| 98 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +182 | 15594 |
| 99 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +181 | 22345 |
| 100 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +179 | 6705 |
| 101 | [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | +178 | 21814 |
| 102 | [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | +175 | 11676 |
| 103 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +173 | 5431 |
| 104 | [zgwl/chinese-buy-us-stock-guide](https://github.com/zgwl/chinese-buy-us-stock-guide) | +173 | 4754 |
| 105 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +173 | 4455 |
| 106 | [Axorax/awesome-free-apps](https://github.com/Axorax/awesome-free-apps) | +168 | 6642 |
| 107 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +167 | 9224 |
| 108 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +166 | 7332 |
| 109 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +166 | 16666 |
| 110 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +165 | 25544 |
| 111 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +162 | 37685 |
| 112 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +159 | 6729 |
| 113 | [openai/skills](https://github.com/openai/skills) | +158 | 22596 |
| 114 | [soxoj/maigret](https://github.com/soxoj/maigret) | +158 | 33386 |
| 115 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +155 | 25259 |
| 116 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +152 | 3494 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +151 | 16725 |
| 118 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +149 | 41230 |
| 119 | [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | +148 | 3357 |
| 120 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +148 | 7746 |
| 121 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +147 | 3488 |
| 122 | [FareedKhan-dev/train-llm-from-scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) | +146 | 7063 |
| 123 | [alistaitsacle/free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | +143 | 2613 |
| 124 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +133 | 4482 |
| 125 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +133 | 35295 |
| 126 | [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) | +132 | 4581 |
| 127 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +131 | 32872 |
| 128 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +129 | 4328 |
| 129 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +127 | 4184 |
| 130 | [Tong89/smartNode](https://github.com/Tong89/smartNode) | +126 | 1985 |
| 131 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +125 | 49508 |
| 132 | [next-1688/1688-shopkeeper](https://github.com/next-1688/1688-shopkeeper) | +122 | 2951 |
| 133 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | +121 | 4427 |
| 134 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +121 | 23708 |
| 135 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +121 | 46917 |
| 136 | [MinishLab/semble](https://github.com/MinishLab/semble) | +120 | 5324 |
| 137 | [google-research/timesfm](https://github.com/google-research/timesfm) | +117 | 24485 |
| 138 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +114 | 18619 |
| 139 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +114 | 24837 |
| 140 | [Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm) | +113 | 5034 |
| 141 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +113 | 8127 |
| 142 | [jundot/omlx](https://github.com/jundot/omlx) | +113 | 16889 |
| 143 | [openai/plugins](https://github.com/openai/plugins) | +109 | 3267 |
| 144 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +105 | 9348 |
| 145 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +104 | 8321 |
| 146 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +102 | 12391 |
| 147 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +102 | 35340 |
| 148 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +101 | 25484 |
| 149 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +100 | 7010 |
| 150 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +97 | 3287 |
| 151 | [Stremio/stremio-web](https://github.com/Stremio/stremio-web) | +96 | 12158 |
| 152 | [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) | +95 | 16843 |
| 153 | [browser-use/video-use](https://github.com/browser-use/video-use) | +93 | 9963 |
| 154 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +93 | 5054 |
| 155 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +93 | 2462 |
| 156 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +92 | 11438 |
| 157 | [floci-io/floci](https://github.com/floci-io/floci) | +92 | 14318 |
| 158 | [steipete/agent-scripts](https://github.com/steipete/agent-scripts) | +90 | 5112 |
| 159 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | +88 | 4512 |
| 160 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +87 | 6923 |
| 161 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +87 | 18726 |
| 162 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +87 | 21352 |
| 163 | [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | +86 | 19900 |
| 164 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +85 | 23668 |
| 165 | [juanjuandog/FinSight-AI](https://github.com/juanjuandog/FinSight-AI) | +85 | 1104 |
| 166 | [facebookresearch/vggt-omega](https://github.com/facebookresearch/vggt-omega) | +84 | 3112 |
| 167 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +83 | 4110 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +82 | 7264 |
| 169 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +81 | 24865 |
| 170 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +81 | 7193 |
| 171 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +79 | 15153 |
| 172 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +78 | 25851 |
| 173 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +78 | 27430 |
| 174 | [maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed) | +77 | 3632 |
| 175 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +77 | 18599 |
| 176 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +76 | 44483 |
| 177 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +76 | 1907 |
| 178 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +75 | 19631 |
| 179 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +75 | 29629 |
| 180 | [jd-opensource/JoyAI-Echo](https://github.com/jd-opensource/JoyAI-Echo) | +74 | 1614 |
| 181 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +74 | 16091 |
| 182 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +73 | 4252 |
| 183 | [browser-act/skills](https://github.com/browser-act/skills) | +73 | 2754 |
| 184 | [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | +70 | 2153 |
| 185 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +68 | 28742 |
| 186 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +66 | 5781 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +65 | 36103 |
| 188 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +64 | 3241 |
| 189 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +62 | 3141 |
| 190 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +62 | 4561 |
| 191 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +61 | 6958 |
| 192 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +61 | 37564 |
| 193 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +60 | 3006 |
| 194 | [QuantFunc/ComfyUI-QuantFunc](https://github.com/QuantFunc/ComfyUI-QuantFunc) | +59 | 0 |
| 195 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +59 | 8721 |
| 196 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +59 | 28149 |
| 197 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +58 | 16932 |
| 198 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +57 | 2784 |
| 199 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +57 | 1296 |
| 200 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +55 | 5199 |
| 201 | [thcp/stemdeck](https://github.com/thcp/stemdeck) | +49 | 1717 |
| 202 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +49 | 4903 |
| 203 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint) | +48 | 1124 |
| 204 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +47 | 1631 |
| 205 | [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | +46 | 520 |
| 206 | [eze-is/web-access](https://github.com/eze-is/web-access) | +45 | 7754 |
| 207 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +41 | 8183 |
| 208 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +41 | 5756 |
| 209 | [wdcpclover/ai4paper](https://github.com/wdcpclover/ai4paper) | +39 | 1748 |
| 210 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +38 | 11253 |
| 211 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +38 | 5325 |
| 212 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +36 | 639 |
| 213 | [Haleclipse/CodexDesktop-Rebuild](https://github.com/Haleclipse/CodexDesktop-Rebuild) | +34 | 2365 |
| 214 | [pguso/ai-agents-from-scratch](https://github.com/pguso/ai-agents-from-scratch) | +34 | 4288 |
| 215 | [WhatDreamsCost/WhatDreamsCost-ComfyUI](https://github.com/WhatDreamsCost/WhatDreamsCost-ComfyUI) | +34 | 1287 |
| 216 | [tejaswigowda/ffmpeg-webCLI](https://github.com/tejaswigowda/ffmpeg-webCLI) | +33 | 793 |
| 217 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +33 | 3949 |
| 218 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +32 | 9432 |
| 219 | [Lucas0623z/NoteLite](https://github.com/Lucas0623z/NoteLite) | +32 | 855 |
| 220 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +29 | 1155 |
| 221 | [Nieobie/Game-Icon-Pack](https://github.com/Nieobie/Game-Icon-Pack) | +29 | 507 |
| 222 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +29 | 2808 |
| 223 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +28 | 3784 |
| 224 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +27 | 943 |
| 225 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +26 | 1936 |
| 226 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +26 | 2828 |
| 227 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +26 | 2301 |
| 228 | [ulsklyc/oikos](https://github.com/ulsklyc/oikos) | +25 | 797 |
| 229 | [sandeco/reversa](https://github.com/sandeco/reversa) | +24 | 1242 |
| 230 | [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | +24 | 205 |
| 231 | [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | +23 | 3306 |
| 232 | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | +23 | 5111 |
| 233 | [robinebers/openusage](https://github.com/robinebers/openusage) | +23 | 2919 |
| 234 | [BeamChunin42/jennymod-installer](https://github.com/BeamChunin42/jennymod-installer) | +23 | 27 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +21 | 13773 |
| 236 | [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) | +20 | 526 |
| 237 | [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | +20 | 954 |
| 238 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +20 | 1981 |
| 239 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +20 | 1912 |
| 240 | [justlovemaki/AIClient2API](https://github.com/justlovemaki/AIClient2API) | +20 | 8263 |
| 241 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +20 | 844 |
| 242 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +20 | 4493 |
| 243 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +20 | 1708 |
| 244 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +19 | 463 |
| 245 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +19 | 4515 |
| 246 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +19 | 12135 |
| 247 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +19 | 2206 |
| 248 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +19 | 2604 |
| 249 | [a5c-ai/babysitter](https://github.com/a5c-ai/babysitter) | +18 | 1377 |
| 250 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +18 | 10271 |
| 251 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +18 | 2531 |
| 252 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +17 | 2121 |
| 253 | [Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) | +17 | 2040 |
| 254 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +16 | 2688 |
| 255 | [cupidbity/cupid-music-player](https://github.com/cupidbity/cupid-music-player) | +16 | 378 |
| 256 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +16 | 433 |
| 257 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +15 | 183 |
| 258 | [royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram) | +15 | 492 |
| 259 | [xiaoyuanda666-ship-it/BaiLongma](https://github.com/xiaoyuanda666-ship-it/BaiLongma) | +15 | 369 |
| 260 | [himself65/finance-skills](https://github.com/himself65/finance-skills) | +15 | 2854 |
| 261 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +15 | 685 |
| 262 | [Gezine/Y2JB](https://github.com/Gezine/Y2JB) | +15 | 1157 |
| 263 | [openmemind/memind](https://github.com/openmemind/memind) | +15 | 903 |
| 264 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +14 | 736 |
| 265 | [soaring-xiongkulu/easyaiot](https://github.com/soaring-xiongkulu/easyaiot) | +14 | 561 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +14 | 2582 |
| 267 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +13 | 384 |
| 268 | [AbhishekSuresh2/Phoenix-MD-Bot](https://github.com/AbhishekSuresh2/Phoenix-MD-Bot) | +12 | 349 |
| 269 | [rotejin/tomari-guruguru](https://github.com/rotejin/tomari-guruguru) | +12 | 287 |
| 270 | [buynao/aipath](https://github.com/buynao/aipath) | +12 | 336 |
| 271 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +11 | 3474 |
| 272 | [oxylabs/chatgpt-scraper](https://github.com/oxylabs/chatgpt-scraper) | +11 | 3023 |
| 273 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +11 | 314 |
| 274 | [microsoft/copilot-for-eclipse](https://github.com/microsoft/copilot-for-eclipse) | +11 | 115 |
| 275 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +10 | 1185 |
| 276 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +10 | 2597 |
| 277 | [OtterMind/Nubase](https://github.com/OtterMind/Nubase) | +10 | 347 |
| 278 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +10 | 644 |
| 279 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +10 | 1671 |
| 280 | [DevYangJC/Argus](https://github.com/DevYangJC/Argus) | +10 | 271 |
| 281 | [ClouGence/open-cdm](https://github.com/ClouGence/open-cdm) | +10 | 294 |
| 282 | [anurag3407/career-pilot](https://github.com/anurag3407/career-pilot) | +9 | 120 |
| 283 | [Premshaw23/Learnova](https://github.com/Premshaw23/Learnova) | +9 | 110 |
| 284 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +9 | 2493 |
| 285 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +8 | 1629 |
| 286 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +8 | 245 |
| 287 | [cha0upup/LeoAI](https://github.com/cha0upup/LeoAI) | +7 | 149 |
| 288 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +7 | 897 |
| 289 | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | +7 | 67 |
| 290 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +6 | 757 |
| 291 | [worenbudaoni/rag-study-helper](https://github.com/worenbudaoni/rag-study-helper) | +6 | 164 |
| 292 | [tmseidel/ai-git-bot](https://github.com/tmseidel/ai-git-bot) | +6 | 101 |
| 293 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +6 | 503 |
| 294 | [jdubois/boot-ui](https://github.com/jdubois/boot-ui) | +6 | 162 |
| 295 | [mubashardev/WaEnhancer](https://github.com/mubashardev/WaEnhancer) | +6 | 230 |
| 296 | [paohaijiao/jquick-java](https://github.com/paohaijiao/jquick-java) | +6 | 460 |
| 297 | [eooce/NanoLimbo](https://github.com/eooce/NanoLimbo) | +5 | 213 |
| 298 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +5 | 3522 |
| 299 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +5 | 2143 |
| 300 | [structurizr/structurizr](https://github.com/structurizr/structurizr) | +5 | 258 |
