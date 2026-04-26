---
title: "2026-04-26 GitHub增长趋势报告"
description: "1.andrej-karpathy-skills+1005 2.skills+613 3.free-claude-code+552 4.tolaria+444 5.rtk+217"
date: 2026-04-26T20:41:01+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-26 20:41:01

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
        'daily': {"categories": ["AmintaCCCP/GithubStarsManager", "browser-use/browser-harness", "PostHog/posthog", "penpot/penpot", "ComposioHQ/awesome-codex-skills", "YouMind-OpenLab/awesome-gpt-image-2", "microsoft/VibeVoice", "safishamsi/graphify", "badlogic/pi-mono", "op7418/guizang-ppt-skill", "heygen-com/hyperframes", "abhigyanpatwari/GitNexus", "JuliusBrussee/caveman", "Fincept-Corporation/FinceptTerminal", "Anil-matcha/Open-Generative-AI", "rtk-ai/rtk", "refactoringhq/tolaria", "Alishahryar1/free-claude-code", "mattpocock/skills", "forrestchang/andrej-karpathy-skills"], "data": [99, 99, 104, 106, 114, 121, 126, 135, 143, 148, 151, 167, 174, 176, 183, 217, 444, 552, 613, 1005]},
        'weekly': {"categories": ["santifer/career-ops", "farion1231/cc-switch", "multica-ai/multica", "addyosmani/agent-skills", "safishamsi/graphify", "thedotmack/claude-mem", "browser-use/browser-harness", "refactoringhq/tolaria", "heygen-com/hyperframes", "VoltAgent/awesome-design-md", "mattpocock/skills", "rtk-ai/rtk", "garrytan/gstack", "Z4nzu/hackingtool", "elder-plinius/CL4R1T4S", "JuliusBrussee/caveman", "Alishahryar1/free-claude-code", "Fincept-Corporation/FinceptTerminal", "NousResearch/hermes-agent", "forrestchang/andrej-karpathy-skills"], "data": [559, 653, 678, 716, 738, 800, 863, 888, 890, 903, 922, 945, 968, 1006, 1144, 1154, 1528, 1569, 2583, 4584]},
        'monthly': {"categories": ["paperclipai/paperclip", "addyosmani/agent-skills", "luongnv89/claude-howto", "thedotmack/claude-mem", "siddharthvaddem/openscreen", "Gitlawb/openclaude", "openclaw/openclaw", "anthropics/claude-code", "garrytan/gstack", "safishamsi/graphify", "chenglou/pretext", "santifer/career-ops", "JuliusBrussee/caveman", "MemPalace/mempalace", "obra/superpowers", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4150, 4218, 4270, 4442, 4519, 4696, 5156, 5164, 5485, 5921, 6901, 7172, 7741, 7897, 8561, 9352, 12282, 12413, 18031, 25369]}
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
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +1005 | 90354 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +613 | 22971 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +552 | 13273 |
| 4 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +444 | 6308 |
| 5 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +217 | 36051 |
| 6 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +183 | 8767 |
| 7 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +176 | 15441 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +174 | 47092 |
| 9 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +167 | 30057 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +151 | 11244 |
| 11 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +148 | 2968 |
| 12 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +143 | 40609 |
| 13 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +135 | 35417 |
| 14 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +126 | 41936 |
| 15 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +121 | 2867 |
| 16 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +114 | 1899 |
| 17 | [penpot/penpot](https://github.com/penpot/penpot) | +106 | 44370 |
| 18 | [PostHog/posthog](https://github.com/PostHog/posthog) | +104 | 31767 |
| 19 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +99 | 7128 |
| 20 | [AmintaCCCP/GithubStarsManager](https://github.com/AmintaCCCP/GithubStarsManager) | +99 | 2008 |
| 21 | [santifer/career-ops](https://github.com/santifer/career-ops) | +97 | 39965 |
| 22 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +95 | 22005 |
| 23 | [tiagozip/cap](https://github.com/tiagozip/cap) | +95 | 5935 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +93 | 21416 |
| 25 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +89 | 8303 |
| 26 | [Michael-A-Kuykendall/shimmy](https://github.com/Michael-A-Kuykendall/shimmy) | +82 | 4503 |
| 27 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +82 | 9589 |
| 28 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +81 | 1118 |
| 29 | [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) | +80 | 23645 |
| 30 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +78 | 10360 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +4584 | 90355 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +2583 | 118149 |
| 3 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +1569 | 15441 |
| 4 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1528 | 13273 |
| 5 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +1154 | 47092 |
| 6 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1144 | 25597 |
| 7 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1006 | 55070 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +968 | 83967 |
| 9 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +945 | 36051 |
| 10 | [mattpocock/skills](https://github.com/mattpocock/skills) | +922 | 22971 |
| 11 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +903 | 65942 |
| 12 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +890 | 11244 |
| 13 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +888 | 6308 |
| 14 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +863 | 7128 |
| 15 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +800 | 30678 |
| 16 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +738 | 35417 |
| 17 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +716 | 23650 |
| 18 | [multica-ai/multica](https://github.com/multica-ai/multica) | +678 | 21416 |
| 19 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +653 | 51866 |
| 20 | [santifer/career-ops](https://github.com/santifer/career-ops) | +559 | 39965 |
| 21 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +534 | 16238 |
| 22 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +529 | 8767 |
| 23 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +522 | 18308 |
| 24 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +510 | 4202 |
| 25 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +503 | 2968 |
| 26 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +492 | 40609 |
| 27 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +485 | 9589 |
| 28 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +455 | 52721 |
| 29 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +427 | 25296 |
| 30 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +425 | 7353 |
| 31 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +421 | 2867 |
| 32 | [tw93/Kami](https://github.com/tw93/Kami) | +419 | 3444 |
| 33 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +403 | 23491 |
| 34 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +401 | 24925 |
| 35 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +394 | 13114 |
| 36 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +372 | 18948 |
| 37 | [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt) | +359 | 4164 |
| 38 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +357 | 22005 |
| 39 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +354 | 10360 |
| 40 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +335 | 40827 |
| 41 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +326 | 18796 |
| 42 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +325 | 6891 |
| 43 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +325 | 14891 |
| 44 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +323 | 8716 |
| 45 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +314 | 11539 |
| 46 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +313 | 8303 |
| 47 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +308 | 30057 |
| 48 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +301 | 13248 |
| 49 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +298 | 26054 |
| 50 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +288 | 21606 |
| 51 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +286 | 49787 |
| 52 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +286 | 48220 |
| 53 | [BasedHardware/omi](https://github.com/BasedHardware/omi) | +282 | 12213 |
| 54 | [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | +275 | 5124 |
| 55 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +273 | 10574 |
| 56 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +269 | 24518 |
| 57 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +263 | 16655 |
| 58 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +258 | 15738 |
| 59 | [open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) | +258 | 13646 |
| 60 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +257 | 56668 |
| 61 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +251 | 41936 |
| 62 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +251 | 28927 |
| 63 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +251 | 32836 |
| 64 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +248 | 3587 |
| 65 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +245 | 6948 |
| 66 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +240 | 32922 |
| 67 | [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon) | +239 | 40436 |
| 68 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +239 | 43042 |
| 69 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +238 | 36907 |
| 70 | [PerryTS/perry](https://github.com/PerryTS/perry) | +237 | 1755 |
| 71 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +231 | 3850 |
| 72 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +224 | 24042 |
| 73 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +222 | 4368 |
| 74 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +219 | 8529 |
| 75 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +217 | 19785 |
| 76 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +215 | 26569 |
| 77 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +211 | 5262 |
| 78 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +208 | 3335 |
| 79 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +207 | 41258 |
| 80 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +206 | 31407 |
| 81 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +205 | 22049 |
| 82 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +204 | 29122 |
| 83 | [PostHog/posthog](https://github.com/PostHog/posthog) | +202 | 31767 |
| 84 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +201 | 29042 |
| 85 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +196 | 31607 |
| 86 | [edwardkim/rhwp](https://github.com/edwardkim/rhwp) | +195 | 2599 |
| 87 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +190 | 35230 |
| 88 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | +183 | 16510 |
| 89 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +182 | 6982 |
| 90 | [vercel-labs/skills](https://github.com/vercel-labs/skills) | +182 | 16130 |
| 91 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +181 | 4114 |
| 92 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +181 | 16009 |
| 93 | [VoltAgent/awesome-claude-design](https://github.com/VoltAgent/awesome-claude-design) | +174 | 1663 |
| 94 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +170 | 16179 |
| 95 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +169 | 5758 |
| 96 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +165 | 1899 |
| 97 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +163 | 32662 |
| 98 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +161 | 1857 |
| 99 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +151 | 33544 |
| 100 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +150 | 10854 |
| 101 | [OranAi-Ltd/oransim](https://github.com/OranAi-Ltd/oransim) | +146 | 1030 |
| 102 | [leigest519/OpenGame](https://github.com/leigest519/OpenGame) | +143 | 1229 |
| 103 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +143 | 12817 |
| 104 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +141 | 4613 |
| 105 | [the-hidden-fish/advisor-ledger](https://github.com/the-hidden-fish/advisor-ledger) | +141 | 1082 |
| 106 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +141 | 28551 |
| 107 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +137 | 38825 |
| 108 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +136 | 25542 |
| 109 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +135 | 2173 |
| 110 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +135 | 1373 |
| 111 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +135 | 36799 |
| 112 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +131 | 1157 |
| 113 | [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | +131 | 1649 |
| 114 | [jundot/omlx](https://github.com/jundot/omlx) | +130 | 11609 |
| 115 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +128 | 861 |
| 116 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +126 | 11288 |
| 117 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +126 | 44545 |
| 118 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +122 | 687 |
| 119 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +121 | 40941 |
| 120 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +120 | 6127 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25369 | 188561 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18031 | 118149 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +12413 | 90355 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12282 | 65942 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +9352 | 51199 |
| 6 | [obra/superpowers](https://github.com/obra/superpowers) | +8561 | 60312 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7897 | 49787 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +7741 | 47092 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7172 | 39965 |
| 10 | [chenglou/pretext](https://github.com/chenglou/pretext) | +6901 | 45406 |
| 11 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +5921 | 35417 |
| 12 | [garrytan/gstack](https://github.com/garrytan/gstack) | +5485 | 83967 |
| 13 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5164 | 69674 |
| 14 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +5156 | 224760 |
| 15 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4696 | 24518 |
| 16 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4519 | 32922 |
| 17 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4442 | 30678 |
| 18 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +4270 | 29122 |
| 19 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4218 | 23650 |
| 20 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +4150 | 59062 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +4148 | 87319 |
| 22 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4141 | 26054 |
| 23 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +4120 | 48220 |
| 24 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3627 | 21416 |
| 25 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3538 | 36051 |
| 26 | [anthropics/skills](https://github.com/anthropics/skills) | +3404 | 74774 |
| 27 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +3336 | 76832 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3223 | 109881 |
| 29 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +3121 | 34148 |
| 30 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2978 | 31407 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +2852 | 51866 |
| 32 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2789 | 16967 |
| 33 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2747 | 41936 |
| 34 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2726 | 16655 |
| 35 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2690 | 56668 |
| 36 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +2644 | 63872 |
| 37 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2547 | 14891 |
| 38 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2495 | 16179 |
| 39 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2454 | 57553 |
| 40 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2424 | 57538 |
| 41 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +2375 | 24042 |
| 42 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2333 | 11288 |
| 43 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2311 | 85286 |
| 44 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2180 | 11539 |
| 45 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2094 | 18308 |
| 46 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2079 | 22005 |
| 47 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +2050 | 12590 |
| 48 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2042 | 15442 |
| 49 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2030 | 40609 |
| 50 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +2025 | 28551 |
| 51 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +1977 | 11244 |
| 52 | [mattpocock/skills](https://github.com/mattpocock/skills) | +1960 | 22971 |
| 53 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1933 | 31098 |
| 54 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1870 | 79656 |
| 55 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1867 | 33878 |
| 56 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +1866 | 30057 |
| 57 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1853 | 30590 |
| 58 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1844 | 21606 |
| 59 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1831 | 16009 |
| 60 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1826 | 10057 |
| 61 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1737 | 13248 |
| 62 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1714 | 17389 |
| 63 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +1693 | 13273 |
| 64 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1652 | 26569 |
| 65 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1648 | 19362 |
| 66 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1553 | 16238 |
| 67 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1546 | 25597 |
| 68 | [openai/codex](https://github.com/openai/codex) | +1540 | 61744 |
| 69 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1528 | 32662 |
| 70 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1478 | 55070 |
| 71 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1452 | 18641 |
| 72 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1450 | 28927 |
| 73 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1437 | 73135 |
| 74 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1429 | 40827 |
| 75 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1423 | 11738 |
| 76 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1413 | 23491 |
| 77 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1408 | 6578 |
| 78 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1395 | 8716 |
| 79 | [github/spec-kit](https://github.com/github/spec-kit) | +1394 | 71722 |
| 80 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1384 | 98536 |
| 81 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1380 | 52721 |
| 82 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1350 | 37330 |
| 83 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1345 | 45886 |
| 84 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1330 | 41258 |
| 85 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1322 | 6689 |
| 86 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1320 | 22091 |
| 87 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1299 | 24925 |
| 88 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1299 | 22050 |
| 89 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1284 | 95754 |
| 90 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1276 | 43042 |
| 91 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1265 | 35230 |
| 92 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1259 | 10574 |
| 93 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +1243 | 18301 |
| 94 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | +1195 | 50350 |
| 95 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1194 | 13114 |
| 96 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1178 | 7128 |
| 97 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +1165 | 20760 |
| 98 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1132 | 15738 |
| 99 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +998 | 6127 |
| 100 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +991 | 8767 |
| 101 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +989 | 78902 |
| 102 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +980 | 7353 |
| 103 | [ChinaSiro/claude-code-sourcemap](https://github.com/ChinaSiro/claude-code-sourcemap) | +962 | 9026 |
| 104 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +959 | 31607 |
| 105 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +954 | 38825 |
| 106 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +949 | 12817 |
| 107 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +922 | 8303 |
| 108 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +895 | 11938 |
| 109 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +889 | 6308 |
| 110 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +889 | 6567 |
| 111 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +860 | 25296 |
| 112 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +856 | 4613 |
| 113 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +851 | 6948 |
| 114 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +835 | 52700 |
| 115 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +834 | 47122 |
| 116 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +834 | 4816 |
| 117 | [google/magika](https://github.com/google/magika) | +818 | 16741 |
| 118 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +811 | 4325 |
| 119 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +759 | 5732 |
| 120 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +747 | 5262 |
| 121 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +747 | 5612 |
| 122 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +737 | 21804 |
| 123 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +737 | 4134 |
| 124 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +734 | 4046 |
| 125 | [jundot/omlx](https://github.com/jundot/omlx) | +730 | 11609 |
| 126 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +729 | 9577 |
| 127 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +727 | 11868 |
| 128 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +724 | 40941 |
| 129 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +720 | 4368 |
| 130 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +720 | 30232 |
| 131 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +714 | 39841 |
| 132 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +713 | 10854 |
| 133 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +657 | 34301 |
| 134 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +650 | 54903 |
| 135 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +629 | 31270 |
| 136 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +614 | 36799 |
| 137 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +604 | 23088 |
| 138 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +602 | 18796 |
| 139 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +592 | 11535 |
| 140 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +587 | 3017 |
| 141 | [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) | +587 | 24361 |
| 142 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +556 | 19473 |
| 143 | [eze-is/web-access](https://github.com/eze-is/web-access) | +552 | 5697 |
| 144 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +550 | 3509 |
| 145 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +546 | 3175 |
| 146 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +541 | 37564 |
| 147 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +540 | 17950 |
| 148 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +532 | 7551 |
| 149 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +530 | 2590 |
| 150 | [zc-zhangchen/any-auto-register](https://github.com/zc-zhangchen/any-auto-register) | +524 | 3186 |
| 151 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +519 | 30723 |
| 152 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +514 | 17230 |
| 153 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +504 | 24700 |
| 154 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +500 | 25801 |
| 155 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +495 | 2859 |
| 156 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +491 | 4832 |
| 157 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +489 | 30458 |
| 158 | [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | +480 | 11674 |
| 159 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +480 | 2648 |
| 160 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | +474 | 44545 |
| 161 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +471 | 3850 |
| 162 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +467 | 3335 |
| 163 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +466 | 6891 |
| 164 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +449 | 2355 |
| 165 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +441 | 11606 |
| 166 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +436 | 2542 |
| 167 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +433 | 6735 |
| 168 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +414 | 3222 |
| 169 | [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | +410 | 15963 |
| 170 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +408 | 36907 |
| 171 | [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | +406 | 2186 |
| 172 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +403 | 9546 |
| 173 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +402 | 6982 |
| 174 | [magnum6actual/flipoff](https://github.com/magnum6actual/flipoff) | +399 | 2820 |
| 175 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +391 | 24086 |
| 176 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +386 | 19666 |
| 177 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +385 | 3317 |
| 178 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +376 | 2286 |
| 179 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +371 | 2231 |
| 180 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +361 | 3480 |
| 181 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +338 | 25753 |
| 182 | [floci-io/floci](https://github.com/floci-io/floci) | +333 | 4192 |
| 183 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +330 | 5758 |
| 184 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +319 | 12513 |
| 185 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +318 | 3279 |
| 186 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +307 | 5795 |
| 187 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +307 | 9095 |
| 188 | [decolua/9router](https://github.com/decolua/9router) | +295 | 3167 |
| 189 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +280 | 3092 |
| 190 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +270 | 36103 |
| 191 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +256 | 7425 |
| 192 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +250 | 1861 |
| 193 | [88lin/video_vip](https://github.com/88lin/video_vip) | +230 | 1532 |
| 194 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +228 | 26323 |
| 195 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +209 | 2790 |
| 196 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +207 | 7330 |
| 197 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +207 | 11334 |
| 198 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +207 | 15856 |
| 199 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +196 | 2696 |
| 200 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +193 | 33712 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +190 | 8788 |
| 202 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +187 | 4233 |
| 203 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +187 | 5543 |
| 204 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +183 | 7953 |
| 205 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +182 | 3112 |
| 206 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +179 | 13049 |
| 207 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +172 | 2541 |
| 208 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +171 | 563 |
| 209 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 814 |
| 210 | [usebruno/bruno](https://github.com/usebruno/bruno) | +161 | 41086 |
| 211 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +159 | 3987 |
| 212 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +155 | 1011 |
| 213 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +153 | 1526 |
| 214 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +151 | 22414 |
| 215 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +149 | 40265 |
| 216 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +142 | 1678 |
| 217 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +140 | 35473 |
| 218 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +134 | 23597 |
| 219 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +127 | 760 |
| 220 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +125 | 1773 |
| 221 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +123 | 29762 |
| 222 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +121 | 700 |
| 223 | [tiagozip/cap](https://github.com/tiagozip/cap) | +120 | 5935 |
| 224 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 609 |
| 225 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +120 | 5450 |
| 226 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +120 | 14345 |
| 227 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +119 | 829 |
| 228 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +118 | 29760 |
| 229 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +113 | 7358 |
| 230 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +111 | 19210 |
| 231 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +111 | 10904 |
| 232 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +110 | 39596 |
| 233 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +107 | 586 |
| 234 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +106 | 26857 |
| 235 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +106 | 6785 |
| 236 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +102 | 638 |
| 237 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +102 | 33000 |
| 238 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +101 | 2022 |
| 239 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +100 | 759 |
| 240 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +100 | 1017 |
| 241 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +98 | 12921 |
| 242 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +97 | 643 |
| 243 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +97 | 641 |
| 244 | [mumuyanjian-ui/caregiver](https://github.com/mumuyanjian-ui/caregiver) | +96 | 289 |
| 245 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +96 | 1395 |
| 246 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1439 |
| 247 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +94 | 1855 |
| 248 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +92 | 1924 |
| 249 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +91 | 1182 |
| 250 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +90 | 1820 |
| 251 | [crimera/piko](https://github.com/crimera/piko) | +90 | 3347 |
| 252 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +88 | 611 |
| 253 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +88 | 461 |
| 254 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +88 | 1083 |
| 255 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +88 | 3088 |
| 256 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +87 | 2361 |
| 257 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +86 | 549 |
| 258 | [openmemind/memind](https://github.com/openmemind/memind) | +86 | 549 |
| 259 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +85 | 468 |
| 260 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +84 | 3864 |
| 261 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +84 | 633 |
| 262 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +83 | 4070 |
| 263 | [openrocket/openrocket](https://github.com/openrocket/openrocket) | +83 | 2770 |
| 264 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +82 | 470 |
| 265 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +82 | 733 |
| 266 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +82 | 424 |
| 267 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +81 | 48784 |
| 268 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1765 |
| 269 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +78 | 45263 |
| 270 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +76 | 685 |
| 271 | [robinebers/openusage](https://github.com/robinebers/openusage) | +76 | 2041 |
| 272 | [zylos-ai/zylos-core](https://github.com/zylos-ai/zylos-core) | +76 | 1166 |
| 273 | [6551Team/claude-code-design-guide](https://github.com/6551Team/claude-code-design-guide) | +76 | 767 |
| 274 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +75 | 1519 |
| 275 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +74 | 2739 |
| 276 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +74 | 3678 |
| 277 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +71 | 972 |
| 278 | [microg/GmsCore](https://github.com/microg/GmsCore) | +71 | 13064 |
| 279 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +66 | 9386 |
| 280 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +66 | 27383 |
| 281 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +65 | 378 |
| 282 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +64 | 599 |
| 283 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +62 | 11766 |
| 284 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +60 | 7327 |
| 285 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +58 | 1700 |
| 286 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +57 | 37313 |
| 287 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +56 | 28969 |
| 288 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +55 | 329 |
| 289 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +52 | 1872 |
| 290 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +50 | 31476 |
| 291 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +49 | 4914 |
| 292 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1794 |
| 293 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +47 | 464 |
| 294 | [risin42/NagramX](https://github.com/risin42/NagramX) | +44 | 1727 |
| 295 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +42 | 224 |
| 296 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +42 | 8588 |
| 297 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +41 | 589 |
| 298 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +39 | 230 |
| 299 | [is-a-dev/register](https://github.com/is-a-dev/register) | +38 | 10182 |
| 300 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
