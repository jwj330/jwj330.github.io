---
title: "2026-04-27 GitHub增长趋势报告"
description: "1.skills+1136 2.free-claude-code+620 3.tolaria+322 4.agent-skills+234 5.GitNexus+224"
date: 2026-04-27T21:04:48+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-27 21:04:48

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
        'daily': {"categories": ["Wei-Shaw/sub2api", "trycua/cua", "multica-ai/multica", "maillab/cloud-mail", "alchaincyf/nuwa-skill", "ComposioHQ/awesome-codex-skills", "heygen-com/hyperframes", "Anil-matcha/Open-Generative-AI", "freestylefly/awesome-gpt-image-2", "Fincept-Corporation/FinceptTerminal", "JuliusBrussee/caveman", "rtk-ai/rtk", "badlogic/pi-mono", "microsoft/VibeVoice", "safishamsi/graphify", "abhigyanpatwari/GitNexus", "addyosmani/agent-skills", "refactoringhq/tolaria", "Alishahryar1/free-claude-code", "mattpocock/skills"], "data": [102, 103, 111, 116, 121, 123, 128, 129, 149, 163, 168, 172, 174, 187, 216, 224, 234, 322, 620, 1136]},
        'weekly': {"categories": ["browser-use/browser-harness", "op7418/guizang-ppt-skill", "Anil-matcha/Open-Generative-AI", "multica-ai/multica", "thedotmack/claude-mem", "farion1231/cc-switch", "safishamsi/graphify", "VoltAgent/awesome-design-md", "addyosmani/agent-skills", "rtk-ai/rtk", "garrytan/gstack", "elder-plinius/CL4R1T4S", "JuliusBrussee/caveman", "Fincept-Corporation/FinceptTerminal", "refactoringhq/tolaria", "Z4nzu/hackingtool", "mattpocock/skills", "Alishahryar1/free-claude-code", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [594, 595, 616, 633, 686, 730, 789, 840, 857, 900, 951, 993, 1029, 1120, 1169, 1384, 1976, 2126, 2366, 4369]},
        'monthly': {"categories": ["Yeachan-Heo/oh-my-codex", "luongnv89/claude-howto", "addyosmani/agent-skills", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "anthropics/claude-code", "openclaw/openclaw", "garrytan/gstack", "safishamsi/graphify", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4188, 4241, 4453, 4485, 4559, 4744, 5181, 5263, 5450, 6126, 6919, 7247, 7905, 7949, 8492, 9312, 12442, 13092, 18431, 25457]}
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
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1136 | 29403 |
| 2 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +620 | 15898 |
| 3 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +322 | 7262 |
| 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +234 | 24518 |
| 5 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +224 | 31364 |
| 6 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +216 | 36392 |
| 7 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +187 | 42926 |
| 8 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +174 | 41544 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +172 | 36938 |
| 10 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +168 | 48034 |
| 11 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +163 | 16137 |
| 12 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +149 | 1214 |
| 13 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +129 | 9288 |
| 14 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +128 | 11887 |
| 15 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +123 | 2689 |
| 16 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +121 | 15563 |
| 17 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +116 | 7938 |
| 18 | [multica-ai/multica](https://github.com/multica-ai/multica) | +111 | 21958 |
| 19 | [trycua/cua](https://github.com/trycua/cua) | +103 | 14731 |
| 20 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +102 | 16126 |
| 21 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +95 | 3425 |
| 22 | [gastownhall/beads](https://github.com/gastownhall/beads) | +95 | 22128 |
| 23 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +95 | 3297 |
| 24 | [zhom/donutbrowser](https://github.com/zhom/donutbrowser) | +91 | 2039 |
| 25 | [PostHog/posthog](https://github.com/PostHog/posthog) | +87 | 31767 |
| 26 | [tiagozip/cap](https://github.com/tiagozip/cap) | +85 | 6093 |
| 27 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +80 | 7549 |
| 28 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +77 | 3210 |
| 29 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +76 | 48583 |
| 30 | [santifer/career-ops](https://github.com/santifer/career-ops) | +75 | 40290 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4369 | 93766 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2366 | 120429 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2126 | 15899 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1976 | 29404 |
| 5 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1384 | 55070 |
| 6 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1169 | 7262 |
| 7 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1120 | 16137 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1029 | 48034 |
| 9 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +993 | 25693 |
| 10 | [garrytan/gstack](https://github.com/garrytan/gstack) | +951 | 85175 |
| 11 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +900 | 36938 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +857 | 24518 |
| 13 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +840 | 66697 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +789 | 36392 |
| 15 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +730 | 52780 |
| 16 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +686 | 30678 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +633 | 21958 |
| 18 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +616 | 9288 |
| 19 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +595 | 3425 |
| 20 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +594 | 7549 |
| 21 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +592 | 11887 |
| 22 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +574 | 41544 |
| 23 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +531 | 4368 |
| 24 | [santifer/career-ops](https://github.com/santifer/career-ops) | +519 | 40290 |
| 25 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +507 | 9843 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +498 | 31364 |
| 27 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +490 | 3210 |
| 28 | [tw93/Kami](https://github.com/tw93/Kami) | +457 | 3637 |
| 29 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +409 | 52855 |
| 30 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +402 | 7707 |
| 31 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +386 | 42926 |
| 32 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +385 | 13467 |
| 33 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +384 | 25141 |
| 34 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +370 | 19101 |
| 35 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +367 | 15563 |
| 36 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +341 | 7092 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +335 | 41165 |
| 38 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +334 | 10655 |
| 39 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +325 | 19019 |
| 40 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +323 | 8648 |
| 41 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +319 | 16126 |
| 42 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +314 | 22210 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +307 | 11784 |
| 44 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +307 | 23664 |
| 45 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +303 | 16372 |
| 46 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +290 | 32836 |
| 47 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +286 | 3934 |
| 48 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +286 | 13684 |
| 49 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +285 | 26353 |
| 50 | [PostHog/posthog](https://github.com/PostHog/posthog) | +283 | 31767 |
| 51 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +281 | 2689 |
| 52 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +280 | 21768 |
| 53 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +273 | 48583 |
| 54 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +270 | 56952 |
| 55 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +270 | 25416 |
| 56 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +269 | 4882 |
| 57 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +267 | 24690 |
| 58 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +267 | 49999 |
| 59 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +264 | 29208 |
| 60 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +258 | 18431 |
| 61 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +247 | 40565 |
| 62 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +236 | 13466 |
| 63 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +235 | 29464 |
| 64 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +231 | 4565 |
| 65 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +231 | 43331 |
| 66 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +229 | 3587 |
| 67 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +228 | 8742 |
| 68 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +227 | 33135 |
| 69 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +227 | 4283 |
| 70 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +225 | 7938 |
| 71 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +224 | 31907 |
| 72 | [victorchen96/deepseek_v4_rolepaly_instruct](https://github.com/victorchen96/deepseek_v4_rolepaly_instruct) | +216 | 1287 |
| 73 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +216 | 19974 |
| 74 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +212 | 41516 |
| 75 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +209 | 8830 |
| 76 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +207 | 5254 |
| 77 | [trycua/cua](https://github.com/trycua/cua) | +205 | 14731 |
| 78 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +205 | 22257 |
| 79 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +202 | 29272 |
| 80 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +200 | 7097 |
| 81 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +199 | 26805 |
| 82 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +196 | 1214 |
| 83 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +191 | 35379 |
| 84 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +191 | 31592 |
| 85 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +189 | 3297 |
| 86 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +189 | 5418 |
| 87 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +187 | 4318 |
| 88 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +187 | 39082 |
| 89 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +185 | 24161 |
| 90 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +184 | 1305 |
| 91 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +181 | 1511 |
| 92 | [tiagozip/cap](https://github.com/tiagozip/cap) | +179 | 6093 |
| 93 | [leigest519/OpenGame](https://github.com/leigest519/OpenGame) | +179 | 1388 |
| 94 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +169 | 33705 |
| 95 | [gastownhall/beads](https://github.com/gastownhall/beads) | +164 | 22128 |
| 96 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +164 | 25752 |
| 97 | [blader/humanizer](https://github.com/blader/humanizer) | +155 | 15900 |
| 98 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +155 | 11039 |
| 99 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +155 | 16774 |
| 100 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +149 | 3565 |
| 101 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +148 | 2320 |
| 102 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +148 | 4722 |
| 103 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +146 | 937 |
| 104 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +146 | 861 |
| 105 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +138 | 16079 |
| 106 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +137 | 32794 |
| 107 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +137 | 36799 |
| 108 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +136 | 811 |
| 109 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +136 | 12930 |
| 110 | [the-hidden-fish/advisor-ledger](https://github.com/the-hidden-fish/advisor-ledger) | +131 | 1094 |
| 111 | [jundot/omlx](https://github.com/jundot/omlx) | +130 | 11682 |
| 112 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +128 | 30575 |
| 113 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +127 | 740 |
| 114 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +126 | 1951 |
| 115 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +125 | 41067 |
| 116 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +125 | 11397 |
| 117 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +125 | 28623 |
| 118 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +123 | 1214 |
| 119 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +123 | 44545 |
| 120 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +122 | 908 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25457 | 188797 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18431 | 120429 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +13092 | 93766 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12442 | 66698 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9312 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +8492 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7949 | 49999 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7905 | 48034 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7247 | 40290 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6919 | 45494 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6126 | 36392 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5450 | 85176 |
| 13 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5263 | 224760 |
| 14 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5181 | 69674 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4744 | 24690 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4559 | 33135 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4485 | 30678 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4453 | 24518 |
| 19 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4241 | 29464 |
| 20 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4188 | 26353 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4159 | 87723 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4158 | 48583 |
| 23 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4094 | 59568 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3734 | 21958 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3647 | 36938 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3452 | 74774 |
| 27 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3302 | 109881 |
| 28 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3290 | 77193 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3112 | 34148 |
| 30 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3039 | 29405 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2969 | 52780 |
| 32 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2902 | 42926 |
| 33 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2896 | 31592 |
| 34 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2804 | 17062 |
| 35 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2752 | 16774 |
| 36 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2662 | 15563 |
| 37 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2644 | 56952 |
| 38 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2520 | 16407 |
| 39 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2451 | 57787 |
| 40 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2427 | 64015 |
| 41 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2408 | 57989 |
| 42 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2363 | 11397 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2307 | 85286 |
| 44 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2293 | 15899 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2234 | 11784 |
| 46 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2193 | 16137 |
| 47 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2170 | 41544 |
| 48 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2138 | 22210 |
| 49 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2131 | 18431 |
| 50 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2118 | 24161 |
| 51 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2094 | 11887 |
| 52 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2043 | 31364 |
| 53 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +2004 | 28623 |
| 54 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1999 | 12879 |
| 55 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1942 | 31098 |
| 56 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1887 | 21768 |
| 57 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1879 | 33878 |
| 58 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1870 | 55070 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1850 | 16079 |
| 60 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1841 | 30590 |
| 61 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1836 | 10077 |
| 62 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1757 | 13466 |
| 63 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1722 | 79656 |
| 64 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1702 | 17565 |
| 65 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1665 | 26805 |
| 66 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1664 | 19519 |
| 67 | [openai/codex](https://github.com/openai/codex) | +1578 | 61744 |
| 68 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1563 | 25693 |
| 69 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1509 | 32794 |
| 70 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1494 | 29208 |
| 71 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1491 | 73135 |
| 72 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1481 | 18734 |
| 73 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1479 | 16372 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1472 | 41165 |
| 75 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1460 | 23664 |
| 76 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1426 | 11749 |
| 77 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1422 | 8830 |
| 78 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1419 | 6630 |
| 79 | [github/spec-kit](https://github.com/github/spec-kit) | +1407 | 71722 |
| 80 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1397 | 98536 |
| 81 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1371 | 52855 |
| 82 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1367 | 45886 |
| 83 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1364 | 37330 |
| 84 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1337 | 41516 |
| 85 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1335 | 22153 |
| 86 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1326 | 25141 |
| 87 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1324 | 6689 |
| 88 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1321 | 22257 |
| 89 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1315 | 95754 |
| 90 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1288 | 43331 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1288 | 35379 |
| 92 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1275 | 10693 |
| 93 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1253 | 7549 |
| 94 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1248 | 18369 |
| 95 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1230 | 13467 |
| 96 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1218 | 16126 |
| 97 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1171 | 7262 |
| 98 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1132 | 20881 |
| 99 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1104 | 9288 |
| 100 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1042 | 7708 |
| 101 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1027 | 78902 |
| 102 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1009 | 6184 |
| 103 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +989 | 39082 |
| 104 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +987 | 31907 |
| 105 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +968 | 8648 |
| 106 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +964 | 9037 |
| 107 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +960 | 12930 |
| 108 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +897 | 25416 |
| 109 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +890 | 11961 |
| 110 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +889 | 4722 |
| 111 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +876 | 6585 |
| 112 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +865 | 7018 |
| 113 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +860 | 47122 |
| 114 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +843 | 52700 |
| 115 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +841 | 4882 |
| 116 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +839 | 4850 |
| 117 | [google/magika](https://github.com/google/magika) | +832 | 16789 |
| 118 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +828 | 4365 |
| 119 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +800 | 5418 |
| 120 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +762 | 4565 |
| 121 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +750 | 5621 |
| 122 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +739 | 11967 |
| 123 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +738 | 4061 |
| 124 | [jundot/omlx](https://github.com/jundot/omlx) | +736 | 11682 |
| 125 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +736 | 21875 |
| 126 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +736 | 5789 |
| 127 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +734 | 41067 |
| 128 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +733 | 11039 |
| 129 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +733 | 9644 |
| 130 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +706 | 39841 |
| 131 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +702 | 4169 |
| 132 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +679 | 3297 |
| 133 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +667 | 30252 |
| 134 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +666 | 54903 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +646 | 34411 |
| 136 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +645 | 19019 |
| 137 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +642 | 31387 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +615 | 36799 |
| 139 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +605 | 23150 |
| 140 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +595 | 11541 |
| 141 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +561 | 3529 |
| 142 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +558 | 19561 |
| 143 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +551 | 3205 |
| 144 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +551 | 18033 |
| 145 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +541 | 37564 |
| 146 | [eze-is/web-access](https://github.com/eze-is/web-access) | +536 | 5741 |
| 147 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +533 | 7628 |
| 148 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +532 | 2603 |
| 149 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +530 | 17331 |
| 150 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +527 | 3200 |
| 151 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +519 | 24407 |
| 152 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +518 | 30811 |
| 153 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +513 | 3587 |
| 154 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +510 | 7092 |
| 155 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +502 | 30575 |
| 156 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +500 | 25866 |
| 157 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +498 | 11772 |
| 158 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +497 | 24806 |
| 159 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +494 | 2867 |
| 160 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +493 | 44545 |
| 161 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +487 | 4909 |
| 162 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +476 | 2665 |
| 163 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +473 | 11727 |
| 164 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +469 | 3887 |
| 165 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +454 | 2380 |
| 166 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +447 | 2596 |
| 167 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +444 | 3565 |
| 168 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +442 | 3310 |
| 169 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +439 | 6824 |
| 170 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +426 | 7097 |
| 171 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +413 | 36907 |
| 172 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +409 | 9590 |
| 173 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +409 | 24167 |
| 174 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +404 | 16011 |
| 175 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +370 | 2304 |
| 176 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +359 | 25752 |
| 177 | [PostHog/posthog](https://github.com/PostHog/posthog) | +355 | 31767 |
| 178 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +354 | 7938 |
| 179 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +346 | 25809 |
| 180 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +339 | 3508 |
| 181 | [floci-io/floci](https://github.com/floci-io/floci) | +334 | 4225 |
| 182 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +325 | 2824 |
| 183 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +323 | 3318 |
| 184 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +322 | 2689 |
| 185 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +322 | 12592 |
| 186 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +320 | 5835 |
| 187 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +304 | 9112 |
| 188 | [decolua/9router](https://github.com/decolua/9router) | +300 | 3220 |
| 189 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +272 | 36103 |
| 190 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +253 | 26456 |
| 191 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +250 | 1897 |
| 192 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +250 | 3096 |
| 193 | [88lin/video_vip](https://github.com/88lin/video_vip) | +231 | 1546 |
| 194 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +209 | 7362 |
| 195 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +209 | 15868 |
| 196 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +209 | 2804 |
| 197 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +206 | 11361 |
| 198 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +203 | 2746 |
| 199 | [tiagozip/cap](https://github.com/tiagozip/cap) | +202 | 6093 |
| 200 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +194 | 33712 |
| 201 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +187 | 5567 |
| 202 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +185 | 8791 |
| 203 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +184 | 4239 |
| 204 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +180 | 3135 |
| 205 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +178 | 7976 |
| 206 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +171 | 2560 |
| 207 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +170 | 565 |
| 208 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +165 | 4000 |
| 209 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +165 | 13062 |
| 210 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 816 |
| 211 | [usebruno/bruno](https://github.com/usebruno/bruno) | +162 | 41086 |
| 212 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +158 | 1033 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +157 | 22436 |
| 214 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +156 | 1538 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +150 | 40265 |
| 216 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +143 | 937 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +142 | 35473 |
| 218 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +137 | 1682 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +137 | 23626 |
| 220 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +131 | 14420 |
| 221 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +130 | 1790 |
| 222 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +130 | 29793 |
| 223 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +129 | 846 |
| 224 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +126 | 29777 |
| 225 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +125 | 760 |
| 226 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +121 | 712 |
| 227 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 609 |
| 228 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +118 | 5466 |
| 229 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +117 | 609 |
| 230 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +117 | 7378 |
| 231 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +116 | 39596 |
| 232 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +114 | 19232 |
| 233 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +112 | 10920 |
| 234 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +109 | 6798 |
| 235 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +106 | 26888 |
| 236 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 493 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +105 | 33000 |
| 238 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +103 | 1040 |
| 239 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +103 | 2023 |
| 240 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +102 | 641 |
| 241 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +101 | 767 |
| 242 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +100 | 656 |
| 243 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +99 | 12943 |
| 244 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | +97 | 1274 |
| 245 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +97 | 643 |
| 246 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 247 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1455 |
| 248 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +95 | 1407 |
| 249 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +93 | 1106 |
| 250 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +93 | 1936 |
| 251 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +92 | 1192 |
| 252 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +92 | 3115 |
| 253 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +92 | 1863 |
| 254 | [crimera/piko](https://github.com/crimera/piko) | +92 | 3361 |
| 255 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +91 | 1848 |
| 256 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +89 | 569 |
| 257 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 465 |
| 258 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +88 | 2380 |
| 259 | [openmemind/memind](https://github.com/openmemind/memind) | +88 | 562 |
| 260 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +87 | 478 |
| 261 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +86 | 3879 |
| 262 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +86 | 48784 |
| 263 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +85 | 640 |
| 264 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +84 | 743 |
| 265 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +83 | 427 |
| 266 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +82 | 474 |
| 267 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +82 | 1786 |
| 268 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +81 | 4082 |
| 269 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +80 | 699 |
| 270 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +80 | 1550 |
| 271 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +79 | 45263 |
| 272 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 2059 |
| 273 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +76 | 2774 |
| 274 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +75 | 2751 |
| 275 | [microg/GmsCore](https://github.com/microg/GmsCore) | +75 | 13076 |
| 276 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +74 | 3687 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +72 | 27396 |
| 278 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +70 | 615 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9404 |
| 280 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +65 | 379 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +60 | 7337 |
| 282 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +60 | 1249 |
| 283 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +60 | 1709 |
| 284 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +59 | 11781 |
| 285 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +58 | 37313 |
| 286 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +56 | 28974 |
| 287 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +55 | 305 |
| 288 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +54 | 4924 |
| 289 | [halo-dev/halo](https://github.com/halo-dev/halo) | +54 | 37991 |
| 290 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 291 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +53 | 1890 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1803 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +49 | 31476 |
| 294 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +45 | 234 |
| 295 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1732 |
| 296 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +43 | 277 |
| 297 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +41 | 594 |
| 298 | [hoo-dles/morphe-patches](https://github.com/hoo-dles/morphe-patches) | +41 | 449 |
| 299 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +41 | 8598 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
