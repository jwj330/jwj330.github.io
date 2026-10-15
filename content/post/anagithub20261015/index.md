---
title: "2026-10-15 GitHub增长趋势报告"
description: "1.rea+28507 2.VoiceStudio+2789 3.photocraft+2235 4.dsh-our-free-model+1691 5.skills+1616"
date: 2026-10-16T07:00:09+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-16 07:00:09

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
        'daily': {"categories": ["storytold/wordcraft", "heygen-com/hyperframes", "Niko1221/Strata", "affaan-m/ECC", "LibreSpark/LibreTV", "Leonxlnx/taste-skill", "anthropics/claude-plugins-official", "eternity4719/HowToLiveBetter", "stablyai/orca", "ifixai-ai/iFixAi", "vxcontrol/pentagi", "K-Dense-AI/scientific-agent-skills", "NationalSecurityAgency/ghidra", "storytold/artcraft", "boykopovar/AnyPS5", "mattpocock/skills", "Ebony-Vinyl/dsh-our-free-model", "storytold/photocraft", "debpalash/VoiceStudio", "morluto/rea"], "data": [808, 841, 853, 860, 914, 916, 944, 948, 961, 1031, 1082, 1123, 1265, 1363, 1514, 1616, 1691, 2235, 2789, 28507]},
        'weekly': {"categories": ["wheresryan22/anatomy"], "data": [12657]},
        'monthly': {"categories": ["cdyforever/how-to-live-better", "wheresryan22/anatomy", "storytold/lightcraft", "storytold/wordcraft", "yetone/magpie", "storytold/filmcraft", "storytold/pdfcraft", "openai/math", "robbietilton/Compositor", "Ebony-Vinyl/dsh-our-free-model", "browser-use/jev-ultrafast", "Niko1221/Strata", "NandhaKishorM/laya", "storytold/photocraft"], "data": [12062, 12657, 12960, 13146, 13429, 13825, 14412, 14931, 17057, 17805, 23007, 25423, 33045, 63204]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +28507 | 268771 |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +2789 | 68962 |
| 3 | [storytold/photocraft](https://github.com/storytold/photocraft) | +2235 | 63204 |
| 4 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +1691 | 17805 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1616 | 292788 |
| 6 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +1514 | 38589 |
| 7 | [storytold/artcraft](https://github.com/storytold/artcraft) | +1363 | 29200 |
| 8 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +1265 | 88687 |
| 9 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +1123 | 50409 |
| 10 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1082 | 30455 |
| 11 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +1031 | 28345 |
| 12 | [stablyai/orca](https://github.com/stablyai/orca) | +961 | 93423 |
| 13 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +948 | 63844 |
| 14 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +944 | 39009 |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +916 | 97287 |
| 16 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +914 | 17989 |
| 17 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +860 | 280305 |
| 18 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +853 | 25423 |
| 19 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +841 | 64504 |
| 20 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +808 | 13146 |
| 21 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +788 | 164368 |
| 22 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +759 | 250419 |
| 23 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +741 | 14412 |
| 24 | [yetone/magpie](https://github.com/yetone/magpie) | +734 | 13429 |
| 25 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +703 | 29769 |
| 26 | [obra/superpowers](https://github.com/obra/superpowers) | +689 | 299837 |
| 27 | [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | +674 | 131601 |
| 28 | [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | +673 | 47477 |
| 29 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +641 | 69754 |
| 30 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +616 | 53066 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +12657 | 12657 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +63204 | 63204 |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | +33045 | 33045 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +25423 | 25423 |
| 4 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | +23007 | 23007 |
| 5 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +17805 | 17805 |
| 6 | [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | +17057 | 17057 |
| 7 | [openai/math](https://github.com/openai/math) | +14931 | 14931 |
| 8 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +14412 | 14412 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +13825 | 13825 |
| 10 | [yetone/magpie](https://github.com/yetone/magpie) | +13429 | 13429 |
| 11 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +13146 | 13146 |
| 12 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +12960 | 12960 |
| 13 | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | +12657 | 12657 |
| 14 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +12062 | 12062 |
