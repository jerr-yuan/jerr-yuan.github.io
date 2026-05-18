# -*- coding: utf-8 -*-
"""用 Playwright 将 resume-v4.16.html 转为 PDF。需先：pip install playwright && playwright install chromium"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "resume-v4.16.html")
OUT_PATH = os.path.join(SCRIPT_DIR, "resume-YuanPeng-one-page.pdf")

def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("请先安装: pip install playwright")
        print("然后执行: playwright install chromium")
        sys.exit(1)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(
            path=OUT_PATH,
            format="A4",
            print_background=True,
            margin={"top": "10mm", "right": "10mm", "bottom": "10mm", "left": "10mm"},
        )
        browser.close()

    print("已生成:", OUT_PATH)

if __name__ == "__main__":
    main()
