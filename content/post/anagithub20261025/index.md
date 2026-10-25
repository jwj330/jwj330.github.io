---
title: "2026-10-25 GitHub增长趋势报告"
description: "1.rea+5929 2.cleanyourtv+3244 3.security-audit-skill+2370 4.VoiceStudio+1785 5.dsh-our-free-model+1681"
date: 2026-10-26T06:25:34+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-26 06:25:34

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
        'daily': {"categories": ["heygen-com/hyperframes", "AgriciDaniel/claude-seo", "mattpocock/skills", "Panniantong/Agent-Reach", "affaan-m/ECC", "Graphify-Labs/graphify", "Niko1221/Strata", "stablyai/orca", "TauricResearch/TradingAgents", "deepseek-ai/deepseek-harness", "experientiallabs/experiential", "ai-job-search-dev/ai-job-search", "liquidslr/leetcode-company-wise-problems", "pbakaus/impeccable", "Nutlope/hallmark", "Ebony-Vinyl/dsh-our-free-model", "debpalash/VoiceStudio", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [666, 679, 709, 734, 757, 764, 782, 830, 858, 888, 910, 913, 937, 1264, 1563, 1681, 1785, 2370, 3244, 5929]},
        'weekly': {"categories": ["wheresryan22/anatomy", "ifixai-ai/iFixAi", "pbakaus/impeccable", "anomalyco/opencode", "boykopovar/AnyPS5", "Niko1221/Strata", "storytold/photocraft", "heygen-com/hyperframes", "yetone/magpie", "affaan-m/ECC", "Graphify-Labs/graphify", "mattpocock/skills", "deepseek-ai/deepseek-harness", "DietrichGebert/ponytail", "stablyai/orca", "debpalash/VoiceStudio", "ai-job-search-dev/ai-job-search", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "morluto/rea"], "data": [4623, 4850, 4887, 5003, 5116, 5303, 5413, 5432, 5530, 5563, 6788, 7070, 8288, 9149, 9204, 11497, 12794, 15619, 18196, 62933]},
        'monthly': {"categories": ["KnifeLemon/Filee", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "storytold/photocraft"], "data": [12223, 14644, 15508, 16040, 16269, 17827, 19580, 20569, 22369, 34802, 72806]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +5929 | 384275 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +3244 | 34802 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2370 | 46730 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1785 | 86644 |
| 5 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1681 | 42884 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +1563 | 33615 |
| 7 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1264 | 87589 |
| 8 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +937 | 32656 |
| 9 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +913 | 65684 |
| 10 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | +910 | 12804 |
| 11 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +888 | 261330 |
| 12 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +858 | 114514 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +830 | 105731 |
| 14 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +782 | 32729 |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +764 | 135162 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +757 | 288796 |
| 17 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +734 | 102454 |
| 18 | [mattpocock/skills](https://github.com/mattpocock/skills) | +709 | 303189 |
| 19 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +679 | 20762 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +666 | 72110 |
| 21 | [yetone/magpie](https://github.com/yetone/magpie) | +663 | 21422 |
| 22 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +662 | 68071 |
| 23 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +657 | 176140 |
| 24 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +630 | 41549 |
| 25 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +595 | 12223 |
| 26 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +563 | 64293 |
| 27 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +556 | 22369 |
| 28 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +531 | 202036 |
| 29 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +525 | 45016 |
| 30 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +500 | 73778 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +62933 | 384275 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +18196 | 42884 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +15619 | 46730 |
| 4 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +12794 | 65684 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +11497 | 86644 |
| 6 | [stablyai/orca](https://github.com/stablyai/orca) | +9204 | 105731 |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +9149 | 176140 |
| 8 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +8288 | 261330 |
| 9 | [mattpocock/skills](https://github.com/mattpocock/skills) | +7070 | 303189 |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +6788 | 135162 |
| 11 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +5563 | 288796 |
| 12 | [yetone/magpie](https://github.com/yetone/magpie) | +5530 | 21422 |
| 13 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5432 | 72110 |
| 14 | [storytold/photocraft](https://github.com/storytold/photocraft) | +5413 | 72806 |
| 15 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5303 | 32729 |
| 16 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +5116 | 48225 |
| 17 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5003 | 221489 |
| 18 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +4887 | 87589 |
| 19 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4850 | 34393 |
| 20 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +4623 | 20569 |
| 21 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4614 | 68071 |
| 22 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4505 | 41549 |
| 23 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +4354 | 142915 |
| 24 | [storytold/artcraft](https://github.com/storytold/artcraft) | +3922 | 36577 |
| 25 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3763 | 89149 |
| 26 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3676 | 524633 |
| 27 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +3624 | 102448 |
| 28 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +3448 | 94291 |
| 29 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3418 | 102454 |
| 30 | [obra/superpowers](https://github.com/obra/superpowers) | +3396 | 305018 |
| 31 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +3393 | 61036 |
| 32 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +3295 | 33615 |
| 33 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +3237 | 19851 |
| 34 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3207 | 68970 |
| 35 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3183 | 107275 |
| 36 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3149 | 140359 |
| 37 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3069 | 45016 |
| 38 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +3009 | 81124 |
| 39 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +2977 | 27849 |
| 40 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2858 | 202036 |
| 41 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2855 | 223802 |
| 42 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2823 | 163987 |
| 43 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2800 | 79264 |
| 44 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +2796 | 32958 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2762 | 73778 |
| 46 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2744 | 148576 |
| 47 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +2635 | 43747 |
| 48 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +2612 | 114514 |
| 49 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2557 | 57103 |
| 50 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2554 | 195308 |
| 51 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2493 | 53706 |
| 52 | [blader/humanizer](https://github.com/blader/humanizer) | +2483 | 60562 |
| 53 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2416 | 67415 |
| 54 | [google/artemis](https://github.com/google/artemis) | +2383 | 14779 |
| 55 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2377 | 330404 |
| 56 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2360 | 71872 |
| 57 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2339 | 135101 |
| 58 | [usestrix/strix](https://github.com/usestrix/strix) | +2327 | 71873 |
| 59 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2309 | 110487 |
| 60 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2287 | 15804 |
| 61 | [jbiaojerry/ebook-treasure-chest](https://github.com/jbiaojerry/ebook-treasure-chest) | +2267 | 23057 |
| 62 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2257 | 49618 |
| 63 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +2222 | 21816 |
| 64 | [supabase/supabase](https://github.com/supabase/supabase) | +2190 | 113927 |
| 65 | [thesysdev/openui](https://github.com/thesysdev/openui) | +2129 | 13936 |
| 66 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2114 | 257044 |
| 67 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2106 | 25612 |
| 68 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2101 | 60031 |
| 69 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2057 | 492126 |
| 70 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +2026 | 253203 |
| 71 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +1978 | 17827 |
| 72 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1933 | 54576 |
| 73 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +1920 | 44545 |
| 74 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1916 | 77809 |
| 75 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1913 | 63427 |
| 76 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1881 | 18592 |
| 77 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1879 | 556204 |
| 78 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1832 | 19457 |
| 79 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1830 | 29925 |
| 80 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1791 | 330258 |
| 81 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1779 | 77265 |
| 82 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1769 | 30106 |
| 83 | [anthropics/skills](https://github.com/anthropics/skills) | +1768 | 183749 |
| 84 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1754 | 103940 |
| 85 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1720 | 16900 |
| 86 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1685 | 23117 |
| 87 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +1678 | 16040 |
| 88 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1637 | 117772 |
| 89 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1615 | 33090 |
| 90 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +1582 | 39564 |
| 91 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1573 | 115033 |
| 92 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +1572 | 20762 |
| 93 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1571 | 81890 |
| 94 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1556 | 153815 |
| 95 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1530 | 184433 |
| 96 | [tw93/Mole](https://github.com/tw93/Mole) | +1501 | 72860 |
| 97 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +1500 | 32235 |
| 98 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1488 | 103098 |
| 99 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1482 | 50573 |
| 100 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +1451 | 16269 |
| 101 | [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) | +1447 | 68567 |
| 102 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1411 | 123487 |
| 103 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | +1407 | 95481 |
| 104 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1407 | 58021 |
| 105 | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | +1369 | 20684 |
| 106 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1359 | 88246 |
| 107 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1327 | 40665 |
| 108 | [cursor/plugins](https://github.com/cursor/plugins) | +1325 | 14033 |
| 109 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1309 | 32412 |
| 110 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +1300 | 43424 |
| 111 | [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | +1282 | 60824 |
| 112 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +1273 | 19378 |
| 113 | [apify/apify-mcp-server](https://github.com/apify/apify-mcp-server) | +1268 | 13148 |
| 114 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1253 | 192161 |
| 115 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1241 | 190345 |
| 116 | [twentyhq/twenty](https://github.com/twentyhq/twenty) | +1237 | 59738 |
| 117 | [php/php-src](https://github.com/php/php-src) | +1216 | 41661 |
| 118 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1215 | 89695 |
| 119 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1205 | 45844 |
| 120 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1205 | 13592 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +72806 | 72806 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +34802 | 34802 |
| 3 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +22369 | 22369 |
| 4 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +20569 | 20569 |
| 5 | [google-research/harness2](https://github.com/google-research/harness2) | +19580 | 19580 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +17827 | 17827 |
| 7 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +16269 | 16269 |
| 8 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16040 | 16040 |
| 9 | [openai/math](https://github.com/openai/math) | +15508 | 15508 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14644 | 14644 |
| 11 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +12223 | 12223 |
