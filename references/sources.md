# 来源与采用边界

核读日期：2026-10-22。竞品链接指向当时公开的主分支文件；未锁定提交。论文案例另记录具体版本、评审及段落定位。竞品指令的比较与真实稿件的编辑选择分别使用。

easyunslop 从 scansci-write 的语言修订规则中抽出独立入口，新增以学术语域保持为中心的简短编辑流程与正反例。保留主张、术语、证据强度、量词和否定范围的规则，在原项目中已有积累。没有复制竞品的整套提示词或安装外部依赖。

## 竞品是否考虑专业性

| 项目与核读原文 | 已明确考虑的部分 | 本技能的取舍 |
|---|---|---|
| [Humanizer-zh](https://github.com/op7418/humanizer-zh/blob/main/SKILL.md) | 明确要求学术等事实性文体保留正式程度、归因、限定和论证结构；认可被动句、名词化及有功能的连接。 | 采用文体优先和清楚处可保留的判断，将学术语域设为默认，而非多种可选语气之一。 |
| [qu-ai-wei 主入口](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/SKILL.md) 与 [编辑边界](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/references/editing-boundaries.md) | 保护原意、证据强度、语域和作者声音；保护必要的术语与名词化，不强加口语、幽默或个人经历。 | 采用概念、语域和力度核对。保持轻量交付，不要求每次生成诊断报告或编辑历史。 |
| [academic-writing-refiner](https://github.com/Zihan-Zhu/academic-writing-refiner/blob/main/academic-writing-refiner/SKILL.md) | 面向计算机领域学术写作，结合章节、目标场合选择表达；主动和被动依用途取舍。 | 采用表达精确、修改幅度适配等原则；计算机会议的篇幅与章节偏好不推广为全学科规则。 |
| [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | 当前版本区分文体，保护事实；认可技术词的正当用途及事实性写作的中性语气。 | 词表只提供检查线索，不逐词触发改写；避免把句式变化作为独立目标。 |
| [humanizer.tw](https://github.com/yelban/humanizer.tw/blob/main/SKILL.md) | 有匹配预期语气的要求，同时含口语化替换、个性与个人反应等建议。 | 这些建议对部分文体有用；直接用于学术稿件存在语域下降的风险，因此不设为默认手段。此处为对指令冲突的分析。 |
| [anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing/SKILL.md) | 强调贡献、减少自我贬低及防御性铺垫；也包含弱化不利材料的建议。 | 采用删去无信息自贬的原则。真实负面结果、研究范围及解释所需的限制继续保留，语言编辑不选择性改变证据。 |

这些项目中的若干版本已经正面处理“去 AI 味导致失去专业性”的问题。easyunslop 的具体选择是：学术文体默认、术语和逻辑保护、局部充分编辑、原文与改文对照，以及展示应保持不变的文字。

## 公开资源补充：从基础清理到表达精修

2026-10-22 补充核读如下资源，形成 [编辑模式库](editing-patterns.md) 及编辑实例第 10–14 例。实例由本项目编写，属于虚构教学文本，未冒充来源作者或真实论文的改稿。

| 来源 | 采用的判断 | 本地转化与边界 |
|---|---|---|
| [stop-slop 短语](https://github.com/hardikpandya/stop-slop/blob/main/references/phrases.md)、[结构](https://github.com/hardikpandya/stop-slop/blob/main/references/structures.md)、[实例](https://github.com/hardikpandya/stop-slop/blob/main/references/examples.md) | 开场铺垫、商业黑话、重复强调、假转折和过程旁白可以具体定位并编辑。 | 整理为按语境处理的候选模式；不采用禁用所有副词、强制主动句、删除真实否定的规则。其个别示例删去了数量范围，未将这些改稿当作学术保义示范。 |
| [qu-ai-wei 症状目录](https://github.com/LifelongLazyLearner/qu-ai-wei/blob/main/references/pattern-catalog.md) | 将词语症状与句法、篇章问题联系起来，给出处理动作并核对改后关系。 | 采用按症状选择编辑动作的思路；不照搬触发配额、自评分或未在本地验证的实证标签。 |
| [Purdue OWL：Concision](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html) | 检查词语是否承担必要任务，选择更有效的表达，适当合并句子。 | 用于句子精修，保留必要信息；长度减少不单独作为成功标准，术语不为同义变化而改写。 |
| [Gopen 与 Swan：The Science of Scientific Writing](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html) | 从读者如何理解句子出发，关注主干、动作、上下文与信息重心。该网页为注明获准转载的原文。 | 用于主干恢复、已知对象承接和段内顺序；不将英语位置偏好机械推广到中文，也不照搬原文示例中利用领域知识补充内容的做法。 |
| [Manchester Academic Phrasebank：About](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/) | 常规学术表达可承担稳定的交际功能，来源包括真实学位论文与多学科文章。 | 保护有功能的学术惯用表达，避免把固定表述整体划为黑话；未复制整套语料或将其中例子当作本项目实验结果。 |

基础清理要求处理已确认无信息的黑话、包装和重复，表达精修进一步处理主干、指代、信息次序和段落承接。二者均保留科学含义与作者意图；不把不同层次拆成默认多代理流程。

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

## 判断质量的依据

每次编辑看原文与改文之间实际发生的变化：含义、概念、证据强度与语域是否保持，表达问题是否减少。AI 检测分数和词表命中数量不作验收标准。

真实使用中的证据应来自作者确认、学科同行对内容与概念的判断，以及目标读者对表达的理解。维护时可用不同学科的固定片段检查典型失误；这些片段只能提供有限的行为证据，不能证明对所有学科和所有稿件都无损。

评价关注：既有信息是否更易理解、编辑是否引入实质变化、好段落是否得到保留。需要比较版本时，用相同原稿和任务，在独立上下文中运行通用润色与技能润色，匿名交给目标读者和学科编辑；专业编辑稿作为参考，允许相当或原稿更好。开发用案例与待评价稿件按整篇论文分开，合成片段与真实稿件分别报告。对学科的效果结论须来自相应稿件的实际评价，不能由案例覆盖数量推出。
