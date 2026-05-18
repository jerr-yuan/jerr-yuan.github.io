# 简历 PDF 生成（一页 A4）

用 [Puppeteer](https://github.com/puppeteer/puppeteer) 将 `resume-pdf.html` / `resume-pdf-tight.html` 转为单页 PDF。

## 方式一：浏览器直接导出（无需 Node）

1. 用浏览器打开上一级目录的 **`resume-pdf.html`**
2. `Ctrl+P`（或 Cmd+P）→ 目标选 **另存为 PDF**
3. 纸张选 **A4**，边距选 **默认** 或 **最小**，保存即可

若一页装不下，可改用 **`resume-pdf-tight.html`** 再打印一次。

## 方式二：用脚本生成（需 Node.js）

```bash
cd 1.resume/pdf-generate
npm install
npm run pdf          # 生成 resume-袁鹏-一页.pdf（标准一页版）
npm run pdf:tight    # 生成 resume-袁鹏-一页-紧凑.pdf（更紧凑备选）
```

生成的 PDF 在 `1.resume/` 目录下，可直接分发。
