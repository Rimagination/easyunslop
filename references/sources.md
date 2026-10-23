# 来源与采用边界

核读日期：2026-10-22；原稿—改稿对照及专业编辑方法补核于 2026-10-23。竞品链接指向当时公开的主分支文件；未锁定提交。论文案例另记录具体版本、评审及段落定位。竞品指令的比较与真实稿件的编辑选择分别使用。

easyunslop 从 scansci-write 的语言修订规则中抽出独立入口，新增以学术语域保持为中心的简短编辑流程与正反例。保留主张、术语、证据强度、量词和否定范围的规则，在原项目中已有积累。没有复制竞品的整套提示词或安装外部依赖。

## 竞品是否考虑专业性

| 项目与核读原文 | 已明确考虑的部分 | 本技能的取舍 |
|---|---|---|
| [Humanizer-zh](https://github.com/op7418/humanizer-zh/blob/main/SKILL.md) | 明确要求学术等事实性文体保留正式程度、归因、限定和论证结构；认可被动句、名词化及有功能的连接。 | 采用文体优先和清楚处可保留的判断，学术稿件保持学术语域，其他专业文本按具体用途编辑。 |
| [qu-ai-wei 主入口](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md) 与 [编辑边界](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/references/editing-boundaries.md) | 保护原意、证据强度、语域和作者声音；保护必要的术语与名词化，不强加口语、幽默或个人经历。 | 采用概念、语域和力度核对。保持轻量交付，不要求每次生成诊断报告或编辑历史。 |
| [academic-writing-refiner](https://github.com/Zihan-Zhu/academic-writing-refiner/blob/main/academic-writing-refiner/SKILL.md) | 面向计算机领域学术写作，结合章节、目标场合选择表达；主动和被动依用途取舍。 | 采用表达精确、修改幅度适配等原则；计算机会议的篇幅与章节偏好不推广为全学科规则。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | 当前版本区分文体，保护事实；认可技术词的正当用途及事实性写作的中性语气。 | 词表只提供检查线索，不逐词触发改写；避免把句式变化作为独立目标。 |
| [humanizer.tw](https://github.com/yelban/humanizer.tw/blob/main/SKILL.md) | 有匹配预期语气的要求，同时含口语化替换、个性与个人反应等建议。 | 这些建议对部分文体有用；直接用于学术稿件存在语域下降的风险，因此不设为默认手段。此处为对指令冲突的分析。 |
| [anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing/SKILL.md) | 强调贡献、减少自我贬低及防御性铺垫；也包含弱化不利材料的建议。 | 采用删去无信息自贬的原则。真实负面结果、研究范围及解释所需的限制继续保留，语言编辑不选择性改变证据。 |

这些项目中的若干版本已经正面处理“去 AI 味导致失去专业性”的问题。easyunslop 按具体文体保持专业程度，保护术语和逻辑；修改后先独立阅读改稿，再对照原文核查含义，并用实例说明何时应保留原句。

## 触发条件与只诊断入口

2026-10-23 参考公开仓库收录的 [Doubao Human Signal 2.2.9](https://github.com/ahang1598/doubao-workbuddy-qwenwork-skills/blob/main/doubao/skills/doubao-human-signal/SKILL.md)，重点核读其描述、Scope / Trigger 与诊断输出规则。

采用“触发场景—不自动触发与不适用场景”的组织方式，把用户对上一稿的自然反馈与只诊断请求写进入口。EasyUnslop 继续围绕已有文本，不扩展到该项目的从零创作、写作 prompt 或评分流程。只诊断按具体文字列问题和建议，不判定生成身份；触发后仍保留用户要求的改稿前确认与实质调整授权。

## 公开资源补充：从基础清理到表达精修

2026-10-22 补充核读如下资源，形成 [编辑模式库](editing-patterns.md) 及编辑实例第 10–14 例。实例由本项目编写，属于虚构教学文本，未冒充来源作者或真实论文的改稿。

| 来源 | 采用的判断 | 本地转化与边界 |
|---|---|---|
| [stop-slop 短语](https://github.com/hardikpandya/stop-slop/blob/main/references/phrases.md)、[结构](https://github.com/hardikpandya/stop-slop/blob/main/references/structures.md)、[实例](https://github.com/hardikpandya/stop-slop/blob/main/references/examples.md) | 开场铺垫、商业黑话、重复强调、假转折和过程旁白可以具体定位并编辑。 | 整理为按语境处理的候选模式；不采用禁用所有副词、强制主动句、删除真实否定的规则。其个别示例删去了数量范围，未将这些改稿当作学术保义示范。 |
| [qu-ai-wei 症状目录](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/references/pattern-catalog.md) | 将词语症状与句法、篇章问题联系起来，给出处理动作并核对改后关系。 | 采用按症状选择编辑动作的思路；不照搬触发配额、自评分或未在本地验证的实证标签。 |
| [Purdue OWL：Concision](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html) | 检查词语是否承担必要任务，选择更有效的表达，适当合并句子。 | 用于句子精修，保留必要信息；长度减少不单独作为成功标准，术语不为同义变化而改写。 |
| [Gopen 与 Swan：The Science of Scientific Writing](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html) | 从读者如何理解句子出发，关注主干、动作、上下文与信息重心。该网页为注明获准转载的原文。 | 用于主干恢复、已知对象承接和段内顺序；不将英语位置偏好机械推广到中文，也不照搬原文示例中利用领域知识补充内容的做法。 |
| [Manchester Academic Phrasebank：About](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/) | 常规学术表达可承担稳定的交际功能，来源包括真实学位论文与多学科文章。 | 保护有功能的学术惯用表达，避免把固定表述整体划为黑话；未复制整套语料或将其中例子当作本项目实验结果。 |

基础清理要求处理已确认无信息的黑话、包装和重复，表达精修进一步处理主干、指代、信息次序和段落承接。主编辑统一处理这两层问题；全文任务采用[分轮编辑与协作](editorial-workflow.md)，由两位检查者分别集中检查阅读效果与原意保留，再由主编辑整合。短段与轻度校改保持单人流程。

## 真实修订与专业编辑方法

2026-10-22 新增 [真实修订案例](real-editing-cases.md)，收录 10 篇论文的公开修改，包含地球与环境领域的海洋碳循环和古海洋地球化学案例；逐例记录版本、定位、证据类型和编辑范围。原有 14 例继续标为项目编写的教学文本。英文论文中的修订及其中文释义分开呈现，未把中文释义标成原作者原句。

| 来源 | 对技能的具体作用 |
|---|---|
| F1000Research 的版本、评审与作者回复（R01、R02、R08） | 采用概念范围与研究视角区分、摘要呈现已有发现、合理保留缩写、按理论依赖组织内容的方法。章节重排和作者补入的研究内容分别标明。 |
| eLife 论文与公开作者回复，PMC／Europe PMC 完整记录（R03、R04） | 采用修饰语位置、比较对象对应、沿同一维度组织结果的方法；核对回复与公开正文，不从评审建议推断作者已实施所有改动。 |
| D’Arcy 等，[ARIES](https://aclanthology.org/2024.acl-long.377/) 的原始评论、人工编辑配对及 OpenReview 版本 PDF（R05、R06） | 采用首次解释符号用途、连接正文概念与图表缩写的方法。人工配对表示评论与改动的关联，不等于独立质量评分。 |
| Jiang、Xu、Stevens，[arXivEdits](https://aclanthology.org/2022.emnlp-main.641/) 与实际 arXiv 版本（R07） | 将标签为简化的数学实质改动用作边界案例；不机械地把语料标签转成改写指令。 |
| Copernicus 的 ESSD 与 Biogeosciences 原稿、正式稿、公开评审及作者回复（R09、R10） | 采用量的类型与水层范围澄清、时间状语归属及局部术语判断的方法。实际数据、深度与研究方法变动保留作者来源，不作为语言编辑可自行补充的内容。 |
| [Editors Canada：Professional Editorial Standards 2024](https://editors.ca/wp-content/uploads/2024/05/EditorsCanada_ProfessionalEditorialStandards_2024.pdf)，A2.5、C1–C3 | 按受众、任务与编辑幅度改善清晰度和连贯性，保留原意、作者声音和语域。 |
| [van der Lee 等：文本人工评价方法](https://aclanthology.org/W19-8643/)、[Schoch 等：评价措辞与偏差](https://aclanthology.org/2020.evalnlgeval-1.2/) | 在技能维护时区分内容忠实与读者理解收益；采用中性问题、匿名呈现和独立评价，报告分歧。日常润色不因此增加评分或审稿流程。 |

案例库保存精简的中文分析、少量术语与可复查链接；各论文与数据集的许可分别记载。未镜像整篇文章或整套数据，也未安装其代码。

## 原稿—改稿对照的身份与采用范围

[对照页](editorial-pairs.md)记录短引文、来源明示的理由或本项目的推断、以及本项目编写的易改坏版本。后者均是教学反例，不能称为来源中的第三份稿件。

| 编号与一手来源 | 稿件身份与理由证据 | 落入技能的判断 |
| --- | --- | --- |
| E01 · [Gopen 与 Swan](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html) | 已发表或已接受论文的原稿，与科学写作专家给出的两种**建议稿**；文章解释插入语如何拉开主谓，也把保留或删除技术细节的决定留给作者。 | S01：安排主干与技术细节；不把建议稿冒充作者采纳版本。 |
| E02 · [ESSD 原稿、评审、回复与修订](https://essd.copernicus.org/articles/18/1405/2026/essd-18-1405-2026-discussion.html#RC1) | 论文作者依审稿意见作出的**实际修订**，没有职业文字编辑身份；审稿者明确询问总量类型与水层范围。 | S07：已有材料支持时明确数值类型与范围，不凭惯例猜深度。 |
| E03 · [Revise & Resubmit 编辑样稿](https://www.reviseandresubmit.com/paper-edit-samples) | Jacob Henry 展示获客户许可的实名项目**职业编辑稿**；源页没有逐处解释。段落衔接理由是本项目的前后稿分析。完整样稿中的事实增补不作语言编辑示范。 | S04、P01：让已有主体名称承担后文信息；不新增效果判断。 |
| E04 · [Kojima 与 Popiel，*JKMS*](https://jkms.org/DOIx.php?id=10.3346/jkms.2023.38.e152) | 两位医学编辑的**真实工作改编教学例**，并非客户逐字原稿；来源明确解释知识范围与时间范围的区别。 | B06：逐项保留有依据的限定，不机械加缓和语。 |
| E05 · [Uni-edit 材料科学 PDF](https://cdn.prod.website-files.com/6820504f1c679c24f766a247/682a6ca8a2eed4580f15ac53_sample_level_2_materials_engineering.pdf) | 机构自述真实客户样稿，编辑者未实名；PDF 提供**编辑建议与作者问询**，接受与发表状态未知。修订方向按页面可视标记核对。 | S09：分清数据支持的具体对象，歧义需要作者确认。 |

对照仅保留少量短摘录和链接，不随技能镜像完整客户样稿。源页未给理由处使用“本项目分析”，不替编辑者发言。教学改编和编辑建议保留其原始状态，因而不能按“职业编辑定稿的正确答案”计分。

## 判断质量的依据

每次编辑看原文与改文之间实际发生的变化：含义、概念、证据强度与语域是否保持，表达问题是否减少。AI 检测分数和词表命中数量不作验收标准。

原文与改文的对应、公开专业修订、语言规范及实际改稿记录，都可用于发现和修正问题。作者、学科同行与目标读者的反馈提供额外判断；维护技能无需等待真人审核。模型复核须指出具体改动及原文依据，不能以自评分或一致同意代替检查。

评价关注：既有信息是否更易理解、编辑是否引入实质变化、好段落是否得到保留。开展目标读者评价时，用相同原稿和任务，在独立上下文中运行通用润色与技能润色，匿名交给目标读者和学科编辑；专业编辑稿作为参考，允许相当或原稿更好。开发用案例与待评价稿件按整篇论文分开，合成片段与真实稿件分别报告。对学科的效果结论须来自相应稿件的实际评价，不能由案例覆盖数量推出。

## 词汇统计与候选词库

[词汇诊断](lexical-diagnostics.md)接入稿内重复统计、[按来源标记的候选词库](lexical-signals.json)和可选参照对照。工具复用scansci-write的`excess_vocab.py`思路，移除将固定次数或倍数解释为普遍标准的输出，补充无参照模式、位置与上下文、词库保留条件和文档清洗。

- [Juzek与Ward，COLING 2025](https://aclanthology.org/2025.coling-main.426/)在历史科学写作样本中研究词汇过度代表。词库选取原文明确举出的少量候选，并注明研究范围；词形变化用于检索，不标成分别经过统计验证。
- [Kobak等的原始项目](https://github.com/berenslab/llm-excess-vocab)提供跨年度超额词分析的背景；[slop-forensics](https://github.com/sam-paech/slop-forensics)提供单词及二三元词组统计的实现参照。此处采用词频比较思路，不移植其作者比例估计、模型评分或创意写作词表。
- [Claude Code的具体用户报告](https://github.com/anthropics/claude-code/issues/53454)只作为`load-bearing`的社区观察，未当成当前Claude全系列的实测词频。
- `glm-local-202609`来自父项目2026-09-15的作者偏好与探索性小样本记录；原记录还存在样本少、提示与词库相互影响等解释限制，因此按本地编辑观察标记。它不代表整个GLM系列的统计特征。
- 其余通用条目根据本项目的[编辑模式](editing-patterns.md)整理检查动作与保留条件。社区观察、作者偏好和发表研究分别标记，不以来源名气替代逐句判断。

## 结构、语法与作者声音的补充方法

以下方法并入已有编辑顺序，按阅读困难调用，不为每篇稿件另设一轮。大学写作中心和编辑标准提供实践指导；关于AI的研究只支持其样本范围内的风险判断，不证明本技能已经取得普遍优势。实例26–33均为本项目自编，不能称为来源中的真实编辑稿。

| 一手资源 | 具体采用 | 适用边界 |
|---|---|---|
| [Wisconsin：反向提纲](https://writing.wisc.edu/handbook/processandstructure/reverseoutlines/)与[长稿修订](https://writing.wisc.edu/handbook/processandstructure/revisinglongprojects/) | 从整段概括主题与职责，发现前提滞后、非相邻语义重复和一段多任务；落入P02、P08及实例26。 | 保留摘要、结果、讨论的不同任务；不强制主题句位于段首，不自行重建缺失论证。 |
| [George Mason：已知与新信息](https://writingcenter.gmu.edu/writing-resources/grammar-style/improving-cohesion-the-known-new-contract)与[Harvard：过渡](https://writingcenter.fas.harvard.edu/transitions) | 先检查主题、指称和句间关系，再调整主语、语态或连接；落入S04及实例27。 | 不强制每句旧信息开头、重点结尾；专业词的必要复现有助于承接。 |
| [George Mason：冠词](https://writingcenter.gmu.edu/writing-resources/grammar-style/definite-and-indefinite-articles)、[可数性](https://writingcenter.gmu.edu/writing-resources/grammar-style/count-vs-noncount-nouns) | 依据实际指称、可数性和既定对象集合处理限定词与一致关系；落入S11及实例28。 | 不以首次/再次出现机械分配a/the；不将英文规则套到中文。 |
| [Purdue：悬垂修饰](https://owl.purdue.edu/owl/general_writing/mechanics/dangling_modifiers_and_how_to_correct_them.html)与[关系从句的限定性](https://owl.purdue.edu/owl/general_writing/grammar/relative_pronouns/defining_vs_non_defining.html) | 拆并句后检查动作主体、从句范围及逗号；落入S12及实例29。 | 不补造施事者，不机械换that/which；期刊的形式偏好不能改变所指子集。 |
| [George Mason：学术时态](https://writingcenter.gmu.edu/writing-resources/grammar-style/the-three-common-tenses-used-in-academic-writing)与[Phrasebank：引用来源](https://www.phrasebank.manchester.ac.uk/referring-to-sources/) | 区分已完成操作、图文陈述、当前解释及既有研究与现在的关系；落入S13及实例30。 | 合理的时态切换保留；不把特定观察改为普遍规律，不把计划写成完成。 |
| [ICMJE：稿件准备](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html)与[Editors Canada：文体编辑](https://editors.ca/publications/professional-editorial-standards/stylistic-editing/) | 区分正文、图表及说明文字的任务；从所给材料恢复必要单位、缩写和误差说明，压缩逐格复述；落入P10及实例32。 | ICMJE的医学格式不推广为全学科规定；不猜样本量或SD/SE/CI，不删不利结果。 |
| [CHI 2025：AI写作协助与跨文化文风](https://arxiv.org/html/2409.11360)及[写作辅导者访谈](https://aclanthology.org/2025.in2writing-1.5/) | 从作者已有好段落或所给样稿辨认文风，保留其评价立场与展开方式；与既有作者声音规则合并。 | 前者涉及印度与美国参与者的特定英文写作任务，后者为10位辅导者的访谈及原型研究；不外推为所有文化、模型或专业论文的已证效果。 |
| [How LLMs Distort Our Written Language](https://arxiv.org/abs/2603.18161)，2026年预印本 | 将立场与含义漂移作为核对重点，检查批评、让步和结尾；落入保义检查与实例33。 | 特定模型和议论文修订实验不代表所有学科；不据此规定所有作者必须语气强烈，也不引用基于分类器推断的AI使用率来证明编辑效果。 |
| [Review Feedback Agent](https://arxiv.org/html/2504.09737)与[friction项目](https://github.com/zhangchaodesign/friction) | 将泛泛反馈拆为可定位的理解问题，检查稿件是否已有答案；合并重复意见，允许有依据地不采纳；落入主编辑整合环节。 | 评审辅助与新手写作研究不构成专业论文效果保证；模型模拟反馈不称为真人审核。 |
| [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)与[qu-ai-wei模式库](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/references/pattern-catalog.md) | 补查跨节套式、解释尾句及权威归属；强化B10、B12、P06，采用前回到原稿核对。 | 社区实践与实证研究分别标记；不按词形、尾句形式或句型相似度自动删改。 |

[Do LLMs write like humans?](https://arxiv.org/html/2410.16107)提供不同模型、任务间写作特征差异的反例背景。被动句、词汇多样性或句子节奏均不设统一人类标准；不采用禁用全部副词、被动句、名词化、固定标点配额、刻意加错、插入私人细节或凭空增加具体事实的做法。词频工具继续承担定位职责，不扩展为作者身份鉴定。

## 按实际失误维护技能

先看原稿、上下文和实际输出，区分含义错误、阅读困难、偏好差异。保留历史输出和原评阅；发现误判时追加更正，不把改写后的记录冒充当时结果。学术修订涉及作者新增研究内容时，只提炼语言方法。

将能共用的修法并入已有规则；单个措辞不升级为禁词，示例应同时说明需要保留的反例。删掉重复要求和互相冲突的限制，主入口保留决策原则，详细取舍放在按需实例中。

一批修改完成后，用不同题材的文本检查实际行为，包含已有优质段落和容易改错的关系。复杂改动可让独立编辑者先按技能改稿，再由核对者对照原文查含义、单读改稿查表达；分歧回到文字依据解决。格式检查只证明技能包可用。已发现问题完成修复、针对性复测通过后结束本批，不把真人反馈、竞品比较或反复自评分设成维护门槛。

## 需要比较竞品时的可复现对照

维护者若要检验“全面超越”，先限定对象为**已有中文或英文学术、专业稿件的语言编辑**，覆盖短段、题名与摘要、长稿、已有优质段落和 LaTeX 文稿。用于开发的案例按整篇作品从评估集排除；真实稿件与自编测试分开报告。文章语言、学科、文体和编辑幅度应在采样前确定，不能根据试验结果删去失利类别。

同一原稿和同一编辑任务分别交给无 skill、EasyUnslop 及待比较项目；使用相同模型与参数、完整原版 skill、独立会话，记录版本和运行日期。随机排列并隐去版本名；不同输出不可互相作参考。GitHub star 数描述传播范围，不进入质量评分。

作者或学科编辑先核对事实、术语、数字、引用、条件和推断力度，逐项记录严重含义错误；目标读者再比较清楚程度、自然度、专业性和作者声音，同时允许选择原稿。对长稿另查题名—摘要—正文—结论一致性，对结构化稿件另查公式、引用键、标签与链接。评价者记录具体文字依据和分歧，盲评结束后再揭示来源。

发布“全面超越”结论前预先写明样本量与判定标准：EasyUnslop 对**每个**比较项目均须在整体及预定的语言、文体、学科分层中取得稳定的盲评优势，严重含义错误率不得升高，优质原稿的无益改写率不得升高。报告配对结果、差异的不确定性及失利样本；若某些分层证据不足，只报告已获支持的范围。一次模型自检、少量教学例或 star 排名都不构成该结论的证据。
