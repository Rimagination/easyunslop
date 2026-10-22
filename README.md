<p align="center">
  <img src="./assets/easyunslop-logo-tight.png" alt="EasyUnslop：Easy 为鼠尾草绿，Unslop 为深墨色的手绘纸笔 Logo" width="920">
</p>
<p align="center">
  <strong>有真意，去粉饰，少做作，勿卖弄。</strong><br>
  <sub>——鲁迅《作文秘诀》</sub>
</p>
<p align="center">
  <a href="#一分钟开始"><img alt="Input: drafts" src="https://img.shields.io/badge/INPUT-DRAFTS-789788?style=for-the-badge&amp;labelColor=555555"></a>
  <a href="#结果长什么样"><img alt="Output: scholarly prose" src="https://img.shields.io/badge/OUTPUT-SCHOLARLY_PROSE-293A39?style=for-the-badge&amp;labelColor=555555"></a>
  <a href="#能改什么"><img alt="Language: Chinese and English" src="https://img.shields.io/badge/LANGUAGE-ZH_%2B_EN-B48B64?style=for-the-badge&amp;labelColor=555555"></a>
</p>

# EasyUnslop

EasyUnslop 是一个中英文学术润色 skill，适用于论文、学位论文和其他专业文本。它帮助作者删去空泛套话和重复表达，理顺句子与段落，让文字更准确、自然。论文题名、各级节标题、摘要和正文都在编辑范围内。

去除 AI 腔的同时，EasyUnslop 保留原意、专业术语和作者的表达风格，并遵循相应学科的写作规范。结论的含义与强度保持不变，已经清楚、准确的文字可以原样保留。

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

可用“只改措辞与句间衔接”或“允许调整段内顺序”指定修改幅度，也可要求“给出原文、改文和简短理由”，方便逐处核对。

<details>
<summary>手动安装</summary>

在你所用工具实际加载的 skills 目录中执行：

```sh
git clone https://github.com/Rimagination/easyunslop.git easyunslop
```

也可以从 [Releases](https://github.com/Rimagination/easyunslop/releases) 下载最新版本的安装包，将其中的 `easyunslop` 文件夹放入该目录。安装后的文件夹应直接包含 `SKILL.md`、`agents/` 和 `references/`。

Codex 使用自定义 `CODEX_HOME` 时，可安装到其 `skills` 子目录；以当前工具实际加载的路径为准。

</details>

## 结果长什么样

全文润色包括题名、各级节标题、摘要与正文，改稿保留原有章节层级、编号与引用格式。也可单独润色标题或指定段落。以下两例取自[编辑检查](docs/validation.md)，输入均为项目自编的虚构材料。

### 地球与环境：清理铺垫，保留测量尺度

**原文**

> 从比较结果的层面来看，2011—2020 年，流域北部站点观测的年平均降水量为 820 mm，南部站点为 760 mm。我们使用空间分辨率为 5 km 的卫星反演降水产品进行了相应的比较工作。该产品对同一时期北部与南部区域的年平均降水量估计分别为 790 mm 和 750 mm。需要指出的是，站点观测值与格网区域平均值在空间代表性方面存在差异。

**改文**

> 2011—2020 年，流域北部站点观测的年平均降水量为 820 mm，南部站点为 760 mm。我们使用空间分辨率为 5 km 的卫星反演降水产品进行比较。该产品对同一时期北部与南部区域的年平均降水量估计分别为 790 mm 和 750 mm。站点观测值与格网区域平均值在空间代表性上存在差异。

删去了无信息的引导语，压缩了冗余措辞；时间、数值、单位、空间分辨率及站点观测与格网区域反演的区别均予以保留。

<details>
<summary>传播研究：用正文中已有的发现组织摘要</summary>

**原摘要**

> 本研究围绕网络辟谣情境下的信息核查行为展开深入探讨，通过对社区居民进行访谈，系统考察了信息来源选择及其背后的意义。文章将讨论社区居民如何使用社区通知与熟人求证，以及两类来源在日常信息核查中的不同作用。本研究具有一定的理论意义和实践价值。

**同时提供的正文内容**

> 本研究访谈了 24 名社区居民。多数受访者会同时查看社区通知并向熟人求证。受访者通常通过社区通知确认是否存在相关安排，通过熟人求证理解这些安排与自身生活的关系。少数受访者主要依靠社区通知。本文据此区分了安排确认与情境解释两类核查任务。

**改后的摘要**

> 本研究通过访谈 24 名社区居民，考察网络辟谣情境下的信息来源选择及其作用。多数受访者会同时查看社区通知并向熟人求证。受访者通常通过社区通知确认是否存在相关安排，通过熟人求证理解这些安排与自身生活的关系。少数受访者主要依靠社区通知。本文据此区分了安排确认与情境解释两类核查任务。

改稿将正文中已有的样本信息、主要发现和概念区分写入摘要。仅提供摘要时，就依据摘要中的信息修改。

</details>

更多中文、英文及应当保留原句的例子，见 [17 个教学实例](references/editing-examples.md)；第 15–17 例专门展示题名、节标题与固定标题的处理。

## 能改什么

| 编辑任务 | 处理方式 |
| --- | --- |
| 黑话、套话与机械衔接 | 删除空泛铺垫、重复强调和正文中的对话残留，保留有实际作用的连接词。 |
| 长句与信息重心 | 找到主干，让对象、动作、条件和修饰语的关系更清楚；保留承担专业功能的名词化与复杂句。 |
| 比较、数字与尺度 | 明确属性属于哪个对象，保留分母、单位、时间窗口、空间范围及观测、模拟、反演的区别。 |
| 术语、缩写与图表衔接 | 同一概念使用一致的名称，将已有定义或说明移至首次使用处附近，保持正文与图表中的表述一致。 |
| 论文题名与各级节标题 | 准确概括研究内容或本节主题，删去空泛修饰，协调同级标题的措辞；保留层级、编号与固定格式，同步修改所给目录及文中引用的章节名称。 |
| 摘要与段落组织 | 突出已提供的研究对象与发现，理顺段内顺序和指代；跨段重排按用户要求进行。 |
| 理论、证明与规范论证 | 保留概念边界、量词次序、否定范围、论证层次，以及“建议”“应当”等不同判断强度。 |

编辑依据原稿及所提供的上下文，保留影响结论解释的研究限制和必要限定。材料中缺少某项检验信息时，不据此断言研究未做该检验。完整论文生成、文献检索、研究设计与事实核验需另行处理。

## 它如何工作

1. **通读原稿。** 确定读者、学科、文体与修改幅度，识别需要保留的主张、术语、数据、条件和引用。
2. **修改表达。** 删去冗余，突出主干，调整信息顺序，说清原文已有的关系；根据具体问题参考编辑模式和案例。
3. **对照复读。** 核对原意、证据强度与专业表达是否保留，判断改稿是否更清楚，撤回没有明确收益的改动。

三轮由同一 Agent 完成，分别关注表达问题、具体修改和原意核对；短文可一次处理。参考材料按需读取，默认直接给出改稿。

## 真实论文中的编辑判断

[案例库](references/real-editing-cases.md)收录 10 篇论文的公开修订，附有论文版本、评审意见、作者回复或人工配对数据，并分别标明作者的实际修改与本项目的编辑分析。

| 领域与案例 | 可借鉴的判断 |
| --- | --- |
| 教育研究 · R01–R02 | 分清概念范围与本文视角，合理保留高频缩写，让摘要交代已有发现。 |
| 神经科学 · R03–R04 | 调整实验条件的位置，明确属性对应的对象，按同一维度组织密集结果。 |
| 计算机科学 · R05–R06 | 在首次使用处说明符号用途，将正文概念与图表缩写对应。 |
| 数学 · R07 | 识别删去“唯一性”表述带来的命题变化，核对简化后的表述是否仍与原文等义。 |
| 语言学 · R08 | 在依赖某一理论框架的分析之前，先交代必要的概念与分类依据。 |
| 地球与环境：海洋碳循环 · R09 | 交代数字所指的总量与水层范围，保留专业单位和原有数值。 |
| 地球与环境：古海洋地球化学 · R10 | 消除时间修饰语的歧义，根据局部语境判断温度术语的具体含义。 |

这些案例展示了具体修改及其依据。涉及方法解释、研究范围等内容的补充，须有相应材料支持；数学案例则说明，删去一个词也可能改变命题含义。

## 项目文档

| 文档 | 内容 |
| --- | --- |
| [SKILL.md](SKILL.md) | 技能入口、编辑范围、须保留的内容与完整流程 |
| [编辑模式库](references/editing-patterns.md) | 从词句清理到比较关系、信息次序和段落组织 |
| [教学实例](references/editing-examples.md) | 17 个项目自编实例，展示题名、节标题与正文如何修改及何时保留 |
| [真实修订案例](references/real-editing-cases.md) | 10 篇论文的版本、修改依据、定位与适用条件 |
| [来源记录](references/sources.md) | 参考项目、编辑研究与具体采用方式 |
| [验证记录](docs/validation.md) | 已完成的检查、观察结果与评价范围 |

仓库由技能说明、参考材料和界面元数据组成，无需安装 Python、R 或 Node.js 依赖。

## 怎样判断改稿质量

先核对原意、概念与证据强度，再看改稿是否让主张、比较对象和适用条件更清楚。真实稿件的质量应结合作者确认、学科同行评议及目标读者的理解情况判断。AI 检测分数、删词数量和句子长短不作为评价标准。

当前保存了 5 项自编材料的独立代理编辑记录，覆盖摘要、工程比较、规范论证、数学及地球与环境，并完成一次规则综合审查。[输入](docs/inputs.md)、[输出](docs/outputs.md)和[验证记录](docs/validation.md)均可查看。真实作者或目标读者对技能输出的盲评，以及独立上下文下的无技能对照实验尚未开展。

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
