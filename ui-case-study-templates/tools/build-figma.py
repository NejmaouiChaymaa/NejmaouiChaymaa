#!/usr/bin/env python3
"""Build a Figma-import-friendly copy of the poster.

The html.to.design plugin renders the page and rebuilds it as Figma layers, so
anything Figma itself cannot express has to go before the import:

  * 3D transforms (perspective / rotateY / rotateX) -> Figma only rotates in 2D
  * .webp images                                    -> Figma imports PNG/JPG/SVG
  * aspect-ratio, filter: drop-shadow               -> fixed height, box-shadow
  * ::before / ::after decorations                  -> real elements, so they
                                                       arrive as their own layers

    python3 tools/build-figma.py infographic.html figma/eyeon-poster-figma.html
"""
import re
import sys


FIGMA_OVERRIDES = """
/* ---- Figma build only: flat 2D hero geometry ---- */
.stage{height:664px}
.pl-web{width:420px; top:48px; right:28px}
.laptop .screen{height:246px}
.pl-p1{width:176px; top:252px; right:292px}
.pl-p2{width:166px; top:298px; right:48px}
.chip-try{top:98px; right:388px}
.chip-rate{top:216px; right:148px}
.chip-time{top:452px; right:296px}
"""


def main(src, dst):
    s = open(src, encoding="utf-8").read()

    # images: point at the PNG pack, keep the Google Fonts link so the plugin
    # maps the family to Figma's own Poppins instead of an embedded blob
    s = s.replace('src="assets/', 'src="assets/').replace(".webp", ".png")

    # --- hero stage: flatten 3D to plain 2D rotation ---------------------
    s = s.replace("perspective:1500px; perspective-origin:60% 40%", "")
    s = re.sub(r"transform:rotateY\([^)]*\) rotateX\([^)]*\) rotateZ\((-?[\d.]+)deg\)",
               r"transform:rotate(\1deg)", s)
    s = s.replace("transform-style:preserve-3d", "")
    s = s.replace("filter:drop-shadow(-34px 40px 44px rgba(9,44,37,.42))",
                  "box-shadow:-34px 40px 44px -18px rgba(9,44,37,.42)")

    # --- fixed sizes instead of computed ones ----------------------------
    s = s.replace("aspect-ratio:16/10; position:relative", "height:271px; position:relative")

    # --- decorations become real layers ----------------------------------
    s = s.replace('<div class="lid">', '<div class="lid"><span class="cam"></span>')
    s = s.replace(".laptop .lid::before{content:\"\"; position:absolute;",
                  ".laptop .cam{position:absolute;")
    s = s.replace('<div class="base"></div>', '<div class="base"><span class="hinge"></span></div>')
    s = s.replace(".laptop .base::after{content:\"\"; position:absolute;",
                  ".laptop .hinge{position:absolute;")
    s = s.replace('<div class="plate phone pl-p1"><img', '<div class="plate phone pl-p1"><span class="notch"></span><img')
    s = s.replace('<div class="plate phone pl-p2"><img', '<div class="plate phone pl-p2"><span class="notch"></span><img')
    s = s.replace('.phone::before{content:""; position:absolute;', '.phone .notch{position:absolute;')
    s = s.replace('<div class="device"><img', '<div class="device"><span class="notch"></span><img')
    s = s.replace('.device::before{content:""; position:absolute;', '.device .notch{position:absolute;')
    s = s.replace('<div class="av"></div>', '<div class="av"><span class="pupil"></span></div>')
    s = s.replace('.persona .av::after{content:""; position:absolute;', '.persona .av .pupil{position:absolute;')
    s = s.replace('.zoomwin::after{content:"1,3×"; position:absolute;',
                  '.zoomwin .mag{position:absolute;')
    s = s.replace('alt="Détail : la ligne praticien avec temps de trajet" style=',
                  'alt="Détail : la ligne praticien avec temps de trajet" data-x style=')
    s = re.sub(r'(<div class="zoomwin"><img[^>]*>)', r'\1<span class="mag">1,3×</span>', s)

    # flattening the perspective removes the foreshortening, so the hero
    # devices need their own geometry in this build
    s = s.replace("</style>", FIGMA_OVERRIDES + "\n</style>", 1)

    # the page-fit scaler is meaningless in an import: keep the poster at 1200
    s = s.replace("<script>", "<script>/* scaler kept: harmless in Figma import */\n", 1)

    open(dst, "w", encoding="utf-8").write(s)
    print("%s -> %s (%.0f KB)" % (src, dst, len(s) / 1024))


if __name__ == "__main__":
    main(*(sys.argv[1:3] or ["infographic.html", "figma/eyeon-poster-figma.html"]))
