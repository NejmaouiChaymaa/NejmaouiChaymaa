#!/usr/bin/env python3
"""Build a self-contained copy of the case study template.

Replaces every src="assets/..." reference with a base64 data URI so the page
can be published or emailed as a single file.

    python3 tools/inline-assets.py eyeon-case-study.html eyeon-case-study.standalone.html
"""
import base64
import mimetypes
import pathlib
import re
import sys


def main(src, dst):
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    html = src.read_text(encoding="utf-8")
    root = src.parent

    def repl(m):
        rel = m.group(1)
        path = root / rel
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        b64 = base64.b64encode(path.read_bytes()).decode("ascii")
        return 'src="data:%s;base64,%s"' % (mime, b64)

    out = re.sub(r'src="(assets/[^"]+)"', repl, html)
    dst.write_text(out, encoding="utf-8")
    print("%s -> %s (%.1f KB)" % (src.name, dst.name, len(out) / 1024))


if __name__ == "__main__":
    main(*(sys.argv[1:3] or ["eyeon-case-study.html", "eyeon-case-study.standalone.html"]))
