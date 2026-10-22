# 2026-10-23：词汇诊断接入与试用

本页材料由本项目自编，研究、数据与结果均为虚构。词汇工具为本轮新增能力；此前的全文协作试跑不作为此工具的验证。

## 已接入的能力

- 稿内高频词与二三元词组统计；中文使用二三元字组，明确区分于分词结果。
- 55条候选、105种词形或表达，逐条附检查动作、保留条件和来源；发表研究、社区报告、本地观察及编辑模式分开标记。
- 提供同语言、同文体参照目录时比较归一化频率；未提供时照常进行稿内统计与词库扫描。
- 报告包含次数及至多前5处位置和上下文，默认排除常见代码、URL、公式、引用键和参考文献内容。工具只读原稿，并拒绝输出覆盖输入。

技能入口现要求全文初改前扫描，编辑者回读候选，实际修改后复扫相关位置。短段和轻校仍按具体任务执行。

## 独立使用试跑

一位未参与工具实现的代理读取新版技能后，按单人任务要求完成下方整篇稿件。实际调用脚本扫描原稿一次、改稿一次，两次退出码均为0；没有同文体参照，因此报告如实标记有效参照为0。

| 候选 | 改前 | 实际处理 | 改后 |
| --- | ---: | --- | ---: |
| utilized | 4 | 根据动作改用analyzed、collected或used | 0 |
| delve | 1 | 直接说明分析对象与目的 | 0 |
| comprehensive | 2 | 摘要改写为正文已有发现，讨论删去重复评价 | 0 |
| robust | 3 | 均属于robust regression，保留方法名称 | 3 |
| systematic | 1 | 属于systematic error，保留技术概念和测量口径 | 1 |

题名、四节结构、传感器数量、采样间隔、监测期、估计数值、回归对象、因果限定和计划状态均经原文对照。摘要纳入正文已有结果后，一些技术词出现次数增加，编辑按其用途保留。

README也已实际执行一次词汇扫描，命中的闭环控制、系统性误差、原文示例及真实步骤表达，经回读后保留。工具提供位置与证据，具体取舍取决于稿件用途。

## 工具验证

运行`python scripts/check_lexical_scan.py`，标准库assert自检通过。覆盖无参照统计、英文词边界、词组不跨句或文件、代码及公式清洗、标题图注保留、单次词库命中、profile选择、归一化频率、坏参照或词库处理和输入覆盖保护。后续发现HTML清洗会误屏蔽不等式附近正文，已定向修复并加入断言。

技能入口格式检查通过，本轮新增的词库条目ID及来源引用有效。未涉及父项目程序，未重复运行其全量测试或构建。已通过且未变化的旧编辑试用未重跑；词频统计不用于估计AI身份或竞品胜率。

## 模拟原稿

# Temperature errors in a closed-loop controller

## Abstract

We utilized measurements from 12 sensors to delve into temperature errors in a closed-loop controller. We utilized robust regression to describe the association between ambient temperature and sensor error. The analysis provides a comprehensive understanding of the errors observed during the monitoring period.

## Methods

We utilized 12 sensors, each sampled every 30 seconds for 14 days. All sensors were calibrated before deployment. We utilized robust regression with ambient temperature as the predictor and sensor error as the response. We examined systematic error using the mean signed difference between the sensor reading and the reference reading. No controller parameters were changed during monitoring.

## Results

The median absolute error across sensors was 0.18 °C. In the robust regression, a 1 °C increase in ambient temperature was associated with a 0.02 °C increase in sensor error. These estimates describe the monitored system during the 14-day period.

## Discussion

The analysis provides a comprehensive understanding of the errors observed during the monitoring period. It does not establish that ambient temperature caused the observed differences. We plan to repeat the measurements after replacing the reference sensor; the replacement has not yet been performed.

## 实际改稿

# Temperature errors in a closed-loop controller

## Abstract

We analyzed measurements from 12 sensors to characterize temperature errors in a closed-loop controller. We used robust regression to describe the association between ambient temperature and sensor error. During the 14-day monitoring period, the median absolute error across sensors was 0.18 °C. A 1 °C increase in ambient temperature was associated with a 0.02 °C increase in sensor error.

## Methods

We collected measurements from 12 sensors, each sampled every 30 seconds for 14 days. All sensors were calibrated before deployment. We used robust regression with ambient temperature as the predictor and sensor error as the response. We examined systematic error using the mean signed difference between the sensor reading and the reference reading. No controller parameters were changed during monitoring.

## Results

The median absolute error across sensors was 0.18 °C. In the robust regression, a 1 °C increase in ambient temperature was associated with a 0.02 °C increase in sensor error. These estimates describe the monitored system during the 14-day period.

## Discussion

The analysis does not establish that ambient temperature caused the observed differences. We plan to repeat the measurements after replacing the reference sensor; the replacement has not yet been performed.
