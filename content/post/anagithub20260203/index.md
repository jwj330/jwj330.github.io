---
title: "GitHub 趋势报告 2026-02-03"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-03T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-03 20:39:54

本报告展示了 GitHub 上 Star 数增长最快的仓库。

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
        'weekly': {"categories": ["immich-app/immich", "x1xhlol/system-prompts-and-models-of-ai-tools", "firecrawl/firecrawl", "bmad-code-org/BMAD-METHOD", "github/spec-kit", "DigitalPlatDev/FreeDomain", "daytonaio/daytona", "Shubhamsaboo/awesome-llm-apps", "remotion-dev/remotion", "codecrafters-io/build-your-own-x", "sindresorhus/awesome", "anthropics/claude-code", "obra/superpowers", "anthropics/skills", "anomalyco/opencode", "affaan-m/everything-claude-code", "ComposioHQ/awesome-claude-skills", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "openclaw/openclaw"], "data": [1354, 1597, 1641, 1661, 1726, 1742, 1858, 1877, 1958, 2074, 2242, 2289, 5499, 6465, 6602, 6671, 29721, 29747, 29871, 88448]},
        'monthly': {"categories": ["daytonaio/daytona", "anthropics/claude-code", "anthropics/skills", "anthropics/prompt-eng-interactive-tutorial", "MHSanaei/3x-ui", "ComposioHQ/awesome-claude-skills", "OpenBMB/ChatDev", "block/goose", "asgeirtj/system_prompts_leaks", "blakeblackshear/frigate", "Lissy93/web-check", "tw93/Mole", "bmad-code-org/BMAD-METHOD", "remotion-dev/remotion", "slatedocs/slate", "ManimCommunity/manim", "affaan-m/everything-claude-code", "obra/superpowers", "anomalyco/opencode", "openclaw/openclaw"], "data": [10155, 12603, 29102, 29475, 29645, 29721, 29747, 29827, 29871, 29927, 31789, 33190, 33963, 34746, 36171, 36607, 38901, 43404, 49119, 157135]}
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

