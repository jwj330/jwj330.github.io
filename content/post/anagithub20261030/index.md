---
title: "2026-10-30 GitHub增长趋势报告"
description: "1.rea+4504 2.dsh-our-free-model+1912 3.DeepTutor+1755 4.impeccable+1745 5.VoiceStudio+1437"
date: 2026-10-31T07:34:17+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-31 07:34:17

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
        'daily': {"categories": ["DietrichGebert/ponytail", "Graphify-Labs/graphify", "mattpocock/skills", "Nutlope/hallmark", "pingdotgg/t3code", "yetone/magpie", "obra/superpowers", "stablyai/orca", "deepseek-ai/deepseek-harness", "KnifeLemon/Filee", "Gathin23/cleanyourtv", "cloudflare/security-audit-skill", "ifixai-ai/iFixAi", "Donchitos/Claude-Code-Game-Studios", "thedotmack/claude-mem", "debpalash/VoiceStudio", "pbakaus/impeccable", "HKUDS/DeepTutor", "Ebony-Vinyl/dsh-our-free-model", "morluto/rea"], "data": [798, 799, 843, 877, 878, 880, 888, 927, 948, 1048, 1238, 1256, 1259, 1277, 1428, 1437, 1745, 1755, 1912, 4504]},
        'weekly': {"categories": ["TauricResearch/TradingAgents", "Niko1221/Strata", "ifixai-ai/iFixAi", "Panniantong/Agent-Reach", "Graphify-Labs/graphify", "mattpocock/skills", "yetone/magpie", "affaan-m/ECC", "DietrichGebert/ponytail", "stablyai/orca", "deepseek-ai/deepseek-harness", "hmjz100/LinkSwift", "HKUDS/DeepTutor", "pbakaus/impeccable", "Nutlope/hallmark", "cloudflare/security-audit-skill", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5315, 5350, 5408, 5469, 5571, 5658, 6053, 6101, 6183, 7294, 7312, 9288, 9451, 11494, 11621, 12039, 12464, 13700, 18906, 39264]},
        'monthly': {"categories": ["tangency-labs/solidcraft", "Zagitta/gpu-unlock", "storytold/lightcraft", "storytold/wordcraft", "storytold/filmcraft", "openai/math", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [12369, 13477, 15106, 16745, 16956, 17135, 18780, 21504, 23010, 24489, 46695, 75217]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +4504 | 412204 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1912 | 52772 |
| 3 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1755 | 51736 |
| 4 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1745 | 97001 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1437 | 95700 |
| 6 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1428 | 106177 |
| 7 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1277 | 30412 |
| 8 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +1259 | 39132 |
| 9 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1256 | 54078 |
| 10 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +1238 | 46695 |
| 11 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +1048 | 18445 |
| 12 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +948 | 266718 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +927 | 111089 |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | +888 | 309403 |
| 15 | [yetone/magpie](https://github.com/yetone/magpie) | +880 | 26244 |
| 16 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +878 | 32708 |
| 17 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +877 | 42948 |
| 18 | [mattpocock/skills](https://github.com/mattpocock/skills) | +843 | 307442 |
| 19 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +799 | 139454 |
| 20 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +798 | 180947 |
| 21 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +794 | 106306 |
| 22 | [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | +781 | 13852 |
| 23 | [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) | +752 | 12857 |
| 24 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +698 | 293388 |
| 25 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +648 | 38325 |
| 26 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +647 | 527486 |
| 27 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +634 | 44648 |
| 28 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +575 | 76029 |
| 29 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +553 | 51984 |
| 30 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +533 | 31262 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +39264 | 412204 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +18906 | 46695 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +13700 | 52772 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12464 | 95700 |
| 5 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +12039 | 54078 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +11621 | 42948 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +11494 | 97001 |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +9451 | 51736 |
| 9 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +9288 | 36629 |
| 10 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7312 | 266718 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +7294 | 111089 |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +6183 | 180947 |
| 13 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6101 | 293388 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +6053 | 26244 |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5658 | 307442 |
| 16 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +5571 | 139454 |
| 17 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +5469 | 106799 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5408 | 39132 |
| 19 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5350 | 36486 |
| 20 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +5315 | 118697 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5269 | 76029 |
| 22 | [obra/superpowers](https://github.com/obra/superpowers) | +5176 | 309403 |
| 23 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +4699 | 106306 |
| 24 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4625 | 24494 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4569 | 71307 |
| 26 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4409 | 44648 |
| 27 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +3930 | 226840 |
| 28 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +3879 | 67962 |
| 29 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3851 | 527486 |
| 30 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +3628 | 106177 |
| 31 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3606 | 143029 |
| 32 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3544 | 91820 |
| 33 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +3538 | 17729 |
| 34 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3516 | 56634 |
| 35 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +3420 | 24489 |
| 36 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +3344 | 23010 |
| 37 | [storytold/photocraft](https://github.com/storytold/photocraft) | +3289 | 75217 |
| 38 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3279 | 71602 |
| 39 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +3193 | 16465 |
| 40 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +3114 | 30412 |
| 41 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +3057 | 32708 |
| 42 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +3039 | 203981 |
| 43 | [google-research/harness2](https://github.com/google-research/harness2) | +2962 | 21504 |
| 44 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2942 | 75740 |
| 45 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2923 | 51984 |
| 46 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2911 | 63253 |
| 47 | [blader/humanizer](https://github.com/blader/humanizer) | +2732 | 62718 |
| 48 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2714 | 223315 |
| 49 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +2581 | 40236 |
| 50 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +2560 | 96187 |
| 51 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2515 | 17741 |
| 52 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2506 | 82883 |
| 53 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +2477 | 49839 |
| 54 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2458 | 332140 |
| 55 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2453 | 101760 |
| 56 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2445 | 23533 |
| 57 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2427 | 197098 |
| 58 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2421 | 69127 |
| 59 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2402 | 108977 |
| 60 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2361 | 150398 |
| 61 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2348 | 258870 |
| 62 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +2332 | 34027 |
| 63 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2321 | 65211 |
| 64 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +2320 | 28226 |
| 65 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2230 | 46219 |
| 66 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2224 | 73400 |
| 67 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +2204 | 59890 |
| 68 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2156 | 61511 |
| 69 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2086 | 111993 |
| 70 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2078 | 45075 |
| 71 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +2061 | 78894 |
| 72 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2027 | 136595 |
| 73 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +2021 | 20767 |
| 74 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1993 | 165496 |
| 75 | [anthropics/skills](https://github.com/anthropics/skills) | +1991 | 185276 |
| 76 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1935 | 557636 |
| 77 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1901 | 15135 |
| 78 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1881 | 493550 |
| 79 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1878 | 254555 |
| 80 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1863 | 144197 |
| 81 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1852 | 185793 |
| 82 | [storytold/artcraft](https://github.com/storytold/artcraft) | +1849 | 37829 |
| 83 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1849 | 34032 |
| 84 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1841 | 20858 |
| 85 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1774 | 26877 |
| 86 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1744 | 155169 |
| 87 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1738 | 65328 |
| 88 | [google/artemis](https://github.com/google/artemis) | +1727 | 15816 |
| 89 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1703 | 116327 |
| 90 | [openai/math](https://github.com/openai/math) | +1702 | 17135 |
| 91 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1696 | 31262 |
| 92 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +1686 | 29974 |
| 93 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1682 | 331406 |
| 94 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1601 | 45206 |
| 95 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1601 | 24345 |
| 96 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1587 | 119022 |
| 97 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +1583 | 14606 |
| 98 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1550 | 19634 |
| 99 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1542 | 124698 |
| 100 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1527 | 80294 |
| 101 | [github/spec-kit](https://github.com/github/spec-kit) | +1525 | 144123 |
| 102 | [usestrix/strix](https://github.com/usestrix/strix) | +1506 | 72945 |
| 103 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1493 | 34171 |
| 104 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1461 | 22846 |
| 105 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1453 | 105041 |
| 106 | [lexmount/moli](https://github.com/lexmount/moli) | +1422 | 21734 |
| 107 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +1409 | 38325 |
| 108 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1385 | 46934 |
| 109 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1372 | 22584 |
| 110 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1369 | 82893 |
| 111 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1352 | 18780 |
| 112 | [localsend/localsend](https://github.com/localsend/localsend) | +1348 | 96693 |
| 113 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1333 | 45440 |
| 114 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1318 | 50592 |
| 115 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | +1307 | 58644 |
| 116 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1286 | 21638 |
| 117 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +1285 | 18993 |
| 118 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +1284 | 196998 |
| 119 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1275 | 57512 |
| 120 | [openai/codex](https://github.com/openai/codex) | +1272 | 131917 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +75217 | 75217 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +46695 | 46695 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +24489 | 24489 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +23010 | 23010 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +21504 | 21504 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +18780 | 18780 |
| 7 | [openai/math](https://github.com/openai/math) | +17135 | 17135 |
| 8 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16956 | 16956 |
| 9 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16745 | 16745 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +15106 | 15106 |
| 11 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +13477 | 13477 |
| 12 | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | +12369 | 12369 |
