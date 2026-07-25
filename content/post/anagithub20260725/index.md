---
title: "2026-07-25 GitHub增长趋势报告"
description: "1.buzz+12 2.ego-lite+9 3.OmniRoute+6 4.ai-job-search+5 5.iFixAi+4"
date: 2026-07-25T20:54:56+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-25 20:54:56

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
        'daily': {"categories": ["1jehuang/jcode", "jgravelle/jcodemunch-mcp", "alibaba/open-code-review", "Galaxy-Dawn/claude-scholar", "humanlayer/advanced-context-engineering-for-coding-agents", "coreyhaines31/marketingskills", "lidge-jun/opencodex", "ogulcancelik/herdr", "BigPizzaV3/CodexPlusPlus", "iOfficeAI/OfficeCLI", "Vincentwei1021/video-shotcraft", "oblien/openship", "stablyai/orca", "calesthio/OpenMontage", "img2threejs/img2threejs", "ifixai-ai/iFixAi", "MadsLorentzen/ai-job-search", "diegosouzapw/OmniRoute", "citrolabs/ego-lite", "block/buzz"], "data": [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 9, 12]},
        'weekly': {"categories": ["JustVugg/colibri", "iOfficeAI/OfficeCLI", "calesthio/OpenMontage", "MoonshotAI/kimi-cli", "HKUDS/Vibe-Trading", "usestrix/strix", "lidge-jun/opencodex", "citrolabs/ego-lite", "img2threejs/img2threejs", "ogulcancelik/herdr", "jamiepine/voicebox", "Fei-Away/Codex-Dream-Skin", "tirth8205/code-review-graph", "rohitg00/ai-engineering-from-scratch", "baidu/Unlimited-OCR", "MadsLorentzen/ai-job-search", "stablyai/orca", "block/buzz", "oblien/openship", "diegosouzapw/OmniRoute"], "data": [13, 13, 13, 14, 14, 14, 14, 14, 15, 16, 16, 17, 19, 19, 22, 25, 27, 35, 42, 45]},
        'monthly': {"categories": ["alibaba/page-agent", "hugohe3/ppt-master", "HKUDS/Vibe-Trading", "Zackriya-Solutions/meetily", "facebook/astryx", "ZhuLinsen/daily_stock_analysis", "simplex-chat/simplex-chat", "JCodesMore/ai-website-cloner-template", "diegosouzapw/OmniRoute", "baidu/Unlimited-OCR", "MadsLorentzen/ai-job-search", "ogulcancelik/herdr", "XxHuberrr/Mineradio", "stablyai/orca", "xbtlin/ai-berkshire", "langchain-ai/openwiki", "google-labs-code/design.md", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [132, 137, 138, 145, 145, 145, 147, 149, 152, 154, 160, 169, 172, 172, 182, 188, 190, 258, 291, 331]}
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
| 1 | [block/buzz](https://github.com/block/buzz) | +12 | 11696 |
| 2 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +9 | 3453 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +6 | 29896 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +5 | 26765 |
| 5 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 2791 |
| 6 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +4 | 4632 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +4 | 42220 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 28951 |
| 9 | [oblien/openship](https://github.com/oblien/openship) | +4 | 8475 |
| 10 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +3 | 1722 |
| 11 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +3 | 22119 |
| 12 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +3 | 26610 |
| 13 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 20733 |
| 14 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +3 | 4782 |
| 15 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 41665 |
| 16 | [humanlayer/advanced-context-engineering-for-coding-agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | +2 | 1988 |
| 17 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +2 | 4816 |
| 18 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +2 | 12856 |
| 19 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +2 | 2194 |
| 20 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 11425 |
| 21 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +2 | 26382 |
| 22 | [NeuroAIHub/BrainPilot](https://github.com/NeuroAIHub/BrainPilot) | +2 | 106 |
| 23 | [ShouqiaoW/erdos](https://github.com/ShouqiaoW/erdos) | +2 | 189 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2 | 50071 |
| 25 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +2 | 7768 |
| 26 | [itayinbarr/little-coder](https://github.com/itayinbarr/little-coder) | +2 | 1936 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +2 | 18958 |
| 28 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +2 | 14995 |
| 29 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +2 | 4968 |
| 30 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 46053 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +45 | 29896 |
| 2 | [oblien/openship](https://github.com/oblien/openship) | +42 | 8475 |
| 3 | [block/buzz](https://github.com/block/buzz) | +35 | 11696 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 28951 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +25 | 26765 |
| 6 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +22 | 18958 |
| 7 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +19 | 43453 |
| 8 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +19 | 26382 |
| 9 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +17 | 12296 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +16 | 46701 |
| 11 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +16 | 20733 |
| 12 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +15 | 4632 |
| 13 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +14 | 3453 |
| 14 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +14 | 4782 |
| 15 | [usestrix/strix](https://github.com/usestrix/strix) | +14 | 44183 |
| 16 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +14 | 27542 |
| 17 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +14 | 10829 |
| 18 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +13 | 42220 |
| 19 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +13 | 22119 |
| 20 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +13 | 18987 |
| 21 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +13 | 6413 |
| 22 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +12 | 11425 |
| 23 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +11 | 50071 |
| 24 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +10 | 6337 |
| 25 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +10 | 14995 |
| 26 | [penecho/penecho](https://github.com/penecho/penecho) | +10 | 1592 |
| 27 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +10 | 4556 |
| 28 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +9 | 35299 |
| 29 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +9 | 20796 |
| 30 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +9 | 1628 |
| 31 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4885 |
| 32 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +8 | 1722 |
| 33 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 41665 |
| 34 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +8 | 10043 |
| 35 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +8 | 19721 |
| 36 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +8 | 29754 |
| 37 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +8 | 2207 |
| 38 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +8 | 15399 |
| 39 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +7 | 30188 |
| 40 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +7 | 7285 |
| 41 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 7917 |
| 42 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +7 | 16888 |
| 43 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +7 | 5044 |
| 44 | [stupside/castor](https://github.com/stupside/castor) | +7 | 1910 |
| 45 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +6 | 6687 |
| 46 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +6 | 12856 |
| 47 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42021 |
| 48 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 2791 |
| 49 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +6 | 39487 |
| 50 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +6 | 1069 |
| 51 | [agegr/pi-web](https://github.com/agegr/pi-web) | +6 | 2730 |
| 52 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +6 | 8019 |
| 53 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 7413 |
| 54 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 12329 |
| 55 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +6 | 1571 |
| 56 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6014 |
| 57 | [browser-use/video-use](https://github.com/browser-use/video-use) | +5 | 17805 |
| 58 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +5 | 4968 |
| 59 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +5 | 2973 |
| 60 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 7768 |
| 61 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +5 | 12599 |
| 62 | [nyblnet/bento](https://github.com/nyblnet/bento) | +5 | 1685 |
| 63 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 26610 |
| 64 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 10710 |
| 65 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +5 | 3288 |
| 66 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 46053 |
| 67 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 41073 |
| 68 | [kurikomi-labs/komi-store](https://github.com/kurikomi-labs/komi-store) | +5 | 16990 |
| 69 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 27774 |
| 70 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 31136 |
| 71 | [Julian-adv/OpenMMO](https://github.com/Julian-adv/OpenMMO) | +5 | 1404 |
| 72 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5 | 37612 |
| 73 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 10373 |
| 74 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +5 | 6382 |
| 75 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +5 | 9379 |
| 76 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +5 | 7897 |
| 77 | [tw93/Waza](https://github.com/tw93/Waza) | +5 | 6629 |
| 78 | [floci-io/floci](https://github.com/floci-io/floci) | +4 | 17335 |
| 79 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 42273 |
| 80 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4 | 44647 |
| 81 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 4706 |
| 82 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +4 | 12443 |
| 83 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +4 | 125 |
| 84 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +4 | 4305 |
| 85 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +4 | 19735 |
| 86 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +4 | 30851 |
| 87 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +4 | 23384 |
| 88 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 31013 |
| 89 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 3900 |
| 90 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +4 | 2295 |
| 91 | [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | +4 | 883 |
| 92 | [butterbase-ai/butterbase](https://github.com/butterbase-ai/butterbase) | +4 | 2783 |
| 93 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +4 | 4227 |
| 94 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +4 | 2510 |
| 95 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +4 | 519 |
| 96 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2167 |
| 97 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 58792 |
| 98 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +3 | 7075 |
| 99 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +3 | 12164 |
| 100 | [mesamirh/MovieBox-Tui](https://github.com/mesamirh/MovieBox-Tui) | +3 | 719 |
| 101 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +3 | 34205 |
| 102 | [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | +3 | 3828 |
| 103 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +3 | 8457 |
| 104 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +3 | 26284 |
| 105 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 4781 |
| 106 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4816 |
| 107 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +3 | 1628 |
| 108 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +3 | 13853 |
| 109 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +3 | 430 |
| 110 | [apache/ossie](https://github.com/apache/ossie) | +3 | 1629 |
| 111 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +3 | 34201 |
| 112 | [Qualcomm-AI-research/MobileWan](https://github.com/Qualcomm-AI-research/MobileWan) | +3 | 78 |
| 113 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +3 | 1090 |
| 114 | [openai/skills](https://github.com/openai/skills) | +3 | 24172 |
| 115 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +3 | 26551 |
| 116 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +3 | 4133 |
| 117 | [google-research/tabfm](https://github.com/google-research/tabfm) | +3 | 2091 |
| 118 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +3 | 1178 |
| 119 | [xiejunjie524/handdraw-story-video](https://github.com/xiejunjie524/handdraw-story-video) | +3 | 660 |
| 120 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +3 | 240 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +331 | 42221 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +291 | 35299 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +258 | 44183 |
| 4 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +190 | 26379 |
| 5 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 13227 |
| 6 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +182 | 14040 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +172 | 28952 |
| 8 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +172 | 8914 |
| 9 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +169 | 20733 |
| 10 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +160 | 26765 |
| 11 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +154 | 18958 |
| 12 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +152 | 29896 |
| 13 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +149 | 30188 |
| 14 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +147 | 19034 |
| 15 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +145 | 58792 |
| 16 | [facebook/astryx](https://github.com/facebook/astryx) | +145 | 10710 |
| 17 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +145 | 26622 |
| 18 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +138 | 27542 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +137 | 41073 |
| 20 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +132 | 27814 |
| 21 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +130 | 46701 |
| 22 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +127 | 29923 |
| 23 | [erincatto/box3d](https://github.com/erincatto/box3d) | +126 | 5544 |
| 24 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +122 | 16888 |
| 25 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +121 | 29317 |
| 26 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +119 | 9389 |
| 27 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +106 | 4096 |
| 28 | [apple/container](https://github.com/apple/container) | +94 | 48273 |
| 29 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +93 | 6337 |
| 30 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +88 | 26551 |
| 31 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +84 | 18987 |
| 32 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 17805 |
| 33 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +83 | 11914 |
| 34 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +81 | 10622 |
| 35 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6768 |
| 36 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +80 | 20796 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +78 | 50071 |
| 38 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6702 |
| 39 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +77 | 31136 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +76 | 6382 |
| 41 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +74 | 16986 |
| 42 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +70 | 15399 |
| 43 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +69 | 22119 |
| 44 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +68 | 7075 |
| 45 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +66 | 10043 |
| 46 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +66 | 37612 |
| 47 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +66 | 39487 |
| 48 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +65 | 8831 |
| 49 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +64 | 4968 |
| 50 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +62 | 7285 |
| 51 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +61 | 12296 |
| 52 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +59 | 42273 |
| 53 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +59 | 26610 |
| 54 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +55 | 24728 |
| 55 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +54 | 14996 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +53 | 41665 |
| 57 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +53 | 47589 |
| 58 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +52 | 43453 |
| 59 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5183 |
| 60 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +50 | 13739 |
| 61 | [baairon/torlink](https://github.com/baairon/torlink) | +49 | 3828 |
| 62 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +48 | 19721 |
| 63 | [antirez/ds4](https://github.com/antirez/ds4) | +48 | 19215 |
| 64 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +48 | 11528 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +47 | 42021 |
| 66 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +47 | 7413 |
| 67 | [every-app/open-seo](https://github.com/every-app/open-seo) | +47 | 7917 |
| 68 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +46 | 27774 |
| 69 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +46 | 3848 |
| 70 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +45 | 6548 |
| 71 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +44 | 23468 |
| 72 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9788 |
| 73 | [EpicGames/lore](https://github.com/EpicGames/lore) | +44 | 8190 |
| 74 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 2091 |
| 75 | [oblien/openship](https://github.com/oblien/openship) | +42 | 8475 |
| 76 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +42 | 34205 |
| 77 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +42 | 26328 |
| 78 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +42 | 35408 |
| 79 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +41 | 19021 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +41 | 31013 |
| 81 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +40 | 6687 |
| 82 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +40 | 27201 |
| 83 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +40 | 21997 |
| 84 | [decolua/9router](https://github.com/decolua/9router) | +39 | 23537 |
| 85 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +39 | 5301 |
| 86 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +39 | 23188 |
| 87 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +39 | 27084 |
| 88 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +39 | 28764 |
| 89 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +39 | 40527 |
| 90 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +39 | 9927 |
| 91 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +38 | 2364 |
| 92 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10690 |
| 93 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +37 | 7744 |
| 94 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +37 | 24446 |
| 95 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +36 | 2731 |
| 96 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +36 | 2027 |
| 97 | [block/buzz](https://github.com/block/buzz) | +35 | 11696 |
| 98 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +35 | 12164 |
| 99 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +33 | 9707 |
| 100 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +32 | 26284 |
| 101 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +32 | 46053 |
| 102 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +31 | 26382 |
| 103 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +31 | 18314 |
| 104 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2211 |
| 105 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2619 |
| 106 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +30 | 34201 |
| 107 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +30 | 31747 |
| 108 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +29 | 25735 |
| 109 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +29 | 6334 |
| 110 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1392 |
| 111 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +28 | 43899 |
| 112 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +28 | 8457 |
| 113 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +27 | 29153 |
| 114 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15228 |
| 115 | [floci-io/floci](https://github.com/floci-io/floci) | +27 | 17336 |
| 116 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +26 | 12329 |
| 117 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +25 | 1254 |
| 118 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +25 | 7197 |
| 119 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +24 | 25997 |
| 120 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1855 |
| 121 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +23 | 29754 |
| 122 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +23 | 6578 |
| 123 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +23 | 8019 |
| 124 | [openai/plugins](https://github.com/openai/plugins) | +23 | 4734 |
| 125 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1442 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +22 | 18185 |
| 127 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +22 | 7075 |
| 128 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 5213 |
| 129 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +22 | 27211 |
| 130 | [anbeime/skill](https://github.com/anbeime/skill) | +21 | 4186 |
| 131 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +21 | 1686 |
| 132 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 2119 |
| 133 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 134 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 4227 |
| 135 | [openai/skills](https://github.com/openai/skills) | +20 | 24172 |
| 136 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 137 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4173 |
| 138 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 10373 |
| 139 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +20 | 5019 |
| 140 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +20 | 2863 |
| 141 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +19 | 5183 |
| 142 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +19 | 9979 |
| 143 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1964 |
| 144 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7887 |
| 145 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +18 | 9062 |
| 146 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +18 | 32647 |
| 147 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +18 | 4840 |
| 148 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +18 | 756 |
| 149 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1426 |
| 150 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 2973 |
| 151 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +17 | 4706 |
| 152 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 10829 |
| 153 | [browser-act/skills](https://github.com/browser-act/skills) | +17 | 4781 |
| 154 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 2791 |
| 155 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2018 |
| 156 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +17 | 17920 |
| 157 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +17 | 4133 |
| 158 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1752 |
| 159 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +17 | 3619 |
| 160 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +17 | 1825 |
| 161 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +17 | 3783 |
| 162 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +17 | 2155 |
| 163 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 676 |
| 164 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3253 |
| 165 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 479 |
| 166 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +16 | 33778 |
| 167 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +16 | 5743 |
| 168 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4556 |
| 169 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +15 | 4632 |
| 170 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +15 | 3608 |
| 171 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +15 | 15294 |
| 172 | [jundot/omlx](https://github.com/jundot/omlx) | +15 | 18175 |
| 173 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 405 |
| 174 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +14 | 27215 |
| 175 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +14 | 1860 |
| 176 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +14 | 3454 |
| 177 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +14 | 4591 |
| 178 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +14 | 27851 |
| 179 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +13 | 982 |
| 180 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +13 | 2093 |
| 181 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +13 | 29473 |
| 182 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1027 |
| 183 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +13 | 8056 |
| 184 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +12 | 9379 |
| 185 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +12 | 16520 |
| 186 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +12 | 13853 |
| 187 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +12 | 9191 |
| 188 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +12 | 7224 |
| 189 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4885 |
| 190 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2510 |
| 191 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 724 |
| 192 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +11 | 18516 |
| 193 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 716 |
| 194 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 195 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +10 | 6751 |
| 196 | [penecho/penecho](https://github.com/penecho/penecho) | +10 | 1592 |
| 197 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +10 | 8842 |
| 198 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 885 |
| 199 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +10 | 26802 |
| 200 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 433 |
| 201 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +10 | 2646 |
| 202 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1314 |
| 203 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5210 |
| 204 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1452 |
| 205 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +9 | 2984 |
| 206 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +9 | 1110 |
| 207 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +9 | 8695 |
| 208 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +9 | 371 |
| 209 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +9 | 714 |
| 210 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +9 | 599 |
| 211 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1640 |
| 212 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +8 | 971 |
| 213 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +8 | 3026 |
| 214 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +8 | 2980 |
| 215 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +8 | 5633 |
| 216 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +8 | 12000 |
| 217 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +8 | 9154 |
| 218 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +8 | 692 |
| 219 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 417 |
| 220 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +8 | 4702 |
| 221 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6248 |
| 222 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1998 |
| 223 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1091 |
| 224 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +7 | 2833 |
| 225 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +7 | 6479 |
| 226 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 227 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +7 | 1404 |
| 228 | [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) | +7 | 2742 |
| 229 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 167 |
| 230 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +7 | 2983 |
| 231 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 1168 |
| 232 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2602 |
| 233 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 484 |
| 234 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 560 |
| 235 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +6 | 705 |
| 236 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6014 |
| 237 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10046 |
| 238 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 193 |
| 239 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 797 |
| 240 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 958 |
| 241 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5971 |
| 242 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 327 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +5 | 14388 |
| 244 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +5 | 646 |
| 245 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 463 |
| 246 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 607 |
| 247 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +5 | 5052 |
| 248 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +5 | 5852 |
| 249 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1649 |
| 250 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 610 |
| 251 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 314 |
| 252 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +5 | 462 |
| 253 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +5 | 3310 |
| 254 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 697 |
| 255 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +4 | 460 |
| 256 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +4 | 463 |
| 257 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 536 |
| 258 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +4 | 384 |
| 259 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 970 |
| 260 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 598 |
| 261 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +4 | 234 |
| 262 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 382 |
| 263 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 647 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2823 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2929 |
| 266 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 267 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 268 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +3 | 427 |
| 269 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9388 |
| 270 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +3 | 3787 |
| 271 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 155 |
| 272 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2590 |
| 273 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1877 |
| 274 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 267 |
| 275 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 108 |
| 276 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 983 |
| 277 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 278 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 279 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +3 | 648 |
| 280 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 281 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 569 |
| 282 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 96 |
| 283 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 181 |
| 284 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 420 |
| 285 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 787 |
| 286 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 168 |
| 287 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 272 |
| 288 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 846 |
| 289 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1702 |
| 290 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 764 |
| 291 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 711 |
| 292 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2433 |
| 293 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 758 |
| 294 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +2 | 129 |
| 295 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 296 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 119 |
| 297 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +2 | 10438 |
| 298 | [kknifer7/FreeBox](https://github.com/kknifer7/FreeBox) | +2 | 1781 |
| 299 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 822 |
| 300 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 63 |
