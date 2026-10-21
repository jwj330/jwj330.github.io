---
title: "2026-10-21 GitHub增长趋势报告"
description: "1.rea+9887 2.cleanyourtv+7390 3.DeepInfer+5803 4.dsh-our-free-model+2942 5.ai-job-search+2492"
date: 2026-10-22T07:07:43+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-22 07:07:43

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
        'daily': {"categories": ["anomalyco/opencode", "affaan-m/ECC", "ifixai-ai/iFixAi", "yetone/magpie", "boykopovar/AnyPS5", "wheresryan22/anatomy", "storytold/photocraft", "deepseek-ai/deepseek-harness", "mattpocock/skills", "Graphify-Labs/graphify", "debpalash/VoiceStudio", "stablyai/orca", "DietrichGebert/ponytail", "google-research/harness2", "cloudflare/security-audit-skill", "ai-job-search-dev/ai-job-search", "Ebony-Vinyl/dsh-our-free-model", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "morluto/rea"], "data": [786, 810, 811, 836, 851, 954, 1007, 1208, 1213, 1401, 1425, 1500, 1959, 1963, 2231, 2492, 2942, 5803, 7390, 9887]},
        'weekly': {"categories": ["Niko1221/Strata", "heygen-com/hyperframes", "anthropics/claude-plugins-official", "yetone/magpie", "anomalyco/opencode", "affaan-m/ECC", "cloudflare/security-audit-skill", "deepseek-ai/deepseek-harness", "storytold/artcraft", "DietrichGebert/ponytail", "mattpocock/skills", "stablyai/orca", "boykopovar/AnyPS5", "storytold/photocraft", "debpalash/VoiceStudio", "ai-job-search-dev/ai-job-search", "Ebony-Vinyl/dsh-our-free-model", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5343, 5520, 5561, 6082, 6130, 6238, 6675, 7286, 7311, 7933, 8648, 8711, 9258, 9633, 14158, 16102, 17639, 17747, 18885, 117146]},
        'monthly': {"categories": ["shihabal3amri/DiPlay", "Droid-Deck/DroidDeck", "storytold/lightcraft", "storytold/wordcraft", "openai/math", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "deepseek-ai/DeepInfer", "wheresryan22/anatomy", "yetone/magpie", "Gathin23/cleanyourtv", "Niko1221/Strata", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft"], "data": [11965, 12226, 14207, 15328, 15347, 15554, 16974, 17179, 17747, 18502, 18777, 18885, 29913, 33753, 70602]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +9887 | 357410 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +7390 | 18885 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +5803 | 17747 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2942 | 33753 |
| 5 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +2492 | 62906 |
| 6 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2231 | 36273 |
| 7 | [google-research/harness2](https://github.com/google-research/harness2) | +1963 | 17179 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1959 | 171513 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +1500 | 101173 |
| 10 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1425 | 80331 |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +1401 | 131566 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1213 | 299820 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1208 | 256946 |
| 14 | [storytold/photocraft](https://github.com/storytold/photocraft) | +1007 | 70602 |
| 15 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +954 | 18502 |
| 16 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +851 | 46333 |
| 17 | [yetone/magpie](https://github.com/yetone/magpie) | +836 | 18777 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +811 | 31454 |
| 19 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +810 | 285683 |
| 20 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +786 | 219649 |
| 21 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +760 | 141473 |
| 22 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +741 | 29913 |
| 23 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +738 | 65204 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +728 | 69183 |
| 25 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +707 | 100546 |
| 26 | [storytold/artcraft](https://github.com/storytold/artcraft) | +660 | 35148 |
| 27 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +642 | 87047 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +636 | 38933 |
| 29 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +626 | 162922 |
| 30 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +621 | 84427 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +117146 | 357410 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +18885 | 18885 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +17747 | 17747 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +17639 | 33753 |
| 5 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +16102 | 62906 |
| 6 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +14158 | 80331 |
| 7 | [storytold/photocraft](https://github.com/storytold/photocraft) | +9633 | 70602 |
| 8 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +9258 | 46333 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +8711 | 101173 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8648 | 299820 |
| 11 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +7933 | 171513 |
| 12 | [storytold/artcraft](https://github.com/storytold/artcraft) | +7311 | 35148 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7286 | 256946 |
| 14 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +6675 | 36273 |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6238 | 285683 |
| 16 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +6130 | 219649 |
| 17 | [yetone/magpie](https://github.com/yetone/magpie) | +6082 | 18777 |
| 18 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +5561 | 43626 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5520 | 69183 |
| 20 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5343 | 29913 |
| 21 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +5191 | 92613 |
| 22 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +5036 | 131566 |
| 23 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +4693 | 67589 |
| 24 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +4573 | 26873 |
| 25 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4288 | 53574 |
| 26 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +4217 | 59502 |
| 27 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +4175 | 100546 |
| 28 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4140 | 31454 |
| 29 | [obra/superpowers](https://github.com/obra/superpowers) | +3994 | 303142 |
| 30 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +3950 | 141473 |
| 31 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +3656 | 38933 |
| 32 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +3650 | 20725 |
| 33 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3549 | 87047 |
| 34 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +3527 | 78204 |
| 35 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3520 | 105664 |
| 36 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3469 | 55919 |
| 37 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3371 | 522366 |
| 38 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +3303 | 16974 |
| 39 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3275 | 100635 |
| 40 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3223 | 84427 |
| 41 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3165 | 65204 |
| 42 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +2990 | 15328 |
| 43 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2977 | 72090 |
| 44 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2963 | 147219 |
| 45 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2852 | 133779 |
| 46 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2827 | 162922 |
| 47 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2824 | 79420 |
| 48 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2686 | 14453 |
| 49 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2683 | 52356 |
| 50 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2646 | 109321 |
| 51 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2641 | 138480 |
| 52 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +2578 | 31644 |
| 53 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2406 | 329032 |
| 54 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2397 | 24635 |
| 55 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2389 | 58808 |
| 56 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +2389 | 31762 |
| 57 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2358 | 491122 |
| 58 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2352 | 193922 |
| 59 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2336 | 70603 |
| 60 | [blader/humanizer](https://github.com/blader/humanizer) | +2333 | 59283 |
| 61 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +2298 | 15554 |
| 62 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2232 | 114121 |
| 63 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +2216 | 38779 |
| 64 | [usestrix/strix](https://github.com/usestrix/strix) | +2201 | 70795 |
| 65 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2187 | 199982 |
| 66 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2153 | 48411 |
| 67 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2130 | 221934 |
| 68 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2090 | 255879 |
| 69 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +2072 | 252166 |
| 70 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2051 | 42801 |
| 71 | [cursor/plugins](https://github.com/cursor/plugins) | +2003 | 13388 |
| 72 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1935 | 22269 |
| 73 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1930 | 555181 |
| 74 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1930 | 66041 |
| 75 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1913 | 103080 |
| 76 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1913 | 15882 |
| 77 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1883 | 62437 |
| 78 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1875 | 152744 |
| 79 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1857 | 77227 |
| 80 | [google/artemis](https://github.com/google/artemis) | +1853 | 13552 |
| 81 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1842 | 81045 |
| 82 | [tw93/Mole](https://github.com/tw93/Mole) | +1838 | 72195 |
| 83 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1831 | 76395 |
| 84 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1822 | 329263 |
| 85 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1771 | 116954 |
| 86 | [lexmount/moli](https://github.com/lexmount/moli) | +1669 | 20044 |
| 87 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +1640 | 14207 |
| 88 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1634 | 49917 |
| 89 | [anthropics/skills](https://github.com/anthropics/skills) | +1598 | 182750 |
| 90 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1595 | 152979 |
| 91 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1560 | 29144 |
| 92 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +1541 | 55691 |
| 93 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1526 | 28737 |
| 94 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1515 | 57289 |
| 95 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1486 | 31163 |
| 96 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1465 | 40148 |
| 97 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1444 | 89037 |
| 98 | [supabase/supabase](https://github.com/supabase/supabase) | +1407 | 112962 |
| 99 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1404 | 102147 |
| 100 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1404 | 17339 |
| 101 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1386 | 122746 |
| 102 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1379 | 183523 |
| 103 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1369 | 112570 |
| 104 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1369 | 53354 |
| 105 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1367 | 32200 |
| 106 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1304 | 43230 |
| 107 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +1291 | 15557 |
| 108 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1241 | 21109 |
| 109 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1228 | 191478 |
| 110 | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | +1222 | 12460 |
| 111 | [torvalds/linux](https://github.com/torvalds/linux) | +1209 | 253046 |
| 112 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1209 | 189637 |
| 113 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +1191 | 18825 |
| 114 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1189 | 87482 |
| 115 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1161 | 45202 |
| 116 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +1154 | 95584 |
| 117 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1138 | 19910 |
| 118 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +1138 | 12984 |
| 119 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1121 | 18513 |
| 120 | [openai/codex](https://github.com/openai/codex) | +1079 | 130310 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +70602 | 70602 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +33753 | 33753 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +29913 | 29913 |
| 4 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +18885 | 18885 |
| 5 | [yetone/magpie](https://github.com/yetone/magpie) | +18777 | 18777 |
| 6 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +18502 | 18502 |
| 7 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +17747 | 17747 |
| 8 | [google-research/harness2](https://github.com/google-research/harness2) | +17179 | 17179 |
| 9 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +16974 | 16974 |
| 10 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +15554 | 15554 |
| 11 | [openai/math](https://github.com/openai/math) | +15347 | 15347 |
| 12 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +15328 | 15328 |
| 13 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14207 | 14207 |
| 14 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +12226 | 12226 |
| 15 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +11965 | 11965 |
