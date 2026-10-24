---
title: "2026-10-24 GitHub增长趋势报告"
description: "1.rea+5406 2.cleanyourtv+3769 3.security-audit-skill+2321 4.dsh-our-free-model+2131 5.VoiceStudio+1623"
date: 2026-10-25T06:21:16+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-25 06:21:16

本报告展示了 GitHub 上 Star 数增长最快的仓库（基于每日 Top-5000 Star 快照差分计算）。

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
        'daily': {"categories": ["hugohe3/ppt-master", "tashfeenahmed/freellmapi", "NVIDIA/OpenShell", "heygen-com/hyperframes", "ai-job-search-dev/ai-job-search", "mattpocock/skills", "DietrichGebert/ponytail", "Nutlope/hallmark", "deepseek-ai/DeepInfer", "affaan-m/ECC", "Niko1221/Strata", "pbakaus/impeccable", "deepseek-ai/deepseek-harness", "xerj-org/xerj", "stablyai/orca", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [671, 680, 684, 684, 688, 696, 719, 725, 744, 752, 811, 818, 1036, 1097, 1106, 1623, 2131, 2321, 3769, 5406]},
        'weekly': {"categories": ["ifixai-ai/iFixAi", "wheresryan22/anatomy", "Niko1221/Strata", "heygen-com/hyperframes", "affaan-m/ECC", "yetone/magpie", "anomalyco/opencode", "storytold/photocraft", "boykopovar/AnyPS5", "Graphify-Labs/graphify", "mattpocock/skills", "deepseek-ai/deepseek-harness", "DietrichGebert/ponytail", "stablyai/orca", "debpalash/VoiceStudio", "cloudflare/security-audit-skill", "ai-job-search-dev/ai-job-search", "Ebony-Vinyl/dsh-our-free-model", "Gathin23/cleanyourtv", "morluto/rea"], "data": [4891, 5072, 5090, 5512, 5639, 5744, 5895, 6066, 6279, 6649, 7457, 8343, 9318, 9589, 11712, 13691, 14539, 19491, 31558, 71731]},
        'monthly': {"categories": ["KnifeLemon/Filee", "shihabal3amri/DiPlay", "Droid-Deck/DroidDeck", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "Niko1221/Strata", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft"], "data": [11628, 12257, 13864, 14536, 15480, 15895, 16065, 17624, 19084, 20119, 21813, 31558, 31947, 41203, 72371]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +5406 | 378346 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +3769 | 31558 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2321 | 44360 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2131 | 41203 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1623 | 84859 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +1106 | 104901 |
| 7 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +1097 | 15288 |
| 8 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1036 | 260442 |
| 9 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +818 | 86325 |
| 10 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +811 | 31947 |
| 11 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +752 | 288039 |
| 12 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +744 | 21813 |
| 13 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +725 | 32052 |
| 14 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +719 | 175483 |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills) | +696 | 302480 |
| 16 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +688 | 64771 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +684 | 71444 |
| 18 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +684 | 19430 |
| 19 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +680 | 40919 |
| 20 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +671 | 67409 |
| 21 | [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) | +596 | 12384 |
| 22 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +592 | 13864 |
| 23 | [yetone/magpie](https://github.com/yetone/magpie) | +568 | 20759 |
| 24 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +563 | 201505 |
| 25 | [google-research/harness2](https://github.com/google-research/harness2) | +542 | 19084 |
| 26 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +515 | 134398 |
| 27 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +502 | 524137 |
| 28 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +502 | 44491 |
| 29 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +496 | 47858 |
| 30 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +481 | 68291 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +71731 | 378346 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +31558 | 31558 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +19491 | 41203 |
| 4 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +14539 | 64771 |
| 5 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +13691 | 44360 |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +11712 | 84859 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +9589 | 104901 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +9318 | 175483 |
| 9 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +8343 | 260442 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7457 | 302480 |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +6649 | 134398 |
| 12 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +6279 | 47858 |
| 13 | [storytold/photocraft](https://github.com/storytold/photocraft) | +6066 | 72371 |
| 14 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5895 | 221063 |
| 15 | [yetone/magpie](https://github.com/yetone/magpie) | +5744 | 20759 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +5639 | 288039 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5512 | 71444 |
| 18 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5090 | 31947 |
| 19 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +5072 | 20119 |
| 20 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4891 | 34021 |
| 21 | [storytold/artcraft](https://github.com/storytold/artcraft) | +4585 | 36286 |
| 22 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +4556 | 142617 |
| 23 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4318 | 40919 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4261 | 67409 |
| 25 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3981 | 86325 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3884 | 88720 |
| 27 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +3755 | 60712 |
| 28 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +3749 | 93959 |
| 29 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3691 | 524137 |
| 30 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3569 | 101997 |
| 31 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3464 | 68634 |
| 32 | [obra/superpowers](https://github.com/obra/superpowers) | +3439 | 304614 |
| 33 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3325 | 106931 |
| 34 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +3242 | 27602 |
| 35 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +3037 | 80738 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3027 | 139902 |
| 37 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3018 | 101720 |
| 38 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +3010 | 79021 |
| 39 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +2900 | 19430 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2841 | 56844 |
| 41 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2832 | 163702 |
| 42 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2781 | 148319 |
| 43 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2753 | 223361 |
| 44 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +2692 | 44339 |
| 45 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2667 | 43562 |
| 46 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2642 | 201505 |
| 47 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2623 | 73278 |
| 48 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2611 | 32603 |
| 49 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2592 | 53428 |
| 50 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2556 | 44491 |
| 51 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2519 | 194989 |
| 52 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2482 | 134854 |
| 53 | [usestrix/strix](https://github.com/usestrix/strix) | +2451 | 71666 |
| 54 | [blader/humanizer](https://github.com/blader/humanizer) | +2433 | 60250 |
| 55 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2426 | 71572 |
| 56 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2381 | 110194 |
| 57 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +2375 | 21609 |
| 58 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2365 | 15506 |
| 59 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2345 | 49363 |
| 60 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2342 | 67103 |
| 61 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2338 | 330000 |
| 62 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2331 | 25370 |
| 63 | [google/artemis](https://github.com/google/artemis) | +2265 | 14421 |
| 64 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +2239 | 54428 |
| 65 | [supabase/supabase](https://github.com/supabase/supabase) | +2194 | 113889 |
| 66 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +2163 | 17624 |
| 67 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +2141 | 77726 |
| 68 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2125 | 491870 |
| 69 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2119 | 256787 |
| 70 | [thesysdev/openui](https://github.com/thesysdev/openui) | +2055 | 13621 |
| 71 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2051 | 59666 |
| 72 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +2043 | 252937 |
| 73 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1928 | 113656 |
| 74 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1920 | 16776 |
| 75 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1881 | 63134 |
| 76 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1875 | 18365 |
| 77 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1871 | 555983 |
| 78 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +1864 | 15895 |
| 79 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1842 | 29747 |
| 80 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1827 | 103753 |
| 81 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +1812 | 22563 |
| 82 | [tw93/Mole](https://github.com/tw93/Mole) | +1802 | 72727 |
| 83 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1796 | 329998 |
| 84 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +1774 | 32052 |
| 85 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1770 | 81700 |
| 86 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1728 | 29841 |
| 87 | [anthropics/skills](https://github.com/anthropics/skills) | +1718 | 183497 |
| 88 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1680 | 22927 |
| 89 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +1667 | 39355 |
| 90 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1655 | 77010 |
| 91 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1647 | 117605 |
| 92 | [cursor/plugins](https://github.com/cursor/plugins) | +1635 | 13906 |
| 93 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1632 | 19211 |
| 94 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1628 | 32897 |
| 95 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1627 | 32124 |
| 96 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1623 | 153282 |
| 97 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +1557 | 55811 |
| 98 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1543 | 153607 |
| 99 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1534 | 114809 |
| 100 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +1518 | 16065 |
| 101 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1513 | 57863 |
| 102 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1509 | 50425 |
| 103 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1470 | 184187 |
| 104 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1404 | 32299 |
| 105 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1396 | 40562 |
| 106 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1394 | 102798 |
| 107 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1390 | 123329 |
| 108 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1356 | 20516 |
| 109 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +1331 | 95335 |
| 110 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1279 | 88067 |
| 111 | [xtool-org/xtool](https://github.com/xtool-org/xtool) | +1270 | 13538 |
| 112 | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | +1265 | 12984 |
| 113 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +1251 | 68291 |
| 114 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +1240 | 19281 |
| 115 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | +1234 | 60713 |
| 116 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1230 | 190155 |
| 117 | [lexmount/moli](https://github.com/lexmount/moli) | +1229 | 20486 |
| 118 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1202 | 191970 |
| 119 | [php/php-src](https://github.com/php/php-src) | +1193 | 41641 |
| 120 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +1191 | 59652 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +72371 | 72371 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +41203 | 41203 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +31947 | 31947 |
| 4 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +31558 | 31558 |
| 5 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +21813 | 21813 |
| 6 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +20119 | 20119 |
| 7 | [google-research/harness2](https://github.com/google-research/harness2) | +19084 | 19084 |
| 8 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +17624 | 17624 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16065 | 16065 |
| 10 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +15895 | 15895 |
| 11 | [openai/math](https://github.com/openai/math) | +15480 | 15480 |
| 12 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14536 | 14536 |
| 13 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +13864 | 13864 |
| 14 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +12257 | 12257 |
| 15 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +11628 | 11628 |
