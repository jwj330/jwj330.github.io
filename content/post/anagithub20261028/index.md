---
title: "2026-10-28 GitHub增长趋势报告"
description: "1.rea+5205 2.impeccable+2128 3.DeepTutor+2121 4.dsh-our-free-model+2105 5.cleanyourtv+2027"
date: 2026-10-29T07:59:32+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-29 07:59:32

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
        'daily': {"categories": ["mattpocock/skills", "affaan-m/ECC", "yetone/magpie", "stablyai/orca", "DietrichGebert/ponytail", "obra/superpowers", "Zagitta/gpu-unlock", "vectorize-io/hindsight", "ifixai-ai/iFixAi", "deepseek-ai/deepseek-harness", "cloudflare/security-audit-skill", "hmjz100/LinkSwift", "KnifeLemon/Filee", "debpalash/VoiceStudio", "Nutlope/hallmark", "Gathin23/cleanyourtv", "Ebony-Vinyl/dsh-our-free-model", "HKUDS/DeepTutor", "pbakaus/impeccable", "morluto/rea"], "data": [887, 891, 983, 992, 1018, 1018, 1058, 1076, 1122, 1126, 1520, 1550, 1595, 1691, 1738, 2027, 2105, 2121, 2128, 5205]},
        'weekly': {"categories": ["Niko1221/Strata", "heygen-com/hyperframes", "ifixai-ai/iFixAi", "yetone/magpie", "HKUDS/DeepTutor", "mattpocock/skills", "affaan-m/ECC", "deepseek-ai/DeepInfer", "Graphify-Labs/graphify", "DietrichGebert/ponytail", "hmjz100/LinkSwift", "deepseek-ai/deepseek-harness", "stablyai/orca", "pbakaus/impeccable", "Nutlope/hallmark", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5399, 5529, 5602, 5783, 5907, 5926, 6058, 6165, 6259, 7655, 7673, 7828, 7836, 8162, 10093, 12634, 15098, 15368, 24937, 45000]},
        'monthly': {"categories": ["tangency-labs/solidcraft", "Zagitta/gpu-unlock", "storytold/lightcraft", "KnifeLemon/Filee", "storytold/wordcraft", "openai/math", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [11647, 12357, 14978, 16296, 16474, 16630, 16727, 18449, 21012, 22089, 23912, 43822, 74399]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +5205 | 402410 |
| 2 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2128 | 92589 |
| 3 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2121 | 47926 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2105 | 48851 |
| 5 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +2027 | 43822 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +1738 | 40666 |
| 7 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1691 | 92965 |
| 8 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +1595 | 16296 |
| 9 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +1550 | 34546 |
| 10 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1520 | 51641 |
| 11 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1126 | 264774 |
| 12 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +1122 | 37056 |
| 13 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +1076 | 55503 |
| 14 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +1058 | 12357 |
| 15 | [obra/superpowers](https://github.com/obra/superpowers) | +1018 | 307420 |
| 16 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1018 | 179168 |
| 17 | [stablyai/orca](https://github.com/stablyai/orca) | +992 | 109009 |
| 18 | [yetone/magpie](https://github.com/yetone/magpie) | +983 | 24560 |
| 19 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +891 | 291741 |
| 20 | [mattpocock/skills](https://github.com/mattpocock/skills) | +887 | 305746 |
| 21 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +878 | 137825 |
| 22 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +797 | 74712 |
| 23 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +778 | 104437 |
| 24 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +768 | 35312 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +718 | 105612 |
| 26 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +701 | 101018 |
| 27 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +692 | 18443 |
| 28 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +668 | 70627 |
| 29 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +654 | 62431 |
| 30 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +653 | 22089 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +45000 | 402410 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +24937 | 43822 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +15368 | 51641 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +15098 | 48851 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12634 | 92965 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +10093 | 40666 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +8162 | 92589 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +7836 | 109009 |
| 9 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7828 | 264774 |
| 10 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +7673 | 34546 |
| 11 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +7655 | 179168 |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +6259 | 137825 |
| 13 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +6165 | 23912 |
| 14 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6058 | 291741 |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5926 | 305746 |
| 16 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +5907 | 47926 |
| 17 | [yetone/magpie](https://github.com/yetone/magpie) | +5783 | 24560 |
| 18 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5602 | 37056 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5529 | 74712 |
| 20 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5399 | 35312 |
| 21 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +5301 | 117871 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5006 | 70210 |
| 23 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +4977 | 105612 |
| 24 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +4546 | 17321 |
| 25 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4428 | 43361 |
| 26 | [obra/superpowers](https://github.com/obra/superpowers) | +4278 | 307420 |
| 27 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +4270 | 67176 |
| 28 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +4037 | 225971 |
| 29 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3941 | 526307 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3937 | 90984 |
| 31 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3891 | 104437 |
| 32 | [google-research/harness2](https://github.com/google-research/harness2) | +3833 | 21012 |
| 33 | [storytold/photocraft](https://github.com/storytold/photocraft) | +3797 | 74399 |
| 34 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3774 | 23357 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3592 | 142072 |
| 36 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +3587 | 22089 |
| 37 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +3563 | 20570 |
| 38 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +3537 | 15763 |
| 39 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +3412 | 203394 |
| 40 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3395 | 45879 |
| 41 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3229 | 75319 |
| 42 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3147 | 55503 |
| 43 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3100 | 222749 |
| 44 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3038 | 70627 |
| 45 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +2970 | 49303 |
| 46 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2929 | 62431 |
| 47 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +2904 | 95517 |
| 48 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2838 | 82258 |
| 49 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2683 | 51094 |
| 50 | [blader/humanizer](https://github.com/blader/humanizer) | +2658 | 61941 |
| 51 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2625 | 108289 |
| 52 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2580 | 17033 |
| 53 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2561 | 68602 |
| 54 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2508 | 149727 |
| 55 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2495 | 196417 |
| 56 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2488 | 33651 |
| 57 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +2418 | 39960 |
| 58 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +2415 | 23322 |
| 59 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2411 | 331443 |
| 60 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2350 | 136129 |
| 61 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +2316 | 143789 |
| 62 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +2293 | 27960 |
| 63 | [storytold/artcraft](https://github.com/storytold/artcraft) | +2270 | 37418 |
| 64 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2246 | 23066 |
| 65 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2192 | 258071 |
| 66 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2189 | 64626 |
| 67 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2136 | 111457 |
| 68 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2128 | 72731 |
| 69 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2124 | 60932 |
| 70 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +2042 | 33677 |
| 71 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2024 | 31168 |
| 72 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +2006 | 14302 |
| 73 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1971 | 78366 |
| 74 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1970 | 19309 |
| 75 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1969 | 101018 |
| 76 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1950 | 164872 |
| 77 | [google/artemis](https://github.com/google/artemis) | +1892 | 15444 |
| 78 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1886 | 493008 |
| 79 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1883 | 104030 |
| 80 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1877 | 44493 |
| 81 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1870 | 20383 |
| 82 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1867 | 254033 |
| 83 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1847 | 59136 |
| 84 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1833 | 65205 |
| 85 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1801 | 22526 |
| 86 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1781 | 185304 |
| 87 | [usestrix/strix](https://github.com/usestrix/strix) | +1772 | 72567 |
| 88 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1769 | 79973 |
| 89 | [anthropics/skills](https://github.com/anthropics/skills) | +1763 | 184513 |
| 90 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1753 | 556934 |
| 91 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1733 | 30470 |
| 92 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1685 | 115806 |
| 93 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1683 | 330946 |
| 94 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1664 | 57583 |
| 95 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1649 | 154628 |
| 96 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1630 | 33830 |
| 97 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1609 | 26244 |
| 98 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1608 | 14388 |
| 99 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1606 | 23875 |
| 100 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1580 | 118534 |
| 101 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1558 | 104638 |
| 102 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1537 | 55111 |
| 103 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1524 | 124270 |
| 104 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1504 | 45130 |
| 105 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1491 | 82536 |
| 106 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1475 | 18449 |
| 107 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1461 | 44691 |
| 108 | [thesysdev/openui](https://github.com/thesysdev/openui) | +1457 | 14373 |
| 109 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +1445 | 29512 |
| 110 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1415 | 21325 |
| 111 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1412 | 28467 |
| 112 | [github/spec-kit](https://github.com/github/spec-kit) | +1353 | 143659 |
| 113 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | +1323 | 196713 |
| 114 | [lexmount/moli](https://github.com/lexmount/moli) | +1298 | 21342 |
| 115 | [supabase/supabase](https://github.com/supabase/supabase) | +1296 | 114258 |
| 116 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1295 | 57126 |
| 117 | [openai/math](https://github.com/openai/math) | +1283 | 16630 |
| 118 | [Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms) | +1280 | 58421 |
| 119 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1279 | 51196 |
| 120 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1273 | 88755 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +74399 | 74399 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +43822 | 43822 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +23912 | 23912 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +22089 | 22089 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +21012 | 21012 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +18449 | 18449 |
| 7 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16727 | 16727 |
| 8 | [openai/math](https://github.com/openai/math) | +16630 | 16630 |
| 9 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16474 | 16474 |
| 10 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +16296 | 16296 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14978 | 14978 |
| 12 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +12357 | 12357 |
| 13 | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | +11647 | 11647 |
