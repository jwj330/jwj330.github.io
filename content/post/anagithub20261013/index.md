---
title: "2026-10-13 GitHub增长趋势报告"
description: "增长数据积累中"
date: 2026-10-14T07:42:30+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-14 07:42:30

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
        'daily': {"categories": [], "data": []},
        'weekly': {"categories": ["storytold/wordcraft", "openai/math"], "data": [11046, 14671]},
        'monthly': {"categories": ["storytold/wordcraft", "yetone/magpie", "cdyforever/how-to-live-better", "storytold/lightcraft", "storytold/filmcraft", "storytold/pdfcraft", "Ebony-Vinyl/dsh-our-free-model", "openai/math", "robbietilton/Compositor", "browser-use/jev-ultrafast", "Niko1221/Strata", "NandhaKishorM/laya", "storytold/photocraft"], "data": [11046, 11494, 11631, 11992, 12514, 12720, 14068, 14671, 16707, 22825, 23689, 32769, 57773]}
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

_日增长数据积累中，明日开始自动展示。_


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openai/math](https://github.com/openai/math) | +14671 | 14671 |
| 2 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +11046 | 11046 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +57773 | 57773 |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | +32769 | 32769 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +23689 | 23689 |
| 4 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | +22825 | 22825 |
| 5 | [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | +16707 | 16707 |
| 6 | [openai/math](https://github.com/openai/math) | +14671 | 14671 |
| 7 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +14068 | 14068 |
| 8 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +12720 | 12720 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +12514 | 12514 |
| 10 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +11992 | 11992 |
| 11 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +11631 | 11631 |
| 12 | [yetone/magpie](https://github.com/yetone/magpie) | +11494 | 11494 |
| 13 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +11046 | 11046 |
