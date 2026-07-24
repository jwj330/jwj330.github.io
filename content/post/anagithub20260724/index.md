---
title: "2026-07-24 GitHub增长趋势报告"
description: "1.buzz+12 2.ego-lite+9 3.OmniRoute+6 4.ai-job-search+5 5.iFixAi+4"
date: 2026-07-24T21:05:20+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-24 21:05:20

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
        'daily': {"categories": ["1jehuang/jcode", "jgravelle/jcodemunch-mcp", "alibaba/open-code-review", "Galaxy-Dawn/claude-scholar", "humanlayer/advanced-context-engineering-for-coding-agents", "coreyhaines31/marketingskills", "lidge-jun/opencodex", "ogulcancelik/herdr", "BigPizzaV3/CodexPlusPlus", "iOfficeAI/OfficeCLI", "Vincentwei1021/video-shotcraft", "oblien/openship", "stablyai/orca", "calesthio/OpenMontage", "hoainho/img2threejs", "ifixai-ai/iFixAi", "MadsLorentzen/ai-job-search", "diegosouzapw/OmniRoute", "citrolabs/ego-lite", "block/buzz"], "data": [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 9, 12]},
        'weekly': {"categories": ["JustVugg/colibri", "calesthio/OpenMontage", "MoonshotAI/kimi-cli", "ibelick/ui-skills", "lidge-jun/opencodex", "emilkowalski/skills", "1jehuang/jcode", "hoainho/img2threejs", "jamiepine/voicebox", "iOfficeAI/OfficeCLI", "ogulcancelik/herdr", "rohitg00/ai-engineering-from-scratch", "tirth8205/code-review-graph", "MadsLorentzen/ai-job-search", "baidu/Unlimited-OCR", "Fei-Away/Codex-Dream-Skin", "block/buzz", "stablyai/orca", "diegosouzapw/OmniRoute", "oblien/openship"], "data": [11, 11, 13, 13, 13, 14, 14, 14, 15, 17, 19, 19, 20, 20, 21, 22, 25, 26, 39, 42]},
        'monthly': {"categories": ["hugohe3/ppt-master", "topoteretes/cognee", "jamiepine/voicebox", "simplex-chat/simplex-chat", "diegosouzapw/OmniRoute", "Zackriya-Solutions/meetily", "facebook/astryx", "MadsLorentzen/ai-job-search", "ogulcancelik/herdr", "JCodesMore/ai-website-cloner-template", "ZhuLinsen/daily_stock_analysis", "XxHuberrr/Mineradio", "baidu/Unlimited-OCR", "xbtlin/ai-berkshire", "langchain-ai/openwiki", "stablyai/orca", "google-labs-code/design.md", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [139, 141, 142, 144, 144, 145, 146, 154, 171, 172, 178, 182, 188, 188, 188, 193, 223, 254, 313, 428]}
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
| 1 | [block/buzz](https://github.com/block/buzz) | +12 | 9669 |
| 2 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +9 | 2465 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +6 | 28679 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +5 | 26298 |
| 5 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 2201 |
| 6 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +4 | 3954 |
| 7 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +4 | 41957 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 28277 |
| 9 | [oblien/openship](https://github.com/oblien/openship) | +4 | 8199 |
| 10 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +3 | 1399 |
| 11 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +3 | 21905 |
| 12 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +3 | 26493 |
| 13 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +3 | 20380 |
| 14 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +3 | 4501 |
| 15 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +2 | 41554 |
| 16 | [humanlayer/advanced-context-engineering-for-coding-agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) | +2 | 1947 |
| 17 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +2 | 4794 |
| 18 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +2 | 12357 |
| 19 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +2 | 2147 |
| 20 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +2 | 11194 |
| 21 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +2 | 26191 |
| 22 | [NeuroAIHub/BrainPilot](https://github.com/NeuroAIHub/BrainPilot) | +2 | 96 |
| 23 | [ShouqiaoW/erdos](https://github.com/ShouqiaoW/erdos) | +2 | 176 |
| 24 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2 | 49604 |
| 25 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +2 | 7688 |
| 26 | [itayinbarr/little-coder](https://github.com/itayinbarr/little-coder) | +2 | 1888 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +2 | 18649 |
| 28 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +2 | 14904 |
| 29 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +2 | 4214 |
| 30 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2 | 46006 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [oblien/openship](https://github.com/oblien/openship) | +42 | 8199 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +39 | 28679 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca) | +26 | 28277 |
| 4 | [block/buzz](https://github.com/block/buzz) | +25 | 9669 |
| 5 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +22 | 12215 |
| 6 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +21 | 18649 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +20 | 26298 |
| 8 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +20 | 26191 |
| 9 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +19 | 43140 |
| 10 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +19 | 20380 |
| 11 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +17 | 21905 |
| 12 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +15 | 46473 |
| 13 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +14 | 3955 |
| 14 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +14 | 11194 |
| 15 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +14 | 20525 |
| 16 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +13 | 4501 |
| 17 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +13 | 6291 |
| 18 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +13 | 10780 |
| 19 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +11 | 41957 |
| 20 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 18608 |
| 21 | [usestrix/strix](https://github.com/usestrix/strix) | +11 | 43972 |
| 22 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +11 | 27278 |
| 23 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +11 | 4485 |
| 24 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +9 | 2465 |
| 25 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +9 | 14904 |
| 26 | [nullclaw/nullhub](https://github.com/nullclaw/nullhub) | +9 | 1562 |
| 27 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9 | 29553 |
| 28 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4866 |
| 29 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +8 | 41554 |
| 30 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +8 | 34931 |
| 31 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +8 | 19576 |
| 32 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +8 | 4927 |
| 33 | [microsoft/Ontology-Playground](https://github.com/microsoft/Ontology-Playground) | +8 | 2186 |
| 34 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +8 | 15266 |
| 35 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +7 | 30071 |
| 36 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +7 | 26493 |
| 37 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +7 | 46006 |
| 38 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +7 | 7926 |
| 39 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +7 | 16803 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +7 | 49604 |
| 41 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +7 | 7256 |
| 42 | [browser-use/video-use](https://github.com/browser-use/video-use) | +6 | 17749 |
| 43 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +6 | 9909 |
| 44 | [every-app/open-seo](https://github.com/every-app/open-seo) | +6 | 7700 |
| 45 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +6 | 30958 |
| 46 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +6 | 12260 |
| 47 | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | +6 | 1562 |
| 48 | [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) | +6 | 7878 |
| 49 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6014 |
| 50 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +6 | 13159 |
| 51 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +6 | 7127 |
| 52 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 7688 |
| 53 | [agegr/pi-web](https://github.com/agegr/pi-web) | +5 | 2603 |
| 54 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +5 | 27724 |
| 55 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +5 | 9360 |
| 56 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +5 | 6296 |
| 57 | [Julian-adv/OpenMMO](https://github.com/Julian-adv/OpenMMO) | +5 | 1384 |
| 58 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 10315 |
| 59 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +5 | 4214 |
| 60 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5 | 37446 |
| 61 | [tw93/Waza](https://github.com/tw93/Waza) | +5 | 6614 |
| 62 | [Open-Dev-Society/OpenStock](https://github.com/Open-Dev-Society/OpenStock) | +5 | 13973 |
| 63 | [getpaseo/paseo](https://github.com/getpaseo/paseo) | +5 | 11323 |
| 64 | [Icex0/wp2shell-poc](https://github.com/Icex0/wp2shell-poc) | +5 | 513 |
| 65 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +4 | 6598 |
| 66 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +4 | 1399 |
| 67 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 2861 |
| 68 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4 | 2201 |
| 69 | [multica-ai/multica](https://github.com/multica-ai/multica) | +4 | 41897 |
| 70 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +4 | 23370 |
| 71 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +4 | 110 |
| 72 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +4 | 19694 |
| 73 | [nyblnet/bento](https://github.com/nyblnet/bento) | +4 | 1391 |
| 74 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +4 | 4794 |
| 75 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4 | 7218 |
| 76 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +4 | 3662 |
| 77 | [facebook/astryx](https://github.com/facebook/astryx) | +4 | 10631 |
| 78 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +4 | 3204 |
| 79 | [Blaizzy/nativ](https://github.com/Blaizzy/nativ) | +4 | 857 |
| 80 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 4614 |
| 81 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14376 |
| 82 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +4 | 4194 |
| 83 | [kurikomi-labs/komi-store](https://github.com/kurikomi-labs/komi-store) | +4 | 16961 |
| 84 | [VexDB-THU/VexDB-Lite](https://github.com/VexDB-THU/VexDB-Lite) | +4 | 1295 |
| 85 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 42117 |
| 86 | [blader/humanizer](https://github.com/blader/humanizer) | +4 | 30840 |
| 87 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +4 | 1028 |
| 88 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +4 | 2489 |
| 89 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +4 | 1807 |
| 90 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +4 | 39376 |
| 91 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +4 | 5744 |
| 92 | [NInagusev47/Silent-Crypto-Miner](https://github.com/NInagusev47/Silent-Crypto-Miner) | +4 | 142 |
| 93 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 58648 |
| 94 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +3 | 44619 |
| 95 | [nexu-io/codex-slides](https://github.com/nexu-io/codex-slides) | +3 | 463 |
| 96 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +3 | 4563 |
| 97 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +3 | 29442 |
| 98 | [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | +3 | 2005 |
| 99 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +3 | 24293 |
| 100 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +3 | 34146 |
| 101 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 40956 |
| 102 | [Qualcomm-AI-research/MobileWan](https://github.com/Qualcomm-AI-research/MobileWan) | +3 | 76 |
| 103 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +3 | 26483 |
| 104 | [openai/skills](https://github.com/openai/skills) | +3 | 24152 |
| 105 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +3 | 4101 |
| 106 | [inssekt/CocoonFE](https://github.com/inssekt/CocoonFE) | +3 | 1106 |
| 107 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +3 | 6528 |
| 108 | [google-research/tabfm](https://github.com/google-research/tabfm) | +3 | 2077 |
| 109 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 7914 |
| 110 | [OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1) | +3 | 4358 |
| 111 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +3 | 1069 |
| 112 | [xiejunjie524/handdraw-story-video](https://github.com/xiejunjie524/handdraw-story-video) | +3 | 640 |
| 113 | [rollingSirius/equity-research-skill](https://github.com/rollingSirius/equity-research-skill) | +3 | 166 |
| 114 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +3 | 1747 |
| 115 | [valqore/valqore](https://github.com/valqore/valqore) | +3 | 1386 |
| 116 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +2 | 5120 |
| 117 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2 | 40482 |
| 118 | [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | +2 | 5682 |
| 119 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +2 | 1754 |
| 120 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +2 | 4742 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +428 | 41957 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +313 | 34931 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +254 | 43972 |
| 4 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +223 | 26333 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +193 | 28277 |
| 6 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 13159 |
| 7 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +188 | 13874 |
| 8 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +188 | 18649 |
| 9 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +182 | 8870 |
| 10 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +178 | 58648 |
| 11 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +172 | 30071 |
| 12 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +171 | 20380 |
| 13 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +154 | 26298 |
| 14 | [facebook/astryx](https://github.com/facebook/astryx) | +146 | 10631 |
| 15 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +145 | 26446 |
| 16 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +144 | 28679 |
| 17 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +144 | 18980 |
| 18 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +142 | 46473 |
| 19 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +141 | 29266 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +139 | 40956 |
| 21 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +137 | 27278 |
| 22 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +134 | 27713 |
| 23 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +130 | 9335 |
| 24 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +129 | 29862 |
| 25 | [erincatto/box3d](https://github.com/erincatto/box3d) | +126 | 5529 |
| 26 | [apple/container](https://github.com/apple/container) | +124 | 48258 |
| 27 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +121 | 16803 |
| 28 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +107 | 4079 |
| 29 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +103 | 26483 |
| 30 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +97 | 7035 |
| 31 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +90 | 20525 |
| 32 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +90 | 16890 |
| 33 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +87 | 5744 |
| 34 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +86 | 30958 |
| 35 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 17749 |
| 36 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +83 | 10604 |
| 37 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +82 | 49605 |
| 38 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +81 | 11530 |
| 39 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +81 | 18608 |
| 40 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6764 |
| 41 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +78 | 6296 |
| 42 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6678 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +74 | 37446 |
| 44 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +72 | 15266 |
| 45 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +71 | 21905 |
| 46 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +68 | 39376 |
| 47 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +67 | 8866 |
| 48 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +66 | 9909 |
| 49 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +66 | 8785 |
| 50 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +66 | 6528 |
| 51 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +64 | 26493 |
| 52 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +62 | 42117 |
| 53 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +62 | 4214 |
| 54 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +60 | 12215 |
| 55 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +60 | 14904 |
| 56 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +59 | 41554 |
| 57 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +59 | 7218 |
| 58 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +56 | 13641 |
| 59 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +55 | 43140 |
| 60 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +55 | 27569 |
| 61 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +55 | 24595 |
| 62 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +54 | 47534 |
| 63 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +51 | 19576 |
| 64 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +51 | 27724 |
| 65 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5156 |
| 66 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +50 | 26287 |
| 67 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +50 | 11500 |
| 68 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +48 | 34030 |
| 69 | [multica-ai/multica](https://github.com/multica-ai/multica) | +48 | 41897 |
| 70 | [baairon/torlink](https://github.com/baairon/torlink) | +48 | 3810 |
| 71 | [antirez/ds4](https://github.com/antirez/ds4) | +48 | 19169 |
| 72 | [every-app/open-seo](https://github.com/every-app/open-seo) | +47 | 7700 |
| 73 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +46 | 7256 |
| 74 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +46 | 23426 |
| 75 | [EpicGames/lore](https://github.com/EpicGames/lore) | +46 | 8183 |
| 76 | [Lakr233/AssppWeb](https://github.com/Lakr233/AssppWeb) | +46 | 3846 |
| 77 | [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book) | +46 | 3043 |
| 78 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +45 | 28705 |
| 79 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9789 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +44 | 30840 |
| 81 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +44 | 35342 |
| 82 | [tigicion/dao-code](https://github.com/tigicion/dao-code) | +44 | 1376 |
| 83 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 2077 |
| 84 | [oblien/openship](https://github.com/oblien/openship) | +42 | 8199 |
| 85 | [decolua/9router](https://github.com/decolua/9router) | +42 | 23419 |
| 86 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +42 | 18984 |
| 87 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +42 | 27144 |
| 88 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +42 | 40482 |
| 89 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +41 | 27022 |
| 90 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | +41 | 24391 |
| 91 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +41 | 9888 |
| 92 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +40 | 23137 |
| 93 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +40 | 2354 |
| 94 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +39 | 5259 |
| 95 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +39 | 7715 |
| 96 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +39 | 11816 |
| 97 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +38 | 6598 |
| 98 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10659 |
| 99 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +37 | 2028 |
| 100 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +35 | 9517 |
| 101 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +34 | 24293 |
| 102 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +33 | 26191 |
| 103 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +33 | 46006 |
| 104 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +31 | 34146 |
| 105 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +31 | 31664 |
| 106 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +31 | 25712 |
| 107 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2199 |
| 108 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2609 |
| 109 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +30 | 43831 |
| 110 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +30 | 8444 |
| 111 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +30 | 6326 |
| 112 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +30 | 5002 |
| 113 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +29 | 29103 |
| 114 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1363 |
| 115 | [openai/plugins](https://github.com/openai/plugins) | +28 | 4723 |
| 116 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +27 | 12260 |
| 117 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +27 | 15218 |
| 118 | [anbeime/skill](https://github.com/anbeime/skill) | +27 | 4150 |
| 119 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +26 | 25961 |
| 120 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +26 | 27180 |
| 121 | [block/buzz](https://github.com/block/buzz) | +25 | 9671 |
| 122 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +25 | 29553 |
| 123 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +25 | 1152 |
| 124 | [floci-io/floci](https://github.com/floci-io/floci) | +25 | 17045 |
| 125 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +24 | 6540 |
| 126 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +24 | 7023 |
| 127 | [fivetaku/insane-search](https://github.com/fivetaku/insane-search) | +24 | 2102 |
| 128 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +24 | 7156 |
| 129 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +23 | 1851 |
| 130 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +23 | 32618 |
| 131 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +23 | 7926 |
| 132 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +22 | 1679 |
| 133 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +22 | 5100 |
| 134 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +21 | 5120 |
| 135 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +21 | 1424 |
| 136 | [openai/skills](https://github.com/openai/skills) | +21 | 24152 |
| 137 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +21 | 18155 |
| 138 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +21 | 745 |
| 139 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +21 | 7114 |
| 140 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +21 | 2111 |
| 141 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 142 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 4194 |
| 143 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +20 | 17864 |
| 144 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +20 | 9954 |
| 145 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 146 | [sums001/Windows-Copilot-API](https://github.com/sums001/Windows-Copilot-API) | +20 | 1166 |
| 147 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4140 |
| 148 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 10315 |
| 149 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +20 | 2847 |
| 150 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +19 | 4101 |
| 151 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +19 | 4823 |
| 152 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +19 | 1812 |
| 153 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1960 |
| 154 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7873 |
| 155 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +18 | 8992 |
| 156 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +18 | 3604 |
| 157 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1423 |
| 158 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +18 | 3772 |
| 159 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +17 | 4614 |
| 160 | [browser-act/skills](https://github.com/browser-act/skills) | +17 | 4745 |
| 161 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2015 |
| 162 | [jundot/omlx](https://github.com/jundot/omlx) | +17 | 18143 |
| 163 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1744 |
| 164 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +17 | 5723 |
| 165 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +17 | 2147 |
| 166 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +17 | 675 |
| 167 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +17 | 27805 |
| 168 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +16 | 2861 |
| 169 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10780 |
| 170 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 471 |
| 171 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +16 | 15284 |
| 172 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | +16 | 33757 |
| 173 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4485 |
| 174 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +15 | 2201 |
| 175 | [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) | +15 | 3616 |
| 176 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +15 | 27184 |
| 177 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +15 | 3240 |
| 178 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +15 | 1859 |
| 179 | [Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) | +15 | 3935 |
| 180 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 401 |
| 181 | [ascending-llc/jarvis-registry](https://github.com/ascending-llc/jarvis-registry) | +14 | 2458 |
| 182 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +14 | 2085 |
| 183 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +14 | 29442 |
| 184 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +14 | 4563 |
| 185 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +14 | 4866 |
| 186 | [hoainho/img2threejs](https://github.com/hoainho/img2threejs) | +13 | 3955 |
| 187 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +13 | 16482 |
| 188 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1023 |
| 189 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +13 | 7209 |
| 190 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +13 | 2643 |
| 191 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +12 | 9360 |
| 192 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +12 | 8023 |
| 193 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +12 | 8802 |
| 194 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +12 | 690 |
| 195 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2489 |
| 196 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 720 |
| 197 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +11 | 26772 |
| 198 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +11 | 18492 |
| 199 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +11 | 8678 |
| 200 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +11 | 712 |
| 201 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 202 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +10 | 2465 |
| 203 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 883 |
| 204 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +10 | 1102 |
| 205 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +10 | 5610 |
| 206 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +10 | 11979 |
| 207 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 432 |
| 208 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +10 | 370 |
| 209 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +10 | 1390 |
| 210 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +10 | 697 |
| 211 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +10 | 584 |
| 212 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5163 |
| 213 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1430 |
| 214 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +9 | 2996 |
| 215 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 2958 |
| 216 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +8 | 9120 |
| 217 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +8 | 6475 |
| 218 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +8 | 5841 |
| 219 | [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) | +8 | 2736 |
| 220 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +8 | 412 |
| 221 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +8 | 2967 |
| 222 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6241 |
| 223 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +7 | 2589 |
| 224 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 962 |
| 225 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +7 | 2963 |
| 226 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 1998 |
| 227 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1083 |
| 228 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 229 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 167 |
| 230 | [XBuilderLAB/cheat-on-money](https://github.com/XBuilderLAB/cheat-on-money) | +7 | 705 |
| 231 | [marcolunapaim/polymarket-5min-arbitrage-trading-bot](https://github.com/marcolunapaim/polymarket-5min-arbitrage-trading-bot) | +7 | 0 |
| 232 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +7 | 4692 |
| 233 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +7 | 3303 |
| 234 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +6 | 1016 |
| 235 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +6 | 14376 |
| 236 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 476 |
| 237 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 559 |
| 238 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +6 | 462 |
| 239 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6014 |
| 240 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +6 | 10042 |
| 241 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +6 | 192 |
| 242 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 776 |
| 243 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5968 |
| 244 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 327 |
| 245 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +5 | 645 |
| 246 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 461 |
| 247 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 605 |
| 248 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1642 |
| 249 | [sparklabx/drawio-ai-kit](https://github.com/sparklabx/drawio-ai-kit) | +5 | 609 |
| 250 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 309 |
| 251 | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) | +5 | 1920 |
| 252 | [rpamis/comet](https://github.com/rpamis/comet) | +5 | 2507 |
| 253 | [rpanigrahi222/intruth-factcheck](https://github.com/rpanigrahi222/intruth-factcheck) | +5 | 562 |
| 254 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +5 | 3781 |
| 255 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +4 | 453 |
| 256 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +4 | 460 |
| 257 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +4 | 924 |
| 258 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 536 |
| 259 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 952 |
| 260 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 592 |
| 261 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +4 | 234 |
| 262 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 381 |
| 263 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 646 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +4 | 2808 |
| 265 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2921 |
| 266 | [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | +4 | 2946 |
| 267 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 684 |
| 268 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +4 | 974 |
| 269 | [NeteaseCloudMusicApiEnhanced/api-enhanced](https://github.com/NeteaseCloudMusicApiEnhanced/api-enhanced) | +3 | 1394 |
| 270 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 271 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 272 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9389 |
| 273 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 155 |
| 274 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2590 |
| 275 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +3 | 1873 |
| 276 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +3 | 566 |
| 277 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 265 |
| 278 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 107 |
| 279 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +3 | 129 |
| 280 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 26 |
| 281 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 251 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +3 | 2802 |
| 283 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 91 |
| 284 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 96 |
| 285 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +2 | 178 |
| 286 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 420 |
| 287 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 783 |
| 288 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 166 |
| 289 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 270 |
| 290 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 846 |
| 291 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +2 | 1701 |
| 292 | [xandergos/terrain-diffusion-mc](https://github.com/xandergos/terrain-diffusion-mc) | +2 | 762 |
| 293 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 710 |
| 294 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2431 |
| 295 | [lishuangqiang/AI-Meeting](https://github.com/lishuangqiang/AI-Meeting) | +2 | 748 |
| 296 | [floci-io/floci-az](https://github.com/floci-io/floci-az) | +2 | 342 |
| 297 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 298 | [vasuki-re/IStanPdf](https://github.com/vasuki-re/IStanPdf) | +2 | 118 |
| 299 | [xm486/YukiHub](https://github.com/xm486/YukiHub) | +2 | 0 |
| 300 | [w8123/EnterpriseAgentFramework](https://github.com/w8123/EnterpriseAgentFramework) | +2 | 517 |
