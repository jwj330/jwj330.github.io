---
title: "2026-10-19 GitHub增长趋势报告"
description: "1.rea+14949 2.ai-job-search+4205 3.dsh-our-free-model+2965 4.VoiceStudio+2298 5.orca+1683"
date: 2026-10-20T07:28:24+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-20 07:28:24

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
        'daily': {"categories": ["Niko1221/Strata", "affaan-m/ECC", "wheresryan22/anatomy", "heygen-com/hyperframes", "storytold/artcraft", "yetone/magpie", "DietrichGebert/ponytail", "Comfy-Org/ComfyUI", "storytold/photocraft", "hmjz100/LinkSwift", "anomalyco/opencode", "boykopovar/AnyPS5", "mattpocock/skills", "cloudflare/security-audit-skill", "deepseek-ai/deepseek-harness", "stablyai/orca", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "MadsLorentzen/ai-job-search", "morluto/rea"], "data": [838, 876, 879, 955, 1033, 1080, 1087, 1113, 1138, 1166, 1269, 1332, 1333, 1379, 1389, 1683, 2298, 2965, 4205, 14949]},
        'weekly': {"categories": [], "data": []},
        'monthly': {"categories": ["Droid-Deck/DroidDeck", "google-research/harness2", "shihabal3amri/DiPlay", "storytold/lightcraft", "storytold/wordcraft", "storytold/filmcraft", "openai/math", "storytold/pdfcraft", "wheresryan22/anatomy", "yetone/magpie", "Ebony-Vinyl/dsh-our-free-model", "Niko1221/Strata", "storytold/photocraft"], "data": [11365, 11650, 11665, 13897, 14743, 15100, 15226, 16285, 16825, 16972, 27653, 28264, 68531]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +14949 | 336291 |
| 2 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +4205 | 57095 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2965 | 27653 |
| 4 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2298 | 77445 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +1683 | 98210 |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1389 | 254431 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +1379 | 32490 |
| 8 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1333 | 297452 |
| 9 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +1332 | 44441 |
| 10 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +1269 | 217755 |
| 11 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +1166 | 26038 |
| 12 | [storytold/photocraft](https://github.com/storytold/photocraft) | +1138 | 68531 |
| 13 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +1113 | 139674 |
| 14 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1087 | 168078 |
| 15 | [yetone/magpie](https://github.com/yetone/magpie) | +1080 | 16972 |
| 16 | [storytold/artcraft](https://github.com/storytold/artcraft) | +1033 | 33688 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +955 | 67633 |
| 18 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +879 | 16825 |
| 19 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +876 | 284109 |
| 20 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +838 | 28264 |
| 21 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +770 | 129144 |
| 22 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +733 | 58376 |
| 23 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +704 | 91547 |
| 24 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +696 | 77160 |
| 25 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +657 | 55203 |
| 26 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +637 | 99673 |
| 27 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +621 | 104713 |
| 28 | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | +606 | 55563 |
| 29 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +603 | 66366 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +593 | 37637 |


### 📅 本周 Top 120 详情

_周增长数据积累中，7 天后自动展示。_


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +68531 | 68531 |
| 2 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +28264 | 28264 |
| 3 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +27653 | 27653 |
| 4 | [yetone/magpie](https://github.com/yetone/magpie) | +16972 | 16972 |
| 5 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +16825 | 16825 |
| 6 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +16285 | 16285 |
| 7 | [openai/math](https://github.com/openai/math) | +15226 | 15226 |
| 8 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +15100 | 15100 |
| 9 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +14743 | 14743 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +13897 | 13897 |
| 11 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +11665 | 11665 |
| 12 | [google-research/harness2](https://github.com/google-research/harness2) | +11650 | 11650 |
| 13 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +11365 | 11365 |
