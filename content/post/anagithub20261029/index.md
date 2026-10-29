---
title: "2026-10-29 GitHub增长趋势报告"
description: "1.rea+5290 2.impeccable+2667 3.DeepTutor+2055 4.dsh-our-free-model+2009 5.LinkSwift+1684"
date: 2026-10-30T07:54:13+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-30 07:54:13

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
        'daily': {"categories": ["ifixai-ai/iFixAi", "Graphify-Labs/graphify", "mattpocock/skills", "YuJunZhiXue/dsh-purge", "affaan-m/ECC", "DietrichGebert/ponytail", "deepseek-ai/deepseek-harness", "Leonxlnx/taste-skill", "obra/superpowers", "KnifeLemon/Filee", "stablyai/orca", "cloudflare/security-audit-skill", "debpalash/VoiceStudio", "Nutlope/hallmark", "Gathin23/cleanyourtv", "hmjz100/LinkSwift", "Ebony-Vinyl/dsh-our-free-model", "HKUDS/DeepTutor", "pbakaus/impeccable", "morluto/rea"], "data": [817, 830, 853, 923, 949, 981, 996, 1075, 1095, 1101, 1153, 1181, 1298, 1405, 1635, 1684, 2009, 2055, 2667, 5290]},
        'weekly': {"categories": ["Panniantong/Agent-Reach", "TauricResearch/TradingAgents", "Niko1221/Strata", "heygen-com/hyperframes", "mattpocock/skills", "Graphify-Labs/graphify", "yetone/magpie", "affaan-m/ECC", "DietrichGebert/ponytail", "stablyai/orca", "deepseek-ai/deepseek-harness", "HKUDS/DeepTutor", "hmjz100/LinkSwift", "pbakaus/impeccable", "Nutlope/hallmark", "debpalash/VoiceStudio", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5270, 5327, 5389, 5478, 5749, 5768, 5867, 6199, 6769, 7458, 7632, 7817, 9116, 10295, 11307, 12556, 13383, 14155, 21614, 41808]},
        'monthly': {"categories": ["tangency-labs/solidcraft", "Zagitta/gpu-unlock", "storytold/lightcraft", "storytold/wordcraft", "storytold/filmcraft", "openai/math", "KnifeLemon/Filee", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [12043, 13063, 15052, 16607, 16859, 17066, 17397, 18628, 21305, 22599, 24242, 45457, 74824]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +5290 | 407700 |
| 2 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2667 | 95256 |
| 3 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2055 | 49981 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2009 | 50860 |
| 5 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +1684 | 36230 |
| 6 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +1635 | 45457 |
| 7 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +1405 | 42071 |
| 8 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1298 | 94263 |
| 9 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1181 | 52822 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | +1153 | 110162 |
| 11 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +1101 | 17397 |
| 12 | [obra/superpowers](https://github.com/obra/superpowers) | +1095 | 308515 |
| 13 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1075 | 105512 |
| 14 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +996 | 265770 |
| 15 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +981 | 180149 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +949 | 292690 |
| 17 | [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | +923 | 13071 |
| 18 | [mattpocock/skills](https://github.com/mattpocock/skills) | +853 | 306599 |
| 19 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +830 | 138655 |
| 20 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +817 | 37873 |
| 21 | [yetone/magpie](https://github.com/yetone/magpie) | +804 | 25364 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +742 | 75454 |
| 23 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +719 | 104749 |
| 24 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +706 | 13063 |
| 25 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +687 | 56190 |
| 26 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +673 | 106285 |
| 27 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +668 | 29135 |
| 28 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +663 | 35975 |
| 29 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +662 | 31830 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +653 | 44014 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +41808 | 407700 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +21614 | 45457 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +14155 | 50860 |
| 4 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +13383 | 52822 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12556 | 94263 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +11307 | 42071 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +10295 | 95256 |
| 8 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +9116 | 36230 |
| 9 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +7817 | 49981 |
| 10 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7632 | 265770 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +7458 | 110162 |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +6769 | 180149 |
| 13 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6199 | 292690 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +5867 | 25364 |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +5768 | 138655 |
| 16 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5749 | 306599 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5478 | 75454 |
| 18 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5389 | 35975 |
| 19 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +5327 | 118313 |
| 20 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +5270 | 106285 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4838 | 70817 |
| 22 | [obra/superpowers](https://github.com/obra/superpowers) | +4800 | 308515 |
| 23 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4724 | 37873 |
| 24 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +4472 | 17579 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4443 | 44014 |
| 26 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +4417 | 24242 |
| 27 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +4404 | 105512 |
| 28 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4263 | 23983 |
| 29 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +3993 | 67525 |
| 30 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +3914 | 226418 |
| 31 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3840 | 91426 |
| 32 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3691 | 526839 |
| 33 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3538 | 142534 |
| 34 | [storytold/photocraft](https://github.com/storytold/photocraft) | +3498 | 74824 |
| 35 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +3476 | 22599 |
| 36 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3461 | 56190 |
| 37 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +3439 | 16132 |
| 38 | [google-research/harness2](https://github.com/google-research/harness2) | +3337 | 21305 |
| 39 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3285 | 71255 |
| 40 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +3262 | 203703 |
| 41 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3131 | 75590 |
| 42 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +3009 | 20690 |
| 43 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +2986 | 46129 |
| 44 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2871 | 62890 |
| 45 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2862 | 223051 |
| 46 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +2741 | 95870 |
| 47 | [blader/humanizer](https://github.com/blader/humanizer) | +2719 | 62352 |
| 48 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +2705 | 49566 |
| 49 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2701 | 82574 |
| 50 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2698 | 51431 |
| 51 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2521 | 68885 |
| 52 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +2513 | 40107 |
| 53 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2488 | 108635 |
| 54 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2477 | 196764 |
| 55 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2474 | 331814 |
| 56 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +2418 | 104749 |
| 57 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2409 | 17320 |
| 58 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2397 | 150062 |
| 59 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2392 | 31830 |
| 60 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2380 | 101570 |
| 61 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2360 | 23357 |
| 62 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +2358 | 28102 |
| 63 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2287 | 33843 |
| 64 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2286 | 64937 |
| 65 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2273 | 258505 |
| 66 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2137 | 73018 |
| 67 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +2125 | 59629 |
| 68 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2098 | 111743 |
| 69 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2084 | 136305 |
| 70 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +2079 | 33738 |
| 71 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +2077 | 78681 |
| 72 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2072 | 61172 |
| 73 | [storytold/artcraft](https://github.com/storytold/artcraft) | +2067 | 37657 |
| 74 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1981 | 143987 |
| 75 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1963 | 44762 |
| 76 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1959 | 19485 |
| 77 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1955 | 29135 |
| 78 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1926 | 165166 |
| 79 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1905 | 254308 |
| 80 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1884 | 557363 |
| 81 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1875 | 20669 |
| 82 | [google/artemis](https://github.com/google/artemis) | +1865 | 15671 |
| 83 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1850 | 493259 |
| 84 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1834 | 185571 |
| 85 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1786 | 65263 |
| 86 | [anthropics/skills](https://github.com/anthropics/skills) | +1768 | 184792 |
| 87 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1706 | 14683 |
| 88 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1702 | 331195 |
| 89 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1702 | 154913 |
| 90 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +1701 | 23384 |
| 91 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1699 | 116096 |
| 92 | [openai/math](https://github.com/openai/math) | +1676 | 17066 |
| 93 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1666 | 80140 |
| 94 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +1665 | 14429 |
| 95 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1663 | 26493 |
| 96 | [usestrix/strix](https://github.com/usestrix/strix) | +1599 | 72754 |
| 97 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1598 | 24134 |
| 98 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1595 | 118804 |
| 99 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1580 | 44964 |
| 100 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1577 | 34026 |
| 101 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1548 | 22678 |
| 102 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1545 | 124491 |
| 103 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1529 | 104871 |
| 104 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +1527 | 29750 |
| 105 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1490 | 57713 |
| 106 | [github/spec-kit](https://github.com/github/spec-kit) | +1451 | 143913 |
| 107 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1422 | 82722 |
| 108 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1418 | 18628 |
| 109 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1417 | 45297 |
| 110 | [lexmount/moli](https://github.com/lexmount/moli) | +1408 | 21530 |
| 111 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1389 | 55269 |
| 112 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1388 | 30729 |
| 113 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1355 | 21496 |
| 114 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | +1346 | 58576 |
| 115 | [thesysdev/openui](https://github.com/thesysdev/openui) | +1343 | 14433 |
| 116 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1305 | 57332 |
| 117 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +1263 | 196866 |
| 118 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1261 | 22424 |
| 119 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1243 | 191054 |
| 120 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1237 | 192896 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +74824 | 74824 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +45457 | 45457 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +24242 | 24242 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +22599 | 22599 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +21305 | 21305 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +18628 | 18628 |
| 7 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +17397 | 17397 |
| 8 | [openai/math](https://github.com/openai/math) | +17066 | 17066 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16859 | 16859 |
| 10 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16607 | 16607 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +15052 | 15052 |
| 12 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +13063 | 13063 |
| 13 | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | +12043 | 12043 |
