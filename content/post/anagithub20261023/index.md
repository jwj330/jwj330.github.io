---
title: "2026-10-23 GitHub增长趋势报告"
description: "1.rea+7048 2.cleanyourtv+3946 3.security-audit-skill+2600 4.dsh-our-free-model+2367 5.VoiceStudio+1529"
date: 2026-10-24T07:01:12+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-24 07:01:12

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
        'daily': {"categories": ["tashfeenahmed/freellmapi", "tt-a1i/archify", "yetone/magpie", "hugohe3/ppt-master", "heygen-com/hyperframes", "affaan-m/ECC", "luongnv89/claude-howto", "mattpocock/skills", "Graphify-Labs/graphify", "NVIDIA/OpenShell", "xerj-org/xerj", "stablyai/orca", "deepseek-ai/DeepInfer", "deepseek-ai/deepseek-harness", "DietrichGebert/ponytail", "debpalash/VoiceStudio", "Ebony-Vinyl/dsh-our-free-model", "cloudflare/security-audit-skill", "Gathin23/cleanyourtv", "morluto/rea"], "data": [668, 690, 694, 759, 784, 796, 846, 934, 996, 1065, 1084, 1091, 1244, 1268, 1384, 1529, 2367, 2600, 3946, 7048]},
        'weekly': {"categories": ["deepseek-ai/DeepInfer", "Gathin23/cleanyourtv"], "data": [21069, 27789]},
        'monthly': {"categories": ["shihabal3amri/DiPlay", "Droid-Deck/DroidDeck", "storytold/lightcraft", "openai/math", "storytold/wordcraft", "storytold/filmcraft", "storytold/pdfcraft", "google-research/harness2", "wheresryan22/anatomy", "yetone/magpie", "deepseek-ai/DeepInfer", "Gathin23/cleanyourtv", "Niko1221/Strata", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft"], "data": [12166, 13272, 14452, 15433, 15743, 15907, 17428, 18542, 19666, 20191, 21069, 27789, 31136, 39072, 71928]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +7048 | 372940 |
| 2 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +3946 | 27789 |
| 3 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | +2600 | 42039 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2367 | 39072 |
| 5 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +1529 | 83236 |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +1384 | 174764 |
| 7 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +1268 | 259406 |
| 8 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +1244 | 21069 |
| 9 | [stablyai/orca](https://github.com/stablyai/orca) | +1091 | 103795 |
| 10 | [xerj-org/xerj](https://github.com/xerj-org/xerj) | +1084 | 14191 |
| 11 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | +1065 | 18746 |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | +996 | 133883 |
| 13 | [mattpocock/skills](https://github.com/mattpocock/skills) | +934 | 301784 |
| 14 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +846 | 43989 |
| 15 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +796 | 287287 |
| 16 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +784 | 70760 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +759 | 66738 |
| 18 | [yetone/magpie](https://github.com/yetone/magpie) | +694 | 20191 |
| 19 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +690 | 88276 |
| 20 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +668 | 40239 |
| 21 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | +627 | 32183 |
| 22 | [storytold/photocraft](https://github.com/storytold/photocraft) | +602 | 71928 |
| 23 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +579 | 13272 |
| 24 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +575 | 33724 |
| 25 | [google-research/harness2](https://github.com/google-research/harness2) | +574 | 18542 |
| 26 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +563 | 31327 |
| 27 | [latent-spaces/brag](https://github.com/latent-spaces/brag) | +558 | 18084 |
| 28 | [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | +551 | 64083 |
| 29 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +550 | 31136 |
| 30 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +546 | 85507 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +27789 | 27789 |
| 2 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +21069 | 21069 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +71928 | 71928 |
| 2 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +39072 | 39072 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +31136 | 31136 |
| 4 | [Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) | +27789 | 27789 |
| 5 | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | +21069 | 21069 |
| 6 | [yetone/magpie](https://github.com/yetone/magpie) | +20191 | 20191 |
| 7 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +19666 | 19666 |
| 8 | [google-research/harness2](https://github.com/google-research/harness2) | +18542 | 18542 |
| 9 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +17428 | 17428 |
| 10 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +15907 | 15907 |
| 11 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +15743 | 15743 |
| 12 | [openai/math](https://github.com/openai/math) | +15433 | 15433 |
| 13 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +14452 | 14452 |
| 14 | [Droid-Deck/DroidDeck](https://github.com/Droid-Deck/DroidDeck) | +13272 | 13272 |
| 15 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +12166 | 12166 |
