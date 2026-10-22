<p align="center">
  <img src="./assets/easyunslop-logo-tight.png" alt="EasyUnslop：Easy 为鼠尾草绿，Unslop 为深墨色的手绘纸笔 Logo" width="920">
</p>
<p align="center">
  <strong>有真意，去粉饰，少做作，勿卖弄。</strong><br>
  <sub>——鲁迅《作文秘诀》</sub>
</p>
<p align="center">
  <a href="#一分钟开始"><img alt="Input: drafts" src="https://img.shields.io/badge/INPUT-DRAFTS-789788?style=for-the-badge&amp;labelColor=555555"></a>
  <a href="#改稿示例"><img alt="Output: scholarly prose" src="https://img.shields.io/badge/OUTPUT-SCHOLARLY_PROSE-293A39?style=for-the-badge&amp;labelColor=555555"></a>
  <a href="#编辑范围"><img alt="Language: Chinese and English" src="https://img.shields.io/badge/LANGUAGE-ZH_%2B_EN-B48B64?style=for-the-badge&amp;labelColor=555555"></a>
</p>

# EasyUnslop

EasyUnslop 是一个中英文学术润色 skill，帮助作者去掉 AI 腔，把文字写得准确、自然。它适用于论文、学位论文和其他专业文本，既可润色整篇稿件，也可单独修改题名、节标题、摘要或正文段落。

它会删去空泛套话和重复内容，理顺句子与段落，同时保留原意和作者的表达风格。专业术语遵循学科惯例，结论中的“可能”“在……条件下”等必要限定也会保留。已经清楚、自然的文字可以不改。

## 一分钟开始

### 使用 Agent

向 Agent 发送以下指令，安装 EasyUnslop：

```text
请帮我安装这个 skill：
https://github.com/Rimagination/easyunslop
```

然后提供需要修改的文字：

```text
请用 $easyunslop 润色以下论文段落，去掉 AI 腔和冗余，保持专业性、
学术规范、原意与证据强度。直接给出改后的正文。

[粘贴待改文字]
```

已有摘要和正文时，可以一起提供：

```text
请用 $easyunslop 修改这篇论文的摘要。
根据下方正文中已经报告的内容，突出研究对象和主要发现，保留结论的适用范围。

[摘要与相关正文]
```

你可以补充“只改措辞与句间衔接”或“允许调整段内顺序”，指定修改幅度。需要对照查看时，可要求“给出原文、改文和简短理由”。

<details>
<summary>手动安装</summary>

进入所用工具的 skills 目录，执行：

```sh
git clone https://github.com/Rimagination/easyunslop.git easyunslop
```

也可以从 [Releases](https://github.com/Rimagination/easyunslop/releases) 下载最新版本的安装包，将其中的 `easyunslop` 文件夹放入该目录。安装后的文件夹应直接包含 `SKILL.md`、`agents/` 和 `references/`。

若 Codex 设置了自定义 `CODEX_HOME`，请使用该路径下的 `skills` 目录。其他工具请确认其实际读取技能的位置。

</details>

## 改稿示例

以下两例取自[编辑检查](docs/validation.md)，使用项目自编的虚构材料，展示具体改法。润色全文时，题名、各级节标题、摘要与正文一并检查，章节层级、编号与引用格式按原稿保留。

### 地球与环境：清理铺垫，保留测量尺度

**原文**

> 从比较结果的层面来看，2011—2020 年，流域北部站点观测的年平均降水量为 820 mm，南部站点为 760 mm。我们使用空间分辨率为 5 km 的卫星反演降水产品进行了相应的比较工作。该产品对同一时期北部与南部区域的年平均降水量估计分别为 790 mm 和 750 mm。需要指出的是，站点观测值与格网区域平均值在空间代表性方面存在差异。

**改文**

> 2011—2020 年，流域北部站点观测的年平均降水量为 820 mm，南部站点为 760 mm。我们使用空间分辨率为 5 km 的卫星反演降水产品进行比较。该产品对同一时期北部与南部区域的年平均降水量估计分别为 790 mm 和 750 mm。站点观测值与格网区域平均值在空间代表性上存在差异。

改稿删去了引导语和冗余措辞，保留时间、数值、单位与空间分辨率，也保留了站点观测和格网区域反演之间的区别。

<details>
<summary>传播研究：用正文中已有的发现组织摘要</summary>

**原摘要**

> 本研究围绕网络辟谣情境下的信息核查行为展开深入探讨，通过对社区居民进行访谈，系统考察了信息来源选择及其背后的意义。文章将讨论社区居民如何使用社区通知与熟人求证，以及两类来源在日常信息核查中的不同作用。本研究具有一定的理论意义和实践价值。

**同时提供的正文内容**

> 本研究访谈了 24 名社区居民。多数受访者会同时查看社区通知并向熟人求证。受访者通常通过社区通知确认是否存在相关安排，通过熟人求证理解这些安排与自身生活的关系。少数受访者主要依靠社区通知。本文据此区分了安排确认与情境解释两类核查任务。

**改后的摘要**

> 本研究通过访谈 24 名社区居民，考察网络辟谣情境下的信息来源选择及其作用。多数受访者会同时查看社区通知并向熟人求证。受访者通常通过社区通知确认是否存在相关安排，通过熟人求证理解这些安排与自身生活的关系。少数受访者主要依靠社区通知。本文据此区分了安排确认与情境解释两类核查任务。

改稿从正文中提取样本信息、主要发现和两类核查任务，替换原摘要中的议程预告与泛泛评价。只提供摘要时，就依据摘要已有的信息修改。

</details>

更多中英文改稿及原句保留的例子，见[编辑实例](references/editing-examples.md)。其中有 18 则自编教学材料和 1 则 README 失败复盘；第 15–17 例关注标题，第 18、19 例讨论生硬表达。

## 编辑范围

| 编辑任务 | 处理方式 |
| --- | --- |
| 黑话、套话与机械衔接 | 删除空泛铺垫、重复强调和正文中的对话残留，保留有实际作用的连接词。 |
| 长句与信息重心 | 理清主干，将条件和修饰语放在对应内容附近；按实际用途保留名词化表达与复杂句。 |
| 比较、数字与尺度 | 说清比较对象及各自的属性，保留分母、单位、时空范围，以及观测、模拟和反演的区别。 |
| 术语、缩写与图表 | 同一概念使用一致的名称，将已有定义或说明放在首次使用处附近，使正文与图表中的术语、缩写相互对应。 |
| 论文题名与各级节标题 | 删去空泛修饰，使标题准确概括全文或本节内容。同级标题的措辞相互协调，层级、编号与固定格式保持不变；改名时一并更新所给目录和文中引用的章节名称。 |
| 摘要与段落组织 | 突出已提供的研究对象与发现，理顺段内顺序和指代；跨段重排按用户要求进行。 |
| 理论、证明与规范论证 | 保留概念边界、量词次序、否定范围和论证层次，区分“建议”“应当”等表述的判断强度。 |

编辑以原稿及所提供的上下文为依据，影响结论解释的研究限制和必要限定会保留。未提供某项检验的信息时，不将其写成“本研究未进行该检验”。完整论文生成、文献检索、研究设计与事实核验需另行处理。

## 编辑流程

1. **通读原稿。** 了解文章写给谁、属于什么文体，以及作者希望怎样修改；确认原稿的主张和需要保留的信息。
2. **修改表达。** 根据具体问题参考编辑模式和案例，删去冗余，调整语序与衔接。句子本身生硬时，可在保留含义的前提下重写。
3. **复读与核对。** 先单独读改稿，看搭配和行文是否自然，再对照原文核查含义与证据强度。没有改善的改动予以撤回。

这些步骤由同一 Agent 完成，短文可一次处理，默认直接给出改稿。

## 真实论文修订案例

[案例库](references/real-editing-cases.md)收录了 10 篇论文的公开修订。每例附有论文版本、评审意见、作者回复或人工配对数据，并标明哪些是作者的实际修改，哪些是本项目的编辑分析。

| 领域与案例 | 可借鉴的判断 |
| --- | --- |
| 教育研究 · R01–R02 | 区分概念的范围与论文采用的视角，保留有用的高频缩写，让摘要交代研究发现。 |
| 神经科学 · R03–R04 | 将实验条件放在对应描述附近，明确各对象的属性，按同一比较维度组织结果。 |
| 计算机科学 · R05–R06 | 在首次使用处说明符号用途，让正文中的概念与图表缩写对应。 |
| 数学 · R07 | 识别删去“唯一性”表述带来的命题变化，核对简化后的表述是否仍与原文等义。 |
| 语言学 · R08 | 在依赖某一理论框架的分析之前，先交代必要的概念与分类依据。 |
| 地球与环境：海洋碳循环 · R09 | 交代数字所指的总量与水层范围，保留专业单位和原有数值。 |
| 地球与环境：古海洋地球化学 · R10 | 消除时间修饰语的歧义，根据局部语境判断温度术语的具体含义。 |

案例也说明了何时需要谨慎：补充方法解释或研究范围须有材料支持，删去“唯一性”这样的词则可能改变数学命题的含义。

## 原稿与编辑稿对照

[原稿—改稿对照](references/editorial-pairs.md)按来源身份记录 5 组短摘录、修改理由和容易改坏的写法。它们覆盖技术信息的位置、段落主体、数值范围、知识与时间限定，以及数据支持模型时的语义分叉。每组都区分来源已说明的理由和本项目的分析。

其中一组来自实名客户的职业编辑前后稿，一组是医学编辑根据实际工作改编的教学例，一组是编辑机构展示的建议稿；另两组分别是科学写作专家的示范和作者回应审稿意见的实际修订。建议稿没有被写成作者定稿，教学例也没有被写成客户逐字原稿。这些例子已进入[编辑模式库](references/editing-patterns.md)及 [SKILL.md](SKILL.md) 的判断步骤。

## 项目文档

| 文档 | 内容 |
| --- | --- |
| [SKILL.md](SKILL.md) | 技能入口、编辑范围、须保留的内容与完整流程 |
| [编辑模式库](references/editing-patterns.md) | 从词句清理到比较关系、信息次序和段落组织 |
| [编辑实例](references/editing-examples.md) | 18 则自编教学材料及 1 则本项目 README 失败复盘 |
| [真实修订案例](references/real-editing-cases.md) | 10 篇论文的版本、修改依据、定位与适用条件 |
| [原稿—改稿对照](references/editorial-pairs.md) | 5 组有来源身份的短对照、修改理由、易改坏版本与使用边界 |
| [来源记录](references/sources.md) | 参考项目、编辑研究与具体采用方式 |
| [验证记录](docs/validation.md) | 已完成的检查、观察结果与评价范围 |
| [留出材料检验](docs/transfer-evaluation.md) | 冻结技能后的四例真实材料对照与匿名评阅 |

仓库由技能说明、参考材料和界面元数据组成，无需安装 Python、R 或 Node.js 依赖。

## 怎样判断改稿质量

判断改稿质量，要看它是否准确保留原意，也要看读者能否更容易理解主张、比较对象和适用条件。作者、学科同行和目标读者的反馈都可用于评价。AI 检测分数、删词数量和句子长短不作为评价标准。

项目保存了 5 项使用自编材料的独立代理编辑记录，涵盖摘要、工程比较、规范论证、数学及地球与环境，并完成过一次规则综合审查。[输入](docs/inputs.md)、[输出](docs/outputs.md)和[验证记录](docs/validation.md)均可查看。

后来又用四段未参与构建的真实材料做了一次[无技能／有技能对照](docs/transfer-evaluation.md)，由不知道分组身份的另一名代理评阅：EasyUnslop 较好 1 例，通用润色较好 1 例，2 例相当。这组短句测试没有显示总体优势。真实作者、学科编辑或目标读者的盲评，以及完整论文层面的对照，仍待进行。

本项目的 README 在使用技能后也曾出现生硬表达，因此补充了文体判断和整段复读的要求。修改依据及三项维护者自检见[写作质量修订记录](docs/writing-quality-check.md)。

## 参考项目与方法依据

EasyUnslop 由 scansci-write 的语言修订规则整理而来，并参考了专业编辑方法、论文公开修订记录和社区项目。各项方法的出处及采用范围见[来源记录](references/sources.md)。

### 专业编辑与科学写作

- [Editors Canada · Professional Editorial Standards 2024](https://editors.ca/wp-content/uploads/2024/05/EditorsCanada_ProfessionalEditorialStandards_2024.pdf)：按受众与任务编辑，保持原意、作者声音和语域。
- [Gopen 与 Swan · The Science of Scientific Writing](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html)：从读者理解出发，组织主干、动作、上下文与信息重心。
- [Purdue OWL · Concision](https://owl.purdue.edu/owl/general_writing/academic_writing/conciseness/index.html)：识别冗余，使词句准确传达信息。
- [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/)：理解常规学术表达的交际功能，保留有用途的固定表述。

### 真实修订与评价研究

- [ARIES · ACL 2024](https://aclanthology.org/2024.acl-long.377/)：结合审稿评论、人工配对与论文版本，分析具体修改。
- [arXivEdits · EMNLP 2022](https://aclanthology.org/2022.emnlp-main.641/)：利用版本编辑记录检查语言变化及其语义影响。
- F1000Research、eLife、Earth System Science Data 与 Biogeosciences 的公开版本和评审记录：具体论文、页码和回复位置见[案例库](references/real-editing-cases.md)。
- [van der Lee 等](https://aclanthology.org/W19-8643/)与 [Schoch 等](https://aclanthology.org/2020.evalnlgeval-1.2/)：为评价内容忠实度、表达改善程度及识别评价偏差提供方法参考。

### 社区项目

- [Humanizer-zh](https://github.com/op7418/humanizer-zh) 与 [qu-ai-wei](https://github.com/LifelongLazyLearner/qu-ai-wei)：保留原有文体、原意、证据强度和作者风格。
- [academic-writing-refiner](https://github.com/Zihan-Zhu/academic-writing-refiner)：按章节和目标场合处理专业表达。
- [humanizer](https://github.com/blader/humanizer)、[humanizer.tw](https://github.com/yelban/humanizer.tw) 与 [stop-slop](https://github.com/hardikpandya/stop-slop)：识别模板化措辞与结构，结合学术语境选择处理方式。
- [anti-defensive-writing](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)：减少无信息的自我贬低与防御性铺垫，同时保留真实证据和必要限制。

第三方论文、数据集与项目保留各自的权利和许可。仓库保存精简分析、少量术语与来源定位，完整原文请访问对应出版方或原始项目。
