---
title: "2026-10-20 GitHub增长趋势报告"
description: "1.rea+11232 2.harness2+3566 3.ai-job-search+3319 4.dsh-our-free-model+3158 5.security-audit-skill+1552"
date: 2026-10-21T07:03:26+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-21 07:03:26

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
        'daily': {"categories": ["affaan-m/ECC", "storytold/artcraft", "heygen-com/hyperframes", "Niko1221/Strata", "yetone/magpie", "Graphify-Labs/graphify", "Comfy-Org/ComfyUI", "boykopovar/AnyPS5", "storytold/photocraft", "anomalyco/opencode", "mattpocock/skills", "deepseek-ai/deepseek-harness", "debpalash/VoiceStudio", "stablyai/orca", "DietrichGebert/ponytail", "cloudflare/security-audit-skill", "Ebony-Vinyl/dsh-our-free-model", "MadsLorentzen/ai-job-search", "google-research/harness2", "morluto/rea"], "data": [764, 800, 822, 908, 969, 1021, 1039, 1041, 1064, 1108, 1155, 1307, 1461, 1463, 1476, 1552, 3158, 3319, 3566, 11232]},
        'weekly': {"categories": ["Niko1221/Strata", "anthropics/claude-plugins-official", "anomalyco/opencode", "heygen-com/hyperframes", "NationalSecurityAgency/ghidra", "affaan-m/ECC", "yetone/magpie", "deepseek-ai/deepseek-harness", "DietrichGebert/ponytail", "stablyai/orca", "storytold/artcraft", "mattpocock/skills", "boykopovar/AnyPS5", "Gathin23/cleanyourtv", "storytold/photocraft", "deepseek-ai/DeepInfer", "MadsLorentzen/ai-job-search", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "morluto/rea"], "data": [5483, 5585, 5618, 5709, 5814, 6292, 6447, 6788, 6819, 8082, 8924, 8991, 10223, 11495, 11822, 11944, 13811, 15747, 16743, 141569]},
        'monthly': {"categories": ["Gathin23/cleanyourtv", "Droid-Deck/DroidDeck", "shihabal3amri/DiPlay", "deepseek-ai/DeepInfer", "storytold/lightcraft", "storytold/wordcraft", "google-research/harness2", "openai/math", "storytold/filmcraft", "storytold/pdfcraft", "wheresryan22/anatomy", "yetone/magpie", "Niko1221/Strata", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft"], "data": [11495, 11786, 11813, 11944, 14038, 15052, 15216, 15302, 15309, 16637, 17548, 17941, 29172, 30811, 69595]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +11232 | 347523 |
| 2 | [google-research/harness2](https://github.com/google-research/harness2) | +3566 | 15216 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +3319 | 60414 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +3158 | 30811 |
| 5 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1552 | 34042 |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1476 | 169554 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +1463 | 99673 |
| 8 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1461 | 78906 |
| 9 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1307 | 255738 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1155 | 298607 |
| 11 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1108 | 218863 |
| 12 | [storytold/photocraft](https://github.com/storytold/photocraft) | +1064 | 69595 |
| 13 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +1041 | 45482 |
| 14 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1039 | 140713 |
| 15 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +1021 | 130165 |
| 16 | [yetone/magpie](https://github.com/yetone/magpie) | +969 | 17941 |
| 17 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +908 | 29172 |
| 18 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +822 | 68455 |
| 19 | [storytold/artcraft](https://github.com/storytold/artcraft) | +800 | 34488 |
| 20 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +764 | 284873 |
| 21 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +723 | 17548 |
| 22 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +702 | 42325 |
| 23 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +691 | 67057 |
| 24 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +660 | 38297 |
| 25 | [supabase/supabase](https://github.com/supabase/supabase) | +655 | 112432 |
| 26 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +645 | 77805 |
| 27 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +603 | 11898 |
| 28 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +600 | 83806 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +599 | 64466 |
| 30 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +598 | 100271 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +141569 | 347523 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +16743 | 30811 |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +15747 | 78906 |
| 4 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +13811 | 60414 |
| 5 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +11944 | 11944 |
| 6 | [storytold/photocraft](https://github.com/storytold/photocraft) | +11822 | 69595 |
| 7 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +11495 | 11495 |
| 8 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +10223 | 45482 |
| 9 | [mattpocock/skills](https://github.com/mattpocock/skills) | +8991 | 298607 |
| 10 | [storytold/artcraft](https://github.com/storytold/artcraft) | +8924 | 34488 |
| 11 | [stablyai/orca](https://github.com/stablyai/orca) | +8082 | 99673 |
| 12 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +6819 | 169554 |
| 13 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +6788 | 255738 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +6447 | 17941 |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6292 | 284873 |
| 16 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +5814 | 92113 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5709 | 68455 |
| 18 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +5618 | 218863 |
| 19 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +5585 | 43394 |
| 20 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5483 | 29172 |
| 21 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +5039 | 67057 |
| 22 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +4915 | 58963 |
| 23 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +4804 | 26500 |
| 24 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +4754 | 34042 |
| 25 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +4585 | 30643 |
| 26 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4532 | 53257 |
| 27 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +4453 | 20324 |
| 28 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +4250 | 99839 |
| 29 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +4006 | 15052 |
| 30 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +3973 | 130165 |
| 31 | [obra/superpowers](https://github.com/obra/superpowers) | +3923 | 302579 |
| 32 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +3917 | 16637 |
| 33 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3681 | 105228 |
| 34 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +3609 | 38297 |
| 35 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +3545 | 55654 |
| 36 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3381 | 86405 |
| 37 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +3378 | 140713 |
| 38 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +3349 | 31544 |
| 39 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3286 | 100271 |
| 40 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3270 | 521920 |
| 41 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +3246 | 77805 |
| 42 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +3196 | 58517 |
| 43 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +3144 | 31344 |
| 44 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3128 | 71780 |
| 45 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +3111 | 14155 |
| 46 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +3040 | 83806 |
| 47 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3018 | 146793 |
| 48 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2892 | 133423 |
| 49 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +2816 | 64466 |
| 50 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +2795 | 15309 |
| 51 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2789 | 78957 |
| 52 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2784 | 108972 |
| 53 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2768 | 52018 |
| 54 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2494 | 328695 |
| 55 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2477 | 137985 |
| 56 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2434 | 490854 |
| 57 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2415 | 162296 |
| 58 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2373 | 113850 |
| 59 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2341 | 24286 |
| 60 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2322 | 70284 |
| 61 | [blader/humanizer](https://github.com/blader/humanizer) | +2305 | 58886 |
| 62 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +2291 | 38540 |
| 63 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2257 | 193464 |
| 64 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2237 | 199712 |
| 65 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2094 | 255571 |
| 66 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +2064 | 48039 |
| 67 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +2059 | 251905 |
| 68 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +2046 | 14038 |
| 69 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2036 | 221522 |
| 70 | [cursor/plugins](https://github.com/cursor/plugins) | +2024 | 13243 |
| 71 | [usestrix/strix](https://github.com/usestrix/strix) | +2016 | 70419 |
| 72 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +2013 | 21976 |
| 73 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +1995 | 152645 |
| 74 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1964 | 62165 |
| 75 | [lexmount/moli](https://github.com/lexmount/moli) | +1932 | 19871 |
| 76 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1904 | 80862 |
| 77 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1855 | 15531 |
| 78 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1847 | 102802 |
| 79 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1832 | 329012 |
| 80 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1805 | 116700 |
| 81 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1784 | 554836 |
| 82 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1740 | 65607 |
| 83 | [google/artemis](https://github.com/google/artemis) | +1717 | 13255 |
| 84 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1644 | 42325 |
| 85 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1636 | 49658 |
| 86 | [tw93/Mole](https://github.com/tw93/Mole) | +1628 | 71838 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1626 | 152741 |
| 88 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +1579 | 39877 |
| 89 | [anthropics/skills](https://github.com/anthropics/skills) | +1561 | 182486 |
| 90 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1545 | 28519 |
| 91 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1540 | 88871 |
| 92 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1540 | 57078 |
| 93 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +1539 | 55659 |
| 94 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1537 | 122514 |
| 95 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1524 | 101952 |
| 96 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1512 | 75855 |
| 97 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +1484 | 15419 |
| 98 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | +1476 | 76726 |
| 99 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1454 | 28857 |
| 100 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1430 | 17170 |
| 101 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1428 | 183317 |
| 102 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +1367 | 95486 |
| 103 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1367 | 53174 |
| 104 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1363 | 35833 |
| 105 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1307 | 191305 |
| 106 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1307 | 43056 |
| 107 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1299 | 31987 |
| 108 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1294 | 112334 |
| 109 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1235 | 30773 |
| 110 | [longbridge/gpui-kit](https://github.com/longbridge/gpui-kit) | +1234 | 18418 |
| 111 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +1228 | 12859 |
| 112 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1207 | 21031 |
| 113 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1192 | 189445 |
| 114 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1186 | 45005 |
| 115 | [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | +1165 | 18664 |
| 116 | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | +1128 | 31786 |
| 117 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +1124 | 55134 |
| 118 | [openai/codex](https://github.com/openai/codex) | +1121 | 130166 |
| 119 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1119 | 55684 |
| 120 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +1112 | 42792 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +69595 | 69595 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +30811 | 30811 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +29172 | 29172 |
| 4 | [yetone/magpie](https://github.com/yetone/magpie) | +17941 | 17941 |
| 5 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +17548 | 17548 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +16637 | 16637 |
| 7 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +15309 | 15309 |
| 8 | [openai/math](https://github.com/openai/math) | +15302 | 15302 |
| 9 | [google-research/harness2](https://github.com/google-research/harness2) | +15216 | 15216 |
| 10 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +15052 | 15052 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14038 | 14038 |
| 12 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +11944 | 11944 |
| 13 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +11813 | 11813 |
| 14 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +11786 | 11786 |
| 15 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +11495 | 11495 |
