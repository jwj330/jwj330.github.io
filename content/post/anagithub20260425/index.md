---
title: "2026-04-25 GitHub增长趋势报告"
description: "1.free-claude-code+592 2.tolaria+191 3.skills+178 4.guizang-ppt-skill+171 5.rtk+158"
date: 2026-04-25T20:41:19+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-25 20:41:19

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
        'daily': {"categories": ["HKUDS/DeepTutor", "nashsu/llm_wiki", "addyosmani/agent-skills", "coreyhaines31/marketingskills", "multica-ai/multica", "santifer/career-ops", "browser-use/browser-harness", "google/osv-scanner", "PostHog/posthog", "safishamsi/graphify", "badlogic/pi-mono", "zilliztech/claude-context", "Anil-matcha/Open-Generative-AI", "YouMind-OpenLab/awesome-gpt-image-2", "JuliusBrussee/caveman", "rtk-ai/rtk", "op7418/guizang-ppt-skill", "mattpocock/skills", "refactoringhq/tolaria", "Alishahryar1/free-claude-code"], "data": [61, 64, 65, 66, 66, 68, 72, 74, 76, 76, 86, 87, 97, 97, 101, 158, 171, 178, 191, 592]},
        'weekly': {"categories": ["santifer/career-ops", "farion1231/cc-switch", "Z4nzu/hackingtool", "Donchitos/Claude-Code-Game-Studios", "multica-ai/multica", "addyosmani/agent-skills", "NawfalMotii79/PLFM_RADAR", "safishamsi/graphify", "rtk-ai/rtk", "thedotmack/claude-mem", "Alishahryar1/free-claude-code", "VoltAgent/awesome-design-md", "browser-use/browser-harness", "garrytan/gstack", "JuliusBrussee/caveman", "heygen-com/hyperframes", "elder-plinius/CL4R1T4S", "Fincept-Corporation/FinceptTerminal", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [592, 606, 615, 674, 762, 777, 798, 816, 912, 931, 1056, 1075, 1087, 1183, 1245, 1349, 1387, 1722, 2898, 4512]},
        'monthly': {"categories": ["paperclipai/paperclip", "addyosmani/agent-skills", "luongnv89/claude-howto", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "openclaw/openclaw", "anthropics/claude-code", "garrytan/gstack", "safishamsi/graphify", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "affaan-m/everything-claude-code", "forrestchang/andrej-karpathy-skills", "VoltAgent/awesome-design-md", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4136, 4150, 4212, 4341, 4478, 4647, 5155, 5167, 5569, 5793, 6881, 7080, 7572, 7850, 8694, 9488, 11470, 12124, 17691, 25298]}
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
| 1 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +592 | 11302 |
| 2 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +191 | 4617 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +178 | 19655 |
| 4 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +171 | 2653 |
| 5 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +158 | 35410 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +101 | 46441 |
| 7 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +97 | 2501 |
| 8 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +97 | 8216 |
| 9 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +87 | 9338 |
| 10 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +86 | 40039 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +76 | 34773 |
| 12 | [PostHog/posthog](https://github.com/PostHog/posthog) | +76 | 31767 |
| 13 | [google/osv-scanner](https://github.com/google/osv-scanner) | +74 | 9728 |
| 14 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +72 | 6809 |
| 15 | [santifer/career-ops](https://github.com/santifer/career-ops) | +68 | 39600 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +66 | 21034 |
| 17 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +66 | 24729 |
| 18 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +65 | 22979 |
| 19 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +64 | 3363 |
| 20 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +61 | 21739 |
| 21 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +61 | 6750 |
| 22 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +58 | 13530 |
| 23 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +54 | 7109 |
| 24 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +51 | 863 |
| 25 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +51 | 14818 |
| 26 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +46 | 29187 |
| 27 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +46 | 8047 |
| 28 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +45 | 10665 |
| 29 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +45 | 18783 |
| 30 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +44 | 15404 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4512 | 87272 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2898 | 116594 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1722 | 14818 |
| 4 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1387 | 25519 |
| 5 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1349 | 10665 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1245 | 46441 |
| 7 | [garrytan/gstack](https://github.com/garrytan/gstack) | +1183 | 83224 |
| 8 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1087 | 6809 |
| 9 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +1075 | 65353 |
| 10 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1056 | 11302 |
| 11 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +931 | 30678 |
| 12 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +912 | 35410 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +816 | 34773 |
| 14 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +798 | 18181 |
| 15 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +777 | 22979 |
| 16 | [multica-ai/multica](https://github.com/multica-ai/multica) | +762 | 21034 |
| 17 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +674 | 16130 |
| 18 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +615 | 55070 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +606 | 51294 |
| 20 | [santifer/career-ops](https://github.com/santifer/career-ops) | +592 | 39600 |
| 21 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +552 | 25125 |
| 22 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +531 | 23301 |
| 23 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +503 | 52598 |
| 24 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +491 | 4020 |
| 25 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +486 | 12924 |
| 26 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +469 | 4617 |
| 27 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +464 | 4048 |
| 28 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +461 | 7109 |
| 29 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +437 | 12186 |
| 30 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +434 | 40039 |
| 31 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +423 | 10503 |
| 32 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +421 | 9338 |
| 33 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +415 | 21739 |
| 34 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +391 | 8615 |
| 35 | [mattpocock/skills](https://github.com/mattpocock/skills) | +384 | 19655 |
| 36 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +384 | 6882 |
| 37 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +376 | 24729 |
| 38 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +373 | 8216 |
| 39 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +366 | 2653 |
| 40 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +359 | 14619 |
| 41 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +353 | 13094 |
| 42 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +352 | 18783 |
| 43 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +350 | 40604 |
| 44 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +335 | 4938 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +333 | 11369 |
| 46 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +332 | 10056 |
| 47 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +327 | 8047 |
| 48 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +326 | 21445 |
| 49 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +317 | 36907 |
| 50 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +313 | 49634 |
| 51 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +312 | 18645 |
| 52 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +311 | 2501 |
| 53 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +311 | 6749 |
| 54 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +303 | 48015 |
| 55 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +295 | 25801 |
| 56 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +279 | 24358 |
| 57 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +271 | 15404 |
| 58 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +270 | 16576 |
| 59 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +270 | 32734 |
| 60 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +266 | 56451 |
| 61 | [PerryTS/perry](https://github.com/PerryTS/perry) | +265 | 1729 |
| 62 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +258 | 42906 |
| 63 | [smol-machines/smolvm](https://github.com/smol-machines/smolvm) | +257 | 2645 |
| 64 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +256 | 28734 |
| 65 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +256 | 13530 |
| 66 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +256 | 16412 |
| 67 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +255 | 26419 |
| 68 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +253 | 15927 |
| 69 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +235 | 23955 |
| 70 | [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | +234 | 1584 |
| 71 | [byoungd/English-level-up-tips](https://github.com/byoungd/English-level-up-tips) | +233 | 41523 |
| 72 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +232 | 32836 |
| 73 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +230 | 3809 |
| 74 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +228 | 37330 |
| 75 | [vercel-labs/wterm](https://github.com/vercel-labs/wterm) | +227 | 2409 |
| 76 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +223 | 40316 |
| 77 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +222 | 3363 |
| 78 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +213 | 19648 |
| 79 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +212 | 4992 |
| 80 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +212 | 32577 |
| 81 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +209 | 31263 |
| 82 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +207 | 2499 |
| 83 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +206 | 4172 |
| 84 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +203 | 21922 |
| 85 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +201 | 28890 |
| 86 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +200 | 8391 |
| 87 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +200 | 40998 |
| 88 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +193 | 28885 |
| 89 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +193 | 35089 |
| 90 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +188 | 3081 |
| 91 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +183 | 2196 |
| 92 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +180 | 31445 |
| 93 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +179 | 39841 |
| 94 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +177 | 5723 |
| 95 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +176 | 16040 |
| 96 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +175 | 37198 |
| 97 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +173 | 1759 |
| 98 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +170 | 10466 |
| 99 | [google/magika](https://github.com/google/magika) | +170 | 16707 |
| 100 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +166 | 12707 |
| 101 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +163 | 29188 |
| 102 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +162 | 28491 |
| 103 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +161 | 41078 |
| 104 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +159 | 10737 |
| 105 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +149 | 38683 |
| 106 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +149 | 11891 |
| 107 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +148 | 6071 |
| 108 | [OranAi-Ltd/oransim](https://github.com/OranAi-Ltd/oransim) | +146 | 1026 |
| 109 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +146 | 1611 |
| 110 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +141 | 36799 |
| 111 | [the-hidden-fish/advisor-ledger](https://github.com/the-hidden-fish/advisor-ledger) | +140 | 1074 |
| 112 | [jundot/omlx](https://github.com/jundot/omlx) | +137 | 11541 |
| 113 | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | +128 | 1476 |
| 114 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +124 | 40850 |
| 115 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +117 | 2096 |
| 116 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +116 | 4418 |
| 117 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +112 | 31208 |
| 118 | [PostHog/posthog](https://github.com/PostHog/posthog) | +107 | 31767 |
| 119 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +104 | 11761 |
| 120 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +102 | 19406 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25298 | 188341 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +17691 | 116594 |
| 3 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12124 | 65353 |
| 4 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +11470 | 87272 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9488 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +8694 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7850 | 49634 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7572 | 46441 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7080 | 39600 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6881 | 45340 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5793 | 34773 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5569 | 83224 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5167 | 69674 |
| 14 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5155 | 224760 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4647 | 24358 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4478 | 32734 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4341 | 30678 |
| 18 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4212 | 28885 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4150 | 22979 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4136 | 58798 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4127 | 86868 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4119 | 48015 |
| 23 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4078 | 25801 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3543 | 21034 |
| 25 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3425 | 76563 |
| 26 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3413 | 35410 |
| 27 | [anthropics/skills](https://github.com/anthropics/skills) | +3383 | 74774 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3181 | 109881 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3130 | 34148 |
| 30 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +3005 | 31263 |
| 31 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2879 | 63772 |
| 32 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2776 | 51294 |
| 33 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2772 | 16912 |
| 34 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2720 | 56451 |
| 35 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2707 | 16576 |
| 36 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2622 | 41078 |
| 37 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2596 | 23955 |
| 38 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2513 | 14619 |
| 39 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2490 | 57336 |
| 40 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2475 | 57326 |
| 41 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2448 | 16076 |
| 42 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2315 | 85286 |
| 43 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2144 | 11369 |
| 44 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2062 | 18181 |
| 45 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2041 | 12506 |
| 46 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +2001 | 28491 |
| 47 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2000 | 21739 |
| 48 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +1923 | 40039 |
| 49 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1912 | 31098 |
| 50 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1878 | 14818 |
| 51 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1868 | 79656 |
| 52 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1856 | 33878 |
| 53 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1844 | 30590 |
| 54 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1829 | 10665 |
| 55 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1816 | 10030 |
| 56 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1811 | 15927 |
| 57 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1803 | 21445 |
| 58 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1782 | 17262 |
| 59 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1726 | 29188 |
| 60 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1715 | 13094 |
| 61 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1665 | 19260 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1638 | 26419 |
| 63 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1631 | 16130 |
| 64 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1570 | 32577 |
| 65 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1527 | 25519 |
| 66 | [openai/codex](https://github.com/openai/codex) | +1522 | 61744 |
| 67 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1452 | 28734 |
| 68 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1437 | 40604 |
| 69 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1430 | 18546 |
| 70 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1420 | 11732 |
| 71 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1403 | 6546 |
| 72 | [github/spec-kit](https://github.com/github/spec-kit) | +1395 | 71722 |
| 73 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1390 | 73135 |
| 74 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1389 | 52598 |
| 75 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1388 | 19657 |
| 76 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1377 | 23301 |
| 77 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1374 | 8615 |
| 78 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1336 | 98536 |
| 79 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1334 | 45886 |
| 80 | [Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) | +1333 | 24905 |
| 81 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1322 | 6692 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1318 | 37330 |
| 83 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1316 | 40998 |
| 84 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1304 | 22028 |
| 85 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1299 | 42906 |
| 86 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1283 | 21922 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1278 | 24729 |
| 88 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1265 | 50258 |
| 89 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1244 | 35089 |
| 90 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1240 | 10503 |
| 91 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1239 | 95754 |
| 92 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1232 | 18218 |
| 93 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1226 | 11302 |
| 94 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1195 | 20687 |
| 95 | [JackChen-me/open-multi-agent](https://github.com/JackChen-me/open-multi-agent) | +1167 | 5895 |
| 96 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1152 | 12924 |
| 97 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1110 | 15404 |
| 98 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1087 | 6809 |
| 99 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1075 | 55070 |
| 100 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +984 | 6071 |
| 101 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +962 | 31445 |
| 102 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +957 | 9014 |
| 103 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +955 | 38683 |
| 104 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +948 | 78902 |
| 105 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +941 | 12707 |
| 106 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +930 | 7109 |
| 107 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +908 | 6538 |
| 108 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +890 | 11891 |
| 109 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +853 | 8047 |
| 110 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +840 | 5706 |
| 111 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +837 | 6882 |
| 112 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +829 | 52700 |
| 113 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +828 | 4797 |
| 114 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +808 | 25125 |
| 115 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +808 | 4418 |
| 116 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +808 | 8216 |
| 117 | [google/magika](https://github.com/google/magika) | +805 | 16707 |
| 118 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +801 | 4276 |
| 119 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +791 | 47122 |
| 120 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +788 | 30222 |
| 121 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +747 | 5606 |
| 122 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +741 | 39841 |
| 123 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +737 | 10737 |
| 124 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +735 | 21753 |
| 125 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +735 | 4096 |
| 126 | [jundot/omlx](https://github.com/jundot/omlx) | +732 | 11541 |
| 127 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +731 | 4037 |
| 128 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +730 | 9572 |
| 129 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +728 | 40850 |
| 130 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +727 | 4992 |
| 131 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +718 | 11761 |
| 132 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +671 | 4172 |
| 133 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +656 | 34258 |
| 134 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +648 | 54903 |
| 135 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +647 | 36799 |
| 136 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +627 | 31208 |
| 137 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +620 | 23050 |
| 138 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +620 | 24338 |
| 139 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +591 | 11531 |
| 140 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +578 | 18645 |
| 141 | [eze-is/web-access](https://github.com/eze-is/web-access) | +578 | 5661 |
| 142 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +555 | 19406 |
| 143 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +541 | 3472 |
| 144 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +540 | 7497 |
| 145 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +538 | 37564 |
| 146 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +535 | 17811 |
| 147 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +534 | 3136 |
| 148 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +530 | 30649 |
| 149 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +527 | 2569 |
| 150 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +523 | 24636 |
| 151 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +520 | 3172 |
| 152 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +519 | 2588 |
| 153 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +506 | 25779 |
| 154 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +506 | 2851 |
| 155 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +505 | 17164 |
| 156 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +495 | 3809 |
| 157 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +493 | 11629 |
| 158 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +478 | 2630 |
| 159 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +464 | 30363 |
| 160 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +444 | 2329 |
| 161 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +443 | 44545 |
| 162 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +435 | 6749 |
| 163 | [usestrix/strix](https://github.com/usestrix/strix) | +434 | 24580 |
| 164 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +430 | 2502 |
| 165 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +427 | 6707 |
| 166 | [cft0808/edict](https://github.com/cft0808/edict) | +416 | 15457 |
| 167 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +415 | 15943 |
| 168 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +413 | 3081 |
| 169 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +411 | 11388 |
| 170 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +407 | 9500 |
| 171 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +403 | 36907 |
| 172 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +402 | 2171 |
| 173 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +398 | 2817 |
| 174 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +396 | 19606 |
| 175 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +389 | 3445 |
| 176 | [jd-opensource/JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) | +380 | 1952 |
| 177 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +373 | 3059 |
| 178 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +366 | 24007 |
| 179 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +365 | 2254 |
| 180 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +362 | 2196 |
| 181 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +340 | 6750 |
| 182 | [floci-io/floci](https://github.com/floci-io/floci) | +335 | 4176 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +334 | 12474 |
| 184 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +330 | 25709 |
| 185 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +323 | 5723 |
| 186 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +320 | 9081 |
| 187 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +311 | 3248 |
| 188 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +298 | 5755 |
| 189 | [decolua/9router](https://github.com/decolua/9router) | +287 | 3088 |
| 190 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +277 | 3087 |
| 191 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +272 | 36103 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +255 | 1831 |
| 193 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +251 | 7178 |
| 194 | [88lin/video_vip](https://github.com/88lin/video_vip) | +224 | 1520 |
| 195 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +211 | 26242 |
| 196 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +208 | 11316 |
| 197 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +205 | 2770 |
| 198 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +203 | 7315 |
| 199 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +201 | 15836 |
| 200 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +196 | 8778 |
| 201 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +195 | 33712 |
| 202 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +192 | 4229 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +189 | 5536 |
| 204 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +186 | 3097 |
| 205 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +185 | 13045 |
| 206 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +184 | 7940 |
| 207 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +172 | 2534 |
| 208 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +172 | 2630 |
| 209 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +170 | 558 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +169 | 41086 |
| 211 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +161 | 813 |
| 212 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +155 | 998 |
| 213 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +155 | 3973 |
| 214 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +148 | 1670 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +146 | 40265 |
| 216 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +146 | 22390 |
| 217 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +144 | 1505 |
| 218 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +138 | 35473 |
| 219 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +133 | 760 |
| 220 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +123 | 1761 |
| 221 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +123 | 23570 |
| 222 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 607 |
| 223 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +120 | 688 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +118 | 29740 |
| 225 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +116 | 5444 |
| 226 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +116 | 29740 |
| 227 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +111 | 10885 |
| 228 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +110 | 7339 |
| 229 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +109 | 14278 |
| 230 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +107 | 19191 |
| 231 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +104 | 26822 |
| 232 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +103 | 6781 |
| 233 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +102 | 1853 |
| 234 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +101 | 39596 |
| 235 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +101 | 637 |
| 236 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +100 | 33000 |
| 237 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +99 | 750 |
| 238 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +98 | 2010 |
| 239 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +98 | 3080 |
| 240 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +98 | 1388 |
| 241 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +96 | 634 |
| 242 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +96 | 994 |
| 243 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 244 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +95 | 553 |
| 245 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +95 | 12900 |
| 246 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +95 | 637 |
| 247 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +95 | 1913 |
| 248 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +93 | 777 |
| 249 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +92 | 1426 |
| 250 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +89 | 1168 |
| 251 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 460 |
| 252 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +88 | 1806 |
| 253 | [WJZ-P/gemini-skill](https://github.com/WJZ-P/gemini-skill) | +87 | 805 |
| 254 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +85 | 529 |
| 255 | [crimera/piko](https://github.com/crimera/piko) | +85 | 3337 |
| 256 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +84 | 1047 |
| 257 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +83 | 629 |
| 258 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +82 | 705 |
| 259 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +81 | 467 |
| 260 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +81 | 4054 |
| 261 | [openmemind/memind](https://github.com/openmemind/memind) | +81 | 534 |
| 262 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +81 | 48784 |
| 263 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +80 | 3854 |
| 264 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +80 | 2343 |
| 265 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +80 | 2770 |
| 266 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +79 | 45263 |
| 267 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +76 | 676 |
| 268 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 2033 |
| 269 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +76 | 1166 |
| 270 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +76 | 767 |
| 271 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +75 | 3673 |
| 272 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +74 | 1742 |
| 273 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +73 | 962 |
| 274 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +73 | 2731 |
| 275 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +71 | 1496 |
| 276 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +70 | 437 |
| 277 | [microg/GmsCore](https://github.com/microg/GmsCore) | +70 | 13041 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +67 | 9381 |
| 279 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +64 | 377 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +64 | 27371 |
| 281 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +61 | 11756 |
| 282 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +60 | 7323 |
| 283 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +59 | 582 |
| 284 | [yunus-0x/meridian](https://github.com/yunus-0x/meridian) | +59 | 314 |
| 285 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +59 | 1690 |
| 286 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +56 | 37313 |
| 287 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +55 | 442 |
| 288 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +55 | 28973 |
| 289 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +54 | 319 |
| 290 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +50 | 4902 |
| 291 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +50 | 1867 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1792 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +48 | 31476 |
| 294 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +44 | 442 |
| 295 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +42 | 8582 |
| 296 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +41 | 589 |
| 297 | [risin42/NagramX](https://github.com/risin42/NagramX) | +41 | 1719 |
| 298 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +38 | 215 |
| 299 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +38 | 221 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
