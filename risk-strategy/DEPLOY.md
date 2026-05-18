# 部署到 GitHub + Vercel

## 一、推送到 GitHub

### 1. 在 GitHub 新建仓库

- 打开 https://github.com/new
- **Repository name**：例如 `yuan-personal-site` 或 `risk-strategy-site`
- **Public**，不要勾选 "Add a README"（本地已有）
- 点 **Create repository**

### 2. 本地添加远程并推送

在终端进入站点目录后执行（把 `你的用户名` 和 `仓库名` 换成你自己的）：

```powershell
cd e:\site-redesign\final

git remote add origin https://github.com/你的用户名/仓库名.git
git branch -M main
git push -u origin main
```

若使用 SSH：

```powershell
git remote add origin git@github.com:你的用户名/仓库名.git
git branch -M main
git push -u origin main
```

首次推送若提示登录，按 GitHub 提示完成认证（或配置 SSH key）。

---

## 二、Vercel 自动托管

### 1. 导入项目

- 打开 https://vercel.com 并登录（可用 GitHub 登录）
- 点 **Add New…** → **Project**
- 在 **Import Git Repository** 里选刚推送的仓库，点 **Import**

### 2. 配置（保持默认即可）

| 项 | 建议 |
|----|------|
| **Framework Preset** | Other（或不选） |
| **Build Command** | 留空 |
| **Output Directory** | 留空（即根目录） |
| **Root Directory** | 留空 |

静态 HTML 无需构建，直接发布根目录即可。

### 3. 部署

- 点 **Deploy**
- 完成后会得到一个 `xxx.vercel.app` 的地址，之后每次 `git push` 到该仓库都会自动重新部署。

---

## 可选：自定义域名

在 Vercel 项目里进入 **Settings → Domains**，添加你的域名并按提示解析即可。
