---
title: "2026-10-14 GitHub增长趋势报告"
description: "1.rea+34310 2.photocraft+3196 3.VoiceStudio+3014 4.artcraft+2273 5.dsh-our-free-model+2046"
date: 2026-10-15T07:05:27+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-10-15 07:05:27

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
        'daily': {"categories": ["stablyai/orca", "eternity4719/HowToLiveBetter", "Niko1221/Strata", "heygen-com/hyperframes", "storytold/pdfcraft", "bilawalsidhu/gods-eye-view", "NationalSecurityAgency/ghidra", "vxcontrol/pentagi", "yetone/magpie", "LibreSpark/LibreTV", "cathrynlavery/diagram-design", "ifixai-ai/iFixAi", "storytold/wordcraft", "mattpocock/skills", "boykopovar/AnyPS5", "Ebony-Vinyl/dsh-our-free-model", "storytold/artcraft", "debpalash/VoiceStudio", "storytold/photocraft", "morluto/rea"], "data": [871, 878, 881, 917, 951, 1098, 1123, 1178, 1201, 1204, 1237, 1256, 1292, 1556, 1816, 2046, 2273, 3014, 3196, 34310]},
        'weekly': {"categories": ["storytold/wordcraft"], "data": [12338]},
        'monthly': {"categories": ["cdyforever/how-to-live-better", "storytold/wordcraft", "storytold/lightcraft", "yetone/magpie", "storytold/filmcraft", "storytold/pdfcraft", "openai/math", "Ebony-Vinyl/dsh-our-free-model", "robbietilton/Compositor", "browser-use/jev-ultrafast", "Niko1221/Strata", "NandhaKishorM/laya", "storytold/photocraft"], "data": [11846, 12338, 12567, 12695, 13256, 13671, 14812, 16114, 16900, 22916, 24570, 32906, 60969]}
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
| 1 | [morluto/rea](https://github.com/morluto/rea) | +34310 | 240264 |
| 2 | [storytold/photocraft](https://github.com/storytold/photocraft) | +3196 | 60969 |
| 3 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | +3014 | 66173 |
| 4 | [storytold/artcraft](https://github.com/storytold/artcraft) | +2273 | 27837 |
| 5 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +2046 | 16114 |
| 6 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | +1816 | 37075 |
| 7 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1556 | 291172 |
| 8 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +1292 | 12338 |
| 9 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +1256 | 27314 |
| 10 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | +1237 | 55285 |
| 11 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | +1204 | 17075 |
| 12 | [yetone/magpie](https://github.com/yetone/magpie) | +1201 | 12695 |
| 13 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | +1178 | 29373 |
| 14 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | +1123 | 87422 |
| 15 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | +1098 | 56419 |
| 16 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +951 | 13671 |
| 17 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +917 | 63663 |
| 18 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +881 | 24570 |
| 19 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | +878 | 62896 |
| 20 | [stablyai/orca](https://github.com/stablyai/orca) | +871 | 92462 |
| 21 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +866 | 29066 |
| 22 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | +864 | 279445 |
| 23 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | +845 | 163580 |
| 24 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +782 | 96371 |
| 25 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +742 | 13256 |
| 26 | [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | +723 | 11767 |
| 27 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | +710 | 249660 |
| 28 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +604 | 22300 |
| 29 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +597 | 102144 |
| 30 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | +589 | 35277 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +12338 | 12338 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | +60969 | 60969 |
| 2 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | +32906 | 32906 |
| 3 | [Niko1221/Strata](https://github.com/Niko1221/Strata) | +24570 | 24570 |
| 4 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | +22916 | 22916 |
| 5 | [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | +16900 | 16900 |
| 6 | [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | +16114 | 16114 |
| 7 | [openai/math](https://github.com/openai/math) | +14812 | 14812 |
| 8 | [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | +13671 | 13671 |
| 9 | [storytold/filmcraft](https://github.com/storytold/filmcraft) | +13256 | 13256 |
| 10 | [yetone/magpie](https://github.com/yetone/magpie) | +12695 | 12695 |
| 11 | [storytold/lightcraft](https://github.com/storytold/lightcraft) | +12567 | 12567 |
| 12 | [storytold/wordcraft](https://github.com/storytold/wordcraft) | +12338 | 12338 |
| 13 | [cdyforever/how-to-live-better](https://github.com/cdyforever/how-to-live-better) | +11846 | 11846 |
