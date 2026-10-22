---
title: "2026-10-22 GitHub增长趋势报告"
description: "1.rea+8482 2.cleanyourtv+4958 3.security-audit-skill+3166 4.dsh-our-free-model+2952 5.DeepInfer+2078"
date: 2026-10-23T07:05:36+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-23 07:05:36

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
        'daily': {"categories": ["yetone/magpie", "storytold/photocraft", "hugohe3/ppt-master", "jbiaojerry/ebook-treasure-chest", "sindresorhus/awesome", "google-research/harness2", "heygen-com/hyperframes", "affaan-m/ECC", "mattpocock/skills", "deepseek-ai/deepseek-harness", "Graphify-Labs/graphify", "debpalash/VoiceStudio", "stablyai/orca", "ifixai-ai/iFixAi", "DietrichGebert/ponytail", "deepseek-ai/DeepInfer", "Ebony-Vinyl/dsh-our-free-model", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [720, 724, 775, 776, 782, 789, 793, 808, 1030, 1192, 1321, 1376, 1531, 1695, 1867, 2078, 2952, 3166, 4958, 8482]},
        'weekly': {"categories": ["heygen-com/hyperframes", "Graphify-Labs/graphify", "yetone/magpie", "affaan-m/ECC", "anomalyco/opencode", "storytold/artcraft", "wheresryan22/anatomy", "deepseek-ai/deepseek-harness", "mattpocock/skills", "storytold/photocraft", "boykopovar/AnyPS5", "DietrichGebert/ponytail", "stablyai/orca", "cloudflare/security-audit-skill", "debpalash/VoiceStudio", "ai-job-search-dev/ai-job-search", "Ebony-Vinyl/dsh-our-free-model", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5472, 5993, 6068, 6186, 6285, 6390, 6466, 7719, 8062, 8122, 8272, 9012, 9281, 9556, 12745, 16055, 18900, 19825, 23843, 97121]},
        'monthly': {"categories": ["shihabal3amri/DiPlay", "Droid-Deck/DroidDeck", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "yetone/magpie", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "Niko1221/Strata", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft"], "data": [12073, 12693, 14320, 15390, 15528, 15736, 17210, 17968, 19123, 19497, 19825, 23843, 30586, 36705, 71326]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +8482 | 365892 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +4958 | 23843 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +3166 | 39439 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2952 | 36705 |
| 5 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +2078 | 19825 |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1867 | 173380 |
| 7 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +1695 | 33149 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +1531 | 102704 |
| 9 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1376 | 81707 |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +1321 | 132887 |
| 11 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1192 | 258138 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1030 | 300850 |
| 13 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +808 | 286491 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +793 | 69976 |
| 15 | [google-research/harness2](https://github.com/google-research/harness2) | +789 | 17968 |
| 16 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +782 | 523148 |
| 17 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +776 | 21683 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +775 | 65979 |
| 19 | [storytold/photocraft](https://github.com/storytold/photocraft) | +724 | 71326 |
| 20 | [yetone/magpie](https://github.com/yetone/magpie) | +720 | 19497 |
| 21 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +674 | 17681 |
| 22 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +673 | 30586 |
| 23 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +659 | 43143 |
| 24 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +638 | 39571 |
| 25 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +626 | 63532 |
| 26 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +621 | 19123 |
| 27 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +604 | 29341 |
| 28 | [obra/superpowers](https://github.com/obra/superpowers) | +573 | 303715 |
| 29 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +570 | 222504 |
| 30 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +562 | 101108 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +97121 | 365892 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +23843 | 23843 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +19825 | 19825 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +18900 | 36705 |
| 5 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +16055 | 63532 |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12745 | 81707 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +9556 | 39439 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +9281 | 102704 |
| 9 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +9012 | 173380 |
| 10 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +8272 | 46861 |
| 11 | [storytold/photocraft](https://github.com/storytold/photocraft) | +8122 | 71326 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8062 | 300850 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7719 | 258138 |
| 14 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +6466 | 19123 |
| 15 | [storytold/artcraft](https://github.com/storytold/artcraft) | +6390 | 35590 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +6285 | 220189 |
| 17 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6186 | 286491 |
| 18 | [yetone/magpie](https://github.com/yetone/magpie) | +6068 | 19497 |
| 19 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +5993 | 132887 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5472 | 69976 |
| 21 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5163 | 30586 |
| 22 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +4871 | 43880 |
| 23 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4804 | 33149 |
| 24 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +4442 | 93129 |
| 25 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +4300 | 142006 |
| 26 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +4229 | 27114 |
| 27 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +4138 | 60019 |
| 28 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +4126 | 67970 |
| 29 | [obra/superpowers](https://github.com/obra/superpowers) | +3878 | 303715 |
| 30 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3821 | 101108 |
| 31 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +3808 | 39571 |
| 32 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3662 | 523148 |
| 33 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3560 | 65979 |
| 34 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3556 | 87586 |
| 35 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +3471 | 53880 |
| 36 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3445 | 106147 |
| 37 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +3385 | 78474 |
| 38 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3362 | 84961 |
| 39 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3263 | 101015 |
| 40 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3157 | 56223 |
| 41 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +3141 | 21130 |
| 42 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2941 | 147665 |
| 43 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2899 | 163240 |
| 44 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2865 | 79873 |
| 45 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +2798 | 17210 |
| 46 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2760 | 138996 |
| 47 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2705 | 72459 |
| 48 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2694 | 52729 |
| 49 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2620 | 134221 |
| 50 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2616 | 109645 |
| 51 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2585 | 14911 |
| 52 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2419 | 222504 |
| 53 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2406 | 43208 |
| 54 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2391 | 194287 |
| 55 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2389 | 329340 |
| 56 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +2382 | 15528 |
| 57 | [blader/humanizer](https://github.com/blader/humanizer) | +2358 | 59633 |
| 58 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2342 | 24830 |
| 59 | [usestrix/strix](https://github.com/usestrix/strix) | +2337 | 71155 |
| 60 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2330 | 200441 |
| 61 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2301 | 491409 |
| 62 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2295 | 70881 |
| 63 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2242 | 48733 |
| 64 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2193 | 59100 |
| 65 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2123 | 256232 |
| 66 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +2107 | 77553 |
| 67 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +2075 | 252403 |
| 68 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +2056 | 31825 |
| 69 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +2027 | 555479 |
| 70 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +2020 | 38977 |
| 71 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1996 | 103342 |
| 72 | [cursor/plugins](https://github.com/cursor/plugins) | +1975 | 13602 |
| 73 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1973 | 66364 |
| 74 | [google/artemis](https://github.com/google/artemis) | +1952 | 13806 |
| 75 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1937 | 16190 |
| 76 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +1911 | 15736 |
| 77 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1906 | 114397 |
| 78 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1906 | 29341 |
| 79 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1861 | 62651 |
| 80 | [supabase/supabase](https://github.com/supabase/supabase) | +1852 | 113463 |
| 81 | [tw93/Mole](https://github.com/tw93/Mole) | +1852 | 72402 |
| 82 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1847 | 152910 |
| 83 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1844 | 22536 |
| 84 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1817 | 329493 |
| 85 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1803 | 81300 |
| 86 | [xtool-org/xtool](https://github.com/xtool-org/xtool) | +1801 | 13383 |
| 87 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1762 | 31556 |
| 88 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1756 | 117209 |
| 89 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1656 | 29438 |
| 90 | [anthropics/skills](https://github.com/anthropics/skills) | +1637 | 183024 |
| 91 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1618 | 50133 |
| 92 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1613 | 112986 |
| 93 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1583 | 32038 |
| 94 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1569 | 76604 |
| 95 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1568 | 153211 |
| 96 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +1551 | 55736 |
| 97 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1537 | 57504 |
| 98 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1494 | 32449 |
| 99 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1475 | 40335 |
| 100 | [lexmount/moli](https://github.com/lexmount/moli) | +1459 | 20122 |
| 101 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1401 | 183737 |
| 102 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1380 | 17526 |
| 103 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1371 | 122946 |
| 104 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +1360 | 14320 |
| 105 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1347 | 18794 |
| 106 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +1340 | 17681 |
| 107 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1301 | 102331 |
| 108 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1295 | 89196 |
| 109 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +1278 | 95147 |
| 110 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1265 | 21163 |
| 111 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1255 | 20141 |
| 112 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1252 | 53491 |
| 113 | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | +1244 | 12663 |
| 114 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1241 | 87716 |
| 115 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1239 | 43143 |
| 116 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1237 | 191659 |
| 117 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1223 | 189811 |
| 118 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1213 | 43384 |
| 119 | [torvalds/linux](https://github.com/torvalds/linux) | +1202 | 253168 |
| 120 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1184 | 45394 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +71326 | 71326 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +36705 | 36705 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +30586 | 30586 |
| 4 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +23843 | 23843 |
| 5 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +19825 | 19825 |
| 6 | [yetone/magpie](https://github.com/yetone/magpie) | +19497 | 19497 |
| 7 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +19123 | 19123 |
| 8 | [google-research/harness2](https://github.com/google-research/harness2) | +17968 | 17968 |
| 9 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +17210 | 17210 |
| 10 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +15736 | 15736 |
| 11 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +15528 | 15528 |
| 12 | [openai/math](https://github.com/openai/math) | +15390 | 15390 |
| 13 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14320 | 14320 |
| 14 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +12693 | 12693 |
| 15 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +12073 | 12073 |
