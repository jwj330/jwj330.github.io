---
title: "2026-10-26 GitHub增长趋势报告"
description: "1.rea+7172 2.cleanyourtv+4353 3.hallmark+2611 4.VoiceStudio+2503 5.LinkSwift+2138"
date: 2026-10-27T07:41:24+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-27 07:41:24

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
        'daily': {"categories": ["Graphify-Labs/graphify", "DietrichGebert/ponytail", "Niko1221/Strata", "affaan-m/ECC", "Panniantong/Agent-Reach", "HKUDS/DeepTutor", "yetone/magpie", "deepseek-ai/deepseek-harness", "xerj-org/xerj", "stablyai/orca", "AgriciDaniel/claude-seo", "TauricResearch/TradingAgents", "pbakaus/impeccable", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "hmjz100/LinkSwift", "debpalash/VoiceStudio", "Nutlope/hallmark", "Gathin23/cleanyourtv", "morluto/rea"], "data": [952, 960, 967, 1013, 1066, 1121, 1138, 1218, 1280, 1294, 1362, 1525, 1546, 1778, 1906, 2138, 2503, 2611, 4353, 7172]},
        'weekly': {"categories": ["storytold/photocraft", "ifixai-ai/iFixAi", "hugohe3/ppt-master", "heygen-com/hyperframes", "Niko1221/Strata", "yetone/magpie", "affaan-m/ECC", "Nutlope/hallmark", "pbakaus/impeccable", "mattpocock/skills", "Graphify-Labs/graphify", "deepseek-ai/deepseek-harness", "google-research/harness2", "stablyai/orca", "DietrichGebert/ponytail", "ai-job-search-dev/ai-job-search", "debpalash/VoiceStudio", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "morluto/rea"], "data": [4817, 4953, 5024, 5402, 5432, 5588, 5700, 5832, 5929, 6601, 6970, 8117, 8499, 8815, 9022, 9238, 11702, 16018, 17137, 55156]},
        'monthly': {"categories": ["yihui-dev/awesome-opus5-5-videos", "KnifeLemon/Filee", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [11539, 13119, 14752, 15567, 16218, 16410, 18038, 20149, 21062, 23013, 39155, 73348]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +7172 | 391447 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +4353 | 39155 |
| 3 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +2611 | 36226 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2503 | 89147 |
| 5 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +2138 | 29987 |
| 6 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1906 | 44790 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1778 | 48508 |
| 8 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1546 | 89135 |
| 9 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1525 | 116039 |
| 10 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +1362 | 22124 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +1294 | 107025 |
| 12 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +1280 | 16830 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1218 | 262548 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +1138 | 22560 |
| 15 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1121 | 43791 |
| 16 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1066 | 103520 |
| 17 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +1013 | 289809 |
| 18 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +967 | 33696 |
| 19 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +960 | 177100 |
| 20 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +952 | 136114 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +925 | 73035 |
| 22 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +896 | 13119 |
| 23 | [mattpocock/skills](https://github.com/mattpocock/skills) | +864 | 304053 |
| 24 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +820 | 68891 |
| 25 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +812 | 224614 |
| 26 | [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) | +809 | 12390 |
| 27 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +660 | 64953 |
| 28 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +650 | 35043 |
| 29 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +649 | 66333 |
| 30 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +644 | 23013 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +55156 | 391447 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +17137 | 44790 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +16018 | 48508 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +11702 | 89147 |
| 5 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +9238 | 66333 |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +9022 | 177100 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +8815 | 107025 |
| 8 | [google-research/harness2](https://github.com/google-research/harness2) | +8499 | 20149 |
| 9 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +8117 | 262548 |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +6970 | 136114 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6601 | 304053 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +5929 | 89135 |
| 13 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +5832 | 36226 |
| 14 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +5700 | 289809 |
| 15 | [yetone/magpie](https://github.com/yetone/magpie) | +5588 | 22560 |
| 16 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5432 | 33696 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5402 | 73035 |
| 18 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5024 | 68891 |
| 19 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4953 | 35043 |
| 20 | [storytold/photocraft](https://github.com/storytold/photocraft) | +4817 | 73348 |
| 21 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4519 | 42156 |
| 22 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +4237 | 21062 |
| 23 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +4208 | 48649 |
| 24 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +4191 | 221946 |
| 25 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +3949 | 29987 |
| 26 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3938 | 89778 |
| 27 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +3925 | 116039 |
| 28 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3847 | 103520 |
| 29 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3694 | 525163 |
| 30 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3637 | 102980 |
| 31 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +3590 | 143264 |
| 32 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +3513 | 14878 |
| 33 | [obra/superpowers](https://github.com/obra/superpowers) | +3480 | 305597 |
| 34 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +3403 | 224614 |
| 35 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +3368 | 20084 |
| 36 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3364 | 45327 |
| 37 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3301 | 140909 |
| 38 | [storytold/artcraft](https://github.com/storytold/artcraft) | +3220 | 36908 |
| 39 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +3155 | 94702 |
| 40 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3138 | 69504 |
| 41 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +3078 | 202572 |
| 42 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2996 | 61372 |
| 43 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2975 | 81515 |
| 44 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2943 | 107656 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2920 | 74353 |
| 46 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +2818 | 22124 |
| 47 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2710 | 33201 |
| 48 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2620 | 148958 |
| 49 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2598 | 195690 |
| 50 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2581 | 67893 |
| 51 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2521 | 164258 |
| 52 | [blader/humanizer](https://github.com/blader/humanizer) | +2521 | 61019 |
| 53 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +2498 | 13793 |
| 54 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2442 | 54094 |
| 55 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2428 | 50099 |
| 56 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2374 | 79534 |
| 57 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2353 | 16232 |
| 58 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +2344 | 23179 |
| 59 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2343 | 330724 |
| 60 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2301 | 135462 |
| 61 | [supabase/supabase](https://github.com/supabase/supabase) | +2257 | 114034 |
| 62 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2257 | 72171 |
| 63 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2238 | 43861 |
| 64 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2191 | 110805 |
| 65 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +2165 | 22127 |
| 66 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2144 | 60414 |
| 67 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2140 | 257403 |
| 68 | [usestrix/strix](https://github.com/usestrix/strix) | +2082 | 72146 |
| 69 | [google/artemis](https://github.com/google/artemis) | +2055 | 15028 |
| 70 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2049 | 57252 |
| 71 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2020 | 43791 |
| 72 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +2014 | 19755 |
| 73 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1996 | 253472 |
| 74 | [thesysdev/openui](https://github.com/thesysdev/openui) | +1988 | 14186 |
| 75 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1953 | 77625 |
| 76 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1932 | 492431 |
| 77 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1893 | 25871 |
| 78 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1875 | 18854 |
| 79 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1874 | 30501 |
| 80 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1858 | 556454 |
| 81 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1849 | 54772 |
| 82 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1837 | 63747 |
| 83 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1784 | 30115 |
| 84 | [anthropics/skills](https://github.com/anthropics/skills) | +1755 | 183980 |
| 85 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1753 | 18038 |
| 86 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1727 | 330468 |
| 87 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1721 | 64953 |
| 88 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1715 | 77929 |
| 89 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1634 | 104152 |
| 90 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1626 | 115295 |
| 91 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +1623 | 33222 |
| 92 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1622 | 184739 |
| 93 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1616 | 103420 |
| 94 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1610 | 118024 |
| 95 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1603 | 33363 |
| 96 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1596 | 23322 |
| 97 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1572 | 44741 |
| 98 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1564 | 58455 |
| 99 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1563 | 154087 |
| 100 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1560 | 43818 |
| 101 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +1548 | 22151 |
| 102 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1500 | 82151 |
| 103 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1484 | 17026 |
| 104 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +1475 | 16218 |
| 105 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +1464 | 95622 |
| 106 | [tw93/Mole](https://github.com/tw93/Mole) | +1462 | 72993 |
| 107 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +1456 | 39729 |
| 108 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +1446 | 68668 |
| 109 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1426 | 50795 |
| 110 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1404 | 123723 |
| 111 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1385 | 88407 |
| 112 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1369 | 20904 |
| 113 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1367 | 32430 |
| 114 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +1310 | 16410 |
| 115 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1300 | 26718 |
| 116 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1300 | 13824 |
| 117 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1260 | 192376 |
| 118 | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | +1259 | 13331 |
| 119 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1251 | 40789 |
| 120 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +1247 | 59833 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +73348 | 73348 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +39155 | 39155 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +23013 | 23013 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +21062 | 21062 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +20149 | 20149 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +18038 | 18038 |
| 7 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16410 | 16410 |
| 8 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16218 | 16218 |
| 9 | [openai/math](https://github.com/openai/math) | +15567 | 15567 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14752 | 14752 |
| 11 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +13119 | 13119 |
| 12 | [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | +11539 | 11539 |
