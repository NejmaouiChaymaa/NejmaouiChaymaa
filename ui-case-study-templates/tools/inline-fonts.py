#!/usr/bin/env python3
"""Embed the Google Fonts stylesheet (latin subsets only) as base64 @font-face
rules, so the poster renders with its real typeface offline and with no
external request.

    python3 tools/inline-fonts.py in.html out.html
"""
import base64
import re
import sys
import urllib.request

CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Poppins:wght@300;400;500;600;700;800&display=swap")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
KEEP = ("latin",)  # subsets the poster actually uses


def fetch(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA})).read()


def build_css():
    css = fetch(CSS_URL).decode("utf-8")
    blocks = re.findall(r"(/\* (\S+) \*/\s*)?(@font-face \{.*?\})", css, re.S)
    out = []
    for _, subset, block in blocks:
        if subset not in KEEP:
            continue
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        b64 = base64.b64encode(fetch(url)).decode("ascii")
        out.append(re.sub(r"url\(https://[^)]+\)",
                          "url(data:font/woff2;base64,%s)" % b64, block))
    return "\n".join(out)


def main(src, dst):
    html = open(src, encoding="utf-8").read()
    faces = build_css()
    # drop the preconnect/stylesheet links, inject the embedded faces instead
    html = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", html)
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis[^>]*>',
                  "<style>\n%s\n</style>" % faces, html)
    open(dst, "w", encoding="utf-8").write(html)
    print("%s -> %s (%.1f KB)" % (src, dst, len(html) / 1024))


if __name__ == "__main__":
    main(*(sys.argv[1:3] or ["infographic.standalone.html",
                             "export/eyeon-case-study-infographic.html"]))
