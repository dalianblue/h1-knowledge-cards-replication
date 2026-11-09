# 预充氧到 PaO₂ 300，呼吸暂停后掉到 70，到底几分钟？

先给结论：**没有直接证据**。

现有文献里，没有任何研究测过"PaO₂ 从 300 掉到 70 mmHg"这条轨迹的分钟数。所有可用的临床终点，都是 SpO₂ 降到 90%/92% 的"安全呼吸暂停时间"，不是 PaO₂ 绝对值。你想要的那个数字，文献里不存在。

基于有限数据的生理学估算（来源等级：unverified 综述卡，仅供参考）：第一段 **PaO₂ 300→100 mmHg 约 1–3 分钟**，第二段 **100→70 mmHg 约 2–5 分钟**，合计约 **3–8 分钟**。个体差异极大，别当确定值引用。

教科书层面能采信的是去饱和终点，不是 PaO₂ 阈值：健康非肥胖成人呼吸暂停至 SpO₂ 80% 约 **9 分钟**；儿童或肥胖成人 **≤3 分钟**（Miller's Anesthesia 10th，教科书）。

临床决策看 SpO₂ 实时轨迹，别拿固定分钟数预设安全窗。

## 为什么是 SpO₂ 说了算

预充氧的本质，是用 FiO₂ 1.0 冲洗肺泡氮气，让 FRC 变成纯氧储库。储库能撑多久，看 FRC 大小和去氮是否完全。

呼吸暂停后没有新鲜氧摄入，肺泡氧被持续摄取。FRC 越小、氧耗越高，储库耗尽越快。

关键在于氧解离曲线。PaO₂ 从 300 掉到 100 这一段，曲线还平坦，SpO₂ 看着没事。等 PaO₂ 进入陡段，SpO₂ 就是悬崖式下跌。这就是临床盯 SpO₂ 而不盯 PaO₂ 的原因——机制推演，卡库无直接验证。

## 预充氧方式改变的是安全窗，不是起点

面罩 vs 单纯 HFNO vs HFNO+口咬嘴，呼吸暂停至 SpO₂ 92% 的中位时间分别为 **309s、344s、386s**（p=0.014；面罩 vs 联合 p=0.006）。预充氧 3 min 后 PaO₂ 中位分别为 **49、57、61 kPa**（p=0.003）（Anaesthesia，PMID:34402044，RCT，n=79 完成）。

HFNO 流率不是越长越好。**45/70/95 L/min** 三档的安全呼吸暂停时间无差异（中位 **472/523/483s**，P=0.59），45 L/min 不适感最低（Br J Anaesth，PMID:41419379，RCT，n=72）。

无呼吸氧合能降低插管期低氧血症：常规护理组 **27.6%** vs 无呼吸氧合组 **19.1%**，RR 降低 30%（95%CI 0.59–0.82）。死亡率 RR 0.77（95%CI 0.59–1.02），呈下降趋势但未达显著（Am J Emerg Med，PMID:28647137，Meta，8 项研究 n=1953）。

## 特殊人群，安全窗差得离谱

健康产妇标准面罩 90% 有效时间 **3.6 分钟**（95%CI 3.3–6.7）。3 分钟达标率：面罩 **71%** vs HFNO **0%**。HFNO 组 8 分钟仍有 **55%**（加简单面罩）和 **92%**（不加）未达标（Anaesthesia，PMID:32048278，RCT，每组 40 例）。

肥胖是硬约束。计算机模拟显示 BMI **50 kg/m²** 时，HFNO 对呼吸暂停时间的改善仅 **1.8–8.5 分钟**；BMI **24 kg/m²** 时改善超过 **60 分钟**（Br J Anaesth，PMID:33549319，综述/模拟，非临床实测）。

## 还有哪些不确定

终点异质性是根本问题。各 RCT 用 SpO₂ 92%、SpO₂ 80%、EtO₂≥90% 等不同终点定义"安全呼吸暂停时间"，彼此不可直接换算，也无法反推 PaO₂ 轨迹。

HFNO 的定位也有分歧。2024 急诊插管指南共识指出，HFNO 预氧合可提高 PaO₂（平均差 **64 mmHg**，95%CI 32–97，p<0.001）并延长无呼吸时间，但**不降低插管时去饱和风险**；NIV 预氧合则可减少低氧血症（SpO₂<85% 发生率 **7% vs 46%**，p<0.01）（Guidelines 2024，指南共识）。"延长安全窗"和"降低去饱和事件"不是同一命题。

BMI 分层数据来自计算机模拟，非临床实测，外推需谨慎。多数预充氧 RCT 为单中心、小样本（72–199 例）、择期 ASA 1–3 患者，危重症与急诊人群证据薄弱。

至于"PaO₂ 300→70 时间"的直接争议——没有，因为根本无直接研究。

## 参考

- [专题深挖] 预充氧到 PaO2 300，呼吸暂停后掉到 70 要几分钟？分两段算（topic_driven_distill，综述，unverified）
- Miller's Anesthesia (10th Edition)·APNEIC OXYGENATION（教科书，trust_book）
- Pre-oxygenation with facemask oxygen vs high-flow nasal oxygen vs high-flow nasal oxygen plus mouthpiece（Anaesthesia，RCT，certified）PMID:34402044
- Determining the effective pre-oxygenation interval in obstetric patients using high-flow nasal oxygen（Anaesthesia，RCT，certified）PMID:32048278
- Apneic oxygenation reduces the incidence of hypoxemia during emergency intubation（Am J Emerg Med，Meta，certified）PMID:28647137
- Preoxygenation with high-flow nasal oxygen at various flow rates in elective surgical patients（Br J Anaesth，RCT，certified）PMID:41419379
- Effect of variable pre-oxygenation endpoints on safe apnoea time using high flow nasal oxygen（Br J Anaesth，综述/模拟，certified）PMID:33549319
- Guidelines 2024: Emergency intubation of an adult outside the operating room（指南共识，certified）