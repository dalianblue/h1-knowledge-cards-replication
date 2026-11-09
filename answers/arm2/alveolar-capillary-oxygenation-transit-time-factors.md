静息时，肺毛细血管里的红细胞完成一次气体交换，平均只有**0.75秒**。而氧合平衡本身，只需要**0.25秒**。

账面上看，储备是3倍。够宽裕。

但这是平均值。有些毛细血管的转运时间，短到**0.1–0.2秒**。弥散限制从来不是从"平均"开始崩的，是从最短的那批毛细血管开始崩的。

先把结论放这儿：**"平均储备充足"不等于"每个毛细血管单元都安全"。** 围术期真正能动的杠杆是V/Q匹配和肺容积维持，不是去追求延长转运时间——那也不是你能直接调的旋钮。

---

**为什么最短的那批先出事**

氧合效率由三样东西决定：弥散面积、膜厚度、毛细血管床容积。肺毛细血管血容量与肺血流量之比，决定平均转运时间。

问题在于，毛细血管路径长度和血流分布天然不均一。所以转运时间是个分布，不是一个数。

当转运时间掉进0.1–0.2秒这个区间，氧合就从"灌注限速"翻成"弥散限速"。运动、心输出量增加、缺氧、高温，都会缩短转运时间。精英运动员、心衰患者、高原暴露者，就是这批容易暴露弥散限制的人。

反方向也一样：休克、麻醉、低温让心输出量下降，转运时间延长，但那是伴随灌注不足的延长，不是好事。

**注意，以上时间数值来自综述级卡片，unverified，没有原始RCT支撑。当机制框架用，别当定量阈值用。**

---

**临床怎么把握**

看几个有数的证据。

健康猪仰卧位机械通气，PEEP为0时，高FiO₂组肺塌陷**32.7±14.5%**，低FiO₂组**18.6±7.6%**（P=0.045）；而呼吸顺应性23.9±6.5 vs 21.9±5.0 ml/cmH₂O（P=0.441），没差异（Anesthesiology，PMID:38207290，动物RCT，n=10）。

这说明什么？没有PEEP支撑时，靠提高FiO₂代偿氧合，代价是吸收性肺不张，而且它并不改变区域通气与灌注分布本身。10分钟内就发生。

ARDS里，PEEP的效应取决于可复张性。15例中重度ARDS，PEEP 5 vs 15 cmH₂O，非依赖区正常V/Q通气增加（p=0.018）、高V/Q通气减少（p=0.023）（Crit Care，PMID:35818077，病例系列）。高PEEP不是普适获益。

COVID-19 ARDS的可复张性变异更大。10例插管患者，PEEP变化10 cmH₂O，recruitment to inflation ratio中位**0.79**；高PEEP改善氧合和通气不均一性，但PaCO₂升高（PMID:32697482）。氧合改善不等于死腔或通气效率改善，这两件事得分开看。

俯卧位呢？21例中重度C-ARDS，背侧肺复张**12.5%±8.0%**、腹侧去复张**-6.9%±5.2%**、整体复张增加**6.0%±6.7%**（均p<0.001），呼吸系统顺应性45±15 vs 45±18 mL/cmH₂O，没变（p=0.957）（Crit Care Med，PMID:35200194）。V/Q获益可以独立于力学改善——别拿顺应性没涨就当俯卧位白做。

术中通气这块有个量化关联：2096例，中位PEEP 5 cmH₂O、驱动压15 cmH₂O；PaO₂/FiO₂每增100 mmHg，肺并发症aOR **0.495**（Anesth Analg，PMID:31107262，回顾性队列）。链条是"术中保护性通气—术后氧合—结局"，但这是观察性证据，有混杂和选择偏倚，不能当因果读。

---

**还有哪些不确定**

转运时间那三个数——0.75秒、0.25秒、0.1–0.2秒——都来自unverified综述卡，无PMID原始研究，不同教材报道有差异。别单独引用当阈值。

高FiO₂增加肺塌陷的证据来自健康猪、n=10、只观察10分钟，外推到人类ARDS或肥胖患者的吸收性肺不张时程，要打折扣。

ARDS的PEEP证据都是小样本生理学研究（n=10–15），没有临床结局，可复张性导向的个体化PEEP仍缺大样本RCT。指南之间对"高PEEP普适性"本身就有分歧。

至于"转运时间直接测量与围术期低氧血症"的关系，卡片库里没有重大争议文献——这个领域本身就是循证缺口。

证据就这样。机制清楚，数字有限，临床决策落在V/Q和肺容积上，别落在那个0.75秒上。

---

**参考**

- Influence of Fractional Inspired Oxygen Tension on Lung Perfusion Distribution, Regional Ventilation. Anesthesiology. RCT. PMID:38207290
- [专题深挖] 肺泡毛细血管氧合时间与影响因素. topic_driven_distill. 综述(unverified,无PMID)
- Potential for Lung Recruitment and Ventilation-Perfusion Mismatch in Patients With the Acute Respiratory Distress Syndrome. Crit Care Med. 病例系列. PMID:32697482
- Effects of PEEP on regional ventilation-perfusion mismatch in the acute respiratory distress syndrome. Crit Care. 病例系列. PMID:35818077
- Effects of Prone Position on Lung Recruitment and Ventilation-Perfusion Matching. Crit Care Med. 病例系列. PMID:35200194
- Association of Intraoperative Ventilator Management With Postoperative Oxygenation, Pulmonary Complications. Anesth Analg. 队列. PMID:31107262