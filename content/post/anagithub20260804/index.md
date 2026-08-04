---
title: "2026-08-04 GitHub增长趋势报告"
description: "1.reverse-skill+7 2.qm+6 3.pdf-inspector+4 4.free-claude-code+3 5.OfficeCLI+3"
date: 2026-08-04T21:13:34+08:00
categories:
  - GitHub Trends
---

**生成时间**: 2026-08-04 21:13:34

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
        'daily': {"categories": ["aipoch/open-science", "agentscope-ai/QwenPaw", "tt-a1i/archify", "multica-ai/multica", "davidondrej/skills", "baidu/Unlimited-OCR", "syswonder/robonix", "xuchonglang/investing-for-beginners", "amap-cvlab/ABot-World", "huangruiteng/loopx", "zhulin025/Codex-QQ-Skin", "browser-use/video-use", "esengine/DeepSeek-Reasonix", "jamiepine/voicebox", "virgiliojr94/book-to-skill", "iOfficeAI/OfficeCLI", "Alishahryar1/free-claude-code", "firecrawl/pdf-inspector", "yc-software/qm", "zhaoxuya520/reverse-skill"], "data": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 6, 7]},
        'weekly': {"categories": ["bryanthaboi/gen1recomp", "digimata/quill", "bashalarmistalt/decimen-optical-transfer", "bradautomates/claude-video", "iOfficeAI/OfficeCLI", "andrewyng/openworker", "opengeos/GeoLibre", "1jehuang/jcode", "pascalorg/editor", "diegosouzapw/OmniRoute", "usestrix/strix", "ayghri/i-have-adhd", "stablyai/orca", "MoonshotAI/Kimi-K3", "zhaoxuya520/reverse-skill", "firecrawl/pdf-inspector", "virgiliojr94/book-to-skill", "block/buzz", "yc-software/qm", "openai/codex-security"], "data": [8, 8, 8, 9, 9, 9, 10, 10, 11, 11, 12, 14, 18, 18, 19, 20, 21, 22, 22, 26]},
        'monthly': {"categories": ["jamiepine/voicebox", "teamchong/pxpipe", "alibaba/page-agent", "emilkowalski/skills", "Fei-Away/Codex-Dream-Skin", "HKUDS/Vibe-Trading", "DeusData/codebase-memory-mcp", "block/buzz", "bradautomates/claude-video", "iOfficeAI/OfficeCLI", "calesthio/OpenMontage", "openai/codex-plugin-cc", "k1tbyte/Wand-Enhancer", "JustVugg/colibri", "herdrdev/herdr", "stablyai/orca", "usestrix/strix", "diegosouzapw/OmniRoute", "Zackriya-Solutions/meetily", "langchain-ai/openwiki"], "data": [55, 57, 59, 62, 64, 66, 67, 73, 74, 77, 78, 81, 89, 96, 97, 102, 110, 115, 121, 134]}
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
| 1 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +7 | 17737 |
| 2 | [yc-software/qm](https://github.com/yc-software/qm) | +6 | 11079 |
| 3 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +4 | 9851 |
| 4 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 44332 |
| 5 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +3 | 25369 |
| 6 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +3 | 16359 |
| 7 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +3 | 49124 |
| 8 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +3 | 30730 |
| 9 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 19231 |
| 10 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 391 |
| 11 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +2 | 1535 |
| 12 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +2 | 1649 |
| 13 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +2 | 3101 |
| 14 | [syswonder/robonix](https://github.com/syswonder/robonix) | +2 | 275 |
| 15 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +2 | 22063 |
| 16 | [davidondrej/skills](https://github.com/davidondrej/skills) | +2 | 3314 |
| 17 | [multica-ai/multica](https://github.com/multica-ai/multica) | +2 | 43912 |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +2 | 9124 |
| 19 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +2 | 32945 |
| 20 | [aipoch/open-science](https://github.com/aipoch/open-science) | +2 | 1542 |
| 21 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +2 | 18757 |
| 22 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +2 | 5039 |
| 23 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +1 | 15858 |
| 24 | [linuxhsj/openclaw-zero-token](https://github.com/linuxhsj/openclaw-zero-token) | +1 | 5102 |
| 25 | [shaharia-lab/slackcli](https://github.com/shaharia-lab/slackcli) | +1 | 106 |
| 26 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +1 | 1222 |
| 27 | [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) | +1 | 2883 |
| 28 | [facebook/astryx](https://github.com/facebook/astryx) | +1 | 11581 |
| 29 | [Coneja-Chibi/TunnelVision](https://github.com/Coneja-Chibi/TunnelVision) | +1 | 116 |
| 30 | [cognyai/claude-code-marketing-skills](https://github.com/cognyai/claude-code-marketing-skills) | +1 | 86 |


### 📅 本周 Top 120 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [openai/codex-security](https://github.com/openai/codex-security) | +26 | 8520 |
| 2 | [yc-software/qm](https://github.com/yc-software/qm) | +22 | 11079 |
| 3 | [block/buzz](https://github.com/block/buzz) | +22 | 22466 |
| 4 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +21 | 16359 |
| 5 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +20 | 9851 |
| 6 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +19 | 17738 |
| 7 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +18 | 8041 |
| 8 | [stablyai/orca](https://github.com/stablyai/orca) | +18 | 37364 |
| 9 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +14 | 16735 |
| 10 | [usestrix/strix](https://github.com/usestrix/strix) | +12 | 48211 |
| 11 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +11 | 39597 |
| 12 | [pascalorg/editor](https://github.com/pascalorg/editor) | +11 | 21032 |
| 13 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +10 | 15858 |
| 14 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +10 | 5373 |
| 15 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +9 | 12771 |
| 16 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +9 | 25369 |
| 17 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +9 | 13862 |
| 18 | [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | +8 | 4524 |
| 19 | [digimata/quill](https://github.com/digimata/quill) | +8 | 3668 |
| 20 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +8 | 1880 |
| 21 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +8 | 24862 |
| 22 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +7 | 22063 |
| 23 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +7 | 18757 |
| 24 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +7 | 32945 |
| 25 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +6 | 30730 |
| 26 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +6 | 28454 |
| 27 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +6 | 49124 |
| 28 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +6 | 22669 |
| 29 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +6 | 42998 |
| 30 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +6 | 24356 |
| 31 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +6 | 7532 |
| 32 | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | +6 | 3038 |
| 33 | [multica-ai/multica](https://github.com/multica-ai/multica) | +5 | 43912 |
| 34 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +5 | 21829 |
| 35 | [antirez/ds4](https://github.com/antirez/ds4) | +5 | 20554 |
| 36 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +5 | 7204 |
| 37 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +5 | 18813 |
| 38 | [different-ai/openwork](https://github.com/different-ai/openwork) | +5 | 20896 |
| 39 | [digimata/parrot](https://github.com/digimata/parrot) | +5 | 1113 |
| 40 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +5 | 3178 |
| 41 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +5 | 8573 |
| 42 | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | +4 | 1535 |
| 43 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +4 | 33309 |
| 44 | [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) | +4 | 13412 |
| 45 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +4 | 45923 |
| 46 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +4 | 6626 |
| 47 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +4 | 29609 |
| 48 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +4 | 3436 |
| 49 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +4 | 32394 |
| 50 | [WilonityLoader/Wilonity](https://github.com/WilonityLoader/Wilonity) | +4 | 0 |
| 51 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +4 | 4238 |
| 52 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +4 | 10370 |
| 53 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +3 | 44332 |
| 54 | [snekxs/openmouse](https://github.com/snekxs/openmouse) | +3 | 769 |
| 55 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +3 | 45102 |
| 56 | [decolua/9router](https://github.com/decolua/9router) | +3 | 24657 |
| 57 | [browser-use/video-use](https://github.com/browser-use/video-use) | +3 | 19231 |
| 58 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +3 | 8309 |
| 59 | [DramaticShape/DramaticShapeVoxelMod](https://github.com/DramaticShape/DramaticShapeVoxelMod) | +3 | 865 |
| 60 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +3 | 1675 |
| 61 | [tytsxai/IDM-Activation-Script-Chinese](https://github.com/tytsxai/IDM-Activation-Script-Chinese) | +3 | 1476 |
| 62 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +3 | 14242 |
| 63 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +3 | 5039 |
| 64 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +3 | 7782 |
| 65 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +3 | 27803 |
| 66 | [aipoch/open-science](https://github.com/aipoch/open-science) | +3 | 1542 |
| 67 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +3 | 5010 |
| 68 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +3 | 9112 |
| 69 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +3 | 9058 |
| 70 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +3 | 6998 |
| 71 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +3 | 37455 |
| 72 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +3 | 13062 |
| 73 | [reflex-dev/xy](https://github.com/reflex-dev/xy) | +3 | 1394 |
| 74 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +3 | 2031 |
| 75 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +3 | 4146 |
| 76 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 587 |
| 77 | [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) | +3 | 3222 |
| 78 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | +3 | 16635 |
| 79 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +3 | 14103 |
| 80 | [abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) | +3 | 1291 |
| 81 | [mauriceboe/TREK](https://github.com/mauriceboe/TREK) | +3 | 11525 |
| 82 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +3 | 9587 |
| 83 | [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) | +3 | 9085 |
| 84 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +3 | 3126 |
| 85 | [callstack/agent-device](https://github.com/callstack/agent-device) | +2 | 3956 |
| 86 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +2 | 23808 |
| 87 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 391 |
| 88 | [TechyCSR/OpenCluely](https://github.com/TechyCSR/OpenCluely) | +2 | 724 |
| 89 | [amap-cvlab/ABot-World](https://github.com/amap-cvlab/ABot-World) | +2 | 1649 |
| 90 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +2 | 3101 |
| 91 | [syswonder/robonix](https://github.com/syswonder/robonix) | +2 | 275 |
| 92 | [davidondrej/skills](https://github.com/davidondrej/skills) | +2 | 3314 |
| 93 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +2 | 60059 |
| 94 | [openai/plugins](https://github.com/openai/plugins) | +2 | 4919 |
| 95 | [adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide) | +2 | 7839 |
| 96 | [openai/skills](https://github.com/openai/skills) | +2 | 24510 |
| 97 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +2 | 8313 |
| 98 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | +2 | 39914 |
| 99 | [mohi-devhub/antivibe](https://github.com/mohi-devhub/antivibe) | +2 | 950 |
| 100 | [mattpocock/dictionary-of-ai-coding](https://github.com/mattpocock/dictionary-of-ai-coding) | +2 | 3400 |
| 101 | [appshubcc/Bettbox](https://github.com/appshubcc/Bettbox) | +2 | 2787 |
| 102 | [oblien/openship](https://github.com/oblien/openship) | +2 | 10278 |
| 103 | [harbor-framework/harbor](https://github.com/harbor-framework/harbor) | +2 | 3843 |
| 104 | [suleimanodetoro/skills](https://github.com/suleimanodetoro/skills) | +2 | 838 |
| 105 | [xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp) | +2 | 656 |
| 106 | [wbh604/UZI-Skill](https://github.com/wbh604/UZI-Skill) | +2 | 5951 |
| 107 | [yangtiming/Fast-SAM-3D-Body](https://github.com/yangtiming/Fast-SAM-3D-Body) | +2 | 353 |
| 108 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +2 | 40881 |
| 109 | [123panNextGen/123pan](https://github.com/123panNextGen/123pan) | +2 | 253 |
| 110 | [frenzymath/Danus](https://github.com/frenzymath/Danus) | +2 | 134 |
| 111 | [jonexaiorg/jonex](https://github.com/jonexaiorg/jonex) | +2 | 238 |
| 112 | [VisionForge-OU/foreman](https://github.com/VisionForge-OU/foreman) | +2 | 423 |
| 113 | [anbeime/skill](https://github.com/anbeime/skill) | +2 | 4719 |
| 114 | [yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5) | +2 | 2109 |
| 115 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +2 | 9958 |
| 116 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +2 | 6291 |
| 117 | [Unclecheng-li/VulnClaw](https://github.com/Unclecheng-li/VulnClaw) | +2 | 2477 |
| 118 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +2 | 1497 |
| 119 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +2 | 29612 |
| 120 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +2 | 762 |


### 🌙 本月 Top 300 详情

| 排名 | 仓库 | 增长 | 总 Stars |
|---|---|---|---|
| 1 | [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) | +134 | 14103 |
| 2 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | +121 | 28265 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | +115 | 39597 |
| 4 | [usestrix/strix](https://github.com/usestrix/strix) | +110 | 48211 |
| 5 | [stablyai/orca](https://github.com/stablyai/orca) | +102 | 37364 |
| 6 | [herdrdev/herdr](https://github.com/herdrdev/herdr) | +97 | 24356 |
| 7 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | +96 | 22669 |
| 8 | [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer) | +89 | 14715 |
| 9 | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | +81 | 31276 |
| 10 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | +78 | 45102 |
| 11 | [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) | +77 | 25369 |
| 12 | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | +74 | 13862 |
| 13 | [block/buzz](https://github.com/block/buzz) | +73 | 22466 |
| 14 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | +67 | 37455 |
| 15 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +66 | 29609 |
| 16 | [Fei-Away/Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) | +64 | 13169 |
| 17 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | +62 | 24862 |
| 18 | [alibaba/page-agent](https://github.com/alibaba/page-agent) | +59 | 28418 |
| 19 | [teamchong/pxpipe](https://github.com/teamchong/pxpipe) | +57 | 6950 |
| 20 | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | +55 | 49124 |
| 21 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | +52 | 16735 |
| 22 | [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) | +50 | 5416 |
| 23 | [oblien/openship](https://github.com/oblien/openship) | +49 | 10278 |
| 24 | [agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw) | +47 | 32945 |
| 25 | [andrewyng/openworker](https://github.com/andrewyng/openworker) | +45 | 12771 |
| 26 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | +45 | 22063 |
| 27 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | +44 | 60059 |
| 28 | [facebook/astryx](https://github.com/facebook/astryx) | +44 | 11581 |
| 29 | [x4gKing/X4G](https://github.com/x4gKing/X4G) | +43 | 7782 |
| 30 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | +42 | 45923 |
| 31 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | +41 | 42998 |
| 32 | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | +40 | 16359 |
| 33 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | +40 | 39476 |
| 34 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +38 | 18813 |
| 35 | [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire) | +38 | 15001 |
| 36 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +37 | 43005 |
| 37 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | +37 | 33309 |
| 38 | [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | +36 | 8041 |
| 39 | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) | +35 | 9587 |
| 40 | [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | +35 | 30972 |
| 41 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | +35 | 9124 |
| 42 | [1jehuang/jcode](https://github.com/1jehuang/jcode) | +34 | 15858 |
| 43 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | +34 | 44332 |
| 44 | [oso95/scroll-world](https://github.com/oso95/scroll-world) | +31 | 7399 |
| 45 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | +31 | 16148 |
| 46 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | +30 | 28454 |
| 47 | [multica-ai/multica](https://github.com/multica-ai/multica) | +30 | 43912 |
| 48 | [dnshe/DNSHE-FreeDomains](https://github.com/dnshe/DNSHE-FreeDomains) | +30 | 9058 |
| 49 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | +30 | 40881 |
| 50 | [steipete/CodexBar](https://github.com/steipete/CodexBar) | +30 | 19635 |
| 51 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +29 | 32394 |
| 52 | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | +29 | 21829 |
| 53 | [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) | +29 | 6101 |
| 54 | [unicity-aos/aos-ce](https://github.com/unicity-aos/aos-ce) | +27 | 8573 |
| 55 | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | +27 | 35840 |
| 56 | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | +27 | 15595 |
| 57 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | +27 | 27803 |
| 58 | [browser-use/video-use](https://github.com/browser-use/video-use) | +27 | 19231 |
| 59 | [openai/codex-security](https://github.com/openai/codex-security) | +26 | 8520 |
| 60 | [lidge-jun/opencodex](https://github.com/lidge-jun/opencodex) | +26 | 7204 |
| 61 | [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic) | +26 | 7532 |
| 62 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | +24 | 18757 |
| 63 | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | +24 | 8313 |
| 64 | [floci-io/floci](https://github.com/floci-io/floci) | +24 | 18204 |
| 65 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | +24 | 23808 |
| 66 | [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | +24 | 4252 |
| 67 | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | +23 | 4146 |
| 68 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | +23 | 48523 |
| 69 | [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | +23 | 3509 |
| 70 | [yc-software/qm](https://github.com/yc-software/qm) | +22 | 11079 |
| 71 | [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | +22 | 30730 |
| 72 | [microsoft/flint-chart](https://github.com/microsoft/flint-chart) | +22 | 3405 |
| 73 | [makerspet/oomwoo](https://github.com/makerspet/oomwoo) | +22 | 7153 |
| 74 | [xuchonglang/investing-for-beginners](https://github.com/xuchonglang/investing-for-beginners) | +22 | 3101 |
| 75 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | +21 | 17738 |
| 76 | [blader/humanizer](https://github.com/blader/humanizer) | +21 | 33442 |
| 77 | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | +21 | 6922 |
| 78 | [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) | +21 | 9851 |
| 79 | [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) | +20 | 9851 |
| 80 | [MDX-Tom/gpt-5.6-instruct](https://github.com/MDX-Tom/gpt-5.6-instruct) | +20 | 4563 |
| 81 | [Yu9191/wloc](https://github.com/Yu9191/wloc) | +20 | 7990 |
| 82 | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | +20 | 4647 |
| 83 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | +19 | 4238 |
| 84 | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | +19 | 6291 |
| 85 | [sharpemu/sharpemu](https://github.com/sharpemu/sharpemu) | +19 | 4736 |
| 86 | [dramaclaw/dramaclaw](https://github.com/dramaclaw/dramaclaw) | +19 | 3178 |
| 87 | [decolua/9router](https://github.com/decolua/9router) | +19 | 24657 |
| 88 | [Shpigford/knockoff](https://github.com/Shpigford/knockoff) | +19 | 1989 |
| 89 | [laoma2053/awesome-zhuiju-free](https://github.com/laoma2053/awesome-zhuiju-free) | +18 | 5286 |
| 90 | [stackryze/FreeDomains](https://github.com/stackryze/FreeDomains) | +18 | 9112 |
| 91 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | +18 | 13326 |
| 92 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | +18 | 23841 |
| 93 | [rednote-machine-learning/RedKnot](https://github.com/rednote-machine-learning/RedKnot) | +18 | 1525 |
| 94 | [kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) | +18 | 8021 |
| 95 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | +17 | 11097 |
| 96 | [zhishile/codex-auth-helper](https://github.com/zhishile/codex-auth-helper) | +17 | 6379 |
| 97 | [palmier-io/palmier-pro](https://github.com/palmier-io/palmier-pro) | +17 | 13062 |
| 98 | [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) | +16 | 3436 |
| 99 | [kunchenguid/firstmate](https://github.com/kunchenguid/firstmate) | +16 | 2813 |
| 100 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | +16 | 34890 |
| 101 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | +16 | 27276 |
| 102 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | +16 | 7150 |
| 103 | [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | +16 | 4658 |
| 104 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | +15 | 14164 |
| 105 | [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) | +14 | 5373 |
| 106 | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | +14 | 3508 |
| 107 | [pascalorg/editor](https://github.com/pascalorg/editor) | +14 | 21032 |
| 108 | [BigDawnGhost/wenyi](https://github.com/BigDawnGhost/wenyi) | +14 | 2031 |
| 109 | [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | +14 | 8109 |
| 110 | [HKUDS/OpenOPC](https://github.com/HKUDS/OpenOPC) | +14 | 1047 |
| 111 | [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | +14 | 12809 |
| 112 | [XxHuberrr/Mineradio](https://github.com/XxHuberrr/Mineradio) | +14 | 9663 |
| 113 | [Chlience/yt-dlp-tauri](https://github.com/Chlience/yt-dlp-tauri) | +14 | 410 |
| 114 | [debpalash/OmniVoice-Studio](https://github.com/debpalash/OmniVoice-Studio) | +13 | 9529 |
| 115 | [shy3130/tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) | +13 | 2547 |
| 116 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | +13 | 46608 |
| 117 | [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | +13 | 10389 |
| 118 | [google-research/tabfm](https://github.com/google-research/tabfm) | +13 | 2343 |
| 119 | [bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp) | +12 | 1880 |
| 120 | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | +12 | 3946 |
| 121 | [CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser) | +12 | 29612 |
| 122 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | +12 | 32634 |
| 123 | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) | +12 | 26912 |
| 124 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | +11 | 5039 |
| 125 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | +11 | 14242 |
| 126 | [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | +11 | 11807 |
| 127 | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) | +11 | 26443 |
| 128 | [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | +11 | 7802 |
| 129 | [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) | +11 | 1946 |
| 130 | [penecho/penecho](https://github.com/penecho/penecho) | +11 | 1893 |
| 131 | [TencentEdgeOne/edgeone-makers-tools](https://github.com/TencentEdgeOne/edgeone-makers-tools) | +11 | 2028 |
| 132 | [Archive228/loopkit](https://github.com/Archive228/loopkit) | +11 | 740 |
| 133 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | +10 | 9958 |
| 134 | [oil-oil/beautify-github-readme](https://github.com/oil-oil/beautify-github-readme) | +10 | 1497 |
| 135 | [anbeime/skill](https://github.com/anbeime/skill) | +10 | 4719 |
| 136 | [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) | +10 | 2277 |
| 137 | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | +10 | 27913 |
| 138 | [eatmoreduck/boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper) | +10 | 1005 |
| 139 | [browser-act/skills](https://github.com/browser-act/skills) | +10 | 5162 |
| 140 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | +10 | 29687 |
| 141 | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | +10 | 18455 |
| 142 | [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | +10 | 1517 |
| 143 | [tandpfun/wardrobe](https://github.com/tandpfun/wardrobe) | +10 | 1793 |
| 144 | [codebymitch/TitanBot](https://github.com/codebymitch/TitanBot) | +9 | 5815 |
| 145 | [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | +9 | 9668 |
| 146 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) | +9 | 40838 |
| 147 | [openai/skills](https://github.com/openai/skills) | +9 | 24510 |
| 148 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | +9 | 19068 |
| 149 | [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | +9 | 5837 |
| 150 | [javaht/claude-desktop-zh-cn](https://github.com/javaht/claude-desktop-zh-cn) | +9 | 5749 |
| 151 | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | +9 | 1616 |
| 152 | [quantskills/quantskills](https://github.com/quantskills/quantskills) | +9 | 1835 |
| 153 | [IR-NETLIFY/zeus](https://github.com/IR-NETLIFY/zeus) | +9 | 0 |
| 154 | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | +9 | 7710 |
| 155 | [iflytek/skillhub](https://github.com/iflytek/skillhub) | +9 | 4862 |
| 156 | [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | +8 | 6626 |
| 157 | [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | +8 | 8309 |
| 158 | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | +8 | 44435 |
| 159 | [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) | +8 | 5139 |
| 160 | [Osmantic/ODS](https://github.com/Osmantic/ODS) | +8 | 3934 |
| 161 | [Robbyant/lingbot-world-v2](https://github.com/Robbyant/lingbot-world-v2) | +8 | 1472 |
| 162 | [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | +8 | 15597 |
| 163 | [mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer) | +8 | 2843 |
| 164 | [openai/plugins](https://github.com/openai/plugins) | +8 | 4919 |
| 165 | [Forward-Future/loopy](https://github.com/Forward-Future/loopy) | +8 | 2965 |
| 166 | [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | +7 | 16945 |
| 167 | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | +7 | 8639 |
| 168 | [apache/ossie](https://github.com/apache/ossie) | +7 | 1771 |
| 169 | [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | +7 | 4984 |
| 170 | [Skyvern-AI/rustwright](https://github.com/Skyvern-AI/rustwright) | +7 | 830 |
| 171 | [OpenNSWM-Lab/FAROS](https://github.com/OpenNSWM-Lab/FAROS) | +7 | 3126 |
| 172 | [Jia-Ethan/claude-keysmith](https://github.com/Jia-Ethan/claude-keysmith) | +7 | 544 |
| 173 | [jianweiweng05/qsx-strategy-score](https://github.com/jianweiweng05/qsx-strategy-score) | +7 | 525 |
| 174 | [ufy2024/AuC](https://github.com/ufy2024/AuC) | +7 | 887 |
| 175 | [ilysenko/codex-desktop-linux](https://github.com/ilysenko/codex-desktop-linux) | +7 | 3352 |
| 176 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | +7 | 29741 |
| 177 | [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | +7 | 8305 |
| 178 | [Sjj1024/PakePlus-Win7](https://github.com/Sjj1024/PakePlus-Win7) | +7 | 3150 |
| 179 | [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) | +7 | 27709 |
| 180 | [JuneYaooo/nihaisha-nishi-tcm](https://github.com/JuneYaooo/nihaisha-nishi-tcm) | +6 | 1883 |
| 181 | [powerycy/goutoujunshi](https://github.com/powerycy/goutoujunshi) | +6 | 1675 |
| 182 | [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) | +6 | 2090 |
| 183 | [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | +6 | 5010 |
| 184 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | +6 | 33046 |
| 185 | [3441293738/creatorhub](https://github.com/3441293738/creatorhub) | +6 | 762 |
| 186 | [pengchujin/jzsub](https://github.com/pengchujin/jzsub) | +6 | 920 |
| 187 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | +6 | 9186 |
| 188 | [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | +6 | 1103 |
| 189 | [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) | +6 | 2531 |
| 190 | [iflytek/astron-rpa](https://github.com/iflytek/astron-rpa) | +6 | 5899 |
| 191 | [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | +6 | 28163 |
| 192 | [crimera/piko](https://github.com/crimera/piko) | +6 | 4569 |
| 193 | [harbor-framework/harbor](https://github.com/harbor-framework/harbor) | +5 | 3843 |
| 194 | [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | +5 | 10370 |
| 195 | [icebird1998/drawio-scientific-illustrator](https://github.com/icebird1998/drawio-scientific-illustrator) | +5 | 1258 |
| 196 | [CatsJuice/sticker-forge](https://github.com/CatsJuice/sticker-forge) | +5 | 676 |
| 197 | [Blueturboguy07/cue](https://github.com/Blueturboguy07/cue) | +5 | 976 |
| 198 | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | +5 | 6998 |
| 199 | [HeyPuter/firefox-wasm](https://github.com/HeyPuter/firefox-wasm) | +5 | 493 |
| 200 | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | +5 | 5465 |
| 201 | [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | +5 | 5810 |
| 202 | [vybenetwork/solana-swap-api](https://github.com/vybenetwork/solana-swap-api) | +5 | 1191 |
| 203 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | +5 | 9082 |
| 204 | [zhongerxin/Cowart](https://github.com/zhongerxin/Cowart) | +5 | 5290 |
| 205 | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | +5 | 27098 |
| 206 | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | +5 | 2798 |
| 207 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | +5 | 7461 |
| 208 | [alam00000/bentopdf](https://github.com/alam00000/bentopdf) | +4 | 14515 |
| 209 | [QoderAI/better-harness](https://github.com/QoderAI/better-harness) | +4 | 1590 |
| 210 | [realzza/bilibili-accelerator](https://github.com/realzza/bilibili-accelerator) | +4 | 384 |
| 211 | [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | +4 | 5032 |
| 212 | [AgwaB/pi-workflow](https://github.com/AgwaB/pi-workflow) | +4 | 333 |
| 213 | [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | +4 | 1147 |
| 214 | [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | +4 | 6336 |
| 215 | [IRNova/Nova-Proxy](https://github.com/IRNova/Nova-Proxy) | +4 | 3242 |
| 216 | [MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow) | +4 | 668 |
| 217 | [ChatCut-Inc/agent-plugin](https://github.com/ChatCut-Inc/agent-plugin) | +4 | 731 |
| 218 | [webbrain-one/webbrain](https://github.com/webbrain-one/webbrain) | +4 | 610 |
| 219 | [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) | +4 | 916 |
| 220 | [nexu-io/motion-anything](https://github.com/nexu-io/motion-anything) | +4 | 645 |
| 221 | [kui123456789/cdk-redeem-only-extension](https://github.com/kui123456789/cdk-redeem-only-extension) | +4 | 1053 |
| 222 | [joeltelling/print-farm-manager](https://github.com/joeltelling/print-farm-manager) | +4 | 171 |
| 223 | [OLmatter/glm-coding-helper](https://github.com/OLmatter/glm-coding-helper) | +4 | 705 |
| 224 | [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | +4 | 664 |
| 225 | [WuKongOpenSource/Wukong-AICRM](https://github.com/WuKongOpenSource/Wukong-AICRM) | +4 | 799 |
| 226 | [MorpheApp/morphe-patches](https://github.com/MorpheApp/morphe-patches) | +4 | 3107 |
| 227 | [x4gKing/3x-ui](https://github.com/x4gKing/3x-ui) | +3 | 2218 |
| 228 | [Kritt-ai/open-kritt](https://github.com/Kritt-ai/open-kritt) | +3 | 1359 |
| 229 | [icebird1998/scientific-illustrator](https://github.com/icebird1998/scientific-illustrator) | +3 | 345 |
| 230 | [0xwilliamortiz/ponytail-improved](https://github.com/0xwilliamortiz/ponytail-improved) | +3 | 587 |
| 231 | [HeiGeAi/heige-codex-skin-studio](https://github.com/HeiGeAi/heige-codex-skin-studio) | +3 | 386 |
| 232 | [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | +3 | 9366 |
| 233 | [sreegjl/timelines](https://github.com/sreegjl/timelines) | +3 | 141 |
| 234 | [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | +3 | 12181 |
| 235 | [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | +3 | 5092 |
| 236 | [simonlin1212/investment-news](https://github.com/simonlin1212/investment-news) | +3 | 388 |
| 237 | [gongnyang/reelforge](https://github.com/gongnyang/reelforge) | +3 | 75 |
| 238 | [changeroa/StyleGallery](https://github.com/changeroa/StyleGallery) | +3 | 148 |
| 239 | [nikitadoudikov/claude-pulse](https://github.com/nikitadoudikov/claude-pulse) | +3 | 243 |
| 240 | [kenzok8/openwrt-daede](https://github.com/kenzok8/openwrt-daede) | +3 | 417 |
| 241 | [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe) | +3 | 18743 |
| 242 | [robzolkos/LazyPi](https://github.com/robzolkos/LazyPi) | +3 | 394 |
| 243 | [1sdv/TripStar](https://github.com/1sdv/TripStar) | +3 | 2105 |
| 244 | [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | +3 | 4889 |
| 245 | [iflytek/astron-agent](https://github.com/iflytek/astron-agent) | +3 | 9285 |
| 246 | [github/copilot-sdk](https://github.com/github/copilot-sdk) | +3 | 10346 |
| 247 | [Snailclimb/interview-guide](https://github.com/Snailclimb/interview-guide) | +3 | 2935 |
| 248 | [JiGuroLGC/FuckGoogleLicense](https://github.com/JiGuroLGC/FuckGoogleLicense) | +3 | 163 |
| 249 | [ingriddaleusag-dotcom/PickTV](https://github.com/ingriddaleusag-dotcom/PickTV) | +3 | 741 |
| 250 | [AutoMQ/automq](https://github.com/AutoMQ/automq) | +3 | 10405 |
| 251 | [calesthio/Crucix](https://github.com/calesthio/Crucix) | +2 | 11145 |
| 252 | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | +2 | 6157 |
| 253 | [TechyCSR/OpenCluely](https://github.com/TechyCSR/OpenCluely) | +2 | 724 |
| 254 | [zhulin025/Codex-QQ-Skin](https://github.com/zhulin025/Codex-QQ-Skin) | +2 | 391 |
| 255 | [ZihangDong/toolknit-desktop](https://github.com/ZihangDong/toolknit-desktop) | +2 | 245 |
| 256 | [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension) | +2 | 1159 |
| 257 | [ulsklyc/yuvomi](https://github.com/ulsklyc/yuvomi) | +2 | 1261 |
| 258 | [BuilderIO/skills](https://github.com/BuilderIO/skills) | +2 | 3904 |
| 259 | [Sami-Uysal/awesome-open-ai-developer-tools](https://github.com/Sami-Uysal/awesome-open-ai-developer-tools) | +2 | 71 |
| 260 | [DotRacel/etherfi-session-manager](https://github.com/DotRacel/etherfi-session-manager) | +2 | 51 |
| 261 | [fxy2311-youyou/expression-trainer](https://github.com/fxy2311-youyou/expression-trainer) | +2 | 702 |
| 262 | [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) | +2 | 1179 |
| 263 | [hunter-read/grimoire](https://github.com/hunter-read/grimoire) | +2 | 154 |
| 264 | [hiz0147/HizSteamButton](https://github.com/hiz0147/HizSteamButton) | +2 | 343 |
| 265 | [goehou/tabbit-toy](https://github.com/goehou/tabbit-toy) | +2 | 469 |
| 266 | [Fast-Editor/Lynkr](https://github.com/Fast-Editor/Lynkr) | +2 | 539 |
| 267 | [Stonewuu/ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | +2 | 1222 |
| 268 | [songrongzhen/easy-agent](https://github.com/songrongzhen/easy-agent) | +2 | 370 |
| 269 | [woheller69/FreeDroidWarn](https://github.com/woheller69/FreeDroidWarn) | +2 | 3042 |
| 270 | [Zoeille/picsou-finance](https://github.com/Zoeille/picsou-finance) | +2 | 432 |
| 271 | [george8188625/Create-Electro-Energetics](https://github.com/george8188625/Create-Electro-Energetics) | +2 | 97 |
| 272 | [booklore-app/booklore](https://github.com/booklore-app/booklore) | +2 | 702 |
| 273 | [JetBrains/youtrackdb](https://github.com/JetBrains/youtrackdb) | +2 | 428 |
| 274 | [xikhar/persona](https://github.com/xikhar/persona) | +1 | 832 |
| 275 | [huangxd-/danmu_api](https://github.com/huangxd-/danmu_api) | +1 | 2895 |
| 276 | [angieruiz17/claude-fintech-skills](https://github.com/angieruiz17/claude-fintech-skills) | +1 | 136 |
| 277 | [nageoffer/ragent](https://github.com/nageoffer/ragent) | +1 | 3432 |
| 278 | [LangLang03/LineCodePro](https://github.com/LangLang03/LineCodePro) | +1 | 70 |
| 279 | [project-openan/a2a-t-sdk-java](https://github.com/project-openan/a2a-t-sdk-java) | +1 | 11 |
| 280 | [anahata-os/anahata-asi](https://github.com/anahata-os/anahata-asi) | +1 | 23 |
| 281 | [SangLuoCN/OneStep4](https://github.com/SangLuoCN/OneStep4) | +1 | 234 |
| 282 | [oxylabs/perplexity-scraper](https://github.com/oxylabs/perplexity-scraper) | +1 | 2832 |
| 283 | [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce) | +1 | 183 |
| 284 | [fish2018/webhtv](https://github.com/fish2018/webhtv) | +1 | 1081 |
| 285 | [Dwinovo/minecraft-numen](https://github.com/Dwinovo/minecraft-numen) | +1 | 248 |
| 286 | [Novinity/ClientID](https://github.com/Novinity/ClientID) | +1 | 8 |
| 287 | [Jaysen13/jaysenwxapkg](https://github.com/Jaysen13/jaysenwxapkg) | +1 | 316 |
| 288 | [finos/fluxnova-bpm-platform](https://github.com/finos/fluxnova-bpm-platform) | +1 | 90 |
| 289 | [grimmory-tools/grimmory](https://github.com/grimmory-tools/grimmory) | +1 | 3870 |
| 290 | [6b6t/AnarchyMod](https://github.com/6b6t/AnarchyMod) | +1 | 105 |
| 291 | [zuo-qirun/amap-companion](https://github.com/zuo-qirun/amap-companion) | +1 | 56 |
| 292 | [microsoft/Spring-AI-for-Beginners](https://github.com/microsoft/Spring-AI-for-Beginners) | +1 | 33 |
| 293 | [7723mod/NPatch](https://github.com/7723mod/NPatch) | +1 | 1942 |
| 294 | [opensolon/soloncode](https://github.com/opensolon/soloncode) | +1 | 164 |
| 295 | [QmDeve/QmBlurView](https://github.com/QmDeve/QmBlurView) | +1 | 211 |
| 296 | [icysymmetra/tiktok-patches-for-morphe](https://github.com/icysymmetra/tiktok-patches-for-morphe) | +1 | 186 |
| 297 | [ispointer/RePairip](https://github.com/ispointer/RePairip) | +1 | 93 |
| 298 | [noVibe/DnsConf](https://github.com/noVibe/DnsConf) | +1 | 838 |
| 299 | [Porters-of-Railways/Railway-1.21.1](https://github.com/Porters-of-Railways/Railway-1.21.1) | +1 | 44 |
| 300 | [bytecodealliance/endive](https://github.com/bytecodealliance/endive) | +1 | 278 |
