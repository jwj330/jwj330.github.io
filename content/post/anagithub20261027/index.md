---
title: "2026-10-27 GitHub增长趋势报告"
description: "1.rea+5758 2.LinkSwift+3009 3.hallmark+2702 4.cleanyourtv+2640 5.VoiceStudio+2127"
date: 2026-10-28T07:39:23+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-28 07:39:23

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
        'daily': {"categories": ["ifixai-ai/iFixAi", "gitroomhq/postiz-app", "stablyai/orca", "alchaincyf/huashu-design", "yetone/magpie", "affaan-m/ECC", "DietrichGebert/ponytail", "deepseek-ai/deepseek-harness", "TauricResearch/TradingAgents", "pbakaus/impeccable", "Panniantong/Agent-Reach", "KnifeLemon/Filee", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "HKUDS/DeepTutor", "debpalash/VoiceStudio", "Gathin23/cleanyourtv", "Nutlope/hallmark", "hmjz100/LinkSwift", "morluto/rea"], "data": [891, 910, 992, 1008, 1017, 1041, 1050, 1100, 1255, 1326, 1374, 1582, 1613, 1956, 2014, 2127, 2640, 2702, 3009, 5758]},
        'weekly': {"categories": ["google-research/harness2", "Niko1221/Strata", "heygen-com/hyperframes", "yetone/magpie", "affaan-m/ECC", "mattpocock/skills", "ai-job-search-dev/ai-job-search", "hmjz100/LinkSwift", "pbakaus/impeccable", "Graphify-Labs/graphify", "deepseek-ai/deepseek-harness", "stablyai/orca", "Nutlope/hallmark", "DietrichGebert/ponytail", "deepseek-ai/DeepInfer", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5316, 5372, 5460, 5636, 5977, 6252, 6366, 6496, 6655, 6782, 7910, 8344, 8478, 8596, 11450, 12368, 15935, 16079, 30300, 49682]},
        'monthly': {"categories": ["tangency-labs/solidcraft", "Zagitta/gpu-unlock", "yihui-dev/awesome-opus5-5-videos", "KnifeLemon/Filee", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [11237, 11299, 11943, 14701, 14866, 16019, 16366, 16574, 18234, 20532, 21436, 23394, 41795, 73916]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +5758 | 397205 |
| 2 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +3009 | 32996 |
| 3 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +2702 | 38928 |
| 4 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +2640 | 41795 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2127 | 91274 |
| 6 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2014 | 45805 |
| 7 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1956 | 46746 |
| 8 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1613 | 50121 |
| 9 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +1582 | 14701 |
| 10 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1374 | 104894 |
| 11 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1326 | 90461 |
| 12 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1255 | 117294 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1100 | 263648 |
| 14 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1050 | 178150 |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +1041 | 290850 |
| 16 | [yetone/magpie](https://github.com/yetone/magpie) | +1017 | 23577 |
| 17 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +1008 | 27726 |
| 18 | [stablyai/orca](https://github.com/stablyai/orca) | +992 | 108017 |
| 19 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +910 | 39331 |
| 20 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +891 | 35934 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +880 | 73915 |
| 22 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +856 | 225470 |
| 23 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +848 | 34544 |
| 24 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +833 | 136947 |
| 25 | [peach-mitao/peach](https://github.com/peach-mitao/peach) | +818 | 12988 |
| 26 | [mattpocock/skills](https://github.com/mattpocock/skills) | +806 | 304859 |
| 27 | [obra/superpowers](https://github.com/obra/superpowers) | +805 | 306402 |
| 28 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +684 | 69575 |
| 29 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +679 | 103659 |
| 30 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +654 | 90432 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +49682 | 397205 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +30300 | 41795 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +16079 | 50121 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +15935 | 46746 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +12368 | 91274 |
| 6 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +11450 | 23394 |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +8596 | 178150 |
| 8 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +8478 | 38928 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +8344 | 108017 |
| 10 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +7910 | 263648 |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +6782 | 136947 |
| 12 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +6655 | 90461 |
| 13 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +6496 | 32996 |
| 14 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +6366 | 66780 |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills) | +6252 | 304859 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +5977 | 290850 |
| 17 | [yetone/magpie](https://github.com/yetone/magpie) | +5636 | 23577 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5460 | 73915 |
| 19 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5372 | 34544 |
| 20 | [google-research/harness2](https://github.com/google-research/harness2) | +5316 | 20532 |
| 21 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5291 | 35934 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +5109 | 69575 |
| 23 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +4960 | 117294 |
| 24 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +4689 | 17107 |
| 25 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +4623 | 104894 |
| 26 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4427 | 42724 |
| 27 | [storytold/photocraft](https://github.com/storytold/photocraft) | +4321 | 73916 |
| 28 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +4027 | 90432 |
| 29 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +3948 | 225470 |
| 30 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +3909 | 45805 |
| 31 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +3888 | 21436 |
| 32 | [obra/superpowers](https://github.com/obra/superpowers) | +3823 | 306402 |
| 33 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3820 | 103659 |
| 34 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3801 | 525721 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3575 | 141560 |
| 36 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +3532 | 49014 |
| 37 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +3509 | 15295 |
| 38 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3508 | 222371 |
| 39 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3502 | 45586 |
| 40 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +3456 | 20279 |
| 41 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +3284 | 202996 |
| 42 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +3254 | 22728 |
| 43 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +2955 | 95068 |
| 44 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2909 | 81866 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2902 | 74682 |
| 46 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +2902 | 69959 |
| 47 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +2846 | 143559 |
| 48 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2814 | 61777 |
| 49 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2784 | 108012 |
| 50 | [storytold/artcraft](https://github.com/storytold/artcraft) | +2682 | 37170 |
| 51 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2660 | 50699 |
| 52 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2652 | 68259 |
| 53 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2640 | 33413 |
| 54 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2602 | 196066 |
| 55 | [blader/humanizer](https://github.com/blader/humanizer) | +2600 | 61486 |
| 56 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2580 | 149373 |
| 57 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2425 | 16580 |
| 58 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2413 | 135836 |
| 59 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2409 | 54427 |
| 60 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2400 | 331095 |
| 61 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +2392 | 23264 |
| 62 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2230 | 164526 |
| 63 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2175 | 72459 |
| 64 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +2174 | 14072 |
| 65 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2171 | 257742 |
| 66 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2171 | 60688 |
| 67 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +2158 | 27726 |
| 68 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2152 | 111124 |
| 69 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2145 | 64310 |
| 70 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +2054 | 77909 |
| 71 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2004 | 22725 |
| 72 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1986 | 22310 |
| 73 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1982 | 20129 |
| 74 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1976 | 79781 |
| 75 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1962 | 30819 |
| 76 | [usestrix/strix](https://github.com/usestrix/strix) | +1928 | 72347 |
| 77 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +1928 | 33541 |
| 78 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1920 | 19090 |
| 79 | [google/artemis](https://github.com/google/artemis) | +1907 | 15162 |
| 80 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1864 | 253769 |
| 81 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +1858 | 39331 |
| 82 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1847 | 492701 |
| 83 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1826 | 556662 |
| 84 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1792 | 26078 |
| 85 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1775 | 65071 |
| 86 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1773 | 57427 |
| 87 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1767 | 30286 |
| 88 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1766 | 103718 |
| 89 | [anthropics/skills](https://github.com/anthropics/skills) | +1758 | 184244 |
| 90 | [supabase/supabase](https://github.com/supabase/supabase) | +1744 | 114176 |
| 91 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1737 | 44170 |
| 92 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1729 | 58807 |
| 93 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1689 | 185006 |
| 94 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1688 | 54945 |
| 95 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1686 | 115536 |
| 96 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1683 | 330695 |
| 97 | [thesysdev/openui](https://github.com/thesysdev/openui) | +1634 | 14286 |
| 98 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1631 | 43956 |
| 99 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1623 | 154364 |
| 100 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1614 | 17145 |
| 101 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1611 | 33598 |
| 102 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1597 | 18234 |
| 103 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1585 | 118285 |
| 104 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1582 | 23558 |
| 105 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1580 | 104382 |
| 106 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1546 | 44940 |
| 107 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1507 | 82369 |
| 108 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1493 | 124007 |
| 109 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1429 | 14095 |
| 110 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1400 | 100317 |
| 111 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1393 | 21119 |
| 112 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1342 | 51000 |
| 113 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1334 | 88577 |
| 114 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +1322 | 39862 |
| 115 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1315 | 78041 |
| 116 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +1314 | 16366 |
| 117 | [lexmount/moli](https://github.com/lexmount/moli) | +1301 | 21172 |
| 118 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +1292 | 95709 |
| 119 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +1290 | 68756 |
| 120 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +1265 | 16574 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +73916 | 73916 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +41795 | 41795 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +23394 | 23394 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +21436 | 21436 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +20532 | 20532 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +18234 | 18234 |
| 7 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16574 | 16574 |
| 8 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16366 | 16366 |
| 9 | [openai/math](https://github.com/openai/math) | +16019 | 16019 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14866 | 14866 |
| 11 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +14701 | 14701 |
| 12 | [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | +11943 | 11943 |
| 13 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +11299 | 11299 |
| 14 | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | +11237 | 11237 |
