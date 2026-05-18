# 袁鹏

401887683@qq.com · (+86) 17782314266
个人主页：https://jerr-yuan.github.io/-risk-digital-assets/

---

## 专业亮点

- **LLM Agent 实践**：独立构建 ReAct 巡检 Agent（6 工具 · 12 轮循环 · Claude API），自动完成多维风险归因与报告生成，人工分析工时减少约 80%；搭建 15+ 模块的贷后产品 AI 中台，实现端到端产品化交付
- **因果推断落地**：运用 DiD + CATE 量化 SMS 策略因果效应（非相关性），发现前置触达边际效应 ≤0.3pp，分层优化方案节省 $10K/月，年化 $118K–$245K
- **策略体系深度**：5 年+ 贷后全链路风险策略实战（菲律宾 CL/BNPL/PPL 多产品线），2025 年回收率历史新高；M2+ 绝对值同比增长 104%

---

## 工作经历

**信也科技 · 贷后策略负责人 · 菲律宾事业部** | 2024.08 - 至今 · 上海

**AI Agent 工具化**

- 构建 **LLM 智能巡检 Agent**（ReAct 架构），集成 6 个定制工具对 DPD30 / D1 / M0 回收率等指标进行多轮自动归因，自动产出 McKinsey 风格 HTML 报告，替代约 80% 日常人工看数分析
- 搭建 **贷后产品 AI 中台**（Streamlit · 15+ 页面 · McKinsey 设计体系），涵盖 Agent 系统管理、运行记录、5 维质检、知识资产、策略工作台等模块
- 沉淀 **20+ 可复用 Skill**（触达 ROI 测算 / 风险预估 / 额度弹性等），构建 Multi-Agent 协作框架及 Skill/Memory 管理体系
- 搭建 **5 维 Agent 评估框架**（任务完成率 / 决策一致性 / 鲁棒性 / 可解释性 / 成本效率），结合自动化成熟度 OKR 持续优化

**策略与业务贡献**

- 风险：现金贷回收率提升 **+3.0pp**，TikTok BNPL 提升 **+5.3pp**；M2+ 绝对值同比增长 **104%**，回收率同比提升 **55%**
- 成本：业务量增长 **80%** 下人力仅增 **25%**，ROI 提升约 **55%**
- 策略体系：全流程精细化运营（分案 / 触达 / AI 催收）；主导全业务线风险目标预估与成本预估管理
- 管理：带 3 人策略团队；统筹 3 条成熟业务线 + 主导 4 条新线（信用卡 / BNPL / Offline）0-1 建设

---

**度小满金融 · 风险策略分析师 · 风险部** | 2020.07 - 2024.07 · 北京

- **AB 测试体系**：负责贷后 AB 测试全流程设计与执行，建立对照组分配方案与显著性检验框架，数据驱动策略迭代
- **风险建模**：搭建逾期率预测模型（XGBoost）并实时监控异动；主导贷后企微、法催等项目全生命周期设计
- **数字化基础建设**：设计底层 SQL 数据库（MaxCompute），搭建多维指标监控看板；沉淀标准化数据分析方法论

---

## 主要项目

### LLM 智能巡检 Agent（inspection_agent_V1）

- **架构**：ReAct 循环（Observe → Think → Act → Observe），最多 12 轮迭代；支持 Claude Opus / Sonnet / Haiku 模型切换
- **工具**：6 个定制工具——`get_data_overview` / `query_dpd_trend` / `query_repay_trend` / `detect_anomaly` / `query_process_metrics` / `generate_report`
- **输出**：自动生成 McKinsey 风格 HTML 归因报告，覆盖风险线（DPD30/M0）/ 回收线（D1/自然日）/ 过程线（坐席/案量）
- **评估**：归因准确率 > 85%，报告生成时间 < 3 分钟，人工复核率 < 20%

### 触达策略因果推断与 ROI 优化

- **方法**：双重差分（DiD）+ 条件平均处理效应（CATE）+ Dose-Response 弹性拟合 + ICER 增量收益决策
- **发现**：客群分化显著——高风险客群（DPD30≥15%）对 SMS 无弹性，弱组（3条）最优；低风险客群（DPD30≤5%）响应明显
- **落地**：分层触达（高风险 3 条 / 中 2 条 / 低 1 条）节省 $10K/月；结合 SMS 长度优化估计追加节省 $20K/月；年化 $118K–$245K
- **交付**：12 张 ApexCharts 可视化 Dashboard（McKinsey 设计体系），完整方法论文档与 SQL 脚本

### 贷后产品 AI 中台（个人项目）

- **平台**：Streamlit 多页面 App（15+ 页面），McKinsey 风格设计体系，统一 Agent 管理入口
- **Agent 管理**：ReAct 实验室（模型选择 + API Key 配置 + 运行记录）；5 维质检体系；自动化成熟度 OKR 评估
- **知识体系**：前沿知识库（CoT / ReAct / Multi-Agent / Prompt Engineering 等）；自有资产地图

### 老客额度弹性策略（额度策略平台）

- 按信用评分维度（B/C/F/E）+ 多头评分维度（A/B/C/D）分层构建弹性曲线；发现优质客群显著响应，高风险客群结构性违约、弹性接近零
- Buffer 机制 + 边际 TR 分析，提供差异化额度调整建议；自动生成 McKinsey 风格评估报告

---

## 技术能力

| 类别 | 工具 / 技能 |
|------|------------|
| **LLM · Agent** | Claude API (Anthropic)、ReAct 架构、CoT 推理链、Tool Use、Prompt Engineering、Multi-Agent 协作、Skill/Memory 体系 |
| **因果推断 · 建模** | DiD、CATE、Dose-Response、ICER、AB Test 设计、XGBoost、逻辑回归、评分卡 |
| **工程 · 数据** | Python (pandas / numpy)、SQL (MaxCompute / MySQL)、Streamlit、HTML / CSS / JavaScript |
| **产品 · 可视化** | McKinsey 设计体系、ApexCharts、端到端产品交付、数字资产管理体系 |
| **语言** | 雅思 7.0、GMAT 700、中英双语工作环境 |

---

## 教育背景

**波士顿大学 · 奎斯特罗姆商学院** | 商业分析硕士（数据科学 / 机器学习 / 可视化）| 2019.07 – 2020.05

**南京农业大学 · 经济管理学院** | 市场营销学士（统计学 / 计量 / 金融学）| 2014.09 – 2018.07
