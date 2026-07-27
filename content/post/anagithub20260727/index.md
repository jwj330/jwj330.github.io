---
title: "2026-07-27 GitHub增长趋势报告"
description: "1.img2threejs+8 2.openworker+7 3.OpenMinis+6 4.ego-lite+6 5.impeccable+5"
date: 2026-07-27T21:11:37+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-07-27 21:11:37

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
        'daily': {"categories": ["KKKKhazix/khazix-skills", "ibelick/ui-skills", "lidge-jun/opencodex", "heygen-com/hyperframes", "calesthio/OpenMontage", "oso95/scroll-world", "diegosouzapw/OmniRoute", "MengTo/Skills", "stablyai/orca", "block/buzz", "hugohe3/ppt-master", "guohuiyuan/go-music-dl", "pascalorg/editor", "alibaba/open-code-review", "agentscope-ai/QwenPaw", "pbakaus/impeccable", "citrolabs/ego-lite", "OpenMinis/OpenMinis", "andrewyng/openworker", "img2threejs/img2threejs"], "data": [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 6, 6, 7, 8]},
        'weekly': {"categories": ["1jehuang/jcode", "ogulcancelik/herdr", "CoreBunch/Instatic", "tirth8205/code-review-graph", "iOfficeAI/OfficeCLI", "calesthio/OpenMontage", "agentscope-ai/QwenPaw", "rohitg00/ai-engineering-from-scratch", "pbakaus/impeccable", "lidge-jun/opencodex", "MadsLorentzen/ai-job-search", "citrolabs/ego-lite", "img2threejs/img2threejs", "unicity-aos/aos-ce", "oblien/openship", "baidu/Unlimited-OCR", "stablyai/orca", "andrewyng/openworker", "diegosouzapw/OmniRoute", "block/buzz"], "data": [11, 11, 11, 12, 14, 14, 14, 15, 15, 16, 21, 21, 21, 22, 23, 26, 27, 34, 43, 46]},
        'monthly': {"categories": ["hugohe3/ppt-master", "jamiepine/voicebox", "ZhuLinsen/daily_stock_analysis", "alibaba/page-agent", "XxHuberrr/Mineradio", "hasaneyldrm/exercises-dataset", "openai/codex-plugin-cc", "erincatto/box3d", "xbtlin/ai-berkshire", "facebook/astryx", "HKUDS/Vibe-Trading", "Zackriya-Solutions/meetily", "ogulcancelik/herdr", "stablyai/orca", "diegosouzapw/OmniRoute", "MadsLorentzen/ai-job-search", "langchain-ai/openwiki", "DeusData/codebase-memory-mcp", "calesthio/OpenMontage", "usestrix/strix"], "data": [104, 108, 109, 110, 113, 122, 123, 126, 130, 132, 137, 144, 146, 146, 155, 160, 188, 216, 226, 256]}
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
| 1 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +8 | 6835 |
| 2 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +7 | 8536 |
| 3 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +6 | 2244 |
| 4 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +6 | 5405 |
| 5 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +5 | 51447 |
| 6 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +5 | 29016 |
| 7 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +4 | 14696 |
| 8 | [pascalorg/editor](https://github.com/pascalorg/editor) | +3 | 18081 |
| 9 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +3 | 3734 |
| 10 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3 | 41412 |
| 11 | [block/buzz](https://github.com/block/buzz) | +3 | 14568 |
| 12 | [stablyai/orca](https://github.com/stablyai/orca) | +3 | 30705 |
| 13 | [MengTo/Skills](https://github.com/MengTo/Skills) | +3 | 3645 |
| 14 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +3 | 32043 |
| 15 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +3 | 5497 |
| 16 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2 | 42693 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2 | 38065 |
| 18 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +2 | 5286 |
| 19 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +2 | 6603 |
| 20 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +2 | 18391 |
| 21 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +2 | 35888 |
| 22 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +2 | 5349 |
| 23 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2 | 30111 |
| 24 | [nyblnet/bento](https://github.com/nyblnet/bento) | +2 | 2575 |
| 25 | [blader/humanizer](https://github.com/blader/humanizer) | +2 | 31547 |
| 26 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +2 | 27353 |
| 27 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +2 | 34668 |
| 28 | [oblien/openship](https://github.com/oblien/openship) | +2 | 8932 |
| 29 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2 | 30498 |
| 30 | [xuzhougeng/wisp-science](https://github.com/xuzhougeng/wisp-science) | +2 | 537 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [block/buzz](https://github.com/block/buzz) | +46 | 14568 |
| 2 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +43 | 32043 |
| 3 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +34 | 8536 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca) | +27 | 30705 |
| 5 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +26 | 19608 |
| 6 | [oblien/openship](https://github.com/oblien/openship) | +23 | 8932 |
| 7 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7606 |
| 8 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +21 | 6835 |
| 9 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +21 | 5405 |
| 10 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +21 | 27617 |
| 11 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +16 | 5286 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +15 | 51447 |
| 13 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +15 | 44201 |
| 14 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +14 | 29016 |
| 15 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +14 | 42693 |
| 16 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +14 | 22620 |
| 17 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +12 | 26899 |
| 18 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +11 | 6190 |
| 19 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +11 | 21433 |
| 20 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +11 | 12011 |
| 21 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +11 | 20116 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +11 | 47055 |
| 23 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +11 | 12581 |
| 24 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +10 | 14696 |
| 25 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +10 | 35888 |
| 26 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +9 | 38065 |
| 27 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +9 | 2212 |
| 28 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9 | 30498 |
| 29 | [usestrix/strix](https://github.com/usestrix/strix) | +9 | 44945 |
| 30 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +9 | 15188 |
| 31 | [floci-io/floci](https://github.com/floci-io/floci) | +8 | 17910 |
| 32 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +8 | 41412 |
| 33 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +8 | 28072 |
| 34 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +8 | 10992 |
| 35 | [penecho/penecho](https://github.com/penecho/penecho) | +8 | 1736 |
| 36 | [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | +7 | 2244 |
| 37 | [blader/humanizer](https://github.com/blader/humanizer) | +7 | 31547 |
| 38 | [nyblnet/bento](https://github.com/nyblnet/bento) | +7 | 2575 |
| 39 | [every-app/open-seo](https://github.com/every-app/open-seo) | +7 | 8598 |
| 40 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +7 | 12444 |
| 41 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +7 | 20224 |
| 42 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +7 | 7689 |
| 43 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +6 | 6617 |
| 44 | [multica-ai/multica](https://github.com/multica-ai/multica) | +6 | 42226 |
| 45 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +6 | 30360 |
| 46 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +6 | 41955 |
| 47 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +6 | 3208 |
| 48 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +6 | 39781 |
| 49 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | +6 | 1033 |
| 50 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +6 | 19860 |
| 51 | [agegr/pi-web](https://github.com/agegr/pi-web) | +6 | 2998 |
| 52 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +6 | 10814 |
| 53 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | +6 | 5349 |
| 54 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +6 | 6603 |
| 55 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +5 | 4858 |
| 56 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +5 | 42545 |
| 57 | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | +5 | 8637 |
| 58 | [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | +5 | 7973 |
| 59 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +5 | 7454 |
| 60 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 614 |
| 61 | [GaoSSR/best-claude-hud](https://github.com/GaoSSR/best-claude-hud) | +5 | 1398 |
| 62 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +5 | 31563 |
| 63 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +5 | 26819 |
| 64 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +5 | 3395 |
| 65 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5 | 46187 |
| 66 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +5 | 12505 |
| 67 | [aakk007/RogueCleaner](https://github.com/aakk007/RogueCleaner) | +5 | 179 |
| 68 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +5 | 12828 |
| 69 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +5 | 4384 |
| 70 | [facebook/astryx](https://github.com/facebook/astryx) | +5 | 10867 |
| 71 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +4 | 10515 |
| 72 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +4 | 21539 |
| 73 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +4 | 5497 |
| 74 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +4 | 34668 |
| 75 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +4 | 14427 |
| 76 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +4 | 12534 |
| 77 | [AdventDevInc/kudu](https://github.com/AdventDevInc/kudu) | +4 | 1750 |
| 78 | [browser-use/video-use](https://github.com/browser-use/video-use) | +4 | 17936 |
| 79 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +4 | 17168 |
| 80 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +4 | 1129 |
| 81 | [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | +4 | 35517 |
| 82 | [kurikomi-labs/komi-store](https://github.com/kurikomi-labs/komi-store) | +4 | 17065 |
| 83 | [nexu-io/codex-slides](https://github.com/nexu-io/codex-slides) | +4 | 635 |
| 84 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +4 | 29537 |
| 85 | [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | +4 | 12496 |
| 86 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 6884 |
| 87 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +3 | 59240 |
| 88 | [nitrocloudofficial/nitrostack](https://github.com/nitrocloudofficial/nitrostack) | +3 | 2164 |
| 89 | [pascalorg/editor](https://github.com/pascalorg/editor) | +3 | 18081 |
| 90 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +3 | 7128 |
| 91 | [guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl) | +3 | 3734 |
| 92 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +3 | 10953 |
| 93 | [MengTo/Skills](https://github.com/MengTo/Skills) | +3 | 3645 |
| 94 | [Charles-0509/Grok-Register](https://github.com/Charles-0509/Grok-Register) | +3 | 482 |
| 95 | [xuzhougeng/wisp-science](https://github.com/xuzhougeng/wisp-science) | +3 | 537 |
| 96 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +3 | 2585 |
| 97 | [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | +3 | 4860 |
| 98 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +3 | 9335 |
| 99 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +3 | 18391 |
| 100 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +3 | 3254 |
| 101 | [Rimagination/scansci-pdf](https://github.com/Rimagination/scansci-pdf) | +3 | 656 |
| 102 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +3 | 10755 |
| 103 | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | +3 | 2290 |
| 104 | [browser-act/skills](https://github.com/browser-act/skills) | +3 | 4849 |
| 105 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +3 | 4852 |
| 106 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +3 | 1811 |
| 107 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +3 | 13934 |
| 108 | [openai/skills](https://github.com/openai/skills) | +3 | 24242 |
| 109 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +3 | 8498 |
| 110 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +3 | 34298 |
| 111 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +3 | 4253 |
| 112 | [x4gKing/PasarGuard](https://github.com/x4gKing/PasarGuard) | +2 | 1210 |
| 113 | [x4gKing/PasarGuard-Node](https://github.com/x4gKing/PasarGuard-Node) | +2 | 1103 |
| 114 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +2 | 7811 |
| 115 | [CodeAbra/iai-personal-memory-engine](https://github.com/CodeAbra/iai-personal-memory-engine) | +2 | 399 |
| 116 | [AdelanSoulX/PM-Sniper](https://github.com/AdelanSoulX/PM-Sniper) | +2 | 413 |
| 117 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +2 | 1783 |
| 118 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +2 | 25788 |
| 119 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +2 | 44018 |
| 120 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +2 | 18254 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [usestrix/strix](https://github.com/usestrix/strix) | +256 | 44945 |
| 2 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +226 | 42693 |
| 3 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +216 | 35888 |
| 4 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +188 | 13372 |
| 5 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +160 | 27617 |
| 6 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +155 | 32043 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +146 | 30706 |
| 8 | [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | +146 | 21433 |
| 9 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +144 | 26996 |
| 10 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +137 | 28072 |
| 11 | [facebook/astryx](https://github.com/facebook/astryx) | +132 | 10867 |
| 12 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +130 | 14427 |
| 13 | [erincatto/box3d](https://github.com/erincatto/box3d) | +126 | 5602 |
| 14 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +123 | 30111 |
| 15 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +122 | 17168 |
| 16 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +113 | 9006 |
| 17 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +110 | 27989 |
| 18 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +109 | 59240 |
| 19 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +108 | 47055 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +104 | 41412 |
| 21 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +96 | 30360 |
| 22 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +86 | 12581 |
| 23 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +86 | 20116 |
| 24 | [topoteretes/cognee](https://github.com/topoteretes/cognee) | +86 | 29454 |
| 25 | [bikini/exploitarium](https://github.com/bikini/exploitarium) | +84 | 4119 |
| 26 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +78 | 21539 |
| 27 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +78 | 6754 |
| 28 | [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | +78 | 26484 |
| 29 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +77 | 9490 |
| 30 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +76 | 6617 |
| 31 | [browser-use/video-use](https://github.com/browser-use/video-use) | +75 | 17936 |
| 32 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +71 | 22620 |
| 33 | [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec) | +70 | 6784 |
| 34 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +68 | 19608 |
| 35 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +67 | 10992 |
| 36 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +66 | 51447 |
| 37 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +63 | 12444 |
| 38 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +63 | 31563 |
| 39 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +63 | 6528 |
| 40 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +61 | 15676 |
| 41 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +60 | 38065 |
| 42 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +60 | 7454 |
| 43 | [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice) | +57 | 8977 |
| 44 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +54 | 26727 |
| 45 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +53 | 39781 |
| 46 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +52 | 6190 |
| 47 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5262 |
| 48 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +50 | 42545 |
| 49 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +49 | 41955 |
| 50 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +49 | 26819 |
| 51 | [baairon/torlink](https://github.com/baairon/torlink) | +49 | 3877 |
| 52 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +48 | 47701 |
| 53 | [block/buzz](https://github.com/block/buzz) | +46 | 14569 |
| 54 | [oblien/openship](https://github.com/oblien/openship) | +46 | 8932 |
| 55 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +46 | 44201 |
| 56 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +46 | 17160 |
| 57 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +45 | 15188 |
| 58 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +45 | 20224 |
| 59 | [google-research/tabfm](https://github.com/google-research/tabfm) | +45 | 2178 |
| 60 | [unicity-sphere/sphere](https://github.com/unicity-sphere/sphere) | +44 | 9790 |
| 61 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +42 | 7689 |
| 62 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +41 | 34668 |
| 63 | [multica-ai/multica](https://github.com/multica-ai/multica) | +41 | 42226 |
| 64 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +40 | 6884 |
| 65 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +40 | 29016 |
| 66 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +40 | 23547 |
| 67 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +39 | 2381 |
| 68 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +38 | 19169 |
| 69 | [kunchenguid/no-mistakes](https://github.com/kunchenguid/no-mistakes) | +38 | 7128 |
| 70 | [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | +38 | 6593 |
| 71 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +38 | 10718 |
| 72 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +38 | 13856 |
| 73 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +37 | 5432 |
| 74 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +37 | 27353 |
| 75 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +37 | 2899 |
| 76 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +36 | 7811 |
| 77 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +36 | 10790 |
| 78 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +34 | 8536 |
| 79 | [decolua/9router](https://github.com/decolua/9router) | +33 | 23778 |
| 80 | [blader/humanizer](https://github.com/blader/humanizer) | +33 | 31547 |
| 81 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +33 | 10515 |
| 82 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +33 | 40607 |
| 83 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +33 | 11585 |
| 84 | [floci-io/floci](https://github.com/floci-io/floci) | +32 | 17910 |
| 85 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +32 | 23303 |
| 86 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +31 | 27899 |
| 87 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +31 | 2634 |
| 88 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +31 | 27214 |
| 89 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +31 | 2027 |
| 90 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +30 | 12534 |
| 91 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +30 | 2224 |
| 92 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +30 | 26431 |
| 93 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +28 | 26899 |
| 94 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +28 | 1445 |
| 95 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +27 | 30498 |
| 96 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +27 | 18413 |
| 97 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +27 | 28901 |
| 98 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +27 | 10001 |
| 99 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +26 | 5497 |
| 100 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +26 | 31919 |
| 101 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +26 | 25788 |
| 102 | [opensquilla/opensquilla](https://github.com/opensquilla/opensquilla) | +26 | 6376 |
| 103 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +25 | 6836 |
| 104 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +25 | 34298 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +25 | 46187 |
| 106 | [KittenML/KittenTTS](https://github.com/KittenML/KittenTTS) | +25 | 15233 |
| 107 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +24 | 6603 |
| 108 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +24 | 14697 |
| 109 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +24 | 1871 |
| 110 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +23 | 5405 |
| 111 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +23 | 12011 |
| 112 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +22 | 7606 |
| 113 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +22 | 44018 |
| 114 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +22 | 26126 |
| 115 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +22 | 8498 |
| 116 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +22 | 1463 |
| 117 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +21 | 0 |
| 118 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +20 | 12505 |
| 119 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +20 | 4253 |
| 120 | [asz798838958/freeAgentIdentity](https://github.com/asz798838958/freeAgentIdentity) | +20 | 1129 |
| 121 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +20 | 7193 |
| 122 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4284 |
| 123 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +19 | 5286 |
| 124 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 4858 |
| 125 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +19 | 29259 |
| 126 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +19 | 18254 |
| 127 | [larlarua/AutoCVE](https://github.com/larlarua/AutoCVE) | +19 | 1262 |
| 128 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1969 |
| 129 | [openai/plugins](https://github.com/openai/plugins) | +19 | 4767 |
| 130 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 7910 |
| 131 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +18 | 6719 |
| 132 | [WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh) | +18 | 4892 |
| 133 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +18 | 10814 |
| 134 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +17 | 3254 |
| 135 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +17 | 3208 |
| 136 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +17 | 18391 |
| 137 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +17 | 2035 |
| 138 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +17 | 8189 |
| 139 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +17 | 7286 |
| 140 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +16 | 10953 |
| 141 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +16 | 9160 |
| 142 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +16 | 5468 |
| 143 | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | +16 | 3275 |
| 144 | [lzh-phd/topic-feasibility-screener](https://github.com/lzh-phd/topic-feasibility-screener) | +16 | 481 |
| 145 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +16 | 4728 |
| 146 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +16 | 2888 |
| 147 | [browser-act/skills](https://github.com/browser-act/skills) | +15 | 4849 |
| 148 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +15 | 32751 |
| 149 | [anbeime/skill](https://github.com/anbeime/skill) | +15 | 4298 |
| 150 | [huohua325/Memslides](https://github.com/huohua325/Memslides) | +15 | 839 |
| 151 | [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) | +15 | 1695 |
| 152 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +15 | 5056 |
| 153 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +15 | 405 |
| 154 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +14 | 5307 |
| 155 | [openai/skills](https://github.com/openai/skills) | +14 | 24242 |
| 156 | [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | +14 | 4203 |
| 157 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +14 | 27285 |
| 158 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +14 | 3815 |
| 159 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +14 | 2230 |
| 160 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +13 | 991 |
| 161 | [jundot/omlx](https://github.com/jundot/omlx) | +13 | 18230 |
| 162 | [jmerelnyc/Talos](https://github.com/jmerelnyc/Talos) | +13 | 891 |
| 163 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +13 | 1034 |
| 164 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +12 | 5676 |
| 165 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +12 | 27479 |
| 166 | [generative-computing/mellea](https://github.com/generative-computing/mellea) | +12 | 1783 |
| 167 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +12 | 15346 |
| 168 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +12 | 10049 |
| 169 | [Hypostasis-Cat/HypoMux](https://github.com/Hypostasis-Cat/HypoMux) | +12 | 1867 |
| 170 | [FB208/OpenBidKit_Yibiao](https://github.com/FB208/OpenBidKit_Yibiao) | +12 | 2130 |
| 171 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +12 | 4919 |
| 172 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +11 | 9335 |
| 173 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +11 | 16623 |
| 174 | [datascale-ai/opentalking](https://github.com/datascale-ai/opentalking) | +11 | 2529 |
| 175 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 13934 |
| 176 | [jiujiu532/grok2api](https://github.com/jiujiu532/grok2api) | +11 | 1865 |
| 177 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1736 |
| 178 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +11 | 29537 |
| 179 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +11 | 8125 |
| 180 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 727 |
| 181 | [nullpointexception-i/agent-sphere](https://github.com/nullpointexception-i/agent-sphere) | +11 | 143 |
| 182 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +11 | 27932 |
| 183 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +10 | 9451 |
| 184 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +10 | 4833 |
| 185 | [lingbol088-spec/reverse-flow-skill](https://github.com/lingbol088-spec/reverse-flow-skill) | +10 | 592 |
| 186 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +10 | 891 |
| 187 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +10 | 18563 |
| 188 | [joaogfc/ZeroDelay](https://github.com/joaogfc/ZeroDelay) | +10 | 434 |
| 189 | [tess1o/geopulse](https://github.com/tess1o/geopulse) | +10 | 1322 |
| 190 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +9 | 1811 |
| 191 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +9 | 1488 |
| 192 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +9 | 8937 |
| 193 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +9 | 5287 |
| 194 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +9 | 4678 |
| 195 | [hyqzz/Solar-Wanderer](https://github.com/hyqzz/Solar-Wanderer) | +9 | 682 |
| 196 | [AaronL725/grok-register](https://github.com/AaronL725/grok-register) | +8 | 1680 |
| 197 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +8 | 7273 |
| 198 | [Silentely/eSIM-Tools](https://github.com/Silentely/eSIM-Tools) | +8 | 2039 |
| 199 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3056 |
| 200 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +7 | 1378 |
| 201 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +7 | 985 |
| 202 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +7 | 26865 |
| 203 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +7 | 3008 |
| 204 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +7 | 5666 |
| 205 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +7 | 9180 |
| 206 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +7 | 1111 |
| 207 | [LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg](https://github.com/LuanSantana0/Polymarket-Trading-Bot-BTC-5-Minute-Up-Down-Dual-Leg) | +7 | 0 |
| 208 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +7 | 699 |
| 209 | [simonmakzon/GitDeepSearch](https://github.com/simonmakzon/GitDeepSearch) | +7 | 167 |
| 210 | [techjarves/Uncensored-Local-Studio](https://github.com/techjarves/Uncensored-Local-Studio) | +7 | 745 |
| 211 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +7 | 619 |
| 212 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +6 | 2646 |
| 213 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +6 | 3064 |
| 214 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +6 | 8817 |
| 215 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +6 | 6266 |
| 216 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +6 | 2670 |
| 217 | [rebel0789/codexpro](https://github.com/rebel0789/codexpro) | +6 | 1432 |
| 218 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 6015 |
| 219 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +6 | 3015 |
| 220 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 832 |
| 221 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 614 |
| 222 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 995 |
| 223 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +5 | 1122 |
| 224 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +5 | 327 |
| 225 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +5 | 12051 |
| 226 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +5 | 513 |
| 227 | [Johell1NS/browser-search](https://github.com/Johell1NS/browser-search) | +5 | 465 |
| 228 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +5 | 615 |
| 229 | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | +5 | 2861 |
| 230 | [qqxpee/antigravity2-cn](https://github.com/qqxpee/antigravity2-cn) | +5 | 317 |
| 231 | [truelockmc/streambert](https://github.com/truelockmc/streambert) | +5 | 5873 |
| 232 | [Webba-Creative-Technologies/vice](https://github.com/Webba-Creative-Technologies/vice) | +5 | 563 |
| 233 | [NotASithLord/peerd](https://github.com/NotASithLord/peerd) | +5 | 371 |
| 234 | [XBuilderLAB/cheat-on-skill](https://github.com/XBuilderLAB/cheat-on-skill) | +5 | 154 |
| 235 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +5 | 4735 |
| 236 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +5 | 3332 |
| 237 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14417 |
| 238 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +4 | 5993 |
| 239 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +4 | 455 |
| 240 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 671 |
| 241 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +4 | 537 |
| 242 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1001 |
| 243 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 615 |
| 244 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +4 | 234 |
| 245 | [QLHazyCoder/FlowPilot](https://github.com/QLHazyCoder/FlowPilot) | +4 | 5065 |
| 246 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +4 | 385 |
| 247 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 166 |
| 248 | [gtxx3600/GPTSession2CPAandSub2API](https://github.com/gtxx3600/GPTSession2CPAandSub2API) | +4 | 1656 |
| 249 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 650 |
| 250 | [feicaiclub/video-spec-builder](https://github.com/feicaiclub/video-spec-builder) | +4 | 845 |
| 251 | [AGI-comming/functional-skill-creator](https://github.com/AGI-comming/functional-skill-creator) | +4 | 462 |
| 252 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 720 |
| 253 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +4 | 10052 |
| 254 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +4 | 2948 |
| 255 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +3 | 10783 |
| 256 | [Quantova/Qweb4.js](https://github.com/Quantova/Qweb4.js) | +3 | 0 |
| 257 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +3 | 468 |
| 258 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 142 |
| 259 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 354 |
| 260 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 68 |
| 261 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 392 |
| 262 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6503 |
| 263 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9390 |
| 264 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2845 |
| 265 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +3 | 1007 |
| 266 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 157 |
| 267 | [Crystaelix/Create-Simurail](https://github.com/Crystaelix/Create-Simurail) | +3 | 112 |
| 268 | [eooce/transfer-api](https://github.com/eooce/transfer-api) | +2 | 463 |
| 269 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 336 |
| 270 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +2 | 3805 |
| 271 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +2 | 92 |
| 272 | [XiaoTong6666/Sui](https://github.com/XiaoTong6666/Sui) | +2 | 571 |
| 273 | [EVV1E/waylandcraft](https://github.com/EVV1E/waylandcraft) | +2 | 2594 |
| 274 | [SGUDestiny/PenumbraPhantasm](https://github.com/SGUDestiny/PenumbraPhantasm) | +2 | 97 |
| 275 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 425 |
| 276 | [mateaix/mateclaw](https://github.com/mateaix/mateclaw) | +2 | 796 |
| 277 | [IIIIIllllIIIIIlllll/llama.cpp-hub](https://github.com/IIIIIllllIIIIIlllll/llama.cpp-hub) | +2 | 279 |
| 278 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +2 | 846 |
| 279 | [jean-voila/FeurStagram](https://github.com/jean-voila/FeurStagram) | +2 | 717 |
| 280 | [datallmhub/claude-governance](https://github.com/datallmhub/claude-governance) | +2 | 0 |
| 281 | [medievalrp-net/Spyglass](https://github.com/medievalrp-net/Spyglass) | +2 | 28 |
| 282 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 661 |
| 283 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +2 | 10451 |
| 284 | [kknifer7/FreeBox](https://github.com/kknifer7/FreeBox) | +2 | 1786 |
| 285 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 824 |
| 286 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 65 |
| 287 | [Margele/OpenZen](https://github.com/Margele/OpenZen) | +1 | 254 |
| 288 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 138 |
| 289 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 309 |
| 290 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 88 |
| 291 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 81 |
| 292 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 54 |
| 293 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 25 |
| 294 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1894 |
| 295 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 155 |
| 296 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 297 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 169 |
| 298 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 43 |
| 299 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +1 | 268 |
| 300 | [adityatandon15/Spring-Framework-Full-Course](https://github.com/adityatandon15/Spring-Framework-Full-Course) | +1 | 188 |
