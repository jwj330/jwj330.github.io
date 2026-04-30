---
title: "2026-04-30 GitHub增长趋势报告"
description: "1.warp+626 2.skills+611 3.symphony+95 4.caveman+88 5.graphify+76"
date: 2026-04-30T21:03:49+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-04-30 21:03:49

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
        'daily': {"categories": ["heygen-com/hyperframes", "mattpocock/sandcastle", "pbakaus/impeccable", "hugohe3/ppt-master", "Fincept-Corporation/FinceptTerminal", "ComposioHQ/awesome-codex-skills", "KKKKhazix/khazix-skills", "abhigyanpatwari/GitNexus", "1jehuang/jcode", "AIDC-AI/Pixelle-Video", "addyosmani/agent-skills", "soxoj/maigret", "Alishahryar1/free-claude-code", "ZhuLinsen/daily_stock_analysis", "microsoft/VibeVoice", "safishamsi/graphify", "JuliusBrussee/caveman", "openai/symphony", "mattpocock/skills", "warpdotdev/warp"], "data": [35, 38, 39, 41, 43, 46, 47, 49, 49, 49, 52, 59, 70, 70, 73, 76, 88, 95, 611, 626]},
        'weekly': {"categories": ["heygen-com/hyperframes", "badlogic/pi-mono", "Anil-matcha/Open-Generative-AI", "Fincept-Corporation/FinceptTerminal", "microsoft/VibeVoice", "op7418/guizang-ppt-skill", "safishamsi/graphify", "abhigyanpatwari/GitNexus", "addyosmani/agent-skills", "JuliusBrussee/caveman", "rtk-ai/rtk", "farion1231/cc-switch", "garrytan/gstack", "refactoringhq/tolaria", "Z4nzu/hackingtool", "warpdotdev/warp", "NousResearch/hermes-agent", "Alishahryar1/free-claude-code", "forrestchang/andrej-karpathy-skills", "mattpocock/skills"], "data": [501, 558, 562, 617, 630, 654, 672, 674, 689, 768, 769, 801, 834, 1224, 1334, 1738, 1838, 2221, 3372, 3618]},
        'monthly': {"categories": ["Yeachan-Heo/oh-my-codex", "thedotmack/claude-mem", "chenglou/pretext", "siddharthvaddem/openscreen", "addyosmani/agent-skills", "mattpocock/skills", "Gitlawb/openclaude", "garrytan/gstack", "openclaw/openclaw", "anthropics/claude-code", "safishamsi/graphify", "santifer/career-ops", "obra/superpowers", "MemPalace/mempalace", "JuliusBrussee/caveman", "affaan-m/everything-claude-code", "VoltAgent/awesome-design-md", "forrestchang/andrej-karpathy-skills", "NousResearch/hermes-agent", "ultraworkers/claw-code"], "data": [4214, 4378, 4462, 4603, 4637, 4650, 4776, 4824, 4918, 5094, 6323, 7324, 7702, 7996, 8126, 8519, 12602, 13824, 18374, 25523]}
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
| 1 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +626 | 48879 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | +611 | 49046 |
| 3 | [openai/symphony](https://github.com/openai/symphony) | +95 | 20007 |
| 4 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +88 | 51276 |
| 5 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +76 | 38979 |
| 6 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +73 | 46048 |
| 7 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +70 | 33454 |
| 8 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +70 | 19119 |
| 9 | [soxoj/maigret](https://github.com/soxoj/maigret) | +59 | 20766 |
| 10 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +52 | 26661 |
| 11 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +49 | 8393 |
| 12 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +49 | 1838 |
| 13 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +49 | 33739 |
| 14 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +47 | 7485 |
| 15 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +46 | 5183 |
| 16 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +43 | 18269 |
| 17 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +41 | 10036 |
| 18 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +39 | 23750 |
| 19 | [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | +38 | 2121 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +35 | 13347 |
| 21 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +34 | 3765 |
| 22 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +34 | 38938 |
| 23 | [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | +34 | 5541 |
| 24 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +33 | 43167 |
| 25 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +31 | 8809 |
| 26 | [caamer20/Telegram-Drive](https://github.com/caamer20/Telegram-Drive) | +30 | 1889 |
| 27 | [multica-ai/multica](https://github.com/multica-ai/multica) | +29 | 23189 |
| 28 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +29 | 49869 |
| 29 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +28 | 42001 |
| 30 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +26 | 2929 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | +3618 | 49047 |
| 2 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +3372 | 102388 |
| 3 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2221 | 19119 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +1838 | 126618 |
| 5 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1738 | 48879 |
| 6 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1334 | 55070 |
| 7 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1224 | 8524 |
| 8 | [garrytan/gstack](https://github.com/garrytan/gstack) | +834 | 87326 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +801 | 56480 |
| 10 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +769 | 38938 |
| 11 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +768 | 51277 |
| 12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +689 | 26661 |
| 13 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +674 | 33739 |
| 14 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +672 | 38980 |
| 15 | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | +654 | 4379 |
| 16 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +630 | 46048 |
| 17 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +617 | 18269 |
| 18 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +562 | 10396 |
| 19 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +558 | 43167 |
| 20 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +501 | 13347 |
| 21 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +479 | 5183 |
| 22 | [YouMind-OpenLab/awesome-gpt-image-2](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) | +469 | 3983 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +412 | 23189 |
| 24 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +395 | 8809 |
| 25 | [openai/symphony](https://github.com/openai/symphony) | +379 | 20007 |
| 26 | [santifer/career-ops](https://github.com/santifer/career-ops) | +351 | 41229 |
| 27 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +350 | 25827 |
| 28 | [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | +343 | 10420 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +320 | 10036 |
| 30 | [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) | +308 | 5204 |
| 31 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +302 | 16963 |
| 32 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +301 | 8467 |
| 33 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | +293 | 11481 |
| 34 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +291 | 16540 |
| 35 | [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) | +287 | 4823 |
| 36 | [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | +286 | 3765 |
| 37 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +285 | 42001 |
| 38 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +283 | 33454 |
| 39 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +282 | 49869 |
| 40 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +281 | 2485 |
| 41 | [PostHog/posthog](https://github.com/PostHog/posthog) | +277 | 31767 |
| 42 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +268 | 30535 |
| 43 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | +267 | 19625 |
| 44 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +265 | 22703 |
| 45 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +248 | 14190 |
| 46 | [victorchen96/deepseek_v4_rolepaly_instruct](https://github.com/victorchen96/deepseek_v4_rolepaly_instruct) | +248 | 1563 |
| 47 | [trycua/cua](https://github.com/trycua/cua) | +246 | 15385 |
| 48 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +242 | 27043 |
| 49 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +240 | 12475 |
| 50 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +234 | 23750 |
| 51 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +233 | 8393 |
| 52 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +228 | 57620 |
| 53 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +227 | 22256 |
| 54 | [gastownhall/beads](https://github.com/gastownhall/beads) | +226 | 22855 |
| 55 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +221 | 26491 |
| 56 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | +221 | 32836 |
| 57 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +220 | 3888 |
| 58 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +220 | 30032 |
| 59 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +211 | 27788 |
| 60 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | +207 | 29990 |
| 61 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +204 | 19451 |
| 62 | [penpot/penpot](https://github.com/penpot/penpot) | +204 | 44370 |
| 63 | [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | +203 | 2929 |
| 64 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +203 | 24155 |
| 65 | [0x0funky/agent-sprite-forge](https://github.com/0x0funky/agent-sprite-forge) | +198 | 1381 |
| 66 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +195 | 7362 |
| 67 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +194 | 33830 |
| 68 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +193 | 44415 |
| 69 | [iamgio/quarkdown](https://github.com/iamgio/quarkdown) | +191 | 12984 |
| 70 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +189 | 4053 |
| 71 | [blader/humanizer](https://github.com/blader/humanizer) | +188 | 16644 |
| 72 | [tiagozip/cap](https://github.com/tiagozip/cap) | +185 | 6168 |
| 73 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +184 | 5132 |
| 74 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +184 | 42042 |
| 75 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +183 | 25212 |
| 76 | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | +183 | 20614 |
| 77 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +182 | 8377 |
| 78 | [getagentseal/codeburn](https://github.com/getagentseal/codeburn) | +182 | 4698 |
| 79 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +177 | 14277 |
| 80 | [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | +175 | 1514 |
| 81 | [jackwener/opencli](https://github.com/jackwener/opencli) | +173 | 18333 |
| 82 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +171 | 7485 |
| 83 | [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | +170 | 9245 |
| 84 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +165 | 32082 |
| 85 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +161 | 35843 |
| 86 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +160 | 5978 |
| 87 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +160 | 3896 |
| 88 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +160 | 16784 |
| 89 | [masterking32/MasterHttpRelayVPN](https://github.com/masterking32/MasterHttpRelayVPN) | +158 | 1842 |
| 90 | [basketikun/chatgpt2api](https://github.com/basketikun/chatgpt2api) | +154 | 1699 |
| 91 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | +153 | 34143 |
| 92 | [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) | +150 | 935 |
| 93 | [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | +150 | 6848 |
| 94 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +149 | 5359 |
| 95 | [wuyoscar/gpt_image_2_skill](https://github.com/wuyoscar/gpt_image_2_skill) | +148 | 1085 |
| 96 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +146 | 1225 |
| 97 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +144 | 11539 |
| 98 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +143 | 18812 |
| 99 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +143 | 12560 |
| 100 | [zhom/donutbrowser](https://github.com/zhom/donutbrowser) | +143 | 2226 |
| 101 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +142 | 25612 |
| 102 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +136 | 39345 |
| 103 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +135 | 2190 |
| 104 | [hydropix/TranslateBooksWithLLMs](https://github.com/hydropix/TranslateBooksWithLLMs) | +134 | 1378 |
| 105 | [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | +133 | 2774 |
| 106 | [deepseek-ai/TileKernels](https://github.com/deepseek-ai/TileKernels) | +131 | 1374 |
| 107 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +128 | 30914 |
| 108 | [wxyhgk/retain-pdf](https://github.com/wxyhgk/retain-pdf) | +127 | 1274 |
| 109 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +119 | 13306 |
| 110 | [jundot/omlx](https://github.com/jundot/omlx) | +118 | 11988 |
| 111 | [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | +118 | 1966 |
| 112 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +117 | 36799 |
| 113 | [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | +112 | 669 |
| 114 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +110 | 5065 |
| 115 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +107 | 41403 |
| 116 | [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image) | +106 | 974 |
| 117 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +104 | 24404 |
| 118 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +103 | 31811 |
| 119 | [alexzhang13/rlm](https://github.com/alexzhang13/rlm) | +103 | 4113 |
| 120 | [google-research/timesfm](https://github.com/google-research/timesfm) | +100 | 19093 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | +25523 | 189403 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | +18374 | 126618 |
| 3 | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | +13824 | 102388 |
| 4 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | +12602 | 68712 |
| 5 | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | +8519 | 51199 |
| 6 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | +8126 | 51277 |
| 7 | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | +7996 | 50528 |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) | +7702 | 60312 |
| 9 | [santifer/career-ops](https://github.com/santifer/career-ops) | +7324 | 41230 |
| 10 | [safishamsi/graphify](https://github.com/safishamsi/graphify) | +6323 | 38980 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | +5094 | 69674 |
| 12 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | +4918 | 224760 |
| 13 | [garrytan/gstack](https://github.com/garrytan/gstack) | +4824 | 87326 |
| 14 | [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) | +4776 | 25212 |
| 15 | [mattpocock/skills](https://github.com/mattpocock/skills) | +4650 | 49047 |
| 16 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | +4637 | 26661 |
| 17 | [siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen) | +4603 | 33830 |
| 18 | [chenglou/pretext](https://github.com/chenglou/pretext) | +4462 | 45906 |
| 19 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | +4378 | 30678 |
| 20 | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | +4214 | 27043 |
| 21 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | +3965 | 89557 |
| 22 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | +3888 | 49869 |
| 23 | [multica-ai/multica](https://github.com/multica-ai/multica) | +3826 | 23189 |
| 24 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | +3644 | 38938 |
| 25 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +3410 | 30535 |
| 26 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | +3357 | 61001 |
| 27 | [anthropics/skills](https://github.com/anthropics/skills) | +3261 | 74774 |
| 28 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | +3209 | 109881 |
| 29 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | +3074 | 56480 |
| 30 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | +2863 | 78115 |
| 31 | [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) | +2834 | 17333 |
| 32 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | +2829 | 34148 |
| 33 | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | +2771 | 17061 |
| 34 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +2736 | 16540 |
| 35 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +2578 | 19119 |
| 36 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | +2572 | 46048 |
| 37 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +2557 | 16898 |
| 38 | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | +2477 | 32082 |
| 39 | [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) | +2377 | 11653 |
| 40 | [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | +2373 | 18269 |
| 41 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | +2284 | 12475 |
| 42 | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | +2249 | 57620 |
| 43 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +2224 | 13347 |
| 44 | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | +2208 | 58483 |
| 45 | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | +2193 | 43168 |
| 46 | [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | +2167 | 59008 |
| 47 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | +2164 | 33739 |
| 48 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +2164 | 22703 |
| 49 | [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) | +2153 | 18812 |
| 50 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | +2082 | 85286 |
| 51 | [aaif-goose/goose](https://github.com/aaif-goose/goose) | +1936 | 31098 |
| 52 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | +1931 | 22256 |
| 53 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +1862 | 16285 |
| 54 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | +1850 | 30590 |
| 55 | [emdash-cms/emdash](https://github.com/emdash-cms/emdash) | +1844 | 10180 |
| 56 | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | +1839 | 55070 |
| 57 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | +1823 | 64370 |
| 58 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | +1813 | 33878 |
| 59 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +1796 | 14277 |
| 60 | [warpdotdev/warp](https://github.com/warpdotdev/warp) | +1784 | 48879 |
| 61 | [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx) | +1771 | 28804 |
| 62 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | +1633 | 27788 |
| 63 | [jackwener/opencli](https://github.com/jackwener/opencli) | +1616 | 18333 |
| 64 | [openai/codex](https://github.com/openai/codex) | +1580 | 61744 |
| 65 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | +1562 | 25835 |
| 66 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +1518 | 19805 |
| 67 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +1482 | 24155 |
| 68 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | +1480 | 73135 |
| 69 | [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | +1457 | 42001 |
| 70 | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | +1451 | 9204 |
| 71 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | +1450 | 24404 |
| 72 | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | +1439 | 30032 |
| 73 | [google-research/timesfm](https://github.com/google-research/timesfm) | +1428 | 19093 |
| 74 | [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | +1426 | 11767 |
| 75 | [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | +1426 | 6756 |
| 76 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | +1401 | 16784 |
| 77 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | +1400 | 98536 |
| 78 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | +1349 | 45886 |
| 79 | [github/spec-kit](https://github.com/github/spec-kit) | +1343 | 71722 |
| 80 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +1342 | 33108 |
| 81 | [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | +1341 | 22352 |
| 82 | [browser-use/browser-harness](https://github.com/browser-use/browser-harness) | +1340 | 8810 |
| 83 | [ultraworkers/claw-code-parity](https://github.com/ultraworkers/claw-code-parity) | +1324 | 6686 |
| 84 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | +1310 | 23750 |
| 85 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | +1309 | 95754 |
| 86 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | +1295 | 37330 |
| 87 | [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) | +1290 | 8524 |
| 88 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +1283 | 25827 |
| 89 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | +1259 | 10903 |
| 90 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +1256 | 13475 |
| 91 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | +1251 | 44415 |
| 92 | [koala73/worldmonitor](https://github.com/koala73/worldmonitor) | +1246 | 53104 |
| 93 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +1226 | 16963 |
| 94 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | +1216 | 14190 |
| 95 | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | +1172 | 35843 |
| 96 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | +1167 | 42042 |
| 97 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | +1166 | 10396 |
| 98 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | +1164 | 79656 |
| 99 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +1131 | 7485 |
| 100 | [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent) | +1100 | 8467 |
| 101 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +1033 | 10036 |
| 102 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | +1028 | 78902 |
| 103 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +996 | 21302 |
| 104 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +988 | 33454 |
| 105 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | +916 | 39345 |
| 106 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +907 | 5065 |
| 107 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | +900 | 25612 |
| 108 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +889 | 5359 |
| 109 | [EvoMap/evolver](https://github.com/EvoMap/evolver) | +876 | 7126 |
| 110 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +864 | 13306 |
| 111 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | +862 | 18563 |
| 112 | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | +860 | 47122 |
| 113 | [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) | +847 | 4940 |
| 114 | [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) | +838 | 4530 |
| 115 | [google/magika](https://github.com/google/magika) | +834 | 16838 |
| 116 | [TheTom/turboquant_plus](https://github.com/TheTom/turboquant_plus) | +832 | 6645 |
| 117 | [unslothai/unsloth](https://github.com/unslothai/unsloth) | +826 | 52700 |
| 118 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +805 | 5132 |
| 119 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +782 | 5978 |
| 120 | [tvytlx/ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive) | +751 | 5641 |
| 121 | [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | +739 | 4098 |
| 122 | [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | +733 | 11539 |
| 123 | [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex) | +732 | 9715 |
| 124 | [QuipNetwork/quip-protocol](https://github.com/QuipNetwork/quip-protocol) | +720 | 11959 |
| 125 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +717 | 3888 |
| 126 | [jundot/omlx](https://github.com/jundot/omlx) | +717 | 11988 |
| 127 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | +690 | 22066 |
| 128 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +681 | 12214 |
| 129 | [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | +676 | 41403 |
| 130 | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) | +665 | 19451 |
| 131 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +650 | 4294 |
| 132 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | +649 | 39841 |
| 133 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | +648 | 54903 |
| 134 | [github/awesome-copilot](https://github.com/github/awesome-copilot) | +614 | 31811 |
| 135 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | +608 | 34621 |
| 136 | [elebumm/RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot) | +596 | 11547 |
| 137 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +593 | 8393 |
| 138 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | +577 | 36799 |
| 139 | [aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID) | +564 | 3600 |
| 140 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +560 | 3296 |
| 141 | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | +547 | 5950 |
| 142 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +542 | 4053 |
| 143 | [sooryathejas/METATRON](https://github.com/sooryathejas/METATRON) | +539 | 2658 |
| 144 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | +534 | 5183 |
| 145 | [FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2) | +534 | 30317 |
| 146 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +529 | 23297 |
| 147 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +521 | 17627 |
| 148 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +518 | 19805 |
| 149 | [nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey) | +512 | 12560 |
| 150 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | +503 | 30914 |
| 151 | [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) | +502 | 2965 |
| 152 | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | +495 | 37564 |
| 153 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +494 | 18299 |
| 154 | [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | +485 | 26007 |
| 155 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +479 | 7836 |
| 156 | [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) | +474 | 25192 |
| 157 | [GetBindu/Bindu](https://github.com/GetBindu/Bindu) | +470 | 4992 |
| 158 | [eze-is/web-access](https://github.com/eze-is/web-access) | +465 | 5890 |
| 159 | [QLHazyCoder/codex-oauth-automation-extension](https://github.com/QLHazyCoder/codex-oauth-automation-extension) | +461 | 2724 |
| 160 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +460 | 2473 |
| 161 | [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | +449 | 31069 |
| 162 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +431 | 3551 |
| 163 | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | +429 | 26491 |
| 164 | [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | +429 | 3896 |
| 165 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +423 | 7362 |
| 166 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +421 | 2716 |
| 167 | [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | +416 | 36907 |
| 168 | [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | +407 | 2631 |
| 169 | [mnfst/awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | +404 | 4010 |
| 170 | [garinasset/leak-check](https://github.com/garinasset/leak-check) | +396 | 3026 |
| 171 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | +395 | 19995 |
| 172 | [maboloshi/github-chinese](https://github.com/maboloshi/github-chinese) | +393 | 24364 |
| 173 | [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | +388 | 6927 |
| 174 | [maillab/cloud-mail](https://github.com/maillab/cloud-mail) | +388 | 8377 |
| 175 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +379 | 9775 |
| 176 | [PostHog/posthog](https://github.com/PostHog/posthog) | +368 | 31767 |
| 177 | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | +365 | 2372 |
| 178 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +328 | 25983 |
| 179 | [PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon) | +327 | 3287 |
| 180 | [FlowElement-ai/m_flow](https://github.com/FlowElement-ai/m_flow) | +324 | 2272 |
| 181 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +320 | 3384 |
| 182 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +308 | 5965 |
| 183 | [liyupi/ai-guide](https://github.com/liyupi/ai-guide) | +305 | 12834 |
| 184 | [decolua/9router](https://github.com/decolua/9router) | +298 | 3407 |
| 185 | [floci-io/floci](https://github.com/floci-io/floci) | +298 | 4286 |
| 186 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +281 | 3590 |
| 187 | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | +264 | 36103 |
| 188 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | +257 | 26695 |
| 189 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +250 | 1990 |
| 190 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +239 | 9155 |
| 191 | [88lin/video_vip](https://github.com/88lin/video_vip) | +232 | 1584 |
| 192 | [tiagozip/cap](https://github.com/tiagozip/cap) | +206 | 6168 |
| 193 | [justlovemaki/AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API) | +206 | 7422 |
| 194 | [youhunwl/TVAPP](https://github.com/youhunwl/TVAPP) | +203 | 16002 |
| 195 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +191 | 2877 |
| 196 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +186 | 2851 |
| 197 | [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) | +185 | 33712 |
| 198 | [Wei-Shaw/claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service) | +183 | 11429 |
| 199 | [sgoudelis/ground-station](https://github.com/sgoudelis/ground-station) | +175 | 4251 |
| 200 | [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | +167 | 8034 |
| 201 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +166 | 8826 |
| 202 | [ComposioHQ/open-claude-cowork](https://github.com/ComposioHQ/open-claude-cowork) | +164 | 4037 |
| 203 | [LarsenCundric/port-whisperer](https://github.com/LarsenCundric/port-whisperer) | +162 | 825 |
| 204 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +161 | 1225 |
| 205 | [zarazhangrui/tab-out](https://github.com/zarazhangrui/tab-out) | +161 | 1094 |
| 206 | [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | +161 | 3194 |
| 207 | [iflytek/astronclaw-tutorial](https://github.com/iflytek/astronclaw-tutorial) | +161 | 578 |
| 208 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +159 | 5852 |
| 209 | [usebruno/bruno](https://github.com/usebruno/bruno) | +157 | 41086 |
| 210 | [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | +150 | 1608 |
| 211 | [qingchencloud/clawpanel](https://github.com/qingchencloud/clawpanel) | +148 | 2602 |
| 212 | [fspecii/ace-step-ui](https://github.com/fspecii/ace-step-ui) | +146 | 2190 |
| 213 | [4ian/GDevelop](https://github.com/4ian/GDevelop) | +145 | 22516 |
| 214 | [zen-browser/desktop](https://github.com/zen-browser/desktop) | +143 | 40265 |
| 215 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub) | +142 | 13129 |
| 216 | [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) | +142 | 35473 |
| 217 | [dwgx/WindsurfAPI](https://github.com/dwgx/WindsurfAPI) | +135 | 923 |
| 218 | [hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift) | +132 | 14587 |
| 219 | [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | +130 | 23681 |
| 220 | [gethomepage/homepage](https://github.com/gethomepage/homepage) | +128 | 29829 |
| 221 | [cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS) | +126 | 5577 |
| 222 | [Paidax01/math-curve-loaders](https://github.com/Paidax01/math-curve-loaders) | +125 | 726 |
| 223 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +124 | 1843 |
| 224 | [yuliskov/SmartTube](https://github.com/yuliskov/SmartTube) | +122 | 29871 |
| 225 | [clawplays/ospec](https://github.com/clawplays/ospec) | +120 | 611 |
| 226 | [hotheadhacker/no-as-a-service](https://github.com/hotheadhacker/no-as-a-service) | +119 | 7443 |
| 227 | [HeyPuter/puter](https://github.com/HeyPuter/puter) | +117 | 39596 |
| 228 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +116 | 1716 |
| 229 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +115 | 692 |
| 230 | [xifangczy/cat-catch](https://github.com/xifangczy/cat-catch) | +113 | 19282 |
| 231 | [loks666/get_jobs](https://github.com/loks666/get_jobs) | +110 | 6826 |
| 232 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +109 | 3385 |
| 233 | [CNCKitchen/stlTexturizer](https://github.com/CNCKitchen/stlTexturizer) | +105 | 507 |
| 234 | [assai-id/nemesis](https://github.com/assai-id/nemesis) | +104 | 690 |
| 235 | [she-llac/claude-counter](https://github.com/she-llac/claude-counter) | +103 | 1114 |
| 236 | [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | +103 | 2032 |
| 237 | [andrewjiang/palantir-for-family-trips](https://github.com/andrewjiang/palantir-for-family-trips) | +101 | 781 |
| 238 | [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | +101 | 26948 |
| 239 | [JingMatrix/Vector](https://github.com/JingMatrix/Vector) | +99 | 10965 |
| 240 | [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | +98 | 650 |
| 241 | [keycloak/keycloak](https://github.com/keycloak/keycloak) | +97 | 33000 |
| 242 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +96 | 1906 |
| 243 | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | +95 | 1496 |
| 244 | [fjb040911/ai-rules](https://github.com/fjb040911/ai-rules) | +95 | 761 |
| 245 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +95 | 524 |
| 246 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +93 | 13005 |
| 247 | [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | +91 | 1146 |
| 248 | [Creators-of-Aeronautics/Simulated-Project](https://github.com/Creators-of-Aeronautics/Simulated-Project) | +91 | 609 |
| 249 | [dbeaver/dbeaver](https://github.com/dbeaver/dbeaver) | +90 | 48784 |
| 250 | [pexoai/pexo-skills](https://github.com/pexoai/pexo-skills) | +89 | 800 |
| 251 | [zacdcook/openclaw-billing-proxy](https://github.com/zacdcook/openclaw-billing-proxy) | +89 | 468 |
| 252 | [xstongxue/best-skills](https://github.com/xstongxue/best-skills) | +89 | 1224 |
| 253 | [datawhalechina/hello-claw](https://github.com/datawhalechina/hello-claw) | +86 | 1888 |
| 254 | [oinone/oinone-pamirs](https://github.com/oinone/oinone-pamirs) | +85 | 2424 |
| 255 | [crimera/piko](https://github.com/crimera/piko) | +85 | 3394 |
| 256 | [openmemind/memind](https://github.com/openmemind/memind) | +84 | 588 |
| 257 | [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | +83 | 492 |
| 258 | [sligter/LandPPT](https://github.com/sligter/LandPPT) | +83 | 3132 |
| 259 | [S-Trespassing/claw-in-chrome](https://github.com/S-Trespassing/claw-in-chrome) | +83 | 434 |
| 260 | [foxhui/WebAI2API](https://github.com/foxhui/WebAI2API) | +82 | 733 |
| 261 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +82 | 1959 |
| 262 | [GargantuaX/gemini-watermark-remover](https://github.com/GargantuaX/gemini-watermark-remover) | +81 | 3934 |
| 263 | [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | +80 | 1583 |
| 264 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +79 | 1835 |
| 265 | [vkehfdl1/slides-grab](https://github.com/vkehfdl1/slides-grab) | +78 | 651 |
| 266 | [jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot) | +77 | 45263 |
| 267 | [robinebers/openusage](https://github.com/robinebers/openusage) | +75 | 2162 |
| 268 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +74 | 2805 |
| 269 | [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | +73 | 1430 |
| 270 | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | +72 | 1305 |
| 271 | [Kail-Fu/InterviewOS](https://github.com/Kail-Fu/InterviewOS) | +72 | 1015 |
| 272 | [PDFCraftTool/pdfcraft](https://github.com/PDFCraftTool/pdfcraft) | +71 | 4115 |
| 273 | [Silent1566/OmniBox-Spider](https://github.com/Silent1566/OmniBox-Spider) | +70 | 647 |
| 274 | [microg/GmsCore](https://github.com/microg/GmsCore) | +70 | 13107 |
| 275 | [monogram-android/monogram](https://github.com/monogram-android/monogram) | +69 | 650 |
| 276 | [devanshutak25/3d-resources](https://github.com/devanshutak25/3d-resources) | +65 | 468 |
| 277 | [Anuken/Mindustry](https://github.com/Anuken/Mindustry) | +64 | 27414 |
| 278 | [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | +63 | 9444 |
| 279 | [snehasishroy/leetcode-companywise-interview-questions](https://github.com/snehasishroy/leetcode-companywise-interview-questions) | +63 | 3731 |
| 280 | [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | +59 | 362 |
| 281 | [mruniquehacker/Knightbot-MD](https://github.com/mruniquehacker/Knightbot-MD) | +58 | 7352 |
| 282 | [DrKLO/Telegram](https://github.com/DrKLO/Telegram) | +57 | 28986 |
| 283 | [TeamNewPipe/NewPipe](https://github.com/TeamNewPipe/NewPipe) | +57 | 37313 |
| 284 | [V-IOLE-T/tab-harbor](https://github.com/V-IOLE-T/tab-harbor) | +56 | 353 |
| 285 | [researchxxl/syncthing-android](https://github.com/researchxxl/syncthing-android) | +56 | 1725 |
| 286 | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) | +55 | 11826 |
| 287 | [matevip/mateclaw](https://github.com/matevip/mateclaw) | +54 | 351 |
| 288 | [chaosblade-io/chaosblade-space-exploration](https://github.com/chaosblade-io/chaosblade-space-exploration) | +53 | 488 |
| 289 | [MarSeventh/CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | +52 | 4957 |
| 290 | [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) | +52 | 1914 |
| 291 | [spring-ai-alibaba/DataAgent](https://github.com/spring-ai-alibaba/DataAgent) | +49 | 1826 |
| 292 | [ryanhcode/sable](https://github.com/ryanhcode/sable) | +48 | 256 |
| 293 | [conductor-oss/conductor](https://github.com/conductor-oss/conductor) | +48 | 31476 |
| 294 | [risin42/NagramX](https://github.com/risin42/NagramX) | +45 | 1750 |
| 295 | [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | +43 | 5206 |
| 296 | [jobrunr/JavaClaw](https://github.com/jobrunr/JavaClaw) | +42 | 608 |
| 297 | [landingbj/LinkMind](https://github.com/landingbj/LinkMind) | +42 | 262 |
| 298 | [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | +39 | 8622 |
| 299 | [OpenAIPay/openaipay](https://github.com/OpenAIPay/openaipay) | +38 | 125 |
| 300 | [is-a-dev/register](https://github.com/is-a-dev/register) | +34 | 10200 |
