# -*- coding: utf-8 -*-
"""生成多字体版 PDF，便于对比。需：pip install playwright && playwright install chromium"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "resume-v4.16.html")

# 要生成的字体版：(输出文件名后缀, font-family 值)
FONT_VARIANTS = [
    ("SegoeUI", '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'),
    ("YaHei", '"Microsoft YaHei", "Microsoft YaHei UI", "PingFang SC", "Hiragino Sans GB", sans-serif'),
    ("Songti", '"SimSun", "NSimSun", "Songti SC", serif'),
]

FONT_FAMILY_PATTERN = re.compile(
    r'font-family:\s*[^;]+;',
    re.IGNORECASE
)

def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("请先安装: pip install playwright")
        print("然后执行: playwright install chromium")
        sys.exit(1)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_base = f.read()

    def set_font(html, font_css_value):
        return FONT_FAMILY_PATTERN.sub("font-family: " + font_css_value + ";", html, count=1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for suffix, font_value in FONT_VARIANTS:
            out_path = os.path.join(SCRIPT_DIR, "resume-YuanPeng-one-page-{}.pdf".format(suffix))
            html = set_font(html_base, font_value)
            page = browser.new_page()
            page.set_content(html, wait_until="networkidle")
            page.pdf(
                path=out_path,
                format="A4",
                print_background=True,
                margin={"top": "10mm", "right": "10mm", "bottom": "10mm", "left": "10mm"},
            )
            page.close()
            print("已生成:", out_path)
        browser.close()

if __name__ == "__main__":
    main()
