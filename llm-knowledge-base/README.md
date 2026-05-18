# AI/LLM 学习中心

> 一个人持续维护的 LLM 学习知识库 · by Mr. Yuan

**在线访问**: https://jerr-yuan.github.io/llm-knowledge-base/
**作者**: [@jerr-yuan](https://github.com/jerr-yuan)
**最后更新**: 2026-05-18

---

## 这是什么

一个用 **纯 HTML + CSS** 搭建的个人 LLM 知识中台。每章遵循统一结构（定义 → 类比 → 对比表 → 业务联系），把工程实践中沉淀的认知整理成可复用、可索引、可对外展示的形态。

设计原则：
- **不依赖任何构建工具** —— 双击 HTML 即用，AI 协作友好
- **视觉对标 portfolio 主页** —— 同一套 CSS 变量 + 字体栈，访客感知是同一品牌
- **轻量可扩展** —— 加一个主题 = 加一个 HTML 文件 + 改一行索引

---

## 目录结构

```
llm-knowledge-base/
├── index.html                        # 知识地图首页
├── 01-llm-training-basics.html       # 章节 1: LLM 训练基础
├── assets/
│   └── styles.css                    # 共享设计系统
├── README.md                         # 你正在看的这个文件
└── .gitignore
```

---

## 怎么加新主题页（3 步）

### Step 1: 复制章节模板

```powershell
Copy-Item 01-llm-training-basics.html 02-rag-architecture.html
```

### Step 2: 改章节内容

打开新 HTML，修改：

| 位置 | 改什么 |
|------|--------|
| `<title>` | 新章节标题 |
| `<meta name="description">` | 章节描述（影响搜索/分享） |
| `<header class="article-header">` | eyebrow / h1 / lede / meta |
| `<aside class="toc-sticky">` | 左侧目录列表 |
| `<div class="toc-mobile">` | 移动端下拉选项（与目录同步） |
| 各个 `<section class="section">` | 主体内容 |
| 底部 `kb-footer` | 一般无需改 |

### Step 3: 在 index.html 增加卡片

在 `index.html` 的 `.kb-grid` 里，把对应 planned 卡片改成 active：

```html
<!-- 改前 -->
<div class="kb-card planned">
  <div class="kb-num">CHAPTER 02</div>
  <h3>RAG 架构</h3>
  ...
  <span class="tag-planned">○ Coming Soon</span>
</div>

<!-- 改后 -->
<a href="02-rag-architecture.html" class="kb-card active">
  <div class="kb-num">CHAPTER 02</div>
  <h3>RAG 架构</h3>
  ...
  <span class="tag-active">● 已发布</span>
  <span class="read-time">⏱ XX 分钟</span>
</a>
```

---

## 本地预览

**最简单**：直接双击 `index.html`，浏览器打开。

**推荐**：VS Code + Live Server 插件，改文件自动刷新。

```powershell
# 用 VS Code 打开整个目录
code D:\jerr-yuan-portfolio\llm-knowledge-base
```

---

## 部署到 GitHub Pages

完整流程参考 [skills_github_pages_deploy.md](file:///C:/Users/yuanpeng03/.claude/projects/E--/memory/memory/skills_github_pages_deploy.md)，4 步：

```powershell
# 1. 本地 init
cd D:\jerr-yuan-portfolio\llm-knowledge-base
git init
git add .
git commit -m "Initial commit: LLM knowledge base MVP"
git branch -M main

# 2. 建公开仓（用 git credential 自动鉴权）
# POST https://api.github.com/user/repos
# Body: {"name":"llm-knowledge-base","public":true}

# 3. push + 开 Pages
git remote add origin https://github.com/jerr-yuan/llm-knowledge-base.git
git push -u origin main
# POST /repos/jerr-yuan/llm-knowledge-base/pages
# Body: {"source":{"branch":"main","path":"/"}}

# 4. 等 1-2 分钟，访问
# https://jerr-yuan.github.io/llm-knowledge-base/
```

---

## 设计规范速查

### 颜色（CSS 变量，全在 `assets/styles.css` `:root`）

| 变量 | Hex | 用途 |
|------|-----|------|
| `--ink` | `#0F172A` | 主文本、标题、深色边框 |
| `--text` | `#1E293B` | 段落正文 |
| `--text-m` | `#475569` | 次要文本（描述、副标题） |
| `--text-l` | `#94A3B8` | 弱化文本（meta、时间戳） |
| `--bg` | `#FAFAF9` | 页面背景 |
| `--surface` | `#FFFFFF` | 卡片、表格底色 |
| `--accent` | `#0F766E` | 品牌色（teal），链接/active |
| `--highlight` | `#E37222` | McKinsey orange 强调 |
| `--danger` | `#DC2626` | 警示色 |
| `--safe` | `#059669` | 安全/积极色 |
| `--info` | `#1D4ED8` | 信息蓝 |

### 字体

```css
--serif: 'Noto Serif SC', 'Inter', serif;
--sans: 'Inter', -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
--mono: 'JetBrains Mono', 'SF Mono', Consolas, 'Microsoft YaHei Mono', monospace;
```

### 主要组件类

| 类名 | 用途 |
|------|------|
| `.section` | 章节区块（自带 scroll-margin） |
| `.compare-table` | 对比表（thead 深色） |
| `.callout` / `.callout.info` / `.callout.warn` / `.callout.biz` / `.callout.danger` | 5 色 callout box |
| `.metaphor` | 类比卡片（橙色左边框） |
| `.code-block` | 代码/公式块（深色背景） |
| `.formula` | 居中虚框公式 |
| `.diagram` | SVG 图表容器 |
| `.kb-card.active` / `.kb-card.planned` | 知识地图卡片 |

### 写作规范

- 每章 5 ~ 20 分钟阅读量
- 章节顶部加 `⏱ X 分钟` meta
- 重要业务联系用 `<div class="callout biz">` 包裹
- 颜色硬编码只允许出现在 `:root` 中
- 中英混排时英文术语用 `<code class="inline">` 包裹

---

## 维护节奏

- **每完成一次和 Claude 的深度学习对话** → 整理成新章节
- **每月** → 回顾 planned 列表，挑 1-2 个落地
- **每季度** → review 已发布章节，根据新认知更新

---

## License

MIT · 内容欢迎引用，注明出处即可。

---

## 维护人

**Mr. Yuan** (袁鹏)
- GitHub: [@jerr-yuan](https://github.com/jerr-yuan)
- Portfolio: https://jerr-yuan.github.io
- Email: 401887683@qq.com
