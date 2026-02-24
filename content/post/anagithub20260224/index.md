---
title: "GitHub 趋势报告 2026-02-24"
description: "GitHub 每日/每周/每月 增长趋势可视化报告"
date: 2026-02-24T12:00:00+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-02-24 20:39:19

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
        'daily': {"categories": ["AUTOMATIC1111/stable-diffusion-webui", "thedotmack/claude-mem", "sindresorhus/awesome", "firecrawl/firecrawl", "github/spec-kit", "bmad-code-org/BMAD-METHOD", "clash-verge-rev/clash-verge-rev", "codecrafters-io/build-your-own-x", "anthropics/claude-code", "nextlevelbuilder/ui-ux-pro-max-skill", "ComposioHQ/awesome-claude-skills", "code-yeongyu/oh-my-opencode", "OpenBB-finance/OpenBB", "f/prompts.chat", "anomalyco/opencode", "anthropics/skills", "affaan-m/everything-claude-code", "obra/superpowers", "x1xhlol/system-prompts-and-models-of-ai-tools", "openclaw/openclaw"], "data": [236, 258, 266, 279, 288, 310, 339, 341, 347, 370, 370, 430, 458, 532, 769, 828, 1057, 1140, 2751, 3791]},
        'weekly': {"categories": ["github/spec-kit", "tw93/Mole", "ComposioHQ/awesome-claude-skills", "nextlevelbuilder/ui-ux-pro-max-skill", "code-yeongyu/oh-my-opencode", "firecrawl/firecrawl", "codecrafters-io/build-your-own-x", "f/prompts.chat", "sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "Developer-Y/cs-video-courses", "anthropics/skills", "affaan-m/everything-claude-code", "anomalyco/opencode", "obra/superpowers", "x1xhlol/system-prompts-and-models-of-ai-tools", "openclaw/openclaw", "qarmin/czkawka", "thedotmack/claude-mem"], "data": [1538, 1762, 1845, 1866, 1902, 1941, 1959, 2107, 2303, 2327, 3174, 3288, 3750, 3836, 3849, 6837, 7946, 19942, 29479, 30678]},
        'monthly': {"categories": ["sindresorhus/awesome", "anthropics/claude-code", "daytonaio/daytona", "x1xhlol/system-prompts-and-models-of-ai-tools", "anthropics/skills", "anomalyco/opencode", "obra/superpowers", "qarmin/czkawka", "TauricResearch/TradingAgents", "patchy631/ai-engineering-hub", "thedotmack/claude-mem", "block/goose", "OpenBMB/ChatDev", "asgeirtj/system_prompts_leaks", "google/langextract", "code-yeongyu/oh-my-opencode", "nextlevelbuilder/ui-ux-pro-max-skill", "ComposioHQ/awesome-claude-skills", "affaan-m/everything-claude-code", "openclaw/openclaw"], "data": [8423, 9121, 9732, 11841, 21991, 22600, 24450, 29479, 30590, 30612, 30678, 31098, 31182, 32872, 33636, 33878, 34148, 37330, 51199, 224760]}
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



### 🚀 今日 Top 50 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +3791 | 224760 |
| 2 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | +2751 | 122870 |
| 3 | [obra/superpowers](https://github.com/obra/superpowers) | +1140 | 60312 |
| 4 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +1057 | 51199 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | +828 | 74774 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +769 | 109881 |
| 7 | [f/prompts.chat](https://github.com/f/prompts.chat) | +532 | 147486 |
| 8 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | +458 | 61818 |
| 9 | [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode) | +430 | 33878 |
| 10 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +370 | 37330 |
| 11 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +370 | 34148 |
| 12 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +347 | 69674 |
| 13 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | +341 | 468668 |
| 14 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +339 | 98536 |
| 15 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +310 | 37564 |
| 16 | [github/spec-kit](https://github.com/github/spec-kit) | +288 | 71722 |
| 17 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +279 | 85286 |
| 18 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | +266 | 440400 |
| 19 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +258 | 30678 |
| 20 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | +236 | 161009 |
| 21 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | +234 | 400074 |
| 22 | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | +226 | 59035 |
| 23 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | +207 | 149018 |
| 24 | [openai/codex](https://github.com/openai/codex) | +191 | 61744 |
| 25 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +189 | 96919 |
| 26 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | +185 | 176173 |
| 27 | [daytonaio/daytona](https://github.com/daytonaio/daytona) | +173 | 60117 |
| 28 | [tw93/Mole](https://github.com/tw93/Mole) | +171 | 36870 |
| 29 | [torvalds/linux](https://github.com/torvalds/linux) | +167 | 218586 |
| 30 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | +165 | 274926 |
| 31 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | +162 | 284403 |
| 32 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | +161 | 336530 |
| 33 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | +161 | 148393 |
| 34 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | +150 | 32872 |
| 35 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +145 | 36799 |
| 36 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +140 | 30590 |
| 37 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | +137 | 207613 |
| 38 | [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | +133 | 74887 |
| 39 | [upstash/context7](https://github.com/upstash/context7) | +130 | 46759 |
| 40 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | +127 | 104078 |
| 41 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | +121 | 95547 |
| 42 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +121 | 47122 |
| 43 | [cloudcommunity/Free-Certifications](https://github.com/cloudcommunity/Free-Certifications) | +120 | 51780 |
| 44 | [langgenius/dify](https://github.com/langgenius/dify) | +116 | 130192 |
| 45 | [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | +114 | 44551 |
| 46 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | +114 | 37810 |
| 47 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | +102 | 124800 |
| 48 | [docling-project/docling](https://github.com/docling-project/docling) | +102 | 54041 |
| 49 | [immich-app/immich](https://github.com/immich-app/immich) | +98 | 93424 |
| 50 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | +96 | 143722 |
