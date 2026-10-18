---
title: "2026-10-18 GitHub增长趋势报告"
description: "1.rea+14727 2.dsh-our-free-model+2976 3.ai-job-search+2658 4.VoiceStudio+2000 5.AnyPS5+1530"
date: 2026-10-19T06:21:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-19 06:21:00

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
        'daily': {"categories": ["NationalSecurityAgency/ghidra", "cathrynlavery/diagram-design", "bannedbook/fanqiang", "heygen-com/hyperframes", "DietrichGebert/ponytail", "affaan-m/ECC", "yetone/magpie", "wheresryan22/anatomy", "deepseek-ai/deepseek-harness", "storytold/artcraft", "anthropics/claude-plugins-official", "storytold/photocraft", "mattpocock/skills", "stablyai/orca", "anomalyco/opencode", "boykopovar/AnyPS5", "debpalash/VoiceStudio", "MadsLorentzen/ai-job-search", "Ebony-Vinyl/dsh-our-free-model", "morluto/rea"], "data": [633, 686, 703, 746, 826, 833, 877, 899, 943, 954, 978, 1088, 1096, 1215, 1318, 1530, 2000, 2658, 2976, 14727]},
        'weekly': {"categories": ["LibreSpark/LibreTV", "deepseek-ai/deepseek-harness", "vxcontrol/pentagi", "ifixai-ai/iFixAi", "heygen-com/hyperframes", "Niko1221/Strata", "DietrichGebert/ponytail", "eternity4719/HowToLiveBetter", "affaan-m/ECC", "bilawalsidhu/gods-eye-view", "MadsLorentzen/ai-job-search", "stablyai/orca", "cathrynlavery/diagram-design", "NationalSecurityAgency/ghidra", "mattpocock/skills", "boykopovar/AnyPS5", "storytold/artcraft", "debpalash/VoiceStudio", "storytold/photocraft", "morluto/rea"], "data": [5477, 5558, 5647, 5711, 5732, 5862, 5894, 5919, 6037, 6329, 6781, 6792, 7371, 7406, 9962, 13127, 14895, 16479, 19960, 218660]},
        'monthly': {"categories": ["shihabal3amri/DiPlay", "cdyforever/how-to-live-better", "storytold/lightcraft", "storytold/wordcraft", "storytold/filmcraft", "openai/math", "storytold/pdfcraft", "yetone/magpie", "wheresryan22/anatomy", "Ebony-Vinyl/dsh-our-free-model", "Niko1221/Strata", "NandhaKishorM/laya", "storytold/photocraft"], "data": [11472, 12532, 13674, 14362, 14818, 15167, 15849, 15892, 15946, 24688, 27426, 33383, 67393]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +14727 | 321342 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2976 | 24688 |
| 3 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +2658 | 52890 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2000 | 75147 |
| 5 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +1530 | 43109 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1318 | 216486 |
| 7 | [stablyai/orca](https://github.com/stablyai/orca) | +1215 | 96527 |
| 8 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1096 | 296119 |
| 9 | [storytold/photocraft](https://github.com/storytold/photocraft) | +1088 | 67393 |
| 10 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +978 | 42625 |
| 11 | [storytold/artcraft](https://github.com/storytold/artcraft) | +954 | 32655 |
| 12 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +943 | 253042 |
| 13 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +899 | 15946 |
| 14 | [yetone/magpie](https://github.com/yetone/magpie) | +877 | 15892 |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +833 | 283233 |
| 16 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +826 | 166991 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +746 | 66678 |
| 18 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +703 | 54957 |
| 19 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +686 | 57643 |
| 20 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +633 | 90843 |
| 21 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +625 | 128374 |
| 22 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +593 | 65763 |
| 23 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +589 | 152248 |
| 24 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +569 | 27426 |
| 25 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +550 | 85386 |
| 26 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +543 | 54546 |
| 27 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +512 | 24872 |
| 28 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +511 | 520957 |
| 29 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +500 | 138561 |
| 30 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +486 | 104092 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [morluto/rea](https://github.com/morluto/rea) | +218660 | 321342 |
| 2 | [storytold/photocraft](https://github.com/storytold/photocraft) | +19960 | 67393 |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +16479 | 75147 |
| 4 | [storytold/artcraft](https://github.com/storytold/artcraft) | +14895 | 32655 |
| 5 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +13127 | 43109 |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills) | +9962 | 296119 |
| 7 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +7406 | 90843 |
| 8 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +7371 | 57643 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +6792 | 96527 |
| 10 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +6781 | 52890 |
| 11 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +6329 | 57930 |
| 12 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +6037 | 283233 |
| 13 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +5919 | 65763 |
| 14 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +5894 | 166991 |
| 15 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +5862 | 27426 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +5732 | 66678 |
| 17 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +5711 | 29543 |
| 18 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +5647 | 31103 |
| 19 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +5558 | 253042 |
| 20 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +5477 | 19594 |
| 21 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +4929 | 42625 |
| 22 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +4241 | 52643 |
| 23 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +4087 | 98824 |
| 24 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +4064 | 30735 |
| 25 | [obra/superpowers](https://github.com/obra/superpowers) | +3925 | 301622 |
| 26 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3753 | 216486 |
| 27 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3745 | 104092 |
| 28 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +3728 | 37044 |
| 29 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +3535 | 71016 |
| 30 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3457 | 61514 |
| 31 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +3399 | 24872 |
| 32 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +3346 | 85386 |
| 33 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +3276 | 520957 |
| 34 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +3170 | 108178 |
| 35 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +3111 | 63457 |
| 36 | [lexmount/moli](https://github.com/lexmount/moli) | +3085 | 19467 |
| 37 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3040 | 145832 |
| 38 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +3034 | 99036 |
| 39 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +3023 | 132762 |
| 40 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | +2893 | 39338 |
| 41 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +2836 | 82702 |
| 42 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +2826 | 128374 |
| 43 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +2802 | 51213 |
| 44 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2797 | 31111 |
| 45 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +2796 | 78115 |
| 46 | [Predidit/Kazumi](https://github.com/Predidit/Kazumi) | +2704 | 37982 |
| 47 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +2634 | 54546 |
| 48 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +2563 | 69512 |
| 49 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +2476 | 490069 |
| 50 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +2409 | 113460 |
| 51 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +2392 | 328027 |
| 52 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2390 | 137210 |
| 53 | [hypit-ai/hypit](https://github.com/hypit-ai/hypit) | +2317 | 23506 |
| 54 | [blader/humanizer](https://github.com/blader/humanizer) | +2288 | 58079 |
| 55 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +2244 | 199178 |
| 56 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2232 | 192754 |
| 57 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +2187 | 21432 |
| 58 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2162 | 80319 |
| 59 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2132 | 254930 |
| 60 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +2103 | 76464 |
| 61 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | +2077 | 220947 |
| 62 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +2063 | 161164 |
| 63 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +2021 | 152248 |
| 64 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +1980 | 47361 |
| 65 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | +1935 | 15180 |
| 66 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +1889 | 101610 |
| 67 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +1870 | 251177 |
| 68 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | +1861 | 28095 |
| 69 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +1822 | 328467 |
| 70 | [earendil-works/pi](https://github.com/earendil-works/pi) | +1820 | 116135 |
| 71 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1766 | 122076 |
| 72 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +1761 | 554325 |
| 73 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +1751 | 156073 |
| 74 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +1727 | 49091 |
| 75 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +1716 | 64999 |
| 76 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +1681 | 35492 |
| 77 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1662 | 152259 |
| 78 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +1640 | 29567 |
| 79 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +1637 | 88480 |
| 80 | [nexu-io/open-design](https://github.com/nexu-io/open-design) | +1623 | 102186 |
| 81 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +1619 | 95232 |
| 82 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1616 | 138561 |
| 83 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +1595 | 42554 |
| 84 | [usestrix/strix](https://github.com/usestrix/strix) | +1592 | 69546 |
| 85 | [corsairdev/corsair](https://github.com/corsairdev/corsair) | +1581 | 15308 |
| 86 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +1526 | 182903 |
| 87 | [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | +1502 | 17383 |
| 88 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +1488 | 42734 |
| 89 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +1478 | 16711 |
| 90 | [anthropics/skills](https://github.com/anthropics/skills) | +1477 | 181981 |
| 91 | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | +1419 | 75486 |
| 92 | [tw93/Mole](https://github.com/tw93/Mole) | +1417 | 71359 |
| 93 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +1416 | 52760 |
| 94 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +1414 | 47585 |
| 95 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +1398 | 12532 |
| 96 | [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | +1396 | 34607 |
| 97 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +1344 | 28337 |
| 98 | [chen08209/FlClash](https://github.com/chen08209/FlClash) | +1337 | 56614 |
| 99 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | +1334 | 190908 |
| 100 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1300 | 98646 |
| 101 | [t8y2/dbx](https://github.com/t8y2/dbx) | +1299 | 27110 |
| 102 | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) | +1276 | 54791 |
| 103 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +1251 | 204803 |
| 104 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1247 | 111902 |
| 105 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +1234 | 44639 |
| 106 | [chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11) | +1208 | 75433 |
| 107 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | +1202 | 189104 |
| 108 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +1202 | 57679 |
| 109 | [longbridge/gpui-kit](https://github.com/longbridge/gpui-kit) | +1199 | 18112 |
| 110 | [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) | +1174 | 19402 |
| 111 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1169 | 55370 |
| 112 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | +1129 | 35758 |
| 113 | [openai/math](https://github.com/openai/math) | +1106 | 15167 |
| 114 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +1089 | 12387 |
| 115 | [openai/codex](https://github.com/openai/codex) | +1084 | 129755 |
| 116 | [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | +1071 | 31555 |
| 117 | [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus) | +1058 | 93911 |
| 118 | [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) | +1058 | 20764 |
| 119 | [google/artemis](https://github.com/google/artemis) | +1052 | 12396 |
| 120 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +1050 | 30162 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +67393 | 67393 |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | +33383 | 33383 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +27426 | 27426 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +24688 | 24688 |
| 5 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +15946 | 15946 |
| 6 | [yetone/magpie](https://github.com/yetone/magpie) | +15892 | 15892 |
| 7 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +15849 | 15849 |
| 8 | [openai/math](https://github.com/openai/math) | +15167 | 15167 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +14818 | 14818 |
| 10 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +14362 | 14362 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +13674 | 13674 |
| 12 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +12532 | 12532 |
| 13 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +11472 | 11472 |
