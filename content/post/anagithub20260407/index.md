---
title: "2026-04-07 GitHub增长趋势报告"
description: "1.awesome-design-md+1679 2.graphify+686 3.agent-skills+650 4.caveman+479 5.hermes-agent+425"
date: 2026-04-07T20:51:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-07 20:51:19

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
        'daily': {"categories": ["GitFrog1111/badclaude", "Yeachan-Heo/oh-my-claudecode", "tobi/qmd", "xandemon/developer-icons", "paperclipai/paperclip", "KeygraphHQ/shannon", "Yeachan-Heo/oh-my-codex", "google-ai-edge/gallery", "matthartman/ghost-pepper", "chenglou/pretext", "kepano/obsidian-skills", "luongnv89/claude-howto", "block/goose", "abhigyanpatwari/GitNexus", "siddharthvaddem/openscreen", "NousResearch/hermes-agent", "JuliusBrussee/caveman", "addyosmani/agent-skills", "safishamsi/graphify", "VoltAgent/awesome-design-md"], "data": [140, 154, 156, 159, 167, 176, 193, 195, 198, 204, 208, 236, 240, 256, 335, 425, 479, 650, 686, 1679]},
        'weekly': {"categories": ["block/goose", "onyx-dot-app/onyx", "openai/codex-plugin-cc", "ultraworkers/claw-code-parity", "garrytan/gstack", "paperclipai/paperclip", "Yeachan-Heo/oh-my-claudecode", "sanbuphy/learn-coding-agent", "msitarzewski/agency-agents", "addyosmani/agent-skills", "luongnv89/claude-howto", "NousResearch/hermes-agent", "obra/superpowers", "Yeachan-Heo/oh-my-codex", "chenglou/pretext", "siddharthvaddem/openscreen", "anthropics/claude-code", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "ultraworkers/claw-code"], "data": [1155, 1225, 1275, 1295, 1319, 1340, 1355, 1362, 1398, 1740, 1834, 1896, 2108, 2648, 2801, 3139, 3546, 3690, 5882, 22941]},
        'monthly': {"categories": ["nextlevelbuilder/ui-ux-pro-max-skill", "anomalyco/opencode", "gsd-build/get-shit-done", "anthropics/skills", "shareAI-lab/learn-claude-code", "NousResearch/hermes-agent", "bytedance/deer-flow", "anthropics/claude-code", "HKUDS/CLI-Anything", "VoltAgent/awesome-design-md", "chenglou/pretext", "paperclipai/paperclip", "666ghj/MiroFish", "obra/superpowers", "garrytan/gstack", "msitarzewski/agency-agents", "karpathy/autoresearch", "affaan-m/everything-claude-code", "openclaw/openclaw", "ultraworkers/claw-code"], "data": [3715, 3920, 4064, 4586, 4648, 4659, 5300, 5384, 5403, 5886, 6162, 8096, 8530, 11152, 11458, 12002, 13084, 13998, 16247, 22942]}
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
| 1 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1679 | 29386 |
| 2 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +686 | 6210 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +650 | 8188 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +479 | 5755 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +425 | 31221 |
| 6 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +335 | 25084 |
| 7 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +256 | 24391 |
| 8 | [block/goose](https://github.com/block/goose) | +240 | 31098 |
| 9 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +236 | 22303 |
| 10 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +208 | 21329 |
| 11 | [chenglou/pretext](https://github.com/chenglou/pretext) | +204 | 41191 |
| 12 | [matthartman/ghost-pepper](https://github.com/matthartman/ghost-pepper) | +198 | 1399 |
| 13 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +195 | 18673 |
| 14 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +193 | 18146 |
| 15 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +176 | 37305 |
| 16 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +167 | 49344 |
| 17 | [xandemon/developer-icons](https://github.com/xandemon/developer-icons) | +159 | 1747 |
| 18 | [tobi/qmd](https://github.com/tobi/qmd) | +156 | 19466 |
| 19 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +154 | 25657 |
| 20 | [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) | +140 | 1123 |
| 21 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +138 | 40405 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +137 | 19660 |
| 23 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +131 | 7866 |
| 24 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +126 | 9973 |
| 25 | [tw93/Waza](https://github.com/tw93/Waza) | +125 | 1440 |
| 26 | [getcompanion-ai/feynman](https://github.com/getcompanion-ai/feynman) | +124 | 2727 |
| 27 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +124 | 16186 |
| 28 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +123 | 16250 |
| 29 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +120 | 49597 |
| 30 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +109 | 37271 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +22941 | 176238 |
| 2 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5882 | 29386 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +3690 | 51199 |
| 4 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +3546 | 69674 |
| 5 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3139 | 25084 |
| 6 | [chenglou/pretext](https://github.com/chenglou/pretext) | +2801 | 41191 |
| 7 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2648 | 18146 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +2108 | 60312 |
| 9 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1896 | 31221 |
| 10 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1834 | 22303 |
| 11 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1740 | 8188 |
| 12 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1398 | 74321 |
| 13 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1362 | 11461 |
| 14 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +1355 | 25657 |
| 15 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +1340 | 49344 |
| 16 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1319 | 66390 |
| 17 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1295 | 6598 |
| 18 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1275 | 12631 |
| 19 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1225 | 25775 |
| 20 | [block/goose](https://github.com/block/goose) | +1155 | 31098 |
| 21 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +1067 | 68059 |
| 22 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1052 | 5320 |
| 23 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1023 | 5756 |
| 24 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +988 | 73135 |
| 25 | [anthropics/skills](https://github.com/anthropics/skills) | +915 | 74774 |
| 26 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +892 | 34148 |
| 27 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +882 | 8583 |
| 28 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +874 | 51236 |
| 29 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +852 | 37271 |
| 30 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +842 | 5413 |
| 31 | [jackwener/opencli](https://github.com/jackwener/opencli) | +836 | 14025 |
| 32 | [google-research/timesfm](https://github.com/google-research/timesfm) | +818 | 15403 |
| 33 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +806 | 49597 |
| 34 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +785 | 6209 |
| 35 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +760 | 59093 |
| 36 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +757 | 32772 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +751 | 40405 |
| 38 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +742 | 33878 |
| 39 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +711 | 19660 |
| 40 | [0xGF/boneyard](https://github.com/0xGF/boneyard) | +705 | 3452 |
| 41 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +680 | 24391 |
| 42 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +677 | 5265 |
| 43 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +643 | 18673 |
| 44 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +613 | 30590 |
| 45 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +609 | 29060 |
| 46 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +596 | 3330 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +592 | 32837 |
| 48 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +546 | 48881 |
| 49 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +543 | 19476 |
| 50 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +533 | 21329 |
| 51 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +521 | 32872 |
| 52 | [capcom6/android-sms-gateway](https://github.com/capcom6/android-sms-gateway) | +497 | 3566 |
| 53 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +466 | 30678 |
| 54 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +460 | 2267 |
| 55 | [lintsinghua/claude-code-book](https://github.com/lintsinghua/claude-code-book) | +437 | 2333 |
| 56 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +435 | 27979 |
| 57 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +432 | 37305 |
| 58 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +428 | 5830 |
| 59 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +419 | 23835 |
| 60 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +418 | 37330 |
| 61 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +408 | 7866 |
| 62 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +401 | 37213 |
| 63 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +396 | 16250 |
| 64 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +388 | 5795 |
| 65 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +379 | 4153 |
| 66 | [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | +379 | 3515 |
| 67 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +377 | 31329 |
| 68 | [motiful/cc-gateway](https://github.com/motiful/cc-gateway) | +376 | 2486 |
| 69 | [tobi/qmd](https://github.com/tobi/qmd) | +375 | 19466 |
| 70 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +364 | 37988 |
| 71 | [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) | +364 | 3831 |
| 72 | [yasasbanukaofficial/claude-code](https://github.com/yasasbanukaofficial/claude-code) | +358 | 1893 |
| 73 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +354 | 17485 |
| 74 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +351 | 8681 |
| 75 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +344 | 1339 |
| 76 | [oboard/claude-code-rev](https://github.com/oboard/claude-code-rev) | +336 | 2834 |
| 77 | [mattpocock/skills](https://github.com/mattpocock/skills) | +334 | 12901 |
| 78 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +333 | 30591 |
| 79 | [codeaashu/claude-code](https://github.com/codeaashu/claude-code) | +331 | 1810 |
| 80 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +331 | 47166 |
| 81 | [chauncygu/collection-claude-code-source-code](https://github.com/chauncygu/collection-claude-code-source-code) | +314 | 1793 |
| 82 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +306 | 34247 |
| 83 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +305 | 21886 |
| 84 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +305 | 22188 |
| 85 | [ponponon/claude_code_src](https://github.com/ponponon/claude_code_src) | +303 | 2079 |
| 86 | [maaslalani/sheets](https://github.com/maaslalani/sheets) | +302 | 1551 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +299 | 19435 |
| 88 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +294 | 9973 |
| 89 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +292 | 44834 |
| 90 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +284 | 1304 |
| 91 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +282 | 9921 |
| 92 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +280 | 1608 |
| 93 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +279 | 4584 |
| 94 | [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) | +278 | 2477 |
| 95 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +274 | 3006 |
| 96 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +265 | 32562 |
| 97 | [leilei926524-tech/anti-distill](https://github.com/leilei926524-tech/anti-distill) | +264 | 1192 |
| 98 | [afar1/fieldtheory-cli](https://github.com/afar1/fieldtheory-cli) | +260 | 1117 |
| 99 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +259 | 16186 |
| 100 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +253 | 19748 |
| 101 | [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) | +248 | 1358 |
| 102 | [jarmuine/claude-code](https://github.com/jarmuine/claude-code) | +244 | 1900 |
| 103 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +235 | 21486 |
| 104 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +234 | 2654 |
| 105 | [jundot/omlx](https://github.com/jundot/omlx) | +234 | 8964 |
| 106 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +233 | 23631 |
| 107 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +227 | 24524 |
| 108 | [wquguru/harness-books](https://github.com/wquguru/harness-books) | +225 | 1213 |
| 109 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +222 | 9602 |
| 110 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +213 | 28396 |
| 111 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +210 | 28715 |
| 112 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +202 | 9474 |
| 113 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +202 | 5679 |
| 114 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +200 | 38385 |
| 115 | [tanbiralam/claude-code](https://github.com/tanbiralam/claude-code) | +199 | 1317 |
| 116 | [Nahuel990/ministack](https://github.com/Nahuel990/ministack) | +198 | 1716 |
| 117 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +196 | 7791 |
| 118 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +194 | 28836 |
| 119 | [roboflow/supervision](https://github.com/roboflow/supervision) | +192 | 36553 |
| 120 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | +187 | 9089 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +22942 | 176238 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +16247 | 224760 |
| 3 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +13998 | 51199 |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +13084 | 68059 |
| 5 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +12002 | 74321 |
| 6 | [garrytan/gstack](https://github.com/garrytan/gstack) | +11458 | 66390 |
| 7 | [obra/superpowers](https://github.com/obra/superpowers) | +11152 | 60312 |
| 8 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +8530 | 51236 |
| 9 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +8096 | 49345 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6162 | 41191 |
| 11 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +5886 | 29387 |
| 12 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +5403 | 29060 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5384 | 69674 |
| 14 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +5300 | 59093 |
| 15 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +4659 | 31221 |
| 16 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +4648 | 49597 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | +4586 | 74774 |
| 18 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +4064 | 48881 |
| 19 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3920 | 109881 |
| 20 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3715 | 34148 |
| 21 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +3526 | 22188 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3393 | 32772 |
| 23 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +3379 | 25084 |
| 24 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +3168 | 46000 |
| 25 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3131 | 22303 |
| 26 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +3131 | 21486 |
| 27 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +3083 | 16186 |
| 28 | [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | +2935 | 44834 |
| 29 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +2927 | 18146 |
| 30 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2880 | 16761 |
| 31 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2843 | 30590 |
| 32 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2840 | 27504 |
| 33 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2835 | 85286 |
| 34 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +2802 | 47166 |
| 35 | [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw) | +2792 | 18706 |
| 36 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2725 | 40405 |
| 37 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2693 | 25657 |
| 38 | [tanweai/pua](https://github.com/tanweai/pua) | +2682 | 15406 |
| 39 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +2601 | 19660 |
| 40 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2577 | 24391 |
| 41 | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | +2394 | 14318 |
| 42 | [jackwener/opencli](https://github.com/jackwener/opencli) | +2351 | 14025 |
| 43 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +2305 | 28715 |
| 44 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +2239 | 17485 |
| 45 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2183 | 28396 |
| 46 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2176 | 19476 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2173 | 32837 |
| 48 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2144 | 30678 |
| 49 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +2133 | 33878 |
| 50 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2025 | 37271 |
| 51 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +2025 | 12685 |
| 52 | [github/spec-kit](https://github.com/github/spec-kit) | +1965 | 71722 |
| 53 | [googleworkspace/cli](https://github.com/googleworkspace/cli) | +1950 | 24065 |
| 54 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1895 | 29265 |
| 55 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +1888 | 12631 |
| 56 | [cft0808/edict](https://github.com/cft0808/edict) | +1885 | 14608 |
| 57 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1864 | 37330 |
| 58 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1855 | 34982 |
| 59 | [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) | +1825 | 28954 |
| 60 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1820 | 23835 |
| 61 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1802 | 31329 |
| 62 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1791 | 12901 |
| 63 | [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) | +1787 | 21886 |
| 64 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +1771 | 60117 |
| 65 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +1759 | 8188 |
| 66 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1752 | 37988 |
| 67 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +1752 | 38385 |
| 68 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1751 | 30591 |
| 69 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +1751 | 19748 |
| 70 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1746 | 37213 |
| 71 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1709 | 16250 |
| 72 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +1675 | 9519 |
| 73 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | +1635 | 19708 |
| 74 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1634 | 11484 |
| 75 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +1627 | 10672 |
| 76 | [openai/codex](https://github.com/openai/codex) | +1562 | 61744 |
| 77 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1557 | 25775 |
| 78 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1555 | 18762 |
| 79 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | +1544 | 37547 |
| 80 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +1543 | 27979 |
| 81 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1541 | 21329 |
| 82 | [jundot/omlx](https://github.com/jundot/omlx) | +1486 | 8964 |
| 83 | [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | +1459 | 13038 |
| 84 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | +1450 | 9538 |
| 85 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1435 | 79656 |
| 86 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1433 | 34247 |
| 87 | [block/goose](https://github.com/block/goose) | +1409 | 31098 |
| 88 | [pascalorg/editor](https://github.com/pascalorg/editor) | +1403 | 9672 |
| 89 | [microsoft/RustTraining](https://github.com/microsoft/RustTraining) | +1395 | 12923 |
| 90 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1382 | 10775 |
| 91 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1382 | 16252 |
| 92 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1362 | 11461 |
| 93 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | +1360 | 7951 |
| 94 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1355 | 19435 |
| 95 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | +1349 | 43973 |
| 96 | [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | +1348 | 26803 |
| 97 | [canopy-network/canopy](https://github.com/canopy-network/canopy) | +1344 | 9072 |
| 98 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +1312 | 8548 |
| 99 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1299 | 8681 |
| 100 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1295 | 6598 |
| 101 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1248 | 73135 |
| 102 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +1246 | 9921 |
| 103 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1242 | 78902 |
| 104 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1225 | 8338 |
| 105 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +1181 | 9474 |
| 106 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +1150 | 14702 |
| 107 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +1092 | 52700 |
| 108 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1052 | 5320 |
| 109 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1023 | 5756 |
| 110 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +1017 | 5745 |
| 111 | [google-research/timesfm](https://github.com/google-research/timesfm) | +966 | 15403 |
| 112 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +949 | 5795 |
| 113 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +920 | 7791 |
| 114 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +910 | 23631 |
| 115 | [openai/skills](https://github.com/openai/skills) | +884 | 16326 |
| 116 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +882 | 8583 |
| 117 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +842 | 5413 |
| 118 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +841 | 39841 |
| 119 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +830 | 49621 |
| 120 | [666ghj/BettaFish](https://github.com/666ghj/BettaFish) | +828 | 35735 |
| 121 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +805 | 23123 |
| 122 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +805 | 45886 |
| 123 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +802 | 28836 |
| 124 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +769 | 37564 |
| 125 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +763 | 5830 |
| 126 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | +754 | 29129 |
| 127 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +753 | 6209 |
| 128 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +750 | 9602 |
| 129 | [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | +744 | 4527 |
| 130 | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | +741 | 17604 |
| 131 | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | +740 | 4715 |
| 132 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +720 | 4107 |
| 133 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +715 | 36799 |
| 134 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +702 | 4874 |
| 135 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +697 | 4584 |
| 136 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +678 | 24524 |
| 137 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +675 | 5265 |
| 138 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +671 | 32562 |
| 139 | [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources) | +671 | 18084 |
| 140 | [langflow-ai/openrag](https://github.com/langflow-ai/openrag) | +671 | 3692 |
| 141 | [Flowseal/tg-ws-proxy](https://github.com/Flowseal/tg-ws-proxy) | +663 | 4438 |
| 142 | [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | +644 | 9285 |
| 143 | [aiming-lab/MetaClaw](https://github.com/aiming-lab/MetaClaw) | +634 | 3553 |
| 144 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +596 | 3330 |
| 145 | [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | +596 | 9804 |
| 146 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | +593 | 47936 |
| 147 | [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | +581 | 7957 |
| 148 | [zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR) | +578 | 5679 |
| 149 | [TomBadash/Mouser](https://github.com/TomBadash/Mouser) | +570 | 2814 |
| 150 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +549 | 15332 |
| 151 | [eze-is/web-access](https://github.com/eze-is/web-access) | +531 | 4224 |
| 152 | [wshobson/agents](https://github.com/wshobson/agents) | +530 | 33131 |
| 153 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +528 | 47122 |
| 154 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +526 | 28644 |
| 155 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +518 | 44545 |
| 156 | [EverMind-AI/MSA](https://github.com/EverMind-AI/MSA) | +513 | 2700 |
| 157 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +511 | 7216 |
| 158 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +488 | 44232 |
| 159 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +479 | 18250 |
| 160 | [EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist) | +474 | 2947 |
| 161 | [datalab-to/chandra](https://github.com/datalab-to/chandra) | +468 | 8416 |
| 162 | [floci-io/floci](https://github.com/floci-io/floci) | +468 | 2923 |
| 163 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +460 | 7866 |
| 164 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +459 | 2267 |
| 165 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +455 | 8416 |
| 166 | [htdt/godogen](https://github.com/htdt/godogen) | +448 | 2623 |
| 167 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +448 | 24646 |
| 168 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +447 | 3669 |
| 169 | [Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm) | +440 | 4153 |
| 170 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +431 | 2654 |
| 171 | [ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch) | +426 | 3006 |
| 172 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +421 | 2646 |
| 173 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +405 | 2166 |
| 174 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +400 | 11415 |
| 175 | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | +399 | 12484 |
| 176 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +384 | 3955 |
| 177 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +371 | 2717 |
| 178 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +370 | 2214 |
| 179 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +362 | 2240 |
| 180 | [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | +343 | 1339 |
| 181 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +334 | 1918 |
| 182 | [pixlcore/xyops](https://github.com/pixlcore/xyops) | +326 | 3762 |
| 183 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +324 | 2414 |
| 184 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +324 | 1641 |
| 185 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +317 | 6677 |
| 186 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +313 | 4844 |
| 187 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +311 | 1803 |
| 188 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +307 | 1608 |
| 189 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +307 | 10760 |
| 190 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +305 | 2945 |
| 191 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +305 | 11030 |
| 192 | [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | +297 | 3670 |
| 193 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +296 | 2544 |
| 194 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +294 | 9973 |
| 195 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +284 | 1304 |
| 196 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +273 | 1433 |
| 197 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | +273 | 29780 |
| 198 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +273 | 22604 |
| 199 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +267 | 25362 |
| 200 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +259 | 5132 |
| 201 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +258 | 33712 |
| 202 | [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book) | +257 | 23494 |
| 203 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +250 | 2075 |
| 204 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +250 | 7507 |
| 205 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +240 | 6163 |
| 206 | [apify/agent-skills](https://github.com/apify/agent-skills) | +237 | 1861 |
| 207 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +234 | 15153 |
| 208 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +231 | 13872 |
| 209 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +226 | 36103 |
| 210 | [decolua/9router](https://github.com/decolua/9router) | +219 | 1887 |
| 211 | [chrysb/alphaclaw](https://github.com/chrysb/alphaclaw) | +218 | 1039 |
| 212 | [usebruno/bruno](https://github.com/usebruno/bruno) | +215 | 41086 |
| 213 | [elder-plinius/V3SP3R](https://github.com/elder-plinius/V3SP3R) | +204 | 900 |
| 214 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +189 | 2642 |
| 215 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +188 | 1324 |
| 216 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +172 | 21901 |
| 217 | [phuc-nt/my-translator](https://github.com/phuc-nt/my-translator) | +166 | 879 |
| 218 | [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | +162 | 2493 |
| 219 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +158 | 2774 |
| 220 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +144 | 3690 |
| 221 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +140 | 1177 |
| 222 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +139 | 849 |
| 223 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +139 | 2471 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +137 | 29357 |
| 225 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +131 | 1202 |
| 226 | [dashersw/gea](https://github.com/dashersw/gea) | +130 | 914 |
| 227 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +130 | 1369 |
| 228 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +128 | 12589 |
| 229 | [HazAT/glimpse](https://github.com/HazAT/glimpse) | +127 | 531 |
| 230 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +127 | 29399 |
| 231 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +124 | 40265 |
| 232 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +124 | 35473 |
| 233 | [rivet-dev/secure-exec](https://github.com/rivet-dev/secure-exec) | +123 | 786 |
| 234 | [pdone/lx-music-source](https://github.com/pdone/lx-music-source) | +123 | 5520 |
| 235 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +123 | 10588 |
| 236 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +121 | 604 |
| 237 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +121 | 23181 |
| 238 | [is-a-dev/register](https://github.com/is-a-dev/register) | +118 | 10088 |
| 239 | [vasilytrofimchuk/domainsearcher-app](https://github.com/vasilytrofimchuk/domainsearcher-app) | +116 | 601 |
| 240 | [kulikov0/whitelist-bypass](https://github.com/kulikov0/whitelist-bypass) | +113 | 753 |
| 241 | [bujue3709/chatgpt-Long-conversation-optimization](https://github.com/bujue3709/chatgpt-Long-conversation-optimization) | +113 | 713 |
| 242 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +113 | 26433 |
| 243 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +110 | 33000 |
| 244 | [libaxuan/cursor2api-go](https://github.com/libaxuan/cursor2api-go) | +108 | 1117 |
| 245 | [cporter202/social-media-scraping-apis](https://github.com/cporter202/social-media-scraping-apis) | +105 | 1049 |
| 246 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +105 | 723 |
| 247 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +105 | 2095 |
| 248 | [epiral/bb-sites](https://github.com/epiral/bb-sites) | +104 | 482 |
| 249 | [songguoxs/gpt4o-image-prompts](https://github.com/songguoxs/gpt4o-image-prompts) | +101 | 3264 |
| 250 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +101 | 1274 |
| 251 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +101 | 859 |
| 252 | [Pavelevich/llm-checker](https://github.com/Pavelevich/llm-checker) | +101 | 1780 |
| 253 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +100 | 1131 |
| 254 | [wasmerio/edgejs](https://github.com/wasmerio/edgejs) | +99 | 550 |
| 255 | [linlay/zenmind](https://github.com/linlay/zenmind) | +99 | 88 |
| 256 | [BillionsNetwork/verified-agent-identity](https://github.com/BillionsNetwork/verified-agent-identity) | +98 | 529 |
| 257 | [OpenLAIR/dr-claw](https://github.com/OpenLAIR/dr-claw) | +98 | 808 |
| 258 | [lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) | +98 | 1866 |
| 259 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +98 | 48784 |
| 260 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +97 | 1616 |
| 261 | [microg/GmsCore](https://github.com/microg/GmsCore) | +97 | 12849 |
| 262 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 516 |
| 263 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +95 | 3447 |
| 264 | [borski/travel-hacking-toolkit](https://github.com/borski/travel-hacking-toolkit) | +93 | 359 |
| 265 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +93 | 1477 |
| 266 | [idinging/freemail](https://github.com/idinging/freemail) | +92 | 1310 |
| 267 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +92 | 448 |
| 268 | [SethGammon/Citadel](https://github.com/SethGammon/Citadel) | +91 | 477 |
| 269 | [StudioSpindler/anaba](https://github.com/StudioSpindler/anaba) | +90 | 536 |
| 270 | [WuKongOpenSource/AI_CRM](https://github.com/WuKongOpenSource/AI_CRM) | +90 | 567 |
| 271 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +89 | 416 |
| 272 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +89 | 745 |
| 273 | [robinebers/openusage](https://github.com/robinebers/openusage) | +89 | 1739 |
| 274 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +88 | 3822 |
| 275 | [skylot/jadx](https://github.com/skylot/jadx) | +87 | 47365 |
| 276 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +86 | 963 |
| 277 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +84 | 3551 |
| 278 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +81 | 0 |
| 279 | [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | +80 | 2625 |
| 280 | [stephengpope/thepopebot](https://github.com/stephengpope/thepopebot) | +79 | 1533 |
| 281 | [meodai/heerich](https://github.com/meodai/heerich) | +77 | 443 |
| 282 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +76 | 9131 |
| 283 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +75 | 713 |
| 284 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +75 | 11491 |
| 285 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +75 | 27152 |
| 286 | [epitome-AISS/epitome](https://github.com/epitome-AISS/epitome) | +73 | 516 |
| 287 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +72 | 409 |
| 288 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +69 | 8442 |
| 289 | [crimera/piko](https://github.com/crimera/piko) | +68 | 3060 |
| 290 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +68 | 37313 |
| 291 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +67 | 452 |
| 292 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +66 | 7196 |
| 293 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +66 | 395 |
| 294 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +66 | 45263 |
| 295 | [ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter) | +64 | 353 |
| 296 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +63 | 31476 |
| 297 | [kestra-io/kestra](https://github.com/kestra-io/kestra) | +63 | 26668 |
| 298 | [ReChronoRain/HyperCeiler](https://github.com/ReChronoRain/HyperCeiler) | +62 | 4638 |
| 299 | [apache/kafka](https://github.com/apache/kafka) | +61 | 32043 |
| 300 | [andforce/Andclaw](https://github.com/andforce/Andclaw) | +59 | 382 |
