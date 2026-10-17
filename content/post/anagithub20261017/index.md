---
title: "2026-10-17 GitHub增长趋势报告"
description: "增长数据积累中"
date: 2026-10-18T06:07:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-18 06:07:19

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
        'weekly': {"categories": [], "data": []},
        'monthly': {"categories": ["shihabal3amri/DiPlay", "cdyforever/how-to-live-better", "storytold/lightcraft", "storytold/wordcraft", "storytold/filmcraft", "yetone/magpie", "wheresryan22/anatomy", "openai/math", "storytold/pdfcraft", "Ebony-Vinyl/dsh-our-free-model", "Niko1221/Strata", "NandhaKishorM/laya", "storytold/photocraft"], "data": [11296, 12387, 13459, 14031, 14547, 15015, 15047, 15101, 15461, 21712, 26857, 33264, 66305]}
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

_周增长数据积累中，7 天后自动展示。_


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +66305 | 66305 |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | +33264 | 33264 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +26857 | 26857 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +21712 | 21712 |
| 5 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +15461 | 15461 |
| 6 | [openai/math](https://github.com/openai/math) | +15101 | 15101 |
| 7 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +15047 | 15047 |
| 8 | [yetone/magpie](https://github.com/yetone/magpie) | +15015 | 15015 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +14547 | 14547 |
| 10 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +14031 | 14031 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +13459 | 13459 |
| 12 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +12387 | 12387 |
| 13 | [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | +11296 | 11296 |
