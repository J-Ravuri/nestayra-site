import fitz
from pathlib import Path

PDF_PATH = Path("source/GL-Revision-Maths.pdf")
OUT_DIR = Path("education-game/gl-pages")

OUT_DIR.mkdir(parents=True, exist_ok=True)

if not PDF_PATH.exists():
    raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

doc = fitz.open(PDF_PATH)
matrix = fitz.Matrix(2.2, 2.2)

for page_index in range(len(doc)):
    out = OUT_DIR / f"page-{page_index + 1:03}.jpg"
    if out.exists():
        continue
    pix = doc[page_index].get_pixmap(matrix=matrix, alpha=False)
    pix.save(out)
    print(f"Saved {out}")

print("All pages rendered into education-game/gl-pages.")
