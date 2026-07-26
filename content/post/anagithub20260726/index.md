---
title: "2026-07-26 GitHub增长趋势报告"
description: "1.buzz+9 2.Instatic+7 3.floci+6 4.QwenPaw+6 5.OmniRoute+5"
date: 2026-07-26T20:59:15+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-26 20:59:15

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
        'daily': {"categories": ["lidge-jun/opencodex", "pbakaus/impeccable", "ogulcancelik/herdr", "virgiliojr94/book-to-skill", "DeusData/codebase-memory-mcp", "img2threejs/img2threejs", "oblien/openship", "MadsLorentzen/ai-job-search", "HKUDS/DeepTutor", "citrolabs/ego-lite", "Yuan1z0825/nature-skills", "iOfficeAI/OfficeCLI", "heygen-com/hyperframes", "1jehuang/jcode", "stablyai/orca", "diegosouzapw/OmniRoute", "agentscope-ai/QwenPaw", "floci-io/floci", "CoreBunch/Instatic", "block/buzz"], "data": [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 9]},
        'weekly': {"categories": ["CoreBunch/Instatic", "jamiepine/voicebox", "usestrix/strix", "calesthio/OpenMontage", "Fei-Away/Codex-Dream-Skin", "1jehuang/jcode", "ogulcancelik/herdr", "iOfficeAI/OfficeCLI", "citrolabs/ego-lite", "tirth8205/code-review-graph", "lidge-jun/opencodex", "img2threejs/img2threejs", "rohitg00/ai-engineering-from-scratch", "unicity-aos/aos-ce", "MadsLorentzen/ai-job-search", "baidu/Unlimited-OCR", "stablyai/orca", "oblien/openship", "diegosouzapw/OmniRoute", "block/buzz"], "data": [11, 12, 12, 12, 13, 13, 14, 15, 15, 16, 16, 16, 19, 22, 23, 24, 25, 30, 43, 43]},
        'monthly': {"categories": ["hasaneyldrm/exercises-dataset", "hugohe3/ppt-master", "openai/codex-plugin-cc", "erincatto/box3d", "JCodesMore/ai-website-cloner-template", "HKUDS/Vibe-Trading", "facebook/astryx", "google-labs-code/design.md", "simplex-chat/simplex-chat", "Zackriya-Solutions/meetily", "diegosouzapw/OmniRoute", "stablyai/orca", "xbtlin/ai-berkshire", "MadsLorentzen/ai-job-search", "XxHuberrr/Mineradio", "ogulcancelik/herdr", "langchain-ai/openwiki", "usestrix/strix", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage"], "data": [123, 124, 124, 126, 131, 137, 140, 142, 143, 145, 155, 158, 159, 160, 165, 165, 188, 257, 282, 291]}
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
| 1 | [block/buzz](https://github.com/block/buzz) | +9 | 13010 |
| 2 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +7 | 5577 |
| 3 | [floci-io/floci](https://github.com/floci-io/floci) | +6 | 17763 |
| 4 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +6 | 27894 |
| 5 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +5 | 30925 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +4 | 29576 |
| 7 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +4 | 11641 |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +4 | 37818 |
| 9 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +4 | 22358 |
| 10 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +3 | 31318 |
| 11 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +3 | 4365 |
| 12 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3 | 30051 |
| 13 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3 | 27247 |
| 14 | [oblien/openship](https://github.com/oblien/openship) | +2 | 8713 |
| 15 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +2 | 5552 |
| 16 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 35560 |
| 17 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +2 | 10063 |
| 18 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +2 | 21020 |
| 19 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2 | 50554 |
| 20 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +2 | 4962 |
| 21 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +2 | 35461 |
| 22 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +2 | 14200 |
| 23 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +2 | 19792 |
| 24 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +2 | 19865 |
| 25 | [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | +2 | 4845 |
| 26 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +2 | 5905 |
| 27 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +2 | 2165 |
| 28 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +2 | 7396 |
| 29 | [AdventDevInc/kudu](https://github.com/AdventDevInc/kudu) | +2 | 1689 |
| 30 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +2 | 12351 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +43 | 13010 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +43 | 30925 |
| 3 | [oblien/openship](https://github.com/oblien/openship) | +30 | 8713 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +25 | 29576 |
| 5 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +24 | 19278 |
| 6 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +23 | 27247 |
| 7 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7396 |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +19 | 43726 |
| 9 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +16 | 5553 |
| 10 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +16 | 4963 |
| 11 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +16 | 26578 |
| 12 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +15 | 4365 |
| 13 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +15 | 22358 |
| 14 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +14 | 21020 |
| 15 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +13 | 11641 |
| 16 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +13 | 12351 |
| 17 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +12 | 42438 |
| 18 | [usestrix/strix](https://github.com/usestrix/strix) | +12 | 44490 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +12 | 46898 |
| 20 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +11 | 5577 |
| 21 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 19568 |
| 22 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +10 | 50554 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +10 | 27807 |
| 24 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +10 | 15109 |
| 25 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10 | 30051 |
| 26 | [floci-io/floci](https://github.com/floci-io/floci) | +9 | 17763 |
| 27 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +9 | 27894 |
| 28 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +9 | 35560 |
| 29 | [penecho/penecho](https://github.com/penecho/penecho) | +9 | 1674 |
| 30 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +9 | 19865 |
| 31 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +9 | 12282 |
| 32 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +8 | 1889 |
| 33 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +8 | 6532 |
| 34 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +8 | 10402 |
| 35 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +8 | 10882 |
| 36 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +7 | 37818 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +7 | 31318 |
| 38 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +7 | 41805 |
| 39 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 8205 |
| 40 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +7 | 6530 |
| 41 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +6 | 13693 |
| 42 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42085 |
| 43 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 2956 |
| 44 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +6 | 39618 |
| 45 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +6 | 19792 |
| 46 | [agegr/pi-web](https://github.com/agegr/pi-web) | +6 | 2859 |
| 47 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +6 | 26690 |
| 48 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +6 | 21038 |
| 49 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +6 | 7542 |
| 50 | [kurikomi-labs/komi-store](https://github.com/kurikomi-labs/komi-store) | +6 | 17033 |
| 51 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +5 | 30270 |
| 52 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 7859 |
| 53 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +5 | 7356 |
| 54 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +5 | 35461 |
| 55 | [blader/humanizer](https://github.com/blader/humanizer) | +5 | 31192 |
| 56 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +5 | 3356 |
| 57 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5 | 41198 |
| 58 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +5 | 12677 |
| 59 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +5 | 1229 |
| 60 | [nyblnet/bento](https://github.com/nyblnet/bento) | +5 | 2155 |
| 61 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 4132 |
| 62 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +5 | 10495 |
| 63 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 10780 |
| 64 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 46117 |
| 65 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +5 | 8111 |
| 66 | [Julian-adv/OpenMMO](https://github.com/Julian-adv/OpenMMO) | +5 | 1419 |
| 67 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +5 | 5175 |
| 68 | [stupside/castor](https://github.com/stupside/castor) | +5 | 1922 |
| 69 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +4 | 6802 |
| 70 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +4 | 42397 |
| 71 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 17869 |
| 72 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +4 | 12432 |
| 73 | [AdventDevInc/kudu](https://github.com/AdventDevInc/kudu) | +4 | 1689 |
| 74 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +4 | 4776 |
| 75 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +4 | 3062 |
| 76 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +4 | 8560 |
| 77 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 17008 |
| 78 | [nexu-io/codex-slides](https://github.com/nexu-io/codex-slides) | +4 | 558 |
| 79 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +4 | 44666 |
| 80 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +4 | 5905 |
| 81 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +4 | 29506 |
| 82 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +4 | 12470 |
| 83 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4 | 12397 |
| 84 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +4 | 137 |
| 85 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +4 | 27808 |
| 86 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +4 | 34243 |
| 87 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +4 | 2367 |
| 88 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2166 |
| 89 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 59022 |
| 90 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +3 | 7099 |
| 91 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 10063 |
| 92 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +3 | 14200 |
| 93 | [mesamirh/MovieBox-Tui](https://github.com/mesamirh/MovieBox-Tui) | +3 | 720 |
| 94 | [evolution-foundation/evolution-go](https://github.com/evolution-foundation/evolution-go) | +3 | 539 |
| 95 | [NeuroAIHub/BrainPilot](https://github.com/NeuroAIHub/BrainPilot) | +3 | 118 |
| 96 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +3 | 2233 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +3 | 34461 |
| 98 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 4813 |
| 99 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4837 |
| 100 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +3 | 1717 |
| 101 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +3 | 13885 |
| 102 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +3 | 8471 |
| 103 | [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director) | +3 | 445 |
| 104 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +3 | 4240 |
| 105 | [Qualcomm-AI-research/MobileWan](https://github.com/Qualcomm-AI-research/MobileWan) | +3 | 85 |
| 106 | [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) | +3 | 1115 |
| 107 | [tw93/Waza](https://github.com/tw93/Waza) | +3 | 6638 |
| 108 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +2 | 5259 |
| 109 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2 | 40575 |
| 110 | [OpenOSINT/OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | +2 | 1187 |
| 111 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +2 | 1771 |
| 112 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +2 | 9267 |
| 113 | [jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch) | +2 | 1380 |
| 114 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +2 | 16580 |
| 115 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +2 | 6643 |
| 116 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2 | 13817 |
| 117 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +2 | 4867 |
| 118 | [PhyAgentOS/PhyAgentOS](https://github.com/PhyAgentOS/PhyAgentOS) | +2 | 1101 |
| 119 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +2 | 32697 |
| 120 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +2 | 359 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +291 | 42438 |
| 2 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +282 | 35560 |
| 3 | [usestrix/strix](https://github.com/usestrix/strix) | +257 | 44490 |
| 4 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 13288 |
| 5 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +165 | 21020 |
| 6 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +165 | 8952 |
| 7 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +160 | 27247 |
| 8 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +159 | 14200 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +158 | 29576 |
| 10 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 30925 |
| 11 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +145 | 26806 |
| 12 | [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat) | +143 | 19074 |
| 13 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +142 | 26435 |
| 14 | [facebook/astryx](https://github.com/facebook/astryx) | +140 | 10780 |
| 15 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +137 | 27807 |
| 16 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +131 | 30270 |
| 17 | [erincatto/box3d](https://github.com/erincatto/box3d) | +126 | 5571 |
| 18 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +124 | 29990 |
| 19 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +124 | 41198 |
| 20 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +123 | 17008 |
| 21 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +122 | 59022 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +121 | 46898 |
| 23 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +120 | 27899 |
| 24 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +110 | 29391 |
| 25 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +106 | 9435 |
| 26 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +106 | 4104 |
| 27 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +100 | 19278 |
| 28 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +93 | 6532 |
| 29 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +86 | 12282 |
| 30 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +85 | 19568 |
| 31 | [browser-use/video-use](https://github.com/browser-use/video-use) | +84 | 17869 |
| 32 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +81 | 6775 |
| 33 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +79 | 21038 |
| 34 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +77 | 6728 |
| 35 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +74 | 50554 |
| 36 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +71 | 22358 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +71 | 31318 |
| 38 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +71 | 15543 |
| 39 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +70 | 5577 |
| 40 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +69 | 6460 |
| 41 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +67 | 10402 |
| 42 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +63 | 12351 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +63 | 37818 |
| 44 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +63 | 39618 |
| 45 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +63 | 7099 |
| 46 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +63 | 8908 |
| 47 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +63 | 10639 |
| 48 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +62 | 26641 |
| 49 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +62 | 17084 |
| 50 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +61 | 7356 |
| 51 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +58 | 42397 |
| 52 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +55 | 26690 |
| 53 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +51 | 15109 |
| 54 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +51 | 47643 |
| 55 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +50 | 43726 |
| 56 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5219 |
| 57 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +50 | 41805 |
| 58 | [baairon/torlink](https://github.com/baairon/torlink) | +49 | 3855 |
| 59 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +48 | 19865 |
| 60 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +48 | 7542 |
| 61 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +45 | 13817 |
| 62 | [oblien/openship](https://github.com/oblien/openship) | +44 | 8713 |
| 63 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +44 | 23513 |
| 64 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +44 | 35461 |
| 65 | [antirez/ds4](https://github.com/antirez/ds4) | +44 | 19256 |
| 66 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9788 |
| 67 | [block/buzz](https://github.com/block/buzz) | +43 | 13010 |
| 68 | [google-research/tabfm](https://github.com/google-research/tabfm) | +43 | 2134 |
| 69 | [multica-ai/multica](https://github.com/multica-ai/multica) | +42 | 42085 |
| 70 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +42 | 27808 |
| 71 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +42 | 11556 |
| 72 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +41 | 6564 |
| 73 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +40 | 6802 |
| 74 | [blader/humanizer](https://github.com/blader/humanizer) | +40 | 31192 |
| 75 | [every-app/open-seo](https://github.com/every-app/open-seo) | +40 | 8205 |
| 76 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +39 | 34461 |
| 77 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +39 | 19089 |
| 78 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +39 | 27260 |
| 79 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +39 | 26379 |
| 80 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +38 | 5361 |
| 81 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +38 | 2371 |
| 82 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10697 |
| 83 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +38 | 27154 |
| 84 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +37 | 27894 |
| 85 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +37 | 23236 |
| 86 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +37 | 40575 |
| 87 | [decolua/9router](https://github.com/decolua/9router) | +36 | 23652 |
| 88 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +36 | 7778 |
| 89 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +36 | 2762 |
| 90 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +35 | 9957 |
| 91 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +34 | 2027 |
| 92 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +33 | 10063 |
| 93 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +33 | 12432 |
| 94 | [floci-io/floci](https://github.com/floci-io/floci) | +32 | 17763 |
| 95 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +32 | 46117 |
| 96 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +31 | 26578 |
| 97 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +31 | 28824 |
| 98 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +31 | 2215 |
| 99 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2623 |
| 100 | [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | +30 | 7786 |
| 101 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +29 | 18357 |
| 102 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +29 | 34243 |
| 103 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1421 |
| 104 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +28 | 6354 |
| 105 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +27 | 31836 |
| 106 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +27 | 8471 |
| 107 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +27 | 25753 |
| 108 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +26 | 12397 |
| 109 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +26 | 15236 |
| 110 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +25 | 30051 |
| 111 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +25 | 43959 |
| 112 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +25 | 29202 |
| 113 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +25 | 1258 |
| 114 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +24 | 11641 |
| 115 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +24 | 26063 |
| 116 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1859 |
| 117 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +23 | 5339 |
| 118 | [openai/plugins](https://github.com/openai/plugins) | +23 | 4751 |
| 119 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7396 |
| 120 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1451 |
| 121 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +22 | 7136 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +21 | 18213 |
| 123 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +21 | 1691 |
| 124 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 125 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +20 | 6643 |
| 126 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 4240 |
| 127 | [zanetanasta/Seed-Generator](https://github.com/zanetanasta/Seed-Generator) | +20 | 0 |
| 128 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4221 |
| 129 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +20 | 8111 |
| 130 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +20 | 10495 |
| 131 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +20 | 7234 |
| 132 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +19 | 10017 |
| 133 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1968 |
| 134 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +18 | 4776 |
| 135 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +18 | 10882 |
| 136 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7901 |
| 137 | [openai/skills](https://github.com/openai/skills) | +18 | 24200 |
| 138 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +18 | 4867 |
| 139 | [0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai) | +18 | 1438 |
| 140 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | +18 | 2127 |
| 141 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +17 | 5259 |
| 142 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +17 | 5553 |
| 143 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 3062 |
| 144 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +17 | 9109 |
| 145 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 2957 |
| 146 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2023 |
| 147 | [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) | +17 | 1755 |
| 148 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +17 | 763 |
| 149 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +17 | 4365 |
| 150 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +17 | 27246 |
| 151 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +17 | 2876 |
| 152 | [browser-act/skills](https://github.com/browser-act/skills) | +16 | 4813 |
| 153 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3262 |
| 154 | [anbeime/skill](https://github.com/anbeime/skill) | +16 | 4229 |
| 155 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 156 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +16 | 4160 |
| 157 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4643 |
| 158 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +16 | 5034 |
| 159 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +16 | 2174 |
| 160 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +15 | 32697 |
| 161 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +15 | 17961 |
| 162 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +15 | 23056 |
| 163 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 405 |
| 164 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +15 | 3794 |
| 165 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +14 | 15322 |
| 166 | [jundot/omlx](https://github.com/jundot/omlx) | +14 | 18196 |
| 167 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +14 | 3631 |
| 168 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +13 | 16580 |
| 169 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +13 | 27255 |
| 170 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +13 | 985 |
| 171 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 891 |
| 172 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +13 | 2098 |
| 173 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +13 | 29506 |
| 174 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1032 |
| 175 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +13 | 8086 |
| 176 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +13 | 7240 |
| 177 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +12 | 9267 |
| 178 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1781 |
| 179 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +12 | 4624 |
| 180 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4901 |
| 181 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +12 | 27883 |
| 182 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2522 |
| 183 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 13885 |
| 184 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1674 |
| 185 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +11 | 8887 |
| 186 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 726 |
| 187 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +11 | 18534 |
| 188 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +11 | 680 |
| 189 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 159 |
| 190 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +10 | 9401 |
| 191 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +10 | 4790 |
| 192 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 578 |
| 193 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 888 |
| 194 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 434 |
| 195 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1316 |
| 196 | [google/skills](https://github.com/google/skills) | +9 | 15267 |
| 197 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1468 |
| 198 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5261 |
| 199 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +9 | 1117 |
| 200 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +9 | 371 |
| 201 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +9 | 610 |
| 202 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1657 |
| 203 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +8 | 3016 |
| 204 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +8 | 973 |
| 205 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +8 | 26824 |
| 206 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +8 | 2990 |
| 207 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +8 | 8749 |
| 208 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +8 | 731 |
| 209 | [lixiaolin94/skills](https://github.com/lixiaolin94/skills) | +8 | 717 |
| 210 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +7 | 1323 |
| 211 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +7 | 3049 |
| 212 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +7 | 6253 |
| 213 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5650 |
| 214 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +7 | 12030 |
| 215 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +7 | 9166 |
| 216 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +7 | 2002 |
| 217 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +7 | 2659 |
| 218 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1097 |
| 219 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 220 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +7 | 694 |
| 221 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +7 | 2847 |
| 222 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +7 | 1415 |
| 223 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 167 |
| 224 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +7 | 4713 |
| 225 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2620 |
| 226 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +6 | 502 |
| 227 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +6 | 6488 |
| 228 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +6 | 562 |
| 229 | [ziwang-Physics/AgentChat](https://github.com/ziwang-Physics/AgentChat) | +6 | 429 |
| 230 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6015 |
| 231 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3005 |
| 232 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 808 |
| 233 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 975 |
| 234 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 326 |
| 235 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +5 | 5986 |
| 236 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 463 |
| 237 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 608 |
| 238 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +5 | 5057 |
| 239 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +5 | 1651 |
| 240 | [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) | +5 | 2746 |
| 241 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 315 |
| 242 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +5 | 5869 |
| 243 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +5 | 462 |
| 244 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +5 | 3321 |
| 245 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +5 | 708 |
| 246 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +5 | 10054 |
| 247 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +4 | 469 |
| 248 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14403 |
| 249 | [byJoey/cfnew-deployer](https://github.com/byJoey/cfnew-deployer) | +4 | 650 |
| 250 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 537 |
| 251 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +4 | 388 |
| 252 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 988 |
| 253 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 607 |
| 254 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +4 | 234 |
| 255 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 383 |
| 256 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 165 |
| 257 | [huilang-me/CF-Server-Monitor](https://github.com/huilang-me/CF-Server-Monitor) | +4 | 946 |
| 258 | [kimsh-1/gongnyang-prompt-kit](https://github.com/kimsh-1/gongnyang-prompt-kit) | +4 | 288 |
| 259 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2940 |
| 260 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 261 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 262 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +3 | 440 |
| 263 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 349 |
| 264 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 67 |
| 265 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9391 |
| 266 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2835 |
| 267 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +3 | 3797 |
| 268 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 157 |
| 269 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +3 | 2590 |
| 270 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +3 | 267 |
| 271 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 108 |
| 272 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 996 |
| 273 | [secondly-com/OpenPhone](https://github.com/secondly-com/OpenPhone) | +3 | 193 |
| 274 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +3 | 27 |
| 275 | [Mininglamp-OSS/octo-android](https://github.com/Mininglamp-OSS/octo-android) | +3 | 258 |
| 276 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +2 | 463 |
| 277 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 278 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +2 | 1885 |
| 279 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 570 |
| 280 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 97 |
| 281 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 424 |
| 282 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 788 |
| 283 | [klboke/kkRepo](https://github.com/klboke/kkRepo) | +2 | 168 |
| 284 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 277 |
| 285 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 845 |
| 286 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 712 |
| 287 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +2 | 2439 |
| 288 | [SpringSunYY/LZ-litchi](https://github.com/SpringSunYY/LZ-litchi) | +2 | 129 |
| 289 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 290 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 653 |
| 291 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +2 | 10441 |
| 292 | [kknifer7/FreeBox](https://github.com/kknifer7/FreeBox) | +2 | 1784 |
| 293 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 823 |
| 294 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 64 |
| 295 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 254 |
| 296 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 310 |
| 297 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 88 |
| 298 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 81 |
| 299 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 300 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 25 |
