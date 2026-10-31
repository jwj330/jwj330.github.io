---
title: "2026-10-31 GitHub增长趋势报告"
description: "1.rea+3198 2.t3code+2693 3.iFixAi+2279 4.claude-mem+1613 5.dsh-our-free-model+1542"
date: 2026-11-01T07:12:39+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-11-01 07:12:39

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
        'daily': {"categories": ["yetone/magpie", "Leonxlnx/taste-skill", "YuJunZhiXue/dsh-purge", "deepseek-ai/deepseek-harness", "Donchitos/Claude-Code-Game-Studios", "KnifeLemon/Filee", "lightpanda-io/browser", "mattpocock/skills", "Nutlope/hallmark", "HKUDS/DeepTutor", "Renhuai123/ziwei-doushu", "debpalash/VoiceStudio", "Gathin23/cleanyourtv", "cloudflare/security-audit-skill", "pbakaus/impeccable", "Ebony-Vinyl/dsh-our-free-model", "thedotmack/claude-mem", "ifixai-ai/iFixAi", "pingdotgg/t3code", "morluto/rea"], "data": [681, 698, 705, 706, 711, 824, 873, 884, 937, 1022, 1061, 1101, 1185, 1192, 1212, 1542, 1613, 2279, 2693, 3198]},
        'weekly': {"categories": ["Panniantong/Agent-Reach", "pingdotgg/t3code", "Graphify-Labs/graphify", "mattpocock/skills", "affaan-m/ECC", "DietrichGebert/ponytail", "yetone/magpie", "stablyai/orca", "deepseek-ai/deepseek-harness", "ifixai-ai/iFixAi", "KnifeLemon/Filee", "hmjz100/LinkSwift", "HKUDS/DeepTutor", "cloudflare/security-audit-skill", "Nutlope/hallmark", "pbakaus/impeccable", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "Gathin23/cleanyourtv", "morluto/rea"], "data": [5492, 5560, 5612, 5846, 5992, 6017, 6166, 6799, 6982, 7390, 7641, 9328, 10232, 10910, 11833, 11888, 11942, 13111, 16322, 37056]},
        'monthly': {"categories": ["tangency-labs/solidcraft", "Zagitta/gpu-unlock", "storytold/wordcraft", "openai/math", "google-research/harness2", "wheresryan22/anatomy", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv"], "data": [12629, 13833, 16859, 17197, 21665, 23336, 24651, 47880]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +3198 | 415402 |
| 2 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +2693 | 35401 |
| 3 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +2279 | 41411 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1613 | 107790 |
| 5 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1542 | 54314 |
| 6 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1212 | 98213 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1192 | 55270 |
| 8 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +1185 | 47880 |
| 9 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1101 | 96801 |
| 10 | [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) | +1061 | 12242 |
| 11 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +1022 | 52758 |
| 12 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +937 | 43885 |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | +884 | 308326 |
| 14 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +873 | 39198 |
| 15 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +824 | 19269 |
| 16 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +711 | 31123 |
| 17 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +706 | 267424 |
| 18 | [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | +705 | 14557 |
| 19 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +698 | 107004 |
| 20 | [yetone/magpie](https://github.com/yetone/magpie) | +681 | 26925 |
| 21 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +643 | 294031 |
| 22 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +628 | 227468 |
| 23 | [obra/superpowers](https://github.com/obra/superpowers) | +626 | 310029 |
| 24 | [stablyai/orca](https://github.com/stablyai/orca) | +611 | 111700 |
| 25 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +606 | 31868 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +583 | 185859 |
| 27 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +577 | 37063 |
| 28 | [openai/codex](https://github.com/openai/codex) | +569 | 132486 |
| 29 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +556 | 140010 |
| 30 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +553 | 181500 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +37056 | 415402 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +16322 | 47880 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +13111 | 54314 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +11942 | 96801 |
| 5 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +11888 | 98213 |
| 6 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +11833 | 43885 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +10910 | 55270 |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +10232 | 52758 |
| 9 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +9328 | 36930 |
| 10 | [KnifeLemon/Filee](https://github.com/KnifeLemon/Filee) | +7641 | 19269 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +7390 | 41411 |
| 12 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +6982 | 267424 |
| 13 | [stablyai/orca](https://github.com/stablyai/orca) | +6799 | 111700 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +6166 | 26925 |
| 15 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +6017 | 181500 |
| 16 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +5992 | 294031 |
| 17 | [mattpocock/skills](https://github.com/mattpocock/skills) | +5846 | 308326 |
| 18 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +5612 | 140010 |
| 19 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +5560 | 35401 |
| 20 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +5492 | 107212 |
| 21 | [obra/superpowers](https://github.com/obra/superpowers) | +5415 | 310029 |
| 22 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +5380 | 119036 |
| 23 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5116 | 37063 |
| 24 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5104 | 76548 |
| 25 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +5007 | 107004 |
| 26 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4992 | 107790 |
| 27 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +4936 | 25019 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +4265 | 45184 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +4238 | 71647 |
| 30 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +4107 | 227468 |
| 31 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3881 | 528018 |
| 32 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +3713 | 31123 |
| 33 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +3666 | 68437 |
| 34 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +3549 | 56977 |
| 35 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3505 | 143407 |
| 36 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3415 | 92135 |
| 37 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +3253 | 71887 |
| 38 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +3217 | 23336 |
| 39 | [storytold/photocraft](https://github.com/storytold/photocraft) | +3188 | 75559 |
| 40 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +3060 | 52423 |
| 41 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +2983 | 16847 |
| 42 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +2838 | 24651 |
| 43 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +2814 | 76092 |
| 44 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +2775 | 18281 |
| 45 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +2761 | 63473 |
| 46 | [blader/humanizer](https://github.com/blader/humanizer) | +2725 | 62975 |
| 47 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2712 | 204217 |
| 48 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +2649 | 17937 |
| 49 | [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | +2634 | 40359 |
| 50 | [google-research/harness2](https://github.com/google-research/harness2) | +2581 | 21665 |
| 51 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +2547 | 223610 |
| 52 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +2520 | 96479 |
| 53 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +2517 | 109448 |
| 54 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | +2490 | 83228 |
| 55 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +2438 | 101877 |
| 56 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2429 | 332429 |
| 57 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2408 | 197397 |
| 58 | [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems) | +2404 | 34123 |
| 59 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +2401 | 23693 |
| 60 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2384 | 259171 |
| 61 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2374 | 73946 |
| 62 | [anthropics/skills](https://github.com/anthropics/skills) | +2362 | 185859 |
| 63 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +2337 | 69440 |
| 64 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2312 | 150631 |
| 65 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2296 | 65430 |
| 66 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | +2277 | 14171 |
| 67 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +2269 | 50127 |
| 68 | [lightpanda-io/browser](https://github.com/lightpanda-io/browser) | +2256 | 39198 |
| 69 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +2225 | 60088 |
| 70 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | +2218 | 28309 |
| 71 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +2148 | 61814 |
| 72 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +2121 | 31868 |
| 73 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +2108 | 45323 |
| 74 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +2054 | 79064 |
| 75 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +2054 | 15473 |
| 76 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +2053 | 136907 |
| 77 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +2047 | 112241 |
| 78 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +1984 | 165686 |
| 79 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +1945 | 493815 |
| 80 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1914 | 557897 |
| 81 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1901 | 254838 |
| 82 | [jub0t/Concat](https://github.com/jub0t/Concat) | +1888 | 13197 |
| 83 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1788 | 185975 |
| 84 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +1785 | 20996 |
| 85 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +1783 | 46274 |
| 86 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +1776 | 30111 |
| 87 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1756 | 155363 |
| 88 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1738 | 144355 |
| 89 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +1735 | 27105 |
| 90 | [storytold/artcraft](https://github.com/storytold/artcraft) | +1717 | 38003 |
| 91 | [openai/math](https://github.com/openai/math) | +1717 | 17197 |
| 92 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1709 | 116518 |
| 93 | [openai/codex](https://github.com/openai/codex) | +1686 | 132486 |
| 94 | [coollabsio/coolify](https://github.com/coollabsio/coolify) | +1680 | 65410 |
| 95 | [github/spec-kit](https://github.com/github/spec-kit) | +1657 | 144390 |
| 96 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1656 | 45383 |
| 97 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1605 | 331603 |
| 98 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +1590 | 24517 |
| 99 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1587 | 34190 |
| 100 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1578 | 119183 |
| 101 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1525 | 124854 |
| 102 | [google/artemis](https://github.com/google/artemis) | +1522 | 15943 |
| 103 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | +1447 | 14709 |
| 104 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1438 | 47128 |
| 105 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1433 | 105186 |
| 106 | [usestrix/strix](https://github.com/usestrix/strix) | +1425 | 73091 |
| 107 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1418 | 23027 |
| 108 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1415 | 19780 |
| 109 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +1414 | 20844 |
| 110 | [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) | +1404 | 19110 |
| 111 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +1400 | 80421 |
| 112 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +1397 | 83097 |
| 113 | [lexmount/moli](https://github.com/lexmount/moli) | +1393 | 21879 |
| 114 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1386 | 90860 |
| 115 | [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | +1384 | 34281 |
| 116 | [localsend/localsend](https://github.com/localsend/localsend) | +1374 | 96828 |
| 117 | [cjpais/Handy](https://github.com/cjpais/Handy) | +1353 | 35896 |
| 118 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1352 | 22668 |
| 119 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +1348 | 50664 |
| 120 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | +1341 | 89408 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +47880 | 47880 |
| 2 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +24651 | 24651 |
| 3 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +23336 | 23336 |
| 4 | [google-research/harness2](https://github.com/google-research/harness2) | +21665 | 21665 |
| 5 | [openai/math](https://github.com/openai/math) | +17197 | 17197 |
| 6 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +16859 | 16859 |
| 7 | [Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) | +13833 | 13833 |
| 8 | [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | +12629 | 12629 |
