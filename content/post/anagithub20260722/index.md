---
title: "2026-07-22 GitHub增长趋势报告"
description: "1.buzz+8 2.ai-job-search+5 3.voicebox+5 4.code-review-graph+4 5.OpenMontage+4"
date: 2026-07-22T21:09:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-22 21:09:49

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
        'daily': {"categories": ["GoogleCloudPlatform/knowledge-catalog", "AgriciDaniel/claude-seo", "hoainho/img2threejs", "every-app/open-seo", "lidge-jun/opencodex", "earthtojake/text-to-cad", "1jehuang/jcode", "worldwonderer/oh-story-claudecode", "JCodesMore/ai-website-cloner-template", "browser-use/video-use", "stablyai/orca", "rohitg00/ai-engineering-from-scratch", "facebook/astryx", "diegosouzapw/OmniRoute", "microsoft/SkillOpt", "calesthio/OpenMontage", "tirth8205/code-review-graph", "jamiepine/voicebox", "MadsLorentzen/ai-job-search", "block/buzz"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 8]},
        'weekly': {"categories": ["Robbyant/lingbot-map", "tt-a1i/archify", "iOfficeAI/OfficeCLI", "calesthio/OpenMontage", "HKUDS/DeepTutor", "MoonshotAI/kimi-cli", "tirth8205/code-review-graph", "usestrix/strix", "ibelick/ui-skills", "rohitg00/ai-engineering-from-scratch", "jamiepine/voicebox", "MadsLorentzen/ai-job-search", "JustVugg/colibri", "HKUDS/Vibe-Trading", "ogulcancelik/herdr", "diegosouzapw/OmniRoute", "stablyai/orca", "emilkowalski/skills", "oblien/openship", "Fei-Away/Codex-Dream-Skin"], "data": [12, 13, 13, 13, 14, 14, 14, 16, 16, 16, 17, 19, 21, 24, 24, 24, 27, 29, 31, 58]},
        'monthly': {"categories": ["simplex-chat/simplex-chat", "alibaba/page-agent", "facebook/astryx", "MadsLorentzen/ai-job-search", "hugohe3/ppt-master", "apple/container", "jamiepine/voicebox", "topoteretes/cognee", "ogulcancelik/herdr", "XxHuberrr/Mineradio", "JCodesMore/ai-website-cloner-template", "stablyai/orca", "langchain-ai/openwiki", "xbtlin/ai-berkshire", "ZhuLinsen/daily_stock_analysis", "baidu/Unlimited-OCR", "google-labs-code/design.md", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [144, 144, 145, 148, 154, 159, 162, 165, 170, 182, 184, 188, 188, 201, 210, 227, 228, 253, 349, 503]}
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
| 1 | [block/buzz](https://github.com/block/buzz) | +8 | 3883 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +5 | 25261 |
| 3 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +5 | 45669 |
| 4 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +4 | 25246 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +4 | 41216 |
| 6 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +4 | 14431 |
| 7 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 25047 |
| 8 | [facebook/astryx](https://github.com/facebook/astryx) | +3 | 10343 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3 | 42162 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 25984 |
| 11 | [browser-use/video-use](https://github.com/browser-use/video-use) | +2 | 17534 |
| 12 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2 | 29664 |
| 13 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +2 | 4474 |
| 14 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 10703 |
| 15 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +2 | 9569 |
| 16 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +2 | 3512 |
| 17 | [every-app/open-seo](https://github.com/every-app/open-seo) | +2 | 7090 |
| 18 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +2 | 1990 |
| 19 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2 | 12064 |
| 20 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +2 | 7605 |
| 21 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 41217 |
| 22 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +2 | 4218 |
| 23 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +2 | 17925 |
| 24 | [yaojingang/geo-citation-lab](https://github.com/yaojingang/geo-citation-lab) | +2 | 531 |
| 25 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +2 | 1521 |
| 26 | [orca-wm/Orca](https://github.com/orca-wm/Orca) | +2 | 464 |
| 27 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +2 | 3202 |
| 28 | [datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | +2 | 5721 |
| 29 | [usestrix/strix](https://github.com/usestrix/strix) | +2 | 43404 |
| 30 | [HapeLee/legado-with-MD3](https://github.com/HapeLee/legado-with-MD3) | +2 | 5218 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +58 | 11826 |
| 2 | [oblien/openship](https://github.com/oblien/openship) | +31 | 7196 |
| 3 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +29 | 19860 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 25984 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +24 | 25047 |
| 6 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +24 | 19509 |
| 7 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +24 | 26462 |
| 8 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +21 | 17925 |
| 9 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +19 | 25261 |
| 10 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +17 | 45669 |
| 11 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +16 | 42162 |
| 12 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +16 | 5980 |
| 13 | [usestrix/strix](https://github.com/usestrix/strix) | +16 | 43404 |
| 14 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +14 | 25246 |
| 15 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +14 | 10606 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +14 | 29086 |
| 17 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +13 | 41216 |
| 18 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +13 | 21040 |
| 19 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +13 | 6957 |
| 20 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +12 | 14887 |
| 21 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +11 | 6400 |
| 22 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +11 | 10847 |
| 23 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 10703 |
| 24 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +11 | 16575 |
| 25 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +11 | 4832 |
| 26 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +10 | 41217 |
| 27 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +10 | 4308 |
| 28 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +10 | 7082 |
| 29 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +10 | 1166 |
| 30 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +9 | 1597 |
| 31 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4888 |
| 32 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +9 | 2049 |
| 33 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +9 | 7051 |
| 34 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +9 | 34135 |
| 35 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +9 | 12892 |
| 36 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1350 |
| 37 | [block/buzz](https://github.com/block/buzz) | +8 | 3883 |
| 38 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +8 | 4569 |
| 39 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +8 | 2126 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +8 | 6118 |
| 41 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +8 | 9631 |
| 42 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +8 | 2581 |
| 43 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +8 | 7670 |
| 44 | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) | +8 | 1945 |
| 45 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 40555 |
| 46 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +8 | 41700 |
| 47 | [Stack-Cairn/LiveAgent](https://github.com/Stack-Cairn/LiveAgent) | +8 | 1284 |
| 48 | [deer-flow/llm-space](https://github.com/deer-flow/llm-space) | +8 | 1167 |
| 49 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +7 | 1990 |
| 50 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +7 | 19200 |
| 51 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +7 | 12064 |
| 52 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +7 | 3099 |
| 53 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +7 | 23920 |
| 54 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +6 | 14431 |
| 55 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 29664 |
| 56 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +6 | 3512 |
| 57 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +6 | 1521 |
| 58 | [stupside/castor](https://github.com/stupside/castor) | +6 | 1779 |
| 59 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6079 |
| 60 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 30479 |
| 61 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6 | 48758 |
| 62 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +6 | 11133 |
| 63 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +6 | 36894 |
| 64 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +6 | 7814 |
| 65 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 41572 |
| 66 | [malisper/pgrust](https://github.com/malisper/pgrust) | +6 | 3708 |
| 67 | [KytyPS5/KytyPS5](https://github.com/KytyPS5/KytyPS5) | +6 | 802 |
| 68 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +6 | 4403 |
| 69 | [team-reflect/reflect-open](https://github.com/team-reflect/reflect-open) | +6 | 1340 |
| 70 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +6 | 924 |
| 71 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +6 | 2020 |
| 72 | [MatinSenPai/Aether-GUI](https://github.com/MatinSenPai/Aether-GUI) | +6 | 723 |
| 73 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +6 | 776 |
| 74 | [browser-use/video-use](https://github.com/browser-use/video-use) | +5 | 17534 |
| 75 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +5 | 26359 |
| 76 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 10343 |
| 77 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +5 | 13957 |
| 78 | [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | +5 | 14101 |
| 79 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +5 | 488 |
| 80 | [modem-dev/hunk](https://github.com/modem-dev/hunk) | +5 | 7612 |
| 81 | [apache/ossie](https://github.com/apache/ossie) | +5 | 1495 |
| 82 | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | +5 | 6140 |
| 83 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 27568 |
| 84 | [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | +5 | 30661 |
| 85 | [yorgai/ORG2](https://github.com/yorgai/ORG2) | +5 | 2223 |
| 86 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +5 | 972 |
| 87 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 26244 |
| 88 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +5 | 13687 |
| 89 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +4 | 58304 |
| 90 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +4 | 9236 |
| 91 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +4 | 27490 |
| 92 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 1700 |
| 93 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +4 | 17288 |
| 94 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +4 | 9569 |
| 95 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +4 | 7605 |
| 96 | [every-app/open-seo](https://github.com/every-app/open-seo) | +4 | 7090 |
| 97 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 30400 |
| 98 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 723 |
| 99 | [tw93/Waza](https://github.com/tw93/Waza) | +4 | 6587 |
| 100 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 5264 |
| 101 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +4 | 7632 |
| 102 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 142 |
| 103 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +4 | 11431 |
| 104 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +3 | 4981 |
| 105 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +3 | 23313 |
| 106 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +3 | 4218 |
| 107 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +3 | 2468 |
| 108 | [chenyme/grok2api](https://github.com/chenyme/grok2api) | +3 | 6558 |
| 109 | [inssekt/CocoonFE](https://github.com/inssekt/CocoonFE) | +3 | 1082 |
| 110 | [google-research/tabfm](https://github.com/google-research/tabfm) | +3 | 2026 |
| 111 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +3 | 5081 |
| 112 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +3 | 1298 |
| 113 | [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | +3 | 11758 |
| 114 | [xiejunjie524/handdraw-story-video](https://github.com/xiejunjie524/handdraw-story-video) | +3 | 619 |
| 115 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +3 | 34010 |
| 116 | [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | +3 | 6075 |
| 117 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | +3 | 17379 |
| 118 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +3 | 1705 |
| 119 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3 | 45775 |
| 120 | [Cjbuilds/Codex-Orchestration](https://github.com/Cjbuilds/Codex-Orchestration) | +3 | 516 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +503 | 41216 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +349 | 34135 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +253 | 43404 |
| 4 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +228 | 26240 |
| 5 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +227 | 17288 |
| 6 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +210 | 58304 |
| 7 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +201 | 13687 |
| 8 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 12892 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +188 | 25984 |
| 10 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +184 | 29664 |
| 11 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8746 |
| 12 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +170 | 19509 |
| 13 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +165 | 29159 |
| 14 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +162 | 45669 |
| 15 | [apple/container](https://github.com/apple/container) | +159 | 48188 |
| 16 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +154 | 40555 |
| 17 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +148 | 25261 |
| 18 | [facebook/astryx](https://github.com/facebook/astryx) | +145 | 10343 |
| 19 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +144 | 27490 |
| 20 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18896 |
| 21 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +142 | 26086 |
| 22 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +134 | 26462 |
| 23 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +130 | 9140 |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +129 | 29660 |
| 25 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +128 | 25048 |
| 26 | [erincatto/box3d](https://github.com/erincatto/box3d) | +125 | 5464 |
| 27 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +122 | 26360 |
| 28 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +119 | 16575 |
| 29 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +108 | 4003 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +97 | 16677 |
| 31 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +96 | 6890 |
| 32 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +95 | 30479 |
| 33 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +89 | 19860 |
| 34 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +87 | 48758 |
| 35 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +87 | 5264 |
| 36 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +87 | 10537 |
| 37 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +86 | 8776 |
| 38 | [browser-use/video-use](https://github.com/browser-use/video-use) | +83 | 17534 |
| 39 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +83 | 36894 |
| 40 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6738 |
| 41 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +79 | 17925 |
| 42 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +78 | 10847 |
| 43 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6613 |
| 44 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +77 | 6118 |
| 45 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +75 | 6406 |
| 46 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +74 | 10939 |
| 47 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 14887 |
| 48 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +70 | 38984 |
| 49 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +70 | 13548 |
| 50 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +67 | 8615 |
| 51 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +67 | 26244 |
| 52 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +64 | 9631 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +63 | 41700 |
| 54 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +62 | 21040 |
| 55 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +62 | 41217 |
| 56 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +60 | 14431 |
| 57 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +60 | 2934 |
| 58 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +59 | 3737 |
| 59 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +59 | 24338 |
| 60 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +58 | 11826 |
| 61 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +58 | 6957 |
| 62 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +58 | 19200 |
| 63 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +58 | 11431 |
| 64 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +56 | 27568 |
| 65 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +55 | 42162 |
| 66 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +55 | 47408 |
| 67 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27548 |
| 68 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +54 | 26150 |
| 69 | [multica-ai/multica](https://github.com/multica-ai/multica) | +53 | 41572 |
| 70 | [antirez/ds4](https://github.com/antirez/ds4) | +51 | 19072 |
| 71 | [EpicGames/lore](https://github.com/EpicGames/lore) | +51 | 8156 |
| 72 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5099 |
| 73 | [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | +49 | 3829 |
| 74 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +48 | 7051 |
| 75 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3759 |
| 76 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +48 | 23351 |
| 77 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +48 | 29907 |
| 78 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +46 | 33632 |
| 79 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +46 | 9810 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +46 | 30400 |
| 81 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +46 | 3835 |
| 82 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +45 | 40282 |
| 83 | [every-app/open-seo](https://github.com/every-app/open-seo) | +45 | 7090 |
| 84 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +44 | 26854 |
| 85 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +44 | 26961 |
| 86 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +44 | 28543 |
| 87 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9790 |
| 88 | [tigicion/dao-code](https://github.com/tigicion/dao-code) | +44 | 1376 |
| 89 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +44 | 7064 |
| 90 | [decolua/9router](https://github.com/decolua/9router) | +43 | 23074 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +43 | 23007 |
| 92 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 2026 |
| 93 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +43 | 24246 |
| 94 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +43 | 35217 |
| 95 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +43 | 4935 |
| 96 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +42 | 7632 |
| 97 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +41 | 18860 |
| 98 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +40 | 5081 |
| 99 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +39 | 10602 |
| 100 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +39 | 2028 |
| 101 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +38 | 6400 |
| 102 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +36 | 8391 |
| 103 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +35 | 9341 |
| 104 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +34 | 34010 |
| 105 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +34 | 12064 |
| 106 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +33 | 31477 |
| 107 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +32 | 23920 |
| 108 | [anbeime/skill](https://github.com/anbeime/skill) | +32 | 4039 |
| 109 | [oblien/openship](https://github.com/oblien/openship) | +31 | 7196 |
| 110 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +31 | 43732 |
| 111 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +31 | 25629 |
| 112 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2167 |
| 113 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2579 |
| 114 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +30 | 28928 |
| 115 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +30 | 45775 |
| 116 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +30 | 6243 |
| 117 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +29 | 25877 |
| 118 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +29 | 32493 |
| 119 | [openai/plugins](https://github.com/openai/plugins) | +28 | 4672 |
| 120 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +27 | 25247 |
| 121 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +27 | 1298 |
| 122 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15212 |
| 123 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +27 | 27079 |
| 124 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +26 | 1138 |
| 125 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +25 | 6356 |
| 126 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +25 | 2060 |
| 127 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +25 | 7044 |
| 128 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +25 | 2833 |
| 129 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 16993 |
| 130 | [openai/skills](https://github.com/openai/skills) | +24 | 24068 |
| 131 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +24 | 1161 |
| 132 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +23 | 4981 |
| 133 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1822 |
| 134 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +23 | 7670 |
| 135 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +22 | 29086 |
| 136 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +22 | 9906 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +22 | 18084 |
| 138 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +22 | 6842 |
| 139 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1669 |
| 140 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +22 | 1778 |
| 141 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 4832 |
| 142 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +21 | 4218 |
| 143 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1394 |
| 144 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +21 | 17737 |
| 145 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +21 | 4749 |
| 146 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 725 |
| 147 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 2064 |
| 148 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 149 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +21 | 2086 |
| 150 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +21 | 12674 |
| 151 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 152 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +19 | 8878 |
| 153 | [browser-act/skills](https://github.com/browser-act/skills) | +19 | 4649 |
| 154 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +19 | 4005 |
| 155 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +19 | 3550 |
| 156 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +19 | 4046 |
| 157 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1954 |
| 158 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +19 | 9569 |
| 159 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7845 |
| 160 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +18 | 27105 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +18 | 18071 |
| 162 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1417 |
| 163 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +18 | 3738 |
| 164 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 1997 |
| 165 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +17 | 1851 |
| 166 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1733 |
| 167 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +17 | 22956 |
| 168 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +17 | 5667 |
| 169 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 670 |
| 170 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10606 |
| 171 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 448 |
| 172 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +16 | 15224 |
| 173 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +16 | 33714 |
| 174 | [XBuilderLAB/cheat-on-content](https://github.com/XBuilderLAB/cheat-on-content) | +16 | 5827 |
| 175 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +16 | 2049 |
| 176 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +15 | 2581 |
| 177 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +15 | 4403 |
| 178 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +15 | 16413 |
| 179 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +15 | 3196 |
| 180 | [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) | +15 | 2576 |
| 181 | [ascending-llc/jarvis-registry](https://github.com/ascending-llc/jarvis-registry) | +15 | 2402 |
| 182 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +15 | 4308 |
| 183 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 399 |
| 184 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +15 | 4474 |
| 185 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +14 | 9236 |
| 186 | [NVIDIA/skills](https://github.com/NVIDIA/skills) | +14 | 2645 |
| 187 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +14 | 3607 |
| 188 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +14 | 16175 |
| 189 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +14 | 8661 |
| 190 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +14 | 7142 |
| 191 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +14 | 26709 |
| 192 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +14 | 2619 |
| 193 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +14 | 685 |
| 194 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +14 | 4888 |
| 195 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +13 | 956 |
| 196 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1017 |
| 197 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +13 | 0 |
| 198 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +12 | 7937 |
| 199 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +12 | 29345 |
| 200 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +12 | 18436 |
| 201 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 713 |
| 202 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +11 | 11956 |
| 203 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +11 | 6440 |
| 204 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 703 |
| 205 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 206 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +11 | 560 |
| 207 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 873 |
| 208 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1089 |
| 209 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 431 |
| 210 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +10 | 8608 |
| 211 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 369 |
| 212 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +10 | 1354 |
| 213 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 681 |
| 214 | [wgjuan2314/shuangzi-xubei](https://github.com/wgjuan2314/shuangzi-xubei) | +10 | 147 |
| 215 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1351 |
| 216 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5056 |
| 217 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +9 | 9074 |
| 218 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +9 | 5562 |
| 219 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +8 | 6217 |
| 220 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 2881 |
| 221 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +8 | 2909 |
| 222 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +8 | 2940 |
| 223 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 409 |
| 224 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +8 | 2939 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +7 | 2550 |
| 226 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +7 | 639 |
| 227 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 949 |
| 228 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1988 |
| 229 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1053 |
| 230 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 231 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +7 | 822 |
| 232 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 166 |
| 233 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +7 | 412 |
| 234 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +7 | 4649 |
| 235 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +7 | 3284 |
| 236 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +6 | 459 |
| 237 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 909 |
| 238 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 442 |
| 239 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 557 |
| 240 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +6 | 462 |
| 241 | [rpamis/comet](https://github.com/rpamis/comet) | +6 | 2439 |
| 242 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +6 | 453 |
| 243 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +6 | 700 |
| 244 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6079 |
| 245 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10042 |
| 246 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 191 |
| 247 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5948 |
| 248 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 321 |
| 249 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 591 |
| 250 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1633 |
| 251 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 605 |
| 252 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 305 |
| 253 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +5 | 1909 |
| 254 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +4 | 723 |
| 255 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +4 | 874 |
| 256 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +4 | 905 |
| 257 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 907 |
| 258 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 518 |
| 259 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 642 |
| 260 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 376 |
| 261 | [jasonkneen/tiny-world-builder](https://github.com/jasonkneen/tiny-world-builder) | +4 | 1470 |
| 262 | [kimsh-1/gongnyang-prompt-kit](https://github.com/kimsh-1/gongnyang-prompt-kit) | +4 | 284 |
| 263 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 164 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2788 |
| 265 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 2913 |
| 266 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2898 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 657 |
| 268 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +4 | 3764 |
| 269 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +4 | 955 |
| 270 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +3 | 1381 |
| 271 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 272 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 139 |
| 273 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9491 |
| 274 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 151 |
| 275 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2587 |
| 276 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1855 |
| 277 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 562 |
| 278 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 264 |
| 279 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 102 |
| 280 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 129 |
| 281 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 282 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 283 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +3 | 2793 |
| 284 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 88 |
| 285 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 94 |
| 286 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 172 |
| 287 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 420 |
| 288 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 779 |
| 289 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 164 |
| 290 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 265 |
| 291 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 845 |
| 292 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1699 |
| 293 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 755 |
| 294 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 701 |
| 295 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2424 |
| 296 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 733 |
| 297 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 341 |
| 298 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 299 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 111 |
| 300 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +2 | 0 |
