# -*- coding: utf-8 -*-
"""用 WeasyPrint 将 resume-pdf.html 转为单页 PDF。需：pip install weasyprint"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "resume-pdf.html")
OUT_PATH = os.path.join(SCRIPT_DIR, "resume-袁鹏-一页.pdf")

def main():
    from weasyprint import HTML
    HTML(HTML_PATH).write_pdf(OUT_PATH)
    print("已生成:", OUT_PATH)

if __name__ == "__main__":
    main()
